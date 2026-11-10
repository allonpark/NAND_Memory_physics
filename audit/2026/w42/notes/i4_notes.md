# W42 item 4 notes (source: arXiv 2610.20154, Guido et al., access-rate dependent endurance of HZO capacitors)

Status: DRAFT in scratchpad only. No repo writes, no push, no PR.
Written: 2026-10-28/29. Output: i4.html (section id="i4").

## 1. Reads (two independent extractions)

| Read | File | Tool | Size | Ranges read |
|---|---|---|---|---|
| R1 | w42/_txt/2610.20154.txt (cached by source verifier) | pdftotext -layout | 73,233 chars (cp1252 decode) | whole file, lines 1-1167 = chars 0-73,233 (main text, refs, SI S1-S4, Tables S1-S3) |
| R2 | sections/_dl_i4/pdf.pdf, re-downloaded 2026-10-28 from https://arxiv.org/pdf/2610.20154v1 (HTTP 200, 3,394,207 bytes, 30 pages, md5 162a5a5186a93993546a37c4e853e807) -> sections/_dl_i4/pypdf.txt | pypdf 6.13.3 (i4_pypdf_extract.py) | 71,926 chars | targeted: chars 10,411-15,528 (Sec 2 Fig 1-2 text), 22,565-29,543 (defect levels, drift-diffusion, charge transfer), 30,537-36,208 (Eq 1-2, alpha/beta, Fig 5, Ea), 38,612-42,210 (Methods electrical), 55,853-56,322 (Table S1), 63,895-69,213 (SI S4 derivation, Tables S2-S3) plus grep hits for abstract (lines 63-64) |
| - | arXiv HTML https://arxiv.org/html/2610.20154v1 | curl | HTTP 404 | no HTML rendering exists; not available |

Figures 1-5, S1, S2 not viewed as images (captions only). Reference list read as text (R1) but primary sources not checked.
Math glyphs (ln, exponents, Greek in equations) are lost in BOTH extractions: Eq. (1), (2), S24-S36 exact functional forms are UNKNOWN. Text words around them are readable.

## 2. Number confirmation (R1 vs R2)

All values used in i4.html agree in R1 and R2:
5 nm Hf0.5Zr0.5O2; 10 nm TiN electrodes; 30 nm W + 10 nm TiN bottom; ALD 300 C; RTA 500 C N2; ~1963 um^2; Pr 19.3 uC/cm^2 after 2x10^6 cycles; ~50 uC/cm^2 expected 2Pr; ~50% -> ~77%; peak merging ~10^4 cycles; delays 200 ns-200 us (wake-up); Delta2Pr 10-12 uC/cm^2 after 10^6; eps_r 34 -> 28.5; t-phase 40 vs o-phase 28-30; eps_r ~27.5 in access-rate cycling; 5 us square pulses, +-2 V; 2 ms delay & 10^6 wake-up at 100 kHz for Fig 3; 10^7 (Fig 5a) and 10^6 (Fig 5b) wake-up at 100 kHz; PUND 4.6 kHz; one capacitor per endurance test; levels 2.0 / 2.85 eV below CBM, 0.85 eV difference, TiN CB offset 2.3 eV, negative V_O level >0.5 eV above EF, relaxation ~1.5 eV; 0.1 C/m^2; D 1e-10..1e-12 cm^2/s; v 1e-5..1e-4 m/s at 1 MV/cm; alpha = 2x10^-9 uC^-2 cm^-4, beta = 1.7 ("respectively", order confirmed in R2 where Greek survives); Table S1 gaps 5.6/6.0 eV and levels; Table S2 (98.0/11.2, 157.1/25.3, 330.1/139.1, 613929.1/837874415809.9, 2385.3/49599.2); Table S3 (111.0/15.9, 79.3/6.2, 61.8/3.1, 58.1/2.6, 53.0/2.1); Ea 0.09 -> 0.04 eV, break ~85 C; V_O migration 0.5-1.2 eV; Ettisserry 0.2 eV; validity up to 135 C and 2 ms; extrapolation to 10^10 cycles.
Correction found by R2: R1 line 335 reads "ns- to s-range" (mu lost); R2 reads "ns- to μs-range". Used the R2 reading (the R1 glyph is lost, not contradictory).
fulltext_notes table row 8 said alpha/beta assignment UNKNOWN; R2 resolves it (alpha 2e-9 with unit, beta 1.7).

## 3. sympy (venv_sympy, sympy 1.14.0) — i4_sympy.py -> i4_sympy_out.txt
Labelled BACKGROUND / ENGINEERING_INFERENCE (not the authors' equations).
- S1 duty = t_p/(t_p+t_d); limits 1 and 0.
- S2 for ANY differentiable G with Delta = -G(N^beta t_d/tau): (dDelta/dlnN)/(dDelta/dln t_d) = beta; iso-damage slope dln t_d/dlnN = -beta.
- S3 field-on clock: dln X/dln t_d = 0; wall clock N^beta (t_p+t_d): elasticity t_d/(t_p+t_d), -> 0 for t_d<<t_p, -> 1 for t_d>>t_p.
- S4 int_0^theta0 cos sin = sin^2(theta0)/2 = (1-cos^2)/2; reconstructed P = P0(1-a^2 ln^2 X) -> squared-log form (ENGINEERING_INFERENCE; not confirmed, glyphs lost).
- S5 recovery-type model: dDelta/dln t_d = t_d R'(t_d) > 0 (less loss with longer delay) -> opposite sign to the source's observation.
- S6 Arrhenius slopes of ln tau0 vs 1/kT from Table S3: 0.08997 eV (25-85 C) and 0.03880 eV (85-135 C) -> reproduces 0.09 / 0.04 eV. (Slope positive because tau0 falls with T.)
- S7 Einstein relation, z = 2, 300 K, 1 MV/cm: D = 1e-10 -> v = 7.74e-5 m/s (inside stated range); D = 1e-12 -> 7.74e-7 m/s (below stated lower bound 1e-5).
- S8 v*t_d with text velocities: 0.002-0.02 nm at 200 ns; 20-200 nm at 2 ms (film 5 nm).
- S9 tau0 falls 2.10x and 1.60x per decade of t_d (1/t_d would give 10x) -> tau = tau0*t_d not constant.
- S10 Table S1: 2.0 and 2.85 eV, diff 0.85 (matches text); V+ empty - V0 occupied = 1.4 (Zr), 1.55 (Hf) vs "approximately 1.5 eV" (reference level of the 1.5 eV not stated; consistent in magnitude).
Earlier plain-Python run (i4_checks.py -> i4_checks_out.txt) made before venv was available; same results; also a magnitude probe of alpha (C8) and a finite-difference check of S2 with three G forms.

## 4. Source inconsistencies / irreproducible points (observed on reading, not confirmed by authors)
1. tau0 definition vs units: text says tau0 is the RATIO tau/t_d (dimensionless), but Tables S2/S3 give tau0 in ns and Fig 5b inset uses "ln tau0 in seconds".
2. alpha unit uC^-2 cm^-4 cannot make Eq. (1) dimensionally consistent with Delta2Pr in uC cm^-2 under any reconstruction we tried; with alpha = 2e-9 the reconstructed Delta2Pr is of order 1e-6 uC/cm^2 (C8, plain Python), i.e. undetectable. Eq. (1) is not reproducible from text (glyphs lost).
3. Figure references: text cites "Figure 2b" for GIXRD (caption: Fig 1b); text cites Fig 2b for peak coalescence/switching field and Fig 2c for Delta2Pr, but caption assigns (b) Delta2Pr, (c) switching fields. Both extractions agree.
4. Drift numbers: the lower end of cited D gives v two orders below the stated lower bound (S7); with the stated v, 2 ms delays give 20-200 nm travel >> 5 nm film (S8), which sits uneasily with "traverse the entire film thickness at sufficiently long delays (order of seconds)". Caveat: the field during the delay is not necessarily 1 MV/cm.
5. RT tau0 at 2 ms: 98.0 +- 11.2 (Table S2, after 10^7 wake-up) vs 111.0 +- 15.9 (Table S3 at 25 C, after 10^6 wake-up, different probe station). 1-sd intervals overlap; not an error, but preconditioning differs between the two data sets.
6. Refs [10] and [28] are the same paper (Xu et al., Nano Research 2026), and [29] = [30] (Hamouda et al. JAP 2020) — duplicate references.
7. Abstract/introduction say "experimentally verified" model; but the 10^10 point is a fit extrapolation and 200 ns / 2 us fits are "purely indicative" (huge SD).

## 5. Labels / grades used
- Measured trends (wake-up independent of delay; larger 2Pr loss for longer delay; unipolar vs bipolar contrast; tau0(T)): C — unreviewed preprint, one capacitor per test, magnitudes only in unread figures; internal arithmetic (Ea, Table S1) reproduces.
- V_O electron-emission mechanism: C — physically consistent, ab initio + drift-diffusion support, no direct experimental isolation; competing explanations not excluded.
- 10^10 cycle projection: D (EXTRAPOLATION_ONLY).
- NAND analogy: D (EXTRAPOLATION_ONLY).

## 6. Archive comparison (published origin/main only: W37-W40, W43; extracted copies in _arch_i4/)
- W40 item 5 (SiC PWM: lifetime up with frequency; recovery vs duty) — opposite sign here.
- W38 item 4 (SiC AC-TDDB: equal HIGH time not enough; edge term) — here: equal field-on time not enough; delay term.
- W39 item 2 (GaN stress-history hidden state) — preconditioning history (10^6 vs 10^7 wake-up).
- W43 item 2 (BGW: fitted shape parameter is a statistical result) — here a fitted tau0 and its Ea are used as mechanism evidence.
W41/W42 drafts not used.

## 7. Not supported / not done
- Exact form of Eq. (1), (2), S24-S36 (glyph loss in both extractions; no arXiv HTML).
- Any value read from figures (Delta2Pr magnitudes vs N, 10^10 inset values, Figure S2 leakage values).
- Number of devices per condition (only "a different capacitor per endurance test").
- Exact number of delays per bipolar cycle (one per pulse vs one per cycle) -> n_p kept symbolic.
- arXiv announcement/listing date (submission 2026-10-14T13:11:11Z confirmed; DataCite registration 2026-10-15).
