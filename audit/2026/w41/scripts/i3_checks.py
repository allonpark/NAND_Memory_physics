"""Item 3 (W41) consistency checks and labelled derivations. sympy only.
All inputs are values printed in arXiv:2610.11643v1 (main text + SI) unless marked CONST.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
from sympy import Rational as R, nsimplify, N, symbols, log, exp, limit, simplify, series, oo, pi

def p(tag, expr, digits=4):
    print(f"{tag}: {expr} = {N(expr, digits)}")

print("== C1 route fractions sum to 100 % (Fig 2a / Table S2 fitted endpoints)")
p("low 2.92: 29+34+37", R(29)+34+37)
p("high 3.15: 9+45+46", R(9)+45+46)
p("K-like low (native+induced)", R(29)+34)
p("K-like high", R(9)+45)

print("== C2 Table S2 overall counts")
p("90+211+195", R(90)+211+195)
for n in (90, 211, 195):
    p(f"{n}/496*100", R(n, 496)*100)
p("499-496 (non-Si-routed cells)", R(499)-496)

print("== C3 ratios quoted as 'more than triples' etc.")
p("uncapped 3-coord Si per cell 0.45/0.12", R(45, 100)/R(12, 100))
p("void fraction 12.6/8.4", R(126, 10)/R(84, 10))
p("internal surface 1225/997", R(1225)/997)
p("specific surface 389/337", R(389)/337)
p("cavity-adjacent native-K precursors 79/57", R(79)/57)

print("== C4 cell volume from composition (CONST: IUPAC atomic masses, Avogadro)")
MSi, MN, NA = nsimplify('28.0855'), nsimplify('14.0067'), nsimplify('6.02214076e23')
m_g = (120*MSi + 160*MN)/NA          # grams per Si120N160 cell
p("cell mass [g]", m_g, 6)
V = {}
for rho in ('2.92', '3.15'):
    v = m_g/nsimplify(rho)*R(10)**24   # cm^3 -> A^3
    V[rho] = v
    p(f"cell volume at {rho} g/cm3 [A^3]", v, 6)
    p(f"  equivalent cube edge V^(1/3) [A] (cell shape not stated)", v**R(1, 3), 4)
p("volume ratio low/high", V['2.92']/V['3.15'])
print("-- recomputed specific surface from per-cell surface / volume (fitted values are separate fits)")
p("997/V(3.15)*1000 [A^2 per 1000 A^3]", R(997)/V['3.15']*1000)
p("1225/V(2.92)*1000 [A^2 per 1000 A^3]", R(1225)/V['2.92']*1000)
print("-- accessible void volume implied by fraction x cell volume")
p("0.084*V(3.15) [A^3]", R(84, 1000)*V['3.15'])
p("0.126*V(2.92) [A^3]", R(126, 1000)*V['2.92'])

print("== C5 volumetric density of uncapped 3-coord Si (DERIVED; model-ensemble value, not a film trap density)")
for cnt, rho in ((R(12, 100), '3.15'), (R(45, 100), '2.92')):
    n_cm3 = cnt/V[rho]*R(10)**24
    p(f"{cnt} per cell at {rho} -> [cm^-3]", n_cm3, 3)
p("one electron per cell at 3.15 -> [cm^-3] (charge density of the q=-1 calculation)", 1/V['3.15']*R(10)**24, 3)
p("one electron per cell at 2.92 -> [cm^-3]", 1/V['2.92']*R(10)**24, 3)

print("== C6 Fig 4d endpoint text vs Table S3 differences (high minus low density)")
fig4d = {  # route: (depth col1, depth col2, relax col1, relax col2) as extracted text order
    'native K': (R(325, 100), R(314, 100), R(145, 100), R(131, 100)),
    'induced K': (R(334, 100), R(317, 100), R(155, 100), R(149, 100)),
    'polaron': (R(287, 100), R(282, 100), R(118, 100), R(116, 100)),
}
tS3 = {'native K': (R(-12, 100), R(-14, 100)), 'induced K': (R(-17, 100), R(-6, 100)), 'polaron': (R(-5, 100), R(-3, 100))}
for k, (d1, d2, r1, r2) in fig4d.items():
    print(f"{k}: col2-col1 depth {N(d2-d1,3)} (Table S3 {N(tS3[k][0],3)}); relax {N(r2-r1,3)} (Table S3 {N(tS3[k][1],3)})")
print("=> sign and size match only if col1 = 2.92 and col2 = 3.15 g/cm3 (rounding <=0.01 eV)")
print("main-text route values 3.25/3.34/2.87 eV coincide with col1 (2.92 g/cm3) entries")

print("== C7 depth gap between K routes and polaron (source: 'approximately 0.4 eV shallower')")
p("3.25-2.87", R(325, 100)-R(287, 100))
p("3.34-2.87", R(334, 100)-R(287, 100))

print("== C8 framework only: Arrhenius emission ratio for a depth difference dE (SYMBOLIC)")
dE, kT = symbols('dE kT', positive=True)
ratio = exp(dE/kT)
print("emission-rate ratio shallow/deep with equal prefactor =", ratio)
kB = nsimplify('8.617333262e-5')  # CONST eV/K
for T in (300,):
    p(f"  illustration dE=0.4 eV, T={T} K: exp(0.4/(kB T))", exp(R(4, 10)/(kB*T)), 3)

print("== C9 coaxial vs planar (SYMBOLIC, no device numbers)")
Qp, eps, a, t, V0 = symbols("Qp eps a t V0", positive=True)
# coaxial: E(r)=Q'/(2 pi eps r); V across layer [a, a+t] = Q'/(2 pi eps) ln(1+t/a)
Qsol = V0*2*pi*eps/log(1+t/a)
Ea = Qsol/(2*pi*eps*a)
ratio_cp = simplify(Ea/(V0/t))
print("E(a)/E_planar at same V,t =", ratio_cp)
print("limit t/a -> 0 :", limit(ratio_cp.subs(t, symbols('x', positive=True)*a), symbols('x', positive=True), 0))
x = symbols('x', positive=True)
print("series in x=t/a:", series(x/log(1+x), x, 0, 3))
