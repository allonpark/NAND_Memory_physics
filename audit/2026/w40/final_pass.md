# W40 final pass (Task A content fixes + Task B 합니다체 register)

Date: 2026-10-21. Scope: sections/s1..s5.html, report_head.html, report_tail.html (edited in place). Baseline: _prefinal/ (untouched). Intermediate snapshot after Task A, before Task B: _postA/.
Tools: tools/hapnida.py (ending converter; log tools/applied.txt, 339 conversions), tools/selfcheck.py (output below).

## Task A edits (intentional token changes)
| id | file | change |
|---|---|---|
| s1-R1 | s1 DOE (ko+en) | H4b criterion: "t_fail independent of V_DG/V_DS" -> "change in t_fail with V_DG/V_DS at fixed T below pre-set tolerance δ_V rejects H4b (weak bias dependence of the H4a component separated out)". Symbolic only, no number. |
| s1-R2 | s1 sourcebox (ko+en) | "vendor FA perspective" -> "appears to be ... (an interpretation from the Crossref affiliation metadata, ENGINEERING_INFERENCE)" |
| s1-R3 | s1..s5 SOURCE TRACE, tail QC paragraph, tail QC Crossref row, tail Sources note (ko+en) | "Crossref re-lookup (2026-10-21)" -> "Crossref lookup (2026-10-19) and re-lookup (2026-10-21)". Basis: review/fetch_out.txt (2026-10-19, 5 DOIs) and fetch_out_recheck.txt (2026-10-21), diff empty per recheck.md. |
| s3-R1 | s3 SymPy header (ko+en) | removed "derived at drafting; ... in the 2026-10-21 independent review" -> "confirmed by symbolic and numerical re-derivation". No sample-size number added. |
| s4-R1 | s4 card CONTRADICTING DATA (ko+en) | "reversed-T reports may exist" -> "Labeled as a hypothesis only (literature not checked here, grade C): the temperature trend may be reversed ... treated only as a falsification candidate until checked." Grade C kept. |
| s5-R1 | s5 (iii) (ko+en) | "most direct argument" -> "one direct argument" |
| s5-R2 | s5 (i) (ko+en) | first sentence now starts with "Assuming Miner linear accumulation and unipolar rectangular pulses" |
| s5 extra | s5 (iii) ko only | "위 경쟁 메커니즘 (1)" -> "아래 경쟁 메커니즘 (1)" (the competing-mechanism list is below (iii); EN already said "below"). Hangul only, no ASCII token change. |
| head-R1 | head evidence box (ko+en); tail QC grid | removed first-pass FAIL history, "PENDING re-check" narrative and "Sonnet-class critic". Neutral row: "independent physics review performed 2026-10-21 on items 1–5; verdicts after correction: items 1–5 PASS-WITH-FIXES or better; all findings applied and re-checked; audit pack in repository folder audit/2026/w40/". Removed the separate "Re-check of applied fixes: PENDING" row (merged). "Numbers only from abstracts" and "Fact vs inference labels" rows -> "re-check DONE (2026-10-21)" (basis: recheck.md sections 2(4), 2(1)-(2)); removed the "untraceable temperature value replaced" narrative. |
| head-R2 | tail QC grid | KR→EN pairing -> "re-check DONE (2026-10-21): paragraphs and card cells paired; tables, h3 headings and chain nodes are English-only". |
Unchanged on purpose: Full text read NOT DONE (0 of 5); Publisher pages NOT VERIFIED; Render / PDF PENDING; Issue grade brief + hypothesis.

## Task B
All sentence-final plain endings in Korean prose converted to 합니다체 (339 sites; mapping table in tools/applied.txt). Only Hangul characters changed (check 1b below).
Intentionally left plain/noun form:
- Quoted propositions: s3 "grain >50 nm에서 분포 폭이 줄어든다", s5 "trap이 적으면 lifetime이 길다", tail '온도 부호는 mechanism별로 다르다' (quotation / proposition, not a sentence ending).
- Noun-phrase items: card cells (e.g. "초록만 읽음.", "미확인."), definition list in head ("외삽일 뿐임."), DOE level/criterion lists ("H1 기각." etc., same style as W39 hypothesis rows), bold run-in heads ("결론.", "라벨과 등급."), assumption lists.
- 보다/마다/다르고 etc. are not endings.

## Mechanical self-check output
## (1) ASCII token multiset: _prefinal vs final, and _postA (after Task A, before Task B) vs final
### report_head: prefinal->final removed={'(': 1, '4': 2, 'SOURCE_REPORTED': 2, 'FAIL).': 1, '(PENDING).': 2, 'item': 1, 'not': 1, '(items': 1, 'FAIL': 1, 'first': 1, 'pass': 1, 'one': 1, 'overstatement).': 1, 'The': 1, 'have': 2, 'been': 2, 'but': 1, 'fixes': 1, 'yet': 1} added={'and': 1, '.': 2, 'is': 1, 'All': 1, 'items': 2, 'were': 1, 'or': 1, '5.': 1, '5': 1, 'audit/2026/w40/': 1, 'are': 1, 'in': 1, 'verdicts': 1, 'after': 1, 'correction': 1, 'better': 1, 'audit': 1, 'pack': 1, 'repository': 1, 'folder': 1, 'audit/2026/w40/.': 1}
    postA->final identical: True
    postA->final change hunks=21, hunks touching non-Hangul chars=0
### s1: prefinal->final removed={'.': 2, 'perspective.': 1, 'independent': 1} added={'the': 2, 'in': 1, 'and': 1, '(Crossref': 1, ').': 1, 'ENGINEERING_INFERENCE).': 2, 'Crossref': 1, 'affiliation': 1, 'with': 1, 'appears': 1, 'to': 1, 'be': 1, 'a': 2, 'perspective': 1, '(an': 1, 'interpretation': 1, 'from': 1, 'metadata': 1, 'V': 2, 'weak': 1, 'below': 1, 'dependence': 1, 'H4a': 1, 'bias': 2, '(H4a': 1, 'pre-set': 1, 'tolerance': 1, 'change': 1, '(any': 1, 'component': 1, 'separated': 1, 'out)': 1, '(2026-10-19)': 2, 'lookup': 1}
    postA->final identical: True
    postA->final change hunks=50, hunks touching non-Hangul chars=0
### s2: prefinal->final removed={} added={'and': 1, '(2026-10-19)': 2, 'lookup': 1}
    postA->final identical: True
    postA->final change hunks=50, hunks touching non-Hangul chars=0
### s3: prefinal->final removed={'in': 1, '2026-10-21': 2, 'the': 1, 'at': 1, '(derived': 1, 'drafting': 1, 're-derivation': 1, 'matched': 1, 'independent': 1, 'review).': 1} added={'and': 1, 'by': 1, '(confirmed': 1, 're-derivation).': 1, '(2026-10-19)': 2, 'lookup': 1}
    postA->final identical: True
    postA->final change hunks=58, hunks touching non-Hangul chars=0
### s4: prefinal->final removed={'for': 1, 'C).': 2, 'Reversed-T': 1, 'reports': 1, 'exist': 1, '(MVE/EES)': 1} added={'in': 1, 'a': 2, 'the': 1, 'temperature': 1, 'and': 1, '.': 2, 'is': 1, 'as': 2, 'trend': 1, 'only': 2, 'C)': 2, 'be': 1, 'falsification': 1, 'Labeled': 1, 'hypothesis': 1, 'reversed': 1, '(MVE/EES).': 1, 'It': 1, 'treated': 1, 'candidate': 1, 'until': 1, 'checked.': 1, '(2026-10-19)': 2, 'lookup': 1}
    postA->final identical: True
    postA->final change hunks=50, hunks touching non-Hangul chars=0
### s5: prefinal->final removed={'the': 1, 'With': 1, 'most': 1} added={'and': 2, 'with': 1, 'unipolar': 2, 'pulse': 1, 'Miner': 2, 'rectangular': 1, 'pulses': 1, 'linear': 1, 'accumulation': 1, 'Assuming': 1, 'one': 1, '(2026-10-19)': 2, 'lookup': 1}
    postA->final identical: True
    postA->final change hunks=75, hunks touching non-Hangul chars=0
### report_tail: prefinal->final removed={'the': 1, 'a': 1, '2': 1, 'item': 1, 'by': 2, 'one': 1, 'of': 1, '4': 2, 'temperature': 2, '5)': 1, 'independent': 1, 'first': 1, '(items': 1, '2026-10-21': 2, 'direct': 1, 'during': 1, 'review.': 1, 'Sonnet-class': 1, 'critic': 2, 'FAIL': 1, '(one': 1, 'SOURCE_REPORTED': 1, 'overstatement)': 1, 'now': 1, 'corrected': 1, 'Re-check': 1, 'applied': 1, 'fixes': 2, 'PENDING': 4, 'untraceable': 1, 'value': 1, 'replaced': 1, 'room': 1, 'writer': 1, 'self-check': 1, '(paragraphs': 1, 'paired)': 1, 'pending': 5} added={'items': 1, '1': 1, 'in': 1, 'and': 5, 'or': 1, '5': 1, 'are': 1, 'all': 1, '(2026-10-19)': 4, '(2026-10-21)': 4, 'lookup': 3, '(2026-10-21).': 1, '2026-10-19': 1, 'DONE': 2, 're-checked': 1, 'review': 1, 'physics': 1, 'performed': 1, 'verdicts': 1, 'correction': 1, 'better': 1, 'audit': 1, 'pack': 1, 'repository': 1, 'folder': 1, 'audit/2026/w40/': 1, 'paragraphs': 1, 'paired': 1, 'tables': 1, 'h3': 1, 'headings': 1, 'chain': 1, 'nodes': 1, 'English-only': 1, 'pass': 3}
    postA->final identical: True
    postA->final change hunks=35, hunks touching non-Hangul chars=0

## (2) structure
tag errors: [] unclosed: []
undefined classes: []
duplicate ids: []
unresolved anchors: [] (12 anchors)
ko/en paragraphs: 153 / 153 adjacency violations: 0 p without lang: 0
leftover plain endings in <p lang=ko>: 2
    줄어든다 | 록의 "grain >50 nm에서 분포 폭이 줄어든다"는 
    다르다 |  지도에 '온도 부호는 mechanism별로 다르다'는 
ko paragraphs containing 합니다체 endings: 96

## (3) forbidden strings in public HTML (all 7 files concatenated)
  S1: 0 (substring count 0)
  S2: 0 (substring count 0)
  S3: 0 (substring count 0)
  S4: 0 (substring count 0)
  S5: 0 (substring count 0)
  sources.yaml: 0 (substring count 0)
  Sonnet: 0 (substring count 0)
  Opus: 0 (substring count 0)
  Fable: 0 (substring count 0)
