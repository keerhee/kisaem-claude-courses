# 13주차 실습 파일 — API 자료로 보고 양식 엑셀 채우기

| 파일 | 용도 |
|---|---|
| Monthly_Macro_Report_template.xlsx | 월간 거시 보고 양식 (노란 칸 = 입력, 회색 칸 = 수식, 검증 칸) |
| answers/mapping.csv | 어느 자료를 어떻게 집계해 몇 행에 넣는가 |
| answers/fill_template.py | 일별 자료 → 월 집계 → 양식 사본에 채우기 |
| answers/CLAUDE.md | 폴더 규칙 예시 |

## 준비
- 12주차 answers/의 common.py · fetch_ecos.py · fetch_fred.py · .env를 이 폴더의 answers/로 복사한다.
- 키 없이 흐름만 볼 때는 `--demo` (가상 자료).

## 실습 순서
1. `python fill_template.py 2026-09 --demo` → Monthly_Macro_Report_2026-09.xlsx 열어 서식·검증 칸 확인
2. `python fill_template.py 2026-09` → 실제 자료
3. 원/달러 월평균 하나를 ECOS 화면과 대조해 비고에 기록

주의: 양식 원본은 덮어쓰지 않는다. 결과는 사본으로만 만든다. 수식 칸 값은 엑셀(또는 LibreOffice)로 열 때 계산된다.
필요 패키지: pandas, numpy, openpyxl (실제 자료는 requests 추가)
