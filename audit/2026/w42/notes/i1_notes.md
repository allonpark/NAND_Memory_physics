# W42 item 1 notes (source: doi 10.1587/elex.23.20260379, Luo et al., IEICE ELEX 23(18) 20260379)

Status: DRAFT section in scratchpad only. No repo writes, no push, no PR.

## Reads (two independent)
- Read 1: cached pdftotext -layout extraction of the J-STAGE ADVANCE PDF, w42/_txt/elex.txt, whole file (38,582 bytes). Greek letters, minus signs, unit prefixes lost. Algorithm 1 and Table I rows present. Header "Vol.21, No.1", footer copyright 2024 (cover 2026).
- Read 2 (2026-10-28): J-STAGE page (WebFetch summary: received 07-13, accepted 07-23, advance online 08-25, published/released 09-25, vol 23 iss 18) and the COPYEDITED PDF (_pdf/-char/en, PDF metadata 2026-09-11) re-downloaded, copied to w42/_dl_s4/elex_read2.pdf, extracted with pdftotext -raw -enc UTF-8 -> w42/_dl_s4/elex_read2_raw.txt, whole file (28,056 bytes). Header "Vol.23, No.18", copyright 2026, "Copyedited September 25, 2026". Algorithm 1/2 and Table I rows NOT in its text layer (images). Units readable: μs, 960B. Eq. (1) glyphs: "Á % ÀTCO Â ÁT; ÁT ¼ Tread À Tprogram" decoded as Δμ ≈ −Tco·ΔT, ΔT = Tread − Tprogram (mapping Á=Δ, %=≈, À=−, Â=·, ¼==; consistent with ÁTco in Eq. 2).
- Figures 1-5 not read as images in either read.

## Number confirmation table
| Value | Read 1 | Read 2 | Status |
|---|---|---|---|
| 24.28% -> 0.44%, 98.19% | yes | yes | confirmed |
| 43.81%, 0.08% | yes | yes | confirmed |
| 774.770 / 440.496 / 435.362 / 435.008 (means) | yes (table+text) | yes (text) | confirmed; unit μs from read 2 only (read 1 "(s)" prefix lost) |
| Baseline P90=max 1094.966, std 323.055 | yes | yes | confirmed |
| MB-RRVC P90 436.020, max 443.300, std 1.320 | yes | yes | confirmed |
| CTDVT P90 438.305, max 606.797, std 25.784 | table only | absent | NOT used (UNKNOWN) |
| Ideal P90 435.666, max 436.177, std 0.415 | table only | absent | NOT used (UNKNOWN) |
| 85 °C, 10 h bake | yes | yes | confirmed |
| Tr −40..120 °C, 20 °C step | yes | yes | confirmed |
| Tp list −40,0,40,80,120 | Algorithm 1 | absent | single read; Fig.5 caption −40/40/120 confirmed in both |
| 45 points, ten traces | yes | yes | confirmed |
| 128-layer other generation | yes | yes | confirmed |
| 32-bit, ~960 | yes | yes | confirmed; unit B read 2 only |
| dates 07-13 / 07-23 / 08-25 | yes | yes | confirmed; 09-25 from J-STAGE page + copyedit PDF + Crossref (sources.yaml) |
| R^2 value, layer count main device, chip/block counts, P/E values, Tco values | - | - | UNKNOWN |

## Derivations
Script: i1_checks.py (this folder). Run: scratchpad\venv_sympy\Scripts\python.exe -I i1_checks.py (sympy 1.14.0). Output: i1_checks_out.txt.
(An earlier run with C:\Python314 used a fraction/sampling fallback because the venv was then missing; superseded by the sympy run, same numeric results.)
- C1: 98.1878% (src 98.19), 43.8076% (src 43.81), 0.0814% rel. to Ideal (src 0.08).
- C2: 5 x 9 = 45 (includes 5 Tp=Tr points); 10 swapped (Tp,Tr) pairs; max |dT| = 160 (from −40 Tp and 120 Tr, both confirmed).
- D1: sensing-only model dmu = g(Tr) − g(Tp): antisymmetry = 0, additivity = 0 symbolically for arbitrary g; quadratic g gives dmu = −a dT − b dT (Tp+Tr−2T0) exactly. Irreversible loss breaks antisymmetry.
- D2: f(u)=ln(1+u)/u, f'(u) = (u − (u+1)ln(u+1))/(u^2 (u+1)) < 0, limit 1 at u->0 (planar).
- D3: E(r0)/E_planar = 1+u for all image charge on channel side; general share C_in/(C_in+C_out).
- D4: |dT|* = sqrt(m^2 − s0^2 z^2)/(s_k z).
No geometry, voltage or thickness number was used anywhere (geometry UNKNOWN in the source).

## Labels and grades used in the HTML
- SOURCE_REPORTED items (1)-(11); AUTHOR_INTERPRETATION (i)-(vi) (GB/trap mechanism cited, "more electrons", ΔT-only conclusion, cycling traps "may", layer non-uniformity "may", physics deferred).
- Grades: measured linearity/compensation B; mechanism attribution C; our frameworks C; DOE D; SSD latency B as simulator result.

## Source inconsistencies observed (put in the "Observed on reading" box)
1. Sec 2 text: bake "after programming", then "random data are then programmed" vs Algorithm 1 program -> bake -> reads (both versions same sentence).
2. Δμ from mean μ, but Fig. 2 text speaks of "median value of Δμ" (population undefined).
3. "baseline condition" for Δμ undefined.
4. "45 cross-temperature points" include 5 zero-ΔT points.
5. "Under the same program/read temperature condition, Baseline shows the highest RBER" conflicts literally with preceding sentence.
6. Advance version header Vol.21 No.1 / ©2024 (template), fixed in copyedited version.
7. ΔT-only conclusion drawn from per-Tp linearity without per-Tp slope comparison; Eq. 2 has no Tp argument.
Additional point (in critical-boundary text): reads up to 120 °C exceed the 85 °C bake; ascending read loop (Algorithm 1, one read) would put any residual loss at high Tr.

## Archive comparison (published only, git show origin/main:reports/2026/wNN/index.html in nand-audit/repo clone)
W37, W38, W39, W40, W43 headings scanned: no cross-temperature read item. Related: W40 i3 (poly-Si grains, coaxial question, TCAD abstract), W37 i1 (lateral migration in CTL), W38 i2 (adjacent-WL VPASS as retention state variable). W41/W42 drafts not used.

## Not supported / left UNKNOWN
Cell geometry (no channel hole/cylinder/radius stated), cell type (CT vs FG not stated), Tco values/units, R^2, sample sizes, P/E levels, Ideal RBER in worst case, which pair is "most severe", read order/dwell actually executed, CTDVT construction.
