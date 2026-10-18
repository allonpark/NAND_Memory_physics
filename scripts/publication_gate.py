#!/usr/bin/env python3
"""Fail-closed publication gate for weekly reports.

Subcommands
  check            validate every non-draft report (exit 1 on any failure)
  weeks            print publishable weeks as "YYYY WW" lines
  stage DIR        copy the publishable site into DIR (draft weeks excluded)
  pdf-check        validate built PDFs (fonts, Hangul text layer)

A week directory containing a file named DRAFT is excluded from validation,
PDF build and the Pages artifact. A week WITHOUT that marker must pass the gate.
"""
import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path

SENTINELS = ("Build staging file", "staging placeholder")
MIN_BYTES = 8000
MIN_HANGUL = 300
HANGUL = re.compile(r"[가-힣]")
REPORT_GLOB = "reports/*/w*/index.html"
SITE_EXCLUDE = {".git", ".github", "scripts", "tests", "__pycache__", ".pytest_cache"}


def discover(root: Path):
    """Return [(year, week, path, is_draft)] sorted by (year, week)."""
    found = []
    for p in sorted(root.glob(REPORT_GLOB)):
        m = re.fullmatch(r"w(\d{2})", p.parent.name)
        if not m or not re.fullmatch(r"\d{4}", p.parent.parent.name):
            continue
        found.append((p.parent.parent.name, m.group(1), p, (p.parent / "DRAFT").exists()))
    return found


def validate_report(path: Path):
    errors = []
    raw = path.read_bytes()
    text = raw.decode("utf-8", errors="replace")
    if len(raw) < MIN_BYTES:
        errors.append(f"too small: {len(raw)} B < {MIN_BYTES} B")
    for s in SENTINELS:
        if s.lower() in text.lower():
            errors.append(f"placeholder sentinel found: {s!r}")
    if len(HANGUL.findall(text)) < MIN_HANGUL:
        errors.append(f"Hangul characters < {MIN_HANGUL}")
    if not re.search(r"[A-Za-z]{3,}", text):
        errors.append("no Latin text")
    if not re.search(r"<title>[^<]{3,}</title>", text):
        errors.append("missing <title>")
    return errors


def cmd_check(root: Path):
    failed = False
    reports = discover(root)
    if not reports:
        print("FAIL: no reports discovered")
        return 1
    for year, week, path, draft in reports:
        if draft:
            print(f"SKIP  {year}-W{week}  (DRAFT marker)")
            continue
        errs = validate_report(path)
        if errs:
            failed = True
            print(f"FAIL  {year}-W{week}")
            for e in errs:
                print(f"      - {e}")
        else:
            print(f"PASS  {year}-W{week}")
    return 1 if failed else 0


def publishable(root: Path):
    return [(y, w) for y, w, _, d in discover(root) if not d]


def cmd_stage(root: Path, dest: Path):
    drafts = {p.parent.resolve() for _, _, p, d in discover(root) if d}
    if dest.exists():
        shutil.rmtree(dest)

    def ignore(directory, names):
        skip = set()
        for n in names:
            full = (Path(directory) / n).resolve()
            if n in SITE_EXCLUDE and Path(directory).resolve() == root:
                skip.add(n)
            elif full in drafts or full == dest:
                skip.add(n)
        return skip

    shutil.copytree(root, dest, ignore=ignore)
    print(f"staged site at {dest}")
    return 0


def cmd_pdf_check(root: Path):
    failed = False
    for year, week in publishable(root):
        pdf = root / "downloads" / year / f"VNAND_HV_Reliability_{year}-W{week}.pdf"
        label = f"{year}-W{week}"
        if not pdf.is_file() or pdf.stat().st_size == 0:
            print(f"FAIL  {label}: PDF missing or empty")
            failed = True
            continue
        fonts = subprocess.run(["pdffonts", str(pdf)], capture_output=True, text=True).stdout
        text = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True, text=True).stdout
        errs = []
        if not re.search(r"NotoSansCJK\S*\s.*\byes\b", fonts):
            errs.append("Noto CJK font not embedded")
        if len(HANGUL.findall(text)) < MIN_HANGUL:
            errs.append(f"Hangul in text layer < {MIN_HANGUL}")
        if errs:
            failed = True
            print(f"FAIL  {label}")
            print(fonts)
            for e in errs:
                print(f"      - {e}")
        else:
            print(f"PASS  {label}")
    return 1 if failed else 0


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check")
    sub.add_parser("weeks")
    st = sub.add_parser("stage")
    st.add_argument("dest")
    sub.add_parser("pdf-check")
    a = ap.parse_args(argv)
    root = Path(a.root).resolve()
    if a.cmd == "check":
        return cmd_check(root)
    if a.cmd == "weeks":
        for y, w in publishable(root):
            print(y, w)
        return 0
    if a.cmd == "stage":
        return cmd_stage(root, Path(a.dest).resolve())
    if a.cmd == "pdf-check":
        return cmd_pdf_check(root)


if __name__ == "__main__":
    sys.exit(main())
