(function () {
  const root = document.getElementById('campaignsShowcase');
  if (!root) return;

  const device = root.querySelector('.campaigns-device');
  const screenType = root.querySelector('[data-camp-screen="type"]');
  const screenAudience = root.querySelector('[data-camp-screen="audience"]');
  const continueBtn = root.querySelector('.camp-type-continue');
  const typeCards = root.querySelectorAll('.camp-type-card');
  const backBtn = root.querySelector('.camp-app-back');
  const doneBtn = root.querySelector('.camp-app-done');
  const nameInput = root.querySelector('#campCampaignName');
  const dropzone = root.querySelector('.camp-dropzone');
  const fileInput = root.querySelector('#campContactsFile');
  const stripBtns = root.querySelectorAll('[data-camp-shot]');
  const shotImg = root.querySelector('.campaigns-device-shot');

  const previewName = root.querySelector('[data-preview="name"]');
  const previewType = root.querySelector('[data-preview="type"]');
  const previewContacts = root.querySelector('[data-preview="contacts"]');
  const previewTags = root.querySelector('[data-preview="tags"]');
  const previewSteps = root.querySelectorAll('.camp-preview-steps li');
  const wizardSubtitle = root.querySelector('#campWizardSubtitle');
  const uploadCard = root.querySelector('#campUploadCard');

  const state = {
    type: null,
    name: '',
    tags: new Set(),
    contacts: 0,
    fileName: '',
    screen: 'type',
    screenshot: false,
  };

  function setScreen(id) {
    state.screen = id;
    screenType?.classList.toggle('is-active', id === 'type');
    screenAudience?.classList.toggle('is-active', id === 'audience');
    root.querySelectorAll('[data-camp-screen]').forEach((el) => {
      el.classList.toggle('is-active', el.getAttribute('data-camp-screen') === id);
    });
    if (device) {
      device.classList.toggle('is-screenshot-mode', state.screenshot);
    }
    updatePreviewSteps();
    syncStrip();
  }

  function syncStrip() {
    stripBtns.forEach((btn) => {
      const shot = btn.getAttribute('data-camp-shot');
      const active =
        state.screenshot &&
        ((shot === 'type' && state.screen === 'type') ||
          (shot === 'audience' && state.screen === 'audience'));
      btn.classList.toggle('is-active', active);
    });
  }

  function renderPreview() {
    const name = state.name.trim() || 'Untitled Campaign';
    if (previewName) previewName.textContent = name;
    if (previewType) {
      if (!state.type) {
        previewType.textContent = '—';
      } else {
        previewType.textContent =
          state.type === 'outbound' ? 'Outbound' : 'Inbound';
      }
    }
    if (previewContacts) {
      previewContacts.textContent =
        state.contacts > 0
          ? state.contacts.toLocaleString() + ' contacts'
          : '—';
    }
    if (previewTags) {
      previewTags.textContent =
        state.tags.size > 0 ? Array.from(state.tags).join(', ') : '—';
    }
    if (doneBtn) {
      doneBtn.classList.toggle(
        'is-ready',
        state.type && state.name.trim().length > 0
      );
    }
  }

  function updatePreviewSteps() {
    const currentIdx = state.screen === 'type' ? -1 : 0;
    previewSteps.forEach((li, i) => {
      li.classList.remove('is-current', 'is-done');
      if (i < currentIdx) li.classList.add('is-done');
      if (i === currentIdx) li.classList.add('is-current');
    });
    root.querySelectorAll('.camp-step').forEach((step, i) => {
      step.classList.remove('is-current', 'is-done');
      if (state.screen === 'audience') {
        if (i === 0) step.classList.add('is-current');
        if (i < 0) step.classList.add('is-done');
      }
    });
    root.querySelectorAll('.camp-step-connector').forEach((c, i) => {
      c.classList.toggle('is-done', state.screen === 'audience' && i === 0);
    });
  }

  function selectType(type) {
    state.type = type;
    state.screenshot = false;
    if (device) device.classList.remove('is-screenshot-mode');
    typeCards.forEach((card) => {
      card.classList.toggle('is-selected', card.getAttribute('data-type') === type);
    });
    continueBtn?.classList.add('is-enabled');
    stripBtns.forEach((b) => b.classList.remove('is-active'));
    if (wizardSubtitle) {
      wizardSubtitle.textContent =
        'Configure your ' +
        type +
        ' campaign in 5 guided steps.';
    }
    if (uploadCard) {
      uploadCard.hidden = type === 'inbound';
    }
    renderPreview();
  }

  typeCards.forEach((card) => {
    card.addEventListener('click', () => {
      selectType(card.getAttribute('data-type'));
    });
    card.addEventListener('keydown', (e) => {
      if (e.key === 'Enter' || e.key === ' ') {
        e.preventDefault();
        selectType(card.getAttribute('data-type'));
      }
    });
    card.setAttribute('tabindex', '0');
    card.setAttribute('role', 'button');
  });

  continueBtn?.addEventListener('click', () => {
    if (!state.type) return;
    state.screenshot = false;
    if (device) device.classList.remove('is-screenshot-mode');
    setScreen('audience');
    nameInput?.focus();
  });

  backBtn?.addEventListener('click', () => {
    state.screenshot = false;
    if (device) device.classList.remove('is-screenshot-mode');
    setScreen('type');
  });

  nameInput?.addEventListener('input', () => {
    state.name = nameInput.value;
    renderPreview();
  });

  root.querySelectorAll('.camp-tag').forEach((tag) => {
    tag.addEventListener('click', () => {
      const val = tag.getAttribute('data-tag');
      if (!val) return;
      if (state.tags.has(val)) state.tags.delete(val);
      else state.tags.add(val);
      tag.classList.toggle('is-on', state.tags.has(val));
      renderPreview();
    });
  });

  function simulateContacts(file) {
    if (!file) return;
    state.fileName = file.name;
    const ext = file.name.split('.').pop()?.toLowerCase() || '';
    const base = Math.max(120, Math.min(8500, file.size / 8 + file.name.length * 40));
    state.contacts = ext === 'csv' ? Math.round(base) : Math.round(base * 1.1);
    dropzone?.classList.add('has-file');
    const strong = dropzone?.querySelector('strong');
    const p = dropzone?.querySelector('p');
    if (strong) strong.textContent = file.name;
    if (p) p.textContent = state.contacts.toLocaleString() + ' contacts ready to dial';
    renderPreview();
  }

  dropzone?.addEventListener('click', () => fileInput?.click());

  dropzone?.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropzone.classList.add('is-dragover');
  });

  dropzone?.addEventListener('dragleave', () => {
    dropzone.classList.remove('is-dragover');
  });

  dropzone?.addEventListener('drop', (e) => {
    e.preventDefault();
    dropzone.classList.remove('is-dragover');
    const file = e.dataTransfer?.files?.[0];
    if (file) simulateContacts(file);
  });

  fileInput?.addEventListener('change', () => {
    const file = fileInput.files?.[0];
    if (file) simulateContacts(file);
  });

  stripBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      const shot = btn.getAttribute('data-camp-shot');
      state.screenshot = true;
      if (shot === 'type') setScreen('type');
      else setScreen('audience');
      if (shotImg) {
        shotImg.src =
          shot === 'type'
            ? 'assets/campaigns/create-campaign-type.png'
            : 'assets/campaigns/create-campaign-audience.png';
        shotImg.alt =
          shot === 'type'
            ? 'EMAAVY choose campaign type screen'
            : 'EMAAVY campaign audience configuration screen';
      }
      if (device) device.classList.add('is-screenshot-mode');
      syncStrip();
    });
  });

  root.querySelector('.campaigns-try-live')?.addEventListener('click', () => {
    state.screenshot = false;
    if (device) device.classList.remove('is-screenshot-mode');
    stripBtns.forEach((b) => b.classList.remove('is-active'));
    setScreen(state.screen || 'type');
  });

  doneBtn?.addEventListener('click', () => {
    if (!state.type || !state.name.trim()) return;
    const demo = document.querySelector('[data-open-demo]');
    if (demo) demo.click();
    else window.location.href = 'book-demo.html';
  });

  setScreen('type');
  renderPreview();
})();
