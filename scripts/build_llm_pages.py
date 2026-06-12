#!/usr/bin/env python3
"""Generate LLM hub + per-model integration pages."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from integration_logos import apply_logos_all
from integration_pages_common import ensure_uses, render_hub, render_partner

ROOT = Path(__file__).resolve().parents[1]
INT = ROOT / "pages" / "integrations"

MODELS = [
    {
        "slug": "openai",
        "name": "OpenAI GPT",
        "short": "OpenAI",
        "region": "Flagship reasoning",
        "tag": "Flagship",
        "logo": '<img src="https://cdn.worldvectorlogo.com/logos/openai-2.svg" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="https://cdn.worldvectorlogo.com/logos/openai-2.svg" alt="" width="32" height="32" loading="lazy" />',
        "title": "OpenAI GPT — EMAAVY",
        "h1": "OpenAI GPT",
        "meta": "Connect OpenAI GPT with EMAAVY — flagship reasoning for sales flows, objection handling, and structured extraction from live calls.",
        "lead": "OpenAI's GPT family delivers the deepest reasoning available for voice agents — multi-step objection handling, dynamic scripts, and reliable JSON extraction when every turn shapes revenue.",
        "stats": [("128K", "Context window"), ("Top tier", "Reasoning"), ("Per-agent", "Routing")],
        "about": [
            "OpenAI builds frontier large language models used across enterprise copilots, support automation, and sales enablement. GPT models excel at following complex instructions, maintaining conversational coherence over long calls, and producing structured outputs for CRM systems.",
            "Teams choose OpenAI when calls involve high-value deals, technical products, or multi-objection sequences where lighter models lose thread. API access supports streaming for low-latency voice loops and function calling for live tool use during calls.",
        ],
        "emaavy": [
            ("Flagship agent brain", "Assign GPT-5.x class models to closing agents and enterprise outbound programs by default."),
            ("Structured dispositions", "Extract JSON fields — budget, timeline, objections — straight from live transcripts."),
            ("Mid-call escalation", "Start on a fast model for greeting; escalate to GPT when intent complexity spikes."),
            ("Cost governance", "Cap tokens per campaign while keeping premium models on high-intent segments only."),
        ],
        "features": [
            ("Multi-step reasoning", "Handle nested objections without losing campaign context."),
            ("Function calling", "Book meetings, query knowledge bases, and update CRM mid-call."),
            ("Streaming responses", "Token streams feed TTS for natural voice pacing."),
            ("JSON mode", "Reliable structured outputs for scoring and disposition codes."),
            ("Long context", "Full call history plus knowledge snippets in one prompt."),
            ("Fine-tuning ready", "Optional custom models for brand tone and compliance phrasing."),
        ],
        "uses": [
            ("Enterprise sales", "Complex B2B cycles with technical discovery and legal hurdles."),
            ("High-ACV outbound", "Agents that must reason before offering discounts or trials."),
            ("Compliance review", "Calls where nuanced language and audit trails matter."),
        ],
        "setup": [
            ("Add OpenAI API key", "Store organization keys in EMAAVY with role-based access."),
            ("Pick default models", "Map GPT variants per agent type — closer vs. support vs. survey."),
            ("Define extraction schemas", "Configure JSON fields synced to Salesforce or HubSpot."),
            ("Pilot on one campaign", "Compare conversion and handle time against your baseline model."),
        ],
        "hub_desc": "Flagship reasoning for complex sales flows, multi-step objection handling, and structured data extraction.",
        "hub_points": ["Multi-step objection handling", "Structured JSON extraction", "Dynamic script adaptation"],
        "hub_badge": "Flagship",
    },
    {
        "slug": "claude",
        "name": "Claude",
        "short": "Claude",
        "region": "Enterprise · Anthropic",
        "tag": "Enterprise",
        "logo": '<img src="https://cdn.simpleicons.org/anthropic/191919" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="https://cdn.simpleicons.org/anthropic/191919" alt="" width="32" height="32" loading="lazy" />',
        "title": "Claude — EMAAVY",
        "h1": "Claude",
        "meta": "Anthropic Claude and EMAAVY — nuanced comprehension for compliance-sensitive and high-empathy voice programs.",
        "lead": "Claude Opus, Sonnet, and Haiku give EMAAVY teams a spectrum from maximum comprehension to cost-efficient turns — ideal when tone, policy, and long-context memory define call quality.",
        "stats": [("200K", "Context (Opus)"), ("3 tiers", "Opus · Sonnet · Haiku"), ("Enterprise", "Ready")],
        "about": [
            "Anthropic's Claude models are known for careful instruction following, reduced hallucination risk on policy-heavy topics, and strong performance on long documents. Enterprises in finance, healthcare, and regulated BPOs often standardize on Claude for customer-facing AI.",
            "The model family lets you pair Haiku-class speed for intent classification with Sonnet or Opus for negotiation and escalation — all through the same EMAAVY agent configuration layer.",
        ],
        "emaavy": [
            ("Compliance-first tone", "Claude excels on scripts with legal disclaimers and sensitive data handling."),
            ("Long-call memory", "Maintain context across 30+ minute support or onboarding sessions."),
            ("Tiered routing", "Route simple FAQs to Haiku; escalate to Opus for dispute resolution."),
            ("Human handoff briefs", "Generate supervisor summaries with cited transcript spans."),
        ],
        "features": [
            ("Opus depth", "Maximum reasoning for escalations and executive-facing calls."),
            ("Sonnet balance", "Default workhorse for sales and support agents at scale."),
            ("Haiku speed", "Sub-second classifications and slot-filling during live audio."),
            ("Document grounding", "Inject policy PDFs and playbooks into the prompt stack."),
            ("Consistent voice", "Stable personality across marathon conversations."),
            ("Safety alignment", "Built-in refusals align with enterprise acceptable-use policies."),
        ],
        "uses": [
            ("Regulated industries", "Banking, insurance, and healthcare voice programs."),
            ("Empathy-heavy support", "Billing disputes, cancellations saves, and VIP care."),
            ("Long-form discovery", "Calls that require many qualifying questions before close."),
        ],
        "setup": [
            ("Connect Anthropic API", "Add keys and set allowed model IDs per environment."),
            ("Map tiers to intents", "Define when EMAAVY upgrades from Haiku to Sonnet or Opus."),
            ("Upload playbooks", "Attach policy docs agents may cite during calls."),
            ("Review sample calls", "QA team validates tone before full traffic migration."),
        ],
        "hub_desc": "Best-in-class comprehension for nuanced, compliance-sensitive, and high-empathy conversations.",
        "hub_points": ["Opus · Sonnet · Haiku tiers", "Long-context call memory", "Policy-grounded responses"],
        "hub_badge": "Enterprise",
    },
    {
        "slug": "gemini",
        "name": "Gemini",
        "short": "Gemini",
        "region": "Google · Real-time",
        "tag": "Real-time",
        "logo": '<img src="https://cdn.simpleicons.org/google/4285F4" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="https://cdn.simpleicons.org/google/4285F4" alt="" width="32" height="32" loading="lazy" />',
        "title": "Gemini — EMAAVY",
        "h1": "Gemini Flash",
        "meta": "Google Gemini and EMAAVY — ultra-fast inference for live intent detection and real-time voice agent loops.",
        "lead": "Gemini Flash brings Google-scale infrastructure and millisecond-class inference to EMAAVY — perfect for intent detection, slot filling, and agent replies when latency beats raw reasoning depth.",
        "stats": [("Flash", "Low latency"), ("Multimodal", "Ready"), ("Google", "Cloud")],
        "about": [
            "Google Gemini is a family of multimodal models spanning ultra-fast Flash variants to larger Pro tiers. Flash models are optimized for high-throughput, low-latency workloads — exactly the profile live voice agents need on every conversational turn.",
            "Organizations already on Google Cloud can keep billing, VPC, and IAM patterns while EMAAVY orchestrates which Gemini variant handles classification versus response generation per call segment.",
        ],
        "emaavy": [
            ("Live intent scoring", "Classify buyer intent on every utterance without blocking TTS."),
            ("Flash for loops", "Default Flash models on high-QPS outbound campaigns."),
            ("Pro on escalation", "Swap to heavier Gemini when scripts require deeper reasoning."),
            ("Workspace synergy", "Optional hooks for Calendar, Docs, and internal knowledge bases."),
        ],
        "features": [
            ("Gemini Flash", "Optimized for real-time voice turn latency."),
            ("Intent classifiers", "Parallel scoring pipelines during active calls."),
            ("Multimodal future", "Room for visual context in advanced agent flows."),
            ("Google Cloud IAM", "Enterprise security and region pinning."),
            ("Cost efficiency", "Lower per-token cost on classification-heavy programs."),
            ("Streaming API", "Token streams aligned with EMAAVY voice pacing."),
        ],
        "uses": [
            ("High-QPS outbound", "Dialer campaigns needing fast turn-taking."),
            ("Intent routing", "Pre-qualify leads before expensive flagship model time."),
            ("Google-native stacks", "Teams standardized on GCP and Workspace."),
        ],
        "setup": [
            ("Enable Gemini API", "Connect Google Cloud project and API credentials."),
            ("Set Flash defaults", "Assign Flash to greeting and qualification agents."),
            ("Define escalation rules", "Promote to Pro/Ultra analogs on intent triggers."),
            ("Load test latency", "Benchmark turn time against SLA targets."),
        ],
        "hub_desc": "Ultra-fast inference for real-time intent detection and responsive voice agent loops.",
        "hub_points": ["Sub-second classification", "Flash-optimized voice turns", "GCP-native security"],
        "hub_badge": "Real-time",
    },
    {
        "slug": "qwen",
        "name": "Qwen",
        "short": "Qwen",
        "region": "Multilingual · APAC",
        "tag": "Multilingual",
        "logo": '<span class="brand-mark">QW</span>',
        "logo_sm": '<span class="brand-mark">QW</span>',
        "title": "Qwen — EMAAVY",
        "h1": "Qwen 3.6",
        "meta": "Qwen and EMAAVY — cost-efficient multilingual models for Hinglish, regional Indian dialects, and APAC voice programs.",
        "lead": "Qwen delivers strong multilingual performance at efficient price points — EMAAVY routes Hinglish, Tamil, Telugu, and other regional programs to Qwen when global models miss nuance or economics.",
        "stats": [("22+", "Language fit"), ("Cost", "Efficient"), ("Hinglish", "Native feel")],
        "about": [
            "Qwen is Alibaba Cloud's open-model family widely adopted for multilingual chat, code, and voice-agent backends across APAC. Recent versions improve Indic language handling, code-mixed Hinglish, and dialect robustness compared with generic Western-trained models.",
            "For Indian outbound and support at millions of minutes per month, Qwen often becomes the default reasoning layer — with EMAAVY handling telephony, STT, and CRM sync around it.",
        ],
        "emaavy": [
            ("Regional campaigns", "Dedicated Qwen agents per language and script variant."),
            ("Cost control", "Run qualification on Qwen; reserve GPT/Claude for closing tiers."),
            ("Dialect tuning", "Prompt packs tuned for city-specific vocabulary and honorifics."),
            ("Unified analytics", "Same intent and sentiment layer regardless of model vendor."),
        ],
        "features": [
            ("Hinglish fluency", "Natural code-mixed sales and support dialogue."),
            ("Regional languages", "Hindi, Tamil, Telugu, Bengali, and more."),
            ("Efficient tokens", "Lower cost per minute on scale outbound."),
            ("Open-weight options", "Deploy variants matching data residency needs."),
            ("Structured output", "JSON dispositions for Indian CRM ecosystems."),
            ("Fast inference", "Suitable for sub-2s voice turn targets on optimized hardware."),
        ],
        "uses": [
            ("India outbound", "D2C, fintech, and ed-tech dial programs."),
            ("Multilingual BPO", "Single platform across language queues."),
            ("Cost-sensitive pilots", "Prove ROI before upgrading select agents to flagship models."),
        ],
        "setup": [
            ("Connect Qwen endpoint", "API keys or self-hosted gateway in EMAAVY."),
            ("Language per agent", "Bind Qwen variants to agent language profiles."),
            ("Localize scripts", "Upload region-specific objection handlers."),
            ("A/B against GPT", "Measure conversion and CSAT by language cohort."),
        ],
        "hub_desc": "Cost-efficient multilingual model optimized for Hinglish and regional Indian dialects.",
        "hub_points": ["Hinglish and Indic languages", "Efficient at high minute volumes", "Regional script libraries"],
        "hub_badge": "Multilingual",
    },
    {
        "slug": "grok",
        "name": "Grok",
        "short": "Grok",
        "region": "xAI · Experimental",
        "tag": "Experimental",
        "logo": '<span class="brand-mark">GX</span>',
        "logo_sm": '<span class="brand-mark">GX</span>',
        "title": "Grok — EMAAVY",
        "h1": "Grok",
        "meta": "Grok and EMAAVY — experimental reasoning for creative outbound scripts and dynamic rebuttals.",
        "lead": "Grok from xAI offers a distinct reasoning style — bold, adaptive copy and dynamic rebuttals. EMAAVY lets innovation teams pilot Grok on select campaigns without destabilizing production defaults.",
        "stats": [("Pilot", "Programs"), ("Dynamic", "Scripts"), ("xAI", "Stack")],
        "about": [
            "Grok is xAI's conversational model family positioned for real-time knowledge and creative generation. While not every enterprise standardizes on Grok for regulated support, it shines in experimental outbound where fresh hooks and rapid rebuttal invention matter.",
            "EMAAVY treats Grok as a first-class routing target — sandbox agents, champion-challenger tests, and creative campaign variants can call Grok while core support lines stay on Claude or GPT.",
        ],
        "emaavy": [
            ("Creative outbound", "Generate variant openings and rebuttals per industry vertical."),
            ("Champion-challenger", "Run Grok on 5–10% traffic with automatic KPI comparison."),
            ("Sandbox agents", "Isolate experimental prompts from production knowledge bases."),
            ("Fast iteration", "Swap Grok prompts daily without redeploying telephony."),
        ],
        "features": [
            ("Dynamic scripts", "Less rigid templates; more adaptive banter within guardrails."),
            ("Rebuttal invention", "Respond to uncommon objections with novel angles."),
            ("Pilot isolation", "Separate API quotas and monitoring per experiment."),
            ("Real-time tone", "Conversational style suited for challenger brands."),
            ("Guardrail layer", "EMAAVY policy filters still apply before speech."),
            ("Easy rollback", "One-click revert to GPT/Claude defaults per agent."),
        ],
        "uses": [
            ("PLG outbound", "Startup campaigns testing edgy positioning."),
            ("Challenger brands", "Categories where differentiation beats safe scripts."),
            ("Innovation labs", "Internal teams exploring next-gen agent personalities."),
        ],
        "setup": [
            ("Enable Grok API", "Add xAI credentials to a sandbox workspace."),
            ("Clone production agent", "Fork an agent profile for Grok-only traffic."),
            ("Set traffic cap", "Limit dial percentage until KPIs validate."),
            ("Review compliance", "Legal approves sample calls before scale."),
        ],
        "hub_desc": "Experimental reasoning for creative outbound scripts and dynamic rebuttals on pilot campaigns.",
        "hub_points": ["Creative script variants", "Champion-challenger testing", "Sandboxed from production"],
        "hub_badge": "Experimental",
    },
]

USE_EXTRAS = [
    ("Lead qualification", "Score and disposition prospects during live conversations."),
    ("Automated follow-ups", "Post-call nurture with model-backed personalization."),
    ("Multi-agent operations", "Standardize routing while scaling AI agent programs."),
]

HUB_CFG = {
    "route": "integration-llms",
    "title": "LLMs — EMAAVY",
    "meta": "EMAAVY routes flagship reasoning, real-time inference, and multilingual models per agent, per intent, or mid-call — without losing context.",
    "og_title": "LLMs — EMAAVY",
    "og_description": "Connect GPT, Claude, Gemini, Qwen, and Grok to EMAAVY voice agents with per-call orchestration.",
    "breadcrumb": "LLMs",
    "kicker": "Reasoning layer · LLMs",
    "h1": "The reasoning engine behind every conversation",
    "lead": "EMAAVY routes flagship reasoning, real-time inference, and multilingual models per agent, per intent, or mid-call — without losing context. Engineering sets defaults once; operations swaps models by campaign without rebuilding agents.",
    "stats": [("5", "Model families"), ("128K+", "Max context"), ("Per-turn", "Routing")],
    "anchor_jumps": [
        ("reasoning-layer", "How EMAAVY orchestrates"),
        ("models", "Model partners"),
        ("orchestration", "Orchestration flow"),
    ],
    "layer_id": "reasoning-layer",
    "layer_num": "Layer 02",
    "layer_tag": "EMAAVY · LLMs",
    "layer_h2": "How EMAAVY orchestrates LLMs",
    "layer_lead": "One conversation layer, many models. Pick flagship reasoning for closes, flash models for intent, and regional models for Hinglish — all on the same agent definitions.",
    "pills": [
        ("Per-agent routing", "Assign GPT, Claude, Gemini, Qwen, or Grok per workflow."),
        ("Mid-call switching", "Escalate to a heavier model when complexity spikes."),
        ("Structured extraction", "JSON dispositions and scores from live transcripts."),
        ("Cost control", "Flash for classification; flagship models for closing."),
    ],
    "partners_id": "models",
    "partners_h2": "Model partners",
    "partners_desc": "Five families integrated today — each with a dedicated page on capabilities, EMAAVY orchestration, and rollout steps.",
    "flow_id": "orchestration",
    "flow_h2": "Live orchestration flow",
    "flow_desc": "How every conversational turn moves through EMAAVY — regardless of which LLM you select.",
    "flow_steps": [
        ("Transcript in", "Live speech becomes text in the reasoning pipeline."),
        ("Model selected", "EMAAVY picks the model for intent, language, and SLA."),
        ("Intent scored", "Buyer signals update on every turn."),
        ("Data extracted", "Structured fields map to CRM and campaigns."),
        ("Agent speaks", "TTS delivers the model-backed reply."),
    ],
    "cta_h2": "Connect LLMs to EMAAVY",
    "cta_desc": "See live model routing, extraction, and agent handoff in a tailored demo.",
}

HUB_FILE = "llms.html"
HUB_LABEL = "All models"
HUB_BREADCRUMB = "LLMs"
HUB_CTA = "LLM overview"


def prepare():
    for m in MODELS:
        m.pop("featured", None)
        ensure_uses(m, USE_EXTRAS)
    apply_logos_all(MODELS)


def write_partner(m: dict) -> str:
    route = m.get("route", f"integration-{m['slug']}")
    return render_partner(
        m,
        partners=MODELS,
        route=route,
        segment_kicker=f"LLMs · {m['tag']}",
        hub_file=HUB_FILE,
        hub_label=HUB_LABEL,
        hub_breadcrumb=HUB_BREADCRUMB,
        hub_cta_label=HUB_CTA,
        nav_label_key="short",
        connect_name_key="short",
        explore_title="Explore other models",
        explore_desc="Mix providers by campaign — EMAAVY keeps transcripts, scoring, and CRM sync consistent.",
        nav_aria="LLM partners",
        overview_fit="your reasoning layer",
        cta_desc="Book a walkthrough — we will map model routing, extraction schemas, and a live agent demo.",
        segment_type="llm",
        hub_label_key="short",
    )



def update_routes():
    path = ROOT / "assets" / "routes.js"
    text = path.read_text(encoding="utf-8")
    lines = ["      { id: 'llm', label: 'LLM layer', path: 'pages/integrations/llms.html' },"]
    for m in MODELS:
        label = m["name"]
        lines.append(
            f"      {{ id: '{m['slug']}', label: '{label}', path: 'pages/integrations/{m['slug']}.html' }},"
        )
    block = "    llm: [\n" + "\n".join(lines) + "\n    ],"
    text = re.sub(r"    llm: \[.*?\],", block, text, count=1, flags=re.DOTALL)
    path.write_text(text, encoding="utf-8")


def main():
    prepare()
    INT.mkdir(parents=True, exist_ok=True)
    (INT / "llms.html").write_text(
        render_hub(HUB_CFG, MODELS, jump_label_key="short", hub_tile_label_key="short"), encoding="utf-8"
    )
    for m in MODELS:
        (INT / f"{m['slug']}.html").write_text(write_partner(m), encoding="utf-8")
    update_routes()
    print(f"OK: llms.html + {len(MODELS)} partner pages, routes.js updated")


if __name__ == "__main__":
    main()
