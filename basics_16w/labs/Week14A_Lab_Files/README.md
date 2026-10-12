# 14주차 1부 실습 파일 — 웹 크롤링

| 파일 | 용도 |
|---|---|
| sample_site/list_p1.html · list_p2.html | 가상 기관 보도자료 목록 2쪽 (실습용 정적 페이지) |
| sample_site/robots.txt | 실습용 robots.txt (Crawl-delay 2) |
| answers/crawl_press.py | robots 확인 → 목록 파싱 → 다음 쪽 → csv 저장 |
| answers/CLAUDE.md | 크롤링 폴더 규칙 예시 |

## 실습 순서 (Claude Code에게 말로 시킨다)
1. "sample_site/list_p1.html을 열어 게시판 구조를 설명해 줘" — 표·행·제목 선택자 확인
2. "robots.txt를 확인하고, 허용되면 두 쪽 모두 모아 csv로 만들어 줘. 요청 간격 2초"
3. 결과 20건 · 번호 중복 없음 · 수집일시 열 확인
4. (선택) 실제 기관 게시판에 적용하기 전에 API·RSS가 있는지 먼저 묻는다

필요 패키지: beautifulsoup4, pandas (실제 사이트는 requests 추가)
기대 결과: 1쪽 10건 + 2쪽 10건 = 20건
