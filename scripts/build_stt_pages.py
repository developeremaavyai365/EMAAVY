#!/usr/bin/env python3
"""Generate STT hub + per-provider integration pages."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from integration_logos import apply_logos_all
from integration_pages_common import ensure_uses, render_hub, render_partner

ROOT = Path(__file__).resolve().parents[1]
INT = ROOT / "pages" / "integrations"

PROVIDERS = [
    {
        "slug": "deepgram",
        "name": "Deepgram",
        "short": "Deepgram",
        "region": "Low latency · Global",
        "tag": "Low latency",
        "route": "integration-deepgram",
        "logo": '<img src="https://cdn.simpleicons.org/deepgram/13EF93" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="https://cdn.simpleicons.org/deepgram/13EF93" alt="" width="32" height="32" loading="lazy" />',
        "title": "Deepgram — EMAAVY",
        "h1": "Deepgram",
        "meta": "Deepgram and EMAAVY — sub-500ms streaming transcription with keyword boosting for live AI voice agents.",
        "lead": "Deepgram is the default STT engine for many EMAAVY programs — streaming Nova models, telephony-tuned accuracy, and keyword boosting so brand names and compliance phrases never get lost on live calls.",
        "stats": [("<500ms", "Streaming latency"), ("Nova", "Model family"), ("Keyword", "Boosting")],
        "about": [
            "Deepgram builds speech-to-text APIs optimized for real-time applications — contact centers, voice agents, and meeting intelligence. Streaming endpoints return partial transcripts as audio arrives, which is essential for sub-second agent loops.",
            "Telephony-specific models handle narrow-band audio, background noise, and accented English common on outbound dialers. Teams on EMAAVY typically route global English campaigns to Deepgram while keeping Indian languages on Sarvam or Gladia.",
        ],
        "emaavy": [
            ("Streaming from ring", "Transcripts begin when the call connects — not after hang-up."),
            ("Keyword boosting", "Inject product names, competitor terms, and compliance phrases per campaign."),
            ("Live intent feed", "Partial transcripts power LLM intent scoring on every turn."),
            ("Unified QA", "Supervisors read the same stream agents use for responses."),
        ],
        "features": [
            ("Streaming API", "WebSocket transcription with interim results."),
            ("Nova models", "Latest generation accuracy for voice agents."),
            ("Keyword boosting", "Custom vocabulary per brand or vertical."),
            ("Diarization options", "Speaker labels for coaching and compliance."),
            ("Multi-language", "Broad coverage for international outbound."),
            ("On-prem options", "Deployment patterns for data-sensitive enterprises."),
        ],
        "uses": [
            ("Global English outbound", "High-volume sales and renewal dialers."),
            ("Real-time agent assist", "Low-latency loops for conversational AI."),
            ("QA automation", "Word-level transcripts for scoring and coaching."),
        ],
        "setup": [
            ("Add Deepgram API key", "Store keys in EMAAVY integrations with environment separation."),
            ("Select Nova model", "Pick telephony vs. general model per campaign."),
            ("Upload keyword list", "Boost brand and compliance terms for the vertical."),
            ("Benchmark latency", "Validate turn time against your voice agent SLA."),
        ],
        "hub_desc": "Sub-500ms streaming transcription with industry-leading accuracy and keyword boosting.",
        "hub_points": ["Streaming real-time API", "Telephony-optimized models", "Custom vocabulary boosting"],
        "hub_badge": "Low latency",
    },
    {
        "slug": "sarvam",
        "name": "Sarvam AI",
        "short": "Sarvam",
        "region": "India · 22 languages",
        "tag": "India · 22 langs",
        "route": "integration-sarvam",
        "logo": '<img src="../../assets/logos/flash-bulbul.svg" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="../../assets/logos/flash-bulbul.svg" alt="" width="32" height="32" loading="lazy" />',
        "title": "Sarvam AI — EMAAVY",
        "h1": "Sarvam AI",
        "meta": "Sarvam AI STT and EMAAVY — native accuracy for Hindi, Tamil, Telugu, and 22 Indian languages on live voice programs.",
        "lead": "Sarvam AI is purpose-built for Indic speech — when international STT models stumble on Hinglish, city accents, or code-mixed dialogue, EMAAVY routes those campaigns to Sarvam by default.",
        "stats": [("22", "Indian languages"), ("Indic", "Optimized"), ("Live", "Streaming")],
        "about": [
            "Sarvam AI develops speech and language models focused on Indian markets — covering major regional languages and everyday Hinglish patterns that generic global engines mis-transcribe.",
            "For BPO, fintech, ed-tech, and D2C dialers operating at crore-scale minutes, Sarvam on EMAAVY often delivers the largest accuracy uplift versus Western-default STT.",
        ],
        "emaavy": [
            ("Language-aware routing", "Auto-select Sarvam when agent language is Hindi, Tamil, or siblings."),
            ("Dialect packs", "Campaign-level tuning for city and vertical vocabulary."),
            ("Same analytics layer", "Intent and sentiment scores use Sarvam text like any other engine."),
            ("Cost alignment", "Regional pricing models fit high-volume domestic programs."),
        ],
        "features": [
            ("22+ languages", "Major Indic languages natively supported."),
            ("Hinglish robustness", "Code-mixed speech on everyday calls."),
            ("Streaming STT", "Live feeds for voice agent loops."),
            ("Domain tuning", "Vertical vocab for banking, retail, and education."),
            ("Low WER", "Competitive error rates on Indian telephony audio."),
            ("API-first", "Drop into EMAAVY without custom media servers."),
        ],
        "uses": [
            ("India outbound", "Sales, verification, and collections in regional languages."),
            ("Multilingual BPO", "One platform across language queues."),
            ("Government & PSU", "Programs requiring domestic language accuracy."),
        ],
        "setup": [
            ("Connect Sarvam credentials", "API keys in EMAAVY integrations console."),
            ("Map languages", "Bind Sarvam to agent language profiles."),
            ("Test sample calls", "Compare WER against prior STT on recorded audio."),
            ("Roll out per queue", "Migrate one language cohort at a time."),
        ],
        "hub_desc": "Optimized for Hindi, Tamil, Telugu — 22 Indian languages with native telephony accuracy.",
        "hub_points": ["22 Indian languages", "Hinglish and dialect robustness", "Streaming for live agents"],
        "hub_badge": "India · 22 langs",
    },
    {
        "slug": "assemblyai",
        "name": "AssemblyAI",
        "short": "AssemblyAI",
        "region": "Real-time · Analytics",
        "tag": "Real-time",
        "route": "integration-assemblyai",
        "logo": '<img src="https://cdn.simpleicons.org/assemblyai/2545D0" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="https://cdn.simpleicons.org/assemblyai/2545D0" alt="" width="32" height="32" loading="lazy" />',
        "title": "AssemblyAI — EMAAVY",
        "h1": "AssemblyAI",
        "meta": "AssemblyAI and EMAAVY — real-time transcription with strong punctuation for live voice agents and analytics.",
        "lead": "AssemblyAI combines accurate streaming STT with rich audio intelligence features — punctuation, formatting, and optional classifiers — so EMAAVY transcripts are readable the moment supervisors glance at a live call.",
        "stats": [("Real-time", "Streaming"), ("Punctuation", "Auto"), ("Audio Intel", "Add-ons")],
        "about": [
            "AssemblyAI offers speech-to-text APIs used by product teams for meetings, media, and voice agents. The Universal streaming model targets low latency with strong formatting — commas and sentence boundaries matter when LLMs parse live text.",
            "Optional audio intelligence layers (topic detection, sentiment) can complement EMAAVY's own scoring or serve pilot programs before full LLM orchestration is enabled.",
        ],
        "emaavy": [
            ("Clean live text", "Formatted transcripts reduce LLM confusion on long utterances."),
            ("Streaming alignment", "Partial results sync with agent turn-taking logic."),
            ("Optional enrichments", "Layer AssemblyAI classifiers where campaigns need them."),
            ("Developer velocity", "Mature SDKs and docs for fast EMAAVY connector setup."),
        ],
        "features": [
            ("Universal streaming", "Low-latency model for voice agents."),
            ("Auto punctuation", "Readable transcripts without post-processing."),
            ("Custom spelling", "Vocabulary hints for brands and products."),
            ("Audio intelligence", "Optional topic and content safety signals."),
            ("Multi-channel", "Support for stereo and multi-party audio."),
            ("Secure API", "Enterprise auth and data handling options."),
        ],
        "uses": [
            ("Product-led voice pilots", "Teams already using AssemblyAI elsewhere."),
            ("Support automation", "Formatted text for knowledge-base retrieval."),
            ("Media-heavy verticals", "Programs needing optional content classifiers."),
        ],
        "setup": [
            ("Add AssemblyAI key", "Configure in EMAAVY per environment."),
            ("Enable streaming", "Point campaigns to Universal streaming endpoint."),
            ("Custom vocabulary", "Upload spelling hints for the vertical."),
            ("Validate formatting", "QA checks punctuation on sample calls."),
        ],
        "hub_desc": "Real-time transcription with strong punctuation and optional audio intelligence.",
        "hub_points": ["Universal streaming model", "Auto punctuation", "Custom spelling hints"],
        "hub_badge": "Real-time",
    },
    {
        "slug": "azure-stt",
        "name": "Azure Speech",
        "short": "Azure",
        "region": "Microsoft · Enterprise",
        "tag": "Enterprise",
        "route": "integration-azure-stt",
        "logo": '<img src="https://cdn.simpleicons.org/microsoftazure/0078D4" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="https://cdn.simpleicons.org/microsoftazure/0078D4" alt="" width="32" height="32" loading="lazy" />',
        "title": "Azure Speech — EMAAVY",
        "h1": "Azure Speech",
        "meta": "Azure Speech Services and EMAAVY — enterprise STT with global languages, private endpoints, and Microsoft compliance posture.",
        "lead": "Azure Speech gives enterprises on Microsoft clouds a governed path to live transcription — private links, region pinning, and Entra ID integration while EMAAVY handles agent orchestration and CRM sync.",
        "stats": [("100+", "Languages"), ("Private", "Endpoints"), ("Entra ID", "Auth")],
        "about": [
            "Microsoft Azure Speech Services provides batch and real-time speech recognition with broad language packs, custom speech models, and deployment in customer VNets for regulated industries.",
            "Organizations with existing Azure EA agreements often mandate Azure STT for voice AI — EMAAVY connects without forcing a parallel media pipeline rebuild.",
        ],
        "emaavy": [
            ("Azure-native security", "Align with existing IAM and network policies."),
            ("Custom speech models", "Train domain vocabulary on Azure; consume via EMAAVY."),
            ("Hybrid cloud", "On-prem voice gateways with Azure STT in region."),
            ("Teams synergy", "Optional hooks for Dynamics and Power platform CRMs."),
        ],
        "features": [
            ("Real-time STT", "Continuous recognition for voice agents."),
            ("Custom Speech", "Fine-tuned acoustic and language models."),
            ("Private endpoints", "Traffic stays on customer networks."),
            ("Global languages", "Extensive locale and voice catalog."),
            ("Pronunciation assessment", "Optional scoring for coaching use cases."),
            ("SLA-backed", "Enterprise availability commitments."),
        ],
        "uses": [
            ("Microsoft shops", "Enterprises standardized on Azure and Entra."),
            ("Regulated finance", "Banks requiring VNet-isolated speech."),
            ("Global enterprises", "Multi-region programs with one vendor contract."),
        ],
        "setup": [
            ("Create Speech resource", "Provision in target Azure region."),
            ("Link to EMAAVY", "Add subscription keys or managed identity."),
            ("Deploy custom model", "Optional domain training before go-live."),
            ("Network review", "Validate private endpoint routing from EMAAVY."),
        ],
        "hub_desc": "Enterprise-grade speech recognition with global languages and private Azure deployment.",
        "hub_points": ["Custom Speech models", "Private endpoints", "Entra ID integration"],
        "hub_badge": "Enterprise",
    },
    {
        "slug": "google-stt",
        "name": "Google STT",
        "short": "Google",
        "region": "Google Cloud · Global",
        "tag": "Global",
        "route": "integration-google-stt",
        "logo": '<img src="https://cdn.simpleicons.org/google/4285F4" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="https://cdn.simpleicons.org/google/4285F4" alt="" width="32" height="32" loading="lazy" />',
        "title": "Google Speech-to-Text — EMAAVY",
        "h1": "Google Speech-to-Text",
        "meta": "Google Cloud Speech-to-Text and EMAAVY — broad language coverage with telephony-optimized models.",
        "lead": "Google Cloud Speech-to-Text spans hundreds of languages and dialects with models tuned for phone audio — ideal when EMAAVY campaigns run on GCP or need Google's latest chirp-class accuracy.",
        "stats": [("125+", "Languages"), ("Telephony", "Models"), ("GCP", "Native")],
        "about": [
            "Google Cloud STT supports synchronous, streaming, and batch recognition with enhanced phone call models that expect 8 kHz narrow-band audio typical of PSTN legs.",
            "Teams on Google Kubernetes, BigQuery analytics, or Chronicle security stacks often keep speech in GCP for unified billing and VPC service controls.",
        ],
        "emaavy": [
            ("GCP alignment", "Same project boundaries as other cloud voice services."),
            ("Phone model selection", "Automatic telephony profile per campaign."),
            ("Multi-language routing", "Pair with EMAAVY language detection rules."),
            ("Data residency", "Region-specific processing for compliance."),
        ],
        "features": [
            ("Streaming recognition", "Interim results for live agents."),
            ("Telephony model", "Optimized for call center audio."),
            ("Speech adaptation", "Phrase hints and custom classes."),
            ("Multilingual", "Automatic language detection options."),
            ("Word timestamps", "Align transcripts to audio for QA."),
            ("VPC controls", "Service perimeter compatible deployments."),
        ],
        "uses": [
            ("GCP-native voice", "Programs already on Google Cloud."),
            ("Global support lines", "Many languages on one platform."),
            ("Analytics pipelines", "Export to BigQuery after EMAAVY enrichment."),
        ],
        "setup": [
            ("Enable Speech API", "In Google Cloud project linked to EMAAVY."),
            ("Create service account", "Least-privilege credentials for STT only."),
            ("Configure adaptation", "Phrase sets for brand and SKU names."),
            ("Test phone audio", "Validate 8 kHz samples from your carrier."),
        ],
        "hub_desc": "Broad language coverage with telephony-optimized models on Google Cloud.",
        "hub_points": ["Phone call model", "Phrase adaptation", "GCP-native security"],
        "hub_badge": "Global",
    },
    {
        "slug": "openai-stt",
        "name": "OpenAI Whisper",
        "short": "Whisper",
        "region": "OpenAI · Multilingual",
        "tag": "Whisper",
        "route": "integration-openai-stt",
        "logo": '<img src="https://cdn.worldvectorlogo.com/logos/openai-2.svg" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="https://cdn.worldvectorlogo.com/logos/openai-2.svg" alt="" width="32" height="32" loading="lazy" />',
        "title": "OpenAI Whisper — EMAAVY",
        "h1": "OpenAI Whisper",
        "meta": "OpenAI Whisper and EMAAVY — accurate multilingual STT across accents for voice and QA workflows.",
        "lead": "Whisper brought robust open-vocabulary transcription to dozens of languages — on EMAAVY it suits accent-heavy cohorts, offline QA batches, and teams already standardized on OpenAI API keys for LLM and speech together.",
        "stats": [("99", "Languages"), ("Robust", "Accents"), ("API", "Streaming")],
        "about": [
            "OpenAI's Whisper models transcribe speech across languages without rigid grammars — valuable when callers code-switch or use regional accents that break narrower engines.",
            "EMAAVY supports Whisper via API for streaming and batch — often as a fallback or challenger against Deepgram on specific agent profiles.",
        ],
        "emaavy": [
            ("Unified OpenAI billing", "One vendor for STT and GPT on the same agent."),
            ("Accent resilience", "Strong on non-native English and mixed speech."),
            ("Batch QA", "Reprocess recordings for compliance audits."),
            ("Champion-challenger", "A/B Whisper vs. other engines per campaign."),
        ],
        "features": [
            ("Multilingual", "Broad language coverage out of the box."),
            ("Accent robustness", "Handles diverse speaker populations."),
            ("API access", "Managed inference without self-hosting GPUs."),
            ("Timestamp support", "Segment-level timing for coaching."),
            ("Translation mode", "Optional translate-to-English pipelines."),
            ("Version upgrades", "Adopt new Whisper generations via config."),
        ],
        "uses": [
            ("Mixed-accent English", "Global outbound with diverse callers."),
            ("Pilot programs", "Quick STT without multi-vendor contracts."),
            ("Post-call QA", "Batch transcription for offline review."),
        ],
        "setup": [
            ("Add OpenAI key", "Reuse org keys with STT scopes in EMAAVY."),
            ("Pick model tier", "Balance cost vs. latency per campaign."),
            ("Define fallback rules", "When to switch from primary STT to Whisper."),
            ("Review PII policy", "Align retention with OpenAI enterprise terms."),
        ],
        "hub_desc": "Accurate multilingual recognition across languages and accents via Whisper.",
        "hub_points": ["99-language coverage", "Accent-heavy audio", "Pairs with OpenAI LLMs"],
        "hub_badge": "Whisper",
    },
    {
        "slug": "elevenlabs-stt",
        "name": "ElevenLabs STT",
        "short": "ElevenLabs",
        "region": "Unified voice stack",
        "tag": "Unified stack",
        "route": "integration-elevenlabs-stt",
        "logo": '<img src="../../assets/logos/elevenlabs.svg" alt="" width="52" height="52" loading="lazy" />',
        "logo_sm": '<img src="../../assets/logos/elevenlabs.svg" alt="" width="32" height="32" loading="lazy" />',
        "title": "ElevenLabs STT — EMAAVY",
        "h1": "ElevenLabs STT",
        "meta": "ElevenLabs speech-to-text and EMAAVY — one API key for STT and expressive TTS on the same voice agents.",
        "lead": "ElevenLabs is known for expressive TTS — their STT offering lets EMAAVY teams run capture and playback on one vendor, one key rotation policy, and one invoice for full voice loops.",
        "stats": [("STT + TTS", "One vendor"), ("Expressive", "Voice stack"), ("Simple", "Ops")],
        "about": [
            "ElevenLabs expanded from voice synthesis into speech recognition so builders can close the listen-and-speak loop without juggling separate STT and TTS contracts.",
            "Campaigns prioritizing brand voice consistency often pick ElevenLabs for TTS already — adding STT through EMAAVY reduces integration surface area.",
        ],
        "emaavy": [
            ("Single vendor loop", "STT → LLM → ElevenLabs TTS in one flow."),
            ("Key management", "One credential store in EMAAVY integrations."),
            ("Voice consistency", "Same platform ethos for listen and speak."),
            ("Faster procurement", "Fewer security reviews for new vendors."),
        ],
        "features": [
            ("Speech-to-text API", "Capture audio for agent reasoning."),
            ("TTS pairing", "Native handoff to ElevenLabs voices."),
            ("Streaming", "Support for live conversational use cases."),
            ("Multilingual", "Growing locale support for global pilots."),
            ("Unified dashboard", "Monitor usage across STT and TTS."),
            ("EMAAVY routing", "Mix with other STT engines per language if needed."),
        ],
        "uses": [
            ("Brand-voice programs", "Premium outbound with matched STT/TTS vendor."),
            ("Startup stacks", "Minimize vendor count early on."),
            ("English-first pilots", "Rapid MVP before multi-engine routing."),
        ],
        "setup": [
            ("Connect ElevenLabs key", "Same key powers STT and TTS in EMAAVY."),
            ("Assign to agents", "Select ElevenLabs STT on agent audio settings."),
            ("Pair TTS voice", "Choose matching voice profile for responses."),
            ("Load test full loop", "Measure end-to-end turn latency."),
        ],
        "hub_desc": "One API key for STT and expressive TTS — a unified ElevenLabs voice stack.",
        "hub_points": ["STT + TTS together", "Simpler credential ops", "Brand-consistent voice loop"],
        "hub_badge": "Unified stack",
    },
    {
        "slug": "gladia",
        "name": "Gladia",
        "short": "Gladia",
        "region": "Multilingual · Code-switch",
        "tag": "Multilingual",
        "route": "integration-gladia",
        "logo": '<span class="brand-mark">GL</span>',
        "logo_sm": '<span class="brand-mark">GL</span>',
        "title": "Gladia — EMAAVY",
        "h1": "Gladia",
        "meta": "Gladia and EMAAVY — multilingual transcription with code-switching and sub-300ms latency for European and global programs.",
        "lead": "Gladia specializes in multilingual and code-switched audio — when callers blend languages mid-sentence, EMAAVY routes to Gladia for accurate live text without forcing a single locale per call.",
        "stats": [("<300ms", "Target latency"), ("Code-switch", "Native"), ("EU", "Friendly")],
        "about": [
            "Gladia provides speech-to-text APIs emphasizing low latency, many languages, and robust handling of speakers who switch languages within an utterance — common in European support and diaspora outbound.",
            "EMAAVY positions Gladia as an alternative to default global engines when WER on mixed-language calls drives escalations and rework.",
        ],
        "emaavy": [
            ("Code-switch routing", "Detect blend scenarios and prefer Gladia automatically."),
            ("EU operations", "Data handling aligned with European customer expectations."),
            ("Live streaming", "Feed LLM intent layers without batch delay."),
            ("Champion tests", "Compare Gladia vs. Deepgram on mixed cohorts."),
        ],
        "features": [
            ("Multilingual STT", "Wide language matrix for global lines."),
            ("Code-switching", "Single stream when speakers mix languages."),
            ("Low latency", "Optimized for conversational AI."),
            ("API simplicity", "Fast integration through EMAAVY connectors."),
            ("Custom vocabulary", "Domain terms for regulated industries."),
            ("Analytics-ready output", "Clean text for downstream NLP."),
        ],
        "uses": [
            ("European support", "Multilingual contact centers."),
            ("Diaspora outbound", "Calls mixing English with heritage languages."),
            ("Marketplace platforms", "Sellers and buyers with varied locales."),
        ],
        "setup": [
            ("Add Gladia API key", "Configure in EMAAVY integrations."),
            ("Set language policy", "Rules for when Gladia wins routing."),
            ("Run WER eval", "Compare transcripts on historical mixed-language calls."),
            ("Production slice", "Start with one queue before global default."),
        ],
        "hub_desc": "Multilingual transcription with code-switching and sub-300ms latency targets.",
        "hub_points": ["Code-switch robustness", "Multilingual streaming", "EU-friendly operations"],
        "hub_badge": "Multilingual",
    },
    {
        "slug": "smallest",
        "name": "Smallest AI",
        "short": "Smallest",
        "region": "Lightweight · Fast",
        "tag": "Lightweight",
        "route": "integration-smallest",
        "logo": '<span class="brand-mark">SM</span>',
        "logo_sm": '<span class="brand-mark">SM</span>',
        "title": "Smallest AI — EMAAVY",
        "h1": "Smallest AI",
        "meta": "Smallest AI and EMAAVY — lightweight, fast transcription for low-latency conversational voice agents.",
        "lead": "Smallest AI focuses on efficient speech models — when every millisecond counts on simple scripts and high-QPS outbound, EMAAVY can route to Smallest for economical, fast transcription without flagship-model cost.",
        "stats": [("Fast", "Inference"), ("Lightweight", "Models"), ("Cost", "Efficient")],
        "about": [
            "Smallest AI builds compact speech recognition systems aimed at real-time conversational use cases where full-size cloud STT is overkill for short, structured dialogues.",
            "On EMAAVY, Smallest fits qualification agents, survey flows, and appointment reminders where utterances are predictable and latency dominates UX scores.",
        ],
        "emaavy": [
            ("Latency tier", "Assign Smallest to speed-critical agent profiles."),
            ("Cost optimization", "Lower STT spend on high-volume short calls."),
            ("Hybrid routing", "Escalate to heavier STT when confidence drops."),
            ("Easy trials", "Pilot on one campaign with clear KPI gates."),
        ],
        "features": [
            ("Low latency", "Tight inference for voice loops."),
            ("Efficient models", "Smaller footprint per minute."),
            ("Streaming", "Live partial transcripts."),
            ("Simple integration", "Quick EMAAVY connector setup."),
            ("Indian focus", "Suitable for domestic short-call programs."),
            ("Scalable QPS", "Handle burst dialer traffic."),
        ],
        "uses": [
            ("Appointment reminders", "Short scripted outbound."),
            ("Lead qualification", "Brief yes/no style dialogs."),
            ("Cost-sensitive scale", "Millions of minutes with tight unit economics."),
        ],
        "setup": [
            ("Connect Smallest API", "Add credentials in EMAAVY."),
            ("Define agent tier", "Mark agents that use lightweight STT."),
            ("Monitor confidence", "Fallback rules to premium STT if needed."),
            ("Measure CSAT", "Ensure speed does not hurt comprehension."),
        ],
        "hub_desc": "Lightweight, fast transcription tuned for low-latency conversational agents.",
        "hub_points": ["Efficient inference", "High-QPS friendly", "Cost-optimized capture"],
        "hub_badge": "Lightweight",
    },
]

USE_EXTRAS = [
    ("Live coaching", "Supervisors see transcripts and intent signals in real time."),
    ("Compliance monitoring", "Keyword and phrase detection for regulated industries."),
    ("Multi-agent operations", "Route languages and accents per campaign without rebuilds."),
]

HUB_CFG = {
    "route": "integration-stt",
    "title": "Speech-to-Text — EMAAVY",
    "meta": "Nine STT providers, one EMAAVY platform. Pick the best engine per language, accent, or latency — routing is automatic so nothing gets lost.",
    "og_title": "Speech-to-Text — EMAAVY",
    "og_description": "Deepgram, Sarvam, AssemblyAI, Azure, Google, Whisper, and more — unified live transcription on EMAAVY.",
    "breadcrumb": "Speech-to-Text",
    "kicker": "Capture layer · Speech-to-Text",
    "h1": "Every word captured — in real time",
    "lead": "Nine STT providers, one EMAAVY platform. Pick the best engine per language, accent, or latency — routing is automatic so supervisors, agents, and CRM systems see words as they are spoken.",
    "stats": [("9", "STT providers"), ("<0.5s", "Typical latency"), ("22+", "Languages")],
    "anchor_jumps": [
        ("capture-layer", "How EMAAVY transcribes"),
        ("providers", "STT partners"),
        ("pipeline", "Speech pipeline"),
    ],
    "layer_id": "capture-layer",
    "layer_num": "Layer 03",
    "layer_tag": "EMAAVY · Speech-to-Text",
    "layer_h2": "How EMAAVY handles transcription",
    "layer_lead": "Telephony audio streams into the STT layer the moment a call connects. Engineering configures defaults; operations routes Indian dialects, global English, and low-latency tiers without rebuilding agents.",
    "pills": [
        ("Provider choice", "Deepgram, Sarvam, Gladia, Azure, Google, and more."),
        ("Language routing", "Indian languages to Sarvam; global English to Deepgram."),
        ("Keyword boosting", "Brand and compliance phrases recognized reliably."),
        ("Live feeds", "Transcripts power intent scoring before hang-up."),
    ],
    "partners_id": "providers",
    "partners_h2": "STT partners",
    "partners_desc": "Nine engines integrated today — each with a dedicated page on capabilities, EMAAVY routing, and rollout steps.",
    "flow_id": "pipeline",
    "flow_h2": "From speech to structured insight",
    "flow_desc": "How every call moves through EMAAVY once audio hits the STT layer.",
    "flow_steps": [
        ("Audio captured", "EMAAVY ingests the live media stream from the voice channel."),
        ("STT transcribes", "Your chosen engine streams words with sub-second latency."),
        ("Intent parsed", "LLM layer classifies buyer signals from the transcript."),
        ("Scores update", "Sentiment and compliance refresh on every turn."),
        ("Actions fire", "CRM, webhooks, and coaching rules run automatically."),
    ],
    "cta_h2": "Connect Speech-to-Text to EMAAVY",
    "cta_desc": "See live STT routing, keyword boosting, and agent handoff in a tailored demo.",
}

HUB_FILE = "stt.html"
HUB_LABEL = "All STT"
HUB_BREADCRUMB = "Speech-to-Text"
HUB_CTA = "STT overview"


def prepare():
    for p in PROVIDERS:
        p.pop("featured", None)
        ensure_uses(p, USE_EXTRAS)
    apply_logos_all(PROVIDERS)


def write_partner(p: dict) -> str:
    route = p.get("route", f"integration-{p['slug']}")
    return render_partner(
        p,
        partners=PROVIDERS,
        route=route,
        segment_kicker=f"Speech-to-Text · {p['tag']}",
        hub_file=HUB_FILE,
        hub_label=HUB_LABEL,
        hub_breadcrumb=HUB_BREADCRUMB,
        hub_cta_label=HUB_CTA,
        nav_label_key="short",
        connect_name_key="name",
        explore_title="Explore other STT engines",
        explore_desc="Mix engines by language and latency — EMAAVY keeps transcripts and scoring consistent.",
        nav_aria="STT partners",
        overview_fit="your capture layer",
        cta_desc="Book a walkthrough — we will map STT routing, keyword boosting, and a live agent demo.",
        segment_type="stt",
        hub_label_key="short",
    )



def update_routes():
    path = ROOT / "assets" / "routes.js"
    text = path.read_text(encoding="utf-8")
    lines = ["      { id: 'stt', label: 'STT layer', path: 'pages/integrations/stt.html' },"]
    for p in PROVIDERS:
        label = p["name"]
        lines.append(
            f"      {{ id: '{p['slug']}', label: '{label}', path: 'pages/integrations/{p['slug']}.html' }},"
        )
    block = "    stt: [\n" + "\n".join(lines) + "\n    ],"
    text = re.sub(r"    stt: \[.*?\],", block, text, count=1, flags=re.DOTALL)
    path.write_text(text, encoding="utf-8")


def main():
    prepare()
    INT.mkdir(parents=True, exist_ok=True)
    (INT / "stt.html").write_text(
        render_hub(HUB_CFG, PROVIDERS, jump_label_key="short", hub_tile_label_key="short"), encoding="utf-8"
    )
    for p in PROVIDERS:
        (INT / f"{p['slug']}.html").write_text(write_partner(p), encoding="utf-8")
    update_routes()
    print(f"OK: stt.html + {len(PROVIDERS)} partner pages, routes.js updated")


if __name__ == "__main__":
    main()
