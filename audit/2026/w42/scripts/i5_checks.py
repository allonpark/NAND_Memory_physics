# i5 (arXiv 2610.16438) derivation checks.
# NOTE: the pinned sympy venv (venv_sympy) was NOT found in the scratchpad on 2026-10-28,
# and no package was installed. All checks below use the Python standard library only
# (math, cmath) with closed forms and a dense numerical scan. Run: python -I i5_checks.py
import sys, math, cmath
sys.stdout.reconfigure(encoding='utf-8')

print('Python', sys.version.split()[0], '(stdlib only; sympy unavailable)')

# D1: frequency of tau = 250 ns (source value) relative to the source window 1 kHz - 1 MHz
tau = 250e-9
f_tau = 1/(2*math.pi*tau)
print('D1 f = 1/(2*pi*tau) for tau=250 ns: %.4g Hz' % f_tau)
print('D1 omega*tau at f=1 MHz: %.4f ; at f=1 kHz: %.4g' % (2*math.pi*1e6*tau, 2*math.pi*1e3*tau))

# D2: conductance-method line shapes (Nicollian-Goetzberger textbook forms, no fluctuation)
# single level:  (Gp/w)/(q Dit) = x/(1+x^2), x = w*tau  -> peak at x=1, value 0.5
# continuum:     (Gp/w)/(q Dit) = ln(1+x^2)/(2x)        -> peak where d/dx = 0
def single(x): return x/(1+x*x)
def cont(x): return math.log(1+x*x)/(2*x)
xs = [10**(k/20000) for k in range(-40000, 40001)]  # 1e-2 .. 1e2
xm1 = max(xs, key=single); xm2 = max(xs, key=cont)
print('D2 single-level peak x=%.4f value=%.4f' % (xm1, single(xm1)))
print('D2 continuum peak x=%.4f value=%.4f' % (xm2, cont(xm2)))
# analytic condition for continuum peak: 2x^2/(1+x^2) = ln(1+x^2); bisection
lo, hi = 1.0, 3.0
g = lambda x: 2*x*x/(1+x*x) - math.log(1+x*x)
for _ in range(200):
    mid = (lo+hi)/2
    if g(lo)*g(mid) <= 0: hi = mid
    else: lo = mid
print('D2 continuum peak by bisection x*=%.6f, value=%.6f' % (lo, cont(lo)))
print('D2 if tau=250 ns and continuum (no fluctuation) shape: f_peak = x*/(2 pi tau) = %.4g Hz' % (lo/(2*math.pi*tau)))

# D3: areal equivalent of the apparent volumetric shallow-state DOS over 4.5 nm (source assumption: uniform)
t = 4.5e-7  # cm
for N in (1e18, 1e19):
    print('D3 N=%.0e eV^-1 cm^-3 * 4.5 nm = %.3g eV^-1 cm^-2' % (N, N*t))

# D4: accumulation/depletion apparent Dit ratio range from source ranges
dep = (9e11, 12e11); acc = (2.8e12, 3.1e12)
print('D4 ratio min=%.3f max=%.3f' % (acc[0]/dep[1], acc[1]/dep[0]))

# D5: distributed RC line (channel sheet resistance R_sh per square, gate-dielectric C_ox per area,
# width W, length L), fed from both ends (S and D shorted). Admittance:
#   Y = 2 W sqrt(j w C_ox / R_sh) tanh( sqrt(j w R_sh C_ox) L/2 )
# Normalize: y = Y/(w C_ox W L) ; x = w R_sh C_ox (L/2)^2 ; then y = tanh(sqrt(j x))/sqrt(j x) * (1/1)*... check:
# Y/(j w C_ox W L) = tanh(s)/s with s = sqrt(j x). Gp/w normalized = Re(Y)/(w C_tot) = Re(j*tanh(s)/s)
def gpw_line(x):
    s = cmath.sqrt(1j*x)
    return (1j*cmath.tanh(s)/s).real
xs5 = [10**(k/5000) for k in range(-10000, 15001)]
xp = max(xs5, key=gpw_line)
print('D5 distributed line: peak of (Gp/w)/C_tot at x = w R_sh C_ox (L/2)^2 = %.4f, value %.4f' % (xp, gpw_line(xp)))
# lumped series R-C for comparison: (Gp/w)/C = x/(1+x^2) with x = w R C -> peak 1, 0.5
# check L-scaling: f_peak = xp/(2 pi R_sh C_ox (L/2)^2) -> ratio for L -> 2L is 1/4
print('D5 f_peak(2L)/f_peak(L) = %.4f (independent of W)' % ((1/(2*1)**2)/(1/1**2)))
# check small-x limit: Re(j tanh(s)/s) ~ x/3 (s^2 = j x; tanh(s)/s ~ 1 - s^2/3)
print('D5 small-x check gpw(1e-4)/1e-4 = %.5f (expect 1/3)' % (gpw_line(1e-4)/1e-4))

# D6: coaxial vs planar normalization (symbolic forms checked numerically by series)
# gate outside a channel of outer radius r0, dielectric thickness t_ox, u = t_ox/r0
# C per unit channel-surface area: eps/(r0 ln(1+u));  planar: eps/t_ox ; ratio = u/ln(1+u)
for u in (1e-3, 1e-2, 1e-1):
    r = u/math.log(1+u)
    print('D6 u=%.0e: u/ln(1+u)=%.6f  1+u/2=%.6f' % (u, r, 1+u/2))
# annular channel of thickness t_ch with outer radius r0, v = t_ch/r0:
# volume per unit outer-surface area = (r0^2-(r0-t_ch)^2)/(2 r0) = t_ch (1 - v/2)
for v in (0.1, 0.5):
    r0 = 1.0; tch = v*r0
    vol_per_area = (r0**2-(r0-tch)**2)/(2*r0)
    print('D6 v=%.1f: vol/area / t_ch = %.6f ; 1-v/2 = %.6f' % (v, vol_per_area/tch, 1-v/2))

# D7: grain-boundary area per volume for cubic grains of edge d: each grain has 6 d^2 faces,
# each shared by 2 grains -> 3 d^2 per d^3 -> S_v = 3/d. Apparent volumetric density = N_GB * S_v.
d = 2.0
print('D7 cubic grains S_v*d = %.3f (expect 3)' % ((6*d*d/2)/d**3*d))
print('done')
