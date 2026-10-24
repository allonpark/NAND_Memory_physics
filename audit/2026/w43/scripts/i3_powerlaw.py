# Item 3 (impact ionization power law) -- labeled derivations only.
# Part A uses only values stated in the source (Eg = 1.12 eV, m_c = 4.6 vs 3.5,
#   wavelengths 250/275/350/360/410/476 nm, "argument" thresholds 0.1/0.35, 0.25-0.35)
#   plus the physical constant hc.
# Part B is GENERAL BACKGROUND (not from the paper): power-law rate averaged over an
#   exponential hot-carrier energy distribution, compared with lucky-electron/Chynoweth forms.
import sys
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp

print("sympy", sp.__version__)

# ---------------- Part A: source-value consistency checks ----------------
hc = sp.Rational(123984198, 100000)  # eV*nm (CODATA hc = 1239.84198 eV nm)
Eg = sp.Rational(112, 100)           # eV, stated in source
lam = sp.symbols('lambda', positive=True)
hnu = hc/lam
x = hnu - 2*Eg                        # quantity on Fig.4 axis (hnu - 2Eg, eV)
arg = sp.log(x, 10)                   # hypothesis: "argument" = log10((hnu-2Eg)/eV)

print("\nA1. wavelength -> h*nu, electron excess energy E = h*nu - Eg, x = h*nu - 2Eg, log10(x)")
for L in [250, 275, 350, 360, 410, 476]:
    hv = hnu.subs(lam, L)
    print(f"  {L} nm: h*nu={float(hv):.4f} eV, E=h*nu-Eg={float(hv-Eg):.4f} eV, "
          f"x={float(x.subs(lam, L)):.4f} eV, log10 x={float(arg.subs(lam, L)):.4f}")
print("  check: source pairs (350 nm, argument>0.1) and (275 nm, argument>0.35) are reproduced"
      " if argument = log10((h*nu-2Eg)/eV)")
for a in [sp.Rational(1, 10), sp.Rational(25, 100), sp.Rational(35, 100)]:
    Lsol = sp.solve(sp.Eq(x, 10**a), lam)[0]
    print(f"  argument={float(a):.2f} -> lambda={float(Lsol):.1f} nm, x={float(10**a):.4f} eV")
print(f"  closed-form zero point x=0 -> h*nu = 2Eg = {float(2*Eg):.2f} eV,"
      f" lambda = {float(hc/(2*Eg)):.1f} nm (outside the measured range)")

# A2. Eq.(4) exponentiated (Eq.(3) typeset form UNKNOWN; this is algebra on Eq.(4) only)
m, Ac, X = sp.symbols('m_c A_c x', positive=True)
g = sp.symbols('g', positive=True)
gsol = sp.solve(sp.Eq(sp.log(g/(1-g), 10), m*sp.log(X, 10) - sp.log(Ac, 10)), g)
print("\nA2. g solved from Eq.(4):", gsol, " equals 1/(1 + A_c x^-m)?",
      sp.simplify(gsol[0] - 1/(1 + Ac*X**(-m))) == 0)

# A3. Span check: decades of g/(1-g) over the x-range of the data (476 -> 250 nm)
xlo = x.subs(lam, 476); xhi = x.subs(lam, 250)
for mm in [sp.Rational(46, 10), sp.Rational(35, 10)]:
    dec = mm*sp.log(xhi/xlo, 10)
    print(f"A3. m_c={float(mm)}: decades of g/(1-g) between 476 and 250 nm = {float(dec):.3f}")
print("    (source: g spans four orders of magnitude over the combined data set; m_c=4.6 is consistent)")
# restricted to the closed-form-valid window (476 nm .. argument 0.1)
xv = sp.Integer(10)**sp.Rational(1, 10)
for mm in [sp.Rational(46, 10), sp.Rational(35, 10)]:
    print(f"    m_c={float(mm)}: decades between 476 nm and argument 0.1 = {float(mm*sp.log(xv/xlo,10)):.3f}")
print(f"    difference 4.6 vs 3.5 over full span: {float(sp.Rational(11,10)*sp.log(xhi/xlo,10)):.3f} decades;"
      f" over valid window: {float(sp.Rational(11,10)*sp.log(xv/xlo,10)):.3f} decades")

# ---------------- Part B: general background (NOT from the paper) ----------------
print("\nB. GENERAL BACKGROUND (not from the paper)")
E, Eth, eps, P = sp.symbols('E E_th epsilon P', positive=True)
# Rate above threshold r(E) = P*(E-Eth)^m ; normalized exponential distribution f = exp(-E/eps)/eps
u = sp.symbols('u', positive=True)  # u = E - Eth
avg = sp.integrate(P*u**m*sp.exp(-(u+Eth)/eps)/eps, (u, 0, sp.oo), conds='none')
avg = sp.simplify(avg)
print("B1. <r>(eps) =", avg)
target = P*sp.gamma(m+1)*eps**m*sp.exp(-Eth/eps)
print("    equals P*Gamma(m+1)*eps^m*exp(-Eth/eps)?", sp.simplify(avg/target) == 1)
# m -> 0 : hard threshold (step) = lucky-electron probability
avg0 = sp.integrate(P*sp.exp(-(u+Eth)/eps)/eps, (u, 0, sp.oo))
print("B2. hard-threshold (m=0) limit <r> =", sp.simplify(avg0), " (lucky-electron form with eps = q*lambda*F)")
# log-slope
slope = sp.simplify(sp.diff(sp.log(target), eps)*eps)
print("B3. d ln<r>/d ln eps =", slope)
# integrand peak / mean / sd in u
integrand = u**m*sp.exp(-u/eps)
upk = sp.solve(sp.diff(sp.log(integrand), u), u)
mean_u = sp.simplify(sp.integrate(u*integrand, (u, 0, sp.oo), conds='none')/sp.integrate(integrand, (u, 0, sp.oo), conds='none'))
var_u = sp.simplify(sp.integrate(u**2*integrand, (u, 0, sp.oo), conds='none')/sp.integrate(integrand, (u, 0, sp.oo), conds='none') - mean_u**2)
print("B4. dominant excess energy u=E-Eth: mode =", upk, ", mean =", mean_u, ", variance =", var_u)
# m-sensitivity at fixed eps
dm = sp.simplify(sp.diff(sp.log(target), m))
print("B5. d ln<r>/d m =", dm, "  (digamma + ln eps): shifts prefactor and adds Delta m to the log-slope")

# Field mapping: eps = q*lam_p*F ; F = Vp/l (Vp = V_D - V_Dsat effective drop, l = characteristic length)
q, lp, F, Vp, l, s = sp.symbols('q lambda_p F V_p l s', positive=True)
Isub_ratio = sp.symbols('C1', positive=True)*F**(m+s)*sp.exp(-Eth/(q*lp*F))
print("B6. generic Isub/Id ~ C1*F^(m+s)*exp(-b/F), b = Eth/(q*lambda_p); s = field-profile/integration exponent (model dependent)")
IsV = Isub_ratio.subs(F, Vp/l)
print("    d ln(Isub/Id)/d ln Vp =", sp.simplify(sp.diff(sp.log(IsV), Vp)*Vp))
print("    Hu/Tam-type lucky-electron form corresponds to prefactor exponent 1 (m_c not present)")
# Chynoweth alpha = alpha_inf*exp(-b/F): prefactor exponent 0
# Fraction of log-slope due to m
frac = sp.simplify(m/(m + s + Eth/eps))
print("B7. fraction of log-slope carried by m (with eps=q*lambda_p*F):", frac)
for Rv in [5, 10, 20, 40]:
    for mm in [sp.Rational(46, 10), sp.Rational(35, 10)]:
        print(f"    Eth/eps={Rv}, s=1, m={float(mm)}: total slope={float(mm+1+Rv):.1f}, m-share={float(mm/(mm+1+Rv)):.3f}")
print("    (Eth/eps values are illustrative symbols-to-numbers, NOT from the paper or any device)")

# Bridging window: mode m*eps inside the energy window where the closed form was compared
print("\nB8. bridging condition: mode u* = m*eps inside x-window supported by the closed form")
for label, xa in [("476 nm (lowest x, earlier-publication data)", xlo),
                  ("410 nm (start of this work's CESR range)", x.subs(lam, 410)),
                  ("argument 0.1 (closed-form validity limit)", xv)]:
    print(f"   {label}: x = {float(xa):.4f} eV -> eps = x/4.6 = {float(xa/sp.Rational(46,10)):.4f} eV")
print("   NOTE: identifying the paper's threshold variable with Eth (=Eg in kinetic energy) is an inference.")

# Tail mapping: first-order spread of ln<r> from spread of ln F
sF = sp.symbols('sigma_lnF', positive=True)
print("B9. sigma_ln<r> ~= (m + s + Eth/eps)*sigma_lnF (first order, field-driven case incl. s)")
