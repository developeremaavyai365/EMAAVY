from pathlib import Path
import re

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
s = HTML.read_text(encoding="utf-8")

start = s.find('<div class="nav-dropdown-menu mega">')
if start < 0:
    raise SystemExit("mega menu not found")
end = s.find("</nav>", start)
chunk = s[start:end]
# find closing of mega menu - first </div> after mega that closes dropdown
# structure: mega > sections > /div (mega) /div (dropdown) 
idx = chunk.find('</div> <div class="nav-dropdown" id="agentsDropdown">')
if idx < 0:
    idx = chunk.find('</div> </div> <div class="nav-dropdown" id="agentsDropdown">')
if idx < 0:
    raise SystemExit("agents dropdown marker not found")

new_menu = '''<div class="nav-dropdown-menu mega"> <div class="dropdown-section"> <div class="dropdown-section-title"> Integrations</div> <div class="dropdown-link-grid"> <a href="pages/integrations/index.html">All integrations</a> <a href="pages/integrations/telephony.html">Telephony</a> <a href="pages/integrations/llms.html">LLMs</a> <a href="pages/integrations/stt.html">Speech-to-Text</a> <a href="pages/integrations/tts.html">Text-to-Speech</a> <a href="pages/integrations/tools.html">Tools &amp; workflow</a> </div> </div> '''

s2 = s[:start] + new_menu + s[start + idx :]
HTML.write_text(s2, encoding="utf-8")
print("ok")
