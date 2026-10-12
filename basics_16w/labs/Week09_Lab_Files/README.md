# 9주차 실습 파일 — Claude Code 개발환경

## 구성
| 파일 | 용도 |
|---|---|
| Week07_PE_Cashflows_input.xlsx | 7주차와 같은 가상 PE 현금흐름 (입력) |
| GP_reports/F01·F03·F05_2026Q3.xlsx | 가상 운용사 분기 보고서 3개 (B2 펀드ID, B5 NAV) |
| answers/CLAUDE.md | 실습 폴더용 CLAUDE.md 예시 |
| answers/.gitignore | git 제외 목록 예시 |
| answers/pe_summary.py | 7주차 요약 시트를 Python으로 재계산 |
| answers/collect_nav.py | 7주차 VBA CollectNAV를 Python으로 옮긴 버전 |

## 실습 순서 (모두 Claude Code에게 말로 시킨다)
1. 이 폴더에서 `claude` 실행 → `/init` 으로 CLAUDE.md 초안 생성 → answers/CLAUDE.md와 비교
2. "이 폴더를 git으로 관리해 줘. .env·산출물은 제외" → 첫 커밋
3. "7주차 요약 시트를 Python으로 다시 계산해 줘" → Excel 답안과 숫자 대조
4. "Week07_Collect_NAV.bas를 Python으로 옮겨 GP_reports를 읽게 해 줘" → 결과 확인 후 커밋

## 확인값
- 재계산 TVPI: F01 1.52 · F02 1.76 · F03 1.10 · F04 1.36 · F05 1.52 · F06 1.06 (7주차 Excel 답안과 일치)
- NAV 수집 후: F01 34.9→36.2, F03 61.5→62.8, F05 127.6→131.4 (3개 갱신)

모든 펀드·수치는 가상 데이터입니다. 필요 패키지: pandas, openpyxl
