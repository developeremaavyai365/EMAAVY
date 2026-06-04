import re
from pathlib import Path

text = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = text.read_text(encoding="utf-8")
m = re.search(r'int-cards-grid[^>]*>.*?llm-flow', text[text.find("integration-llm"):], re.DOTALL)
chunk = m.group(0) if m else ""
# count int-cards-grid openings before llm-flow in llm section
start = text.find('id="integration-llm"')
end = text.find('id="integration-stt"', start)
seg = text[start:end]
print("int-cards-grid count:", seg.count("int-cards-grid"))
for i, m in enumerate(re.finditer(r'<div class="int-cards-grid[^"]*"[^>]*>', seg)):
    print(i, m.group(0))
# write snippet to file
Path(__file__).resolve().parents[1] / "scripts" / "llm_grid_snippet.txt"
out = Path(__file__).resolve().parents[1] / "scripts" / "llm_grid_snippet.txt"
idx = seg.find("int-cards-grid")
out.write_text(seg[idx:idx+2500], encoding="utf-8")
print("wrote snippet", len(out.read_text()))
