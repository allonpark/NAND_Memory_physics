import sys
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp
from sympy import Rational as R, N
# atomic masses (standard): Si 28.085, N 14.007
mSi,mN=R('28.085'),R('14.007')
M=120*mSi+160*mN
amu=R('1.66053906660')  # g/cm3 * A^3 per amu
def V(rho): return M*amu/rho
for rho in (R('3.15'),R('2.92')): print('rho',rho,'M',N(M,7),'V(A^3)=',N(V(rho),6),' edge',N(V(rho)**R(1,3),5))
print('V ratio %:',N((V(R('2.92'))/V(R('3.15'))-1)*100,4))
V315,V292=V(R('3.15')),V(R('2.92'))
print('spec surf 997/V315*1000=',N(997/V315*1000,5),' 1225/V292*1000=',N(1225/V292*1000,5),' stated 337, 389')
print('void vol',N(R('0.084')*V315,5),N(R('0.126')*V292,5))
print('ratios: void',N(R('12.6')/R('8.4'),4),' surf',N(R(1225,997),5),' Si3c',N(R('0.45')/R('0.12'),4))
print('D1 sum 90+211+195',90+211+195,[N(R(x,496)*100,4) for x in (90,211,195)],' K-like 29+? ,54:',9+45,' 63:',29+34,' fractions sum 100?:',9+45+46,29+34+37)
print('D4 uncapped: ',N(R('0.12')/V315*1e24,4),N(R('0.45')/V292*1e24,4),' e density',N(1/V315*1e24,4),N(1/V292*1e24,4))
kT=R('8.617333262e-5')*300
print('D5 exp(0.4/kT)=',N(sp.exp(R('0.4')/kT),4))
print('D3 diffs depth',[N(a-b,3) for a,b in ((R('3.14'),R('3.25')),(R('3.17'),R('3.34')),(R('2.82'),R('2.87')))],' relax',[N(a-b,3) for a,b in ((R('1.31'),R('1.45')),(R('1.49'),R('1.55')),(R('1.16'),R('1.18')))],' gaps',N(R('3.25')-R('2.87'),3),N(R('3.34')-R('2.87'),3))
# coaxial field ratio t/(a ln(1+t/a))
a,t=sp.symbols('a t',positive=True); V0=sp.Symbol('V0',positive=True)
# planar E=V/t ; coax inner surface E(a)=V/(a ln(1+t/a))
ratio=sp.simplify((V0/(a*sp.log(1+t/a)))/(V0/t))
print('inner ratio',ratio,' limit t/a->0:',sp.limit(ratio.subs(a,1),t,0),' numeric t/a=1:',N(ratio.subs({a:1,t:1}),4))
# outer surface ratio
print('outer ratio at t/a=1:',N((V0/((a+t)*sp.log(1+t/a)))/(V0/t)).subs({a:1,t:1}) if False else N(((1/((1+1)*sp.log(2)))/(1/1)),4))
# 5 pairs/4 pairs excess in i2: skip
print('native K at 2.92 vs 3.15 ratio ',N(R(29,9),3))
print('K-like totals: 9+45=',9+45,' 29+34=',29+34)
