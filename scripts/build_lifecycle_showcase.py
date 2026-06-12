#!/usr/bin/env python3
"""Replace call lifecycle section with premium lc-showcase panel in index.html."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

sys.path.insert(0, str(Path(__file__).resolve().parent))
from lifecycle_showcase import LIFECYCLE_STEPS, NODE_LAYOUT  # noqa: E402

PREFIX = "lc"
STEPS = LIFECYCLE_STEPS
SECTION_ID = "journey"


def svg_point(x_pct: float, y_pct: float) -> tuple[int, int]:
    return int(x_pct * 6), int(y_pct * 6)


def p(name: str) -> str:
    return f"{PREFIX}-{name}"


def build_paths() -> str:
    lines = []
    mods = ["", f" {p('sc-path-flow--b')}", f" {p('sc-path-flow--c')}", f" {p('sc-path-flow--d')}", f" {p('sc-path-flow--e')}"]
    cx, cy = 300, 300
    for i, step in enumerate(STEPS):
        x, y = NODE_LAYOUT[step["id"]]
        sx, sy = svg_point(x, y)
        qx = (cx + sx) // 2
        qy = (cy + sy) // 2
        d = f"M{cx} {cy} Q{qx} {qy} {sx} {sy}"
        fid = step["id"]
        mod = mods[i] if i < len(mods) else ""
        lines.append(f'                <path class="{p("sc-path-soft")}" data-lc-link="{fid}" d="{d}"/>')
        lines.append(f'                <path class="{p("sc-path")}" data-lc-link="{fid}" d="{d}"/>')
        lines.append(f'                <path class="{p("sc-path-flow")}{mod}" data-lc-link="{fid}" d="{d}"/>')
    return "\n".join(lines)


def build_nodes() -> str:
    cards = []
    for i, step in enumerate(STEPS):
        x, y = NODE_LAYOUT[step["id"]]
        active = " is-active" if i == 0 else ""
        num = f"{i + 1:02d}"
        short = step["kicker"]
        cards.append(
            f'''                <article class="{p("sc-node")} {p("sc-node")}--{step["id"]}{active}" data-step="{step["id"]}" style="--lc-x: {x}%; --lc-y: {y}%;">
                  <div class="{p("sc-node-card")}">
                    <span class="{p("sc-node-num")}">{num}</span>
                    <span class="{p("sc-node-title")}">{short}</span>
                  </div>
                </article>'''
        )
    return "\n".join(cards)


def build_layer_cards() -> str:
    variants = ["a", "b", "c", "d", "e"]
    items = []
    for i, step in enumerate(STEPS):
        v = variants[i]
        num = f"{i + 1:02d}"
        items.append(
            f'''          <li class="{p("layer-card")} {p("layer-card")}--{v} reveal" data-detail="lc-{step["id"]}" tabindex="0">
            <span class="{p("layer-card-icon")}" aria-hidden="true">{step["icon"]}</span>
            <div class="{p("layer-card-body")}">
              <span class="{p("layer-card-kicker")}">Stage {num} · {step["kicker"]}</span>
              <h3>{step["title"]}</h3>
              <p>{step["short"]}</p>
            </div>
            <span class="{p("layer-card-tag")}">{step["kicker"]}</span>
          </li>'''
        )
    return "\n".join(items)


def build_pipeline_visual(current_id: str) -> str:
    chips = []
    for step in STEPS:
        live = " is-live" if step["id"] == current_id else ""
        chips.append(f'\n                    <span class="{p("vis-pipe-step")}{live}">{step["kicker"]}</span>')
    return "".join(chips)


def build_stats_visual(step: dict) -> str:
    return "".join(
        f'\n                    <div class="{p("vis-stat")}"><b>{a}</b><span>{b}</span></div>'
        for a, b in step.get("stats", [])
    )


def build_slides() -> str:
    slides = []
    for i, step in enumerate(STEPS):
        num = f"{i + 1:02d}"
        points = "".join(f"\n                  <li>{pt}</li>" for pt in step["points"])
        outcomes = "".join(f'\n                  <span class="{p("sc-slide-outcome")}">{o}</span>' for o in step["outcomes"])
        usecases = "".join(f"\n                    <li>{u}</li>" for u in step["usecases"])
        flow = "".join(
            f'\n                    <span class="{p("vis-flow-step")}{" is-live" if j == 0 else ""}">{s}</span>'
            for j, s in enumerate(step["flow"])
        )
        pipeline = build_pipeline_visual(step["id"])
        stats = build_stats_visual(step)
        slides.append(
            f'''              <article class="{p("sc-slide")}" data-slide="{step["id"]}" role="tabpanel" aria-hidden="true">
                <span class="{p("sc-slide-kicker")}">{num} — {step["kicker"]}</span>
                <h3 class="{p("sc-slide-headline")}">{step["title"]}</h3>
                <p class="{p("sc-slide-desc")}">{step["desc"]}</p>
                <p class="{p("sc-slide-detail")}">{step["detail"]}</p>
                <div class="{p("sc-slide-visual")}">
                  <div class="{p("vis-stage")}">
                    <span class="{p("vis-stage-icon")}" aria-hidden="true">{step["icon"]}</span>
                    <div class="{p("vis-pipeline")}" aria-label="Lifecycle position">{pipeline}
                    </div>
                    <div class="{p("vis-flow")}">{flow}
                    </div>
                  </div>
                  <div class="{p("vis-stats")}">{stats}
                  </div>
                </div>
                <ul class="{p("sc-slide-points")}">{points}
                </ul>
                <div class="{p("sc-slide-outcomes")}">{outcomes}
                </div>
                <div class="{p("sc-slide-usecases")}">
                  <span class="{p("sc-slide-usecases-label")}">Ideal for</span>
                  <ul class="{p("sc-slide-usecase-list")}">{usecases}
                  </ul>
                </div>
                <a href="{step["page"]}" class="{p("sc-slide-link")}">Full stage guide →</a>
              </article>'''
        )
    return "\n".join(slides)


def build_section_html() -> str:
    n = len(STEPS)
    first_title = STEPS[0]["title"]
    return f'''<!-- CALL LIFECYCLE HUB --> <section id="{SECTION_ID}" class="hub-zone hub-zone--7 hub-zone--alt hub-zone--clear hub-zone--lifecycle">
  <div class="hub-zone-bg" aria-hidden="true"></div>
  <div class="hub-zone-header reveal">
    <span class="hub-zone-index">07</span>
    <p class="hub-zone-title">Call lifecycle</p>
  </div>
  <div class="hub-clear-shell reveal" id="call-lifecycle-emaavy">
    <header class="hub-clear-intro">
      <h2 class="hub-clear-intro-title">Five stages. Zero manual handoffs.</h2>
      <p class="hub-clear-intro-lead">From ring to learn on one automated pipeline — CRM and triggers fire while the caller is still on the line.</p>
    </header>
    <div class="{p("split")} reveal">
      <div class="{p("steps-col")}" aria-label="Call lifecycle stages">
        <p class="{p("steps-head")}">The five-stage pipeline</p>
        <p class="{p("steps-sub")}">Click any stage to explore what EMAAVY captures, scores, and automates — live on every call.</p>
        <ol class="{p("layer-steps")}">
{build_layer_cards()}
        </ol>
      </div>
      <div class="{p("showcase-col")}">
        <div class="{p("showcase")}" id="lcShowcase" tabindex="0" aria-label="EMAAVY call lifecycle — live pipeline preview" aria-live="polite">
          <div class="{p("sc-stage")}">
            <div class="{p("sc-hub")}">
              <div class="{p("sc-ambient")}" aria-hidden="true"></div>
              <div class="{p("sc-grid")}" aria-hidden="true"></div>
              <svg class="{p("sc-paths")}" viewBox="0 0 600 600" aria-hidden="true">
                <defs>
                  <linearGradient id="{p("sc-path-gradient")}" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#18345d" stop-opacity="0.35"/>
                    <stop offset="50%" stop-color="#4a658b" stop-opacity="0.65"/>
                    <stop offset="100%" stop-color="#5a7d9e" stop-opacity="0.4"/>
                  </linearGradient>
                </defs>
{build_paths()}
              </svg>
              <div class="{p("sc-core")}" aria-hidden="true">
                <div class="{p("sc-core-body")}">
                  <span class="{p("sc-core-label")}">Emaavy</span>
                  <span class="{p("sc-core-sub")}">Lifecycle</span>
                </div>
              </div>
              <div class="{p("sc-nodes")}">
{build_nodes()}
              </div>
              <div class="{p("sc-status")}">
                <span class="{p("sc-status-live")}"><span class="{p("sc-status-dot")}" aria-hidden="true"></span><span data-lc-status-label>{first_title}</span></span>
                <span class="{p("sc-status-metric")}" data-lc-metric><strong>1</strong> / {n} stages</span>
              </div>
            </div>
            <div class="{p("sc-presentation")}" aria-label="Lifecycle stage detail" aria-hidden="true">
              <div class="{p("sc-toolbar")}">
                <button type="button" class="{p("sc-back")}" aria-label="Return to pipeline view">← Pipeline</button>
                <span class="{p("sc-progress")}" data-lc-pres-progress><strong>1</strong> / {n}</span>
                <div class="{p("sc-nav-group")}">
                  <button type="button" class="{p("sc-nav")} {p("sc-nav")}--prev" aria-label="Previous stage">←</button>
                  <button type="button" class="{p("sc-nav")} {p("sc-nav")}--next" aria-label="Next stage">→</button>
                </div>
              </div>
              <div class="{p("sc-slides-viewport")}">
{build_slides()}
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="{p("benefits")}" aria-label="Why EMAAVY lifecycle wins">
      <div class="{p("benefit")}"><strong>During the call</strong><span>Intelligence and actions before hang-up</span></div>
      <div class="{p("benefit")}"><strong>Closed loop</strong><span>Every outcome improves the next dial</span></div>
      <div class="{p("benefit")}"><strong>100% automated</strong><span>No manual steps between systems</span></div>
    </div>
    <div class="hub-clear-cta reveal">
      <a href="pages/call-lifecycle/index.html" class="hub-btn-primary">Explore call lifecycle</a>
      <a href="book-demo.html" class="hub-btn-secondary">Book a demo</a>
    </div>
  </div>
</section>'''


INLINE_STYLE = f'''
  /* Call lifecycle premium showcase */
  body[data-page="home"] #{SECTION_ID} .{p("showcase")} {{
    padding: 4px !important;
    border-radius: 24px !important;
    background: linear-gradient(145deg, #4a658b 0%, #18345d 42%, #5a7d9e 100%) !important;
    box-shadow:
      0 0 0 1px rgba(74, 101, 139, 0.45),
      0 22px 52px -14px rgba(24, 52, 93, 0.32),
      0 0 40px -10px rgba(74, 101, 139, 0.28) !important;
  }}
  body[data-page="home"] #{SECTION_ID} .{p("sc-stage")}:not(.is-presenting) .{p("sc-hub")} {{
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
  }}
  body[data-page="home"] #{SECTION_ID} .{p("sc-stage")}.is-presenting .{p("sc-hub")},
  body[data-page="home"] #{SECTION_ID} .{p("sc-stage")}.is-presenting .{p("sc-ambient")},
  body[data-page="home"] #{SECTION_ID} .{p("sc-stage")}.is-presenting .{p("sc-grid")},
  body[data-page="home"] #{SECTION_ID} .{p("sc-stage")}.is-presenting .{p("sc-paths")},
  body[data-page="home"] #{SECTION_ID} .{p("sc-stage")}.is-presenting .{p("sc-nodes")},
  body[data-page="home"] #{SECTION_ID} .{p("sc-stage")}.is-presenting .{p("sc-core")} {{
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
  }}
  body[data-page="home"] #{SECTION_ID} .{p("sc-presentation")} {{
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
  }}
  body[data-page="home"] #{SECTION_ID} .{p("sc-stage")}.is-presenting .{p("sc-presentation")} {{
    display: flex !important;
    flex-direction: column !important;
    visibility: visible !important;
    opacity: 1 !important;
    pointer-events: auto !important;
    z-index: 20 !important;
    background: linear-gradient(165deg, #f8fafc 0%, #f1f5f9 48%, #eef2f7 100%) !important;
  }}
  body[data-page="home"] #{SECTION_ID} .{p("sc-stage")}.is-presenting .{p("sc-slide")}.is-active {{
    display: flex !important;
    flex-direction: column !important;
  }}
  body[data-page="home"] #{SECTION_ID} .{p("sc-stage")}.is-presenting .{p("sc-slide")}:not(.is-active) {{
    display: none !important;
  }}
  body[data-page="home"] #{SECTION_ID} .{p("sc-slide-usecase-list")} li::before,
  body[data-page="home"] #{SECTION_ID} .{p("sc-slide-points")} li::before {{
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
    content: "" !important;
  }}
  body[data-page="home"] #{SECTION_ID} .{p("sc-stage")}.is-presenting {{
    min-height: 520px !important;
  }}
  body[data-page="home"] #{SECTION_ID} .{p("vis-pipe-step")}::before,
  body[data-page="home"] #{SECTION_ID} .{p("vis-pipe-step")}::after,
  body[data-page="home"] #{SECTION_ID} .{p("vis-flow-step")}::before,
  body[data-page="home"] #{SECTION_ID} .{p("vis-flow-step")}::after {{
    display: block !important;
    visibility: visible !important;
    content: none !important;
  }}
'''


def write_lc_css() -> None:
    base = (ROOT / "assets" / "int-showcase.css").read_text(encoding="utf-8")
    css = base.replace("int-sc", p("sc")).replace("int-showcase", p("showcase"))
    css = css.replace("int-vis", p("vis")).replace("int-layer", p("layer"))
    css = css.replace("int-split", p("split")).replace("int-layers-col", p("steps-col"))
    css = css.replace("#integrations", f"#{SECTION_ID}")
    css = css.replace("Integrations hub", "Call lifecycle")
    css = css.replace(f".{p('sc-pipeline')}", f".{p('sc-hub')}")
    css = css.replace("--int-x", "--lc-x").replace("--int-y", "--lc-y")
    css = re.sub(rf"\.{p('sc-node')}--\w+ \{{ --lc-x:.*?;\s*\}}\n", "", css)

    extra = f'''
#{SECTION_ID} .hub-clear-shell {{ max-width: 1180px; }}

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
  max-height: min(78vh, 560px);
  overflow-y: auto;
  padding-right: 0.35rem;
  scrollbar-width: thin;
}}

#{SECTION_ID} .{p("layer-steps")} {{
  list-style: none;
  margin: 0;
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

#{SECTION_ID} .{p("layer-card")}.is-selected {{
  border-color: #4a658b !important;
  box-shadow: 0 8px 22px rgba(24, 52, 93, 0.12) !important;
}}

.{p("sc-node")} {{
  position: absolute;
  left: var(--lc-x);
  top: var(--lc-y);
  transform: translate(-50%, -50%);
  z-index: 4;
  width: clamp(3.8rem, 11vw, 5rem);
  cursor: pointer;
  pointer-events: auto;
}}

.{p("sc-node-card")} {{
  padding: 0.32rem 0.36rem;
  text-align: center;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.94);
  border: 1px solid rgba(74, 101, 139, 0.22);
  box-shadow: 0 6px 18px rgba(24, 52, 93, 0.1);
  transition: transform 0.2s ease, box-shadow 0.2s ease, border-color 0.2s ease;
}}

.{p("sc-node")}.is-active .{p("sc-node-card")},
.{p("sc-node")}:hover .{p("sc-node-card")} {{
  border-color: #4a658b;
  box-shadow: 0 10px 24px rgba(24, 52, 93, 0.16);
  transform: scale(1.04);
}}

.{p("sc-node-num")} {{
  display: block;
  font-size: 0.48rem;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: #4a658b;
  margin-bottom: 0.1rem;
}}

.{p("sc-node-title")} {{
  display: block;
  font-size: 0.5rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: #18345d;
  line-height: 1.2;
}}

.{p("sc-slide-visual")} {{
  display: grid;
  grid-template-columns: minmax(0, 1.1fr) minmax(0, 0.9fr);
  gap: 0.75rem;
  align-items: stretch;
  margin: 0.65rem 0 0.85rem;
}}

.{p("vis-stage")} {{
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 0.45rem;
  padding: 0.85rem;
  border-radius: 12px;
  background: linear-gradient(165deg, #f8fafc 0%, #eef2f7 100%);
  border: 1px solid rgba(74, 101, 139, 0.15);
}}

.{p("vis-stage-icon")} {{
  font-size: 1.35rem;
  line-height: 1;
}}

.{p("vis-pipeline")} {{
  display: flex;
  flex-wrap: wrap;
  gap: 0.22rem;
  justify-content: center;
  width: 100%;
}}

.{p("vis-pipe-step")} {{
  font-size: 0.46rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: #94a3b8;
  padding: 0.16rem 0.34rem;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.85);
  border: 1px solid rgba(148, 163, 184, 0.3);
}}

.{p("vis-pipe-step")}.is-live {{
  color: #18345d;
  border-color: #4a658b;
  background: rgba(74, 101, 139, 0.14);
  box-shadow: 0 0 0 1px rgba(74, 101, 139, 0.2);
}}

.{p("vis-flow")} {{
  display: flex;
  flex-wrap: wrap;
  gap: 0.3rem;
  justify-content: center;
}}

.{p("vis-flow-step")} {{
  font-size: 0.52rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  text-transform: uppercase;
  color: #64748b;
  padding: 0.2rem 0.42rem;
  border-radius: 999px;
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid rgba(148, 163, 184, 0.35);
}}

.{p("vis-flow-step")}.is-live {{
  color: #18345d;
  border-color: #4a658b;
  background: rgba(74, 101, 139, 0.12);
}}

.{p("vis-stats")} {{
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
  justify-content: center;
}}

.{p("vis-stat")} {{
  padding: 0.55rem 0.65rem;
  border-radius: 10px;
  background: #ffffff;
  border: 1px solid rgba(74, 101, 139, 0.14);
  box-shadow: 0 4px 12px rgba(24, 52, 93, 0.06);
}}

.{p("vis-stat")} b {{
  display: block;
  font-family: 'Clash Display', sans-serif;
  font-size: 0.95rem;
  font-weight: 600;
  color: #18345d;
  line-height: 1.2;
}}

.{p("vis-stat")} span {{
  display: block;
  font-size: 0.56rem;
  color: #64748b;
  margin-top: 0.1rem;
  text-transform: uppercase;
  letter-spacing: 0.06em;
}}

.{p("sc-slide-link")} {{
  display: inline-flex;
  align-self: flex-start;
  margin-top: 0.35rem;
  font-size: 0.72rem;
  font-weight: 600;
  color: #4a658b;
  text-decoration: none;
}}

.{p("sc-slide-link")}:hover {{
  color: #18345d;
  text-decoration: underline;
}}

#{SECTION_ID} .{p("benefits")} {{
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 0.65rem;
  margin-top: 1.35rem;
}}

#{SECTION_ID} .{p("benefit")} {{
  padding: 0.75rem 0.85rem;
  border-radius: 10px;
  background: rgba(255, 255, 255, 0.9);
  border: 1px solid rgba(74, 101, 139, 0.14);
}}

#{SECTION_ID} .{p("benefit")} strong {{
  display: block;
  font-size: 0.72rem;
  font-weight: 600;
  color: #18345d;
  margin-bottom: 0.15rem;
}}

#{SECTION_ID} .{p("benefit")} span {{
  font-size: 0.66rem;
  line-height: 1.45;
  color: #475569;
}}

#{SECTION_ID} .hub-clear-cta {{
  display: flex;
  flex-wrap: wrap;
  gap: 0.65rem;
  justify-content: center;
  margin-top: 1.25rem;
}}

@media (max-width: 900px) {{
  .{p("sc-slide-visual")} {{
    grid-template-columns: 1fr;
  }}
  #{SECTION_ID} .{p("benefits")} {{
    grid-template-columns: 1fr;
  }}
}}
'''
    (ROOT / "assets" / "lc-showcase.css").write_text(css + extra, encoding="utf-8")


def write_lc_js() -> None:
    ids = [s["id"] for s in STEPS]
    labels = {s["id"]: s["title"] for s in STEPS}
    detail_map = {f"lc-{s['id']}": s["id"] for s in STEPS}
    n = len(ids)
    js = f"""(function () {{
  'use strict';

  var STEP_ORDER = {ids!r};
  var labels = {labels!r};
  var detailMap = {detail_map!r};

  function init() {{
    var root = document.getElementById('lcShowcase');
    if (!root) return;

    var stage = root.querySelector('.{p("sc-stage")}');
    var presentation = root.querySelector('.{p("sc-presentation")}');
    var nodes = Array.prototype.slice.call(root.querySelectorAll('.{p("sc-node")}'));
    var slideEls = Array.prototype.slice.call(root.querySelectorAll('.{p("sc-slide")}'));
    var layerCards = Array.prototype.slice.call(document.querySelectorAll('#{SECTION_ID} .{p("layer-card")}'));
    var statusLabel = root.querySelector('[data-lc-status-label]');
    var metricEl = root.querySelector('[data-lc-metric]');
    var presProgress = root.querySelector('[data-lc-pres-progress]');
    var btnBack = root.querySelector('.{p("sc-back")}');
    var btnPrev = root.querySelector('.{p("sc-nav")}--prev');
    var btnNext = root.querySelector('.{p("sc-nav")}--next');
    var slidesViewport = root.querySelector('.{p("sc-slides-viewport")}');

    if (!stage || !presentation || !nodes.length || !slideEls.length) return;

    var slideMap = {{}};
    slideEls.forEach(function (slide) {{
      var id = slide.getAttribute('data-slide');
      if (id) slideMap[id] = slide;
    }});

    var stepIdx = 0;
    var isPresenting = false;
    var touchStartX = 0;
    var touchStartY = 0;

    function stepFromDetail(detail) {{
      return detailMap[detail] || detail;
    }}

    function indexForStep(step) {{
      var i = STEP_ORDER.indexOf(step);
      return i >= 0 ? i : 0;
    }}

    function clearSlideStates() {{
      slideEls.forEach(function (slide) {{
        slide.classList.remove('is-active');
        slide.setAttribute('aria-hidden', 'true');
      }});
    }}

    function setHubActive(step) {{
      nodes.forEach(function (node) {{
        var s = node.getAttribute('data-step');
        node.classList.toggle('is-active', s === step);
      }});
      layerCards.forEach(function (card) {{
        var d = stepFromDetail(card.getAttribute('data-detail'));
        card.classList.toggle('is-selected', d === step);
        if (d === step && !isPresenting) {{
          card.scrollIntoView({{ block: 'nearest', behavior: 'smooth' }});
        }}
      }});
      if (statusLabel && labels[step]) statusLabel.textContent = labels[step];
      if (metricEl) {{
        var idx = indexForStep(step);
        metricEl.innerHTML = '<strong>' + (idx + 1) + '</strong> / {n} stages';
      }}
    }}

    function setSlideActive(index) {{
      if (index < 0) index = STEP_ORDER.length - 1;
      if (index >= STEP_ORDER.length) index = 0;
      var targetId = STEP_ORDER[index];
      var targetSlide = slideMap[targetId];
      slideEls.forEach(function (slide) {{
        var isTarget = slide === targetSlide;
        slide.classList.toggle('is-active', isTarget);
        slide.setAttribute('aria-hidden', isTarget ? 'false' : 'true');
      }});
      stepIdx = index;
      setHubActive(targetId);
      if (presProgress) presProgress.innerHTML = '<strong>' + (index + 1) + '</strong> / {n}';
    }}

    function openPresentation(step) {{
      isPresenting = true;
      stage.classList.add('is-presenting');
      root.classList.add('is-presenting');
      presentation.setAttribute('aria-hidden', 'false');
      setSlideActive(indexForStep(step));
    }}

    function closePresentation() {{
      isPresenting = false;
      stage.classList.remove('is-presenting');
      root.classList.remove('is-presenting');
      presentation.setAttribute('aria-hidden', 'true');
      clearSlideStates();
      setHubActive(STEP_ORDER[stepIdx]);
    }}

    function nextSlide() {{ if (!isPresenting) return; setSlideActive(stepIdx + 1); }}
    function prevSlide() {{ if (!isPresenting) return; setSlideActive(stepIdx - 1); }}
    function selectStep(step) {{ if (STEP_ORDER.indexOf(step) < 0) return; openPresentation(step); }}

    clearSlideStates();
    presentation.setAttribute('aria-hidden', 'true');
    setHubActive(STEP_ORDER[0]);

    nodes.forEach(function (node) {{
      var step = node.getAttribute('data-step');
      node.addEventListener('click', function () {{ selectStep(step); }});
      node.setAttribute('tabindex', '0');
      node.setAttribute('role', 'button');
      node.addEventListener('keydown', function (e) {{
        if (e.key === 'Enter' || e.key === ' ') {{ e.preventDefault(); selectStep(step); }}
      }});
    }});

    layerCards.forEach(function (card) {{
      function activate() {{
        var d = card.getAttribute('data-detail');
        if (d) selectStep(stepFromDetail(d));
      }}
      card.addEventListener('click', activate);
      card.addEventListener('keydown', function (e) {{
        if (e.key === 'Enter' || e.key === ' ') {{ e.preventDefault(); activate(); }}
      }});
    }});

    if (btnBack) btnBack.addEventListener('click', function (e) {{ e.preventDefault(); closePresentation(); }});
    if (btnPrev) btnPrev.addEventListener('click', function (e) {{ e.preventDefault(); prevSlide(); }});
    if (btnNext) btnNext.addEventListener('click', function (e) {{ e.preventDefault(); nextSlide(); }});

    root.addEventListener('keydown', function (e) {{
      if (!isPresenting) return;
      if (e.key === 'ArrowRight') {{ e.preventDefault(); nextSlide(); }}
      if (e.key === 'ArrowLeft') {{ e.preventDefault(); prevSlide(); }}
      if (e.key === 'Escape') {{ e.preventDefault(); closePresentation(); }}
    }});

    if (slidesViewport) {{
      slidesViewport.addEventListener('touchstart', function (e) {{
        if (!isPresenting || !e.touches.length) return;
        touchStartX = e.touches[0].clientX;
        touchStartY = e.touches[0].clientY;
      }}, {{ passive: true }});
      slidesViewport.addEventListener('touchend', function (e) {{
        if (!isPresenting || !e.changedTouches.length) return;
        var dx = e.changedTouches[0].clientX - touchStartX;
        var dy = e.changedTouches[0].clientY - touchStartY;
        if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 40) {{
          if (dx < 0) nextSlide(); else prevSlide();
        }}
      }}, {{ passive: true }});
    }}
  }}

  if (document.readyState === 'loading') {{
    document.addEventListener('DOMContentLoaded', init);
  }} else {{
    init();
  }}
}})();
"""
    (ROOT / "assets" / "lc-showcase.js").write_text(js, encoding="utf-8")


SECTION_RE = re.compile(
    r"<!-- CALL LIFECYCLE HUB.*?</section>",
    re.DOTALL,
)


def patch_index() -> None:
    text = INDEX.read_text(encoding="utf-8")
    new_section = build_section_html()
    if not SECTION_RE.search(text):
        raise SystemExit("Could not find call lifecycle section in index.html")
    text = SECTION_RE.sub(new_section, text, count=1)

    if "lc-showcase.css" not in text:
        text = text.replace(
            'href="assets/camp-showcase.css"',
            'href="assets/camp-showcase.css" />\n  <link rel="stylesheet" href="assets/lc-showcase.css"',
        )

    if "lc-showcase.js" not in text:
        text = text.replace(
            'src="assets/camp-showcase.js"',
            'src="assets/camp-showcase.js" defer></script>\n  <script src="assets/lc-showcase.js"',
        )

    if "Call lifecycle premium showcase" not in text:
        text = text.replace(
            "body[data-page=\"home\"] .demo-video {",
            INLINE_STYLE + "\n  body[data-page=\"home\"] .demo-video {",
        )

    INDEX.write_text(text, encoding="utf-8")


def main():
    write_lc_css()
    write_lc_js()
    patch_index()
    print(f"OK: call lifecycle premium showcase ({len(STEPS)} stages)")


if __name__ == "__main__":
    main()
