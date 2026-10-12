# 16주차 1부 실습 파일 — 업무 대시보드와 HTML MVP

PRD 한 장 → 한 파일 HTML → 대조 · 판정 순서로 **대시보드 1개와 업무 MVP 1개**를 만듭니다.
앞 주차의 가상 자료를 다시 씁니다(7주차 PE 현금흐름 · 11주차 출자 명단). API 키는 필요 없습니다.

## 구성
| 파일 | 용도 |
|---|---|
| PRD_template.md | PRD 일곱 칸(목적 · 사용자 · 입력 · 핵심 기능 · 판정 규칙 · 성공 기준 · 제외 범위) |
| Artifact_Path_Prompts.md | 경로 A — 코드 없이 Claude 앱 Artifact로 시안 만들기 |
| MVP_Review_Sheet.md | 시연 판정표 7항목 + 사용자 피드백 3개 → PRD 개정 |
| data/Week07_PE_Cashflows_input.xlsx | 7주차 입력 그대로 (현금흐름 128건 · 6개 펀드) |
| data/capital_call_roster.xlsx | 11주차 명단 그대로 (20건, 13번은 약정 초과 — 일부러 넣은 오류) |
| answers/PRD_fund_dashboard.md · PRD_capital_call_mvp.md | 완성 PRD 예시 |
| answers/build_fund_dashboard.py · fund_dashboard_template.html | 실습 1 대시보드 생성 (계산은 스크립트, 화면은 표시) |
| answers/check_dashboard.py | 대시보드 숫자를 7주차 Excel 정답과 따로 대조 |
| answers/review_engine.py · rules.json · capital_call_mvp_template.html | 실습 2 MVP — 엔진 판정 + 화면 + 마감 대조(`--close`) |
| answers/out/ | 완성 화면 2개 (더블클릭으로 바로 열림) |
| answers/CLAUDE.md | 폴더 규칙 예시 |

## 실습 1 — 대시보드 (40분)
1. PRD_template.md를 Claude Code와 인터뷰 방식으로 채운다 (완성 예시와 비교)
2. "이 PRD대로 한 파일 HTML 대시보드를 만들어 줘. 계산은 파이썬 스크립트가 하고 화면은 표시만 하게 해 줘."
3. `python answers/build_fund_dashboard.py` → 기대 결과: 전체 TVPI 1.40배 · 납입 551.7 · 분배 387.6 · NAV 384.7
4. `python answers/check_dashboard.py` → 기대 결과: 대조 43칸 · 불일치 0 · 판정 통과
5. 전략 필터를 눌러 Credit TVPI 1.09배가 Excel '전략별' 시트와 같은지 눈으로 한 번 더 본다

## 실습 2 — 업무 MVP (50분)
1. PRD ⑤ 판정 규칙을 rules.json으로 옮긴다
2. `python answers/review_engine.py` → 기대 결과: 20건 · 요청액 149.7 · 통과 16 · 확인 필요 3(1·8·17번) · 차단 1(13번, 잔액 −2.0)
3. out/capital_call_mvp.html을 열어 판정한다 — 13번은 승인 버튼이 꺼져 있고, 확인 필요 건은 사유 없이 승인되지 않는다
4. '판정 내보내기' → `python answers/review_engine.py --close decisions_<실행번호>.csv`
   → 기대 결과(13번 반려 · 20번 보류 · 나머지 승인): 판정 20/20 · 승인 18건 · 승인 요청액 112.9 · 마감
5. 옆 사람에게 5분 시연하고 MVP_Review_Sheet.md를 채운다 → PRD를 한 줄 고쳐 v1로 다시 실행

필요 패키지: openpyxl (화면은 브라우저만 있으면 됨)
판정 기록은 브라우저 저장소에 실행 번호별로 남습니다. 다른 PC에서 이어서 하려면 CSV로 내보내 옮깁니다.
모든 펀드 · 운용사 · 담당자 · 금액은 실습용 가상 데이터입니다.
