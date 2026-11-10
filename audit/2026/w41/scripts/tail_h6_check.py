# W41-H6 scope check (tail): ratios from item 4 derivations (ii) and (iii)
import sys
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp
from sympy import Rational as R
print('sympy', sp.__version__)
V6 = R(384,100)*6/10   # 3.84 MV/cm * 6 nm -> V
V8 = R(352,100)*8/10   # 3.52 MV/cm * 8 nm -> V
print('V10y(6nm) =', V6, float(V6), ' V10y(8nm) =', V8, float(V8))
print('ratio V6/V8 =', sp.nsimplify(V6/V8), float(V6/V8))
print('field gain 3.84/3.52 - 1 =', float(R(384,352)-1))
# (iii) TZDB V_BD ratios from E_BD ratios 1.266 and 1.141
print('VBD 6/8 =', float(R(1266,1000)*6/8), ' VBD 7/8 =', float(R(1141,1000)*7/8))
