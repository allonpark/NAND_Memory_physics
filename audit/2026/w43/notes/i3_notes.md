# i3 notes — W43-S3, DOI 10.1063/5.0347445 (AIP Advances 16(10), 105116)

Writer notes (scratchpad only). Read: sources.yaml header + W43-S3 entry; fulltext_notes_W43-S3.md.
Re-fetched myself 2026-10-21 via WebFetch (4 passes on pubs.aip.org stable URL, 1 pass Crossref API).
WebFetch is a summarizing fetcher: verbatim fragments were requested and capped; figures not readable.

## Verification of each number/condition used (notes vs my re-fetch)

| Item | Notes said | Re-fetch | Used in HTML |
|---|---|---|---|
| Dates | online 2026-10-20, rcv 06-21, acc 10-05 | confirmed (page + Crossref) | yes |
| Licence | CC BY 4.0 | confirmed | yes |
| Authors | diacritics dropped in yaml | Crossref: Kilpeläinen, Kübarsepp ... 11 authors, order confirmed | yes |
| Responsivity range | 250-476 nm (abstract) | abstract 250-476; THIS WORK CESR only 250-410 nm; 360-476 nm from earlier publication (Ref.14, Werner et al., PQED, two-photodiode trap) | yes, split stated |
| u_rel responsivity | ~0.1% | confirmed "about 0.1%" | yes |
| Radiant power | 2.8-4.5 uW | confirmed | yes |
| Reverse bias | 1 V | confirmed | yes |
| Structure | 220 nm SiO2 on high-res Si | confirmed | yes |
| Model layers | 220.9 / 0.6 / 0.3 nm | confirmed (0.3 nm roughness fixed nominal, little effect) | yes |
| rho 325 nm | 0.03787 (1.0%) | confirmed | yes |
| rho 405 nm | 0.000545 (2.2%) | confirmed | yes |
| rho peak | 0.120 at 290 nm | confirmed | yes |
| combined u(rho) | <0.005 | confirmed | yes |
| delta | ~1e-3 (Fig.3) | TEXT: "about 0.002 in the UV range"; Fig.3 caption has no number | used 0.002 (text) — **notes value not supported** |
| Eg | 1.12 eV | confirmed | yes |
| m_c | 4.6 vs 3.5 | confirmed; 3.5 = Alig parabolic band; 4.6 = Kamakura (empirical pseudopotential band). **Line in Fig.4 is drawn at Kamakura's 4.6; no fitted m_c, no CI, no A_c value found** | reported as "agreement with 4.6 reference line" only |
| Eq.(1) | R=(e/hν)(1-ρ)(1-δ)(1+g) | confirmed | yes |
| Eq.(2) | notes: r_c ∝ (E-Eg)^m_c | flattened; the "proportional to" expression did not render; r_c' = electron–phonon scattering rate | form UNKNOWN in HTML |
| Eq.(3) | garbled | flattened "ghν=1+Achν−2Egmc−1"; consistent with g=[1+A_c x^-m]^-1 but typeset form not confirmed | UNKNOWN; only algebra on Eq.4 shown (A2) |
| Eq.(4) | log10(g/(1-g)) = m_c log10(hν-2Eg) - log10 A_c | confirmed; Fig.4 caption: hν−2Eg in eV | yes |
| 4 orders | span of g | confirmed: "values of g range over four orders of magnitude"; figure combines this work + Ref.14 (+ Korpusenko) | yes |
| argument>0.1 at <350 nm | AUTHOR_INTERPRETATION | confirmed; reason: P_c broadens, "less efficient for impact ionization" | yes |
| argument>0.35 at <275 nm | hole II | confirmed ("also needs to be considered") | yes |
| 0.25-0.35 structure | non-constant e-ph scattering | confirmed, "structure above the line" | yes |
| Fig.4 "fall clearly below at argument 0.3" (notes) | caption claim | **NOT in Fig.4 caption on my re-fetch** (caption = log-log plot ... four orders ... hν−2Eg in eV). One fetch pass paraphrased such a caption, a later verbatim pass did not contain it. Not used. | no |
| Temperature | unknown | not stated (only a reference title mentions 300 K) | UNKNOWN |
| Electric field / hot carriers | — | not mentioned in body; "hot carriers" only in a reference title | stated as absent |
| MOS/tunneling, APD | abstract ties to MOS tunneling | intro: MOS transistors injected with electrons by quantum tunneling; APDs | AUTHOR context only |
| Korpusenko et al. | — | g at 250-400 nm, same photodiode type, pyroelectric reference, 1% uncertainty; position vs line not described | yes |

## Source / manifest inconsistencies noticed
1. sources.yaml `why_fits` and extrapolation_warnings call the photodiode "field-free"; the paper never discusses electric field (an induced junction with 1 V reverse bias is not demonstrably field-free). HTML says the photon, not a field, sets the energy, and that the field is not discussed.
2. Notes: δ ~1e-3 vs text "about 0.002".
3. Notes Fig.4 row ("fall clearly below at argument 0.3") not confirmed in the caption.
4. Abstract range 250-476 nm vs this work's CESR range 250-410 nm (rest from earlier publication). Abstract wording "characterized by a power-law exponent of 4.6" vs body: line drawn at Kamakura's value, no fit/CI — risk of reading as a measured exponent.
5. The text contains a condition "which is the case at wavelengths longer than 250 nm" whose referent I could not confirm; not used as a contradiction.
6. "argument" undefined in text; log10((hν−2Eg)/eV) reproduces the pairs (A1) — inference.

## Derivations (labeled)
Script: i3_powerlaw.py (same folder); output: i3_powerlaw_out.txt. sympy 1.14.0, venv_sympy, python -I.
- Part A (source values + hc only): A1 wavelength→x and argument; A2 algebra on Eq.4; A3 decades span: 4.014 (m=4.6) vs 3.054 (m=3.5) over 476–250 nm; within valid window 476 nm..argument 0.1: 2.475 vs 1.883, difference 0.592 decades.
- Part B (GENERAL BACKGROUND, not from paper): <r> = PΓ(m+1)E_h^m exp(−Eth/E_h); m→0 gives lucky-electron hard threshold; log-slope m+Eth/E_h; integrand mode mE_h, mean (m+1)E_h, var (m+1)E_h²; Isub/Id ∝ F^(m+s) exp(−b/F), bias log-slope m+s+Eth·l/(qλ_p V_p); m-share m/(m+s+Eth/E_h). B7 illustrative Eth/E_h numbers are NOT used in the HTML. B8 window: E_h ≈ 0.079 (476 nm) / 0.170 (410 nm) / 0.274 eV (argument 0.1) for m=4.6 — used in HTML as derivation. B9 tail mapping.
- Coaxial equation (Gauss law, textbook) quoted with conditions; no new numbers.

## Evidence grades
- In-domain optical result (agreement with 4.6): B — full text, peer-reviewed metrology, not reproduced; no fitted CI.
- Transfer to HCI/GIDL: D.
- Background derivation: C (math checked; applicability conditional).

## Archive comparison (only origin/main w37-w39 and origin/weekly/2026-w40)
- W40 item 4: cryogenic HCI 180 nm NMOS; lucky-electron Isub/Id with λ(T) as textbook background. This item adds the rate-shape benchmark beneath it; no change to W40.
- W38 item 1: CTL-local BTBT path. W37: caution on interpreting GIDL/select stress ΔVth as permanent HCI.
- No impact-ionization measurement paper in W37-W40 found by grep.

## Not supported / not done
- No fitted m_c or CI; no raw data; figures unread; Eq.(2)(3) exact form; temperature; active area.
- Any quantitative claim about NAND HCI/GIDL; no device data in source.
- Static check: i3_check.py (classes ⊂ style.css, ko/en pairing 64 p = 32 pairs, 13 card rows, no internal names, tags balanced).
