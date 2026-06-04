#!/usr/bin/env python3
"""Patch emaavy_white_blue (2).html with full SPA multi-page navigation."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent
FILE = ROOT / 'emaavy_white_blue (2).html'

INTEGRATIONS = [
    ('vobiz', 'Vobiz', 'Telephony', 'Enterprise-grade outbound telephony with global number provisioning and sub-second connect times.',
     [('99.2%', 'Connect rate'), ('<1s', 'Ring-to-answer')],
     ['Global DID provisioning', 'Campaign routing rules', 'Real-time webhooks', 'Carrier redundancy']),
    ('openai', 'OpenAI GPT', 'LLM', 'Flagship reasoning for complex sales flows and structured data extraction.',
     [('128K', 'Context'), ('Top tier', 'Reasoning')],
     ['Multi-step objection handling', 'JSON extraction', 'Dynamic scripts', 'Enterprise sales']),
    ('claude', 'Claude', 'LLM', 'Best-in-class comprehension for nuanced and compliance-sensitive conversations.',
     [('3 tiers', 'Opus/Sonnet/Haiku'), ('Best', 'Comprehension')],
     ['Deep reasoning', 'Balanced speed', 'Intent classification', 'Safety alignment']),
    ('gemini', 'Gemini Flash', 'LLM', 'Ultra-low-latency inference for real-time intent detection.',
     [('<200ms', 'Inference'), ('Live', 'Scoring')],
     ['Intent classification', 'Keyword detection', 'Streaming', 'Cost-efficient']),
    ('qwen', 'Qwen 3.6', 'LLM', 'Multilingual model optimized for Hinglish and regional dialects.',
     [('22+', 'Languages'), ('Low', 'Cost')],
     ['Hinglish support', 'Regional dialects', 'High-volume', 'Indian names']),
    ('grok', 'Grok Beta', 'LLM', 'Experimental reasoning for creative scripts and dynamic rebuttals.',
     [('Beta', 'Access'), ('Creative', 'Scripts')],
     ['Dynamic rebuttals', 'Script variants', 'A/B testing', 'Pilot campaigns']),
    ('deepgram', 'Deepgram', 'STT', 'Sub-500ms streaming transcription for live agent assist.',
     [('<500ms', 'Latency'), ('Streaming', 'Real-time')],
     ['WebSocket STT', 'Speaker diarization', 'Custom vocabulary', 'Live assist']),
    ('sarvam', 'Sarvam AI', 'STT', 'Purpose-built for 22 Indian languages and accents.',
     [('22', 'Languages'), ('#1', 'Indian STT')],
     ['Indian languages', 'Hinglish', 'Noisy environments', 'Accent tuning']),
    ('elevenlabs', 'ElevenLabs', 'TTS', 'Low-latency expressive voice synthesis for outbound agents.',
     [('<300ms', 'Latency'), ('Expressive', 'Voice')],
     ['Voice cloning', 'Tone control', 'Multi-language', 'Real-time']),
    ('flash-bulbul', 'Flash · Bulbul', 'TTS', 'Native Indian voices with natural Hinglish cadence.',
     [('Native', 'Hinglish'), ('22', 'Languages')],
     ['Bulbul V3 quality', 'Flash v2 latency', 'Code-switching', 'Telephony audio']),
    ('webhooks', 'Webhooks', 'Tools', 'Push call events and transcripts to any endpoint instantly.',
     [('Real-time', 'Delivery'), ('Custom', 'Payloads')],
     ['Event webhooks', 'Full transcripts', 'HMAC verify', 'Retry logic']),
    ('calcom', 'Cal.com', 'Tools', 'Book meetings live during calls with instant calendar events.',
     [('Live', 'Booking'), ('Zero', 'Manual entry')],
     ['Availability check', 'Auto events', 'Timezones', 'Confirmations']),
    ('google-calendar', 'Google Calendar', 'Tools', 'Sync appointments into shared team calendars.',
     [('Instant', 'Sync'), ('Team', 'Calendars')],
     ['Shared calendars', 'Auto invites', 'Reminders', 'Two-way sync']),
    ('whatsapp', 'WhatsApp', 'Tools', 'Send confirmations and follow-ups when calls conclude.',
     [('Auto', 'Follow-ups'), ('Rich', 'Media')],
     ['Post-call messages', 'Booking links', 'Templates', 'Human handoff']),
    ('slack', 'Slack', 'Tools', 'Route call intelligence and alerts to Slack channels in real time.',
     [('Real-time', 'Alerts'), ('Channels', 'Any workspace')],
     ['Live alerts', 'Sentiment drops', 'Daily digests', 'Custom formatting']),
    ('salesforce', 'Salesforce', 'Tools', 'Update CRM records and log dispositions automatically.',
     [('Zero', 'Manual CRM'), ('Auto', 'Disposition')],
     ['Record updates', 'Call logging', 'Intent scores', 'Task creation']),
    ('hubspot', 'HubSpot', 'Tools', 'Create deals and trigger workflows from conversation data.',
     [('Auto', 'Deals'), ('Workflow', 'Triggers')],
     ['Contact updates', 'Deal stages', 'AI summaries', 'Keyword workflows']),
]

AGENTS = [
    ('sales-agent', 'Sales Agent', 'Outbound agent for prospecting, objections, and meeting booking.',
     [('28%', 'Conversion lift'), ('24/7', 'Operation')],
     ['Sales flows', 'Objection handling', 'Cal.com booking', 'CRM sync']),
    ('support-agent', 'Support Agent', 'Empathetic agent for triage, FAQ, and escalation.',
     [('61%', 'Faster resolution'), ('22', 'Languages')],
     ['Sentiment responses', 'Ticket creation', 'Human escalation', 'CSAT follow-up']),
    ('outbound-agent', 'Outbound Agent', 'High-volume campaigns for registrations and qualification.',
     [('68%', 'Registration rate'), ('10M+', 'Contacts')],
     ['Campaign pacing', 'Personalized scripts', 'Data capture', 'WhatsApp confirm']),
]


def page_view(route_id, kicker, title, desc, body_extra=''):
    vid = 'view-' + route_id.replace('/', '-')
    return f'''
    <div id="{vid}" class="spa-view">
      <div class="page-main">
        <section class="page-hero">
          <div class="container">
            <span class="page-kicker">{kicker}</span>
            <h1>{title}</h1>
            <p>{desc}</p>
          </div>
        </section>
        <section class="page-section">
          <div class="container">
            {body_extra}
          </div>
        </section>
      </div>
    </div>'''


def stat_features(stats, features):
    stats_html = ''.join(f'<div class="stat-box"><b>{b}</b><span>{s}</span></div>' for b, s in stats)
    feat_html = ''.join(f'<li>{f}</li>' for f in features)
    return f'''<div class="stat-row">{stats_html}</div>
            <ul class="feature-list">{feat_html}</ul>
            <div class="cta-row"><a href="#/book-demo" class="btn-primary">Get started →</a></div>'''


def card_grid(cards):
    return '<div class="card-grid">' + ''.join(
        f'<a href="{href}" class="glow-card"><div class="card-icon">{icon}</div><h3>{title}</h3><p>{text}</p></a>'
        for href, icon, title, text in cards
    ) + '</div>'


def build_spa_views():
    views = []

    views.append(page_view('how-it-works', 'The EMAAVY Method', 'How it works',
        'From the first ring to the final insight — four steps that turn every call into compounding intelligence.',
        card_grid([
            ('#/how-it-works', '1', 'Connect', 'Plug in telephony via Vobiz — listening from second one.'),
            ('#/how-it-works', '2', 'Transcribe', 'Deepgram + Sarvam — 22 languages in under 500ms.'),
            ('#/how-it-works', '3', 'Reason', 'GPT, Claude, Gemini, Qwen, or Grok analyze live.'),
            ('#/how-it-works', '4', 'Act', 'WhatsApp, CRM, calendars — triggers fire automatically.'),
        ])))

    views.append(page_view('features', 'Platform Capabilities', 'Built for scale. Designed for humans.',
        'Every feature reduces cognitive load and amplifies signal inside every conversation.',
        card_grid([
            ('#/features', '📞', 'Bulk Calling', 'Campaigns to thousands — personalized at scale.'),
            ('#/features', '⚡', 'API Triggers', 'Custom logic when keywords or sentiment cross thresholds.'),
            ('#/features', '🎙', 'Real-Time STT', '22 languages, Hinglish, Deepgram + Sarvam.'),
            ('#/features', '🤖', 'AI Voice Agents', 'Custom voice, flow, and campaign in minutes.'),
            ('#/features', '📊', 'Call Intelligence', 'Sentiment arcs, intent spikes, heatmaps.'),
            ('#/features', '🔒', 'Enterprise Security', 'SOC 2 aligned encryption and audit logs.'),
        ])))

    int_cards = [(f'#/integrations/{s}', '🔗', t, d[:70] + '…') for s, t, _, d, _, _ in INTEGRATIONS]
    views.append(page_view('integrations', 'Integrations Hub', 'Your entire AI stack — connected',
        'Every model, telephony provider, and workflow tool — each with its own dedicated route.',
        card_grid(int_cards)))

    for slug, title, cat, desc, stats, feats in INTEGRATIONS:
        views.append(page_view(f'integrations/{slug}', cat, title, desc, stat_features(stats, feats)))

    agent_cards = [(f'#/agents/{s}', '🤖', t, d[:80] + '…') for s, t, d, _, _ in AGENTS]
    views.append(page_view('agents', 'AI Workforce', 'Meet your AI agents',
        'Agents that speak like humans, think faster, and never call in sick.',
        card_grid(agent_cards) + '<div class="cta-row"><a href="#/book-demo" class="btn-primary">Build your agent →</a></div>'))

    for slug, title, desc, stats, feats in AGENTS:
        views.append(page_view(f'agents/{slug}', 'AI Voice Agent', title, desc, stat_features(stats, feats)))

    views.append(page_view('case-studies', 'Client Success', 'What we\'ve built for our clients',
        'Real results from real campaigns.',
        card_grid([
            ('#/case-studies', '🏛', 'Warehouse by Mudita', '68% registration rate — 5,000 outbound calls.'),
            ('#/case-studies', '📋', 'NextCall BPO', '61% faster QA with real-time intelligence.'),
            ('#/case-studies', '🚛', 'FleetIQ Logistics', '28% CSAT lift — 50K follow-ups/month.'),
        ])))

    views.append(page_view('pricing', 'Signal tiers', 'Pick your frequency',
        'Scale from first call to enterprise fleets.',
        '''<div class="card-grid cols-4">
              <div class="glow-card"><h3>Starter</h3><p><b style="font-size:1.5rem;color:#2563eb">$0</b>/mo · 500 calls</p></div>
              <div class="glow-card" style="border-color:#2563eb"><h3>Pro</h3><p><b style="font-size:1.5rem;color:#2563eb">$149</b>/mo · 5K calls</p></div>
              <div class="glow-card"><h3>Business</h3><p><b style="font-size:1.5rem;color:#2563eb">$399</b>/mo · 50K calls</p></div>
              <div class="glow-card"><h3>Enterprise</h3><p><b style="font-size:1.5rem;color:#2563eb">Custom</b> · Unlimited</p></div>
            </div><div class="cta-row"><a href="#/book-demo" class="btn-primary">Talk to sales →</a></div>'''))

    views.append(page_view('documentation', 'Documentation', 'Build with EMAAVY',
        'Guides, API references, and quickstarts.',
        card_grid([
            ('#/documentation', '🚀', 'Quickstart', 'First campaign in 15 minutes.'),
            ('#/documentation', '⚡', 'API Reference', 'Webhooks, REST, event schemas.'),
            ('#/documentation', '🤖', 'Agent Builder', 'Voice flows across languages.'),
        ])))

    views.append(page_view('contact', 'Contact', 'Get in touch',
        'Our team responds within 24 hours.',
        '''<form class="glow-card" style="padding:2rem;max-width:520px" onsubmit="event.preventDefault();alert('Message sent!');">
              <input type="text" placeholder="Your name" required style="width:100%;padding:0.85rem;border:2px solid rgba(37,99,235,0.15);border-radius:12px;margin-bottom:0.75rem;font-family:inherit" />
              <input type="email" placeholder="Work email" required style="width:100%;padding:0.85rem;border:2px solid rgba(37,99,235,0.15);border-radius:12px;margin-bottom:0.75rem;font-family:inherit" />
              <textarea placeholder="Message" rows="4" style="width:100%;padding:0.85rem;border:2px solid rgba(37,99,235,0.15);border-radius:12px;margin-bottom:1rem;font-family:inherit"></textarea>
              <button type="submit" class="btn-primary" style="border:none;width:100%;justify-content:center">Send →</button>
            </form>'''))

    views.append(page_view('login', 'Secure sign in', 'Welcome back',
        'Sign in to your EMAAVY workspace.',
        '''<form class="glow-card" style="padding:2rem;max-width:420px;margin:0 auto" onsubmit="event.preventDefault();EMAAVYRouter.navigate('home');">
              <input type="email" placeholder="Work email" required style="width:100%;padding:0.85rem;border:2px solid rgba(37,99,235,0.15);border-radius:12px;margin-bottom:0.75rem;font-family:inherit" />
              <input type="password" placeholder="Password" required style="width:100%;padding:0.85rem;border:2px solid rgba(37,99,235,0.15);border-radius:12px;margin-bottom:1rem;font-family:inherit" />
              <button type="submit" class="btn-primary" style="border:none;width:100%;justify-content:center">Log In →</button>
            </form>'''))

    views.append(page_view('book-demo', 'Live walkthrough', 'Book your demo',
        'See a real campaign in your industry — 20 minutes, no commitment.',
        '''<form class="glow-card" style="padding:2rem;max-width:560px;margin:0 auto" onsubmit="event.preventDefault();alert('Demo booked!');">
              <div style="display:grid;grid-template-columns:1fr 1fr;gap:0.75rem;margin-bottom:0.75rem">
                <input type="text" placeholder="Name" required style="padding:0.85rem;border:2px solid rgba(37,99,235,0.15);border-radius:12px;font-family:inherit" />
                <input type="text" placeholder="Company" required style="padding:0.85rem;border:2px solid rgba(37,99,235,0.15);border-radius:12px;font-family:inherit" />
              </div>
              <input type="email" placeholder="Work email" required style="width:100%;padding:0.85rem;border:2px solid rgba(37,99,235,0.15);border-radius:12px;margin-bottom:1rem;font-family:inherit" />
              <button type="submit" class="btn-primary" style="border:none;width:100%;justify-content:center">Book My Demo →</button>
            </form>'''))

    return '\n'.join(views)


def main():
    text = FILE.read_text(encoding='utf-8')

    # Head: SEO + site.css
    if 'assets/site.css' not in text:
        text = text.replace(
            '<link rel="stylesheet" href="assets/nav.css" />',
            '<link rel="stylesheet" href="assets/nav.css" />\n  <link rel="stylesheet" href="assets/site.css" />'
        )
    if 'meta name="description"' not in text:
        text = text.replace(
            '<title>EMAAVY — Signal From Every Call</title>',
            '<title>EMAAVY — Signal From Every Call</title>\n  <meta name="description" content="EMAAVY call intelligence — record, transcribe, analyze, and act on every conversation." />\n  <meta name="robots" content="index, follow" />\n  <meta property="og:title" content="EMAAVY — Signal From Every Call" />\n  <meta property="og:description" content="Decode every conversation with EMAAVY call intelligence." />'
        )

    # Body SPA attrs
    text = text.replace('<body data-page="home">', '<body data-spa="true" data-base="" data-route="home">')

    # SPA view CSS
    spa_css = '''
    .spa-view { display: none; }
    .spa-view.active { display: block; }
    body[data-spa="true"] .masthead { display: none !important; }
    body[data-spa="true"] .mobile-nav-drawer,
    body[data-spa="true"] .mobile-nav-backdrop { z-index: 960; }
    body[data-spa="true"] .shell { margin-left: var(--rail, 88px); }
    @media (max-width: 1024px) { body[data-spa="true"] .shell { margin-left: 0; } }
'''
    if '.spa-view { display: none' not in text:
        text = text.replace('  </style>', spa_css + '\n  </style>', 1)

    # Replace masthead + mobile nav with component mount
    old_nav = re.search(
        r'  <header class="masthead".*?</nav>\n\n  <aside class="rail">',
        text, re.DOTALL
    )
    if old_nav:
        text = text.replace(
            old_nav.group(0),
            '  <div id="site-nav-root"></div>\n\n  <div id="spa-views">\n  <div id="view-home" class="spa-view active">\n  <aside class="rail">'
        )

    # Close view-home before detail drawer
    if '<div id="spa-views">' in text and '</div>\n\n\n  <div class="detail-drawer"' not in text:
        text = text.replace(
            '\n\n\n  <div class="detail-drawer"',
            '\n  </div>\n' + build_spa_views() + '\n  </div>\n\n  <div id="site-footer-root"></div>\n\n  <div class="detail-drawer"'
        )

    # Scripts
    old_scripts = '<script src="assets/nav.js"></script>'
    new_scripts = '''<script src="assets/routes.js"></script>
  <script src="assets/components.js"></script>
  <script src="assets/nav.js"></script>
  <script src="assets/spa-router.js"></script>'''
    if 'assets/routes.js' not in text:
        text = text.replace(old_scripts, new_scripts)

    # detailCta -> spa book demo
    text = text.replace(
        "window.location.href = 'book-demo.html'",
        "EMAAVYRouter.navigate('book-demo')"
    )

    FILE.write_text(text, encoding='utf-8')
    print('Patched', FILE.name)


if __name__ == '__main__':
    main()
