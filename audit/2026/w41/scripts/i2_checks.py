# i2 checks: arXiv:2610.06173 (Cottom & Olsson). Source values only + labeled derivations.
import sys
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp
print('sympy', sp.__version__)
R = sp.Rational

print('\n== A. Arithmetic consistency of SOURCE_REPORTED counts ==')
pol, ind, nat, other = 165, 182, 65, 3
print('A1 routes sum', pol+ind+nat, '(source: 412); +unassigned', pol+ind+nat+other, '(source: 415)')
print('A2 Si4 precursors pol+ind =', pol+ind, '(source 347); Si3 endpoints ind+nat =', ind+nat, '(source 247)')
print('A3 182/347 =', sp.N(R(182,347)*100, 5), '% (source 52.4)')
print('A4 30/42 =', sp.N(R(30,42)*100,5), '; 3/42 =', sp.N(R(3,42)*100,5), '; 29/42 =', sp.N(R(29,42)*100,5),
      '; 182/412 =', sp.N(R(182,412)*100,5), '; 165/412 =', sp.N(R(165,412)*100,5), '; 65/412 =', sp.N(R(65,412)*100,5))
print('A5 decile composition stab 3+30+9 =', 3+30+9, '; depth 7+29+6 =', 7+29+6, '; decile size ceil(412/10)=', sp.ceiling(R(412,10)))
print('A6 exclusion criteria 14+15+7+9 =', 14+15+7+9, 'vs 40 excluded -> surplus memberships', 14+15+7+9-40,
      '(Methods: "Five pairs met multiple criteria"; Table S1: "four pairs meet more than one criterion")')
print('A7 robustness note: 29/41 =', sp.N(R(29,41)*100,5), '%; ceil((412-6)/10)=', sp.ceiling(R(406,10)))
print('A8 455-40 =', 455-40)

print('\n== B. Enrichment and hypergeometric tail (OUR DERIVATION; null = 42 traps drawn at random from 412) ==')
def hyp_ge(N,K,n,k):
    return sum(sp.binomial(K,i)*sp.binomial(N-K,n-i) for i in range(k, min(K,n)+1))/sp.binomial(N,n)
def hyp_le(N,K,n,k):
    return sum(sp.binomial(K,i)*sp.binomial(N-K,n-i) for i in range(0, k+1))/sp.binomial(N,n)
N, n = 412, 42
for lab,K,k in [('induced-K, upper stabilisation decile',182,30),('induced-K, deepest spectral decile',182,29)]:
    print('B', lab, ': enrichment', sp.N(R(k,n)/R(K,N),4), '; P(X>=%d)='%k, sp.N(hyp_ge(N,K,n,k),3), '; expected', sp.N(R(n*K,N),4))
for lab,K,k in [('polaron, upper stabilisation decile',165,3),('polaron, deepest spectral decile',165,7)]:
    print('B', lab, ': enrichment', sp.N(R(k,n)/R(K,N),4), '; P(X<=%d)='%k, sp.N(hyp_le(N,K,n,k),3), '; expected', sp.N(R(n*K,N),4))
for lab,K,k in [('native-K, upper stabilisation decile',65,9),('native-K, deepest spectral decile',65,6)]:
    print('B', lab, ': enrichment', sp.N(R(k,n)/R(K,N),4), '; expected', sp.N(R(n*K,N),4))

print('\n== C. Source identity check: int_0^inf ||(e^{-tL}-e^{-2tL}) D^{1/2} U||_F^2 dt/t^2 = (10 ln2 - 6 ln3) Q_D ==')
t, lam = sp.symbols('t lambda', positive=True)
I = sp.integrate((sp.exp(-lam*t)-sp.exp(-2*lam*t))**2/t**2, (t,0,sp.oo))
I = sp.simplify(I)
print('C1 scalar integral per eigenvalue lambda:', I, '; equals lambda*(10ln2-6ln3)?', sp.simplify(I - lam*(10*sp.log(2)-6*sp.log(3)))==0)
print('C2 coefficient numeric', sp.N(10*sp.log(2)-6*sp.log(3), 6))
# D^{1/2} L D^{1/2} = D - A on a small weighted graph, so tr(U^T (D-A) U) = sum_edges w_ij |u_i-u_j|^2
w12,w23,w13 = sp.symbols('w12 w23 w13', positive=True)
A = sp.Matrix([[0,w12,w13],[w12,0,w23],[w13,w23,0]])
D = sp.diag(*[sum(A.row(i)) for i in range(3)])
Dm = sp.diag(*[1/sp.sqrt(D[i,i]) for i in range(3)]); Dp = sp.diag(*[sp.sqrt(D[i,i]) for i in range(3)])
L = sp.eye(3) - Dm*A*Dm
print('C3 D^1/2 L D^1/2 - (D-A) =', sp.simplify(Dp*L*Dp - (D-A)))
u = sp.Matrix(sp.symbols('u1 u2 u3'))
QD = w12*(u[0]-u[1])**2 + w23*(u[1]-u[2])**2 + w13*(u[0]-u[2])**2
print('C4 u^T(D-A)u - Q_D =', sp.expand((u.T*(D-A)*u)[0] - QD))

print('\n== D. GENERAL BACKGROUND (not from the paper): harmonic configuration-coordinate model ==')
k_, g_, q = sp.symbols('k g q', positive=True)
# charged-state energy E-(q) = k q^2/2 - g q (linear coupling); neutral E0(q) = k q^2/2
q_min = sp.solve(sp.diff(k_*q**2/2 - g_*q, q), q)[0]
Erel = sp.simplify(-(k_*q_min**2/2 - g_*q_min))
level_drop = sp.simplify(g_*q_min)   # occupied level eps(q) = eps0 - g q
print('D1 relaxation energy E_rel =', Erel, '; occupied-level drop at relaxed geometry =', level_drop, '; ratio =', sp.simplify(level_drop/Erel))
# thermal vs optical ionization (equal curvature): E_opt(from relaxed charged) = E_T + E_rel(neutral side)
ET, Er = sp.symbols('E_T E_rel', positive=True)
print('D2 equal-curvature: E_opt = E_T + E_rel  =>  E_T = E_opt - E_rel (symbolic only)')
# Marcus-type barrier, symmetric hop between equivalent sites
lamr, dG = sp.symbols('lambda_r DeltaG', real=True)
x = sp.symbols('x', real=True)
Ea = sp.simplify(((lamr+dG)**2/(4*lamr)))
print('D3 Marcus barrier E_a = (lambda_r + DeltaG)^2/(4 lambda_r); symmetric hop DeltaG=0 ->', Ea.subs(dG,0))
# emission time ratio
kB, T, nuA, nuB, EA, EB = sp.symbols('k_B T nu_A nu_B E_A E_B', positive=True)
tauA = sp.exp(EA/(kB*T))/nuA; tauB = sp.exp(EB/(kB*T))/nuB
print('D4 tau_A/tau_B =', sp.simplify(tauA/tauB))
# demarcation energy
tt, nu = sp.symbols('t nu', positive=True)
Ed = kB*T*sp.log(nu*tt)
print('D5 demarcation energy E_d = k_B T ln(nu t); dE_d/dlnt =', sp.simplify(sp.diff(Ed, tt)*tt), '; dE_d/dln nu =', sp.simplify(sp.diff(Ed,nu)*nu))

print('\n== E. Coaxial bridging (textbook Gauss law; symbolic only) ==')
r, Qp, eps, rin, rout = sp.symbols("r Q' epsilon r_in r_out", positive=True)
E = Qp/(2*sp.pi*eps*r)
dV = sp.integrate(E, (r, rin, rout))
print('E1 dV over a layer =', sp.simplify(dV))
# trapped sheet at radius rc in nitride (eps_N), blocking layer (eps_B) out to gate rg; channel-side reference
rc, rn, rg, eN, eB = sp.symbols('r_c r_n r_g epsilon_N epsilon_B', positive=True)
dVth = Qp/(2*sp.pi)*(sp.log(rn/rc)/eN + sp.log(rg/rn)/eB)
print('E2 |dVth| for sheet at r_c (nitride outer radius r_n, gate r_g) =', dVth)
print('E3 d|dVth|/dr_c =', sp.simplify(sp.diff(dVth, rc)), '(negative: charge nearer the gate shifts Vth less)')
