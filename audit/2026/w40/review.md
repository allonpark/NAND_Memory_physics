# W40 섹션 s1~s5 독립 검수 (nand-physics-critic)

검수일: 2026-10-21 / 검수자: 작성자(Opus)와 다른 모델 / 섹션 파일은 수정하지 않음.
모든 PASS는 실행한 스크립트 또는 문자 단위 비교 근거를 적었다. 확인하지 못한 항목은 UNKNOWN으로 남겼다.

## 0. 총평

| 섹션 | 판정 | blocker | major | minor |
|---|---|---|---|---|
| s1 (ISTFA p0151) | PASS-WITH-FIXES | 0 | 2 | 7 |
| s2 (ISTFA p0478) | PASS-WITH-FIXES | 0 | 1 | 8 |
| s3 (ERX aea754) | PASS-WITH-FIXES | 0 | 0 | 5 |
| s4 (Sensors 6254) | PASS-WITH-FIXES | 0 | 3 | 7 |
| s5 (JPhysD ae9c4e, archive-gap) | **FAIL** | **1** | 2 | 5 |

blocker 목록 (수정 전 게시 불가):
- **B1 (s5-1)**: s5가 "lifetime 증가를 fast g(τ) cluster와 정량적으로 연결"했다고 SOURCE_REPORTED로 서술한다. 초록의 정량 상관은 **slow-trap filling-rate ratio**와 lifetime ratio 사이다. fast trap de-trapping은 저자가 제안한 물리적 기원(proposed origin)일 뿐이고, drift 약 30% 감소는 그 정성 근거다.

물리 부호·기하·차원 오류는 5개 섹션 모두에서 발견하지 못했다(아래 근거 참조).
SOURCE_REPORTED 문장 가운데 초록에 없는 사실은 B1 하나다. s4(저전압, both/particularly)와 s2(multi-block signature)는 서술 강도가 초록보다 높아 major로 분류했다. 엄격하게 적용하면 blocker로 올릴 수 있으므로 조정자가 판단해 달라.

## 1. 수행한 검수와 근거 파일

모든 파일은 `...\scratchpad\w40\review\`에 있다.

| 파일 | 내용 |
|---|---|
| `fetch.py`, `fetch_out.txt`, `cr_S1..S5.json` | Crossref API(`api.crossref.org/works/<DOI>`)에서 5건을 직접 재조회했다. 제목, 저자, 날짜, 권/호/쪽, 초록 전문이 들어 있다. |
| `markup_check.py`, `markup_out.txt` | 태그 균형, `assets/style.css` 클래스 대조, ko→en 인접성 검사. |
| `cardcheck.py` | 9필드 카드와 라벨 개수 검사. |
| `numtrace.py` | 각 섹션의 모든 숫자 토큰 추출. |
| `indep_checks.py`, `indep_checks_out.txt` | sympy 1.14.0 독립 재유도 (S1~S5 식). |
| `s3_numeric.py`, `s3_numeric_out.txt`, `s3_sample.py`, `s3_sample_out.txt` | S3 다층 동축 계수의 40자리 수치 검증과 20만 점 무작위 표본 검사. |
| `pagefetch.py` | 출판사 페이지 재확인 시도. 결과는 아래 UNKNOWN 참조. |

UNKNOWN: ASM(S1, S2)과 MDPI(S4)는 HTTP 403을 반환했고, IOP(S3, S5)는 bot-manager 챌린지 페이지로 리다이렉트됐다. 따라서 "PDF subscriber-only", "poster", "revised 5 Sep", "data not public per publisher page", "ASM 페이지에서 확인"이라는 서술은 독립 재현하지 못했다. 이 서술들은 manifest 의존이다.
S4의 "MDPI 본문 HTTP 403"은 내 요청에서도 403이 나와 일치했다.

## 2. 서지·날짜 점검 (Crossref 직접 대조, 전 섹션)

| 항목 | s1 | s2 | s3 | s4 | s5 |
|---|---|---|---|---|---|
| 제목 일치 | PASS | PASS | PASS | PASS | PASS |
| 저자 일치 | PASS (given "Lito De La", family "Rama") | PASS (6명) | PASS | PASS ("Ayoub El"+"El Abdi"의 concat이 "Ayoub El El Abdi"가 된 것을 s4가 설명함) | PASS |
| 권/호/쪽 | 151–156 PASS | 478–480 PASS | 8(19) 195322 PASS | 26(19) 6254 PASS | 59(37) 375105 PASS |
| 날짜 | published 2026-10-04 PASS | 2026-10-04 PASS | epub 2026-10-01 PASS | 2026-10-02 PASS | 2026-09-18 PASS |
| W40 창(2026-09-28~10-04) 내부 | 예 | 예 | 예 | 예 | **아니오 → archive_gap 맞음** |

- 중복 점검: main 브랜치의 `reports/`, `knowledge/`, `index.html`에서 5개 DOI 문자열을 grep했고 모두 0건이었다 (PASS). W41/W42 브랜치와의 중복은 확인하지 않았다 (UNKNOWN).
- **sources.yaml 오류 확정**: S5 `selection_class` 주석의 "published 4 days before window start (2026-09-22)"는 틀렸다. 올바른 값은 창 시작 2026-09-28이고 게재는 2026-09-18이므로 **10일 전**이다. 2026-09-18은 W38 창(09-14~20)에 속한다. s5.html 본문은 이 오류를 복제하지 않았다 (PASS, "W40 window(2026-09-28–10-04) 이전인 2026-09-18").
- Crossref `created`/`deposited` 값은 s1과 s2가 2026-09-30/2026-10-06, s5가 2026-08-20/2026-09-18이다. s1 본문의 "Crossref deposit 2026-09-30"은 `created`를 `deposit`이라 부른 용어 오류다 (s1-5).
- Crossref 부가정보: S1·S2 모든 저자의 소속은 "Sandisk Technologies Inc., Milpitas"다. S3의 assertion은 received 2026-07-15, accepted 2026-09-14, epub 2026-10-01이다. s3.html의 "revised 5 Sep"은 Crossref에 없다 (s3-2). S5의 assertion은 received 2026-04-12, accepted 2026-08-20, epub 2026-09-18이다. S4의 license는 CC BY 4.0이다 (s4 본문과 일치, PASS).

## 3. 공통 점검 결과

**(8) 마크업**: `markup_out.txt` 기준으로 5개 섹션 모두 태그 불일치 0건, 미종료 0건, inline style 0건, script 0건이다. 사용 클래스는 모두 `assets/style.css`에 존재한다 (boundary, chain, compare, doebox, eq, inference, label, sourcebox, pass, pending, qc, tag). 모두 PASS. 섹션 id는 i1~i5로 W39 규칙과 같다.

**(5) 이중언어 구조**: `<p lang="ko">` 직후 `<p lang="en">` 인접성 위반이 0건이다 (s1 9쌍, s2 25쌍, s3 11쌍, s4 10쌍, s5 12쌍). PASS. 표 셀과 h3 제목은 한 언어만 쓰거나 slash로 병기되어 쌍 구조가 아니다 (cross-6).

**(6) 9필드 카드**: CLAIM, EVIDENCE, MODEL, VALID RANGE, ASSUMPTION, CONTRADICTING DATA, CRITICAL BOUNDARY, CONFIDENCE, SOURCE TRACE가 5개 섹션 모두에 있다 (`cardcheck.py`, 누락 0). 추가 필드(Competing mechanisms, Electrical signatures, Failure modes, Change vs archive)도 모두 있다. 단 s5는 "Change vs archive"가 카드 안이 아니라 별도 h3 표다.

**(7) 날조 점검**: 숫자 토큰을 `numtrace.py`로 추출해 하나씩 대조했다.
- 초록에서 온 숫자: s3의 3–5×10¹⁹, 4–5 nm, ≤15%, 10 yr, >50 nm. s4의 180 nm, 140 K. s5의 1.2 kV, 150 °C, 100 kHz, 4.1–4.7, 0.7 ms, 0.5–50 s, 약 30%.
- 라벨된 유도값: 3.33, 2√3, 3.46/1.89/0.99/0.72, 1/150, 0.21–0.24, 0.518/0.502, 1.49.
- 추적 불가 숫자: s4의 "140–300 K"에서 **300 K** (초록은 room temperature라고만 말함, s4-6).
- Weibull 파라미터, 곡선, 제품 수치의 날조는 없다. DOI도 5건 모두 Crossref에서 해석되며 제목이 일치한다. W37/W39 참조 DOI(10.1109/TED.2026.3665857, 10.1049/pel2.70286)는 repo의 W37/W39 index.html 본문과 일치한다. 기밀·제품 수치도 없다. 모두 PASS.

## 4. 섹션별 상세

### s1 — 판정: PASS-WITH-FIXES

(1) 출처 충실도: PASS. SOURCE_REPORTED 3건을 Crossref 초록과 대조했다.
- (a) 초록 "three classes of transient failures originating from defects located in the row circuits, column circuitry, and peripheral logic ... outside the memory array" = s1 (a). 일치.
- (b) "Beginning with the observed failure signatures, we analyze the underlying root causes and explain the physical mechanisms" = s1 (b). 일치.
- (c) "defining effective screening strategies and stress methodologies ... stringent DPPM requirements" = s1 (c). 일치.
- 초록에 없는 mechanism, 수치는 UNKNOWN으로 표기했다 (PASS). causal chain, E1~E3, H1~H5는 ENGINEERING_INFERENCE로 라벨됐다 (PASS).

(2) 물리: PASS. `indep_checks_out.txt`에서 sympy로 재유도한 결과는 다음과 같다.
- E1: t_d−(R_d+R_x)C ln(1/(1−f)) = 0, R_x,crit 잔차 0, θ=3·f=½에서 r_crit=3.328.
- E2: R_b,crit−R_on m/(1−m) = 0.
- E3: d ln t_fail/d(1/T) = E_a/k, 부호 양(+).
- 차원: Ω·F=s, F·V/A=s.
- 주변회로이므로 planar·lumped 근사를 쓴다고 "Geometry / domain gate"에 명시했다. 원통 동축 식을 적용하지 않는다고 밝혔다 (PASS).

(3) 경쟁 메커니즘과 critical boundary: PASS. H1~H5와 non-defect 기준선이 있고, R_crit 근방 band라는 비순환 경계가 있다.

(4) DOE 반증 가능성: 부분 FAIL (s1-1, s1-2 참조).

(5) 이중언어 6쌍 스팟체크(geometry gate, chain 설명, E1~E3, critical boundary, failure-mode, DOE, 결론): 의미 이탈 없음. PASS.

(9) 날짜: PASS.

**Findings**

- **s1-1 (major)** 위치: `.doebox`, "ln t_fail vs 1/T가 평탄하면 H4 기각".
  - 문제: H4는 "junction/GIDL, floating gate"를 포함한다. GIDL과 터널링 누설은 field 구동이라 T 의존이 약하다. 작성자 notes는 이를 약점으로 인정했으나 HTML에는 없다. 평탄한 기울기만으로 H4 전체를 기각하는 것은 과잉이다.
  - 수정: H4를 H4a(열활성 접합 누설: 평탄 기울기로 기각)와 H4b(GIDL·터널링 계열: 고정 T에서 V_DG/V_DS 전계 의존 유무로 기각)로 나눈다. 또는 "기울기 |E_a/k|가 허용치 δ 미만이면 H4a만 기각"으로 쓴다. 문서 안에 이 한계를 적는다.
- **s1-2 (major)** 위치: 같은 box, "고정 v,T에서 P_fail이 τ에 무관하면 H1 기각".
  - 문제: τ 수준이 R_crit band 밖(항상 pass 또는 항상 fail)이면 P_fail은 τ와 무관하므로 거짓 기각이 일어난다.
  - 수정: "τ 수준은 측정된 fail boundary τ_b를 사이에 두어야 한다(예: τ∈{τ_b/2, τ_b, 2τ_b}). 그렇지 않으면 inconclusive"라고 추가한다.
- **s1-3 (minor)** 위치: Geometry gate, "periphery(CMOS 논리, HV 디코더, page buffer)에 있다".
  - 문제: 초록은 row circuits, column circuitry, peripheral logic만 말한다. 괄호 안 예시는 출처 사실처럼 쓰인 추정이다.
  - 수정: "(row/column/peripheral logic; HV 디코더·page buffer는 본 보고서의 예시이며 ENGINEERING_INFERENCE)".
- **s1-4 (minor)** 위치: "What is new vs known"의 "새로운 점은 ... framing이다".
  - 문제: 신규성 판단은 초록 문구에 대한 작성자의 독해다.
  - 수정: "(ENGINEERING_INFERENCE, abstract 기반 판단)" 표기를 추가한다.
- **s1-5 (minor)** 위치: sourcebox, "Crossref deposit 2026-09-30".
  - 문제: 2026-09-30은 Crossref `created`다. `deposited`는 2026-10-06이다.
  - 수정: "Crossref 최초 등록(created) 2026-09-30".
- **s1-6 (minor)** 위치: card "Change vs archive", "Adjacent W41 ISTFA 2026 p0653 ...".
  - 문제: W41은 W40 이후 주차 문서(draft 브랜치)다. 아직 공개되지 않은 미래 주차를 W40 본문이 참조한다. 나도 이 논문의 존재를 확인하지 못했다 (UNKNOWN).
  - 수정: 해당 문장을 삭제한다. archive 비교는 W37~W39로 제한한다.
- **s1-7 (minor)** 위치: sourcebox "PDF subscriber-only", card "SOURCE TRACE ... sources.yaml S1 → Crossref + doi.org → ASM DL page".
  - 문제: ASM 페이지 접근은 내가 재현하지 못했다 (403, UNKNOWN). "sources.yaml S1"은 내부 작업 파일 참조다.
  - 수정: "Crossref 재조회(2026-10-21)로 제목, 저자, 날짜 일치 확인; 출판사 페이지 미확인"으로 바꾸고 파일명 참조를 제거한다.
- **s1-8 (minor)** 위치: (E2).
  - 문제: bridge가 연결되는 기준 노드(접지)가 서술에 없다.
  - 수정: "R_b는 노드와 0 V 기준 사이의 저항성 bridge"라고 쓴다.
- **s1-9 (minor, 선택)** 저자 소속이 Sandisk Technologies(Crossref)다. 벤더 FA 관점 논문임을 sourcebox에 사실로 적으면 독자가 근거 수준을 판단하기 쉽다.

### s2 — 판정: PASS-WITH-FIXES

(1) 출처 충실도: 대체로 PASS. 초록과 대조한 결과는 다음과 같다.
- (1) "A defect affecting even a single load can disturb the integrity of the shared global signal, causing degradation across multiple functional blocks" 일치.
- (3) "small physical footprint ... buried deep within the die, which makes typical OBIRCH hotspots diffused or smeared out" 일치.
- (4) "The methodology presented here" 일치.
- (2) "gate oxide"는 초록 본문에 없고 제목에만 있다 (s2-2).
- 구조, workflow, 수치는 UNKNOWN으로 표기했고 inference 라벨이 촘촘하다 (PASS).

(2) 물리: PASS. `indep_checks_out.txt`의 독립 재유도 결과는 다음과 같다.
- 동축/평면 비: `u/log(u+1)` (잔차 0). 급수 `1+u/2−u²/12`. u=1e-3~1e3 표본에서 비>1. 따라서 s2의 u/ln(1+u)>1과 u→0에서 1이라는 서술은 일치한다.
- 정상상태 표면 온도(source+image): `P/(2πk√(ρ²+d²))`. FWHM=2√3·d. P_min=2πk·d·ΔT_min. 차원은 W로 일치.
- lock-in: `exp(-(1+i)R/μ)/R`이 μ=√(2D/ω)에서 열방정식 잔차 0. FWHM/d는 g=0, 1, 5, 10에서 3.464, 1.887, 0.9935, 0.7221로 s2의 3.46, 1.89, 0.99, 0.72와 일치. g=10의 점근식은 0.745로 일치.
- e⁵=148.4로 s2의 "약 1/150"과 일치.
- 평면 MOS 식 `E_ox=(V_G−V_FB−ψ_s−V_poly)/t_ox`는 부호와 차원(V/m)이 맞다. 주변회로 평면 가정과 원통 식 "대비 용도"를 명시했다 (PASS).
- 열모델은 균질 반무한 매질, 단열 표면, 점열원 가정이다. 이 가정의 한계는 본문에 적혀 있다. OBIRCH 레이저 기하에 대한 엄밀 유도는 아니다 (작성자도 인정). 라벨은 ENGINEERING_INFERENCE이고 가설 수준이므로 허용한다.

(3) 경쟁 메커니즘: PASS. 5종과 boundary가 있고 비순환이다.

(4) DOE: 대체로 PASS. 반증 기준 (a)~(d)와 열확산 가설 기각 조건이 있다. 정량 임계가 없다 (s2-4).

(5) 이중언어 6쌍 스팟체크(sourcebox, 사슬 설명, 동축 식, 열확산 설명, DOE, 반증 기준): 의미 이탈 없음. PASS.

**Findings**

- **s2-1 (major)** 위치: `.chain` 마지막에서 두 번째 노드 `<i>[SR]</i>` ("multi-block functional degradation"), ko "SOURCE_REPORTED 'multiple blocks' signature와 일치한다", en "consistent with the reported multi-block signature".
  - 문제: 초록은 일반적 위험("can disturb ... causing degradation across multiple functional blocks")을 말한다. 시연한 결함이 실제로 multi-block 불량을 일으켰다는 관측은 초록에 없다. [SR] 태그와 "reported signature"는 관측처럼 읽힌다.
  - 수정: 해당 노드를 `[SR: 일반 동기]`로 바꾸거나 `[INF]`로 바꾼다. 문장을 "초록이 일반론으로 언급한 multi-block 열화 범주와 정합"으로 고친다. 엄격 해석 시 blocker로 올릴 수 있다 (조정자 판단).
- **s2-2 (minor)** 위치: What is new (2) "pool capacitor 내부의 미세한 gate-oxide defect".
  - 문제: "gate oxide"는 제목에만 있고 초록 본문에는 "subtle defect within the pool capacitor"로 되어 있다.
  - 수정: "(gate oxide는 제목 표기)".
- **s2-3 (minor)** 위치: sourcebox "포스터, 3쪽" / "(poster, 3 pp.)".
  - 문제: Crossref에는 쪽수 478–480만 있다. "poster"는 재현하지 못했다 (UNKNOWN).
  - 수정: "pp. 478–480 (3쪽)"만 남기거나 "poster(manifest 기준, 미재현)".
- **s2-4 (minor)** 위치: 경쟁 메커니즘 표와 반증 기준 (a) "강한 Arrhenius".
  - 문제: "약한/강한 T 활성"에 정량 문턱이 없다. TAT 자체도 열보조 성분이 있다.
  - 수정: 상징적 문턱을 정의한다 (예: 겉보기 E_a,def ≪ E_a,j 기준). 같은 sample의 I-V-T로 비교한다고 쓴다.
- **s2-5 (minor)** 위치: DOE "FWHM이 g 증가에 따라 위 표처럼 줄어듦".
  - 문제: 수치는 표가 아니라 `.eq` 줄에 있다.
  - 수정: "위 식의 FWHM/d 수열처럼".
- **s2-6 (minor)** 위치: 사슬 `[SR]`/`[INF]`, 표의 "LIT", "It complements S1".
  - 문제: 약어 정의가 없다. "S1"은 manifest 내부 ID다.
  - 수정: `[SR]`=SOURCE_REPORTED, `[INF]`=ENGINEERING_INFERENCE를 한 번 정의한다. LIT를 정의한다. "S1"은 "본 보고서 item 1(§1)"로 바꾼다.
- **s2-7 (minor)** 위치: 동축 식 단락.
  - 문제: u=t/r_in에서 t=r_out−r_in 정의가 ko에 없다 ("같은 두께 비교"만 있음).
  - 수정: 한 줄 추가.
- **s2-8 (minor)** 위치: `.qc` 블록.
  - 문제: "Invented numbers NONE", "sympy 1.13.3 run"은 작성자의 자기평가다. 타 섹션은 sympy 1.14.0을 쓴다.
  - 수정: 항목별 `.qc`를 삭제하고 보고서 단위 QC로 일원화한다.
- **s2-9 (minor)** 위치: card "Change vs archive", "같은 저자·학회의 S1".
  - 문제: S1은 4명, S2는 6명이고 겹치는 저자는 일부(Zhu, Rill, De La Rama)다.
  - 수정: "공통 저자 일부, 같은 학회".

### s3 — 판정: PASS-WITH-FIXES (minor만)

(1) 출처 충실도: PASS. 초록과 문자 대조한 결과는 다음과 같다.
- "Silvaco Atlas with the DYNASONOS charge trapping model" 일치.
- "optimal trap density ... approximately 3–5 × 10¹⁹ cm⁻³, beyond which the incremental window gain saturates" 일치.
- "tunnel oxide thickness of 4–5 nm provides the best trade-off ... ⩽15% charge loss over 10 years when combined with an optimized Al₂O₃ blocking oxide" 일치.
- "larger grain sizes (>50 nm) significantly reduce the Vth distribution width" 일치.
- "calibrated validated against published experimental P/E, retention, and endurance data" = "claim" 일치.
- 기하(planar/cylindrical)는 초록에 없고, s3는 이를 UNKNOWN 박스로 명시했다 (핵심 장점, PASS). "TCAD 10년 수치는 외삽(EXTRAPOLATION_ONLY)"도 적절하다.

(2) 물리: PASS (가장 강하게 검증됨).
- 다층 동축 계수: `S3_numeric_out`에서 40자리 mp로 12개 무작위 (a, b, e_n, e_b) 조합에서 g₀의 1차 계수가 s3 식 `(a²e_b+2ab e_n+2a e_b+b² e_n+2b e_n+e_b e_n)/[2(a e_b+b e_n+e_b e_n)]`와 모두 일치했다 (불일치 0). sympy 기호 극한에서도 잔차 0이다 (`indep_checks_out.txt` line 15).
- g_gate의 1차 계수는 −(…)/(…)로 음수(<0)이며 12/12 모두 확인됐다. 기호 형태도 일치한다.
- r₁(TOX측)의 1차 계수는 `(a²e_b+2ab e_n+b² e_n−e_b e_n)/(2(…))`이고 부호가 바뀐다. 실제로 12개 중 1개에서 음수(−0.2527)가 나왔다. s3 (iii)와 일치한다.
- 20만 점 무작위 표본 (`s3_sample_out.txt`, κ∈[1e-3, 10^1.5], a, b∈[10^-1.5, 10^1.5], e_n, e_b∈[0.1, 20])에서 g₀≤1은 0건, g_gate≥1은 0건이다.
- 단일 층: `x/ln(1+x)=1+x/2−x²/12` 일치.
- **retention 동일성 (ii)**: 채널·게이트 접지, TOX/CTL 계면 sheet charge, ΔVth=Qs·A₂로 정의하면 coax/planar 비 ÷ g₀ = **정확히 1** (`indep_checks_out.txt` line 20 근처). exact identity가 확인됐다.
- FN 감도 `d lnJ/d lnE = 2 + B/E` 일치.
- 층 순서, 가정(축방향 무한 균일, 동일 Q′), 교과서 Gauss 법칙 출처 라벨 모두 적절하다.
- 곡률 효과 방향 추론("TOX 최적점이 두꺼운 쪽")은 retention의 field 민감도가 낮다는 조건부이며, 반대 경우(TAT)에 약해지거나 뒤집힐 수 있다고 명시했다. 크기는 제시하지 않았다 (PASS, 과잉 주장 없음).

(3) 경쟁 메커니즘: PASS. 4종과 "≤15% 수치가 이 경로를 볼 수 있는가" 열이 있다. boundary는 비순환이다.

(4) DOE: PASS (대체로). 요인·대조·예상 signature·반증 (a)~(d)가 있다. 수준은 무차원이다 (s3-3 참조).

(5) 이중언어 6쌍 스팟체크(sourcebox, geometry 박스, 곡률 연결 설명, SymPy 결과 (i)~(iii), 추론 박스, 한계 박스): 의미 이탈 없음. PASS.

**Findings**

- **s3-1 (minor)** 위치: sourcebox SR 문장 "poly-Si grain-boundary trap이 Vth variability를 만들고" / "Poly-Si grain-boundary traps drive Vth variability".
  - 문제: 초록은 "we investigate the effect of polysilicon grain boundary traps on Vth variability"이며 인과 동사 "drive"는 더 강하다.
  - 수정: "grain-boundary trap이 Vth variability에 미치는 영향을 분석했고 grain >50 nm에서 분포 폭이 줄어든다".
- **s3-2 (minor)** 위치: sourcebox "revised 5 Sep", "paywalled; data not public per publisher page".
  - 문제: Crossref에는 received 07-15, accepted 09-14, epub 10-01만 있다. "revised 5 Sep"과 "data not public"은 재현하지 못했다 (UNKNOWN).
  - 수정: 두 항목을 삭제하거나 "(manifest 기준, 미재현)"을 붙인다.
- **s3-3 (minor)** 위치: DOE 표 "Trap density N_t/N* ∈ {below, inside, above}" 및 반증 (a).
  - 문제: 실물 소자에서는 N_t를 직접 세팅할 수 없다. TCAD 행과 측정 행이 섞여 있다.
  - 수정: TCAD arm(N_t 직접 sweep)과 measurement arm(SiN 조성 변형으로 N_t를 간접 측정)을 분리하고 반증 (a)를 TCAD arm 중심으로 다시 쓴다.
- **s3-4 (minor)** 위치: "New vs known", "이 논문의 가치는 ... 정량 최적점의 위치".
  - 문제: 평가 문장이 라벨 없이 서술되어 있다.
  - 수정: "(ENGINEERING_INFERENCE)" 표기.
- **s3-5 (minor)** 위치: SymPy 결과 (ii).
  - 문제: "같은 ΔVth"의 정의가 없다. 정의는 게이트·채널 접지 상태에서 sheet charge가 만드는 Vth 이동 크기다. 이 정의에서 동일성이 정확히 성립한다 (내 재유도).
  - 수정: ΔVth 정의 한 줄과 "sheet charge 위치 r₁이 planar 기준에서도 같다" 가정을 명시한다.

### s4 — 판정: PASS-WITH-FIXES

(1) 출처 충실도: 부분 FAIL → 수정 후 PASS. 초록과 대조한 결과는 다음과 같다.
- 일치: "hot-carrier injection (HCI) mechanisms in 180 nm NMOS transistors operating from room temperature down to 140 K"; "Time-to-failure modeling confirms accelerated degradation kinetics while validating conventional substrate-current-based reliability methodologies at cryogenic temperatures"; "gate-length optimization".
- 강도 차이: 초록 "a strong impact of hot-carrier effects at low temperatures, resulting in increased degradation ..., **particularly under** CHE and DAHC stress conditions" vs s4 "(b) CHE와 DAHC stress 모두에서 저온일수록 열화가 더 큼" (s4-2).
- 초록에 없는 "저전압" (s4-1).

(2) 물리: PASS. `indep_checks_out.txt`에서 sympy로 재유도했다.
- 국소 기울기 `d lnτ/d ln(I_sub/I_d) = −φ_it/(φ_i + L)` (L=qλE_m)로, s4가 "−φ_it/(φ_i+qλE_m)"라고 쓴 것과 일치하고 L≪φ_i에서만 −φ_it/φ_i로 수렴한다.
- λ=λ₀tanh(E_p/2kT)에서 dλ/dT<0 (정규화 수치: −0.1175), E_m 고정 시 d ln(I_sub/I_d)/dT<0 (−2.44), d lnτ/dT>0 (+5.88). 저온 악화 방향이다. 부호 PASS.
- 단위: τ=A_HC·(W/I_d)·r^−m에서 A_HC [A·s/m]. 차원 PASS.
- 평면 소자(planar MOSFET)이며 원통 어레이와 무관하다고 명시했다. 정당하다 (PASS). 온도 부호 구분(HCI 저온 악화 vs BTI·열활성 고온 악화)은 표준 지식과 일치한다.

**CHE / DAHC 용어 관례 (내가 확인한 범위)**: 이 세션에서 1차 문헌에 접근하지 못했으므로 기억 기반이며 근거 등급 B- (문헌 일반 지식)이다.
- 관례는 다음과 같다. **DAHC** = V_g ≈ V_d/2 근방(기판전류 I_sub 최대) 영역의 avalanche 기원 hot carrier. **CHE** = V_g ≈ V_d 근방(게이트 전류와 전자 주입 최대) 영역의 channel hot electron. V_g가 더 낮은(≈V_th 근방) 영역에서는 hole 주입과 이차 생성(SGHE·기판 hot carrier) 성분이 커진다.
- 일부 문헌과 JEDEC 문서는 V_g≈V_d/2 worst-case를 "CHC"라고 부르므로 라벨 사용은 문헌마다 다르다. s4_notes.md가 인용한 사전 브리프("CHE는 V_g~V_d/2 근방, DAHC는 저 V_g")는 위 관례와 반대 방향이다.
- s4는 라벨 중립("V_g/V_d 비율로 비교")으로 썼으며, I_sub 피크는 중간 V_g라는 서술은 관례와 일치한다. 따라서 용어 오류는 없다. 다만 관례 매핑을 한 줄로 명시하면 독자 오독을 막을 수 있다 (s4-3).

(3) 경쟁 메커니즘: PASS. HCI vs BTI(온도 부호), N_it 생성 vs oxide trapping, MVE/EES 영역 반전 가능성이 있다. 경계는 "가설, 등급 C", "문헌 미확인"으로 적절히 라벨됐다.

(4) DOE: 부분 FAIL (s4-4, s4-5).

(5) 이중언어 6쌍 스팟체크(sourcebox, New vs known, chain 설명, 온도 부호 단락, EXTRAPOLATION 박스, DOE): **sourcebox와 DOE에서 이탈** (s4-7).

**Findings**

- **s4-1 (major)** 위치: h2 "a low-voltage contrast case", sourcebox "저전압 cryogenic CMOS 대조 사례", card VALID RANGE "180 nm 저전압 NMOS", EXTRAPOLATION 박스 "저전압 180 nm" / "low-voltage".
  - 문제: 초록은 bias 조건을 말하지 않는다. 같은 섹션이 "Stress 전압 ... UNKNOWN"이라고 인정하므로 모순이다. manifest의 extrapolation_warnings 문구를 사실처럼 옮긴 것이다.
  - 수정: "저전압" 전부를 "180 nm CMOS ROIC(공칭/stress 전압 미확인)"으로 바꾸거나 "(ENGINEERING_INFERENCE: ROIC는 통상 저전압 동작으로 추정)"이라는 라벨을 붙인다.
- **s4-2 (major)** 위치: sourcebox (b) "CHE와 DAHC stress 모두에서 저온일수록 열화가 더 큼", New vs known "두 모드 모두 이 경향을 140 K까지 확인", en "confirmation ... in both CHE and DAHC modes down to 140 K".
  - 문제: 초록은 "particularly under CHE and DAHC"이며 두 모드를 각각 비교했다거나 140 K까지 모든 모드에서 확인했다는 문장이 없다.
  - 수정: "저온에서 hot-carrier 열화가 크게 증가하며 특히 CHE와 DAHC stress 조건에서 두드러진다(초록)". "140 K까지 두 모드 모두 확인"은 삭제하거나 UNKNOWN으로 바꾼다.
- **s4-3 (minor)** 위치: Competing mechanisms 단락, "CHE/DAHC 라벨이 어느 bias 영역에 붙는지는 문헌마다 다르고".
  - 문제: 관례 매핑이 없다.
  - 수정: "통상 DAHC≈V_g~V_d/2(I_sub 최대), CHE≈V_g≈V_d; 단, 문헌마다 다름(이 세션 1차 문헌 미확인)" 한 줄 추가.
- **s4-4 (major)** 위치: DOE "V_g/V_d ∈ {r_low, r_peak, r_high} × ... × stress mode {CHE, DAHC}".
  - 문제: stress mode는 V_g/V_d 비로 정의되므로 요인이 완전 교락(redundant)이다. 같은 섹션의 "라벨이 아니라 비율로 비교" 원칙과도 모순이다.
  - 수정: mode 요인을 삭제하거나 r_peak, r_high를 각각 DAHC형, CHE형으로 nested 정의해 설계 행수를 줄인다.
- **s4-5 (minor)** 위치: DOE 반증 "warm-up 후 열화 대부분 회복(trapping 지배)이면 cryogenic I_sub 방법론 등가성은 기각".
  - 문제: 회복은 열화 성분이 trapping임을 뜻하며 I_sub 모델 유효성의 직접 반증이 아니다.
  - 수정: (i) m이 T 의존이면 등가성 기각, (ii) 회복 우세면 permanent-damage 기준으로 TTF 재정의 — 두 판정을 분리한다.
- **s4-6 (minor)** 위치: EXTRAPOLATION 박스 "140–300 K".
  - 문제: 초록은 "room temperature"이며 300 K는 작성자의 가정이다.
  - 수정: "RT–140 K".
- **s4-7 (minor)** 위치: sourcebox의 ko/en, DOE 말미, card.
  - 문제: ko 문단은 제목, "Crossref 표기", CC BY 4.0, bias 미확인 서술이 있으나 en 문단은 제목과 "Crossref 표기"가 빠졌다. DOE 영어 "Falsified if ..."는 무엇이 기각되는지 목적어가 없다 (ko는 "cryogenic I_sub 방법론 등가성은 기각"). 카드의 MODEL, ASSUMPTION, CONFIDENCE, Competing mechanisms, Electrical signatures, Failure modes 셀은 한국어 전용이다.
  - 수정: 영어를 ko와 같은 정보량으로 맞추고, 목적어를 추가하고, 카드 셀을 병기한다.
- **s4-8 (minor)** 위치: card "What changed vs archive", "W39가 ... 추가했다면".
  - 문제: W39에는 "HCI/BTI — sequential stress/history-state boundary 추가"가 있다 (문자 확인, PASS). 조건문은 불필요하다.
  - 수정: "W39가 ... 추가했고".
- **s4-9 (minor)** 위치: EXTRAPOLATION 박스 첫 문장(HV NAND periphery는 두꺼운 산화막, drift/LDD, 높은 V_d, 상온 이상).
  - 문제: 일반 배경 서술이 라벨 없이 사실로 쓰였다.
  - 수정: "일반 배경(ENGINEERING_INFERENCE; 제품값 아님)".
- **s4-10 (minor)** 문체: s4만 "~합니다"체이고 s1, s2, s3는 평서체다 (cross-1).

### s5 — 판정: FAIL (B1 수정 전 게시 불가; 수정 후 PASS-WITH-FIXES 예상)

(1) 출처 충실도: FAIL. 초록과 대조한 결과는 다음과 같다.
- 일치: "three commercial 1.2 kV device families (Wolfspeed C2M and C3M planar, Infineon trench)"; "150 °C and five switching frequencies (DC to 100 kHz)"; "Weibull characteristic lifetime increases monotonically with frequency, ... 4.1×–4.7×"; "bimodal ... fast interface-state cluster near τ≈0.7 ms and a slow ... shoulder extending from about 0.5 to 50 s"; "quasi-permanent threshold-voltage drift under millisecond pulsing (≈30% relative to DC at 150 °C) provides direct evidence that fast traps de-trap during each OFF interval, which is the proposed physical origin of the lifetime extension"; "bounding and empirical ... field mismatch ... discussed explicitly".
- **불일치**: 초록의 상관 대상은 "**the slow-trap filling-rate ratio derived from g(τ)** and the measured lifetime ratio"다. 이 둘은 "agree within the propagated measurement uncertainty"이다 (s5-1).
- archive-gap 라벨은 h2와 상단 boundary 박스에 모두 있고 날짜가 정확하다 (PASS).
- "Already known" 문단은 "배경 지식, 1차 출처 재확인 안 함"이라고 라벨되어 있다 (PASS).

(2) 물리: 대체로 PASS. `indep_checks_out.txt`의 sympy 재유도 결과는 다음과 같다.
- 유효 stress 시간 회계 (Miner, unipolar 직사각형): E-model, 1/E-model, Q_BD(J=A·E²·exp(−B/E)) 세 모델 모두 wall-clock 이득 = **1/D**이며 f에 무관. s5의 "정확히 1/D, 고정 D에서 주파수 무관"이 맞다. 1/4.7=0.2128, 1/4.1=0.2439이므로 "D≈0.21–0.24"도 맞다.
- 단일 τ 모델: n* = (1−a)b/(1−ab), n_peak=(1−a)/(1−ab) 모두 잔차 0. D=0.5, τ_c=τ_e에서 f·τ=7이면 n_peak=0.51785, 70이면 0.50179, 상대 변화 3.1%로 s5의 0.518, 0.502, 약 3%와 일치한다.
- Weibull MLE 상수: Var(η̂)/η²·nβ² = 1.10866, 비의 sd 상수 √(2×1.10866)=1.48907이므로 s5의 1.49와 일치한다.
- 평면 MOS 식 ΔV_FB=−(Q_ot/C_ox)(x̄/t_ox)는 작성자 notes의 sympy 출력만 있고 내가 재실행하지는 않았다 (UNKNOWN, 단 단순 Gauss 법칙 결과이며 부호·차원은 수기로 일치).
- 동축 식 E_i(r)=Q′/(2πε_i r), ΔV_i=Q′/(2πε_i)ln(r_out/r_in)이 VNAND 방사 스택에 적용되고, 조건(동축, 층별 균일 ε, 축 fringe 무시)이 명시됐다 (PASS). SiC는 planar라 한다고 명시했다 (PASS).

(3) 경쟁 메커니즘: PASS (5종, critical boundary: OFF bias 부호). 단 논리 결함이 있다 (s5-2).

(4) DOE: PASS. 요인, equal-t_eff와 equal-wall-clock arm, 대조군, 예상 signature, 반증 기준이 있다 ("equal t_eff에서 η가 DC와 같으면 duty artifact").

(5) 이중언어 6쌍 스팟체크(archive gap 박스, sourcebox, (i)(ii) 추론, 경쟁 메커니즘, DOE, NAND 관련성): 숫자 일치, 의미 이탈 없음. PASS. 위 B1은 ko와 en에 동일하게 존재한다.

**Findings**

- **s5-1 (BLOCKER)** 위치: "New vs known"의 ko "이 논문에서 새로운 점(SOURCE_REPORTED): ... lifetime 증가를 g(τ)의 fast cluster 및 drift 감소와 정량적으로 연결하려 했습니다", en "the lifetime gain is linked quantitatively to the fast g(τ) cluster and to the drift reduction"; card CLAIM ko "fast-trap 회복과 상관한다" / en "correlated with fast-trap recovery"; sourcebox "trap과 lifetime의 상관을 empirical·bounding".
  - 문제: 초록이 정량 상관을 보고한 대상은 **slow-trap filling-rate ratio**이다. fast trap de-trapping은 drift 약 30% 감소를 근거로 한 저자의 "proposed physical origin"이며 정량 연결이 아니다. s5는 slow-trap filling-rate ratio를 한 번도 언급하지 않아 SOURCE_REPORTED가 사실을 바꾼다.
  - 수정: (a) 문장을 "SOURCE_REPORTED: g(τ)에서 도출한 slow-trap filling-rate ratio와 측정 lifetime ratio 사이의 empirical 상관이 propagated measurement uncertainty 내에서 일치하나 bounding·empirical이다; 저자는 ms pulsing에서 quasi-permanent Vth drift가 약 30% 낮은 것을 fast trap이 OFF 구간에서 de-trap한다는 직접 증거이자 lifetime 연장의 제안된 물리 기원으로 해석한다"로 바꾼다. (b) 카드 CLAIM의 "fast-trap 회복과 상관"을 "slow-trap filling-rate ratio와 empirical 상관(저자 해석: fast-trap de-trapping이 원인)"으로 바꾼다. (c) sourcebox에서 "trap과 lifetime의 상관"의 대상을 slow-trap filling-rate ratio로 특정한다. 영어도 동일하게 고친다.
- **s5-2 (major)** 위치: `.inference` (i), "4.1–4.7배가 wall-clock 기준이라면 D≈0.21–0.24일 때 전부 duty artifact일 수 있습니다".
  - 문제: 같은 단락이 이득이 "고정 D에서는 주파수와 무관"하다고 인정한다. 그러나 초록은 lifetime이 DC에서 100 kHz까지 5개 주파수에서 monotonic하게 증가한다고 한다. 고정 D의 순수 duty artifact는 이 주파수 의존성을 만들 수 없다. artifact가 성립하려면 D가 f와 함께 변해야 한다 (예: ON 폭 고정, f 증가로 D 변화). 이 구분이 본문에 없어 artifact 가설이 실제보다 넓게 읽힌다.
  - 추가(내 ENGINEERING_INFERENCE, 라벨 필요): 초록의 상관 대상인 slow trap(τ 0.5–50 s ≫ 펄스 주기)은 주기 평균 충전율이 ON 시간 비율에 비례하는 duty 가중 평균에 가깝다. 따라서 slow-trap filling-rate ratio와 lifetime ratio의 상관 자체가 duty·시간 회계 signature일 수 있다. 이 점은 s5의 "duty artifact" 경쟁 가설을 지지하는 가장 직접적인 논거인데 s5에 없다.
  - 수정: (i)에 "고정 D에서 주파수 의존이 관측되면 순수 duty artifact는 기각; duty artifact는 D(f)가 변할 때만 가능"을 추가한다. (ii) 또는 competing-mechanism (1)에 slow-trap filling-rate의 duty 가중 해석을 ENGINEERING_INFERENCE로 추가한다.
- **s5-3 (major)** 위치: (ii) "n_peak은 f가 커질수록 감소해 D로 포화하고, τ_c=τ_e이면 주기 평균 occupancy는 f와 무관하게 D".
  - 문제: "D로 포화"는 τ_c=τ_e일 때만 맞다. 일반적으로는 τ_e/(kτ_c+τ_e)(sympy `indep_checks`/작성자 출력)이다. 문장 순서가 일반 결론처럼 읽힌다. 또한 "0.7 ms cluster만으로는 설명하기 어렵다"는 결론이 τ_c=τ_e, D=0.5라는 가정 위에 서 있다.
  - 수정: 같은 문장에 "τ_c=τ_e일 때"를 명시하고, 결론에 "τ_c≠τ_e이면 포화값과 f 의존이 달라짐(미확인)"을 병기한다.
- **s5-4 (minor)** 위치: card EVIDENCE "근거 등급 B−".
  - 문제: 프로젝트 등급은 A~D다. "B−"는 비표준이다 (작성자 notes도 자인).
  - 수정: abstract만 읽은 문헌 보고이므로 "C (문헌 초록, 본문 미검증)" 또는 정의에 맞는 B/C로 정규화한다.
- **s5-5 (minor)** 위치: card CONTRADICTING DATA "W37 SiC DGS: 동적 gate stress가 ...", competing (4), "SiC bipolar switching instability 문헌".
  - 문제: W37 index.html은 "Cao et al., ... competing electron/hole trap populations with different activation energies ... VTH drifts ... sign crossover"를 서술하지만 "DGS=dynamic gate stress"와 "bipolar"라는 단어는 W37에 없다. 이 확장은 s5의 추가다. "SiC bipolar switching instability 문헌"은 출처 없는 배경이다.
  - 수정: W37 서술을 문자 그대로 인용하고(주석: "DGS 약어는 W37 표기"), bipolar 문헌에는 "배경 지식, 미확인" 라벨을 붙인다.
- **s5-6 (minor)** 위치: NAND 관련성 박스 "WL-to-WL field는 hole과 slit 가장자리에서 증강되므로".
  - 문제: 기하 서술이 사실 문장으로 쓰였다.
  - 수정: "(ENGINEERING_INFERENCE; 형상 계산 T09로 확인)".
- **s5-7 (minor)** 위치: 상단 boundary 박스.
  - 문제: archive-gap 이유와 대상 주차가 없다. 2026-09-18은 W38 창(09-14~20)에 속한다.
  - 수정: "W38 창(09-14~20)에 게재, W37~W39 archive에 없음(main 브랜치 grep 0건)".
- **s5-8 (minor)** 위치: 식 (E-model: τ₀e^{−γE}) 변수 정의.
  - 문제: γ, G의 단위가 없다.
  - 수정: γ [cm/MV], G [MV/cm] 추가.
- **s5-9 (positive)** W39 비교는 문자로 확인됐다: W39 본문에 "HTGB at 150°C, VG=27 V shifted VTH from 3.01 to 4.08 V ... bond-wire fatigue was emulated by cutting source wires"가 있어 s5의 "Oxide 열화는 DC HTGB(150 °C)로 emulate"와 일치한다 (PASS).

## 5. 섹션 간 일관성 문제

1. **cross-1 문체**: s4만 "~합니다"체, s1~s3은 평서체, s5는 혼합. W39 본문은 "~합니다"체다. 하나로 통일한다.
2. **cross-2 항목별 `.qc`**: s2, s3, s5에는 있고 s1, s4에는 없다. W39는 보고서 말미에 하나만 둔다. 항목별 qc는 작성자 자기평가("Invented numbers NONE", s2는 sympy 1.13.3, 타 섹션은 1.14.0)라 QC 증거가 아니다. 삭제하고 nand-build-qa로 일원화한다.
3. **cross-3 카드 형식**: s1/s3는 영어 전용 th/td, s2는 셀 안 ko/en 단락 쌍, s4/s5는 slash 병기와 일부 한국어 전용, 헤더 "Field/Content" 유무도 다르다. 하나의 형식으로 통일한다.
4. **cross-4 내부 참조 노출**: "S1", "sources.yaml S1/S2/S3", "W40 S5"가 공개 HTML에 남아 있다 (s1 SOURCE TRACE, s2 SOURCE TRACE·Change vs archive, s3 SOURCE TRACE, s5 표). DOI와 Crossref 재조회 기록으로 교체한다.
5. **cross-5 근거 등급 척도**: s1 "abstract-level", s2 "evidence grade C", s3 "B/C", s4 "B"/"C", s5 "B−". CLAUDE.md의 A~D로 통일한다.
6. **cross-6 이중언어 범위**: 문단은 ko→en 쌍이 모두 지켜졌다. h3 제목과 표는 영어만 있고, s4/s5 카드 셀은 부분 병기라 규칙 해석에 따라 위반일 수 있다.
7. **cross-7 AUTHOR_INTERPRETATION 미사용**: 5개 섹션 어디에도 이 라벨이 없다 (cardcheck 개수 0). s5의 "저자들은 이를 ... 해석합니다", s1~s2의 저자 주장 해석은 이 라벨을 쓰는 것이 맞다. SR 라벨 표기 방식도 섹션마다 다르다 (헤더 라벨, 대괄호, 굵은 글씨, 평문).
8. **cross-8 분량**: 한글 음절 수는 s1 833, s2 1562, s3 1527, s4 1521, s5 1829 (`markup_out.txt`). s5 notes가 인용한 목표 1800–2800과 s1~s4는 차이가 크다. 기준 문서가 어느 것인지 UNKNOWN.
9. **cross-9 미래 주차 참조**: s1의 W41 p0653 참조 (s1-6).
10. **cross-10 원통 식**: E_i(r)=Q′/(2πε_i r) 표기가 s1, s2, s3, s4, s5에서 같다. 적용 범위 한정(원통은 array만, 주변회로·SiC는 planar)도 모든 섹션에서 지켜졌다 (PASS).
11. **cross-11 W39 참조**: s2 (W39 item 1 Wu & Ando), s3 (W39 item 4 IGZO), s4 (W39 HCI/BTI history-state), s5 (W39 item 5, W37 item 5)는 repo 본문과 모두 일치했다 (문자 대조). 단 s5-5의 DGS 확장은 예외다.

## 6. 요약 판정표 (필수 확인 항목별)

| 점검 | s1 | s2 | s3 | s4 | s5 |
|---|---|---|---|---|---|
| (1) 출처 충실도·라벨 | PASS | PASS (s2-1 major) | PASS | FAIL→수정 (s4-1, s4-2) | **FAIL (B1)** |
| abstract_only 한계 준수 | PASS | PASS | PASS | PASS | PASS |
| (2) 물리 부호·단위·기하 | PASS (sympy) | PASS (sympy) | PASS (sympy+수치+표본) | PASS (sympy) | PASS (sympy; 논리 s5-2) |
| (3) 경쟁 메커니즘·경계 | PASS | PASS | PASS | PASS | PASS |
| (4) DOE 반증 가능성 | 부분 (s1-1, s1-2) | PASS (s2-4 minor) | PASS (s3-3 minor) | 부분 (s4-4, s4-5) | PASS |
| (5) 이중언어 | PASS | PASS | PASS | s4-7 | PASS |
| (6) 9필드 카드 | PASS | PASS | PASS | PASS | PASS |
| (7) 날조·기밀 | PASS (s1-3 minor) | PASS | PASS | PASS (300 K s4-6) | PASS |
| (8) 마크업·클래스 | PASS | PASS | PASS | PASS | PASS |
| 날짜 / archive-gap | PASS | PASS | PASS | PASS | PASS (라벨·날짜 정확; manifest의 "4 days/09-22"는 오류) |

## 7. 결론

- s5는 B1이 해결될 때까지 게시 불가다. 수정은 문장 3곳(ko와 en 각각)에 국한되며 새 계산은 필요 없다.
- s1, s2, s3, s4는 blocker가 없고 major를 고치면 게시 가능하다. s4는 "저전압" 삭제·완화와 DOE 교락 해소를 우선한다.
- sources.yaml의 S5 주석(4 days / 2026-09-22)은 10일 전 / 창 시작 2026-09-28로 정정해야 한다.
- 확인하지 못한 항목(UNKNOWN): 출판사 페이지 서술 일체("subscriber-only", "poster", "revised 5 Sep", "data not public"), W41/W42 브랜치 중복, CHE/DAHC 관례의 1차 문헌 대조, s1의 W41 p0653 존재 여부.
