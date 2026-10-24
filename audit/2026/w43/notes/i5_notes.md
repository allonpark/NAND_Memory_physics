# i5 notes — W43 item 5 (ARCHIVE_GAP), DOI 10.1063/5.0355163

Source: Liu Y., Yue Y., Yu H., Yan J., Cui H., AIP Advances 16(10) 105114, CC BY 4.0. Received 2026-08-03, accepted 2026-09-30,
online 2026-10-15 (Crossref; page header). Citation line on page: 1 Oct 2026 = issue label. Used 2026-10-15.
Access: full_text (publisher HTML). Figures (images) and supplementary (figshare) NOT read. Eqs (1)-(8) garbled -> UNKNOWN form.

## Re-fetch log (own WebFetch, 2026-10-21; summarizing fetcher)
1. chars 0-100000, all numeric sentences -> confirmed abstract numbers, Table I/II, mechanism sentences, 1600 K, W_eff, 33.6-33.7%, 800 V/15 V, 600 V/75 A, 1200 V.
2. offset 100000 (conclusion, Table III) -> Table III: BV 1423/1685 V (Vgs 0 V, Ids 100 uA), Ron 42/45.6 (Vgs 15 V, Ids 40 A),
   Qgd 38/22 nC (@600 V), Crss 11/3 pF (@800 V), t_SC 10.6/14.5 us (800 V, 15 V, Tmax 1600 K), HF-FOM 1596/1003.2,
   E_max 3.48/1.95 MV/cm, Eon 555.93/342.69, Eoff 61.93/54.45 uJ, Isc 108.07/93.21 A and Tmax 1580.86/1475.82 K at t = 10 us.
   Eon 10%Vgs-10%Vds, Eoff 90%Vgs-90%Vds. Data availability: on request. Conclusion has no limitation statement.
3. targeted: 1600 K justification n_i ~1.42e16 cm^-3 vs N_drift 1e16; W_eff = span on JFET cutline with |Jn| >= 1e2 A/cm2 (superscript flattened; read as 10^2);
   "further narrowing of W_eff does not necessarily lead to a proportional reduction in I_SC"; "current distribution is not necessarily more uniform".
   Al implant 30/60 keV, 7e14/3e14 cm^-2, peak 2e19; JFET doping 7e16 in text (not Table I); poly 0.2 um in process text.
   Parameters: NC(300)=1.6e19, NV(300)=2.5e19, Eg(0)=3.265 eV, alpha=6.5e-4 eV/K, beta=1300 K; at 1600 K NC~1.97e20, NV~3.08e20, Eg~2.691 eV.
   Fig.5 caption: field contour + gate-oxide-corner profiles at 1200 V; crowding near split-gate corner; 3.48 -> 1.95.
4. targeted: "planar" appears only as "process-compatible with conventional planar SiC MOSFET fabrication"; no "trench".
   Not stated: tool name, SC initial T / thermal BCs, Vgs during 1200 V blocking, split-gate electrode connection, oxide-vs-SiC side of E_max,
   new peak location, initial Isc peak value, avalanche/UIS, TDDB/lifetime, experiments, 2D limitations.

## Source inconsistencies / problems noticed
- Date: header 2026-10-15 vs citation line 2026-10-01 (issue label). Used Crossref online date.
- The input fulltext notes listed BV as "higher, no value read (UNKNOWN)"; Table III actually gives 1423 -> 1685 V. Text near Fig. 3(c) gives no number; Table III and a sentence in the later part do. Notes were incomplete, not the paper.
- The input notes say "Peak-temperature rise ... final 5 us"; I could confirm "~33.6%-33.7% lower" but not the "final 5 us" window -> not used.
- My first re-fetch pass returned a fetcher-made claim that n_i(1600 K) should be ~5.6e17 (i.e. paper inconsistent). sympy with the paper's own parameters gives 1.423e16 -> the PAPER IS CONSISTENT; the fetcher's own arithmetic was wrong. Not used.
- 1200 V field comparison is at different V/BV fractions (0.843 vs 0.712); paper does not discuss this.
- Isc reported in A from 2D TCAD: device width/area normalization not found -> UNKNOWN.
- Equations (1)-(8) garbled; fetcher offered reconstructions; NOT adopted except as "standard form" in the n_i check (labelled).

## Tags used in i5.html
SOURCE_REPORTED: only Table/text values above + Fig.2 trend sentence + "planar process-compatible" sentence + W_eff/Isc non-proportional + "not necessarily more uniform".
AUTHOR_INTERPRETATION: low-potential clamping weakening drain-corner coupling; depletion narrowing electron path; path compression -> lower post-peak current -> lower power -> SCWT; 1600 K adoption rationale (stated as authors' choice).
ENGINEERING_INFERENCE / hypotheses: oxide-lifetime gain (not computed by paper, grade D); all competing mechanisms except clamping; tail discussion; cell being planar-type (inferred from process-compat sentence + JFET region); DOE.
EXTRAPOLATION_ONLY: NAND/T07 relevance, coaxial contrast.
Background knowledge (not re-checked, labelled): grounded p-shield and split-gate as known techniques; Ron-SCWT trade-off; other SC failure paths (metallization melt, gate rupture, delayed runaway).

## Grades
Simulated values C (TCAD only, no calibration/measurement; internal arithmetic consistent). Mechanism C. Oxide-life gain D. NAND transfer D.

## Archive comparison (only W37-W40)
git show origin/main:reports/2026/w37..w39/index.html and origin/weekly/2026-w40:reports/2026/w40/index.html in nand-audit/repo.
No DOI overlap; no split-gate / P-shield / SCWT item in W37-W40. Compared with W38 item 4 (Nakata & Sato, ICMTS, SiC AC-TDDB rise time),
W38 item 5 (Munshi, Mir & Shrivastava, IRPS, GaN electrothermal SOA crossover), W39 item 5 (Zhang et al., IET PE, diD/dt diagnosis),
W40 item 5 (Yan et al., J. Phys. D, PWM TDDB). W37 item 5 (Cao, SiC DGS) not used: no direct link.
Dedup vs W41/W42 was NOT done by me (instruction: no W41-W43 material); HTML does not claim it.

## Derivations (sympy 1.14.0, venv_sympy, python -I)
Script: i5_checks.py (same folder). Output: i5_checks_out.txt (same folder). Verbatim output:

```
sympy 1.14.0
[1a] Ron change = 8.571 % (source: +8.6%)
[1b] HF-FOM = Ron*Qgd: 1596 , 1003.20 (source 1596 / 1003.2)
[1c] Etot = 617.860 / 397.140 ; reduction 35.723 % (source 617.86/397.14, 35.72%)
[1d] corner peak field ratio = 0.5603 ; reduction 43.97 %
[1e] W_eff reduction 59.26 % (source ~59%); Isc ratio 0.8625 ; implied mean |Jn| over W_eff ratio (I1/W1)/(I0/W0) = 2.117 [DERIVATION: assumes all current inside W_eff on one cutline; not source-reported]
[1f] SCWT change 36.79 %
[1g] BV change 18.41 %
[2] at 1600 K: NC = 1.971e+20 NV = 3.079e+20 Eg = 2.6912 eV, ni = 1.423e+16 cm^-3 (source: 1.97e20, 3.08e20, 2.691 eV, ~1.42e16)
[2] ni(1600 K)/N_drift(1e16) = 1.423
[3] SG: E_ox*t_ox = 34.80 V  [1D uniform-field equivalent only; actual corner field is 2D-crowded]
[3] SG-PS: E_ox*t_ox = 19.50 V  [1D uniform-field equivalent only; actual corner field is 2D-crowded]
[3b] on-state planar average field Vgs/t_ox = 1.50 MV/cm  [DERIVATION; ignores V_FB, surface potential, poly depletion, oxide charge]
[3c] blocking voltage / BV: 0.843 (SG), 0.712 (SG-PS)  [DERIVATION]
[3] interface normal-field relation: E_ox = (E_s*epsilon_s + Q_it)/epsilon_ox
[4] E_coax(r=a)/E_planar = t/(a*log((a + t)/a)) ; limit t/a->0: 1
[4] d/dx [x/ln(1+x)] > 0 check at x=1: 0.4020 (field enhancement grows with t/a)
[4] dV_i = log((r_out/r_in)**(Q'/(2*pi*epsilon_i)))
```
Numbers in HTML not in the source, all from above: 34.8 V, 19.5 V, 1.5 MV/cm, 0.863 / -13.8% (rounded 0.8625), 59% (source ~59%), ~2.1x, +36.8%, 0.84/0.71, 1.42x, "about 14%".
Note: [4] d/dx check at a single point only; monotonicity of x/ln(1+x) is used qualitatively in notes, not in HTML.

## Weak points
- Fetcher is summarizing; numbers were cross-confirmed across 2-3 passes, but verbatim exactness of Table III relies on a single pass at offset 100000 (consistent with abstract/text values).
- "Planar-type cell" is an inference; if the cell were trench-type, the planar E_ox discussion still holds only for flat segments.
- SC lumped adiabatic equation is a framework, not the paper's Eq. (7)-(8).
- Hangul count 3780 (HTML).
