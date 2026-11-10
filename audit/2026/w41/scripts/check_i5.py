import sys
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp
from sympy import Rational as R, N, pi, EulerGamma, exp, log
# [1]
for r in (R('1.40'),R('2.03')): print('ratio',r,'variance fraction 1-(1/r)^2=',N(1-1/r**2,4))
bQ,s=sp.symbols('beta_Q sigma',positive=True)
print('predicted ratio bQ=4 sigma=.25:',N(sp.sqrt(1+6*16*R(1,16)/pi**2),5))
# [2]
c=1+6*(1-EulerGamma)**2/pi**2; print('1+6(1-gE)^2/pi^2=',N(c,6),' sqrt=',N(sp.sqrt(c),6),' sd_Q/sd_t at ratios:',N(1/R('1.40'),3),N(1/R('2.03'),3))
# verify Weibull MLE asymptotic variance of ln eta: Fisher info for (eta,beta): Var(ln eta) = (1/(n beta^2))*(1+6(1-gE)^2/pi^2)
# via Fisher information in (mu=ln eta, beta) of Weibull with u=ln x ~ Gumbel-min(mu, 1/beta)
x,mu,b=sp.symbols('x mu b',real=True)
z=sp.symbols('z',real=True)
# standard smallest-extreme: pdf f(z)=exp(z-exp(z)); u=mu+z/b
f=exp(z-exp(z))
# log-lik per obs l = log b + z - exp(z), z=b(u-mu)
# dl/dmu = -b(1-exp(z)) ; dl/db = 1/b + (u-mu)(1-exp(z)) = 1/b + z/b (1-exp(z))
dmu=-b*(1-exp(z)); db=1/b+z/b*(1-exp(z))
E=lambda g: sp.integrate(sp.simplify(g*f),(z,-sp.oo,sp.oo))
I11=sp.simplify(E(dmu**2)); I12=sp.simplify(E(dmu*db)); I22=sp.simplify(E(db**2))
print('I11',I11,'I12',I12,'I22',sp.simplify(I22))
Inv=sp.Matrix([[I11,I12],[I12,I22]]).inv()
print('n*b^2*Var(mu)=',sp.simplify(Inv[0,0]*b**2),' ->',N(sp.simplify(Inv[0,0]*b**2),6))
# [4]
V0,dV,Vx,n_,Gp,tox=sp.symbols('V0 dV V_x n G tox',positive=True)
V=sp.symbols('V',positive=True)
pw=-n_*log(V-Vx); inv=Gp*tox/(V-Vx)
print('curv power',sp.simplify(sp.diff(pw,V,2)),' inverse',sp.simplify(sp.diff(inv,V,2)),' exp:',sp.diff(-V*5,V,2))
def devspan(f_):
    chord=lambda Vv: f_.subs(V,V0-dV/2)+(f_.subs(V,V0+dV/2)-f_.subs(V,V0-dV/2))*(Vv-(V0-dV/2))/dV
    dev=sp.simplify(chord(V0)-f_.subs(V,V0)); span=f_.subs(V,V0+dV/2)-f_.subs(V,V0-dV/2)
    return sp.simplify(dev/span)
e=sp.symbols('epsilon',positive=True)
for nm,f_ in (('power',pw),('inverse',inv)):
    r_=devspan(f_); ser=sp.series(r_.subs(dV,e*(V0-Vx)),e,0,2).removeO(); print(nm,'dev/span ~',sp.simplify(ser),' (leading)')
print('numeric eps=2/39:',N(R(2,39)/8,3),N(R(2,39)/4,3))
# [5]
a2=sp.symbols('a2',positive=True); xs=[R(38),R('38.5'),R(39),R('39.5')]
X=sp.Matrix([[1,xx] for xx in xs]); yv=sp.Matrix([a2*xx**2 for xx in xs])
beta=(X.T*X).inv()*X.T*yv; pred=beta[0]+beta[1]*40; print('held-out error at 40:',sp.simplify(a2*40**2-pred))
# asymmetric design counterexample
xs2=[R(38),R(38),R('38.5'),R('39.5')]
X2=sp.Matrix([[1,xx] for xx in xs2]); y2=sp.Matrix([a2*xx**2 for xx in xs2]); b2=(X2.T*X2).inv()*X2.T*y2
cb=sum(xs2)/4; s2=sum((xx-cb)**2 for xx in xs2)/4
print('asym design: true error',sp.simplify(a2*40**2-(b2[0]+b2[1]*40)),' formula',sp.simplify(a2*((40-cb)**2-s2)))
# [6]
print('8.75/e^(1.4*1.5)=',N(R('8.75')/exp(R('1.4')*R('1.5')),4),' /e^(1.4*2)=',N(R('8.75')/exp(R('1.4')*2),4))
# [3] curvature
E_,B,G,gm=sp.symbols('E B G gamma',positive=True)
lnQ1=-gm*E_+2*log(E_)-B/E_
lnQ2=G/E_+2*log(E_)-B/E_
print('d1',sp.simplify(sp.diff(lnQ1,E_)),' d2',sp.simplify(sp.diff(lnQ1,E_,2)),' vs -2(B+E)/E^3 diff',sp.simplify(sp.diff(lnQ1,E_,2)+2*(B+E_)/E_**3))
print('1/E d1',sp.simplify(sp.diff(lnQ2,E_)-(B+2*E_-G)/E_**2),' d2 diff',sp.simplify(sp.diff(lnQ2,E_,2)+2*(B+E_-G)/E_**3),' G=B:',sp.simplify(lnQ2.subs(G,B)))
# NAND
Ip,r_,r0,r1=sp.symbols('Ip r r0 r1',positive=True)
J=Ip/(2*pi*r_); print('J(r0)/J(r1)=',sp.simplify(J.subs(r_,r0)/J.subs(r_,r1)))
# covariance condition
lI,lt=sp.symbols('lI lt'); vI,vt,cov=sp.symbols('vI vt cov')
print('Var(lnQ)<Var(lnt) <=>', sp.solve(sp.Eq(vt+vI+2*cov,vt),cov))
