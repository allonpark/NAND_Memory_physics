# W40 수정 pass 재검수 (recheck)

재검수일: 2026-10-21 / 대상: `sections\s1..s5.html`, `report_head.html`, `report_tail.html` (현재본) vs `_orig\` 및 `review.md`, `fixlog.md`.
섹션 파일은 수정하지 않았다. 확인하지 못한 것은 UNKNOWN으로 남겼다.

## 0. 결론

| 섹션 | 1차 판정 | 재검수 판정 | blocker | major | minor(잔여) |
|---|---|---|---|---|---|
| s1 | PASS-WITH-FIXES | **PASS-WITH-FIXES** | 0 | 0 | 3 |
| s2 | PASS-WITH-FIXES | **PASS** | 0 | 0 | 1 |
| s3 | PASS-WITH-FIXES | **PASS-WITH-FIXES** | 0 | 0 | 1 |
| s4 | PASS-WITH-FIXES | **PASS** | 0 | 0 | 1 |
| s5 | FAIL | **PASS-WITH-FIXES** | **0 (B1 해소)** | 0 | 3 |
| head/tail | - | PASS-WITH-FIXES | 0 | 0 | 2 |

**잔존 blocker: 없음.** 이전 blocker B1과 조정자가 blocker로 취급하라고 한 s2-1, s4-1, s4-2는 모두 해소됐다. 수정이 새로 만든 오류나 초록 밖 주장은 발견하지 못했다. 남은 것은 모두 minor다.

## 1. 수행한 점검과 근거 파일 (`...\scratchpad\w40\review\`)

| 파일 | 내용 |
|---|---|
| `fetch_out_recheck.txt` | Crossref 5건 오늘 재조회. 1차 `fetch_out.txt`와 공백 정규화 diff가 비어 있다(CROSSREF_UNCHANGED). 초록, 제목, 저자, 날짜가 그대로다. |
| `recheck_markup.py` | 연결 문서(head+s1~s5+tail) 태그 균형, 클래스, id, anchor, ko→en 인접성, 금지 문자열, 초록 문자 대조. |
| `recheck_s5.py` | s5 핵심 식을 sympy 1.14.0으로 다시 실행. |

## 2. 점검 항목별 결과

### (1) B1 (s5) — 해소 (PASS)

초록(`cr_S5.json`)과 현재 s5의 SOURCE_REPORTED 문구를 문자 대조했다. `recheck_markup.py`가 12개 구문을 대조했고 12개 모두 초록에 있다(True).

- 다섯 switching 주파수, 단조 증가, 4.1×–4.7×, fast interface-state cluster, 0.5–50 s, ≈30% drift 감소(150 °C), slow-trap filling-rate ratio, "agree within the propagated measurement uncertainty", "bounding and empirical", field mismatch 명시적 논의가 모두 문자 일치한다.
- 현재 s5의 SOURCE_REPORTED는 "slow-trap filling-rate ratio와 lifetime ratio의 empirical 상관(불확도 내 일치, bounding)"만 담는다. 이전의 "fast cluster와 정량적으로 연결" 문구는 sourcebox, New vs known, 카드 CLAIM(ko/en)에서 모두 사라졌다.
- fast-trap de-trapping은 `AUTHOR_INTERPRETATION:` 라벨 아래에만 있다: "drift 약 30% 감소를 fast trap이 매 OFF 구간에 de-trap한다는 직접 증거로 보고, ... 제안된 물리적 기원으로 해석한다". 초록의 "direct evidence ... proposed physical origin"과 일치하고, 저자의 해석으로 올바르게 표기됐다.
- "fast trap과 lifetime 사이의 정량 연결은 초록에 없다"는 부재 진술이다. 초록에는 그런 정량 연결이 실제로 없으므로 맞다.
- 카드 EVIDENCE의 "인과 메커니즘은 AUTHOR_INTERPRETATION이며 등급 C 이하", head 표 5행, tail의 S5 관련 문구도 같은 방향으로 고쳐졌다.

**duty artifact (i) — 정확하고 ENGINEERING_INFERENCE 상자 안에 있다 (PASS).**
- sympy(`recheck_s5.py`): E, 1/E, Q_BD 세 모델 모두 wall-clock 이득 = 1/D. 고정 D에서 d(1/D)/df = 0. 1/4.7=0.2128, 1/4.1=0.2439이므로 D≈0.21–0.24도 맞다.
- 논리: 고정 D의 순수 duty artifact는 DC와 펄스 조건 사이의 계단만 만든다. 초록은 다섯 주파수에서 단조 증가를 보고하므로, D가 모든 f에서 같았다면 순수 artifact는 기각된다. artifact는 D(f)가 변할 때만 가능하다. 본문 서술과 일치하고, D(f)는 UNKNOWN으로 표기했다. 이전 major s5-2는 해소됐다.
- DOE에도 "각 D를 모든 f에서 고정"과 "고정 D에서 펄스 주파수 사이 η 증가 → 순수 duty artifact 기각"이 들어가 반증 가능성이 유지된다.

**τ_c=τ_e (ii) — 정확하다 (PASS).**
- n*, n_peak 닫힌 식 잔차 0. D=0.5, f·τ=7/70에서 n_peak=0.51785/0.50179, 상대 변화 3.1%이므로 본문의 0.518, 0.502, 약 3%와 일치한다.
- 일반화 확인: τ_c=1, τ_e=3, D=½에서 f→∞ 극한은 3/4로, D·τ_e/(D·τ_e+(1−D)·τ_c)와 같다. τ_c=τ_e이면 D로 수렴(D=0.3에서 3/10). 따라서 본문의 "τ_c≠τ_e이면 포화값은 τ_c/τ_e와 D에 따라 달라진다"는 서술이 맞다. 이전 major s5-3은 해소됐다.
- 결론 문장에 "τ_c=τ_e, D=0.5 가정 아래", "가정이 다르면 달라질 수 있음"이 붙어 있다.

**(iii) duty 가중 해석 — 올바르게 ENGINEERING_INFERENCE로 라벨됨 (PASS).** 조건("slow trap이 펄스 주기보다 충분히 느리다면; 주파수 값 UNKNOWN")이 명시됐다. 논리는 일차 kinetics에서 느린 trap이 주기 평균 bias에 반응한다는 표준 결과와 정합한다. 표현은 minor로 s5-R1에 남긴다.

### (2) s2-1, s4-1, s4-2 — 해소 (PASS)

- **s2-1**: 사슬 노드가 `[INF; the abstract names this only as a general risk]`로 바뀌었다. "일치한다"는 "초록이 일반론으로 언급한 multi-block 열화 범주와 정합; 시연 결함에서 관측됐는지는 초록에 없다(UNKNOWN)"로 바뀌었다. What is new (1)은 "일반적 위험(동기)"으로 명시했고 UNKNOWN 목록에 "시연 결함이 실제로 multi-block 불량을 일으켰는지"가 들어갔다. head, 카드 CLAIM, Electrical signatures, tail 합성부에도 같은 수정이 적용됐다. 초록 대조: "A defect affecting even a single load can disturb the integrity of the shared global signal, causing degradation across multiple functional blocks" 문자 일치.
- **s4-1**: `저전압|low-voltage` 잔존 0건(전 섹션 grep). 대체 표현은 "공칭·stress 전압 미확인"이다. 초록에 "low-voltage"가 없음을 확인했다(False).
- **s4-2**: "particularly under channel hot-electron (CHE) and drain avalanche hot carrier (DAHC)"가 초록에 있고 s4 (b)와 일치한다. "both modes ... 140 K까지 확인"은 사라졌다. UNKNOWN 목록에 "각 모드를 140 K까지 비교했는지"가 들어갔다. 카드 CLAIM, head, tail 문구도 같다.
- 추가: s4 (c)와 s2 (4)와 s3 calibration이 AUTHOR_INTERPRETATION으로 라벨됐다. 초록 문구와 대조해 모두 저자 주장에 해당한다(PASS).

### (3) DOE 수정의 논리와 반증 가능성 — PASS (minor 1건)

- **s1-1 (H4a/H4b)**: H4a(열활성 접합 누설)는 |E_a/k|<δ(사전 허용치)이면 기각, H4b(GIDL·터널링)는 고정 T에서 t_fail이 V_DG/V_DS에 무관하면 기각이다. 서로 다른 축(T 대 노드 전계)으로 분리됐고 둘 다 기각 조건이 있어 반증 가능하다. 이전의 과잉 기각(평탄한 기울기로 GIDL까지 기각)이 해소됐다. 표, critical boundary, 카드, W40-H 목록에 일관되게 반영됐다. 잔여 minor는 s1-R1(H4b 허용치 미정의)이다.
- **s1-2 (τ 수준)**: τ_b를 사이에 두는 수준(τ_b/2, τ_b, 2τ_b)을 쓰고, 모든 수준이 같은 쪽이면 inconclusive라고 명시했다. 거짓 기각이 사라졌다. tail W40-H1에도 같은 조건이 들어갔고, H1 행에도 "τ levels bracketing the measured fail boundary"가 있다.
- **s4-4 (V_g/V_d 교락 해소)**: stress mode 요인을 삭제하고 V_g/V_d 수준 안에 nested 이름(r_peak=DAHC형, r_high=CHE형, r_low=저 V_g)으로 뒀다. 교락 이유도 서술했다. 설계는 T × V_g/V_d × L이며 여전히 기각 가능하다(판정 (i): m의 T 의존이나 짧은 L collapse 실패). 판정 (ii)(회복 → trapping 지배)를 분리해 비약이 해소됐다(이전 s4-5). tail W40-H6에도 반영됐다.
- nested 이름은 관례(기억 기반, 라벨됨)에 따른 것이고 "논문 라벨과의 대응은 UNKNOWN"이라고 적어 단정하지 않는다(PASS).

### (4) 수정이 새로 넣은 문장 — 초록 밖 주장 없음 (PASS), 확인한 항목

- **s1 E2 "driver가 노드를 high로 구동"**: 분압식 V_n/V₀=R_b/(R_b+R_on)가 성립하기 위한 서술상 가정이다. sympy로 R_b,crit=R_on·m/(1−m) 잔차 0을 다시 확인했다(`indep_checks_out.txt`). ENGINEERING_INFERENCE 절 안에 있고 새 수치가 없다. PASS.
- **s4 CHE/DAHC 관례 한 줄**: "일반 문헌 관례(기억에 근거한 것이며 이번 세션에서 1차 출처로 확인하지 않음)", "라벨과 bias 영역의 대응은 문헌마다 다르고 이 논문의 bias 점은 UNKNOWN"이 모두 들어 있다. 내가 1차 검수에서 제시한 관례(DAHC≈V_g~V_d/2, CHE≈V_g≈V_d)와 같고 단정하지 않는다. 1차 문헌은 이번 세션에서도 확인하지 못했다(UNKNOWN). PASS.
- **등급 변경**: s4 "교과서 배경"을 B에서 C로 낮춘 것은 방향이 맞다(1차 문헌 미확인). s3 "B/C"→C, s5 "B−"→C로 바꿨고, 모든 등급이 A~D 안에 있다. head에 등급 정의가 ko/en으로 들어갔고 "초록만 읽은 항목의 메커니즘 주장은 A/B 불가"가 명시됐다. PASS.
- **s2의 6명 Sandisk, s1의 4명 Sandisk**: Crossref affiliation과 일치한다(`cr_S1.json`, `cr_S2.json`). PASS. 단 s1의 "벤더 FA 관점의 논문이다"는 해석이다(s1-R2).
- **s3 날짜**: 접수 2026-07-15, 채택 2026-09-14, 온라인 2026-10-01은 Crossref assertion과 일치. "revised 5 Sep"은 삭제됐다. PASS.
- **s5 archive 박스**: "W38 window(2026-09-14–09-20)에 속함", "W37–W39 공개 archive 본문에서 DOI 미발견"은 1차 검수 때 main 브랜치 grep 결과(0건)와 일치한다. 날짜 계산(09-18은 09-14~20 안)도 맞다. PASS.
- **s2 notation 단락**: [SR]=SOURCE_REPORTED, [INF]=ENGINEERING_INFERENCE, LIT=lock-in thermography 정의가 ko/en으로 들어갔다. "S1" 참조는 "item 1"로 바뀌었다. PASS.
- 숫자 토큰: 원본 대비 새 토큰은 날짜(21, 01, 07, 09, 14, 20), 쪽·저자 수(4, 6), HTTP 403, W38의 8, "0 V"의 0, H4b의 4 등이다. 물리 수치 추가는 없다. 제거된 것은 W41의 653, 300 K, sympy 1.13 표기다. PASS. (head의 '4180'은 표의 `<td>4</td><td>180 nm` 연결에서 생긴 토큰 추출 artifact다.)

### (5) 형식·안정성 — PASS

`recheck_markup.py` 결과:
- 연결 문서 태그 오류 0, 미종료 0, inline style 0, script 0.
- 미정의 클래스 0 (사용: boundary, chain, compare, doebox, eq, inference, label, lead, pass, pending, qc, sourcebox, source-links, tag, toc, topbar 등 모두 `assets/style.css`에 존재).
- 중복 id 0, 미해결 anchor 0 (TOC의 #overview, #i1~#i5, #synthesis, #matrix, #insight, #hypotheses, #qc, #sources 모두 해석됨).
- ko→en 인접성 위반 0, lang 없는 `<p>` 0. 카드 셀도 모두 ko/en 쌍이다.
- 항목별 `.qc` 블록 0, 문서 전체 1건(tail).
- 금지 문자열: `S1..S5`, `sources.yaml`, `notes`(파일 의미), W41/W42/p0653, `High/Medium/Low`(등급 의미), `B−`, `저전압`, `low-voltage`, `300 K`, `poster`, `DGS`, `revised`, `subscriber`, `not public`, 합니다체 잔존 0건. (정규식에서 걸린 'high', 'medium', 'denotes'는 모두 일반 단어이며 등급 표기가 아니다. 위 맥락을 확인했다.)
- 등급: 섹션 안의 등급은 C와 D뿐이다.
- 문체: 5개 섹션과 head/tail이 평서체로 통일됐다. 단 W39는 합니다체이므로 주차 간 차이가 생긴다(fixlog가 이미 지적).

### (6) 수정 문단 ko/en 의미 이탈 점검 — 이탈 0건 (12쌍 확인)

확인한 쌍: s5 sourcebox, s5 New vs known, s5 UNKNOWN 목록, s5 (i)(ii), s5 (iii), s5 DOE, s5 archive 박스, s4 sourcebox, s4 New vs known, s4 CHE/DAHC 단락, s4 DOE, s1 E2 단락, s1 critical boundary, s1 DOE, s2 What is new, s2 chain 설명, s2 mechanism 후속 단락, s3 sourcebox, s3 SymPy (ii), s3 Controls/Falsification. ko와 en의 수치(0.518, 0.502, 3%, 0.21–0.24, 4.1–4.7, 0.5–50 s, 140 K)와 조건절(τ_c=τ_e, D=0.5, D(f) UNKNOWN)이 일치한다. 이전에 지적한 s4 영어 "Falsified if" 목적어 누락도 해소됐다.

## 3. 잔여 finding (모두 minor)

- **s1-R1 (minor)** 위치: s1 DOE "t_fail이 V_DG/V_DS에 무관하면 H4b 기각".
  - 문제: 허용치가 없다. H4a의 접합 누설도 역바이어스에 약하게 의존할 수 있다.
  - 수정: "V_DG/V_DS 변화에 따른 t_fail 변화가 사전 허용치 δ_V 미만이면 H4b 기각(H4a 성분의 약한 바이어스 의존은 별도 분리)"로 한 구절 추가한다.
- **s1-R2 (minor)** 위치: s1 sourcebox ko "벤더 FA 관점의 논문이다" / en "so this is a vendor FA perspective".
  - 문제: Crossref는 소속(Sandisk)만 보여 준다. "FA 관점"은 해석이다.
  - 수정: "(Crossref 소속 기준; 관점은 초록 기반 해석, ENGINEERING_INFERENCE)".
- **s1-R3 (minor)** 위치: s1 sourcebox "HTTP 403으로 확인하지 못함", tail "Crossref 재조회(2026-10-21)".
  - 문제: 1차 Crossref 조회는 2026-10-19였고, 2026-10-21 재조회는 이번 재검수에서 수행됐다. 둘 다 결과가 같지만, 본문이 "독립 검수 2026-10-21 수행"만 말해 1차 검수일(10-19)이 빠진다.
  - 수정: "독립 검수 2026-10-19~21" 또는 날짜 문구를 "독립 검수 시점"으로 일반화한다.
- **s3-R1 (minor)** 위치: s3 SymPy 결과 머리 "작성 단계 유도; 2026-10-21 독립 검수에서 기호·수치 재유도 일치".
  - 문제: 공개 본문에 내부 검수 절차 서술이 들어 있다.
  - 수정: "sympy 기호·수치 재유도로 확인(무작위 20만 표본 포함)"처럼 사실만 남기고 절차 서술은 QC 블록으로 옮긴다.
- **s4-R1 (minor)** 위치: s4 카드 CONTRADICTING DATA의 "역온도 경향 보고가 존재할 수 있음(문헌 미확인, 등급 C)".
  - 문제: 가능성 진술이어서 틀리지 않지만 근거가 없는 "존재할 수 있음"이다.
  - 수정: 문헌 미확인 상태를 유지하되 "확인 전까지 반증 후보로만 취급"으로 바꾸거나 해당 행을 CRITICAL BOUNDARY와 합친다. 필수 아님.
- **s5-R1 (minor)** 위치: s5 (iii) "이 해석은 위 경쟁 메커니즘 (1)을 지지하는 가장 직접적인 논거이며".
  - 문제: 조건부 추론에 "가장 직접적"이라는 최상급이 붙었다.
  - 수정: "하나의 직접적인 논거"로 완화한다.
- **s5-R2 (minor)** 위치: s5 (i) 첫 줄 "wall-clock 이득은 정확히 1/D" 이후.
  - 문제: Miner 선형 누적과 unipolar 직사각형 가정(변수 단락에 있음)이 (i) 본문에는 반복되지 않아, 가정이 빠진 채 읽힐 수 있다.
  - 수정: (i) 첫 문장에 "(Miner 선형 누적, unipolar 직사각형 pulse 가정)"을 붙인다.
- **s5-R3 (minor)** 위치: s5 CONTRADICTING DATA의 "SiC bipolar switching instability 문헌(배경 지식, 미확인)".
  - 문제: 라벨은 있으나 출처가 없다. "W37 item 5" 문장은 repo의 W37 본문 서술과 일치한다(1차 검수에서 문자 확인).
  - 수정: 추가 조치 불필요. 후속 pass에서 1차 출처를 붙일 수 있다.
- **head-R1 (minor)** 위치: head 근거 등급 박스 마지막 문장, tail QC "Physics independent review ... by a Sonnet-class critic ... item 5 FAIL on first pass".
  - 문제: 공개 페이지에 내부 검수 서사와 모델 계열명이 들어 있다. 사실이지만 독자에게 필요한 정보는 아니다.
  - 수정: 공개본에는 "독립 물리 검수 수행; 반영 후 재검수 PENDING" 정도만 남기고 1차 FAIL 이력과 모델명은 내부 기록으로 옮긴다. 게시 결정은 조정자 판단.
- **head-R2 (minor)** 위치: tail QC 항목 "KR→EN pairing ... writer self-check".
  - 문제: 이번 재검수에서 독립 확인했다(인접성 위반 0, lang 없는 문단 0).
  - 수정: "independent re-check DONE (2026-10-21)"로 갱신해도 된다. 표, h3 제목, chain 노드는 영어 전용이라는 한계는 그대로 남겨 두어야 한다.

## 4. UNKNOWN (이번에도 확인 못함)

- 출판사 페이지(ASM, MDPI, IOP)의 접근 조건. 이전과 같이 403 또는 bot challenge다. 본문이 "확인하지 못함"으로 정직하게 적었다.
- W41/W42 브랜치와의 DOI 중복. main 브랜치만 확인했다.
- CHE/DAHC 관례의 1차 문헌 대조.
- Render/PDF 빌드는 이번 점검 범위가 아니다(tail이 PENDING으로 표시).

## 5. 최종 요약

- 잔존 blocker 없음. B1(s5), s2-1, s4-1, s4-2, s1-1, s1-2, s4-4, s5-2, s5-3 모두 해소 확인.
- sources.yaml S5 주석 오류("4 days/2026-09-22" → 실제 10일 전/창 시작 2026-09-28)는 작업 범위 밖이라 여전히 manifest에서 정정해야 한다.
- 물리 재검증(sympy): s1 E1~E3, s2 비율·열확산, s3 계수·retention 동일성, s4 기울기·온도 부호, s5 1/D 이득과 단일 τ 식 모두 1차 검수 때와 같은 결과다.
