import sys, math
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp
from sympy import symbols, Rational, log, exp, sqrt, simplify, diff, limit, pi, oo, I, sin, cos, tanh, nsolve
import mpmath as mp
print('sympy', sp.__version__)
def chk(name, ok, extra=''):
    print(('PASS ' if ok else 'FAIL ') + name, extra)

print('== ITEM 1 ==')
r1 = (1 - Rational('0.44')/Rational('24.28'))*100
r2 = (Rational('774.770') - Rational('435.362'))/Rational('774.770')*100
r3 = (Rational('435.362') - Rational('435.008'))/Rational('435.008')*100
print('98.19 ->', float(r1), '| 43.81 ->', float(r2), '| 0.08 (gap rel. Ideal) ->', float(r3))
chk('98.19%', abs(float(r1)-98.19) < 0.005); chk('43.81%', abs(float(r2)-43.81) < 0.005); chk('0.08%', abs(float(r3)-0.08) < 0.005)
Trl = list(range(-40, 121, 20)); Tp5 = [-40, 0, 40, 80, 120]
chk('5x9=45', len(Trl) == 9 and len(Trl)*len(Tp5) == 45, 'levels %d' % len(Trl))
print('unordered swapped pairs among 5 Tp levels:', sum(1 for a_ in Tp5 for b_ in Tp5 if a_ < b_), '; max|dT| on grid', max(abs(b_-a_) for a_ in Trl for b_ in Tp5))
Tp, Tr, T1, T2, T3, T0, a, b = symbols('Tp Tr T1 T2 T3 T0 a b', real=True)
g = sp.Function('g')
dmu = lambda tp, tr: g(tr) - g(tp)
chk('antisymmetry (arbitrary g)', simplify(dmu(T1, T2) + dmu(T2, T1)) == 0)
chk('additivity (arbitrary g)', simplify(dmu(T1, T2) + dmu(T2, T3) - dmu(T1, T3)) == 0)
gq = lambda T: -a*(T-T0) - b*(T-T0)**2
chk('quadratic g -> -a dT - b dT (Tp+Tr-2T0)', simplify(sp.expand(gq(Tr)-gq(Tp)) - sp.expand(-a*(Tr-Tp) - b*(Tr-Tp)*(Tp+Tr-2*T0))) == 0)
u, r0, t, eps, Qp, rr, sigma = symbols('u r0 t epsilon Qp r sigma', positive=True)
E = Qp/(2*pi*eps*rr)
dV = sp.integrate(E, (rr, r0, r0+t))
chk('dV = Q/(2 pi eps) ln(rout/rin)', simplify(dV - Qp/(2*pi*eps)*log((r0+t)/r0)) == 0)
f = log(1+u)/u
ratio = simplify(dV.subs(Qp, sigma*2*pi*r0)/(sigma*t/eps))
chk('coax/planar dV for sheet sigma at r0 = ln(1+u)/u, u=t/r0', simplify(ratio.subs(t, u*r0) - f) == 0)
print("f'(u) =", simplify(diff(f, u)))
chk('f<1 for u>0', all(float((u-log(1+u)).subs(u, v)) > 0 for v in (1e-3, .1, 1, 10)))
chk('f->1 as u->0', limit(f, u, 0) == 1)
sig_c = symbols('sigma_c', positive=True)
chk('D3 E(r0)/E_planar = 1+u (all image charge on channel side)', simplify(((sig_c*2*pi*(r0+t))/(2*pi*eps*r0)/(sig_c/eps)).subs(t, u*r0) - (1+u)) == 0)
print('opposite radius dependence: df/dr0 at t=1,r0=2 =', float(sp.diff(f.subs(u, t/r0), r0).subs({t: 1, r0: 2})), '(>0); d(1+t/r0)/dr0 =', float(diff(1+t/r0, r0).subs({t: 1, r0: 2})), '(<0)')
s0, sk, dT, m, z = symbols('sigma0 sigma_k dT m z', positive=True)
sol = sp.solve(sp.Eq(z*sqrt(s0**2 + sk**2*dT**2), m), dT)
chk('D4 |dT|* = sqrt((m/z)^2 - s0^2)/sk', simplify(sol[0] - sqrt((m/z)**2 - s0**2)/sk) == 0, str(sol))
print('large-dT: sres/(sk dT) ->', limit(sqrt(s0**2 + sk**2*dT**2)/(sk*dT), dT, oo))

print('== ITEM 2 ==')
ra, rb, tt, eG, eI = symbols('ra rb tt epsilon_GBL epsilon_IL', positive=True)
gaa = simplify((Qp/(2*pi*eI*ra))/(Qp/(2*pi*eG*rb)))
caa = simplify((Qp/(2*pi*eI*rb))/(Qp/(2*pi*eG*ra)))
print('GAA E_IL/E_GBL =', gaa, '| CAA =', caa)
chk('geometric factors reciprocal', simplify((gaa*eI/eG)*(caa*eI/eG) - 1) == 0)
chk('rb/ra = 1+t/ra ; ra/rb = 1 - t/(ra+t)', simplify((ra+tt)/ra - (1+tt/ra)) == 0 and simplify(ra/(ra+tt) - (1 - tt/(ra+tt))) == 0)
rm = symbols('rm', positive=True)
print('literal CAA reading (inner face of IL / outer face of GBL at the common interface rm):', simplify((Qp/(2*pi*eI*rm))/(Qp/(2*pi*eG*rm))), '-> no geometric factor at all')
rc2, t2 = symbols('rc t2', positive=True)
chk('VFB coax/planar = ln(1+u)/u, u=t/rc', simplify(((sigma*rc2*log((rc2+t2)/rc2)/eps)/(sigma*t2/eps)).subs(t2, u*rc2) - f) == 0)
VG0, s, c, F, d, n, DP = symbols('VG0 s c F d n DP')
VTf = lambda nn: (VG0 + s*nn) - c - F*d
chk('ISPP steady-state slope 1', simplify((VTf(n+1)-VTf(n))/s) == 1)
print('with extra VT term DP per pulse slope =', simplify(((VTf(n+1)+DP*(n+1)) - (VTf(n)+DP*n))/s))
tsp, dVWL, EBD, gam, tau0, Fld = symbols('tsp dVWL EBD gamma tau0 Fld', positive=True)
chk('fixed dV: d ln tBD/d ln tsp = gamma dV/tsp', simplify(diff(log(tau0) - gam*dVWL/tsp, tsp)*tsp - gam*dVWL/tsp) == 0)
chk('fixed field: tBD independent of tsp', diff(log(tau0) - gam*Fld, tsp) == 0)
chk('dm/dtsp = EBD/dVWL', simplify(diff(EBD*tsp/dVWL, tsp) - EBD/dVWL) == 0)
print('== ITEM 3 ==')
h, dl = symbols('h d', positive=True)
Qf = lambda x: sp.erfc(x/sqrt(2))/2
phi = lambda x: exp(-x**2/2)/sqrt(2*pi)
Eoff = Qf(h+dl) + Qf(h-dl)
ser = sp.series(Eoff, dl, 0, 4).removeO()
coef = ser.coeff(dl, 2)/ser.coeff(dl, 0)
target = h*phi(h)/(2*Qf(h))
chk('retry cost coefficient = h phi(h)/(2 Q(h))', all(abs(float((coef-target).subs(h, v))) < 1e-12 for v in (0.5, 1.7, 3.1)), 'at h=2: %.6f vs %.6f' % (float(coef.subs(h,2)), float(target.subs(h,2))))
mua, mub, sa, sb = symbols('mu_a mu_b sigma_a sigma_b', positive=True)
Vopt = (sb*mua + sa*mub)/(sa+sb)
chk('dVopt/dmu_a', simplify(diff(Vopt, mua) - sb/(sa+sb)) == 0)
chk('dVopt/dsigma_a', simplify(diff(Vopt, sa) - sb*(mub-mua)/(sa+sb)**2) == 0)
r0_, tT, tB, eT, eB, dVth = symbols('r0 tT tB epsilon_T epsilon_B dVth', positive=True)
r1_ = r0_ + tT; r2_ = r1_ + tB
CT = 2*pi*eT/log(r1_/r0_); CB = 2*pi*eB/log(r2_/r1_)
ET = (dVth*CB)*CT/(CT+CB)/(2*pi*eT*r0_)
claim = dVth/(r0_*(log(r1_/r0_) + (eT/eB)*log(r2_/r1_)))
vals = {r0_: 3, tT: 1, tB: 2, eT: 3.9, eB: 7, dVth: 1}
chk('E_T(r0) formula', abs(float((ET-claim).subs(vals))) < 1e-12, '%.6f' % float(ET.subs(vals)))
x, aa, e = symbols('x a e', positive=True)
G2 = ((x + e*aa*x)/(log(1+x) + e*log(1 + aa*x/(1+x))))
G2s = sp.simplify(sp.series(G2, x, 0, 2).removeO())
claimG = 1 + x*(1 + 2*e*aa + e*aa**2)/(2*(1 + e*aa))
print('G first-order series:', G2s)
print('item formula 1 + x(1+2ea+ea^2)/[2(1+ea)] (ea read as product e*a); series minus claim =', sp.simplify(G2s-claimG))
for ev, av in [(0.5, 1.0), (0.557, 2.0), (2.0, 0.5)]:
    xv = 0.001
    print('  e=%s,a=%s: exact G-1 = %.3e; series = %.3e; item formula = %.3e' % (ev, av, float(G2.subs({e:ev,aa:av,x:xv}))-1, float((G2s-1).subs({e:ev,aa:av,x:xv})), float((claimG-1).subs({e:ev,aa:av,x:xv}))))
print('G(x) for e=0.557,a=2:', [round(float(G2.subs({e: 0.557, aa: 2, x: v})), 5) for v in (0.01, 0.1, 0.5, 1, 2)])
A, tau, aT, t1, t2x, kap, stol = symbols('A tau aT t1 t2 kappa s', positive=True)
sol = sp.solve(sp.Eq(kap*A*(log(1+aT*t2x/tau) - log(1+aT*t1/tau)), stol), t2x)[0]
chk('reuse interval', simplify(sol - t1 - (tau/aT + t1)*(exp(stol/(kap*A)) - 1)) == 0)
C = 160
print('rel SE sqrt(2/(C-1)) =', math.sqrt(2/(C-1)), '| 1-0.05^(1/C) =', 1-0.05**(1/C), '| 1-0.051/C (wrong reading if superscript lost) =', 1-0.051/C)
Ab, Abp, Aw, Awr, aw, awr, gt, kk = symbols('Ab Abp Aw Awr aw awr gt kk')
print('additive:', simplify(-kk*((Ab+Aw)-(Ab+Awr)-(Abp+Aw)+(Abp+Awr))*gt), '| multiplicative:', sp.factor(-kk*(Ab*aw-Ab*awr-Abp*aw+Abp*awr)*gt))

print('== ITEM 4 ==')
kB = 8.617333262e-5
T3v = [111.0, 79.3, 61.8, 58.1, 53.0]; Tc = [25, 55, 85, 105, 135]
def slope(idx):
    xs_ = [1/(kB*(Tc[i]+273.15)) for i in idx]; ys_ = [math.log(T3v[i]) for i in idx]
    mx = sum(xs_)/len(xs_); my = sum(ys_)/len(ys_)
    return sum((p-mx)*(q-my) for p, q in zip(xs_, ys_))/sum((p-mx)**2 for p in xs_)
print('Ea low =', slope([0, 1, 2]), ' high =', slope([2, 3, 4]))
chk('Ea 0.08997/0.03880', abs(slope([0,1,2])-0.08997) < 2e-5 and abs(slope([2,3,4])-0.03880) < 2e-5)
print('tau0 per decade factors:', 157.1/98.0, 330.1/157.1, '| HSE06 gap diff', 2.85-2.0)
q_ = 1.602176634e-19; kBJ = 1.380649e-23; Tk = 300.0; Ef = 1e8
for Dc in (1e-10, 1e-11, 1e-12):
    v = 2*q_*(Dc*1e-4)/(kBJ*Tk)*Ef
    print('D=%g cm2/s -> v=%.3e m/s ; 2 ms travel = %.3g nm' % (Dc, v, v*2e-3*1e9))
v_low = 2*q_*1e-16/(kBJ*Tk)*Ef
print('Einstein drift at D=1e-12 cm2/s:', v_low, '| 1e-5/v =', 1e-5/v_low, '=', math.log10(1e-5/v_low), 'decades below 1e-5;', math.log10(1e-4/v_low), 'decades below 1e-4')
N_, tdl, bet, tau_, tp_ = symbols('N td beta tau tp', positive=True)
Gf = sp.Function('G')
Dl = -Gf(N_**bet*tdl/tau_)
chk('discriminant ratio = beta', simplify(simplify(diff(Dl, N_)*N_/(diff(Dl, tdl)*tdl)) - bet) == 0)
print('wall-clock dlnX/dln td =', simplify(diff(log(N_**bet*(tp_+tdl)/tau_), tdl)*tdl))
Rf = sp.Function('R'); gg = sp.Function('g')
print('recovery model dDelta/dln td =', diff(-gg(N_*tp_) + Rf(tdl), tdl)*tdl)
th0, th = symbols('theta0 theta', positive=True)
print('int cos*sin =', sp.integrate(cos(th)*sin(th), (th, 0, th0)))
V_, rin, rout = symbols('V rin rout', positive=True)
Qv = sp.solve(sp.Eq(Qp/(2*pi*eps)*log(rout/rin), V_), Qp)[0]
chk('E(r)=V/[r ln(rout/rin)]', simplify(Qv/(2*pi*eps*rr) - V_/(rr*log(rout/rin))) == 0)

print('== ITEM 5 ==')
tau_s = 250e-9
print('1/(2 pi tau) =', 1/(2*math.pi*tau_s), ' w*tau at 1 MHz =', 2*math.pi*1e6*tau_s, ' at 1 kHz =', 2*math.pi*1e3*tau_s)
w = symbols('w', positive=True)
cont = log(1+w**2)/(2*w); single = w/(1+w**2)
wc = nsolve(diff(cont, w), w, 2.0); ws = nsolve(diff(single, w), w, 1.0)
print('continuum peak w*tau =', wc, 'height', cont.subs(w, wc).evalf(), '| single-level', ws, single.subs(w, ws).evalf())
print('continuum-form peak frequency (tau=250ns) =', float(wc)/(2*math.pi*tau_s), 'Hz')
chk('D3 4.5e11..4.5e12', abs(1e18*4.5e-7-4.5e11) < 1 and abs(1e19*4.5e-7-4.5e12) < 10)
print('D4 ratios', 2.8e12/1.2e12, 3.1e12/9e11)
mp.mp.dps = 25
gnum = lambda x_: mp.re(mp.sqrt(1j*x_)*mp.tanh(mp.sqrt(1j*x_))/x_)
xs = [mp.mpf(v)/100 for v in range(1, 3000)]
best = max(xs, key=gnum)
print('distributed RC (both ends driven), Re[sqrt(jx)tanh(sqrt(jx))]/x peak at x ~', best, '(x = omega*Rsh*Cox*(L/2)^2)')
yy = sp.Symbol('y')
print('sqrt(y)tanh(sqrt(y)) series:', sp.series(sp.sqrt(yy)*sp.tanh(sp.sqrt(yy)), yy, 0, 4))
Cs = eps/(r0*log(1+u))
print('Cs_coax/Cs_planar =', simplify(Cs/(eps/(u*r0))), '; series', sp.series(u/log(1+u), u, 0, 2))
tch, v_ = symbols('tch v', positive=True)
chk('annulus volume per outer surface = tch(1-v/2)', simplify(((pi*(r0**2-(r0-tch)**2))/(2*pi*r0)).subs(tch, v_*r0) - v_*r0*(1-v_/2)) == 0)
chk('u/ln(1+u) * ln(1+u)/u = 1', simplify((u/log(1+u))*(log(1+u)/u)) == 1)
