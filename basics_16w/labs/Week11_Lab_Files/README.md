# 11주차 실습 파일 — 문서 대량 생성과 결과물 세트

| 파일 | 용도 |
|---|---|
| capital_call_roster.xlsx | 가상 출자 펀드 20건 명단 (1건은 약정 초과 요청 — 일부러 넣은 오류) |
| capital_call_letter_template.docx | 납입 계획 통보 공문 양식 ({{ }} 자리표시자) |
| answers/mail_merge.py | 명단 행마다 공문 1건 생성 · 검증 · (선택) PDF 변환 |
| answers/build_set.py | 처리 결과 한 원천(summary.json) → Word 보고서 + PPT 요약 · 숫자 대조 |
| answers/CLAUDE.md | 폴더 규칙 예시 |

## 실습 순서
1. "양식의 자리표시자와 명단의 열이 맞는지 먼저 대조해 줘"
2. `python answers/mail_merge.py capital_call_roster.xlsx capital_call_letter_template.docx --pdf`
   → 기대 결과: 생성 19건 / 명단 20건, 13번 제외(미납 약정 -2.0), 합계 117.0 + 32.7 = 149.7
3. 생성된 공문 3건을 무작위로 열어 명단과 대조
4. `python answers/build_set.py` → Word·PPT 숫자 일치 '예' 확인

필요 패키지: pandas, openpyxl, docxtpl, python-docx, python-pptx (PDF는 LibreOffice)
HWPX 공문은 10주차(kordoc)의 fill 기능으로 같은 흐름을 적용합니다.
모든 기관·펀드·담당자는 가상입니다.
