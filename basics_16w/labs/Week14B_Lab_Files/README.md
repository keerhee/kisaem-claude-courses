# 14주차 2부 실습 파일 — 뉴스 수집 × LLM 구조화

| 파일 | 용도 |
|---|---|
| sample_news.csv | 가상 기사 20건 (제목·요약·날짜·매체) — 키 없이 분류 실습 |
| schema.md | 분류 기준 5칸 (topic · sentiment · entities · summary · evidence) |
| answers/news_search.py | 네이버 뉴스 검색 API 수집 (제목·요약·링크만) |
| answers/answer_key.csv | 20건의 정답 topic · sentiment |
| answers/check_labels.py | Claude 결과와 정답 비교 → 일치율 · 불일치 기사 |
| answers/CLAUDE.md | 폴더 규칙 예시 |

## 실습 순서
1. "schema.md 기준으로 sample_news.csv 20건을 분류해 labeled.csv로 저장해 줘. 근거 구절도 원문에서 복사해"
2. `python answers/check_labels.py labeled.csv answers/answer_key.csv` → 일치율 확인
3. 불일치 기사를 보고 schema.md 규칙을 한 줄 고친 뒤 다시 분류 → 일치율 비교
4. (선택) 네이버 검색 API 키로 실제 키워드 50건 수집 → 같은 기준으로 분류

필요 패키지: pandas (실제 수집은 requests)
모든 기사는 실습용 가상 기사입니다.
