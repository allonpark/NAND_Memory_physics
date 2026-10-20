# S3 notes — W40 (nand-physics-writer)

Source: Zhu, Wang, He, Eng. Res. Express 8(19) 195322 (2026), DOI 10.1088/2631-8695/aea754. Access: abstract_only.
Input used: sources.yaml S3 entry + header comments only. I did NOT re-fetch the abstract or body; all
"abstract" facts below are as recorded in sources.yaml (verified there via Crossref + doi.org + IOP page, 2026-10-19).

## 1. SOURCE_REPORTED claims (location = abstract, per sources.yaml; sentence position within abstract not recorded)
| # | Claim | Location |
|---|---|---|
| 1 | Silvaco Atlas + DYNASONOS charge-trapping model; varies trap density, tunnel-oxide thickness, poly-Si channel properties | abstract |
| 2 | Optimal trap density for P/E window ~3-5e19 cm^-3; window gain saturates beyond | abstract |
| 3 | Tunnel oxide 4-5 nm = best speed/retention trade-off | abstract |
| 4 | <=15% charge loss over 10 yr with optimized Al2O3 blocking oxide | abstract |
| 5 | Poly-Si grain-boundary traps drive Vth variability; grains >50 nm narrow the Vth distribution | abstract |
| 6 | Calibration against published P/E, retention, endurance data is claimed | abstract (which data: unknown) |
Metadata (publisher page via sources.yaml): received 15 Jul, revised 5 Sep, accepted 14 Sep, online 1 Oct 2026.

## 2. UNKNOWN items
- Simulated geometry: cylindrical/coaxial vs planar/2D cross-section (most important).
- Channel radius, core radius, CTL/BOX thicknesses, WL length/pitch, number of cells simulated (single cell vs string).
- Temperature(s), P/E pulse amplitude/width/waveform, ISPP or not, erase method.
- How the 10-yr number was obtained (time integration vs Arrhenius extrapolation), trap-energy distribution inputs.
- Which published data set was used for calibration, calibration error, endurance cycle count.
- Whether lateral CTL migration, TAT after cycling, GB-trap dynamics (RTN) are in the model.
- Definition of "charge loss" (% of stored charge vs % of window) and of Vth "distribution narrowing" metric.
- Whether CTL is SiN; Al2O3 "optimization" variable (thickness? permittivity? trap?).

## 3. Weak points of the source (for the reader)
- Simulation-only; grade B/C at best. Calibration not independently verifiable from abstract.
- Optimum locations (N_t band, TOX band, grain threshold) are the most geometry/calibration-sensitive outputs.
- 10-yr retention is an extrapolation; mechanism equivalence not shown.
- Single-cell TCAD (if so) cannot capture lateral migration or neighbor interference.
- Grain-size effect in TCAD depends on how GBs are placed (deterministic vs random); statistics of a tail need many instances.

## 4. My additions (ENGINEERING_INFERENCE, not from source)
- Ideal coaxial Gauss-law analysis (below): g0 = E_coax(r0)/E_planar > 1, grows with kappa; gate-side field < planar.
- Exact identity: with stored sheet charge at TOX/CTL interface, gate+channel grounded, equal dVth,
  retention-field enhancement at r0 == program-field enhancement g0. So the optimum shift comes from
  differing field sensitivity (FN: dlnJ/dlnE = 2 + B/E) vs low-field retention paths. Direction: thicker TOX
  admissible in coax IF retention is weakly field-sensitive; may weaken/reverse for field-sensitive TAT.
  Magnitude NOT estimated (depends on unknown kappa, a, b).
- TOX/CTL-side (r1) first-order coefficient sign is geometry dependent: negative iff a^2 e_b + 2ab e_n + b^2 e_n < e_b e_n.
- Grain percolation / RTN framing: inference only.

## 5. SymPy derivation
Environment: Python 3.14 (C:\Python314) venv in scratchpad/venv_sympy, sympy==1.14.0 (pinned). Run with `python -I`.
Non-dimensional: lengths / t_TOX, permittivities / eps_TOX; kappa = t_TOX/r0, a = t_CTL/t_TOX, b = t_BOX/t_TOX,
e_n = eps_CTL/eps_TOX, e_b = eps_BOX/eps_TOX. No product dimensions used.
Script also saved as scratchpad/w40/sections/s3_coax.py (output: s3_coax_out.txt).

### Script
```python
# S3 (W40) coaxial vs planar field comparison -- symbolic, non-dimensional.
# Ideal coaxial stack: channel surface r0 | TOX | CTL | BOX | gate.
# Lengths normalized by t_tox; permittivities normalized by eps_ox(TOX).
# kappa = t_tox / r0 (curvature, dimensionless). a = t_ctl/t_tox, b = t_box/t_tox.
# en = eps_ctl/eps_tox, eb = eps_box/eps_tox. No product dimensions are used.
import sympy as sp

k, a, b, en, eb, x = sp.symbols('kappa a b e_n e_b x', positive=True)
V, Qs = sp.symbols('V Q', positive=True)

# radii in units of t_tox
r0 = 1/k
r1 = r0 + 1
r2 = r1 + a
r3 = r2 + b

# --- 1. single layer: E(r0)/(V/t) ---
x_ = sp.Symbol('x', positive=True)          # x = t/r0
f1 = x_/sp.log(1+x_)
print("[1] single-layer E(r_in)/(V/t) =", f1)
print("    series in x:", sp.series(f1, x_, 0, 4))
print("    E(r_out)/(V/t) =", sp.simplify(x_/((1+x_)*sp.log(1+x_))),
      " series:", sp.series(x_/((1+x_)*sp.log(1+x_)), x_, 0, 3))
d = sp.diff(f1, x_)
print("    d/dx of E(r_in) ratio =", sp.simplify(d))
print("    numerical sign check at x=0.1,0.5,1,3:",
      [sp.N(d.subs(x_, v), 4) for v in (0.1, 0.5, 1, 3)])

# --- 2. three-layer stack, program field (applied V, no stored charge) ---
S_lin = 1 + a/en + b/eb                          # planar sum t_i/eps_i (units t_tox/eps_tox)
S_log = sp.log(r1/r0) + sp.log(r2/r1)/en + sp.log(r3/r2)/eb
E_pl = V/S_lin                                   # planar TOX field (uniform)
E_r0 = V/(r0*S_log)                              # coax E at channel/TOX interface
E_r1 = V/(r1*S_log)                              # coax E at TOX/CTL interface
E_r3 = V/(eb*r3*S_log)                           # coax E in BOX at gate interface
E_pl_box = V/(eb*S_lin)
R_prog_r0 = sp.simplify(E_r0/E_pl)
R_prog_r1 = sp.simplify(E_r1/E_pl)
R_gate = sp.simplify(E_r3/E_pl_box)
s_r0 = sp.series(R_prog_r0, k, 0, 2).removeO()
s_r1 = sp.series(R_prog_r1, k, 0, 2).removeO()
s_g = sp.series(R_gate, k, 0, 2).removeO()
print("\n[2] program field ratio coax/planar, first order in kappa")
print("    at channel/TOX (r0):", sp.factor(sp.simplify(s_r0 - 1)), "(+1)")
print("    at TOX/CTL    (r1):", sp.factor(sp.simplify(s_r1 - 1)), "(+1)")
print("    at BOX/gate   (r3):", sp.factor(sp.simplify(s_g - 1)), "(+1)")

# --- 3. retention: stored sheet charge at TOX/CTL interface (r1), gate & channel at 0,
#        normalized to the SAME Vth shift dV (charge-to-gate capacitance).
C_in = 1/sp.log(r1/r0)                                   # 2*pi*eps_ox factored out
C_out = 1/(sp.log(r2/r1)/en + sp.log(r3/r2)/eb)
dV = sp.Symbol('dV', positive=True)
Q = dV*C_out                                             # Q'/(2 pi eps_ox) at fixed dVth
Q_in = Q*C_in/(C_in+C_out)
Eret_r0 = Q_in/r0
Eret_r1 = Q_in/r1
# planar: per-area caps 1/t
c_in, c_out = 1, 1/(a/en + b/eb)
Eret_pl = dV*c_out*c_in/(c_in+c_out)
R_ret_r0 = sp.series(sp.simplify(Eret_r0/Eret_pl), k, 0, 2).removeO()
R_ret_r1 = sp.series(sp.simplify(Eret_r1/Eret_pl), k, 0, 2).removeO()
print("\n[3] retention field ratio coax/planar at fixed dVth, first order in kappa")
print("    at r0:", sp.factor(sp.simplify(R_ret_r0 - 1)), "(+1)")
print("    at r1:", sp.factor(sp.simplify(R_ret_r1 - 1)), "(+1)")

# --- 4. differential: does curvature enhance program field more than retention field?
diff_r0 = sp.factor(sp.simplify((s_r0 - 1) - (R_ret_r0 - 1)))
print("\n[4] (program enhancement) - (retention enhancement) at r0, O(kappa):", diff_r0)
# sign check on generic positive values (symbols, not product values)
import itertools
vals = [0.5, 1, 2, 4]
signs = set()
for A, B, EN, EB in itertools.product(vals, vals, [1, 2], [1, 2.5]):
    signs.add(sp.sign(sp.N(diff_r0.subs({a: A, b: B, en: EN, eb: EB, k: 1}))))
print("    sign over grid a,b in {0.5,1,2,4}, en in {1,2}, eb in {1,2.5}:", signs)

# exact (not series) identity check
exact = sp.simplify(Eret_r0/Eret_pl - (E_r0/E_pl).subs(V, 1))
print("    exact identity  (Eret/Eret_pl) - (Eprog/Eprog_pl) at r0 =", exact)
# sign of first-order coefficient at r1 (TOX/CTL side): geometry dependent?
c_r1 = sp.factor(sp.simplify((s_r1 - 1)/k))
signs1 = set()
for A, B, EN, EB in itertools.product([0.25, 0.5, 1, 2, 4], [0.25, 0.5, 1, 2, 4], [1, 2], [1, 2.5]):
    signs1.add(sp.sign(sp.N(c_r1.subs({a: A, b: B, en: EN, eb: EB}))))
print("    r1 coefficient signs over grid:", signs1)
print("    r1 coefficient < 0  <=>  a^2 e_b + 2ab e_n + b^2 e_n < e_b e_n")

# --- 5. TOX thickness bound for a field-limited program-speed target E* at fixed V.
#        planar single-layer-equivalent: t_max = V/E*; coax single layer: x/ln(1+x) solved.
print("\n[5] single-layer: coax field at fixed V and t exceeds planar by factor x/ln(1+x)>1,")
print("    so for fixed E* the admissible t is larger in coax (direction: thicker).")
print("    exact check x=0.2:", sp.N(f1.subs(x_, 0.2), 5), " x=1:", sp.N(f1.subs(x_, 1), 5))
```

### Output (verbatim)
```
[1] single-layer E(r_in)/(V/t) = x/log(x + 1)
    series in x: 1 + x/2 - x**2/12 + x**3/24 + O(x**4)
    E(r_out)/(V/t) = x/((x + 1)*log(x + 1))  series: 1 - x/2 + 5*x**2/12 + O(x**3)
    d/dx of E(r_in) ratio = (-x + (x + 1)*log(x + 1))/((x + 1)*log(x + 1)**2)
    numerical sign check at x=0.1,0.5,1,3: [0.4845, 0.4388, 0.4020, 0.3311]

[2] program field ratio coax/planar, first order in kappa
    at channel/TOX (r0): kappa*(a**2*e_b + 2*a*b*e_n + 2*a*e_b + b**2*e_n + 2*b*e_n + e_b*e_n)/(2*(a*e_b + b*e_n + e_b*e_n)) (+1)
    at TOX/CTL    (r1): kappa*(a**2*e_b + 2*a*b*e_n + b**2*e_n - e_b*e_n)/(2*(a*e_b + b*e_n + e_b*e_n)) (+1)
    at BOX/gate   (r3): -kappa*(a**2*e_b + 2*a*b*e_b + 2*a*e_b*e_n + b**2*e_n + 2*b*e_b*e_n + e_b*e_n)/(2*(a*e_b + b*e_n + e_b*e_n)) (+1)

[3] retention field ratio coax/planar at fixed dVth, first order in kappa
    at r0: kappa*(a**2*e_b + 2*a*b*e_n + 2*a*e_b + b**2*e_n + 2*b*e_n + e_b*e_n)/(2*(a*e_b + b*e_n + e_b*e_n)) (+1)
    at r1: kappa*(a**2*e_b + 2*a*b*e_n + b**2*e_n - e_b*e_n)/(2*(a*e_b + b*e_n + e_b*e_n)) (+1)

[4] (program enhancement) - (retention enhancement) at r0, O(kappa): 0
    sign over grid a,b in {0.5,1,2,4}, en in {1,2}, eb in {1,2.5}: {0}
    exact identity  (Eret/Eret_pl) - (Eprog/Eprog_pl) at r0 = 0
    r1 coefficient signs over grid: {0, 1, -1}
    r1 coefficient < 0  <=>  a^2 e_b + 2ab e_n + b^2 e_n < e_b e_n

[5] single-layer: coax field at fixed V and t exceeds planar by factor x/ln(1+x)>1,
    so for fixed E* the admissible t is larger in coax (direction: thicker).
    exact check x=0.2: 1.0970  x=1: 1.4427
```

### Reading of the output
- [1] single layer: E(r_in)/(V/t) = x/ln(1+x) = 1 + x/2 - x^2/12 + ...; derivative positive at sampled x -> enhancement grows with t/r0.
  Outer surface: x/((1+x)ln(1+x)) = 1 - x/2 + ... < 1.
- [2] three-layer first-order coefficients: r0 positive for all positive params (all terms positive);
  r3 (gate) negative; r1 sign-indefinite.
- [3]/[4] retention at fixed dVth reproduces exactly the program enhancement at r0 (exact identity = 0).
- [5] The x=0.2, x=1 values are evaluations of the math function only, not product geometry; not used in the HTML.

## 6. Validity limits of the ideal formula (also in HTML)
Volume (not sheet) CTL charge with moving centroid; interface charge / Vfb; axial fringing (finite WL, spacer);
finite WL pitch neighbor coupling; poly-Si depletion & surface potential (channel not a metal); GB potential barriers;
non-circular, tapered holes (kappa distributed along string). Retention case also assumes both electrodes grounded.

## 7. Output stats
s3.html: 11 ko/en paragraph pairs (each <p lang=ko> immediately followed by <p lang=en>), all classes exist in assets/style.css,
tags balanced. Korean paragraphs: ~1530 Hangul syllables (~4400 chars incl. symbols/spaces/Latin terms).
No figures; no numbers beyond the abstract facts.
