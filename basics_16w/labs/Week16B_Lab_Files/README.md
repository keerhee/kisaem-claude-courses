# 16주차 2부 실습 파일 — 발표 영상 만들기 (Claude Code에게 시키기)

최종 발표(16주차 3부)에 쓸 **5분 발표 영상**을 Claude Code에게 시켜 만듭니다.
녹화 한 번으로 끝까지 말하는 방식이 아니라, **장면(HTML) + 문장 단위 나레이션**을 이어 붙이는 방식입니다.
문장 하나를 고치면 그 문장만 다시 만들면 되고, 길이와 음량이 늘 일정하며, 자막이 저절로 생깁니다.

> 참고한 방식: NeoMatrix 시리즈 소개영상 — 장면마다 문장이 하나 나올 때마다 화면 요소가 하나씩 드러난다.

## 준비
- 9주차 환경(Claude Code · Python · git) + `ffmpeg` · Google Chrome
- 음성: edge-tts(인터넷 필요) · 막히면 macOS 내장 음성(say, Yuna) · 본인 복제 음성(Voicebox)은 본인 동의와 회사 승인이 있을 때만
- 내 업무 자료: 16주차 1부에서 만든 PRD · 화면 · 대조 결과 (없으면 1부 완성본으로 연습)

## Claude Code에게 시키는 순서 (각 단계가 끝나면 결과를 눈으로 확인한 뒤 다음으로)

**1. 대본** — 내용은 사람이 정하고, 형식은 Claude가 맞춘다
```text
"Week16C_Lab_Files/Final_Presentation_Guide.md의 5단계(문제 · 전후 · 시연 · 검증 · 거버넌스)에 맞춰
내 업무 발표 대본을 script.json으로 써 줘. 표지까지 장면 6개, 장면마다 문장 4–7개, 문장은 15–45자.
숫자와 영문 약어는 읽는 대로 한글로 쓰고, 숫자로 시작하는 문장은 만들지 마.
문장마다 몇 번째 화면 요소가 보일지 steps로 적고, 전체 예상 길이를 표로 보여 줘."
```
→ 확인: 장면별 문장 수 · 예상 길이(5분 이내) · 숫자 읽기

**2. 장면** — 문장 하나 = 화면 요소 하나
```text
"script.json의 장면마다 1920×1080 HTML 장면을 scenes.html 한 파일로 만들어 줘.
?s=장면ID&k=단계로 열면 data-s가 k 이하인 요소만 보이게 해. 글자는 21px 이상, 색의 의미는 고정
(주황 핵심 숫자 · 초록 좋아진 것 · 빨강 문제). 모든 장면 오른쪽 위에 'AI 합성 음성 · 가상 자료'를 넣고,
다 만들면 장면마다 마지막 단계를 스크린샷해 모아보기 한 장으로 보여 줘."
```
→ 확인: 모아보기에서 글자 넘침 · 겹침 · 빈 공간

**3. 음성** — 문장마다 파일 하나
```text
"tts.py를 만들어 script.json의 문장마다 음성 파일을 out/_sent/에 따로 만들어 줘.
엔진은 edge-tts(ko-KR-InJoonNeural), 인터넷이 막히면 macOS say로. 문장이 바뀐 것만 다시 만들고,
첫머리 잡음이나 너무 짧은 문장은 다시 만들어 보고 그래도 안 되면 목록으로 알려 줘."
```
→ 확인: 실패 목록이 비었는지 · 문장 두세 개를 직접 들어 보기

**4. 렌더** — 문장 시작에 맞춰 화면이 바뀐다
```text
"render.py를 만들어 줘. 장면마다 단계별 스크린샷을 찍고, 새 단계는 그 단계를 쓰는 첫 문장 0.1초 전부터
0.4초 동안 겹쳐 나타나게. 첫 문장 전 0.5초, 문장 사이 1초, 마지막 문장 뒤 1.95초, 장면은 검은 화면에서
열고 닫아. 전체를 이어 붙여 음량을 −16 LUFS로 맞추고, 문장 시각으로 자막 srt도 만들어 줘. 5분 넘으면 경고해."
```
→ 확인: 길이 · 자막 · 몇 군데 프레임을 뽑아 화면과 말이 맞는지

**5. 시연 녹화 섞기** — 실제 화면은 녹화로
```text
"DEMO 장면은 HTML 대신 내 녹화 파일 clips/demo.mp4를 쓰게 render.py를 고쳐 줘. 녹화가 나레이션보다 짧으면
마지막 화면을 멈춰 두고, 길면 알려 줘. 그리고 DEMO 문장마다 몇 초에 시작하는지 표로 보여 줘 —
그 시각에 맞춰 다시 녹화할게."
```
녹화: macOS `Cmd+Shift+5` → 선택 부분 기록 · Windows 11 캡처 도구 → 녹화(또는 `Win+Alt+R`)

**6. 고치기** — 문장 하나만 바꿔 다시
```text
"PROBLEM 장면 세 번째 문장을 '…'로 바꾸고, 그 문장 음성과 그 장면만 다시 만들어 최종 영상을 갱신해 줘."
```

## 완성본 (answers/)
| 파일 | 내용 |
|---|---|
| out/final_presentation.mp4 · .srt | 예시 발표 영상 3분 4초 (1부 캐피털콜 MVP 발표, edge-tts, −15.8 LUFS, 자막 35줄) |
| script.json · scenes.html | 예시 대본 6장면 35문장 · 장면 HTML |
| out/contact_sheet.png | 장면 모아보기 |
| clips/demo_mvp.mp4 · record_demo.py | 시연 장면 — 1부 MVP를 나레이션 시각에 맞춰 자동 조작하며 녹화(Playwright) |
| tools/tts.py · tools/render.py | 3–5번 프롬프트로 Claude Code가 만들 결과의 예 (막히면 이것으로 진행) |
| templates/ | 내 발표용 빈 대본 · 장면(○○ 칸을 채움) |

완성본으로 다시 만들기 (Week16B_Lab_Files에서):
```bash
uv run --with edge-tts python answers/tools/tts.py answers/script.json
uv run --with playwright python answers/record_demo.py        # 시연 장면 (16주차 1부 MVP 필요)
python answers/tools/render.py answers/script.json             # → answers/out/final_presentation.mp4
```

점검은 `Video_Checklist.md`, 최종 제출은 `../Week16C_Lab_Files/Final_Presentation_Guide.md`를 따릅니다.
화면의 펀드 · 금액은 모두 가상 자료입니다.
