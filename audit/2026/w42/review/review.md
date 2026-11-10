# W42 항목 i1~i5 및 report_head / report_tail 독립 검수 (review.md)

검수일: 2026-11-10 / 검수자: 작성자(Opus)와 다른 모델(Sonnet 5.5) / sections의 i1~i5.html, report_head.html, report_tail.html, notes, sources.yaml은 수정하지 않았다.
이 문서와 스크립트는 `work\w42\review\`에만 썼다. push, PR 없음. 모든 PASS는 내가 실행한 점검 또는 원문과의 문자 대조에 근거한다. 두 번의 서로 다른 읽기에서 일치하지 않거나 한 번만 확인된 값은 UNKNOWN이다.
임시 폴더 유실 후 재구성된 파일이므로 "현재 텍스트"를 기준으로 판정했다.

## 0. 총평

| 대상 | 판정 | blocker | major | minor |
|---|---|---|---|---|
| i1 (Luo 외, IEICE ELEX, 3D TLC 교차온도 read 보상, archive_gap) | PASS-WITH-FIXES | 0 | 2 | 4 |
| i2 (Kim 외, FeNAND Perspective, archive_gap) | PASS-WITH-FIXES | 0 | 3 (M2-2는 blocker 가능) | 4 |
| i3 (Jang 외, PAHT, Eng, abstract_only) | PASS-WITH-FIXES | 0 | 0 | 3 |
| i4 (Guido 외, HZO 접근률 endurance, preprint) | FAIL | 1 | 2 (M4-2는 blocker 가능) | 3 |
| i5 (Chen 외, AOS CSC, preprint) | PASS-WITH-FIXES | 0 | 1 | 3 |
| report_head | PASS-WITH-FIXES | 0 | 1 | 2 |
| report_tail | FAIL (i4 blocker와 M4-2를 그대로 인용) | 1 | 3 (+M4-2 전파) | 3 |

전체 판정: **FAIL**. blocker는 한 건이고(B-1, i4 관찰 (4)의 "두 자릿수" 수치 오류와 tail의 같은 문장), 수정이 쉽다. 엄격하게 읽으면 blocker로 올릴 수 있는 major가 둘 있다: M2-2(i2 관찰 (2)의 출처에 없는 서술), M4-2(i4와 tail 행 2의 "opposite sign" 교차 비교). 조정자가 판단해 달라.
물리(부호, 기하, 단위)는 내가 sympy로 다시 유도한 모든 식(item 1~5)에서 일치했다. 유일한 수치 오류는 B-1이다. 환각된 DOI, 수치, 그림, 조건은 찾지 못했다. 기밀 수치도 없다.

## 1. 수행한 점검과 근거 파일 (`work\w42\review\`)

| 파일 | 내용 |
|---|---|
| quarantine\cr1.json, cr3.json | Crossref 직접 재조회(item 1, 3): 제목, 8명/7명 저자, 날짜, 초록 유무, 라이선스. parse_meta.py로 출력 |
| quarantine\abs_*.html, dc_*.json | arXiv 초록 페이지 3건(제목, 저자, 초록, 제출일 UTC, 분류, comments)과 DataCite API 3건(registered/Submitted/Updated). arXiv Atom API는 4회 시도 모두 HTTP 429 "Rate exceeded"로 **UNKNOWN**(대신 abs 페이지와 DataCite를 두 번째 독립 출처로 썼다) |
| quarantine\a1~a5 | item 1은 J-STAGE `_23.20260379` 기사 페이지와 copyedit PDF(`_pdf/-char/en`), item 2, 4, 5는 arXiv PDF를 curl로 받아 pdftotext -layout과 -raw(-enc UTF-8)로 각각 추출(두 번의 읽기). item 1의 advance판 PDF는 다시 받지 못했다(UNKNOWN 처리) |
| extract.py, txt\ | 섹션 HTML을 태그 구조 보존 텍스트로 변환해 영문 문단 전체와 한국어 표본을 읽었다 |
| derive_checks.py, derive_out.txt | 독립 sympy 1.14.0 재유도 (venv_sympy, -I). 아래 항목별 근거 |
| mech_checks.py, mech_out.txt, card_check.py, ctx2.py, ctx3.py | 태그 균형, style.css 클래스 대조, ko→en 인접성, 라벨/등급/숫자 토큰 쌍 대조, 합니다체, 금지 문자열, 카드 13행, 앵커 |
| writer_scripts_rerun\ | 작성자 스크립트 i1_checks, i2_checks, i3_checks, i5_checks, i5_sympy를 같은 venv로 다시 실행: 모두 exit 0, FAIL 0 |

## 2. 서지와 날짜 (직접 재조회)

| 항목 | 제목/저자 | 날짜 | 판정 |
|---|---|---|---|
| i1 | Crossref 일치(8명, Luo C. ... Huo Z., IEICE Electronics Express 23(18) 20260379). Crossref에는 초록이 없다(본문 PDF에서 읽음) | J-STAGE 페이지: Received 2026-07-13, Accepted 2026-07-23, Advance online publication 2026-08-25, Released/Published 2026-09-25. PDF 표지: Publicized 2026-08-25, Copyedited 2026-09-25. Crossref issued 2026-09-25 (created 2026-08-24 UTC). 모두 window(10-12~10-18) 이전 | PASS (archive_gap 맞음) |
| i2 | arXiv abs 일치(15명 전원, 순서 일치). arXiv:2512.15988 [physics.app-ph] | v1 2025-12-17T21:43:39Z. DataCite Submitted 2025-12-17, Updated 2025-12-19 | PASS (archive_gap 맞음) |
| i3 | Crossref 일치(7명, Eng 7(10) 563). 초록 전문 확보(아래 3.3 대조) | published-online/issued/created 2026-10-15, CC BY 4.0 start 같은 날 | PASS (new_this_week 맞음) |
| i4 | arXiv abs 일치(9명). cond-mat.mtrl-sci | v1 2026-10-14T13:11:11Z (KST 10-14 22:11). DataCite Submitted 같음, registered 2026-10-15T02:54Z | PASS (new_this_week 맞음) |
| i5 | arXiv abs 일치(5명). cond-mat.mtrl-sci, Comments "4 pages, 10 figures" (i5 소스박스와 일치) | v1 2026-10-12T09:03:22Z (KST 10-12 18:03, window 안). DataCite Submitted 같음, registered 2026-10-14T07:07Z | PASS (new_this_week 맞음) |

arXiv 공지(announcement)일은 나도 확인하지 못했다(UNKNOWN). 항목들이 "미확인"이라고 쓴 것은 정직하다.
메모: 소스 목록 [1]의 제목은 title case("Model-Based Read-Reference-Voltage Compensation ... Memory")인데 Crossref와 J-STAGE 페이지의 제목은 sentence case다(minor m-T-3).

## 3. 항목별 검수

공통 기계 점검(mech_out.txt, card_check.py): 연결 대상 7개 파일 모두 태그 균형 오류 0(tail 단독 파싱의 article/div/body 닫힘은 head가 연 태그를 닫는 것이며 연결 시 균형), 중복 id 0, style.css에 없는 클래스 0, TOC 앵커 미해결 0. ko 365 / en 365 문단(head 22, i1 31, i2 106, i3 35, i4 43, i5 43, tail 85), ko→en 인접성 위반 0, 영문 문단 안 한글 0, 문단 쌍마다 라벨(SOURCE_REPORTED 등) 개수와 등급 문자가 ko와 en에서 같음(차이 0), 두 자리 이상 숫자 토큰은 365쌍 중 364쌍 일치(나머지 1쌍은 "10배당" 대 "per decade"로 무해). 카드는 5개 항목 모두 13행, 각 값 셀에 ko와 en 모두 있음(13/13). item 내부에 .qc 블록 없음(.qc는 tail의 보고서 단위 블록 1개뿐). 등급은 A–D만 사용(A-, B- 같은 비척도 값 없음).

### 3.1 i1 — Luo 외, 교차온도 read 기준 전압 보상 (full_text, archive_gap)

| 점검 | 판정 | 근거 |
|---|---|---|
| (1) 출처 충실도, 라벨 | PASS-WITH-FIXES | 아래 대조. 지적 M1-1, M1-2, m1-3 |
| (2) 물리, 기하 | PASS (기하는 UNKNOWN으로 올바르게 표기) | derive_out.txt |
| (3) 경쟁 메커니즘, 경계 | PASS | 표 M1–M7, Tr>Tbake 경계, D4 존재 조건 |
| (4) DOE 반증 가능성 | PASS | A0는 기존 grid 재분석, 기호 수준, (A0)~(E) 기각 기준 |
| (5) 이중언어 | PASS | 31쌍 인접성 0 위반, 라벨/숫자 일치. 의미 대조 표본 6쌍(소스박스, 새로운 점, D1 변수/가정, D4 변수, 카드 CLAIM 등): 이탈 없음. 합니다체 위반 0 |
| (6) 카드 13행 | PASS | card_check.py |
| (7) 환각, 내부명, 등급 | FAIL (M1-1) | 환각 없음. 내부 노트 언급은 m1-4 |
| (8) 마크업 | PASS | |
| (9) 날짜 | PASS | 위 2절 |

**원문 대조(copyedit PDF의 raw와 layout 추출 두 번, 문자 대조).** 24.28%→0.44%, 98.19%, 43.81%, 0.08%, 774.770/440.496/435.362/435.008 μs, P90 1094.966, 표준편차 323.055, MB-RRVC 436.020/443.300/1.320, 85 °C 10 h, −40~120 °C 20 °C 간격, 45 points, ten traces, 960 B, 128-layer 다른 세대, Received 07-13, Accepted 07-23, Publicized 08-25, Copyedited 09-25, CC BY-NC-ND 4.0, NplusT 모두 본문과 일치한다(두 추출 일치). "program 후 bake 다음 random data를 program"이라는 문장, "median value of Δμ", "baseline condition" 미정의, "same program/read temperature condition, Baseline shows the highest RBER" 문장도 원문에 그대로 있다(관찰 (1)~(5) 확인). Eq.(1)은 raw에서 "Á % ÀTCO Â ÁT; ÁT ¼ Tread À Tprogram"로 나오며 Á→Δ, %→≈, À→−로 읽고, 본문 "increased channel current at T2 makes the threshold voltage appear to shift toward a lower voltage"와 "Tco defined as positive"가 −Tco·ΔT 부호를 지지한다: 부호 PASS(한 번의 글리프 읽기라는 한계도 item이 정직하게 적음).

copyedit 추출에는 Algorithm 1/2와 Table I 행이 없다(grep 확인). 따라서 5개 program 온도 목록(−40, 0, 40, 80, 120)과 CTDVT/Ideal 행은 내 읽기로는 확인 불가(**UNKNOWN**)이며, 작성자가 "한 번만 읽힘, 미사용"으로 처리한 것이 맞다. Fig. 5 캡션의 −40/40/120 °C는 확인했다.

기하: 본문(참고문헌 제외)에서 "cylind", "channel hole", "radius", "coaxial", "charge-trap", "floating gate" 일치 0건이다. 참고문헌 제목에만 [4] "3-D CTF NAND", [9] "undoped cylindrical gate-all-around-based MOSFETs"가 있다. item 1이 "기하 UNKNOWN, CT/FG 미기재, 일부 참고문헌 제목이 CT 소자"라고 쓴 것은 정확하다.

**독립 sympy 재유도(derive_out.txt).** 98.1878%(원문 98.19), 43.8076%(43.81), 0.0814%(0.08, Ideal 대비): PASS. 5×9=45(9개 read 온도), 서로 바꾼 쌍 10개, 최대 |ΔT|=160: PASS. Δμ=g(Tr)−g(Tp)의 반대칭과 가산성은 임의 g에 대해 기호적으로 0: PASS. 2차 g에서 Δμ=−aΔT−bΔT(Tp+Tr−2T0): PASS. 동축 ΔV=Q′/(2πε)·ln(rout/rin), 단층 비 f(u)=ln(1+u)/u(u=t/r0), f′(u)=(u−(u+1)ln(u+1))/(u²(u+1))<0, u→0에서 1: PASS. D3 E(r0)/E_planar=1+u(모든 영상 전하가 채널 쪽): PASS. **두 개의 반대 부호 동축 진술**: 같은 t에서 df/dr0=+0.0721>0(trap 점유 경로의 Tco는 r0와 양의 상관), d(1+t/r0)/dr0=−0.25<0(전계 의존 손실 경로는 음의 상관): item 1 (c)와 DOE의 부호 예측(M1 양, M4 음)과 일치. **꼬리 진술(D4)**: z·sqrt(σ0²+σk²ΔT²)=m의 해 |ΔT|*=sqrt(m²−σ0²z²)/(σk z), 존재 조건 m/z>σ0, 큰 ΔT에서 σres→σk|ΔT|: PASS.

**지적 (i1)**
- **M1-1 (major)** 위치: 카드 CONFIDENCE "SSD latency figures: grade B as simulator results, not drive measurements" 및 report_head "Labels and grades"의 "Grade B is used only in item 1, ... and to the SSD latency figures as simulator results". 문제: 프로젝트의 등급 정의에서 B는 문헌+동일 영역 계산이다. SSDsim 응답 시간은 소자 수준 등가 지연을 lookup table로 시뮬레이터 파라미터에 넣은 출력이며, 본 보고서가 재현하지 않았고 입력 표와 workload도 보지 못했다. 시뮬레이터 결과를 B로 두는 것은 등급 인플레이션이다(synth_notes 4번이 이미 의심). 수정: SSDsim 수치는 "원문 보고값, 시뮬레이터 결과, 등급 C"로 낮추고, head의 해당 문구에서 "and to the SSD latency figures as simulator results"를 삭제해 "Grade B is used only in item 1, limited to the linearity of the mean Vth shift and the compensation effect measured on that chip"로 줄인다(ko/en 동시).
- **M1-2 (major, 참고문헌 제목 기반 추론)** 위치: "New vs known"의 "Known ... Temperature-dependent current in poly-Si channels and the resulting Vth shift, comparisons of temperature effects in 2D and 3D arrays, temperature activation and variability of string current, cross-temperature effects of program and read in 2D and 3D NAND, dynamic Vth tracking, and cell-to-cell cross-temperature variability are topics of prior work in this paper's reference list (by title)". 문제: 원문 본문이 설명하는 것은 [7–10](채널 전류가 온도에 따라 변함), [6,17–20](알고리즘 수준 read 전압 조정), [12–16](온칩 보상)뿐이다. 나머지 주제 목록은 참고문헌 제목에서 읽은 것이어서 "이미 알려진 것"의 근거로 약하다. item이 "by title"이라 밝히고 등급 C로 낮췄으므로 완화되어 있다(이 완화 문구가 빠지면 blocker 후보). 수정: "Known" 문장을 본문이 인용하는 맥락([7–10], [6,17–20], [12–16])으로만 쓰고, 제목에서 읽은 주제는 "reference titles suggest (not read)"로 따로 표기하거나 삭제한다.
- **m1-3 (minor)** 위치: SOURCE_REPORTED (10) "...consistent cross-temperature trends; no data are shown." 그림을 읽지 못했으므로 "no data are shown"은 확인할 수 없는 부정이다(캡션 Fig. 1~5에 128-layer 언급은 없다). 수정: "no data are given in the text or captions (figures not read)".
- **m1-4 (minor)** 위치: "the script and output are kept in the working notes". 공개 HTML이 내부 노트를 가리킨다. 삭제하거나 "SymPy 1.14.0으로 확인"으로 줄인다.
- **m1-5 (minor, 라벨 충돌)** 위치: "derivations C1, C2", "(derivation C2)". item 2의 checklist C1–C11과 겹치고, D1–D4는 등급 D와 글자가 같다. 수정: 유도 라벨을 "derivation (i)"처럼 쓰거나 N1, N2, E1~E4로 바꾼다. tail은 item 2 checklist만 가리킨다고 밝히고 있어 혼동은 제한적이다.
- **m1-6 (minor)** 위치: h2 "a linear-in-ΔT engineering model". 관찰 (7)과 매트릭스 행 1이 "ΔT-only는 데이터로 입증되지 않음"이라 하므로 제목이 "ΔT만의 함수"로 읽힐 여지가 있다. "(authors' linear-in-ΔT model; ΔT-only dependence not shown)"으로 한정한다.

### 3.2 i2 — Kim 외, Vertical NAND in a Ferroelectric-driven Paradigm Shift (Perspective, archive_gap)

| 점검 | 판정 | 근거 |
|---|---|---|
| (1) 출처 충실도, 라벨 | PASS-WITH-FIXES | 아래. M2-1, M2-2, M2-3 |
| (2) 물리, 기하 | PASS (m2-4, m2-5 표현 지적) | derive_out.txt |
| (3) 경쟁 메커니즘, 경계 | PASS | 5행 표(Perspective의 귀속과 경쟁 설명 열 분리), 경계(equal field 대 equal ΔV, plate 대 edge) |
| (4) DOE | PASS | 우선 arm 기호 수준, 기각 기준 (1)~(4), C1~C11 각각 기각 기준 |
| (5) 이중언어 | PASS | 106쌍. 표본 6쌍(chain 1, Poly-Si 행, C 카드 GAA/CAA, 사슬 해설, 소스박스, 관찰 단락) 의미 일치 |
| (6) 카드 13행 | PASS | |
| (7) 환각, 내부명, 등급 | PASS-WITH-FIXES | 등급 C, D만 사용 |
| (8) 마크업 | PASS | |
| (9) 날짜 | PASS | |

**원문 대조(layout과 raw 두 추출).** SOURCE_REPORTED (1)~(13)을 문자 대조했다. WL+space oxide 약 40 nm [22], program 전압 "typically above 20 V" [25,39,40], "typically exceeding ±20 V"(raw에서 ± 확인, layout은 깨짐), ISPP slope "cannot exceed 1"과 FeNAND "above 2" [25,26,39,40], CTF "excellent retention ... above 20 V ... only about 10^3 to 10^4 cycles" [39,67,68,79], FeFET "below 5 V ... tens of nanoseconds" [72,73,80], gate-side-injection FeNAND 10^3–10^4 [21,66,67,79], 산소 interdiffusion [94,95;96], poly-Si "exceeding 950 C" [94,95,107], "below 3 nm", BTBT between GSL and CSL [99;100–102], OS 넓은 bandgap이 hole 생성을 제한하고 GIDL-assisted ERS를 못 쓰게 함 [100,101], 비정질 OS "≤50 cm²/Vs"(raw에서 ≤ 확인) [105], 다결정 OS ">100 cm²/Vs", data availability "does not contain any new experimental data": 모두 원문에 있고 인용 번호도 일치한다. AUTHOR_INTERPRETATION (b) GAA에서 GBL이 바깥, IL이 안쪽, CAA 제안, "radical architectural change ... comprehensive evaluation"도 원문과 일치한다. 관찰 (1)(Gb/mm² 축 대 100 GB/mm² 캡션)과 (3)(p.17 holes from the gate, p.21 gate-injected electrons are trapped, p.26 detrapping of gate-injected electrons)도 원문 확인.

문헌 인용 값은 "SOURCE_REPORTED — literature-cited statements (not measured by these authors)"로 분리되어 있어, 인용 수치가 저자 자신의 측정으로 제시된 곳은 찾지 못했다(PASS).

**독립 sympy 재유도.** (i) GAA E_IL/E_GBL=(εGBL/εIL)(rb/ra), CAA=(εGBL/εIL)(ra/rb): 기하 인자는 정확히 역수(곱=1), rb/ra=1+t/ra, ra/rb=1−t/(ra+t): PASS. (ii) VFB 단층 비 ln(1+u)/u(u=t/rc)<1, u→0에서 1: PASS. (iii) 순수 trapping의 steady-state ISPP 기울기=1(VT(n+1)−VT(n)=s), 추가 항 ΔP가 있으면 1+ΔP/s: PASS. (iv) 고정 ΔV에서 d ln tBD/d ln tsp=γΔV/tsp>0, 고정 전계에서는 tsp 무관, dm/dtsp=EBD/ΔVWL>0: PASS. "고정 총전압 대 고정 전계" 구분과 plate 영역 한정(V/d를 edge에 쓰지 않음)은 정확하다.

**지적 (i2)**
- **M2-1 (major, 라벨 이동)** 위치: 카드 CLAIM "Charge-trap 3D NAND has reached limits in reliability, power and vertical scaling because of high-field FN operation, ... (cited statement)". 문제: "because of high-field FN operation"이라는 인과는 본문에서 인용 없이 저자가 Fig. 2(b) 논의("the physical bottleneck of NAND scaling arises from the high-field FN tunneling mechanism")로 서술한 것이고, 같은 item의 AUTHOR_INTERPRETATION (a)가 정확히 그렇게 분류했다. 카드가 같은 내용을 "cited statement"로 부르는 것은 라벨 불일치이며 source-fact 어조로의 이동이다. 수정: 카드 CLAIM에서 "because of high-field FN operation"을 분리해 "(authors' interpretation, AUTHOR_INTERPRETATION)"으로 옮긴다(ko/en).
- **M2-2 (major, 출처에 없는 서술; blocker 가능)** 위치: 관찰 (2) "yet on the same page gives 10^3–10^4 cycles for gate-side-injection FeNAND, the type the authors rate most promising". 문제: "the type the authors rate most promising"에 해당하는 문장을 원문에서 찾지 못했다(layout 추출의 "most", "promising" 전수 확인: "promising"은 일반 문맥뿐이며 gate-side injection 유형을 최고로 평가한 문장은 없음). 나머지(p.27 "promising superior endurance", 같은 쪽의 10^3–10^4, p.20의 CTF 같은 범위)는 정확하다. 수정: "the type the authors rate most promising"를 삭제하고 "gate-side-injection FeNAND, the type this section discusses"로 바꾼다(ko/en 동시).
- **M2-3 (major, 참고문헌 제목 기반 추론)** 위치: 관찰 (4)(Citation mapping), 카드 CONTRADICTING DATA의 "title-level mismatches between some citations and statements", tail의 Item 2 (4). 문제: 제목만으로 인용이 진술을 뒷받침하는지를 판단하는 것은 근거가 약하다. 제목 사실(ref 67, 68, 79는 FeFET/FeNAND 논문, ref 39는 negative-capacitance flash 논문, ref 110은 ALD indium oxide 트랜지스터, ref 87은 cylindrical GAA nanowire FET)은 내가 원문 참고문헌에서 확인했으나 원문 논문을 읽지 않았다. item이 "인용이 진술을 못 뒷받침한다고 결론짓지 않는다"고 밝혀 완화되어 있다. 그래도 카드의 CONTRADICTING DATA 행에 "title-level mismatches"가 모순 데이터로 들어간 것은 과하다. 수정: CONTRADICTING DATA에서 해당 구절을 삭제하고 관찰 단락에만 둔다. 관찰 (4) 첫 문장에 "reference titles only; not evidence of misattribution"을 명시한다.
- **m2-4 (minor)** 위치: (i)의 "the field ratio between the inner face of the IL and the outer face of the GBL is ... (εGBL/εIL)(ra/rb) in CAA (IL outside)". 문자 그대로 읽으면 CAA에서 "IL의 안쪽 면과 GBL의 바깥 면"은 같은 계면(rm)이라 기하 인자가 없다(sympy: 비=εGBL/εIL). 식 (ra/rb)는 스택의 두 경계 면(IL의 바깥 면 rb, GBL의 안쪽 면 ra)에서 얻어진다. 결과(정확한 역수)는 맞다. 수정: "E at the stack's inner boundary ra over E at the outer boundary rb"로 면 정의를 GAA와 CAA에서 같게 쓴다.
- **m2-5 (minor)** 같은 단락 마지막 문장 "The same relation is why the channel-side tunnel-oxide field exceeds the blocking-oxide field in production charge-trap VNAND." 곡률 인자는 한 기여일 뿐이고 두께와 유전율 비도 기여한다. "a curvature contribution to why"로 한정한다.
- **m2-6 (minor)** AUTHOR_INTERPRETATION (g)(OS 채널 BTI는 VO와 수소 관련 결함이 원인)는 원문이 [90], [80]을 인용한 서술이므로 인용 서술에 가깝다. 라벨 이동이 보수적 방향이라 위험은 낮다. 필요하면 SOURCE_REPORTED(문헌 인용)로 옮긴다.
- **m2-7 (minor)** ko 카드 CLAIM의 문장 끝 "경로이다."(합니다체 아님) → "경로입니다."

### 3.3 i3 — Jang 외, PAHT (abstract_only, new_this_week)

| 점검 | 판정 | 근거 |
|---|---|---|
| (1) 출처 충실도, 라벨 | PASS (m3-1 표현) | Crossref 초록 전문과 문자 대조 |
| (2) 물리, 기하 | PASS (기하 UNKNOWN 정확) | derive_out.txt |
| (3) 경쟁 메커니즘, 경계 | PASS | 6행 표, 경계 (a)~(d), 순환 아님 |
| (4) DOE | PASS | 기호 수준, 기대 signature와 기각 (a)~(f) |
| (5) 이중언어 | PASS | 35쌍. 표본 6쌍(UNKNOWN 상자, 변수 단락, [4], 카드 ASSUMPTION 등) 이탈 없음 |
| (6) 카드 13행 | PASS | |
| (7) 환각, 내부명, 등급 | PASS | 등급 C, D만 |
| (8), (9) | PASS | new_this_week: Crossref published-online 2026-10-15 |

**초록 대조(Crossref 재조회 전문).** 초록: "...read-retry operations that search for the optimal read reference voltage (VOPT). Read-retry reduces raw bit error rates (RBERs), but it significantly degrades read performance because multiple read iterations are required to complete a single host read request ... (i) VOPT does not need to be updated for a long interval, and (ii) the VOPT offset between wordlines (WLs) is identical across blocks in a chip ... when a read on a given WL succeeds, we record and reuse the VOPT ... we keep only one VOPT per block. For other WLs, we determine the VOPT using a predefined offset table that accounts for process variability in 3D flash memory. Based on comprehensive characterizations using 160 real 3D flash chips, system evaluations show that PAHT improves SSD performance by 58.3% on average by reducing read-retry invocations." SOURCE_REPORTED 단락의 모든 문장이 이 초록에 있다. 160개 chip이 system 평가 문장에서만 나온다는 UNKNOWN 서술, 지표/기준선/workload/실제 SSD 여부 UNKNOWN도 사실이다. "offset table accounts for process variability"를 AUTHOR_INTERPRETATION으로 분류한 것도 적절하다. 기하: 초록에서 "cylind", "channel hole", "radius", "coaxial", "charge-trap", "floating" 일치 0건. item 3의 coaxial 식은 처음부터 "framework, not the paper's model"로 표기되었고 인과 사슬의 r0(w)도 ENGINEERING_INFERENCE 표지가 있다: 기하를 원문의 것으로 읽게 하는 제목이나 표기는 없다.

**독립 sympy 재유도(derive_out.txt).** 오프셋 비용 계수 h·φ(h)/(2Q(h))(h=2에서 2.373216, 3점 모두 차이 <1e-12): PASS. ∂VOPT/∂μa=σb/(σa+σb), ∂VOPT/∂σa=σb(μb−μa)/(σa+σb)²>0: PASS. 동축 retention 자기장 E_T(r0)=ΔVth/{r0[ln(r1/r0)+e·ln(r2/r1)]}, e=εT/εB(직렬 용량 분할로 독립 유도; 수치 차이 <1e-12), planar 극한 ΔVth/(tT+e·tB): PASS. G(x)의 1차 계수 1+x(1+2ea+ea²)/[2(1+ea)]는 sympy 급수와 차이 0(a=tB/tT): PASS. 예: e=0.557, a=2에서 G(0.01)=1.01283, G(2)=2.69204로 단조 증가, G>1. 재사용 간격 t2−t1=(τ/aT+t1)(e^{s/(κA)}−1): PASS. 집단 통계: 상대 표준오차 sqrt(2/159)=0.1122(item "약 0.11"), 1−0.05^(1/160)=0.01855(item "약 0.019"): PASS. 가산 모델에서 block간 WL offset 차이는 0, 곱셈 모델에서는 −κ·g·(Ab−Ab′)(aw−aw,ref)로 g(t)에 비례: PASS.

**지적 (i3)**
- **m3-1 (minor)** 위치: SOURCE_REPORTED "because several read iterations are needed". 초록은 "multiple"이다. 의미는 같으나 SOURCE_REPORTED는 원문 단어에 맞추는 편이 안전하다(synth_notes 11번). 수정: "multiple"로 교체(ko는 "여러 번"으로 이미 중립).
- **m3-2 (minor)** ko 문장 끝 "...변하지 않는다."(합니다체 아님, (ii-b) 정의 문장). "않습니다."로 수정.
- **m3-3 (minor, 기록)** 유도 도구 표기가 "analytic derivation, numerically checked"로 stdlib를 가리키는데, 내가 같은 값을 sympy로 재현했다(위). 표기 변경 불필요.

### 3.4 i4 — Guido 외, Access Rate-Dependent Endurance of HZO capacitors (preprint, new_this_week)

| 점검 | 판정 | 근거 |
|---|---|---|
| (1) 출처 충실도, 라벨 | PASS-WITH-FIXES | 아래 대조. M4-1(제목 라벨) |
| (2) 물리, 기하, 단위 | **FAIL** (B-1) | 나머지 식은 PASS |
| (3) 경쟁 메커니즘, 경계 | PASS-WITH-FIXES | 7개 경쟁 설명과 경계 (a)~(e) 있음. M4-2 |
| (4) DOE | PASS | 기호 수준(tp, td, N, V, T, Vd, 분극 상태, Nw), 대조군 (a)~(d), 기각 기준 (1)~(7) |
| (5) 이중언어 | PASS | 43쌍. 표본 6쌍(변수 단락, (i) 회계 틀, 카드 CLAIM, SOURCE TRACE 등) 이탈 없음 |
| (6) 카드 13행 | PASS | |
| (7) 환각, 내부명, 등급 | PASS-WITH-FIXES | 등급 C, D만(B 사용 없음). preprint 표기 있음. m4-3 |
| (8) 마크업 | PASS | |
| (9) 날짜 | PASS | |

**원문 대조(layout과 raw 두 추출, 문자 대조).** 1963 μm², 30 nm W와 10 nm TiN 하부 전극, 5 nm Hf0.5Zr0.5O2 ALD 300 °C, 10 nm TiN 상부, RTA 500 °C N2, p-type Si, TiOxN1−x 계면층(양쪽), Pr 19.3 μC cm−2 (2×10^6 cycle), 5 μs 사각 pulse ±2 V, PUND 4.6 kHz, 지연 200 ns–200 μs에서 wake-up이 약 10^4 cycle에 완료, Δ2Pr 최대 10–12 μC cm−2 (10^6 cycle), 유전율 34→28.5, 피로 단계 유전율 약 27.5와 누설 불변(Fig. S2), 2 ms 지연 단극/양극 대조(10^6 wake-up, 100 kHz), Fig. 5a는 10^7, 5b는 10^6 wake-up 후, α=2×10^-9 μC^-2 cm^-4와 β=1.7 고정, Table S2의 τ0 98.0/157.1/330.1 ns(표준편차 11.2/25.3/139.1)와 200 ns/2 μs 값 2385.3/613929.1 및 "purely indicative", Table S3의 111.0/79.3/61.8/58.1/53.0 ns, Ea 0.09→0.04 eV(85 °C 부근), V_O 이동 0.5–1.2 eV, HSE06 2.0 eV(Zr)와 2.85 eV(Hf), TiN 전도대 offset 2.3 eV, 이온화 후 약 1.5 eV, drift-diffusion 0.1 C m^-2, "2 ms exceeds the maximum delay for embedded DRAM", Ettissery(원문 철자) 대비: 모두 원문과 일치한다. 1e10 cycle 값이 외삽이라는 서술(Fig. 5a inset)도 확인했다. AUTHOR_INTERPRETATION과 SOURCE_REPORTED의 구분이 대체로 정확하다.
소스박스의 읽기 범위는 pdftotext 전체 + pypdf 구간이라고 적었는데, 나는 pdftotext layout과 raw로 확인했다(같은 도구의 다른 모드). item이 말한 값은 두 추출에서 모두 재현되었다. 식 (1), (2)는 두 추출 모두에서 깨져 있어(raw의 "∆2 ( ) = − ∙ ( / ) , (1)") 형태 UNKNOWN 처리가 옳다.

**독립 sympy 재유도.** 판별 비 (∂Δ/∂lnN)/(∂Δ/∂ln td)=β(임의 G, X=N^β·td/τ): PASS, iso-loss 기울기 −β, wall-clock 시계에서 ∂lnX/∂ln td=td/(td+tp): PASS. 회복형 모델 Δ=−g(N tp)+R(td)에서 ∂Δ/∂ln td=td·R′(td)>0(긴 지연일수록 손실 감소): PASS(sign test 논리 정확). ∫0^θ0 cosθ sinθ dθ=sin²θ0/2: PASS(재구성 (iv)에서 P0 인자 1/2가 [1−a²ln²X] 앞 P0에 흡수된다는 설명이 생략, m4-3). 활성화 에너지: 최소제곱 기울기 Ea(25–85 °C)=0.089969 eV, Ea(85–135 °C)=0.038804 eV(item 0.08997/0.03880): PASS. τ0 감소 배율 157.1/98.0=1.603, 330.1/157.1=2.101(10배 지연당; τ0∝1/td면 10배여야 함): PASS. HSE06 차이 0.85 eV: PASS. 단일층 E(r)=V/[r ln(rout/rin)], 내면에서 최대: PASS(item 4의 동축 서술은 단층, 공간 전하 없음, 축방향 fringe 무시 조건이 명시됨). α와 β 배정: 원문 "α and β fixed to 2⋅10-9 µC-2 cm-4 and 1.7, respectively" 그대로(α=2×10^-9, β=1.7): PASS.
**Einstein 드리프트**: 원문 D=10^-10~10^-12 cm²/s, z=2, 300 K, 1 MV/cm에서 v=zqDE/(kBT)는 D=10^-12일 때 **7.736×10^-7 m/s**(item 7.74e-7 일치), D=10^-11일 때 7.7×10^-6, D=10^-10일 때 7.7×10^-5이며, 2 ms 이동 거리는 각각 1.55, 15.5, 155 nm. 원문이 쓴 드리프트 범위 10^-5~10^-4 m/s는 D≈10^-11~10^-10에 해당한다. 따라서 7.74e-7을 원문의 하한 10^-5와 비교하면 비는 12.9배, 즉 **약 1.1 decade 아래**이지 "two decades"가 아니다(10^-4와 비교하면 2.1 decades). 반면 "원문 속도로 2 ms 동안 20–200 nm 이동"은 정확하다(10^-5 m/s×2 ms=20 nm).

**지적 (i4)**
- **B-1 (blocker; 수치/물리 오류, 수정 쉬움)** 위치: i4 관찰 (4) "gives a drift velocity of 7.74 × 10^−7 m/s, two decades below the stated lower bound of 10^−5 m/s (sympy)"(ko 동일)와 report_tail "Item 4 ... (4) The lower end of the cited diffusion-coefficient range gives a drift velocity two decades below the stated lower bound". 문제: 위 재계산에서 7.736e-7 대 1e-5는 log10(12.93)=1.11 decades다. "two decades"는 틀린 크기이며, "(sympy)" 표시가 붙어 있어 검증된 값처럼 읽힌다. 수정: "about one decade (a factor of about 13) below the stated lower bound of 10^-5 m/s; about two decades below the upper bound 10^-4 m/s"로 고치고 ko와 tail 문장(ko/en)도 같이 고친다. 또한 "D의 두 자릿수 범위(10^-12~10^-10)는 속도 두 자릿수에 대응하는데 원문의 속도 범위는 한 자릿수(10^-5~10^-4)만 쓰므로, 원문 속도는 D≈10^-11~10^-10과 일치한다"를 한 문장 추가하면 모순의 크기가 정확히 전달된다.
- **M4-1 (major, item 수준 추론이 제목에 사실처럼 들어감)** 위치: h2 "...the delay acts as stress, not rest, and the 10^10-cycle curve is a fit extrapolation" 및 ko 제목. 문제: "the delay acts as stress, not rest"는 item의 sign test (iii)의 추론이다. 같은 (iii)가 "sign alone does not show recovery is absent: coexisting recovery and dominant stress give the same sign"이라고 쓰고, 원문은 이 결론을 말하지 않는다(원문은 delay-dependent loss를 전자 방출에 의한 양전하 축적으로 설명). 제목만 읽으면 SOURCE 주장으로 읽힌다. 수정: "...: in this stack the delay acts as net stress rather than net recovery (this report's sign-test inference), and the 10^10-cycle curve is a fit extrapolation"로 쓰거나 제목에서 해당 절을 빼고 (iii)에만 둔다. 엄격히는 블로커가 될 수 있다(제목에 인용 부호도 라벨도 없음).
- **M4-2 (major; blocker 가능, 교차 비교의 부호 서술)** 위치: i4 카드 "Change vs archive"의 "It adds an access-rate dependence of opposite sign to W40 item 5 (higher SiC PWM frequency, longer TDDB life ...)", 표 행 W40 item 5의 "In HZO capacitors the opposite sign is reported: a lower access rate (longer off interval) gives more loss", "Updated position"의 "lifetime effects of opposite sign in two devices", 그리고 tail 매트릭스 행 2의 "Tension" 열 "the same word 'de-trapping' explains lifetime effects of opposite sign". 문제: 두 보고값을 그대로 놓고 보면 방향이 같다. W40 item 5(Yan 외): PWM 주파수가 높을수록 TDDB 특성수명 증가(DC가 최저, 시간 회계와 duty D(f)는 UNKNOWN). 본 item: 같은 cycle 수에서 접근률이 낮을수록(지연이 길수록) 2Pr 손실이 크다. 즉 둘 다 "낮은 rate가 더 나쁘다"이다. 반대인 것은 (a) 저자들이 제안한 de-trapping의 역할(SiC는 OFF 구간의 fast-trap de-trapping이 수명을 늘림, HZO는 전자 방출이 손실을 늘림), (b) DC/연속 stress 기준에 대한 OFF 시간의 효과(SiC는 OFF가 이득, HZO는 지연이 손해) 정도이며, 비교 기준(equal N 대 wall-clock 또는 stress time UNKNOWN)이 달라 "rate 의존성의 부호"는 비교가 성립하지 않는다(UNKNOWN). 수정: "opposite sign" 문구를 "the same direction of rate dependence (lower rate/frequency is worse), but the authors' proposed role of de-trapping is beneficial in SiC and harmful in HZO, and the comparison bases (equal N vs wall-clock/stress time UNKNOWN) differ"로 바꾼다. 결론(de-trapping이라는 말이 메커니즘을 고정하지 못한다)은 유지된다. 매트릭스 행 2의 "Updated position"과 head 요약 (4)는 영향이 없다.
- **m4-3 (minor)** 위치: (iv) "giving P = P0[1 − a² ln² X]". ∫=(1−cos²θ0)/2이므로 앞 인자는 P0/2다. "P0를 재정의"한다는 말을 추가하거나 "P ∝ [1−a²ln²X]"로 쓴다. 관찰 (2)의 "numeric probe in the notes"도 내부 노트 참조이므로 삭제한다(m1-4와 같은 종류). "sympy" 소문자 표기는 "SymPy"로 통일.
- **m4-4 (minor)** 위치: "New vs known"과 인용 설명. item이 "Already known"으로 적은 "internal field from charged defects that move during the delay ([23]–[25], [27])"은 원문 Sec. 2의 "Some reports ascribe ... greater internal electric field originating from charged defects migrating"와 일치한다. 다만 원문 서론은 같은 [23–25,27]을 "domain wall pinning by defects generated and redistributed during the delay"로도 서술하고, 저자들은 "nucleation inhibition rather than domain wall pinning"이라고 쓴다. item의 경쟁 설명 (3) domain-wall pinning은 이 서론 문장을 인용하면 더 정확하다. 수정은 선택.
- **m4-5 (minor)** 위치: NAND 관련성 상자 "it is widely discussed in reliability practice (background knowledge; primary sources not checked for this issue) that changing the rest interval between cycles can change the outcome, usually understood as rest giving detrapping recovery." 출처 없는 일반 진술이다. 매트릭스 행 2의 "Prior simplification: Off time = recovery"의 근거가 이 문장이다. 수정: ENGINEERING_INFERENCE(근거 미확인)로 표지하거나 "Prior simplification"의 출처를 W40 item 5(저자 해석)로 한정한다.

### 3.5 i5 — Chen 외, AOS CSC 구조 (preprint, new_this_week)

| 점검 | 판정 | 근거 |
|---|---|---|
| (1) 출처 충실도, 라벨 | PASS | 아래 대조 |
| (2) 물리, 기하, 단위 | PASS (m5-3 표기) | derive_out.txt |
| (3) 경쟁 메커니즘, 경계 | PASS | 6개 경쟁 해석, 창 경계, 기하 경계 |
| (4) DOE | PASS | 구조 S1~S4(기호 수준), F1~F6 각각 기각 기준, 대조군 |
| (5) 이중언어 | PASS | 43쌍. 표본 6쌍(소재/기하 경계, 변수, F1~F3 기각 기준, 카드 CLAIM 등) 이탈 없음 |
| (6) 카드 13행 | PASS | |
| (7) 환각, 내부명, 등급 | PASS-WITH-FIXES | 등급 C, D만. preprint 표기 있음. 도구 표기 불일치 M5-1, 라벨 m5-2 |
| (8) 마크업 | PASS | |
| (9) 날짜 | PASS | submitted 2026-10-12 09:03:22 UTC = KST 18:03, window 안 |

**원문 대조(layout과 raw 두 추출).** 30 nm Ni 게이트, p+ Si, 100 nm SiO2, 6 nm HfO2 열 ALD와 N2 400 ℃ 30 min, 4.5 nm IGZTO(Ar, 실온 스퍼터), Ni/W/Pt S/D의 역할 서술, O2 400 ℃ 1 h, 5 μm overlap margin, SS 약 63.6 mV/dec, 히스테리시스 약 4.7 mV, drain floating 시 depletion 용량이 S/D 단락의 약 절반, 400/900 μm²와 유효 약 600 μm², 1 kHz 성분이 DC 누설의 bias 의존을 따르고 약 1/f, 100 kHz 위에서 무시, fpeak와 1/Rtotal의 선형 상관, W=10 μm에서 L을 늘리면 추가 peak, 광학 bandgap 3.839 eV와 EC−EF 약 0.283 eV, depletion 9–12×10^11 eV^-1cm^-2와 약 250 ns, 약 0.3 eV 표면전위 변조, 10^18–10^19 eV^-1cm^-3, 강한 accumulation 2.8–3.1×10^12, "approximately threefold", L=5 μm W=80/50 μm, Fig. 9(d) 캡션의 "without RC correction": 모두 원문과 일치한다. 초록 대 본문 불일치 관찰 (1)~(4)도 원문에서 확인된다(초록 "associated with donor-like states", "identified and calibrated", "increased state quantity" 대 본문 "possible donor-like", "needs rigorous equivalent-circuit model", 비단조). 관찰 (4)의 "initially increases with VG and subsequently decreases with frequency" 문장도 원문 그대로다.

**독립 sympy/mpmath 재유도.** f_peak=1/(2πτ)=636,620 Hz(τ=250 ns), 1 MHz에서 ωτ=1.5708, 1 kHz에서 1.571e-3: PASS. 단일 준위 Gp/ω가 ωτ=1에서 높이 0.5, 연속(ln(1+ω²τ²)/(2ωτ)) 형이 ωτ=1.9803에서 높이 0.40237: PASS. 연속형 τ=250 ns의 peak 주파수 1.2607 MHz(item "약 1.26 MHz, 창 밖"): PASS. D3 환산 4.5×10^11~4.5×10^12 eV^-1cm^-2: PASS. D4 비 2.333~3.444: PASS. D5 분산 RC(양단 구동) 정규화 Gp/ω가 x=ωRsh Cox (L/2)²≈2.54에서 최대, 작은 x에서 Re[√(jx)tanh√(jx)]/x→x/3(급수 y−y²/3, y=jx): PASS(f∝1/(Rsh Cox L²), L 2배면 1/4). 동축 Cs 비 u/ln(1+u)≈1+u/2: PASS. 환형 채널 부피 비 tch(1−v/2): PASS. 입방 입자 경계 면적/부피 3/d: PASS. **보고서 수준 항등식**: u/ln(1+u)와 ln(1+u)/u는 정확히 역수(곱=1): PASS(단층, u=그 층 두께/내반경으로 맞출 때). 작성자 스크립트 i5_sympy.py도 같은 환경에서 exit 0으로 같은 값(0.4023712, 1.26069e+6 Hz, x=2.54065)을 출력했다.

**지적 (i5)**
- **M5-1 (major, QC 서술 불일치)** 위치: item 5의 상자 제목 "ENGINEERING_INFERENCE — derivation checks (Python standard library; the pinned SymPy environment was unavailable for this item)" 및 report_tail QC "Derivations ... numeric checks with the Python standard library (items 3 and 5, as stated in those items)". 문제: i5_notes.md는 SymPy로 다시 돌렸고 HTML이 "SymPy-checked"로 바뀌었다고 쓰며(48행), i5_sympy.py가 실제로 존재하고 내가 같은 venv로 실행해 같은 값을 얻었다. 즉 현재 HTML의 "SymPy 환경 사용 불가"는 사실이 아니다(패치 유실 의심). 어느 쪽이든 결과 수치는 sympy로 재현되므로 내용 오류는 아니고 QC 진술 오류다. 수정: i5 상자 제목을 "(SymPy 1.14.0; script re-run)"로 바꾸고, tail QC를 "symbolic checks with SymPy (items 1, 2, 4, 5); numeric checks with the Python standard library (item 3)"로 고친다(ko/en).
- **m5-2 (minor)** 위치: DOE "Test structures. (S1) ... (S2) ... (S3) ... (S4)". S1–S4가 item 4의 Supporting Information S1–S4와 글자가 같고, 내부 출처 번호(S1~S5)와도 같다. 수정: "T-A ... T-D" 또는 "Structure A–D"로 바꾸고 본문 안의 "S1/S2/S3" 참조도 함께 바꾼다.
- **m5-3 (minor)** 위치: F1 "an RC peak follows fpeak ∝ 1/(R·L²)". R이 정의되어 있지 않고, R이 총 저항이면 R∝L이라 1/L³가 된다. D5의 Rsh를 써서 "fpeak ∝ 1/(Rsh·Cox·L²)"로 쓴다.
- **m5-4 (minor, 라벨 충돌)** 유도 D1–D7과 가교 B1–B6이 등급 문자 D, B와 겹친다(item 1의 D1–D4와 같은 문제). tail이 "(B1)–(B6)"을 인용할 때 등급과 혼동될 여지는 문맥으로 제한된다. 선택적으로 "bridge 1–6", "derivation 1–7"로 쓴다.

## 4. report_head / report_tail

| 점검 | head | tail | 근거 |
|---|---|---|---|
| 증거 배너의 정직성 | PASS | PASS | 5건 중 4건 full text, item 3은 초록만, 그림 미열람, 깨진 식은 UNKNOWN, item 1 Eq.(1) 부호는 글리프 매핑 한 판과 공통 본문에 근거, 403 미우회, 독립 물리 검수 PENDING, 페이지 단위 시각 점검 미수행을 모두 정확히 기술한다. 내가 확인한 사실과 충돌 없음(단 M-H-1의 등급 서술) |
| 형상을 항목별로 기술, 불명 항목이 동축처럼 읽히지 않는가 | PASS | PASS | head Topical scope와 tail Geometry, item by item: item 1과 3은 UNKNOWN(내가 원문에서 cylind, channel hole, radius 0건 확인), item 2는 1D flat-band, item 4와 5는 planar. 제목에 불명 형상을 동축으로 읽게 하는 표현 없음. i1 소제목도 "(cell geometry in the source: UNKNOWN)"로 한정 |
| QC 진술 | PASS-WITH-FIXES | FAIL (M-T-1) | 아래 |
| 가설 H1~H8: 예측 signature, 반증 기준, 등급 D | — | PASS-WITH-FIXES | 8개 모두 signature, falsification, 등급 D 표시. H7과 H8은 "own cross-constructions ... do not appear in that form in any item's DOE"로 선언. 지적 M-T-2, m-T-5 |
| 모순 매트릭스 | — | FAIL (B-1과 M4-2 전파) | 7행 |
| 이중언어 | PASS | PASS | head 22쌍, tail 85쌍. 표본 11쌍(head 배너, 선정 분류, 주제 범위, 등급 요약 행; tail item 1과 3, 매트릭스 행 3, H1 signature, H3 signature, 관찰 단락, 소스 [4]) 의미 이탈 없음. 합니다체 위반 0 |
| 마크업, 클래스, 내부명 | PASS | PASS | mech_out.txt |

**독립 확인.** 매트릭스 행 5와 head 기호 단락의 항등식(item 5의 u/ln(1+u)와 item 1, 2의 ln(1+u)/u는 단층에서 정확히 역수)은 sympy로 PASS(곱=1). "참조 반경과 층 구조가 다르므로 정의를 맞추라"는 단서도 정확하다. "shared" 서술 점검: item 1과 3의 "같은 관측량"은 Δμ(상태 평균 이동)와 VOPT(오류율 최소 read level)를 구분해 두었고(VOPT는 폭에도 의존, item 3 유도) 데이터 공유가 없다고 명시한다. item 4와 1의 "fitted parameter의 온도 의존성"은 재료와 저장 원리가 다르다고 한정했다. 과장된 shared claim은 찾지 못했다(M4-2의 "opposite sign" 제외).

**지적 (head/tail)**
- **M-H-1 (major)** 위치: head Labels and grades의 "...and to the SSD latency figures as simulator results (not drive measurements)". M1-1과 같은 문제이며 수정도 같다. 같은 단락의 "Grade B is used only in item 1" 문장은 수정 후에도 참이다.
- **m-H-2 (minor)** 위치: head 배너 "An independent physics review has not yet been performed (PENDING)", tail QC "Physics independent review PENDING: not performed", "independent check PENDING", "independent review PENDING". 이 검수가 수행되었으므로 "performed 2026-11-10; blocker 1, major N found; fixes pending 또는 applied"로 사실대로 쓰고, 재검수 통과 전에는 PASS로 바꾸지 않는다.
- **m-H-3 (minor)** 위치: head 배너 "full-text single-source analysis"와 tail Issue grade. "single-source"가 항목당 하나의 출처라는 뜻임을 풀어쓴다(두 번 읽은 것과 혼동 방지).
- **B-1 (blocker, tail)** 위치: tail "Source inconsistencies observed on reading"의 Item 4 (4) "The lower end of the cited diffusion-coefficient range gives a drift velocity two decades below the stated lower bound ..."(ko/en). 3.4의 B-1과 동일하며 "about one decade (a factor of about 13)"로 고친다.
- **M4-2 (tail 행)** 위치: 매트릭스 행 2의 W42/archive evidence 열과 Tension 열("lifetime effects of opposite sign"). 3.4 M4-2의 수정을 적용한다.
- **M-T-1 (major)** 위치: tail QC "Derivations: Symbolic checks with SymPy (items 1, 2, 4); numeric checks with the Python standard library (items 3 and 5, as stated in those items)". i5 표기가 낡은 것이므로(M5-1) item 5를 SymPy로 바로잡으면 "items 1, 2, 4, 5는 SymPy, item 3은 stdlib"이어야 한다. item 3의 stdlib 점검은 내가 sympy로 재현해 일치를 확인했다.
- **M-T-2 (major, 라벨 반전)** 위치: H3 "The inter-WL VOPT offset is equal across blocks at one data age (ii-a) but changes with data age (ii-b), faster at WLs of smaller hole radius."와 같은 행의 반증 기준 "Rejected if the offset does not change by more than the tolerance s ..., since (ii-b) then holds." 문제: i3는 (ii-b)를 "offset이 age, cycle, 온도에 따라 변하지 않는다"로 정의한다. 가설 문장은 (ii-b)를 반대 명제(변한다)에 붙였고, 반증 문장은 i3의 의미로 썼다. 한 행 안에서 라벨이 뒤집혀 독자가 반증 조건을 거꾸로 읽을 수 있다. 수정: 가설 문장을 "...equal across blocks at one data age (ii-a) but not constant in data age (the negation of ii-b), faster at WLs of smaller hole radius"로 쓴다(ko/en).
- **M-T-3 (major, 중복과 경로 충돌; 조정자 결정 필요)** 위치: tail QC "Duplicate check PASS for what was checked ... published reports (W37–W40 and W43) and the used-source ledger ... Scope limited to those two". 이 범위 서술은 정직하다. 그러나 내가 git grep으로 origin 브랜치에서 5개 식별자를 찾은 결과 다음을 확인했다. 원격 브랜치 origin/reliability-w42(커밋 f216e46, 2026-10-12, "W42 statistical reliability note")에 이미 reports/2026/w42/index.html이 있고, 그 안에서 item 1의 논문(DOI 10.1587/elex.23.20260379)을 다룬다. 같은 브랜치의 models/w42_cross_temperature.json도 같은 DOI를 source로 둔다(origin/main보다 9개 파일 앞섬, merge 안 됨). 또 origin/main의 audit/2026/w43/rejected.md에 item 3(10.3390/eng7100563)과 item 4(arXiv 2610.20154)가 "reserve only"로 올라 있다(synth_notes 19번과 일치, 단 item 1은 "unverified hint"가 아니라 확인된 중복이다). 게시 경로 reports/2026/w42/와 item 1 논문이 그 브랜치와 겹친다. 수정: QC 중복 검사 문장에 "an earlier unpublished W42 draft already covers item 1's paper"라는 사실을 쓰고(공개 HTML에 브랜치 이름은 쓰지 않는다), 게시 전에 그 브랜치를 닫거나 이름을 바꾸는 결정을 내린다. 결정 없이 게시하면 경로 충돌과 중복 보고가 생긴다. 이 결정은 본 검수의 범위 밖이다.
- **m-T-4 (minor)** 소스 [1]의 제목이 title case인데 Crossref와 J-STAGE 페이지는 sentence case다. 원문 표기대로 쓴다(synth_notes 7번).
- **m-T-5 (minor)** H8: 예측 signature의 "positive for rest in the programmed state"의 부호 근거가 설명되지 않았고, "with radius splits the effect is larger at smaller radius"에 대응하는 반증 기준이 없다(반증 절은 stored state와 trest만 다룸). 수정: 반경 절의 반증 기준(반경 분할에서 효과의 크기가 반경과 무관하거나 반대 방향이면 G(x) 연결을 기각)과 programmed 상태에서 양의 부호를 예측하는 이유 한 문장을 추가한다. 등급 D와 cross-construction 선언은 정확하다.
- **m-T-6 (minor, 형식)** 항목 제목 태그: i1, i2 제목에는 "[archive_gap]"이 있고 i3~i5 제목에는 분류 태그가 없다. 기능상 문제 없음, 선택적 통일.

## 5. 항목 간 일관성

1. **부호 서술(M4-2)**: item 4와 tail 매트릭스 행 2를 같이 고친다. head 영향 없음.
2. **참고문헌 제목 기반 추론이 두 항목에 반복**(M1-2, M2-3, tail Item 2 (4)): 한 가지 규칙(제목만 읽은 것은 근거로 쓰지 않거나 별도 표기)으로 통일한다.
3. **등급 B**: 실제 사용은 item 1 하나이고, 수정(M1-1) 후에도 item 1의 측정 선형성과 보상 효과만 남는다. 다른 항목은 C, D만이므로 head 문장과 일치한다.
4. **기호 충돌**: head가 β, τ, σ, C, L, D는 공개했다. 추가로 item 3의 G(≡E_T,coax/E_T,planar)와 item 4의 일반 함수 G(X), 라벨 C1/C2, D1–D7, B1–B6, S1–S4는 head에 없다(m1-5, m5-2, m5-4). 한 줄 추가를 권한다.
5. **도구 서술**: item 5와 tail QC가 어긋난다(M5-1, M-T-1). item 3은 stdlib라고 정직하게 썼다.
6. **날짜와 분류**: item 1 archive_gap(08-25 online, 09-25 issued), item 2 archive_gap(2025-12-17), item 3, 4, 5 new_this_week가 head, 각 item, tail, sources에서 모두 같다(문자 대조).
7. **형상 서술**: head, tail, 각 item 박스가 같은 사실을 말한다. item 1과 3 UNKNOWN, item 2 1D, item 4와 5 planar.
8. **preprint 표기**: item 2(arXiv-only Perspective), 4, 5 모두 동료 심사 전이 head, tail, item 박스에 있다.

## 6. synth_notes.md의 19개 불일치 검증

| # | 내용 | 현재 텍스트 확인 | 조치 |
|---|---|---|---|
| 1 | i5 도구 라벨과 notes | 확인됨(i5.html은 stdlib, notes는 SymPy, i5_sympy.py 존재, 내 재실행 exit 0) | M5-1, M-T-1 |
| 2 | item 3 stdlib | i3는 numerically checked 유지. 내가 sympy로 재현해 일치 | 없음 |
| 3 | manifest의 비척도 등급 | 공개 HTML에는 A–D만 있음(A-, B- 0건) | 없음 |
| 4 | item 1의 SSDsim B | 확인됨 | M1-1 |
| 5 | C1/C2 충돌 등 | 확인됨(i1 derivation C2) | m1-5, m5-2, m5-4 |
| 6 | 항목에 H 번호 없음 | grep 0건 | 없음 |
| 7 | 제목 대소문자 | 확인됨(tail [1]) | m-T-4 |
| 8 | 제목 태그 불균일 | 확인됨 | m-T-6 |
| 9 | item 4 제목 해석성 | 확인됨 | M4-1 |
| 10 | 참고문헌 제목 추론 | i1, i2 확인됨 | M1-2, M2-3 |
| 11 | several과 multiple | 확인됨 | m3-1 |
| 12 | ℃ 글리프 | 원문도 ℃를 씀(원문 확인). 일관성만의 문제 | 선택 |
| 13 | sympy와 SymPy | item 4가 소문자 | m4-3 |
| 14 | 읽기 범위 숫자 차이 | 내용 공백 아님. 정확한 문자 수는 내 추출과 달라 UNKNOWN | 없음 |
| 15 | manifest F6 오독 위험 | 공개 HTML에 해당 표현 없음 | 없음 |
| 16 | manifest 추론이 사실로 | item 3은 해당 문구 미사용, ENGINEERING_INFERENCE로만 서술 | 없음 |
| 17 | item 3 접근일 | 403은 우회 금지 지시에 따라 내가 재시도하지 않았다(403 재현은 UNKNOWN). Crossref 초록은 내가 재조회 | 없음 |
| 18 | 단위 | item 1 Tco 단위 UNKNOWN(V/K 차원 추정은 라벨됨), item 4 τ0 ns 표기는 원문 Table S2 헤더 "τ0 (ns)" 확인 | 없음 |
| 19 | 중복 기록 | origin/reliability-w42에 item 1 논문이 이미 있음을 확인(unverified hint가 아님) | M-T-3 |

## 7. UNKNOWN (내가 확인하지 못한 것)

- arXiv Atom API(item 2, 4, 5): 4회 시도 모두 HTTP 429. 같은 내용을 arXiv 초록 페이지와 DataCite로 확인했으므로 서지 일치 판정은 유지하되, "arXiv API로 일치"라는 QC 문구는 내 재현으로는 확인하지 못했다.
- item 1 advance판 PDF(Algorithm 1의 5개 program 온도 목록, Table I의 CTDVT/Ideal 행, "Vol.21 No.1, 2024" 머리글): 내 접근에서는 다시 받지 못했다. copyedit판 두 추출에는 해당 행이 없음만 확인.
- item 3의 MDPI 본문 HTTP 403: 우회 금지 지시에 따라 접근하지 않았다. 본문, 표, 그림은 아무도 읽지 않았다.
- 모든 그림 이미지(item 1 Fig. 1~5, item 2 Fig. 3, 4, item 4 Fig. 1~5, item 5 Fig. 1~10): 나도 읽지 않았다. item 2 Fig. 3 식과 item 4 식 (1), (2), (S24)–(S36)은 두 추출 모두 깨져 형태 UNKNOWN이 맞다.
- item 2의 인용 원문(refs 21, 22, 25 등)과 item 4의 인용 원문(Ettissery 등): 읽지 않았다. 이 문서의 모든 "인용 일치"는 원문(Perspective, 논문)의 인용 번호 대응뿐이다.
- arXiv 공지(announcement)일: 확인하지 못했다.
- 작성자 노트에 적힌 정확한 읽기 범위(문자 오프셋)는 내 추출과 오프셋이 달라 재현하지 못했다. 수치와 문장 단위로만 대조했다.

## 8. 수정 요구 요약 (우선순위)

1. [blocker] B-1: i4 관찰 (4)와 tail Item 4 (4)의 "two decades" → "about one decade (a factor of about 13)" (ko/en 4곳).
2. [major, blocker 가능] M2-2: i2 관찰 (2)에서 "the type the authors rate most promising" 삭제. M4-2: "opposite sign" 서술 교정(i4 카드와 표, tail 행 2).
3. [major] M1-1(+M-H-1): SSDsim 등급을 C로, head 문구 정리. M1-2, M2-3: 참고문헌 제목 기반 추론 정리. M2-1: i2 카드 CLAIM의 인과 라벨 이동. M4-1: i4 제목의 해석 표지. M5-1(+M-T-1): item 5와 tail의 SymPy 도구 서술. M-T-2: H3 라벨 반전. M-T-3: 중복 브랜치 사실 반영과 게시 경로 결정.
4. [minor] m1-3~m1-6, m2-4~m2-7, m3-1~m3-3, m4-3~m4-5, m5-2~m5-4, m-H-2, m-H-3, m-T-4~m-T-6.

수정 후에는 mech_checks.py와 derive_checks.py를 다시 실행하고(결과 파일 mech_out.txt, derive_out.txt와 비교), B-1의 새 문구가 sympy 값(비 12.93, 1.11 decades)과 일치하는지 확인해야 한다. 수정 전 본문은 건드리지 않았다.
