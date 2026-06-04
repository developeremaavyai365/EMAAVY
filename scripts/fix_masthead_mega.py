from pathlib import Path
import re

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
s = HTML.read_text(encoding="utf-8")

# masthead uses id="integrationsMenu" or nav-dropdown-menu
for marker in ['id="integrationsMenu"', 'class="nav-dropdown-menu mega"', 'class="nav-dropdown-menu"']:
    if marker in s:
        print("found", marker)
        break

m = re.search(
    r'id="integrationsDropdown"[^>]*>.*?id="agentsDropdown"',
    s,
    re.S,
)
if not m:
    raise SystemExit("integrationsDropdown block not found")

block = m.group(0)
new_block = '''id="integrationsDropdown"> <div class="nav-dropdown-split"> <a href="#integrations" class="nav-integrations-link" data-nav-section="integrations">Integrations</a> <button class="nav-dropdown-caret" id="integrationsDropdownTrigger" type="button" aria-label="Integration categories">▾</button> </div> <div class="nav-dropdown-menu mega" id="integrationsMenu"> <div class="dropdown-section"> <div class="dropdown-section-title"> Integrations</div> <div class="dropdown-link-grid"> <a href="pages/integrations/index.html">All integrations</a> <a href="pages/integrations/telephony.html">Telephony</a> <a href="pages/integrations/llms.html">LLMs</a> <a href="pages/integrations/stt.html">Speech-to-Text</a> <a href="pages/integrations/tts.html">Text-to-Speech</a> <a href="pages/integrations/tools.html">Tools</a> </div> </div> </div> </div> <div class="nav-dropdown" id="agentsDropdown"'''

# preserve split/caret from original if structure differs - simpler: replace from integrationsDropdown to agentsDropdown
start = m.start()
# find start of integrationsDropdown div
div_start = s.rfind('<div class="nav-dropdown"', 0, start + 5)
if div_start < 0:
    div_start = s.find('<div class="nav-dropdown" id="integrationsDropdown"')

agents_start = s.find('<div class="nav-dropdown" id="agentsDropdown"', start)

prefix = s[div_start : s.find('id="integrationsDropdown"', div_start)]
# rebuild from opening div
opening = '<div class="nav-dropdown" id="integrationsDropdown">'
inner = ''' <div class="nav-dropdown-split"> <a href="#integrations" class="nav-integrations-link" data-nav-section="integrations">Integrations</a> <button class="nav-dropdown-caret" id="integrationsDropdownTrigger" type="button" aria-label="Integration categories">▾</button> </div> <div class="nav-dropdown-menu mega" id="integrationsMenu"> <div class="dropdown-section"> <div class="dropdown-section-title"> Integrations</div> <div class="dropdown-link-grid"> <a href="pages/integrations/index.html">All integrations</a> <a href="pages/integrations/telephony.html">Telephony</a> <a href="pages/integrations/llms.html">LLMs</a> <a href="pages/integrations/stt.html">Speech-to-Text</a> <a href="pages/integrations/tts.html">Text-to-Speech</a> <a href="pages/integrations/tools.html">Tools</a> </div> </div> </div> </div> '''

s2 = s[:div_start] + opening + inner + s[agents_start:]
HTML.write_text(s2, encoding="utf-8")
print("ok", div_start, agents_start)
