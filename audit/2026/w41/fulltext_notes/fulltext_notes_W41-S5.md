# fulltext_notes W41-S5: Oh & Shin, J. Comput. Electron. 25:196 (2026), 10.1007/s10825-026-02647-9 (archive_gap, online 2026-09-29)

Read: pdftotext of publisher OA PDF (33,530 chars), chars 0-33,530 = entire document including references. Figures not viewed; equations (1)-(4) garbled by extraction so only text-stated relations are recorded. Paraphrased.

| Location | Item | Condition | Value | Unit |
|---|---|---|---|---|
| Front page | dates | | Received 2026-05-12; Accepted 2026-09-19 | |
| Abstract; Conclusion | RTN decay constant (delta) vs average trap number N_trap | poly-Si channel 3D NAND | delta ~ N_trap^(1/3); 2D NAND ~ N_trap^(1/2) | - |
| Sec 2 | 2D validation | W, L, Tox varied, 3 levels each; 100 trap positions (10x10) per level | 100 TCAD runs per condition | count |
| Sec 2; Fig 2 | 3D unit cell | read bias Vread on WLn, Vpass elsewhere; channel/filler/O/N/O; macaroni channel | | |
| Sec 2 | 3D trap grid | channel thickness 5 segments, WL length 20 segments | 100 locations | count |
| Sec 2; Fig 3 | single-Si-channel 3D | trends like 2D; delta inversely related to filler radius Rf | axis labels in extraction: L_WL^-0.54, T_poly^-1.03 (figure not viewed) | |
| Sec 2; Fig 4a | poly-Si with random grain boundaries | delta vs Tpoly | non-monotonic | |
| Sec 3 | ANN training set | random grain boundary + trap positions | 1000 TCAD cells | count |
| Sec 3 | Monte Carlo | Markov capture/emission, per cell-variation split | 10,000 runs | count |
| Sec 3 | validity limit | average trap number | analysis only for N_trap >= 3 | |
| Sec 3; Fig 5 | O/N/O thickness exponents (Tox, Tctn, Tbox) | | sum ~0.9, independent of N_trap | - |
| Sec 3; Fig 7 | LWL | low N_trap | delta ~ LWL^(-1/4) approx (text: inversely ~ fourth root); exponent magnitude falls with N_trap | |
| Sec 3; Fig 8 | Tpoly | low N_trap | delta ~ 1/Tpoly; exponent magnitude decreases and saturates with N_trap | |
| Sec 3, near Eq 4 | Vt-shift amplitude distribution | poly-Si 3D | double-Gaussian vs single Gaussian in 2D | |
| Data availability | | | "No datasets were generated or analysed" | |

Labels: scaling statements SOURCE_REPORTED (simulation outputs). Percolation/double-Gaussian explanation = AUTHOR_INTERPRETATION (simulation-supported, no measured data). Applying to product-level BER = EXTRAPOLATION_ONLY. Numeric absolute dimensions (nm) of the simulated cell beyond figure axis ranges: UNKNOWN (not stated in text read).
Geometry check: text and Fig 2c label channel, filler and O/N/O, consistent with a cylindrical coaxial macaroni channel; the paper does not itself use the word "cylindrical" in the text read (ENGINEERING_INFERENCE).
