# team-ai-marketplace (예시)

팀 공용 플러그인 저장소 예시. git 저장소(사내 GitHub 등)로 올려 팀원이 설치한다.

## 개발 중 시험
    claude --plugin-dir ./plugins/finance-team

## 팀원 설치 (저장소를 올린 뒤)
    /plugin marketplace add <조직>/<저장소>
    /plugin install finance-team@team-ai-marketplace

## 규칙
- 스킬·에이전트를 고치면 plugin.json의 version을 올리고 변경 내용을 커밋 메시지에 적는다.
- 새 스킬은 AI 업무 대장(16주차)에 한 줄 등록한 뒤 추가한다.
- 키·개인정보·내부 자료는 플러그인에 넣지 않는다.
