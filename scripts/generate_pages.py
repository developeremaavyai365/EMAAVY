#!/usr/bin/env python3
"""Generate all EMAAVY multi-page routes."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

FONTS = '''  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=general-sans@300,400,500,600&display=swap" rel="stylesheet" />'''

SCRIPTS = '''  <script src="{base}assets/routes.js"></script>
  <script src="{base}assets/components.js"></script>
  <script src="{base}assets/nav.js"></script>'''

CSS = '''  <link rel="stylesheet" href="{base}assets/nav.css" />
  <link rel="stylesheet" href="{base}assets/masthead-flex.css" />
  <link rel="stylesheet" href="{base}assets/site.css" />
  <link rel="stylesheet" href="{base}assets/emaavy-theme.css" />'''


def shell(title, description, route, base, content, extra_head=''):
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{title} — EMAAVY</title>
  <meta name="description" content="{description}" />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="{title} — EMAAVY" />
  <meta property="og:description" content="{description}" />
  <meta property="og:type" content="website" />
{FONTS}
{CSS.format(base=base)}
{extra_head}
</head>
<body data-base="{base}" data-route="{route}">
  <div id="site-nav-root"></div>
  <main class="page-main">
{content}
  </main>
  <div id="site-footer-root"></div>
{SCRIPTS.format(base=base)}
</body>
</html>
'''


def hero(kicker, h1, p, compact=False):
    cls = 'page-hero compact' if compact else 'page-hero'
    return f'''    <section class="{cls}">
      <div class="container">
        <span class="page-kicker">{kicker}</span>
        <h1>{h1}</h1>
        <p>{p}</p>
      </div>
    </section>'''


def breadcrumb(base, items):
    parts = []
    for label, path in items:
        if path:
            parts.append(f'<a href="{base}{path}">{label}</a>')
        else:
            parts.append(f'<span>{label}</span>')
    return f'        <nav class="breadcrumb" aria-label="Breadcrumb">{" › ".join(parts)}</nav>'


def integration_page(slug, title, category, desc, stats, features, base='../../'):
    stats_html = ''.join(f'          <div class="stat-box"><b>{b}</b><span>{s}</span></div>\n' for b, s in stats)
    feat_html = ''.join(f'          <li>{f}</li>\n' for f in features)
    bc = breadcrumb(base, [('Home', 'index.html'), ('Integrations', 'pages/integrations/index.html'), (title, '')])
    content = f'''{hero(category, title, desc, compact=True)}
    <section class="page-section">
      <div class="container">
{breadcrumb(base, [('Home', 'index.html'), ('Integrations', 'pages/integrations/index.html'), (title, '')])}
        <div class="stat-row">
{stats_html}        </div>
        <ul class="feature-list">
{feat_html}        </ul>
        <div class="cta-row">
          <a href="{base}book-demo.html" class="btn-primary">Connect {title} →</a>
          <a href="{base}pages/integrations/index.html" class="btn-outline">All integrations</a>
        </div>
      </div>
    </section>'''
    return shell(
        f'{title} Integration',
        f'Connect {title} with EMAAVY. {desc[:120]}',
        f'integration-{slug}',
        base,
        content,
    )


def agent_page(slug, title, desc, stats, features, base='../../'):
    stats_html = ''.join(f'          <div class="stat-box"><b>{b}</b><span>{s}</span></div>\n' for b, s in stats)
    feat_html = ''.join(f'          <li>{f}</li>\n' for f in features)
    content = f'''{hero('AI Voice Agent', title, desc, compact=True)}
    <section class="page-section">
      <div class="container">
{breadcrumb(base, [('Home', 'index.html'), ('Agents', 'pages/agents/index.html'), (title, '')])}
        <div class="stat-row">
{stats_html}        </div>
        <ul class="feature-list">
{feat_html}        </ul>
        <div class="cta-row">
          <a href="{base}book-demo.html" class="btn-primary">Deploy {title} →</a>
          <a href="{base}pages/agents/index.html" class="btn-outline">All agents</a>
        </div>
      </div>
    </section>'''
    return shell(
        title,
        f'{title} for EMAAVY — {desc[:120]}',
        f'agent-{slug}',
        base,
        content,
    )


INTEGRATIONS = [
    ('vobiz', 'Vobiz', 'Telephony', 'Enterprise-grade outbound telephony with global number provisioning, intelligent routing, and sub-second connect times.',
     [('99.2%', 'Connect rate'), ('<1s', 'Ring-to-answer')],
     ['Global DID provisioning & number pools', 'Campaign-level routing rules', 'Real-time call status webhooks', 'Carrier-grade redundancy', 'Compliance-ready recording']),
    ('openai', 'OpenAI GPT', 'LLM', 'Flagship reasoning for complex sales flows, objection handling, and structured data extraction from live calls.',
     [('128K', 'Context'), ('Top tier', 'Reasoning')],
     ['Multi-step objection handling', 'Structured JSON extraction', 'Dynamic script adaptation', 'High-value enterprise sales']),
    ('claude', 'Claude', 'LLM', 'Best-in-class comprehension for nuanced conversations and compliance-sensitive industries.',
     [('3 tiers', 'Opus/Sonnet/Haiku'), ('Best', 'Comprehension')],
     ['Deep reasoning on complex calls', 'Balanced speed + quality', 'Ultra-fast intent classification', 'Safety & compliance alignment']),
    ('gemini', 'Gemini Flash', 'LLM', 'Ultra-low-latency inference for real-time intent detection during live calls.',
     [('<200ms', 'Inference'), ('Live', 'Intent scoring')],
     ['Real-time intent classification', 'Live keyword detection', 'Streaming architecture', 'Cost-efficient at scale']),
    ('qwen', 'Qwen 3.6', 'LLM', 'Cost-efficient multilingual model optimized for Hinglish and regional Indian dialects.',
     [('22+', 'Languages'), ('Low', 'Cost tier')],
     ['Native Hinglish support', 'Regional dialect comprehension', 'High-volume campaigns', 'Indian names & places']),
    ('grok', 'Grok Beta', 'LLM', 'Experimental reasoning layer for creative outbound scripts and dynamic rebuttals.',
     [('Beta', 'Access'), ('Creative', 'Scripts')],
     ['Dynamic rebuttal generation', 'Creative script variants', 'A/B test generation', 'Pilot campaigns']),
    ('assemblyai', 'AssemblyAI', 'STT', 'Real-time transcription with strong punctuation and formatting for live voice agents.',
     [('Real-time', 'Streaming'), ('Smart', 'Punctuation')],
     ['Streaming real-time transcription', 'Automatic punctuation & formatting', 'Speaker diarization', 'Entity detection']),
    ('azure-stt', 'Azure Speech', 'STT', 'Microsoft Azure Speech Services — enterprise-grade speech recognition with global language support.',
     [('Enterprise', 'Grade'), ('100+', 'Languages')],
     ['Azure Cognitive Services integration', 'Custom speech models', 'Real-time streaming STT', 'Multi-language support']),
    ('deepgram', 'Deepgram', 'STT', 'High-accuracy, low-latency transcription with keyword boosting for live agent assist.',
     [('<500ms', 'Latency'), ('Streaming', 'Real-time')],
     ['WebSocket transcription', 'Speaker diarization', 'Custom vocabulary & keyword boosting', 'Live agent assist']),
    ('elevenlabs-stt', 'ElevenLabs STT', 'STT', 'Transcription powered by ElevenLabs — unified voice stack for STT and TTS.',
     [('Unified', 'Voice stack'), ('Streaming', 'Real-time')],
     ['ElevenLabs transcription API', 'Same API key as TTS', 'Real-time streaming', 'Multi-language support']),
    ('gladia', 'Gladia', 'STT', 'Multilingual transcription with code-switching, custom vocabulary, and sub-300ms latency.',
     [('<300ms', 'Latency'), ('100+', 'Languages')],
     ['Multilingual code-switching', 'Custom vocabulary boosting', 'Telephony audio enhancement', 'Configurable endpointing']),
    ('google-stt', 'Google STT', 'STT', 'Google Cloud Speech-to-Text with broad language coverage and telephony-optimized models.',
     [('Google', 'Cloud'), ('Broad', 'Language coverage')],
     ['Google Cloud Speech-to-Text API', 'Telephony-optimized models', 'Streaming recognition', 'Automatic punctuation']),
    ('openai-stt', 'OpenAI Whisper', 'STT', 'OpenAI Whisper-based transcription for accurate speech recognition across languages.',
     [('Whisper', 'Models'), ('Multi-language', 'Support')],
     ['OpenAI Whisper API', 'High-accuracy transcription', 'Multi-language auto-detection', 'Batch and streaming modes']),
    ('sarvam', 'Sarvam AI', 'STT', 'Optimized for Indian languages like Hindi, Tamil, and Telugu — 22 languages with native accuracy.',
     [('22', 'Languages'), ('#1', 'Indian STT')],
     ['Official Indian languages', 'Hinglish code-switching', 'Noisy environment optimization', 'Regional accent tuning']),
    ('smallest', 'Smallest AI', 'STT', 'Lightweight, fast transcription provider optimized for low-latency voice conversations.',
     [('Lightweight', 'Architecture'), ('Fast', 'Latency')],
     ['Low-latency streaming STT', 'Optimized for real-time agents', 'Cost-efficient at scale', 'Simple API integration']),
    ('elevenlabs', 'ElevenLabs', 'TTS', 'Low-latency expressive voice synthesis for warm, persuasive outbound agents.',
     [('<300ms', 'Latency'), ('Expressive', 'Voice')],
     ['Voice cloning', 'Emotional tone control', 'Multi-language voices', 'Real-time conversation']),
    ('flash-bulbul', 'Flash · Bulbul', 'TTS', 'Native Indian voice models with natural Hinglish cadence for sales and support.',
     [('Native', 'Hinglish'), ('22', 'Languages')],
     ['Bulbul V3 premium quality', 'Flash v2 low latency', 'Natural code-switching', 'Telephony-optimized audio']),
    ('webhooks', 'Webhooks', 'Tools', 'Push call events, transcripts, and scores to any endpoint the moment a call ends.',
     [('Real-time', 'Delivery'), ('Custom', 'Payloads')],
     ['call.started / ended / scored events', 'Full transcript payloads', 'HMAC verification', 'Retry with backoff']),
    ('calcom', 'Cal.com', 'Tools', 'Book meetings live during calls — agent captures the slot and creates the event instantly.',
     [('Live', 'Booking'), ('Zero', 'Manual entry')],
     ['Real-time availability', 'Auto calendar events', 'Timezone-aware scheduling', 'Email confirmations']),
    ('google-calendar', 'Google Calendar', 'Tools', 'Sync confirmed appointments into shared Google Calendars with invites and reminders.',
     [('Instant', 'Sync'), ('Team', 'Calendars')],
     ['Shared team calendars', 'Automatic invites', 'Reminder configuration', 'Two-way rescheduling']),
    ('whatsapp', 'WhatsApp', 'Tools', 'Send confirmations, links, and follow-ups automatically when a call concludes.',
     [('Auto', 'Follow-ups'), ('Rich', 'Media')],
     ['Post-call confirmations', 'Payment & booking links', 'Template messages', 'Human handoff']),
    ('slack', 'Slack', 'Tools', 'Route call intelligence, alerts, and coaching notifications to your team Slack channels in real time.',
     [('Real-time', 'Alerts'), ('Channels', 'Any workspace')],
     ['Live call alerts to channels', 'Sentiment drop notifications', 'Daily digest summaries', 'Custom webhook formatting']),
    ('salesforce', 'Salesforce', 'Tools', 'Update records, log dispositions, and push intent scores — no manual CRM entry.',
     [('Zero', 'Manual CRM'), ('Auto', 'Disposition')],
     ['Lead & contact updates', 'Call activity logging', 'Intent → lead score mapping', 'Task creation']),
    ('hubspot', 'HubSpot', 'Tools', 'Create deals, update contacts, and trigger workflows based on conversation intelligence.',
     [('Auto', 'Deals'), ('Workflow', 'Triggers')],
     ['Contact property updates', 'Deal stage progression', 'AI call summaries', 'Keyword workflow enrollment']),
]

AGENTS = [
    ('sales-agent', 'Sales Agent', 'AI outbound agent that handles prospecting, objection handling, and meeting booking with human-like persuasion.',
     [('28%', 'Conversion lift'), ('24/7', 'Operation')],
     ['Multi-step sales flows', 'Dynamic objection handling', 'Live Cal.com booking', 'CRM auto-update on close']),
    ('support-agent', 'Support Agent', 'Empathetic support agent for ticket triage, FAQ resolution, and escalation to human specialists.',
     [('61%', 'Faster resolution'), ('22', 'Languages')],
     ['Sentiment-aware responses', 'Auto ticket creation', 'Human escalation triggers', 'CSAT follow-up calls']),
    ('outbound-agent', 'Outbound Agent', 'High-volume campaign agent for registrations, follow-ups, and lead qualification at any scale.',
     [('68%', 'Registration rate'), ('10M+', 'Contacts')],
     ['Campaign pacing & retry', 'Personalized scripts', 'Real-time data capture', 'WhatsApp confirmations']),
]


def write(path, content):
    path = ROOT / path
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')
    print(f'  wrote {path.relative_to(ROOT)}')


def main():
    base = ''

    # --- HOME ---
    home = shell(
        'Signal From Every Call',
        'EMAAVY — Call intelligence platform. Record, transcribe, analyze, and act on every conversation.',
        'home',
        '',
        f'''    <section class="home-hero">
      <div>
        <p class="page-kicker">Call intelligence · reimagined</p>
        <h1>Decode <span class="accent">every</span> conversation.</h1>
        <p class="home-hero-desc">From satellite view to syllable-level insight. Record, transcribe, dissect — then act on signal your competitors never see.</p>
        <div class="cta-row">
          <a href="book-demo.html" class="btn-primary">Book a Demo →</a>
          <a href="pages/how-it-works.html" class="btn-outline">How it works</a>
        </div>
      </div>
      <div class="home-visual"><div class="home-orb" aria-hidden="true"></div></div>
    </section>
    <section class="explore-grid">
      <div class="container">
        <h2 class="section-title">Explore the platform</h2>
        <p class="section-desc">Every capability has its own dedicated page — dive into features, integrations, agents, and more.</p>
        <div class="card-grid">
          <a href="pages/how-it-works.html" class="glow-card"><div class="card-icon">⚙️</div><h3>How It Works</h3><p>Four steps from ring to action.</p><span class="card-tag">Platform →</span></a>
          <a href="pages/features.html" class="glow-card"><div class="card-icon">✨</div><h3>Features</h3><p>Bulk calling, STT, agents, intelligence.</p><span class="card-tag">Capabilities →</span></a>
          <a href="pages/integrations/index.html" class="glow-card"><div class="card-icon">🔗</div><h3>Integrations</h3><p>LLMs, STT, TTS, CRM, WhatsApp, Slack.</p><span class="card-tag">Connect →</span></a>
          <a href="pages/agents/index.html" class="glow-card"><div class="card-icon">🤖</div><h3>AI Agents</h3><p>Sales, support, and outbound agents.</p><span class="card-tag">Workforce →</span></a>
          <a href="pages/pricing.html" class="glow-card"><div class="card-icon">💎</div><h3>Pricing</h3><p>Starter to enterprise tiers.</p><span class="card-tag">Plans →</span></a>
          <a href="pages/case-studies.html" class="glow-card"><div class="card-icon">📈</div><h3>Case Studies</h3><p>Real results from real campaigns.</p><span class="card-tag">Proof →</span></a>
        </div>
      </div>
    </section>''',
    )
    write('index.html', home)

    # --- HOW IT WORKS ---
    write('pages/how-it-works.html', shell(
        'How It Works',
        'Learn how EMAAVY turns every call into intelligence — connect, transcribe, reason, and act in four steps.',
        'how-it-works', '../',
        f'''{hero('The EMAAVY Method', 'How it works', 'From the first ring to the final insight — four steps that turn every call into compounding intelligence.')}
    <section class="page-section">
      <div class="container">
        <div class="card-grid cols-2">
          <div class="glow-card"><div class="card-icon">1</div><h3>Connect</h3><p>Plug in your telephony via Vobiz. EMAAVY starts listening from the very first second of every call.</p></div>
          <div class="glow-card"><div class="card-icon">2</div><h3>Transcribe</h3><p>Real-time STT via AssemblyAI, Azure, Deepgram, Gladia, Google, OpenAI, Sarvam, and more — structured text in under 500ms.</p></div>
          <div class="glow-card"><div class="card-icon">3</div><h3>Reason</h3><p>GPT, Claude, Gemini, Qwen, or Grok analyzes intent, sentiment, and risk in real time.</p></div>
          <div class="glow-card"><div class="card-icon">4</div><h3>Act</h3><p>Triggers fire automatically — WhatsApp, CRM updates, calendar bookings. Zero manual work.</p></div>
        </div>
        <div class="cta-row"><a href="../book-demo.html" class="btn-primary">See it live →</a></div>
      </div>
    </section>''',
    ))

    # --- FEATURES ---
    write('pages/features.html', shell(
        'Features',
        'EMAAVY platform features — bulk calling, real-time transcription, AI agents, call intelligence, and enterprise security.',
        'features', '../',
        f'''{hero('Platform Capabilities', 'Built for scale. Designed for humans.', 'Every feature reduces cognitive load and amplifies the signal inside every conversation.')}
    <section class="page-section alt">
      <div class="container">
        <div class="card-grid">
          <div class="glow-card"><div class="card-icon">📞</div><h3>Bulk Calling at Scale</h3><p>Launch outbound campaigns to thousands simultaneously — personalized at individual level, executed at population scale.</p></div>
          <div class="glow-card"><div class="card-icon">⚡</div><h3>Custom API Triggers</h3><p>When keywords are detected or sentiment thresholds cross — your downstream systems react instantly.</p></div>
          <div class="glow-card"><div class="card-icon">🎙</div><h3>Real-Time Transcription</h3><p>9 STT providers — Deepgram, Sarvam, Gladia, Azure, Google, OpenAI Whisper, and more. 22 Indian languages supported.</p></div>
          <div class="glow-card"><div class="card-icon">🤖</div><h3>AI Voice Agents</h3><p>Deploy custom agents with their own voice, flow, and campaign in minutes.</p></div>
          <div class="glow-card"><div class="card-icon">📊</div><h3>Call Intelligence</h3><p>Sentiment arcs, intent spikes, drop-off heatmaps — generated automatically.</p></div>
          <div class="glow-card"><div class="card-icon">🔒</div><h3>Enterprise Security</h3><p>SOC 2 aligned infrastructure with encryption at rest and in transit.</p></div>
        </div>
      </div>
    </section>''',
    ))

    # --- INTEGRATIONS INDEX ---
    int_cards = ''.join(
        f'          <a href="{slug}.html" class="glow-card"><div class="card-icon">🔗</div><h3>{title}</h3><p>{desc[:80]}…</p><span class="card-tag">{cat} →</span></a>\n'
        for slug, title, cat, desc, _, _ in INTEGRATIONS
    )
    write('pages/integrations/index.html', shell(
        'Integrations',
        'Connect EMAAVY with OpenAI, Claude, Deepgram, WhatsApp, Slack, Salesforce, and your entire AI stack.',
        'integrations', '../../',
        f'''{hero('Integrations Hub', 'Your entire AI stack — connected', 'Every model, telephony provider, and workflow tool — with dedicated pages for each integration.')}
    <section class="page-section">
      <div class="container">
        <div class="card-grid">
{int_cards}        </div>
      </div>
    </section>''',
    ))

    for slug, title, cat, desc, stats, feats in INTEGRATIONS:
        write(f'pages/integrations/{slug}.html', integration_page(slug, title, cat, desc, stats, feats))

    # --- AGENTS INDEX ---
    agent_cards = ''.join(
        f'          <a href="{slug}.html" class="glow-card"><div class="card-icon">🤖</div><h3>{title}</h3><p>{desc[:90]}…</p><span class="card-tag">Deploy →</span></a>\n'
        for slug, title, desc, _, _ in AGENTS
    )
    write('pages/agents/index.html', shell(
        'AI Voice Agents',
        'Deploy EMAAVY AI voice agents for sales, support, and outbound campaigns at any scale.',
        'agents', '../../',
        f'''{hero('AI Workforce', 'Meet your AI agents', 'Agents that speak like humans, think faster, and never call in sick — each with its own dedicated page.')}
    <section class="page-section">
      <div class="container">
        <div class="card-grid cols-2">
{agent_cards}        </div>
        <div class="cta-row" style="margin-top:2rem"><a href="../../book-demo.html" class="btn-primary">Build your agent →</a></div>
      </div>
    </section>''',
    ))

    for slug, title, desc, stats, feats in AGENTS:
        write(f'pages/agents/{slug}.html', agent_page(slug, title, desc, stats, feats))

    # --- CASE STUDIES ---
    write('pages/case-studies.html', shell(
        'Case Studies',
        'Real EMAAVY client results — exhibition campaigns, QA automation, and logistics follow-ups.',
        'case-studies', '../',
        f'''{hero('Client Success', 'What we\'ve built for our clients', 'Real results from real campaigns — from exhibition registrations to enterprise healthcare follow-ups.')}
    <section class="page-section">
      <div class="container">
        <div class="card-grid cols-2">
          <div class="glow-card"><div class="card-icon">🏛</div><h3>Warehouse by Mudita</h3><p>5,000 outbound calls for luxury exhibition registration. Bilingual Hindi + English agent with real-time capture.</p><span class="card-tag">68% registration rate</span></div>
          <div class="glow-card"><div class="card-icon">📋</div><h3>NextCall BPO</h3><p>Replaced manual auditing with real-time intelligence — every call scored for sentiment, compliance, and intent.</p><span class="card-tag">61% faster QA</span></div>
          <div class="glow-card"><div class="card-icon">🚛</div><h3>FleetIQ Logistics</h3><p>50,000 post-delivery follow-ups per month across 8 languages. Unhappy customers routed to humans in 60 seconds.</p><span class="card-tag">28% CSAT lift</span></div>
        </div>
      </div>
    </section>''',
    ))

    # --- PRICING ---
    write('pages/pricing.html', shell(
        'Pricing',
        'EMAAVY pricing — Starter, Pro, Business, and Enterprise plans for call intelligence at any scale.',
        'pricing', '../',
        f'''{hero('Signal tiers', 'Pick your frequency', 'Scale from first call to enterprise fleets. Switch plans anytime — no lock-in.')}
    <section class="page-section alt">
      <div class="container">
        <div class="card-grid cols-4">
          <div class="glow-card"><h3>Starter</h3><p><b style="font-size:1.5rem;color:#2563eb">$0</b> /mo · 14-day trial</p><p>500 calls, 5 languages, 1 seat.</p></div>
          <div class="glow-card" style="border-color:#2563eb"><h3>Pro</h3><p><b style="font-size:1.5rem;color:#2563eb">$149</b> /mo</p><p>5K calls, all languages, 2 AI agents.</p></div>
          <div class="glow-card"><h3>Business</h3><p><b style="font-size:1.5rem;color:#2563eb">$399</b> /mo</p><p>50K calls, unlimited agents, API access.</p></div>
          <div class="glow-card"><h3>Enterprise</h3><p><b style="font-size:1.5rem;color:#2563eb">Custom</b></p><p>Dedicated infra, custom models, SLA 99.99%.</p></div>
        </div>
        <div class="cta-row"><a href="../book-demo.html" class="btn-primary">Talk to sales →</a></div>
      </div>
    </section>''',
    ))

    # --- DOCUMENTATION ---
    write('pages/documentation.html', shell(
        'Documentation',
        'EMAAVY docs — quickstart guides, API reference, and agent builder documentation.',
        'documentation', '../',
        f'''{hero('Documentation', 'Build with EMAAVY', 'Guides, API references, and quickstarts to get your first agent live in under an hour.')}
    <section class="page-section">
      <div class="container">
        <div class="card-grid cols-2">
          <div class="glow-card"><div class="card-icon">🚀</div><h3>Quickstart Guide</h3><p>Launch your first outbound campaign in 15 minutes.</p></div>
          <div class="glow-card"><div class="card-icon">⚡</div><h3>API Reference</h3><p>Webhooks, REST endpoints, and event schemas.</p></div>
          <div class="glow-card"><div class="card-icon">🤖</div><h3>Agent Builder</h3><p>Design voice flows and deploy agents across languages.</p></div>
        </div>
      </div>
    </section>''',
    ))

    # --- CONTACT ---
    write('pages/contact.html', shell(
        'Contact Us',
        'Contact EMAAVY — sales, support, and partnership inquiries.',
        'contact', '../',
        f'''{hero('Contact', 'Get in touch', 'Questions about EMAAVY? Our team responds within 24 hours.')}
    <section class="page-section alt">
      <div class="container" style="max-width:560px">
        <form class="glow-card" style="padding:2rem">
          <input class="demo-input" type="text" placeholder="Your name" style="width:100%;padding:0.85rem;border:2px solid rgba(37,99,235,0.15);border-radius:12px;margin-bottom:0.75rem;font-family:inherit" required />
          <input class="demo-input" type="email" placeholder="Work email" style="width:100%;padding:0.85rem;border:2px solid rgba(37,99,235,0.15);border-radius:12px;margin-bottom:0.75rem;font-family:inherit" required />
          <textarea placeholder="How can we help?" rows="4" style="width:100%;padding:0.85rem;border:2px solid rgba(37,99,235,0.15);border-radius:12px;margin-bottom:1rem;font-family:inherit;resize:vertical"></textarea>
          <button type="submit" class="btn-primary" style="width:100%;justify-content:center;border:none">Send message →</button>
        </form>
      </div>
    </section>''',
    ))

    # --- LOGIN & BOOK DEMO ---
    auth_pages = [
        ('login.html', 'login', 'Log In', 'Sign in to your EMAAVY workspace.',
         '''          <form id="authForm" class="glow-card" style="padding:2rem;max-width:420px;margin:0 auto">
            <span class="page-kicker">Secure sign in</span>
            <h1 style="font-family:'Clash Display',sans-serif;font-size:1.75rem;margin:0.5rem 0">Welcome back</h1>
            <p style="color:#64748b;margin-bottom:1.25rem">Sign in to manage campaigns, agents, and intelligence.</p>
            <input type="email" placeholder="Work email" required style="width:100%;padding:0.85rem;border:2px solid rgba(37,99,235,0.15);border-radius:12px;margin-bottom:0.75rem;font-family:inherit" />
            <input type="password" placeholder="Password" required style="width:100%;padding:0.85rem;border:2px solid rgba(37,99,235,0.15);border-radius:12px;margin-bottom:1rem;font-family:inherit" />
            <button type="submit" class="btn-primary" style="width:100%;justify-content:center;border:none">Log In →</button>
          </form>'''),
        ('book-demo.html', 'book-demo', 'Book a Demo', 'Schedule a live EMAAVY product walkthrough.',
         '''          <form id="demoForm" class="glow-card" style="padding:2rem;max-width:560px;margin:0 auto">
            <span class="page-kicker">Live walkthrough</span>
            <h1 style="font-family:'Clash Display',sans-serif;font-size:1.75rem;margin:0.5rem 0">Book your demo</h1>
            <p style="color:#64748b;margin-bottom:1.25rem">See a real campaign in your industry — 20 minutes, no commitment.</p>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;margin-bottom:0.75rem">
              <input type="text" placeholder="Name" required style="padding:0.85rem;border:2px solid rgba(37,99,235,0.15);border-radius:12px;font-family:inherit" />
              <input type="text" placeholder="Company" required style="padding:0.85rem;border:2px solid rgba(37,99,235,0.15);border-radius:12px;font-family:inherit" />
            </div>
            <input type="email" placeholder="Work email" required style="width:100%;padding:0.85rem;border:2px solid rgba(37,99,235,0.15);border-radius:12px;margin-bottom:0.75rem;font-family:inherit" />
            <input type="text" placeholder="What are you building?" style="width:100%;padding:0.85rem;border:2px solid rgba(37,99,235,0.15);border-radius:12px;margin-bottom:1rem;font-family:inherit" />
            <button type="submit" class="btn-primary" style="width:100%;justify-content:center;border:none">Book My Demo →</button>
          </form>'''),
    ]
    for fname, route, title, desc, form in auth_pages:
        content = f'''    <section class="page-hero compact">
      <div class="container">
{form}
      </div>
    </section>'''
        page = shell(title, desc, route, '', content)
        page = page.replace('</body>', '''  <script>
    document.querySelector('form')?.addEventListener('submit', (e) => { e.preventDefault(); alert("Thank you! We'll be in touch shortly."); });
  </script>
</body>''')
        write(fname, page)

    print(f'\nGenerated {len(list(ROOT.rglob("pages/**/*.html")))} page files.')


if __name__ == '__main__':
    print('Generating EMAAVY pages...')
    main()
