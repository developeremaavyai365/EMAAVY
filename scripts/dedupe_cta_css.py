from pathlib import Path
import re

p = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = p.read_text(encoding="utf-8")
text2, n = re.subn(
    r"/\* ═══ CTA — Your calls are talking ═══ \*/.*?@media \(prefers-reduced-motion: reduce\) \{\s*\.cta-signal-ring.*?\}\s*\}\s*\n\n",
    "",
    text,
    count=1,
    flags=re.DOTALL,
)
if n:
    p.write_text(text2, encoding="utf-8")
    print("removed inline CTA CSS duplicate")
else:
    print("no inline block found")
