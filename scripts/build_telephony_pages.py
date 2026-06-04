#!/usr/bin/env python3
"""Generate telephony hub + per-partner integration pages."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INT = ROOT / "pages" / "integrations"

HEAD_COMMON = """  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://api.fontshare.com/v2/css?f[]=clash-display@400,500,600,700&f[]=general-sans@300,400,500,600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="../../assets/nav.css" />
  <link rel="stylesheet" href="../../assets/masthead-flex.css" />
  <link rel="stylesheet" href="../../assets/site.css" />
  <link rel="stylesheet" href="../../assets/emaavy-theme.css" />
"""

PARTNERS = [
    {
        "slug": "vobiz",
        "name": "Vobiz",
        "region": "Native carrier · Global",
        "tag": "Native partner",
        "featured": True,
        "logo": '<img src="../../assets/logos/vobiz.svg" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="../../assets/logos/vobiz.svg" alt="" width="32" height="32" loading="lazy" />',
        "title": "Vobiz — EMAAVY",
        "h1": "Vobiz",
        "meta": "Connect Vobiz with EMAAVY — global DIDs, intelligent routing, and sub-second connect times built for AI voice at scale.",
        "lead": "Vobiz is EMAAVY's native telephony partner — engineered for AI voice programs that need global numbers, campaign-level routing, and carrier-grade reliability from day one.",
        "stats": [("99.2%", "Connect rate"), ("<1s", "Ring-to-answer"), ("Global", "DID pools")],
        "about": [
            "Vobiz provides programmable voice infrastructure with global number provisioning, intelligent routing, and real-time call control APIs. Teams use Vobiz when they need predictable connect rates and sub-second media setup for high-volume AI dialers.",
            "Unlike generic CPaaS setups bolted onto agents as an afterthought, Vobiz was the reference carrier when EMAAVY's voice stack was designed — so webhooks, disposition events, and media streaming align with how AI agents actually run in production.",
        ],
        "emaavy": [
            ("Native media path", "EMAAVY opens the voice channel on Vobiz and streams audio into STT and LLM pipelines from the first ring."),
            ("Campaign routing", "Assign numbers and routing rules per outbound or inbound campaign without duplicate configuration."),
            ("Live operations", "Supervisors see connect rates, active calls, and agent handoffs in the same workspace as conversation intelligence."),
            ("Compliance hooks", "Recording, retention, and audit events flow through EMAAVY's governance layer automatically."),
        ],
        "features": [
            ("Global DID provisioning", "Purchase and pool numbers across regions for localized caller ID."),
            ("Intent-aware routing", "Route by campaign, geography, or agent skill without manual trunk juggling."),
            ("Real-time webhooks", "Ring, answer, hangup, and transfer events drive CRM and supervisor dashboards."),
            ("Number pools", "Rotate outbound caller IDs to improve answer rates on large programs."),
            ("Carrier redundancy", "Failover paths when primary routes degrade during peak hours."),
            ("Recording ready", "Call audio available for QA, coaching, and compliance review."),
        ],
        "uses": [
            ("Enterprise outbound", "High-volume registration, renewal, and sales programs with AI agents."),
            ("Multilingual support", "Inbound lines with regional numbers and language-specific agents."),
            ("BPO operations", "Replace manual dialers with governed AI voice at scale."),
        ],
        "setup": [
            ("Connect Vobiz credentials", "Add API keys and account identifiers in the EMAAVY integrations console."),
            ("Provision numbers", "Select DIDs or pools mapped to each campaign or agent group."),
            ("Map webhooks", "EMAAVY registers call-status endpoints on your Vobiz application automatically."),
            ("Assign agents", "Link voice agents to campaigns — test with a sandbox call before go-live."),
        ],
        "hub_desc": "Global DIDs, intelligent routing, and sub-second connect times — the native carrier integration EMAAVY was built around.",
        "hub_points": ["Global DID provisioning and number pools", "Campaign-level routing rules", "Real-time call status webhooks"],
        "hub_badge": "Native carrier",
    },
    {
        "slug": "twilio",
        "name": "Twilio",
        "region": "Global CPaaS",
        "tag": "Global CPaaS",
        "logo": '<img src="https://cdn.worldvectorlogo.com/logos/twilio-2.svg" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="https://cdn.worldvectorlogo.com/logos/twilio-2.svg" alt="" width="32" height="32" loading="lazy" />',
        "title": "Twilio Voice — EMAAVY",
        "h1": "Twilio Voice",
        "meta": "Integrate Twilio Programmable Voice with EMAAVY — global numbers, media streams, and webhook-driven AI agents.",
        "lead": "Twilio Programmable Voice gives teams worldwide number inventory, elastic scale, and mature APIs — EMAAVY connects your agents to Twilio without rebuilding orchestration or analytics.",
        "stats": [("Global", "Coverage"), ("REST + WS", "APIs"), ("Elastic", "Scale")],
        "about": [
            "Twilio is the world's most widely adopted communications platform-as-a-service. Programmable Voice lets you place and receive calls, manage phone numbers, record conversations, and stream live audio over WebSockets.",
            "Organizations already standardized on Twilio keep their carrier contracts and number porting while EMAAVY layers transcription, reasoning, and campaign logic on top of the same voice sessions.",
        ],
        "emaavy": [
            ("Programmable outbound", "Launch AI campaigns that dial through Twilio with per-campaign caller ID and pacing rules."),
            ("Inbound lines", "Route support and hotline traffic to EMAAVY agents with IVR handoff when needed."),
            ("Media streams", "Live audio feeds STT and LLM pipelines for sub-second agent responses."),
            ("Unified analytics", "Twilio call events and EMAAVY intelligence appear in one operations view."),
        ],
        "features": [
            ("Programmable Voice", "Outbound and inbound call control via REST APIs."),
            ("Global numbers", "Provision local, mobile, and toll-free numbers in 100+ countries."),
            ("Media Streams", "WebSocket audio for real-time AI processing."),
            ("Call recording", "Store and replay conversations for QA workflows."),
            ("Elastic SIP", "Trunk enterprise PBX systems into the same agent layer."),
            ("Status callbacks", "Webhook events for initiated, ringing, answered, and completed states."),
        ],
        "uses": [
            ("Global sales teams", "Multi-region outbound with localized numbers and compliance tooling."),
            ("Contact centers", "Blend human queues with AI triage on shared Twilio infrastructure."),
            ("Product-led growth", "Spin up pilot voice agents on existing Twilio subaccounts."),
        ],
        "setup": [
            ("Link Twilio account", "Provide Account SID and auth token in EMAAVY integrations."),
            ("Configure TwiML or API", "EMAAVY sets voice URLs and status callbacks on your application."),
            ("Enable media streams", "Optional WebSocket stream for lowest-latency agent loops."),
            ("Test and scale", "Run sandbox calls, then attach production numbers to campaigns."),
        ],
        "hub_desc": "Programmable Voice APIs with global reach and trusted carrier infrastructure for teams on Twilio.",
        "hub_points": ["Elastic scale for burst outbound", "Mature global number inventory", "Webhook-driven call control"],
        "hub_badge": "Global CPaaS",
    },
    {
        "slug": "plivo",
        "name": "Plivo",
        "region": "Global CPaaS",
        "tag": "Direct routes",
        "logo": '<img src="../../assets/logos/plivo.svg" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="../../assets/logos/plivo.svg" alt="" width="32" height="32" loading="lazy" />',
        "title": "Plivo — EMAAVY",
        "h1": "Plivo",
        "meta": "Route AI voice through Plivo with EMAAVY — direct carrier routes, competitive international rates, and voice API parity.",
        "lead": "Plivo combines cloud telephony APIs with direct carrier relationships — ideal for high-volume international dial programs that need cost control without sacrificing API simplicity.",
        "stats": [("190+", "Countries"), ("Direct", "Carriers"), ("Voice API", "Parity")],
        "about": [
            "Plivo offers Voice API, SMS, and number services with emphasis on direct carrier routes and transparent international pricing. Engineering teams choose Plivo when per-minute economics matter at scale.",
            "EMAAVY maps Plivo call events to the same agent lifecycle used across other carriers, so switching or combining providers does not require retraining operations staff.",
        ],
        "emaavy": [
            ("High-volume outbound", "Run tens of thousands of AI calls per day with rate-optimized routing."),
            ("Inbound parity", "Support lines and verification flows on the same integration."),
            ("Event alignment", "Plivo hangup and recording events sync to CRM dispositions automatically."),
            ("SIP option", "Enterprise SIP trunks terminate into EMAAVY media processing."),
        ],
        "features": [
            ("Voice API", "Place and receive calls with XML or REST control."),
            ("Direct routes", "Carrier relationships that improve answer rates abroad."),
            ("Global inventory", "Search and rent numbers across major markets."),
            ("Call recording", "Compliance and coaching-ready audio artifacts."),
            ("Conference & bridge", "Complex flows when agents escalate to humans."),
            ("Real-time events", "HTTP callbacks on call state changes."),
        ],
        "uses": [
            ("International outbound", "Sales and collections across multiple countries."),
            ("Verification calls", "OTP and appointment confirmation at low cost."),
            ("Startup scale-ups", "API-first telephony without long carrier contracts."),
        ],
        "setup": [
            ("Add Plivo auth", "Connect auth ID and token in EMAAVY."),
            ("Rent numbers", "Attach Plivo numbers to campaigns or agent groups."),
            ("Set answer URLs", "EMAAVY configures voice answer and hangup handlers."),
            ("Monitor spend", "Track minutes and connect rates beside agent KPIs."),
        ],
        "hub_desc": "Cloud telephony with direct carrier routes and competitive international pricing for high-volume programs.",
        "hub_points": ["Direct carrier routes", "International rate optimization", "Voice API parity with EMAAVY events"],
        "hub_badge": "Global CPaaS",
    },
    {
        "slug": "vonage",
        "name": "Vonage",
        "region": "Global CPaaS · SIP",
        "tag": "SIP + PSTN",
        "logo": '<img src="https://cdn.simpleicons.org/vonage/000000" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="https://cdn.simpleicons.org/vonage/000000" alt="" width="32" height="32" loading="lazy" />',
        "title": "Vonage Voice API — EMAAVY",
        "h1": "Vonage Voice API",
        "meta": "Vonage Voice API and EMAAVY — programmable calling, SIP connectivity, and global numbers for AI voice deployments.",
        "lead": "Vonage (formerly Nexmo) powers voice, video, and messaging for enterprises worldwide. EMAAVY integrates Vonage Voice API for blended contact-center and SIP workloads.",
        "stats": [("SIP + PSTN", "Connectivity"), ("Global", "Numbers"), ("Enterprise", "Support")],
        "about": [
            "Vonage Voice API supports outbound and inbound calls, NCCO call control, recording, and SIP interconnect. It is a common choice for organizations migrating legacy contact centers to programmable infrastructure.",
            "With EMAAVY, Vonage sessions feed the same real-time transcription and agent reasoning layer — whether calls originate from PSTN, SIP trunks, or WebRTC endpoints.",
        ],
        "emaavy": [
            ("Blended centers", "AI handles tier-1 volume; Vonage routes escalations to human queues."),
            ("SIP enterprises", "Keep existing trunks while adding AI agents on selective campaigns."),
            ("Global footprint", "Provision numbers in key markets without separate orchestration code."),
            ("Recording & compliance", "Align Vonage recordings with EMAAVY audit policies."),
        ],
        "features": [
            ("Voice API", "NCCO-driven call flows with JSON control."),
            ("SIP trunks", "Connect on-prem or cloud PBX infrastructure."),
            ("Number management", "Search, buy, and port numbers globally."),
            ("WebRTC", "Browser-based calling for supervisor monitoring."),
            ("Call recording", "Store conversations with configurable retention."),
            ("Low-latency media", "Optimized paths for conversational AI loops."),
        ],
        "uses": [
            ("Contact centers", "AI-first routing with human overflow on Vonage."),
            ("Financial services", "Secure voice with enterprise Vonage contracts."),
            ("Retail support", "Seasonal inbound spikes handled by AI agents."),
        ],
        "setup": [
            ("Connect Vonage API", "Add API key and application ID to EMAAVY."),
            ("Configure application", "EMAAVY sets answer and event URLs on your Vonage app."),
            ("Attach numbers", "Map inbound or outbound numbers to campaigns."),
            ("Validate SIP", "Optional trunk testing before production traffic."),
        ],
        "hub_desc": "Voice API platform for inbound, outbound, and SIP connectivity worldwide.",
        "hub_points": ["Inbound and outbound parity", "SIP interconnect options", "Enterprise support tiers"],
        "hub_badge": "Global CPaaS",
    },
    {
        "slug": "exotel",
        "name": "Exotel",
        "region": "India · APAC",
        "tag": "India · APAC",
        "logo": '<img src="../../assets/logos/exotel.png" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="../../assets/logos/exotel.png" alt="" width="32" height="32" loading="lazy" />',
        "title": "Exotel — EMAAVY",
        "h1": "Exotel",
        "meta": "Exotel and EMAAVY — India-focused cloud telephony with IVR, call tracking, and TRAI-aligned AI voice operations.",
        "lead": "Exotel is India's leading cloud telephony platform for virtual numbers, IVR, and call analytics — now connected to EMAAVY's multilingual AI agent layer for regulated domestic programs.",
        "stats": [("India", "Primary market"), ("IVR + API", "Stack"), ("TRAI", "Aligned ops")],
        "about": [
            "Exotel provides virtual numbers, click-to-call, IVR studio, and call tracking APIs used by thousands of Indian enterprises. Compliance, domestic routing, and familiar ops tooling make it the default for India-first voice.",
            "EMAAVY preserves Exotel call flows while replacing or augmenting human agents with AI — sentiment, intent, and dispositions still sync to CRM in real time.",
        ],
        "emaavy": [
            ("Domestic outbound", "High-volume Hindi and English campaigns with local caller ID."),
            ("IVR + AI", "Exotel IVR can hand off to EMAAVY agents on intent match."),
            ("Call tracking", "Marketing attribution plus conversational intelligence in one view."),
            ("Compliance", "Recording and DND-aware dialing governed by EMAAVY policies."),
        ],
        "features": [
            ("Virtual numbers", "Landline and mobile numbers across India."),
            ("IVR designer", "Visual flows before AI agent engagement."),
            ("Call analytics", "Duration, status, and agent performance metrics."),
            ("API dialer", "Programmatic outbound for sales and support."),
            ("Call recording", "On-demand and always-on recording modes."),
            ("CRM integrations", "Native connectors plus EMAAVY webhook enrichment."),
        ],
        "uses": [
            ("Indian BPOs", "QA automation on Exotel-backed call centers."),
            ("D2C brands", "Order confirmation and NPS calls at scale."),
            ("Fintech", "KYC reminders and collections with regional languages."),
        ],
        "setup": [
            ("Link Exotel account", "API key and subdomain in EMAAVY settings."),
            ("Map ExoPhones", "Assign virtual numbers to campaigns."),
            ("Configure passthru", "EMAAVY registers voice URLs on your Exotel applet."),
            ("Pilot in Hindi", "Test one language variant before full rollout."),
        ],
        "hub_desc": "India-focused cloud telephony with IVR, call tracking, and compliance for domestic operations.",
        "hub_points": ["IVR and call tracking", "Domestic compliance workflows", "High-volume Indian outbound"],
        "hub_badge": "India · APAC",
    },
    {
        "slug": "knowlarity",
        "name": "Knowlarity",
        "region": "India · APAC",
        "tag": "Cloud PBX",
        "logo": '<img src="../../assets/logos/knowlarity.png" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="../../assets/logos/knowlarity.png" alt="" width="32" height="32" loading="lazy" />',
        "title": "Knowlarity — EMAAVY",
        "h1": "Knowlarity",
        "meta": "Knowlarity cloud telephony with EMAAVY — virtual numbers, cloud PBX, and AI voice for high-volume Indian operations.",
        "lead": "Knowlarity (Gupshup) delivers virtual business numbers, cloud PBX, and call distribution for Indian enterprises — integrated with EMAAVY so AI agents inherit your existing number strategy.",
        "stats": [("Cloud PBX", "Platform"), ("India", "Scale"), ("Virtual nums", "Inventory")],
        "about": [
            "Knowlarity powers click-to-call, toll-free lines, and cloud PBX features for sales and support teams across India. Operations teams value its dashboards and number management for high-volume dialing.",
            "EMAAVY connects to Knowlarity APIs so AI agents answer or place calls on the same virtual numbers your customers already recognize — no forced migration to a new carrier.",
        ],
        "emaavy": [
            ("PBX + AI", "Route extensions or departments to AI agents during peak load."),
            ("Campaign dialers", "Outbound programs with Knowlarity CLI and EMAAVY scripting."),
            ("Supervisor tools", "Live monitoring with Knowlarity metrics plus EMAAVY scores."),
            ("Regional languages", "Agents in Hindi, Tamil, and more on domestic routes."),
        ],
        "features": [
            ("Virtual numbers", "Business lines with IVR and call routing."),
            ("Cloud PBX", "Extensions, queues, and business-hour rules."),
            ("Click-to-call", "Website and app-initiated calls into AI queues."),
            ("Call recording", "Monitor and coach at scale."),
            ("Analytics dashboard", "Ops visibility before and after AI rollout."),
            ("API access", "Programmatic control for custom dialers."),
        ],
        "uses": [
            ("Inside sales", "Lead follow-up with AI and human hybrid teams."),
            ("Healthcare", "Appointment reminders on familiar local numbers."),
            ("Ed-tech", "Counseling and admission calls in regional languages."),
        ],
        "setup": [
            ("Authorize Knowlarity", "API credentials in EMAAVY integrations hub."),
            ("Sync numbers", "Import active virtual numbers per business unit."),
            ("Define routing", "Point hunt groups or IVR branches to EMAAVY agents."),
            ("Go live gradually", "Shift one queue at a time to measure CSAT impact."),
        ],
        "hub_desc": "Virtual numbers and cloud PBX for high-volume Indian voice operations.",
        "hub_points": ["Virtual number inventory", "Cloud PBX features", "Regional accent-friendly routing"],
        "hub_badge": "India · APAC",
    },
    {
        "slug": "telnyx",
        "name": "Telnyx",
        "region": "Private network",
        "tag": "Private network",
        "logo": '<img src="../../assets/logos/telnyx.svg" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="../../assets/logos/telnyx.svg" alt="" width="32" height="32" loading="lazy" />',
        "title": "Telnyx — EMAAVY",
        "h1": "Telnyx",
        "meta": "Telnyx programmable voice and EMAAVY — private network, media streaming, and low-latency AI agents.",
        "lead": "Telnyx operates a private global IP network for voice and messaging — when milliseconds matter, EMAAVY agents run on Telnyx media streams with programmable number APIs.",
        "stats": [("Private", "Network"), ("<300ms", "Media target"), ("Global", "Numbers")],
        "about": [
            "Telnyx gives developers direct access to carrier-grade voice on a private backbone, avoiding the public internet hops common in legacy CPaaS paths. Number search, provisioning, and TeXML or Call Control APIs are fully programmable.",
            "Latency-sensitive AI agents — rapid turn-taking, barge-in, and live coaching — benefit from Telnyx media streaming integrated with EMAAVY's orchestration layer.",
        ],
        "emaavy": [
            ("Low-latency agents", "Stream audio bidirectionally for natural conversation loops."),
            ("Global campaigns", "Provision numbers in target countries from one API."),
            ("SIP + API", "Hybrid enterprise setups without separate agent codebases."),
            ("Observability", "Telnyx call detail records enriched with EMAAVY intent scores."),
        ],
        "features": [
            ("Call Control API", "Fine-grained command set for live call manipulation."),
            ("Media streaming", "Real-time audio for STT and TTS pipelines."),
            ("Number APIs", "Search, order, and port numbers programmatically."),
            ("Private backbone", "Reduced jitter for voice AI workloads."),
            ("Elastic SIP", "Connect existing voice infrastructure."),
            ("Global coverage", "Reach customers in 100+ countries."),
        ],
        "uses": [
            ("Real-time sales", "Sub-second agent responses on competitive outbound."),
            ("US enterprise", "Programs requiring direct carrier relationships."),
            ("Voice AI labs", "Pilot cutting-edge agents before wide rollout."),
        ],
        "setup": [
            ("Add Telnyx API key", "Store credentials securely in EMAAVY."),
            ("Create connection", "Link Call Control or TeXML application to EMAAVY."),
            ("Enable streaming", "Turn on media stream for agent sessions."),
            ("Benchmark latency", "Compare MOS and turn times against other carriers."),
        ],
        "hub_desc": "Private global network with programmable voice and number provisioning for latency-sensitive agents.",
        "hub_points": ["Private IP backbone", "Programmable number APIs", "Low-latency media paths"],
        "hub_badge": "Private network",
    },
    {
        "slug": "bandwidth",
        "name": "Bandwidth",
        "region": "Direct carrier · US",
        "tag": "Enterprise SLA",
        "logo": '<img src="../../assets/logos/bandwidth.png" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="../../assets/logos/bandwidth.png" alt="" width="32" height="32" loading="lazy" />',
        "title": "Bandwidth — EMAAVY",
        "h1": "Bandwidth",
        "meta": "Bandwidth voice APIs and EMAAVY — direct-to-carrier reliability, E911 compliance, and enterprise SLAs for US-heavy programs.",
        "lead": "Bandwidth provides direct-to-carrier voice APIs with enterprise SLAs — for US-centric programs that demand control, compliance, and carrier-grade uptime, EMAAVY sits on top without compromising governance.",
        "stats": [("Direct", "Carrier"), ("Enterprise", "SLA"), ("E911", "Ready")],
        "about": [
            "Bandwidth owns and operates communications infrastructure rather than reselling third-party routes. Enterprises choose Bandwidth for 911 compliance, number porting, and contractual SLAs on mission-critical voice.",
            "EMAAVY integrates Bandwidth Voice API so AI agents inherit the same compliance posture — recording policies, emergency calling rules, and audit exports stay centralized.",
        ],
        "emaavy": [
            ("US outbound", "Collections, healthcare reminders, and sales on Bandwidth CLI."),
            ("Regulated industries", "Finance and healthcare with stricter recording rules."),
            ("Number porting", "Bring existing Bandwidth inventory into EMAAVY campaigns."),
            ("Enterprise support", "Joint escalation paths for carrier and platform issues."),
        ],
        "features": [
            ("Voice API", "REST control for outbound and inbound calls."),
            ("Direct carrier access", "Fewer hops than aggregated CPaaS paths."),
            ("Number management", "Order, port, and host numbers on Bandwidth."),
            ("Emergency calling", "E911 compliance for US deployments."),
            ("Recording APIs", "Configurable capture for QA and legal hold."),
            ("Enterprise SLAs", "Contractual uptime for critical programs."),
        ],
        "uses": [
            ("US healthcare", "Patient outreach with HIPAA-aware workflows."),
            ("Collections", "Regulated dialing with full audit trails."),
            ("Enterprise IT", "Standardize on Bandwidth while adopting AI agents."),
        ],
        "setup": [
            ("Connect Bandwidth account", "User ID and API token in EMAAVY."),
            ("Import numbers", "Sync existing Bandwidth numbers or order new."),
            ("Set applications", "EMAAVY configures voice and status callback URLs."),
            ("Compliance review", "Align recording and retention with legal stakeholders."),
        ],
        "hub_desc": "Direct-to-carrier voice APIs with enterprise-grade reliability and control for US-heavy programs.",
        "hub_points": ["Direct carrier access", "Enterprise SLAs", "E911 and compliance tooling"],
        "hub_badge": "Direct carrier",
    },
]

ALL_SLUGS = [p["slug"] for p in PARTNERS]


def partner_nav(current: str) -> str:
    links = []
    for p in PARTNERS:
        cls = ' class="is-current"' if p["slug"] == current else ""
        links.append(
            f'<a href="{p["slug"]}.html"{cls}>{p["name"]}</a>'
        )
    links.append('<a href="telephony.html">All telephony</a>')
    return "\n          ".join(links)


def render_partner(p: dict) -> str:
    stats = "".join(
        f'<div class="tel-partner-stat"><b>{a}</b><span>{b}</span></div>'
        for a, b in p["stats"]
    )
    about = "".join(f"<p>{para}</p>" for para in p["about"])
    benefits = "".join(
        f'<li><div><strong>{t}</strong><span>{d}</span></div></li>'
        for t, d in p["emaavy"]
    )
    features = "".join(
        f'<article class="tel-feature-card"><h3>{t}</h3><p>{d}</p></article>'
        for t, d in p["features"]
    )
    uses = "".join(
        f'<article class="tel-use-card"><h3>{t}</h3><p>{d}</p></article>'
        for t, d in p["uses"]
    )
    setup = "".join(
        f'<li><div><strong>{t}</strong><p>{d}</p></div></li>'
        for t, d in p["setup"]
    )
    route = f"integration-telephony-{p['slug']}"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{p['title']}</title>
  <meta name="description" content="{p['meta']}" />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="{p['title']}" />
  <meta property="og:description" content="{p['meta']}" />
  <meta property="og:type" content="website" />
{HEAD_COMMON}
  <link rel="stylesheet" href="../../assets/telephony-partner.css" />
</head>
<body data-base="../../" data-route="{route}">
  <div id="site-nav-root"></div>
  <main class="page-main tel-partner-page">
    <section class="tel-partner-hero">
      <div class="container tel-partner-hero-grid">
        <div class="tel-partner-hero-copy">
          <nav class="breadcrumb" aria-label="Breadcrumb">
            <a href="../../index.html">Home</a>
            <span aria-hidden="true"> / </span>
            <a href="../../index.html#integrations">Integrations</a>
            <span aria-hidden="true"> / </span>
            <a href="telephony.html">Telephony</a>
            <span aria-hidden="true"> / </span>
            <span>{p['name']}</span>
          </nav>
          <span class="tel-partner-kicker">Telephony · {p['tag']}</span>
          <h1>{p['h1']}</h1>
          <p class="tel-partner-lead">{p['lead']}</p>
          <div class="tel-partner-stats">{stats}</div>
          <div class="tel-partner-hero-actions">
            <a href="../../book-demo.html" class="btn-primary">Connect {p['name']}</a>
            <a href="telephony.html" class="btn-outline">All carriers</a>
          </div>
        </div>
        <aside class="tel-partner-hero-card" aria-label="{p['name']} overview">
          <div class="tel-partner-hero-logo">{p['logo']}</div>
          <span class="tel-partner-hero-region">{p['region']}</span>
          <p>Integrated with EMAAVY voice agents, campaigns, and live call intelligence.</p>
        </aside>
      </div>
    </section>

    <section class="tel-partner-section">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>What {p['name']} does</h2>
          <p>Understanding the carrier helps you choose the right voice path for each campaign.</p>
        </header>
        <div class="tel-partner-prose">{about}</div>
      </div>
    </section>

    <section class="tel-partner-section alt">
      <div class="container tel-partner-split">
        <header class="tel-partner-section-head">
          <h2>How EMAAVY uses {p['name']}</h2>
          <p>One integration layer — your agents, analytics, and CRM sync stay consistent regardless of carrier.</p>
        </header>
        <ul class="tel-partner-benefits">{benefits}</ul>
      </div>
    </section>

    <section class="tel-partner-section">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>Key capabilities</h2>
          <p>What teams typically configure when {p['name']} powers EMAAVY voice programs.</p>
        </header>
        <div class="tel-feature-grid">{features}</div>
      </div>
    </section>

    <section class="tel-partner-section alt">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>Ideal use cases</h2>
          <p>Where {p['name']} and EMAAVY deliver the strongest combined outcomes.</p>
        </header>
        <div class="tel-use-grid">{uses}</div>
      </div>
    </section>

    <section class="tel-partner-section">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>Getting connected</h2>
          <p>A typical rollout path from credentials to production traffic.</p>
        </header>
        <ol class="tel-setup-steps">{setup}</ol>
      </div>
    </section>

    <section class="tel-partner-section alt">
      <div class="container">
        <header class="tel-partner-section-head">
          <h2>Explore other carriers</h2>
          <p>EMAAVY unifies every partner below — mix carriers by region or campaign without rebuilding agents.</p>
        </header>
        <nav class="tel-partner-nav-strip" aria-label="Telephony partners">
          {partner_nav(p['slug'])}
        </nav>
      </div>
    </section>

    <section class="tel-partner-cta">
      <div class="container">
        <h2>Ready to connect {p['name']}?</h2>
        <p>Book a walkthrough — we will map numbers, routing, and your first AI campaign on a live call.</p>
        <div class="cta-row">
          <a href="../../book-demo.html" class="btn-primary">Book a demo</a>
          <a href="telephony.html" class="btn-outline">Telephony overview</a>
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


def card_html(p: dict) -> str:
    points = "".join(f"<li>{x}</li>" for x in p["hub_points"])
    featured = " tel-partner-card--native" if p.get("featured") else ""
    cta = "Explore integration →" if not p.get("featured") else "View full integration →"
    badge = f'<span class="tel-partner-badge">{p["hub_badge"]}</span>'
    return f"""          <a href="{p['slug']}.html" id="{p['slug']}" class="tel-partner-card{featured}">
            <div class="tel-partner-card-top">
              <div class="tel-partner-card-logo">{p['logo_sm']}</div>
              {badge}
            </div>
            <h3>{p['name']}</h3>
            <p class="tel-partner-card-desc">{p['hub_desc']}</p>
            <ul class="tel-partner-card-points">{points}</ul>
            <span class="tel-partner-card-cta">{cta}</span>
          </a>"""


def render_hub() -> str:
    cards = "\n".join(card_html(p) for p in PARTNERS)
    jumps = " ".join(
        f'<a href="#{p["slug"]}">{p["name"]}</a>' for p in PARTNERS
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Telephony — EMAAVY</title>
  <meta name="description" content="EMAAVY telephony — enterprise voice infrastructure for AI agents. CPaaS, SIP, PSTN, global carriers, and live call lifecycle." />
  <meta name="robots" content="index, follow" />
  <meta property="og:title" content="Telephony — EMAAVY" />
  <meta property="og:description" content="Connect EMAAVY to Vobiz, Twilio, and global carriers. Voice infrastructure built for AI agents at scale." />
  <meta property="og:type" content="website" />
{HEAD_COMMON}
  <link rel="stylesheet" href="../../assets/telephony-hub.css" />
</head>
<body data-base="../../" data-route="integration-telephony">
  <div id="site-nav-root"></div>
  <main class="page-main telephony-page">
    <section class="page-hero telephony-hero">
      <div class="container">
        <nav class="breadcrumb" aria-label="Breadcrumb">
          <a href="../../index.html">Home</a>
          <span aria-hidden="true"> / </span>
          <a href="../../index.html#integrations">Integrations</a>
          <span aria-hidden="true"> / </span>
          <span>Telephony</span>
        </nav>
        <span class="page-kicker">Foundation layer · Telephony</span>
        <h1>Enterprise voice infrastructure for AI agents</h1>
        <p class="telephony-hero-lead">EMAAVY is the connective tissue between your AI agents and the world's phone networks. Provision numbers globally, route via CPaaS or SIP, and capture audio from the first ring — with carrier-grade reliability your revenue teams can trust.</p>
        <div class="stat-row telephony-hero-stats">
          <div class="stat-box"><b>8</b><span>Carrier partners</span></div>
          <div class="stat-box"><b>180+</b><span>Countries</span></div>
          <div class="stat-box"><b>&lt;1s</b><span>Ring-to-answer</span></div>
          <div class="stat-box"><b>99.9%</b><span>Platform uptime</span></div>
        </div>
        <div class="capabilities-jump telephony-jump">
          <a href="#voice-layer">How EMAAVY handles voice</a>
          <a href="#partners">Carriers</a>
          <a href="#call-flow">Call flow</a>
          {jumps}
        </div>
      </div>
    </section>

    <section id="voice-layer" class="tel-hub-voice">
      <div class="container">
        <article class="tel-hub-voice-card">
          <div class="tel-hub-voice-meta">
            <span class="tel-hub-voice-num">Layer 01</span>
            <span class="tel-hub-voice-tag">EMAAVY · Telephony</span>
            <h2>How EMAAVY handles voice</h2>
            <p class="tel-hub-voice-lead">Every AI voice conversation starts with a reliable channel. EMAAVY normalizes telephony across providers so engineering configures once and operations scales everywhere.</p>
          </div>
          <div class="tel-hub-pill-grid">
            <div class="tel-hub-pill"><strong>CPaaS APIs</strong><span>Connect programmable voice platforms without rebuilding your agent stack.</span></div>
            <div class="tel-hub-pill"><strong>SIP trunks</strong><span>Bring your own carrier relationships while EMAAVY orchestrates media.</span></div>
            <div class="tel-hub-pill"><strong>PSTN reach</strong><span>Reach real phone numbers worldwide for outbound and inbound lines.</span></div>
            <div class="tel-hub-pill"><strong>First-ring capture</strong><span>Audio streams into transcription and reasoning from connect.</span></div>
          </div>
        </article>
      </div>
    </section>

    <section id="partners" class="tel-hub-partners page-section alt">
      <div class="container">
        <header class="tel-hub-partners-head">
          <h2>Carrier partners</h2>
          <p>Eight integrations today — each with a dedicated page covering what the provider does, how EMAAVY connects, and how to roll out.</p>
        </header>
        <div class="tel-partner-grid">
{cards}
        </div>
      </div>
    </section>

    <section id="call-flow" class="tel-hub-flow">
      <div class="container">
        <header class="tel-hub-flow-head">
          <h2>Live call flow</h2>
          <p>What happens on every call when EMAAVY is in the loop — regardless of which carrier you choose.</p>
        </header>
        <div class="tel-flow-track">
          <article class="tel-flow-step"><strong>Voice channel opens</strong><p>EMAAVY establishes the media path and prepares the agent session.</p></article>
          <article class="tel-flow-step"><strong>Carrier routes</strong><p>Your partner connects the callee with optimal routing rules.</p></article>
          <article class="tel-flow-step"><strong>Audio streams</strong><p>Real-time audio feeds transcription and LLM pipelines.</p></article>
          <article class="tel-flow-step"><strong>Agent responds</strong><p>The AI speaks, listens, and adapts within latency targets.</p></article>
          <article class="tel-flow-step"><strong>CRM updates</strong><p>Dispositions and scores land before hang-up.</p></article>
        </div>
      </div>
    </section>

    <section class="tel-hub-cta">
      <div class="container">
        <h2>Connect telephony to EMAAVY</h2>
        <p>See live routing, carrier setup, and agent handoff in a tailored demo.</p>
        <div class="cta-row">
          <a href="../../book-demo.html" class="btn-primary">Book a demo</a>
          <a href="index.html" class="btn-outline">All integrations</a>
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


def update_routes():
    path = ROOT / "assets" / "routes.js"
    text = path.read_text(encoding="utf-8")
    import re

    lines = [
        "      { id: 'telephony', label: 'Telephony layer', path: 'pages/integrations/telephony.html' },",
    ]
    for p in PARTNERS:
        lines.append(
            f"      {{ id: '{p['slug']}', label: '{p['name']}', path: 'pages/integrations/{p['slug']}.html' }},"
        )
    block = "    telephony: [\n" + "\n".join(lines) + "\n    ],"
    text = re.sub(r"    telephony: \[.*?\],", block, text, count=1, flags=re.DOTALL)
    path.write_text(text, encoding="utf-8")


def main():
    INT.mkdir(parents=True, exist_ok=True)
    (INT / "telephony.html").write_text(render_hub(), encoding="utf-8")
    for p in PARTNERS:
        (INT / f"{p['slug']}.html").write_text(render_partner(p), encoding="utf-8")
    update_routes()
    print(f"OK: telephony hub + {len(PARTNERS)} partner pages, routes.js updated")


if __name__ == "__main__":
    main()
