# 12주차 실습 파일 — 공개 API 데이터 파이프라인

데이터 파일은 없습니다. 각자 발급한 인증키로 직접 받아 옵니다.

## 준비 (수업 전 키 발급)
| 기관 | 신청 위치 | 비고 |
|---|---|---|
| OpenDART | opendart.fss.or.kr → 인증키 신청 | 개인 즉시 발급, 일 2만 건 |
| 한국은행 ECOS | ecos.bok.or.kr/api → 인증키 신청 | 발급 직후 잠시 막힐 수 있음 |
| FRED | fred.stlouisfed.org → My Account → API Keys | 무료 계정 |
| 공공데이터포털 | data.go.kr → API별 활용신청 | 인코딩·디코딩 키 2종 |

## 구성 (answers/)
| 파일 | 용도 |
|---|---|
| common.py | .env 읽기 · 원본 저장 · 실행 기록 |
| fetch_ecos.py · fetch_fred.py | 한 계열 받기 |
| rate_gap.py | 한미 정책금리 차 표·차트 (ECOS 722Y001 − FRED DFEDTARU) |
| dart_monitor.py · watchlist.csv | 관심 기업 최근 공시 표 |
| CLAUDE.md · .env.example · .gitignore | 폴더 규칙 · 키 형식 · git 제외 |

## 실습 순서 (Claude Code에게 말로 시킨다)
1. `.env.example`을 `.env`로 복사하고 키 입력 → "키가 git에 안 들어가는지 확인해 줘"
2. "ECOS 기준금리와 FRED 연방기금 목표 상단으로 한미 금리차 표와 차트를 만들어 줘"
3. "watchlist.csv 기업의 최근 7일 DART 공시를 표로 만들어 줘"
4. 최신 값 하나를 ECOS · FRED · DART 웹 화면과 직접 대조 → 커밋

필요 패키지: requests, pandas, matplotlib
스크립트는 각 기관 문서의 응답 형식으로 모의 응답 테스트를 마쳤습니다. 실제 호출 결과는 키와 날짜에 따라 다릅니다.
