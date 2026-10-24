# W43 report-level synth notes (writer; scratchpad only, not for publication)

Files written: report_head.html, report_tail.html, synth_notes.md (this folder only). No repo access, no push.
Inputs read: sources.yaml (all), i1..i5.html (full English text + structure), i1..i5_notes.md, ../rejected.md (context only, not cited),
W40 report_head.html / report_tail.html (format reference). Temporary English-text dumps were made in ../ during reading and deleted.

## Mechanical checks run (python -I inline, 2026-10-24 session)
- KR->EN pairing: head 42 p (21 pairs), tail 166 p (83 pairs), head+i1..i5+tail 542 p, 0 pairing errors.
- Tag balance over the concatenation head+i1..i5+tail: div 108/108, table 16/16, section 6/6, article 1/1, p 542/542, tr 138/138, td 303/303, ol/li balanced.
- Anchors: ids overview,i1..i5,synthesis,matrix,insight,hypotheses,qc,sources == TOC hrefs (same order).
- Forbidden strings in head/tail (S1..S5, W43-S, sources.yaml, model names, scratchpad, .md, .py, WebFetch): none.
- DOI links in tail: 5 distinct doi.org links.
- Grade letters in head/tail: A/B/C/D only (A appears only in the grade definition).
- CSS classes used: only ones used by W40 head/tail or by the items (boundary, inference, compare, label, qc, pass, pending, lead, source-links, download-box, btn primary, report-hero, kicker, toc, report-layout, topbar, nav, brand, spacer, wrap, footer). style.css itself NOT checked (no repo access).
- NOT done: render, PDF, independent physics review.

## Claim -> support trace

### Hero / banner / exec summary (report_head.html)
| Claim | Support |
|---|---|
| Items 1-2 abstract-only; 3-5 full text via summarizing extraction, figures not read | sources.yaml header line 3 ("WebFetch (a summarizing fetcher)"); source_access per entry; i3/i4/i5 source boxes |
| Garbled: item 3 Eq.(2)(3) layout, item 4 Eq.(1) symbols, item 5 Eqs.(1)-(8) | sources.yaml S3 source_access comment (Eq.3); i3.html "Layout of Eqs. (2)(3) lost"; S4 "Eq.1 symbols missing"; i5.html "Equations (1)–(8) are garbled" |
| Wording not guaranteed verbatim | i1_notes.md "Caveat: wording comes from a summarizing fetcher"; i3_notes.md fetcher caveat |
| Item 1 paywall not bypassed; item 2 MDPI HTTP 403, Crossref abstract | sources.yaml S1/S2 source_access comments |
| Independent review, render/PDF PENDING | per instruction; no review record exists |
| Online dates 10-19, 10-19, 10-20; 10-16, 10-15; window 10-19..25 | sources.yaml online_date per entry, header line 2 |
| Only item 1 VNAND-type CT stack; its geometry UNKNOWN | S1 why_fits ("Test-device geometry ... UNKNOWN"); i1.html UNKNOWN block |
| Item 2 statistics method on IC isolation TDDB | S2 title/facts; i2.html |
| Item 3 optical Si impact ionization; item 4 planar DG TFET TCAD; item 5 SiC 2D TCAD | S3/S4/S5 key_conditions |
| Only grade B = item 3 optical result | i3.html CONFIDENCE row "grade B"; other items' cards C/D only (grep) |
| Table row 1 (two routes, levels, calibration targets, ANO, accuracy = author claim; unknowns) | i1.html SOURCE_REPORTED / AUTHOR_INTERPRETATION / UNKNOWN paragraphs; CONFIDENCE row (C structure, D transfer) |
| Table row 2 | i2.html SOURCE_REPORTED, UNKNOWN paragraphs; CONFIDENCE row (C, D) |
| Table row 3 (R eq., reflectance, four decades incl. earlier data, 4.6 line, argument 0.1/0.35; no CI, A_c, Eq 2-3, T) | i3.html SOURCE_REPORTED, UNKNOWN, CRITICAL BOUNDARY rows |
| Table row 4 | i4.html SOURCE_REPORTED (structure, results), UNKNOWN block, CONFIDENCE (C, D) |
| Table row 5 (3.48->1.95, 10.6->14.5 us, Ron +8.6%, W_PB sweep, 1600 K) | sources.yaml S5 facts; i5.html SOURCE_REPORTED, UNKNOWN, CONFIDENCE (C, D oxide-life, D NAND) |
| Exec summary (1)-(4) | i1 eq. block (m*_fit aliasing); i2 causal-chain paragraph; i3 device-chain paragraph and H1-H4; i4/i5 NAND-relevance paragraphs |

### Synthesis (report_tail.html)
| Claim | Support |
|---|---|
| Only item 1 has geometry in injection field; i3 planar photodiode; i4 planar DG; i5 2D, authors "planar process-compatible" | i3.html H4 ("planar induced-junction photodiode"); S4 key_conditions; i5.html AUTHOR_INTERPRETATION + governing-relations note (planar-type is inference) |
| Coax ratio forms g0 / x/ln(1+x) / t/(a ln(1+t/a)) same Gauss-law result | i1.html eq block; i4.html line 4; i5.html NAND-relevance paragraph |
| R/g0 < 1; local Kane amplification g^P exp[...]; magnitude not estimated | i1.html SymPy (iii); i4.html SymPy (iv); both CONFIDENCE rows "Magnitude: not estimated" |
| No source measured a coaxial device | S1 geometry UNKNOWN; S3-S5 planar/2D |
| i3/i4 = multiplication vs generation terms; photon sets energy; bridging conditions | i3.html device chain + H1-H4; i4.html VNAND analogy chain |
| Combinable DOE (same axes) | i3.html DOE arms A / A-control; i4.html DOE geometry/T/F arms -> W43-H5 (my inference) |
| i2 mixture-with-equal-acceleration passes invariance | i2.html [6] |
| i5: off-state oxide breakdown vs SC thermal failure different populations, not one Weibull | i5.html "Failure mode and tail" (b) |
| Both i2 and i5 cite W40 item 5; their additions | i2.html archive table W40 item 5 row; i5.html archive table W40 item 5 row |
| i4 borrowed coefficients + inconsistencies; i5 arithmetic consistent; 1600 K modelling choice | S4 extrapolation_warnings; i4 observed block; i5.html (i) |
| "Do not connect" (a)-(f) | manifests key_conditions; i2 NAND-relevance (kV-class, 3800 V not to transfer); S5 warnings |

### Matrix
Archive items used only where an item cites them: W40 item 3 (i1 change-vs-archive), W40 item 5 / W38 item 3 / W39 item 1 (i2 card + table), W40 item 4 (i3 change-vs-archive), W38 item 1 + W40 items 2,3 (i4 change-vs-archive), W40 item 5 / W38 item 4 / W38 item 5 (i5 table). W37 item 1 and the W37 GIDL caution and W39 item 5 are cited by items but not used in the matrix. Each row's numbers: 38.4 -> 142.94 (S4 facts), 3.48 -> 1.95 (S5), m*_fit form (i1), prefactor share (i3 GENERAL BACKGROUND (ii)).

### What changed
"No change established" - conservative by instruction. Point 3 (optical reference, grade B) from i3 CONFIDENCE row; points 1, 4 from i1 derivation (iv) and i4/i5 DOE.

### Hypotheses W43-H1..H8 (all ENGINEERING_INFERENCE)
| ID | Source in items |
|---|---|
| H1 | i1 DOE falsification (d) |
| H2 | i1 failure mode (1) + DOE (e); ANO control from i1 controls. The "weaker in ANO" signature is my addition, consistent with i1's statement that the oxide barrier is absent only in AN. |
| H3 | i2 DOE (hold-out, equivalence margin, FA, p(V)) + competing mechanism (4) |
| H4 | i3 DOE arm D, D control, falsification (D) |
| H5 | i3 DOE arm A + falsification (A); i4 DOE Ea(F) falsification (b); geometry control from both |
| H6 | i4 DOE falsification (a), (c) |
| H7 | i5 DOE falsification (1), (2) |
| H8 | i5 NAND-relevance paragraph (T07) + falsification (3); analogy only |

### QC and sources
- Crossref match 5/5 (title, authors, online dates) lookup 2026-10-21: sources.yaml resolve_evidence each entry. I state only title/authors/dates (volume/pages not stated in resolve_evidence, so not claimed).
- doi.org redirect 5/5: resolve_evidence each entry (item 2 redirect from source-verification record, not re-checked by the item 2 writer - i2_notes line 8).
- Publisher pages: S1 abstract (paywall), S2 403, S3/S5 AIP body, S4 Frontiers body.
- Dedup: sources.yaml meta.dedup_checked_against + overlap_check per entry ("used-source ledger" = generic wording for the ledger).
- Observed-on-reading notes: i2.html [5] + UNKNOWN (four symbols); i3.html SOURCE_REPORTED/UNKNOWN (range split, reference line, argument, >250 nm condition); i4.html observed block (1)-(4) + UNKNOWN block (pocket 10 nm vs 20-30 nm); i5.html archive-gap banner (date), (iii), (iv), (i).
- Source author lists, venues, pages, licences: sources.yaml; diacritics Kilpeläinen, Kübarsepp from i3.html / Crossref note.

## Inconsistencies among the five item sections (for the editor; not fixed by me, items not modified)
1. Coaxial notation differs: i1 g0 with x = tN/r0 (two-layer), a = tA/tN, e = epsA/epsN; i4 g = x/ln(1+x), x = t/r_in; i5 t/(a ln(1+t/a)) with a = inner radius; i2 and i5 also write only Ei(r); i3 refers to "item 3 of the W40 report" for the derivation. Symbol collisions across items: a (i1 thickness ratio / i2 BGW shape / i5 radius), x (i1 tN/r0 / i3 hν−2Eg / i4 t/r_in and lateral position in nm), g (i1/i4 field ratio / i3 impact-ionization contribution), B (i1 FN / i4 BTBT / i2 beta function), γ (i2 BGW shape / i5 TDDB "γ" in tail discussion). Report-level text keeps symbols item-local; a one-line "symbols are local to each item" note could be added by the editor.
2. Units: i1 SI (V/m, C/m, m); i4 and i5 practical cgs (V/cm, cm, cm^-3); i3 eV. Not wrong, but mixed.
3. Causal-chain heading labels differ: i1/i2/i4 "(ENGINEERING_INFERENCE)", i3 no tag in heading (labels inside), i5 "(AUTHOR_INTERPRETATION, links marked ? are hypotheses)".
4. Archive comparison format: i2 and i5 have a separate "What changes vs previous archive" table; i1, i3, i4 have it only as a card row.
5. Selection label case: i4 source box "Selection: archive_gap" vs i5 "Selection: ARCHIVE_GAP"; i1-i3 "new_this_week".
6. Hypothesis numbering: only i3 uses internal H1-H4; i1 uses (a)-(e), i4 (a)-(d), i5 (1)-(3) for falsification. Report-level uses W43-H1..H8 (stated in the HTML).
7. Grades: i3 is the only B (in-domain, full text). i2 deliberately gives no letter grade to its sympy framework checks (i2_notes line 40), while i1, i3, i4 give C to their derivations. Minor asymmetry; acceptable but noted.
8. i5 rounds the Isc change as both "−13.8%" and "about 14%" in the same item; consistent but two forms.
9. Dedup statement: i4 banner says DOI absent from published W37-W40 archive text; i5_notes says W41/W42 dedup not done by the item writer; manifest says W41/W42 branches were checked. Report QC follows the manifest (source verification).
10. Manifest vs items: S3 why_fits/warnings call the photodiode "field-free"; i3 deliberately avoids that (field not discussed in the paper). Report-level text follows i3 ("photon sets the energy") and never says field-free. S3 fact "data support m_c = 4.6" is weaker in i3 ("agree with the 4.6 reference line", no fitted CI); report follows i3. S1 fact 3 level assignment -> i1 UNKNOWN; report follows i1.
11. Dates in item source boxes: i1 and i3-i5 give received/accepted dates; i2 gives only online date (not available). Fine.
12. i3 card table lists data range as "250–410 nm" this work + "360–476 nm" earlier; manifest S3 fact 1 says 250–476 nm. Report follows i3.

## Points the reviewer should check
- Matrix row "Earlier work almost exclusively used 3.5" relies on i3's wording "used almost exclusively in earlier work".
- W43-H2 "weaker in ANO" signature and H5's combination of i3/i4 DOEs are my composition.
- QC "PASS" for KR->EN pairing is a mechanical paragraph-order check, not a translation-equivalence check.
