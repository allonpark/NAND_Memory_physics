# S4 writer notes — W40 item i4 (DOI 10.3390/s26196254)

Access: abstract_only (MDPI full text HTTP 403). Only sources.yaml S4 entry + header read. No web fetch done by this writer.

## SOURCE_REPORTED claims (all from the abstract, per sources.yaml `source_reported_facts`)
| # | Claim | Location |
|---|---|---|
| 1 | HCI studied in 180 nm NMOS from RT down to 140 K | abstract (sources.yaml fact 1) |
| 2 | Stronger HC degradation at low T under CHE and DAHC stress | abstract (fact 2) |
| 3 | TTF modeling shows accelerated kinetics; substrate-current-based methodology validated at cryogenic T | abstract (fact 3) |
| 4 | Gate-length optimization proposed as mitigation | abstract (fact 4) |
Bibliographic: authors/venue 26(19) 6254/date 2026-10-02/CC BY 4.0 from Crossref record (sources.yaml resolve_evidence).

## UNKNOWN (not in abstract)
- Stress Vg/Vd values, exact bias points labelled CHE vs DAHC, stress times, failure criterion (dVth vs dId, %)
- Fitted m, A_HC, lifetimes, activation/temperature coefficients, number of devices, Weibull parameters (if any)
- Whether "validated" means a tau*Id/W vs Isub/Id collapse across T, and whether m is T-independent
- Split between N_it generation and oxide trapping; recovery/warm-up behaviour; gate lengths tested; recommended L
- Whether short-channel energy-driven (MVE/EES) regime was reached

## ENGINEERING_INFERENCE / HYPOTHESIS used in s4.html
- Causal chain middle steps (lambda(T) -> tail -> Isub -> N_it/trapping) : textbook-based inference (B for physics, C for applicability to this paper)
- Isub-collapse interpretation of "methodology validated" : inference
- Critical boundary (MVE/EES reversal, non-local transport, trapping dominance) : hypothesis, grade C; literature for reversed-T reports NOT checked in this session
- Tail origin from L/LDD/tox spread : inference
- HV NAND transfer : EXTRAPOLATION_ONLY

## Formula check (SymPy 1.14.0, venv_sympy, run with python -I)
General framework: Hu-type lucky-electron Isub lifetime model; no paper values used.
Script: s4work/s4_hci_sympy.py
```python
# S4 general-framework check (lucky-electron Isub lifetime model). No paper values used.
import sympy as sp
x, phi_i, phi_it, C1, C2, W, Id, lam0, Ep, k, T, qE = sp.symbols(
    'x phi_i phi_it C1 C2 W I_d lambda0 E_p k T qE', positive=True)
# x = 1/(q*lambda*E_m)  [1/eV]; phi in eV
ln_r   = sp.log(C1) - sp.log(x*phi_i) - phi_i*x          # ln(Isub/Id), lucky-electron w/ prefactor
ln_tau = sp.log(W/Id) - sp.log(C2) + phi_it*x            # tau ~ (W/Id) exp(phi_it*x)
slope  = sp.simplify(sp.diff(ln_tau, x)/sp.diff(ln_r, x)) # d ln tau / d ln(Isub/Id)
print("1) d ln(tau)/d ln(Isub/Id) with prefactor =", slope)
print("   limit x->oo (q*lambda*E_m << phi_i):", sp.limit(slope, x, sp.oo))
# prefactor neglected: exact power law
ln_r0 = sp.log(C1) - phi_i*x
xs = sp.solve(sp.Eq(sp.Symbol('lnr'), ln_r0), x)[0]
ln_tau0 = sp.expand(ln_tau.subs(x, xs))
print("2) ln(tau) (prefactor neglected) =", ln_tau0)
print("   coefficient of ln(Isub/Id) =", sp.diff(ln_tau0, sp.Symbol('lnr')))
# 3) optical-phonon mean free path temperature dependence (Crowell-Sze form)
lam = lam0*sp.tanh(Ep/(2*k*T))
dlam = sp.simplify(sp.diff(lam, T))
print("3) d lambda/dT =", dlam, "; sign negative for all T>0:", sp.simplify(dlam < 0))
# 4) at fixed E_m, d ln(Isub/Id)/dT and d ln(tau)/dT (prefactor neglected)
xT = 1/(qE*lam)   # qE = q*E_m
d_lnr_dT  = sp.simplify(sp.diff(-phi_i*xT, T))
d_lntau_dT= sp.simplify(sp.diff(phi_it*xT, T))
print("4) d ln(Isub/Id)/dT|E_m =", d_lnr_dT)
print("   d ln(tau)/dT|E_m      =", d_lntau_dT)
vals = {phi_i:1, phi_it:3, qE:1, lam0:1, Ep:1, k:1, T:sp.Rational(1,2)}
print("   numeric sign check (arbitrary normalized units):",
      sp.sign(d_lnr_dT.subs(vals)), sp.sign(d_lntau_dT.subs(vals)))
# 5) units: tau = A_hc * (W/Id) * r^-m ; [A_hc]=A*s/m so tau in s
import sympy.physics.units as u
A_hc = u.ampere*u.second/u.meter
print("5) units of A_hc*W/Id:", sp.simplify(A_hc*u.meter/u.ampere))
```

Output (actual run):
```
1) d ln(tau)/d ln(Isub/Id) with prefactor = -phi_it*x/(phi_i*x + 1)
   limit x->oo (q*lambda*E_m << phi_i): -phi_it/phi_i
2) ln(tau) (prefactor neglected) = -lnr*phi_it/phi_i - log(C2) - log(I_d) + log(W) + phi_it*log(C1)/phi_i
   coefficient of ln(Isub/Id) = -phi_it/phi_i
3) d lambda/dT = -E_p*lambda0/(T**2*k*(cosh(E_p/(T*k)) + 1)) ; sign negative for all T>0: True
4) d ln(Isub/Id)/dT|E_m = -E_p*phi_i/(T**2*k*lambda0*qE*(cosh(E_p/(T*k)) - 1))
   d ln(tau)/dT|E_m      = E_p*phi_it/(T**2*k*lambda0*qE*(cosh(E_p/(T*k)) - 1))
   numeric sign check (arbitrary normalized units): -1 1
5) units of A_hc*W/Id: second
```

Interpretation:
1. With the (lambda*E_m/phi_i) prefactor kept, d ln tau / d ln(Isub/Id) = -phi_it/(phi_i + q*lambda*E_m) (x = 1/(q lambda E_m)); equals -phi_it/phi_i only for q*lambda*E_m << phi_i. -> stated in s4.html as m being an approximation.
2. Prefactor neglected: exact power law tau ∝ (W/Id)(Isub/Id)^(-phi_it/phi_i).
3. lambda = lambda0 tanh(Ep/2kT): d lambda/dT < 0 for all T>0.
4. At fixed E_m: d ln(Isub/Id)/dT < 0, d ln tau/dT > 0 -> worse HCI at lower T (consistent with source fact 2).
5. Units: A_HC [A s/m] * W[m]/Id[A] -> s.
Not done: no numeric evaluation with real parameters (deliberately; none available from source).

## Weak points / caveats
- CHE/DAHC bias labelling: caller brief framed "CHE max near Vg~Vd/2, DAHC max near low Vg". Common literature (e.g. Takeda-type taxonomy) instead often calls the Isub-peak (Vg~Vd/2) condition DAHC and Vg≈Vd CHE. I wrote the section label-neutral (Isub peak at intermediate Vg, low-Vg avalanche/hole contribution, Vg≈Vd electron injection) and stated that label assignment varies and the paper's bias points are UNKNOWN. Lead should confirm the convention against full text.
- Textbook value of m (~3) and phi_i/phi_it numbers deliberately NOT written to avoid unsourced numbers; Hu et al. 1985 (IEEE JSSC/TED) is the origin of the framework but its DOI was not verified in this session, so it is not cited with DOI in the HTML.
- lambda(T)=lambda0 tanh(Ep/2kT) is the Crowell–Sze phonon form; primary source not re-checked here (grade B from memory).
- Charge pumping at cryogenic T has its own interpretation issues (freeze-out of emission); DOE says "where feasible".
- "What changed vs archive" compares only to W39 (read for format); w37/w38 content not read; overlap check relies on sources.yaml (no DOI overlap w37–w42).
- .qc class not used: QC grid is a report-level block in W39, not per-item.
- No figures created; no copyrighted figures used.
