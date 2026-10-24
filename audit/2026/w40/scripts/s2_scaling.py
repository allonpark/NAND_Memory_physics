# S2 scaling checks (symbolic / non-dimensional only; no source numbers exist)
import sympy as sp
rho, d, k, P, D, w, mu, r, A1, A2, beta, D0, A = sp.symbols('rho d k P D omega mu r A1 A2 beta D0 A', positive=True)

# 1) Steady point source P at depth d below adiabatic surface, semi-infinite medium (image method)
#    Delta T_surface(rho) = P/(2 pi k sqrt(rho^2+d^2))
Ts = P/(2*sp.pi*k*sp.sqrt(rho**2+d**2))
# check Laplace eq. for the full-space kernel 1/r (r>0) in spherical coords
f = 1/r
lap = sp.simplify(sp.diff(r**2*sp.diff(f, r), r)/r**2)
print('1a) Laplacian of 1/r (r>0):', lap)
sol = sp.solve(sp.Eq(Ts/Ts.subs(rho, 0), sp.Rational(1, 2)), rho)
print('1b) half-max radius rho_1/2 =', sol, '-> FWHM =', [sp.simplify(2*s) for s in sol])
print('1c) peak surface rise Ts(0) =', sp.simplify(Ts.subs(rho, 0)))
dTmin = sp.symbols('DeltaT_min', positive=True)
print('1d) min detectable power P_min =', sp.solve(sp.Eq(Ts.subs(rho, 0), dTmin), P))

# 2) Lock-in (harmonic) point source: T ~ exp(-(1+i) r/mu)/r, mu = sqrt(2D/omega)
q = (1+sp.I)/mu
T = sp.exp(-q*r)/r
helm = sp.simplify(sp.diff(r**2*sp.diff(T, r), r)/r**2 - sp.I*w/D*T)
print('2a) residual of heat eq with mu=sqrt(2D/w):', sp.simplify(helm.subs(mu, sp.sqrt(2*D/w))))
# normalized surface amplitude profile, x = rho/d, g = d/mu
x, g = sp.symbols('x g', positive=True)
amp = (1/sp.sqrt(1+x**2))*sp.exp(-g*(sp.sqrt(1+x**2)-1))
print('2b) FWHM/d vs g=d/mu (numeric root of amp=1/2):')
for gv in [0, 0.5, 1, 2, 5, 10]:
    xs = sp.nsolve(amp.subs(g, gv)-sp.Rational(1, 2), x, (1e-3, 5), solver="bisect")
    approx = 2*sp.sqrt(2*sp.log(2)/gv) if gv >= 2 else None
    print(f'    g={gv:>4}: FWHM/d={float(2*xs):.3f}', f' (small-mu approx 2*sqrt(2ln2/g)={float(approx):.3f})' if approx else '')
print('2c) on-axis amplitude attenuation factor exp(-d/mu)/d ; phase lag = d/mu rad')
print('    signal at g=5 relative to g=0 (same d):', float(sp.exp(-5)))

# 3) Weibull area scaling (intrinsic, weakest-link) and Poisson defect-limited (extrinsic) tail
print('3a) eta2/eta1 =', sp.simplify((A1/A2)**(1/beta)), '(weakest-link, same E,T,criterion)')
F_ext = 1-sp.exp(-D0*A)
print('3b) extrinsic fraction F_ext = 1-exp(-D0*A); small D0*A ->', sp.series(F_ext, D0, 0, 2).removeO())

# 4) Planar vs coaxial field (contrast only; pool cap = planar)
V, t, rin, rout, eps = sp.symbols('V t r_in r_out epsilon', positive=True)
E_pl = V/t
Qp = 2*sp.pi*eps*V/sp.log(rout/rin)          # Q' per length from dV = Q'/(2 pi eps) ln(rout/rin)
E_in = Qp/(2*sp.pi*eps*rin)
ratio = sp.simplify(E_in/E_pl.subs(t, rout-rin))
print('4a) E_coax(r_in)/E_planar(same t=r_out-r_in, same V) =', ratio)
u = sp.symbols('u', positive=True)  # u = t/r_in
print('4b) in u=t/r_in:', sp.simplify(ratio.subs(rout, rin*(1+u))), '; limit u->0 =', sp.limit(u/sp.log(1+u), u, 0))
