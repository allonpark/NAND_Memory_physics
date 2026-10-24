# i1 notes (W43 item 1) — writer notes, scratchpad only

Source: Cho, Hwang, Park, Park, Lee, "Electron injection in tunneling-oxide-less charge-trap flash memories",
APL 129(16) 163502, DOI 10.1063/5.0345638. Access: abstract_only (AIP paywall, "You do not currently have
access", pay-per-view offered; not bypassed). Selection: new_this_week.

## Re-fetch of the abstract (2026-10-21, WebFetch on the AIP stable URL; summarizing fetcher)
Three passes. Fetcher refuses verbatim abstract; short phrases returned:
- "place the Si3N4 layer in direct contact with the poly-Si channel"; "requiring a different electron injection model"
- first sentence is about a framework "for electron trapping" (not "injection")
- "Fowler–Nordheim tunneling through Si3N4" + "direct channel-to-nitride injection"; "shallow and deep trap-energy levels in the nitride layer"
  -> which route each level belongs to is AMBIGUOUS in the fetched wording; HTML says "represented with shallow and deep levels" and lists level assignment as UNKNOWN.
- calibration: "simulated programming transients" and "I_D–V_G characteristics", calibrated "to measurements from fabricated AN devices"; "spatial distribution are calibrated"
- AN: "accurately predicts the threshold-voltage shift" and "trapped-electron distributions as functions of programming voltage and temperature"; "clarifies how" Et/Nt/m*/distribution determine trapping rate, stored charge, trapping location
- ANO: "accurately predicts their trapped-electron density distribution"; basis of accuracy not stated, no ANO measurement comparison mentioned -> AUTHOR_INTERPRETATION
- "effective platforms for extracting intrinsic nitride trap parameters"
- No numbers; no geometry word (cylindrical / GAA / 3D / vertical / planar) in the abstract.
- Page metadata: received 2026-05-28, accepted 2026-10-01, published 2026-10-19. Affiliations: SNU ECE/ISRC; SK hynix R&D (Cho); Gachon Univ. (Min-Kyu Park) — affiliations not used in HTML.
Caveat: wording comes from a summarizing fetcher; quoted phrases may not be exact verbatim.

## Discrepancies vs manifest entry
1. Manifest fact 3 says direct injection is "represented by shallow and deep nitride trap levels"; re-fetch wording can be read as both routes represented with the levels. Treated as UNKNOWN.
2. Manifest facts 5/6 omit the abstract's "accurately predicts" (author claim) and the ANO "trapped-electron density distribution" prediction with no stated benchmark. HTML labels both as AUTHOR_INTERPRETATION.
3. Manifest fact 4 lists calibration targets as "programming transients and ID-VG"; abstract wording is "simulated" transients and I_D-V_G calibrated "to measurements". Consistent in substance.
4. Manifest calls it "Physics-based TCAD framework"; not quoted in HTML (word not confirmed verbatim).

## Derivations (labeled; no paper numbers; dimensionless symbols only)
Script: i1_coax.py (run: venv_sympy python -I). Output: i1_coax_out.txt. Key results:
- [1] AN two-layer coax, g0 = E_coax(r0)/E_planar,N, x=t_N/r0, a=t_A/t_N, e=eps_A/eps_N:
  g0 - 1 = x(a^2+2a+e)/(2(a+e)); coefficient - 1/2 = a(a+1)/(2(a+e)) > 0.
  N/A interface (nitride side): x(a^2-e)/(2(a+e)) (sign varies). Gate side: -x(a^2+2ae+e)/(2(a+e)).
- [2] WKB exponent in 1/r field at equal E0: R(lam) = (3/2) Int_0^1 sqrt(1-w) e^{lam w} dw
  = 1 + 2lam/5 + 4lam^2/35 + 8lam^3/315 + ...; lam = phi_B/(q E0 r0). Quad check matches (1.0203, 1.0848, 1.2321 at lam=0.05,0.2,0.5 — these are function values, not device numbers; not in HTML).
- [3] Net FN exponent ratio at equal V = R(lam_c)/g0 with lam_c <= ln(1+x): max over generic grid
  x in {0.05..1}, a in {0.25..4}, e in {0.5..3} = 0.9928 (<1). First-order argument: 2/5 < c1 and lam <= x.
  Grid values are generic dimensionless, not product values; the 0.9928 number is NOT put in HTML.
- [4] Aliasing: planar-field analysis of a coax device gives m*_fit = m* (R/g0)^2 (phi fixed).
- [5] Sheet at r_c: dVth = Q'/(2pi)[ln(r1/rc)/eps_N + ln(r2/r1)/eps_A]; d/drc = -Q'/(2pi eps_N rc);
  planar limit r0->oo ratio = 1 (checked).
Textbook (not derived, background): FN J=AE^2exp(-B/E), B=4sqrt(2m*)phi^{3/2}/(3q hbar); tunneling-front
tau=tau0 exp(2 kappa x); thermal emission e_n = nu exp(-Et/kT). Labeled "framework, not the paper's model".

## Archive comparison (W37–W40 only; origin/main w37–w39, origin/weekly/2026-w40)
- W37 item 1: Direct observation of lateral hole migration in Si3N4 CTL
- W38 item 1: CTL-local band-to-band tunneling as an IVS/interference path
- W40 item 3: CTL trap density / tunnel-oxide / poly-Si grains TCAD, planar-vs-coaxial question
DOI 10.1063/5.0345638 not found in these. No W41–W43 branch material used.

## Grades
Reported model structure C (abstract only; measurement-calibrated per abstract but unread). Transfer to VNAND D.
Curvature directions C (ideal model, conditional, sympy). No A/B.

## Not supported / left out
- No numeric Et, Nt, m*, phi_B, thicknesses, voltages, temperatures (none available).
- Direction of temperature dependence: UNKNOWN (abstract only says the model predicts vs T).
- Whether the paper's devices or TCAD are cylindrical: UNKNOWN.
- Failure modes (fast charge loss, read disturb, interface-state generation) are inference only.
