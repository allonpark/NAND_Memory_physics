# S5 notes — W40 item 5 (ARCHIVE_GAP)

Source: Yan J., Cheng F., Luo X., Liu Y., Yang W., J. Phys. D: Appl. Phys. 59(37) 375105, DOI 10.1088/1361-6463/ae9c4e, published 2026-09-18, access abstract_only (Crossref abstract; body/publisher page not read).

## Selection / date check
- W40 window per sources.yaml header and task brief: 2026-09-28..2026-10-04. Published 2026-09-18, i.e. 10 days before the window start -> ARCHIVE_GAP, labelled as not new this week in s5.html.
- INCONSISTENCY: the sources.yaml S5 inline comment says "published 4 days before window start (2026-09-22)". That conflicts with the header (2026-09-28). Classification (archive gap) holds either way; the day count in the comment looks wrong. Not edited (read-only input).
- Crossref record created 2026-08-20 = metadata deposit date, not taken as the publication date.

## SOURCE_REPORTED claims (all = abstract; sentence positions not verifiable beyond "abstract", per sources.yaml)
1. Pulsed vs DC TDDB, three commercial 1.2 kV families (Wolfspeed C2M, C3M planar; Infineon trench), 150 C, DC to 100 kHz — [abstract]
2. Weibull characteristic lifetime rises monotonically with frequency; 100 kHz = 4.1x-4.7x DC across families — [abstract]
3. Differential-Vth trap time-constant spectroscopy: bimodal g(tau), fast cluster ~0.7 ms, slow shoulder 0.5-50 s — [abstract]
4. Quasi-permanent Vth drift ~30% lower under ms pulsing vs DC at 150 C; read by authors as fast-trap de-trapping in OFF — [abstract]
5. Authors call the trap/lifetime correlation empirical and bounding; field mismatch between spectroscopy and TDDB discussed — [abstract]

## UNKNOWN
Weibull beta and CI; sample size per family/frequency; stress field / VGS; ON/OFF levels (unipolar/bipolar, recovery bias); duty cycle; rise/fall time; failure criterion; whether lifetime is wall-clock or stress-time; which field model (E, 1/E, Q_BD) authors use; the frequency points between DC and 100 kHz and the size of increments; spectroscopy field level; per-family spread significance; whether the 30% drift is the same population that fails in TDDB.

## ENGINEERING_INFERENCE in s5.html (not from the paper)
- Causal chain last two links (fewer trapped charges -> fewer precursors -> longer eta) is hypothesis; sign/centroid of trapped charge could make trapping self-limiting instead.
- Duty-artifact equivalence (gain = 1/D for all three models) and D = 0.21-0.24 needed for full-artifact explanation of 4.1-4.7x IF wall-clock.
- Single-tau first-order kinetics: n_peak decreases with f toward D; period-average = D for tau_c = tau_e; tau = 0.7 ms gives f*tau = 7 (10 kHz) / 70 (100 kHz), n_peak 0.518 -> 0.502 at D = 0.5 (illustrative; tau_c = tau_e and D = 0.5 are assumptions, not paper values). Hence a strong monotonic rise above ~10 kHz is hard to attribute to the 0.7 ms cluster alone.
- Edge (C_ox dV/dt, overshoot) and thermal terms as competing mechanisms; bipolar boundary.
- DC-qualification "conservative only if mechanism-equivalent and unipolar".
- Comparisons with W37 item 5 (Cao et al., IEEE TED 73(4) 2076-2086, DOI 10.1109/TED.2026.3665857, SiC DGS temperature-dependent trap competition) and W39 item 5 (Zhang et al., IET PE 19(1) e70286, DOI 10.1049/pel2.70286, DC HTGB 150 C emulation for diD/dt diagnosis), read from repo reports/2026/w37 and w39 index.html.

## EXTRAPOLATION_ONLY
- NAND relevance (T05 WL-to-WL TDDB, T07 HV BTI): methodology only. SiC/SiO2 interface-trap physics not transferred to poly-Si/ONO or HV Si gate oxide. Coaxial formula given only for the radial VNAND stack, with conditions; WL-to-WL field flagged as edge-enhanced, needs geometry (T09).

## Weak points
- Abstract-only: cannot confirm duty, time accounting, beta -> the central "recovery vs duty artifact" question is open, and the inference (ii) depends on an assumed tau_c = tau_e and unknown duty.
- "Already known" paragraph (AC TDDB > DC in Si/high-k; SiC bipolar gate-switching instability) is background knowledge, no primary DOI re-checked this session; labelled so in HTML.
- sd(ln eta ratio) uses asymptotic complete-sample MLE variance 1.1087/(n beta^2) per eta; censoring would widen it.
- Grade "B-" in the card is my label (literature, body unread), not a CLAUDE.md grade level; caller may normalise to B or C.
- Hangul syllable count in s5.html: 1829 (target 1800-2800 Korean chars) — at the low end.

## Verification script (run with scratchpad/venv_sympy, sympy 1.14.0, Python 3.14.3; `python -I`)
```python
# S5 framework checks (NOT the paper's model). sympy symbolic verification.
import sympy as sp
D, f, t, tc, te, tau0, gam, G, E, QBD, A, B, n, beta = sp.symbols(
    'D f t tau_c tau_e tau0 gamma G E Q_BD A B n beta', positive=True)

# (1) Effective stress time, Miner linear damage accumulation for unipolar rectangular pulse
#     damage rate = 1/t_BD(E_on) during ON, 0 during OFF -> wall-clock lifetime = t_BD(E_on)/D
models = {
    'E-model':   tau0*sp.exp(-gam*E),
    '1/E-model': tau0*sp.exp(G/E),
    'Q_BD (FN J=A E^2 exp(-B/E))': QBD/(A*E**2*sp.exp(-B/E)),
}
Tw = sp.symbols('T_w', positive=True)
for name, tbd in models.items():
    # solve D*T_w / tbd = 1 for T_w
    sol = sp.solve(sp.Eq(D*Tw/tbd, 1), Tw)[0]
    print(f"[1] {name}: wall-clock t_BD = {sp.simplify(sol)} ; gain vs DC = {sp.simplify(sol/tbd)}")
print("[1] -> pure duty artifact gain = 1/D, identical for all three field models; gain is f-independent at fixed D.")
print("[1] duty needed for pure-artifact gain g: D = 1/g ->", sp.solve(sp.Eq(1/D, sp.Symbol('g', positive=True)), D))

# (2) Single trap class, first-order capture (ON, tau_c) / emission (OFF, tau_e), periodic steady state
ton, toff = D/f, (1-D)/f
a = sp.exp(-ton/tc); b = sp.exp(-toff/te)
x = sp.symbols('x')
# ON: x -> 1-(1-x)a ; OFF: x -> x b ; fixed point at end of OFF. Closed form in decaying exponentials:
nstar = (1-a)*b/(1-a*b)
print("[2] closed form n* = (1-a)b/(1-ab) satisfies fixed point?", sp.simplify((1-(1-nstar)*a)*b - nstar) == 0)
npeak = sp.simplify(1-(1-nstar)*a)          # = (1-a)/(1-ab)
print("[2] n_peak == (1-a)/(1-ab)?", sp.simplify(npeak-(1-a)/(1-a*b)) == 0)
# low-f limit: a,b -> 0 ; high-f limit: series in u=1/f -> 0
aa, bb = sp.symbols('a b', positive=True)
ns_ab = (1-aa)*bb/(1-aa*bb); np_ab = (1-aa)/(1-aa*bb)
print("[2] f->0 (a,b->0): n* ->", ns_ab.subs({aa:0, bb:0}), " n_peak ->", np_ab.subs({aa:0, bb:0}))
u = sp.symbols('u', positive=True)
k = sp.symbols('k', positive=True)  # D = 1/(1+k), 0<D<1
sub = {f: 1/u, D: 1/(1+k)}
ns_u = nstar.subs(sub); np_u = npeak.subs(sub)
lim_hi = sp.simplify(sp.limit(ns_u, u, 0, '+')); lim_hi_p = sp.simplify(sp.limit(np_u, u, 0, '+'))
quasi = ((D/tc)/(D/tc+(1-D)/te)).subs(D, 1/(1+k))
print("[2] f->inf: n* ->", lim_hi, "; n_peak ->", lim_hi_p)
print("[2] both equal quasi-static D/tau_c/(D/tau_c+(1-D)/tau_e)?",
      sp.simplify(lim_hi-quasi) == 0, sp.simplify(lim_hi_p-quasi) == 0)
fn = sp.lambdify((D, f, tc, te), nstar, 'math')
grid = [10.0**k_ for k_ in range(-3, 5)]
mono = all(fn(d, f2, 1.0, 1.0) >= fn(d, f1, 1.0, 1.0) - 1e-12
           for d in (0.2, 0.5, 0.8) for f1, f2 in zip(grid, grid[1:]))
print("[2] n* (end-of-OFF) non-decreasing in f on dimensionless grid (tau_c=tau_e=1)?", mono)
for d in (0.2, 0.5, 0.8):
    print("    D=%.1f  n*(f*tau=1e-2,1,1e2,1e4) =" % d, [round(fn(d, x_, 1.0, 1.0), 4) for x_ in (1e-2, 1.0, 1e2, 1e4)],
          " quasi-static =", round(d/(d+(1-d)), 4))
print("[2] -> single-tau first-order kinetics: per-cycle recovery benefit shrinks with f and saturates once f*tau >> 1;")
print("     a lifetime gain that keeps rising for f >> 1/tau needs a tau distribution, non-first-order physics, or a non-trap term.")
tau_fast = sp.Rational(7, 10)/1000
print("[2] abstract fast cluster tau~0.7 ms: 1/tau [Hz] =", sp.N(1/tau_fast, 4),
      "; at 100 kHz f*tau =", sp.N(100000*tau_fast, 3))

# (3) Planar MOS oxide-charge shift (SiC gate oxide; planar is appropriate for planar/trench SiO2 locally)
eps, tox, xb, Q = sp.symbols('epsilon_ox t_ox xbar Q', positive=True)
Cox = eps/tox
dV = -Q*xb/eps
print("[3] dV_FB sheet charge at centroid xbar (from gate) =", dV, " == -(Q/Cox)(xbar/tox)?",
      sp.simplify(dV + (Q/Cox)*(xb/tox)) == 0)

# (4) Weibull characteristic-life uncertainty (complete sample MLE, asymptotic): Var(ln eta) ~ 1.1087/(n beta^2)
# ratio of two independent eta's: Var(ln ratio) = 2*1.1087/(n beta^2) (equal n, beta)
var_ln_ratio = 2*sp.Float(1.1087)/(n*beta**2)
print("[4] sd(ln eta_ratio) =", sp.sqrt(var_ln_ratio), "-> unknown n, beta: CI of 4.1x-4.7x cannot be evaluated")

# (5) Coaxial field check (VNAND radial stack, analogy section only)
r, rin, rout, Qp, epsi = sp.symbols("r r_in r_out Qp epsilon_i", positive=True)
Er = Qp/(2*sp.pi*epsi*r)
print("[5] coaxial: integral E dr from r_in to r_out =", sp.simplify(sp.integrate(Er, (r, rin, rout))),
      " == Q'/(2 pi eps) ln(rout/rin)?",
      sp.simplify(sp.integrate(Er, (r, rin, rout)) - Qp/(2*sp.pi*epsi)*sp.log(rout/rin)) == 0)

# (6) peak and period-averaged occupancy vs f (which metric drives damage is UNKNOWN)
tt = sp.symbols('tt', positive=True)
npk = (1-a)/(1-a*b)   # explicit, numerically stable
xon = 1-(1-nstar)*sp.exp(-tt/tc); xoff = npk*sp.exp(-tt/te)
navg = (sp.integrate(xon, (tt, 0, ton)) + sp.integrate(xoff, (tt, 0, toff)))*f
fp = sp.lambdify((D, f, tc, te), npk, 'math'); fa = sp.lambdify((D, f, tc, te), navg, 'math')
grid = [10.0**k_ for k_ in range(-3, 5)]
print("[6] n_peak non-increasing in f (tau=1)?", all(fp(d, f2, 1., 1.) <= fp(d, f1, 1., 1.) + 1e-12
      for d in (0.2, 0.5, 0.8) for f1, f2 in zip(grid, grid[1:])))
for d in (0.2, 0.5, 0.8):
    print("    D=%.1f n_peak(f*tau=0.7,7,70)=" % d, [round(fp(d, x_, 1., 1.), 4) for x_ in (0.7, 7., 70.)],
          " n_avg(f*tau=0.01,0.7,7,70)=", [round(fa(d, x_, 1., 1.), 4) for x_ in (0.01, 0.7, 7., 70.)])
print("[6] f*tau=0.7,7,70 corresponds to 1,10,100 kHz for tau=0.7 ms (tau_c=tau_e assumed, illustrative).")
```

## Script output
```
[1] E-model: wall-clock t_BD = tau0*exp(-E*gamma)/D ; gain vs DC = 1/D
[1] 1/E-model: wall-clock t_BD = tau0*exp(G/E)/D ; gain vs DC = 1/D
[1] Q_BD (FN J=A E^2 exp(-B/E)): wall-clock t_BD = Q_BD*exp(B/E)/(A*D*E**2) ; gain vs DC = 1/D
[1] -> pure duty artifact gain = 1/D, identical for all three field models; gain is f-independent at fixed D.
[1] duty needed for pure-artifact gain g: D = 1/g -> [1/g]
[2] closed form n* = (1-a)b/(1-ab) satisfies fixed point? True
[2] n_peak == (1-a)/(1-ab)? True
[2] f->0 (a,b->0): n* -> 0  n_peak -> 1
[2] f->inf: n* -> tau_e/(k*tau_c + tau_e) ; n_peak -> tau_e/(k*tau_c + tau_e)
[2] both equal quasi-static D/tau_c/(D/tau_c+(1-D)/tau_e)? True True
[2] n* (end-of-OFF) non-decreasing in f on dimensionless grid (tau_c=tau_e=1)? True
    D=0.2  n*(f*tau=1e-2,1,1e2,1e4) = [0.0, 0.1289, 0.1992, 0.2]  quasi-static = 0.2
    D=0.5  n*(f*tau=1e-2,1,1e2,1e4) = [0.0, 0.3775, 0.4988, 0.5]  quasi-static = 0.5
    D=0.8  n*(f*tau=1e-2,1,1e2,1e4) = [0.0, 0.7132, 0.7992, 0.8]  quasi-static = 0.8
[2] -> single-tau first-order kinetics: per-cycle recovery benefit shrinks with f and saturates once f*tau >> 1;
     a lifetime gain that keeps rising for f >> 1/tau needs a tau distribution, non-first-order physics, or a non-trap term.
[2] abstract fast cluster tau~0.7 ms: 1/tau [Hz] = 1429. ; at 100 kHz f*tau = 70.0
[3] dV_FB sheet charge at centroid xbar (from gate) = -Q*xbar/epsilon_ox  == -(Q/Cox)(xbar/tox)? True
[4] sd(ln eta_ratio) = 1.4890936840911/(beta*sqrt(n)) -> unknown n, beta: CI of 4.1x-4.7x cannot be evaluated
[5] coaxial: integral E dr from r_in to r_out = log((r_out/r_in)**(Qp/(2*pi*epsilon_i)))  == Q'/(2 pi eps) ln(rout/rin)? True
[6] n_peak non-increasing in f (tau=1)? True
    D=0.2 n_peak(f*tau=0.7,7,70)= [0.3269, 0.2116, 0.2011]  n_avg(f*tau=0.01,0.7,7,70)= [0.2, 0.2, 0.2, 0.2]
    D=0.5 n_peak(f*tau=0.7,7,70)= [0.6713, 0.5178, 0.5018]  n_avg(f*tau=0.01,0.7,7,70)= [0.5, 0.5, 0.5, 0.5]
    D=0.8 n_peak(f*tau=0.7,7,70)= [0.8958, 0.8113, 0.8011]  n_avg(f*tau=0.01,0.7,7,70)= [0.8, 0.8, 0.8, 0.8]
[6] f*tau=0.7,7,70 corresponds to 1,10,100 kHz for tau=0.7 ms (tau_c=tau_e assumed, illustrative).
```
