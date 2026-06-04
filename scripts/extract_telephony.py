from pathlib import Path
import re
t = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = t.read_text(encoding="utf-8")
# telephony showcase block
m = re.search(
    r'<div class="int-showcase[^"]*" id="integration-telephony">(.*?)</div>\s*</div>\s*<div class="int-showcase',
    text,
    re.S,
)
if not m:
    m = re.search(r'id="integration-telephony"[^>]*>(.*?)(?=id="integration-llm"|id="integration-llm")', text, re.S)
if m:
    chunk = m.group(1)[:8000]
    Path(__file__).parent.joinpath("telephony_chunk.txt").write_text(chunk, encoding="utf-8")
    print("wrote chunk", len(chunk))
    # headings
    for tag in ["h3", "h4", "section-kicker"]:
        for x in re.findall(rf"<{tag}[^>]*>([^<]+)</{tag}>", chunk):
            print(tag, x[:80])
    print("stats", re.findall(r'int-stat[^>]*><b>([^<]+)</b>', chunk))
else:
    print("not found")
    # find integration-telephony pos
    i = text.find('id="integration-telephony"')
    print("pos", i, text[i:i+500] if i>=0 else "")
