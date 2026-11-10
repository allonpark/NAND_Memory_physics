# W42 감사 자료 (외부 감사용)

`reports/2026/w42/index.html`이 거친 근거와 검증의 기록입니다.

| 경로 | 내용 |
|---|---|
| `sources.yaml`, `rejected.md` | 출처 5건(DOI/arXiv, 날짜, 접근 수준, 신규/archive-gap)과 탈락 후보. manifest의 알려진 오류는 파일 머리말의 ERRATA에 적었습니다 |
| `fulltext_notes/` | 본문을 읽은 항목의 추출 노트 |
| `review/review.md`, `review/recheck.md` | 독립 검수(1차 FAIL 1건: 수치 크기 오류)와 수정에 대한 집중 재검수 |
| `fixlog.md` | 수정 기록(3차까지) |
| `notes/` | 작성자의 SOURCE_REPORTED, UNKNOWN 목록과 약점 |
| `scripts/` | SymPy 검산 스크립트와 실행 출력, 점검 스크립트 |

기록해 둘 사항:
- 1차 검수는 "원문에 '가장 유망'이라는 평가가 없다"고 했으나 **원문에는 해당 문장이 있었고**, 재검수가 이를 바로잡아 항목 2에 SOURCE_REPORTED로 복원했습니다(`fixlog.md`의 정정 기록).
- 재검수 이후의 마지막 minor 수정(3차)은 독립 재검수 없이 기계 점검만 받았습니다.
- 작성 중간 파일은 에이전트 기록에서 복구했고 Bash 수정분은 복구되지 않아 일부가 다를 수 있습니다. 최종 본문은 위 검수를 거친 상태 기준입니다.
- 항목 3은 초록만 읽었습니다(출판사 403, 우회하지 않음). 그림은 읽지 못했습니다.
- `scripts/`의 로컬 경로는 `<local-path>`로 치환되어 그대로 실행되지는 않습니다.
