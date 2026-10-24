# Item 2 notes — W43 (nand-physics-writer)

Source: Cheng W., Zheng H., Song W., Cattani P., "Reliability Analysis of Isolation Structures for Integrated Circuits Based on the Beta Generalized Weibull Distribution", Fractal and Fractional 10(10) 728 (MDPI, CC BY 4.0), DOI 10.3390/fractalfract10100728, published online 2026-10-19. Access: abstract_only.

## Inputs actually used
- sources.yaml: header comments + this item's entry only.
- Crossref REST `works/10.3390/fractalfract10100728` re-fetched 2026-10-21 in this session: full abstract (JATS), title, authors + affiliations (Minnan Univ. of Sci. & Tech.; Shanghai Univ. of Eng. Sci.; Sapienza Rome), published 2026-10-19, license CC BY 4.0 (vor + tdm), reference-count 0.
- Did NOT open MDPI pages (sources.yaml records HTTP 403; no bypass attempted). doi.org redirect is taken from the sources.yaml record, not re-checked by me; HTML says so.
- Archive comparison: origin/main reports/2026/w37, w38, w39 index.html and origin/weekly/2026-w40 reports/2026/w40/index.html in the nand-audit clone (read-only `git show`). Used: W38 item 3 (polarity β change as population signature), W39 item 1 (Wu & Ando area scaling / annihilation), W40 item 2 (bimodal extrinsic/intrinsic Weibull expectation), W40 item 5 (equal β requirement; duty = 1/D under Miner). No W41/W42/W43 branch material used.

## SOURCE_REPORTED (all from the Crossref abstract; sentence-level only, no figure/eq numbers available)
1. Two problems: describe TTF distribution; obtain TTF distribution under actual working conditions (AWCs).
2. Five-parameter BGW; represents IFR, DFR, CFR, BFR (bathtub), UBT.
3. Hazard-derivative sign via Glaser eta-function theorem + origin/infinity asymptotics; "exact, necessary-and-sufficient" conditions; origin controlled by product aγω, tail by γ.
4. BGW-based TTF model for AWCs; "proved analytically" that a stress change affects only scale Δ, all shape parameters unchanged.
5. Invariance "previously stated as an assumption"; verified empirically on TDDB data with (i) per-level Weibull shape estimates + bootstrap CIs, (ii) Kruskal–Wallis on standardized failure times, (iii) parametric-bootstrap LRT within BGW; all three "support" stress-invariant shapes.
6. Reliability function recast as convergent infinite series, "correct beta-integral kernel", explicit ratio-test bound.
7. Effectiveness and superiority verified on TDDB TTF data (-> labelled AUTHOR_INTERPRETATION in HTML: evaluative, comparator/criterion unknown).
8. Untested 3800 V condition predicted from fitted linear voltage-acceleration model.

## UNKNOWN
Structure type, dielectric material/thickness/geometry, voltage levels and count, temperature, n per level, censoring, failure criterion, data origin (own vs literature), fifth parameter's name (abstract names a, γ, ω, Δ only; b presumed), exact base G, functional form of the "linear voltage-acceleration" model, standardization for KW, whether 3800 V is inside or outside the tested range, test statistics/p-values/CIs, comparator for "superiority", whether FA was done.

## ENGINEERING_INFERENCE / background in i2.html (not from the paper)
- Beta-G construction and BGW/Beta-Weibull literature existence: background, primary sources not re-checked (labelled).
- Parametrization G = [1 − exp(−(t/Δ)^γ)]^ω (exponentiated Weibull base): chosen because it reproduces the abstract's "origin aγω / tail γ" statements; mapping is a hypothesis.
- "Analytic proof" of scale-only invariance looks structural (automatic once stress is put only in Δ) — inference; proof text unseen.
- Mixture with equal acceleration passes any shape-invariance test; unequal acceleration gives drifting apparent shape (illustrative numbers 1.46/1.73/2.25 — NOT paper values).
- Competing risks DFR+IFR → bathtub; exponential mixtures → DFR.
- Weibull MLE asymptotics: n Var(β̂) = 6β²/π² ≈ 0.608 β²; sd(ln β̂) ≈ 0.78/√n; two-level diff ≈ 1.10/√n; MDE at 5%/80% ≈ 3.09/√n → ratios 2.66/1.76/1.36 at n = 10/30/100 (illustrative n). 50%-power variants (2.16/√n; 1.98/1.48/1.24) computed but not used in HTML.
- KW mainly location-sensitive → low power vs shape after scale standardization (inference; standardization unknown).
- BGW weakest-link area conversion not a pure Δ shift (counterexample a=2,b=1,m=2; Δ needed 0.778 at x=0.3 vs 0.682 at x=2, λ=1 units).
- 3800 V "may point to kV-class isolation": inference, labelled.
- Low-stress mechanism switch (extrinsic / trapping) as competing explanation: hypothesis.
- NAND relevance: methodology only (T05 model selection + Weibull uncertainty, P1 backlog); coaxial field formula with conditions; WL-to-WL edge enhancement flagged for T09.

## Evidence grades used
- Paper's statistical claims: C (abstract only; data/proofs unseen) — abstract-only so not A/B.
- Mechanism equivalence: not established; whether paper addresses it UNKNOWN (no grade assigned to a claim the paper may not make).
- Framework sympy checks: described as "calculation under an assumed parametrization, not verification of the paper" (deliberately not given a letter grade for the paper; if the caller wants one, B for the math identities themselves is defensible, but they do not verify the paper).
- VNAND transfer: D.

## Source inconsistencies / tensions noticed
1. Abstract says invariance is "proved analytically" AND that it "was previously stated as an assumption" and therefore is "verified empirically" — if proved, no empirical check would be needed; consistent only if the proof is conditional on putting stress in Δ alone (which is the assumption). Flagged in HTML as inference.
2. "Five-parameter" but abstract names only four symbols (a, γ, ω, Δ).
3. sources.yaml fact list says "bathtub"; abstract acronym is BFR — same thing, no conflict.
4. Crossref reference-count 0 (no reference list deposited) — cannot check which prior BGW work the "correct beta-integral kernel" remark corrects.
5. Journal scope (fractal/fractional calculus) vs. content: no fractional element visible in the abstract — not an error, just noted; not mentioned in HTML.
6. sources.yaml why_fits/warnings consistent with abstract; no date conflict (2026-10-19 inside W43 window 2026-10-19..25).

## Weak points
- Everything about the paper's data is UNKNOWN; the critique of KW and of "proof" is necessarily conditional.
- The necessary-and-sufficient conditions were not verified, only asymptotics + examples consistent with them.
- Censoring effect described qualitatively (background), not derived.
- Hangul syllable count of i2.html: 4598.

## Verification script (venv_sympy: sympy 1.14.0, mpmath 1.3.0, Python 3.14.3; run with `python -I`; exit 0)
Script and output were run as i2_bgw.py / i2_bgw_out.txt in this folder and are reproduced below; the separate files were then removed so that only i2.html and i2_notes.md remain for this item.

```python
# Item 2 (W43) framework checks for a Beta-G / Beta generalized Weibull construction.
# NOT the paper's model: the paper's exact parametrization is unknown (abstract only).
# Assumed construction (background, literature-standard Beta-G): F(x) = I_{G(x)}(a, b),
# with base G = exponentiated Weibull G(x) = (1 - exp(-(x/lam)^k))^alpha.
# Mapping to the abstract's symbols (gamma ~ k, omega ~ alpha, Delta ~ lam) is a HYPOTHESIS.
import sys
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp
import mpmath as mp

x, a, b, al, k, lam, u = sp.symbols('x a b alpha k lam u', positive=True)

def G_expr(x, al, k, lam):
    return (1 - sp.exp(-(x/lam)**k))**al

# ---------------------------------------------------------------- [1] nested special cases
print("[1] nested special cases of F = I_G(a,b)")
# Regularized incomplete beta I_u(a,b) = (1/B(a,b)) int_0^u t^(a-1)(1-t)^(b-1) dt
t = sp.symbols('t', positive=True)
def I(uu, aa, bb):
    return sp.integrate(t**(aa-1)*(1-t)**(bb-1), (t, 0, uu)) / sp.beta(aa, bb)
print("  I_u(1,1) =", sp.simplify(I(u, 1, 1)), "-> a=b=1 gives F=G (exponentiated Weibull)")
Ia1 = sp.simplify(I(u, a, 1))
print("  I_u(a,1) =", Ia1, "-> b=1 gives F=G^a = (1-e^{-(x/lam)^k})^(a*alpha): a and alpha enter only as the product a*alpha (not separately identifiable)")
I1b = sp.simplify(I(u, 1, b))
print("  I_u(1,b) =", I1b, "-> a=1 gives F = 1-(1-G)^b")
W = 1 - sp.exp(-(x/lam)**k)
print("  a=b=alpha=1: F =", W, "(2-parameter Weibull)")
print("  alpha=1 gives Beta-Weibull; k=1 gives a beta exponentiated-exponential (by substitution)")

# ---------------------------------------------------------------- [2] origin asymptotics
print("\n[2] origin: G ~ (x/lam)^(k*alpha), F ~ G^a/(a B(a,b)) -> F ~ C x^(a*alpha*k), h ~ x^(a*alpha*k - 1)")
Gs = sp.series((1 - sp.exp(-u))**al, u, 0, 2).removeO()
print("  (1-e^{-u})^alpha near u=0, leading term:", sp.simplify(sp.limit((1 - sp.exp(-u))**al / u**al, u, 0)), "* u^alpha")
lead = sp.limit(I(u, a, b).subs({a: 2, b: 3}) / u**2, u, 0)
print("  check I_u(2,3)/u^2 -> 1/(a B(a,b)) =", lead, "vs", sp.Rational(1, 1)/(2*sp.beta(2, 3)))

mp.mp.dps = 60
def F_num(xv, A, Bp, Al, K, L=1):
    g = (1 - mp.e**(-(mp.mpf(xv)/L)**K))**Al
    return mp.betainc(A, Bp, 0, g, regularized=True)
def S_num(xv, A, Bp, Al, K, L=1):
    w = (mp.mpf(xv)/L)**K
    one_minus_g = -mp.expm1(Al*mp.log1p(-mp.e**(-w)))   # 1-G without cancellation
    return mp.betainc(Bp, A, 0, one_minus_g, regularized=True)   # S = I_{1-G}(b,a)
def h_num(xv, A, Bp, Al, K, L=1):
    f = mp.diff(lambda z: F_num(z, A, Bp, Al, K, L), xv)
    return f / S_num(xv, A, Bp, Al, K, L)

def loglog_slope(fun, x1, x2):
    return (mp.log(fun(x2)) - mp.log(fun(x1))) / (mp.log(x2) - mp.log(x1))

for (A, Bp, Al, K) in [(2, 3, mp.mpf('0.5'), mp.mpf('0.8')), (mp.mpf('0.5'), 2, 1, mp.mpf('1.5')), (3, 1, 2, mp.mpf('0.6'))]:
    s = loglog_slope(lambda z: h_num(z, A, Bp, Al, K), mp.mpf('1e-8'), mp.mpf('1e-7'))
    print(f"  a={A}, b={Bp}, alpha={Al}, k={K}: numeric dlog h/dlog x near 0 = {mp.nstr(s, 6)}, predicted a*alpha*k-1 = {mp.nstr(A*Al*K-1, 6)}")

# ---------------------------------------------------------------- [3] tail asymptotics
print("\n[3] tail: 1-G ~ alpha e^{-(x/lam)^k}, S = I_{1-G}(b,a) ~ C (1-G)^b -> h ~ b k x^(k-1)/lam^k")
for (A, Bp, Al, K) in [(2, 3, mp.mpf('0.5'), mp.mpf('0.8')), (mp.mpf('0.5'), 2, 1, mp.mpf('1.5'))]:
    xv = mp.mpf(30) if K < 1 else mp.mpf(6)
    hn = h_num(xv, A, Bp, Al, K)
    pred = Bp*K*xv**(K-1)
    print(f"  a={A}, b={Bp}, alpha={Al}, k={K}: h({xv}) numeric = {mp.nstr(hn, 8)}, tail law b k x^(k-1) = {mp.nstr(pred, 8)}, ratio = {mp.nstr(hn/pred, 6)}")
print("  -> tail rising iff k>1, falling iff k<1, constant iff k=1 (tail controlled by k only, b sets the level)")

# ---------------------------------------------------------------- [4] example hazard shapes
print("\n[4] example shapes (sign changes of dh/dx on a log grid; illustrative parameter sets, not fitted values)")
def shape(A, Bp, Al, K):
    xs = [mp.mpf(10)**(mp.mpf(e)/10) for e in range(-30, 11)]
    hs = [h_num(z, A, Bp, Al, K) for z in xs]
    d = [0 if abs(hs[i+1]/hs[i]-1) < mp.mpf('1e-15') else (1 if hs[i+1] > hs[i] else -1) for i in range(len(hs)-1)]
    if all(v == 0 for v in d):
        return '0 (flat)'
    d = [v for v in d if v != 0]
    ch = [d[0]] + [d[i] for i in range(1, len(d)) if d[i] != d[i-1]]
    return ''.join('+' if c > 0 else '-' for c in ch)
cases = {
    'IFR  (a*alpha*k>1, k>1)': (2, 1, 1, mp.mpf('1.5')),
    'DFR  (a*alpha*k<1, k<1)': (mp.mpf('0.5'), 1, 1, mp.mpf('0.7')),
    'CFR  (a=b=alpha=k=1)': (1, 1, 1, 1),
    'BT   (a*alpha*k<1, k>1)': (mp.mpf('0.3'), 1, 1, mp.mpf('2')),
    'UBT  (a*alpha*k>1, k<1)': (4, 1, 1, mp.mpf('0.6')),
}
for nm, p in cases.items():
    print(f"  {nm}: params a,b,alpha,k = {[mp.nstr(v,3) for v in p]}: monotonic pattern of h = {shape(*p)}")
print("  ('+' rising, '-' falling; '-+' = bathtub, '+-' = upside-down bathtub). CFR case: h constant, numerically flat.")

# ---------------------------------------------------------------- [5] scale-only stress dependence
print("\n[5] if stress enters only via the scale lam(S): F(t;S) = H((t/lam(S)))")
H = sp.Function('H')
l1, l2 = sp.symbols('lam1 lam2', positive=True)
lhs = H(x/l2)
rhs = H((x*l1/l2)/l1)
print("  F(t;lam2) == F(t*lam1/lam2; lam1):", sp.simplify(lhs - rhs) == 0)
print("  -> every quantile ratio t_p(S1)/t_p(S2) = lam1/lam2 for all p; log-times shift by a constant;")
print("     shape invariance is built in once stress is placed only in lam (it is a modeling choice, testable, not a physics result)")

# ---------------------------------------------------------------- [6] two mechanisms that pass a shape-invariance test
print("\n[6] two-mechanism mixture with EQUAL acceleration is still a pure scale family")
p, b1, b2, e1, e2, c, V = sp.symbols('p beta1 beta2 eta1 eta2 c V', positive=True)
def Fmix(tt, AF):
    return p*(1 - sp.exp(-(tt/(e1/AF))**b1)) + (1-p)*(1 - sp.exp(-(tt/(e2/AF))**b2))
AF = sp.exp(c*V)
print("  Fmix(t; AF) == Fmix(t*AF; 1):", sp.simplify(Fmix(x, AF) - Fmix(x*AF, 1)) == 0)
print("  -> two physically different subpopulations with equal voltage acceleration pass every shape-invariance test;")
print("     invariance cannot prove a single mechanism.")
# unequal acceleration: shape of mixture changes with stress
c1, c2 = sp.symbols('c1 c2', positive=True)
Fm2 = lambda tt, VV: p*(1 - sp.exp(-(tt*sp.exp(c1*VV)/e1)**b1)) + (1-p)*(1 - sp.exp(-(tt*sp.exp(c2*VV)/e2)**b2))
vals = {p: sp.Rational(3, 10), b1: sp.Rational(1, 1), b2: 3, e1: 1, e2: 10, c1: 1, c2: 2}
# compare Weibull-plot slope d ln(-ln(1-F))/d ln t at the median of each stress level
def wslope_at_median(VV):
    f = sp.lambdify(x, Fm2(x, VV).subs(vals), 'mpmath')
    lt = mp.findroot(lambda y: f(mp.e**y) - mp.mpf('0.5'), (mp.mpf(-20), mp.mpf(10)), solver='illinois')
    tm = mp.e**lt
    g = lambda z: mp.log(-mp.log(1 - f(mp.e**z)))
    return mp.diff(g, mp.log(tm))
print("  unequal acceleration (c1 != c2), illustrative values:", {str(kk): str(vv) for kk, vv in vals.items()})
for VV in [0, 1, 2]:
    print(f"    V={VV}: Weibull-plot slope at median = {mp.nstr(wslope_at_median(VV), 6)}")
print("  -> with unequal acceleration the apparent shape drifts with stress; detectability depends on n and censoring.")

# ---------------------------------------------------------------- [7] competing risks mimic bathtub
print("\n[7] competing risks: series system of DFR (beta1<1) and IFR (beta2>1) Weibull mechanisms")
h = (b1/e1)*(x/e1)**(b1-1) + (b2/e2)*(x/e2)**(b2-1)
dh = sp.diff(h, x)
crit = sp.solve(sp.Eq(dh, 0), x)
print("  h(t) = h1 + h2; stationary point(s):", crit)
num = {b1: sp.Rational(1, 2), b2: 3, e1: 100, e2: 10}
hn = h.subs(num); dhn = sp.diff(hn, x)
tstar = sp.nsolve(dhn, x, 3)
print("  example beta1=1/2, beta2=3, eta1=100, eta2=10: t* =", sp.N(tstar, 6),
      "; dh/dt at t*/2 =", sp.N(dhn.subs(x, tstar/2), 4), "; at 2t* =", sp.N(dhn.subs(x, 2*tstar), 4), "-> bathtub")
print("  -> a single flexible-family fit showing BT can be two physical mechanisms in competition.")
# mixture of two exponentials -> DFR
l_1, l_2, q = sp.symbols('l_1 l_2 q', positive=True)
Sm = q*sp.exp(-l_1*x) + (1-q)*sp.exp(-l_2*x)
hm = -sp.diff(Sm, x)/Sm
dhm = sp.simplify(sp.diff(hm, x))
print("  mixture of exponentials: dh/dt =", sp.factor(dhm), " (always <= 0: CFR components mix into DFR)")

# ---------------------------------------------------------------- [8] Weibull MLE shape uncertainty (complete sample)
print("\n[8] Weibull (complete sample) Fisher information, per observation, in (beta, eta)")
z = sp.symbols('z', positive=True)
bb, ee = sp.symbols('beta eta', positive=True)
logf = sp.log(bb/ee) + (bb-1)*sp.log(x/ee) - (x/ee)**bb
Hs = sp.hessian(logf, (bb, ee))
# expectation under Weibull: substitute x = ee*z^(1/bb), z ~ Exp(1)
def Ex(expr):
    e = sp.simplify(expr.subs(x, ee*z**(1/bb)))
    return sp.simplify(sp.integrate(e*sp.exp(-z), (z, 0, sp.oo)))
Info = -sp.Matrix(2, 2, lambda i, j: Ex(Hs[i, j]))
Info = sp.simplify(Info)
print("  I =", Info)
Cov = sp.simplify(Info.inv())
vb = sp.simplify(Cov[0, 0])
print("  n*Var(beta_hat) =", vb, "=", sp.N(vb/bb**2, 6), "* beta^2")
print("  n*Var(ln beta_hat) ~", sp.N(vb/bb**2, 6), " -> sd(ln beta_hat) ~", sp.N(sp.sqrt(vb/bb**2), 5), "/sqrt(n)")
n = sp.symbols('n', positive=True)
sd_diff = sp.sqrt(2*vb/bb**2/n)
print("  two levels, equal n: sd(ln beta1_hat - ln beta2_hat) =", sp.N(sp.sqrt(2*vb/bb**2), 5), "/sqrt(n)")
for zz, lab in [(sp.Rational(196, 100), 'z=1.96 (5% two-sided, 50% power)'), (sp.Rational(196, 100) + sp.Rational(84, 100), 'z=1.96+0.84 (80% power)')]:
    print(f"  minimum detectable |ln(beta1/beta2)| at {lab}: {sp.N(zz*sp.sqrt(2*vb/bb**2), 5)}/sqrt(n)")
    for nn in [10, 30, 100]:
        md = sp.N(zz*sp.sqrt(2*vb/bb**2/nn), 4)
        print(f"     n={nn}: |ln ratio| >= {md}  (ratio >= {sp.N(sp.exp(md), 4)})")
print("  (asymptotic, complete samples; censoring and small n make these wider; illustrative n only)")

# ---------------------------------------------------------------- [9] weakest-link area scaling inside / outside the family
print("\n[9] weakest-link area scaling S_m = S^m")
m = sp.symbols('m', positive=True)
Sw = sp.exp(-(x/lam)**k)
print("  Weibull: S^m == Weibull with eta*m^(-1/k):", sp.simplify(Sw**m - sp.exp(-(x/(lam*m**(-1/k)))**k)) == 0)
# BGW counterexample: a=2,b=1 vs a=2,b=2 on the same base G (u = G)
S_a2b1 = 1 - u**2
lhsA = sp.expand(S_a2b1**2)
S_a2b2 = sp.expand(1 - I(u, 2, 2))
print("  BGW a=2,b=1, m=2: S^2 =", sp.factor(lhsA), "; BGW a=2,b=2 survival =", sp.factor(S_a2b2), "; equal:", sp.simplify(lhsA - S_a2b2) == 0)
# not a pure scale shift either: test whether exists lam' with S(x;lam')^... using numeric two-point check
A_, B_, Al_, K_ = 2, 1, 1, mp.mpf('1.5')
Sm_ = lambda z: S_num(z, A_, B_, Al_, K_)**2
def lam_match(z):
    return mp.findroot(lambda L: S_num(z, A_, B_, Al_, K_, L) - Sm_(z), mp.mpf('0.7'))
print("  scale needed to match S^2 at x=0.3:", mp.nstr(lam_match(mp.mpf('0.3')), 8), "; at x=2:", mp.nstr(lam_match(mp.mpf(2)), 8))
print("  -> different -> area conversion is NOT a pure scale (Delta) shift for this BGW member; the shape-only-in-scale property")
print("     that holds for Weibull area scaling does not carry over automatically.")
```

### Output
```
[1] nested special cases of F = I_G(a,b)
  I_u(1,1) = u -> a=b=1 gives F=G (exponentiated Weibull)
  I_u(a,1) = u**a -> b=1 gives F=G^a = (1-e^{-(x/lam)^k})^(a*alpha): a and alpha enter only as the product a*alpha (not separately identifiable)
  I_u(1,b) = 1 - (1 - u)**b -> a=1 gives F = 1-(1-G)^b
  a=b=alpha=1: F = 1 - exp(-(x/lam)**k) (2-parameter Weibull)
  alpha=1 gives Beta-Weibull; k=1 gives a beta exponentiated-exponential (by substitution)

[2] origin: G ~ (x/lam)^(k*alpha), F ~ G^a/(a B(a,b)) -> F ~ C x^(a*alpha*k), h ~ x^(a*alpha*k - 1)
  (1-e^{-u})^alpha near u=0, leading term: 1 * u^alpha
  check I_u(2,3)/u^2 -> 1/(a B(a,b)) = 6 vs 6
  a=2, b=3, alpha=0.5, k=0.8: numeric dlog h/dlog x near 0 = -0.200825, predicted a*alpha*k-1 = -0.2
  a=0.5, b=2, alpha=1, k=1.5: numeric dlog h/dlog x near 0 = -0.249997, predicted a*alpha*k-1 = -0.25
  a=3, b=1, alpha=2, k=0.6: numeric dlog h/dlog x near 0 = 2.59993, predicted a*alpha*k-1 = 2.6

[3] tail: 1-G ~ alpha e^{-(x/lam)^k}, S = I_{1-G}(b,a) ~ C (1-G)^b -> h ~ b k x^(k-1)/lam^k
  a=2, b=3, alpha=0.5, k=0.8: h(30.0) numeric = 1.2155897, tail law b k x^(k-1) = 1.2155896, ratio = 1.0
  a=0.5, b=2, alpha=1, k=1.5: h(6.0) numeric = 7.3484697, tail law b k x^(k-1) = 7.3484692, ratio = 1.0
  -> tail rising iff k>1, falling iff k<1, constant iff k=1 (tail controlled by k only, b sets the level)

[4] example shapes (sign changes of dh/dx on a log grid; illustrative parameter sets, not fitted values)
  IFR  (a*alpha*k>1, k>1): params a,b,alpha,k = ['2', '1', '1', '1.5']: monotonic pattern of h = +
  DFR  (a*alpha*k<1, k<1): params a,b,alpha,k = ['0.5', '1', '1', '0.7']: monotonic pattern of h = -
  CFR  (a=b=alpha=k=1): params a,b,alpha,k = ['1', '1', '1', '1']: monotonic pattern of h = 0 (flat)
  BT   (a*alpha*k<1, k>1): params a,b,alpha,k = ['0.3', '1', '1', '2.0']: monotonic pattern of h = -+
  UBT  (a*alpha*k>1, k<1): params a,b,alpha,k = ['4', '1', '1', '0.6']: monotonic pattern of h = +-
  ('+' rising, '-' falling; '-+' = bathtub, '+-' = upside-down bathtub). CFR case: h constant, numerically flat.

[5] if stress enters only via the scale lam(S): F(t;S) = H((t/lam(S)))
  F(t;lam2) == F(t*lam1/lam2; lam1): True
  -> every quantile ratio t_p(S1)/t_p(S2) = lam1/lam2 for all p; log-times shift by a constant;
     shape invariance is built in once stress is placed only in lam (it is a modeling choice, testable, not a physics result)

[6] two-mechanism mixture with EQUAL acceleration is still a pure scale family
  Fmix(t; AF) == Fmix(t*AF; 1): True
  -> two physically different subpopulations with equal voltage acceleration pass every shape-invariance test;
     invariance cannot prove a single mechanism.
  unequal acceleration (c1 != c2), illustrative values: {'p': '3/10', 'beta1': '1', 'beta2': '3', 'eta1': '1', 'eta2': '10', 'c1': '1', 'c2': '2'}
    V=0: Weibull-plot slope at median = 1.46364
    V=1: Weibull-plot slope at median = 1.7334
    V=2: Weibull-plot slope at median = 2.24878
  -> with unequal acceleration the apparent shape drifts with stress; detectability depends on n and censoring.

[7] competing risks: series system of DFR (beta1<1) and IFR (beta2>1) Weibull mechanisms
  h(t) = h1 + h2; stationary point(s): [exp(log(beta2*eta1**beta1*(1 - beta2)/(beta1*eta2**beta2*(beta1 - 1)))/(beta1 - beta2))]
  example beta1=1/2, beta2=3, eta1=100, eta2=10: t* = 1.76976 ; dh/dt at t*/2 = -0.02472 ; at 2t* = 0.01748 -> bathtub
  -> a single flexible-family fit showing BT can be two physical mechanisms in competition.
  mixture of exponentials: dh/dt = q*(l_1 - l_2)**2*(q - 1)*exp(l_1*x)*exp(l_2*x)/(q*exp(l_1*x) - q*exp(l_2*x) - exp(l_1*x))**2  (always <= 0: CFR components mix into DFR)

[8] Weibull (complete sample) Fisher information, per observation, in (beta, eta)
  I = Matrix([[(hyper((2, 2, 2), (3, 3, 3), -1) + 8*meijerg(((), (-1, -1, -1)), ((-2, -2, -2, 0), ()), 1) + 4)/(4*beta**2), (-1 + EulerGamma)/eta], [(-1 + EulerGamma)/eta, beta**2/eta**2]])
  n*Var(beta_hat) = 4*beta**2/(hyper((2, 2, 2), (3, 3, 3), -1) - 4*EulerGamma**2 + 8*meijerg(((), (-1, -1, -1)), ((-2, -2, -2, 0), ()), 1) + 8*EulerGamma) = 0.607927 * beta^2
  n*Var(ln beta_hat) ~ 0.607927  -> sd(ln beta_hat) ~ 0.77970 /sqrt(n)
  two levels, equal n: sd(ln beta1_hat - ln beta2_hat) = 1.1027 /sqrt(n)
  minimum detectable |ln(beta1/beta2)| at z=1.96 (5% two-sided, 50% power): 2.1612/sqrt(n)
     n=10: |ln ratio| >= 0.6834  (ratio >= 1.981)
     n=30: |ln ratio| >= 0.3946  (ratio >= 1.484)
     n=100: |ln ratio| >= 0.2161  (ratio >= 1.241)
  minimum detectable |ln(beta1/beta2)| at z=1.96+0.84 (80% power): 3.0874/sqrt(n)
     n=10: |ln ratio| >= 0.9763  (ratio >= 2.655)
     n=30: |ln ratio| >= 0.5637  (ratio >= 1.757)
     n=100: |ln ratio| >= 0.3087  (ratio >= 1.362)
  (asymptotic, complete samples; censoring and small n make these wider; illustrative n only)

[9] weakest-link area scaling S_m = S^m
  Weibull: S^m == Weibull with eta*m^(-1/k): True
  BGW a=2,b=1, m=2: S^2 = (u - 1)**2*(u + 1)**2 ; BGW a=2,b=2 survival = (2*u**3 - 3*u**2 + 6*beta(2, 2))/(6*beta(2, 2)) ; equal: False
  scale needed to match S^2 at x=0.3: 0.77767186 ; at x=2: 0.68213647
  -> different -> area conversion is NOT a pure scale (Delta) shift for this BGW member; the shape-only-in-scale property
     that holds for Weibull area scaling does not carry over automatically.
```
