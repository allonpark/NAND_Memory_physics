# W41 report-level synthesis notes (internal; not for publication)

Files written: report_head.html, report_tail.html, synth_notes.md (+ helper scripts _en_extract.py, _report_check.py and i*_en.txt text dumps; all in this folder).
Inputs read: sources.yaml (whole), i1–i5.html (English text extracted in full via _en_extract.py; Korean paragraphs are paired translations), i1–i5_notes.md, W43 report_head/report_tail (format reference).
No repo access, no push, no PR. Independent physics review: NOT done (QC marked PENDING).

Item ↔ manifest id mapping (internal only, never in HTML): item 1 = W41-S5 (Oh & Shin), item 2 = W41-S1 (arXiv 2610.06173), item 3 = W41-S2 (arXiv 2610.11643), item 4 = W41-S3 (Wang et al., HZO), item 5 = W41-S4 (Qiu et al., SiC).

## Mechanical check (_report_check.py on head + i1..i5 + tail)
- KR→EN pairing: head 22/22, tail 85/85, full document 297/297, 0 pair errors.
- Tags balanced (div, p, table, tr, td, section, article, ol, li, h2, h3, span); all TOC anchors resolve (#overview, #i1..#i5, #synthesis, #matrix, #insight, #hypotheses, #qc, #sources).
- No internal ids, file paths, manifest name or model names in head/tail. "grade A" hit = the sentence "no grade A in this issue" (intended).
- Korean ending heuristic: only bold run-in labels and the label-definition list (same pattern as W43) are flagged.
- 5 unique doi.org links in sources; arXiv abs links added for items 2 and 3.
- Not done: rendering, PDF build, page visual check.

## Claim → support trace
### Hero / evidence banner / overview
| Claim | Support |
|---|---|
| Items 1–4 full text, item 5 abstract only | manifest counts full_text 4 / abstract_only 1; source_access per entry; i1–i5 sourcebox |
| Items 1, 4: pdftotext of OA PDF + publisher HTML via summarizing tool | i1_notes "What was read" 1–2; i4_notes inputs (hzo.txt + WebFetch); i1/i4 sourcebox |
| Items 2, 3: arXiv PDF pdftotext; item 2 also arXiv HTML | i2_notes re-fetch; i3_notes re-fetch (HTML not fetched for item 3) |
| Figures not read (all) | manifest header; each item sourcebox |
| Garbled eqs UNKNOWN: item 1 Eqs (1)–(4); item 3 trap-depth and void-fraction equations | i1 UNKNOWN box; i3 UNKNOWN para + Governing relations |
| Item 2: no equation left UNKNOWN (not stated in HTML, consistent) | i2_notes verification table |
| Item 5 publisher 403, not bypassed | manifest S4 resolve_evidence; i5 sourcebox |
| Dates 10-05, 10-08, 10-09, 10-09; item 1 2026-09-29, 6 days | manifest online_date; i1 archive_gap box (6 days) |
| No in-window VNAND-direct paper; keyword search not proof of absence | manifest meta in_window note; i1 archive_gap box |
| Item 1 geometry UNKNOWN (macaroni, filler Rf; "cylindrical" absent) | i1 UNKNOWN box; i1_notes confirmation table |
| Items 2–3 one research line, not independent | manifest S2 overlap_check; i2 box; i3 box |
| No grade A; only grade B = item 4 measured trends | i4 card CONFIDENCE (B); all other cards C/D |
| Symbol collisions (δ, η, β, γ, t) | i1 governing (δ, γ, t = Tpoly/rf); i2 (δε, η, t diffusion scale); i3 (η = 1/4, βm, t thickness); i4 (β, γ, t time, τ); i5 (η scale, β, γ [cm/MV]) |
| Coaxial relations: items 3/4 field ratio, item 1 sheet ratio ln(1+u)/u (reciprocal), item 2 ΔVth(rc), item 5 J ratio r1/r0 | i3 geometry box; i4 NAND box; i1 geometry block; i2 "Bulk cell vs coaxial CTL"; i5 NAND box. Reciprocal = my algebra (u/ln(1+u) vs ln(1+u)/u) |
| Per-item table numbers | i1 SOURCE_REPORTED (7)–(9); i2 results para; i3 SOURCE_REPORTED; i4 SOURCE_REPORTED; i5 abstract para |
| Lead (1): fixed-fraction double-Gaussian + independent traps → 1/2 | i1 ENGINEERING_INFERENCE box (SymPy D1) |

### Synthesis
| Claim | Support |
|---|---|
| Bulk cells ~14–15 Å | i3 D2 / geometry box |
| Item 5 treats oxide as planar MOS, trench UNKNOWN | i5 governing relations; i5_notes |
| Direction of coaxial effects (inner field up; sheet amplitude down; fluence up at inner interface) | i3/i4 boxes; i1 SymPy (a); i5 NAND box |
| Item 1 trap location UNKNOWN; split by percolation distance | i1 UNKNOWN box; AUTHOR_INTERPRETATION |
| Item 1 τc/τe not in text | i1 UNKNOWN box |
| Items 2–3 route fractions not volumetric density | i2 UNKNOWN box/H1; i3 D4 |
| Item 2 derivation F (Dtrap ranking ≠ ET ranking) | i2 derivation F |
| Item 3: 415 of 499 cells from same group's population | i3 SOURCE_REPORTED, one-line box |
| Mobility edge: item 2 N_eff ≥ 56 (1/5); item 3 N/4 with 0.35 eV shift N/5↔N/4 | i2 SOURCE_REPORTED comp. conditions; i3 governing relations + observation (5) |
| Item 2 SI Table 2 depths uncorrected 3.24/3.65/3.49; item 3 corrected 3.25/3.34/2.87 = low-density endpoint | i2 results + observation (3); i3 observation (3) |
| Route order differs | i2 (polaron/iK/nK) vs i3 (nK/iK/pol) |
| Item 4 α ≡ gamma-mixed heterogeneity | i4 derivation (vi) |
| Item 5 βQ>βt ⇔ b<−1/2; scale uncertainty automatic; collapse local | i5 framework [1]–[3] |
| No FA in items 4–5 | i4 UNKNOWN/failure section; i5 UNKNOWN |
| W43 item 2 cited in item 4; W40 item 5 cited in items 4 and 5 | i4 archive table; i5 archive table |
| Item 4 VBD 0.95 / 0.998; ranking reversal | i4 derivations (ii)–(iii) |
| Item 5 model differences 0.6% / 1.3% (Vx = 0) | i5 framework [4] |
| Item 5 37–40 V, 1.2 kV | i5 abstract para |

### Matrix (archive citations only where the item already cites them)
- Row 1: W40 item 3 cited by item 1 (Change vs archive). Row 2: W43 item 1, W40 item 3 cited by items 2 and 3. Row 5: W43 item 2, W39 item 1 cited by item 4. Row 7: W40 item 5 cited by items 4 and 5; W37 item 5 cited by item 5. W38 items 1/2/4, W37 item 1, W39 item 5 are cited by items but not used in the matrix.
- Row 3 "about 0.35 eV": i3 observation (5). Row 6: i4 (ii)–(iii), i3/i4 coax.

### What changed
- "No change established" — conservative; item 1 does not raise W40 item 3 grade (i1 Change vs archive says exactly this).
- Item 5 b criterion as candidate method for WL-to-WL/TCMC: i5 NAND box (methodology only).

### Hypotheses W41-H1..H8 (all ENGINEERING_INFERENCE, grade D, none tested)
| ID | Basis |
|---|---|
| H1 | i1 DOE expected signature + falsification (1)–(5) |
| H2 | i1 geometry block (t = Tpoly/rf), failure-mode (b) layer dependence, DOE cell position factor |
| H3 | i2 DOE arm M + i3 DOE (density split, ESR, peak weights vs positions); one research line stated |
| H4 | i2 H2 (reversibility) + DOE arm C′ and M cycles |
| H5 | NEW bridging hypothesis built by me from i1 (percolation split, amplitude bimodality, channel-process control) and i2/i3 (CTL film splits). Not in any item; flagged as bridging test. Most speculative of the set. |
| H6 | i4 competing (2)/(3), DOE falsification (1)–(2), NAND box (equal field and equal voltage) |
| H7 | i5 DOE (b, T, βQ equivalence) + NAND box (methodology) |
| H8 | i4 derivation (vi) + DOE falsification (3); i5 [1] (current spread raises βQ/βt). Combination is mine. |

### QC
- Crossref match items 1, 4, 5 on 2026-10-26: manifest searched_on + resolve_evidence crossref lines (S5, S3, S4); i5_notes re-fetch 2026-10-26.
- arXiv API for items 2, 3: manifest resolve_evidence arxiv_api; "not applicable (arXiv DOIs are DataCite)" (S1).
- DOI 302 redirects 5/5: manifest resolve_evidence doi_org.
- Duplicate check wording: taken from the coordinator's instruction (published W37–W40, W43, used-source ledger, unpublished W42/W44 candidate lists). The manifest overlap_check lines cover used_sources.md and origin branches; I did not re-run the check myself.
- Independent review PENDING; "writer self-check only" = per-item notes self-checks.

### Observed-on-reading summary
- Item 1 (1)–(6): i1 observation box. Item 2 (1)–(4): i2 observation box. Item 3 (1)–(5): i3 observation box. Item 4 (1)–(4): i4 observation box. Item 5: no box; Qeff undefined + scale ratio not reproduced from i5 UNKNOWN box and framework [6].

## Inconsistencies among the five sections and the manifest
1. Manifest says item 1 (S5) was published "7 days before 2026-10-05"; 2026-09-29 → 2026-10-05 is 6 days. i1.html and the report use 6.
2. Manifest S1 fact: "N_eff <= 56"; source and i2 use ≥ 56 (i2_notes item 5).
3. Manifest S2 fact: crystalline reference "beta-Si3N4" 7.8%; paper says α-Si3N4 (i3_notes discrepancy 1; i3.html uses α).
4. Manifest S2 overlap note: "415 from the companion study"; i3 attributes the 415 to the Vitriflow population (separate Comput. Mater. Sci. paper) and cites item 2 for the method. i2 and i3 both treat them as one line; i3 states the shared-cell identity as ENGINEERING_INFERENCE (not cross-checked).
5. Manifest S4 labels "post-TDDB I-V sweeps support ..." SOURCE_REPORTED; i5 labels it AUTHOR_INTERPRETATION (i5_notes item 6). Report follows i5.
6. Manifest read ranges are superseded by the items: S1 manifest 0–52,241 vs i2 full 0–75,330; S2 manifest 0–~26,937 vs i3 0–30,000 + filtered SI; S3 manifest 0–62,122 vs i4 whole PDF. S2 manifest extraction 75,722 chars vs i3 75,875 (different pdftotext mode). S1 manifest 75,396 vs i2 75,330.
7. Manifest S3 says publication date from Crossref "article page not separately inspected"; i4 states the publisher page "Published" date matches Crossref (i4 writer checked via HTML).
8. Mobility-edge criterion: i2 N_eff ≥ 56 = N/5; i3 η = 1/4 = N/4 (70 atoms). Could be a real difference between the two papers or a section reading difference; not resolved. Report says "as written in the sections", cause not judged.
9. Depth quantities: i2 uses SI Table 2 uncorrected medians (polaron/iK/nK 3.24/3.65/3.49) and corrected Estab 1.17/1.47/1.33; i3 uses corrected depths 3.25/3.34/2.87 and relaxation ~1.4/1.5/1.2 (nK/iK/pol). Different quantities and different route ordering between the two sections.
10. Supplementary notation: i2 writes "SI Table n" / "SI Fig. n"; i3 writes "Supplementary Table n" (drops the S prefix). Both define their convention in-section.
11. Zenodo identifiers: i2 cites 10.5281/zenodo.21111822; i3 cites .8239085, .21111823, .23235037. Not necessarily inconsistent (different deposits); neither opened. Not used in report.
12. Evidence-grade style: i1 header box is an archive_gap boundary before the sourcebox and the h2 carries "[archive_gap]"; i4 opens with a new_this_week boundary; i2, i3, i5 open with the sourcebox. Item 4 is the only item with grade B. Grades otherwise C/D; all A–D only.
13. Hypothesis numbering: only i2 uses internal H1–H3; i1, i3, i4, i5 have no numbered hypotheses (DOE falsification lists instead). Report uses W41-H1..H8 to avoid collision.
14. Observation boxes: i1–i4 have "Observed on reading" boxes; i5 has none (its issues are in the UNKNOWN box and framework [6]).
15. Unit conventions: i1 SI [m]; i2/i3 eV, Å, g cm−3; i4 MV/cm, nm, ℃/°C mixed (RTA "500 ℃" vs PE-ALD "280 °C" — follows source glyphs); i5 MV/cm, cm, [C] vs [C/cm2] unresolved.
16. Coaxial symbols differ: i3 a = inner radius; i4 r_in (NAND box) and t_d/r_in in notes; i1 r0, u = t/r0, t = Tpoly/rf; i5 r0 < r1; i2 rc, rn, rg. Head's symbols paragraph maps them.
17. i5 lists Unpaywall "closed"; i5 sourcebox says "Unpaywall lists it as not open access" — same meaning.
18. Item 5 writer did not re-verify the publisher 403 (permission refusal); attributed to the verification record. Report QC says "not re-checked while writing".
19. Manifest note (not in HTML): a V-NAND HCI programming paper reserved for W44 may fall in the W41 window per OpenAlex (2026-10-08) but was not used or read here; date conflict to be resolved by the W44 owner.
20. Item 1 DOI also appears in an earlier unreviewed W41 draft branch; manifest says no fact from that branch was used. Not mentioned in HTML.

## Points for the independent reviewer
- H5 and H8 are my cross-item constructions (not in any item); check they are labelled and not overstated.
- Head's statement "for a single layer ln(1+u)/u is the reciprocal of the field ratio" is my algebra.
- Duplicate-check PASS text follows the coordinator's statement; the writer did not re-run it.
- Synthesis "0.6–1.3% (Vx = 0)" from i5 [4].
