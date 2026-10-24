# W40 fix pass 기록 (nand-physics-writer, 2026-10-21)

- 입력: `review\review.md` (critic 검수, 전문 확인), `review\cr_S1..S5.json` (Crossref 초록), 각 섹션 notes.
- 백업: 수정 전 원본 7개를 `sections\_orig\`에 그대로 복사했다 (s1–s5.html, report_head.html, report_tail.html).
- 수정 방식: 원본 파일을 제자리에서 고쳤다. 변경량이 많아 각 파일을 전체 재작성했고, 지적과 무관한 문장·식·수치는 그대로 두었다.
- 자체 점검: `sections\fixcheck.py` → 출력 `sections\fixcheck_out.txt`. 이 점검은 작성자 자기 점검이다. 독립 재검수는 아직 하지 않았다 (PENDING).
- 저장소 접근, push, PR은 하지 않았다. `assets/style.css`만 클래스 대조용으로 읽었다.

## 1. Finding별 반영 현황

표기: 반영 = applied, 부분 = partially, 미반영 = not applied.

### s1 (item 1)
| ID | 등급 | 상태 | 내용 |
|---|---|---|---|
| s1-1 | major (조정자 지시로 필수) | 반영 | H4를 H4a(열활성 접합 누설)와 H4b(GIDL·터널링, 전계 구동)로 나눴다. 표, critical boundary, DOE, 카드에 모두 반영했다. 판정 규칙: \|E_a/k\| < δ(사전 허용치)이면 H4a만 기각한다. H4b는 고정 T에서 t_fail이 V_DG/V_DS에 무관할 때 기각한다. DOE에 노드 bias 요인 {low, nominal, high}를 추가했다. 이 한계는 본문에 명시했다. |
| s1-2 | major (필수) | 반영 | τ 수준이 측정 fail boundary τ_b를 사이에 두도록 했다 (예: τ_b/2, τ_b, 2τ_b). 그렇지 않으면 inconclusive라고 적었다. 같은 조건을 tail의 W40-H1 반증 기준에도 넣었다. |
| s1-3 | minor | 반영 | Geometry gate에 "초록 표현: row/column circuit과 peripheral logic; HV 디코더·page buffer는 본 보고서의 예시(ENGINEERING_INFERENCE)"라고 적었다. |
| s1-4 | minor | 반영 | "What is new"에 "(ENGINEERING_INFERENCE, 초록 기반 판단)" 라벨을 붙였다. "~framing이다"는 "~framing으로 보인다"로 바꿨다. |
| s1-5 | minor | 반영 | "Crossref deposit 2026-09-30"을 "Crossref 최초 등록(created) 2026-09-30"으로 바꿨다. |
| s1-6 | minor | 반영 | W41 p0653 문장을 삭제했다. 대신 "archive 비교는 W37–W39로 한정"이라고 적었다. |
| s1-7 | minor | 반영 | "PDF subscriber-only"와 "sources.yaml S1 → … ASM DL page"를 삭제했다. "Crossref 재조회(2026-10-21) 제목·저자·날짜·쪽수 일치; 출판사 페이지 미확인(HTTP 403)"으로 바꿨다. |
| s1-8 | minor | 반영 | E2에 "R_b는 신호 노드와 0 V 기준(접지) 사이 bridge, driver R_on이 노드를 high로 구동"이라고 적었다. 구동 방향(high)은 분압식이 성립하려면 필요한 가정이어서 함께 명시했다. |
| s1-9 | minor (선택) | 반영 | sourcebox에 "저자 소속(Crossref) 4명 모두 Sandisk Technologies Inc., 벤더 FA 관점"을 추가했다. |

추가 변경: 초록 (b)의 "derives"를 "explains"로 바꿔 초록 문구("explain the physical mechanisms")에 맞췄다. 카드를 `div.inference` 안 영어 전용 표에서 h3와 ko/en 단락 쌍 형식으로 바꿨다 (cross-3).

### s2 (item 2)
| ID | 등급 | 상태 | 내용 |
|---|---|---|---|
| s2-1 | major → 조정자 지시로 blocker 취급 | 반영 | chain 노드 `[SR]`을 `[INF; the abstract names this only as a general risk]`로 바꿨다. ko/en 단락의 "SOURCE_REPORTED 'multiple blocks' signature와 일치"는 "초록이 일반론으로 언급한 multi-block 열화 범주와 정합; 시연 결함에서 관측됐는지는 UNKNOWN"으로 바꿨다. 같은 수정을 What is new (1)("일반적 위험(동기)"), 카드 CLAIM, Electrical signatures, head 표, tail synthesis에도 했다. |
| s2-2 | minor | 반영 | "(gate oxide라는 표기는 제목에 있다)"를 추가했다. 본문 표현은 "subtle defect"로 바꿨다. |
| s2-3 | minor | 반영 | "포스터/poster"를 삭제하고 "pp. 478–480 (3쪽)"만 남겼다. Domain boundary 박스와 tail Sources에서도 지웠다. |
| s2-4 | minor | 반영 | 상대 문턱을 정의했다. 같은 sample I-V-T에서 E_a,def와 E_a,j를 함께 추출해 비교하고 "약함 = E_a,def ≪ E_a,j"로 둔다. 절대 문턱은 두지 않는다(TAT의 열보조 성분 때문). 표, DOE, 반증 (a)에 반영했다. 새 수치는 없다. |
| s2-5 | minor | 반영 | "위 표처럼"을 "위 식의 FWHM/d 수열처럼"으로 바꿨다. |
| s2-6 | minor | 반영 | 섹션 앞부분에 표기 단락(ko/en)을 넣어 [SR], [INF], LIT를 정의했다. "S1"은 "본 보고서 item 1"로 바꿨다. |
| s2-7 | minor | 반영 | t = r_out − r_in 정의를 식과 ko/en 단락에 추가했다. "u>0에서"도 명시했다. |
| s2-8 | minor | 반영 | 항목별 `.qc` 블록을 삭제했다 (cross-2). |
| s2-9 | minor | 반영 | "같은 저자·학회"를 "공통 저자 일부(Zhu, Rill, De La Rama), 같은 학회"로 바꿨다. tail도 같게 고쳤다. |

추가 변경: (4) "enables precise identification"에 AUTHOR_INTERPRETATION 라벨을 붙였다 (조정자 5(f)). 저자 소속 6명이 Sandisk라는 점을 Crossref 기준으로 적었다 (s1-9와 같은 취지).

### s3 (item 3)
| ID | 등급 | 상태 | 내용 |
|---|---|---|---|
| s3-1 | minor | 반영 | "Vth variability를 만들고 / drive"를 "Vth variability에 미치는 영향을 분석했고 grain >50 nm에서 분포 폭이 줄어든다 / is analysed"로 바꿨다. |
| s3-2 | minor | 반영 | "revised 5 Sep"과 "paywalled; data not public per publisher page"를 삭제했다. 날짜는 Crossref assertion(접수 07-15, 채택 09-14, epub 10-01)만 남겼다. 출판사 페이지는 "bot challenge로 확인하지 못함"으로 적었다. |
| s3-3 | minor | 반영 | DOE 표를 TCAD arm(N_t 직접 sweep)과 measurement arm(SiN 조성·공정 split, N_t 간접 추정)으로 나눴다. 반증 (a)는 (a-TCAD)를 주 판정으로, (a-meas)를 보조 판정으로 다시 썼다. 추출 불확도가 크면 inconclusive다. |
| s3-4 | minor | 반영 | "이 논문의 가치는 …" 문장에 (ENGINEERING_INFERENCE)를 붙였다. |
| s3-5 | minor | 반영 | SymPy (ii)에 ΔVth 정의(gate·channel 접지에서 sheet charge가 만드는 Vth 이동)를 넣었다. "planar 기준에서도 sheet charge가 같은 층 위치(TOX/CTL 계면)에 있다"는 가정도 ko/en에 명시했다. |

추가 변경:
- 근거 등급 "B/C at best"를 "C (TCAD, 측정 아님, 초록만)"로 바꿨다.
- 카드 CONFIDENCE의 Medium/Low 표기를 등급 C/D와 사유로 바꿨다.
- "재현 스크립트는 notes에 저장"은 내부 파일 참조이므로 "작성 단계 유도; 2026-10-21 독립 검수에서 재유도 일치"로 바꿨다. 근거는 review §4 s3 (2).
- calibration 주장에 AUTHOR_INTERPRETATION을 붙였다.
- sourcebox의 서지 줄을 ko/en 단락 쌍으로 만들었다.
- h3 "Model card"를 "Claim–evidence card"로 통일하고, 카드 셀을 ko/en 쌍으로 만들었다.
- `.qc`를 삭제했다.

### s4 (item 4)
| ID | 등급 | 상태 | 내용 |
|---|---|---|---|
| s4-1 | major → blocker 취급 | 반영 | "저전압/low-voltage"를 모두 삭제했다. 대상은 h2, sourcebox, New vs known, 카드 VALID RANGE, EXTRAPOLATION 박스, head의 lead와 표다. 대체 표현은 "180 nm NMOS(공칭·stress 전압 미확인)"와 "cryogenic CMOS ROIC 대조 사례"다. 점검 결과 잔존 0건이다. |
| s4-2 | major → blocker 취급 | 반영 | "CHE와 DAHC 모두 / both modes … down to 140 K"를 초록 문구에 맞춰 "저온에서 hot-carrier 열화가 크게 증가하며 특히 CHE·DAHC stress 조건에서 두드러진다"로 바꿨다. "두 모드를 각각 140 K까지 확인했는지는 UNKNOWN"을 sourcebox와 New vs known에 명시했다. 카드 CLAIM, head 표, tail synthesis, tail matrix도 고쳤다. 점검 결과 "both modes" 계열 잔존 0건이고, cr_S4 초록에 "particularly under … CHE … DAHC" 문구가 있음을 확인했다. |
| s4-3 | minor (조정자 4) | 반영 | 관례 한 줄을 추가했다: DAHC ≈ V_g~V_d/2(I_sub 최대), CHE ≈ V_g≈V_d. "기억에 근거, 이번 세션 1차 출처 미확인", "라벨 대응은 문헌마다 다름", "이 논문의 bias 점은 UNKNOWN"을 함께 적었다. JEDEC/CHC 언급은 1차 확인이 없어 넣지 않았다. |
| s4-4 | major (필수) | 반영 | stress mode 요인을 삭제했다. mode는 V_g/V_d 수준 안의 nested 이름으로 둔다: r_peak = DAHC형, r_high = CHE형, r_low = 저 V_g 영역. 교락 이유도 문장으로 적었다. |
| s4-5 | minor | 반영 | 판정을 둘로 나눴다. 판정 (i)은 m의 T 의존 또는 짧은 L에서의 collapse 실패이며, 해당하면 방법론 등가성을 기각한다. 판정 (ii)는 warm-up 후 대부분 회복되는 경우로, trapping 지배이며 I_sub 모델의 직접 반증이 아니다. 이 경우 TTF를 permanent-damage 기준으로 재정의한 뒤 (i)을 다시 적용한다. tail W40-H6에도 반영했다. |
| s4-6 | minor | 반영 | "140–300 K"를 "RT–140 K"로 바꿨다. tail QC의 "300 K" 언급도 "room temperature"로 바꿨다. 점검 결과 잔존 0건이다. |
| s4-7 | minor | 반영 | en sourcebox를 ko와 같은 정보량으로 맞췄다(전체 제목, Crossref 표기, CC BY 4.0, bias 미확인). DOE의 en 판정 문장에 목적어(무엇을 기각하는지)를 넣었다. 카드 13행을 모두 ko/en 단락 쌍으로 만들었다. 한국어였던 chain 노드는 다른 섹션과 맞춰 영어로 바꿨다. |
| s4-8 | minor | 반영 | "W39가 … 추가했다면"을 "추가했고"로 바꿨다. |
| s4-9 | minor | 반영 | EXTRAPOLATION 박스 첫 문장에 "일반 배경(ENGINEERING_INFERENCE; 제품값 아님)"을 붙이고 "대체로"를 넣었다. |
| s4-10 | minor (cross-1) | 반영 | 합니다체를 평서체로 바꿨다 (아래 cross-1 참조). |

추가 변경:
- "(c) TTF 방법론 유효"에 AUTHOR_INTERPRETATION을 붙였다.
- "Known (textbook, grade B)"를 "grade C (이번 세션 1차 문헌 미확인, sympy 부호 점검만)"로 낮췄다. 프로젝트 B 정의(문헌 + 동일 영역 계산)의 '문헌'을 이번 세션에서 확인하지 않았기 때문이다. 이 하향은 작성자 판단이다. 조정자가 B를 유지하겠다면 되돌릴 수 있다.
- SOURCE TRACE를 Crossref 재조회 기록으로 바꿨다.

### s5 (item 5)
| ID | 등급 | 상태 | 내용 |
|---|---|---|---|
| s5-1 (B1) | **blocker** | 반영 | 세 곳 모두 고쳤다(ko/en 각각). 고친 문장은 cr_S5.json 초록 문구와 문자 대조했고, `fixcheck_out.txt`에서 8개 핵심 구문이 모두 초록에 존재한다(True). (a) New vs known: SOURCE_REPORTED에는 g(τ)에서 도출한 slow-trap filling-rate ratio와 측정 lifetime ratio의 empirical 상관(전파 불확도 내 일치, 저자 스스로 bounding·empirical)만 둔다. AUTHOR_INTERPRETATION에는 drift 약 30% 감소를 fast-trap de-trapping의 직접 증거이자 lifetime 연장의 제안된 물리 기원으로 본다는 해석을 둔다. "fast trap–lifetime의 정량 연결은 초록에 없음"도 명시했다. (b) 카드 CLAIM: "slow-trap filling-rate ratio와 empirical 상관; 저자 해석(AUTHOR_INTERPRETATION): fast-trap de-trapping이 원인". (c) sourcebox: 상관 대상을 slow-trap filling-rate ratio로 특정했다. "five switching frequencies"와 "explicitly discussed field mismatch"도 초록대로 적었다. head 표의 item 5 행도 같게 고쳤다. "linked quantitatively / 정량적으로 연결 / correlated with fast-trap" 잔존 0건이다. |
| s5-2 | major (필수) | 반영 | (i)에 추가한 내용: 고정 D의 순수 duty artifact는 DC와 첫 펄스 주파수 사이의 계단만 만들 수 있다. 초록이 다섯 주파수에서 단조 증가를 보고하므로 D가 모든 f에서 같았다면 순수 duty artifact는 기각된다. duty artifact는 D가 f와 함께 변할 때만 가능하다. D(f)는 UNKNOWN이다. 기존 "D≈0.21–0.24" 문장은 "D(f)가 변하는 경우, 100 kHz에서" 조건 아래로 옮겼다. 새 단락 (iii)에는 slow-trap(0.5–50 s, 펄스 주기보다 느리다면) filling rate가 duty 가중 평균에 가까우므로 상관 자체가 duty·시간 회계 signature일 수 있다는 해석을 ENGINEERING_INFERENCE 라벨로 넣었다. 경쟁 메커니즘 (1), DOE(각 D를 모든 f에서 고정, 고정 D 기각 기준 추가), 카드 CRITICAL BOUNDARY와 Competing에도 반영했다. 주파수 값은 초록에 없으므로 UNKNOWN으로 적었다. |
| s5-3 | major (필수) | 반영 | (ii)를 "τ_c = τ_e일 때 n_peak → D 포화"로 한정했다. "τ_c ≠ τ_e이면 포화값은 τ_c/τ_e와 D에 의존하고 f 의존도 달라짐(계산하지 않음, UNKNOWN)"을 추가했다. 결론 "0.7 ms cluster만으로는 설명하기 어렵다"에는 "τ_c = τ_e, D = 0.5 가정 아래" 조건과 "가정이 다르면 달라질 수 있음"을 붙였다. critic이 쓴 일반식 τ_e/(kτ_c+τ_e)의 k 정의가 review에 없어서 식 자체는 넣지 않았다 (새 주장 금지 원칙). |
| s5-4 | minor | 반영 | "B−"를 "C (문헌 초록만, 본문·데이터 미검증)"로 바꿨다. 인과 메커니즘은 "AUTHOR_INTERPRETATION, 등급 C 이하"다. |
| s5-5 | minor | 반영 | "DGS / dynamic gate stress" 표기를 전부 삭제했다(s5, tail synthesis, tail matrix). W37 비교는 review에 인용된 W37 서술 요지(활성화 에너지가 다른 electron/hole trap population의 경쟁 → V_th drift sign crossover)로 바꾸고 "W37 item 5 (Cao et al.)"로 표기했다. bipolar 문헌에는 "배경 지식, 미확인" 라벨을 붙였다. 주의: critic의 수정안 문구("DGS 약어는 W37 표기")가 같은 finding의 문제 서술("DGS는 W37에 없음")과 모순된다. 그래서 약어를 삭제하는 쪽을 택했다. W37 원문은 이번 pass에서 직접 읽지 않았다 (저장소 접근 없음). |
| s5-6 | minor | 반영 | "hole·slit 가장자리에서 증강될 것으로 보이므로(ENGINEERING_INFERENCE; 형상 계산 T09로 확인 필요)"로 바꿨다. |
| s5-7 | minor | 반영 | archive-gap 박스에 "W38 window(2026-09-14–09-20)에 속함, W37–W39 공개 archive 본문에서 DOI 미발견(2026-10-21 검색)"을 추가했다. 근거는 critic의 main 브랜치 grep 결과다. "main 브랜치 grep"이라는 내부 표현은 쓰지 않았다. |
| s5-8 | minor | 반영 | γ [cm/MV], G [MV/cm] 단위 정의를 ko/en에 추가했다. |
| s5-9 | positive | 해당 없음 | W39 비교가 일치한다는 확인이다. 표기만 "W39 SiC diagnosis"에서 "W39 item 5"로 바꿨다 (cross-11의 critic 표기를 따름). |

추가 변경:
- 카드 CONFIDENCE의 Medium/Low/Very low를 등급과 사유로 바꿨다.
- 카드에 "Change vs archive" 행을 추가했다(아래 표 참조로 연결, cross-3). 비교 표의 slash 병기 셀은 ko/en 단락 쌍으로 바꿨다.
- 표 헤더 "W40 S5 adds"를 "W40 item 5 adds"로 바꿨다.
- 비교 표의 "DC와 PWM은 trap occupancy 상태가 다르다"를 "다를 수 있다(추론)"로 완화했다.
- UNKNOWN 목록에 "다섯 주파수의 구체적 값", "duty가 주파수마다 같은지"를 추가했다.
- `.qc`를 삭제했다.

## 2. 섹션 간 항목 (review §5, cross-1..11)
| ID | 상태 | 내용 |
|---|---|---|
| cross-1 문체 | 반영 | 조정자 지시("다수 문체에 맞춤, s4 합니다체 수정")에 따라 평서체(~다)로 통일했다. 다섯 섹션 중 s1–s3가 평서체이고 s4, s5는 합니다체였다. 대상은 s4, s5, 그리고 일관성을 위해 report_head와 report_tail이다. 점검 결과 합니다체 잔존 0건이다. 참고로 critic은 W39 본문이 합니다체라고 했다. W40만 평서체가 되므로 주차 간 문체가 달라진다. 조정자 확인이 필요하다. |
| cross-2 항목별 .qc | 반영 | s2, s3, s5의 `.qc`를 삭제했다. tail의 report-level QC 하나만 남겼다 (`class="qc"` 전체 1건, section 내부 0건). |
| cross-3 카드 형식 | 부분 | 다섯 카드를 같은 형식으로 통일했다: h3 "Claim–evidence card" + `<tr><th>FIELD</th><td><p lang=ko>…</p><p lang=en>…</p></td></tr>`, 13행. Field/Content 헤더 행은 없앴다. 미반영: 카드가 아닌 표(s1·s3 경쟁 메커니즘 표, s3 DOE 표, s5 archive 비교표 1열, head 요약표, tail matrix·가설표)는 영어 전용이거나 slash 병기로 남아 있다. chain 노드와 h3도 영어 전용이다. 조정자 지시 5(d)의 범위를 "카드 셀과 인용 줄"로 해석했다. |
| cross-4 내부 참조 | 반영 | "S1..S5", "sources.yaml", "notes", 파일명을 모두 제거하고 "항목/item 1..5"로 바꿨다. SOURCE TRACE는 "Crossref 재조회 2026-10-21 일치; 출판사 페이지 미확인"으로 통일했다. tail Sources 목록의 "S1." 접두는 "[1]"로 바꿨다. 점검 결과 잔존 0건이다. |
| cross-5 등급 척도 | 반영 | A/B/C/D만 쓴다. 초록 사실과 초록 기반 메커니즘은 C, VNAND 이전은 D, 본 보고서 framework는 C다. 모든 등급에 한 줄 사유를 붙였다. High/Medium/Low 잔존 0건이다. head에 등급 정의와 "초록만 읽은 항목의 메커니즘 주장은 A/B 불가"를 ko/en으로 추가했다. |
| cross-6 이중언어 범위 | 부분 | 문단과 카드 셀은 모두 ko→en 쌍이다(전체 문서 위반 0). 표와 h3의 한계는 cross-3과 같다. |
| cross-7 AUTHOR_INTERPRETATION | 반영(부분) | s2 (4), s3 calibration, s4 (c), s5 proposed origin에 적용했다. s1에는 저자 해석 문장이 초록에 없다고 판단해 쓰지 않았다(0건). head에 라벨 정의를 추가했다. SR 라벨의 시각 표기(헤더 라벨, 굵은 글씨, 대괄호)는 섹션마다 여전히 조금씩 다르다. |
| cross-8 분량 | 미반영 | 기준 문서가 UNKNOWN이다. 분량을 맞추려고 내용을 덧붙이지 않았다 (새 주장 금지). |
| cross-9 미래 주차 참조 | 반영 | s1-6과 같다. W41/W42 잔존 0건이다. |
| cross-10 원통 식 | 조치 불요 | PASS 항목이다. 수정하지 않았다. |
| cross-11 W39 참조 | 조치 불요 | s5-5 예외만 위에서 처리했다. |

## 3. 조정자 지시 항목 대조
| 지시 | 상태 |
|---|---|
| 1. 모든 finding 반영 또는 사유 기록 | 위 표로 대응했다. 미반영은 cross-8 하나이고, 부분 반영은 cross-3, cross-6, cross-7이다. |
| 2. B1 + s5-2 + s5-3 | 반영. 초록 문자 대조 결과 True 8/8. |
| 3. s2-1, s4-1, s4-2를 blocker로 취급; s1-1, s1-2, s4-4 | 반영. |
| 4. CHE/DAHC 관례 한 줄 | 반영(s4). "기억 기반, 1차 출처 미확인", "논문 bias 점 UNKNOWN"을 명시했다. |
| 5(a) 등급 A–D | 반영. |
| 5(b) 내부 참조 제거, 출판사 페이지 서술 | 반영. "subscriber-only", "poster", "revised 5 Sep", "data not public"은 삭제했다. 출판사 페이지 접근 조건은 "2026-10-21 재조회에서 확인 못함(403/bot challenge)"으로 적었다. MDPI 403은 critic이 재현했으므로 남겼다. |
| 5(c) 항목별 .qc 삭제 | 반영. |
| 5(d) 카드·인용 줄 ko/en | 반영. sourcebox 서지 줄(s1, s3, s4의 en 보강)과 tail Sources를 ko/en 쌍으로 만들었다. |
| 5(e) 문체 통일 | 반영(평서체). 위 cross-1 주의 참조. |
| 5(f) AUTHOR_INTERPRETATION | 반영. |
| 5(g) 미래 주차 참조 삭제 | 반영. |
| 5(h) [SR]/[INF]/LIT 정의, "S1" 수정 | 반영. 약어는 s2에서만 쓰며 s2 첫머리에서 정의했다. 다른 섹션은 전체 라벨명만 쓴다. |
| 5(i) s1-5, s4-6, s3-2, 소속 | 반영. 소속은 s1·s2에 추가했다. s3–s5에는 넣지 않았다(선택 사항). |
| 6. 새 수치·주장 금지 | 준수. 원본 대비 새 숫자 토큰은 날짜(2026-10-21, Crossref 접수·채택일, W38 창 날짜), 주차 번호(W37–W39, W38), 저자 수(4, 6), HTTP 403뿐이다. 물리 수치는 추가하지 않았다(`fixcheck_out.txt` "new number tokens"). 초록에 없어 채울 수 없는 정보(주파수 값, D(f), τ_c≠τ_e 포화값)는 UNKNOWN으로 적었다. |
| 7. head/tail QC | 반영. head 배너: 0/5 full text, 독립 검수 결과, 재검수 PENDING. tail QC: Crossref PASS(재조회), 출판사 페이지 NOT VERIFIED, full text NOT DONE, 창 분류 PASS, 독립 검수 DONE(Sonnet-class; items 1–4 PASS-WITH-FIXES, item 5 1차 FAIL, 수정 완료), 수정 재검수 PENDING, 라벨·수치·쌍 구조는 re-check PENDING, Render/PDF PENDING. 재검증하지 않은 항목은 PASS로 표시하지 않았다. |
| 8. 자체 점검 | 아래 4절. |

## 4. 자체 점검 결과 (`fixcheck_out.txt` 요약)
- 태그 균형: head + s1–s5 + tail 연결 문서에서 태그 오류 0, 미종료 0. 섹션 단독 파일도 오류 0이다. tail 단독 파일에서 `</article></div></body></html>` 불일치 4건이 나오지만, head에서 연 태그를 닫는 정상 구조다.
- CSS 클래스: 연결 문서에서 미정의 클래스 0건 (repo `assets/style.css` 대조).
- inline style·script: 0건.
- ko→en 인접성: 연결 문서 전체 위반 0건. 쌍 수는 head 5, s1 23, s2 26, s3 25, s4 23, s5 32, tail 19이다.
- 카드 셀: s1–s5 각 13행이고, ko/en 쌍이 없는 행은 0이다.
- anchor: TOC의 `#` 링크는 모두 id로 해석된다. 미해결 0건, 중복 id 0건.
- `.qc`: 문서 전체 1건(tail report-level), `<section>` 내부 0건.
- 금지 문자열 잔존 0건: `\bS[1-5]\b`, sources.yaml, 파일명·notes, W41/W42/p0653, 저전압, low-voltage, 300 K, B−, High/Medium/Low, poster, revised, subscriber, not public, DGS, "both modes" 계열, 합니다체, "fast-trap 정량 연결" 계열, "Crossref deposit".
- 초록 문자 대조: cr_S5에서 B1 핵심 구문 8/8 True. cr_S4는 "particularly under … CHE … DAHC"와 "room temperature down to 140 K"가 True이고, "low-voltage", "300 K", "both"는 False다(삭제가 정당함). cr_S2는 "causing degradation across multiple functional blocks"와 "subtle defect within the pool capacitor"가 True이고, "gate oxide"(본문)와 "poster"는 False다.

## 5. 남은 일과 불확실한 점
1. 반영 결과의 독립 재검수: PENDING. 특히 B1, s2-1, s4-1, s4-2, s5-2/3 문장은 critic 재확인이 필요하다.
2. Full text: 0/5. 출판사 페이지는 미확인이다(403/bot challenge).
3. Render/PDF 빌드: PENDING. 이번 pass에서 렌더링하지 않았다.
4. sources.yaml S5 주석 오류("4 days before / 2026-09-22", 실제는 10일 전 / 창 시작 2026-09-28): 이번 pass의 작업 범위(sections 폴더) 밖이라 고치지 않았다. manifest 소유자가 정정해야 한다.
5. 문체: W40을 평서체로 통일했다. W39는 합니다체라고 critic이 보고했으므로 주차 간 문체가 달라진다.
6. QC의 "Sonnet-class critic"은 조정자 지시를 그대로 적은 것이다. review.md에는 "작성자(Opus)와 다른 모델"이라고만 되어 있다.
7. s4 교과서 배경의 등급을 B에서 C로 낮춘 것은 작성자 판단이다.
8. s5-5의 W37 서술은 review.md 인용을 근거로 요약했다. W37 원문은 직접 대조하지 않았다.
9. s1 E2의 "driver가 노드를 high로 구동"은 분압식이 성립하려면 필요한 서술상 가정이다. 새 수치는 아니지만 원문에 없던 문장이다.
