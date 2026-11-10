"""Item 4 (HZO thickness scaling / TDC model) sympy checks. Inputs are values printed in the source."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp
R = sp.Rational

print('sympy', sp.__version__)

# (1) Eq. (4): V_O = 1/4 [Hf3+/(2 Hf_tot) + Hf2+/Hf_tot + 3 Hf+/(2 Hf_tot)], Hf2+ and Hf+ negligible (source)
for d, hf3 in [(8, R('7.04')), (7, R('7.68')), (6, R('8.56'))]:
    vo = R(1, 4) * (hf3 / 2)
    print(f'(1) d={d} nm: Hf3+={float(hf3)}% -> V_O = Hf3+/8 = {float(vo):.4f}%')

# (2) DFT supercell: 2 V_O in 3x3x3 supercell. ASSUMPTION (not in source): 12-atom orthorhombic cell, 8 O per cell.
nO = 3 * 3 * 3 * 8
print('(2) O sites (assumed 8 O/cell) =', nO, '; 2/nO =', float(R(2, nO) * 100), '%  (source: 0.93%)')

# (3) defect-level spread ratio
print('(3) 1.39/0.51 =', float(R('1.39') / R('0.51')))

# (4) 10-year allowable field ratio and equivalent voltage V = E*d (ignores dead layer / Vfb / work-function asymmetry)
E6, E8 = R('3.84'), R('3.52')  # MV/cm
print('(4) E10y ratio 6/8 =', float(E6 / E8), '-> +', float((E6 / E8 - 1) * 100), '%')
# 1 MV/cm * 1 nm = 1e6 V/cm * 1e-7 cm = 0.1 V
for d, E in [(6, E6), (8, E8)]:
    print(f'    V10y(d={d} nm) = E*d = {float(E * d * R(1, 10))} V')
for d in (6, 8):
    print(f'    endurance field 4.2 MV/cm, d={d} nm -> V = {float(R("4.2") * d * R(1, 10))} V')
for d in (6, 7, 8):
    print(f'    wake-up/leakage cycling 4.0 MV/cm, d={d} nm -> V = {float(R("4.0") * d * R(1, 10))} V')
# TZDB: E_BD(6)=1.266 E_BD(8) -> V_BD ratio
print('(4b) V_BD(6)/V_BD(8) = 1.266*6/8 =', float(R('1.266') * R(6, 8)), '; V_BD(7)/V_BD(8) = 1.141*7/8 =', float(R('1.141') * R(7, 8)))

# (5) TDC model Eq. (6): Fc = 1 - [1 + (1/alpha)(t/tau)^beta]^(-alpha)
t, tau, a, b, x = sp.symbols('t tau alpha beta x', positive=True)
Fc = 1 - (1 + (t / tau) ** b / a) ** (-a)
Fw = 1 - sp.exp(-(t / tau) ** b)
print('(5a) lim alpha->oo Fc - Fweibull =', sp.simplify(sp.limit(Fc - Fw, a, sp.oo)))
# Weibull-plot coordinate W = ln(-ln(1-Fc)) in terms of x=(t/tau)^beta
W = sp.log(a * sp.log(1 + x / a))
ser = sp.series(W, x, 0, 3).removeO()
print('(5b) W(x) small-x series =', sp.simplify(ser))
# local slope dW/dln t = beta * x dW/dx
slope = sp.simplify(b * x * sp.diff(W, x))
print('(5c) dW/dln t =', slope)
print('     at x->0:', sp.limit(slope, x, 0), '; as x->oo:', sp.limit(slope, x, sp.oo))
# low-percentile: F ~ x for small x for any alpha -> W ~ ln x ; percentile p: x_p for TDC vs Weibull
p = sp.symbols('p', positive=True)
xp_tdc = sp.solve(sp.Eq(1 - (1 + x / a) ** (-a), p), x)[0]
xp_w = -sp.log(1 - p)
print('(5d) x_p TDC =', sp.simplify(xp_tdc))
for av in [1, 2, 5]:
    for pv in [R(1, 10**5), R(1, 10**4), R(632, 1000), R(99, 100)]:
        r = sp.N(xp_tdc.subs({a: av, p: pv}) / xp_w.subs(p, pv), 6)
        print(f'     alpha={av}, p={float(pv)}: x_p(TDC)/x_p(Weibull) = {r}')
# time ratio t_p(TDC)/t_p(Weibull) = (x ratio)^(1/beta): at p=1e-5 and alpha=1 the ratio is close to 1
# (6) mean of the alpha->oo limit (Weibull) is tau*Gamma(1+1/beta), not tau unless beta=1
mean_w = sp.integrate(sp.exp(-(t / tau) ** b), (t, 0, sp.oo))
print('(6) mean of Weibull limit =', sp.simplify(mean_w))

# (7) Eq. (7): beta = gamma d / a0 -> a0 ratio
g6, g8, b6, b8 = sp.symbols('gamma6 gamma8 beta6 beta8', positive=True)
ratio = sp.simplify((g6 * 6 / b6) / (g8 * 8 / b8))
print('(7) a0(6nm)/a0(8nm) =', ratio, '; with gamma6<=gamma8 and beta6>beta8 => < 3/4')

# (8) coaxial contrast (VNAND default geometry), symbolic only: E(r)=Q'/(2 pi eps r)
Qp, eps, r, rin, rout = sp.symbols("Qp epsilon r r_in r_out", positive=True)
E = Qp / (2 * sp.pi * eps * r)
dV = sp.simplify(sp.integrate(E, (r, rin, rout)))
print('(8) dV =', dV)
tt = sp.symbols('t_d', positive=True)
ratio_E = sp.simplify((Qp / (2 * sp.pi * eps * rin)) / (dV.subs(rout, rin + tt) / tt))
print('    E(r_in)/(V/t) at equal V =', ratio_E, '; limit t/r_in->0:', sp.limit(ratio_E.subs(tt, x * rin), x, 0))
