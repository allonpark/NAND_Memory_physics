import sys; sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp
D,z,e,E,k,T=sp.symbols('D z e E k T',positive=True)
v=D*z*e*E/(k*T)
e_=sp.Rational('1.602176634e-19'); kB=sp.Rational('1.380649e-23')
for Dcgs in ['1e-12','1e-11','1e-10']:
    Dsi=sp.Rational(Dcgs)*sp.Rational(1,10**4)
    val=v.subs({D:Dsi,z:2,e:e_,E:sp.Integer(10)**8,k:kB,T:300})
    print(Dcgs,sp.N(val,6))
v0=sp.N(v.subs({D:sp.Rational('1e-16'),z:2,e:e_,E:10**8,k:kB,T:300}))
print('ratio lo',1e-5/v0, sp.log(1e-5/v0,10).evalf(), 'ratio hi',1e-4/v0, sp.log(1e-4/v0,10).evalf())
print('D for 1e-5',sp.N(1e-5*kB*300/(2*e_*1e8)*1e4), 'for 1e-4',sp.N(1e-4*kB*300/(2*e_*1e8)*1e4))
