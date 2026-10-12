# 15주차 실습 파일 — 리서치 에이전트 · 예약 작업 · 뉴스레터

데이터 파일은 없습니다. 12주차 실습 폴더의 수집 코드와 키(.env)를 그대로 씁니다.

## 준비
1. 12주차 `answers/` 폴더 내용(common.py, fetch_*.py, rate_gap.py, dart_monitor.py, watchlist.csv, .env)을
   이 폴더의 `answers/`에 복사한다.
2. Gmail 커넥터(8주차)가 연결돼 있어야 실습 2의 메일 초안 단계가 동작한다.

## 구성 (answers/)
| 파일 | 용도 |
|---|---|
| .claude/agents/macro-researcher.md | 거시 지표 연구원 |
| .claude/agents/disclosure-researcher.md | 공시 연구원 |
| .claude/agents/news-researcher.md | 뉴스 연구원 (웹 검색) |
| .claude/agents/fact-checker.md | 검증 담당 — 판정표만 작성 |
| newsletter_template.md | 뉴스레터 양식 |
| CLAUDE.md | 폴더 규칙 · 실행 순서 |
| schedule_prompt.txt | 예약 작업에 넣을 단독 실행 프롬프트 |
| run_weekly.sh | OS cron + claude -p 예시 |

## 실습 순서
1. `claude` 실행 → `/agents`로 네 에이전트가 보이는지 확인
2. "CLAUDE.md 순서대로 이번 주 뉴스레터 초안을 만들어 줘" → 결과와 판정표 확인
3. schedule_prompt.txt 내용으로 매주 월요일 07:50 예약 작업 생성 → 지금 한 번 실행해 확인
4. 사람 검토 후 직접 발송

서브에이전트 파일 형식은 Claude Code 공식 문서(sub-agents) 기준입니다. 예약 방식별 차이는 덱 3부를 참고하세요.
