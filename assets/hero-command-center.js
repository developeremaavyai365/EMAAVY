(function () {
  'use strict';

  var STORY_ORDER = [
    'agents', 'telephony', 'whatsapp', 'crm', 'workflows', 'campaigns',
    'integrations', 'analytics', 'knowledge', 'automation', 'support', 'sales'
  ];

  var labels = {
    agents: 'Agent orchestration',
    telephony: 'Call routing',
    whatsapp: 'Channel sync',
    crm: 'CRM pipeline',
    campaigns: 'Campaign execution',
    workflows: 'Workflow run',
    integrations: 'Ecosystem sync',
    analytics: 'Insight pipeline',
    knowledge: 'Knowledge index',
    automation: 'Automation run',
    support: 'Support queue',
    sales: 'Revenue operations'
  };

  function init() {
    var root = document.getElementById('heroVisual');
    if (!root || !root.classList.contains('hero-command-center')) return;

    var stage = root.querySelector('.hcc-stage');
    var svg = root.querySelector('.hcc-connections');
    var nodes = Array.prototype.slice.call(root.querySelectorAll('.hcc-node'));
    var presentation = root.querySelector('.hcc-presentation');
    var slideEls = Array.prototype.slice.call(root.querySelectorAll('.hcc-slide'));
    var statusLabel = root.querySelector('[data-hcc-status-label]');
    var metricEl = root.querySelector('[data-hcc-metric]');
    var presProgress = root.querySelector('[data-hcc-pres-progress]');
    var btnBack = root.querySelector('.hcc-pres-back');
    var btnPrev = root.querySelector('.hcc-pres-nav--prev');
    var btnNext = root.querySelector('.hcc-pres-nav--next');
    var slidesViewport = root.querySelector('.hcc-slides-viewport');

    if (!stage || !nodes.length || !presentation || !slideEls.length) return;

    var slideMap = {};
    slideEls.forEach(function (slide) {
      var id = slide.getAttribute('data-slide');
      if (id) slideMap[id] = slide;
    });

    var orbitIdx = 0;
    var slideIdx = 0;
    var isPresenting = false;
    var touchStartX = 0;
    var touchStartY = 0;

    function systemForOrbitNode(node) {
      return node.getAttribute('data-system');
    }

    function slideIndexForSystem(system) {
      var i = STORY_ORDER.indexOf(system);
      return i >= 0 ? i : 0;
    }

    function clearSlideStates() {
      slideEls.forEach(function (slide) {
        slide.classList.remove('is-active');
        slide.setAttribute('aria-hidden', 'true');
      });
    }

    function setOrbitActive(index) {
      nodes.forEach(function (node, i) {
        node.classList.toggle('is-active', i === index);
      });
      var key = nodes[index] && systemForOrbitNode(nodes[index]);
      if (statusLabel && key && labels[key]) {
        statusLabel.textContent = labels[key];
      }
      if (metricEl) {
        metricEl.innerHTML = '<strong>' + (index + 1) + '</strong> / ' + nodes.length + ' systems live';
      }
      orbitIdx = index;
    }

    function highlightOrbitForSystem(system) {
      nodes.forEach(function (node) {
        var s = systemForOrbitNode(node);
        node.classList.toggle('is-active', s === system);
      });
      if (statusLabel && labels[system]) {
        statusLabel.textContent = labels[system];
      }
    }

    function setSlideActive(index) {
      if (index < 0) index = STORY_ORDER.length - 1;
      if (index >= STORY_ORDER.length) index = 0;

      var targetId = STORY_ORDER[index];
      var targetSlide = slideMap[targetId];

      slideEls.forEach(function (slide) {
        var isTarget = slide === targetSlide;
        slide.classList.toggle('is-active', isTarget);
        slide.setAttribute('aria-hidden', isTarget ? 'false' : 'true');
      });

      slideIdx = index;
      if (presProgress) {
        presProgress.innerHTML = '<strong>' + (index + 1) + '</strong> / ' + STORY_ORDER.length;
      }
      if (statusLabel && labels[targetId]) {
        statusLabel.textContent = labels[targetId];
      }
    }

    function openPresentation(system) {
      var idx = slideIndexForSystem(system);
      var nodeIdx = nodes.findIndex(function (n) {
        return systemForOrbitNode(n) === system;
      });
      if (nodeIdx >= 0) setOrbitActive(nodeIdx);

      isPresenting = true;
      stage.classList.add('is-presenting');
      root.classList.add('is-presenting');
      presentation.setAttribute('aria-hidden', 'false');
      setSlideActive(idx);
    }

    function closePresentation() {
      isPresenting = false;
      stage.classList.remove('is-presenting');
      root.classList.remove('is-presenting');
      presentation.setAttribute('aria-hidden', 'true');
      clearSlideStates();
      setOrbitActive(orbitIdx);
      window.requestAnimationFrame(syncConnectionPaths);
    }

    function nextSlide() {
      if (!isPresenting) return;
      setSlideActive(slideIdx + 1);
    }

    function prevSlide() {
      if (!isPresenting) return;
      setSlideActive(slideIdx - 1);
    }

    function syncConnectionPaths() {
      if (!svg || !stage || isPresenting) return;
      var stageRect = stage.getBoundingClientRect();
      if (stageRect.width < 1 || stageRect.height < 1) return;
      var cx = 300;
      var cy = 300;
      var scaleX = 600 / stageRect.width;
      var scaleY = 600 / stageRect.height;
      var paths = svg.querySelectorAll('[data-hcc-link]');
      paths.forEach(function (pathEl) {
        var system = pathEl.getAttribute('data-hcc-link');
        var node = root.querySelector('.hcc-node[data-system="' + system + '"] .hcc-node-card');
        if (!node) return;
        var rect = node.getBoundingClientRect();
        var nx = (rect.left + rect.width / 2 - stageRect.left) * scaleX;
        var ny = (rect.top + rect.height / 2 - stageRect.top) * scaleY;
        var qx = (cx + nx) / 2 + (ny - cy) * 0.08;
        var qy = (cy + ny) / 2 - (nx - cx) * 0.08;
        pathEl.setAttribute('d', 'M' + cx + ' ' + cy + ' Q' + qx + ' ' + qy + ' ' + nx + ' ' + ny);
      });
    }

    clearSlideStates();
    presentation.setAttribute('aria-hidden', 'true');
    setOrbitActive(0);
    syncConnectionPaths();

    nodes.forEach(function (node) {
      var system = systemForOrbitNode(node);
      node.setAttribute('tabindex', '0');
      node.setAttribute('role', 'button');
      var titleEl = node.querySelector('.hcc-node-title');
      node.setAttribute('aria-label', 'Open ' + ((titleEl && titleEl.textContent) || system) + ' presentation');

      node.addEventListener('click', function (e) {
        e.preventDefault();
        e.stopPropagation();
        openPresentation(system);
      });

      node.addEventListener('mouseenter', function () {
        if (!isPresenting) highlightOrbitForSystem(system);
      });

      node.addEventListener('mouseleave', function () {
        if (!isPresenting) setOrbitActive(orbitIdx);
      });

      node.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') {
          e.preventDefault();
          openPresentation(system);
        }
      });
    });

    if (btnBack) {
      btnBack.addEventListener('click', function (e) {
        e.preventDefault();
        closePresentation();
      });
    }
    if (btnPrev) {
      btnPrev.addEventListener('click', function (e) {
        e.preventDefault();
        prevSlide();
      });
    }
    if (btnNext) {
      btnNext.addEventListener('click', function (e) {
        e.preventDefault();
        nextSlide();
      });
    }

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
          if (dx < 0) nextSlide();
          else prevSlide();
        }
      }, { passive: true });
    }

    var resizeTimer;
    window.addEventListener('resize', function () {
      window.clearTimeout(resizeTimer);
      resizeTimer = window.setTimeout(syncConnectionPaths, 80);
    });

    if (typeof ResizeObserver !== 'undefined') {
      var ro = new ResizeObserver(function () {
        syncConnectionPaths();
      });
      ro.observe(stage);
    }

    window.setTimeout(syncConnectionPaths, 120);
    window.setTimeout(syncConnectionPaths, 500);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
