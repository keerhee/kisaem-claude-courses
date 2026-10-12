# 분류 기준 (Claude Code에게 그대로 전달)

각 기사(title + description)에 대해 아래 다섯 칸을 채운다. 기사 문장에 없는 내용은 추론하지 않는다.

| 칸 | 값 | 규칙 |
|---|---|---|
| topic | 통화정책 · 환율 · 부동산 · 기업실적 · 규제 | 하나만. 중앙은행·물가 → 통화정책, 대출 규제지만 주택시장이 주어면 부동산 |
| sentiment | 긍정 · 중립 · 부정 | 금융시장·해당 기업 입장 기준. 사실 전달·결정 발표는 중립 |
| entities | 기관·기업 이름 (쉼표) | 기사에 나온 이름만 |
| summary | 한 문장, 40자 이내 | 숫자는 원문 그대로 |
| evidence | 판단 근거가 된 원문 구절 | 원문에서 그대로 복사 |

출력: labeled.csv (id, topic, sentiment, entities, summary, evidence)
