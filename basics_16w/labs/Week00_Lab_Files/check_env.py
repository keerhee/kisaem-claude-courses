"""수강생 실습 환경 점검 (사전 세팅 세션).

실행: python check_env.py            → 화면 표시 + env_report.txt 저장
      python check_env.py --net      → 주요 사이트 접속까지 확인 (회사망 방화벽 점검)
키 값은 출력하지 않는다. '있음/없음'만 표시한다.
"""
import sys, shutil, subprocess, importlib, platform, datetime as dt
from pathlib import Path

OK, NG, OPT = "OK  ", "없음", "선택"
rows = []


def add(group, item, ok, note="", optional=False):
    rows.append((group, item, OK if ok else (OPT if optional else NG), note))


# 1) Python
v = sys.version_info
add("Python", f"버전 {v.major}.{v.minor}", v >= (3, 10), "3.10 이상 필요")

# 2) 패키지 (주차)
for mod, week in [("pandas", "7·9주차"), ("openpyxl", "7·9주차"), ("requests", "12주차"), ("matplotlib", "12주차"),
                  ("bs4", "14주차 1부"), ("docxtpl", "11주차"), ("docx", "11주차"), ("pptx", "11주차")]:
    try:
        importlib.import_module(mod); add("패키지", mod, True, week)
    except Exception:
        add("패키지", mod, False, f"{week} — pip install {'beautifulsoup4' if mod=='bs4' else 'python-docx' if mod=='docx' else 'python-pptx' if mod=='pptx' else mod}")

# 3) 명령
def ver(cmd):
    try:
        return subprocess.run([cmd, "--version"], capture_output=True, text=True, timeout=20).stdout.strip().splitlines()[0]
    except Exception:
        return ""
for cmd, need, optional in [("claude", "9주차 — Claude Code", False), ("git", "9주차", False),
                            ("node", "kordoc(npx) — 10주차", True), ("soffice", "PDF 변환 — 선택", True)]:
    path = shutil.which(cmd)
    add("명령", cmd, bool(path), (ver(cmd) or need) if path else need, optional)

# 4) 키 (.env) — 값은 표시하지 않음
env = {}
for p in [Path(".env"), Path("answers/.env")]:
    if p.exists():
        for line in p.read_text(encoding="utf-8").splitlines():
            if "=" in line and not line.startswith("#"):
                k, val = line.split("=", 1); env[k.strip()] = bool(val.strip())
for k, week in [("DART_API_KEY", "12주차"), ("ECOS_API_KEY", "12주차"), ("FRED_API_KEY", "12주차"),
                ("NAVER_CLIENT_ID", "14주차 2부"), ("NAVER_CLIENT_SECRET", "14주차 2부")]:
    add("키", k, env.get(k, False), week, optional=k.startswith("NAVER"))

# 5) 접속 (선택)
if "--net" in sys.argv:
    import urllib.request
    for host in ["https://claude.ai", "https://pypi.org", "https://opendart.fss.or.kr", "https://ecos.bok.or.kr",
                 "https://api.stlouisfed.org", "https://openapi.naver.com"]:
        try:
            urllib.request.urlopen(urllib.request.Request(host, method="HEAD"), timeout=8); ok = True
        except Exception as e:
            ok = hasattr(e, "code")          # 403/404 등 응답이 오면 '도달'은 한 것
        add("접속", host.replace("https://", ""), ok, "회사망 방화벽 확인")

lines = [f"환경 점검 {dt.datetime.now():%Y-%m-%d %H:%M} · {platform.system()} {platform.release()}", ""]
for g, i, s, n in rows:
    lines.append(f"[{s}] {g:<6} {i:<22} {n}")
need = [r for r in rows if r[2] == NG]
lines += ["", f"필수 항목 미비 {len(need)}개" + (" — 수업 전에 해결하세요." if need else " — 준비 완료.")]
print("\n".join(lines))
Path("env_report.txt").write_text("\n".join(lines), encoding="utf-8")
sys.exit(1 if need else 0)
