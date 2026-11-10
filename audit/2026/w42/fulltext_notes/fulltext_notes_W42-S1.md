# fulltext_notes W42-S1: arXiv 2610.20154 (Guido et al., access-rate dependent endurance, HZO capacitors)

Read: pdftotext -layout extraction, characters 0-73233 (whole document: main text lines 1-728, Supporting Information S1-S4 lines 730-1166). Figures not viewed as images. Symbols/Greek letters and some exponents are lost in the extraction; where that matters it is flagged.
Date facts: arXiv v1 submitted 2026-10-14T13:11:11Z (DataCite/arXiv API). Search date 2026-10-26.

| # | Location | Condition | Value (unit) | Label |
|---|---|---|---|---|
| 1 | Sec 2, Methods | Capacitor stack | 5 nm Hf0.5Zr0.5O2; 10 nm TiN top; 30 nm W + 10 nm TiN bottom; ALD 300 C; RTA 500 C N2; area 1963 um^2 | SOURCE_REPORTED |
| 2 | Fig 1c caption, Sec 2 | after bipolar cycling (exponent printed garbled, caption reads as 2x10^6) | Pr 19.3 uC/cm^2; 2Pr 50 uC/cm^2 expected for random polycrystal; switching fraction ~50% -> ~77% | SOURCE_REPORTED (fraction = AUTHOR_INTERPRETATION) |
| 3 | Fig 2b-d | delay 200 ns, 2 us, 20 us, 200 us | peak merging complete ~1e4 cycles; extra 2Pr 10-12 uC/cm^2 at 1e6 cycles; eps_r 34 -> 28.5 | SOURCE_REPORTED |
| 4 | Fig 3, Methods | 1e6 cycles, delay 2 ms, +-2 V, 5 us pulses, wake-up at 100 kHz | unipolar non-switching: coercive-field/peak shift, no 2Pr drop; bipolar: 2Pr drop, no shift | SOURCE_REPORTED |
| 5 | Fig 4a inset, p.10 | HSE06 defect levels | neutral V_O occupied level ~2.0 eV (ZrO2) vs ~2.85 eV (HfO2) below CBM; TiN CB offset 2.3 eV; relaxation shifts empty state up ~1.5 eV | SOURCE_REPORTED (calc) / AUTHOR_INTERPRETATION |
| 6 | Table S1 | HSE06 gaps | ZrO2 5.6 eV, HfO2 6.0 eV | SOURCE_REPORTED (calc) |
| 7 | p.11 | sim | accumulated charge fixed 0.1 C/m^2; D(V_O) 1e-10..1e-12 cm^2/s cited from AIMD; drift velocity 1e-5..1e-4 m/s at 1 MV/cm (cited) | SOURCE_REPORTED (cited) |
| 8 | Eq. (1), (2), S24-S36 | log charge relaxation | alpha, beta fixed at 2e-9 uC^-2 cm^-4 and 1.7 (symbols lost; assignment of which is which UNKNOWN); only tau0 fitted | SOURCE_REPORTED |
| 9 | Table S2 | RT, Fig 5a | tau0 (ns): 200 ns -> 2385.3 (sd 49599.2); 2 us -> 613929.1 (sd 8.4e11); 20 us -> 330.1 (139.1); 200 us -> 157.1 (25.3); 2 ms -> 98.0 (11.2) | SOURCE_REPORTED |
| 10 | Table S3 | delay 2 ms | tau0 (ns): 111.0 @25 C, 79.3 @55, 61.8 @85, 58.1 @105, 53.0 @135 | SOURCE_REPORTED |
| 11 | p.15, Fig 5b inset | Arrhenius of ln tau0 | Ea 0.09 eV (low T) -> 0.04 eV (high T), break ~85 C; V_O migration 0.5-1.2 eV (cited); ref [27] reports 0.2 eV | SOURCE_REPORTED / AUTHOR_INTERPRETATION (de-trapping) |
| 12 | Fig 5a inset | extrapolated | 2Pr at 1e10 cycles vs access rate | EXTRAPOLATION_ONLY |
| 13 | Fig S2 caption | leakage, eps_r | leakage and eps_r "no appreciable variation" during access-rate cycling; eps_r ~27.5 | SOURCE_REPORTED |

Limitations stated by authors: single stack; drift-diffusion is a simplification (kinetic MC would be more realistic but too costly); AIMD diffusion coefficients usually exceed experimental ones; delays > 2 ms not studied.
Not read: all figure images; reference list details beyond [1]-[60] titles.
Short quote (<=1): "cannot be described as a mere superposition of fatigue and imprint effects".
