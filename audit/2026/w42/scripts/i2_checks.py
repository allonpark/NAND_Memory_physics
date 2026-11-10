"""W42 item 2 framework derivations (symbolic). Run: venv_sympy python -I i2_checks.py
sympy 1.14.0 / mpmath 1.3.0 / Python 3.14.3. No value from the source is used; all results symbolic.
"""
import sys
sys.stdout.reconfigure(encoding='utf-8')
import sympy as sp

ok = True
def check(name, cond):
    global ok
    cond = bool(cond); ok &= cond
    print(f"[{'PASS' if cond else 'FAIL'}] {name}")

Q, r, ra, rb, t, eG, eI, eps = sp.symbols("Q r r_a r_b t eps_GBL eps_IL eps", positive=True)
E = lambda e, rr: Q / (2 * sp.pi * e * rr)          # coaxial field, layer permittivity e, radius rr

# (A) IL vs GBL field ratio. Stack occupies r_a..r_b (r_b = r_a + t).
gaa = sp.simplify(E(eI, ra) / E(eG, rb))            # GAA: IL at inner r_a, GBL at outer r_b
caa = sp.simplify(E(eI, rb) / E(eG, ra))            # CAA: GBL at inner r_a, IL at outer r_b
print("A  GAA E_IL/E_GBL =", gaa, "  CAA E_IL/E_GBL =", caa)
check("A: GAA ratio = (eps_GBL/eps_IL)*(r_b/r_a)", sp.simplify(gaa - eG / eI * rb / ra) == 0)
check("A: CAA ratio = (eps_GBL/eps_IL)*(r_a/r_b)", sp.simplify(caa - eG / eI * ra / rb) == 0)
gG = (ra + t) / ra; gC = ra / (ra + t)
check("A: geometric factors g_GAA*g_CAA = 1", sp.simplify(gG * gC - 1) == 0)
check("A: g_GAA - 1 = t/r_a > 0", sp.simplify(gG - 1 - t / ra) == 0)
check("A: g_CAA - 1 = -t/(r_a+t) < 0", sp.simplify(gC - 1 + t / (ra + t)) == 0)
check("A: both -> 1 as t/r_a -> 0", sp.limit(gG.subs(t, 0), ra, 1) == 1 and gC.subs(t, 0) == 1)

# (B) coaxial vs planar V_FB shift from charge sheet at r_c, one dielectric r_c..r_c+t
rc, sig, u = sp.symbols("r_c sigma u", positive=True)
dVc = sig * rc * sp.log((rc + t) / rc) / eps        # coax: Q' = 2 pi r_c sigma
dVp = sig * t / eps
ratio = sp.simplify((dVc / dVp).subs(t, u * rc))
print("B  coax/planar =", ratio)
check("B: ratio = ln(1+u)/u", sp.simplify(ratio - sp.log(1 + u) / u) == 0)
check("B: ratio -> 1 as u -> 0", sp.limit(sp.log(1 + u) / u, u, 0) == 1)
# ln(1+u) < u for u>0: f(u) = u - ln(1+u), f(0)=0, f'(u) = u/(1+u) > 0
f = u - sp.log(1 + u)
check("B: u - ln(1+u) has f(0)=0 and f' = u/(1+u) > 0  => ratio < 1", f.subs(u, 0) == 0 and sp.simplify(sp.diff(f, u) - u / (1 + u)) == 0)

# (C) ISPP steady-state slope (lumped, linear electrostatics)
# V_T = V_T0 + k*q ; tunnel field e = (V_G - V_T - c)/d. Steady state: e constant pulse-to-pulse
VG, VT0, k, q, c, d = sp.symbols("V_G V_T0 k q c d", positive=True)
s = sp.symbols("s", positive=True)                  # ISPP step
e_n = (VG - (VT0 + k * q) - c) / d
dq = sp.symbols("Delta_q")
e_np1 = (VG + s - (VT0 + k * (q + dq)) - c) / d
sol = sp.solve(sp.Eq(e_n, e_np1), dq)[0]
slope = sp.simplify(k * sol / s)
print("C  steady-state dV_T/dV_PGM =", slope)
check("C: steady-state ISPP slope = 1 (field held constant)", slope == 1)
# If an extra field-independent dipole term P adds to V_T per pulse (e.g., polarization switching),
# V_T increment = k*dq + dP; steady state with constant e still gives k*dq = s, so slope = 1 + dP/s.
dP = sp.symbols("Delta_P")
e_np1b = (VG + s - (VT0 + k * (q + dq)) - c) / d        # field set by charge only (P inside V_T bookkeeping assumption)
slope_b = sp.simplify((k * sp.solve(sp.Eq(e_n, e_np1b), dq)[0] + dP) / s)
print("C' slope with extra non-charge V_T term =", slope_b)
check("C': slope = 1 + Delta_P/s  (>1 needs a V_T term beyond trapped charge)", sp.simplify(slope_b - 1 - dP / s) == 0)

# (D) space oxide, parallel-plate region away from hole/slit edges
EBD, dV, tsp, g, tau0 = sp.symbols("E_BD DeltaV_WL t_sp gamma tau_0", positive=True)
Esp = dV / tsp
m = EBD * tsp / dV                                   # V_BD/DeltaV_WL with V_BD = E_BD t_sp
lnt = sp.log(tau0) - g * Esp                         # E-model
check("D: dm/dt_sp = E_BD/DeltaV_WL", sp.simplify(sp.diff(m, tsp) - EBD / dV) == 0)
dln = sp.simplify(sp.diff(lnt, tsp) * tsp)
print("D  dln t_BD/dln t_sp (fixed DeltaV_WL) =", dln)
check("D: dln t_BD/dln t_sp = gamma*DeltaV_WL/t_sp", sp.simplify(dln - g * dV / tsp) == 0)
F = sp.symbols("F", positive=True)
lnt_F = (sp.log(tau0) - g * Esp).subs(dV, F * tsp)
check("D: at fixed field F, field-only E-model has no t_sp dependence", sp.diff(lnt_F, tsp) == 0)

# (E) bookkeeping numbers used in the HTML text
import datetime as _dt
GB_over_Gb = sp.Integer(8)   # 1 byte = 8 bit
check("E: GB/mm^2 vs Gb/mm^2 differ by a factor of 8", GB_over_Gb == 8)
gap = (_dt.date(2026, 10, 12) - _dt.date(2025, 12, 17)).days
print("E  days from arXiv v1 (2025-12-17) to window start (2026-10-12):", gap, "=", sp.Rational(gap, 1) / sp.Rational(36525, 1200), "months (approx)")
check("E: gap is about ten months (between 9.5 and 10.5)", 9.5 < gap / 30.4375 < 10.5)

# (E) bookkeeping numbers used in the HTML text
import datetime as _dt
GB_over_Gb = sp.Integer(8)   # 1 byte = 8 bit
check("E: GB/mm^2 vs Gb/mm^2 differ by a factor of 8", GB_over_Gb == 8)
gap = (_dt.date(2026, 10, 12) - _dt.date(2025, 12, 17)).days
print("E  days from arXiv v1 (2025-12-17) to window start (2026-10-12):", gap, "=", sp.Rational(gap, 1) / sp.Rational(36525, 1200), "months (approx)")
check("E: gap is about ten months (between 9.5 and 10.5)", 9.5 < gap / 30.4375 < 10.5)

print("ALL PASS" if ok else "SOME FAIL")
sys.exit(0 if ok else 1)
