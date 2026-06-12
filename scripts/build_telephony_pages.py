#!/usr/bin/env python3
"""Generate telephony hub + per-partner integration pages."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from integration_logos import apply_logos_all
from integration_pages_common import ensure_uses, render_hub, render_partner

ROOT = Path(__file__).resolve().parents[1]
INT = ROOT / "pages" / "integrations"

PARTNERS = [
    {
        "slug": "vobiz",
        "name": "Vobiz",
        "region": "Global · CPaaS",
        "tag": "Global CPaaS",
        "logo": '<img src="../../assets/logos/vobiz.svg" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="../../assets/logos/vobiz.svg" alt="" width="32" height="32" loading="lazy" />',
        "title": "Vobiz — EMAAVY",
        "h1": "Vobiz",
        "meta": "Connect Vobiz with EMAAVY — global DIDs, intelligent routing, and sub-second connect times for AI voice programs.",
        "lead": "Vobiz provides programmable voice infrastructure with global number provisioning, intelligent routing, and real-time call control — integrated with EMAAVY for AI agents, campaigns, and live call intelligence.",
        "stats": [("99.2%", "Connect rate"), ("<1s", "Ring-to-answer"), ("Global", "DID pools")],
        "about": [
            "Vobiz offers programmable voice infrastructure with global number provisioning, intelligent routing, and real-time call control APIs. Teams use Vobiz when they need predictable connect rates and sub-second media setup for high-volume AI dialers.",
            "Through EMAAVY, Vobiz sessions feed the same transcription, reasoning, and CRM sync layer as every other telephony partner — so operations can standardize on one agent stack regardless of carrier.",
        ],
        "emaavy": [
            ("Unified media path", "EMAAVY opens the voice channel and streams audio into STT and LLM pipelines from the first ring."),
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
            ("Outbound campaigns", "High-volume registration, renewal, and sales programs with AI agents."),
            ("Customer support", "Inbound lines with regional numbers and language-specific agents."),
            ("Lead qualification", "Screen and route prospects before human handoff."),
            ("Appointment booking", "Confirm slots and send calendar invites during live calls."),
            ("Automated follow-ups", "Post-call reminders and nurture sequences without manual dialing."),
            ("Multi-agent operations", "Run parallel campaigns across regions from one workspace."),
        ],
        "setup": [
            ("Connect Vobiz credentials", "Add API keys and account identifiers in the EMAAVY integrations console."),
            ("Provision numbers", "Select DIDs or pools mapped to each campaign or agent group."),
            ("Map webhooks", "EMAAVY registers call-status endpoints on your Vobiz application automatically."),
            ("Assign agents", "Link voice agents to campaigns — test with a sandbox call before go-live."),
        ],
        "hub_desc": "Global DIDs, intelligent routing, and sub-second connect times for AI voice programs at scale.",
        "hub_points": ["Global DID provisioning and number pools", "Campaign-level routing rules", "Real-time call status webhooks"],
        "hub_badge": "Global CPaaS",
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
            ("Sales calls", "Multi-region outbound with localized numbers and compliance tooling."),
            ("Customer support", "Blend human queues with AI triage on shared Twilio infrastructure."),
            ("Lead qualification", "Screen inbound and outbound prospects before human handoff."),
            ("Appointment booking", "Schedule meetings and send confirmations during live calls."),
            ("Outbound campaigns", "Burst dial programs with elastic Twilio capacity."),
            ("Multi-agent operations", "Run parallel agents across subaccounts from one EMAAVY workspace."),
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
            ("Customer support", "Inbound lines with cost-optimized international routing."),
            ("Lead qualification", "High-volume screening before sales team engagement."),
            ("Automated follow-ups", "Payment reminders and nurture calls at scale."),
            ("Multi-agent operations", "Regional campaigns with unified Plivo inventory."),
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
            ("Customer support", "Seasonal inbound spikes handled by AI agents."),
            ("Sales calls", "Outbound and blended programs on shared Vonage infrastructure."),
            ("Appointment booking", "Confirm slots with calendar sync during conversations."),
            ("Lead qualification", "Tier-1 screening before specialist handoff."),
            ("Multi-agent operations", "SIP and PSTN traffic through one agent orchestration layer."),
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
            ("Customer support", "QA automation on Exotel-backed call centers."),
            ("Outbound campaigns", "Order confirmation and NPS calls at scale."),
            ("Lead qualification", "KYC reminders and pre-sales screening in regional languages."),
            ("Appointment booking", "Healthcare and service scheduling on domestic numbers."),
            ("Automated follow-ups", "Collections and payment reminders with DND-aware dialing."),
            ("Multi-agent operations", "Hindi, English, and regional agents on shared Exotel routes."),
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
            ("Sales calls", "Lead follow-up with AI and human hybrid teams."),
            ("Appointment booking", "Healthcare and service reminders on familiar local numbers."),
            ("Customer support", "Inbound queues routed through cloud PBX to AI agents."),
            ("Outbound campaigns", "High-volume dial programs on virtual business numbers."),
            ("Lead qualification", "Counseling and admission screening in regional languages."),
            ("Multi-agent operations", "Department-based routing with shared Knowlarity inventory."),
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
            ("Sales calls", "Sub-second agent responses on competitive outbound."),
            ("Customer support", "Low-latency inbound with private network media paths."),
            ("Lead qualification", "Real-time screening with minimal conversational delay."),
            ("Outbound campaigns", "Global programs on programmable Telnyx numbers."),
            ("Automated follow-ups", "Post-call sequences with consistent media quality."),
            ("Multi-agent operations", "Pilot and production agents on shared Call Control apps."),
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
            ("Customer support", "Patient and member outreach with HIPAA-aware workflows."),
            ("Outbound campaigns", "Regulated collections dialing with full audit trails."),
            ("Appointment booking", "Healthcare scheduling with E911-compliant numbers."),
            ("Lead qualification", "Financial services screening with enterprise SLAs."),
            ("Automated follow-ups", "Payment and renewal reminders on direct carrier routes."),
            ("Multi-agent operations", "Standardize on Bandwidth while scaling AI agent programs."),
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


USE_EXTRAS = [
    ("Appointment booking", "Schedule and confirm calls on provisioned numbers."),
    ("Automated follow-ups", "Outbound reminders and callbacks at scale."),
    ("Multi-agent operations", "Standardize carriers while scaling AI programs."),
]

HUB_CFG = {
    "route": "integration-telephony",
    "title": "Telephony — EMAAVY",
    "meta": "EMAAVY telephony — enterprise voice infrastructure for AI agents. CPaaS, SIP, PSTN, global carriers, and live call lifecycle.",
    "og_title": "Telephony — EMAAVY",
    "og_description": "Connect EMAAVY to global carriers. Voice infrastructure built for AI agents at scale.",
    "breadcrumb": "Telephony",
    "kicker": "Foundation layer · Telephony",
    "h1": "Voice infrastructure for AI agents",
    "lead": "Connect AI agents to global phone networks through a single integration layer. Provision numbers, route via CPaaS or SIP, and capture audio from the first ring — with consistent reliability across every carrier.",
    "stats": [("8", "Carrier partners"), ("180+", "Countries"), ("<1s", "Ring-to-answer"), ("99.9%", "Platform uptime")],
    "anchor_jumps": [
        ("voice-layer", "How EMAAVY handles voice"),
        ("partners", "Carriers"),
        ("call-flow", "Call flow"),
    ],
    "layer_id": "voice-layer",
    "layer_num": "Layer 01",
    "layer_tag": "EMAAVY · Telephony",
    "layer_h2": "How EMAAVY handles voice",
    "layer_lead": "Every AI voice conversation starts with a reliable channel. EMAAVY normalizes telephony across providers so engineering configures once and operations scales everywhere.",
    "pills": [
        ("CPaaS APIs", "Connect programmable voice platforms without rebuilding your agent stack."),
        ("SIP trunks", "Bring your own carrier relationships while EMAAVY orchestrates media."),
        ("PSTN reach", "Reach real phone numbers worldwide for outbound and inbound lines."),
        ("First-ring capture", "Audio streams into transcription and reasoning from connect."),
    ],
    "partners_id": "partners",
    "partners_h2": "Carrier partners",
    "partners_desc": "Eight integrations today — each with a dedicated page.",
    "flow_id": "call-flow",
    "flow_h2": "Live call flow",
    "flow_desc": "How every call moves through EMAAVY once telephony connects.",
    "flow_steps": [
        ("Call initiated", "Outbound dial or inbound ring hits your configured numbers."),
        ("EMAAVY routes", "Carrier, region, and agent profile selected automatically."),
        ("Media streams", "Audio captured for STT and live intelligence."),
        ("Agent engages", "LLM and TTS layers respond in real time."),
        ("Call completes", "Dispositions, recordings, and automations finalize."),
    ],
    "cta_h2": "Connect telephony to EMAAVY",
    "cta_desc": "See live number provisioning, routing, and agent handoff in a tailored demo.",
}

HUB_FILE = "telephony.html"
HUB_LABEL = "All carriers"
HUB_BREADCRUMB = "Telephony"
HUB_CTA = "Telephony overview"


def prepare():
    for p in PARTNERS:
        ensure_uses(p, USE_EXTRAS)
    apply_logos_all(PARTNERS)


def write_partner(p: dict) -> str:
    route = f"integration-telephony-{p['slug']}"
    return render_partner(
        p,
        partners=PARTNERS,
        route=route,
        segment_kicker=f"Telephony · {p['tag']}",
        hub_file=HUB_FILE,
        hub_label=HUB_LABEL,
        hub_breadcrumb=HUB_BREADCRUMB,
        hub_cta_label=HUB_CTA,
        nav_label_key="name",
        connect_name_key="name",
        explore_title="Explore other carriers",
        explore_desc="EMAAVY unifies every partner below — mix carriers by region or campaign without rebuilding agents.",
        nav_aria="Telephony partners",
        overview_fit="your voice stack",
        cta_desc="Book a walkthrough — we will map numbers, routing, and your first AI campaign on a live call.",
        segment_type="telephony",
        hub_label_key="name",
    )


def update_routes():
    path = ROOT / "assets" / "routes.js"
    text = path.read_text(encoding="utf-8")
    lines = ["      { id: 'telephony', label: 'Telephony layer', path: 'pages/integrations/telephony.html' },"]
    for p in PARTNERS:
        lines.append(
            f"      {{ id: '{p['slug']}', label: '{p['name']}', path: 'pages/integrations/{p['slug']}.html' }},"
        )
    block = "    telephony: [\n" + "\n".join(lines) + "\n    ],"
    text = re.sub(r"    telephony: \[.*?\],", block, text, count=1, flags=re.DOTALL)
    path.write_text(text, encoding="utf-8")


def main():
    prepare()
    INT.mkdir(parents=True, exist_ok=True)
    (INT / "telephony.html").write_text(
        render_hub(HUB_CFG, PARTNERS, jump_label_key="name", hub_tile_label_key="name"), encoding="utf-8"
    )
    for p in PARTNERS:
        (INT / f"{p['slug']}.html").write_text(write_partner(p), encoding="utf-8")
    update_routes()
    print(f"OK: telephony hub + {len(PARTNERS)} partner pages, routes.js updated")


if __name__ == "__main__":
    main()
