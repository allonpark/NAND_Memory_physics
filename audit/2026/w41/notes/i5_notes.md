# W41 item 5 — writer notes (Qiu et al., MPLB, DOI 10.1142/s0217984926502520)

Status: DRAFT section only. No repo writes, no push, no PR.

## Source access
- Crossref abstract re-fetched 2026-10-26 via https://api.crossref.org/works/10.1142/s0217984926502520 (read in full).
  Crossref: title, 4 authors (Song Qiu, Lumei Zhang, Lintao Shi, Kai Ou), issued = published-online = 2026-10-09, container Modern Physics Letters B.
- Publisher page: NOT re-checked by the writer. One attempt with curl (doi.org redirect + publisher status) was refused by the
  session permission classifier as possible bot-check circumvention; not retried, not worked around.
  The 403 and doi.org redirect in the HTML are attributed to the source-verification record.
- Body, figures, tables, supplementary: not read.

## Abstract facts used (SOURCE_REPORTED)
46 CV-TDDB tests; 1.2-kV 4H-SiC MOSFET bare dies; 37–40 V; BD = three consecutive samples |IG| >= 10 mA; 44 valid; Weibull on 42 devices at 38–40 V;
Q_BD = integral |IG| to t_BD; "Across these groups, beta_Q/beta_t ranges from 1.40 to 2.03"; bootstrap scale uncertainty smaller for Q_BD;
exp/power/inverse-voltage comparable; exponential kept only as finite-range empirical normalization; calibration 38–39.5 V gives k = 1.40 V^-1,
characteristic-scale ratio 8.75 -> 1.36; held-out 40 V prediction underestimates measured scale; criterion/integration sensitivity do not alter group-level
conclusions; "Q_eff is not an operating-life prediction law". AUTHOR_INTERPRETATION: post-TDDB I–V "support" persistent low-resistance conduction.

## What the shape ratio refers to
beta_Q / beta_t over "these groups" (the 38–40 V Weibull groups). Symbols are not defined in the abstract; read as Weibull shapes of Q_BD and t_BD.
Number of groups and grouping rule (per voltage?) not stated. Whether the 1.40–2.03 spread is per-level variation of beta_Q or beta_t: UNKNOWN.

## Framework derivations (labeled in HTML; not from the paper)
Script: i5_framework.py ; output: i5_framework_out.txt (sympy 1.14.0, Python 3.14.3, run with -I).
[1] ln Q = ln t + ln Ibar; log-variance proxy: beta_Q > beta_t iff Cov(lnI, lnt) < -Var(lnI)/2 (slope b < -1/2).
    Independent-Q model: ratio = sqrt(1 + 6 beta_Q^2 sigma^2/pi^2); fraction of Var(ln t) removed = 1 - 1/r^2 = 0.490 (r=1.40), 0.757 (r=2.03).
    MC check (beta_Q=4, sigma=0.25, N=20000, illustrative): MLE ratio 1.457 vs proxy 1.268 -> direction holds, magnitude approximate.
[2] n beta^2 Var(ln eta_hat) -> 1 + 6(1-gamma_E)^2/pi^2 = 1.1087; sd = 1.053/(beta sqrt n); sd_Q/sd_t = 0.714 (1.40), 0.493 (2.03).
[3] Collapse of Q_eff = w(V) Q_BD iff beta_Q const and w*eta_Q const (dF/dV = 0 verified). E-model+FN d2 lnQ/dE2 = -2(B+E)/E^3 < 0;
    1/E+FN: -2(B+E-G)/E^3; G=B -> Q_BD = tau0 A E^2. Exponential weight collapses only locally.
[4] Exponential model curvature 0 independent of offset Vx; power n/(V-Vx)^2; inverse 2Gp tox/(V-Vx)^3.
[5] Mid-range deviation/span: power eps/8, inverse eps/4; eps=2/39 -> 0.0064, 0.0128.
[6] Linear LS extrapolation error = a2[(x-cbar)^2 - s^2]; example 38,38.5,39,39.5 (spacing ASSUMED) at 40 V: 5 a2/4.
[7] Scale-ratio probe: 8.75/exp(1.40*1.5) = 1.071; 8.75/exp(1.40*2) = 0.532; neither = 1.36 -> definition UNKNOWN.
[8] Coax contrast: J(r0)/J(r1) = r1/r0 for conserved I' per unit length.

## Evidence grades used
Reported statistics C (abstract only); fluence-driven reading C (hypothesis, not claimed); framework C (conditional); VNAND transfer D.

## Archive comparison (origin/main only; b12b780)
W40 item 5 (Yan et al., SiC PWM TDDB, archive gap), W38 item 4 (Nakata & Sato, SiC AC-TDDB displacement current),
W37 item 5 (Cao et al., SiC DGS trap competition), W39 item 5 (Zhang et al., SiC dynamic diagnosis). No W41/W42 draft material used.
Extracted to _arch/ (local copies of origin/main index.html) via _arch_extract.py.

## Could not support / UNKNOWN
Q_eff definition (sign, reference V, applied to Q or scale); temperature; oxide thickness/field; planar vs trench gate (abstract silent — HTML treats
oxide with planar MOS framework and flags trench as UNKNOWN); levels and n per level; per-level beta and CIs; meaning of 8.75/1.36;
size of 40 V miss; why 2 trajectories invalid and 2 not in Weibull set; IG(t) shape; FA.

## Source inconsistencies / ambiguities noticed
1. Brief called the paper a "charge-based damage coordinate"; actual title is "Voltage-weighted effective charge as a statistical damage coordinate".
2. Brief said "say planar"; the abstract does not state planar vs trench. Kept as UNKNOWN with a planar-MOS framework.
3. Q_eff appears only in the final sentences without definition; link of k to Q_eff is inference from title and units.
4. The scale ratio 8.75 -> 1.36 cannot be reproduced from the simplest reading with k = 1.40 /V (see [7]).
5. k = 1.40 V^-1 and the lower end of beta_Q/beta_t = 1.40 share the same digits; presumably coincidental, not interpreted.
6. sources.yaml labels "post-TDDB I-V sweeps support ..." as SOURCE_REPORTED; HTML labels the "support" reading AUTHOR_INTERPRETATION.
7. Publisher 403 not independently re-verified by the writer (permission refusal); attributed to the source-verification record.

## Files
- i5.html (section id="i5"; lint: classes all in style.css, tags balanced, 88 <p> in strict ko/en pairs, card 13 rows) — _i5_lint.py
- i5_framework.py / i5_framework_out.txt
- _arch_extract.py, _arch/w37..w40.html (read-only copies from origin/main)
