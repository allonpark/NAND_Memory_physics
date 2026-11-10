# fulltext_notes W42-S4: doi 10.1587/elex.23.20260379 (Luo et al., cross-temperature read-reference compensation, 3D TLC NAND)

Read: pdftotext -layout extraction of the J-STAGE advance PDF, characters 0-38582 (whole 6-page letter incl. references; page 1 text layer was present). Figures 1-5 not viewed as images; Greek letters (delta-Vth, alpha/Tco, delta-T) and some units (Table I time unit, overhead unit) are lost in the extraction.
Date facts: PDF cover Received 2026-07-13, Accepted 2026-07-23, Publicized 2026-08-25. Crossref: issued 2026-09-25, created 2026-08-24T22:12:22Z, volume 23 issue 18. PDF running header says "Vol.21, No.1" and copyright 2024 (template artifact; flagged). Search date 2026-10-26. archive_gap.

| # | Location | Condition | Value (unit) | Label |
|---|---|---|---|---|
| 1 | Abstract, Sec 4.1, Sec 5 | most severe program/read pair of Fig 5 | RBER 24.28% -> 0.44% (98.19% relative reduction) | SOURCE_REPORTED |
| 2 | Abstract, Sec 4.2 | SSDsim | average read response time -43.81% vs baseline | SOURCE_REPORTED (simulator, not drive measurement) |
| 3 | Sec 2 text, Algorithm 1 | characterization | compensation circuit disabled; Tp = -40, 0, 40, 80, 120 C; 85 C bake 10 h; Tr = -40..120 C, 20 C step; random data | SOURCE_REPORTED |
| 4 | Sec 2, Fig 2, Eq. (1) | per Tp | mean Vth shift ~linear in Tread; high R^2 reported (value not in text); depends mainly on delta-T | SOURCE_REPORTED |
| 5 | Sec 2, Fig 3a-c, Eq. (2) | factors | temperature coefficient grows with P/E cycles; varies with state-center voltage; layer index via lookup table; piecewise-linear fits | SOURCE_REPORTED |
| 6 | Sec 2 paras 1,4 | mechanism | poly-Si channel grain boundaries/traps; cycling-induced traps "may" explain growth | AUTHOR_INTERPRETATION (cited, untested here) |
| 7 | Sec 2 end | extra device | 128-layer 3D TLC of another generation: consistent trends (data not shown) | SOURCE_REPORTED (unverifiable here) |
| 8 | Sec 4 | schemes | Baseline (default voltages), CTDVT (lookup-table), MB-RRVC (proposed), Ideal (read-retry optimum) | SOURCE_REPORTED |
| 9 | Table I | 45 temperature pairs x 10 traces | mean 774.770 / 440.496 / 435.362 / 435.008 (Baseline / CTDVT / MB-RRVC / Ideal); P90 1094.966 / 438.305 / 436.020 / 435.666; max 1094.966 / 606.797 / 443.300 / 436.177; std 323.055 / 25.784 / 1.320 / 0.415; unit symbol lost | SOURCE_REPORTED |
| 10 | Sec 4.2 | gap to ideal | MB-RRVC within 0.08% of Ideal mean | SOURCE_REPORTED |
| 11 | Sec 4.2 | overhead | ~960 (unit lost) with 32-bit parameters for the tested chip | SOURCE_REPORTED |

Not stated in the text: main test chip layer count and number of chips/blocks (UNKNOWN); P/E-cycle values tested; retention-time coupling (suppressed by bake); temperature-compensation circuit internals.
Limitations stated by authors: model is "a re-characterizable engineering framework rather than a universal fixed-parameter model"; physics deferred to future device-level work.
Short quote (<=1): "re-characterizable engineering framework rather than a universal fixed-parameter model".
