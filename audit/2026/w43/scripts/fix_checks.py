import sys, math, random
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp
print('sympy', sp.__version__)

# ---- F1-1: curvature of ln(rate/E0^2) vs 1/E0 in a coaxial device (route A) ----
B, phi, q, r0, E = sp.symbols('B phi_B q r0 E0', positive=True)
lam = phi/(q*E*r0)
w = sp.symbols('w', positive=True)
R_series = 1 + sp.Rational(2,5)*lam + sp.Rational(4,35)*lam**2
# check series against R(lam) = 3/2 int_0^1 sqrt(1-w) e^{lam w} dw
L = sp.symbols('L', positive=True)
Rint = sp.Rational(3,2)*sp.integrate(sp.sqrt(1-w)*sp.series(sp.exp(L*w),L,0,3).removeO(), (w,0,1))
print('R series check (should be 0):', sp.simplify(sp.expand(Rint) - (1 + sp.Rational(2,5)*L + sp.Rational(4,35)*L**2)))
expo = R_series*B/E          # exponent magnitude in exp(-R B/E0)
u = sp.symbols('u', positive=True)  # u = 1/E0
y = sp.expand(-expo.subs(E, 1/u))   # ln(rate/E0^2) up to a constant
print('ln(rate/E0^2) vs u=1/E0 :', sp.collect(y, u))
print('d2y/du2 =', sp.simplify(sp.diff(y,u,2)), ' (non-zero -> uncorrected 1/E0 plot is curved)')
# corrected abscissa X = R(lam)/E0 makes it exactly linear with slope -B
X = sp.symbols('X')
print('with abscissa X = R(lam)/E0, ln(rate/E0^2) = -B*X  (linear by construction)')
# planar limit
print('planar limit r0->oo of exponent:', sp.limit(expo, r0, sp.oo))

# ---- F2-2: reproduce illustrative median Weibull-plot slopes 1.46/1.73/2.25 ----
t = sp.symbols('t', positive=True)
p, b1, b2, e1, e2, c1, c2 = sp.Rational(3,10), 1, 3, 1, 10, 1, 2
for V in (0,1,2):
    a1, a2 = sp.exp(c1*V), sp.exp(c2*V)
    F = p*(1-sp.exp(-(t*a1/e1)**b1)) + (1-p)*(1-sp.exp(-(t*a2/e2)**b2))
    tm = sp.nsolve(F-sp.Rational(1,2), t, (1e-3, 50), solver='bisect')
    # Weibull-plot slope d ln(-ln(1-F)) / d ln t at median
    s = sp.diff(sp.log(-sp.log(1-F)), t)*t
    print(f'V={V}: median t={float(tm):.4g}, Weibull-plot slope at median = {float(s.subs(t,tm)):.4f}')

# ---- F2-1: Monte Carlo of complete-sample Weibull MLE shape spread ----
def mle_beta(x):
    lx=[math.log(v) for v in x]; n=len(x); b=1.0
    for _ in range(100):
        xb=[v**b for v in x]; S=sum(xb); S1=sum(xb[i]*lx[i] for i in range(n)); S2=sum(xb[i]*lx[i]**2 for i in range(n))
        f=1/b+sum(lx)/n-S1/S; fp=-1/b**2-(S2*S-S1**2)/S**2
        nb=b-f/fp
        if nb<=0: nb=b/2
        if abs(nb-b)<1e-10: b=nb; break
        b=nb
    return b
random.seed(43)
z=1.959964+0.841621
for n in (10,30,100):
    bs=[mle_beta([(-math.log(random.random()))**(1/2.0) for _ in range(n)]) for _ in range(2500)]
    lb=[math.log(v) for v in bs]; ml=sum(lb)/len(lb); sd=math.sqrt(sum((v-ml)**2 for v in lb)/(len(lb)-1))
    ratio_mc=math.exp(z*math.sqrt(2)*sd); ratio_as=math.exp(z*math.sqrt(2)*math.sqrt(6)/math.pi/math.sqrt(n))
    print(f'n={n}: sd(ln b)*sqrt(n)={sd*math.sqrt(n):.3f} (asym 0.780); mean(b_hat)/b={sum(bs)/len(bs)/2:.3f}; detectable ratio MC={ratio_mc:.2f}, asymptotic={ratio_as:.2f}')

# ---- F4-1: Hurkx-type apparent activation energy with / without tau ~ T^-1/2 ----
T, k, Eg, F_, FG0 = sp.symbols('T k E_g F F_G0', positive=True)
FG = FG0*T**sp.Rational(3,2)
ni = T**sp.Rational(3,2)*sp.exp(-Eg/(2*k*T))
Gam = 2*sp.sqrt(3*sp.pi)*(F_/FG)*sp.exp((F_/FG)**2)
for name, tau in (('tau const', 1), ('tau ~ T^-1/2', T**sp.Rational(-1,2))):
    G = ni*Gam/tau
    Ea = sp.simplify(k*T**2*sp.diff(sp.log(G), T))
    print(f'E_a ({name}) =', sp.simplify(sp.expand(Ea)))
# Gamma>>1 limit drops the (F/FG) prefactor-derived -3kT/2 ... print explicit pieces
