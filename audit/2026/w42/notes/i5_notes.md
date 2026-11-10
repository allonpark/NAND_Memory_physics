# W42 item 5 notes: arXiv 2610.16438 (Chen, Zhang, Fong, Li, Li), CSC AOS MOS trap decoupling

Status: DRAFT section in scratchpad only. No repo write, no commit, no push, no PR.
Output: i5.html (same folder). Scripts: i5_sympy.py -> i5_sympy_out.txt (sympy 1.14.0, mpmath 1.3.0, venv_sympy, python -I, exit 0).
Earlier stdlib-only run (written while the venv was missing): i5_checks.py -> i5_checks_out.txt. All values agree with the SymPy run.
Caches: _i5_cache/dl_s2_reread (abs.html, paper.pdf, raw.txt, html.html = arXiv HTML 404), _i5_cache/arch_s2 (git show origin/main W39/W40/W43 index.html).

## Source reads (two independent)
1. Read 1: cached layout extraction `w42/_txt/2610.16438.txt`, chars 0-23,584 per notes (file 23,791 bytes, legacy encoding; mu/omega garbled). Whole letter incl. captions/refs.
2. Read 2: PDF re-downloaded 2026-10-28 from https://arxiv.org/pdf/2610.16438 (sha256 prefix cf21f6bf82971b9d), `pdftotext -enc UTF-8` (non-layout), 19,738 chars, read in full.
- Figures not read as images. arXiv HTML: 404 (none).
- All numbers used in HTML were found in both reads (spot count in read 2: 63.6, 4.7 mV, 3.839, 0.283, 250 ns x3, 2.8-3.1, 9-12, 600 um2, 400 and 900, 100 kHz, 0.3 eV, 10 um, 80 and 50, 4.5-nm, 6-nm, 30-nm, 100 nm, 400 C, 5 um overlap).
- CSC confirmed from text (abstract, title, Sec II): "conductive-semiconducting-conductive".
- Dates: abs page "[Submitted on 12 Oct 2026]", meta citation_date/online_date 2026/10/12; arXiv API 2026-10-12T09:03:22Z (from manifest). DataCite 2026-10-14 from manifest, not re-checked. Announcement date UNKNOWN. Subject cond-mat.mtrl-sci; Comments "4 pages, 10 figures".

## Labels used
- SOURCE_REPORTED: device/process; SS ~63.6 mV/dec; hysteresis ~4.7 mV; drain-floating C ~half; 400/900/~600 um2; RC peak f_peak vs 1/R_total; 1 kHz leakage ~1/f, negligible >100 kHz; extra peaks with L at W=10 um; Eg 3.839 eV, EC-EF ~0.283 eV; depletion Dit 9-12e11, tau ~250 ns; weak acc DOS 1e18-1e19 /eV/cm3 Gaussian-like, us-ns, ~0.3 eV, no RC correction (Fig 9d caption); strong acc Dit decreases then 2.8-3.1e12, tau ~250 ns; ~3x; W=80/50 consistent.
- AUTHOR_INTERPRETATION: contact-artifact mitigation, edge compensation explains 600, donor-like "possible", shallow-state assignment "consistent with", RC "limited", minimum origin, 3x "may help", "simple, scalable".
- UNKNOWN: temperature, device count/spread, AC amplitude, continuum-model equations + sigma_s, psi_s(VG) method, f_pred definition, capacitance ratio values, Fig 5 L values, HfO2 k / C_ox, border-trap treatment, stress data.
- Grades: AOS values/procedure C; regime assignment C; degradation link D; poly-Si transfer D.

## Derivations (i5_sympy_out.txt)
- D1 1/(2 pi 250 ns) = 636,620 Hz; w*tau = 1.5708 at 1 MHz, 1.5708e-3 at 1 kHz.
- D2 single level peak x=1, value 1/2; continuum (no fluctuation) x*=1.980291, value 0.4023712; f_peak for tau=250 ns = 1.26069 MHz (outside window). Authors' fluctuation model peak condition UNKNOWN -> only a caution.
- D3 1e18..1e19 * 4.5 nm = 4.5e11..4.5e12 /eV/cm2 (same magnitude as Dit values).
- D4 accumulation/depletion ratio 2.333..3.444 (consistent with "approximately threefold").
- D5 distributed RC line fed from both ends: Gp/w/C_tot peak at x = w R_sh C_ox (L/2)^2 = 2.54065 (value 0.417227); small-x Re -> x/3; f_peak(2L)/f_peak(L) = 1/4, W-independent.
- D6 coaxial: C_coax/C_planar = u/ln(1+u) = 1 + u/2 - u^2/12 + ...; annulus volume per outer area = t_ch(1 - v/2).
- D7 cubic grains S_v = 3/d.

## Archive comparison (published origin/main only: W37-W40, W43)
- W39 item 4 (IGZO vertical CTM, Jung/Hwang/Yoon): "not a drop-in VNAND model" boundary kept.
- W40 item 3 (Zhu/Wang/He TCAD, grain-boundary traps, planar vs coaxial): adds measurement normalization + GB-R_total coupling.
- W43 item 4 (Dutta/Bose/Hoque/Saha TFET TCAD Gaussian interface traps): adds RC-correction caution for measured Gaussian DOS.
- W37, W38, W43 others: no AOS / conductance-method overlap found by keyword scan. W41/W42 drafts not used.

## Source inconsistencies observed (in HTML "Observed on reading" box)
1. Abstract asserts donor-like association; body says "possible"/"may partly reflect".
2. Abstract "identified and calibrated" vs body/Fig 9d caption "without RC correction", equivalent-circuit model still needed.
3. Abstract "increased" strong-acc density vs body non-monotonic with unexplained minimum.
4. Sec III-B sentence mixes VG and frequency dependence of the 1 kHz component.
5. tau ~250 ns identical across regimes and widths, near the 1 MHz window top (D1/D2) - not discussed by authors.
## Manifest/notes wording issue (not in HTML)
- Manifest fact F6 phrase "time constant near 250 ns (about 3x the depletion value)" can be misread as tau being 3x; the source's ~3x refers to apparent interface-related state density.
- Notes give 23,584 chars for read 1; cached file is 23,791 bytes (encoding difference, not a content gap).

## Deviations
- First derivation pass used Python stdlib because venv_sympy was missing; re-run in SymPy after the coordinator recreated it; HTML now labels derivations "SymPy-checked".
- HTML numbers not from source: only D1-D7 derived values, each labeled as derivation.
