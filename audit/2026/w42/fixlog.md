# W42 fix pass log (fixlog.md)

Scope: sections\ only (i1..i5.html, report_head.html, report_tail.html). No push, no PR, no network access in this pass.
Input: review\review.md (read in full) and review\derive_out.txt, mech_out.txt. Every finding was checked against the CURRENT text before patching.

## How the edits were made

- Backup: `sections\_orig\*.html` (copied before any change; untouched since).
- The section files have multi-kilobyte single lines and many ko/en twins, so the edits were applied in place by a deterministic patch script instead of one-by-one Edit calls:
  `_fix\patches.py` (85 exact-string patches; each asserts the exact match count) and `_fix\apply.py` (35 regex passes with expected counts for label renames and supplementary references; rebuilds sections\*.html from `_orig` every run, so the result is reproducible).
- Every applied change (finding id, file, old -> new excerpt) is logged in `_fix\changes.log`.
- Run: `venv_sympy\Scripts\python.exe -I sections\_fix\apply.py`.

## Finding status

| ID | Status | Where (ko+en unless noted) | What was done |
|---|---|---|---|
| B-1 (blocker) | applied | i4 obs (4); tail "Source inconsistencies" Item 4 (4) — 4 places | "two decades below the lower bound" -> "about one decade (a factor of about 13) below the lower bound 1e-5 m/s; about two decades below the upper bound 1e-4 m/s". Added the review's sentence: D range spans two decades but the stated velocity range one decade, matching D ≈ 1.3e-11 to 1.3e-10 cm²/s. Re-derived with SymPy: `_fix\b1\b1_drift_sympy.py` -> `_fix\b1\b1_drift_sympy_out.txt` (v = 7.73634e-7 m/s; ratio 12.926 = 1.111 decades; vs upper bound 129.26 = 2.111 decades; D for 1e-5/1e-4 m/s = 1.293e-11/1.293e-10 cm²/s; 2 ms travel 20–200 nm). Source range (D 1e-10..1e-12 cm²/s, v 1e-5..1e-4 m/s) re-read in both extractions (layout and raw) of the review's downloaded PDF. |
| M2-2 (blocker per coordinator) | applied | i2 obs (2) | en "the type the authors rate most promising" -> "the type this section discusses"; ko "저자들이 가장 유망하다고 꼽은" -> "이 절이 다루는". Source check (raw extraction): the section says "we focus on the gate-side injection" type; no "most promising" rating. |
| M4-2 (blocker per coordinator) | applied | i4 card "Change vs archive"; i4 compare table (W40 item 5 row: "Item 4 adds" and "Updated position"); tail matrix row 2 (evidence and tension cells) | "opposite sign" removed. New wording: reported direction is the same (lower rate/frequency worse in both); what is opposite is the authors' proposed role of de-trapping (gain in SiC, loss in HZO); comparison bases differ (equal N vs wall-clock/stress time UNKNOWN in W40 item 5), so a sign comparison does not hold. Conclusion (the word de-trapping does not fix a mechanism) kept. W40 item 5 time accounting UNKNOWN confirmed in the published W40 text. |
| M1-1 / M-H-1 | applied | i1 card CONFIDENCE and EVIDENCE, i1 source-box grade sentence; head "Labels and grades" | SSDsim latency figures now grade C (source-reported simulator output via lookup table, not reproduced). Head: "and to the SSD latency figures as simulator results" removed; added "Item 1's SSD latency figures are simulator results (not drive measurements) and are grade C". |
| M1-2 | applied | i1 "New vs known" | Known list rebuilt only from what the introduction attributes to cited work ([7]–[10] channel-current temperature dependence and Vth shift; [12]–[16] on-chip compensation; [6], [17]–[20] algorithm-level read-voltage adjustment). Title-only topics deleted. Checked in raw and layout extractions. |
| M2-3 | applied | i2 obs (4) removed and (5) renumbered (4); i2 card CONTRADICTING DATA phrase removed; tail Item 2 (4) removed, (5) -> (4) | No contradiction is claimed from reference titles anywhere. The source-box statement that reference-list titles were read (reading procedure) is kept. |
| M2-1 | applied | i2 card CLAIM | Causal clause "because of high-field FN operation" moved from the cited statement to AUTHOR_INTERPRETATION ("the physical bottleneck is high-field FN operation"), matching AUTHOR_INTERPRETATION (a). Also fixes m2-7 and the second non-polite ending "심화시킨다" -> "심화시킵니다". |
| M4-1 | applied | i4 h2; i4 (iii) ko/en; i4 NAND-relevance box ("counter-example" sentence) | Title: "in this stack the delay acts as net stress rather than net recovery (this report's sign-test inference; recovery may coexist)". (iii) now states it as this report's inference. |
| M5-1 / M-T-1 | applied | i5 inference-box label; tail QC "Derivations" | `i5_sympy.py` re-run with the pinned venv -> `sections\i5_sympy_out.txt` (exit 0; identical to the review's rerun). Values match the HTML: 1/(2πτ)=636620 Hz (HTML 6.37e5), ωτ 1.5708 / 1.5708e-3 (1.57, 1.57e-3), single-level peak x=1 height 1/2 (0.5), continuum x*=1.980291 height 0.4023712 (1.98, 0.402), f_peak 1.26069e6 Hz (1.26 MHz), 4.5e11–4.5e12 (same), 2.333–3.444 (2.33–3.44), RC peak x=2.54065 (2.54), small-x x/3, f(2L)/f(L)=1/4, u/ln(1+u)≈1+u/2, t_ch(1−v/2), 3/d. Label now "SymPy 1.14.0 with mpmath 1.3.0; script re-run, values agree"; tail QC: SymPy for items 1, 2, 4, 5, standard library for item 3. |
| M-T-2 | applied | tail H3 hypothesis cell | "(ii-b)" no longer attached to the opposite proposition: "not constant in data age (the negation of (ii-b))"; the refutation ("since (ii-b) then holds") now reads consistently with item 3's definition. |
| M-T-3 | not applied (coordinator decision) | tail QC "Duplicate check" | No branch name or draft is mentioned in public HTML. The statement already reads "published reports (W37–W40 and W43) and the used-source ledger ... scope limited to those two"; left unchanged. Open issue for the coordinator: the review reports an unpublished W42 draft on another remote branch that covers item 1's paper and the same publish path; this pass did not touch it. |
| m1-3 | applied | i1 obs (10) | "no data are shown" -> "no data are given in the text or captions (figures not read)". |
| m1-4 | applied | i1 arithmetic-check paragraph | Reference to working notes deleted. |
| m1-5 | applied (prefix differs from coordinator example) | i1, tail, head | C1/C2 -> N1/N2 (not A1/A2: item 1's DOE arms are A0 and A–E, so A1/A2 would collide inside item 1). D1–D4 -> J1–J4 (E1–E4 would collide with DOE arm E; D collides with grade D and item 5). Tail references "Item 1 derivation D1", "Item 1 D2" updated. |
| m1-6 | applied | i1 h2 | "the authors' linear-in-ΔT engineering model ... (ΔT-only dependence not shown)". |
| m2-4 | applied | i2 derivation (i) | Faces defined the same way for GAA and CAA: field at the IL-side stack boundary over field at the GBL-side stack boundary (GAA: IL side r_a, GBL side r_b; CAA reverse). SymPy check `_fix\b1\m24_faces_sympy.py` -> `_out.txt` (GAA εGBL·rb/(εIL·ra), CAA εGBL·ra/(εIL·rb), product of geometric factors 1). |
| m2-5 | applied | i2 derivation (i) last sentence | "a curvature contribution to why ... (layer thickness and permittivity ratios also contribute)". |
| m2-6 | partially applied | i2 AUTHOR_INTERPRETATION (g) | Kept under AUTHOR_INTERPRETATION (conservative) and annotated that the source cites [90] and [80] in that passage (confirmed in layout and raw extractions). Not moved to SOURCE_REPORTED. |
| m2-7 | applied | i2 card CLAIM | "경로이다." -> "경로입니다." (with M2-1). |
| m3-1 | applied | i3 SOURCE_REPORTED (en) | "several ... are needed" -> "multiple ... are required" (abstract wording). |
| m3-2 | applied | i3 (ii-a)/(ii-b) definition sentence | Polite ending; definition text unchanged in meaning. |
| m3-3 | no change needed | — | Review records that item 3's stdlib checks were reproduced with SymPy. |
| m4-3 | applied | i4 (iv); i4 obs (2) | "P ∝ [1 − a² ln² X] (the factor 1/2 absorbed into P0)"; "numeric probe in the notes" -> "this report's numerical probe"; all "sympy" -> "SymPy". |
| m4-4 | applied | i4 competing mechanism (3) | Added that the introduction presents domain-wall pinning by defects generated in cycling and redistributed during the delay as the explanation of [23]–[25], [27], and that the authors chose nucleation inhibition rather than pinning (both sentences confirmed in layout and raw extractions). |
| m4-5 | applied | i4 NAND-relevance box; tail matrix row 2 "Prior simplification" | Background statement marked ENGINEERING_INFERENCE with an unverified basis; prior simplification attributed to the authors' interpretation in W40 item 5. |
| m5-2 | applied | i5 DOE and controls | Test structures S1–S4 -> Structure 1–4 (ko 구조 1–4). Also required by the linter (S[1-9] = internal-id pattern). |
| m5-3 | applied | i5 refutation criterion R1 | f_peak ∝ 1/(R_sh·C_ox·L²) with symbols defined at the use (derivation K5). |
| m5-4 | applied | i5, tail | Derivations D1–D5 -> K1–K5; bridging steps B1–B6 -> BR1–BR6 (tail references updated). |
| coordinator (4) F labels | applied | i5, tail | F1–F6 -> R1–R6 (tail "H6 from DOE criteria R1 and R4"). |
| coordinator (4) item 3 box | applied | i3 | Added the selection-classification boundary box ("new_this_week · journal article (Eng, MDPI) · abstract only") with ko/en paragraphs; only dates and facts already in item 3 (2026-10-15, window, CC BY 4.0, HTTP 403, abstract only, geometry not described). |
| coordinator (4) observation-box title | applied | tail | Tail box label aligned to the item label "Observed on reading, not confirmed by the authors (not a source claim)" + "summary of items 1, 2, 4, 5". Item 3 has no observation box (abstract only). |
| coordinator (4) inference labels / SymPy spelling | applied | i3, i4, all files | "Engineering inference ·" -> "ENGINEERING_INFERENCE —" (i3, i4); all 22 "sympy" -> "SymPy". |
| coordinator (4) label namespaces (review 5.4) | applied | head "Symbols and units" | One ko/en sentence listing the per-item label prefixes and that they are unrelated to grades A–D. |
| m-H-2 / coordinator (6) | applied | head banner; tail QC (independent review, numbers, labels, derivations) | "independent physics review PERFORMED; first pass PASS-WITH-FIXES for items 1, 2, 3, 5 and FAIL for item 4 (one numerical-magnitude error and wording that misstated a sign comparison, now corrected); fixes applied; re-check PENDING". Nothing re-verified is called PASS. |
| m-H-3 | applied | head banner label; tail QC "Issue grade" | "single-source" -> "full-text analysis, one source per item". |
| m-T-4 | applied | tail sources [1] ko/en | Sentence-case title as in Crossref and the J-STAGE page (both checked in the review's downloads). |
| m-T-5 | applied | tail H8 | Added the reason for the predicted positive sign in the programmed state (assumption) and a radius refutation criterion via item 3's G(x) (defined at the use). |
| m-T-6 | not applied | i3–i5 h2 | The published W43 report tags only archive_gap items in h2; the current W42 headings follow that convention. |
| U-1 (review 7, arXiv API) | applied | tail QC "Bibliographic match"; tail sources intro ko/en | Added that in the physics review the arXiv API was rate-limited and the match was re-confirmed from arXiv abstract pages and DataCite. |
| L-1 (linter) | applied | i4, head, tail, i2, i5 | The _orig assembly FAILS leak-check (111 source-id hits: "Table S1–S3", "Fig. S2", "Eq. S10", "S4 derivation", structure labels "(S1)", subscripts "V_S1"). Converted to "Supplementary Table n / Supplementary Fig. n / Supplementary Eq. (n) / Supporting Information Section n" (ko: "Supplementary Table n", "보충 그림 n", "보충 식 (n)", "Supporting Information n절"); i2 V_S1/V_S2 -> V_PS1/V_PS2. |
| X-notes | applied | i4 (iv); tail synthesis | Verb "notes" removed (coordinator: no "notes" in public HTML): "states", "points out". |

## Self-checks

Scripts: `_fix\selfcheck.py` (output `_fix\selfcheck_out.txt`), the review's `mech_checks.py` and `card_check.py` re-run on the fixed files (`_fix\mech_out_after.txt`, `_fix\card_out_after.txt`), the review's `derive_checks.py` re-run (`_fix\derive_rerun_out.txt`, identical to review\derive_out.txt).

- Tag balance on the assembled head+i1..i5+tail: 0 unclosed, 0 mismatches: PASS
- Classes not in assets\style.css: none: PASS
- ko->en adjacency (head+i1..i5+tail): ko 366 / en 366, 0 violations, 0 orphan en: PASS (also linter kr-en-adjacency PASS)
- Card cells: 13/13 rows, 13/13 cells with ko and en, items 1–5: PASS
- Anchors: 0 unresolved, 0 duplicate ids: PASS
- Forbidden strings (model names, S#/W42-S#, sources.yaml, file paths, writer, notes, branch name, per-item .qc, lowercase sympy, old labels, non-scale grades, "two decades below the stated lower", "of opposite sign", "most promising"): 0 each. One remaining hit of the title-mismatch pattern is the i2 source box describing the reading procedure ("참고문헌 목록의 해당 항목(제목 수준)을 읽었습니다"), not a claim; kept.
- Non-polite Korean endings: 0 in every file. ko/en numeric-token mismatches: none new (diff vs review\mech_out.txt shows only label renames; one pre-existing i1 mismatch disappeared with the M1-2 rewrite).
- Linter (repo clone, `python -I scripts\report_lint.py all --root sections\_assembled --offline`, plus leak-check and policy --week 2026-W42): doi-format PASS, doi-duplicate PASS, kr-en-adjacency PASS, vocabulary PASS, leak-check PASS; abstract-only-guard and derivations NA (no claims ledger / audit folder in the assembled root). The same leak-check on the _orig assembly: FAIL, 111 hits.

## Not verified in this pass

- No new network reads. Source confirmations used the review's downloaded copies (J-STAGE copyedit PDF and arXiv PDFs, layout and raw pdftotext extractions = two reads) and Crossref JSON.
- A re-check by an independent reviewer is PENDING; nothing here should be read as PASS of the corrected text.

## Appendix A. Linter output (final assembly)
```
CHECK                WEEK      RESULT    DETAIL
doi-format           2026-W42  PASS      5 distinct DOI(s) well-formed
doi-duplicate        2026-W42  PASS      no DOI shared with another week
kr-en-adjacency      2026-W42  PASS      ko=366 en=366 ko_without_following_en=0 en_without_preceding_ko=0
vocabulary           2026-W42  PASS      349 label/grade token(s), all within vocabulary
leak-check           2026-W42  PASS      no internal references found
abstract-only-guard  2026-W42  NA        no claims ledger for this week
derivations          2026-W42  NA        no audit scripts folder

SUMMARY: PASS=5, NA=2
[all exit 0]
CHECK       WEEK      RESULT    DETAIL
leak-check  2026-W42  PASS      no internal references found

SUMMARY: PASS=1
[leak-check exit 0]
CHECK                WEEK      RESULT    DETAIL
doi-format           2026-W42  PASS      5 distinct DOI(s) well-formed
doi-duplicate        2026-W42  PASS      no DOI shared with another week
kr-en-adjacency      2026-W42  PASS      ko=366 en=366 ko_without_following_en=0 en_without_preceding_ko=0
vocabulary           2026-W42  PASS      349 label/grade token(s), all within vocabulary
leak-check           2026-W42  PASS      no internal references found
abstract-only-guard  2026-W42  NA        no claims ledger for this week
derivations          2026-W42  NA        no audit scripts folder

SUMMARY: PASS=5, NA=2
[policy exit 0]
```

## Appendix B. Linter leak-check on the _orig assembly
```
CHECK       WEEK      RESULT    DETAIL
leak-check  2026-W42  FAIL      111 hit(s): source-id x111 (e.g. 'S1' line 250)

SUMMARY: FAIL=1
```

## Appendix C. selfcheck.py output (incl. ASCII-token multiset diff vs _orig)

Token-diff attribution: label renames N1/N2, J1-J4 (m1-5), K1-K5, BR1-BR6 (m5-4), R1-R6 (coordinator F), Structure 1-4 (m5-2); Supplementary/Supporting/Information/Section(s)/Tables and removed S1..S36 tokens (L-1); PS1/PS2 vs S1/S2 (L-1, i2); SymPy vs sympy (X-sympy, m4-3); 13, 1.3, 11/12, two/decade(s)/upper/bound/velocities (B-1); SiC/HZO/W40/rate/worse/bases/de-trapping/direction (M4-2); stress/net/inference/sign-test/coexist (M4-1); 7,10,12,16,6,17,20, introduction, on-chip, lookup (M1-2); SSDsim/simulator/grade C/lookup/output (M1-1, M-H-1); removed 67,68,79,39,110,87, FeFET, title-level, Citation mapping (M2-3); 80, cites, passage (m2-6); boundary/side/stack/reverse (m2-4); curvature/contribution/thickness/permittivity (m2-5); bottleneck/physical/interpretation (M2-1); i3 box tokens (coordinator box); PERFORMED/PASS-WITH-FIXES/FAIL/re-check/corrected (m-H-2); one source per item (m-H-3); rate-limited/DataCite/pages (U-1); Model-based etc. case (m-T-4); G/radius/programmed/self-field (m-T-5); negation (M-T-2); Prior simplification attribution (m4-5); pinning/oxygen/vacancies/introduction (m4-4); mpmath 1.3.0, re-run, agree (M5-1); R_sh/C_ox/sheet/resistance (m5-3); multiple/required (m3-1); notes removal (m1-4, m4-3, X-notes).
```
== 1. tag balance (assembled head+i1..i5+tail)
   unclosed: []  mismatches: []  -> PASS
== 2. classes not in assets/style.css: none -> PASS
== 3. ko->en adjacency (all <p lang>)
   ko=366 en=366 ko_without_en=0 orphan_en=0 -> PASS
== 4. card cells paired (13 rows per item, each value cell has ko and en)
   i1: rows 13/13, paired 13/13 PASS
   i2: rows 13/13, paired 13/13 PASS
   i3: rows 13/13, paired 13/13 PASS
   i4: rows 13/13, paired 13/13 PASS
   i5: rows 13/13, paired 13/13 PASS
== 5. anchors
   unresolved: none  duplicate ids: none -> PASS
== 6. forbidden strings (count per pattern, public HTML)
   model names: 0 
   internal ids S#/W42-S#: 0 
   sources.yaml: 0 
   file paths: 0 
   word writer: 0 
   notes: 0 
   unpublished branch: 0 
   per-item .qc: 0
   lowercase sympy: 0 
   old labels (i1 C1/C2, D1-D4; i5 D#/B#/F#): 0
   non-scale grades: 0 
   two decades vs lower bound: 0 
   opposite sign (archive comparison): 0 
   most promising: 0 
   title-level mismatch: 1 [('i2', '제목 수준')]
   tail qc blocks: 1 (report-level, expected 1)
== 7. ASCII-token multiset diff vs _orig (per file)
   [report_head] +169 -11
     added  : .x4 1x8 2x4 24x2 3x2 36x2 4x4 5x4 Ax4 A0x2 BR1x2 BR6x2 C C. C1x2 C11x2 D D. DOEx2 Ex2 Eqs.x2 FAILx2 Item J1x2 J4x2 K1x2 K5x2 M1x2 M7x2 N1x2 N2x2 Numbered On PASS-WITH-FIXESx2 PENDING. PERFORMED. R1x2 R6 R6. Supplementaryx2 These ax3 also an andx7 applied arex4 arithmetic arm arms bridging checklistx2 checks comparison competing corrected criteria derivationsx2 distinct error evidence first fixes grade grades have is itemx7 items labelsx2 mechanisms misstated now numerical-magnitude onex2 only pass perx2 prefix re-check refutation s sign source steps structures symbolic test that thex2 unrelated used usesx3 wasx2 were with within wording
     removed: PENDING S24x2 S36x2 as has not performed single-source yet
   [i1] +157 -107
     added  : .x2 1.14.0. 10x2 12x2 16x2 17x2 20x2 6x2 7x2 Cx6 J1x6 J2x8 J3x9 J4x5 N1x2 N2x6 SSDsimx6 T-only That adjustment algorithm-level arex2 attributes authors captions cell chipx2 circuits citedx2 compensation context dependence details device-level equivalent fed figuresx2 given gradex2 here input introductionx2 latency lookupx4 measurements models notx4 on-chip only operating orx2 originals outputx2 prediction presented read-voltage reproduced response-time results same seen shifts shown simulatorx4 so source source-reported tablex3 tablesx2 temperature text that thex6 through to varies were withx4 work. workloadx2
     removed: 1 1.14.0 2Dx4 3Dx4 Bx2 C1x2 C2x6 D1x6 D2x8 D3x9 D4x5 NANDx2 Temperature-dependent Vx2 activation andx4 arrays background cell-to-cell channels comparisons cross-temperaturex4 current dynamicx2 effectsx2 inx4 kept list literature notes. ofx3 paper poly-Six2 primary programx2 reference resulting scriptx2 shift shown. stringx2 thx2 this title topics trackingx2 variabilityx2 working
   [i2] +65 -163
     added  : 80x2 CAAx2 GBLx2 ILx2 PS1x2 PS2x2 VNAND a also as atx2 bx2 bottleneck boundaryx2 cites close conservatively contribute contribution curvature diffusion discusses inx3 interpretation it keeps layer literature-cited on passage permittivity physical rx4 ratios report reverse section sidex4 source stackx4 thickness thisx4
     removed: .x4 10x4 110x2 2x2 3x4 39x2 4x2 5x2 67x2 68x2 79x2 87x2 BTIx2 By Citation FETx2 FeFETx3 FeFETs FeNANDx2 GAAx2 HfOx2 OS OS-channel Poly-Si RAWDx2 S1x2 S2x2 The Vx2 VNAND. alone an and are atomic-layer-deposited attachedx4 because below betweenx2 bracketed cannot capacitance channel charge-trapx2 citationsx2 conclude confirm cyclex2 cylindrical degrading diffusion. do facex2 fail flashx3 for hetero-strainx2 imbalance indium indium-oxide inner is mapping.x2 mismatches most nanowirex2 negative negative-capacitance-in-flash nmx2 notx2 number ofx3 originals outer oxide p.24x2 paperx3 paper. papers poly-Si promising rate re-examining read refx6 reference-list refsx2 same some statementsx2 support supports thx2 that these title-level titlesx2 tox2 transistorx2 we were windowx2
   [i3] +128 -4
     added  : .x4 10-18x2 2026-10-12x2 2026-10-15x2 4.0x2 403x2 BYx2 CCx2 Crossrefx3 Crossref-deposited ENGINEERING_INFERENCE Eng HTTPx2 MDPI Thex2 This ax2 abstractx3 abstract. access according and are article as automated based below briefx2 bypassed cellx2 channelx2 coaxial day describe does expressions frameworkx2 geometry holex2 inside isx2 issuedx2 it item journal licensex2 model. multiple new new_this_weekx3 notx3 onx2 online onlyx2 page paperx2 published published-onlinex2 publisher radius report required result returned sx3 same sox3 stackx2 starts thex6 thisx4 tox3 treated wasx2 weekx2 windowx2
     removed: Engineering inference needed several
   [i4] +570 -143
     added  : .x10 1x18 1.3x4 10x21 11x2 12x2 13x2 2x30 23x2 24x4 25x2 27x2 3x22 3.x2 32x3 33 34 36x4 4x15 5x8 A ENGINEERING_INFERENCEx3 Eqs.x4 Figs. HZOx6 Informationx9 Nx4 Sectionx4 Sectionsx2 SiCx6 Supplementaryx52 Supportingx9 SymPyx26 SymPy-checked Tablesx8 Thex3 UNKNOWNx4 W40x6 What ax8 aboutx4 above absorbed accounting acts andx8 asx6 assumption at authors basesx2 basis be below beneficial both bound but by cannot cause cmx4 coefficients coexist comparisonx4 corresponds count cyclex2 cyclingx2 de-trappingx4 decade decadesx2 defects delayx2 dependence differx2 diffusion diffusion-coefficient directionx2 doesx2 domainx2 domain-wallx2 duringx2 equalx3 explanation factorx2 frequency from gain generated give given harmful here hold.x2 however identified iiix2 inx10 increases infer inferencex3 into introduction is itx2 itemx6 its lengthens life lossx2 lowerx2 mx4 matches may netx2 numerical ofx8 onex2 orx2 oxygen pinningx4 presents proposed rangex2 ratex6 ratherx3 reads recoveryx3 redistributed reportx5 rolex2 roles sx14 same should shows sign-test sox2 source spanningx2 spans stack statedx2 states stressx2 taken test thanx3 that thex10 therefore thisx6 timex3 twox2 typically universal unverified upper vacancies velocities velocity vs wallx2 wall-clockx2 we with worse worse.
     removed: Engineering S1x16 S10x3 S2x24 S24x4 S3x22 S3.x2 S32x3 S33 S34 S36x4 S4x11 SIx2 Sec. Tablex8 adds effects explain it. not notesx3 numeric recovery. rest showing sympyx24 sympy-checked to universal. used
   [i5] +117 -83
     added  : 1x6 1.14.0 1.3.0 2x6 3x6 4x4 BR1x2 BR2x2 BR3x2 BR4x6 BR5x2 BR6x2 Cx4 K1x6 K2x6 K3x2 K4x2 K5x8 Rx2 R1x2 R2x2 R3x2 R4x2 R5x2 R6x2 Structurex9 Structures agree and area capacitance channelx2 derivation gatex2 mpmath oxx4 per re-run resistance script shx4 sheet values with
     removed: B1x2 B2x2 B3x2 B4x6 B5x2 B6x2 D1x6 D2x6 D3x2 D4x2 D5x6 F1x2 F2x2 F3x2 F4x2 F5x2 F6x2 Python S1x6 S2x6 S3x6 S4x4 environment for item library pinned standard the this unavailable was
   [report_tail] +396 -96
     added  : .x2 1x4 13x2 2x6 24x2 3x7 36x2 4x8 5x3 APIx3 BR1x2 BR2x2 BR3x2 BR4x4 BR5x2 BR6x2 DataCitex2 DataCite. Each Eqs.x2 FAIL Gx4 HZOx2 If In J1x2 J2x2 Model-basedx2 Nx2 PASS-WITH-FIXES PENDING PERFORMED R1x3 R4x3 Sections SiCx2 Supplementaryx6 SymPy Tables UNKNOWNx2 W40x2 ax8 aboutx3 abstractx2 accounting across act andx11 applied arXivx6 asx3 assumption at authors basesx2 below bothx2 bound but can cause charge cited claim coaxial compared comparisonx5 compensationx2 constant correctedx5 cross-temperaturex2 decade depend dependence differx2 direction doesx2 drift during effect electrons equal errorx3 factor fieldx4 first-pass fixes flashx2 forx4 foundx3 gain grade grows hold inx8 interpretation interval isx7 itemx8 items keep label largerx2 layer link loss lowerx2 magnitudex2 match memory.x2 misstated negation now numerical-magnitude ofx7 onx2 onex5 or out pagesx2 per physicsx5 planarx2 points program programmed radiusx6 ratex6 rate-limitedx2 ratio re-checkx4 re-confirmedx2 re-derived read-reference-voltagex2 rejected. reliabilityx2 repeated report report-level reported restx2 reviewx4 sx2 samex2 self-field shifts shrinks sign size sox2 sourcex3 splits state storedx2 stressx2 summaryx2 text thatx3 thex32 through time tunnelx3 tunnel-layer upper values verdicts vs wasx3 well withx2 wording worsex2 xx4
     removed: B1x2 B2x2 B3x2 B4x4 B5x2 B6x2 Compensationx2 Cross-Temperaturex2 D1x2 D2x2 F1x3 F4x3 Flashx2 For Memory.x2 Model-Basedx2 Read-Reference-Voltagex2 Reliabilityx2 S1x2 S2x2 S24x2 S3x4 S36x2 S4x2 Self-check Table alone be between changes check citationx2 citations conclusion confirmed could drawn each effects explains fail independentx2 lifetime no notes numbers only opposite originals performed radius. re-run read reference-list single-source some stated statement statements. summarized support thosex2 titles were
```

## Appendix D. Change log
Full per-change log (finding id, file, old -> new): _fix/changes.log


---

# Third fix pass (review\recheck.md minor findings m-1..m-6 + QC wording), 2026-11-10

Backup: `sections\_orig3\*.html` (copied before any change). Edits: `_fix3\patch3.py` (32 exact-string patches, each asserts count 1; rebuilds sections\*.html from _orig3 every run, so re-running is idempotent). Per-change log: `_fix3\changes3.log`. Self-checks: `_fix3\selfcheck3.py` -> `_fix3\selfcheck3_out.txt`. Linter output: `_fix3\lint3.txt`.
Bash changes this pass: mkdir `_orig3` and cp of the 7 html files into it; fresh per-page pdftotext of the item-2 PDF and one curl of the arXiv HTML page into the session scratchpad (outside sections\, read-only use); runs of patch3.py, selfcheck3.py and the repo linter (read-only on the repo clone). The assembled file `_assembled\reports\2026\w42\index.html` was overwritten by selfcheck3.py (plain concatenation head+i1..i5+tail, the same method as before; the previous assembled file was verified byte-identical to the concatenation of _orig3). The work was interrupted once by a usage limit; on resume, _orig3 was confirmed untouched (no "greatest promise" in _orig3/i2.html) and patch3.py was re-run from _orig3 (idempotent).

## Correction note (m-1): the earlier M2-2 rationale was wrong

The first review and the M2-2 row above said the source contains no "most promising"-type rating. **That claim was wrong.** The source (arXiv:2512.15988v1) states, in the first paragraph of the section "Challenges and Prospects of Gate-injection-type FeNAND" (PDF p.22), that the authors focus on the gate-side injection ferroelectric transistor, which "holds the greatest promise for future NAND technology". Two independent reads in this pass:
1. Fresh `pdftotext -f 22 -l 22` of the quarantined PDF (sha256 eeb525f1...dd3e; pdftotext 4.00): the sentence is on p.22 (p.21 ends with printed page number 21; the section heading opens p.22). It is also in the older extractions (raw.txt 1007-1008, layout.txt 683-685).
2. arXiv HTML rendering https://arxiv.org/html/2512.15988v1 (HTTP 200, title matches), tags stripped: same sentence, same section.
Action: observation (2) restored as SOURCE_REPORTED (the authors' own assessment) in short paraphrase with its location, ko/en; tail Item 2 (2) given the same statement. No other place contradicts it (grep: "this section discusses"/"이 절이 다루는" 0, "most promising"/"가장 유망" 0, no "authors do not rank" wording anywhere).

## Applied

| ID | Files | Change |
|---|---|---|
| m-1 | i2 obs (2) ko/en; tail Item 2 (2) ko/en | "the type this section discusses" removed; added: on p.22 (first paragraph of "Challenges and Prospects of Gate-injection-type FeNAND") the authors say they focus on this type and describe it as introducing new physical mechanisms and holding the greatest promise for future NAND technology (SOURCE_REPORTED, authors' own assessment; both extractions agree). |
| m-2 | i4 obs (4) ko/en; tail Item 4 (4) ko/en | "stated lower/upper bound" / "하한·상한" -> "lower/upper end of the order-of-magnitude range stated in the text ("of the order of" 10^-5-10^-4 m/s)" / "본문이 쓴 자릿수 범위(... 정도)의 아래쪽/위쪽 끝". Numbers unchanged (source raw 297-298: "of the order of"). |
| m-3 | i1 DOE arms B and E | N in {N1<N2<N3} -> {N_lo<N_mid<N_hi}; C in {C0<C1<C2<C3} -> {C_w0<C_w1<C_w2<C_w3}. The coordinator's example L1<L2<L3 was not used because L is item 1's layer index (and item 5's channel length); the symbol C (P/E count, defined in the head) is kept with w-subscripts instead of W0-W3. The tail has no reference to these levels (grep). The head now names the new symbols. |
| m-4 | head "Labels" ko/en | "distinct prefix per item" narrowed to numbered derivation/check/criterion labels; added that DOE level symbols are redefined per item and can coincide with other labels (examples: item 3 R0-R2 vs item 5 R1-R6; item 3 N0-N2 and item 4 N1-N3 vs item 1 N1-N2), plus the item-1 renaming. |
| m-5a | i4 card Change vs archive ko/en; i4 archive table W40 row ko/en; tail matrix row 2 ko/en | Split into plain sentences: the direction is the same; but the comparison bases differ, so the shared direction alone does not allow concluding that the two are the same phenomenon; separately, the proposed role of de-trapping is opposite. "sign comparison does not hold" wording removed. |
| m-5b | i4 competing mechanism (3) ko/en | Now matches the source (raw 85-90 / layout 99-104, both extractions): the introduction calls the pinning explanation of [23]-[25],[27] "reasonable" but says it remains unclear how imprint and fatigue interplay and how that correlates with the larger loss at lower access rates. |
| m-5c | tail Item 2 (3) ko/en | "described differently" -> aligned to i2 (3): p.17 holes (or electron detrapping), p.21/p.26 gate-injected electrons; consistent if holes in PGM and electrons in ERS, but not stated explicitly. |
| m-6 | head evidence paragraph ko/en | Added: Supplementary Eq. (n) (ko: 보충 식 (n)) and Supplementary Table n denote the SI items numbered with the letter S before n, e.g. Supplementary Eq. (10) = (S10), Eqs. (24)-(36) = (S24)-(S36). Checked: the SI uses (S10), (S24)-(S36) and Table S1-S3 numbering; the "(S10)" form does not trigger leak-check. The optional arXiv-429 sentence was left as is. |
| QC | head ko/en; tail QC cells Physics independent review, Numbers traced, Fact vs inference labels, Derivations | Review cell now reads exactly: "independent physics review PERFORMED (item 4 FAIL on first pass; one numerical-magnitude error and a misstated sign comparison, now corrected); the fixes received a focused independent re-check (no blocker, no major); minor edits after that re-check received mechanical checks only". The other three cells carry the same status phrase; no PASS is claimed beyond that. "re-check PENDING" count is 0. |

## Self-checks (selfcheck3_out.txt)

- Tag balance: unclosed 0, mismatches 0: PASS
- Classes not in assets/style.css: none: PASS
- ko->en adjacency head+i1..i5+tail: ko 366 / en 366, 0 violations, 0 orphan en: PASS
- Card cells: 13/13 rows and 13/13 ko->en paired in each of i1..i5: PASS
- Anchors: 0 unresolved, 0 duplicate ids: PASS
- Forbidden strings: model names 0, S#/W42-S# 0, sources.yaml 0, paths 0, writer 0, notes 0, Table/Fig/Eq S# style 0, unpublished draft branch 0, lowercase sympy 0, non-scale grades 0, per-item qc 0 (tail qc 1). Finding-specific residues: stated lower/upper bound 0, old sign-comparison wording 0, described differently 0, distinct prefix per item 0, this section discusses 0, re-check PENDING 0, most promising 0. Old item-1 DOE level pattern: 1 hit, in i3 (item 3's own P/E levels N0<N1<N2; intended, not item 1).
- Linter (repo clone: `python -I scripts\report_lint.py all --root ..\w42\sections\_assembled --offline --report-only`): doi-format PASS, doi-duplicate PASS, kr-en-adjacency PASS (366/366), vocabulary PASS (353 tokens), leak-check PASS; abstract-only-guard NA, derivations NA. SUMMARY PASS=5, NA=2.

## ASCII-token diff vs _orig3, tied to findings

- report_head (+281 -7): removed "PENDING PENDING. been have" (QC); "distinct per prefix" (m-4). Added "N1 N2 R1 R6 C1 C11 DOE level(s) redefined coincide overlap prefixes label(s) lo hi w0 w3 Within" (m-4/m-3); "Supplementary Eq. Eqs. Table S10 S24 S36 SI supplementary information letter denote equation(s) example" (m-6); "focused independent re-check blocker major minor edits mechanical checks received restored source statement" (QC).
- i1 (+7 -7): removed subscripts "0 1 2 3" -> added "lo mid hi w0 w1 w2 w3" (m-3).
- i2 (+59 -2): removed "this discusses" -> added "On p.22 Challenges Prospects Gate-injection-type FeNAND authors say focus gate-side-injection introducing new physical mechanisms holding greatest promise future NAND technology SOURCE_REPORTED own assessment both extractions agree" (m-1).
- i4 (+91 -23): removed "stated bound(x2) m s" / added "order order-of-magnitude range text end(x2) its" (m-2); removed "What sign comparison hold. rate dependence however" / added "However Separately shared direction alone allow conclusion results same phenomenon. devices two" (m-5a); removed "presents as" / added "calls reasonable ascribes switched polarization loss remains unclear imprint fatigue interplay how correlates larger lower access rates." (m-5b).
- report_tail (+192 -32): removed "first-pass verdicts PASS-WITH-FIXES items report-level summary repeated well wording applied PENDING x4" (QC); "bound x2 sign comparison hold" (m-2, m-5a); "described differently p.20. p.26." (m-5c). Added "p.22 greatest promise holding future NAND technology SOURCE_REPORTED authors describe type" (m-1); "order-of-magnitude range text end its" (m-2); "However Separately shared direction alone allow conclusion same phenomenon. contradiction." (m-5a); "On PGM ERS hole(s) electron(s) gate-injected detrapping refers refer while explicitly. agree" (m-5c); "independent physics review focused re-check blocker major minor edits mechanical checks only received restored" (QC).
- i3, i5: no change.

## Not applied / open

- The optional arXiv-429 operational sentence (second half of m-6): left unchanged (factual; optional).
- fixlog M-T-3 (overlap with an unpublished W42 draft on another remote branch): out of scope, still unresolved (UNKNOWN); not mentioned in public HTML.
- The minor edits of this pass received mechanical checks only; there has been no independent physics re-check of them.
