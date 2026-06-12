(function () {
  'use strict';

  var STEP_ORDER = ['real-estate', 'appointment-reminder', 'appointment-booking', 'nps-review', 'event-agent', 'recruiter-outreach', 'payment-checkin', 'support-playbook', 'order-returns', 'financial-assistant', 'customer-reactivation', 'job-applicant', 'distributor-collection', 'fashion-event'];

  var labels = {'real-estate': 'Real Estate Lead Qualificati', 'appointment-reminder': 'Contextual Appointment Remin', 'appointment-booking': 'Appointment Booking', 'nps-review': 'Insightful NPS Review', 'event-agent': 'High-Conversion Event Agent', 'recruiter-outreach': 'Recruiter-grade Outreach', 'payment-checkin': 'Friendly Payment Check-in', 'support-playbook': 'Intelligent Support Playbook', 'order-returns': 'Order, Refund & Returns', 'financial-assistant': 'Financial Assistant', 'customer-reactivation': 'High-Conversion Customer Rea', 'job-applicant': 'Job Applicant Concierge', 'distributor-collection': 'Distributor Payment Collecti', 'fashion-event': 'Fashion Event Registration C'};

  var detailMap = {'agt-real-estate': 'real-estate', 'agt-appointment-reminder': 'appointment-reminder', 'agt-appointment-booking': 'appointment-booking', 'agt-nps-review': 'nps-review', 'agt-event-agent': 'event-agent', 'agt-recruiter-outreach': 'recruiter-outreach', 'agt-payment-checkin': 'payment-checkin', 'agt-support-playbook': 'support-playbook', 'agt-order-returns': 'order-returns', 'agt-financial-assistant': 'financial-assistant', 'agt-customer-reactivation': 'customer-reactivation', 'agt-job-applicant': 'job-applicant', 'agt-distributor-collection': 'distributor-collection', 'agt-fashion-event': 'fashion-event'};

  function init() {
    var root = document.getElementById('agtShowcase');
    if (!root) return;

    var stage = root.querySelector('.agt-sc-stage');
    var presentation = root.querySelector('.agt-sc-presentation');
    var nodes = Array.prototype.slice.call(root.querySelectorAll('.agt-sc-node'));
    var slideEls = Array.prototype.slice.call(root.querySelectorAll('.agt-sc-slide'));
    var layerCards = Array.prototype.slice.call(document.querySelectorAll('#agents .agt-layer-card'));
    var statusLabel = root.querySelector('[data-agt-status-label]');
    var metricEl = root.querySelector('[data-agt-metric]');
    var presProgress = root.querySelector('[data-agt-pres-progress]');
    var btnBack = root.querySelector('.agt-sc-back');
    var btnPrev = root.querySelector('.agt-sc-nav--prev');
    var btnNext = root.querySelector('.agt-sc-nav--next');
    var slidesViewport = root.querySelector('.agt-sc-slides-viewport');

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

    function setFleetActive(step, scrollCard) {
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
      if (statusLabel && labels[step]) {
        statusLabel.textContent = labels[step];
      }
      if (metricEl) {
        var idx = indexForStep(step);
        metricEl.innerHTML = '<strong>' + (idx + 1) + '</strong> / ' + STEP_ORDER.length + ' templates';
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
      setFleetActive(targetId);
      if (presProgress) {
        presProgress.innerHTML = '<strong>' + (index + 1) + '</strong> / ' + STEP_ORDER.length;
      }
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
      setFleetActive(STEP_ORDER[stepIdx]);
    }

    function nextSlide() { if (!isPresenting) return; setSlideActive(stepIdx + 1); }
    function prevSlide() { if (!isPresenting) return; setSlideActive(stepIdx - 1); }
    function selectStep(step) { if (STEP_ORDER.indexOf(step) < 0) return; openPresentation(step); }

    clearSlideStates();
    presentation.setAttribute('aria-hidden', 'true');
    setFleetActive(STEP_ORDER[0]);

    nodes.forEach(function (node) {
      var step = node.getAttribute('data-step');
      node.setAttribute('tabindex', '0');
      node.setAttribute('role', 'button');
      node.addEventListener('click', function (e) { e.preventDefault(); e.stopPropagation(); selectStep(step); });
      node.addEventListener('mouseenter', function () { if (!isPresenting) setFleetActive(step, true); });
      node.addEventListener('mouseleave', function () { if (!isPresenting) setFleetActive(STEP_ORDER[0], false); });
      node.addEventListener('keydown', function (e) {
        if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); selectStep(step); }
      });
    });

    layerCards.forEach(function (card) {
      var step = stepFromDetail(card.getAttribute('data-detail'));
      card.addEventListener('click', function (e) {
        e.preventDefault(); e.stopPropagation(); e.stopImmediatePropagation();
        selectStep(step);
      }, true);
      card.addEventListener('mouseenter', function () { if (!isPresenting) setFleetActive(step, true); });
      card.addEventListener('mouseleave', function () { if (!isPresenting) setFleetActive(STEP_ORDER[0], false); });
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
