# Item 5 (W41) framework checks. FRAMEWORK ONLY, not the paper's model.
# Inputs taken from the Crossref abstract: beta_Q/beta_t in [1.40, 2.03]; Weibull voltages 38-40 V;
# calibration 38-39.5 V; k = 1.40 /V; scale ratio 8.75 -> 1.36.
import sys, math, random
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp

print("== [1] beta_Q/beta_t from log-variance (Weibull: Var(ln X) = pi^2/(6 beta^2)) ==")
bQ, bt, s2, c, r = sp.symbols('beta_Q beta_t sigma2 C r', positive=True)
# identity ln Q = ln t + ln Ibar  ->  Var(lnQ) = Var(lnt) + Var(lnI) + 2 Cov(lnI, lnt)
VlnQ = sp.pi**2/(6*bQ**2); Vlnt = sp.pi**2/(6*bt**2)
cov = sp.symbols('Cov', real=True)
cond = sp.simplify(VlnQ - Vlnt)  # <0  <=> beta_Q > beta_t
print("Var(lnQ)-Var(lnt) = Var(lnI) + 2 Cov  ->  beta_Q>beta_t  iff  Cov(lnI,lnt) < -Var(lnI)/2")
print("  i.e. regression slope b = Cov/Var(lnI) of ln t on ln Ibar must satisfy b < -1/2")
# independent Q (intrinsic) and I: ln t = ln Q - ln I -> Var(lnt) = Var(lnQ) + s2
ratio = sp.sqrt(1 + 6*bQ**2*s2/sp.pi**2)
chk = sp.simplify(sp.pi**2/(6*(bQ/ratio)**2) - (VlnQ + s2))
print("independent-Q model: beta_Q/beta_t = sqrt(1 + 6 beta_Q^2 sigma^2/pi^2); check residual =", chk)
frac = 1 - 1/r**2   # share of Var(ln t) removed by passing to Q (independent model)
for rv in (1.40, 2.03):
    print(f"  r={rv}: fraction of Var(ln t) removed = 1-1/r^2 = {float(frac.subs(r,rv)):.3f}; "
          f"sigma_lnI*beta_t = {float(sp.pi/sp.sqrt(6)*sp.sqrt(frac.subs(r,rv))):.3f}")

print("\n== [1b] Monte Carlo check of [1] (stdlib, illustrative parameters, not paper values) ==")
def wb_mle_beta(x):
    lx=[math.log(v) for v in x]; n=len(x)
    def g(b):
        xb=[v**b for v in x]; S=sum(xb)
        return sum(a*l for a,l in zip(xb,lx))/S - 1/b - sum(lx)/n
    lo,hi=0.05,50
    for _ in range(200):
        m=(lo+hi)/2
        if g(m)>0: hi=m
        else: lo=m
    return (lo+hi)/2
random.seed(1)
betaQ=4.0; sig=0.25; N=20000
Q=[random.weibullvariate(1.0,betaQ) for _ in range(N)]
I=[math.exp(random.gauss(0,sig)) for _ in range(N)]
t=[q/i for q,i in zip(Q,I)]
bq=wb_mle_beta(Q); btt=wb_mle_beta(t)
pred=math.sqrt(1+6*betaQ**2*sig**2/math.pi**2)
print(f"  beta_Q=4, sigma_lnI=0.25: MLE beta_Q/beta_t = {bq/btt:.3f}; log-variance prediction = {pred:.3f}")

print("\n== [2] Weibull scale uncertainty (complete-sample MLE, asymptotic) ==")
g = sp.EulerGamma
k2 = sp.nsimplify(1) + 6*(1-g)**2/sp.pi**2
print("  n*beta^2*Var(ln eta_hat) ->", sp.simplify(k2), "=", sp.N(k2,5), "; sd(ln eta_hat) =", sp.N(sp.sqrt(k2),4), "/(beta*sqrt(n))")
for rv in (1.40, 2.03):
    print(f"  equal n: sd_Q/sd_t = beta_t/beta_Q = {1/rv:.3f} (r={rv})")

print("\n== [3] collapse condition for Q_eff = w(V) Q_BD (Weibull per voltage) ==")
q, V, kk = sp.symbols('q V k', positive=True)
eta = sp.Function('eta_Q')(V); beta = sp.Function('beta_Q')(V); w = sp.Function('w')(V)
F = 1 - sp.exp(-(q/(w*eta))**beta)
print("  F_Qeff(q;V) =", F)
print("  dF/dV == 0 for all q  <=>  d(w*eta)/dV = 0 and dbeta/dV = 0")
dF = sp.diff(F, V)
test = sp.simplify(dF.subs({sp.Derivative(beta,V):0}).subs(sp.Derivative(w,V), -w*sp.Derivative(eta,V)/eta))
print("  with dbeta/dV=0 and w'/w = -eta'/eta: dF/dV ->", test)
# exponential weight w = exp(k V): need d ln eta/dV = -k on the whole range
E, gam, B, G, A, tau0 = sp.symbols('E gamma B G A tau0', positive=True)
J = A*E**2*sp.exp(-B/E)   # planar FN current density (textbook)
lnQ_E = sp.expand_log(sp.log(tau0*sp.exp(-gam*E)*J), force=True)
lnQ_1E = sp.expand_log(sp.log(tau0*sp.exp(G/E)*J), force=True)
print("  E-model+FN : d lnQ/dE =", sp.simplify(sp.diff(lnQ_E,E)), "; d2 =", sp.simplify(sp.diff(lnQ_E,E,2)))
print("  1/E-model+FN: d lnQ/dE =", sp.simplify(sp.diff(lnQ_1E,E)), "; d2 =", sp.factor(sp.simplify(sp.diff(lnQ_1E,E,2))))
print("  1/E with G=B: Q_BD =", sp.simplify((tau0*sp.exp(G/E)*J).subs(G,B)), "-> only prefactor E^2 remains")
print("  -> slope of ln Q_BD is not constant in E in either framework: an exponential weight collapses only locally")

print("\n== [4] voltage offset: E = (V - Vx)/tox ==")
Vx, tox, n_, Gp = sp.symbols('V_x t_ox n Gp', positive=True)
for name, f in [("exp ", -gam*(V-Vx)/tox), ("pow ", -n_*sp.log((V-Vx)/tox)), ("1/E ", Gp*tox/(V-Vx))]:
    print("  ", name, "d2 ln t/dV2 =", sp.simplify(sp.diff(f,V,2)))
print("  exponential: curvature 0 for any Vx (offset only shifts the prefactor); power/inverse depend on Vx")

print("\n== [5] narrow-range discriminability: mid-point deviation from the chord, relative to span ==")
V0, dV, eps = sp.symbols('V0 dV epsilon', positive=True)
for name, f, m in [("power", lambda x: -sp.log(x), 1), ("inverse", lambda x: 1/x, 2)]:
    x1, x2 = V0 - dV/2, V0 + dV/2
    dev = sp.Abs((f(x1)+f(x2))/2 - f(V0)); span = sp.Abs(f(x1)-f(x2))
    rel = sp.series(sp.simplify((dev/span).subs(dV, eps*V0)), eps, 0, 2).removeO()
    print(f"  {name}: deviation/span ~ {sp.simplify(rel)}  (expected m*eps/8, m={m})")
    print(f"    eps = 2/39 (38-40 V, Vx=0): {float(rel.subs(eps, sp.Rational(2,39))):.4f}")
print("  with Vx>0, eps = dV/(V0-Vx) is larger (Vx not in abstract)")

print("\n== [6] sign of the extrapolation error of a linear fit of ln(scale) vs V ==")
a0,a1,a2,x,cc = sp.symbols('a0 a1 a2 x c', real=True)
pts = sp.symbols('v1:5', real=True)
f = lambda v: a0 + a1*v + a2*v**2
# least squares line through 4 points; error at x
p0,p1 = sp.symbols('p0 p1')
S = sum((f(v)-(p0+p1*v))**2 for v in pts)
sol = sp.solve([sp.diff(S,p0), sp.diff(S,p1)],[p0,p1], dict=True)[0]
err = sp.simplify(f(x) - (sol[p0]+sol[p1]*x))
vals = {pts[0]:38, pts[1]:sp.Rational(77,2), pts[2]:39, pts[3]:sp.Rational(79,2)}
print("  equally spaced example 38,38.5,39,39.5 (spacing ASSUMED; levels not in abstract):")
print("   error at x=40:", sp.factor(err.subs(vals).subs(x,40)), " -> sign = sign(a2) = sign of curvature")
print("  general quadratic: f(x)-fit(x) = a2*[(x-cbar)^2 - s^2] > 0 for x outside the range when a2>0")
print("  -> 'measured > predicted' at 40 V is what a convex ln(scale)(V) gives, if noise is negligible")

print("\n== [7] simplest reading of the 8.75 -> 1.36 scale ratio (consistency probe) ==")
for span in (sp.Rational(3,2), 2):
    res = 8.75/math.exp(1.40*float(span))
    print(f"  ratio/exp(k*{span} V) = {res:.3f}  (abstract reports 1.36)")
print("  neither simple reading gives 1.36 -> definition of the ratio is UNKNOWN")

print("\n== [8] coaxial contrast (VNAND background, not the paper) ==")
Ip, r0, r1 = sp.symbols("I' r0 r1", positive=True)
Jr = lambda rr: Ip/(2*sp.pi*rr)
print("  steady current per unit length I' through coax: J(r0)/J(r1) =", sp.simplify(Jr(r0)/Jr(r1)), "(fluence per area larger at inner surface)")
