#!/usr/bin/env python3
"""Replace integration hub cards with premium int-showcase panel in index.html."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "index.html"

LAYER_CARDS = r'''    <div class="int-split reveal">
      <div class="int-layers-col" aria-label="Integration layers">
        <ol class="int-layer-steps">
          <li class="int-layer-card int-layer-card--a reveal" data-detail="int-telephony" tabindex="0">
            <span class="int-layer-card-kicker">Layer 01</span>
            <span class="int-layer-card-num" aria-hidden="true">1</span>
            <h3>Telephony</h3>
            <p>Connect Vobiz, Twilio, and global carriers — every inbound and outbound call streams into EMAAVY from the first ring with live routing and monitoring.</p>
          </li>
          <li class="int-layer-card int-layer-card--b reveal" data-detail="int-llms" tabindex="0">
            <span class="int-layer-card-kicker">Layer 02</span>
            <span class="int-layer-card-num" aria-hidden="true">2</span>
            <h3>LLMs</h3>
            <p>Route each conversation to GPT, Claude, Gemini, Qwen, or Grok — swap models per agent, intent, or campaign without rebuilding your voice stack.</p>
          </li>
          <li class="int-layer-card int-layer-card--c reveal" data-detail="int-stt" tabindex="0">
            <span class="int-layer-card-kicker">Layer 03</span>
            <span class="int-layer-card-num" aria-hidden="true">3</span>
            <h3>Speech-to-text</h3>
            <p>Nine STT engines, 22 Indian languages, and sub-500ms streaming transcripts — pick Deepgram, Sarvam, or Gladia per language and campaign.</p>
          </li>
          <li class="int-layer-card int-layer-card--d reveal" data-detail="int-tts" tabindex="0">
            <span class="int-layer-card-kicker">Layer 04</span>
            <span class="int-layer-card-num" aria-hidden="true">4</span>
            <h3>Text-to-speech</h3>
            <p>Natural voice output through ElevenLabs and Flash Bulbul — enterprise-grade synthesis with Hinglish support for Indian customer programs.</p>
          </li>
          <li class="int-layer-card int-layer-card--e reveal" data-detail="int-tools" tabindex="0">
            <span class="int-layer-card-kicker">Layer 05</span>
            <span class="int-layer-card-num" aria-hidden="true">5</span>
            <h3>Tools &amp; CRM</h3>
            <p>Salesforce, HubSpot, WhatsApp, Slack, calendars, and webhooks — post-call automations and live sync without manual data entry.</p>
          </li>
        </ol>
      </div>
      <div class="int-showcase-col">
        <div class="int-showcase" id="intShowcase" tabindex="0" aria-label="EMAAVY integration stack — live hub preview" aria-live="polite">
          <div class="int-sc-stage">
            <div class="int-sc-pipeline">
              <div class="int-sc-ambient" aria-hidden="true"></div>
              <div class="int-sc-grid" aria-hidden="true"></div>
              <svg class="int-sc-paths" viewBox="0 0 600 600" aria-hidden="true">
                <defs>
                  <linearGradient id="int-sc-path-gradient" x1="0%" y1="0%" x2="100%" y2="100%">
                    <stop offset="0%" stop-color="#18345d" stop-opacity="0.35"/>
                    <stop offset="50%" stop-color="#4a658b" stop-opacity="0.65"/>
                    <stop offset="100%" stop-color="#5a7d9e" stop-opacity="0.4"/>
                  </linearGradient>
                </defs>
                <path class="int-sc-path-soft" data-int-link="telephony" d="M300 300 Q300 215 300 108"/>
                <path class="int-sc-path" data-int-link="telephony" d="M300 300 Q300 215 300 108"/>
                <path class="int-sc-path-flow" data-int-link="telephony" d="M300 300 Q300 215 300 108"/>
                <path class="int-sc-path-soft" data-int-link="llms" d="M300 300 Q380 260 492 168"/>
                <path class="int-sc-path" data-int-link="llms" d="M300 300 Q380 260 492 168"/>
                <path class="int-sc-path-flow int-sc-path-flow--b" data-int-link="llms" d="M300 300 Q380 260 492 168"/>
                <path class="int-sc-path-soft" data-int-link="stt" d="M300 300 Q380 340 492 432"/>
                <path class="int-sc-path" data-int-link="stt" d="M300 300 Q380 340 492 432"/>
                <path class="int-sc-path-flow int-sc-path-flow--c" data-int-link="stt" d="M300 300 Q380 340 492 432"/>
                <path class="int-sc-path-soft" data-int-link="tts" d="M300 300 Q220 340 108 432"/>
                <path class="int-sc-path" data-int-link="tts" d="M300 300 Q220 340 108 432"/>
                <path class="int-sc-path-flow int-sc-path-flow--d" data-int-link="tts" d="M300 300 Q220 340 108 432"/>
                <path class="int-sc-path-soft" data-int-link="tools" d="M300 300 Q220 260 108 168"/>
                <path class="int-sc-path" data-int-link="tools" d="M300 300 Q220 260 108 168"/>
                <path class="int-sc-path-flow int-sc-path-flow--e" data-int-link="tools" d="M300 300 Q220 260 108 168"/>
              </svg>
              <div class="int-sc-core" aria-hidden="true">
                <div class="int-sc-core-body">
                  <span class="int-sc-core-label">Emaavy</span>
                  <span class="int-sc-core-sub">Stack</span>
                </div>
              </div>
              <div class="int-sc-nodes">
                <article class="int-sc-node int-sc-node--telephony is-active" data-step="telephony">
                  <div class="int-sc-node-card">
                    <span class="int-sc-node-num">01</span>
                    <span class="int-sc-node-title">Telephony</span>
                    <p class="int-sc-node-desc">Voice layer</p>
                  </div>
                </article>
                <article class="int-sc-node int-sc-node--llms" data-step="llms">
                  <div class="int-sc-node-card">
                    <span class="int-sc-node-num">02</span>
                    <span class="int-sc-node-title">LLMs</span>
                    <p class="int-sc-node-desc">Reasoning</p>
                  </div>
                </article>
                <article class="int-sc-node int-sc-node--stt" data-step="stt">
                  <div class="int-sc-node-card">
                    <span class="int-sc-node-num">03</span>
                    <span class="int-sc-node-title">STT</span>
                    <p class="int-sc-node-desc">Live text</p>
                  </div>
                </article>
                <article class="int-sc-node int-sc-node--tts" data-step="tts">
                  <div class="int-sc-node-card">
                    <span class="int-sc-node-num">04</span>
                    <span class="int-sc-node-title">TTS</span>
                    <p class="int-sc-node-desc">Voice out</p>
                  </div>
                </article>
                <article class="int-sc-node int-sc-node--tools" data-step="tools">
                  <div class="int-sc-node-card">
                    <span class="int-sc-node-num">05</span>
                    <span class="int-sc-node-title">Tools</span>
                    <p class="int-sc-node-desc">CRM sync</p>
                  </div>
                </article>
              </div>
              <div class="int-sc-status">
                <span class="int-sc-status-live"><span class="int-sc-status-dot" aria-hidden="true"></span><span data-int-status-label>Voice connectivity</span></span>
                <span class="int-sc-status-metric" data-int-metric><strong>1</strong> / 5 layers</span>
              </div>
            </div>
            <div class="int-sc-presentation" aria-label="Integration layer detail" aria-hidden="true">
              <div class="int-sc-toolbar">
                <button type="button" class="int-sc-back" aria-label="Return to stack view">← Stack</button>
                <span class="int-sc-progress" data-int-pres-progress><strong>1</strong> / 5</span>
                <div class="int-sc-nav-group">
                  <button type="button" class="int-sc-nav int-sc-nav--prev" aria-label="Previous layer">←</button>
                  <button type="button" class="int-sc-nav int-sc-nav--next" aria-label="Next layer">→</button>
                </div>
              </div>
              <div class="int-sc-slides-viewport">
__SLIDES__
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>'''

SLIDES_HTML = r'''              <article class="int-sc-slide" data-slide="telephony" role="tabpanel" aria-hidden="true">
                <span class="int-sc-slide-kicker">01 — Telephony</span>
                <h3 class="int-sc-slide-headline">Enterprise Voice Connectivity for Every Call</h3>
                <p class="int-sc-slide-desc">The telephony layer is where every EMAAVY program begins. Connect Vobiz, Twilio, Plivo, Vonage, and regional carriers so inbound, outbound, and campaign traffic routes through one orchestration fabric — recorded, monitored, and ready for AI agents from the first ring.</p>
                <p class="int-sc-slide-detail">No separate PBX consoles or manual trunk management. EMAAVY normalizes SIP, PSTN, and programmatic dials, provisions global DIDs, and streams live call events into your CRM and analytics stack automatically.</p>
                <div class="int-sc-slide-visual">
                  <div class="int-vis-route">
                    <div class="int-vis-route-row">
                      <span class="int-vis-route-node">Inbound</span>
                      <span class="int-vis-route-node int-vis-route-node--hub">Emaavy</span>
                      <span class="int-vis-route-node">AI Agent</span>
                    </div>
                    <div class="int-vis-route-row">
                      <span class="int-vis-route-node">Outbound</span>
                      <span class="int-vis-route-node">Campaign</span>
                      <span class="int-vis-route-node">Human</span>
                    </div>
                  </div>
                </div>
                <ul class="int-sc-slide-points">
                  <li>Global DID provisioning and intelligent routing across 180+ countries</li>
                  <li>Sub-second connect times with carrier redundancy and live webhooks</li>
                  <li>Seamless handoff from AI voice to human representatives with full context</li>
                </ul>
                <div class="int-sc-slide-outcomes">
                  <span class="int-sc-slide-outcome">99.2% connect rate</span>
                  <span class="int-sc-slide-outcome">&lt;1s ring-to-answer</span>
                  <span class="int-sc-slide-outcome">Global DIDs</span>
                  <span class="int-sc-slide-outcome">Live call control</span>
                </div>
                <div class="int-sc-slide-partners">
                  <span class="int-sc-slide-partners-label">Integrated partners</span>
                  <div class="int-sc-slide-partner-chips">
                    <span class="int-sc-slide-partner">Vobiz</span>
                    <span class="int-sc-slide-partner">Twilio</span>
                    <span class="int-sc-slide-partner">Plivo</span>
                    <span class="int-sc-slide-partner">Vonage</span>
                    <span class="int-sc-slide-partner">Exotel</span>
                    <span class="int-sc-slide-partner">Knowlarity</span>
                    <span class="int-sc-slide-partner">Telnyx</span>
                    <span class="int-sc-slide-partner">Bandwidth</span>
                  </div>
                </div>
                <div class="int-sc-slide-usecases">
                  <span class="int-sc-slide-usecases-label">Common applications</span>
                  <ul class="int-sc-slide-usecase-list">
                    <li>High-volume outbound dialers</li>
                    <li>Inbound support hotlines</li>
                    <li>Appointment scheduling lines</li>
                    <li>Multi-region call centers</li>
                  </ul>
                </div>
              </article>
              <article class="int-sc-slide" data-slide="llms" role="tabpanel" aria-hidden="true">
                <span class="int-sc-slide-kicker">02 — LLMs</span>
                <h3 class="int-sc-slide-headline">Pick the Perfect Brain for Every Conversation</h3>
                <p class="int-sc-slide-desc">EMAAVY routes each live call to the best large language model for the job — GPT for complex sales reasoning, Claude for compliance-sensitive dialogue, Gemini for multimodal context, Qwen for cost-efficient scale, or Grok for fast-turn programs.</p>
                <p class="int-sc-slide-detail">Swap LLM providers per agent, per intent, or mid-call without rebuilding orchestration. Prompts, guardrails, function calling, and audit logs stay centralized while your model strategy evolves with the market.</p>
                <div class="int-sc-slide-visual">
                  <div class="int-vis-llm-row">
                    <span class="int-vis-llm-chip is-active">GPT</span>
                    <span class="int-vis-llm-chip">Claude</span>
                    <span class="int-vis-llm-chip">Gemini</span>
                    <span class="int-vis-llm-chip">Qwen</span>
                    <span class="int-vis-llm-chip">Grok</span>
                  </div>
                </div>
                <ul class="int-sc-slide-points">
                  <li>Per-agent and per-campaign model routing with token governance</li>
                  <li>Structured JSON extraction for CRM fields, dispositions, and scoring</li>
                  <li>Streaming responses feed TTS for natural, low-latency voice loops</li>
                </ul>
                <div class="int-sc-slide-outcomes">
                  <span class="int-sc-slide-outcome">128K context</span>
                  <span class="int-sc-slide-outcome">Function calling</span>
                  <span class="int-sc-slide-outcome">Per-call routing</span>
                  <span class="int-sc-slide-outcome">Audit-ready prompts</span>
                </div>
                <div class="int-sc-slide-partners">
                  <span class="int-sc-slide-partners-label">Integrated partners</span>
                  <div class="int-sc-slide-partner-chips">
                    <span class="int-sc-slide-partner">OpenAI GPT</span>
                    <span class="int-sc-slide-partner">Claude</span>
                    <span class="int-sc-slide-partner">Gemini</span>
                    <span class="int-sc-slide-partner">Qwen</span>
                    <span class="int-sc-slide-partner">Grok</span>
                  </div>
                </div>
                <div class="int-sc-slide-usecases">
                  <span class="int-sc-slide-usecases-label">Common applications</span>
                  <ul class="int-sc-slide-usecase-list">
                    <li>Enterprise B2B sales</li>
                    <li>Compliance-heavy support</li>
                    <li>Lead qualification &amp; scoring</li>
                    <li>Executive insight summaries</li>
                  </ul>
                </div>
              </article>
              <article class="int-sc-slide" data-slide="stt" role="tabpanel" aria-hidden="true">
                <span class="int-sc-slide-kicker">03 — Speech-to-Text</span>
                <h3 class="int-sc-slide-headline">Real-Time Transcription Across Languages and Providers</h3>
                <p class="int-sc-slide-desc">Nine speech-to-text engines power EMAAVY's live transcription layer — Deepgram for global English speed, Sarvam for 22 Indian languages, Gladia for multilingual coverage, and Azure, Google, OpenAI, AssemblyAI, ElevenLabs, and Smallest for specialized programs.</p>
                <p class="int-sc-slide-detail">Transcripts stream in under 500ms with word-level timestamps and keyword boosting. Route STT by language, campaign, or cost profile without touching your agent logic — the same analytics and CRM layer works regardless of engine.</p>
                <div class="int-sc-slide-visual">
                  <div class="int-vis-wave" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i></div>
                  <div class="int-vis-langs">
                    <span class="int-vis-lang">EN</span><span class="int-vis-lang">HI</span><span class="int-vis-lang">TA</span><span class="int-vis-lang">TE</span><span class="int-vis-lang">MR</span><span class="int-vis-lang">+17</span>
                  </div>
                </div>
                <ul class="int-sc-slide-points">
                  <li>Streaming partial transcripts from connect — not after hang-up</li>
                  <li>Per-campaign keyword boosting for brand and compliance terms</li>
                  <li>Language-aware auto-routing to the best engine for each call</li>
                </ul>
                <div class="int-sc-slide-outcomes">
                  <span class="int-sc-slide-outcome">&lt;500ms latency</span>
                  <span class="int-sc-slide-outcome">22 languages</span>
                  <span class="int-sc-slide-outcome">9 STT engines</span>
                  <span class="int-sc-slide-outcome">Live streaming</span>
                </div>
                <div class="int-sc-slide-partners">
                  <span class="int-sc-slide-partners-label">Integrated partners</span>
                  <div class="int-sc-slide-partner-chips">
                    <span class="int-sc-slide-partner">Deepgram</span>
                    <span class="int-sc-slide-partner">Sarvam</span>
                    <span class="int-sc-slide-partner">AssemblyAI</span>
                    <span class="int-sc-slide-partner">Azure STT</span>
                    <span class="int-sc-slide-partner">Google STT</span>
                    <span class="int-sc-slide-partner">OpenAI STT</span>
                    <span class="int-sc-slide-partner">ElevenLabs STT</span>
                    <span class="int-sc-slide-partner">Gladia</span>
                    <span class="int-sc-slide-partner">Smallest</span>
                  </div>
                </div>
                <div class="int-sc-slide-usecases">
                  <span class="int-sc-slide-usecases-label">Common applications</span>
                  <ul class="int-sc-slide-usecase-list">
                    <li>Multilingual customer support</li>
                    <li>Real-time agent assist</li>
                    <li>Compliance recording &amp; QA</li>
                    <li>Conversation analytics</li>
                  </ul>
                </div>
              </article>
              <article class="int-sc-slide" data-slide="tts" role="tabpanel" aria-hidden="true">
                <span class="int-sc-slide-kicker">04 — Text-to-Speech</span>
                <h3 class="int-sc-slide-headline">Natural Voice Output for Every Agent Persona</h3>
                <p class="int-sc-slide-desc">EMAAVY synthesizes agent responses through ElevenLabs for studio-quality global voices and Flash Bulbul for natural Hinglish and Indian-market programs — so every outbound and inbound call sounds human, on-brand, and locally authentic.</p>
                <p class="int-sc-slide-detail">Voice selection is per agent and per campaign. Stream LLM tokens into TTS for conversational pacing, clone brand voices for consistency, and switch providers when programs move across regions without rebuilding flows.</p>
                <div class="int-sc-slide-visual">
                  <div class="int-vis-wave" aria-hidden="true"><i></i><i></i><i></i><i></i><i></i><i></i></div>
                  <div class="int-vis-langs">
                    <span class="int-vis-lang">EN</span><span class="int-vis-lang">HI</span><span class="int-vis-lang">Hinglish</span><span class="int-vis-lang">Studio</span>
                  </div>
                </div>
                <ul class="int-sc-slide-points">
                  <li>Low-latency streaming synthesis tied to live LLM output</li>
                  <li>Per-agent voice personas with pitch, pace, and tone control</li>
                  <li>Hinglish-native voices for Indian customer engagement programs</li>
                </ul>
                <div class="int-sc-slide-outcomes">
                  <span class="int-sc-slide-outcome">Studio quality</span>
                  <span class="int-sc-slide-outcome">Hinglish native</span>
                  <span class="int-sc-slide-outcome">Streaming TTS</span>
                  <span class="int-sc-slide-outcome">Brand voice clone</span>
                </div>
                <div class="int-sc-slide-partners">
                  <span class="int-sc-slide-partners-label">Integrated partners</span>
                  <div class="int-sc-slide-partner-chips">
                    <span class="int-sc-slide-partner">ElevenLabs</span>
                    <span class="int-sc-slide-partner">Flash Bulbul</span>
                  </div>
                </div>
                <div class="int-sc-slide-usecases">
                  <span class="int-sc-slide-usecases-label">Common applications</span>
                  <ul class="int-sc-slide-usecase-list">
                    <li>Sales agent personas</li>
                    <li>Regional support voices</li>
                    <li>IVR &amp; outbound campaigns</li>
                    <li>Brand-consistent narration</li>
                  </ul>
                </div>
              </article>
              <article class="int-sc-slide" data-slide="tools" role="tabpanel" aria-hidden="true">
                <span class="int-sc-slide-kicker">05 — Tools &amp; CRM</span>
                <h3 class="int-sc-slide-headline">Connect Your Revenue Stack and Workflow Tools</h3>
                <p class="int-sc-slide-desc">The tools layer closes every conversation loop — Salesforce and HubSpot CRM updates, WhatsApp follow-ups, Slack alerts, Cal.com and Google Calendar bookings, plus signed webhooks to any internal system. EMAAVY writes outcomes the moment calls end.</p>
                <p class="int-sc-slide-detail">Field mappings, escalation rules, and cross-channel sequences are configurable per team. Every automation is auditable, retry-safe, and runs 24/7 with the same reliability as your telephony and AI layers.</p>
                <div class="int-sc-slide-visual">
                  <div class="int-vis-hub">
                    <span class="int-vis-hub-spoke">CRM</span>
                    <span class="int-vis-hub-spoke">WhatsApp</span>
                    <span class="int-vis-hub-core">Emaavy</span>
                    <span class="int-vis-hub-spoke">Calendar</span>
                    <span class="int-vis-hub-spoke">Slack</span>
                    <span class="int-vis-hub-spoke">Webhooks</span>
                  </div>
                </div>
                <ul class="int-sc-slide-points">
                  <li>Post-call CRM sync with leads, opportunities, and custom fields</li>
                  <li>Cross-channel follow-ups on WhatsApp, email, and voice</li>
                  <li>Signed webhooks with full transcript and disposition payloads</li>
                </ul>
                <div class="int-sc-slide-outcomes">
                  <span class="int-sc-slide-outcome">CRM auto-sync</span>
                  <span class="int-sc-slide-outcome">Channel triggers</span>
                  <span class="int-sc-slide-outcome">Zero manual entry</span>
                  <span class="int-sc-slide-outcome">Audit-ready ops</span>
                </div>
                <div class="int-sc-slide-partners">
                  <span class="int-sc-slide-partners-label">Integrated partners</span>
                  <div class="int-sc-slide-partner-chips">
                    <span class="int-sc-slide-partner">Salesforce</span>
                    <span class="int-sc-slide-partner">HubSpot</span>
                    <span class="int-sc-slide-partner">WhatsApp</span>
                    <span class="int-sc-slide-partner">Slack</span>
                    <span class="int-sc-slide-partner">Cal.com</span>
                    <span class="int-sc-slide-partner">Google Calendar</span>
                    <span class="int-sc-slide-partner">Webhooks</span>
                  </div>
                </div>
                <div class="int-sc-slide-usecases">
                  <span class="int-sc-slide-usecases-label">Common applications</span>
                  <ul class="int-sc-slide-usecase-list">
                    <li>Sales follow-up sequences</li>
                    <li>Support ticket creation</li>
                    <li>Demo &amp; meeting scheduling</li>
                    <li>Custom ERP &amp; data warehouse sync</li>
                  </ul>
                </div>
              </article>'''

SPLIT_HTML = LAYER_CARDS.replace("__SLIDES__", SLIDES_HTML.strip())

GRID_RE = re.compile(
    r'    <div class="hub-clear-grid" role="list" aria-label="Integration layers">.*?</div>\n',
    re.DOTALL,
)

SLIDES_VIEWPORT_RE = re.compile(
    r'(<div class="int-sc-slides-viewport">)\s*(?:<article class="int-sc-slide".*?</article>\s*)+(</div>)',
    re.DOTALL,
)

ASSETS_CSS = '  <link rel="stylesheet" href="assets/int-showcase.css" />\n'
ASSETS_JS = '<script src="assets/int-showcase.js" defer></script>\n'

INLINE_STYLE = '''
  /* Integrations premium showcase */
  body[data-page="home"] #integrations .int-showcase {
    padding: 4px !important;
    border-radius: 24px !important;
    background: linear-gradient(145deg, #4a658b 0%, #18345d 42%, #5a7d9e 100%) !important;
    box-shadow:
      0 0 0 1px rgba(74, 101, 139, 0.45),
      0 22px 52px -14px rgba(24, 52, 93, 0.32),
      0 0 40px -10px rgba(74, 101, 139, 0.28) !important;
  }
  body[data-page="home"] #integrations .int-sc-stage:not(.is-presenting) .int-sc-pipeline {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
  }
  body[data-page="home"] #integrations .int-sc-stage.is-presenting .int-sc-pipeline,
  body[data-page="home"] #integrations .int-sc-stage.is-presenting .int-sc-ambient,
  body[data-page="home"] #integrations .int-sc-stage.is-presenting .int-sc-grid,
  body[data-page="home"] #integrations .int-sc-stage.is-presenting .int-sc-paths,
  body[data-page="home"] #integrations .int-sc-stage.is-presenting .int-sc-nodes,
  body[data-page="home"] #integrations .int-sc-stage.is-presenting .int-sc-core {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
  }
  body[data-page="home"] #integrations .int-sc-presentation {
    display: none !important;
    visibility: hidden !important;
    opacity: 0 !important;
    pointer-events: none !important;
  }
  body[data-page="home"] #integrations .int-sc-stage.is-presenting .int-sc-presentation {
    display: flex !important;
    flex-direction: column !important;
    visibility: visible !important;
    opacity: 1 !important;
    pointer-events: auto !important;
    z-index: 20 !important;
    background: linear-gradient(165deg, #f8fafc 0%, #f1f5f9 48%, #eef2f7 100%) !important;
  }
  body[data-page="home"] #integrations .int-sc-stage.is-presenting .int-sc-slide.is-active {
    display: flex !important;
    flex-direction: column !important;
  }
  body[data-page="home"] #integrations .int-sc-stage.is-presenting .int-sc-slide:not(.is-active) {
    display: none !important;
  }
  body[data-page="home"] #integrations .int-sc-slide-usecase-list li::before,
  body[data-page="home"] #integrations .int-sc-slide-points li::before {
    display: block !important;
    visibility: visible !important;
    opacity: 1 !important;
    content: "" !important;
  }
  body[data-page="home"] #integrations .int-vis-chain-block::before {
    display: none !important;
  }
  body[data-page="home"] #integrations .int-sc-stage.is-presenting {
    min-height: 500px !important;
  }
'''


def replace_slides(text: str) -> tuple[str, int]:
    def repl(m: re.Match) -> str:
        return m.group(1) + "\n" + SLIDES_HTML + "\n              " + m.group(2)

    return SLIDES_VIEWPORT_RE.subn(repl, text, count=1)


def main():
    text = INDEX.read_text(encoding="utf-8")

    if 'id="intShowcase"' not in text:
        m = GRID_RE.search(text)
        if not m:
            raise SystemExit("Could not find hub-clear-grid in integrations section")
        text = text[: m.start()] + SPLIT_HTML + text[m.end() :]
        print("Replaced integration cards with int-showcase split")
    else:
        print("int-showcase already present")

    text = text.replace(
        "<p class=\"hub-clear-intro-lead\">Connect telephony, LLMs, speech, voice, and CRM tools through one API — swap vendors per call without rebuilding your agent flows.</p>",
        "<p class=\"hub-clear-intro-lead\">Five connected layers — telephony, LLMs, speech, voice, and tools. Click any layer to explore partners, capabilities, and how EMAAVY orchestrates your full stack.</p>",
    )

    if "assets/int-showcase.css" not in text:
        for needle in (
            '<link rel="stylesheet" href="assets/hiw-showcase.css" />',
            '  <link rel="stylesheet" href="assets/hiw-showcase.css" />',
        ):
            if needle in text:
                text = text.replace(
                    needle,
                    needle + "\n  <link rel=\"stylesheet\" href=\"assets/int-showcase.css\" />",
                    1,
                )
                print("Added int-showcase.css link")
                break

    if "assets/int-showcase.js" not in text:
        text = text.replace(
            '<script src="assets/hiw-showcase.js" defer></script>',
            '<script src="assets/hiw-showcase.js" defer></script>\n' + ASSETS_JS.strip(),
            1,
        )
        print("Added int-showcase.js script")

    if "Integrations premium showcase" not in text:
        text = text.replace(
            "  </style>\n</head>",
            INLINE_STYLE + "  </style>\n</head>",
            1,
        )
        print("Added integrations inline overrides")

    text, n = replace_slides(text)
    if n:
        print("Updated integration slide content")

    INDEX.write_text(text, encoding="utf-8")
    print("Done:", INDEX)


if __name__ == "__main__":
    main()
