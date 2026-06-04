"""Align LLM model orchestration strip with telephony call-flow."""
import re
from pathlib import Path

HTML = Path(__file__).resolve().parents[1] / "emaavy_white_blue (2).html"
text = HTML.read_text(encoding="utf-8")

FLOW_OLD = (
    '<div class="llm-flow" aria-label="LLM orchestration lifecycle"> '
    '<header class="llm-flow-head"> '
    '<span class="llm-flow-kicker">Model orchestration</span> '
    '<p class="llm-flow-title">How EMAAVY uses your LLM stack</p> '
    "</header> "
    '<ol class="llm-flow-track"> '
    '<li class="llm-flow-step"><span class="llm-flow-index">01</span>'
    '<span class="llm-flow-label">Transcript in</span></li> '
    '<li class="llm-flow-step" aria-hidden="true"><span class="llm-flow-connector"></span></li> '
    '<li class="llm-flow-step"><span class="llm-flow-index">02</span>'
    '<span class="llm-flow-label">Model selected</span></li> '
    '<li class="llm-flow-step" aria-hidden="true"><span class="llm-flow-connector"></span></li> '
    '<li class="llm-flow-step"><span class="llm-flow-index">03</span>'
    '<span class="llm-flow-label">Intent detected</span></li> '
    '<li class="llm-flow-step" aria-hidden="true"><span class="llm-flow-connector"></span></li> '
    '<li class="llm-flow-step"><span class="llm-flow-index">04</span>'
    '<span class="llm-flow-label">Data extracted</span></li> '
    '<li class="llm-flow-step" aria-hidden="true"><span class="llm-flow-connector"></span></li> '
    '<li class="llm-flow-step"><span class="llm-flow-index">05</span>'
    '<span class="llm-flow-label">Agent responds</span></li> '
    "</ol></div> "
)

FLOW_NEW = (
    '<div class="call-flow" aria-label="LLM orchestration lifecycle"> '
    '<header class="call-flow-head"> '
    '<span class="call-flow-kicker">Model orchestration</span> '
    '<p class="call-flow-title">How EMAAVY uses your LLM stack</p> '
    "</header> "
    '<ol class="call-flow-track"> '
    '<li class="call-flow-step"><span class="call-flow-index">01</span>'
    '<span class="call-flow-label">Transcript in</span></li> '
    '<li class="call-flow-step" aria-hidden="true"><span class="call-flow-connector"></span></li> '
    '<li class="call-flow-step"><span class="call-flow-index">02</span>'
    '<span class="call-flow-label">Model selected</span></li> '
    '<li class="call-flow-step" aria-hidden="true"><span class="call-flow-connector"></span></li> '
    '<li class="call-flow-step"><span class="call-flow-index">03</span>'
    '<span class="call-flow-label">Intent detected</span></li> '
    '<li class="call-flow-step" aria-hidden="true"><span class="call-flow-connector"></span></li> '
    '<li class="call-flow-step"><span class="call-flow-index">04</span>'
    '<span class="call-flow-label">Data extracted</span></li> '
    '<li class="call-flow-step" aria-hidden="true"><span class="call-flow-connector"></span></li> '
    '<li class="call-flow-step"><span class="call-flow-index">05</span>'
    '<span class="call-flow-label">Agent responds</span></li> '
    "</ol></div> "
)

if FLOW_OLD not in text:
    # fallback: replace llm-* class names in place
    if "llm-flow" not in text:
        print("ERROR: llm-flow block not found")
        exit(1)
    text = text.replace("llm-flow", "call-flow")
    text = text.replace("call-flow-head", "call-flow-head")  # noop
    print("Renamed llm-flow classes to call-flow")
else:
    text = text.replace(FLOW_OLD, FLOW_NEW, 1)
    print("Replaced LLM flow HTML with call-flow markup")

# Remove dedicated llm-flow CSS block inside LLM CARDS section
marker_start = "#integration-llm .llm-flow {"
marker_end = "@media (max-width: 1180px)"
if marker_start in text:
    s = text.index(marker_start)
    e = text.index(marker_end, s)
    text = text[:s] + text[e:]
    print("Removed llm-flow CSS block")

# Remove llm-flow mobile rules from 560px media query
text = re.sub(
    r"\n  #integration-llm \.llm-flow-track \{[^}]+\}\n"
    r"  #integration-llm \.llm-flow-step \{[^}]+\}\n"
    r"  #integration-llm \.llm-flow-step\[aria-hidden=\"true\"\] \{[^}]+\}\n"
    r"  #integration-llm \.llm-flow-connector \{[^}]+\}\n"
    r"  #integration-llm \.llm-flow-connector::after \{[^}]+\}\n",
    "\n",
    text,
    count=1,
)

# Scope call-flow CSS to LLM section too
replacements = [
    ("#integration-telephony .call-flow", "#integration-telephony .call-flow,\n#integration-llm .call-flow"),
    ("#integration-telephony .call-flow-head", "#integration-telephony .call-flow-head,\n#integration-llm .call-flow-head"),
    ("#integration-telephony .call-flow-kicker", "#integration-telephony .call-flow-kicker,\n#integration-llm .call-flow-kicker"),
    ("#integration-telephony .call-flow-title", "#integration-telephony .call-flow-title,\n#integration-llm .call-flow-title"),
    ("#integration-telephony .call-flow-track", "#integration-telephony .call-flow-track,\n#integration-llm .call-flow-track"),
    ("#integration-telephony .call-flow-step", "#integration-telephony .call-flow-step,\n#integration-llm .call-flow-step"),
    ("#integration-telephony .call-flow-index", "#integration-telephony .call-flow-index,\n#integration-llm .call-flow-index"),
    ("#integration-telephony .call-flow-label", "#integration-telephony .call-flow-label,\n#integration-llm .call-flow-label"),
    ("#integration-telephony .call-flow-connector", "#integration-telephony .call-flow-connector,\n#integration-llm .call-flow-connector"),
]
for old, new in replacements:
    if ",\n#integration-llm" not in text[text.find(old): text.find(old) + len(old) + 30] if old in text else "":
        if old in text and new not in text:
            text = text.replace(old, new, 1)

# Avoid double-scoping if run twice
text = text.replace(
    "#integration-telephony .call-flow,\n#integration-llm .call-flow,\n#integration-llm .call-flow",
    "#integration-telephony .call-flow,\n#integration-llm .call-flow",
)

HTML.write_text(text, encoding="utf-8")
print("Done")
print("llm-flow left:", "llm-flow" in HTML.read_text(encoding="utf-8"))
print("llm call-flow:", "integration-llm" in HTML.read_text(encoding="utf-8") and "call-flow" in HTML.read_text(encoding="utf-8"))
