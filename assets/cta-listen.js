/**
 * CTA enterprise platform — layer highlight + status ribbon + pipeline.
 */
(function () {
  const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  const pulses = [
    {
      label: 'Connect',
      line: 'Vobiz · SIP · Twilio — every call captured from ring one',
      meta: 'Telephony layer',
      layer: 0,
    },
    {
      label: 'Transcribe',
      line: 'Deepgram · Sarvam · 22 languages including Hinglish',
      meta: 'STT layer',
      layer: 1,
    },
    {
      label: 'AI Agents',
      line: 'Sales · support · campaign agents — 24/7 with human handoff',
      meta: 'Voice workforce',
      layer: 2,
    },
    {
      label: 'Orchestrate',
      line: 'Salesforce · HubSpot · WhatsApp · Cal.com — triggers on intent',
      meta: 'Tools & CRM',
      layer: 3,
    },
    {
      label: 'Analytics',
      line: 'Volume · intent funnel · operator leaderboard · latency SLAs',
      meta: 'Intelligence matrix',
      layer: 4,
    },
    {
      label: 'Govern',
      line: 'SOC 2 controls · PII redaction · exportable audit trails',
      meta: 'Enterprise security',
      layer: 5,
    },
  ];

  const labelEl = document.getElementById('ctaPulseLabel');
  const lineEl = document.getElementById('ctaPulseLine');
  const metaEl = document.getElementById('ctaPulseMeta');
  const cardEl = document.getElementById('ctaPulseCard');
  const layerChips = document.querySelectorAll('.cta-layer-chip[data-layer]');

  function setActiveLayer(index) {
    layerChips.forEach((chip) => {
      chip.classList.toggle('is-active', Number(chip.dataset.layer) === index);
    });
  }

  if (labelEl && lineEl && metaEl && !reduced) {
    let i = 0;
    setActiveLayer(pulses[0].layer);

    const cycle = () => {
      if (cardEl) cardEl.style.opacity = '0.65';
      setTimeout(() => {
        const p = pulses[i];
        labelEl.textContent = p.label;
        lineEl.textContent = p.line;
        metaEl.textContent = p.meta;
        setActiveLayer(p.layer);
        i = (i + 1) % pulses.length;
        if (cardEl) cardEl.style.opacity = '1';
      }, 280);
    };

    if (cardEl) cardEl.style.transition = 'opacity 0.35s ease';
    setInterval(cycle, 4200);
  } else if (layerChips.length) {
    setActiveLayer(0);
  }

  const pipeSteps = document.querySelectorAll('.cta-pipe-step');
  if (pipeSteps.length && !reduced) {
    let step = 0;
    setInterval(() => {
      pipeSteps.forEach((s, idx) => s.classList.toggle('is-active', idx === step));
      step = (step + 1) % pipeSteps.length;
    }, 2400);
  }
})();
