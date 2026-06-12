(function () {
  'use strict';

  var STEP_ORDER = ['ring', 'transcribe', 'analyze', 'act', 'learn'];
  var labels = {'ring': 'Ring — Call Connects', 'transcribe': 'Transcribe — Every Word Captured', 'analyze': 'Analyze — Score Live', 'act': 'Act — Triggers Fire', 'learn': 'Learn — Models Improve'};
  var detailMap = {'lc-ring': 'ring', 'lc-transcribe': 'transcribe', 'lc-analyze': 'analyze', 'lc-act': 'act', 'lc-learn': 'learn'};

  function init() {
    var root = document.getElementById('lcShowcase');
    if (!root) return;

    var stage = root.querySelector('.lc-sc-stage');
    var presentation = root.querySelector('.lc-sc-presentation');
    var nodes = Array.prototype.slice.call(root.querySelectorAll('.lc-sc-node'));
    var slideEls = Array.prototype.slice.call(root.querySelectorAll('.lc-sc-slide'));
    var layerCards = Array.prototype.slice.call(document.querySelectorAll('#journey .lc-layer-card'));
    var statusLabel = root.querySelector('[data-lc-status-label]');
    var metricEl = root.querySelector('[data-lc-metric]');
    var presProgress = root.querySelector('[data-lc-pres-progress]');
    var btnBack = root.querySelector('.lc-sc-back');
    var btnPrev = root.querySelector('.lc-sc-nav--prev');
    var btnNext = root.querySelector('.lc-sc-nav--next');
    var slidesViewport = root.querySelector('.lc-sc-slides-viewport');

    if (!stage || !presentation || !nodes.length || !slideEls.length) return;

    var slideMap = {};
    slideEls.forEach(function (slide) {
      var id = slide.getAttribute('data-slide');
      if (id) slideMap[id] = slide;
    });

    var stepIdx = 0;
    var isPresenting = false;
    var touchStartX = 0;
    var touchStartY = 0;

    function stepFromDetail(detail) {
      return detailMap[detail] || detail;
    }

    function indexForStep(step) {
      var i = STEP_ORDER.indexOf(step);
      return i >= 0 ? i : 0;
    }

    function clearSlideStates() {
      slideEls.forEach(function (slide) {
        slide.classList.remove('is-active');
        slide.setAttribute('aria-hidden', 'true');
      });
    }

    function setHubActive(step, scrollCard) {
      nodes.forEach(function (node) {
        var s = node.getAttribute('data-step');
        node.classList.toggle('is-active', s === step);
      });
      layerCards.forEach(function (card) {
        var d = stepFromDetail(card.getAttribute('data-detail'));
        card.classList.toggle('is-selected', d === step);
        if (d === step && !isPresenting && scrollCard) {
          card.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
        }
      });
      if (statusLabel && labels[step]) statusLabel.textContent = labels[step];
      if (metricEl) {
        var idx = indexForStep(step);
        metricEl.innerHTML = '<strong>' + (idx + 1) + '</strong> / 5 stages';
      }
    }

    function setSlideActive(index) {
      if (index < 0) index = STEP_ORDER.length - 1;
      if (index >= STEP_ORDER.length) index = 0;
      var targetId = STEP_ORDER[index];
      var targetSlide = slideMap[targetId];
      slideEls.forEach(function (slide) {
        var isTarget = slide === targetSlide;
        slide.classList.toggle('is-active', isTarget);
        slide.setAttribute('aria-hidden', isTarget ? 'false' : 'true');
      });
      stepIdx = index;
      setHubActive(targetId);
      if (presProgress) presProgress.innerHTML = '<strong>' + (index + 1) + '</strong> / 5';
    }

    function openPresentation(step) {
      isPresenting = true;
      stage.classList.add('is-presenting');
      root.classList.add('is-presenting');
      presentation.setAttribute('aria-hidden', 'false');
      setSlideActive(indexForStep(step));
    }

    function closePresentation() {
      isPresenting = false;
      stage.classList.remove('is-presenting');
      root.classList.remove('is-presenting');
      presentation.setAttribute('aria-hidden', 'true');
      clearSlideStates();
      setHubActive(STEP_ORDER[stepIdx]);
    }

    function nextSlide() { if (!isPresenting) return; setSlideActive(stepIdx + 1); }
    function prevSlide() { if (!isPresenting) return; setSlideActive(stepIdx - 1); }
    function selectStep(step) { if (STEP_ORDER.indexOf(step) < 0) return; openPresentation(step); }

    clearSlideStates();
    presentation.setAttribute('aria-hidden', 'true');
    setHubActive(STEP_ORDER[0]);

    nodes.forEach(function (node) {
      var step = node.getAttribute('data-step');
      node.addEventListener('click', function () { selectStep(step); });
      node.setAttribute('tabindex', '0');
      node.setAttribute('role', 'button');
      node.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); selectStep(step); }
      });
    });

    layerCards.forEach(function (card) {
      function activate() {
        var d = card.getAttribute('data-detail');
        if (d) selectStep(stepFromDetail(d));
      }
      card.addEventListener('click', activate);
      card.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); activate(); }
      });
    });

    if (btnBack) btnBack.addEventListener('click', function (e) { e.preventDefault(); closePresentation(); });
    if (btnPrev) btnPrev.addEventListener('click', function (e) { e.preventDefault(); prevSlide(); });
    if (btnNext) btnNext.addEventListener('click', function (e) { e.preventDefault(); nextSlide(); });

    root.addEventListener('keydown', function (e) {
      if (!isPresenting) return;
      if (e.key === 'ArrowRight') { e.preventDefault(); nextSlide(); }
      if (e.key === 'ArrowLeft') { e.preventDefault(); prevSlide(); }
      if (e.key === 'Escape') { e.preventDefault(); closePresentation(); }
    });

    if (slidesViewport) {
      slidesViewport.addEventListener('touchstart', function (e) {
        if (!isPresenting || !e.touches.length) return;
        touchStartX = e.touches[0].clientX;
        touchStartY = e.touches[0].clientY;
      }, { passive: true });
      slidesViewport.addEventListener('touchend', function (e) {
        if (!isPresenting || !e.changedTouches.length) return;
        var dx = e.changedTouches[0].clientX - touchStartX;
        var dy = e.changedTouches[0].clientY - touchStartY;
        if (Math.abs(dx) > Math.abs(dy) && Math.abs(dx) > 40) {
          if (dx < 0) nextSlide(); else prevSlide();
        }
      }, { passive: true });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
