# 16주차 3부 실습 파일 — 웹 대시보드 배포 · 최종 발표 · 거버넌스

> 대시보드 · HTML MVP를 **만드는 법**은 16주차 1부(`../Week16A_Lab_Files`)에서 다루고, 발표 영상을 만드는 법은 16주차 2부(`../Week16B_Lab_Files`)에서 다룹니다. 3부는 12 · 15주차 산출물로 갱신되는 대시보드를 배포하고, 거버넌스와 최종 발표로 과정을 마무리합니다.

## 구성
| 파일 | 용도 |
|---|---|
| answers/build_dashboard.py | 12·15주차 산출 csv로 한 장짜리 HTML 대시보드 생성 (외부 라이브러리 없음) |
| AI_Use_Register_template.xlsx | AI 업무 대장 양식 · 작성 기준 |
| Final_Presentation_Guide.md | 최종 발표 형식 · 평가 기준 |

## 실습 순서
1. `build_dashboard.py`를 15주차 폴더(answers/)에 복사
2. `python build_dashboard.py --demo` 로 화면 확인 (가상 데이터)
3. `python rate_gap.py 2020-01-01 && python dart_monitor.py 7 && python build_dashboard.py` → 실제 데이터
4. 배포: 공개 자료만 담긴 경우 Claude 아티팩트(비공개 링크)로 게시, 내부 자료가 있으면 사내 서버
5. 15주차 예약 작업 프롬프트 끝에 "build_dashboard.py를 실행해 대시보드를 갱신한다"를 추가
6. AI 업무 대장에 자기 업무 한 줄 작성

데모 화면의 금리 값은 화면 확인용 가상 데이터입니다.
