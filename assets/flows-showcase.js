(function () {
  const root = document.getElementById('flowsShowcase');
  if (!root) return;

  const device = root.querySelector('.flows-device');
  const nodes = root.querySelectorAll('.flows-node[data-flow-node]');
  const lines = root.querySelectorAll('.flows-lines path[data-flow-edge]');
  const previewTitle = root.querySelector('[data-flow-preview="title"]');
  const previewMeta = root.querySelector('[data-flow-preview="meta"]');
  const previewScript = root.querySelector('[data-flow-preview="script"]');
  const previewBranches = root.querySelector('[data-flow-preview="branches"]');
  const previewOutcome = root.querySelector('[data-flow-preview="outcome"]');
  const branchPills = root.querySelectorAll('.flows-branch-pill');
  const shotToggle = root.querySelector('.flows-shot-toggle');
  const tryLiveBtn = root.querySelector('.flows-try-live');

  const vars = {
    name: root.querySelector('#flowVarName'),
    agent: root.querySelector('#flowVarAgent'),
    company: root.querySelector('#flowVarCompany'),
  };

  const NODE_DATA = {
    begin: {
      title: 'BEGIN',
      meta: 'Flow entry point',
      script: 'The conversation starts when the agent connects to the contact.',
      branches: [],
      outcome: 'Select a node or branch to explore the flow.',
    },
    hook: {
      title: 'Hook + Context',
      meta: 'Curiosity-driven hook',
      script:
        'Hi {{name}}, this is {{agent_name}} from {{company}}. I’m reaching out about {{offer}} — do you have a quick minute?',
      branches: [
        { id: 'interested', label: '⚡ Yes / Interested', edge: 'e-hook-value' },
        { id: 'maybe', label: '◇ Maybe / Need info', edge: 'e-hook-nurture' },
        { id: 'not', label: '✕ Not interested', edge: 'e-hook-soft' },
      ],
      outcome: 'Choose how the contact responds.',
    },
    value: {
      title: 'Value Tease',
      meta: 'Benefits & proof',
      script:
        'Great — here’s what teams like yours gain: faster outreach, live intent scoring, and CRM updates before hang-up. Worth a 2-minute walkthrough?',
      branches: [
        { id: 'yes', label: '✓ Yes — register', edge: 'e-value-capture' },
        { id: 'later', label: '◷ Schedule follow-up', edge: 'e-value-follow' },
      ],
      outcome: 'Path: Interested → Value',
    },
    capture: {
      title: 'Capture Registration',
      meta: 'Conversion step',
      script:
        'Perfect, {{name}}. I’ll send the registration link to your preferred channel and confirm your slot. Anything else before we wrap?',
      branches: [],
      outcome: '→ END Registered',
      end: 'registered',
    },
    nurture: {
      title: 'Nurture Path',
      meta: 'Info & follow-up',
      script:
        'No problem — I can email a one-pager and a short demo clip. What’s the best address, and when should we reconnect?',
      branches: [],
      outcome: '→ END Info Sent',
      end: 'info',
    },
    end_registered: {
      title: 'END Registered',
      meta: 'Success outcome',
      script: 'Contact registered. CRM updated and confirmation sent automatically.',
      branches: [],
      outcome: 'Flow complete — registered',
      end: 'registered',
    },
    end_follow: {
      title: 'END Follow-up Scheduled',
      meta: 'Scheduled outcome',
      script: 'Follow-up booked. Agent hands off to calendar workflow.',
      branches: [],
      outcome: 'Flow complete — follow-up',
      end: 'follow',
    },
    end_info: {
      title: 'END Info Sent',
      meta: 'Nurture outcome',
      script: 'Materials sent. Nurture sequence triggered for re-engagement.',
      branches: [],
      outcome: 'Flow complete — info sent',
      end: 'info',
    },
    end_soft: {
      title: 'END Soft Refusal',
      meta: 'Polite close',
      script:
        'Understood, {{name}}. I’ll note your preference and close the loop — thank you for your time.',
      branches: [],
      outcome: 'Flow complete — soft close',
      end: 'soft',
    },
  };

  const PATH_EDGES = {
    interested: [
      'e-begin-hook',
      'e-hook-value',
      'e-value-capture',
      'e-capture-endreg',
    ],
    maybe: ['e-begin-hook', 'e-hook-nurture', 'e-nurture-endinfo'],
    not: ['e-begin-hook', 'e-hook-soft'],
    yes: [
      'e-begin-hook',
      'e-hook-value',
      'e-value-capture',
      'e-capture-endreg',
    ],
    later: [
      'e-begin-hook',
      'e-hook-value',
      'e-value-follow',
      'e-follow-end',
    ],
  };

  const state = {
    activeNode: 'hook',
    branch: null,
    screenshot: false,
  };

  function substitute(text) {
    const v = {
      name: vars.name?.value?.trim() || 'Rahul',
      agent_name: vars.agent?.value?.trim() || 'Priya',
      company: vars.company?.value?.trim() || 'EMAAVY',
      offer: 'our enterprise voice platform',
    };
    return text.replace(/\{\{(\w+)\}\}/g, (_, key) => v[key] ?? '');
  }

  function setScreenshot(on) {
    state.screenshot = on;
    device?.classList.toggle('is-shot-mode', on);
    shotToggle?.classList.toggle('is-active', on);
  }

  function lightEdges(edgeIds) {
    const set = new Set(edgeIds || []);
    lines.forEach((p) => {
      p.classList.toggle('is-lit', set.has(p.getAttribute('data-flow-edge')));
    });
  }

  function dimNodes(activeId, branch) {
    const onPath = new Set(['begin', activeId]);
    if (branch === 'interested' || branch === 'yes') {
      ['hook', 'value', 'capture', 'end_registered'].forEach((n) => onPath.add(n));
    } else if (branch === 'later') {
      ['hook', 'value', 'end_follow'].forEach((n) => onPath.add(n));
    } else if (branch === 'maybe') {
      ['hook', 'nurture', 'end_info'].forEach((n) => onPath.add(n));
    } else if (branch === 'not') {
      ['hook', 'end_soft'].forEach((n) => onPath.add(n));
    }

    nodes.forEach((el) => {
      const id = el.getAttribute('data-flow-node');
      el.classList.toggle('is-active', id === activeId);
      el.classList.toggle('is-dim', branch ? !onPath.has(id) : id !== activeId);
    });
  }

  function renderBranches(node) {
    if (!previewBranches) return;
    previewBranches.innerHTML = '';
    if (!node.branches?.length) {
      previewBranches.hidden = true;
      return;
    }
    previewBranches.hidden = false;
    node.branches.forEach((b) => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'flows-preview-branch';
      btn.textContent = b.label;
      btn.dataset.branch = b.id;
      if (state.branch === b.id) btn.classList.add('is-on');
      btn.addEventListener('click', () => selectBranch(b.id, node));
      previewBranches.appendChild(btn);
    });
  }

  function selectBranch(branchId, fromNode) {
    setScreenshot(false);
    state.branch = branchId;
    branchPills.forEach((p) => {
      p.classList.toggle('is-active', p.getAttribute('data-branch') === branchId);
    });
    const edgeList = PATH_EDGES[branchId];
    if (edgeList) lightEdges(edgeList);

    const branchDef = fromNode?.branches?.find((b) => b.id === branchId);
    if (branchDef?.edge) {
      const targetMap = {
        'e-hook-value': 'value',
        'e-hook-nurture': 'nurture',
        'e-hook-soft': 'end_soft',
        'e-value-capture': 'capture',
        'e-value-follow': 'end_follow',
      };
      const next = targetMap[branchDef.edge];
      if (next && branchId === 'not') {
        selectNode('end_soft', branchId);
        return;
      }
      if (next && (branchId === 'maybe')) {
        selectNode('nurture', branchId);
        return;
      }
      if (next && branchId === 'interested') {
        selectNode('value', branchId);
        return;
      }
      if (next && branchId === 'yes') {
        selectNode('capture', branchId);
        return;
      }
      if (next && branchId === 'later') {
        selectNode('end_follow', branchId);
        return;
      }
    }

    if (branchId === 'interested') selectNode('value', branchId);
    else if (branchId === 'maybe') selectNode('nurture', branchId);
    else if (branchId === 'not') selectNode('end_soft', branchId);
    else if (branchId === 'yes') selectNode('capture', branchId);
    else if (branchId === 'later') selectNode('end_follow', branchId);
  }

  const layerCards = document.querySelectorAll('#features .flow-layer-card');
  const statusLabel = document.querySelector('[data-flow-status-label]');
  const LAYER_MAP = {
    'flow-hook': { title: 'Hook & Context', node: 'hook' },
    'flow-branch': { title: 'Branching Paths', node: 'hook', branch: 'interested' },
    'flow-value': { title: 'Value & Capture', node: 'value' },
    'flow-nurture': { title: 'Nurture & Follow-up', node: 'nurture' },
    'flow-ends': { title: 'End States', node: 'end_registered' },
  };

  function setLayerSelected(layerId) {
    layerCards.forEach((card) => {
      card.classList.toggle('is-selected', card.getAttribute('data-detail') === layerId);
    });
    const meta = LAYER_MAP[layerId];
    if (statusLabel && meta) statusLabel.textContent = meta.title;
  }

  function syncLayerFromNode(nodeId) {
    layerCards.forEach((card) => {
      const meta = LAYER_MAP[card.getAttribute('data-detail')];
      if (!meta || meta.branch) return;
      if (meta.node === nodeId) setLayerSelected(card.getAttribute('data-detail'));
    });
  }

  function selectNode(nodeId, branchKeep) {
    state.activeNode = nodeId;
    if (!branchKeep) state.branch = null;
    const node = NODE_DATA[nodeId];
    if (!node) return;

    syncLayerFromNode(nodeId);

    dimNodes(nodeId, state.branch);
    if (state.branch && PATH_EDGES[state.branch]) {
      lightEdges(PATH_EDGES[state.branch]);
    } else {
      lightEdges(['e-begin-hook']);
    }

    if (previewTitle) previewTitle.textContent = node.title;
    if (previewMeta) previewMeta.textContent = node.meta;
    if (previewScript) previewScript.textContent = '"' + substitute(node.script) + '"';
    if (previewOutcome) {
      previewOutcome.textContent = node.outcome;
      previewOutcome.classList.toggle('is-end', !!node.end);
    }
    renderBranches(node);

    branchPills.forEach((p) => {
      if (!branchKeep) p.classList.remove('is-active');
    });
  }

  nodes.forEach((el) => {
    el.addEventListener('click', () => {
      setScreenshot(false);
      selectNode(el.getAttribute('data-flow-node'));
    });
  });

  branchPills.forEach((pill) => {
    pill.addEventListener('click', () => {
      setScreenshot(false);
      const branchId = pill.getAttribute('data-branch');
      selectBranch(branchId, NODE_DATA.hook);
    });
  });

  Object.values(vars).forEach((input) => {
    input?.addEventListener('input', () => {
      selectNode(state.activeNode, state.branch);
    });
  });

  shotToggle?.addEventListener('click', () => {
    setScreenshot(!state.screenshot);
  });

  tryLiveBtn?.addEventListener('click', () => {
    setScreenshot(false);
    setLayerSelected('flow-hook');
    selectNode('hook');
  });

  layerCards.forEach((card) => {
    function activate() {
      const detail = card.getAttribute('data-detail');
      const meta = LAYER_MAP[detail];
      if (!meta) return;
      setScreenshot(false);
      setLayerSelected(detail);
      if (meta.branch) {
        selectBranch(meta.branch, NODE_DATA.hook);
      } else {
        selectNode(meta.node);
      }
    }
    card.addEventListener('click', activate);
    card.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        activate();
      }
    });
  });

  setLayerSelected('flow-hook');
  selectNode('hook');
})();
