# fulltext_notes W41-S1: Cottom & Olsson, arXiv:2610.06173v1 (2026-10-05)

Read: pdftotext (non-layout) extraction, 75,396 chars; chars 0-52,241 read (main text, methods, references, start of SI). Unread: chars 52,241-75,396 (SI figs/tables S3-S12, Tables S1-S8). Figures not viewed; captions only. Paraphrased; no quotes beyond the title.

| Location | Item | Condition | Value | Unit |
|---|---|---|---|---|
| Abstract, Sec 2.1 | paired neutral/negative cells | a-Si3N4, HSE06 | 415 pairs (455 deposited, 40 excluded) | count |
| Sec 2.2 | classified traps by route | | polaron 165, induced K 182, native K 65 (=412); 3 unassigned | count |
| Sec 2.2 | CV classification accuracy (T0, delta readouts) | 15-NN, 5-fold | 95.7 | % |
| Sec 2.2 | AUC polaron vs induced-K (precursor vector) / induced vs native (trapped vector) | logistic reg. | 0.83 / 0.87 | - |
| Sec 2.2 | AUC without coordination channels, polaron vs induced K | | 0.50 | - |
| Sec 2.2 | median relative fingerprint change delta | by route | 0.821 polaron, 1.665 induced K, 0.201 native K | - |
| Sec 2.2; Fig 3e | median effective participation (relaxation) / max displacement | by route | 9.6 atoms,0.51 A induced K; 12.0 atoms,0.30 A polaron; 3.8 atoms,0.40 A native K | atoms, angstrom |
| Sec 2.3 | 5th-95th percentile ranges | all traps | participation 4-33 atoms; RMS displacement 0.12-0.30 A; corrected stabilisation 0.9-2.1 eV | |
| Sec 2.3; Fig 4a | Spearman: occupation response vs localisation gain | n=412 | 0.765 | - |
| Sec 2.3; Fig 4b | Spearman: fingerprint change vs RMS displacement | n=412 | 0.636 (R2 0.26 vs 0.24 route-mean baseline) | - |
| Sec 2.3; Fig 4c | Spearman: graph deformation Q_D vs stabilisation | n=412 | 0.664; held-out R2 0.59 (Q_D), 0.60 (max displacement), 0.70 (ridge, 205 descriptors) | - |
| Sec 2.4; Fig 5a | Si4 precursors converting to Si3 on capture | | 182 of 347 | 52.4 % |
| Sec 2.4; Fig 5c | induced-K share of top stabilisation decile | 42 traps | 30 (71.4%) vs 44.2% base rate; polaron 3 (7.1%) vs 40.0% base | |
| Sec 2.4 | induced-K share of deepest spectral-depth decile | | 29 of 42 | 69.0 % |
| Fig 2 caption | example cell box_106 | | participation 13.24 -> 4.72 atoms; delta log10 I = 0.448; neutral mobility edges -1.020 and +4.300 eV | eV |
| Methods 4.1 | DFT | CP2K v2023.1, HSE06, Gamma, spin-polarised, DZVP-SR-MOLOPT, GTH; cutoffs 650/70 Ry | force 0.005 eV/A, energy 1e-7 eV | |
| Methods 4.1 | structure generation | MG2 melt-quench, NPT, cooling 1 K/ps; cell relax at hybrid level | | |
| Methods 4.3 | dielectric constants for correction | clamped-ion / static | 4.2 / 7.8 | - |
| Methods 4.3 | mobility-edge criterion | N_eff >= 56 (one fifth of cell) | | atoms |
| Methods 4.4 | graph | Si-N contact cutoff 2.33 A, Gaussian sigma 1.25 A, diffusion scales t = 0.5,1,2,4,8 | 116,200 neutral atoms standardised | |
| Data availability | structures | Zenodo 10.5281/zenodo.21111822 (not opened) | | |

Evidence labels: all table values SOURCE_REPORTED. Interpretations ("charge-induced Si-N bond breaking is the dominant route to the deepest traps in this ensemble") are AUTHOR_INTERPRETATION limited by the authors to "this ensemble".
Not verified: Zenodo data, GitHub code, supplementary tables. No independent recalculation.
