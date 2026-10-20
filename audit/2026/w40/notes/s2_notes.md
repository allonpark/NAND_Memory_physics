# S2 notes — W40 item i2 (ISTFA 2026 p0478, DOI 10.31399/asm.cp.istfa2026p0478)

Access: abstract_only (3-page poster; PDF not read). Output: sections/s2.html (`<section id="i2">`, ~1560 Hangul syllables + English pairs; 25 ko/en paragraph pairs, HTML parse clean; classes used: sourcebox, inference, boundary, doebox, eq, chain, compare, qc, label, tag, pass, pending — all present in assets/style.css).

## SOURCE_REPORTED claims and abstract location (as recorded in sources.yaml S2 `source_reported_facts`)
1. A single defective load on a shared global reference/clock line can degrade multiple functional blocks. [abstract, fact 1]
2. Target defect: subtle gate-oxide defect inside a pool capacitor on a global signal line. [abstract, fact 2]
3. Small footprint and deep burial make typical OBIRCH hotspots diffused/smeared. [abstract, fact 3]
4. A localization methodology is presented (workflow/results unconfirmed). [abstract, fact 4]
Bibliographic: authors, venue, pages 478-480, DOI, publication/online 2026-10-04 — from sources.yaml resolve_evidence (Crossref + doi.org + ASM page). Sentence-level location within the abstract is not available to me (I did not re-read the abstract; I rely on the sources.yaml extraction).

## UNKNOWN items
- Actual localization workflow, tools (LIT/OBIRCH variant/PEM/nanoprobing/FIB), wavelengths, bias, lock-in frequency.
- Pool-capacitor structure (MOS vs MIM/MOM; bottom plate = well/diffusion/poly?), oxide type/thickness, area.
- Defect morphology (thinning, particle, SBD/HBD spot, contamination) and root cause.
- Electrical signature details (I-V, T dependence, which reference/clock line, which blocks, failure symptom).
- Any statistics, Weibull, DPPM numbers; whether the defect was latent or time-dependent.
- Affiliation of authors (not stated in sources.yaml; not written).

## Labeled inferences written (all ENGINEERING_INFERENCE unless noted)
- Causal chain beyond "line shared / multi-block": TAT/percolation leak, line droop/RC delay, SBD->HBD possibility.
- Planar MOS E_ox form for the pool capacitor (explicitly not cylindrical); coaxial form only as array contrast.
- Two smearing hypotheses: (H1) thermal spreading set by depth d (FWHM = 2√3 d steady; lock-in resolution/SNR trade-off); (H2) OBIRCH responds to the whole TCR current path, contrast C = I_def/(J_int A + I_par) small in a large-area cap.
- Competing mechanisms table and falsification DOE (symbolic levels).
- Weibull bimodal/extrinsic tail expectation (no data).
- Array/HV transfer = EXTRAPOLATION_ONLY.

## Sympy verification (sympy 1.13.3, mpmath 1.3.0, scratch venv; run with `python -I`)
Script: w40/sections/s2_scaling.py (output w40/sections/s2_scaling_out.txt); venv at scratchpad/s2venv
```python
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
```

Output (actual run):
```
1a) Laplacian of 1/r (r>0): 0
1b) half-max radius rho_1/2 = [sqrt(3)*d] -> FWHM = [2*sqrt(3)*d]
1c) peak surface rise Ts(0) = P/(2*pi*d*k)
1d) min detectable power P_min = [2*pi*DeltaT_min*d*k]
2a) residual of heat eq with mu=sqrt(2D/w): 0
2b) FWHM/d vs g=d/mu (numeric root of amp=1/2):
    g=   0: FWHM/d=3.464 
    g= 0.5: FWHM/d=2.323 
    g=   1: FWHM/d=1.887 
    g=   2: FWHM/d=1.464  (small-mu approx 2*sqrt(2ln2/g)=1.665)
    g=   5: FWHM/d=0.993  (small-mu approx 2*sqrt(2ln2/g)=1.053)
    g=  10: FWHM/d=0.722  (small-mu approx 2*sqrt(2ln2/g)=0.745)
2c) on-axis amplitude attenuation factor exp(-d/mu)/d ; phase lag = d/mu rad
    signal at g=5 relative to g=0 (same d): 0.006737946999085467
3a) eta2/eta1 = (A1/A2)**(1/beta) (weakest-link, same E,T,criterion)
3b) extrinsic fraction F_ext = 1-exp(-D0*A); small D0*A -> A*D0
4a) E_coax(r_in)/E_planar(same t=r_out-r_in, same V) = (-r_in + r_out)/(r_in*log(r_out/r_in))
4b) in u=t/r_in: u/log(u + 1) ; limit u->0 = 1
```

Interpretation checks:
- 1a/2a: 1/r and exp(-(1+i)r/mu)/r satisfy Laplace / harmonic heat equation with mu = sqrt(2D/omega) (residual 0).
- 1b: steady surface profile from buried point source (adiabatic surface, image doubling) has FWHM = 2√3 d — independent of defect size when a << d.
- 2b: lock-in FWHM/d = 3.464, 2.323, 1.887, 1.464, 0.993, 0.722 for d/mu = 0, 0.5, 1, 2, 5, 10; large-g asymptote 2*sqrt(2 ln2/g) converges (1.665 vs 1.464 at g=2, 0.745 vs 0.722 at g=10). Signal factor e^-5 = 0.0067 ≈ 1/148 ("about 1/150" in text).
- 4a/4b: E_coax(r_in)/E_planar = u/ln(1+u) > 1, -> 1 as u -> 0.
- On-axis phase lag = d/mu is exact for this kernel (phase of exp(-(1+i)r/mu) at r=d); off-axis and layered-medium phase not checked.
- Independent cross-check: FWHM 2√3 d from hand derivation (d/sqrt(rho^2+d^2)=1/2 -> rho=√3 d) agrees with sympy.

## Self-identified weak points
1. Thermal model is homogeneous semi-infinite with adiabatic surface; real BEOL/FEOL stack (Si high k, oxide low k, metal high k) gives anisotropic spreading, and backside vs frontside access changes d. FWHM numbers are dimensionless illustrations, not predictions.
2. In OBIRCH the heat source is the laser absorption region, not the defect; I used "effective depth between heat source and TCR-sensitive element" by reciprocity-style reasoning — not rigorously derived for laser-stimulation geometry; laser spot convolution not modeled.
3. Contrast C is a definition, not a validated detectability criterion; noise floor of OBIRCH amplifier not modeled.
4. Assumed pool cap is MOS-type; if it is MOM/MIM, "gate oxide" wording in abstract argues against, but structure is still UNKNOWN; junction-leakage competitor only applies if bottom plate is a diffusion/well.
5. Mechanism signature table (Arrhenius types, polarity asymmetry) is generic textbook-level reasoning, not calibrated to this process.
6. Weibull/area-scaling expectation is weakest-link; W39 item 1 shows it can fail — stated in text.
7. "Change vs archive" references only W39 item 1 and S1 (from sources.yaml); I did not read W41 p0653 content, so no comparison to it was written.
8. I did not re-open the ASM abstract page; SOURCE_REPORTED rests on the sources.yaml extraction.
