"""W41 item 1 (Oh & Shin, RTN decay constant) - symbolic framework checks.
All quantities symbolic / dimensionless. No product values.
Run: venv_sympy python -I i1_derive.py
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp

print('sympy', sp.__version__)
ok = []

# ---------- D1: trap-statistics frameworks for d ln(delta)/d ln(mu) ----------
mu, p, sd, sn, A, B, g = sp.symbols('mu p sigma_d sigma_n A B gamma', positive=True)
# (a) Independent traps, Poisson count with mean mu, each contributes s_i*a_i, zero-mean sign,
#     amplitude from a two-component (double-Gaussian) mixture with fixed dominant fraction p.
#     Var(sum) = mu * E[s^2] * E[a^2]; delta taken proportional to std at a fixed probability window.
Es2 = sp.Symbol('E_s2', positive=True)
Ea2 = p*sd**2 + (1-p)*sn**2
var_a = mu*Es2*Ea2
expo_a = sp.simplify(sp.diff(sp.log(sp.sqrt(var_a)), mu)*mu)
print('D1a exponent (fixed-fraction double Gaussian, independent traps):', expo_a)
ok.append(sp.simplify(expo_a - sp.Rational(1, 2)) == 0)

# (b) Dominant-trap count grows sublinearly as mu**gamma (e.g. limited percolation paths), negligible part linear.
var_b = A*mu**g + B*mu
expo_b = sp.simplify(sp.diff(sp.log(sp.sqrt(var_b)), mu)*mu)
print('D1b local exponent:', expo_b)
# limits
print('   A-dominated limit (B->0):', sp.simplify(expo_b.subs(B, 0)))
print('   B-dominated limit (A->0):', sp.simplify(expo_b.subs(A, 0)))
gam_req = sp.solve(sp.Eq(expo_b.subs(B, 0), sp.Rational(1, 3)), g)
print('   gamma needed for 1/3 when dominant part dominates:', gam_req)
ok.append(gam_req == [sp.Rational(2, 3)])
# exponent lies between gamma/2 and 1/2 for gamma<1
x = sp.symbols('x', positive=True)  # x = A mu^gamma / (B mu)
expo_bx = sp.Rational(1, 2)*(g*x + 1)/(x + 1)
print('   exponent in terms of x=A mu^g/(B mu):', expo_bx,
      ' d/dx =', sp.simplify(sp.diff(expo_bx, x)))
ok.append(sp.simplify(expo_bx.subs(x, 0) - sp.Rational(1, 2)) == 0)
ok.append(sp.simplify(sp.limit(expo_bx, x, sp.oo) - g/2) == 0)

# (c) Gaussian tail slope at fixed tail probability P: x_P = sigma*z_P; d x / d log10(P) at fixed z.
s, z = sp.symbols('sigma z', positive=True)
# 1-Phi(z) ~ phi(z)/z ; d ln(1-Phi)/dz ~ -(z + 1/z); slope in mV/dec = sigma*ln10/(z+1/z)
slope = s*sp.log(10)/(z + 1/z)
print('D1c Gaussian local tail slope [units of sigma per decade]:', slope,
      '-> proportional to sigma at fixed window: d ln slope/d ln sigma =',
      sp.simplify(sp.diff(sp.log(slope), s)*s))
ok.append(sp.simplify(sp.diff(sp.log(slope), s)*s - 1) == 0)
# window drift: if the extraction window (z) moves with mu, the apparent exponent changes:
dz = sp.Symbol('dz_dlnmu')
app = sp.Rational(1, 2) - (1 - 1/z**2)/(z + 1/z)*dz  # d ln slope/d ln mu = 1/2 + d ln(1/(z+1/z))/dz * dz/dlnmu
print('   apparent exponent if window z drifts with ln mu (std ~ mu^1/2):', sp.simplify(app))

# ---------- D2: coaxial sheet-charge amplitude vs planar estimate ----------
# layers from channel surface r0 outward: tunnel ox, CTN, blocking ox. Uniform sheet q around circumference
# over length L at r0. Gate stack capacitance per length C' = 2*pi / sum(ln(r_{i+1}/r_i)/eps_i)
eps0 = sp.Symbol('epsilon_0', positive=True)
r0, t1, t2, t3, e1, e2, e3, L, q = sp.symbols('r_0 t_1 t_2 t_3 epsilon_1 epsilon_2 epsilon_3 L q', positive=True)
r1, r2, r3 = r0 + t1, r0 + t1 + t2, r0 + t1 + t2 + t3
inv_C = (sp.log(r1/r0)/e1 + sp.log(r2/r1)/e2 + sp.log(r3/r2)/e3)/(2*sp.pi)
dV_coax = q*inv_C/L
dV_planar = q*(t1/e1 + t2/e2 + t3/e3)/(2*sp.pi*r0*L)   # planar formula with area at channel surface
ratio = sp.simplify(dV_coax/dV_planar)
print('D2 coax/planar sheet amplitude ratio:', ratio)
# single-layer check: ratio = ln(1+u)/u <= 1
u = sp.symbols('u', positive=True)
single = sp.simplify((sp.log(1+u)/u))
print('   single layer: ln(1+u)/u, series:', sp.series(single, u, 0, 3))
ok.append(sp.simplify(ratio.subs({t2: 0, t3: 0}) - sp.log(1 + t1/r0)*r0/t1) == 0)
# numeric spot-check of ratio<1 on a dimensionless grid (not product values)
import itertools
mx = 0
for a_, b_, c_, ea, eb, ec in itertools.product([0.05, 0.2, 0.5], [0.05, 0.3, 0.6], [0.05, 0.3, 0.6],
                                                [1, 2], [1, 2], [1, 2]):
    v = float(ratio.subs({r0: 1, t1: a_, t2: b_, t3: c_, e1: ea, e2: eb, e3: ec}))
    mx = max(mx, v)
print('   max ratio on dimensionless grid (t_i/r0 in 0.05..0.6):', round(mx, 4))
ok.append(mx < 1)

# ---------- D3: trap count in an annular (macaroni) channel shell ----------
rf, tp, nv, ns = sp.symbols('r_f T_poly n_v n_s', positive=True)
t = sp.symbols('t', positive=True)  # t = T_poly/r_f
mu_bulk = nv*sp.pi*((rf+tp)**2 - rf**2)*L
mu_surf_out = ns*2*sp.pi*(rf+tp)*L       # traps at channel / tunnel-oxide interface
mu_surf_in = ns*2*sp.pi*rf*L             # traps at filler / channel interface
el = lambda f, v: sp.simplify(sp.diff(sp.log(f), v)*v)
eb_T = sp.simplify(el(mu_bulk, tp).subs(tp, t*rf))
es_T = sp.simplify(el(mu_surf_out, tp).subs(tp, t*rf))
eb_R = sp.simplify(el(mu_bulk, rf).subs(tp, t*rf))
print('D3 d ln mu/d ln Tpoly: bulk =', eb_T, '; outer-interface =', es_T)
print('   d ln mu/d ln r_f (bulk, Tpoly fixed) =', eb_R)
print('   d ln mu/d ln L = 1 for all three')
ok.append(sp.simplify(eb_T - (2+2*t)/(2+t)) == 0)
ok.append(sp.simplify(es_T - t/(1+t)) == 0)
ok.append(sp.simplify(eb_R - 2/(2+t)) == 0)
# planar-slab limit (t->0): bulk -> 1, outer interface -> 0
print('   t->0 limits: bulk', sp.limit(eb_T, t, 0), ' interface', sp.limit(es_T, t, 0))

# ---------- D4: total sensitivity at FIXED trap density, using text-stated low-mu exponents ----------
# delta ∝ L^(-1/4) * Tpoly^(-1) * mu^(1/3)   (text: fourth root of LWL, ~1/Tpoly at low mu, cube root of mu)
# NOTE: mixing the low-mu explicit exponents with the mu^(1/3) law is an assumption (the text gives the
# 1/3 law over its mu range; the explicit exponents are stated for low mu only).
k = sp.Rational(1, 3)
tot_L = -sp.Rational(1, 4) + k*1
tot_T_bulk = sp.simplify(-1 + k*eb_T)
tot_T_surf = sp.simplify(-1 + k*es_T)
print('D4 total d ln delta/d ln L at fixed density:', tot_L)
print('   total d ln delta/d ln Tpoly, bulk traps:', tot_T_bulk, ' range t->0:', sp.limit(tot_T_bulk, t, 0),
      ' t->oo:', sp.limit(tot_T_bulk, t, sp.oo))
print('   total d ln delta/d ln Tpoly, outer-interface traps:', tot_T_surf, ' t->0:', sp.limit(tot_T_surf, t, 0),
      ' t->oo:', sp.limit(tot_T_surf, t, sp.oo))
ok.append(tot_L == sp.Rational(1, 12))
# same with 2D square-root law for comparison
print('   with a 1/2 law instead: d ln delta/d ln L =', -sp.Rational(1, 4) + sp.Rational(1, 2))

# ---------- D5: conditional reading of Eq.(1) V_filler^(1/4) ----------
# IF the denominator contains V_filler^(1/4) and V_filler = pi r_f^2 L (cylindrical filler), then:
Vf = sp.pi*rf**2*L
print('D5 IF delta ∝ V_filler^(-1/4): d ln/d ln r_f =', el(Vf**sp.Rational(-1, 4), rf),
      '; d ln/d ln L =', el(Vf**sp.Rational(-1, 4), L))
ok.append(el(Vf**sp.Rational(-1, 4), rf) == -sp.Rational(1, 2))
ok.append(el(Vf**sp.Rational(-1, 4), L) == -sp.Rational(1, 4))

print('ALL ASSERTIONS:', all(ok), ok)
