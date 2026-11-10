import sys
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp
mu,p,sd,sn,A,B,g,x=sp.symbols('mu p sigma_d sigma_n A B gamma x',positive=True)
Es2=sp.Symbol('Es2',positive=True)
# D1a: Var = mu*Es2*(p sd^2+(1-p) sn^2)  -> exponent 1/2
V=mu*Es2*(p*sd**2+(1-p)*sn**2)
print('D1a dlnsigma/dlnmu =',sp.simplify(mu*sp.diff(sp.log(V),mu)/2))
# D1b: Var = A mu^g + B mu
V2=A*mu**g+B*mu
e=sp.simplify(mu*sp.diff(sp.log(V2),mu)/2)
xx=A*mu**g/(B*mu)
claim=(g*xx+1)/(2*(xx+1))
print('D1b diff vs claim',sp.simplify(e-claim))
print('limits x->0',sp.limit(claim,x,0) if False else sp.simplify(claim.subs(xx,0)), ' x->oo', sp.limit((g*x+1)/(2*(x+1)),x,sp.oo))
print('gamma for 1/3 dominant:', sp.solve(sp.Eq(g/2,sp.Rational(1,3)),g))
# D1c tail slope: Gaussian tail dx ln... slope in mV/dec: sigma*ln10/(z+1/z) approx; check proportional to sigma at fixed z
z=sp.symbols('z',positive=True); s=sp.symbols('s',positive=True)
Q=sp.erfc(z/sp.sqrt(2))/2
# CDF tail F(v)=Q(v/s); dlog10F/dv = -(1/ln10)*phi(z)/(s*Q(z))  -> slope = s*ln10*Q/phi
phi=sp.exp(-z**2/2)/sp.sqrt(2*sp.pi)
print('slope(z)/s =',sp.simplify(sp.log(10)*Q/phi), '; numeric z=3.7:', sp.N((sp.log(10)*Q/phi).subs(z,3.7)), ' approx ln10/(z+1/z)=',sp.N(sp.log(10)/(3.7+1/3.7)))
# D2 coaxial amplitude
r0,t1,eps=sp.symbols('r0 t1 epsilon',positive=True)
u=t1/r0
ratio=r0*sp.log((r0+t1)/r0)/eps/(t1/eps)
print('D2 ratio vs ln(1+u)/u:',sp.simplify(ratio-sp.log(1+u)/u))
# planar-ratio <1
uu=sp.symbols('uu',positive=True)
print(' ln(1+u)/u <1 for u>0: derivative sign', sp.simplify(sp.diff(sp.log(1+uu)/uu,uu)), ' numeric u=.5,2:', sp.N(sp.log(1.5)/.5), sp.N(sp.log(3)/2))
# multilayer: r0*sum ln(r_{i+1}/r_i)/e_i / sum t_i/e_i <1: each ln(1+t_i/r_i)<t_i/r_i < t_i/r0 since r_i>=r0
# D3 annular
rf,T,nv,ns,L=sp.symbols('r_f T n_v n_s L',positive=True)
t=T/rf
Nb=nv*sp.pi*((rf+T)**2-rf**2)*L
Ni=ns*2*sp.pi*(rf+T)*L
cl=sp.simplify(T*sp.diff(Nb,T)/Nb - 2*(1+t)/(2+t)); print('D3 bulk dlnN/dlnT minus claim',sp.simplify(cl))
print(' d lnN/d ln rf - 2/(2+t):',sp.simplify(rf*sp.diff(Nb,rf)/Nb - 2/(2+t)))
print(' interface dlnN/dlnT - t/(1+t):',sp.simplify(T*sp.diff(Ni,T)/Ni - t/(1+t)))
tq=sp.symbols('tq',positive=True); print(' limits bulk t->0,t->oo:',sp.limit(2*(1+tq)/(2+tq),tq,0),sp.limit(2*(1+tq)/(2+tq),tq,sp.oo))
# D4 fixed density
a_L=-sp.Rational(1,4); a_T=-1
# N ~ L (both bulk and interface), dlnN/dlnL=1 ; delta ∝ N^{1/3} L^{-1/4}
print('D4 L exponent fixed density:', sp.Rational(1,3)*1+a_L, ' sqrt law:', sp.Rational(1,2)+a_L)
tt=sp.symbols('t',positive=True)
bulkT=sp.simplify(sp.Rational(1,3)*2*(1+tt)/(2+tt)-1)
intT=sp.simplify(sp.Rational(1,3)*tt/(1+tt)-1)
print(' T total bulk',sp.factor(bulkT),' claim -(t+4)/(3(t+2)):',sp.simplify(bulkT+(tt+4)/(3*(tt+2))))
print(' T total interface',sp.factor(intT),' claim -(2t+3)/(3(t+1)):',sp.simplify(intT+(2*tt+3)/(3*(tt+1))))
print(' bulk range t->0,oo:',bulkT.subs(tt,0),sp.limit(bulkT,tt,sp.oo),' interface:',intT.subs(tt,0),sp.limit(intT,tt,sp.oo))
# D5: delta ∝ Vf^{-1/4}, Vf=pi Rf^2 L -> Rf^{-1/2} L^{-1/4}
Rf,Lw=sp.symbols('R_f L_WL',positive=True)
Vf=sp.pi*Rf**2*Lw
d=Vf**sp.Rational(-1,4)
print('D5 delta exponent Rf:',sp.simplify(Rf*sp.diff(sp.log(d),Rf)),' L:',sp.simplify(Lw*sp.diff(sp.log(d),Lw)))
# single-source data: T_ox,T_ctn,T_box sum 0.9 trivial; tail depth 1e-4
print('1/10000=',1/10000)
