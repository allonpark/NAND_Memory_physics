import sys; sys.stdout.reconfigure(encoding="utf-8")
import sympy as sp, mpmath as mp, random, math
print("sympy",sp.__version__)
x,a,e,lam,w=sp.symbols('x a e lam w',positive=True)
VoverQ=(sp.log(1+x)+sp.log((1+x+a*x)/(1+x))/e)
E0=1/VoverQ
Epl=1/(x+a*x/e)
g0=sp.simplify(E0/Epl)
s=sp.series(g0,x,0,2).removeO()
writer=1+x*(a**2+2*a+e)/(2*(a+e))
print("I1 g0 first-order matches writer:",sp.simplify(s-writer)==0)
nside=sp.series(g0/(1+x),x,0,2).removeO()
print("I1 N/A nitride-side matches:",sp.simplify(nside-(1+x*(a**2-e)/(2*(a+e))))==0)
gate=sp.series(g0/(1+x+a*x),x,0,2).removeO()
print("I1 gate-side matches:",sp.simplify(gate-(1-x*(a**2+2*a*e+e)/(2*(a+e))))==0)
Rs=sp.series(sp.Rational(3,2)*sp.integrate(sp.sqrt(1-w)*sp.series(sp.exp(lam*w),lam,0,4).removeO(),(w,0,1)),lam,0,3)
print("R series:",Rs)
mp.mp.dps=30
def Rnum(l): return mp.mpf(3)/2*mp.quad(lambda ww: mp.sqrt(1-ww)*mp.e**(l*ww),[0,1])
def Rdirect(l): return mp.quad(lambda r: mp.sqrt(1-mp.log(r)/l),[1,mp.e**l])/(l*mp.mpf(2)/3)
for l in (0.05,0.3,1.0): print("R numeric (subst) vs direct r-integral",l,mp.nstr(Rnum(l),12),mp.nstr(Rdirect(l),12))
def g0n(xv,av,ev):
    return (1+av/ev)/((math.log(1+xv)+math.log(1+av*xv/(1+xv))/ev)/xv)
def Rf(lv,N=300):
    return 1.5*sum(math.sqrt(1-(i+0.5)/N)*math.exp(lv*(i+0.5)/N) for i in range(N))/N
random.seed(1); mx=-1; viol=0; gv=0; cnt=0
for _ in range(40000):
    xv=10**random.uniform(-3,1.5); av=10**random.uniform(-2,1); ev=10**random.uniform(-1,1.3)
    lv=random.uniform(0,math.log(1+xv))
    g=g0n(xv,av,ev); r=Rf(lv)/g
    mx=max(mx,r); cnt+=1
    if r>=1 or g<=1: viol+=1
    if g/(1+xv+av*xv)>=1: gv+=1
print("I1 grid n=",cnt,"max R/g0 =",mx,"violations:",viol,"gate-side ratio>=1 count:",gv)
for xv in (1,5,20,100):
    for av,ev in ((0.1,0.1),(1,1),(5,20)):
        lv=math.log(1+xv); print(" x",xv,"a",av,"e",ev,"R/g0 at lam=ln(1+x):",round(Rf(lv,4000)/g0n(xv,av,ev),4))
r0,tN,tA,rc,eN,eA,Q=sp.symbols('r0 t_N t_A r_c eps_N eps_A Q',positive=True)
dV=Q/(2*sp.pi)*(sp.log((r0+tN)/rc)/eN+sp.log((r0+tN+tA)/(r0+tN))/eA)
print("I1 dVth/drc:",sp.simplify(sp.diff(dV,rc)))
xc=sp.symbols('x_c',positive=True)
lim=sp.limit((dV.subs(rc,r0+xc)*2*sp.pi*r0/Q),r0,sp.oo)
print("I1 planar limit (times sigma-normalisation):",sp.simplify(lim))
