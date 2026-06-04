import re
from pathlib import Path

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
s = HTML.read_text(encoding="utf-8")

new_grid = """<div class="nav-dropdown-grid"> <div class="dropdown-section dropdown-section-wide"> <div class="dropdown-section-title"> EMAAVY integration layers</div> <div class="dropdown-link-grid"> <a href="pages/integrations/index.html">All integrations</a> <a href="pages/integrations/telephony.html">Telephony</a> <a href="pages/integrations/llms.html">LLMs</a> <a href="pages/integrations/stt.html">Speech-to-Text</a> <a href="pages/integrations/tts.html">Text-to-Speech</a> <a href="pages/integrations/tools.html">Tools &amp; workflow</a> </div> </div> </div>"""

s2, n = re.subn(
    r'<div class="nav-dropdown-grid">.*?</div>\s*</div>\s*</div>\s*<a href="#agents"',
    new_grid + " </div> </div> <a href=\"#agents\"",
    s,
    count=1,
    flags=re.S,
)
if not n:
    raise SystemExit("mega replace failed")
HTML.write_text(s2, encoding="utf-8")
print("ok")
