# i1 notes — W41 item 1: Oh & Shin, J. Comput. Electron. 25:196 (2026), DOI 10.1007/s10825-026-02647-9

Writer notes (internal; not for publication). Section file: i1.html (same folder).

## What was read
1. `w41/txt/rtn.txt` — pdftotext of the publisher OA PDF, read in full (sources.yaml states 33,530 chars; file is 33,942 bytes because of non-ASCII bytes). Abstract → references. Figure images not viewed; only captions and extracted axis strings.
2. Publisher HTML re-read twice on 2026-10-26 with WebFetch (link.springer.com article page; reached via the idp cookie-transit redirect `?error=cookies_not_supported`, which is Springer's cookie-less fallback page, open access; no access control bypassed). Direct PDF URL also redirected to the same cookie flow and was not used. WebFetch is a summarizing tool: quotations are short and not guaranteed verbatim; no character offsets available (whole page summarized).
3. sources.yaml header + W41-S5 entry; fulltext_notes_W41-S5.md.
4. Format refs: w43/sections/i3.html (full), i4.html/i5.html (box conventions). CSS classes used: boundary, chain, compare, doebox, eq, inference, label, sourcebox (all in assets/style.css).
5. Archive: origin/main reports/2026/w37..w40, w43 (h2 titles + RTN/percolation grep). W41/W42 draft branches not used.

## Confirmation table (each used number/condition: extraction + both WebFetch passes)
| Item | rtn.txt | WebFetch #1/#2 | Used |
|---|---|---|---|
| Received 2026-05-12 / Accepted 2026-09-19 / Published 2026-09-29, CC BY 4.0 | yes (pub date from yaml/Crossref) | #1 yes | yes |
| δ ∝ cube root N_trap (3D), square root (2D) | yes | #1 yes | yes |
| <2 abnormal CDF; analysis ≥3 | yes | #1 yes | yes |
| 1000 TCAD cells ANN training; 10,000 MC per CV split | yes | #1 yes | yes |
| 2D: 3 conditions per CV, 100 TCAD per condition, 10×10 | yes | #1 (10 segments), #2 (100 per condition, three conditions) | yes |
| 3D: thickness 5 segments, WL length 20 | yes | #1 yes | yes |
| sum of Tox/Tctn/Tbox exponents ≈0.9 | yes | #1 yes | yes |
| LWL fourth root (low N); Tpoly ~1/Tpoly low N; saturates | yes | #1 yes | yes |
| double-Gaussian vs single Gaussian | yes | #1 yes | yes |
| "macaroni" present; "cylindrical" absent; no Vread/Vpass values; temperature only in a ref title; no grain size | yes | #1 yes | yes |
| LWL/Tpoly ↔ W/L of 2D | yes | #1 yes | yes (observed-on-reading) |
| Data availability "No datasets were generated or analysed" | yes | #1 yes | yes |
| Rf inverse relationship (single-Si, Sec 2) | yes | #1 yes | yes |
| Fig 4 non-monotonic; several hundred TCAD insufficient; Markov; δ increases with N; Rf weak N dependence; filler > WL dimension; 2D MC exponents unchanged; ANN inputs/outputs | yes | #2 yes | yes |
| No trap energy, τc/τe, trap location class stated | yes | #2 yes | yes (UNKNOWN) |

NOT confirmed twice → not used as numbers in HTML (UNKNOWN):
- Figure axis strings: Fig 3 "LWL-0.54", "Tpoly-1.03"; LWL 21–23 nm, Tpoly 7.5–8.5 nm, Rf 14–16 nm axes; Fig 6 exponent axis 0.48–0.62 and "-0.6/-0.5"; Fig 7 "-0.25/-0.22", 0.20–0.26; Fig 8 "-1", "Tpoly-0.7", "Saturated", 0.6–1.0; δ axes 15–36 "[mV/dec]". Only in rtn.txt figure text; figures not viewed.
- Equations (1)–(4): rtn.txt and WebFetch #2 give different garbled renderings (WebFetch reconstructs e.g. Eq1 as K/(αG)·Tox^a/(V_filler^(1/4)·Tpoly), Eq3/4 with √Tpoly and Tpoly^(β/(−μ_trap)); the fetcher itself flagged them as best reconstructions). Common elements only: Tox^a, V_filler, Tpoly, cube root of N_trap in Eq 4. Marked UNKNOWN; not reconstructed. The V_filler^(1/4) reading is used ONLY as a conditional observation (D5), explicitly labeled.

## Labels decided
- SOURCE_REPORTED: simulation outputs stated in body text (scaling relations, counts, restrictions, double-Gaussian as a simulation result, data statement).
- AUTHOR_INTERPRETATION: percolation → dominant/negligible split → cube root; O/N/O acts on gate controllability; Rf dominance via field distribution; "more accurate prediction / design guidelines".
- Intro statement "RTN uniquely widens the left tail [9,10]" → SOURCE_REPORTED (authors citing literature), placed in failure-mode section.
- Geometry: UNKNOWN ("macaroni" + filler radius stated; "cylindrical" not stated; coordinate system not stated). Coaxial analysis = ENGINEERING_INFERENCE framework.
- Grades: source results C (simulation only); real-device exponent D; percolation interpretation C; our frameworks C.

## Source inconsistencies observed (not confirmed by authors)
1. LWL↔W and Tpoly↔L mapping to 2D (Sec 2) vs vertical current along WL-length direction (usual mapping LWL↔L, perimeter↔W).
2. Gap: abnormal CDF described for mean trap number <2, analysis restricted to ≥3; 2–3 unexplained.
3. Fig 4 non-monotonic Tpoly dependence attributed both to "additional dominant physical factors" and to insufficient TCAD sample size.
4. Abstract contrasts poly-Si 3D with "2D NAND or single-Si 3D NAND" for N-dependent scaling, but MC vs N_trap is described only for 2D (Fig 13); no MC for single-Si 3D found.
5. Data availability "no datasets generated" vs 1000 TCAD cells + 10,000 MC per split.
6. Equations garbled differently in two extractions.
7. Trap grid has no azimuthal coordinate (5 thickness × 20 length) — whether azimuth sampled is UNKNOWN (put in UNKNOWN box, not in inconsistencies list).
8. Minor: Fig 5 caption "Ttox".
Upstream manifest discrepancy: sources.yaml says published "7 days before 2026-10-05"; 2026-09-29 → 2026-10-05 is 6 days. HTML uses 6 days.

## Archive comparison (origin/main only)
- W40 item 3 (h2 "CTL trap density, tunnel-oxide thickness and poly-Si grains in TCAD: planar-vs-coaxial"): inference that small-integer GB count → percolation-like paths → single GB trap RTN and large ΔVth; notes the abstract gives no evidence the paper treats percolation/RTN.
- W40 item 1 (transient failures, peripheral): hypothesis list contains "H5 RTN/BTI" — different device region; not linked.
- W43 item 1: competing-mechanism table row "Poly-Si channel (grain-boundary) trap charging … RTN … not mentioned".
- W37, W38, W39: no RTN items (W38/W39 "percolation" only in TDDB context).

## SymPy derivations (script i1_derive.py, sympy 1.14.0, run with venv_sympy python -I)
D1 trap statistics: fixed-fraction double-Gaussian + independent Poisson traps → exponent exactly 1/2; Var = Aμ^γ + Bμ → local exponent (γx+1)/(2(x+1)), limits 1/2 and γ/2; 1/3 needs γ = 2/3 if dominant part dominates; Gaussian tail local slope σ·ln10/(z+1/z) ∝ σ at fixed window; window drift changes apparent exponent.
D2 coaxial sheet amplitude: ratio coax/planar (area at r0) < 1 (single layer ln(1+u)/u; grid max < 1).
D3 annular channel trap count: d ln N_bulk/d ln Tpoly = 2(1+t)/(2+t); outer interface t/(1+t); d ln N_bulk/d ln r_f = 2/(2+t); t = Tpoly/r_f.
D4 conditional fixed-density total sensitivity using text low-N exponents with N^(1/3): LWL +1/12; Tpoly bulk −(t+4)/(3(t+2)) ∈ (−2/3, −1/3); interface −(2t+3)/(3(t+1)) ∈ (−1, −2/3); with 1/2 law LWL +1/4.
D5 conditional: IF δ ∝ V_filler^(−1/4), V_filler = πRf²LWL → Rf^(−1/2), LWL^(−1/4).
Arithmetic (not sympy): 1/10,000 empirical tail floor per MC split.

### Script output (i1_derive_out.txt)
```
sympy 1.14.0
D1a exponent (fixed-fraction double Gaussian, independent traps): 1/2
D1b local exponent: (A*gamma*mu**gamma + B*mu)/(2*(A*mu**gamma + B*mu))
   A-dominated limit (B->0): gamma/2
   B-dominated limit (A->0): 1/2
   gamma needed for 1/3 when dominant part dominates: [2/3]
   exponent in terms of x=A mu^g/(B mu): (gamma*x/2 + 1/2)/(x + 1)  d/dx = (gamma - 1)/(2*(x**2 + 2*x + 1))
D1c Gaussian local tail slope [units of sigma per decade]: sigma*log(10)/(z + 1/z) -> proportional to sigma at fixed window: d ln slope/d ln sigma = 1
   apparent exponent if window z drifts with ln mu (std ~ mu^1/2): (-dz_dlnmu*(z**2 - 1) + z*(z**2 + 1)/2)/(z*(z**2 + 1))
D2 coax/planar sheet amplitude ratio: log((((r_0 + t_1)/r_0)**(epsilon_2*epsilon_3)*((r_0 + t_1 + t_2)/(r_0 + t_1))**(epsilon_1*epsilon_3)*((r_0 + t_1 + t_2 + t_3)/(r_0 + t_1 + t_2))**(epsilon_1*epsilon_2))**(r_0/(epsilon_1*epsilon_2*t_3 + epsilon_1*epsilon_3*t_2 + epsilon_2*epsilon_3*t_1)))
   single layer: ln(1+u)/u, series: 1 - u/2 + u**2/3 + O(u**3)
   max ratio on dimensionless grid (t_i/r0 in 0.05..0.6): 0.9428
D3 d ln mu/d ln Tpoly: bulk = 2*(t + 1)/(t + 2) ; outer-interface = t/(t + 1)
   d ln mu/d ln r_f (bulk, Tpoly fixed) = 2/(t + 2)
   d ln mu/d ln L = 1 for all three
   t->0 limits: bulk 1  interface 0
D4 total d ln delta/d ln L at fixed density: 1/12
   total d ln delta/d ln Tpoly, bulk traps: (-t - 4)/(3*(t + 2))  range t->0: -2/3  t->oo: -1/3
   total d ln delta/d ln Tpoly, outer-interface traps: (-2*t - 3)/(3*(t + 1))  t->0: -1  t->oo: -2/3
   with a 1/2 law instead: d ln delta/d ln L = 1/4
D5 IF delta ∝ V_filler^(-1/4): d ln/d ln r_f = -1/2 ; d ln/d ln L = -1/4
ALL ASSERTIONS: True [True, True, True, True, True, True, True, True, True, True, True, True, True]
```

## Self-check of i1.html
- 29 ko / 29 en paragraphs, strictly ko→en order; card 13 rows; classes only from style.css; no internal ids/paths/model names; no .qc block.
- Caveats for critic: D1 assumes δ ∝ std at a fixed window (Gaussian-like tail); for exponential-tail single-trap amplitudes the far tail of a sum is dominated by single largest traps — mentioned only indirectly via the window effect. D4 mixes low-N explicit exponents with the N≥3 cube-root law — flagged as assumption in HTML.
