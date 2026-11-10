# i5 (arXiv 2610.16438) SymPy re-derivation of D1-D7 (supersedes stdlib-only i5_checks.py; results must agree)
# Run: venv_sympy\Scripts\python.exe -I i5_sympy.py
import sys
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp, mpmath
print('sympy', sp.__version__, 'mpmath', mpmath.__version__)

x = sp.symbols('x', positive=True)
tau = sp.Rational(250, 10**9)

# D1
f_tau = 1/(2*sp.pi*tau)
print('D1 1/(2 pi tau) =', sp.N(f_tau, 6), 'Hz')
print('D1 w*tau at 1 MHz =', sp.N(2*sp.pi*10**6*tau, 6), '; at 1 kHz =', sp.N(2*sp.pi*10**3*tau, 6))

# D2 single level and continuum (textbook, no fluctuation)
single = x/(1+x**2)
cont = sp.log(1+x**2)/(2*x)
xs1 = sp.solve(sp.diff(single, x), x)
print('D2 single-level peak x =', xs1, 'value =', [single.subs(x, v) for v in xs1])
xs2 = sp.nsolve(sp.diff(cont, x), x, 2)
print('D2 continuum peak x* =', sp.N(xs2, 7), 'value =', sp.N(cont.subs(x, xs2), 7))
print('D2 f_peak = x*/(2 pi tau) =', sp.N(xs2/(2*sp.pi*tau), 6), 'Hz')

# D3 areal equivalent
t = sp.Rational(45, 10**8)  # 4.5 nm in cm
for N in (sp.Integer(10)**18, sp.Integer(10)**19):
    print('D3', N, '* 4.5 nm =', sp.N(N*t, 4), 'eV^-1 cm^-2')

# D4 ratio range
print('D4 min =', sp.N(sp.Rational(28, 12), 4), ' max =', sp.N(sp.Rational(31, 9), 4))

# D5 distributed RC line fed from both ends: normalized Gp/w/C_tot = Re(j tanh(s)/s), s = sqrt(j x)
s = sp.sqrt(sp.I*x)
g = sp.I*sp.tanh(s)/s
gser = sp.series(sp.I*sp.tanh(sp.sqrt(sp.I*x))/sp.sqrt(sp.I*x), x, 0, 3).removeO()
print('D5 small-x series of j tanh(s)/s =', sp.expand(gser), ' (real part leading term x/3)')
gre = lambda xv: mpmath.re(1j*mpmath.tanh(mpmath.sqrt(1j*xv))/mpmath.sqrt(1j*xv))
xpk = mpmath.findroot(lambda xv: mpmath.diff(gre, xv), 2.5)
print('D5 peak x = w R_sh C_ox (L/2)^2 =', mpmath.nstr(xpk, 6), ' value =', mpmath.nstr(gre(xpk), 6))
L = sp.symbols('L', positive=True); Rsh, Cox = sp.symbols('R_sh C_ox', positive=True)
fpk = xpk/(2*sp.pi*Rsh*Cox*(L/2)**2)
print('D5 f_peak(2L)/f_peak(L) =', sp.simplify(fpk.subs(L, 2*L)/fpk))

# D6 coaxial
u, v, r0, tox, eps, tch = sp.symbols('u v r0 t_ox epsilon t_ch', positive=True)
Ccoax = eps/(r0*sp.log(1+tox/r0)); Cpl = eps/tox
ratio = sp.simplify((Ccoax/Cpl).subs(tox, u*r0))
print('D6 C_coax/C_planar =', ratio, ' series:', sp.series(ratio, u, 0, 3))
volpa = sp.simplify((r0**2-(r0-tch)**2)/(2*r0))
print('D6 volume per outer area =', sp.factor(volpa), ' / t_ch =', sp.simplify(volpa/tch).subs(tch, v*r0).simplify())

# D7 cubic grains
d = sp.symbols('d', positive=True)
print('D7 S_v =', sp.simplify((6*d**2/2)/d**3))
print('done')
