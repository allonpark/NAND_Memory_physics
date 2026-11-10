# fulltext_notes W42-S2: arXiv 2610.16438 (Chen et al., CSC-AOS MOS trap-state spectroscopy)

Read: pdftotext -layout extraction, characters 0-23584 (entire 4-page letter incl. figure captions and reference list). Two-column layout is interleaved in the extraction; I re-associated sentences by section headings. Figures not viewed as images. Units like um^2 and eV^-1cm^-3 were partly stripped by extraction; values below are as recoverable.
Date facts: arXiv v1 submitted 2026-10-12T09:03:22Z. Search date 2026-10-26.

| # | Location | Condition | Value (unit) | Label |
|---|---|---|---|---|
| 1 | Sec II, Fig 2 | device | bottom gate 30 nm Ni; 100 nm SiO2 on p+ Si; 6 nm HfO2 ALD, N2 400 C 30 min; 4.5 nm IGZTO (sputter, Ar, RT); Ni/W/Pt S/D; O2 anneal 400 C 1 h; 5 um overlap margin | SOURCE_REPORTED |
| 2 | Sec III-A, Fig 3a | transfer curve | SS ~63.6 mV/dec; hysteresis ~4.7 mV | SOURCE_REPORTED |
| 3 | Sec III-A, Fig 3b-d | S/D shorted vs drain floating | depletion capacitance with drain floating ~half of shorted; nominal channel area 400 um^2, total S/D overlap 900 um^2, effective channel ~600 um^2 | SOURCE_REPORTED (effective area = authors' estimate) |
| 4 | Sec III-B, Fig 4a-d | drain floating | Gp/omega peak shifts with Vg; f_peak linear in total conductance 1/R_total; time constant follows R_total -> RC origin | SOURCE_REPORTED |
| 5 | Sec III-B, Fig 4b, 8a | 1 kHz component | follows DC gate leakage; falls ~1/f; negligible above 100 kHz | SOURCE_REPORTED |
| 6 | Sec III-B, Fig 5 | L varied, W=10 um | longer channel adds extra Gp/omega peaks (distributed channel resistance) | SOURCE_REPORTED |
| 7 | Sec III-C, Fig 6 | optical + UPS | Eg 3.839 eV; EC-EF ~0.283 eV | SOURCE_REPORTED |
| 8 | Fig 7-8, text | L=5 um, W=80 um, Vg -1..-0.1 V | Dit 9-12e11 eV^-1cm^-2; tau ~250 ns constant; possible donor-like contribution | SOURCE_REPORTED / AUTHOR_INTERPRETATION |
| 9 | Fig 9a-f, text | Vg 0-0.7 V | shallow-state apparent DOS 1e18-1e19 eV^-1cm^-3 Gaussian-like; tau us..ns; ~0.3 eV surface-potential modulation; no complete RC correction | SOURCE_REPORTED (authors: still contains residual RC) |
| 10 | Fig 9g-j, text | Vg 0.8-2 V | Dit initially drops then rises to 2.8-3.1e12 eV^-1cm^-2; tau ~250 ns; ~3x depletion value | SOURCE_REPORTED |
| 11 | Fig 10 | W=80 and 50 um, L=5 um | consistent Dit and tau (~250 ns) after area normalization | SOURCE_REPORTED |
| 12 | Conclusion | scope | method claimed "simple, scalable" for AOS trap characterization | AUTHOR_INTERPRETATION |

Not stated in the text read: measurement temperature; number of devices measured; any stress (BTI/PBTI) experiment; statistical spread. These are UNKNOWN, not zero.
Limitations stated: residual RC contamination; need for rigorous equivalent-circuit model; minimum in Dit at low accumulation "requires further clarification" (e.g. low-temperature measurement).
Not read: figure images; supplementary (none referenced).
Short quote (<=1): "providing intuitive metrics for understanding reliability degradation".
