# W41 fix pass — fixlog (2026-11-10)

Scope: edits only inside `work/w41/sections/` (i1..i5.html, report_head.html, report_tail.html). No push, no PR, no change to `sources.yaml` or the repo clone.

## 0. Backup and helper files
- Backup of all 7 html files before any edit: `sections/_orig/*.html` (byte-identical copies).
- Helper scripts (new, not public): `sections/_tools/` — `noun_endings.py`, `assemble.py`, `i2_enrichment_check.py`, `supp_refs.py`, `selfcheck.py`; outputs `*_out.txt`.
- Download for source re-read (item 3 only): `sections/_dl/i3/` — `2610.11643v1.pdf` (arXiv, 3,615,842 B), `abs.html`, `html.html` (arXiv HTML v1), `i3.txt` (pdftotext -layout), `i3_utf8.txt` (pdftotext -enc UTF-8).
- Per-file changed-line counts vs `_orig` (git diff --no-index --numstat): head 5, i1 14, i2 11, i3 20, i4 23, i5 7, tail 21 added / 19 removed.

## 1. Blockers
### M-1 (report_tail, synthesis geometry heading)
- Replaced the heading "형상: 동축 시뮬레이션, bulk, 평판, 미상 / Geometry: coaxial simulation, bulk, planar, unknown" with "형상은 항목마다 따로 적습니다 / Geometry is stated item by item" and rewrote the paragraph item by item: item 1 = UNKNOWN in the source (no coordinate system, the word "cylindrical" not used; our coaxial analysis is a framework under an assumed cylindrical shape); items 2–3 = bulk amorphous Si3N4 material calculation, no cell geometry (computational cell ~14–15 Å, no field); item 4 = planar MFM capacitor; item 5 = planar or UNKNOWN (planar MOS framework, trench UNKNOWN).
- Closing sentence (ko/en) now says no source states a cylindrical geometry or measured a coaxial device.
- i5 "Governing relations" lead sentence reworded so item 5 geometry is stated as UNKNOWN (planar framework) in verb form.

### M-3 (report_tail, hypotheses)
- Lead-in rewritten: H1, H2, H3, H4, H6, H7 come from item DOEs (H2 = item-1 DOE layer-position factor + item-1 coaxial framework; H3 = item-3 DOE expected signature placed in item-2 DOE arm M planar-capacitor setting); H5 and H8 are explicitly this report's cross-constructions that appear in no item DOE; all hypotheses grade D. Verified against current item text: i1 DOE (cell-position factor, falsification 1–5), i2 DOE arm M/C′ and H2, i3 DOE expected signature/falsification, i4 DOE falsification (1)(2), i5 DOE expected signature b ≈ −1 / falsification (a).
- Added a "Grade" column with "D" in every row; basis cells now say "item N DOE" or "cross-construction … in no item DOE".
- H5: removed the rate premise ("CTL film conditions mainly change capture/emission time distributions", which items 2–3 do not compute) and the τc/τe signature; hypothesis now: amplitude distribution changes with channel-process (grain) split and not with a CTL density split at fixed composition/H. Criterion rewritten per part with a pre-set margin; the leap "rejection would mean a direct link through trap type" replaced by "rejection does not by itself imply trap type sets the amplitude; CTL splits can also change trap location/density, a separate test is needed".
- H8: removed the ranking "reflects heterogeneity more than defect arrangement"; replaced by a neutral conditional (if differences come from heterogeneity, they shrink when heterogeneity is reduced; no ranking assumed). Criterion: reject heterogeneity-only explanation if α difference stays outside CI after paired refit; failure-site clustering adds support for the defect reading but does not exclude heterogeneity.

### 1-A (i1, New vs known)
- Deleted the "Known" statements inferred from reference titles (decananometer-flash exponential-tail framework, 3D percolation view, pass-voltage measurements in vertical NAND). Replaced with: primary literature not read this week, so no background is inferred from titles; kept only the Fig. 12 2D square-root statement and that agreement with the references was not checked.

## 2. Other review findings
### 3-A (i3 one-research-line box; also i2 box for symmetry)
- i3: "shared setup (…, the mobility-edge definition, …)" corrected: mobility-edge definition is NOT shared — item 3 uses N/4 (η = 1/4, N = 280), item 2 uses N_eff ≥ 56 (N/5); item 3 states N/5↔N/4 shifts the mean gap by ~0.35 eV; absolute depths not compared across items.
- i2 box: added the same statement (ko/en).
- i2 critical boundary (3) and valid-range card: added N_eff ≥ 56 next to "one fifth of the cell".

### M-2 / H-1 (QC wording)
- QC grid "Independent physics review": now exactly "independent physics review PERFORMED with verdicts PASS-WITH-FIXES; fixes applied; re-check PENDING".
- Added ko/en paragraph above the grid with the same status.
- "writer self-check only" (2 cells) replaced by "internal self-check … plus the independent physics review (PASS-WITH-FIXES); fixes applied …; re-check PENDING".
- Duplicate check now reads "checked against the published reports (W37-W40 and W43) and the used-source ledger; no overlap was found." (mention of unpublished candidate lists removed).
- report_head evidence box: "독립 물리 검수는 아직 수행하지 않았습니다(PENDING)" → performed, PASS-WITH-FIXES, fixes applied, re-check PENDING (ko/en).

### (6) Numbers and sentence endings
- i2 derivation B: native-K depth-decile enrichment 0.906 → 0.905 (ko/en). SymPy 1.14.0 exact rationals (`_tools/i2_enrichment_check.py`, output `_tools/i2_enrichment_check_out.txt`): (6/42)/(65/412) = 412/455 = 0.905494. All other derivation-B values reconfirmed: 1.61695, 1.56306, 0.178355, 1.35824, E = 18.5534, P(iK≥30) = 1.601e-4, P(iK≥29) = 5.506e-4, P(pol≤3) = 6.300e-7, 29/41 = 0.70732.
- Noun-form endings converted to 합니다체 where a sentence was intended: head label/grade definitions; i1 card EVIDENCE/MODEL/ASSUMPTION/SOURCE TRACE, i1 trap-statistics assumption sentence; i2 critical boundary (1)(2)(4)(5), card VALID RANGE/ASSUMPTION/CONFIDENCE/SOURCE TRACE; i3 card EVIDENCE/ASSUMPTION/CONFIDENCE/SOURCE TRACE; i4 card EVIDENCE/MODEL/VALID RANGE/SOURCE TRACE/Failure modes; i5 governing-relations lead, DOE controls, card VALID RANGE and CONFIDENCE. Residual flags from `noun_endings.py` (128 P-lines) are bold headings ("<b>…</b>"), "접근 수준: …"/"선정 분류: …" metadata, and colon-introduced variable/condition lists; kept intentionally.
- i4 typo: "반결정성(semi-quantitative)" → "반정량적(semi-quantitative)" (Korean term was wrong).

### (7) Cross-item consistency
- One common title for observed-on-reading boxes: tail box label changed to the item label "Observed on reading, not confirmed by the authors (not a source claim)", class boundary → inference (same as items); tail h3 → "Observed on reading: summary of items 1–4".
- Inference box labels unified to "ENGINEERING_INFERENCE · SymPy-checked …" (i1 dash → ·; i3, i4, i5 "Engineering inference · sympy-checked …"). DOE labels in i3/i4 → "Falsifiable DOE (symbolic levels)" (i1 keeps its longer DOE label).
- archive_gap spelling: i1 "archive gap"/"archive-gap" and i5 "archive gap" → "archive_gap".
- Symbols at each use: item 1 sheet-amplitude ratio now uses u = t₁/r₀ with t₁ = single-layer thickness, distinguished from radius ratio t = T_poly/r_f (i1 eq + variable list, head symbol paragraph); i1 Gaussian-tail slope now defines z.
- Items 2–3 one research line: tail "415 … from the same group's cell population" → "from a separate Vitriflow cell population of the same group"; i3 box same wording; tail matrix "largely the same cells" → "probably largely the same cells (inference; not cross-checked cell by cell)".
- Unpublished paper 10.1088/1361-6641/aeb1e8: 0 occurrences (checked).
- i4 derivation numbering: "(ix)" → "(vi)" everywhere in i4 (10 occurrences). Basis: `i4_notes.md` maps "(9) -> (vi) gamma-mixture identity"; (vi) directly follows (v); the "(ix)" label was a reconstruction artefact.

### Leak-check fix (found by repo linter, not in the review list)
- Baseline linter FAIL: leak-check source-id ×68 — bare supplementary references "Table S2", "Fig. S1", "S1.1–S1.5" match the internal-id pattern S[1-9]. Applied via script `_tools/supp_refs.py` (PowerShell-invoked Python; every replacement printed in `_tools/supp_refs_out.txt`): i3 and i4 now write "Supplementary Table 2", "Supplementary Fig. 1", "Supplementary Sections 1.1–1.5, 3.1–3.3, 4.3–4.5, 5.1", "Supplementary Figs. 1–9" etc. This matches i3's own stated convention ("Supplementary Table 2"). Remaining bare S<digit>: 0.
- i2 "the SI Table 1 note" → "the SI Table 1 footnote" (forbidden word 'note(s)'); tail "notes that" → "states that".

## 3. Manifest-error check against the current text (no html change needed)
- '7 days' (item 1): current text says 6 days / 6일 everywhere; 0 hits for "7 days"/"7일".
- N_eff <= 56: current text says ≥ 56; 0 hits for ≤ 56.
- beta-Si3N4: re-read item 3 source twice independently — (a) arXiv PDF v1 via `pdftotext -enc UTF-8`, (b) arXiv HTML v1. Both read: crystalline reference for void fraction = **α-Si3N4** (7.8%), and the Hückmann et al. 84-cell population = **β-Si3N4-derived** cells. Current i3 text already has α for the crystalline reference and β for the 84-cell starting structure, so both stay; only the manifest is wrong. Same reads confirm 415 of Ref. [2] (Vitriflow) + 84 of Ref. [1], mobility edge N/4, N/5↔N/4 mean-gap shift ≈ 0.35 eV.
- '415 cells from the companion study': html did not say this; it now says "separate Vitriflow population of the same group" in tail and i3.

## 4. Self-checks (outputs saved)
- `_tools/selfcheck_out.txt` (head + i1..i5 + tail concatenated): tag balance 0 errors, 0 unclosed; classes used all present in repo `assets/style.css` (26 classes, 0 missing); ko→en adjacency ko=298 en=298, 0 violations (parser and raw-text checks); card cells 172 with paragraphs, 0 unpaired; internal anchors 12, 0 unresolved; forbidden strings all 0 (writer, notes, sources.yaml, S1..S9, W41-S#, model names, aeb1e8/1361-6641, local paths, grades outside A–D, 7 days, ≤ 56, crystalline β, companion-415, decananometer, "동축 시뮬레이션/coaxial simulation"); per-item qc blocks 0 (one report-level grid).
- Hypothesis table: every row has 5 cells.
- Repo linter on assembled `_assembled/reports/2026/w41/index.html`: `python -I repo/scripts/report_lint.py all --root sections/_assembled --report-only --offline` → doi-format PASS, doi-duplicate PASS, kr-en-adjacency PASS (298/298), vocabulary PASS (322 tokens), leak-check PASS, abstract-only-guard NA, derivations NA. SUMMARY PASS=5, NA=2. Output: `_tools/report_lint_out.txt`. (Baseline before fixes: leak-check FAIL ×68.)

## 5. Not applied / uncertain
- Re-check by the independent reviewer is PENDING; QC grid wording says so.
- "Numbers traced" and "fact vs inference" QC cells state the independent review covered them; the exact scope of the lost review file could not be confirmed.
- Items 2–3 cell identity (item 2's 415 analysed pairs vs item 3's 415 Vitriflow cells) stays an inference; item 2's text was not re-read for its data provenance in this pass.
- Residual noun-form list/metadata/heading lines were not converted (see §2(6)).
- i4 derivations (vii)–(viii) never existed in the notes; numbering now (i)–(vi) with no gap.
- `sources.yaml` still contains the known errors (outside this pass's write scope).
- No figure images were opened; no new numbers were introduced beyond sources or labeled derivations (0.905 is a corrected rounding of an existing derivation).

---

# Second fix pass (2026-11-10) — against the second independent review (`../review/review.md`, F1–F12)

Scope: edits only in `sections/` (i1, i2, i4, i5, report_head, report_tail; i3 unchanged). No push, no PR, repo clone untouched (`git status` in the repo clone: clean).

## 0. Backup, Bash-side changes, downloads
- Backup before any edit: `sections/_orig2/*.html` (cp of all 7 files).
- New scripts/outputs in `_tools/` (Bash heredoc, run with pinned venv `python -I`, SymPy 1.14.0): `i2_derivA.py` → `i2_derivA_out.txt` (F1); `tail_h6_check.py` → `tail_h6_check_out.txt` (F2); `i5_f7_check.py` → `i5_f7_check_out.txt` (F7); `ascii_diff.py` → `ascii_diff_pass2_out.txt`; `noun_endings_pass2_before.txt` / `noun_endings_pass2_after.txt`; `selfcheck_pass2_out.txt`; `report_lint_pass2_out.txt`.
- Download (F6): `_dl/i1/page.html` = `curl -L` of the item-1 Springer article page (HTTP 200, 341,721 B; differs from the review's quarantine copy only after char 195,652, a cookie token region). Equation TeX extracted with grep/python -I; identical TeX to the review's copy. PDF-side read: pdftotext extractions `../review/quarantine/pub/i1.txt` and `i1_raw.txt` (read only).
- All HTML edits made with the Edit tool. `_assembled/reports/2026/w41/index.html` regenerated with `_tools/assemble.py`.
- Changed-line counts vs `_orig2` (git diff --no-index --numstat, added/removed): head 4/4, i1 16/15, i2 2/0, i3 0/0, i4 3/3, i5 3/3, tail 13/13.

## 1. Majors
### F1 (i2, missing derivation A) — APPLIED (option a: block added)
- Verified: i2 cited "유도 A / derivation A" (Source box, card EVIDENCE) and A6/A7 (observations 1–2) but contained only B, C, F. Derivation A existed in the item-2 working material (route sums, 52.4%, decile shares, exclusion surplus 5, 29/41).
- Added a ko/en "유도 A / Derivation A" paragraph pair at the top of the SymPy inference box: A1 165+182+65 = 412, +3 = 415 = 455−40; A2 182/347 = 52.4%; A3 182/412 = 44.2%, 165/412 = 40.0%; A4 30/42 = 71.4%, 3/42 = 7.1%, 29/42 = 69.0%; A5 3+30+9 = 42, 7+29+6 = 42; A6 14+15+7+9 = 45 (5 over 40); A7 29/41 = 70.7%. All are source counts or exact quotients of them; SymPy exact rationals (`_tools/i2_derivA_out.txt`) agree with the review's `check_i2_out.txt`. Letters D and E remain absent (nothing references them); not renumbered.
### F2 (tail W41-H6) — APPLIED
- Verified against i4: derivation (ii) 2.304 V vs 2.816 V; (iii) V_BD ratios 0.95 and 0.998. SymPy: 2.304/2.816 = 9/11 = 0.818 (`tail_h6_check_out.txt`).
- H6 restricted to planar TiN/HZO/MoOx, 6–8 nm, one process, TZDB E_BD only; explicit sentence that the 10-year TDDB gain is not explained (voltage ratio 0.818) and that the probability basis (0.001% vs 0.01%) must be checked first; extension to other HfO2 films demoted to a test proposal. Signature now V_BD-based; falsification adds a separately judged equal-voltage TDDB comparison against 0.82. Basis cell → "item 4 DOE → TZDB thickness splits, one process".
### F3 (tail W41-H7) — APPLIED
- Verified against i5 [1] and competitor (3). Hypothesis now: narrower Q_BD distribution ⇔ b < −1/2 (necessary and sufficient, item 5 [1]); b ≈ −1 fits fluence-driven damage, but b < −1/2 can also come from a trapping correlation (item 5 competitor (3)), so narrowness alone does not establish fluence dominance. Signature and criterion kept.
### F4 (head evidence banner) — APPLIED
- Verified against the i3 Source box (supplementary read with ≤40-char lines filtered, Supplementary Sections 1.1–1.5 and Tables 2–3 re-read, reference list skimmed). One ko and one en sentence added to the banner. Tail QC "Full text read" cell and Sources [3] (ko/en) now state the same reading level.

## 2. Minors
- F5 (i1 symbols) — APPLIED: mapping λ → δ and μ_trap → N_trap (to avoid item 4's λ = hazard 배율 / hazard multiplier) stated at first use (SOURCE_REPORTED (1)) and repeated in the Variables paragraph.
- F6 (i1 Eqs. (1)–(4)) — APPLIED for Eq. (1) only. Two reads: (a) publisher HTML TeX (fetched 2026-11-10); (b) PDF text extraction character sequence ("K = Ta ox / G 4 VfillerTpoly (1)"). They agree for Eq. (1): λ = (K/α_G)·T_ox^a/(⁴√V_filler·T_poly); the T_poly power 1 also matches the body sentence (nearly inversely proportional to T_poly at low trap number). Added a labeled eq line in report symbols (δ). For Eqs. (2)–(4) the PDF loses radicals and Greek letters (√T_poly and β cannot be confirmed) → one usable read → form kept UNKNOWN; their TeX forms are NOT reproduced in the HTML. K, α_G, a are undefined in the source text → UNKNOWN. Updated: i1 Source box, UNKNOWN/geometry box, observation (6), Variables, derivation (d) (now "two reads agree"; consistency conditional only on the cylindrical-filler assumption), card MODEL and SOURCE TRACE; head banner and head table row 1 ("Eqs. (2)–(4)"); tail observation summary item 1 (6) and Sources [1].
- F7 (i5 [5]) — APPLIED: added "for equally spaced calibration levels (more generally, zero third central moment)" and that the expression is not exact for asymmetric levels; the abstract gives no level placement. SymPy (`i5_f7_check_out.txt`): 38/38.5/39/39.5 → exact 5a2/4 = formula; 38/38/38.5/39.5 → exact 9a2/8 vs formula 15a2/8; general exact = a2[(x−c̄)² − s² − (m3/s²)(x−c̄)].
- F8 (head row 4) — APPLIED: "(중도 절단) / (censored)" → "(right-censored로 읽음, 시험 중단 여부는 UNKNOWN) / (read as right-censored; whether the test stopped there is UNKNOWN)".
- F9 (tail H1, H2) — APPLIED: H1 rejection = slope CI excludes 1/3 (inclusion of 1/2 only for interpreting controls). H2 = layer-to-layer δ difference is a monotonic function of the measured hole radius with the sign fixed before measurement (reason stated: volume trap number rises with r_f, sheet amplitude falls, so item 1's framework does not fix the sign); criterion adds non-monotonic and opposite-sign cases.
- F10 (i4 boundary (d) and card) — APPLIED: 4–14 nm is described as the range of the literature grain-size-vs-thickness trend in Supplementary Fig. 8, not the paper's own TDDB range (checked in the source text: literature grain-size analysis, "at least within the 4- to 14-nm range examined").
- F11 (합니다체) — APPLIED where a real sentence: i1 "1/3 ... 세 가지로 설명될 수 있습니다" (colon list folded into the sentence); the new derivation A lines end in 입니다. Remaining checker hits (240 lines in `noun_endings_pass2_after.txt`, was 242) are bold run-in labels, "접근 수준/선정 분류" metadata, colon-introduced variable/condition/factor lists, B2–B5 chain items, table cells, and splitter artefacts at "Fig."/"Ref."/"Sec."; kept.
- F12 (i5 DOE (c)) — APPLIED: KR now says the curvature reading is rejected and the under-prediction at 40 V is attributed to sampling noise.

## 3. QC wording
- Tail QC grid "Independent physics review" cell is now exactly: "independent physics review PERFORMED on the corrected text (no blocker; four majors found and fixed); minor edits after this review received mechanical checks only; re-check of those last edits not done".
- Statements implying the first review's scope was known removed: "Numbers traced" and "Fact vs inference" cells no longer cite "the independent physics review (PASS-WITH-FIXES)"; they describe only the review on the corrected text (numbers and derivations of items 1–5 re-derived with SymPy, all matched except the F7 condition) and say that edits after it got mechanical checks only. Head banner and tail QC paragraph (ko/en) rewritten accordingly. All "PASS-WITH-FIXES" and review "PENDING" strings removed from the public HTML (the CSS class "pending" is unchanged).
- The head and tail paragraphs say the edits after the review "(the major fixes and the minor edits)" received mechanical checks only — slightly broader than the grid cell, so as not to imply the major fixes were re-reviewed.

## 4. Self-checks (this pass)
- `_tools/selfcheck_pass2_out.txt` (head + i1..i5 + tail): tag balance 0 errors / 0 unclosed; 26 classes used, 0 missing from repo `assets/style.css`; ko→en adjacency ko=299 en=299, 0 violations (parser and raw-text); 172 table cells with paragraphs, 0 unpaired; 12 internal anchors, 0 unresolved; forbidden strings all 0 (writer, notes, sources.yaml, bare S1..S9, W41-S#, model names, unpublished paper id, local paths, grade outside A–D, 7 days, ≤ 56, crystalline β, companion-415, decananometer, coaxial-simulation heading); per-item qc blocks 0. OVERALL PASS.
- Repo linter on `_assembled/reports/2026/w41/index.html`: from the repo clone, `python -I scripts/report_lint.py all --root ../w41/sections/_assembled --report-only --offline` → doi-format PASS (6), doi-duplicate PASS, kr-en-adjacency PASS (299/299), vocabulary PASS (328 tokens), leak-check PASS, abstract-only-guard NA, derivations NA; SUMMARY PASS=5, NA=2 (`_tools/report_lint_pass2_out.txt`). NA = not verified.
- ASCII-token multiset diff vs `_orig2` (`_tools/ascii_diff_pass2_out.txt`), tied to findings:
  - head (+138/−8): F4 (40, characters, lines, filtered, supplementary, skimmed, reference, list, main, level); F6 (Eq, TeX, PDF, HTML, agree, reads, form, 2–4 tokens); F8 (right-censored ×2, UNKNOWN, whether, stopped, test; − censored); QC (blocker ×2, four, majors, corrected, mechanical, checks, edits, done; − PASS-WITH-FIXES ×2, PENDING ×2, applied, requested, verdict).
  - i1 (+351/−24): F5 (source, writes, symbol(s), clash, hazard, multiplier, decay, constant, average, trap, number, N); F6 (Eq ×8, Eqs ×4, TeX ×17, PDF ×13, HTML ×4, publisher ×7, 2026-11-10 ×4, Greek, letters, radical, signs, character, sequence, agree(s), reads, K, G, a, 1/4, filler, volume, m, Governing; − garbled ×3, extractions ×4, Equations ×2, differently ×2, typeset, unconfirmed, exact ×2, equation, Form); derivation (d) (cylindrical-filler, assumption, holds).
  - i2 (+190/−0): F1 only (A1–A7, 165, 182, 65, 412, 415, 455, 40, 3, 347, 42, 30, 29, 41, 14, 15, 7, 9, 45, 5, 6, 52.4%, 44.2%, 40.0%, 71.4%, 7.1%, 69.0%, 70.7%, 10%, SymPy, exact, rationals, arithmetic, consistency, ...). No value outside the source counts and their quotients.
  - i3: no change.
  - i4 (+44/−7): F10 (literature, grain-size, grain-size-versus-thickness, trend, confirmed, range, validity, TDDB, own, paper; − mentioned, mentions, reference, by, with, to, source).
  - i5 (+43/−0): F7 (equally, spaced, third, central, moment, zero, 0, 3, asymmetric, calibration, levels, placement, abstract, exact, expression, 40, V). F12 is Korean-only.
  - tail (+586/−52): F2 (W41-H6, TZDB, TiN/HZO/MoO, 6, 7, 8, nm, process, 0.95, 0.998, 2.304, 2.816, 2.304/2.816, 0.818, 0.82, 0.001%, 0.01%, ii, iii, BD, V, allowable, allowable-voltage, ramp, margin, proposal, Extension; − TDDB-life, vanishes, Compared, remains, systematically, high-k, thickness, differs, comes, voltage); F3 (b, ln, I, early, necessary, sufficient, trapping, correlation, fluence-driven, competing, mechanism, narrower, alone, establish); F9 (1/2, monotonic ×4, pre-fixed, sign, opposite, layer-to-layer, controls, interpret, sheet, amplitude, volume, r; − unrelated, direction ×2, follows, varies); F4 (supplementary, 40, characters, lines, filtered, skimmed, re-reads, partial); F6 (Eq, TeX, PDF, Greek, letters, radical, signs, agreeing; − garbled ×3, extractions, differently); QC (review, corrected, blocker, majors, mechanical, checks, edits, last, done, re-derived, derivation, SymPy-checked, applicability, condition, labels, scope; − PASS-WITH-FIXES ×5, PENDING ×5, applied ×5, fixes ×4, requested, verdict(s), recomputation, enrichment, still).

## 5. Not applied / uncertain
- F6: TeX forms of Eqs. (2)–(4) not shown (single usable read). The PDF read of Eq. (1) cannot itself show radicals; agreement rests on the character order, the visible root index "4", and the body sentence for the T_poly power. Whether the TeX difference between Eq. (1) (T_poly) and Eqs. (3)–(4) (√T_poly · T_poly^{β/(−μ_trap)}) is a typo or a definition was not judged.
- Derivation letters D and E are still absent in item 2 (no references; not renumbered).
- No re-review of this pass's edits (the QC text says so). Linter NA rows (claims ledger, audit scripts) remain unverified. Rendering/PDF and figure images not opened.

## Third pass (coordinator, 2026-11-10): minor findings of the focused re-check (Python exact-string replace, each asserted unique)
- F1-m1 (i2 A7, ko/en): added that 41 is not 42 - 6 and its derivation is UNKNOWN.
- F1-m2 (i2 A, ko/en): separated source-printed percentages from the derived share 29/41.
- F3-m1 (tail H7, ko/en): added 'under the Weibull log-variance proxy' to the necessary-and-sufficient statement.
- F6-m1 (head banner, ko/en): 'could not be cross-checked by two reads' instead of 'two reads did not agree' for equations (2)-(4) of item 1.
- QC wording (head and tail, ko/en and the three QC cells): the major fixes received a focused independent re-check (no blocker, no major); minor edits after that re-check received mechanical checks only.
