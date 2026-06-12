#!/usr/bin/env python3
"""Upgrade conversational flows section — premium split + keep live canvas."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from flow_showcase import FLOW_LAYERS  # noqa: E402

PREFIX = "flow"
SECTION_ID = "features"


def p(name: str) -> str:
    return f"{PREFIX}-{name}"


def build_layer_cards() -> str:
    variants = ["a", "b", "c", "d", "e"]
    items = []
    for i, layer in enumerate(FLOW_LAYERS):
        v = variants[i]
        num = f"{i + 1:02d}"
        items.append(
            f'''          <li class="{p("layer-card")} {p("layer-card")}--{v} reveal" data-detail="flow-{layer["id"]}" tabindex="0">
            <span class="{p("layer-card-icon")}" aria-hidden="true">{layer["icon"]}</span>
            <div class="{p("layer-card-body")}">
              <span class="{p("layer-card-kicker")}">Layer {num} · {layer["kicker"]}</span>
              <h3>{layer["title"]}</h3>
              <p>{layer["short"]}</p>
            </div>
            <span class="{p("layer-card-tag")}">{layer["kicker"]}</span>
          </li>'''
        )
    return "\n".join(items)


def extract_device_html(text: str) -> str:
    start = text.find('<div class="flows-device" aria-label="Interactive conversational flow">')
    if start < 0:
        raise SystemExit("Could not find flows-device block in index.html")
    end_marker = '</div>\n  </div>\n</section>'
    end = text.find(end_marker, start)
    if end < 0:
        end_marker = "</div>\r\n  </div>\r\n</section>"
        end = text.find(end_marker, start)
    if end < 0:
        raise SystemExit("Could not find end of flows-device block in index.html")
    block = text[start:end].rstrip()
    if not block.endswith("</div>"):
        raise SystemExit("flows-device block extraction looks truncated")
    return block


def build_section_html(device_html: str) -> str:
    return f'''<!-- CONVERSATIONAL FLOWS -->
<section id="{SECTION_ID}" class="hub-zone hub-zone--5 hub-zone--clear hub-zone--flows">
  <div class="hub-zone-bg" aria-hidden="true"></div>
  <div class="hub-zone-header reveal">
    <span class="hub-zone-index">05</span>
    <p class="hub-zone-title">Conversational flows</p>
  </div>
  <div class="hub-clear-shell reveal" id="flows-emaavy">
    <header class="hub-clear-intro">
      <h2 class="hub-clear-intro-title">Design conversations your agents actually follow.</h2>
      <p class="hub-clear-intro-lead">Map every branch — hooks, objections, nurture paths, and outcomes — with a visual flow builder and live script preview that updates as you explore.</p>
    </header>
    <div class="{p("split")} reveal" id="flowsShowcase">
      <div class="{p("steps-col")}" aria-label="Flow builder layers">
        <p class="{p("steps-head")}">Explore the flow</p>
        <p class="{p("steps-sub")}">Click a layer to jump on the canvas — then simulate branches and edit live variables.</p>
        <ol class="{p("layer-steps")}">
{build_layer_cards()}
        </ol>
        <div class="flows-vars" aria-label="Personalize flow variables">
          <p class="flows-vars-label">Live variables</p>
          <label for="flowVarName">Contact name</label>
          <input type="text" id="flowVarName" value="Rahul" autocomplete="off" />
          <label for="flowVarAgent">Agent name</label>
          <input type="text" id="flowVarAgent" value="Priya" autocomplete="off" />
          <label for="flowVarCompany">Company</label>
          <input type="text" id="flowVarCompany" value="EMAAVY" autocomplete="off" />
        </div>
        <p class="flows-vars-label" style="margin-bottom:0.35rem">Simulate a response</p>
        <div class="flows-branch-pills">
          <button type="button" class="flows-branch-pill" data-branch="interested">Interested</button>
          <button type="button" class="flows-branch-pill" data-branch="maybe">Maybe</button>
          <button type="button" class="flows-branch-pill" data-branch="not">Not interested</button>
        </div>
        <ul class="flows-showcase-points">
          <li>Visual flow builder with branches, scripts, and end states</li>
          <li>Dynamic placeholders — preview updates as you edit</li>
          <li>Deploy one flow across campaigns, agents, and languages</li>
        </ul>
        <div class="{p("actions")}">
          <a href="book-demo.html" class="hub-btn-primary">Build your flow</a>
          <button type="button" class="hub-btn-secondary flows-try-live">Reset explorer</button>
        </div>
        <button type="button" class="flows-shot-toggle" aria-label="View full product flow canvas">
          <img src="assets/flows/conversational-flow.png" width="1200" height="680" alt="" loading="lazy" decoding="async" />
          <span>Full flow canvas · product view</span>
        </button>
      </div>
      <div class="{p("showcase-col")}">
        <div class="{p("showcase")}" tabindex="0" aria-label="EMAAVY conversational flow — live explorer" aria-live="polite">
          <div class="{p("sc-stage")}">
            {device_html}
            <div class="{p("sc-status")}">
              <span class="{p("sc-status-live")}"><span class="{p("sc-status-dot")}" aria-hidden="true"></span><span data-flow-status-label>Hook &amp; Context</span></span>
              <span class="{p("sc-status-metric")}" data-flow-metric><strong>Live</strong> · Flow explorer</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>'''


INLINE_STYLE = f'''
  /* Conversational flows premium showcase */
  body[data-page="home"] #{SECTION_ID} .{p("showcase")} {{
    padding: 4px !important;
    border-radius: 24px !important;
    background: linear-gradient(145deg, #4a658b 0%, #18345d 42%, #5a7d9e 100%) !important;
    box-shadow:
      0 0 0 1px rgba(74, 101, 139, 0.45),
      0 22px 52px -14px rgba(24, 52, 93, 0.32),
      0 0 40px -10px rgba(74, 101, 139, 0.28) !important;
  }}
  body[data-page="home"] #{SECTION_ID} .{p("sc-stage")} {{
    border-radius: 20px !important;
    overflow: hidden !important;
    background: linear-gradient(165deg, #f8fafc 0%, #f1f5f9 48%, #eef2f7 100%) !important;
    border: 2px solid rgba(255, 255, 255, 0.92) !important;
  }}
  body[data-page="home"] #{SECTION_ID} .flows-device {{
    border: none !important;
    border-radius: 0 !important;
    box-shadow: none !important;
  }}
'''


def write_flow_showcase_css() -> None:
    css = f'''
#{SECTION_ID} .hub-clear-shell {{ max-width: 1180px; }}

#{SECTION_ID} .{p("split")} {{
  display: grid;
  grid-template-columns: minmax(0, 0.95fr) minmax(0, 1.15fr);
  gap: clamp(1.25rem, 3.5vw, 2.5rem);
  align-items: start;
}}

#{SECTION_ID} .{p("steps-head")} {{
  font-family: 'Clash Display', sans-serif;
  font-size: 1.05rem;
  font-weight: 600;
  color: #18345d;
  margin: 0 0 0.25rem;
}}

#{SECTION_ID} .{p("steps-sub")} {{
  font-size: 0.78rem;
  line-height: 1.5;
  color: #64748b;
  margin: 0 0 0.85rem;
}}

#{SECTION_ID} .{p("steps-col")} {{
  max-height: min(82vh, 640px);
  overflow-y: auto;
  padding-right: 0.35rem;
  scrollbar-width: thin;
}}

#{SECTION_ID} .{p("layer-steps")} {{
  list-style: none;
  margin: 0 0 1rem;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 0.55rem;
}}

#{SECTION_ID} .{p("layer-card")} {{
  display: grid;
  grid-template-columns: auto 1fr auto;
  gap: 0.55rem;
  align-items: start;
  padding: 0.75rem 0.85rem;
  list-style: none;
  border-radius: 10px;
  border: 1px solid rgba(74, 101, 139, 0.18);
  cursor: pointer;
  outline: none;
  transition: border-color 0.2s ease, box-shadow 0.2s ease, transform 0.2s ease;
}}

#{SECTION_ID} .{p("layer-card-icon")} {{
  font-size: 1.15rem;
  line-height: 1;
  margin-top: 0.1rem;
}}

#{SECTION_ID} .{p("layer-card-body")} h3 {{
  font-family: 'Clash Display', sans-serif;
  font-size: 0.82rem;
  font-weight: 600;
  color: #0f172a;
  margin: 0.1rem 0 0.2rem;
  line-height: 1.25;
}}

#{SECTION_ID} .{p("layer-card-body")} p {{
  font-size: 0.68rem;
  line-height: 1.45;
  color: #475569;
  margin: 0;
}}

#{SECTION_ID} .{p("layer-card-kicker")} {{
  font-size: 0.5rem;
  font-weight: 600;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #4a658b;
}}

#{SECTION_ID} .{p("layer-card-tag")} {{
  font-size: 0.48rem;
  font-weight: 700;
  letter-spacing: 0.06em;
  text-transform: uppercase;
  color: #18345d;
  padding: 0.18rem 0.38rem;
  border-radius: 999px;
  background: rgba(74, 101, 139, 0.1);
  border: 1px solid rgba(74, 101, 139, 0.18);
  white-space: nowrap;
}}

#{SECTION_ID} .{p("showcase")} {{
  position: relative;
  width: 100%;
}}

#{SECTION_ID} .{p("showcase-col")} {{
  position: relative;
  min-width: 0;
}}

#{SECTION_ID} .{p("sc-stage")} {{
  position: relative;
  width: 100%;
  min-height: 460px;
  overflow: hidden;
  isolation: isolate;
}}

#{SECTION_ID} .{p("sc-status")} {{
  position: absolute;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 5;
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.75rem;
  padding: 0.55rem 1rem;
  background: rgba(255, 255, 255, 0.92);
  border-top: 1px solid rgba(74, 101, 139, 0.14);
  backdrop-filter: blur(8px);
  font-size: 0.62rem;
  color: #64748b;
}}

#{SECTION_ID} .{p("sc-status-live")} {{
  display: inline-flex;
  align-items: center;
  gap: 0.4rem;
  font-weight: 600;
  color: #18345d;
}}

#{SECTION_ID} .{p("sc-status-dot")} {{
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #4a658b;
  animation: flow-sc-pulse 2s ease-in-out infinite;
}}

@keyframes flow-sc-pulse {{
  50% {{ opacity: 0.45; }}
}}

#{SECTION_ID} .{p("sc-status-metric")} {{
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: #4a658b;
}}

#{SECTION_ID} .{p("sc-status-metric")} strong {{
  color: #18345d;
}}

#{SECTION_ID} .flows-device-body {{
  padding-bottom: 2.5rem;
}}

#{SECTION_ID} .{p("actions")} {{
  display: flex;
  flex-wrap: wrap;
  gap: 0.55rem;
  margin-bottom: 0.85rem;
}}

@media (max-width: 1024px) {{
  #{SECTION_ID} .{p("split")} {{
    grid-template-columns: 1fr;
  }}
  #{SECTION_ID} .{p("layer-card")} {{
    max-width: 100% !important;
    margin-left: 0 !important;
    margin-right: 0 !important;
  }}
}}
'''
    (ROOT / "assets" / "flow-showcase.css").write_text(css, encoding="utf-8")


def patch_flows_css() -> None:
    path = ROOT / "assets" / "flows-showcase.css"
    text = path.read_text(encoding="utf-8")

    text = re.sub(
        r"#features\.hub-zone--flows \{[^}]+\}",
        "#features.hub-zone--flows {\n  padding-bottom: clamp(2.5rem, 5vw, 4rem) !important;\n}",
        text,
        count=1,
    )

    text = re.sub(
        r"\.flows-showcase \{[^}]+\}",
        "",
        text,
        count=1,
    )

    text = re.sub(
        r"\.flows-showcase-copy \{[^}]+\}",
        "",
        text,
        count=1,
    )

    if "@media (max-width: 1024px)" in text and ".flow-split" not in text:
        text = text.replace(
            "@media (max-width: 1024px) {\n  .flows-showcase {\n    grid-template-columns: 1fr;\n  }",
            "@media (max-width: 1024px) {",
        )

    path.write_text(text, encoding="utf-8")


SECTION_RE = re.compile(
    r"<!-- CONVERSATIONAL FLOWS -->.*?</section>",
    re.DOTALL,
)


def patch_index(device_html: str) -> None:
    text = INDEX.read_text(encoding="utf-8")
    new_section = build_section_html(device_html)
    if not SECTION_RE.search(text):
        raise SystemExit("Could not find conversational flows section in index.html")
    text = SECTION_RE.sub(new_section, text, count=1)

    if "flow-showcase.css" not in text:
        text = text.replace(
            'href="assets/flows-showcase.css"',
            'href="assets/flows-showcase.css" />\n  <link rel="stylesheet" href="assets/flow-showcase.css"',
        )

    if "Conversational flows premium showcase" not in text:
        text = text.replace(
            "body[data-page=\"home\"] .demo-video {",
            INLINE_STYLE + "\n  body[data-page=\"home\"] .demo-video {",
        )

    INDEX.write_text(text, encoding="utf-8")


def main():
    text = INDEX.read_text(encoding="utf-8")
    device_html = extract_device_html(text)
    write_flow_showcase_css()
    patch_flows_css()
    patch_index(device_html)
    print(f"OK: conversational flows premium showcase ({len(FLOW_LAYERS)} layers + live canvas)")


if __name__ == "__main__":
    main()
