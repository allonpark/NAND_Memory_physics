"""W43 item 4: generic BTBT (Kane-type) vs trap-assisted (Hurkx-type) background checks.
General textbook background, NOT the paper's model (the paper's Eq.1 was not readable).
Only source numbers used: B_Ge = 6.55e6 V/cm, B_Si = 2.38e7 V/cm, E_peak = 1.067e5 V/cm (trap-free, x = 22.14 nm).
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp

E, B, P, A, E0, g, T, k, Eg, F, c, x = sp.symbols('E B P A E0 g T k E_g F c x', positive=True)
dEgdT = sp.Symbol('dEg_dT')  # sign left free; Si/Ge: negative (textbook)

print('== 1. Local Kane-type generation G = A (E/E0)^P exp(-B/E)')
G = A*(E/E0)**P*sp.exp(-B/E)
sens = sp.simplify(sp.diff(sp.log(G), E)*E)
print('d lnG / d lnE =', sens)
assert sp.simplify(sens - (P + B/E)) == 0

print('\n== 2. Field-ratio amplification R(g) = G(gE)/G(E)')
R = sp.simplify(G.subs(E, g*E)/G)
print('R =', R)
target = g**P*sp.exp(B/E*(1-1/g))
assert sp.simplify(sp.log(R) - sp.log(target)) == 0
dlnR = sp.simplify(sp.diff(sp.log(target), g))
print('d lnR/dg =', dlnR, '  (>0 for g>0: positive terms only)')

print('\n== 3. Labeled derivation from source values (local-field illustration only)')
Bge, Bsi, Ep = sp.Float('6.55e6'), sp.Float('2.38e7'), sp.Float('1.067e5')
for name, b in (('Ge', Bge), ('Si', Bsi)):
    r = b/Ep
    print(f'{name}: B/E_peak = {float(r):.4g};  exp(-B/E_peak) = {float(sp.exp(-r)):.3e};  d lnG/d lnE (P=2) = {float(2+r):.4g}')
print('CAVEAT: the paper uses a NON-LOCAL (WKB) BTBT model; a local-field evaluation at the reported peak is not the paper\'s generation rate.')

print('\n== 4. Kane: apparent activation energy via Eg(T); B proportional to Eg^(3/2) (m* assumed T-independent)')
Cb = sp.Symbol('C_B', positive=True)
EgT = sp.Function('Eg')(T)
lnG_T = sp.log(A) + P*sp.log(E/E0) - Cb*EgT**sp.Rational(3, 2)/E
Ea_kane = sp.simplify(k*T**2*sp.diff(lnG_T, T))
Ea_kane = Ea_kane.subs(sp.Derivative(EgT, T), dEgdT).subs(EgT, Eg)
print('Ea_app(Kane) =', sp.simplify(Ea_kane))
check = -sp.Rational(3, 2)*(Cb*Eg**sp.Rational(3, 2)/E)*k*T**2*dEgdT/Eg
assert sp.simplify(Ea_kane - check) == 0
print('  = -(3/2)(B/E)(k T^2/Eg) dEg/dT  -> positive if dEg/dT<0; scales with B/E, no exp(-Eg/2kT) factor')

print('\n== 5. Trap-assisted (SRH + Hurkx-type field enhancement), generic background')
# G_TAT ~ n_i * Gamma / tau ; n_i ~ T^(3/2) exp(-Eg/(2kT)) (Eg const here); tau ~ T^(-1/2) via v_th
# Gamma = 2 sqrt(3 pi) (F/F_G) exp((F/F_G)^2), F_G = c T^(3/2)   (Gamma >> 1 regime)
FG = c*T**sp.Rational(3, 2)
lnGt = sp.Rational(3, 2)*sp.log(T) - Eg/(2*k*T) + sp.Rational(1, 2)*sp.log(T) \
       + sp.log(2*sp.sqrt(3*sp.pi)) + sp.log(F/FG) + (F/FG)**2
Ea_tat = sp.expand(sp.simplify(k*T**2*sp.diff(lnGt, T)))
print('Ea_app(TAT) =', Ea_tat)
u = sp.Symbol('u', positive=True)  # u = F/F_G
expected = Eg/2 + k*T/2 - 3*k*T*u**2
assert sp.simplify(Ea_tat.subs(F, u*FG) - expected) == 0
print('  = Eg/2 + kT/2 - 3 kT (F/F_G)^2   [Gamma>>1 limit]; dEa/dF =', sp.simplify(sp.diff(Ea_tat, F)), '(<0)')
print('  zero-field (Gamma->1, no enhancement) limit: Ea -> Eg/2 + 2kT (n_i T^(3/2), v_th T^(1/2))')

print('\n== 6. Coaxial single-dielectric field enhancement at the inner surface (same V)')
gcoax = x/sp.log(1+x)  # x = t/r_in
print('series g_coax =', sp.series(gcoax, x, 0, 3))
for xv in (sp.Rational(1, 10), sp.Rational(1, 2), 1):
    assert gcoax.subs(x, xv).evalf() > 1
print('g_coax > 1 checked at x = 0.1, 0.5, 1 (symbolic proof: ln(1+x) < x for x>0)')
print('Combined with section 2: a coaxial geometry multiplies local Kane generation by g^P exp((B/E)(1-1/g)) > 1.')
print('\n== 7. Tail resolution of n = 100 Monte Carlo devices (source: 100 per case)')
p, n = sp.symbols('p n', positive=True)
# zero events in n trials: one-sided 95% upper bound p_u solves (1-p)^n = 0.05
pu = 1 - sp.Float('0.05')**(sp.Integer(1)/100)
print(f'exact p_u = {float(pu):.4f}; rule-of-three approx 3/n = {3/100:.2f}')
print('=> fractions below ~3e-2 per case are not resolvable; ppm-level tails are out of reach.')

print('\nALL ASSERTIONS PASSED')
