"""
Replace home #agents inline cards with unified EMAAVY agents promo.
Adds agents-promo CSS and creates pages/agents/workforce.html hub.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "emaavy_white_blue (2).html"
WORKFORCE = ROOT / "pages" / "agents" / "workforce.html"
INDEX = ROOT / "pages" / "agents" / "index.html"

AGENTS_CSS = """
/* ═══ AGENTS — unified landing promo ═══ */
.agents-promo-shell {
  padding: clamp(2rem, 4vw, 2.75rem) clamp(1.25rem, 4vw, 2.25rem) !important;
}
.agents-promo {
  display: grid !important;
  grid-template-columns: 1.05fr 0.95fr !important;
  gap: clamp(1.5rem, 4vw, 2.25rem) !important;
  align-items: start !important;
  text-align: left !important;
  margin-bottom: 1.75rem !important;
}
.agents-promo h3 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(1.5rem, 3.2vw, 2.1rem) !important;
  font-weight: 600 !important;
  letter-spacing: -0.03em !important;
  line-height: 1.12 !important;
  color: #0f172a !important;
  margin: 0 0 1rem !important;
  max-width: 22ch !important;
}
.agents-promo-lead {
  font-size: clamp(0.9rem, 1.45vw, 1.02rem) !important;
  line-height: 1.7 !important;
  color: #475569 !important;
  margin: 0 0 1.2rem !important;
  max-width: 54ch !important;
}
.agents-promo-highlights {
  list-style: none !important;
  margin: 0 0 1.6rem !important;
  padding: 0 !important;
  display: grid !important;
  gap: 0.5rem !important;
}
.agents-promo-highlights li {
  font-size: 0.86rem !important;
  line-height: 1.55 !important;
  color: #64748b !important;
  padding: 0.32rem 0 0.32rem 0.85rem !important;
  border-left: 3px solid #4A658B !important;
}
.agents-promo-highlights strong { color: #0f172a !important; font-weight: 600 !important; }
.agents-promo-actions {
  display: flex !important;
  flex-wrap: wrap !important;
  gap: 0.7rem !important;
}
.btn-agents-explore {
  display: inline-flex !important;
  align-items: center !important;
  padding: 0.82rem 1.5rem !important;
  font-size: 0.9rem !important;
  font-weight: 600 !important;
  color: #fff !important;
  background: #4A658B !important;
  border: none !important;
  border-radius: 8px !important;
  text-decoration: none !important;
  box-shadow: 0 4px 14px rgba(74, 101, 139, 0.28) !important;
}
.btn-agents-explore:hover { background: #18345D !important; transform: translateY(-1px) !important; }
.btn-agents-secondary {
  display: inline-flex !important;
  align-items: center !important;
  padding: 0.8rem 1.3rem !important;
  font-size: 0.86rem !important;
  font-weight: 600 !important;
  color: #4A658B !important;
  background: #fff !important;
  border: 1px solid #cbd5e1 !important;
  border-radius: 8px !important;
  text-decoration: none !important;
}
.btn-agents-secondary:hover { border-color: #4A658B !important; background: #f8fafc !important; }
.agents-promo-panel {
  padding: 1.2rem 1rem !important;
  border-radius: 10px !important;
  background: linear-gradient(145deg, #f8fafc 0%, #f0f4f8 100%) !important;
  border: 1px solid #e2e8f0 !important;
}
.agents-promo-panel-head {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.92rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  margin-bottom: 0.75rem !important;
}
.agents-role-cards { display: grid !important; gap: 0.45rem !important; }
.agents-role-card {
  display: grid !important;
  grid-template-columns: 1fr auto !important;
  grid-template-rows: auto auto !important;
  gap: 0.1rem 0.5rem !important;
  padding: 0.65rem 0.75rem !important;
  border-radius: 8px !important;
  background: #fff !important;
  border: 1px solid #e2e8f0 !important;
  text-decoration: none !important;
  transition: border-color 0.2s, box-shadow 0.2s !important;
}
.agents-role-card:hover {
  border-color: #4A658B !important;
  box-shadow: 0 6px 18px rgba(15, 23, 42, 0.06) !important;
}
.agents-role-label {
  grid-column: 1 !important;
  font-size: 0.58rem !important;
  font-weight: 600 !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
}
.agents-role-card strong {
  grid-column: 1 !important;
  font-size: 0.88rem !important;
  color: #0f172a !important;
  font-weight: 600 !important;
}
.agents-role-meta {
  grid-column: 2 !important;
  grid-row: 1 / span 2 !important;
  align-self: center !important;
  font-size: 0.62rem !important;
  color: #4A658B !important;
  text-align: right !important;
  max-width: 11ch !important;
  line-height: 1.35 !important;
}
.agents-promo-stats {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 0.65rem !important;
  padding-top: 0.25rem !important;
  border-top: 1px solid #e2e8f0 !important;
}
.agents-promo-stats .int-stat {
  text-align: center !important;
  padding: 0.85rem 0.5rem !important;
  background: #f8fafc !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 8px !important;
}
.agents-promo-stats .int-stat b {
  display: block !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: 1.25rem !important;
  color: #4A658B !important;
  margin-bottom: 0.2rem !important;
}
@media (max-width: 900px) {
  .agents-promo { grid-template-columns: 1fr !important; }
  .agents-promo h3 { max-width: none !important; }
  .agents-promo-stats { grid-template-columns: repeat(2, 1fr) !important; }
  .agents-role-meta { display: none !important; }
}
"""

AGENTS_SECTION = """<!-- AGENTS HUB --> <section id="agents" class="cap-section">
 <div class="features-head reveal">
  <span class="section-kicker">AI Workforce · Voice Agents</span>
  <h2>Meet your AI workforce</h2>
  <p class="int-hub-desc">EMAAVY deploys sales, support, and campaign agents with human-like voice — each on its own page. Explore roles, specs, and the builder without scrolling through everything on the home page.</p>
 </div>
 <div class="int-showcase reveal agents-promo-wrap" id="agents-emaavy">
  <div class="int-shell agents-promo-shell">
    <div class="agents-promo reveal">
      <div class="agents-promo-copy">
        <span class="section-kicker">AI Workforce · EMAAVY</span>
        <h3>Voice agents that sell, support, and scale — on one platform</h3>
        <p class="agents-promo-lead">EMAAVY is where your AI workforce lives: dedicated agents with their own voice, flow, and mission. Configure once, run 24/7 across 22 languages, and open any role for full capabilities on its own page.</p>
        <ul class="agents-promo-highlights" aria-label="Agent highlights">
          <li><strong>Four ready roles</strong> — sales, support, outbound campaigns, and custom builder flows</li>
          <li><strong>Human-like voice</strong> — Bulbul V3 and ElevenTurbo with natural Hinglish and regional fluency</li>
          <li><strong>Live intelligence</strong> — intent scoring, CRM sync, and supervisor handoff built in</li>
          <li><strong>Minutes to deploy</strong> — visual flow builder, no code required to go live</li>
        </ul>
        <div class="agents-promo-actions">
          <a href="pages/agents/workforce.html" class="btn-agents-explore">Explore all agents</a>
          <a href="book-demo.html" class="btn-agents-secondary">Book a demo</a>
        </div>
      </div>
      <div class="agents-promo-panel" aria-hidden="true">
        <div class="agents-promo-panel-head">Agent roles on EMAAVY</div>
        <div class="agents-role-cards">
          <a href="pages/agents/sales-agent.html" class="agents-role-card">
            <span class="agents-role-label">01 · Sales</span>
            <strong>Sales Agent</strong>
            <span class="agents-role-meta">28% conversion lift</span>
          </a>
          <a href="pages/agents/support-agent.html" class="agents-role-card">
            <span class="agents-role-label">02 · Support</span>
            <strong>Support Agent</strong>
            <span class="agents-role-meta">61% faster resolution</span>
          </a>
          <a href="pages/agents/outbound-agent.html" class="agents-role-card">
            <span class="agents-role-label">03 · Campaign</span>
            <strong>Campaign Agent</strong>
            <span class="agents-role-meta">10M+ contacts</span>
          </a>
          <a href="pages/agents/workforce.html#builder" class="agents-role-card">
            <span class="agents-role-label">04 · Builder</span>
            <strong>Custom Agent Builder</strong>
            <span class="agents-role-meta">Visual flows</span>
          </a>
        </div>
      </div>
    </div>
    <div class="agents-promo-stats">
      <div class="int-stat"><span class="int-stat-dot" aria-hidden="true"></span><b>24/7</b><span>Always on</span></div>
      <div class="int-stat"><b>22</b><span>Languages</span></div>
      <div class="int-stat"><b>4</b><span>Agent roles</span></div>
      <div class="int-stat"><b>&lt;15m</b><span>To first call</span></div>
    </div>
  </div>
 </div>
</section>"""

WORKFORCE_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>AI Voice Workforce — EMAAVY</title>
  <meta name="description" content="Deploy EMAAVY AI voice agents for sales, support, and outbound campaigns — human-like voice, live intelligence, and visual builder flows." />
  <meta name="robots" content="index, follow" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=general-sans@300,400,500,600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../assets/nav.css" />
  <link rel="stylesheet" href="../../assets/site.css" />
</head>
<body data-base="../../" data-route="agents-workforce">
  <div id="site-nav-root"></div>
  <main class="page-main int-category-page">
    <section class="page-hero telephony-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="../../emaavy_white_blue%20(2).html">Home</a>
          <span aria-hidden="true"> / </span>
          <a href="../../emaavy_white_blue%20(2).html#agents">Agents</a>
          <span aria-hidden="true"> / </span>
          <span>AI Workforce</span>
        </nav>
        <span class="page-kicker">AI Workforce · Voice Agents</span>
        <h1>Meet your AI workforce</h1>
        <p class="telephony-hero-lead">Agents that speak like humans, think faster, and never call in sick. Deploy in minutes — each with its own voice, flow, and mission — running 24/7 across every language you serve.</p>
        <div class="stat-row telephony-hero-stats">
          <div class="stat-box"><b>24/7</b><span>Always on</span></div>
          <div class="stat-box"><b>22</b><span>Languages</span></div>
          <div class="stat-box"><b>4</b><span>Agent roles</span></div>
        </div>
        <div class="capabilities-jump telephony-jump">
          <a href="#emaavy-agents">EMAAVY &amp; agents</a>
          <a href="#roles">Agent roles</a>
          <a href="#builder">Custom builder</a>
          <a href="#deploy">Deploy flow</a>
        </div>
      </div>
    </section>

    <section id="emaavy-agents" class="page-section">
      <div class="container">
        <article class="capability-block">
          <div class="capability-block-inner">
            <div class="capability-meta">
              <span class="capability-num">—</span>
              <span class="capability-tag">EMAAVY · AI Workforce</span>
            </div>
            <div class="capability-content">
              <h2>How EMAAVY runs your voice agents</h2>
              <p class="capability-lead">One platform for every conversational role. Operations launches campaigns; engineering wires LLM, STT, TTS, and tools once — then swaps voices and flows per agent without rebuilding the stack.</p>
              <ul class="capability-points">
                <li><strong>Per-agent routing</strong> — unique voice, prompt stack, and integration map per role.</li>
                <li><strong>Live handoff</strong> — supervisors join or take over when sentiment or intent signals escalation.</li>
                <li><strong>Campaign scale</strong> — intelligent pacing, retry, and timezone-aware outreach to millions.</li>
                <li><strong>Full logging</strong> — transcripts, scores, and CRM dispositions on every conversation.</li>
              </ul>
            </div>
          </div>
        </article>
      </div>
    </section>

    <section id="roles" class="page-section alt">
      <div class="container">
        <h2 class="section-title">Agent roles</h2>
        <p class="section-desc">Each role has a dedicated page with specs, stats, and deployment paths — open in the same tab from home or nav.</p>
        <div class="int-layer-nav">
          <a href="sales-agent.html" class="int-layer-pill">Sales</a>
          <a href="support-agent.html" class="int-layer-pill">Support</a>
          <a href="outbound-agent.html" class="int-layer-pill">Campaign</a>
          <a href="#builder" class="int-layer-pill">Builder</a>
        </div>
        <div class="telephony-provider-grid">
          <article id="sales" class="telephony-provider-card">
            <span class="telephony-provider-tag">Voice · Sales</span>
            <h3>Sales Agent</h3>
            <p>Qualifies leads, handles objections, and books meetings — with natural Hinglish and regional language fluency.</p>
            <ul class="feature-list compact">
              <li>Multi-step objection handling</li>
              <li>Live Cal.com booking</li>
              <li>Intent scoring &amp; CRM sync</li>
            </ul>
            <a href="sales-agent.html" class="telephony-provider-link">Sales Agent details →</a>
          </article>
          <article id="support" class="telephony-provider-card">
            <span class="telephony-provider-tag">Voice · Support</span>
            <h3>Support Agent</h3>
            <p>Resolves issues, de-escalates frustrated callers, and routes complex cases to humans with full context.</p>
            <ul class="feature-list compact">
              <li>Sentiment-aware responses</li>
              <li>Auto ticket creation</li>
              <li>Human escalation triggers</li>
            </ul>
            <a href="support-agent.html" class="telephony-provider-link">Support Agent details →</a>
          </article>
          <article id="campaign" class="telephony-provider-card">
            <span class="telephony-provider-tag">Outbound · Campaigns</span>
            <h3>Campaign Agent</h3>
            <p>Runs high-volume outreach — registrations, follow-ups, and reminders across thousands of contacts.</p>
            <ul class="feature-list compact">
              <li>Campaign pacing &amp; retry</li>
              <li>Personalized scripts</li>
              <li>WhatsApp confirmations</li>
            </ul>
            <a href="outbound-agent.html" class="telephony-provider-link">Campaign Agent details →</a>
          </article>
        </div>
      </div>
    </section>

    <section id="builder" class="page-section">
      <div class="container">
        <article class="capability-block">
          <div class="capability-block-inner">
            <div class="capability-meta">
              <span class="capability-num">04</span>
              <span class="capability-tag">AI Agents · Builder</span>
            </div>
            <div class="capability-content">
              <h2>Custom Agent Builder</h2>
              <p class="capability-lead">Design any voice flow in minutes — pick a voice, set prompts, branch logic, and deploy across languages. No code required to go live.</p>
              <ul class="capability-points">
                <li>Visual drag-and-drop flow builder</li>
                <li>Bulbul V3 &amp; ElevenTurbo voice selection</li>
                <li>Custom multi-step branching logic</li>
                <li>Per-agent LLM &amp; STT routing</li>
              </ul>
              <div class="cta-row" style="margin-top:1.25rem">
                <a href="../../book-demo.html" class="btn-primary">Build your agent →</a>
                <a href="../../pages/documentation.html" class="btn-outline">Agent builder docs</a>
              </div>
            </div>
          </div>
        </article>
      </div>
    </section>

    <section id="deploy" class="page-section alt">
      <div class="container">
        <h2 class="section-title">From idea to live calls</h2>
        <div class="telephony-flow-panel">
          <ol class="telephony-flow-steps">
            <li><span class="telephony-flow-num">01</span><strong>Choose a role</strong><p>Start from Sales, Support, Campaign, or a blank builder template.</p></li>
            <li><span class="telephony-flow-num">02</span><strong>Configure voice &amp; flow</strong><p>Set prompts, branching, languages, and integration triggers.</p></li>
            <li><span class="telephony-flow-num">03</span><strong>Connect stack</strong><p>Wire telephony, LLM, STT, TTS, and CRM through EMAAVY layers.</p></li>
            <li><span class="telephony-flow-num">04</span><strong>Launch campaign</strong><p>Upload contacts, set pacing, and monitor live performance.</p></li>
            <li><span class="telephony-flow-num">05</span><strong>Optimize</strong><p>Scores and transcripts feed coaching and script improvements automatically.</p></li>
          </ol>
        </div>
      </div>
    </section>

    <section class="page-section">
      <div class="container capabilities-page-cta">
        <h2>Deploy your AI workforce on EMAAVY</h2>
        <p>See live agents handling sales, support, and campaigns in a tailored demo.</p>
        <div class="cta-row">
          <a href="../../book-demo.html" class="btn-primary">Book a demo</a>
          <a href="index.html" class="btn-outline">Agent directory</a>
        </div>
      </div>
    </section>
  </main>
  <div id="site-footer-root"></div>
  <script src="../../assets/routes.js"></script>
  <script src="../../assets/components.js"></script>
  <script src="../../assets/nav.js"></script>
</body>
</html>
"""

INDEX_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>AI Voice Agents — EMAAVY</title>
  <meta name="description" content="Deploy EMAAVY AI voice agents for sales, support, and outbound campaigns at any scale." />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="AI Voice Agents — EMAAVY" />
  <meta property="og:description" content="Deploy EMAAVY AI voice agents for sales, support, and outbound campaigns at any scale." />
  <meta property="og:type" content="website" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=general-sans@300,400,500,600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../assets/nav.css" />
  <link rel="stylesheet" href="../../assets/site.css" />
</head>
<body data-base="../../" data-route="agents">
  <div id="site-nav-root"></div>
  <main class="page-main">
    <section class="page-hero">
      <div class="container">
        <span class="page-kicker">AI Workforce</span>
        <h1>Meet your AI agents</h1>
        <p>Agents that speak like humans, think faster, and never call in sick — explore the full workforce overview or jump to a role.</p>
        <div class="cta-row" style="margin-top:1.25rem">
          <a href="workforce.html" class="btn-primary">Full workforce overview →</a>
        </div>
      </div>
    </section>
    <section class="page-section">
      <div class="container">
        <div class="int-layer-nav">
          <a href="workforce.html" class="int-layer-pill">Overview</a>
          <a href="sales-agent.html" class="int-layer-pill">Sales</a>
          <a href="support-agent.html" class="int-layer-pill">Support</a>
          <a href="outbound-agent.html" class="int-layer-pill">Campaign</a>
          <a href="workforce.html#builder" class="int-layer-pill">Builder</a>
        </div>
        <div class="card-grid cols-2">
          <a href="sales-agent.html" class="glow-card"><div class="card-icon"><span class="brand-mark">SA</span></div><h3>Sales Agent</h3><p>Qualifies leads, handles objections, and books meetings with human-like persuasion.</p><span class="card-tag">Deploy →</span></a>
          <a href="support-agent.html" class="glow-card"><div class="card-icon"><span class="brand-mark">SU</span></div><h3>Support Agent</h3><p>Empathetic support for ticket triage, FAQ resolution, and escalation to specialists.</p><span class="card-tag">Deploy →</span></a>
          <a href="outbound-agent.html" class="glow-card"><div class="card-icon"><span class="brand-mark">CA</span></div><h3>Campaign Agent</h3><p>High-volume outreach for registrations, follow-ups, and lead qualification at scale.</p><span class="card-tag">Deploy →</span></a>
          <a href="workforce.html#builder" class="glow-card"><div class="card-icon"><span class="brand-mark">CB</span></div><h3>Custom Agent Builder</h3><p>Visual flows, custom prompts, and multi-language deployment in minutes.</p><span class="card-tag">Build →</span></a>
        </div>
        <div class="cta-row" style="margin-top:2rem"><a href="../../book-demo.html" class="btn-primary">Build your agent →</a></div>
      </div>
    </section>
  </main>
  <div id="site-footer-root"></div>
  <script src="../../assets/routes.js"></script>
  <script src="../../assets/components.js"></script>
  <script src="../../assets/nav.js"></script>
</body>
</html>
"""


def main():
    text = HTML.read_text(encoding="utf-8")

    if "/* ═══ AGENTS — unified landing promo ═══ */" not in text:
        marker = "/* ═══ INTEGRATIONS — unified landing promo ═══ */"
        if marker not in text:
            raise SystemExit("integrations CSS marker not found")
        end = text.find("/* ═══ TELEPHONY — landing promo", text.index(marker))
        if end < 0:
            end = text.find("@media (max-width: 900px)", text.index(marker))
            end = text.find("}", end) + 1
        insert_at = text.rfind("}", 0, end) + 1
        text = text[:insert_at] + AGENTS_CSS + text[insert_at:]

    pattern = re.compile(
        r"<!-- AGENTS -->.*?</section>\s*<!-- CASE STUDIES -->",
        re.DOTALL,
    )
    if not pattern.search(text):
        raise SystemExit("agents section not found")
    text = pattern.sub(AGENTS_SECTION + "\n <!-- CASE STUDIES -->", text, count=1)

    HTML.write_text(text, encoding="utf-8")
    WORKFORCE.write_text(WORKFORCE_HTML, encoding="utf-8")
    INDEX.write_text(INDEX_HTML, encoding="utf-8")

    routes = (ROOT / "assets" / "routes.js").read_text(encoding="utf-8")
    if "workforce.html" not in routes:
        routes = routes.replace(
            "agents: [\n    { id: 'sales-agent'",
            "agents: [\n    { id: 'workforce', label: 'AI Workforce', path: 'pages/agents/workforce.html' },\n    { id: 'sales-agent'",
        )
        (ROOT / "assets" / "routes.js").write_text(routes, encoding="utf-8")

    print("OK: unified agents promo, workforce.html, index updated")


if __name__ == "__main__":
    main()
