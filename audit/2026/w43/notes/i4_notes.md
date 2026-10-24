# i4 notes — 10.3389/fnano.2026.1961029 (writer notes; internal, not for the HTML)

## Re-fetch log (WebFetch, summarizing fetcher; 2026-10-21)
URL: https://www.frontiersin.org/articles/10.3389/fnano.2026.1961029/full (CC BY 4.0, open; no paywall).
Four passes: (1) verbatim numeric sentences Sec.2/3.1/Table 3, (2) IOFF/SS/immunity/case definitions,
(3) Tables 1-2 full rows, hetero-dielectric, Eq.1, TAT model, VDS/VG, Debye, (4) close paraphrase of 3.3-3.5 + conclusion.

| Item used in HTML | Re-fetch result | Status |
|---|---|---|
| Sentaurus TCAD | confirmed | SOURCE_REPORTED |
| Ge source, Eg 0.66 eV (text only, Table 1 has no material column) | confirmed | SOURCE_REPORTED |
| Ls=Ld=20 nm, tSi 20 nm, tpkt 10, tch 10, Lg 70 nm | confirmed (Table 1) | SOURCE_REPORTED |
| 2 nm SiO2 + 7 nm HfO2, WF 4.25 eV | confirmed; stacking order not explicit | SOURCE_REPORTED |
| Doping 5e19/1e19/5e19/1e19/1e18 ("Lightly doped channel") | confirmed | SOURCE_REPORTED |
| BTBT A,B Si 3.29e15/2.38e7; Ge 1.67e15/6.55e6 | confirmed verbatim | SOURCE_REPORTED |
| Eq.1 | symbols missing in rendering | UNKNOWN (not reconstructed) |
| Table 2 (acceptor, ET 0.0 mid-gap, Esig 0.1, mean 4.96e12, sigma 2.88e12, peak 9.88e12, sn=sp=1e-15) | confirmed | SOURCE_REPORTED |
| SRH model for traps; no explicit TAT (Hurkx) model in methods | confirmed (fetch: "absent") | SOURCE_REPORTED / used for AUTHOR_INTERPRETATION caveat |
| 5 nm segments, 100 devices per case | confirmed | SOURCE_REPORTED |
| Case defs: Case-2 x>30 nm, Case-3 20<x<30 nm, Case-4 whole | confirmed | SOURCE_REPORTED |
| Case-1: ION 1.208e-10, IOFF 1.71e-13 (Sec.3.1), Vth 0.3137 V, v 1.37e8 cm/s, SSmin 38.4 | confirmed | SOURCE_REPORTED |
| Case-2: ION 1.192e-10 (~1.3%), v 7.85e7 (42% in conclusion), SS 148.12 sd 4.12 | confirmed | SOURCE_REPORTED |
| Case-3: SS 142.94 sd 2.41; Vth 0.3137 | confirmed | SOURCE_REPORTED |
| Case-4: ION 1.192e-10, SS 148.35 sd 3.69 | confirmed | SOURCE_REPORTED |
| Peak field 1.067e5 V/cm at x=22.14 nm (trap-free) | confirmed | SOURCE_REPORTED |
| Gaussian vs uniform: "marginal shift", no numbers | confirmed | SOURCE_REPORTED |
| Authors: 100 samples insufficient for tails | confirmed ("substantially larger sample ... distribution tails") | SOURCE_REPORTED |
| Temperature | not given for simulations (only appears in Table 3 rows about other devices) | UNKNOWN |
| VDS, VG sweep | absent; only Fig.13 inset Vg -0.9 to -0.2 V | UNKNOWN |
| Debye length doping value in Sec.3.3 | missing in rendering | UNKNOWN |
| Table 3 HDDG row: ION 1.192e-10, IOFF 1.71e-12, SS 148.35 | confirmed | SOURCE_REPORTED |

Not used: "InSeAp" (fetcher paraphrase of conclusion; unclear token), Fig.11b alt-text BTBT peak (auto-generated alt text, not body), Table 3 rows for other papers.
Note on notes file: earlier notes said pocket "20-30 nm" (lateral, Case-3) and Table 1 says pocket thickness 10 nm; geometry ambiguity flagged as UNKNOWN in HTML. Earlier notes' "channel dopant As in Fig.1 caption" not re-checked (figures/captions not used) -> omitted.

## Inconsistency verification (reported in HTML as "observed on reading, not confirmed by the authors")
1. "immunity" / "(σ ∼ 0)" (Sec.3.3 heading, Sec.3.5.2, conclusion) vs Case-3 SS 38.4 -> 142.94 ± 2.41. CONFIRMED on re-fetch. Text gives no mechanism for the Case-3 SS rise. Which quantity has σ~0 is not named in the conclusion; Sec.3.3 variable symbols missing.
2. IOFF 1.71e-13 (Sec.3.1, trap-free) vs 1.71e-12 (Table 3 HDDG row). CONFIRMED as a numeric mismatch. Caveat added: the Table 3 row's ION/SS equal Case-4 values, so the row may be a trapped case; text gives no Case-4 IOFF -> cannot decide. Presented neutrally.
3. Sec.3.4 "reduction in SS" while SS increases in all trap cases. CONFIRMED.
4. TAT invoked qualitatively; methods list only SRH + non-local BTBT. CONFIRMED (fetch: explicit TAT model absent). Note: Sentaurus SRH can include field enhancement as an option; whether it was enabled is UNKNOWN — so the HTML says "no field-enhanced TAT model is stated", not "was not used".

## Derivations (sympy 1.14.0, venv_sympy, python -I)
Script: i4_btbt.py (same folder). Output: i4_btbt_out.txt. All assertions passed.
- d lnG/d lnE = P + B/E (local Kane form G = A (E/E0)^P exp(-B/E)).
- G(gE)/G(E) = g^P exp[(B/E)(1-1/g)], d lnR/dg = P/g + B/(E g^2) > 0.
- Labeled numbers (source values only): B_Ge/E_peak = 61.39, exp(-61.39) = 2.187e-27; B_Si/E_peak = 223.1, exp = 1.344e-97. Used only to show that the reported peak field cannot be read as the local-Kane E; paper uses non-local model.
- Kane Ea_app = -(3/2)(B/E)(kT^2/Eg) dEg/dT, with B ∝ Eg^{3/2} and m* T-independent.
- TAT (SRH, mid-gap, Hurkx-type Γ ≈ 2√(3π)(F/FΓ)exp[(F/FΓ)^2], FΓ ∝ T^{3/2}, Γ>>1, n_i ∝ T^{3/2}exp(-Eg/2kT), τ ∝ T^{-1/2}): Ea_app = Eg/2 + kT/2 - 3kT(F/FΓ)^2; dEa/dF < 0. Zero-field limit Eg/2 + 2kT. Hurkx form is background knowledge (Hurkx, Klaassen, Knuvers, IEEE TED 39, 1992 — NOT re-checked this session).
- Coax single layer g = x/ln(1+x) = 1 + x/2 - x^2/12 + ..., > 1.
- Tail bound n=100, zero failures: p_u = 1 - 0.05^(1/100) = 0.0295 (rule of three 0.03).

## Grades
- Source-reported trends: C (TCAD only, borrowed coefficients, internal inconsistencies).
- Transfer to VNAND GIDL: D (planar DG TFET vs cylindrical poly-Si channel; analogy only).
- Background BTBT/TAT equations: C (textbook, sympy-consistent, primary sources not re-checked).

## Archive comparison (W37-W40 only)
- DOI and "TFET" absent from origin/main w37, w38, w39 and origin/weekly/2026-w40 w40 index.html (grep count 0).
- W38 item 1: CTL-local BTBT, J ≈ A E^2 exp(-B/E), DOE refutes by onset vs Arrhenius.
- W40 item 2 (pool-capacitor defect: TAT leakage at weak spot), item 3 (TOX direct/TAT retention competitor).
- No W41/W42/W43 branch material used.

## Could not support / not included
- Eq.1 form; figures (band diagrams, BTBT maps, Fig.13 curves); temperature; VDS; numerical IOFF for Cases 2-4; any experimental validation (none exists in the paper).
- No magnitude estimate for coaxial GIDL enhancement (geometry unknown and confidential-class numbers avoided).
