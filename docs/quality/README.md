# Report quality checks

`scripts/report_lint.py` (standard library only) runs deterministic checks on the weekly reports and on the evidence ledger in
`claims/`. It complements, and does not replace, `scripts/publication_gate.py` (placeholder, size, Hangul, PDF fonts).

```
python3 -I scripts/report_lint.py <check> [--root DIR] [--week 2026-W40 ...] [--strict] [--report-only] [--markdown]
```

| check | what it does | levels |
|---|---|---|
| `doi-format` | DOI syntax in report HTML and ledger; the same DOI in more than one week (`doi-duplicate`) | PASS / FAIL |
| `kr-en-adjacency` | every `<p lang="ko">` is directly followed by `<p lang="en">`; reports without `lang` paragraphs are `NA` | PASS / FAIL / WARN (English paragraph without a preceding Korean one) / NA |
| `vocabulary` | only the five labels and grades A to D (rejects `B-`, `grade E`, `SOURCE_REPORT`); also applied to ledger claims | PASS / FAIL |
| `leak-check` | internal references in public HTML: the internal source-registry file name, `S1` to `S9` used as source ids, model-family names, local Windows paths, e-mail addresses | PASS / FAIL |
| `abstract-only-guard` | in weeks whose ledger has abstract_only sources, numeric tokens in the report that no ledger claim contains | PASS / WARN / NA |
| `claims-validate` | ledger schema, abstract_only rules, `claims/index.json` consistency | PASS / FAIL |
| `crossref-resolve` | optional network check against `api.crossref.org`; compares the ledger title; `--offline` skips; network errors give `UNKNOWN` | PASS / FAIL (title mismatch) / WARN (not registered at Crossref) / UNKNOWN / SKIP |
| `derivations` | re-runs `audit/<year>/<week>/scripts/*.py` that declare `RERUN_OK` in their first 20 lines and compares with `*_out.txt`; scripts importing sympy are `SKIPPED (sympy not available)` when it is missing | PASS / FAIL / SKIP / NA |
| `all` | all of the above except `crossref-resolve` (add `--online`) | |
| `policy` | `all`, then the new-week blocking policy below | |

Exit code is 0 unless some result is FAIL. WARN, UNKNOWN, NA, SKIP and BASELINE never fail. `--strict` turns WARN into FAIL
(UNKNOWN stays non-failing, because a network error says nothing about the report). `--report-only` always exits 0.

Known limits of the heuristics (they are deterministic, not intelligent):

- A PASS on `vocabulary` for a report that uses no labels or grades is vacuous; the detail text says so.
- `leak-check` looks for a fixed list of patterns. A leak in another form is not detected. `S1` to `S9` also match a genuine symbol such as a stage name.
- `abstract-only-guard` compares number strings. A WARN means "not in the ledger", not "wrong". Citation metadata (volume, page, article numbers) and numbers derived inside the report are reported too.
- `kr-en-adjacency` compares paragraph order only; it does not judge whether the English text is a faithful translation.
- `crossref-resolve` shows that a DOI exists and the title matches; it does not show that the paper supports the sentence citing it.

## CI (`.github/workflows/pages.yml`)

| step | mode |
|---|---|
| `python3 -m unittest discover -s tests -v` (includes `tests/test_report_lint.py`) | blocking (unchanged step) |
| `publication_gate.py check` and the PDF steps | blocking (unchanged) |
| Report linters, all weeks, `--report-only`, plus `crossref-resolve` | non-blocking (`continue-on-error`), output in the step summary and the `report-lint-output` artifact |
| `report_lint.py policy --offline` | blocking, but only for weeks from the marker onward, only for the three policy checks |

### New-week policy

The marker is `new_week_policy` in `claims/index.json`:

```json
"new_week_policy": { "first_blocking_week": "2026-W43",
                     "blocking_checks": ["leak-check", "kr-en-adjacency", "vocabulary"] }
```

- Weeks from `first_blocking_week` on (`reports/2026/w43` and later, also later years): a FAIL of a policy check blocks the build.
- W37 to W42 are baseline: their FAILs are printed as `BASELINE` and never block.
- `kr-en-adjacency` blocks only for reports that use `lang` attributes; a report without them is `NA`.
- FAILs of checks that are not in the policy (for example `doi-format`) are printed as `BASELINE` in the `policy` step and are visible in the report-only step instead.
- The code default equals the file marker; a unit test keeps them equal.

### Moving one check to blocking

1. Make the check pass on the weeks you care about, or accept the FAILs as baseline.
2. For all weeks: add a step `python3 -I scripts/report_lint.py <check>` without `--report-only` and without `continue-on-error`.
3. For new weeks only: add the check name to `blocking_checks` in `claims/index.json` and to `DEFAULT_POLICY` in the script (the test fails if they differ).
4. To tighten warnings, add `--strict` to the step.
5. To move the baseline boundary, change `first_blocking_week` in both places.

## Baseline

See `docs/quality/baseline_2026-10-22.md` for the measured state of W37 to W40 (and the W41 to W43 drafts).
