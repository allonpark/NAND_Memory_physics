# Item 5 (W43) consistency checks and labelled derivations. Inputs = values printed in the source text only.
# Run: venv_sympy\Scripts\python.exe -I i5_checks.py
import sys
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp

R = sp.Rational
print("sympy", sp.__version__)

# [1] Internal arithmetic checks of reported pairs (baseline SG -> SG-PS)
Ron0, Ron1 = R(42), R('45.6'); Qgd0, Qgd1 = R(38), R(22)
print("[1a] Ron change =", sp.N((Ron1/Ron0-1)*100, 4), "% (source: +8.6%)")
print("[1b] HF-FOM = Ron*Qgd:", Ron0*Qgd0, ",", sp.N(Ron1*Qgd1, 6), "(source 1596 / 1003.2)")
Eon0, Eon1, Eoff0, Eoff1 = R('555.93'), R('342.69'), R('61.93'), R('54.45')
Et0, Et1 = Eon0+Eoff0, Eon1+Eoff1
print("[1c] Etot =", sp.N(Et0, 6), "/", sp.N(Et1, 6), "; reduction", sp.N((1-Et1/Et0)*100, 5), "% (source 617.86/397.14, 35.72%)")
E0, E1 = R('3.48'), R('1.95')
print("[1d] corner peak field ratio =", sp.N(E1/E0, 4), "; reduction", sp.N((1-E1/E0)*100, 4), "%")
W0, W1 = R('0.81'), R('0.33')
I0, I1 = R('108.07'), R('93.21')
print("[1e] W_eff reduction", sp.N((1-W1/W0)*100, 4), "% (source ~59%); Isc ratio", sp.N(I1/I0, 4),
      "; implied mean |Jn| over W_eff ratio (I1/W1)/(I0/W0) =", sp.N((I1/W1)/(I0/W0), 4),
      "[DERIVATION: assumes all current inside W_eff on one cutline; not source-reported]")
t0, t1 = R('10.6'), R('14.5')
print("[1f] SCWT change", sp.N((t1/t0-1)*100, 4), "%")
BV0, BV1 = 1423, 1685
print("[1g] BV change", sp.N((R(BV1)/BV0-1)*100, 4), "%")

# [2] Source's own 1600 K intrinsic-carrier argument, using only source-printed parameters
T, kB = sp.symbols('T k_B', positive=True)
kB_eV = R('8.617333262e-5')  # Boltzmann constant, eV/K (CODATA)
NC300, NV300 = R('1.6e19'), R('2.5e19')
Eg0, alpha, beta = R('3.265'), R('6.5e-4'), R(1300)
NC = NC300*(T/300)**R(3, 2); NV = NV300*(T/300)**R(3, 2)
Eg = Eg0 - alpha*T**2/(T+beta)
ni = sp.sqrt(NC*NV)*sp.exp(-Eg/(2*kB*T))
sub = {T: 1600, kB: kB_eV}
print("[2] at 1600 K: NC =", sp.N(NC.subs(sub), 4), "NV =", sp.N(NV.subs(sub), 4),
      "Eg =", sp.N(Eg.subs(sub), 5), "eV, ni =", sp.N(ni.subs(sub), 4), "cm^-3 (source: 1.97e20, 3.08e20, 2.691 eV, ~1.42e16)")
print("[2] ni(1600 K)/N_drift(1e16) =", sp.N(ni.subs(sub)/R('1e16'), 4))

# [3] Planar MOS oxide field: uniform-field equivalent oxide voltage (DERIVATION, planar 1D, no crowding)
tox_cm = R('0.1e-4')  # 0.1 um
for lab, E in (("SG", E0), ("SG-PS", E1)):
    print(f"[3] {lab}: E_ox*t_ox = {sp.N(E*R(10)**6*tox_cm, 4)} V  [1D uniform-field equivalent only; actual corner field is 2D-crowded]")
Vgs_on = 15
print(f"[3b] on-state planar average field Vgs/t_ox = {sp.N(Vgs_on/tox_cm/R(10)**6, 3)} MV/cm  [DERIVATION; ignores V_FB, surface potential, poly depletion, oxide charge]")
print("[3c] blocking voltage / BV:", sp.N(R(1200)/1423, 3), "(SG),", sp.N(R(1200)/1685, 3), "(SG-PS)  [DERIVATION]")
# Gauss law at oxide/semiconductor interface (normal components, no interface charge): eps_ox E_ox = eps_s E_s
eox, es, Es, Qit = sp.symbols('epsilon_ox epsilon_s E_s Q_it', positive=True)
Eox_expr = sp.solve(sp.Eq(eox*sp.Symbol('E_ox') - es*Es, Qit), sp.Symbol('E_ox'))[0]
print("[3] interface normal-field relation: E_ox =", Eox_expr)

# [4] Coaxial contrast (VNAND), symbolic: E(r)=V/(r ln(b/a)); at inner radius vs planar V/t, t=b-a
a, t, V, r = sp.symbols('a t V r', positive=True)
Ecoax_a = V/(a*sp.log((a+t)/a))
ratio = sp.simplify(Ecoax_a/(V/t))
print("[4] E_coax(r=a)/E_planar =", ratio, "; limit t/a->0:", sp.limit(ratio.subs(t, sp.Symbol('x')*a), sp.Symbol('x'), 0))
x = sp.Symbol('x', positive=True)
g = x/sp.log(1+x)
print("[4] d/dx [x/ln(1+x)] > 0 check at x=1:", sp.N(sp.diff(g, x).subs(x, 1), 4), "(field enhancement grows with t/a)")
# per-layer drop in a coaxial stack
Qp, ei, rin, rout = sp.symbols("Q' epsilon_i r_in r_out", positive=True)
Ei = Qp/(2*sp.pi*ei*r)
dVi = sp.integrate(Ei, (r, rin, rout))
print("[4] dV_i =", sp.simplify(dVi))
