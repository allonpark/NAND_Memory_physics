# i4 notes — report item 4 (W41), Wang et al., Moore and More 3:15 (2026), DOI 10.1007/s44275-026-00054-7

Writer notes, internal only (not published). Date of work: 2026-10-26. No repo writes, no push, no PR.

## Inputs read
- sources.yaml: header + entry for this source only.
- fulltext_notes for this source (summarizing fetcher notes; exponents flagged as garbled).
- `w41/txt/hzo.txt` = pdftotext extraction of the CC BY PDF (73,453 bytes, legacy-encoded glyphs). READ IN FULL (all 16 pages incl. reference tail and author bios), not only chars 0-62,122 as recorded in sources.yaml.
- Publisher HTML via WebFetch (link.springer.com -> idp.springer.com cookie redirect -> link.springer.com/...?error=cookies_not_supported), 4 fetches on 2026-10-26, page text 139,189 chars; tool covered chars 0-100,000 each time; 100,000-139,189 NOT read (reference tail/footer per fetch tool).
- A curl download of the HTML was attempted and was denied by the permission classifier; not retried, not bypassed.
- NOT read: Supplementary Information (Figs. S1-S9, TDDB protocol, I-t traces, Fig. S3 multi-device endurance); figure images (captions only).
- Format refs: w43/sections/i5.html (structure, labels, card), w43/sections/i4.html (observed box wording), i2.html header. CSS classes used all exist in nand-audit/repo/assets/style.css (checked).
- Archive: `git show origin/main:reports/2026/{w39,w40,w43}/index.html` in nand-audit/repo (origin/main head b12b780). No W41/W42 draft-branch material used.

## Number verification (twice-confirmed rule)
Source 1 = PDF extraction (garbled superscripts), Source 2 = publisher HTML (WebFetch, superscripts rendered; read twice with different prompts).

| Value | PDF extraction | HTML | Status |
|---|---|---|---|
| 6 nm endurance at 4.2 MV/cm | "1 010" | 10^10 (fetch 1), "1010" w/ sup (fetch 2) | CONFIRMED 10^10 |
| 8 nm breakdown cycles | "2-1 08" | 2 x 10^8 (fetch 1 and 2) | CONFIRMED 2x10^8 |
| 6 nm leakage, no increase after | "1 09" | 10^9 (both) | CONFIRMED |
| 7 nm leakage onset | "106" | 10^6 (both) | CONFIRMED |
| 8 nm leakage onset | "5-1 07" | 5 x 10^7 (both) | CONFIRMED |
| DFT energy criterion | "1-1 0-5 eV" | 1 x 10^-5 eV | confirmed once in HTML; NOT used in HTML item |
| E_BD +26.6% / +14.1% | yes | yes | CONFIRMED |
| 2Ec/E_BD -4-6%/nm | yes | not asked | single read (PDF text clear, no exponent) |
| Hf3+ 7.04/7.68/8.56; V_O 0.88/0.96/1.07 | yes | V_O confirmed | CONFIRMED (+ sympy reproduces) |
| ZrOx 7.73/6.74/5.92 (6/7/8) | yes | not asked | PDF text clear |
| alpha +~69% | yes | yes | CONFIRMED |
| 10-yr field 3.84 / 3.52 MV/cm | yes | yes | CONFIRMED |
| failure prob body 0.001% vs caption 0.01% | yes | yes (fetch 1 and 2) | CONFIRMED INCONSISTENCY |
| Fig 5 panel refs (body 5d=63.2% lifetimes, 5e=10-yr; caption 5d=10-yr extrapolation, 5e=10-yr E_BD) | yes | yes (fetch 4) | CONFIRMED MISMATCH |
| grain 25 -> 16 nm, AFM 1x1 um^2, >200 grains | yes | AFM area yes | CONFIRMED |
| 0.51 -> 1.39 eV, ~2.7x, V_O 0.93% | yes | yes | CONFIRMED |
| RTA 500 (unit glyph lost in PDF) | "500  for 30 s" | "500 ℃" | CONFIRMED 500 ℃ |
| PE-ALD 280 °C, 100x100 um^2 | yes | yes | CONFIRMED |
| Eq. (4)-(7) forms | garbled | LaTeX transcribed (fetch 3) | Eq 6: Fc=1-[1+(1/alpha)(t/tau)^beta]^-alpha ; Eq 7: beta=gamma d/a0 ; Eq 5 and 4 as in HTML. Structure consistent with garbled PDF; HTML-confirmed once by a transcription prompt. |
| TDDB device count, stress V/E, temperature | absent in main text (fetch 2 states so; PDF text points to SI) | — | UNKNOWN |
| alpha, beta numeric values | figure-only | — | UNKNOWN |

No garbled exponent remained unconfirmed among the values used in the HTML.

## Observed-on-reading items (in HTML box, not author-confirmed)
1. 0.001% (body, Sec. 3) vs 0.01% (Fig. 5 caption) for the 10-year extrapolation.
2. Fig. 5 panel-letter mismatch body vs caption; caption says "Operation voltage extrapolation", body "operating electric field".
3. Leakage-degradation onset non-monotonic: 7 nm (~10^6) earlier than 8 nm (~5x10^7); not discussed by the authors.
4. tau called "mean time to failure"; in the Weibull limit mean = tau*Gamma(1+1/beta) (sympy (6)).

## Sympy derivations
Script: `i4_checks.py` (same folder), run with venv_sympy python -I, sympy 1.14.0. Output: `i4_checks_out.txt`.
Mapping script -> HTML inference box:
- (1),(2),(3) -> (i) internal consistency. (2) uses an ASSUMPTION not in the source: 12-atom orthorhombic HZO cell with 8 O; labeled in HTML.
- (4),(4b),(10) -> (ii) field vs voltage and (iii) E_BD baseline. V = E*d with 1 MV/cm x 1 nm = 0.1 V; ignores dead layer, Vfb, work-function asymmetry, polarization (stated in HTML).
- (5a)-(5d) -> (iv) TDC tail structure. alpha = 1, 2, 5 are illustrative values, labeled "not from the source".
- (6) -> observation (4).
- (7) -> (v) a0 bound (< 3/4).
- (9) -> (vi) gamma-mixture identity: TDC survival = Gamma(alpha, alpha)-mixed Weibull/exponential survival.
- (8) -> NAND contrast box (coaxial formula, symbolic only, no NAND numbers).

Full output copied here:
```
sympy 1.14.0
(1) d=8 nm: Hf3+=7.04% -> V_O = Hf3+/8 = 0.8800%
(1) d=7 nm: Hf3+=7.68% -> V_O = Hf3+/8 = 0.9600%
(1) d=6 nm: Hf3+=8.56% -> V_O = Hf3+/8 = 1.0700%
(2) O sites (assumed 8 O/cell) = 216 ; 2/nO = 0.9259259259259259 %  (source: 0.93%)
(3) 1.39/0.51 = 2.7254901960784315
(4) E10y ratio 6/8 = 1.0909090909090908 -> + 9.090909090909092 %
    V10y(d=6 nm) = E*d = 2.304 V
    V10y(d=8 nm) = E*d = 2.816 V
    endurance field 4.2 MV/cm, d=6 nm -> V = 2.52 V
    endurance field 4.2 MV/cm, d=8 nm -> V = 3.36 V
    wake-up/leakage cycling 4.0 MV/cm, d=6 nm -> V = 2.4 V
    wake-up/leakage cycling 4.0 MV/cm, d=7 nm -> V = 2.8 V
    wake-up/leakage cycling 4.0 MV/cm, d=8 nm -> V = 3.2 V
(4b) V_BD(6)/V_BD(8) = 1.266*6/8 = 0.9495 ; V_BD(7)/V_BD(8) = 1.141*7/8 = 0.998375
(5a) lim alpha->oo Fc - Fweibull = 0
(5b) W(x) small-x series = log(x) - x/(2*alpha) + 5*x**2/(24*alpha**2)
(5c) dW/dln t = beta*x/((alpha + x)*log((alpha + x)/alpha))
     at x->0: beta ; as x->oo: 0
(5d) x_p TDC = -alpha + (-alpha**alpha/(p - 1))**(1/alpha)
     alpha=1, p=1e-05: 1.00001 | p=1e-4: 1.00005 | p=0.632: 1.71795 | p=0.99: 21.4976
     alpha=2, p=1e-05: 1.00000 | p=1e-4: 1.00003 | p=0.632: 1.29733 | p=0.99: 3.90865
     alpha=5, p=1e-05: 1.00000 | p=1e-4: 1.00001 | p=0.632: 1.10698 | p=0.99: 1.64151
(6) mean of Weibull limit = tau*gamma(1 + 1/beta)
(7) a0(6nm)/a0(8nm) = 3*beta8*gamma6/(4*beta6*gamma8) ; with gamma6<=gamma8 and beta6>beta8 => < 3/4
(8) dV = log((r_out/r_in)**(Qp/(2*pi*epsilon)))
    E(r_in)/(V/t) at equal V = t_d/(r_in*log((r_in + t_d)/r_in)) ; limit t/r_in->0: 1
(9) E_lam[exp(-lam x)] = (alpha/(alpha + x))**alpha ; equals (1+x/alpha)^-alpha: True
    variance of lam = 1/alpha
(10) constant-V_BD reference: E_BD(6)/E_BD(8) = 8/6 = 1.3333 ; source 1.266 ; 7 nm: 8/7 = 1.1429 ; source 1.141
```

## Grades (A/B/C/D) used
- Measured trends: B — peer-reviewed measurement, internal arithmetic recomputed; device counts/uncertainty UNKNOWN. (Not A: no raw data or reproduction by us.)
- Defect-organization mechanism: C — fit-parameter-based author interpretation, no direct evidence, alternatives not excluded.
- 10-year allowable field: C — acceleration model and probability basis unclear.
- NAND transfer: D — EXTRAPOLATION_ONLY.

## Key analytic findings (for synthesis)
- E_BD gain is almost exactly the constant-voltage expectation for 7 nm (1.141 vs 8/7=1.143) and 95% of V_BD(8 nm) for 6 nm: TZDB data are compatible with a near-thickness-independent breakdown voltage; the "+26.6%" is a field-normalization effect to a large extent (hypothesis, not proof).
- 10-year allowable value: field basis favours 6 nm (+9.1%), voltage basis favours 8 nm (2.304 V vs 2.816 V).
- TDC alpha does not change low-percentile quantiles for fixed (beta, tau); it affects extrapolation only through the fitted beta. Alpha is mathematically identical to a gamma-distributed device-to-device hazard multiplier, so "clustering inside film" is not identifiable from shape alone.
- 6 nm 10^10 cycles is censored (no breakdown) — lower bound.

## Archive comparison sources
- W39 item 1: Wu & Ando, Front. Nanotechnol. (published 2026-09-14), H-doped HfO2 generation-annihilation area scaling.
- W40 item 5: Yan et al., J. Phys. D 59(37) 375105, abstract only, SiC PWM TDDB (archive gap).
- W43 item 2: Cheng et al., Fractal Fract. 10(10) 728, abstract only, BGW shape invariance.
- W40 item 2 (pool-capacitor oxide defect) judged not TDDB-statistics related enough; not used.

## Self-check
`i4_selfcheck.py` -> `i4_selfcheck_out.txt`: 41 ko / 41 en paragraphs, every ko followed by en; classes all in style.css; 13 card rows; no internal names (W41, sources.yaml, scratchpad, model names, track ids), no "(exp?)", no .qc block; no non-polite Korean sentence endings detected (heuristic); HTML tags balanced.
Not done: independent critic review; rendering in the full report shell.
