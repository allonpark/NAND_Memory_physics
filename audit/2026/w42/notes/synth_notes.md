# W42 report-level notes (report_head.html, report_tail.html)

Status: DRAFT in the work folder only. No commit, no push, no PR. Items i1–i5 were not edited.
Inputs read: i1.html (whole), i2–i5.html (whole; English paragraphs, tables and labels via a text
extraction; Korean paragraphs spot-read), i1–i5_notes.md, sources.yaml, published W43 index.html
(head and tail blocks) from the repo clone, W41 report_head.html (format only), assets/style.css class list.
Manifest-to-item mapping: W42-S4 = item 1, W42-S5 = item 2, W42-S3 = item 3, W42-S1 = item 4, W42-S2 = item 5.

## Mechanical checks run (scratchpad script, venv python -I)
- Assembled head + i1..i5 + tail: 365 `lang="ko"` paragraphs, 365 `lang="en"` paragraphs, 0 pairing failures,
  no Hangul inside an English paragraph.
- HTML tag balance: 0 errors, nothing unclosed. All TOC anchors (#overview, #i1..#i5, #synthesis, #matrix,
  #insight, #hypotheses, #qc, #sources) resolve.
- Banned-string scan of head/tail: no "writer", no W42-S#, no sources.yaml/manifest, no model names, no file
  paths, no non-scale grades. Only hits for `S1–S4`, `S2–S3`, `S3` are the paper's Supporting-Information
  table names in item 4 (legitimate).
- Links: doi.org for all five; arXiv abs links for items 2, 4, 5. Relative paths ../../../assets/style.css and
  ../../../downloads/2026/VNAND_HV_Reliability_2026-W42.pdf. No class outside style.css used.
- Not done: rendering, PDF build, visual check, independent physics review.

## Claim ledger (head)
| Claim in head/tail | Support |
|---|---|
| Full text 4/5 (items 1,2,4,5); item 3 abstract only | i1 sourcebox; i2 sourcebox; i4 sourcebox; i5 sourcebox; i3 sourcebox; manifest source_access |
| Item 1 read from two editions (advance PDF, copyedited PDF) | i1 sourcebox; i1_notes Reads |
| Items 2,4,5 second read of re-downloaded PDF by different method; item 2 second read targeted string search | i2 sourcebox "(2) ... targeted cross-check"; i4 sourcebox (pypdf); i5 sourcebox |
| Figures not read; garbled eqs UNKNOWN: item 2 Fig.3 eqs, item 4 Eqs (1),(2),(S24)-(S36) | i2 UNKNOWN box; i4 sourcebox/UNKNOWN |
| Item 1 Eq.(1) sign from font mapping in one edition + common text | i1 "Limits of reading the equations" |
| Item 3 publisher HTTP 403 not bypassed | i3 sourcebox; manifest S3 access_basis |
| Independent review PENDING | brief; no review evidence exists |
| Item 3 online 2026-10-15; items 4/5 submitted 2026-10-14 / 10-12; announcement unconfirmed | i3 sourcebox; i4 boundary; i5 boundary; manifest S1/S2/S3 |
| Item 1 online 2026-08-25, Crossref issued 2026-09-25 | i1 archive_gap box; manifest S4 |
| Item 2 arXiv v1 2025-12-17; no journal version as of 2026-10-26 | i2 archive_gap box |
| Item 1 geometry UNKNOWN; CT vs FG not stated | i1 "Geometry: UNKNOWN" |
| Item 2 no new data (data-availability statement) | i2 SOURCE_REPORTED (13); manifest S5 F1 |
| Item 3 only in-window 3D NAND item | manifest window_finding_directness; i3 |
| Item 5 AOS not poly-Si; item 4 planar HZO | i5 boundary; i4 boundary |
| Grade B only in item 1 (measured linearity/compensation; SSD latency as simulator) | i1 claim card CONFIDENCE |
| Symbols: β item 4 exponent 1.7 / Weibull in item 2 DOE | i4 governing relations; i2 DOE |
| τ in items 3, 4, 5 | i3 [1]; i4 variables; i5 variables |
| σ in items 1, 2, 3; C in items 1, 3; L in items 1, 5; D in item 4 (duty, diffusion) | i1 eq vars, D4; i2 vars; i3 vars, D6 population; i5 D5; i4 (i), S10 |
| Coaxial quantities: item 1 ln(1+u)/u, u=t/r0; item 2 ln(1+u)/u, u=t/r_c; item 5 u/ln(1+u), u=t_ox/r0; item 4 E(r)=V/[r ln(rout/rin)]; item 3 G(x), x=t_T/r0 | i1 D2; i2 (ii); i5 coaxial eq; i4 NAND box; i3 governing relations |
| "single-layer reciprocals; different reference radius; magnitudes not estimated" | own algebra (u/ln(1+u) = 1/[ln(1+u)/u]); i1/i2/i3/i5 state no geometry used |
| Unit systems per item | read from each item's variable lists |
| Overview table rows | item 1: i1 SOURCE_REPORTED (2),(3),(5),(7),(8) + UNKNOWN box + CONFIDENCE; item 2: i2 SOURCE_REPORTED (2),(3),(5),(6),(12),(13) + CONFIDENCE; item 3: i3 SOURCE_REPORTED + UNKNOWN + CONFIDENCE; item 4: i4 SOURCE_REPORTED + UNKNOWN + CONFIDENCE; item 5: i5 SOURCE_REPORTED + UNKNOWN + CONFIDENCE |
| Lead (1)-(4) | i1 obs (7) and "not a mechanism test" heading; i2 heading + checklist; i3 UNKNOWN; i4 (iii) sign test; i5 B4 |

## Claim ledger (tail)
| Claim | Support |
|---|---|
| Geometry item by item | i1 geometry box; i2 UNKNOWN/geometry box ("every MW model is 1D"); i3 UNKNOWN box ("Device geometry ... not in the abstract"); i4 boundary; i5 material/geometry boundary |
| Checklist C1–C11 recast by this report; falsification criteria set by this report | i2 checklist footnote |
| Items 1/3 test no checklist entry; C10 nearest; C10 needs T-dependent current, SS, thickness/crystallization splits | i2 C10 row; i1 UNKNOWN box (no I–V) and AUTHOR_INTERPRETATION (i) |
| T_co(C) growth relates to C4; C4 measurement set | i1 SOURCE_REPORTED (5); i2 C4 row |
| Item 1 bake suppresses retention → not C7 | i1 SOURCE_REPORTED (2); i2 C7 |
| Item 3 retention conditions UNKNOWN | i3 UNKNOWN box |
| C1, C2 not measured this week | own reading of all five items |
| Item 1 ↔ 3: different chips, manufacturer/generation UNKNOWN; framework [4] | i1 UNKNOWN; i3 UNKNOWN; i3 [4] |
| Item 4 ↔ item 1: delay changes loss at equal N; direction opposite to rest=recovery; item 1 read order/dwell not described; item 1 arms A, B | i4 SOURCE_REPORTED, (iii); i1 UNKNOWN box, DOE arms A/B |
| τ0 not a stack constant; T_co lumps contributions | i4 (v); i1 "lumps (a)+(b)+(c)", competing table M1–M7 |
| Item 5 bridging B1–B6 | i5 bridging box |
| Item 1 GB attribution as natural target | i1 AUTHOR_INTERPRETATION (i) (ENGINEERING_INFERENCE link, stated as not measured) |
| "Where they do not connect" (a)-(f) | own reading; i2 "originals not read"; i2 VNAND box; i4 NAND box; i5 NAND box; no item has FA/Weibull data (i2 "no distributions", i5 "no stress data", i1 none, i4 one capacitor) |
| Matrix row 1 | i1 obs (7), D1, DOE A0 |
| Matrix row 2 | i4 SOURCE_REPORTED, (iii), archive table W40 item 5 row |
| Matrix row 3 | i4 (v) (2.10x, 1.60x; 0.08997/0.03880 eV), archive table W43 item 2 row; i1 model lumping |
| Matrix row 4 | i3 observation (ii), [2], UNKNOWN; i1 SOURCE_REPORTED (5); i3 change-vs-archive W38 item 2 |
| Matrix row 5 | i2 (i), (ii), archive table rows W43 item 1 / W40 item 3; i1 D2; i5 coaxial eq |
| Matrix row 6 | i5 SOURCE_REPORTED, B4; i1 AUTHOR_INTERPRETATION (i); i1 and i5 change-vs-archive W40 item 3 |
| Matrix row 7 | i2 (iv), archive table W40 item 5 / W43 item 2 row |
| Archive items used only where an item cites them | W37 i1 (i1, i2, i3), W38 i1 (i3), W38 i2 (i1, i2, i3), W38 i4 (i4), W39 i2 (i4), W39 i4 (i2, i5), W39 i5 (i3), W40 i1 (i3), W40 i3 (i1, i2, i5), W40 i5 (i2, i4), W43 i1 (i2, i3), W43 i2 (i2, i4), W43 i4 (i5). Matrix uses W38 i2, W40 i3, W40 i5, W43 i1, W43 i2 only. |
| What changed 1: no prior cross-temperature item in W37–W40, W43 | i1 change-vs-archive |
| What changed 2–5 | i4 NAND box; i2 change-vs-archive ("does not raise that inference's grade"); i3 framework + CONFIDENCE; i5 NAND box |
| Hypotheses H1–H6 provenance | H1: i1 DOE A0 + falsification (A0); H2: i1 DOE A + falsification (A); H3: i3 DOE falsification (b)-(d) + [5]; H4: i2 DOE priority arm falsification (1)-(4); H5: i4 DOE (2) and (4); H6: i5 F1 and F4 |
| H7 cross-construction | i1 SOURCE_REPORTED (5) T_co(L) + i3 framework [4]; own combination; grade D |
| H8 cross-construction | i4 (iii) sign test + i4 NAND box ("whether stored charge ... self-field ... is a hypothesis") + i3 D5/G(x) retention self-field; stored-state split is my analogue of i4 DOE factor "polarization state before the delay"; grade D |
| QC: Crossref 2026-10-26; item 3 re-check 2026-10-28; item 1 dates vs J-STAGE page + PDF cover | manifest resolve_evidence; i3_notes §1; i1_notes Read 2 |
| QC: arXiv API + DataCite for items 2,4,5 | manifest resolve_evidence S1, S2, S5 |
| QC: doi.org 5/5 redirects (2026-10-26) | manifest resolve_evidence |
| QC: arXiv HTML 404 items 4, 5 | i4 sourcebox; i5 sourcebox / notes |
| QC: tools pdftotext layout/non-layout, pypdf (item 4) | i1_notes, i2_notes, i4_notes, i5_notes |
| QC: derivations SymPy items 1,2,4; stdlib items 3,5 | i1 arithmetic paragraph; i2 box label; i4 box label; i3 "numerically checked"; i5 box label "Python standard library" (see inconsistency 1) |
| QC: duplicate check scope | brief; manifest overlap_check |
| Observed-on-reading summary | i1 inference box (1)-(7); i2 inference box (1)-(5); i4 inference box (1)-(6); i5 inference box (1)-(5) |
| Sources list | manifest authors/titles/venues/DOIs; i1–i5 sourceboxes for access level and licence |

No number, DOI, author or finding was added that is not in an item section or the manifest. Report-level
derived statement: only the single-layer reciprocal relation between u/ln(1+u) and ln(1+u)/u (identity).

## Inconsistencies found among the five sections and against the manifest
1. **Item 5 HTML vs its notes (tooling label).** i5.html labels its derivations "Python standard library; the
   pinned SymPy environment was unavailable for this item", while i5_notes.md says the derivations were
   re-run in SymPy (i5_sympy.py exists) and that "HTML now labels derivations 'SymPy-checked'". The HTML is
   apparently an earlier version (reconstruction artefact). The QC grid follows the HTML text. Caller should
   decide which label is correct and fix i5.html.
2. **Item 3 tooling.** i3 says "analytic derivation, numerically checked" (stdlib); notes say the venv was
   missing at that time. Items 1, 2, 4 used SymPy. Derivation tooling therefore differs by item; stated as such in QC.
3. **Grades in the manifest use non-scale values.** Manifest S1 (item 4) "B-", S4 (item 1) "B-", S3 (item 3)
   "D for any physics use; A-/B for the existence of the claim". Items use only A–D: item 1 B (measured), item 4
   C (trends), item 3 C (reported result). Report follows the items. Item 4 is therefore one grade lower than the
   manifest suggested (C vs "B-"), item 1 one notch higher (B vs "B-").
4. **Item 1 grade B for SSDsim latencies "as simulator results".** Grade B is defined as literature + same-domain
   calculation; a simulator output mapped from device RBER via a lookup table being B is debatable. Kept as the
   item states, but flagged for the physics review.
5. **Label collision C1/C2.** Item 1 uses "C1, C2" for arithmetic checks; item 2 uses "C1–C11" for its checklist.
   The tail refers only to item 2's checklist and says so each time. Similarly D1–D4 (item 1), D1–D7 (item 5),
   [1]–[5] (item 3), (i)–(v) (item 4), (i)–(iv) (item 2) are per-item derivation labels; F1–F6 in item 5 are
   falsification criteria while the manifest uses F1–F7 for facts.
6. **No hypothesis numbering inside items.** None of i1–i5 uses H-numbers, so W42-H1..H8 do not collide.
7. **Title case.** i1 sourcebox gives the title in sentence case ("Model-based read-reference-voltage
   compensation ..."); manifest/Crossref use title case. Sources list uses the manifest form.
8. **Section-heading tags.** Items 1 and 2 headings carry "[archive_gap]"; items 3–5 headings carry no class tag;
   item 3 has no selection boundary box (new_this_week is stated only in its sourcebox), while items 4 and 5 have
   a "new_this_week · preprint" boundary box. Style only.
9. **Item 4 heading is interpretive.** "the delay acts as stress, not rest" is the item's own sign-test inference
   (derivation (iii), which itself says coexisting recovery is not excluded); a reader may take it as a source
   claim. Suggest softening or labelling in the heading.
10. **Reference-title inference inside items.** Item 1 "New vs known" lists prior topics "by title" from its
    reference list; item 2 observation (4) maps citations by title (with the caveat that titles cannot confirm).
    The report head/tail does not add any title-based inference; the tail summary of item 2 (4) keeps the caveat.
11. **Item 3 wording vs abstract.** i3.html says read-retry needs "several read iterations"; i3_notes say the
    abstract says "multiple" (the manifest F1 also says "several"). Wording only.
12. **Degree sign glyph.** Item 5 uses "℃" (U+2103) for anneal temperatures; the other items use "°C". Style only.
13. **"sympy" vs "SymPy".** Item 4 writes "sympy", items 1, 2 "SymPy". Style only.
14. **Read-range numbers.** Manifest S5 (item 2) read range "chars 0-92062" vs item 2 "0–91,986"; manifest S2
    (item 5) "0-23584" vs cached file 23,791 bytes (encoding, noted by item 5). Not content gaps.
15. **Manifest fact wording (item 5).** Manifest S2 F6 "time constant near 250 ns (about 3x the depletion value)"
    can be misread as τ being 3x; the source's ~3x refers to density (noted in i5_notes). The report uses the
    item's wording.
16. **Manifest inference presented as fact (item 3).** Manifest S3 `why_it_fits` ("WL-dependent optimum read
    voltage is a signature of layer/process dependence in VNAND") is not abstract content (noted in i3_notes).
    Not used in the report.
17. **Item 3 access date.** The 403 is from the 2026-10-26 verification step; the publisher page was not
    re-accessed when the item was written (i3 says so). QC states the 2026-10-26 result.
18. **Units.** Item 1 T_co value and unit UNKNOWN (dimensionally V/K); item 4 τ0 tabulated in ns though defined
    dimensionless (source issue, already in item 4). Consistent across report; no unit conversion was made.
19. **Overlap records.** Manifest lists items 3 and 4 in a W43 reserve list (never used) and item 1 as an
    unverified hint on an unreviewed W42 branch. The QC duplicate statement is limited to the published reports
    (W37–W40, W43) and the used-source ledger, as instructed; those reserve/branch mentions are not "use".

## Open for the caller
- Resolve inconsistency 1 (item 5 tooling label) before publication; QC wording "numeric checks ... items 3 and 5"
  must be updated if i5.html is switched to the SymPy label.
- Independent physics review is PENDING for all five items and for the report-level hypotheses H1–H8.
