import contextlib
import copy
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import report_lint as rl  # noqa: E402

DOI_A = "10.1234/abc.001"
DOI_B = "10.5678/def-002"


def page(body):
    return f"<!doctype html><html lang=\"ko\"><head><title>t</title></head><body>{body}</body></html>"


def pair(ko="한국어 문단입니다.", en="English paragraph."):
    return f'<p lang="ko">{ko}</p><p lang="en">{en}</p>'


def make_report(root, week, body, year=2026):
    d = Path(root) / "reports" / str(year) / f"w{week:02d}"
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(page(body), encoding="utf-8")


def claim(n=1, **kw):
    c = {
        "id": f"2026-w40-c{n:03d}", "week": "2026-W40",
        "source": {"doi": DOI_A, "location": {"kind": "abstract", "ref": "abstract"}},
        "conditions": {k: "UNKNOWN" for k in rl.CONDITION_KEYS},
        "quantity": None, "label": "SOURCE_REPORTED", "grade": "C", "access": "abstract_only",
        "status": "supported", "claim_type": "observation", "text": "a literal abstract sentence with 150 and 4.1",
        "mechanism_ids": [], "related_claim_ids": [],
    }
    c.update(kw)
    return c


def ledger(claims, access="abstract_only", week="2026-W40"):
    return {"schema_version": 1, "week": week, "year": 2026,
            "sources": [{"doi": DOI_A, "title": "A title", "access": access}], "claims": claims}


def write_claims(root, doc, name="2026-w40.json"):
    d = Path(root) / "claims"
    d.mkdir(exist_ok=True)
    (d / name).write_text(json.dumps(doc), encoding="utf-8")


def run(root, *args, fetch=None):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = rl.main([args[0], "--root", str(root), *args[1:]], fetch=fetch)
    return code, buf.getvalue()


def findings(root, check, week=None):
    ctx = rl.Context(root)
    return rl.CHECKS[check](ctx, ctx.select([week] if week else []))


def levels(fs, check=None):
    return {(f.check, f.week): f.level for f in fs if check is None or f.check == check}


class Tmp(unittest.TestCase):
    def setUp(self):
        self._t = tempfile.TemporaryDirectory()
        self.root = Path(self._t.name)
        self.addCleanup(self._t.cleanup)


class DoiTests(Tmp):
    def test_well_formed_passes(self):
        make_report(self.root, 38, f'<p>DOI {DOI_A}. and <a href="https://doi.org/{DOI_B}">x</a></p>')
        fs = findings(self.root, "doi-format")
        self.assertEqual(levels(fs)[("doi-format", "2026-W38")], "PASS")

    def test_malformed_fails(self):
        make_report(self.root, 38, "<p>DOI 10.12/short and doi: 10.1234 nope</p>")
        fs = findings(self.root, "doi-format")
        self.assertEqual(levels(fs)[("doi-format", "2026-W38")], "FAIL")

    def test_trailing_punctuation_is_not_part_of_doi(self):
        good, bad = rl.extract_dois("(see DOI 10.1109/TED.2026.3677021.) and 10.1063/5.0314307,")
        self.assertEqual(good, ["10.1109/TED.2026.3677021", "10.1063/5.0314307"])
        self.assertEqual(bad, [])

    def test_duplicate_across_weeks_fails_for_both(self):
        make_report(self.root, 38, f"<p>{DOI_A}</p>")
        make_report(self.root, 39, f"<p>{DOI_A.upper()} again</p><p>{DOI_B}</p>")
        lv = levels(findings(self.root, "doi-format"), "doi-duplicate")
        self.assertEqual(lv[("doi-duplicate", "2026-W38")], "FAIL")
        self.assertEqual(lv[("doi-duplicate", "2026-W39")], "FAIL")

    def test_same_doi_repeated_inside_one_week_is_fine(self):
        make_report(self.root, 38, f"<p>{DOI_A}</p><p>{DOI_A}</p>")
        self.assertEqual(levels(findings(self.root, "doi-format"), "doi-duplicate")[("doi-duplicate", "2026-W38")], "PASS")

    def test_ledger_and_report_of_same_week_do_not_collide(self):
        make_report(self.root, 40, f"<p>{DOI_A}</p>")
        write_claims(self.root, ledger([claim()]))
        lv = levels(findings(self.root, "doi-format"), "doi-duplicate")
        self.assertEqual(lv[("doi-duplicate", "2026-W40")], "PASS")

    def test_allow_list_in_index(self):
        make_report(self.root, 38, f"<p>{DOI_A}</p>")
        make_report(self.root, 39, f"<p>{DOI_A}</p>")
        (self.root / "claims").mkdir()
        (self.root / "claims" / "index.json").write_text(
            json.dumps({"allowed_duplicate_dois": [DOI_A]}), encoding="utf-8")
        fs = findings(self.root, "doi-format")
        self.assertNotIn("FAIL", levels(fs, "doi-duplicate").values())


class AdjacencyTests(Tmp):
    def test_pass(self):
        make_report(self.root, 40, pair() + pair())
        fs = findings(self.root, "kr-en-adjacency")
        self.assertEqual(fs[0].level, "PASS")
        self.assertIn("ko=2 en=2", fs[0].detail)

    def test_ko_without_following_en_fails_and_reports_count(self):
        make_report(self.root, 40, pair() + '<p lang="ko">고아 문단</p><p>untagged</p>')
        f = findings(self.root, "kr-en-adjacency")[0]
        self.assertEqual(f.level, "FAIL")
        self.assertIn("ko_without_following_en=1", f.detail)

    def test_ko_at_end_of_document_fails(self):
        make_report(self.root, 40, pair() + '<p lang="ko">끝</p>')
        self.assertEqual(findings(self.root, "kr-en-adjacency")[0].level, "FAIL")

    def test_two_ko_in_a_row_fails(self):
        make_report(self.root, 40, '<p lang="ko">a</p><p lang="ko">b</p><p lang="en">b</p>')
        self.assertEqual(findings(self.root, "kr-en-adjacency")[0].level, "FAIL")

    def test_report_without_lang_attributes_is_not_applicable(self):
        make_report(self.root, 37, "<p>한국어만 있는 문단 without lang attributes</p>")
        f = findings(self.root, "kr-en-adjacency")[0]
        self.assertEqual(f.level, "NA")
        self.assertIn("not applicable", f.detail)

    def test_orphan_en_is_warn_and_strict_fails(self):
        make_report(self.root, 40, '<p lang="en">only english</p>' + pair())
        self.assertEqual(findings(self.root, "kr-en-adjacency")[0].level, "WARN")
        self.assertEqual(run(self.root, "kr-en-adjacency")[0], 0)
        self.assertEqual(run(self.root, "kr-en-adjacency", "--strict")[0], 1)


class VocabularyTests(Tmp):
    def test_valid_grades_and_labels_pass(self):
        make_report(self.root, 40, pair("grade C 입니다. SOURCE_REPORTED, ENGINEERING_INFERENCE, 등급 A",
                                        "Grade B, UNKNOWN, EXTRAPOLATION_ONLY, AUTHOR_INTERPRETATION"))
        self.assertEqual(findings(self.root, "vocabulary")[0].level, "PASS")

    def test_b_minus_grade_in_html_fails(self):
        make_report(self.root, 40, "<p>This is grade B- evidence.</p>")
        f = findings(self.root, "vocabulary")[0]
        self.assertEqual(f.level, "FAIL")
        self.assertIn("B-", f.detail)

    def test_grade_e_and_korean_form_fail(self):
        make_report(self.root, 40, "<p>등급 E 이고 Grade X</p>")
        self.assertEqual(findings(self.root, "vocabulary")[0].level, "FAIL")

    def test_article_a_and_korean_particles_are_not_grades(self):
        make_report(self.root, 40, "<p>This is a grade a bit lower; 등급을 매기지 않습니다; the grade of rain.</p>")
        self.assertEqual(findings(self.root, "vocabulary")[0].level, "PASS")

    def test_near_miss_label_fails(self):
        make_report(self.root, 40, "<p>SOURCE_REPORT and AUTHOR_INTERPRETATIONS</p>")
        self.assertEqual(findings(self.root, "vocabulary")[0].level, "FAIL")

    def test_claim_with_b_minus_fails(self):
        write_claims(self.root, ledger([claim(grade="B-")]))
        f = findings(self.root, "vocabulary")[0]
        self.assertEqual(f.level, "FAIL")
        self.assertIn("B-", f.detail)

    def test_claim_with_invalid_label_fails(self):
        write_claims(self.root, ledger([claim(label="SOURCE_REPORTED_ISH")]))
        self.assertEqual(findings(self.root, "vocabulary")[0].level, "FAIL")


class LeakTests(Tmp):
    def test_clean_report_passes(self):
        make_report(self.root, 40, "<p>CS1 chip, S10 sample, Sonnets, contact the group.</p>")
        self.assertEqual(findings(self.root, "leak-check")[0].level, "PASS")

    def test_sources_yaml_leak_fails(self):
        make_report(self.root, 40, "<p>see audit/sources.yaml for details</p>")
        f = findings(self.root, "leak-check")[0]
        self.assertEqual(f.level, "FAIL")
        self.assertIn("internal-file-ref", f.detail)

    def test_each_pattern_detected(self):
        cases = {
            "source-id": "<p>as shown for S1 and S7</p>",
            "model-name": "<p>drafted with Opus then reviewed</p>",
            "local-path": r"<p>C:\Users\someone\work\x.py</p>",
            "email": "<p>write to someone@example.com</p>",
        }
        for name, body in cases.items():
            with self.subTest(name):
                make_report(self.root, 40, body)
                f = findings(self.root, "leak-check")[0]
                self.assertEqual(f.level, "FAIL")
                self.assertIn(name, f.detail)

    def test_script_and_style_are_ignored(self):
        make_report(self.root, 40, "<style>.S1{color:red}</style><script>var S2=1;</script><p>ok</p>")
        self.assertEqual(findings(self.root, "leak-check")[0].level, "PASS")


class AbstractGuardTests(Tmp):
    def test_unledgered_number_warns_not_fails(self):
        make_report(self.root, 40, "<p>Value 150 and 4.1 but also 777 and 3.14.</p>")
        write_claims(self.root, ledger([claim()]))
        f = findings(self.root, "abstract-only-guard")[0]
        self.assertEqual(f.level, "WARN")
        self.assertIn("777", f.detail)
        self.assertIn("3.14", f.detail)
        self.assertEqual(run(self.root, "abstract-only-guard")[0], 0)
        self.assertEqual(run(self.root, "abstract-only-guard", "--strict")[0], 1)

    def test_all_numbers_in_ledger_passes(self):
        make_report(self.root, 40, "<p>Value 150.0 and 4.10, 2026-10-21, W40, DOI 10.1234/abc.001, 3 items.</p>")
        write_claims(self.root, ledger([claim()]))
        self.assertEqual(findings(self.root, "abstract-only-guard")[0].level, "PASS")

    def test_quantity_values_count_as_ledger_numbers(self):
        make_report(self.root, 40, "<p>range 3e19 to 5e19</p>")
        write_claims(self.root, ledger([claim(quantity={"name": "n", "value_min": 3e19, "value_max": 5e19, "unit": "cm^-3"})]))
        self.assertEqual(findings(self.root, "abstract-only-guard")[0].level, "PASS")

    def test_report_without_numbers_is_not_a_vacuous_pass(self):
        make_report(self.root, 40, "<p>no digits here</p>")
        write_claims(self.root, ledger([claim()]))
        self.assertEqual(findings(self.root, "abstract-only-guard")[0].level, "NA")

    def test_not_applicable_without_ledger_or_for_full_text(self):
        make_report(self.root, 39, "<p>12345</p>")
        self.assertEqual(findings(self.root, "abstract-only-guard")[0].level, "NA")
        make_report(self.root, 40, "<p>777</p>")
        write_claims(self.root, ledger([claim(access="full_text", source={"doi": DOI_A, "location": {"kind": "figure"}})],
                                       access="full_text"))
        lv = levels(findings(self.root, "abstract-only-guard"))
        self.assertEqual(lv[("abstract-only-guard", "2026-W40")], "NA")


class ClaimsValidateTests(Tmp):
    def errs(self, doc):
        return rl.validate_claims_doc(doc, expect_week="2026-W40")

    def test_valid_ledger(self):
        self.assertEqual(self.errs(ledger([claim(1), claim(2, related_claim_ids=["2026-w40-c001"])])), [])

    def test_abstract_only_mechanism_grade_b_rejected(self):
        for g in ("A", "B"):
            e = self.errs(ledger([claim(claim_type="mechanism", grade=g, label="AUTHOR_INTERPRETATION")]))
            self.assertTrue(any("cannot be grade A or B" in x for x in e), e)

    def test_abstract_only_mechanism_grade_c_ok_and_full_text_b_ok(self):
        self.assertEqual(self.errs(ledger([claim(claim_type="mechanism", grade="C", label="AUTHOR_INTERPRETATION")])), [])
        doc = ledger([claim(claim_type="mechanism", grade="B", access="full_text",
                            source={"doi": DOI_A, "location": {"kind": "figure", "ref": "Fig. 3"}})], access="full_text")
        self.assertEqual(self.errs(doc), [])

    def test_source_reported_abstract_only_must_cite_abstract(self):
        e = self.errs(ledger([claim(source={"doi": DOI_A, "location": {"kind": "figure", "ref": "Fig. 2"}})]))
        self.assertTrue(any("location.kind == abstract" in x for x in e), e)

    def test_missing_condition_key_duplicate_id_dangling_relation(self):
        c = claim(1)
        del c["conditions"]["bias"]
        e = self.errs(ledger([c, claim(1, related_claim_ids=["2026-w40-c999"])]))
        joined = " | ".join(e)
        self.assertIn("conditions.bias missing", joined)
        self.assertIn("duplicate claim ids", joined)
        self.assertIn("not in this file", joined)

    def test_bad_enum_values(self):
        e = self.errs(ledger([claim(status="maybe", claim_type="vibes", access="partial", label="X", grade="B-")]))
        self.assertGreaterEqual(len(e), 5)

    def test_quantity_requires_unit_and_value(self):
        self.assertTrue(self.errs(ledger([claim(quantity={"name": "x", "value": 1})])))
        self.assertTrue(self.errs(ledger([claim(quantity={"name": "x", "unit": "nm"})])))

    def test_index_consistency(self):
        write_claims(self.root, ledger([claim(1)]))
        fs = findings(self.root, "claims-validate")
        self.assertEqual(levels(fs)[("claims-validate", "index")], "FAIL")      # no index.json
        (self.root / "claims" / "index.json").write_text(json.dumps(
            {"files": [{"week": "2026-W40", "claims_count": 1}]}), encoding="utf-8")
        fs = findings(self.root, "claims-validate")
        self.assertEqual(levels(fs)[("claims-validate", "index")], "PASS")
        (self.root / "claims" / "index.json").write_text(json.dumps(
            {"files": [{"week": "2026-W40", "claims_count": 2}]}), encoding="utf-8")
        self.assertEqual(levels(findings(self.root, "claims-validate"))[("claims-validate", "index")], "FAIL")

    def test_real_w40_ledger_is_valid(self):
        doc = json.loads((REPO / "claims" / "2026-w40.json").read_text(encoding="utf-8"))
        self.assertEqual(rl.validate_claims_doc(doc, expect_week="2026-W40"), [])
        self.assertEqual(len(doc["claims"]), 20)
        for c in doc["claims"]:
            self.assertEqual(c["label"], "SOURCE_REPORTED")
            self.assertEqual(c["access"], "abstract_only")
            self.assertEqual(c["source"]["location"]["kind"], "abstract")
            self.assertIn(c["grade"], rl.GRADES)
        idx = json.loads((REPO / "claims" / "index.json").read_text(encoding="utf-8"))
        self.assertEqual(idx["files"][0]["claims_count"], len(doc["claims"]))


class CrossrefTests(Tmp):
    def setUp(self):
        super().setUp()
        make_report(self.root, 40, f"<p>DOI {DOI_A}</p>")
        write_claims(self.root, ledger([claim()]))

    def run_with(self, fetch, *extra):
        return run(self.root, "crossref-resolve", *extra, fetch=fetch)

    def test_offline_skips_without_calling_fetch(self):
        def boom(d):
            raise AssertionError("network used in --offline")
        code, out = self.run_with(boom, "--offline")
        self.assertEqual(code, 0)
        self.assertIn("SKIP", out)

    def test_match_passes(self):
        code, out = self.run_with(lambda d: ("ok", "a TITLE"))
        self.assertEqual((code, "PASS" in out), (0, True))

    def test_title_mismatch_fails(self):
        code, out = self.run_with(lambda d: ("ok", "Completely different paper about something else"))
        self.assertEqual(code, 1)

    def test_network_error_is_unknown_and_never_fails_even_strict(self):
        code, out = self.run_with(lambda d: ("error", "URLError: offline"), "--strict")
        self.assertEqual(code, 0)
        self.assertIn("UNKNOWN", out)

    def test_not_found_is_warn(self):
        code, out = self.run_with(lambda d: ("notfound", None))
        self.assertEqual(code, 0)
        self.assertIn("WARN", out)

    def test_titles_match_helper(self):
        self.assertTrue(rl.titles_match("TCAD-based  Investigation", "tcad based investigation"))
        self.assertFalse(rl.titles_match("alpha beta gamma", "delta epsilon zeta"))


class DerivationTests(Tmp):
    def script(self, name, body, out=None):
        d = self.root / "audit" / "2026" / "w40" / "scripts"
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{name}.py").write_text(body, encoding="utf-8")
        if out is not None:
            (d / f"{name}_out.txt").write_text(out, encoding="utf-8")
        make_report(self.root, 40, "<p>x</p>")

    def detail(self):
        return [f for f in findings(self.root, "derivations") if f.week == "2026-W40"][0]

    def test_rerun_ok_matches(self):
        self.script("a", "# RERUN_OK\nprint('x = 3')\n", "x = 3\n")
        self.assertEqual(self.detail().level, "PASS")

    def test_rerun_ok_with_crlf_expected_output_matches(self):
        self.script("a", "# RERUN_OK\nprint('x = 3')\n", "x = 3\r\n")
        self.assertEqual(self.detail().level, "PASS")

    def test_output_mismatch_fails(self):
        self.script("a", "# RERUN_OK\nprint('x = 4')\n", "x = 3\n")
        f = self.detail()
        self.assertEqual(f.level, "FAIL")
        self.assertIn("differs", f.detail)

    def test_script_error_fails(self):
        self.script("a", "# RERUN_OK\nraise SystemExit(3)\n", "x\n")
        self.assertEqual(self.detail().level, "FAIL")

    def test_no_header_is_skipped_not_run(self):
        self.script("a", "raise SystemExit(9)\n", "x\n")
        f = self.detail()
        self.assertEqual(f.level, "SKIP")
        self.assertIn("no RERUN_OK", f.detail)

    def test_missing_out_file_is_skipped(self):
        self.script("a", "# RERUN_OK\nprint(1)\n")
        self.assertEqual(self.detail().level, "SKIP")

    def test_sympy_script_skipped_when_unavailable(self):
        self.script("a", "# RERUN_OK\nimport sympy\nprint(sympy.__version__)\n", "1\n")
        with mock.patch.object(rl.importlib.util, "find_spec", return_value=None):
            f = self.detail()
        self.assertEqual(f.level, "SKIP")
        self.assertIn("SKIPPED (sympy not available)", f.detail)

    def test_no_audit_folder_is_na(self):
        make_report(self.root, 40, "<p>x</p>")
        self.assertEqual(self.detail().level, "NA")


class StrictAndExitTests(Tmp):
    def test_fail_gives_exit_1_and_report_only_gives_0(self):
        make_report(self.root, 40, "<p>sources.yaml</p>")
        self.assertEqual(run(self.root, "leak-check")[0], 1)
        self.assertEqual(run(self.root, "leak-check", "--report-only")[0], 0)

    def test_all_runs_without_crossref(self):
        make_report(self.root, 40, pair())
        code, out = run(self.root, "all")
        self.assertEqual(code, 0)
        self.assertNotIn("crossref-resolve", out)
        self.assertIn("SUMMARY", out)

    def test_week_filter_and_bad_label(self):
        make_report(self.root, 38, "<p>sources.yaml</p>")
        make_report(self.root, 39, "<p>fine</p>")
        self.assertEqual(run(self.root, "leak-check", "--week", "2026-W39")[0], 0)
        self.assertEqual(run(self.root, "leak-check", "--week", "garbage")[0], 2)


class PolicyTests(Tmp):
    def test_baseline_weeks_never_block(self):
        for w in (37, 38, 39, 40, 41, 42):
            make_report(self.root, w, "<p lang=\"ko\">x sources.yaml S1 Opus grade B-</p>")
        code, out = run(self.root, "policy")
        self.assertEqual(code, 0)
        self.assertIn("BASELINE", out)
        self.assertNotIn(" FAIL ", out)

    def test_new_week_with_leak_blocks(self):
        make_report(self.root, 43, "<p>see sources.yaml</p>")
        self.assertEqual(run(self.root, "policy")[0], 1)

    def test_new_week_with_ko_without_en_blocks(self):
        make_report(self.root, 43, pair() + '<p lang="ko">alone</p>')
        self.assertEqual(run(self.root, "policy")[0], 1)

    def test_new_week_with_bad_grade_or_label_blocks(self):
        make_report(self.root, 43, "<p>grade B-</p>")
        self.assertEqual(run(self.root, "policy")[0], 1)
        make_report(self.root, 44, "<p>SOURCE_REPORT</p>")
        self.assertEqual(run(self.root, "policy", "--week", "2026-W44")[0], 1)

    def test_new_week_without_lang_attributes_is_not_blocked_by_adjacency(self):
        make_report(self.root, 43, "<p>한국어 only paragraph, no lang attribute.</p>")
        self.assertEqual(run(self.root, "policy")[0], 0)

    def test_clean_new_week_passes(self):
        make_report(self.root, 43, pair("그림 1 설명", "Figure 1 caption") + pair())
        self.assertEqual(run(self.root, "policy")[0], 0)

    def test_non_policy_failures_do_not_block_new_week(self):
        make_report(self.root, 43, pair() + "<p>DOI 10.12/bad</p>")
        code, out = run(self.root, "policy")
        self.assertEqual(code, 0)
        self.assertIn("BASELINE", out)

    def test_marker_in_index_moves_the_boundary(self):
        make_report(self.root, 41, "<p>sources.yaml</p>")
        (self.root / "claims").mkdir()
        (self.root / "claims" / "index.json").write_text(json.dumps(
            {"files": [], "new_week_policy": {"first_blocking_week": "2026-W41",
                                              "blocking_checks": ["leak-check"]}}), encoding="utf-8")
        self.assertEqual(run(self.root, "policy")[0], 1)

    def test_default_boundary_is_w43_and_excludes_w37_to_w40(self):
        ctx = rl.Context(self.root)
        self.assertEqual(ctx.first_blocking(), (2026, 43))
        for w in (37, 38, 39, 40, 41, 42):
            self.assertFalse(ctx.is_new_week(rl.Week(2026, w)))
        self.assertTrue(ctx.is_new_week(rl.Week(2026, 43)))
        self.assertTrue(ctx.is_new_week(rl.Week(2027, 1)))

    def test_repo_marker_matches_code_default(self):
        idx = json.loads((REPO / "claims" / "index.json").read_text(encoding="utf-8"))
        self.assertEqual(idx["new_week_policy"], rl.DEFAULT_POLICY)

    def test_real_repo_policy_and_ledger_checks_pass(self):
        self.assertEqual(run(REPO, "policy")[0], 0)
        self.assertEqual(run(REPO, "claims-validate")[0], 0)


if __name__ == "__main__":
    unittest.main()
