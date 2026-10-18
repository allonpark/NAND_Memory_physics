import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import publication_gate as g  # noqa: E402

GOOD = ("<!doctype html><html><head><title>Weekly report</title></head><body>"
        + "<p>이번 주 핵심 메커니즘 설명입니다. 전하 포획과 전계 재분포를 다룹니다. Charge trapping field redistribution.</p>" * 120
        + "</body></html>")
PLACEHOLDER = ('<!doctype html><html><head><meta charset="utf-8"><title>2026 W40</title></head>'
               '<body><h1>W40 Reliability Co-Scientist</h1><p>Build staging file.</p></body></html>')


def make(root, year, week, html, draft=False):
    d = Path(root) / "reports" / year / f"w{week}"
    d.mkdir(parents=True)
    (d / "index.html").write_text(html, encoding="utf-8")
    if draft:
        (d / "DRAFT").write_text("")


class GateTests(unittest.TestCase):
    def test_good_report_passes(self):
        with tempfile.TemporaryDirectory() as t:
            make(t, "2026", "39", GOOD)
            self.assertEqual(g.main(["--root", t, "check"]), 0)

    def test_placeholder_fails(self):
        with tempfile.TemporaryDirectory() as t:
            make(t, "2026", "39", GOOD)
            make(t, "2026", "40", PLACEHOLDER)
            self.assertEqual(g.main(["--root", t, "check"]), 1)

    def test_english_only_long_report_fails(self):
        with tempfile.TemporaryDirectory() as t:
            make(t, "2026", "40", "<html><head><title>x report</title></head><body>" + "english text " * 2000 + "</body></html>")
            self.assertEqual(g.main(["--root", t, "check"]), 1)

    def test_draft_is_skipped_and_not_staged(self):
        with tempfile.TemporaryDirectory() as t, tempfile.TemporaryDirectory() as out:
            make(t, "2026", "39", GOOD)
            make(t, "2026", "40", PLACEHOLDER, draft=True)
            (Path(t) / "index.html").write_text("home", encoding="utf-8")
            (Path(t) / "scripts").mkdir()
            self.assertEqual(g.main(["--root", t, "check"]), 0)
            dest = Path(out) / "site"
            self.assertEqual(g.main(["--root", t, "stage", str(dest)]), 0)
            self.assertTrue((dest / "reports/2026/w39/index.html").exists())
            self.assertFalse((dest / "reports/2026/w40").exists())
            self.assertFalse((dest / "scripts").exists())
            self.assertTrue((dest / "index.html").exists())

    def test_weeks_excludes_drafts(self):
        with tempfile.TemporaryDirectory() as t:
            make(t, "2026", "39", GOOD)
            make(t, "2026", "40", PLACEHOLDER, draft=True)
            self.assertEqual(g.publishable(Path(t).resolve()), [("2026", "39")])

    def test_no_reports_fails_closed(self):
        with tempfile.TemporaryDirectory() as t:
            self.assertEqual(g.main(["--root", t, "check"]), 1)


if __name__ == "__main__":
    unittest.main()
