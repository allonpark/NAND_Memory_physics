# S3 (W40) coaxial vs planar field comparison -- symbolic, non-dimensional.
# Ideal coaxial stack: channel surface r0 | TOX | CTL | BOX | gate.
# Lengths normalized by t_tox; permittivities normalized by eps_ox(TOX).
# kappa = t_tox / r0 (curvature, dimensionless). a = t_ctl/t_tox, b = t_box/t_tox.
# en = eps_ctl/eps_tox, eb = eps_box/eps_tox. No product dimensions are used.
import sympy as sp

k, a, b, en, eb, x = sp.symbols('kappa a b e_n e_b x', positive=True)
V, Qs = sp.symbols('V Q', positive=True)

# radii in units of t_tox
r0 = 1/k
r1 = r0 + 1
r2 = r1 + a
r3 = r2 + b

# --- 1. single layer: E(r0)/(V/t) ---
x_ = sp.Symbol('x', positive=True)          # x = t/r0
f1 = x_/sp.log(1+x_)
print("[1] single-layer E(r_in)/(V/t) =", f1)
print("    series in x:", sp.series(f1, x_, 0, 4))
print("    E(r_out)/(V/t) =", sp.simplify(x_/((1+x_)*sp.log(1+x_))),
      " series:", sp.series(x_/((1+x_)*sp.log(1+x_)), x_, 0, 3))
d = sp.diff(f1, x_)
print("    d/dx of E(r_in) ratio =", sp.simplify(d))
print("    numerical sign check at x=0.1,0.5,1,3:",
      [sp.N(d.subs(x_, v), 4) for v in (0.1, 0.5, 1, 3)])

# --- 2. three-layer stack, program field (applied V, no stored charge) ---
S_lin = 1 + a/en + b/eb                          # planar sum t_i/eps_i (units t_tox/eps_tox)
S_log = sp.log(r1/r0) + sp.log(r2/r1)/en + sp.log(r3/r2)/eb
E_pl = V/S_lin                                   # planar TOX field (uniform)
E_r0 = V/(r0*S_log)                              # coax E at channel/TOX interface
E_r1 = V/(r1*S_log)                              # coax E at TOX/CTL interface
E_r3 = V/(eb*r3*S_log)                           # coax E in BOX at gate interface
E_pl_box = V/(eb*S_lin)
R_prog_r0 = sp.simplify(E_r0/E_pl)
R_prog_r1 = sp.simplify(E_r1/E_pl)
R_gate = sp.simplify(E_r3/E_pl_box)
s_r0 = sp.series(R_prog_r0, k, 0, 2).removeO()
s_r1 = sp.series(R_prog_r1, k, 0, 2).removeO()
s_g = sp.series(R_gate, k, 0, 2).removeO()
print("\n[2] program field ratio coax/planar, first order in kappa")
print("    at channel/TOX (r0):", sp.factor(sp.simplify(s_r0 - 1)), "(+1)")
print("    at TOX/CTL    (r1):", sp.factor(sp.simplify(s_r1 - 1)), "(+1)")
print("    at BOX/gate   (r3):", sp.factor(sp.simplify(s_g - 1)), "(+1)")

# --- 3. retention: stored sheet charge at TOX/CTL interface (r1), gate & channel at 0,
#        normalized to the SAME Vth shift dV (charge-to-gate capacitance).
C_in = 1/sp.log(r1/r0)                                   # 2*pi*eps_ox factored out
C_out = 1/(sp.log(r2/r1)/en + sp.log(r3/r2)/eb)
dV = sp.Symbol('dV', positive=True)
Q = dV*C_out                                             # Q'/(2 pi eps_ox) at fixed dVth
Q_in = Q*C_in/(C_in+C_out)
Eret_r0 = Q_in/r0
Eret_r1 = Q_in/r1
# planar: per-area caps 1/t
c_in, c_out = 1, 1/(a/en + b/eb)
Eret_pl = dV*c_out*c_in/(c_in+c_out)
R_ret_r0 = sp.series(sp.simplify(Eret_r0/Eret_pl), k, 0, 2).removeO()
R_ret_r1 = sp.series(sp.simplify(Eret_r1/Eret_pl), k, 0, 2).removeO()
print("\n[3] retention field ratio coax/planar at fixed dVth, first order in kappa")
print("    at r0:", sp.factor(sp.simplify(R_ret_r0 - 1)), "(+1)")
print("    at r1:", sp.factor(sp.simplify(R_ret_r1 - 1)), "(+1)")

# --- 4. differential: does curvature enhance program field more than retention field?
diff_r0 = sp.factor(sp.simplify((s_r0 - 1) - (R_ret_r0 - 1)))
print("\n[4] (program enhancement) - (retention enhancement) at r0, O(kappa):", diff_r0)
# sign check on generic positive values (symbols, not product values)
import itertools
vals = [0.5, 1, 2, 4]
signs = set()
for A, B, EN, EB in itertools.product(vals, vals, [1, 2], [1, 2.5]):
    signs.add(sp.sign(sp.N(diff_r0.subs({a: A, b: B, en: EN, eb: EB, k: 1}))))
print("    sign over grid a,b in {0.5,1,2,4}, en in {1,2}, eb in {1,2.5}:", signs)

# exact (not series) identity check
exact = sp.simplify(Eret_r0/Eret_pl - (E_r0/E_pl).subs(V, 1))
print("    exact identity  (Eret/Eret_pl) - (Eprog/Eprog_pl) at r0 =", exact)
# sign of first-order coefficient at r1 (TOX/CTL side): geometry dependent?
c_r1 = sp.factor(sp.simplify((s_r1 - 1)/k))
signs1 = set()
for A, B, EN, EB in itertools.product([0.25, 0.5, 1, 2, 4], [0.25, 0.5, 1, 2, 4], [1, 2], [1, 2.5]):
    signs1.add(sp.sign(sp.N(c_r1.subs({a: A, b: B, en: EN, eb: EB}))))
print("    r1 coefficient signs over grid:", signs1)
print("    r1 coefficient < 0  <=>  a^2 e_b + 2ab e_n + b^2 e_n < e_b e_n")

# --- 5. TOX thickness bound for a field-limited program-speed target E* at fixed V.
#        planar single-layer-equivalent: t_max = V/E*; coax single layer: x/ln(1+x) solved.
print("\n[5] single-layer: coax field at fixed V and t exceeds planar by factor x/ln(1+x)>1,")
print("    so for fixed E* the admissible t is larger in coax (direction: thicker).")
print("    exact check x=0.2:", sp.N(f1.subs(x_, 0.2), 5), " x=1:", sp.N(f1.subs(x_, 1), 5))
