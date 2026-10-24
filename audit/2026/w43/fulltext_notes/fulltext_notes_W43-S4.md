# fulltext_notes W43-S4 — 10.3389/fnano.2026.1961029 (Frontiers in Nanotechnology 8, 1961029)
Read via WebFetch of frontiersin.org /full (Sections 1-4, Tables 1-3; figures not viewable; Eq.1 symbols missing). Read date 2026-10-21. Simulation-only paper.

| Location | Condition | Value | Unit | Tag |
|---|---|---|---|---|
| Sec.2.1 / Table 1 | Source material, Eg, length | Ge p+, 0.66, 20 | eV, nm | SOURCE_REPORTED |
| Sec.2.1 / Table 1 | Si body thickness / gate length | 20 / 70 | nm | SOURCE_REPORTED |
| Sec.2.1 / Table 1 | Gate stack | 2 nm SiO2 + 7 nm HfO2; WF 4.25 eV | nm, eV | SOURCE_REPORTED |
| Table 1 | Doping source/drain/pocket/channel/light channel | 5e19 / 1e19 / 5e19 / 1e19 / 1e18 | cm^-3 | SOURCE_REPORTED |
| Sec.2.2.1 | BTBT Si: A, B | 3.29e15, 2.38e7 | cm^-3 s^-1, V/cm | SOURCE_REPORTED |
| Sec.2.2.1 | BTBT Ge: A, B | 1.67e15, 6.55e6 | cm^-3 s^-1, V/cm | SOURCE_REPORTED |
| Eq.1 | Kane / WKB non-local BTBT expression | symbols lost in extraction | - | UNKNOWN |
| Sec.2.2.2 / Table 2 | Trap type, ET, sigma_E | acceptor, 0.0, 0.1 | eV | SOURCE_REPORTED |
| Table 2 | Mean Nit, spatial sigma, peak Nit | 4.96e12, 2.88e12, 9.88e12 | cm^-2 eV^-1 | SOURCE_REPORTED |
| Table 2 | Capture cross-section n and p | 1e-15 | cm^2 | SOURCE_REPORTED |
| Sec.2.2.3 | Segments / Monte Carlo devices | 14 x 5 nm; 100 per case | - | SOURCE_REPORTED |
| Sec.3.1 | Trap-free ION / IOFF / Vth / v_e / SS_min | 1.208e-10 / 1.71e-13 / 0.3137 / 1.37e8 / 38.4 | A/um, A/um, V, cm/s, mV/dec | SOURCE_REPORTED |
| Sec.3.2, Fig.6 | Channel traps: ION / v_e / SS | 1.192e-10 (~1.3% drop) / 7.85e7 (~42% drop) / 148.12 +/- 4.12 | A/um, cm/s, mV/dec | SOURCE_REPORTED |
| Sec.3.3, Fig.8 | Pocket traps SS | 142.94 +/- 2.41 | mV/dec | SOURCE_REPORTED |
| Sec.3.4, Fig.10 | Both regions SS / ION | 148.35 +/- 3.69 / 1.192e-10 | mV/dec, A/um | SOURCE_REPORTED |
| Sec.3.5.1, Fig.11a | Peak E-field, trap-free, at x = 22.14 nm | 1.067e5 | V/cm | SOURCE_REPORTED |
| Fig.13 | Gaussian vs uniform trap distribution | "marginal shift", no numbers | - | SOURCE_REPORTED |

Inconsistencies (my cross-check of the text, ENGINEERING_INFERENCE): (1) pocket called 'immune' vs SS 38.4 -> 142.94 mV/dec; (2) IOFF 1.71e-13 (Sec.3.1) vs 1.71e-12 (Table 3); (3) Sec.3.4 says 'reduction in SS' though SS rises in all trap cases; (4) channel dopant (As) in Fig.1 caption not stated in text.
UNKNOWN: temperature dependence, experimental validation, Debye length value, mean ET values partly lost.
Limits stated by authors: simulation only, 100 MC devices (no tails), borrowed BTBT coefficients, Gaussian trap form not physically derived.
