(function () {
  const tabs = document.querySelectorAll('.auth-tab');
  const loginForm = document.getElementById('loginForm');
  const signupForm = document.getElementById('signupForm');
  const panelTitle = document.getElementById('authPanelTitle');
  const panelDesc = document.getElementById('authPanelDesc');
  const switchFoot = document.getElementById('authSwitchFoot');
  const toast = document.getElementById('authToast');
  const signupPassword = document.getElementById('signupPassword');
  const meterBar = document.querySelector('.auth-meter-bar');
  const meterHint = document.querySelector('.auth-meter-hint');

  const copy = {
    login: {
      title: 'Welcome back',
      desc: 'Pick up where you left off — campaigns, agents, and live intelligence.',
      footHtml:
        'New to EMAAVY? <button type="button" data-auth-switch="signup">Create your workspace</button>',
    },
    signup: {
      title: 'Start exploring',
      desc: 'Free trial · no credit card · full platform access in minutes.',
      footHtml:
        'Already have an account? <button type="button" data-auth-switch="login">Log in</button>',
    },
  };

  function setMode(mode) {
    const isLogin = mode === 'login';
    tabs.forEach((t) => {
      const on = t.dataset.authTab === mode;
      t.classList.toggle('is-active', on);
      t.setAttribute('aria-selected', on ? 'true' : 'false');
    });
    loginForm?.classList.toggle('is-active', isLogin);
    signupForm?.classList.toggle('is-active', !isLogin);
    if (panelTitle) panelTitle.textContent = copy[mode].title;
    if (panelDesc) panelDesc.textContent = copy[mode].desc;
    if (switchFoot) switchFoot.innerHTML = copy[mode].footHtml;
    document.title = isLogin ? 'Log In — EMAAVY' : 'Sign Up — EMAAVY';
    bindSwitchButtons();
  }

  function bindSwitchButtons() {
    switchFoot?.querySelectorAll('[data-auth-switch]').forEach((btn) => {
      btn.addEventListener('click', () => setMode(btn.dataset.authSwitch));
    });
  }

  tabs.forEach((tab) => {
    tab.addEventListener('click', () => setMode(tab.dataset.authTab));
  });

  function showToast(message) {
    if (!toast) return;
    toast.textContent = message;
    toast.classList.add('is-visible');
    setTimeout(() => toast.classList.remove('is-visible'), 4200);
  }

  function passwordStrength(value) {
    let score = 0;
    if (value.length >= 8) score++;
    if (/[A-Z]/.test(value) && /[a-z]/.test(value)) score++;
    if (/\d/.test(value)) score++;
    if (/[^A-Za-z0-9]/.test(value)) score++;
    return score;
  }

  signupPassword?.addEventListener('input', () => {
    const v = signupPassword.value;
    const score = passwordStrength(v);
    const pct = v ? (score / 4) * 100 : 0;
    if (meterBar) meterBar.style.width = pct + '%';
    const hints = ['', 'Add 8+ characters', 'Mix upper & lower case', 'Add a number', 'Strong password'];
    if (meterHint) meterHint.textContent = v ? hints[score] || hints[4] : 'Use 8+ characters with letters and numbers';
  });

  loginForm?.addEventListener('submit', (e) => {
    e.preventDefault();
    showToast('Welcome back — redirecting to your workspace…');
  });

  signupForm?.addEventListener('submit', (e) => {
    e.preventDefault();
    const pwd = signupPassword?.value || '';
    const confirm = document.getElementById('signupConfirm')?.value || '';
    if (pwd !== confirm) {
      showToast('Passwords do not match — please try again.');
      return;
    }
    if (passwordStrength(pwd) < 2) {
      showToast('Choose a stronger password to secure your workspace.');
      return;
    }
    showToast('Account created — welcome to EMAAVY. Explore the platform!');
  });

  document.querySelectorAll('.auth-social-btn').forEach((btn) => {
    btn.addEventListener('click', () => {
      showToast('Social sign-in will connect here — use email for now.');
    });
  });

  const params = new URLSearchParams(window.location.search);
  setMode(params.get('mode') === 'signup' ? 'signup' : 'login');
})();
