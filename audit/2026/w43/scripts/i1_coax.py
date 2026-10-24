# W43 item 1: coaxial electrostatics of a tunnel-oxide-less stack (poly-Si | Si3N4 | Al2O3 | gate)
# Framework only. All quantities dimensionless; NO product or paper dimensions are used
# (the paper's thicknesses/voltages are unknown: abstract only).
# Ideal assumptions: axially infinite, uniform; free charge only on electrodes; same Q' through
# every layer; metal-like channel surface (no poly depletion, no Vfb, no stored charge).
import sys, itertools
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp

x, a, e, k = sp.symbols('x a e kappa', positive=True)   # x=t_N/r0, a=t_A/t_N, e=eps_A/eps_N
lam, w, u = sp.symbols('lambda w u', positive=True)

# ---------- [1] program field at channel/nitride interface, coax vs planar (same total V)
# radii in units of r0: r0=1, r1=1+x (N/A interface), r2=1+x+a*x (gate)
S_log = sp.log(1 + x) + sp.log((1 + x + a*x)/(1 + x))/e      # sum ln(r_out/r_in)/(eps_i/eps_N)
S_lin = x + a*x/e                                             # sum t_i/(eps_i/eps_N), units r0
g0 = S_lin/S_log                                              # E_coax(r0)/E_planar(nitride)
g0_s = sp.series(g0, x, 0, 2).removeO()
print("[1] g0 = E_coax(r0)/E_planar,nitride  (AN two-layer)")
print("    first order in x=t_N/r0:  g0 - 1 =", sp.factor(sp.simplify(g0_s - 1)))
c1 = sp.factor(sp.simplify((g0_s - 1)/x))
print("    coefficient positive for all a,e>0? numerator/denominator are sums of positive terms:", c1)
# gate-side (Al2O3/gate) field ratio
gg = (S_lin/e)/((1 + x + a*x)*S_log/e)   # E_coax(r2) in Al2O3 / planar Al2O3 field
gg_s = sp.series(gg, x, 0, 2).removeO()
print("    gate-side ratio - 1 (first order):", sp.factor(sp.simplify(gg_s - 1)))
# nitride/Al2O3 interface, nitride side
g1 = S_lin/((1 + x)*S_log)
g1_s = sp.series(g1, x, 0, 2).removeO()
print("    N/A interface (nitride side) ratio - 1:", sp.factor(sp.simplify(g1_s - 1)))

# ---------- [2] WKB exponent of FN barrier in 1/r field at the SAME interface field E0
# U(r)/phi = 1 - ln(r/r0)/lam, lam = phi/(q E0 r0) = (planar barrier length)/r0.
# Turning point r_t/r0 = exp(lam). Substituting r/r0 = exp(lam*w):
# exponent_coax / exponent_planar = R(lam) = (3/2) * Int_0^1 sqrt(1-w) exp(lam*w) dw
R = sp.Rational(3, 2)*sp.integrate(sp.sqrt(1 - w)*sp.exp(lam*w), (w, 0, 1))
R = sp.simplify(R)
print("\n[2] R(lam) = WKB exponent coax/planar at equal E0:", R)
Rser = sp.series(sp.Rational(3, 2)*sp.integrate(sp.series(sp.sqrt(1 - w)*sp.exp(lam*w), lam, 0, 4).removeO(), (w, 0, 1)), lam, 0, 4)
print("    series:", Rser)
Rn = sp.lambdify(lam, R, 'mpmath')
print("    numeric R at lam=0.05,0.2,0.5:", [sp.N(R.subs(lam, v), 5) for v in (0.05, 0.2, 0.5)])
# direct numeric integration check
import mpmath as mp
chk = [mp.mpf(1.5)*mp.quad(lambda ww: mp.sqrt(1-ww)*mp.e**(v*ww), [0, 1]) for v in (0.05, 0.2, 0.5)]
print("    quad check:", [mp.nstr(c, 5) for c in chk])

# ---------- [3] net FN exponent at the SAME total V: coax/planar = R(lam_coax)/g0
# FN regime requires the turning point inside the nitride: exp(lam_c) - 1 <= x  <=> lam_c <= ln(1+x),
# where lam_c = phi/(q E0 r0) uses the coax interface field E0 = g0*E_pl.
print("\n[3] net exponent ratio N = R(lam_c)/g0 on a generic dimensionless grid (lam_c <= ln(1+x))")
worst = 0
for X, A, E in itertools.product([0.05, 0.1, 0.2, 0.5, 1.0], [0.25, 0.5, 1, 2, 4], [0.5, 1, 1.5, 2, 3]):
    G = float(g0.subs({x: X, a: A, e: E}))
    for f in (0.1, 0.5, 0.9, 1.0):
        L = f*float(sp.log(1 + X))
        Nr = float(Rn(L))/G
        worst = max(worst, Nr)
print("    max N over grid =", round(worst, 6), "(<1 means coax still lowers the FN exponent at equal V)")
# analytic first-order: single-layer-like bound: R(lam)<=R(ln(1+x)) ~ 1+2x/5 ; g0 >= ? compare orders
print("    first-order: R ~ 1 + 2*lam/5, lam <= x ; g0 ~ 1 + x*c1 ; c1 at a->0:", sp.limit(c1, a, 0))

# ---------- [4] parameter aliasing: fitting FN with a planar field assumption
# exponent = B/E_true_eff with B ∝ sqrt(m*) phi^(3/2); E_true_eff = g0*E_pl/R.
# If the analyst uses E_pl and fixed phi: sqrt(m_fit)/E_pl = sqrt(m)*R/(g0*E_pl) -> m_fit = m*(R/g0)^2
m, gS, RS = sp.symbols('m g_0 R', positive=True)
m_fit = sp.solve(sp.Eq(sp.sqrt(sp.Symbol('m_fit', positive=True)), sp.sqrt(m)*RS/gS), sp.Symbol('m_fit', positive=True))
print("\n[4] m*_fit (planar-field analysis of a coaxial device) =", m_fit)

# ---------- [5] Vth shift of a stored sheet at radius rc inside the nitride (charge per length Q')
# dVth = Q'/(2 pi) * [ ln(r1/rc)/eps_N + ln(r2/r1)/eps_A ]   (sheet-to-gate inverse capacitance)
rc, r1s, r2s, epsN, epsA, Qp = sp.symbols('r_c r_1 r_2 epsilon_N epsilon_A Qprime', positive=True)
dV = Qp/(2*sp.pi)*(sp.log(r1s/rc)/epsN + sp.log(r2s/r1s)/epsA)
print("\n[5] dVth(rc) =", dV)
print("    d(dVth)/d rc =", sp.simplify(sp.diff(dV, rc)))
# same areal density sigma at rc (Q'=2 pi rc sigma) vs planar sigma*((t_N - xc)/eps_N + t_A/eps_A):
sig, r0s = sp.symbols('sigma r_0', positive=True)
xc = rc - r0s
dV_coax = (2*sp.pi*rc*sig)/(2*sp.pi)*(sp.log(r1s/rc)/epsN + sp.log(r2s/r1s)/epsA)
dV_pl = sig*((r1s - rc)/epsN + (r2s - r1s)/epsA)
print("    planar limit check (r0 -> large, fixed thicknesses):")
T, TA, XC = sp.symbols('t_N t_A x_c', positive=True)
ratio = (dV_coax/dV_pl).subs({r1s: r0s + T, r2s: r0s + T + TA, rc: r0s + XC})
print("    lim r0->oo of coax/planar =", sp.simplify(sp.limit(ratio, r0s, sp.oo)))
print("    c1 - 1/2 =", sp.factor(sp.simplify(c1 - sp.Rational(1, 2))), "(>0 for a>0: first-order g0 coefficient exceeds 1/2 > 2/5)")
