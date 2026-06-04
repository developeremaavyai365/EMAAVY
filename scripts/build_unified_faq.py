"""
Redesign home #faq as unified promo; create pages/faq/*.html with descriptive answers.
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "emaavy_white_blue (2).html"
FAQ_DIR = ROOT / "pages" / "faq"
HUB = ROOT / "pages" / "faq.html"
ROUTES = ROOT / "assets" / "routes.js"
HOME = "emaavy_white_blue%20(2).html"

FAQ_CSS = r"""
/* ═══ FAQ — unified landing promo ═══ */
#faq.faq-hub-section {
  position: relative !important;
  overflow: hidden !important;
  background: linear-gradient(165deg, #f8fafc 0%, #eef2f7 42%, #ffffff 100%) !important;
}
#faq.faq-hub-section::before {
  content: '' !important;
  position: absolute !important;
  inset: 0 !important;
  background:
    radial-gradient(ellipse 70% 55% at 12% 20%, rgba(74, 101, 139, 0.14) 0%, transparent 55%),
    radial-gradient(ellipse 60% 50% at 88% 75%, rgba(24, 52, 93, 0.1) 0%, transparent 50%) !important;
  pointer-events: none !important;
  z-index: 0 !important;
}
#faq .features-head,
#faq .faq-promo-wrap { position: relative !important; z-index: 1 !important; }
.faq-promo-shell {
  padding: clamp(2rem, 4vw, 2.75rem) clamp(1.25rem, 4vw, 2.25rem) !important;
  border-radius: 14px !important;
  background: linear-gradient(145deg, rgba(255,255,255,0.92) 0%, rgba(248,250,252,0.88) 100%) !important;
  border: 1px solid #e2e8f0 !important;
  box-shadow: 0 20px 50px rgba(15, 23, 42, 0.06), 0 1px 0 rgba(255,255,255,0.8) inset !important;
}
.faq-promo {
  display: grid !important;
  grid-template-columns: 1fr 1.15fr !important;
  gap: clamp(1.5rem, 4vw, 2.25rem) !important;
  align-items: start !important;
  margin-bottom: 1.75rem !important;
}
.faq-promo h3 {
  font-family: 'Clash Display', sans-serif !important;
  font-size: clamp(1.55rem, 3.4vw, 2.15rem) !important;
  font-weight: 600 !important;
  letter-spacing: -0.03em !important;
  line-height: 1.1 !important;
  color: #0f172a !important;
  margin: 0 0 1rem !important;
  max-width: 20ch !important;
}
.faq-promo-lead {
  font-size: clamp(0.92rem, 1.5vw, 1.05rem) !important;
  line-height: 1.72 !important;
  color: #475569 !important;
  margin: 0 0 1.25rem !important;
  max-width: 52ch !important;
}
.faq-promo-highlights {
  list-style: none !important;
  margin: 0 0 1.5rem !important;
  padding: 0 !important;
  display: grid !important;
  gap: 0.55rem !important;
}
.faq-promo-highlights li {
  font-size: 0.86rem !important;
  line-height: 1.55 !important;
  color: #64748b !important;
  padding: 0.38rem 0 0.38rem 0.9rem !important;
  border-left: 3px solid #4A658B !important;
}
.faq-promo-highlights strong { color: #0f172a !important; font-weight: 600 !important; }
.faq-promo-actions { display: flex !important; flex-wrap: wrap !important; gap: 0.7rem !important; }
.btn-faq-explore {
  display: inline-flex !important;
  align-items: center !important;
  padding: 0.85rem 1.55rem !important;
  font-size: 0.9rem !important;
  font-weight: 600 !important;
  color: #fff !important;
  background: linear-gradient(135deg, #4A658B 0%, #18345D 100%) !important;
  border: none !important;
  border-radius: 10px !important;
  text-decoration: none !important;
  box-shadow: 0 6px 20px rgba(74, 101, 139, 0.35) !important;
  transition: transform 0.2s, box-shadow 0.2s !important;
}
.btn-faq-explore:hover {
  transform: translateY(-2px) !important;
  box-shadow: 0 10px 28px rgba(24, 52, 93, 0.38) !important;
}
.btn-faq-secondary {
  display: inline-flex !important;
  align-items: center !important;
  padding: 0.82rem 1.35rem !important;
  font-size: 0.86rem !important;
  font-weight: 600 !important;
  color: #4A658B !important;
  background: #fff !important;
  border: 1px solid #cbd5e1 !important;
  border-radius: 10px !important;
  text-decoration: none !important;
}
.btn-faq-secondary:hover { border-color: #4A658B !important; background: #f8fafc !important; }
.faq-promo-panel {
  padding: 1.15rem !important;
  border-radius: 12px !important;
  background: linear-gradient(160deg, #f8fafc 0%, #f1f5f9 100%) !important;
  border: 1px solid #e2e8f0 !important;
}
.faq-promo-panel-head {
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.95rem !important;
  font-weight: 600 !important;
  color: #0f172a !important;
  margin-bottom: 0.85rem !important;
  padding-bottom: 0.65rem !important;
  border-bottom: 1px solid #e2e8f0 !important;
}
.faq-topic-grid {
  display: grid !important;
  grid-template-columns: repeat(2, 1fr) !important;
  gap: 0.55rem !important;
}
.faq-topic-card {
  --faq-accent: #4A658B;
  display: grid !important;
  grid-template-columns: auto 1fr !important;
  gap: 0.65rem !important;
  padding: 0.75rem 0.8rem !important;
  border-radius: 10px !important;
  background: #fff !important;
  border: 1px solid #e2e8f0 !important;
  text-decoration: none !important;
  transition: border-color 0.22s, box-shadow 0.22s, transform 0.22s !important;
  position: relative !important;
  overflow: hidden !important;
}
.faq-topic-card::before {
  content: '' !important;
  position: absolute !important;
  left: 0 !important;
  top: 0 !important;
  bottom: 0 !important;
  width: 3px !important;
  background: var(--faq-accent) !important;
  opacity: 0.85 !important;
}
.faq-topic-card:hover {
  border-color: var(--faq-accent) !important;
  box-shadow: 0 10px 24px rgba(15, 23, 42, 0.08) !important;
  transform: translateY(-2px) !important;
}
.faq-topic-card:hover .faq-topic-explore { color: #18345D !important; }
.faq-topic-icon {
  width: 2.1rem !important;
  height: 2.1rem !important;
  border-radius: 8px !important;
  display: flex !important;
  align-items: center !important;
  justify-content: center !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: 0.72rem !important;
  font-weight: 700 !important;
  color: #fff !important;
  background: linear-gradient(135deg, var(--faq-accent), #18345D) !important;
  flex-shrink: 0 !important;
}
.faq-topic-body { min-width: 0 !important; }
.faq-topic-label {
  display: block !important;
  font-size: 0.58rem !important;
  font-weight: 700 !important;
  letter-spacing: 0.07em !important;
  text-transform: uppercase !important;
  color: #64748b !important;
  margin-bottom: 0.15rem !important;
}
.faq-topic-card strong {
  display: block !important;
  font-size: 0.82rem !important;
  line-height: 1.35 !important;
  color: #0f172a !important;
  font-weight: 600 !important;
  margin-bottom: 0.2rem !important;
}
.faq-topic-snippet {
  display: block !important;
  font-size: 0.68rem !important;
  line-height: 1.45 !important;
  color: #64748b !important;
}
.faq-topic-explore {
  display: block !important;
  font-size: 0.66rem !important;
  font-weight: 600 !important;
  color: #4A658B !important;
  margin-top: 0.35rem !important;
}
.faq-topic-card[data-topic="go-live"] { --faq-accent: #4A658B; }
.faq-topic-card[data-topic="voice-models"] { --faq-accent: #3d5a80; }
.faq-topic-card[data-topic="compliance"] { --faq-accent: #18345D; }
.faq-topic-card[data-topic="pricing-scale"] { --faq-accent: #5b7a9d; }
.faq-topic-card[data-topic="crm-integrations"] { --faq-accent: #2563eb; }
.faq-topic-card[data-topic="enterprise-support"] { --faq-accent: #1e3a5f; }
.faq-promo-stats {
  display: grid !important;
  grid-template-columns: repeat(4, 1fr) !important;
  gap: 0.65rem !important;
  padding-top: 0.35rem !important;
  border-top: 1px solid #e2e8f0 !important;
}
.faq-promo-stats .int-stat {
  text-align: center !important;
  padding: 0.9rem 0.5rem !important;
  background: #fff !important;
  border: 1px solid #e2e8f0 !important;
  border-radius: 10px !important;
}
.faq-promo-stats .int-stat b {
  display: block !important;
  font-family: 'Clash Display', sans-serif !important;
  font-size: 1.2rem !important;
  color: #4A658B !important;
  margin-bottom: 0.15rem !important;
}
@media (max-width: 960px) {
  .faq-promo { grid-template-columns: 1fr !important; }
  .faq-promo h3 { max-width: none !important; }
  .faq-topic-grid { grid-template-columns: 1fr !important; }
  .faq-promo-stats { grid-template-columns: repeat(2, 1fr) !important; }
}
"""

TOPICS = {
    "go-live": {
        "route": "faq-go-live",
        "num": "01",
        "icon": "GO",
        "kicker": "Getting started · Launch",
        "title": "How fast can we go live?",
        "meta": "< 48 hours",
        "snippet": "Same-day launch on Starter & Pro with zero infra changes.",
        "hero_lead": "Most EMAAVY customers run their first live call within 48 hours — many on Starter or Pro go live the same day they sign up, with no telephony migration or infrastructure project required.",
        "stats": [("&lt;48h", "Typical go-live"), ("0", "Infra changes"), ("15m", "Quickstart path")],
        "short_answer": "Starter and Pro teams routinely go live in under 48 hours. Same-day launch is common when you already have numbers or use EMAAVY-native telephony — no rip-and-replace of your stack.",
        "deep_dive": [
            (
                "What “go live” actually means",
                "Going live on EMAAVY means your telephony source is connected (Vobiz, SIP, or a supported carrier), at least one STT and LLM route is configured, and your first campaign or inbound flow can place or receive a scored call. You do not need to rebuild CRM, retrain agents on new desktops, or wait for batch transcription pipelines.",
            ),
            (
                "The typical 48-hour path",
                "Day zero: account, API keys, and number provisioning. Hours 2–8: agent or campaign flow in the visual builder, language and voice selection, webhook smoke test. Hours 8–24: pilot list of 50–200 calls, supervisor live view validation. Hours 24–48: scale pacing, CRM mapping, and production alerting.",
            ),
            (
                "Same-day launch scenarios",
                "Teams that start with outbound-only pilots, use EMAAVY-managed numbers, and keep CRM sync to webhooks-only often place their first production calls the afternoon of signup. Enterprise VPC or SSO setups extend the timeline — but not the core voice intelligence layer.",
            ),
        ],
        "typical_questions": [
            "Do we need to port numbers before testing?",
            "Can we run a pilot without touching production CRM?",
            "What blockers usually delay launch past a week?",
        ],
        "emaavy_handles": [
            "Guided quickstart in Documentation — signup to first call in ~15 minutes for sandbox flows.",
            "Pre-built templates for sales, support, and registration campaigns.",
            "Sandbox API keys and test numbers so engineering validates webhooks before production traffic.",
            "Dedicated solutions engineer on Business+ for complex routing or multi-region rollouts.",
        ],
        "related": ["crm-integrations", "pricing-scale", "enterprise-support"],
    },
    "voice-models": {
        "route": "faq-voice-models",
        "num": "02",
        "icon": "VM",
        "kicker": "AI & voice · Customization",
        "title": "Can we use our own voice models?",
        "meta": "Business+",
        "snippet": "Custom voices, prompts, and per-intent model routing.",
        "hero_lead": "Yes — Business and Enterprise plans support custom voice synthesis, prompt stacks, and model routing rules so you can align tone, language, and reasoning depth with your brand and compliance needs.",
        "stats": [("22+", "Languages"), ("Custom", "Voices"), ("Multi", "LLM routes")],
        "short_answer": "Business and Enterprise customers can bring custom TTS voices (including cloned brand voices where policy allows), tune prompt stacks per campaign, and route intents to different LLMs — e.g. Claude for nuance, Gemini Flash for speed.",
        "deep_dive": [
            (
                "Custom voices and TTS",
                "EMAAVY integrates ElevenLabs, Flash/Bulbul, and other TTS providers. Business plans can select premium voices; Enterprise can deploy cloned or custom-trained voices with approval workflows and telephony-optimized audio profiles.",
            ),
            (
                "Prompt stacks and flows",
                "Rather than a single monolithic prompt, EMAAVY agents use staged prompts — opener, discovery, objection, close — each editable per campaign. Versioning lets you A/B scripts without redeploying telephony.",
            ),
            (
                "Model routing by intent",
                "Route high-stakes compliance dialogue to Claude, volume scoring to Gemini Flash, and multilingual Hinglish to Qwen — all within one agent flow. Routing rules trigger on detected intent, language, or supervisor override.",
            ),
        ],
        "typical_questions": [
            "Can we use our own fine-tuned LLM?",
            "Is voice cloning allowed for regulated industries?",
            "How do we test a new voice before full rollout?",
        ],
        "emaavy_handles": [
            "Provider abstraction — swap STT/TTS/LLM without rewriting call flows.",
            "Side-by-side A/B on pilot campaigns with conversion and sentiment comparison.",
            "Enterprise VPC option for models that cannot leave your network boundary.",
            "Agent Builder documentation for prompt engineering patterns.",
        ],
        "related": ["go-live", "compliance", "enterprise-support"],
    },
    "compliance": {
        "route": "faq-compliance",
        "num": "03",
        "icon": "CP",
        "kicker": "Security · Compliance",
        "title": "Compliance and audit logs",
        "meta": "SOC 2 aligned",
        "snippet": "Encryption, retention controls, and exportable audit trails.",
        "hero_lead": "EMAAVY is built for regulated teams: encryption in transit and at rest, configurable retention, PII handling, compliance keyword flagging, and audit logs you can export for internal risk and external assessors.",
        "stats": [("SOC 2", "Aligned"), ("256-bit", "Encryption"), ("Full", "Audit export")],
        "short_answer": "Yes. EMAAVY supports SOC 2–aligned controls, role-based access, configurable data retention, automatic PII redaction options, and searchable audit trails for every material action on calls, agents, and admin settings.",
        "deep_dive": [
            (
                "Encryption and data residency",
                "All call audio and transcripts are encrypted in transit (TLS 1.2+) and at rest (AES-256). Enterprise plans can discuss data residency, dedicated infrastructure, and hybrid deployments for banks and platforms with hard locality requirements.",
            ),
            (
                "Retention and redaction",
                "Set retention windows per workspace — 7 days to unlimited on Enterprise. PII detection can flag or redact account numbers, government IDs, and custom regex patterns before transcripts land in CRM or data lakes.",
            ),
            (
                "Audit and compliance monitoring",
                "Every admin change, API key rotation, and export event is logged. Live calls can be flagged for forbidden phrases; supervisors receive alerts and can join or terminate per policy. Post-call compliance scores attach to QA dashboards.",
            ),
        ],
        "typical_questions": [
            "Can we get a SOC 2 report under NDA?",
            "How do we prove who listened to a recording?",
            "What happens when a compliance keyword is spoken?",
        ],
        "emaavy_handles": [
            "Compliance dashboard in Intelligence Matrix — flagged calls, PII events, policy status.",
            "Exportable audit logs in CSV/JSON for GRC tooling.",
            "Role-based access — agents, supervisors, admins, read-only auditors.",
            "Enterprise legal and security review package on request.",
        ],
        "related": ["enterprise-support", "crm-integrations", "voice-models"],
    },
    "pricing-scale": {
        "route": "faq-pricing-scale",
        "num": "04",
        "icon": "PR",
        "kicker": "Plans · Usage",
        "title": "How pricing scales with usage",
        "meta": "Flexible tiers",
        "snippet": "Volume-based plans; switch monthly or yearly anytime.",
        "hero_lead": "EMAAVY pricing scales by monthly call volume, automation depth (agents, campaigns, API), and support tier — with transparent plan caps and Enterprise custom deals for unlimited or dedicated infrastructure.",
        "stats": [("4", "Plan tiers"), ("20%", "Yearly save"), ("No", "Lock-in")],
        "short_answer": "Plans scale from 500 calls/month on Starter through 50K on Business, with Enterprise custom pricing for unlimited volume, dedicated infra, and white-glove onboarding. Switch monthly or yearly billing anytime without migration.",
        "deep_dive": [
            (
                "What drives your bill",
                "Primary meter: completed call minutes and monthly call count against plan tier. Secondary factors: number of AI agents, API/webhook volume, retention length, and premium models (custom voices, dedicated LLM routing). Overage policies are documented per plan.",
            ),
            (
                "Growing from Starter to Enterprise",
                "Starter is for proof-of-value — 500 calls, 5 languages, one seat. Pro adds sentiment, 5K calls, two agents. Business unlocks unlimited agents, campaigns, and API. Enterprise removes caps, adds VPC/SSO, custom SLAs, and named CSM/architect.",
            ),
            (
                "Billing flexibility",
                "Toggle monthly vs yearly on the pricing page for instant display of annual savings (~20%). Upgrades prorate; downgrades apply next cycle. No long-term lock-in — export your data if you leave.",
            ),
        ],
        "typical_questions": [
            "What counts as a billable call?",
            "Do failed or sub-10-second calls count?",
            "Can we get a committed-use discount?",
        ],
        "emaavy_handles": [
            "Full comparison table on the Pricing page — calls, agents, API, custom models.",
            "Usage dashboards in Intelligence Matrix — volume trends before you hit caps.",
            "Sales-led Enterprise quotes for committed volume and multi-workspace deals.",
            "FAQ and docs on webhook payloads for self-serve usage tracking.",
        ],
        "related": ["go-live", "enterprise-support", "crm-integrations"],
    },
    "crm-integrations": {
        "route": "faq-crm-integrations",
        "num": "05",
        "icon": "CR",
        "kicker": "Integrations · CRM",
        "title": "CRM and stack connectivity",
        "meta": "Native + API",
        "snippet": "Salesforce, HubSpot, Zoho, webhooks, and custom APIs.",
        "hero_lead": "Connect EMAAVY to Salesforce, HubSpot, Zoho, Slack, WhatsApp, calendars, and any system that accepts webhooks — with event-driven updates from live call intelligence, not end-of-day CSV imports.",
        "stats": [("6+", "Native tools"), ("REST", "API"), ("Real-time", "Events")],
        "short_answer": "Native connectors and webhooks push call outcomes, transcripts, sentiment, and intent scores into your CRM and ops tools the moment a call ends — or mid-call for high-priority triggers.",
        "deep_dive": [
            (
                "Native connectors",
                "Salesforce and HubSpot mappings update leads, log activities, create tasks, and advance deal stages based on intent thresholds. Cal.com and Google Calendar book meetings from live conversations. WhatsApp sends confirmations and links post-call.",
            ),
            (
                "Webhooks and custom APIs",
                "Subscribe to call.started, call.scored, call.ended, and custom keyword events. Payloads include transcript excerpts, scores, and campaign metadata. HMAC verification and retries make production integrations reliable.",
            ),
            (
                "Zoho and regional stacks",
                "Zoho CRM and regional tools connect via the same REST surface and partner recipes. Solutions engineering documents field mapping for APAC deployments where HubSpot penetration is lower.",
            ),
        ],
        "typical_questions": [
            "Can we write to custom CRM objects?",
            "Do you support bi-directional sync?",
            "How fast do webhooks fire after hang-up?",
        ],
        "emaavy_handles": [
            "Integrations hub — telephony, LLM, STT, TTS, and tools layers documented per provider.",
            "Sandbox webhooks for staging environments.",
            "Field mapping templates for Salesforce and HubSpot common objects.",
            "API reference for custom ERP or data warehouse pipelines.",
        ],
        "related": ["go-live", "compliance", "pricing-scale"],
    },
    "enterprise-support": {
        "route": "faq-enterprise-support",
        "num": "06",
        "icon": "EN",
        "kicker": "Enterprise · Success",
        "title": "Enterprise support",
        "meta": "Dedicated CSM",
        "snippet": "Named CSM, solutions architect, SLA 99.99%, rollout playbooks.",
        "hero_lead": "Enterprise customers receive a dedicated Customer Success Manager, solutions architect access, SLA-backed uptime, tailored rollout playbooks by region and team, and priority escalation paths — not a generic ticket queue.",
        "stats": [("99.99%", "SLA"), ("CSM", "Dedicated"), ("24/7", "Escalation")],
        "short_answer": "Enterprise includes a named CSM, solutions engineer for integration design, 99.99% uptime SLA, custom onboarding runbooks, and executive business reviews — plus optional on-prem or hybrid deployment models.",
        "deep_dive": [
            (
                "Onboarding and rollout",
                "Joint success plan covering telephony cutover, pilot cohorts, supervisor training, and compliance sign-off. Playbooks vary for BPO scale-ups vs single-brand enterprises vs platform partners embedding EMAAVY.",
            ),
            (
                "Ongoing partnership",
                "Quarterly business reviews with usage trends, conversion benchmarks, and roadmap previews. Priority feature requests and early access to beta models (e.g. new STT languages) where contracts allow.",
            ),
            (
                "Support and escalation",
                "24/7 escalation for production-impacting incidents. Named contacts bypass tier-1 triage. Status page and incident comms for Enterprise tenants with multi-region operations.",
            ),
        ],
        "typical_questions": [
            "Who answers if our CEO is on a live board demo?",
            "Do you offer professional services for custom flows?",
            "Can we get a dedicated Slack channel?",
        ],
        "emaavy_handles": [
            "Enterprise plan on Pricing — contact sales for tailored MSAs.",
            "VPC, SSO/SAML, and hybrid deployment options.",
            "Custom model and voice fine-tuning with ML ops review.",
            "Book a demo for scoping workshop with solutions architect.",
        ],
        "related": ["compliance", "pricing-scale", "voice-models"],
    },
}


def topic_card(slug, t):
    return f"""          <a href="pages/faq/{slug}.html" class="faq-topic-card" data-topic="{slug}">
            <span class="faq-topic-icon" aria-hidden="true">{t['icon']}</span>
            <span class="faq-topic-body">
              <span class="faq-topic-label">{t['num']} · {t['kicker']}</span>
              <strong>{t['title']}</strong>
              <span class="faq-topic-snippet">{t['snippet']}</span>
              <span class="faq-topic-explore">Read full answer →</span>
            </span>
          </a>"""


FAQ_SECTION = """<!-- FAQ HUB --> <section id="faq" class="cap-section faq-hub-section">
 <div class="features-head reveal">
  <span class="section-kicker">Support · Knowledge base</span>
  <h2>Questions teams ask before they scale</h2>
  <p class="int-hub-desc">Clear, in-depth answers — no jargon. Each topic opens on its own page with everything you need to evaluate, launch, and grow with EMAAVY.</p>
 </div>
 <div class="int-showcase reveal faq-promo-wrap" id="faq-emaavy">
  <div class="int-shell faq-promo-shell">
    <div class="faq-promo reveal">
      <div class="faq-promo-copy">
        <span class="section-kicker">Support · EMAAVY</span>
        <h3>Answers that match how you buy and build</h3>
        <p class="faq-promo-lead">From go-live timelines and custom voice models to compliance, pricing, CRM wiring, and Enterprise success — explore six guided topics written for operators, engineers, and leadership.</p>
        <ul class="faq-promo-highlights" aria-label="FAQ highlights">
          <li><strong>Six deep-dive topics</strong> — launch, AI voices, security, pricing, integrations, Enterprise support</li>
          <li><strong>Same-tab pages</strong> — full narratives without losing your place on the site</li>
          <li><strong>Brand-consistent design</strong> — slate blues, Clash Display, and EMAAVY UI patterns throughout</li>
          <li><strong>Still have questions?</strong> — book a demo or email hello@emaavy.ai from any topic page</li>
        </ul>
        <div class="faq-promo-actions">
          <a href="pages/faq.html" class="btn-faq-explore">Browse all topics</a>
          <a href="pages/contact.html" class="btn-faq-secondary">Contact support</a>
        </div>
      </div>
      <div class="faq-promo-panel">
        <div class="faq-promo-panel-head">Popular questions</div>
        <div class="faq-topic-grid">
{cards}
        </div>
      </div>
    </div>
    <div class="faq-promo-stats">
      <div class="int-stat"><span class="int-stat-dot" aria-hidden="true"></span><b>6</b><span>Topic guides</span></div>
      <div class="int-stat"><b>&lt;48h</b><span>Typical go-live</span></div>
      <div class="int-stat"><b>SOC 2</b><span>Aligned controls</span></div>
      <div class="int-stat"><b>99.99%</b><span>Enterprise SLA</span></div>
    </div>
  </div>
 </div>
</section>"""


def topic_page(slug, t):
    deep = "".join(
        f"""        <article class="capability-block faq-deep-block">
          <div class="capability-block-inner">
            <div class="capability-meta">
              <span class="capability-num">{i:02d}</span>
              <span class="capability-tag">Deep dive</span>
            </div>
            <div class="capability-content">
              <h2>{title}</h2>
              <p class="capability-lead">{body}</p>
            </div>
          </div>
        </article>"""
        for i, (title, body) in enumerate(t["deep_dive"], 1)
    )
    typical = "".join(f"<li>{q}</li>" for q in t["typical_questions"])
    handles = "".join(f"<li>{h}</li>" for h in t["emaavy_handles"])
    stats = "".join(f'<div class="stat-box"><b>{b}</b><span>{l}</span></div>' for b, l in t["stats"])
    related = "".join(
        f'<a href="{r}.html" class="int-layer-pill">{TOPICS[r]["title"]}</a>'
        for r in t["related"]
    )
    nav_all = "".join(f'<a href="{k}.html" class="int-layer-pill">{TOPICS[k]["title"]}</a>' for k in TOPICS)

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{t['title']} — FAQ — EMAAVY</title>
  <meta name="description" content="{t['hero_lead'][:155]}…" />
  <meta name="robots" content="index, follow" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=general-sans@300,400,500,600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../assets/nav.css" />
  <link rel="stylesheet" href="../../assets/site.css" />
</head>
<body data-base="../../" data-route="{t['route']}">
  <div id="site-nav-root"></div>
  <main class="page-main int-category-page">
    <section class="page-hero telephony-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="../../{HOME}">Home</a>
          <span aria-hidden="true"> / </span>
          <a href="../faq.html">FAQ</a>
          <span aria-hidden="true"> / </span>
          <span>{t['title']}</span>
        </nav>
        <span class="page-kicker">{t['kicker']}</span>
        <h1>{t['title']}</h1>
        <p class="telephony-hero-lead">{t['hero_lead']}</p>
        <div class="stat-row telephony-hero-stats">{stats}</div>
        <div class="capabilities-jump telephony-jump">
          <a href="#answer">Short answer</a>
          <a href="#deep-dive">Deep dive</a>
          <a href="#related">Related</a>
        </div>
      </div>
    </section>

    <section class="page-section">
      <div class="container">
        <div class="int-layer-nav">{nav_all}</div>
      </div>
    </section>

    <section id="answer" class="page-section alt">
      <div class="container">
        <article class="capability-block faq-answer-hero">
          <div class="capability-block-inner">
            <div class="capability-meta">
              <span class="capability-num">{t['num']}</span>
              <span class="capability-tag">Short answer</span>
            </div>
            <div class="capability-content">
              <h2>At a glance</h2>
              <p class="capability-lead">{t['short_answer']}</p>
            </div>
          </div>
        </article>
      </div>
    </section>

    <section id="deep-dive" class="page-section">
      <div class="container">
{deep}
      </div>
    </section>

    <section class="page-section alt">
      <div class="container">
        <div class="card-grid cols-2">
          <div class="glow-card">
            <h3>What teams typically ask</h3>
            <ul class="faq-list">{typical}</ul>
          </div>
          <div class="glow-card">
            <h3>How EMAAVY handles it</h3>
            <ul class="faq-list">{handles}</ul>
          </div>
        </div>
      </div>
    </section>

    <section id="related" class="page-section">
      <div class="container">
        <h2 class="section-title" style="margin-bottom:1rem">Related topics</h2>
        <div class="int-layer-nav">{related}</div>
        <div class="cta-row" style="margin-top:2rem">
          <a href="../faq.html" class="btn-outline">All FAQ topics</a>
          <a href="../../book-demo.html" class="btn-primary">Book a demo →</a>
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


def hub_page():
    cards = []
    for slug, t in TOPICS.items():
        cards.append(f"""          <a href="faq/{slug}.html" class="glow-card faq-hub-card">
            <div class="card-icon"><span class="brand-mark">{t['icon']}</span></div>
            <h3>{t['title']}</h3>
            <p>{t['snippet']}</p>
            <span class="card-tag">{t['meta']}</span>
            <span class="faq-topic-explore" style="display:block;margin-top:0.5rem">Read full answer →</span>
          </a>""")
    nav = "".join(f'<a href="faq/{k}.html" class="int-layer-pill">{TOPICS[k]["title"]}</a>' for k in TOPICS)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>FAQ — EMAAVY</title>
  <meta name="description" content="EMAAVY FAQ — go-live, voice models, compliance, pricing, CRM integrations, and Enterprise support." />
  <meta name="robots" content="index, follow" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=general-sans@300,400,500,600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../assets/nav.css" />
  <link rel="stylesheet" href="../assets/site.css" />
</head>
<body data-base="../" data-route="faq">
  <div id="site-nav-root"></div>
  <main class="page-main">
    <section class="page-hero telephony-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="../{HOME}">Home</a>
          <span aria-hidden="true"> / </span>
          <span>FAQ</span>
        </nav>
        <span class="page-kicker">Support · Knowledge base</span>
        <h1>Questions teams ask before they scale</h1>
        <p class="telephony-hero-lead">Six guided topics — each with a full page of context, not a one-line accordion.</p>
        <div class="stat-row telephony-hero-stats">
          <div class="stat-box"><b>6</b><span>Topics</span></div>
          <div class="stat-box"><b>&lt;48h</b><span>Go-live</span></div>
          <div class="stat-box"><b>SOC 2</b><span>Aligned</span></div>
        </div>
      </div>
    </section>
    <section class="page-section">
      <div class="container">
        <div class="int-layer-nav">{nav}</div>
        <div class="card-grid cols-2" style="margin-top:1.5rem">
{chr(10).join(cards)}
        </div>
        <div class="cta-row" style="margin-top:2rem">
          <a href="contact.html" class="btn-outline">Contact support</a>
          <a href="../book-demo.html" class="btn-primary">Book a demo →</a>
        </div>
      </div>
    </section>
  </main>
  <div id="site-footer-root"></div>
  <script src="../assets/routes.js"></script>
  <script src="../assets/components.js"></script>
  <script src="../assets/nav.js"></script>
</body>
</html>
"""


def patch_routes():
    text = ROUTES.read_text(encoding="utf-8")
    if "faqTopics:" not in text:
        block = """  faqTopics: [
    { id: 'go-live', label: 'Go live', path: 'pages/faq/go-live.html' },
    { id: 'voice-models', label: 'Voice models', path: 'pages/faq/voice-models.html' },
    { id: 'compliance', label: 'Compliance', path: 'pages/faq/compliance.html' },
    { id: 'pricing-scale', label: 'Pricing & usage', path: 'pages/faq/pricing-scale.html' },
    { id: 'crm-integrations', label: 'CRM integrations', path: 'pages/faq/crm-integrations.html' },
    { id: 'enterprise-support', label: 'Enterprise support', path: 'pages/faq/enterprise-support.html' },
  ],

"""
        text = text.replace("  agents: [", block + "  agents: [")
    if "pages/faq/" not in text:
        text = text.replace(
            "    if (path.startsWith('pages/case-studies/')) {",
            "    if (path.startsWith('pages/faq/')) {\n"
            "      const slug = path.replace('pages/faq/', '').replace('.html', '');\n"
            "      return '#/faq/' + slug;\n"
            "    }\n"
            "    if (path.startsWith('pages/case-studies/')) {",
        )
    if "faq-" not in text:
        text = text.replace(
            "    if (routeId.startsWith('case-study-')) return '#/case-studies/' + routeId.replace('case-study-', '');",
            "    if (routeId.startsWith('faq-')) return '#/faq/' + routeId.replace('faq-', '');\n"
            "    if (routeId.startsWith('case-study-')) return '#/case-studies/' + routeId.replace('case-study-', '');",
        )
    ROUTES.write_text(text, encoding="utf-8")


def remove_faq_accordion_js(text):
    block = re.compile(
        r"/\* FAQ accordion \*/ document\.querySelectorAll\('\.faq-item'\)\.forEach\(\(item\) => \{.*?\}\); \}\); ",
        re.DOTALL,
    )
    return block.sub("", text)


def main():
    FAQ_DIR.mkdir(parents=True, exist_ok=True)
    cards = "\n".join(topic_card(k, t) for k, t in TOPICS.items())
    section = FAQ_SECTION.format(cards=cards)

    text = HTML.read_text(encoding="utf-8")
    if "/* ═══ FAQ — unified landing promo ═══ */" not in text:
        marker = "/* ═══ CALL LIFECYCLE"
        if marker not in text:
            marker = "/* ═══ INTELLIGENCE MATRIX"
        idx = text.index(marker)
        insert_at = text.rfind("}", 0, idx) + 1
        text = text[:insert_at] + FAQ_CSS + text[insert_at:]

    pattern = re.compile(r"<!-- FAQ -->.*?</section>\s*<!-- CTA -->", re.DOTALL)
    if not pattern.search(text):
        pattern = re.compile(r"<!-- FAQ HUB -->.*?</section>\s*<!-- CTA -->", re.DOTALL)
    if not pattern.search(text):
        raise SystemExit("FAQ section not found")
    text = pattern.sub(section + "\n <!-- CTA -->", text, count=1)
    text = remove_faq_accordion_js(text)
    HTML.write_text(text, encoding="utf-8")

    for slug, data in TOPICS.items():
        (FAQ_DIR / f"{slug}.html").write_text(topic_page(slug, data), encoding="utf-8")
    HUB.write_text(hub_page(), encoding="utf-8")
    patch_routes()

    # FAQ list styles on subpages
    site = ROOT / "assets" / "site.css"
    extra = """
.faq-list {
  margin: 0.75rem 0 0;
  padding-left: 1.15rem;
  color: #475569;
  font-size: 0.92rem;
  line-height: 1.65;
}
.faq-list li { margin-bottom: 0.45rem; }
.faq-hub-card:hover { border-color: #4A658B !important; }
.faq-answer-hero .capability-lead { font-size: 1.05rem !important; }
"""
    sc = site.read_text(encoding="utf-8")
    if ".faq-list" not in sc:
        site.write_text(sc + extra, encoding="utf-8")

    print("OK: FAQ promo, hub, and", len(TOPICS), "topic pages")


if __name__ == "__main__":
    main()
