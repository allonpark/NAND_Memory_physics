#!/usr/bin/env python3
"""Deterministic report linters for the weekly NAND Memory Physics reports.

Standard library only. Every check is a pure function of the files under --root
(except crossref-resolve, which is optional and network-based).

Subcommands (each returns exit code 0 = no FAIL, 1 = at least one FAIL)
  doi-format            DOI syntax + the same DOI appearing in more than one week
  kr-en-adjacency       every <p lang="ko"> is immediately followed by <p lang="en">
  vocabulary            label / grade vocabulary (reports and claims files)
  leak-check            internal references in public report HTML
  abstract-only-guard   numeric tokens in the report that are in no ledger claim (WARN)
  claims-validate       claims/*.json schema + abstract_only rules + index consistency
  crossref-resolve      optional network check against api.crossref.org (--offline skips)
  derivations           re-run audit scripts that declare RERUN_OK, diff against *_out.txt
  all                   every check above except crossref-resolve (use --online to add it)
  policy                new-week blocking policy (see docs/quality/README.md)

Result levels: PASS, FAIL, WARN, UNKNOWN, NA (not applicable), SKIP, BASELINE.
WARN, UNKNOWN, NA, SKIP and BASELINE never fail. --strict promotes WARN to FAIL.
--report-only prints everything but always exits 0.
"""
import argparse
import difflib
import html
import importlib.util
import json
import re
import subprocess
import sys
import urllib.error
import urllib.parse
import urllib.request
from collections import OrderedDict
from html.parser import HTMLParser
from pathlib import Path

LABELS = ("SOURCE_REPORTED", "AUTHOR_INTERPRETATION", "ENGINEERING_INFERENCE",
          "UNKNOWN", "EXTRAPOLATION_ONLY")
GRADES = ("A", "B", "C", "D")
ACCESS = ("full_text", "abstract_only")
STATUSES = ("supported", "contested", "superseded")
CLAIM_TYPES = ("observation", "quantity", "method", "mechanism", "scope")
LOCATION_KINDS = ("abstract", "figure", "table", "equation", "text")
CONDITION_KEYS = ("material", "geometry", "temperature", "bias", "time", "sample_count")

REPORT_GLOB = "reports/*/w*/index.html"
DEFAULT_POLICY = {
    "first_blocking_week": "2026-W43",
    "blocking_checks": ["leak-check", "kr-en-adjacency", "vocabulary"],
}

LEVEL_ORDER = ["FAIL", "WARN", "UNKNOWN", "BASELINE", "PASS", "SKIP", "NA"]


class Finding:
    __slots__ = ("check", "week", "level", "detail")

    def __init__(self, check, week, level, detail=""):
        self.check, self.week, self.level, self.detail = check, week, level, detail

    def __repr__(self):
        return f"Finding({self.check!r},{self.week!r},{self.level!r},{self.detail!r})"


def week_label(year, week):
    return f"{int(year):04d}-W{int(week):02d}"


def parse_week_label(s):
    m = re.fullmatch(r"(\d{4})-[Ww](\d{1,2})", s.strip())
    if not m:
        raise ValueError(f"bad week label: {s!r}")
    return int(m.group(1)), int(m.group(2))


# --------------------------------------------------------------------------- loading

class _TextParser(HTMLParser):
    """Collects visible text, <p> elements (in document order) and skips script/style."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.text = []
        self.ps = []  # list of (lang or None, line)
        self._skip = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("script", "style"):
            self._skip += 1
        if tag == "p":
            self.ps.append((dict(attrs).get("lang"), self.getpos()[0]))

    def handle_endtag(self, tag):
        if tag in ("script", "style") and self._skip:
            self._skip -= 1

    def handle_data(self, data):
        if not self._skip:
            self.text.append(data)


class Week:
    def __init__(self, year, week):
        self.year, self.week = int(year), int(week)
        self.report_path = None
        self.html = None
        self.claims_path = None
        self.claims = None
        self.claims_error = None
        self._parsed = None

    @property
    def key(self):
        return (self.year, self.week)

    @property
    def label(self):
        return week_label(self.year, self.week)

    def parsed(self):
        if self._parsed is None:
            p = _TextParser()
            p.feed(self.html or "")
            self._parsed = (" ".join(p.text), p.ps)
        return self._parsed

    def visible_text(self):
        return self.parsed()[0]

    def paragraphs(self):
        return self.parsed()[1]


class Context:
    def __init__(self, root):
        self.root = Path(root).resolve()
        self.weeks = OrderedDict()
        self.index = None
        self.index_error = None
        self.policy = dict(DEFAULT_POLICY)
        self.allowed_dup = set()
        self._load()

    def _week(self, y, w):
        k = (int(y), int(w))
        if k not in self.weeks:
            self.weeks[k] = Week(*k)
        return self.weeks[k]

    def _load(self):
        for p in sorted(self.root.glob(REPORT_GLOB)):
            m = re.fullmatch(r"w(\d{2})", p.parent.name)
            if not m or not re.fullmatch(r"\d{4}", p.parent.parent.name):
                continue
            wk = self._week(p.parent.parent.name, m.group(1))
            wk.report_path = p
            wk.html = p.read_bytes().decode("utf-8", errors="replace")
        for p in sorted((self.root / "claims").glob("*-w*.json")):
            m = re.fullmatch(r"(\d{4})-w(\d{1,2})\.json", p.name)
            if not m:
                continue
            wk = self._week(m.group(1), m.group(2))
            wk.claims_path = p
            try:
                wk.claims = json.loads(p.read_text(encoding="utf-8"))
            except (OSError, ValueError) as e:
                wk.claims_error = f"{type(e).__name__}: {e}"
        ip = self.root / "claims" / "index.json"
        if ip.is_file():
            try:
                self.index = json.loads(ip.read_text(encoding="utf-8"))
                pol = self.index.get("new_week_policy")
                if isinstance(pol, dict):
                    self.policy.update(pol)
                self.allowed_dup = {d.lower() for d in self.index.get("allowed_duplicate_dois", [])}
            except (OSError, ValueError, AttributeError) as e:
                self.index_error = f"{type(e).__name__}: {e}"
        self.weeks = OrderedDict(sorted(self.weeks.items()))

    def select(self, labels):
        if not labels:
            return list(self.weeks.values())
        want = {parse_week_label(x) for x in labels}
        return [w for k, w in self.weeks.items() if k in want]

    def first_blocking(self):
        return parse_week_label(self.policy["first_blocking_week"])

    def is_new_week(self, wk):
        return wk.key >= self.first_blocking()


# --------------------------------------------------------------------------- (a) DOI

DOI_CAND = re.compile(r"10\.\d{4,9}/[^\s<>\"']+")
DOI_KEYWORD = re.compile(r"(?i)\bdoi\b[\s:=]{0,3}(10\.[^\s<>\"']*)")
DOI_VALID = re.compile(r"^10\.\d{4,9}/[A-Za-z0-9._;()/:\-]+$")
TRAIL = ".,;:)]}"


def normalize_doi(raw):
    d = html.unescape(raw)
    while d and d[-1] in TRAIL:
        # keep a closing parenthesis only when balanced inside the DOI
        if d[-1] == ")" and d.count("(") >= d.count(")"):
            break
        d = d[:-1]
    return d


def extract_dois(text):
    """Return (list of normalized DOIs, list of malformed fragments)."""
    good, bad = [], []
    for m in DOI_CAND.finditer(text):
        d = normalize_doi(m.group(0))
        (good if DOI_VALID.match(d) else bad).append(d)
    for m in DOI_KEYWORD.finditer(text):
        d = normalize_doi(m.group(1))
        if not DOI_VALID.match(d):
            bad.append(d)
    return good, bad


def ledger_dois(wk):
    out = []
    if isinstance(wk.claims, dict):
        for s in wk.claims.get("sources", []) or []:
            if isinstance(s, dict) and isinstance(s.get("doi"), str):
                out.append(s["doi"])
        for c in wk.claims.get("claims", []) or []:
            try:
                out.append(c["source"]["doi"])
            except (KeyError, TypeError):
                pass
    return out


def check_doi_format(ctx, weeks):
    res = []
    seen = {}  # doi(lower) -> {week label}
    for wk in weeks:
        per_week = set()
        good, bad = ([], [])
        if wk.html is not None:
            good, bad = extract_dois(wk.html)
        led = ledger_dois(wk)
        for d in led:
            if not DOI_VALID.match(d):
                bad.append(d)
            else:
                good.append(d)
        if wk.html is None and not led:
            res.append(Finding("doi-format", wk.label, "NA", "no report HTML and no ledger DOIs"))
            continue
        if bad:
            res.append(Finding("doi-format", wk.label, "FAIL",
                               f"{len(bad)} malformed DOI(s): " + ", ".join(sorted(set(bad))[:8])))
        else:
            res.append(Finding("doi-format", wk.label, "PASS",
                               f"{len(set(x.lower() for x in good))} distinct DOI(s) well-formed"))
        for d in good:
            per_week.add(d.lower())
        for d in per_week:
            seen.setdefault(d, set()).add(wk.label)
    for d, labels in sorted(seen.items()):
        if len(labels) > 1 and d not in ctx.allowed_dup:
            for lab in sorted(labels):
                res.append(Finding("doi-duplicate", lab, "FAIL",
                                   f"{d} also appears in {', '.join(sorted(labels - {lab}))}"))
    flagged = {f.week for f in res if f.check == "doi-duplicate"}
    for wk in weeks:
        if wk.label not in flagged and any(f.check == "doi-format" and f.week == wk.label
                                           and f.level != "NA" for f in res):
            res.append(Finding("doi-duplicate", wk.label, "PASS", "no DOI shared with another week"))
    return res


# --------------------------------------------------------------------------- (b) ko/en

def check_kr_en(ctx, weeks):
    res = []
    for wk in weeks:
        if wk.html is None:
            continue
        ps = wk.paragraphs()
        n_ko = sum(1 for lang, _ in ps if (lang or "").lower().startswith("ko"))
        n_en = sum(1 for lang, _ in ps if (lang or "").lower().startswith("en"))
        if n_ko + n_en == 0:
            res.append(Finding("kr-en-adjacency", wk.label, "NA",
                               "not applicable: no <p lang> attributes in this report"))
            continue
        offenders = []
        for i, (lang, line) in enumerate(ps):
            if (lang or "").lower().startswith("ko"):
                nxt = ps[i + 1][0] if i + 1 < len(ps) else None
                if not (nxt or "").lower().startswith("en"):
                    offenders.append(line)
        orphan_en = 0
        for i, (lang, _) in enumerate(ps):
            if (lang or "").lower().startswith("en"):
                prev = ps[i - 1][0] if i > 0 else None
                if not (prev or "").lower().startswith("ko"):
                    orphan_en += 1
        detail = f"ko={n_ko} en={n_en} ko_without_following_en={len(offenders)} en_without_preceding_ko={orphan_en}"
        if offenders:
            res.append(Finding("kr-en-adjacency", wk.label, "FAIL",
                               detail + "; offender line(s): " + ", ".join(map(str, offenders[:10]))))
        elif orphan_en:
            res.append(Finding("kr-en-adjacency", wk.label, "WARN", detail))
        else:
            res.append(Finding("kr-en-adjacency", wk.label, "PASS", detail))
    return res


# --------------------------------------------------------------------------- (c) vocabulary

GRADE_RE = re.compile(r"(?:[Gg]rade|등급)[ \t:=]{0,3}([A-Z][-+−]?)(?![A-Za-z가-힣])")
LABEL_WORD_RE = re.compile(r"\b(?:" + "|".join(LABELS) + r")\b")
LABEL_LIKE_RE = re.compile(r"\b(?:SOURCE|AUTHOR|ENGINEERING|EXTRAPOLATION|UNKNOWN)[_-][A-Z][A-Z_-]*\b")


def vocab_problems_in_text(text):
    probs = []
    for m in GRADE_RE.finditer(text):
        g = m.group(1)
        if g not in GRADES:
            probs.append(f"invalid grade {g!r}")
    for m in LABEL_LIKE_RE.finditer(text):
        if m.group(0) not in LABELS:
            probs.append(f"invalid label {m.group(0)!r}")
    return probs


def check_vocabulary(ctx, weeks):
    res = []
    for wk in weeks:
        probs = []
        used = 0
        if wk.html is not None:
            txt = wk.visible_text()
            probs += vocab_problems_in_text(txt)
            used = len(GRADE_RE.findall(txt)) + len(LABEL_WORD_RE.findall(txt))
        if isinstance(wk.claims, dict):
            for c in wk.claims.get("claims", []) or []:
                if not isinstance(c, dict):
                    continue
                cid = c.get("id", "?")
                if c.get("label") not in LABELS:
                    probs.append(f"claim {cid}: invalid label {c.get('label')!r}")
                if c.get("grade") not in GRADES:
                    probs.append(f"claim {cid}: invalid grade {c.get('grade')!r}")
        if wk.html is None and not isinstance(wk.claims, dict):
            continue
        if probs:
            uniq = list(OrderedDict.fromkeys(probs))
            res.append(Finding("vocabulary", wk.label, "FAIL",
                               f"{len(probs)} problem(s): " + "; ".join(uniq[:8])))
        else:
            note = "" if used else " (vacuous: report uses no label or grade tokens)"
            res.append(Finding("vocabulary", wk.label, "PASS",
                               f"{used} label/grade token(s), all within vocabulary{note}"))
    return res


# --------------------------------------------------------------------------- (d) leak

LEAK_PATTERNS = [
    ("internal-file-ref", re.compile(r"\bsources?\.ya?ml\b", re.I)),
    ("source-id", re.compile(r"(?<![A-Za-z0-9_-])S[1-9](?![A-Za-z0-9_-])")),
    ("model-name", re.compile(r"\b(?:Opus|Sonnet|Haiku|Fable)\b", re.I)),
    ("local-path", re.compile(r"(?:\b[A-Za-z]:\\[^\s<>\"']+|/Users/[A-Za-z0-9_.-]+|<local-path>|&lt;local-path&gt;)")),
    ("email", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)+")),
]


def strip_script_style(raw):
    return re.sub(r"(?is)<(script|style)\b.*?</\1\s*>", " ", raw)


def leak_hits(raw):
    body = strip_script_style(raw)
    hits = []
    for name, rx in LEAK_PATTERNS:
        for m in rx.finditer(body):
            line = body.count("\n", 0, m.start()) + 1
            hits.append((name, m.group(0), line))
    return hits


def check_leak(ctx, weeks):
    res = []
    for wk in weeks:
        if wk.html is None:
            continue
        hits = leak_hits(wk.html)
        if hits:
            by = OrderedDict()
            for name, tok, line in hits:
                by.setdefault(name, []).append((tok, line))
            parts = [f"{n} x{len(v)} (e.g. {v[0][0]!r} line {v[0][1]})" for n, v in by.items()]
            res.append(Finding("leak-check", wk.label, "FAIL", f"{len(hits)} hit(s): " + "; ".join(parts)))
        else:
            res.append(Finding("leak-check", wk.label, "PASS", "no internal references found"))
    return res


# --------------------------------------------------------------------------- (e) abstract-only guard

NUM_RE = re.compile(r"(?<![\w.])\d+(?:\.\d+)?(?:[eE][+-]?\d+)?(?![\w])")
DATE_RE = re.compile(r"\b\d{4}-\d{2}(?:-\d{2})?\b")


def norm_num(tok):
    try:
        f = float(tok)
    except (TypeError, ValueError):
        return str(tok)
    return str(int(f)) if f.is_integer() else repr(f)


def numeric_tokens(text, drop_noise=True):
    t = DOI_CAND.sub(" ", text)
    t = re.sub(r"https?://\S+", " ", t)
    t = DATE_RE.sub(" ", t)
    t = re.sub(r"\b[Ww]\d{1,2}\b", " ", t)
    out = set()
    for m in NUM_RE.finditer(t):
        tok = m.group(0)
        if drop_noise:
            if re.fullmatch(r"\d", tok):          # bare single digit: list numbers, counts
                continue
            if re.fullmatch(r"20[0-3]\d", tok):    # year
                continue
        out.add(norm_num(tok))
    return out


def claim_numbers(claims):
    nums = set()
    for c in claims.get("claims", []) or []:
        if not isinstance(c, dict):
            continue
        parts = [str(c.get("text", ""))]
        q = c.get("quantity")
        cond = c.get("conditions")
        if isinstance(cond, dict):
            parts += [str(v) for v in cond.values()]
        nums |= numeric_tokens(" ".join(parts), drop_noise=False)
        if isinstance(q, dict):
            for k in ("value", "value_min", "value_max"):
                v = q.get(k)
                if isinstance(v, (int, float)) and not isinstance(v, bool):
                    nums.add(norm_num(v))
    return nums


def week_is_abstract_only(claims):
    if not isinstance(claims, dict):
        return False
    for s in claims.get("sources", []) or []:
        if isinstance(s, dict) and s.get("access") == "abstract_only":
            return True
    for c in claims.get("claims", []) or []:
        if isinstance(c, dict) and c.get("access") == "abstract_only":
            return True
    return False


def check_abstract_guard(ctx, weeks):
    res = []
    for wk in weeks:
        if wk.html is None:
            continue
        if not isinstance(wk.claims, dict):
            res.append(Finding("abstract-only-guard", wk.label, "NA", "no claims ledger for this week"))
            continue
        if not week_is_abstract_only(wk.claims):
            res.append(Finding("abstract-only-guard", wk.label, "NA", "ledger has no abstract_only sources"))
            continue
        known = claim_numbers(wk.claims)
        rep = numeric_tokens(wk.visible_text())
        if not rep:
            res.append(Finding("abstract-only-guard", wk.label, "NA",
                               "report contains no numeric tokens (placeholder or empty report?)"))
            continue
        unknown = sorted(rep - known, key=lambda s: (len(s), s))
        if unknown:
            res.append(Finding("abstract-only-guard", wk.label, "WARN",
                               f"{len(unknown)} numeric token(s) in report not in any claim "
                               f"(of {len(rep)} distinct): " + ", ".join(unknown[:15])
                               + (" ..." if len(unknown) > 15 else "")))
        else:
            res.append(Finding("abstract-only-guard", wk.label, "PASS",
                               f"all {len(rep)} numeric token(s) appear in the ledger"))
    return res


# --------------------------------------------------------------------------- claims validate

CLAIM_ID_RE = re.compile(r"^\d{4}-w\d{2}-c\d{3,}$")
MECH_ID_RE = re.compile(r"^[a-z0-9][a-z0-9_.-]*$")
REQUIRED_CLAIM = ("id", "week", "source", "conditions", "label", "grade", "access", "status",
                  "claim_type", "text")


def validate_claims_doc(doc, expect_week=None):
    errs = []
    if not isinstance(doc, dict):
        return ["top level is not an object"]
    if doc.get("schema_version") != 1:
        errs.append("schema_version must be 1")
    if expect_week and doc.get("week") != expect_week:
        errs.append(f"file week {doc.get('week')!r} != expected {expect_week!r}")
    srcs = doc.get("sources")
    src_access = {}
    if not isinstance(srcs, list):
        errs.append("sources must be a list")
    else:
        for s in srcs:
            if not isinstance(s, dict) or not isinstance(s.get("doi"), str):
                errs.append("source entry without doi")
                continue
            if s.get("access") not in ACCESS:
                errs.append(f"source {s.get('doi')}: invalid access {s.get('access')!r}")
            src_access[s["doi"].lower()] = s.get("access")
    claims = doc.get("claims")
    if not isinstance(claims, list):
        return errs + ["claims must be a list"]
    ids = [c.get("id") for c in claims if isinstance(c, dict)]
    dup = {i for i in ids if ids.count(i) > 1}
    if dup:
        errs.append(f"duplicate claim ids: {sorted(dup)}")
    idset = set(ids)
    for c in claims:
        if not isinstance(c, dict):
            errs.append("claim is not an object")
            continue
        cid = c.get("id", "?")
        for k in REQUIRED_CLAIM:
            if k not in c:
                errs.append(f"{cid}: missing field {k}")
        if "id" in c and not CLAIM_ID_RE.match(str(c["id"])):
            errs.append(f"{cid}: id does not match YYYY-wWW-cNNN")
        if "label" in c and c["label"] not in LABELS:
            errs.append(f"{cid}: invalid label {c['label']!r}")
        if "grade" in c and c["grade"] not in GRADES:
            errs.append(f"{cid}: invalid grade {c['grade']!r}")
        if "access" in c and c["access"] not in ACCESS:
            errs.append(f"{cid}: invalid access {c['access']!r}")
        if "status" in c and c["status"] not in STATUSES:
            errs.append(f"{cid}: invalid status {c['status']!r}")
        if "claim_type" in c and c["claim_type"] not in CLAIM_TYPES:
            errs.append(f"{cid}: invalid claim_type {c['claim_type']!r}")
        src = c.get("source")
        loc = None
        if isinstance(src, dict):
            if not isinstance(src.get("doi"), str) or not DOI_VALID.match(src.get("doi", "")):
                errs.append(f"{cid}: source.doi missing or malformed")
            elif src["doi"].lower() not in src_access:
                errs.append(f"{cid}: source.doi not listed in sources[]")
            elif c.get("access") and src_access[src["doi"].lower()] != c.get("access"):
                errs.append(f"{cid}: access differs from the source's access")
            loc = src.get("location")
            if not isinstance(loc, dict) or loc.get("kind") not in LOCATION_KINDS:
                errs.append(f"{cid}: source.location.kind must be one of {LOCATION_KINDS}")
                loc = None
        elif "source" in c:
            errs.append(f"{cid}: source must be an object")
        cond = c.get("conditions")
        if isinstance(cond, dict):
            for k in CONDITION_KEYS:
                if k not in cond:
                    errs.append(f"{cid}: conditions.{k} missing (use \"UNKNOWN\" if not stated)")
        elif "conditions" in c:
            errs.append(f"{cid}: conditions must be an object")
        q = c.get("quantity")
        if q is not None:
            if not isinstance(q, dict) or not isinstance(q.get("unit"), str):
                errs.append(f"{cid}: quantity must be null or an object with a unit")
            else:
                has = any(isinstance(q.get(k), (int, float)) and not isinstance(q.get(k), bool)
                          for k in ("value", "value_min", "value_max"))
                if not has:
                    errs.append(f"{cid}: quantity needs value or value_min/value_max")
        for k in ("mechanism_ids", "related_claim_ids"):
            v = c.get(k, [])
            if not isinstance(v, list):
                errs.append(f"{cid}: {k} must be a list")
        for m in c.get("mechanism_ids", []) or []:
            if not isinstance(m, str) or not MECH_ID_RE.match(m):
                errs.append(f"{cid}: bad mechanism id {m!r}")
        for r in c.get("related_claim_ids", []) or []:
            if r not in idset:
                errs.append(f"{cid}: related claim {r!r} not in this file")
            if r == cid:
                errs.append(f"{cid}: related to itself")
        # --- evidence rules
        if c.get("access") == "abstract_only":
            if c.get("label") == "SOURCE_REPORTED" and loc is not None and loc.get("kind") != "abstract":
                errs.append(f"{cid}: SOURCE_REPORTED + abstract_only must have location.kind == abstract")
            if c.get("grade") in ("A", "B") and c.get("claim_type") == "mechanism":
                errs.append(f"{cid}: abstract_only mechanism claim cannot be grade A or B")
        if c.get("label") == "SOURCE_REPORTED" and not str(c.get("text", "")).strip():
            errs.append(f"{cid}: SOURCE_REPORTED claim has empty text")
    return errs


def check_claims_validate(ctx, weeks):
    res = []
    for wk in weeks:
        if wk.claims_path is None:
            continue
        if wk.claims_error:
            res.append(Finding("claims-validate", wk.label, "FAIL", f"unreadable: {wk.claims_error}"))
            continue
        errs = validate_claims_doc(wk.claims, expect_week=wk.label)
        if errs:
            res.append(Finding("claims-validate", wk.label, "FAIL",
                               f"{len(errs)} error(s): " + "; ".join(errs[:6])))
        else:
            n = len(wk.claims.get("claims", []))
            res.append(Finding("claims-validate", wk.label, "PASS", f"{n} claim(s) valid"))
    # index consistency (global, attributed to the pseudo-week 'index')
    ip = ctx.root / "claims" / "index.json"
    has_files = any(w.claims_path for w in ctx.weeks.values())
    if ctx.index_error:
        res.append(Finding("claims-validate", "index", "FAIL", f"claims/index.json unreadable: {ctx.index_error}"))
    elif ip.is_file():
        listed = {}
        for e in ctx.index.get("files", []) if isinstance(ctx.index, dict) else []:
            if isinstance(e, dict):
                listed[e.get("week")] = e
        actual = {w.label: w for w in ctx.weeks.values() if w.claims_path}
        errs = []
        for lab, w in actual.items():
            e = listed.get(lab)
            if e is None:
                errs.append(f"{lab} not listed in index")
            elif isinstance(w.claims, dict) and e.get("claims_count") != len(w.claims.get("claims", [])):
                errs.append(f"{lab} claims_count {e.get('claims_count')} != {len(w.claims.get('claims', []))}")
        for lab in listed:
            if lab not in actual:
                errs.append(f"{lab} listed but file missing")
        try:
            ctx.first_blocking()
        except (ValueError, KeyError) as e:
            errs.append(f"new_week_policy.first_blocking_week invalid: {e}")
        res.append(Finding("claims-validate", "index",
                           "FAIL" if errs else "PASS",
                           "; ".join(errs) if errs else "index.json consistent with claims files"))
    elif has_files:
        res.append(Finding("claims-validate", "index", "FAIL", "claims files exist but claims/index.json is missing"))
    return res


# --------------------------------------------------------------------------- (f) crossref

def norm_title(t):
    return re.sub(r"[^a-z0-9]+", "", html.unescape(t).lower())


def titles_match(a, b):
    na, nb = norm_title(a), norm_title(b)
    if na == nb:
        return True
    return difflib.SequenceMatcher(None, na, nb).ratio() >= 0.92


def crossref_fetch(doi, timeout=15):
    """Return ('ok', title) | ('notfound', None) | ('error', message)."""
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/")
    req = urllib.request.Request(url, headers={
        "User-Agent": "NAND-Memory-physics-report-lint/1.0 (+https://github.com/allonpark/NAND_Memory_physics)"})
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            data = json.loads(r.read().decode("utf-8"))
        titles = data.get("message", {}).get("title") or []
        return "ok", (titles[0] if titles else "")
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return "notfound", None
        return "error", f"HTTP {e.code}"
    except Exception as e:  # network down, DNS, timeout, bad JSON
        return "error", f"{type(e).__name__}: {e}"


def check_crossref(ctx, weeks, offline=False, fetch=None):
    res = []
    fetch = fetch or crossref_fetch
    for wk in weeks:
        dois = OrderedDict()
        if wk.html is not None:
            for d in extract_dois(wk.html)[0]:
                dois.setdefault(d.lower(), (d, None))
        if isinstance(wk.claims, dict):
            for s in wk.claims.get("sources", []) or []:
                if isinstance(s, dict) and isinstance(s.get("doi"), str):
                    dois[s["doi"].lower()] = (s["doi"], s.get("title"))
        if not dois:
            continue
        if offline:
            res.append(Finding("crossref-resolve", wk.label, "SKIP", f"--offline ({len(dois)} DOI(s) not queried)"))
            continue
        ok = nf = err = 0
        bad = []
        for _, (doi, title) in dois.items():
            st, val = fetch(doi)
            if st == "ok":
                if title and not titles_match(title, val or ""):
                    bad.append(f"{doi}: ledger title differs from Crossref title")
                else:
                    ok += 1
            elif st == "notfound":
                nf += 1
            else:
                err += 1
        if bad:
            res.append(Finding("crossref-resolve", wk.label, "FAIL", "; ".join(bad[:5])))
        elif err:
            res.append(Finding("crossref-resolve", wk.label, "UNKNOWN",
                               f"network/API error for {err} of {len(dois)} DOI(s); resolved {ok}, not found {nf}"))
        elif nf:
            res.append(Finding("crossref-resolve", wk.label, "WARN",
                               f"{nf} DOI(s) not registered at Crossref (could be another registrar); resolved {ok}"))
        else:
            res.append(Finding("crossref-resolve", wk.label, "PASS", f"{ok} DOI(s) resolved"))
    return res


# --------------------------------------------------------------------------- (g) derivations

def _norm_out(s):
    return [ln.rstrip() for ln in s.replace("\r\n", "\n").replace("\r", "\n").rstrip("\n").split("\n")]


def check_derivations(ctx, weeks, timeout=120):
    res = []
    for wk in weeks:
        d = ctx.root / "audit" / f"{wk.year:04d}" / f"w{wk.week:02d}" / "scripts"
        if not d.is_dir():
            if wk.html is not None:
                res.append(Finding("derivations", wk.label, "NA", "no audit scripts folder"))
            continue
        scripts = sorted(d.glob("*.py"))
        if not scripts:
            res.append(Finding("derivations", wk.label, "NA", "audit scripts folder has no .py"))
            continue
        outcomes = []
        for sp in scripts:
            out = sp.with_name(sp.stem + "_out.txt")
            src = sp.read_text(encoding="utf-8", errors="replace")
            head = "\n".join(src.splitlines()[:20])
            if not out.is_file():
                outcomes.append((sp.name, "SKIP", "no accompanying _out.txt"))
                continue
            if "RERUN_OK" not in head:
                outcomes.append((sp.name, "SKIP", "no RERUN_OK header"))
                continue
            if re.search(r"(?m)^\s*(?:import|from)\s+sympy\b", src) and importlib.util.find_spec("sympy") is None:
                outcomes.append((sp.name, "SKIP", "SKIPPED (sympy not available)"))
                continue
            try:
                p = subprocess.run([sys.executable, "-I", "-X", "utf8", str(sp)], cwd=str(d),
                                   capture_output=True, timeout=timeout)
            except subprocess.TimeoutExpired:
                outcomes.append((sp.name, "FAIL", f"timeout after {timeout}s"))
                continue
            if p.returncode != 0:
                tail = p.stderr.decode("utf-8", "replace").strip().splitlines()[-1:] or [""]
                outcomes.append((sp.name, "FAIL", f"exit {p.returncode}: {tail[0][:120]}"))
                continue
            got = _norm_out(p.stdout.decode("utf-8", "replace"))
            want = _norm_out(out.read_text(encoding="utf-8", errors="replace"))
            if got == want:
                outcomes.append((sp.name, "PASS", "output identical"))
            else:
                diff = list(difflib.unified_diff(want, got, "expected", "actual", lineterm="", n=0))
                outcomes.append((sp.name, "FAIL", "output differs: " + " | ".join(diff[2:5])[:200]))
        levels = [o[1] for o in outcomes]
        detail = "; ".join(f"{n}: {x}" for n, _, x in outcomes)
        if "FAIL" in levels:
            lvl = "FAIL"
        elif "PASS" in levels:
            lvl = "PASS"
        else:
            lvl = "SKIP"
        res.append(Finding("derivations", wk.label, lvl, detail))
    return res


# --------------------------------------------------------------------------- orchestration

CHECKS = OrderedDict([
    ("doi-format", check_doi_format),
    ("kr-en-adjacency", check_kr_en),
    ("vocabulary", check_vocabulary),
    ("leak-check", check_leak),
    ("abstract-only-guard", check_abstract_guard),
    ("claims-validate", check_claims_validate),
    ("derivations", check_derivations),
])


def run_checks(ctx, names, weeks, offline=True, fetch=None):
    res = []
    for n in names:
        if n == "crossref-resolve":
            res += check_crossref(ctx, weeks, offline=offline, fetch=fetch)
        else:
            res += CHECKS[n](ctx, weeks)
    return res


def apply_policy(ctx, findings):
    """Apply the new-week blocking policy.

    A FAIL stays FAIL only when its check is in new_week_policy.blocking_checks AND the
    week is >= new_week_policy.first_blocking_week. Every other FAIL (baseline weeks, or
    checks outside the policy) becomes BASELINE: still printed, never blocking.
    """
    blocking = set(ctx.policy.get("blocking_checks", []))
    out = []
    for f in findings:
        by_week = {w.label: w for w in ctx.weeks.values()}
        wk = by_week.get(f.week)
        is_new = wk is not None and ctx.is_new_week(wk)
        base = {"doi-duplicate": "doi-format"}.get(f.check, f.check)
        if f.level == "FAIL" and not (base in blocking and is_new):
            out.append(Finding(f.check, f.week, "BASELINE", f.detail))
        else:
            out.append(f)
    return out


def finalize(findings, strict=False):
    if strict:
        return [Finding(f.check, f.week, "FAIL", f.detail + " [strict]") if f.level == "WARN" else f
                for f in findings]
    return findings


def exit_code(findings, report_only=False):
    if report_only:
        return 0
    return 1 if any(f.level == "FAIL" for f in findings) else 0


def render(findings, markdown=False):
    cells = OrderedDict()
    for f in findings:
        k = (f.check, f.week)
        cur = cells.get(k)
        if cur is None or LEVEL_ORDER.index(f.level) < LEVEL_ORDER.index(cur[0]):
            cells[k] = [f.level, [f]]
        else:
            if f.level == cur[0]:
                cur[1].append(f)
    lines = []
    if markdown:
        lines.append("| check | week | result | detail |")
        lines.append("|---|---|---|---|")
        for (chk, wk), (lvl, fs) in cells.items():
            d = " / ".join(x.detail for x in fs)[:300].replace("|", "\\|")
            lines.append(f"| {chk} | {wk} | {lvl} | {d} |")
    else:
        wid = max([len(k[0]) for k in cells] + [5])
        lines.append(f"{'CHECK':<{wid}}  {'WEEK':<8}  {'RESULT':<8}  DETAIL")
        for (chk, wk), (lvl, fs) in cells.items():
            d = " / ".join(x.detail for x in fs)
            lines.append(f"{chk:<{wid}}  {wk:<8}  {lvl:<8}  {d}")
    counts = OrderedDict((l, 0) for l in LEVEL_ORDER)
    for lvl, _ in cells.values():
        counts[lvl] += 1
    summary = "SUMMARY: " + ", ".join(f"{k}={v}" for k, v in counts.items() if v)
    lines.append("")
    lines.append(summary)
    return "\n".join(lines)


def build_parser():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    common = argparse.ArgumentParser(add_help=False)
    common.add_argument("--root", default=".")
    common.add_argument("--week", action="append", default=[], help="restrict to YYYY-Www (repeatable)")
    common.add_argument("--strict", action="store_true", help="WARN counts as FAIL")
    common.add_argument("--report-only", action="store_true", help="always exit 0")
    common.add_argument("--markdown", action="store_true", help="markdown table output")
    sub = ap.add_subparsers(dest="cmd", required=True)
    for name in list(CHECKS) + ["crossref-resolve", "all", "policy"]:
        p = sub.add_parser(name, parents=[common])
        if name in ("crossref-resolve", "all", "policy"):
            p.add_argument("--offline", action="store_true", help="skip network checks")
        if name in ("all", "policy"):
            p.add_argument("--online", action="store_true", help="also run crossref-resolve")
    return ap


def main(argv=None, fetch=None):
    for s in (sys.stdout, sys.stderr):
        try:
            s.reconfigure(encoding="utf-8")
        except (AttributeError, ValueError):
            pass
    a = build_parser().parse_args(argv)
    ctx = Context(a.root)
    try:
        weeks = ctx.select(a.week)
    except ValueError as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    if a.cmd == "all":
        names = list(CHECKS) + (["crossref-resolve"] if getattr(a, "online", False) else [])
        findings = run_checks(ctx, names, weeks, offline=not getattr(a, "online", False), fetch=fetch)
    elif a.cmd == "policy":
        names = list(CHECKS) + (["crossref-resolve"] if getattr(a, "online", False) else [])
        findings = run_checks(ctx, names, weeks, offline=not getattr(a, "online", False), fetch=fetch)
        findings = apply_policy(ctx, findings)
    elif a.cmd == "crossref-resolve":
        findings = check_crossref(ctx, weeks, offline=a.offline, fetch=fetch)
    else:
        findings = CHECKS[a.cmd](ctx, weeks)
    findings = finalize(findings, a.strict)
    if not findings:
        findings = [Finding(a.cmd, "-", "NA", "nothing to check under --root")]
    print(render(findings, a.markdown))
    return exit_code(findings, a.report_only)


if __name__ == "__main__":
    sys.exit(main())
