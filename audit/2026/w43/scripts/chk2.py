import sys; sys.stdout.reconfigure(encoding="utf-8")
import sympy as sp, mpmath as mp, math, random
mp.mp.dps=40
def Fb(t,A,B,om,gm,D=1):
    G=(1-mp.e**(-(t/D)**gm))**om; return mp.betainc(A,B,0,G,regularized=True)
def Sb(t,A,B,om,gm,D=1):
    w_=(t/D)**gm; omg=-mp.expm1(om*mp.log1p(-mp.e**(-w_))); return mp.betainc(B,A,0,omg,regularized=True)
def hb(t,A,B,om,gm): return mp.diff(lambda z:Fb(z,A,B,om,gm),t)/Sb(t,A,B,om,gm)
for (A,B,om,gm) in [(2,3,0.5,0.8),(0.5,2,1,1.5),(3,1,2,0.6)]:
    A,B,om,gm=map(mp.mpf,(A,B,om,gm))
    s0=(mp.log(hb(mp.mpf('1e-7'),A,B,om,gm))-mp.log(hb(mp.mpf('1e-8'),A,B,om,gm)))/mp.log(10)
    t_=mp.mpf(6) if gm>1 else mp.mpf(30)
    print("I2 origin slope",mp.nstr(s0,6),"pred",mp.nstr(A*om*gm-1,6),"| tail ratio",mp.nstr(hb(t_,A,B,om,gm)/(B*gm*t_**(gm-1)),6))
tt=mp.mpf('0.7')
print("I2 b=1: F vs G^a:",mp.nstr(Fb(tt,mp.mpf(3),mp.mpf(1),mp.mpf(2),mp.mpf('1.3')),15),mp.nstr(((1-mp.e**(-tt**mp.mpf('1.3')))**2)**3,15))
print("I2 6/pi^2 =",float(6/sp.pi**2),"sd ln b*sqrt n=",float(sp.sqrt(6)/sp.pi),"diff",float(sp.sqrt(12)/sp.pi))
zz=1.959963984540054+0.8416212335729143
c=zz*float(sp.sqrt(12)/sp.pi);print("I2 coef",c,[(n,round(math.exp(c/math.sqrt(n)),3)) for n in (10,30,100)])
def mle_beta(xs):
    lx=[math.log(v) for v in xs]; n=len(xs); mlx=sum(lx)/n
    def f(b):
        xb=[v**b for v in xs]; return sum(q*l for q,l in zip(xb,lx))/sum(xb)-1/b-mlx
    lo,hi=0.05,50.0
    for _ in range(80):
        mid=(lo+hi)/2
        if f(mid)>0: hi=mid
        else: lo=mid
    return (lo+hi)/2
random.seed(3)
for n in (10,30,200):
    bs=[mle_beta([(-math.log(random.random()))**(1/2.0) for _ in range(n)]) for _ in range(2500)]
    lb=[math.log(q) for q in bs]; ml=sum(lb)/len(lb); sd=math.sqrt(sum((q-ml)**2 for q in lb)/(len(lb)-1))
    print("I2 MC complete-sample n",n,"sd(ln beta_hat)*sqrt(n)=",round(sd*math.sqrt(n),3),"(asymptotic 0.780); mean bias of beta_hat",round(sum(bs)/len(bs)/2.0,3))
p,b1,b2,e1,e2,c_,V,X=sp.symbols('p b1 b2 e1 e2 c V X',positive=True)
AF=sp.exp(c_*V)
Fm=lambda t,af:p*(1-sp.exp(-(t*af/e1)**b1))+(1-p)*(1-sp.exp(-(t*af/e2)**b2))
print("I2 mixture equal-accel scale family:",sp.simplify(Fm(X,AF)-Fm(X*AF,1))==0)
u=sp.symbols('u',positive=True)
print("I2 S^2 differs from BGW(2,2) survival:",sp.simplify((1-u**2)**2-(1-(3*u**2-2*u**3)))!=0)
def match(xv):
    S2=(1-(1-mp.e**(-xv))**2)**2
    return mp.findroot(lambda l:1-Fb(xv,mp.mpf(2),mp.mpf(2),mp.mpf(1),mp.mpf(1),l)-S2,0.7)
print("I2 Delta matching at x=.3,2:",mp.nstr(match(mp.mpf('0.3')),8),mp.nstr(match(mp.mpf(2)),8))
# slopes
def wslope(Vv):
    pp,B1,B2,E1,E2,C1,C2=0.3,1.0,3.0,1.0,10.0,1.0,2.0
    F=lambda t:pp*(1-mp.e**(-(t*mp.e**(C1*Vv)/E1)**B1))+(1-pp)*(1-mp.e**(-(t*mp.e**(C2*Vv)/E2)**B2))
    y=mp.findroot(lambda z:F(mp.e**z)-0.5,(-20,10),solver='illinois')
    return mp.diff(lambda z:mp.log(-mp.log(1-F(mp.e**z))),y)
print("I2 slopes at median (writer params, my own implementation):",[mp.nstr(wslope(v),5) for v in (0,1,2)])
# competing risk single stationary point
x=sp.symbols('x',positive=True)
h=0.5/100*(x/100)**(-0.5)+3/10*(x/10)**2
print("I2 bathtub stationary pts:",sp.nsolve(sp.diff(h,x),x,3))
l1,l2,q=sp.symbols('l1 l2 q',positive=True)
Sm=q*sp.exp(-l1*x)+(1-q)*sp.exp(-l2*x)
hm=-sp.diff(Sm,x)/Sm
print("I2 exp-mixture dh/dt num sample:",[float(sp.diff(hm,x).subs({l1:1,l2:5,q:sp.Rational(3,10),x:v})) for v in (0.1,1,3)])
# ----- ITEM 3
hc=1239.84;Eg=1.12
for wl in (476,410,350,275,250):
    xe=hc/wl-2*Eg; print("I3",wl,"nm x=",round(xe,3),"log10x=",round(math.log10(xe),3))
x476=hc/476-2*Eg;x250=hc/250-2*Eg
span=math.log10(x250)-math.log10(x476);print("I3 span",round(span,4),"4.6:",round(4.6*span,3),"3.5:",round(3.5*span,3))
sp1=0.1-math.log10(x476);print("I3 to arg 0.1: diff",round(1.1*sp1,3),"x(0.1)=",round(10**0.1,3))
print("I3 Eh window 4.6:",round(x476/4.6,4),round(10**0.1/4.6,4),"from 410:",round((hc/410-2*Eg)/4.6,4))
E,Eth,Eh,m=sp.symbols('E E_th E_h m',positive=True)
expr=sp.gamma(m+1)*Eh**m*sp.exp(-Eth/Eh)
print("I3 dln<r>/dlnEh:",sp.simplify(sp.diff(sp.log(expr),Eh)*Eh))
mm=sp.Rational(23,5)
chk=sp.integrate((E-Eth)**3*sp.exp(-E/Eh)/Eh,(E,Eth,sp.oo))
print("I3 integer-m check m=3:",sp.simplify(chk-sp.gamma(4)*Eh**3*sp.exp(-Eth/Eh)))
# ----- ITEM 4
n=100;print("I4 95% upper bound:",round(1-0.05**(1/n),4))
T,k,Egp,cc,uu,F=sp.symbols('T k Eg c u F',positive=True)
for texp,name in ((0,"tau T-independent"),(sp.Rational(-1,2),"tau ~ T^-1/2 (writer)")):
    Fg=cc*T**sp.Rational(3,2); ur=F/Fg
    lnG=sp.Rational(3,2)*sp.log(T)-Egp/(2*k*T)-texp*sp.log(T)+sp.log(2*sp.sqrt(3*sp.pi)*ur)+ur**2
    Ea=sp.simplify(k*T**2*sp.diff(lnG,T)).subs(F,uu*Fg)
    print("I4 TAT Ea,",name,":",sp.simplify(Ea))
print("I4 B/E",6.55e6/1.067e5,2.38e7/1.067e5,"exp",math.exp(-6.55e6/1.067e5),math.exp(-2.38e7/1.067e5))
xx=sp.symbols('xx',positive=True)
print("I4 coax g series",sp.series(xx/sp.log(1+xx),xx,0,3))
g_,B_,E_,P_=sp.symbols('g B E P',positive=True)
print("I4 amplification",sp.simplify(sp.log(g_**P_*sp.exp(B_/E_*(1-1/g_)))-sp.log((g_*E_)**P_*sp.exp(-B_/(g_*E_))/(E_**P_*sp.exp(-B_/E_)))))
# ----- ITEM 5
kB=8.617333262e-5
def ni(T_,Nc0=1.6e19,Nv0=2.5e19,Eg0=3.265,al=6.5e-4,be=1300):
    Eg_=Eg0-al*T_**2/(T_+be); Nc=Nc0*(T_/300)**1.5; Nv=Nv0*(T_/300)**1.5
    return Nc,Nv,Eg_,math.sqrt(Nc*Nv)*math.exp(-Eg_/(2*kB*T_))
print("I5 n_i(1600K) Nc,Nv,Eg,ni:",ni(1600))
print("I5 HFFOM",42*38,45.6*22,"Etot",round(555.93+61.93,2),round(342.69+54.45,2),round((617.86-397.14)/617.86*100,2),"Ron %",round(3.6/42*100,2))
print("I5 fields->V",3.48e6*1e-5,1.95e6*1e-5,"ON avg MV/cm",15/1e-5/1e6,"Isc ratio",round(93.21/108.07,4),"Weff red%",round((1-0.33/0.81)*100,1),"J ratio",round((93.21/108.07)/(0.33/0.81),3),"SCWT +%",round((14.5/10.6-1)*100,1),"BV frac",round(1200/1423,3),round(1200/1685,3),"Tmax gap K",round(1580.86-1475.82,2))
