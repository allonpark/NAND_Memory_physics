# fulltext_notes W42-R1 (reserve, not in the 5): arXiv 2608.09622 (Elhagrasy, Hill, Ivanov, MCTS adaptive test planning)

Read: pdftotext -layout extraction, characters 0-100174 (title through reference [18]; whole technical body incl. Tables I-XI, limitations and conclusion). Characters 100174-110722 (rest of reference list) not read. Figures not viewed as images. arXiv v1 submitted 2026-08-10T14:04:22Z (DataCite shows later 'Updated' 2026-08-17; PDF header reads v1). archive_gap.

| # | Location | Condition | Value | Label |
|---|---|---|---|---|
| 1 | Eq (1)-(4), Sec III-A | action grid | V {0.9,1.0,1.1,1.2} V; J {0.8..3.0} normalized; T {325,350,375} K; t {50,100,150,200} h | SOURCE_REPORTED (simulation design) |
| 2 | Eq (7)-(8), (9)-(11) | models | BTI stretched exponential; EM Black; TDDB E-model with power-law voltage term; reference 1.1 V, 350 K; no Weibull statistics used | SOURCE_REPORTED |
| 3 | Table I-II | calibrated | Vmax 0.20 V; EM Q 0.80 eV, n 2.0; TDDB Ea 0.70 eV, gamma-like exponent 3.0 (symbol lost); chosen so the three mechanisms fail at comparable (~150 epoch) times | SOURCE_REPORTED (assumed, "representative simulation values") |
| 4 | Sec III-C | threshold | Vfail = 0.09 V (~45% of mean asymptote 0.20 V) | SOURCE_REPORTED |
| 5 | Fig 1, Table V | 5000 iterations | CY 20.4% -> 54.2% across 500-iteration windows; 39.2% cumulative; random 16%, fixed-stress 22% | SOURCE_REPORTED |
| 6 | Table VI | best sequence | 119 epochs; D_EM 0.564; D_TDDB 0.537; U 0.044 | SOURCE_REPORTED |
| 7 | Table IX-X | perturbation | device mean +10% -> CY 83.2%; -10% -> 0%; BTI-only +-10% -> 69.6% / 0.0% | SOURCE_REPORTED |
| 8 | Sec VIII-E | limitations | simulation-only; single technology calibration; BTI recovery omitted; 38 h single-core run; EM/TDDB damage assumed directly observable | SOURCE_REPORTED |

Why reserve only: no experimental device data; parameters assumed; far from VNAND. Short quote (<=1): "Simulation-only validation".
