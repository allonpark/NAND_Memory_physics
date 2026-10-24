import sys; sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp, mpmath as mp
print('sympy', sp.__version__)
# ---------- S1 ----------
Rd, Rx, C, t, tw, f, Ron, Rb, m, dV, Ea, k, I0 = sp.symbols('R_d R_x C t t_w f R_on R_b m dV E_a k I_0', positive=True)
v = 1 - sp.exp(-t/((Rd+Rx)*C))
td = sp.solve(sp.Eq(v, f), t)[0]
print('S1 E1 t_d - (Rd+Rx)C ln(1/(1-f)) =', sp.simplify(td - (Rd+Rx)*C*sp.log(1/(1-f))))
Rxc = sp.solve(sp.Eq(td, tw), Rx)[0]
print('   Rx,crit - [tw/(C ln(1/(1-f))) - Rd] =', sp.simplify(Rxc - (tw/(C*sp.log(1/(1-f))) - Rd)))
print('   theta=3,f=1/2 -> r_crit =', sp.N(3/sp.log(2) - 1, 6))
print('S1 E2 Rb,crit - Ron m/(1-m) =', sp.simplify(sp.solve(sp.Eq(Rb/(Rb+Ron), m), Rb)[0] - Ron*m/(1-m)))
bet = sp.symbols('beta_T', positive=True)  # 1/T
tf = C*dV/(I0*sp.exp(-Ea*bet/k))
print('S1 E3 dln t_fail/d(1/T) =', sp.simplify(sp.diff(sp.log(tf), bet)), '(expect Ea/k)')
# ---------- S2 ----------
V, rin, Eps, uu = sp.symbols('V r_in epsilon u', positive=True)
rout = rin*(1+uu)
Qp = 2*sp.pi*Eps*V/sp.log(rout/rin)
Ein = Qp/(2*sp.pi*Eps*rin)
ratio = sp.simplify(Ein/(V/(rin*uu)))
print('S2 coax/planar =', ratio, '| minus u/ln(1+u):', sp.simplify(ratio - uu/sp.log(1+uu)))
print('   series =', sp.series(uu/sp.log(1+uu), uu, 0, 3))
print('   ratio>1 at u=1e-3,.1,1,10,1e3:', all(x/mp.log(1+x) > 1 for x in [1e-3, .1, 1, 10, 1e3]))
rho, d, P, kk = sp.symbols('rho d P k', positive=True)
Ts = 2*P/(4*sp.pi*kk*sp.sqrt(rho**2+d**2))
print('S2 steady surface rise =', sp.simplify(Ts), ' FWHM =', [2*s for s in sp.solve(sp.Eq(Ts/Ts.subs(rho, 0), sp.Rational(1, 2)), rho)])
print('   Pmin =', sp.solve(sp.Eq(Ts.subs(rho, 0), sp.Symbol('dTmin', positive=True)), P))
def fwhm(g):
    amp = lambda x: (1/mp.sqrt(1+x*x))*mp.e**(-g*(mp.sqrt(1+x*x)-1))
    return 2*mp.findroot(lambda x: amp(x)-0.5, (0.01, 20), solver='anderson')
print('   FWHM/d for g=0,1,5,10:', [mp.nstr(fwhm(g), 4) for g in (0, 1, 5, 10)], ' 1/e^-5 =', mp.nstr(mp.e**5, 5))
print('   asym 2sqrt(2ln2/g) g=10:', mp.nstr(2*mp.sqrt(2*mp.log(2)/10), 4))
R, mu, D, w = sp.symbols('R mu D omega', positive=True)
Tt = sp.exp(-(1+sp.I)*R/mu)/R
res = sp.simplify((sp.diff(R**2*sp.diff(Tt, R), R)/R**2 - sp.I*w/D*Tt).subs(mu, sp.sqrt(2*D/w)))
print('   heat-eq residual =', res)
# ---------- S3 ----------
r0, tT, tC, tB, eT, eC, eB, Vv, kap, a, b, en, eb = sp.symbols('r0 tT tC tB epsT epsC epsB V kappa a b e_n e_b', positive=True)
r1 = r0+tT; r2 = r1+tC; r3 = r2+tB
Sigma = tT/eT + tC/eC + tB/eB
Slog = sp.log(r1/r0)/eT + sp.log(r2/r1)/eC + sp.log(r3/r2)/eB
Qc = 2*sp.pi*Vv/Slog
E_in_T = Qc/(2*sp.pi*eT*r0)
E_pl_T = Vv/(eT*Sigma)
sub = {tT: kap*r0, tC: a*kap*r0, tB: b*kap*r0, eC: en*eT, eB: eb*eT}
g0 = sp.simplify((E_in_T/E_pl_T).subs(sub))
c1 = sp.simplify(sp.limit(sp.diff(g0, kap), kap, 0))
claimed = (a**2*eb + 2*a*b*en + 2*a*eb + b**2*en + 2*b*en + eb*en)/(2*(a*eb + b*en + eb*en))
print('S3 g0 first-order coeff - claimed =', sp.simplify(c1 - claimed))
x = sp.symbols('x', positive=True); print('   single layer series:', sp.series(x/sp.log(1+x), x, 0, 3))
E_in_B = Qc/(2*sp.pi*eB*r3); E_pl_B = Vv/(eB*Sigma)
gg = sp.simplify((E_in_B/E_pl_B).subs(sub))
cg = sp.factor(sp.simplify(sp.limit(sp.diff(gg, kap), kap, 0)))
print('   g_gate first-order coeff =', cg)
E1T = Qc/(2*sp.pi*eT*r1)
g1 = sp.simplify((E1T/E_pl_T).subs(sub)); c1b = sp.factor(sp.simplify(sp.limit(sp.diff(g1, kap), kap, 0)))
print('   g(r1, TOX side) first-order coeff =', c1b)
print('   c1b*2*(a eb+b en+eb en) - (a^2 eb+2ab en+b^2 en - eb en) =', sp.simplify(c1b*(2*(a*eb+b*en+eb*en)) - (a**2*eb+2*a*b*en+b**2*en-eb*en)))
qc, Qs = sp.symbols('q_c Q_s')
A1c = sp.log(r1/r0)/eT/(2*sp.pi); A2c = (sp.log(r2/r1)/eC + sp.log(r3/r2)/eB)/(2*sp.pi)
qc_sol = sp.solve(sp.Eq(qc*A1c + (qc+Qs)*A2c, 0), qc)[0]
E_ret = qc_sol/(2*sp.pi*eT*r0)
dVth = Qs*A2c
ratio_ret = sp.simplify(E_ret/dVth)
qp, sigma = sp.symbols('qp sigma')
L1 = tT/eT; L2 = tC/eC + tB/eB
qps = sp.solve(sp.Eq(qp*L1 + (qp+sigma)*L2, 0), qp)[0]
ratio_pl = sp.simplify((qps/eT)/(sigma*L2))
g0full = sp.simplify(E_in_T/E_pl_T)
print('S3 retention identity: |coax/planar field-per-dVth| / g0 =', sp.simplify(sp.Abs(ratio_ret/ratio_pl)/g0full), '(1 => exact; both signs negative so ratio itself:', sp.simplify(ratio_ret/ratio_pl/g0full), ')')
Es, Bs = sp.symbols('E B', positive=True)
print('   FN dlnJ/dlnE =', sp.simplify(sp.diff(sp.log(Es**2*sp.exp(-Bs/Es)), Es)*Es))
# ---------- S4 ----------
phi_i, phi_it, C1, W, Id, lam0, Ep, kB, TT, qE, L = sp.symbols('phi_i phi_it C1 W I_d lambda0 E_p k T qE L', positive=True)
lnr = sp.log(C1) + sp.log(L/phi_i) - phi_i/L
lntau = sp.log(W/Id) + phi_it/L
slope = sp.simplify(sp.diff(lntau, L)/sp.diff(lnr, L))
print('S4 dln tau/dln r =', slope, '| + phi_it/(phi_i+L) =', sp.simplify(slope + phi_it/(phi_i+L)))
lam = lam0*sp.tanh(Ep/(2*kB*TT))
vals = {lam0: 1, Ep: 1, kB: 1, TT: 2, qE: 1, phi_i: 1, phi_it: 3, C1: 1, W: 1, Id: 1}
print('   dlam/dT =', sp.N(sp.diff(lam, TT).subs(vals)), ' dlnr/dT =', sp.N(sp.diff(lnr.subs(L, qE*lam), TT).subs(vals)), ' dlntau/dT =', sp.N(sp.diff(lntau.subs(L, qE*lam), TT).subs(vals)))
# ---------- S5 ----------
Dd, Tw, tau0, gam, G, E, QBD, A, B = sp.symbols('D T_w tau0 gamma G E Q_BD A B', positive=True)
for name, tb in {'E': tau0*sp.exp(-gam*E), '1/E': tau0*sp.exp(G/E), 'Qbd': QBD/(A*E**2*sp.exp(-B/E))}.items():
    sol = sp.solve(sp.Eq(Dd*Tw/tb, 1), Tw)[0]; print('S5', name, 'gain =', sp.simplify(sol/tb))
print('   1/4.7, 1/4.1 =', round(1/4.7, 4), round(1/4.1, 4))
ton, toff, tc, te = sp.symbols('ton toff tau_c tau_e', positive=True); n = sp.symbols('n')
a_ = sp.exp(-ton/tc); b_ = sp.exp(-toff/te)
ns = sp.solve(sp.Eq(n, b_*(1-(1-n)*a_)), n)[0]
print('   n* - (1-a)b/(1-ab) =', sp.simplify(ns - (1-a_)*b_/(1-a_*b_)))
npk = sp.simplify(1-(1-ns)*a_); print('   npeak - (1-a)/(1-ab) =', sp.simplify(npk - (1-a_)/(1-a_*b_)))
def npeak(D_, ft):
    A_ = mp.e**(-D_/ft); B_ = mp.e**(-(1-D_)/ft); return (1-A_)/(1-A_*B_)
print('   D=0.5 npeak f*tau=7,70:', mp.nstr(npeak(.5, 7), 5), mp.nstr(npeak(.5, 70), 5), ' rel change', mp.nstr((npeak(.5, 7)-npeak(.5, 70))/npeak(.5, 7), 3))
g = mp.euler; c = 1 + (1-g)**2/(mp.pi**2/6)
print('   Weibull Var(eta)/eta^2*n*beta^2 =', mp.nstr(c, 6), ' sd(ln ratio)*beta*sqrt(n) =', mp.nstr(mp.sqrt(2*c), 6))
print('   logic: pure-duty gain 1/D is independent of f at fixed D')
