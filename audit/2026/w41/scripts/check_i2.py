import sys
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp
from sympy import Rational as R, log, integrate, oo, binomial, N
lam,t=sp.symbols('lambda t',positive=True)
I=integrate((sp.exp(-lam*t)-sp.exp(-2*lam*t))**2/t**2,(t,0,oo))
print('integral =',sp.simplify(I),' vs lam*(10ln2-6ln3):',sp.simplify(sp.expand_log(I-lam*(10*log(2)-6*log(3)),force=True)), ' coef',N(10*log(2)-6*log(3),6))
# numeric check of integral
import mpmath as mp
f=lambda x:(mp.e**(-x)-mp.e**(-2*x))**2/x**2
print(' numeric',mp.quad(f,[0,1,10,mp.inf]))
# matrix identity on random graph
import random
n=6; A=sp.zeros(n,n)
for i in range(n):
    for j in range(i+1,n):
        w=sp.Rational(random.randint(1,9),10); A[i,j]=w;A[j,i]=w
Dm=sp.diag(*[sum(A.row(i)) for i in range(n)])
L=sp.eye(n)-Dm**R(-1,2)*A*Dm**R(-1,2)
U=sp.Matrix(n,3,lambda i,j:random.randint(-5,5))
QD=sum(A[i,j]*(U.row(i)-U.row(j)).norm()**2 for i in range(n) for j in range(i+1,n))
print(' Q_D vs Tr(U^T(D-A)U):',sp.simplify(QD-(U.T*(Dm-A)*U).trace()))
M=Dm**R(1,2)*L*Dm**R(1,2); print(' D^1/2 L D^1/2 == D-A:',sp.simplify(M-(Dm-A))==sp.zeros(n,n))
# hypergeometric
def tail(K,n,N_,k,upper=True):
    num=lambda x: binomial(K,x)*binomial(N_-K,n-x)/binomial(N_,n)
    if upper: return sum(num(x) for x in range(k,min(K,n)+1))
    return sum(num(x) for x in range(0,k+1))
p1=tail(182,42,412,30); p2=tail(182,42,412,29); p3=tail(165,42,412,3,upper=False)
print('P(iK>=30)=',N(p1,6),' P(iK>=29)=',N(p2,6),' P(pol<=3)=',N(p3,6))
print('enrich iK stab',N(R(30,42)/R(182,412),6),' depth',N(R(29,42)/R(182,412),6),' pol',N(R(3,42)/R(165,412),6),' nK stab',N(R(9,42)/R(65,412),6),' nK depth',N(R(6,42)/R(65,412),6),' =412/455?',R(6,42)/R(65,412)==R(412,455), N(R(412,455),6))
print('expectation 42*182/412 =',N(R(42*182,412),6))
print('counts 165+182+65',165+182+65,' 182/347',N(R(182,347)*100,4),' 182/412',N(R(182,412)*100,4),' 165/412',N(R(165,412)*100,4),' 29/41',N(R(29,41)*100,4),' 30/42',N(R(30,42)*100,4),' 3/42',N(R(3,42)*100,3),' 29/42',N(R(29,42)*100,3))
print('exclusions 14+15+7+9=',14+15+7+9,' 455-40=',455-40,' excess',14+15+7+9-40)
# decile of 412 -> 41.2 ~42? 
print('412/10=',412/10)
# energy bookkeeping
q,k,qm,Dv,ec=sp.symbols('q k q_m D_v e_c',real=True)
E0=sp.Rational(1,2)*k*q**2
Em=sp.Rational(1,2)*k*(q-qm)**2 + sp.Symbol('c')   # anion surface, linear coupling, equal curvature
c=sp.Symbol('c')
Dvert=E0.subs(q,0)+ec-Em.subs(q,0)
Estab=Em.subs(q,0)-Em.subs(q,qm)
ET=E0.subs(q,0)+ec-Em.subs(q,qm)
Dopt=E0.subs(q,qm)+ec-Em.subs(q,qm)
print('ET-(Dv+Es)=',sp.simplify(ET-(Dvert+Estab)),' Dopt-(Dv+2Es)=',sp.simplify(Dopt-(Dvert+2*Estab)),' level drop = dE-/dq*...: ',sp.simplify(sp.diff(Em,q).subs(q,0)*(-qm)/Estab) )
# coaxial
Qp,eN,eB,rc,rn,rg=sp.symbols("Qp eN eB rc rn rg",positive=True)
V=Qp/(2*sp.pi)*(log(rn/rc)/eN+log(rg/rn)/eB)
print("d|dV|/drc =",sp.simplify(sp.diff(V,rc)),' claim -Qp/(2 pi eN rc):',sp.simplify(sp.diff(V,rc)+Qp/(2*sp.pi*eN*rc)))
# poisson/binomial relative spread
Nn,f=sp.symbols('N f',positive=True)
print('rel spread binomial sqrt((1-f)/(N f)):',sp.simplify(sp.sqrt(Nn*f*(1-f))/(Nn*f)-sp.sqrt((1-f)/(Nn*f))))
# Marcus
lr,dG=sp.symbols('lambda_r dG',real=True)
Ea=(lr+dG)**2/(4*lr); print('Marcus dG=0:',Ea.subs(dG,0))
# demarcation
nu,kT,tt,E1=sp.symbols('nu kT tt E1',positive=True)
Ed=kT*log(nu*tt); print('dEd/dln t, dEd/dln nu:',sp.simplify(tt*sp.diff(Ed,tt)),sp.simplify(nu*sp.diff(Ed,nu)))
