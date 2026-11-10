# W42 item 1 (cross-temperature read-reference compensation, 3D TLC NAND) - checks.
# Inputs: ONLY values printed in the source (both reads agree) or symbols.
# SymPy is used if importable; the pinned venv_sympy was NOT found on this machine
# (searched the scratchpad and Temp\claude), so the fallback path uses exact
# rational arithmetic (fractions) and analytic identities verified by dense sampling.
import sys, math
from fractions import Fraction as F
from itertools import combinations
sys.stdout.reconfigure(encoding='utf-8')

try:
    import sympy as sp
    HAVE_SYMPY = True
    print("sympy", sp.__version__)
except Exception as e:
    HAVE_SYMPY = False
    print("sympy NOT available (", type(e).__name__, ") -> fraction/analytic fallback")

print("\n[C1] arithmetic consistency of source percentages (source values only)")
def pct(a, b):  # relative reduction from a to b, exact
    return (F(a) - F(b)) / F(a) * 100
r1 = pct("24.28", "0.44");      print("RBER 24.28 -> 0.44 : %.4f %%  (source 98.19%%)" % float(r1))
r2 = pct("774.770", "435.362"); print("mean 774.770 -> 435.362 : %.4f %%  (source 43.81%%)" % float(r2))
g  = (F("435.362") - F("435.008")) / F("435.008") * 100
print("gap MB-RRVC vs Ideal (rel. to Ideal): %.4f %%  (source 0.08%%)" % float(g))
g2 = (F("435.362") - F("435.008")) / F("435.362") * 100
print("gap MB-RRVC vs Ideal (rel. to MB-RRVC): %.4f %%" % float(g2))
assert round(float(r1), 2) == 98.19 and round(float(r2), 2) == 43.81 and round(float(g), 2) == 0.08

print("\n[C2] temperature grid count")
Tp = [-40, 0, 40, 80, 120]   # Algorithm 1 (advance-version extraction only)
Tr = list(range(-40, 121, 20))  # 'from -40 to 120 C with a 20 C interval' (both reads)
print("len(Tp) x len(Tr) =", len(Tp), "x", len(Tr), "=", len(Tp) * len(Tr), "(source: 45 cross-temperature points)")
same = [t for t in Tp if t in Tr]
print("points with Tp == Tr included in the 45:", len(same))
swapped = [(a, b) for a, b in combinations(Tp, 2) if b in Tr and a in Tr]
print("unordered (T1,T2) pairs for which both (Tp=T1,Tr=T2) and (Tp=T2,Tr=T1) exist:", len(swapped))
print("max |dT| on grid:", max(abs(r - p) for p in Tp for r in Tr))

print("\n[D1] sensing-only model: apparent Vth = V_int + g(T); verify sets V_app(Tp)=V_vfy")
# dmu(Tp,Tr) = g(Tr) - g(Tp)  -> antisymmetry and path additivity for ANY g
def gq(T, a, b, T0):  # quadratic test function
    return -a * (T - T0) - b * (T - T0) ** 2
if HAVE_SYMPY:
    T1, T2, T3, a, b, T0 = sp.symbols('T1 T2 T3 a b T0', real=True)
    gfun = sp.Function('g')
    dmu = lambda p, r: gfun(r) - gfun(p)
    print("antisymmetry dmu(T1,T2)+dmu(T2,T1) =", sp.simplify(dmu(T1, T2) + dmu(T2, T1)))
    print("additivity dmu(T1,T2)+dmu(T2,T3)-dmu(T1,T3) =", sp.simplify(dmu(T1, T2) + dmu(T2, T3) - dmu(T1, T3)))
    q = sp.expand(gq(T2, a, b, T0) - gq(T1, a, b, T0))
    target = -a * (T2 - T1) - b * (T2 - T1) * (T1 + T2 - 2 * T0)
    print("quadratic g: dmu - [-a dT - b dT (Tp+Tr-2T0)] =", sp.simplify(q - target))
else:
    import random
    random.seed(1)
    worst = 0.0
    for _ in range(20000):
        a_, b_, T0_ = random.uniform(-5, 5), random.uniform(-5, 5), random.uniform(-50, 50)
        p, r, s = (random.uniform(-100, 150) for _ in range(3))
        G = lambda T: gq(T, a_, b_, T0_) + math.sin(0.01 * T)  # arbitrary nonlinear g
        dm = lambda x, y: G(y) - G(x)
        worst = max(worst, abs(dm(p, r) + dm(r, p)), abs(dm(p, r) + dm(r, s) - dm(p, s)))
        lhs = gq(r, a_, b_, T0_) - gq(p, a_, b_, T0_)
        rhs = -a_ * (r - p) - b_ * (r - p) * (p + r - 2 * T0_)
        worst = max(worst, abs(lhs - rhs) / (1 + abs(lhs)))
    print("antisymmetry / additivity / quadratic identity, max residual over 20000 samples: %.2e" % worst)
print("=> pure dT dependence (dmu = h(Tr-Tp)) with g of this form requires b = 0;")
print("   a nonzero b adds -b*dT*(Tp+Tr-2T0): same dT, different mean temperature -> different dmu.")
print("   an irreversible loss term -L(history) breaks antisymmetry: dmu(T1,T2)+dmu(T2,T1) = -(L12+L21) != 0.")

print("\n[D2] coaxial stack: Vth shift from areal charge sigma at channel surface r0")
# dV = sigma*r0*sum ln(r_{i+1}/r_i)/eps_i ; planar: sigma*sum t_i/eps_i ; one layer ratio f(u)=ln(1+u)/u, u=t/r0
if HAVE_SYMPY:
    u = sp.symbols('u', positive=True)
    f = sp.log(1 + u) / u
    df = sp.simplify(sp.diff(f, u))
    print("f(u)=ln(1+u)/u, f'(u) =", df, "; limit u->0:", sp.limit(f, u, 0))
else:
    us = [10 ** (k / 200.0) for k in range(-800, 801)]
    fs = [math.log1p(x) / x for x in us]
    mono = all(fs[i] > fs[i + 1] for i in range(len(fs) - 1))
    print("f(u)=ln(1+u)/u strictly decreasing on sampled u in [1e-4,1e4]:", mono,
          "; f(1e-6) =", round(math.log1p(1e-6) / 1e-6, 6), "(planar limit 1)")
    print("analytic: f'(u) = [u/(1+u) - ln(1+u)]/u^2 < 0 because ln(1+u) > u/(1+u) for u > 0")
print("=> fixed thicknesses: smaller r0 (larger u) -> smaller Vth shift per unit areal channel-surface charge.")

print("\n[D3] coaxial field at channel surface from areal CTL charge sigma_c at r_c = r0 + t (all image charge on channel side)")
# Q' = 2 pi r_c sigma_c ; E(r0) = Q'/(2 pi eps r0) = sigma_c (r_c/r0)/eps = (sigma_c/eps)(1+u)
print("E(r0)/E_planar = r_c/r0 = 1 + u  (> 1, increasing as r0 shrinks at fixed t)")
print("   (upper bound: in reality Q' splits between channel and gate according to C'_in/C'_out)")
if HAVE_SYMPY:
    ci, co = sp.symbols('C_in C_out', positive=True)
    print("fraction of stored line charge imaged on channel side =", ci / (ci + co))
else:
    print("fraction of stored line charge imaged on channel side = C'_in/(C'_in + C'_out) (grounded channel and gate)")

print("\n[D4] tail: per-cell coefficient spread after mean-only compensation")
# residual spread: s_res^2 = s0^2 + (s_k*dT)^2 (independent); boundary when z*s_res = m (margin half-width m)
print("s_res(dT) = sqrt(s0^2 + s_k^2 dT^2);  z*s_res = m  ->  |dT|* = sqrt((m/z)^2 - s0^2)/s_k  (exists only if m/z > s0)")
if HAVE_SYMPY:
    s0, sk, m, z, dT = sp.symbols('s0 s_k m z dT', positive=True)
    sol = sp.solve(sp.Eq(z ** 2 * (s0 ** 2 + sk ** 2 * dT ** 2), m ** 2), dT)
    print("sympy solve:", sol)
print("done")
