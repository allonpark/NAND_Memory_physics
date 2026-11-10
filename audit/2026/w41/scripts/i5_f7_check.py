# F7: exactness of error = a2[(x-cbar)^2 - s^2] for a straight-line LS fit to a quadratic
import sys
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp
from sympy import Rational as R
a0,a1,a2,x = sp.symbols('a0 a1 a2 x')
def check(levels, xv):
    n=len(levels); c=sum(levels)/n; s2=sum((v-c)**2 for v in levels)/n; m3=sum((v-c)**3 for v in levels)/n
    y=[a0+a1*v+a2*v**2 for v in levels]
    b=sum((v-c)*(yy) for v,yy in zip(levels,y))/sum((v-c)**2 for v in levels); a=sum(y)/n-b*c
    err=sp.simplify(a0+a1*xv+a2*xv**2-(a+b*xv)); formula=sp.simplify(a2*((xv-c)**2-s2))
    print(levels,'x=',xv,'exact err =',err,' formula =',formula,' m3 =',m3,' exact-formula =',sp.simplify(err-formula))
check([R(38),R(77,2),R(39),R(79,2)], R(40))
check([R(38),R(38),R(77,2),R(79,2)], R(40))
# general: exact - formula = -a2*m3/s2*(x-c)
v=sp.symbols('v1:5'); n=4
c=sum(v)/n; s2=sum((vi-c)**2 for vi in v)/n; m3=sum((vi-c)**3 for vi in v)/n
y=[a2*vi**2 for vi in v]; b=sum((vi-c)*yi for vi,yi in zip(v,y))/(n*s2); a=sum(y)/n-b*c
print('general exact-formula + a2*m3/s2*(x-c) =', sp.simplify(a2*x**2-(a+b*x) - a2*((x-c)**2-s2) + a2*m3/s2*(x-c)))
