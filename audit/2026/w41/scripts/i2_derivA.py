# Derivation A for item 2 (arXiv:2610.06173v1): internal arithmetic of reported counts.
import sys
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp
from sympy import Rational as R
print('sympy', sp.__version__)
def pct(a, b):
    v = R(a, b) * 100
    return f"{a}/{b} = {v} = {sp.N(v, 6)} %  -> {float(v):.1f} %"
print('A1 routes 165+182+65 =', 165+182+65, '; +3 unassigned =', 165+182+65+3, '; 455-40 =', 455-40)
print('A2', pct(182, 347))
print('A3', pct(182, 412), '|', pct(165, 412))
print('A4', pct(30, 42), '|', pct(3, 42), '|', pct(29, 42))
print('A5 stab decile 3+30+9 =', 3+30+9, '; depth decile 7+29+6 =', 7+29+6)
print('A6 14+15+7+9 =', 14+15+7+9, '; excess over 40 =', 14+15+7+9-40)
print('A7', pct(29, 41))
