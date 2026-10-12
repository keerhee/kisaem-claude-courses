# 10주차 실습 파일 — HWP 문서 자동화(kordoc)

## inputs/ — 실습 입력
| 파일 | 원래 이름 | 쓰임 |
|---|---|---|
| template1_work_report.hwpx | 1_업무보고 양식.hwpx | 실습 A · patch |
| template3_one_page_report.hwpx | 3_보고서 양식.hwpx | 실습 B · patch |
| template2_cover_report.hwpx | 2_보고서 양식.hwpx | 실습 C · generate |
| plan_ai_training_virtual.pdf | 서울시_공무원_생성형_AI_활용_교육_계획서_gemini.pdf | 공통 원재료 (4쪽) |

> 계획서 PDF는 생성형 AI가 만든 **가상 문서**입니다. 기관명·일정·인원은 지어낸 값이므로
> 실제 근거로 인용하거나 외부로 내보내지 마십시오. 양식의 이름·전화번호는 자리표시 값입니다.

## answers/ — 강사용 예시 결과 (kordoc v4.18.0, 2026-10-01 실행)
- A_report1.hwpx / A_t1_new.md — 양식1 patch 결과 (14블록 변경, 재파싱 일치, validate 통과)
- B_report2_one_page.hwpx / B_t3_new.md — 양식3 patch 결과 (머리 글상자 1곳 SKIP)
- C_report3_cover.hwpx / C_plan_report.md — generate --preset 보고서 --cover 결과 (--date 미지정 시 날짜 불완전)
- plan.md, plan_chunks.json — PDF 변환·청크 결과 (62줄, 청크 18개)

## 순서 (Claude Code에게 말로 시킨다)
PDF 읽기 → 양식 구조 읽기(--keep-layout-tables) → 개조식 원고 → lint → patch/generate → validate → render 확인
