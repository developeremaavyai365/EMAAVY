#!/usr/bin/env python3
"""Inject premium HIW showcase panel into index.html."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

SLIDES_HTML = r'''              <article class="hiw-sc-slide" data-slide="connect" role="tabpanel" aria-hidden="true">
                <span class="hiw-sc-slide-kicker">01 — Connect</span>
                <h3 class="hiw-sc-slide-headline">Enterprise Telephony, Connected in Seconds</h3>
                <p class="hiw-sc-slide-desc">Plug Vobiz or your existing carrier into EMAAVY and every call becomes a structured data stream from the first ring. Inbound, outbound, and campaign traffic routes through one orchestration layer — recorded, monitored, and ready for AI agents or human handoff.</p>
                <p class="hiw-sc-slide-detail">No separate PBX tooling or manual call logging. EMAAVY normalizes SIP, PSTN, and programmatic dials so sales, support, and operations teams work from a single live call fabric.</p>
                <div class="hiw-sc-slide-visual">
                  <div class="hiw-vis-route">
                    <div class="hiw-vis-route-row">
                      <span class="hiw-vis-route-node">Inbound</span>
                      <span class="hiw-vis-route-node hiw-vis-route-node--hub">Emaavy</span>
                      <span class="hiw-vis-route-node">AI Agent</span>
                    </div>
                    <div class="hiw-vis-route-row">
                      <span class="hiw-vis-route-node">Outbound</span>
                      <span class="hiw-vis-route-node">Campaign</span>
                      <span class="hiw-vis-route-node">Human</span>
                    </div>
                  </div>
                </div>
                <ul class="hiw-sc-slide-points">
                  <li>Carrier and Vobiz integration with enterprise-grade routing rules</li>
                  <li>Live call state synced to agents, campaigns, and dashboards</li>
                  <li>Seamless escalation from AI voice to human representatives</li>
                </ul>
                <div class="hiw-sc-slide-outcomes">
                  <span class="hiw-sc-slide-outcome">Sub-second routing</span>
                  <span class="hiw-sc-slide-outcome">Global scale</span>
                  <span class="hiw-sc-slide-outcome">Live monitoring</span>
                  <span class="hiw-sc-slide-outcome">Zero dropped handoffs</span>
                </div>
                <div class="hiw-sc-slide-usecases">
                  <span class="hiw-sc-slide-usecases-label">Common applications</span>
                  <ul class="hiw-sc-slide-usecase-list">
                    <li>Inbound support lines</li>
                    <li>Outbound sales campaigns</li>
                    <li>Appointment scheduling</li>
                    <li>High-volume call centers</li>
                  </ul>
                </div>
              </article>
              <article class="hiw-sc-slide" data-slide="transcribe" role="tabpanel" aria-hidden="true">
                <span class="hiw-sc-slide-kicker">02 — Transcribe</span>
                <h3 class="hiw-sc-slide-headline">Real-Time Speech-to-Text at Enterprise Speed</h3>
                <p class="hiw-sc-slide-desc">Every spoken word is converted to structured text in under 500ms using your choice of nine STT providers. EMAAVY supports 22 Indian languages and code-switching — so transcripts stay accurate whether your customers speak English, Hindi, Tamil, or regional dialects.</p>
                <p class="hiw-sc-slide-detail">Transcripts stream live into agents, analytics, and compliance workflows. Switch STT vendors per campaign or language without rebuilding your voice stack.</p>
                <div class="hiw-sc-slide-visual">
                  <div class="hiw-vis-wave" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i></div>
                  <div class="hiw-vis-langs">
                    <span class="hiw-vis-lang">EN</span><span class="hiw-vis-lang">HI</span><span class="hiw-vis-lang">TA</span><span class="hiw-vis-lang">TE</span><span class="hiw-vis-lang">MR</span><span class="hiw-vis-lang">+17</span>
                  </div>
                </div>
                <ul class="hiw-sc-slide-points">
                  <li>Word-level timestamps and speaker attribution on live calls</li>
                  <li>Per-call STT routing — Deepgram, Sarvam, and more</li>
                  <li>Searchable transcript history tied to CRM records</li>
                </ul>
                <div class="hiw-sc-slide-outcomes">
                  <span class="hiw-sc-slide-outcome">&lt;500ms latency</span>
                  <span class="hiw-sc-slide-outcome">22 languages</span>
                  <span class="hiw-sc-slide-outcome">9 STT providers</span>
                  <span class="hiw-sc-slide-outcome">Live streaming text</span>
                </div>
                <div class="hiw-sc-slide-usecases">
                  <span class="hiw-sc-slide-usecases-label">Common applications</span>
                  <ul class="hiw-sc-slide-usecase-list">
                    <li>Multilingual customer support</li>
                    <li>Compliance recording</li>
                    <li>Agent assist &amp; coaching</li>
                    <li>Conversation analytics</li>
                  </ul>
                </div>
              </article>
              <article class="hiw-sc-slide" data-slide="reason" role="tabpanel" aria-hidden="true">
                <span class="hiw-sc-slide-kicker">03 — Reason</span>
                <h3 class="hiw-sc-slide-headline">LLM Intelligence on Every Live Conversation</h3>
                <p class="hiw-sc-slide-desc">Your chosen large language model — GPT, Claude, Gemini, Qwen, or Grok — analyzes each conversation as it happens. EMAAVY extracts intent, sentiment, entities, and risk signals so teams respond with context instead of scripts.</p>
                <p class="hiw-sc-slide-detail">Reasoning runs on live transcript streams and historical customer data. Swap LLM providers per workflow while keeping prompts, guardrails, and audit logs centralized in one platform.</p>
                <div class="hiw-sc-slide-visual">
                  <div class="hiw-vis-reason">
                    <span class="hiw-vis-reason-step is-live">Intent</span>
                    <span class="hiw-vis-reason-step">Sentiment</span>
                    <span class="hiw-vis-reason-step">Risk</span>
                    <span class="hiw-vis-reason-step">Entities</span>
                  </div>
                </div>
                <ul class="hiw-sc-slide-points">
                  <li>Real-time classification of sales, support, and escalation intents</li>
                  <li>Sentiment trends surfaced before a call turns negative</li>
                  <li>Policy and compliance risk flags with explainable outputs</li>
                </ul>
                <div class="hiw-sc-slide-outcomes">
                  <span class="hiw-sc-slide-outcome">Intent detection</span>
                  <span class="hiw-sc-slide-outcome">Sentiment scoring</span>
                  <span class="hiw-sc-slide-outcome">Risk flags</span>
                  <span class="hiw-sc-slide-outcome">Smarter routing</span>
                </div>
                <div class="hiw-sc-slide-usecases">
                  <span class="hiw-sc-slide-usecases-label">Common applications</span>
                  <ul class="hiw-sc-slide-usecase-list">
                    <li>Lead qualification</li>
                    <li>Churn prevention</li>
                    <li>Quality assurance</li>
                    <li>Executive insight dashboards</li>
                  </ul>
                </div>
              </article>
              <article class="hiw-sc-slide" data-slide="act" role="tabpanel" aria-hidden="true">
                <span class="hiw-sc-slide-kicker">04 — Act</span>
                <h3 class="hiw-sc-slide-headline">Automations That Fire Without Handoffs</h3>
                <p class="hiw-sc-slide-desc">The moment a conversation ends — or a key phrase is detected — EMAAVY triggers the next business action automatically. CRM fields update, WhatsApp messages send, calendars book, and managers get notified without anyone copying notes or switching tabs.</p>
                <p class="hiw-sc-slide-detail">Every automation is auditable and configurable per team. Build escalation paths, follow-up sequences, and data enrichment flows that run 24/7 with the same reliability as your telephony layer.</p>
                <div class="hiw-sc-slide-visual">
                  <div class="hiw-vis-chain">
                    <span class="hiw-vis-chain-block is-firing">Update CRM</span>
                    <span>→</span>
                    <span class="hiw-vis-chain-block">Send WhatsApp</span>
                    <span>→</span>
                    <span class="hiw-vis-chain-block">Book meeting</span>
                    <span>→</span>
                    <span class="hiw-vis-chain-block">Notify team</span>
                  </div>
                </div>
                <ul class="hiw-sc-slide-points">
                  <li>Post-call CRM sync with deals, contacts, and custom fields</li>
                  <li>Cross-channel follow-ups on WhatsApp, email, or voice</li>
                  <li>Human-in-the-loop rules for high-value or sensitive actions</li>
                </ul>
                <div class="hiw-sc-slide-outcomes">
                  <span class="hiw-sc-slide-outcome">CRM sync</span>
                  <span class="hiw-sc-slide-outcome">Channel triggers</span>
                  <span class="hiw-sc-slide-outcome">Zero manual steps</span>
                  <span class="hiw-sc-slide-outcome">Audit-ready ops</span>
                </div>
                <div class="hiw-sc-slide-usecases">
                  <span class="hiw-sc-slide-usecases-label">Common applications</span>
                  <ul class="hiw-sc-slide-usecase-list">
                    <li>Sales follow-up sequences</li>
                    <li>Support ticket creation</li>
                    <li>Demo scheduling</li>
                    <li>Manager escalations</li>
                  </ul>
                </div>
              </article>'''

SHOWCASE_HTML = '''    <div class="hiw-showcase-col">
      <div class="hiw-showcase" id="hiwShowcase" tabindex="0" aria-label="EMAAVY method — live pipeline preview" aria-live="polite">
        <div class="hiw-sc-stage">
          <div class="hiw-sc-pipeline">
            <div class="hiw-sc-ambient" aria-hidden="true"></div>
            <div class="hiw-sc-grid" aria-hidden="true"></div>
            <svg class="hiw-sc-paths" viewBox="0 0 600 600" aria-hidden="true">
              <defs>
                <linearGradient id="hiw-sc-path-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
                  <stop offset="0%" stop-color="#18345d" stop-opacity="0.35"/>
                  <stop offset="50%" stop-color="#4a658b" stop-opacity="0.65"/>
                  <stop offset="100%" stop-color="#5a7d9e" stop-opacity="0.4"/>
                </linearGradient>
              </defs>
              <path class="hiw-sc-path-soft" data-hiw-link="connect" d="M300 300 Q220 260 108 168"/>
              <path class="hiw-sc-path" data-hiw-link="connect" d="M300 300 Q220 260 108 168"/>
              <path class="hiw-sc-path-flow" data-hiw-link="connect" d="M300 300 Q220 260 108 168"/>
              <path class="hiw-sc-path-soft" data-hiw-link="transcribe" d="M300 300 Q380 260 492 168"/>
              <path class="hiw-sc-path" data-hiw-link="transcribe" d="M300 300 Q380 260 492 168"/>
              <path class="hiw-sc-path-flow hiw-sc-path-flow--b" data-hiw-link="transcribe" d="M300 300 Q380 260 492 168"/>
              <path class="hiw-sc-path-soft" data-hiw-link="reason" d="M300 300 Q220 340 108 432"/>
              <path class="hiw-sc-path" data-hiw-link="reason" d="M300 300 Q220 340 108 432"/>
              <path class="hiw-sc-path-flow hiw-sc-path-flow--c" data-hiw-link="reason" d="M300 300 Q220 340 108 432"/>
              <path class="hiw-sc-path-soft" data-hiw-link="act" d="M300 300 Q380 340 492 432"/>
              <path class="hiw-sc-path" data-hiw-link="act" d="M300 300 Q380 340 492 432"/>
              <path class="hiw-sc-path-flow" data-hiw-link="act" d="M300 300 Q380 340 492 432"/>
            </svg>
            <div class="hiw-sc-core" aria-hidden="true">
              <div class="hiw-sc-core-body">
                <span class="hiw-sc-core-label">Emaavy</span>
                <span class="hiw-sc-core-sub">Pipeline</span>
              </div>
            </div>
            <div class="hiw-sc-nodes">
              <article class="hiw-sc-node hiw-sc-node--connect is-active" data-step="connect">
                <div class="hiw-sc-node-card">
                  <span class="hiw-sc-node-num">01</span>
                  <span class="hiw-sc-node-title">Connect</span>
                  <p class="hiw-sc-node-desc">Telephony live</p>
                </div>
              </article>
              <article class="hiw-sc-node hiw-sc-node--transcribe" data-step="transcribe">
                <div class="hiw-sc-node-card">
                  <span class="hiw-sc-node-num">02</span>
                  <span class="hiw-sc-node-title">Transcribe</span>
                  <p class="hiw-sc-node-desc">Real-time STT</p>
                </div>
              </article>
              <article class="hiw-sc-node hiw-sc-node--reason" data-step="reason">
                <div class="hiw-sc-node-card">
                  <span class="hiw-sc-node-num">03</span>
                  <span class="hiw-sc-node-title">Reason</span>
                  <p class="hiw-sc-node-desc">LLM analysis</p>
                </div>
              </article>
              <article class="hiw-sc-node hiw-sc-node--act" data-step="act">
                <div class="hiw-sc-node-card">
                  <span class="hiw-sc-node-num">04</span>
                  <span class="hiw-sc-node-title">Act</span>
                  <p class="hiw-sc-node-desc">Auto triggers</p>
                </div>
              </article>
            </div>
            <div class="hiw-sc-status">
              <span class="hiw-sc-status-live"><span class="hiw-sc-status-dot" aria-hidden="true"></span><span data-hiw-status-label>Telephony connect</span></span>
              <span class="hiw-sc-status-metric" data-hiw-metric><strong>1</strong> / 4 steps</span>
            </div>
          </div>
          <div class="hiw-sc-presentation" aria-label="Step detail presentation" aria-hidden="true">
            <div class="hiw-sc-toolbar">
              <button type="button" class="hiw-sc-back" aria-label="Return to pipeline view">← Pipeline</button>
              <span class="hiw-sc-progress" data-hiw-pres-progress><strong>1</strong> / 4</span>
              <div class="hiw-sc-nav-group">
                <button type="button" class="hiw-sc-nav hiw-sc-nav--prev" aria-label="Previous step">←</button>
                <button type="button" class="hiw-sc-nav hiw-sc-nav--next" aria-label="Next step">→</button>
              </div>
            </div>
            <div class="hiw-sc-slides-viewport">
__SLIDES__
            </div>
          </div>
        </div>
      </div>
    </div>'''.replace("__SLIDES__", SLIDES_HTML.strip())

FLOW_CARD_COPY = {
    "hiw-connect": "Plug Vobiz or your carrier into EMAAVY — inbound, outbound, and campaign calls route through one live telephony layer from the first ring.",
    "hiw-transcribe": "Live speech-to-text across nine STT providers and 22 Indian languages — structured transcripts stream in under 500ms for agents and analytics.",
    "hiw-reason": "Your chosen LLM analyzes intent, sentiment, entities, and risk on every live conversation — so teams respond with context, not scripts.",
    "hiw-act": "Post-call automations fire instantly — CRM updates, WhatsApp follow-ups, calendar bookings, and team alerts without manual handoffs.",
}

SLIDES_VIEWPORT_RE = re.compile(
    r'(<div class="hiw-sc-slides-viewport">)\s*(?:<article class="hiw-sc-slide".*?</article>\s*)+(</div>)',
    re.DOTALL,
)

OLD_INLINE_USECASE = """  body[data-page=\"home\"] #how-it-works .hiw-sc-slide-usecase-list li::before,
  body[data-page=\"home\"] #how-it-works .hiw-vis-chain-block::before {
    display: none !important;
  }"""

NEW_INLINE_USECASE = """  body[data-page=\"home\"] #how-it-works .hiw-sc-slide-usecase-list li::before,
  body[data-page=\"home\"] #how-it-works .hiw-sc-slide-points li::before {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
    content: \"\" !important;
  }
  body[data-page=\"home\"] #how-it-works .hiw-vis-chain-block::before {
    display: none !important;
  }
  body[data-page=\"home\"] #how-it-works .hiw-sc-stage.is-presenting {
    min-height: 480px !important;
  }"""

ASSETS_CSS = '  <link rel="stylesheet" href="assets/hiw-showcase.css" />\n'
ASSETS_JS = '<script src="assets/hiw-showcase.js" defer></script>\n'

INLINE_STYLE = '''
  /* HIW premium showcase */
  body[data-page="home"] #how-it-works .hiw-showcase {
    padding: 4px !important;
    border-radius: 24px !important;
    background: linear-gradient(145deg, #4a658b 0%, #18345d 42%, #5a7d9e 100%) !important;
    box-shadow:
      0 0 0 1px rgba(74, 101, 139, 0.45),
      0 22px 52px -14px rgba(24, 52, 93, 0.32),
      0 0 40px -10px rgba(74, 101, 139, 0.28) !important;
  }
  body[data-page="home"] #how-it-works .hiw-sc-stage:not(.is-presenting) .hiw-sc-pipeline {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
  }
  body[data-page="home"] #how-it-works .hiw-sc-stage.is-presenting .hiw-sc-pipeline,
  body[data-page="home"] #how-it-works .hiw-sc-stage.is-presenting .hiw-sc-ambient,
  body[data-page="home"] #how-it-works .hiw-sc-stage.is-presenting .hiw-sc-grid,
  body[data-page="home"] #how-it-works .hiw-sc-stage.is-presenting .hiw-sc-paths,
  body[data-page="home"] #how-it-works .hiw-sc-stage.is-presenting .hiw-sc-nodes,
  body[data-page="home"] #how-it-works .hiw-sc-stage.is-presenting .hiw-sc-core {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
  }
  body[data-page="home"] #how-it-works .hiw-sc-presentation {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
  }
  body[data-page="home"] #how-it-works .hiw-sc-stage.is-presenting .hiw-sc-presentation {
    display: flex !important;
    flex-direction: column !important;
    visibility: visible !important;
    opacity: 1 !important;
    pointer-events: auto !important;
    z-index: 20 !important;
    background: linear-gradient(165deg, #f8fafc 0%, #f1f5f9 48%, #eef2f7 100%) !important;
  }
  body[data-page="home"] #how-it-works .hiw-sc-stage.is-presenting .hiw-sc-slide.is-active {
    display: flex !important;
    flex-direction: column !important;
  }
  body[data-page="home"] #how-it-works .hiw-sc-stage.is-presenting .hiw-sc-slide:not(.is-active) {
    display: none !important;
  }
  body[data-page="home"] #how-it-works .hiw-sc-slide-usecase-list li::before,
  body[data-page="home"] #how-it-works .hiw-sc-slide-points li::before {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
    content: "" !important;
  }
  body[data-page="home"] #how-it-works .hiw-vis-chain-block::before {
    display: none !important;
  }
  body[data-page="home"] #how-it-works .hiw-sc-stage.is-presenting {
    min-height: 480px !important;
  }
'''


def replace_slides(text: str) -> tuple[str, int]:
    def repl(m: re.Match) -> str:
        return m.group(1) + "\n" + SLIDES_HTML + "\n            " + m.group(2)

    return SLIDES_VIEWPORT_RE.subn(repl, text, count=1)


def update_flow_cards(text: str) -> str:
    for detail, copy in FLOW_CARD_COPY.items():
        text = re.sub(
            rf'(<li class="hiw-flow-card[^"]*" data-detail="{detail}"[^>]*>.*?<p>)(.*?)(</p>)',
            rf"\1{copy}\3",
            text,
            count=1,
            flags=re.DOTALL,
        )
    return text


def main():
    text = INDEX.read_text(encoding="utf-8")

    if "id=\"hiwShowcase\"" in text:
        print("HIW showcase already present")
    else:
        marker = "    </div>\n  </div>\n</section> <!-- INTEGRATIONS HUB -->"
        if marker not in text:
            marker = "    </div>\n  </div>\n</section>"
            # fallback: insert before closing hiw-split
            text = text.replace(
                "      </ol>\n    </div>\n  </div>\n</section>",
                "      </ol>\n    </div>\n" + SHOWCASE_HTML + "\n  </div>\n</section>",
                1,
            )
        else:
            text = text.replace(
                "      </ol>\n    </div>\n  </div>\n</section> <!-- INTEGRATIONS HUB -->",
                "      </ol>\n    </div>\n" + SHOWCASE_HTML + "\n  </div>\n</section> <!-- INTEGRATIONS HUB -->",
                1,
            )
        print("Injected HIW showcase HTML")

    if "assets/hiw-showcase.css" not in text:
        text = text.replace(
            '  <link rel="stylesheet" href="assets/hero-command-center-slides.css" />',
            '  <link rel="stylesheet" href="assets/hero-command-center-slides.css" />\n' + ASSETS_CSS.strip(),
            1,
        )
        print("Added hiw-showcase.css link")

    if "assets/hiw-showcase.js" not in text:
        text = text.replace(
            '<script src="assets/hero-command-center.js" defer></script>',
            '<script src="assets/hero-command-center.js" defer></script>\n' + ASSETS_JS.strip(),
            1,
        )
        print("Added hiw-showcase.js script")

    if "HIW premium showcase" not in text:
        text = text.replace(
            "  </style>\n</head>",
            INLINE_STYLE + "  </style>\n</head>",
            1,
        )
        print("Added HIW inline overrides")
    elif OLD_INLINE_USECASE in text:
        text = text.replace(OLD_INLINE_USECASE, NEW_INLINE_USECASE)
        print("Updated HIW inline pseudo-element overrides")

    text, n = replace_slides(text)
    if n:
        print("Updated HIW slide content")

    text = update_flow_cards(text)
    print("Updated HIW flow card copy")

    INDEX.write_text(text, encoding="utf-8")
    print("Done:", INDEX)


if __name__ == "__main__":
    main()
