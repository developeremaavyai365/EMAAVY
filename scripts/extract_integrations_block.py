"""Find integrations section boundaries in main HTML."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "emaavy_white_blue (2).html"
s = HTML.read_text(encoding="utf-8")

start = s.find("<!-- INTEGRATIONS HUB -->")
end = s.find("<!-- AGENTS -->")
print("start", start, "end", end, "len", end - start)
chunk = s[start:end]
# markers
for mid in [
    "integration-telephony",
    "integration-llm",
    "integration-stt",
    "integration-tts",
    "integration-tools",
]:
    i = chunk.find(mid)
    print(mid, i)
