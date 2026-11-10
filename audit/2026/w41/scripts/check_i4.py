import sys
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp
from sympy import Rational as R, N, log, exp, gamma, oo
print('VO=Hf3/8:',[N(R(x)/8,4) for x in ('7.04','7.68','8.56')])
print('1.39/0.51=',N(R('1.39')/R('0.51'),4),' 2/216=',N(R(2,216)*100,4),'%')
print('E*d: 4.2*6/10=',R('4.2')*6/10,' 4.2*8/10=',R('4.2')*8/10,' 4.0:',[R('4.0')*d/10 for d in (6,7,8)],' 10y',R('3.84')*6/10,R('3.52')*8/10,' gain',N(R('3.84')/R('3.52')-1,4))
print('8/6=',N(R(8,6),4),' 8/7=',N(R(8,7),4),' EBD ratios 1.266,1.141 -> VBD',N(R('1.266')*6/8,4),N(R('1.141')*7/8,4))
# tau mean life
b,tau=sp.symbols('beta tau',positive=True)
mean=tau*gamma(1+1/b); print('mean life Weibull tau*Gamma(1+1/beta):',mean,' =tau iff beta=1:',sp.simplify(mean.subs(b,1)))
# TDC tail
x,al=sp.symbols('x alpha',positive=True)
F=1-(1+x/al)**(-al); W=sp.log(-sp.log(1-F)); Wc=sp.log(al*sp.log(1+x/al))
print('W identity:',sp.simplify(sp.expand_log(W-Wc,force=True)))
ser=sp.series(Wc,x,0,3).removeO(); print('series',sp.simplify(ser - (sp.log(x)-x/(2*al)+5*x**2/(24*al**2))))
slope=sp.simplify(x*sp.diff(Wc,x)); print('slope dW/dlnx =',slope,' claim x/((al+x)ln(1+x/al)) diff:',sp.simplify(slope-x/((al+x)*sp.log(1+x/al))))
print(' limits x->0:',sp.limit(slope,x,0),' x->oo:',sp.limit(slope.subs(al,2),x,oo))
# xp ratio TDC/Weibull: Weibull F=1-exp(-x) -> x_W=-ln(1-p); TDC: x = al*((1-p)^(-1/al)-1)
import mpmath as mp
for a_ in (1,2,5):
    for p in (mp.mpf('1e-5'),mp.mpf('0.99')):
        xW=-mp.log(1-p); xT=a_*((1-p)**(-1/mp.mpf(a_))-1)
        print(' alpha',a_,'p',p,'ratio',mp.nstr(xT/xW,6))
# gamma mixture
lam=sp.symbols('lambda',positive=True); k=al
pdf=al**al*lam**(al-1)*exp(-al*lam)/gamma(al)
S=sp.integrate(sp.simplify(pdf*exp(-lam*x)),(lam,0,oo),conds='none')
print('gamma mixture survival:',sp.simplify(S),' vs (1+x/al)^-al:',sp.simplify(S-(1+x/al)**(-al)))
print(' mean,var of lambda: 1, 1/alpha (shape al, rate al)')
# a0 bound
g6,g8,b6,b8=sp.symbols('g6 g8 b6 b8',positive=True)
a06_a08=sp.simplify((g6*6/b6)/(g8*8/b8)); print('a0 ratio:',a06_a08,' claim (3/4)(g6/g8)(b8/b6) diff',sp.simplify(a06_a08-R(3,4)*(g6/g8)*(b8/b6)),' bound if g6<=g8,b6>b8: <',R(3,4))
# coax ratio at t/r =1
print('coax inner ratio at t/rin=1:',N(1/log(2),4))
# censoring: 10^10 lower bound; quick check: nothing
