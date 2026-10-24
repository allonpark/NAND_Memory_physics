# W43 수정 pass 재검수 (recheck.md)

재검수일: 2026-10-24 / 대상: sections의 i1~i5.html, report_head.html, report_tail.html 현재본 vs _prefinal(수정 전) 및 review.md, fixlog.md. 섹션 파일은 수정하지 않았다. 확인하지 못한 것은 UNKNOWN으로 남겼다.

## 0. 결론

| 항목 | 1차 판정 | 재검수 판정 | blocker | major | minor(잔여) |
|---|---|---|---|---|---|
| i1 | PASS-WITH-FIXES | PASS-WITH-FIXES | 0 | 0 | 1 (R1) |
| i2 | PASS-WITH-FIXES | PASS | 0 | 0 | 0 |
| i3 | PASS-WITH-FIXES | PASS | 0 | 0 | 0 (F3-4 수용, 참고 R4) |
| i4 | PASS-WITH-FIXES | PASS | 0 | 0 | 0 |
| i5 | PASS-WITH-FIXES | PASS-WITH-FIXES | 0 | 0 | 1 (R2) |
| head/tail | - | PASS-WITH-FIXES | 0 | 0 | 2 (R3, R5) |

잔존 blocker 없음. F1-1, F3-1, F5-1 모두 해소가 확인됐다. 수정이 새로 만든 출처 밖 주장은 발견하지 못했다. 남은 것은 모두 minor다.

근거 파일(scratchpad\w43\review\): re_markup.py(연결 문서 전체 점검), re_sym.py(곡률 항 sympy), diffp.py(수정 전후 문단 diff), pairs.py(KR/EN 쌍 출력).

## 1. 항목별 확인

### (1) F1-1 - 해소 (PASS)
- 논리: route A 신호가 "planar control는 1/E0 축에서 직선, 동축 소자는 R(lambda)로 보정한 abscissa R(lambda)/E0에서 직선"으로 바뀌었다. 표(competing mechanism), Expected signature, Falsification (a), 카드 Electrical signatures에 반영됐다(ko/en). Falsification (a)는 "보정하지 않은 축의 곡률만으로는 기각하지 않는다"를 명시해 이전의 자기모순이 사라졌다. 동축 소자에서 보정 축이 직선이 아니면 기각하므로 반증 가능성은 유지된다.
- 곡률 항 독립 재유도(re_sym.py, sympy 1.14.0): R(lambda) 급수를 lambda = phi_B/(q E0 r0)에 넣으면 ln(rate/E0^2) = 상수 + B(-1/E0 - 2 phi/(5 E0^2 q r0) - 4 phi^2/(35 E0^3 q^2 r0^2) - ...). E0^-2 계수가 -(2/5) B phi_B/(q r0)이며 본문 식과의 차이 0(True). 예전 11% 예시는 넣지 않았고 새 수치도 없다.
- 잔여 minor R1: "(phi_B와 r0를 함께 적합하거나 독립 측정값을 씀)". 두 parameter를 함께 적합하면 보정 축의 직선성이 자유도 두 개로 흡수되어 반증력이 약해진다. 수정: "r0는 TEM 등 독립 측정으로 고정하고 phi_B는 planar control 값을 우선 사용; 함께 적합하면 parameter 수와 허용 범위를 사전에 적는다"를 한 구절 보완(ko/en).

### (2) F3-1 - 해소 (PASS)
- i3 AUTHOR_INTERPRETATION (v)가 "초록(MOS transistor의 electron tunneling 모델링)과 맨 끝 요약 문단(quantum tunneling으로 전자가 주입되는 MOS transistor, avalanche photodiode)"으로 바뀌었다(ko/en 일치). 이번 pass의 내 재조회 2회에서도 도입부에는 없고 초록에 MOS tunneling, 요약 문단에 MOS와 APD가 있었다.

### (3) F5-1 - 복원이 정당함 (PASS)
- offset 100000으로 직접 다시 읽었다. Table III의 유일한 각주 a가 다음을 담는다(요약 도구 출력의 짧은 인용): "BV at Vgs = 0 V; Ids = 100 uA." / "Ron at Vgs = 15 V; Ids = 40 A." / "Qgd was extracted at Vds = 600 V, whereas Crss was extracted at Vds = 800 V." / "t_SC at Vds = 800 V, Vgs = 15 V, and Tmax = 1600 K." / "Isc and Tmax at t = 10 us." 이전 재조회가 놓친 것은 이 각주가 100000자 이후에 있어 내 offset 0 조회가 범위에 포함하지 않았기 때문이다. 1차 검수의 F5-1은 내 fetch 범위 한계에서 나온 UNKNOWN이었고 원 작성자의 값이 맞았다.
- 현재 i5: "BV 1423 -> 1685 V(Table III 각주: Vgs = 0 V, Ids = 100 uA; 곡선은 Fig. 3(c))", "Qgd 38 -> 22 nC(Table III 각주: Vds = 600 V에서 추출; Fig. 4(a)는 Vds 0-600 V 구간)"가 ko/en 모두에 있고 출처가 명시돼 SOURCE_REPORTED로 적절하다. 이전 UNKNOWN 문구는 잔존 0건이다. 이 값도 요약 도구 출력(조정자와 나, 2회 일치)이며 글자 그대로의 보장은 아니고, head에 같은 유보 문구가 있다.

### (4) 기타 finding 적용 상태 (fixlog 대조)
- F1-2, F1-3: 적용 확인(ko/en). F1-3은 저자의 establish 주장과 "DOE 반증 (c)가 이 주장을 겨냥" 문장이 쌍으로 있다. F1-4: phi_B, phi_t를 [J]로 수정(diff에서 J 토큰 변경과 일치).
- F2-1, F2-2: 아래 (5)에서 재현 확인. F2-3: 적용. F2-4: T05/T09 제거, 트랙 ID 잔존 0건.
- F3-2: roughness만 공칭 고정, 나머지 두께는 325/405 nm 반사율로 결정(재조회 일치). F3-5: 작업 노트 문구 삭제. 적용.
- F4-1, F4-2, F4-3, F4-4: 적용(아래 (5), diff 확인). F5-2: "선택된 JFET cutline(정확한 좌표는 본문에서 확인하지 못함)"으로 수용 가능. F5-3: 문구 유지. fixlog의 재조회가 "lower current after the initial peak ... reduces transient power dissipation"을 보고했으나 이번에 내가 독립 재확인하지는 못했다(UNKNOWN 유지, AUTHOR_INTERPRETATION 라벨 아래라 허용). F5-4, F5-5: 적용, 수용.
- F3-4: 등급 B 유지 + "저자 서술 기준, 적합값과 CI 없음, 보수적으로 읽으면 C에 가까움" 병기. 수용 가능.

### (5) 수정이 새로 넣은 문장 - 출처 밖 주장 점검
- **head "기호와 단위" 단락**: 새 수치 없음. 정의가 본문과 맞다: 항목 1 g0(x = t_N/r0, a = t_A/t_N, e = eps_A/eps_N), 항목 4 g = x/ln(1+x), 항목 5 t/(a ln(1+t/a)). 내 1차 검수에서 a=0이면 g0 = x/ln(1+x)이고, 항목 5 식은 t/a = x로 두면 항목 4 식과 동일하다. "단일층 극한에서 셋은 같다"는 항목 4와 5가 극한이 아니라 동일 식이므로 R5(minor)로 정정 권고. 나머지 기호 목록(항목 3의 x, g, 항목 2의 a, gamma, 항목 1·2·4의 B)은 각 항목 본문과 일치.
- **F4-1**: "+kT/2는 tau가 T^-1/2로 변한다는 가정에서만 나오며 tau가 T에 무관하면 없음". 1차 검수 sympy와 fixlog 재실행이 같다(tau 상수 -> Eg/2 - 3kT(F/F_Gamma)^2, tau ~ T^-1/2 -> +kT/2). "dE_a/dF<0 결론은 두 경우 모두 같다"도 맞다. PASS.
- **F4-2**: "0.107 MV/cm가 Ge/Si tunneling 접합에서 통상 기대되는 MV/cm급보다 낮아 보임"은 ENGINEERING_INFERENCE(배경 지식)로 라벨됐고, "지수가 105로 렌더링"은 내 fetch에서도 확인됐으며 "표기 오류 또는 다른 성분 가능성"은 UNKNOWN으로 라벨됐다. 1.067e5 V/cm = 0.1067 MV/cm 환산도 맞다. 출처 사실로 오인될 문장이 아니다. PASS.
- **i5 gamma [cm/MV]**: "TDDB 전계 가속 계수 gamma [cm/MV], Weibull shape beta(무차원)가 원문에 없으므로 수명 이득은 계산하지 않음, 이 gamma는 항목 2의 gamma와 다른 기호". 원문에 TDDB 모델이 없다는 진술은 내 fetch로 확인했다. 단위 [cm/MV]는 E-model 관행에 대한 가정이며 부정 진술에 붙은 것이라 허용 가능하나 R2(minor)로 가정 표기를 권고.
- **i2 Monte Carlo 문장**: "beta = 2, 수준당 2,500회, n = 10에서 sd(ln b)·sqrt(n) 약 0.87, beta_hat 평균 약 17% 높음, 검출 비 약 2.97-2.98배(점근 2.66배)". 내 1차 MC(seed 3: 0.868, +17%, 2.97)와 fixlog MC(seed 43: 0.871, +17.1%, 2.98)가 모두 이 범위를 지지한다. 표시된 유도로 라벨됨. PASS.
- **i3 F3-3 승격(UNKNOWN -> SOURCE_REPORTED)**: 이번 pass에서 서로 다른 질문으로 2회 더 재조회했고 모두 같은 내용이었다: 한 primary electron이 둘 이상의 이차전자를 만들 확률이 무시 가능하다는 가정에서 식 (2)가 g와 이온화율을 잇고, 저자들은 이것이 "wavelengths longer than 250 nm"에서 성립한다고 쓴다. 1차 검수 1회, 이번 2회, fixlog 1회로 총 4회 일치한다. 그러나 모두 요약형 도구 출력이며 글자 그대로의 원문 확인은 아니다. 본문이 "요약형 추출 도구 재조회 두 번에서 확인, 원문 문장 그대로라고 보장하지는 않음"을 명시하므로 라벨 강도가 적절하다. 판정: 승격 수용(PASS), 단 여전히 summarizer-level 확인이다.
- 그 밖: i3 변수 단락의 "이 항목의 g는 impact ionization 기여분이며 항목 1·4의 field 비가 아님", i4의 "x는 이 줄에서만 t/r_in, 다른 곳은 길이 방향 위치 [nm]"는 정의 문장이고 수치가 없다. i5 New vs known에서 신규성 판단을 ENGINEERING_INFERENCE로 이동한 문장도 적절하다. fixlog F절의 토큰 diff가 각 finding에 대응된다.

### (6) KR/EN 의미 이탈 점검 - 이탈 0건 (15쌍 확인)
i1 Expected signature+Falsification (a), i1 AUTHOR_INTERPRETATION, i1 route A 표 행, i2 [8] Monte Carlo, i3 (v), i3 변수·validity(F3-3), i3 CONFIDENCE, i4 구조 SOURCE_REPORTED, i4 Governing 변수·validity, i4 labeled derivation, i5 SOURCE_REPORTED(Table III 각주), i5 Failure mode, i5 CONTRADICTING DATA, head "기호와 단위", head 배너. 수치(2.97-2.98, 0.87, 17%, 100 uA, 600 V, 0.107 MV/cm, 0.863, 13.8%)와 조건절(planar control/동축, tau 가정, 요약 도구 보장 없음)이 ko와 en에서 일치한다.

### (7) 형식·누수 (re_markup.py, head+i1~i5+tail 연결)
- 태그 불균형 0, 미종료 0, inline style/script 0, 미정의 클래스 0, 중복 id 0, 미해결 anchor 0.
- ko->en 인접성: ko 272 / en 272, 위반 0, lang 없는 p 0.
- 금지 문자열: S1..S5 패턴 매치 2건은 모두 S^2 표기(false positive). W43-S, sources.yaml, 파일 경로, 모델명, 트랙 ID(T0x, T10), ARCHIVE_GAP, notes/session/세션/노트 모두 0건.
- .qc 블록: 항목 파일 0건, report_tail 1건(보고서 단위 QC).
- 등급: A-D만 사용, E/F 0건. 합니다체: 평서체 종결 0건. 카드: 5개 모두 13행(fixlog selfcheck와 일치, 이번에는 구조 점검만 다시 했고 셀 쌍은 p 인접성 점검으로 갈음).

## 2. 잔여 finding (모두 minor)
- **R1 (i1)** 위치: Expected signature의 "(phi_B와 r0를 함께 적합하거나 독립 측정값을 씀)". 수정: "r0는 독립 측정(TEM 등)으로 고정, phi_B는 planar control 값을 우선; 함께 적합하면 parameter 수와 허용 범위를 사전에 적고 반증력 저하를 명시".
- **R2 (i5)** 위치: Failure mode (a)의 "gamma [cm/MV]". 수정: "[cm/MV] (E-model 관행의 단위 가정; 원문에는 TDDB 모델이 없음)".
- **R3 (head/tail)** 위치: head 배너 "반영 결과의 재검수는 아직 하지 않았습니다(PENDING)"와 tail QC "re-check PENDING". 이번 재검수가 수행됐으므로 게시 전에 "재검수 수행(잔존 blocker 없음)"으로 갱신 가능. 갱신 여부는 조정자 판단.
- **R4 (i3/head/tail)** 등급 B 유지는 수용한다. head의 "the only grade B" 문구와 tail 표가 항목 3을 B로 일관되게 적고 있는지만 조정자가 한 번 더 확인할 것(이번 diff에서 해당 문구는 변경되지 않았음).
- **R5 (head)** 위치: "기호와 단위"의 "단일층 극한에서 셋은 같습니다". 수정: "항목 4와 5의 식은 x = t/r_in = t/a로 놓으면 동일하고, 항목 1의 g0는 a = 0(단일층)에서 x/ln(1+x)로 환원됩니다"(ko/en).

## 3. UNKNOWN
- F5-3의 "첫 peak 이후 전류 감소와 과도 전력 감소" 표현: 독립 재확인 못함(fixlog의 단일 보고뿐). AUTHOR_INTERPRETATION 라벨 아래라 허용.
- 요약형 도구 출력은 전부 글자 그대로의 원문 확인이 아니다(Table III 각주, 250 nm 문장 포함).
- W42 브랜치 중복(브랜치 없음). Render/PDF 점검은 이번 범위 밖.

## 4. 최종 요약
- 잔존 blocker 없음. F1-1, F3-1, F5-1 해소 확인, 나머지 finding은 로그대로 적용됐거나 수용 가능하다.
- 판정: i1 PASS-WITH-FIXES(R1), i2 PASS, i3 PASS, i4 PASS, i5 PASS-WITH-FIXES(R2), head/tail PASS-WITH-FIXES(R3, R5).
