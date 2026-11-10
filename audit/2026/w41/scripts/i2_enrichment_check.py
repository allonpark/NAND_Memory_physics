"""Recompute item 2 derivation B (enrichment ratios and hypergeometric tails) with exact SymPy rationals."""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp
from sympy import Rational as R, binomial

N, n = 412, 42
routes = {'polaron': 165, 'induced K': 182, 'native K': 65}
dec = {'stab': {'polaron': 3, 'induced K': 30, 'native K': 9},
       'depth': {'polaron': 7, 'induced K': 29, 'native K': 6}}
print('sympy', sp.__version__)
for d, cnt in dec.items():
    assert sum(cnt.values()) == n, (d, sum(cnt.values()))
    for r, K in routes.items():
        k = cnt[r]
        enr = R(k, n) / R(K, N)
        print(f'{d:5s} {r:10s} k={k:2d}/{n}  overall {K}/{N}  enrichment = {enr} = {sp.N(enr, 6)}')
assert sum(routes.values()) == 412

def hyp_upper(K, k):
    return sum(binomial(K, i) * binomial(N - K, n - i) for i in range(k, min(K, n) + 1)) / binomial(N, n)

def hyp_lower(K, k):
    return sum(binomial(K, i) * binomial(N - K, n - i) for i in range(0, k + 1)) / binomial(N, n)

print('E[induced K in decile] =', sp.N(R(n * 182, N), 6))
print('P(iK>=30) =', sp.N(hyp_upper(182, 30), 4))
print('P(iK>=29) =', sp.N(hyp_upper(182, 29), 4))
print('P(pol<=3) =', sp.N(hyp_lower(165, 3), 4))
print('29/41 =', sp.N(R(29, 41), 5), ' 182/412 =', sp.N(R(182, 412), 5), ' 182/347 =', sp.N(R(182, 347), 5))
print('native K depth enrichment rounded 3 d.p.:', round(float(R(6 * 412, 42 * 65)), 3))
