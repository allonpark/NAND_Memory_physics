# i2 notes — report item 2, arXiv:2610.06173v1 (Cottom & Olsson, 2026-10-05)

Writer notes (scratchpad only; not for publication). Inputs read: sources.yaml header + this source's entry; fulltext_notes for this source.
HTML output: i2.html (same folder). Derivation script: i2_checks.py; output: i2_checks_out.txt (sympy 1.14.0, venv_sympy, python -I).
Format/number checks: fmt_check_i2.py, num_check_i2.py (same folder).

## Re-fetch (done myself, 2026-10-26)
- `curl https://arxiv.org/pdf/2610.06173v1` -> HTTP 200, 3,562,656 bytes -> `pdftotext -enc UTF-8` -> 75,330 chars (refetch_s1/b.txt).
  Same PDF text as the earlier non-layout extraction w41/txt/p1.txt (cmp identical for the default-encoding extraction).
  **Read in full, chars 0–75,330** (main text, methods, data/code availability, refs [1]–[63], SI figure captions, SI Tables S1–S8 text).
- `curl https://arxiv.org/html/2610.06173v1` (LaTeXML HTML, HTTP 200) -> text 80,926 chars (refetch_s1/h.txt). Used as the **second, independent rendering**: every number and equation in i2.html was searched there (refetch_s1/hcheck.txt + targeted greps). All found.
- abs page: title, "Submitted on 5 Oct 2026", licence CC BY 4.0 confirmed.
- No summarizing fetcher used, so the ~100k truncation issue does not apply. Figures not viewed as images. Supplementary Data, Zenodo (10.5281/zenodo.21111822), GitHub not opened.

## Verification table (notes vs re-fetch; PDF = pdftotext, HTML = arXiv HTML)
| Item | Notes said | PDF | HTML | Used |
|---|---|---|---|---|
| pairs 455 / excluded 40 / analysed 415 | same | yes | yes | yes |
| exclusion criteria 14/15/7/9 | not in notes | yes | yes | yes |
| "Five pairs met multiple criteria" (Methods) vs "four pairs" (Table S1) | not noted | both present | both present | yes, as observed inconsistency |
| routes 165/182/65, 3 unassigned, 412 | same | yes | yes | yes |
| 182 of 347 Si4 (52.4%) | same | yes | yes | yes |
| top stabilisation decile 30/42 (71.4%), base 44.2%; polaron 3/42 (7.1%), base 40.0% | same | yes | yes | yes |
| deepest corrected spectral decile 29/42 (69.0%); abstract "69%" | same | yes | yes | yes |
| decile route counts 7/29/6 (depth), 3/30/9 (stab) | not in notes | Table S2 | Table S2 | yes |
| 6 pairs "neutral lower at anion geometry", all in upper stab decile; without them induced K 29 of 41 | not in notes | Table S1 (row/note layout scrambled) | Table S1 (clean) | yes |
| 95.7% CV; AUC 0.83 / 0.87 / 0.50 | same | yes | yes | 95.7 and 0.50 used |
| Spearman 0.765 / 0.636 / 0.664; R2 0.26 vs 0.24; 0.59/0.60/0.70; baseline 0.13 (stab) | same (+0.13 new) | yes | yes | yes |
| 5–95%: 4–33 atoms, 0.12–0.30 Å, 0.9–2.1 eV | same | yes | yes | yes |
| median max displacement 0.30/0.51/0.40 Å | same | yes | yes | yes |
| Table S2 E_stab medians 1.17/1.47/1.33 eV; relaxed depth 3.24/3.65/3.49 eV (uncorrected) | not in notes | yes | yes | yes, flagged uncorrected |
| level-drop/E_stab median ratio 2.2/1.9/1.6 | not in notes | yes | yes | yes (qualitative) |
| longest Si–N 1.962 Å, +0.578 Å; 98% | not in notes | Table S5 / Fig S6 caption | yes | yes |
| CP2K v2023.1, HSE06, Γ, spin-polarised; 0.005 eV/Å; MG2, NPT, 1 K/ps | same | yes | yes | yes |
| Si120N160, 280 atoms | not in notes | Table S1 | yes | yes |
| eps_inf 4.2, eps_s 7.8 | same | yes | yes | yes |
| mobility edge N_eff^el **≥ 56** | notes ">= 56"; **sources.yaml fact says "<= 56" (typo in manifest)** | ≥ | ≥ | ≥ used |
| graph: 2.33 Å, σ 1.25 Å, t = 0.5–8 | same | yes | yes | yes |
| equations (I_atom, D_trap, E_stab, Q_D, η, T0, L, H_t, S1t, identity) | partly | partly garbled | clean | all used; none left UNKNOWN |
| FNV "served as an established control" | — | yes, no comparison values | same | stated "no values" |

Numbers in HTML not literally in the source: 0.3398 (= 10 ln2 − 6 ln3, derivation C2), 0.906 (native-K depth enrichment 0.9055, B), 1.6e-4/5.5e-4/6.3e-7 and 1.617/1.563/0.178/1.358/18.55 (derivation B), 70.7% (29/41, A7), and the character counts 75,330 / 80,926 (my extraction lengths).

## Derivations (labeled in HTML)
- A (arithmetic): routes sum 412, +3 = 415; Si4 precursors 347; Si3 endpoints 247; 52.45%; 71.43/7.14/69.05/44.17/40.05%; decile composition sums 42; exclusion surplus 45−40 = 5; 29/41 = 70.73%, ceil(406/10) = 41.
- B (OUR statistics, hypergeometric null N=412, n=42): induced K P(X≥30)=1.60e-4 (enrichment 1.617, expected 18.55); P(X≥29)=5.51e-4 (1.563); polaron P(X≤3)=6.30e-7 (0.178); P(X≤7)=6.02e-4 (0.416, not used in HTML); native K enrichment 1.358 / 0.906. Assumes exchangeable cells; ignores workflow-wide systematics.
- C (source identity): ∫(e^{-λt}−e^{-2λt})²/t² dt = λ(10 ln2 − 6 ln3) ≈ 0.3398 λ; D^{1/2} L D^{1/2} = D − A; u^T(D−A)u = Q_D. Consistent.
- D (GENERAL BACKGROUND): harmonic linear coupling: level drop = 2 E_rel; Marcus E_a = (λ+ΔG)²/(4λ) → λ/4; τ ratio; demarcation energy slope k_BT in ln t and ln ν.
- E (textbook Gauss law, symbols only): coaxial ΔV per layer; |ΔVth(r_c)| = Q'/(2π)[ln(r_n/r_c)/ε_N + ln(r_g/r_n)/ε_B]; d/dr_c < 0.
- F (OUR bookkeeping): E_T = D_vert + E_stab (general); equal-curvature harmonic: D_opt = D_vert + 2E_stab, E_T = D_opt − E_stab.
- Deliberately NOT computed: any E_T from route medians (medians not additive; corrected vs uncorrected quantities would be mixed). Stated in HTML as computable per cell from Supplementary Data (not opened).

## What I could not support
- Any retention, emission, capture, hopping or lateral-migration rate: not in the paper (UNKNOWN). All device links are ENGINEERING_INFERENCE (grade D).
- Thermal ionization energies per route: not reported; only symbolic bookkeeping.
- Whether route fractions represent film trap densities: not supported (one site per cell, one cell size) — H1.
- Reversibility of induced-K bond breaking after emission: not computed — H2.
- Mapping of routes to the "shallow/deep" levels of W43 item 1 or N_t of W40 item 3: no basis.
- Hole trapping (W37 item 1 is about holes): paper is electron-only.

## Source / manifest inconsistencies noticed
1. Methods "Five pairs met multiple criteria" vs SI Table 1 note "four pairs meet more than one criterion"; per-criterion sum 45 vs 40 excluded (surplus 5) — undecidable from text.
2. SI Table 1: 6 pairs with "neutral lower at the anion geometry", all in the upper corrected-stabilisation decile; removal leaves induced K 29 of 41. Flagged pairs concentrate in the tail (enrichment survives).
3. SI Table 2 route-median depths are uncorrected, decile rankings are corrected — easy to mis-combine.
4. Abstract "69%" = corrected spectral-depth decile; 71.4% = stabilisation decile (different rankings).
5. Manifest (sources.yaml fact line for this source) writes "N_eff <= 56"; source says ≥ 56. Fulltext notes have it right.
6. Manifest fact "Held-out R^2 ... 0.26 for relaxation vs 0.24 route-mean baseline" — source: η vs local ionic RMS displacement (ionic motion), fine; "0.59-0.60 for stabilisation" fine.
7. Main text "trap level lies below the anion HOMO in 42 cells" vs Table S1 "Trap state not index 641: 42" and "Trap below the neutral HOMO: 44" — consistent once read as different quantities (anion vs neutral HOMO); not an inconsistency, not used.
8. Main text "outside the precursor participation region in four of the 412" vs Table S1 "7" = 4 polarons + 3 unclassified — consistent.

## Evidence grades
- In-ensemble route classification and tail enrichment: C (DFT-only preprint, not reproduced, arithmetic consistent).
- Transfer to CTL retention / lateral migration / Vth tails: D.
- Our derivations: math checked (SymPy); applicability conditional.

## Companion-item statement
HTML box states items 2 and 3 are one research line (same authors, workflow, DFT settings, taxonomy) and not independent evidence; no item-3 numbers are used in i2.html.

## Archive comparison (origin/main only: w37, w38, w39, w40, w43 via `git show origin/main:reports/2026/wNN/index.html` in the nand-audit clone after `git fetch`)
- W37 item 1: Hwang et al., hole lateral migration in Si3N4 CTL, PF-type diffusivity (measured). Different carrier/evidence; no change; adds microscopic candidate to W37 "single-population incomplete" DOE criterion.
- W37 item 3: charge-ring lateral field — not used.
- W38 item 1 (CTL-local BTBT; trap spectrum may shift onset) and item 2 (VPASS changes occupied-trap energy distribution; stretched exponential): route mixture offered only as a candidate interpretation, untested.
- W39: no CTL trap-physics item (item 4 IGZO vertical CTM, not used).
- W40 item 3 (CTL N_t TCAD, abstract-only) and W43 item 1 (AN stack, shallow/deep nitride levels, abstract-only): no mapping basis.
- No W41/W42 draft-branch material used.
