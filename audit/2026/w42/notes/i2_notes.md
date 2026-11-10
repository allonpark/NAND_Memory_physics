# W42 item 2 — writer notes (source W42-S5, arXiv:2512.15988v1, Kim et al., Perspective)

Output: i2.html (same folder). `<section id="i2">`, classes only from assets/style.css
(boundary, sourcebox, inference, label, chain, eq, doebox, compare — all present in the clone's style.css).
No repo writes, no push, no PR.

## Reads
- Read 1 (linear): cached layout extraction `w42/_txt/2512.15988.txt`, lines 1–1108 = bytes 0–91,986
  (main text ends at 90,546 = data-availability statement; then references 1–9). File is non-UTF-8
  (U+FFFD for some symbols: ±, ≤, °, superscripts, en-dashes).
- Read 2 (independent cross-check, not a linear re-read): PDF re-downloaded 2026-10-28 via WebFetch
  (arxiv.org/pdf/2512.15988v1), saved to `sections/_dl_i2/2512.15988v1.pdf`
  (sha256 eeb525f17d8be751f82bd838831c73960a20932d434f5ec9ec93fdc2c6f9dd3e), extracted with
  `pdftotext -enc UTF-8` (raw mode, no -layout) -> `sections/_dl_i2/read2_raw.txt` (85,700 chars; main
  text 0–63,028; references after). Every number in the HTML was grep-confirmed in read 2.
  Reference list (`_dl_i2/refs.txt`) read at title level for refs 21, 22, 25, 26, 39–41, 57, 66–68, 79,
  80, 87–102, 105, 107–110.
- Figures not viewed as images. Fig. 3 equations garbled in both reads -> UNKNOWN. Fig. 4 table cells
  scrambled in read 1 -> not used.
- Archive comparison: `git show origin/main:reports/2026/{w37,w38,w39,w40,w43}/index.html` from the
  nand-audit clone, saved to `sections/_arch_i2/`, snippets via `_arch_i2/arch_extract.py`.
  No W41/W42 draft material used. No published week mentions 2512.15988, ferroelectric or FeNAND.

## Number confirmation (two reads)
| Value | Read 1 | Read 2 | Status |
|---|---|---|---|
| WL+space oxide ≈40 nm (ref 22) | yes | yes | confirmed |
| PGM "typically above 20 V" | yes | yes | confirmed |
| "typically exceeding ±20 V" | "?20 V" (symbol lost) | "±20 V" | number confirmed; ± single-read (stated in HTML) |
| ISPP slope CTF cannot exceed 1; FeNAND above 2 | yes | yes | confirmed |
| CTF "about 103 to 104 cycles" | "103 to 104" | "103 to 104" | digits confirmed; 10^3–10^4 = context interpretation (stated) |
| FeFET below 5 V, tens of ns | yes | yes | confirmed |
| gate-side FeNAND 103-104 cycles | yes | yes | as above |
| poly-Si crystallization exceeding 950 °C | "950 C" | "950 ◦C" | confirmed |
| amorphous OS mobility (50 cm2/Vs) | "(50" symbol lost | "(≤50" | number confirmed; ≤ single-read (stated) |
| poly OS >100 cm2/Vs | yes | yes | confirmed |
| poly-Si degrades below 3 nm; OS sub-nm | yes | yes | confirmed |
| >1,000 layers, >100 GB/mm2 (Fig.1 caption) | yes | yes | confirmed; axis "Gb/mm2" both reads |
| FeMFET stack beyond 50 nm | yes | yes | not used in HTML |
| Fig 2a strings VPASS WL0 / VPGM WL1 / VPASS WL2 | yes | yes | used as figure strings only |

## Label decisions
- Cited CTF statements = SOURCE_REPORTED but explicitly "literature-cited, not measured by authors".
- Reasoning/proposals (V_BD trade-off as FN origin, GAA imbalance + CAA, RAWD detrap pulse, ERS retention
  loop, OS hole issues, BTI, projections) = AUTHOR_INTERPRETATION.
- ΔV_WL = V_PGM − V_PASS across space oxide = ENGINEERING_INFERENCE from Fig. 2a strings (text says only
  "field during programming").
- Grades: overall C (no new data; data-availability statement). Projections D. Checklist criteria D.

## SymPy derivations
Script `i2_checks.py`, output `i2_checks_out.txt`; venv_sympy python -I (sympy 1.14.0, mpmath 1.3.0,
Python 3.14.3); exit 0, ALL PASS. (An earlier stdlib-only draft was replaced after the venv was restored.)
- A: GAA E_IL/E_GBL = (eps_GBL/eps_IL)(r_b/r_a); CAA = (eps_GBL/eps_IL)(r_a/r_b); product of geometric
  factors 1; 1+t/r_a and 1−t/(r_a+t); both → 1 as t/r_a → 0.
- B: coax/planar V_FB shift for one layer = ln(1+u)/u < 1, → 1 as u → 0.
- C: lumped ISPP steady state slope = 1; with extra non-charge V_T term ΔP per step: 1 + ΔP/s.
- D: dm/dt_sp = E_BD/ΔV_WL; d ln t_BD/d ln t_sp = γΔV_WL/t_sp (fixed ΔV_WL); zero at fixed field.
- E: GB vs Gb factor 8; 299 days from 2025-12-17 to 2026-10-12 ≈ ten months.

## Source inconsistencies noticed (observed on reading, not confirmed by authors)
1. Fig. 1 axis "Gb/mm2" vs caption "100 GB/mm2" (factor 8).
2. p.27 "promising superior endurance" vs gate-side FeNAND 10^3–10^4 cycles = same range as CTF (p.20).
3. Gate-injected carrier: p.17 holes (or e- detrapping) positive Q_it,gate; p.21 "gate-injected electrons
   are trapped"; p.26 ERS-state loss of gate-injected electrons. Consistent only if holes at PGM and
   electrons at ERS — not stated.
4. Citation mapping by title: CTF 10^3–10^4 cycles cites 39 (NC flash), 67, 68, 79 (FeFET/FeNAND
   papers); poly-Si <3 nm cites 110 (ALD indium-oxide transistors); OS BTI cites [90] (HfO2 FeFET Vth
   window; also used for RAWD p.24) in square brackets unlike the superscript style elsewhere, [80] (3D
   vertical FeNOR); GAA imbalance cites 87 (hetero-strain GAA nanowire FET). Originals not read.
5. >950 °C poly-Si crystallization is a cited process value; generality not established.
6. Fig. 3 analytical-model equations garbled in both extractions (not reconstructed).

## Not supported / left UNKNOWN
- Space-oxide thickness alone, V_PASS, breakdown test conditions/statistics/location, CTF endurance
  criterion, retention T/t, GIDL bias/speed, poly-Si thickness/grain size, Fig. 3 equation forms, Fig. 4
  cell values, any tail/Weibull information. Original cited papers unread.
