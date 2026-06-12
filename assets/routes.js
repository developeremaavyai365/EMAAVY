/**
 * EMAAVY central route registry — single source of truth for navigation
 */
window.EMAAVY_ROUTES = {
  siteName: 'EMAAVY',
  logo: 'assets/brand/emaavy-logo.svg',
  logoMark: 'assets/brand/emaavy-logo.svg',
  logoAspect: 648 / 116,
  landingPage: 'index.html',

  mainNav: [
    { id: 'how-it-works', label: 'How It Works', path: 'pages/how-it-works.html' },
    { id: 'integrations', label: 'Integrations', path: 'pages/integrations/index.html', dropdown: 'integrations' },
    { id: 'agents', label: 'Agents', path: 'pages/agents/index.html', dropdown: 'agents' },
    { id: 'campaigns', label: 'Campaigns', path: 'index.html#campaigns' },
    { id: 'features', label: 'Flows', path: 'pages/features.html' },
    { id: 'case-studies', label: 'Case Studies', path: 'pages/case-studies.html' },
    { id: 'journey', label: 'Call lifecycle', path: 'pages/call-lifecycle/index.html', dropdown: 'lifecycle' },
    { id: 'faq', label: 'FAQ', path: 'pages/faq.html', dropdown: 'faq' },
    { id: 'pricing', label: 'Pricing', path: 'pages/pricing.html' },
    { id: 'documentation', label: 'Documentation', path: 'pages/documentation.html' },
    { id: 'contact', label: 'Contact Us', path: 'pages/contact.html' },
  ],

  authNav: [
    { id: 'login', label: 'Log In', path: 'login.html', className: 'btn-nav-login' },
    { id: 'book-demo', label: 'Book a Demo', path: 'book-demo.html', className: 'btn-nav-demo' },
  ],

  integrationHubLayers: [
    { label: 'All integrations', path: 'pages/integrations/index.html' },
    { label: 'Telephony', path: 'pages/integrations/telephony.html' },
    { label: 'LLMs', path: 'pages/integrations/llms.html' },
    { label: 'Speech-to-Text', path: 'pages/integrations/stt.html' },
    { label: 'Text-to-Speech', path: 'pages/integrations/tts.html' },
    { label: 'Tools & workflow', path: 'pages/integrations/tools.html' },
  ],

  integrations: {
    telephony: [
      { id: 'telephony', label: 'Telephony layer', path: 'pages/integrations/telephony.html' },
      { id: 'vobiz', label: 'Vobiz', path: 'pages/integrations/vobiz.html' },
      { id: 'twilio', label: 'Twilio', path: 'pages/integrations/twilio.html' },
      { id: 'plivo', label: 'Plivo', path: 'pages/integrations/plivo.html' },
      { id: 'vonage', label: 'Vonage', path: 'pages/integrations/vonage.html' },
      { id: 'exotel', label: 'Exotel', path: 'pages/integrations/exotel.html' },
      { id: 'knowlarity', label: 'Knowlarity', path: 'pages/integrations/knowlarity.html' },
      { id: 'telnyx', label: 'Telnyx', path: 'pages/integrations/telnyx.html' },
      { id: 'bandwidth', label: 'Bandwidth', path: 'pages/integrations/bandwidth.html' },
    ],
    llm: [
      { id: 'llm', label: 'LLM layer', path: 'pages/integrations/llms.html' },
      { id: 'openai', label: 'OpenAI GPT', path: 'pages/integrations/openai.html' },
      { id: 'claude', label: 'Claude', path: 'pages/integrations/claude.html' },
      { id: 'gemini', label: 'Gemini', path: 'pages/integrations/gemini.html' },
      { id: 'qwen', label: 'Qwen', path: 'pages/integrations/qwen.html' },
      { id: 'grok', label: 'Grok', path: 'pages/integrations/grok.html' },
    ],
    stt: [
      { id: 'stt', label: 'STT layer', path: 'pages/integrations/stt.html' },
      { id: 'deepgram', label: 'Deepgram', path: 'pages/integrations/deepgram.html' },
      { id: 'sarvam', label: 'Sarvam AI', path: 'pages/integrations/sarvam.html' },
      { id: 'assemblyai', label: 'AssemblyAI', path: 'pages/integrations/assemblyai.html' },
      { id: 'azure-stt', label: 'Azure Speech', path: 'pages/integrations/azure-stt.html' },
      { id: 'google-stt', label: 'Google STT', path: 'pages/integrations/google-stt.html' },
      { id: 'openai-stt', label: 'OpenAI Whisper', path: 'pages/integrations/openai-stt.html' },
      { id: 'elevenlabs-stt', label: 'ElevenLabs STT', path: 'pages/integrations/elevenlabs-stt.html' },
      { id: 'gladia', label: 'Gladia', path: 'pages/integrations/gladia.html' },
      { id: 'smallest', label: 'Smallest AI', path: 'pages/integrations/smallest.html' },
    ],
    tts: [
      { id: 'tts', label: 'TTS layer', path: 'pages/integrations/tts.html' },
      { id: 'elevenlabs', label: 'ElevenLabs', path: 'pages/integrations/elevenlabs.html' },
      { id: 'flash-bulbul', label: 'Flash · Bulbul', path: 'pages/integrations/flash-bulbul.html' },
    ],
    tools: [
      { id: 'tools', label: 'Tools layer', path: 'pages/integrations/tools.html' },
      { id: 'webhooks', label: 'Webhooks', path: 'pages/integrations/webhooks.html' },
      { id: 'salesforce', label: 'Salesforce', path: 'pages/integrations/salesforce.html' },
      { id: 'hubspot', label: 'HubSpot', path: 'pages/integrations/hubspot.html' },
      { id: 'calcom', label: 'Cal.com', path: 'pages/integrations/calcom.html' },
      { id: 'google-calendar', label: 'Google Calendar', path: 'pages/integrations/google-calendar.html' },
      { id: 'whatsapp', label: 'WhatsApp', path: 'pages/integrations/whatsapp.html' },
      { id: 'slack', label: 'Slack', path: 'pages/integrations/slack.html' },
    ],
  },

  caseStudies: [
    { id: 'mudita', label: 'Warehouse by Mudita', path: 'pages/case-studies/mudita.html' },
    { id: 'nextcall', label: 'NextCall BPO', path: 'pages/case-studies/nextcall.html' },
    { id: 'fleetiq', label: 'FleetIQ Logistics', path: 'pages/case-studies/fleetiq.html' },
  ],

  callLifecycle: [
    { id: 'ring', label: 'Call connects', path: 'pages/call-lifecycle/ring.html' },
    { id: 'transcribe', label: 'Every word captured', path: 'pages/call-lifecycle/transcribe.html' },
    { id: 'analyze', label: 'Score live', path: 'pages/call-lifecycle/analyze.html' },
    { id: 'act', label: 'Triggers fire', path: 'pages/call-lifecycle/act.html' },
    { id: 'learn', label: 'Models improve', path: 'pages/call-lifecycle/learn.html' },
  ],

  faqTopics: [
    { id: 'go-live', label: 'Go live', path: 'pages/faq/go-live.html' },
    { id: 'voice-models', label: 'Voice models', path: 'pages/faq/voice-models.html' },
    { id: 'compliance', label: 'Compliance', path: 'pages/faq/compliance.html' },
    { id: 'pricing-scale', label: 'Pricing & usage', path: 'pages/faq/pricing-scale.html' },
    { id: 'crm-integrations', label: 'CRM integrations', path: 'pages/faq/crm-integrations.html' },
    { id: 'enterprise-support', label: 'Enterprise support', path: 'pages/faq/enterprise-support.html' },
  ],

  agents: [
    { id: 'workforce', label: 'Agent Templates', path: 'pages/agents/workforce.html' },
    { id: 'agents-index', label: 'Agent Directory', path: 'pages/agents/index.html' },
    { id: 'real-estate', label: 'Real Estate Lead Qualification', path: 'pages/agents/real-estate.html' },
    { id: 'appointment-reminder', label: 'Contextual Appointment Reminder', path: 'pages/agents/appointment-reminder.html' },
    { id: 'appointment-booking', label: 'Appointment Booking', path: 'pages/agents/appointment-booking.html' },
    { id: 'nps-review', label: 'Insightful NPS Review', path: 'pages/agents/nps-review.html' },
    { id: 'event-agent', label: 'High-Conversion Event Agent', path: 'pages/agents/event-agent.html' },
    { id: 'recruiter-outreach', label: 'Recruiter-grade Outreach', path: 'pages/agents/recruiter-outreach.html' },
    { id: 'payment-checkin', label: 'Friendly Payment Check-in', path: 'pages/agents/payment-checkin.html' },
    { id: 'support-playbook', label: 'Intelligent Support Playbook', path: 'pages/agents/support-playbook.html' },
    { id: 'order-returns', label: 'Order, Refund & Returns', path: 'pages/agents/order-returns.html' },
    { id: 'financial-assistant', label: 'Financial Assistant (Loan & EMI)', path: 'pages/agents/financial-assistant.html' },
    { id: 'customer-reactivation', label: 'High-Conversion Customer Reactivation', path: 'pages/agents/customer-reactivation.html' },
    { id: 'job-applicant', label: 'Job Applicant Concierge', path: 'pages/agents/job-applicant.html' },
    { id: 'distributor-collection', label: 'Distributor Payment Collection', path: 'pages/agents/distributor-collection.html' },
    { id: 'fashion-event', label: 'Fashion Event Registration Call', path: 'pages/agents/fashion-event.html' },
  ],

  footerNav: {
    apiDocs: [
    { id: 'api-authentication', label: 'API Authentication', path: 'pages/api-docs/api-authentication.html', route: 'footer-api-authentication' },
    { id: 'using-agents-apis', label: 'Using Agents APIs', path: 'pages/api-docs/using-agents-apis.html', route: 'footer-using-agents-apis' },
    { id: 'making-phone-calls-apis', label: 'Making Phone Calls APIs', path: 'pages/api-docs/making-phone-calls-apis.html', route: 'footer-making-phone-calls-apis' },
    { id: 'get-call-data-apis', label: 'Get Call Data APIs', path: 'pages/api-docs/get-call-data-apis.html', route: 'footer-get-call-data-apis' },
    { id: 'phone-numbers-apis', label: 'Phone Numbers APIs', path: 'pages/api-docs/phone-numbers-apis.html', route: 'footer-phone-numbers-apis' },
    { id: 'inbound-agents-apis', label: 'Inbound Agents APIs', path: 'pages/api-docs/inbound-agents-apis.html', route: 'footer-inbound-agents-apis' },
    { id: 'knowledgebases-apis', label: 'Knowledgebases APIs', path: 'pages/api-docs/knowledgebases-apis.html', route: 'footer-knowledgebases-apis' },
    { id: 'batch-queue-apis', label: 'Batch & Queue APIs', path: 'pages/api-docs/batch-queue-apis.html', route: 'footer-batch-queue-apis' },
    { id: 'sub-account-isolation-apis', label: 'Sub-account Isolation APIs', path: 'pages/api-docs/sub-account-isolation-apis.html', route: 'footer-sub-account-isolation-apis' },
    ],
    productFeatures: [
    { id: 'dashboard-analytics', label: 'Dashboard & Analytics', path: 'pages/product/dashboard-analytics.html', route: 'footer-dashboard-analytics' },
    { id: 'function-tool-calling', label: 'Function & Tool Calling', path: 'pages/product/function-tool-calling.html', route: 'footer-function-tool-calling' },
    { id: 'pdfs-rags-knowledge-bases', label: 'PDFs, RAGs & Knowledge bases', path: 'pages/product/pdfs-rags-knowledge-bases.html', route: 'footer-pdfs-rags-knowledge-bases' },
    { id: 'twilio-voice-integrations', label: 'Twilio Voice Integrations', path: 'pages/product/twilio-voice-integrations.html', route: 'footer-twilio-voice-integrations' },
    { id: 'plivo-voice-integrations', label: 'Plivo Voice Integrations', path: 'pages/product/plivo-voice-integrations.html', route: 'footer-plivo-voice-integrations' },
    { id: 'multilingual-voice-support', label: 'Multilingual Voice Support', path: 'pages/product/multilingual-voice-support.html', route: 'footer-multilingual-voice-support' },
    { id: 'bulk-calls-campaigns', label: 'Bulk Calls & Campaigns', path: 'pages/product/bulk-calls-campaigns.html', route: 'footer-bulk-calls-campaigns' },
    { id: 'agent-library-templates', label: 'Agent Library & Templates', path: 'pages/product/agent-library-templates.html', route: 'footer-agent-library-templates' },
    { id: 'voice-agent-integrations-ecosystem', label: 'Voice Agent Integrations Ecosystem', path: 'pages/product/voice-agent-integrations-ecosystem.html', route: 'footer-voice-agent-integrations-ecosystem' },
    ],
    companyResources: [
    { id: 'yc-launch-profile', label: 'YC Launch Profile', path: 'pages/company/yc-launch-profile.html', route: 'footer-yc-launch-profile' },
    { id: 'contact-us', label: 'Contact Us', path: 'pages/contact.html', route: 'footer-contact-us' },
    { id: 'schedule-demo-call', label: 'Schedule a Demo Call', path: 'book-demo.html', route: 'footer-schedule-demo-call' },
    { id: 'pricing-plans', label: 'Pricing & Plans', path: 'pages/pricing.html', route: 'footer-pricing-plans' },
    { id: 'engineering-blog', label: 'EMAAVY Engineering Blog', path: 'pages/company/engineering-blog.html', route: 'footer-engineering-blog' },
    { id: 'news-product-updates', label: 'News & Product Updates', path: 'pages/company/news-product-updates.html', route: 'footer-news-product-updates' },
    { id: 'llms-txt', label: 'LLMs.txt (AI Scraping Spec)', path: 'pages/company/llms-txt.html', route: 'footer-llms-txt' },
    { id: 'docs-llms-txt', label: 'Docs LLMs.txt', path: 'pages/company/docs-llms-txt.html', route: 'footer-docs-llms-txt' },
    { id: 'top-voice-agents-use-cases', label: 'Top Voice Agents Use Cases', path: 'pages/company/top-voice-agents-use-cases.html', route: 'footer-top-voice-agents-use-cases' },
    { id: 'system-status', label: 'System Status Indicator', path: 'pages/company/system-status.html', route: 'footer-system-status' },
    ],
    legal: [
    { id: 'terms-of-use', label: 'Terms of Use', path: 'pages/legal/terms-of-use.html', route: 'footer-terms-of-use' },
    { id: 'privacy-policy', label: 'Privacy Policy', path: 'pages/legal/privacy-policy.html', route: 'footer-privacy-policy' },
    ],
    social: [
      { id: 'x', label: 'X (Twitter)', url: 'https://x.com/emaavy' },
      { id: 'linkedin', label: 'LinkedIn', url: 'https://linkedin.com/company/emaavy' },
      { id: 'youtube', label: 'YouTube', url: 'https://youtube.com/@emaavy' },
    ],
  },

  integrationGroups: [
    { key: 'telephony', title: 'Telephony' },
    { key: 'llm', title: 'LLMs' },
    { key: 'stt', title: 'STT' },
    { key: 'tts', title: 'TTS' },
    { key: 'tools', title: 'Tools' },
  ],

  spaHref(routeId) {
    if (routeId === 'home') return '#/';
    if (routeId.startsWith('integration-')) return '#/integrations/' + routeId.replace('integration-', '');
    if (routeId.startsWith('faq-')) return '#/faq/' + routeId.replace('faq-', '');
    if (routeId.startsWith('case-study-')) return '#/case-studies/' + routeId.replace('case-study-', '');
    if (routeId.startsWith('lifecycle-')) return '#/call-lifecycle/' + routeId.replace('lifecycle-', '');
    if (routeId.startsWith('matrix-')) return '#/intelligence-matrix/' + routeId.replace('matrix-', '');
    if (routeId.startsWith('agent-')) return '#/agents/' + routeId.replace('agent-', '');
    return '#/' + routeId;
  },

  pathToSpa(path) {
    if (path === 'pages/integrations/index.html') return '#/integrations';
    if (path === 'pages/agents/index.html') return '#/agents';
    if (path.startsWith('pages/integrations/')) {
      const slug = path.replace('pages/integrations/', '').replace('.html', '');
      return '#/integrations/' + slug;
    }
    if (path.startsWith('pages/agents/')) {
      const slug = path.replace('pages/agents/', '').replace('.html', '');
      return '#/agents/' + slug;
    }
    if (path === 'pages/call-lifecycle/index.html') return '#/call-lifecycle';
    if (path.startsWith('pages/call-lifecycle/')) {
      const slug = path.replace('pages/call-lifecycle/', '').replace('.html', '');
      return '#/call-lifecycle/' + slug;
    }
    if (path.startsWith('pages/case-studies/')) {
      const slug = path.replace('pages/case-studies/', '').replace('.html', '');
      return '#/case-studies/' + slug;
    }
    if (path.startsWith('pages/')) return '#/' + path.replace('pages/', '').replace('.html', '');
    if (path === 'login.html') return '#/login';
    if (path === 'book-demo.html') return '#/book-demo';
    if (path === 'index.html' || path === this.landingPage) return '#/';
    return path;
  },

  homeHref(base) {
    return this.href(this.landingPage, base);
  },

  href(path, base) {
    if (path === 'index.html') path = this.landingPage;
    if (document.body?.dataset?.spa === 'true') return this.pathToSpa(path);
    if (!path) return base || './';
    if (path.startsWith('http') || path.startsWith('#')) return path;
    return (base || '') + path;
  },

  allIntegrations() {
    return Object.values(this.integrations).flat();
  },

  matchRoute(currentRoute) {
    if (!currentRoute) return null;
    if (currentRoute === 'home') return 'home';
    if (currentRoute.startsWith('integration-')) return 'integrations';
    if (currentRoute.startsWith('agent-')) return 'agents';
    if (currentRoute.startsWith('lifecycle-')) return 'journey';
    if (currentRoute.startsWith('faq-')) return 'faq';
    if (currentRoute.startsWith('case-study-')) return 'case-studies';
    for (const item of this.mainNav) {
      if (item.id === currentRoute) return item.id;
    }
    for (const item of this.authNav) {
      if (item.id === currentRoute) return item.id;
    }
    return currentRoute;
  },
};
