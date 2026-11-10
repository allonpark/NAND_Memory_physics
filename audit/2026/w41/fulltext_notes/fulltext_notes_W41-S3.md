# fulltext_notes W41-S3: Wang et al., Moore and More 3:15 (2026), 10.1007/s44275-026-00054-7

Read: pdftotext extraction of publisher OA PDF, 73,040 chars; chars 0-62,122 read (front page, Intro, Methods, Results/Discussion, Conclusions, declarations, references to ~[43]). Unread: ~62,122-73,040 (reference tail) and the Supplementary Information file (TDDB protocol, Figs S1-S9). Figures not viewed. pdftotext garbled exponents (e.g. "1 010", "2-1 08", "1 09"); exponents below are my reading of that garbling = ENGINEERING_INFERENCE about typography, flagged "(exp?)".
Quote (one short phrase allowed): authors describe "defect organization" as the controlling factor.

| Location | Item | Condition | Value | Unit |
|---|---|---|---|---|
| Sec 2.1 | stack | TiN 50 nm / HZO / MoOx 50 nm; PE-ALD 280 C; RTA 500 C 30 s N2; 100x100 um^2 | HZO 6, 7, 8 | nm |
| Sec 2.2 | TDDB bias | TiN bottom grounded, positive on MoOx top; CVS | (details in SI, not read) | |
| Sec 2.2 | endurance | bipolar pulses 1 MHz; P-V at 1 kHz | | |
| Sec 3; Fig 2a-b | wake-up field | | 4.0 | MV/cm |
| Sec 3; Fig 3a | endurance 6 nm / 8 nm | 4.2 MV/cm | 6 nm: no breakdown up to ~1e10 (exp?) cycles; 8 nm: breakdown after ~2e8 (exp?) cycles | cycles |
| Sec 3; Fig 3c | E_BD enhancement vs 8 nm (TZDB ramp via PMU) | breakdown = leakage jump > 1 decade | +26.6 (6 nm), +14.1 (7 nm) | % |
| Sec 3; Fig 3d | 2Ec/E_BD trend | | -4 to -6 per nm thickness | %/nm |
| Sec 3; Fig 3f | leakage degradation onset during cycling at 4.0 MV/cm, 1 MHz | | 6 nm none up to ~1e9 (exp?); 7 nm ~1e6 (exp?); 8 nm ~5e7 (exp?) | cycles |
| Sec 3; Fig 4b-d | Hf3+ fraction (8/7/6 nm) | XPS | 7.04 / 7.68 / 8.56 | % |
| Sec 3; Eq 4 | V_O estimate (conversion factor 1/4) | | 0.88 / 0.96 / 1.07 | % |
| Sec 3; Fig S4 (cited) | ZrOx fraction (6/7/8 nm) | | 7.73 / 6.74 / 5.92 | % |
| Sec 3; Eq 5 | Weibull plot | W = ln(-ln(1-F)) | | |
| Sec 3; Fig 5a-c | observed vs Weibull | downward deviation at high percentiles | TDC model fits | |
| Sec 3; Fig 5f | clustering factor change 8 -> 6 nm | | ~ +69 | % |
| Sec 3; Fig 5e | 10-year allowable field | body: 0.001% failure; Fig 5d caption: 0.01% (inconsistent) | 3.84 (6 nm), 3.52 (8 nm) | MV/cm |
| Sec 3; Fig 6b | mean grain size | AFM, >200 grains per sample | ~25 (8 nm) -> ~16 (6 nm) | nm |
| Sec 2.3 | DFT | PWmat, PBE, 50 Ry, 3x3x3 supercell, k 6x6x6 | lattice a,b,c = 0.502, 0.505, 0.524 | nm |
| Sec 3; Fig 7b-c | in-gap defect spread, dispersed vs clustered V_O4 pair | V_O 0.93% | 0.51 -> 1.39 (~2.7x) | eV |

Labels: SOURCE_REPORTED for measured/computed values; V_O concentration is a semi-quantitative inference the authors flag as indirect. Clustering explanation, grain-boundary accommodation = AUTHOR_INTERPRETATION (they admit atomic-scale verification is missing). Any transfer to VNAND oxides = EXTRAPOLATION_ONLY.
UNKNOWN: number of devices per TDDB group, stress voltages/temperature, Weibull slopes numeric values (only in figures/SI).
Internal inconsistency: 0.001% (body) vs 0.01% (figure caption text) for the 10-year extrapolation.
