"""Generates the six site pages from shared head, nav, footer, and form snippets.
Run from anywhere: python3 tools/build_pages.py
Edit copy here, not in the generated HTML, or the next run overwrites it."""
import os
SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STYLE_VERSION = "20260917e"  # bump when styles.css changes so browsers fetch the new file
FORM_APPLY = "https://formspree.io/f/mgoqbjbw"
FORM_AUDIT = "https://formspree.io/f/mnpnqnyd"

LOGO = '''<svg viewBox="0 0 200 44" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="LocalScaling"><path d="M22 3C14.82 3 9 8.82 9 16C9 25.5 22 41 22 41C22 41 35 25.5 35 16C35 8.82 29.18 3 22 3Z" stroke="#002c0a" stroke-width="2.5" fill="none"/><circle cx="22" cy="16" r="4.5" stroke="#002c0a" stroke-width="2.5" fill="none"/><text x="46" y="30" font-family="League Spartan, sans-serif" font-weight="800" font-size="22" fill="#002c0a" letter-spacing="-0.5">LocalScaling</text></svg>'''

TICK = '<svg viewBox="0 0 24 24" aria-hidden="true"><polyline points="20 6 9 17 4 12"/></svg>'

def head(title, desc, path, robots="index, follow"):
    url = "https://www.localscaling.com" + path
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="google-site-verification" content="vuhUFodBG7Lhvyset2w9S04fy0lGlzcXcztLsg1d1nk" />
<link rel="icon" href="/favicon.ico" sizes="32x32">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="LocalScaling">
<meta name="theme-color" content="#0e5a38">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;500;600;700;800&family=League+Spartan:wght@800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/styles.css?v={STYLE_VERSION}">
</head>
<body>
<a class="skip-link" href="#main">Skip to content</a>
'''

NAV = f'''
<header class="nav">
  <div class="nav-inner">
    <a class="logo" href="/">{LOGO}</a>
    <nav class="nav-links" aria-label="Primary">
      <a href="/apply">Apply</a>
      <a href="/free-seo-audit" class="btn btn-primary btn-sm">Get a free audit</a>
    </nav>
  </div>
</header>
'''

NAV_MIN = f'''
<header class="nav">
  <div class="nav-inner">
    <a class="logo" href="/">{LOGO}</a>
    <nav class="nav-links" aria-label="Primary">
      <a href="/">Back to site</a>
    </nav>
  </div>
</header>
'''

FOOTER = f'''
<footer class="footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a class="logo" href="/">{LOGO}</a>
        <p>Local SEO for contractors and home service businesses. One operator, month to month, results guaranteed.</p>
      </div>
      <nav class="footer-col" aria-label="Pages">
        <h3>Pages</h3>
        <a href="/">Home</a>
        <a href="/free-seo-audit">Free audit</a>
        <a href="/apply">Apply</a>
        <a href="/locations/los-angeles">Los Angeles</a>
      </nav>
      <div class="footer-col">
        <h3>Start here</h3>
        <p>See where you are losing calls before you spend anything.</p>
        <a href="/free-seo-audit" class="btn btn-light btn-sm">Get a free audit</a>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© 2026 LocalScaling</span>
      <a href="mailto:info@localscaling.com">info@localscaling.com</a>
    </div>
  </div>
</footer>
'''

STICKY = """
<div class="sticky-cta" aria-hidden="false">
  <span>Free audit, no call, in your inbox within 24 hours.</span>
  <a href="/free-seo-audit" class="btn btn-clay btn-sm">Get a free audit</a>
</div>
"""

REVEAL_JS = """
<script>
  (function () {
    var els = document.querySelectorAll('.reveal');
    if (!('IntersectionObserver' in window) || window.matchMedia('(prefers-reduced-motion: reduce)').matches) {
      els.forEach(function (el) { el.classList.add('in'); }); return;
    }
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
    }, { rootMargin: '0px 0px -8% 0px', threshold: 0.1 });
    els.forEach(function (el) { io.observe(el); });
  })();
  (function () {
    var bar = document.querySelector('.sticky-cta');
    var hero = document.querySelector('.hero-actions');
    if (!bar || !hero || !('IntersectionObserver' in window)) { if (bar) bar.classList.add('show'); return; }
    new IntersectionObserver(function (entries) {
      bar.classList.toggle('show', !entries[0].isIntersecting && entries[0].boundingClientRect.top < 0);
    }).observe(hero);
  })();
</script>
"""

TEST_JS = """
<script>
  (function () {
    var form = document.getElementById('testForm');
    if (!form) return;
    var result = document.getElementById('testResult');
    var yes = document.getElementById('testYes');
    var no = document.getElementById('testNo');
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var trade = document.getElementById('tTrade').value.trim();
      var city = document.getElementById('tCity').value.trim();
      if (!trade || !city) { (trade ? document.getElementById('tCity') : document.getElementById('tTrade')).focus(); return; }
      var q = encodeURIComponent(trade + ' ' + city);
      window.open('https://www.google.com/maps/search/' + q, '_blank', 'noopener');
      result.classList.add('show');
      yes.classList.remove('show'); no.classList.remove('show');
      result.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
    });
    document.getElementById('choiceYes').addEventListener('click', function () { yes.classList.add('show'); no.classList.remove('show'); });
    document.getElementById('choiceNo').addEventListener('click', function () { no.classList.add('show'); yes.classList.remove('show'); });
  })();
</script>
"""

def cta(h, p):
    return f'''
<section class="bg-forest cta topo" aria-labelledby="cta-title">
  <div class="container">
    <h2 id="cta-title">{h}</h2>
    <p class="lede">{p}</p>
    <div class="cta-actions">
      <a href="/free-seo-audit" class="btn btn-light">Get a free audit</a>
      <a href="/apply" class="btn btn-ghost">Apply now</a>
    </div>
    <p class="cta-note">The audit is free and comes with no obligation.</p>
  </div>
</section>
'''

def point(title, text):
    return f'''
      <div class="point">
        <div class="point-icon">{TICK}</div>
        <div><h3>{title}</h3><p>{text}</p></div>
      </div>'''

FORM_JS = '''
<script>
  document.getElementById('%(form)s').addEventListener('submit', async function(e) {
    e.preventDefault();
    const btn = document.getElementById('submitBtn');
    const submitText = document.getElementById('submitText');
    const spinner = document.getElementById('submitSpinner');
    const errorDiv = document.getElementById('formError');

    errorDiv.style.display = 'none';
    this.querySelectorAll('input, select').forEach(el => { el.classList.remove('error'); el.removeAttribute('aria-invalid'); });

    let valid = true;
    let first = null;
    %(ids)s.forEach(id => {
      const el = document.getElementById(id);
      if (!el.value.trim()) { el.classList.add('error'); el.setAttribute('aria-invalid', 'true'); valid = false; first = first || el; }
    });
    if (!valid) { first.focus(); return; }

    btn.disabled = true;
    submitText.style.display = 'none';
    spinner.style.display = 'block';

    try {
      const res = await fetch(this.action, {
        method: 'POST',
        body: new FormData(this),
        headers: { 'Accept': 'application/json' }
      });
      if (res.ok) {
        window.location.href = '%(next)s';
      } else {
        throw new Error();
      }
    } catch {
      errorDiv.style.display = 'block';
      btn.disabled = false;
      submitText.style.display = 'inline';
      spinner.style.display = 'none';
    }
  });
</script>
'''

# ---------------- INDEX ----------------
def neighborhood_map():
    blocks = []
    park = (2, 2)
    for col in range(7):
        for row in range(6):
            x = 10 + col * 76; y = 10 + row * 64
            fill = "#bfe0c9" if (col, row) == park else "#d3e0d8"
            blocks.append(f'<rect x="{x}" y="{y}" width="60" height="50" rx="5" fill="{fill}"/>')
    pin = 'M12 2C7 2 3 6 3 11c0 6.5 9 17 9 17s9-10.5 9-17c0-5-4-9-9-9z'
    def pin_at(x, y, color, ring=False):
        out = ""
        if ring:
            out += f'<circle class="radius" cx="{x}" cy="{y}" r="112" fill="#e39b2c" fill-opacity="0.10" stroke="#e39b2c" stroke-width="1.5" stroke-dasharray="6 6"/>'
        out += f'<g transform="translate({x-16},{y-38}) scale(1.35)"><path d="{pin}" fill="{color}" stroke="#ffffff" stroke-width="1.2"/><circle cx="12" cy="11" r="3.2" fill="#ffffff"/></g>'
        return out
    return f'''<svg viewBox="0 0 520 380" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Illustration of a neighborhood map with a service radius drawn around your business">
  <rect width="520" height="380" fill="#e6eee9"/>
  {"".join(blocks)}
  <path d="M-10 330 C 120 300, 200 180, 330 140 S 480 40, 540 20" stroke="#ffffff" stroke-width="16" fill="none" stroke-linecap="round"/>
  <path d="M-10 330 C 120 300, 200 180, 330 140 S 480 40, 540 20" stroke="#b9cbc0" stroke-width="1.5" fill="none" stroke-dasharray="10 10"/>
  {pin_at(118, 128, "#6f8478")}
  {pin_at(402, 262, "#6f8478")}
  {pin_at(262, 206, "#e39b2c", ring=True)}
  <rect x="290" y="184" width="118" height="30" rx="15" fill="#0f1c15"/>
  <text x="349" y="204" text-anchor="middle" font-family="Plus Jakarta Sans, Arial, sans-serif" font-size="13" font-weight="700" fill="#ffffff">Your business</text>
</svg>'''

def sheet_row(title, sub):
    return f'''
        <li class="sheet-row">
          <span class="sheet-box">{TICK}</span>
          <span><strong>{title}</strong><span>{sub}</span></span>
        </li>'''

def step(n, title, text):
    return f'''
      <div class="step reveal reveal-{n}">
        <div class="step-num" aria-hidden="true">{n}</div>
        <h3>{title}</h3>
        <p>{text}</p>
      </div>'''

def service(icon, title, text):
    return f'''
      <div class="card reveal">
        <div class="card-icon" aria-hidden="true">{icon}</div>
        <h3>{title}</h3>
        <p>{text}</p>
      </div>'''

def faq(q, a):
    return f'''
      <details class="faq-item">
        <summary>{q}</summary>
        <p>{a}</p>
      </details>'''

ICON_PIN = '<svg viewBox="0 0 24 24"><path d="M12 2C8.13 2 5 5.13 5 9c0 5.25 7 13 7 13s7-7.75 7-13c0-3.87-3.13-7-7-7z"/><circle cx="12" cy="9" r="2.5"/></svg>'
ICON_LIST = '<svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 9h10M7 13h10M7 17h6"/></svg>'
ICON_PAGES = '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18M9 21V9"/></svg>'
ICON_STAR = '<svg viewBox="0 0 24 24"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>'
ICON_CHART = '<svg viewBox="0 0 24 24"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>'
ICON_SITE = '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 9h18"/><path d="M7 13h4M7 17h8"/></svg>'

index = head(
  "Local SEO for Service Businesses | LocalScaling",
  "LocalScaling gets local service businesses to the top of Google Maps and organic search. Starting at $1,500/mo with a results guarantee. Built for contractors and home service businesses.",
  "/",
).replace("<body>", "<body class=\"has-sticky\">") + NAV + f'''
<main id="main">
<section class="hero topo" aria-labelledby="hero-title">
  <div class="container hero-grid">
    <div>
      <p class="eyebrow">Local SEO for service businesses</p>
      <h1 id="hero-title">More calls.<br>More jobs.<br><em>Zero ad spend.</em></h1>
      <p class="lede">We get contractors and home service companies to the top of Google Maps in the neighborhoods they work. Stop renting leads and start owning them.</p>
      <div class="hero-actions">
        <a href="/free-seo-audit" class="btn btn-clay">Get a free audit</a>
        <a href="/apply" class="text-link">Or apply to work with us</a>
      </div>
      <p class="cta-note"><strong>Free.</strong> No call required. Sent to your inbox within 24 hours.</p>
      <ul class="hero-facts">
        <li>{TICK}Starting at $1,500/mo</li>
        <li>{TICK}Month to month</li>
        <li>{TICK}Results guarantee</li>
      </ul>
    </div>
    <div class="map-visual">
      <div class="map-frame">
        {neighborhood_map()}
        <div class="map-caption">
          <strong>Your service radius</strong>
          <span>Google ranks your profile by distance from the searcher. We find out how far yours reaches, then push it outward.</span>
        </div>
      </div>
    </div>
  </div>
</section>

<div class="trades" aria-label="Trades we work with">
  <div class="container trades-inner">
    <strong>Built for the trades</strong>
    <span>Restoration</span><span>Plumbing</span><span>HVAC</span><span>Roofing</span><span>Garage doors</span><span>Electrical</span><span>Landscaping</span>
  </div>
</div>

<section class="test" aria-labelledby="test-title">
  <div class="container">
    <div class="test-card reveal">
      <div>
        <p class="eyebrow">The ten second test</p>
        <h2 id="test-title">Are you in the top three right now?</h2>
        <p>Type your trade and city. We'll open the real Google Maps result in a new tab so you can see who is getting the calls today.</p>
      </div>
      <form id="testForm" class="test-form" novalidate>
        <div class="field-row">
          <div class="field">
            <label for="tTrade">Your trade</label>
            <input type="text" id="tTrade" name="trade" placeholder="plumber" autocomplete="off" required>
          </div>
          <div class="field">
            <label for="tCity">Your city</label>
            <input type="text" id="tCity" name="city" placeholder="Dallas" autocomplete="off" required>
          </div>
        </div>
        <button type="submit" class="btn btn-clay">Check Google Maps</button>
        <div id="testResult" class="test-result" aria-live="polite">
          <strong>Were you in the top three?</strong>
          <div class="choices">
            <button type="button" id="choiceYes" class="btn btn-secondary btn-sm">Yes</button>
            <button type="button" id="choiceNo" class="btn btn-secondary btn-sm">No</button>
          </div>
          <div id="testYes" class="answer">Good. The audit will show you how to hold the spot and push your radius outward. <a href="/free-seo-audit" class="text-link">Get the free audit</a></div>
          <div id="testNo" class="answer">That is where the calls are going. The audit shows you exactly why they rank above you and what it takes to change it. <a href="/free-seo-audit" class="text-link">Get the free audit</a></div>
        </div>
        <p class="test-note">Opens Google Maps in a new tab. Nothing is sent to us.</p>
      </form>
    </div>
  </div>
</section>

<section class="section bg-white" aria-labelledby="audit-title">
  <div class="container audit-split">
    <div class="reveal">
      <p class="eyebrow">Start with the audit</p>
      <h2 id="audit-title" class="section-title">See what is costing you calls before you spend a dollar.</h2>
      <p class="section-intro">Every engagement starts with a free audit of your profile, your listings, your website, and the three businesses ranking above you. You keep it whether or not we ever work together.</p>
      <a href="/free-seo-audit" class="btn btn-primary">Request your audit</a>
    </div>
    <div class="sheet reveal reveal-2">
      <div class="sheet-head"><h3>Local audit</h3><span>What we check</span></div>
      <ul class="sheet-list">
      {sheet_row("Primary category and services", "Set up for the searches people run in your city")}
      {sheet_row("Name, address, and phone", "Matching on Google, Apple, Yelp, and the rest")}
      {sheet_row("Service and city pages", "One page per service and per area, and Google can find them")}
      {sheet_row("Reviews", "Count, rating, and recency next to the top three")}
      {sheet_row("Top three competitors", "Who holds the map pack and what they do differently")}
      {sheet_row("Service radius", "How far your listing reaches, and what is winnable next")}
      </ul>
    </div>
  </div>
</section>

<section class="section bg-sand topo" id="how" aria-labelledby="how-title">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="eyebrow">How it works</p>
        <h2 id="how-title" class="section-title">Ranked in three plain steps</h2>
      </div>
      <p class="section-intro">No long onboarding and no jargon.</p>
    </div>
    <div class="steps">
      {step("1", "Free local audit", "We check your profile, listings, reviews, and rankings. You see what is costing you calls before you spend anything.")}
      {step("2", "We build your presence", "Profile setup, listing cleanup, review follow-up, and a page for every service and city you cover. All done for you.")}
      {step("3", "You get the calls", "Leads go straight to your phone. Each month you get a plain report of what moved and what came in.")}
    </div>
  </div>
</section>

<section class="section bg-white manifesto" aria-labelledby="who-title">
  <div class="container manifesto-grid">
    <div class="reveal">
      <p class="eyebrow">Who we are</p>
      <h2 id="who-title">A small shop, on purpose.</h2>
      <p>We only work with local service businesses: contractors, restoration companies, garage door techs, and the trades that live on the phone ringing.</p>
      <p><strong>One operator.</strong> The person who builds your plan is the person who runs it.</p>
      <p><strong>Month to month.</strong> No setup fee and no long contract.</p>
      <p><strong>We grow you, or you don't pay.</strong> If your rankings don't move in the agreed timeframe, you owe nothing.</p>
      <p class="close">If you want one operator who knows your trade, apply. If you want the cheapest package you can find, we're not it.</p>
      <a href="/apply" class="btn btn-primary">Apply now</a>
    </div>
    <aside class="facts-card reveal reveal-2" aria-labelledby="facts-title">
      <h3 id="facts-title">The short version</h3>
      <dl class="facts">
        <div class="fact"><dt>Retainer</dt><dd>Starting at $1,500/mo</dd></div>
        <div class="fact"><dt>Term</dt><dd>Month to month</dd></div>
        <div class="fact"><dt>Setup fee</dt><dd>None</dd></div>
        <div class="fact"><dt>Who runs it</dt><dd>One operator</dd></div>
        <div class="fact"><dt>Guarantee</dt><dd>Results, or you don't pay</dd></div>
      </dl>
      <a href="/free-seo-audit" class="btn btn-light">Start with a free audit</a>
    </aside>
  </div>
</section>

<section class="section bg-sand" id="services" aria-labelledby="services-title">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="eyebrow">What you get</p>
        <h2 id="services-title" class="section-title">Everything a local campaign needs</h2>
      </div>
      <p class="section-intro">One flat retainer covers all of it.</p>
    </div>
    <div class="cards">
      {service(ICON_PIN, "Google Business Profile", "Full setup, weekly posts, Q and A, and photos that win the map pack.")}
      {service(ICON_LIST, "Listings that match", "Your name, address, and phone matched on the directories Google checks.")}
      {service(ICON_PAGES, "Service and city pages", "One page for each service and each area you cover, written for that area.")}
      {service(ICON_STAR, "Review generation", "Follow-up that asks every finished customer at the right moment.")}
      {service(ICON_CHART, "Monthly reporting", "Rankings, calls, and profile activity in one plain report.")}
      {service(ICON_SITE, "A website built for local search", "Built for your trade and service area, with a structure that gets stronger over time.")}
    </div>
  </div>
</section>

<section class="section bg-white" aria-labelledby="faq-title">
  <div class="container">
    <p class="eyebrow">Questions</p>
    <h2 id="faq-title" class="section-title">What owners ask us first</h2>
    <div class="faq">
      {faq("Do you need to be in my city to rank my business?", "No. Every ranking signal is attached to your business, not to ours. We work remotely and the math does not change.")}
      {faq("How long before I show up in the map pack?", "We target the map pack inside 90 days for most service areas. Dense cities take longer, and we tell you which yours is before you commit.")}
      {faq("I already have a profile and a website. Do I start over?", "No. You keep your profile and your site. We fix what is holding them back and build from there.")}
      {faq("What does it cost?", "Campaigns start at $1,500 a month, flat, with no setup fee. Month to month.")}
    </div>
  </div>
</section>
''' + cta("We grow you, or you don't pay.", "If your rankings don't move in the agreed timeframe, you owe nothing. Start with the free audit.") + '''
</main>
''' + STICKY + FOOTER + REVEAL_JS + TEST_JS + '''
</body>
</html>
'''

# ---------------- APPLY ----------------
apply = head(
  "Apply Now | LocalScaling",
  "Apply to work with LocalScaling. Tell us about your business and we will send you a free local SEO audit within 24 hours.",
  "/apply", robots="noindex, follow",
) + NAV_MIN + f'''
<main class="form-page" id="main">
  <div class="container form-center">
    <div class="form-card">
      <h1>Apply now</h1>
      <p class="sub">Tell us about your business. We respond within 24 hours.</p>

      <form id="applyForm" action="{FORM_APPLY}" method="POST" novalidate>
        <input type="hidden" name="_subject" value="New LocalScaling application">
        <div class="honey" aria-hidden="true">
          <label for="fcompany">Leave this empty</label>
          <input type="text" id="fcompany" name="_gotcha" tabindex="-1" autocomplete="off">
        </div>

        <div class="field-row">
          <div class="field">
            <label for="fname">Name</label>
            <input type="text" id="fname" name="name" placeholder="John Smith" autocomplete="name" required>
          </div>
          <div class="field">
            <label for="femail">Email</label>
            <input type="email" id="femail" name="email" placeholder="john@yourbiz.com" autocomplete="email" required>
          </div>
        </div>

        <div class="field-row">
          <div class="field">
            <label for="fbiz">Business name</label>
            <input type="text" id="fbiz" name="business" placeholder="Smith Restoration LLC" autocomplete="organization" required>
          </div>
          <div class="field">
            <label for="fcity">City</label>
            <input type="text" id="fcity" name="city" placeholder="Dallas, TX" required>
          </div>
        </div>

        <div class="field">
          <label for="fbudget">Monthly budget</label>
          <select id="fbudget" name="budget" required>
            <option value="" disabled selected>Select a range</option>
            <option value="Under $1,500/mo">Under $1,500/mo</option>
            <option value="$1,500 to $2,500/mo">$1,500 to $2,500/mo</option>
            <option value="$2,500/mo and up">$2,500/mo and up</option>
          </select>
        </div>

        <div class="form-error" id="formError" role="alert">
          Something went wrong. Email us at <a href="mailto:info@localscaling.com">info@localscaling.com</a>
        </div>

        <button type="submit" class="btn btn-primary btn-block" id="submitBtn">
          <span id="submitText">Submit application</span>
          <span class="spinner" id="submitSpinner" aria-hidden="true"></span>
        </button>
      </form>

      <p class="form-footer">Questions? <a href="mailto:info@localscaling.com">info@localscaling.com</a></p>
    </div>
  </div>
</main>
''' + FOOTER + FORM_JS % {"form": "applyForm", "ids": "['fname', 'femail', 'fbiz', 'fcity', 'fbudget']", "next": "/thank-you"} + '''
</body>
</html>
'''

# ---------------- THANK YOU ----------------
def notice_page(title, desc, path, h1, intro, steps):
    step_html = "".join(f'''
        <li class="next-step"><span class="n" aria-hidden="true">{i+1}</span><p>{s}</p></li>''' for i, s in enumerate(steps))
    return head(title, desc, path, robots="noindex, follow") + NAV_MIN + f'''
<main class="notice-page" id="main">
  <div class="notice">
    <div class="notice-check" aria-hidden="true">{TICK}</div>
    <h1>{h1}</h1>
    <p>{intro}</p>
    <hr class="hairline">
    <div class="next">
      <p class="label">What happens next</p>
      <ol>{step_html}
      </ol>
    </div>
    <a href="/" class="btn btn-primary">Back to LocalScaling</a>
  </div>
</main>
</body>
</html>
'''

thankyou = notice_page(
  "Application Received | LocalScaling",
  "Thank you for applying to LocalScaling. We will review your details and be in touch within 24 hours.",
  "/thank-you",
  "Application received.",
  "Thanks for applying. We'll review your details and be in touch within 24 hours.",
  ["We review your business and pull a competitor snapshot for your market",
   "We send you a custom local SEO audit within 24 hours",
   "If it's a fit, we get started with no long sales process"],
)

audit_thanks = notice_page(
  "Audit Request Received | LocalScaling",
  "Thanks for requesting a free local SEO audit from LocalScaling. We will email your audit within 24 hours.",
  "/audit-thank-you",
  "Audit request received.",
  "Thanks. We'll look over your business and email your audit within 24 hours. Check your spam folder if it hasn't turned up by then.",
  ["We check your Google Business Profile, your listings, and your website",
   "We look at who holds the top spots for your main search and what they do differently",
   "You get the written audit by email. Reply to it if you want to talk it through"],
)

# ---------------- AUDIT ----------------
audit = head(
  "Free Local SEO Audit | LocalScaling",
  "Get a free local SEO audit for your service business. We check your Google Business Profile, listings, website, and reviews against the competitors ranking above you and email you the findings.",
  "/free-seo-audit",
) + NAV + f'''
<main class="audit-page" id="main"><div class="container audit-grid">
  <section class="audit-intro" aria-labelledby="audit-h1">
    <p class="eyebrow">Free local SEO audit</p>
    <h1 id="audit-h1">Find out where you're losing calls to the businesses above you.</h1>
    <p class="lede">We look at your Google Business Profile, your website, your listings, and the businesses that outrank you, then email you a written audit. No call required.</p>

    <p class="block-title">What the audit covers</p>
    <div class="points">
      {point("Google Business Profile", "Categories, hours, photos, posts, and whether the profile is set up for the searches people run in your city.")}
      {point("Listings", "Whether your name, address, and phone match on the directories that matter.")}
      {point("Website", "Whether you have a page for each service and each city you cover, and whether Google can find them.")}
      {point("Reviews", "How your count and rating compare with the businesses holding the top spots.")}
      {point("Competitors", "Who holds the top three spots for your main search, and what they do that you do not.")}
    </div>

    <p class="block-title">What happens after you send it</p>
    <div class="prose">
      <p>We email the audit within 24 hours. If we can help, we'll say so. If we can't, we'll tell you that too. No sales call unless you ask for one.</p>
      <p>This is for local service businesses. If you run an online store or a national brand, we're not the right fit.</p>
    </div>
  </section>

  <div class="form-card">
    <h2>Request your audit</h2>
    <p class="sub">Six quick fields. We email the audit within 24 hours.</p>

    <form id="auditForm" action="{FORM_AUDIT}" method="POST" novalidate>
      <input type="hidden" name="_subject" value="New free SEO audit request">
      <div class="honey" aria-hidden="true">
        <label for="fcompany">Leave this empty</label>
        <input type="text" id="fcompany" name="_gotcha" tabindex="-1" autocomplete="off">
      </div>

      <div class="field-row">
        <div class="field">
          <label for="fname">Name</label>
          <input type="text" id="fname" name="name" placeholder="John Smith" autocomplete="name" required>
        </div>
        <div class="field">
          <label for="femail">Email</label>
          <input type="email" id="femail" name="email" placeholder="john@yourbiz.com" autocomplete="email" required>
        </div>
      </div>

      <div class="field">
        <label for="fbiz">Business name</label>
        <input type="text" id="fbiz" name="business" placeholder="Smith Restoration LLC" autocomplete="organization" required>
      </div>

      <div class="field">
        <label for="fsite">Website</label>
        <input type="text" id="fsite" name="website" placeholder="yourbusiness.com" inputmode="url" autocomplete="url" required>
      </div>

      <div class="field-row">
        <div class="field">
          <label for="fcity">City you serve</label>
          <input type="text" id="fcity" name="city" placeholder="Dallas, TX" required>
        </div>
        <div class="field">
          <label for="ftrade">Trade</label>
          <select id="ftrade" name="trade" required>
            <option value="" disabled selected>Select one</option>
            <option value="Plumbing">Plumbing</option>
            <option value="HVAC">HVAC</option>
            <option value="Electrical">Electrical</option>
            <option value="Roofing">Roofing</option>
            <option value="Water damage / restoration">Water damage / restoration</option>
            <option value="Garage doors">Garage doors</option>
            <option value="Landscaping">Landscaping</option>
            <option value="Painting">Painting</option>
            <option value="Cleaning">Cleaning</option>
            <option value="Pest control">Pest control</option>
            <option value="Other">Other</option>
          </select>
        </div>
      </div>

      <details class="more-fields">
        <summary>Add more detail <span>(optional, helps us go deeper)</span></summary>
        <div>
      <div class="field">
        <label for="fgbp">Google Business Profile link</label>
        <p class="hint" id="fgbp-hint">Find your business on Google Maps, tap Share, and paste the link here.</p>
        <input type="text" id="fgbp" name="gbp_link" placeholder="maps.app.goo.gl/..." inputmode="url" aria-describedby="fgbp-hint">
      </div>

      <div class="field-row">
        <div class="field">
          <label for="fsearch">Search you want to win</label>
          <input type="text" id="fsearch" name="target_search" placeholder="water damage repair Dallas">
        </div>
        <div class="field">
          <label for="fphone">Phone</label>
          <input type="tel" id="fphone" name="phone" placeholder="(555) 555-0100" autocomplete="tel">
        </div>
      </div>

      <div class="field">
        <label for="fnotes">Anything else we should look at?</label>
        <textarea id="fnotes" name="notes" placeholder="A competitor that keeps beating you, a listing with the wrong number, a second location..."></textarea>
      </div>
        </div>
      </details>

      <div class="form-error" id="formError" role="alert">
        Something went wrong. Email us at <a href="mailto:info@localscaling.com">info@localscaling.com</a>
      </div>

      <button type="submit" class="btn btn-clay btn-block" id="submitBtn">
        <span id="submitText">Send my free audit request</span>
        <span class="spinner" id="submitSpinner" aria-hidden="true"></span>
      </button>
    </form>

    <p class="form-footer">Prefer email? Send your business name, website, and city to <a href="mailto:info@localscaling.com">info@localscaling.com</a></p>
  </div>
</div></main>
''' + FOOTER + FORM_JS % {"form": "auditForm", "ids": "['fname', 'femail', 'fbiz', 'fsite', 'fcity', 'ftrade']", "next": "/audit-thank-you"} + '''
</body>
</html>
'''

# ---------------- LOS ANGELES ----------------
def ncard(title, text):
    return f'''
      <div class="card card-link reveal">
        <h3><a href="/apply">{title}</a></h3>
        <p>{text}</p>
      </div>'''

def num(n, title, text):
    return f'''
      <div class="numbered-item reveal">
        <p class="n" aria-hidden="true">{n}</p>
        <h3>{title}</h3>
        <p>{text}</p>
      </div>'''

areas = ["Santa Monica","Sherman Oaks","Pasadena","Glendale","Burbank","Long Beach","Torrance","Culver City","Van Nuys","Woodland Hills","Studio City","Encino","Northridge","El Segundo","Redondo Beach","Silver Lake","Highland Park","Whittier","Downey","San Pedro"]
chips = "".join(f'<li class="chip">{a}</li>' for a in areas)

la = head(
  "Local SEO Agency in Los Angeles | LocalScaling",
  "Local SEO for Los Angeles service businesses. We get contractors into the Google map pack across LA County, one service area at a time. Starting at $1,500/mo.",
  "/locations/los-angeles",
).replace("<body>", "<body class=\"has-sticky\">") + NAV + f'''
<main id="main">
<section class="hero-simple topo" aria-labelledby="la-title">
  <div class="container">
    <nav class="crumb" aria-label="Breadcrumb"><a href="/">Home</a><span class="crumb-sep" aria-hidden="true">/</span><span aria-current="page">Los Angeles</span></nav>
    <p class="eyebrow">Serving LA County</p>
    <h1 id="la-title">Local SEO agency in Los Angeles</h1>
    <p class="lede">We get contractors and home service companies into the map pack where their customers actually search from, one service area at a time. LA is not one market, and treating it like one is why most campaigns here stall.</p>
    <div class="hero-actions">
      <a href="/free-seo-audit" class="btn btn-clay">Get a free audit</a>
      <a href="/apply" class="text-link">Or apply to work with us</a>
    </div>
    <p class="cta-note"><strong>Free.</strong> No call required. Sent to your inbox within 24 hours.</p>
    <ul class="hero-facts">
      <li>{TICK}Starting at $1,500/mo</li>
      <li>{TICK}Month to month</li>
      <li>{TICK}Service businesses only</li>
    </ul>
  </div>
</section>

<section class="section bg-white" aria-labelledby="la-why">
  <div class="container">
    <p class="eyebrow">Why LA is different</p>
    <h2 id="la-why" class="section-title">Distance decides who shows up</h2>
    <div class="prose narrow">
      <p>Google builds the map pack around the person searching, not around your office. A plumber in Van Nuys will not show for a homeowner in Santa Monica, however strong the profile. Los Angeles County is bigger than some states.</p>
      <p class="pull">One profile cannot cover 88 cities. Any agency selling you all of LA is selling you a ranking that geography will not permit.</p>
      <p>So we start by measuring how far your listing already reaches. Some cities sit inside that reach today. The rest need a location page and a longer runway. That map decides the plan.</p>
    </div>
  </div>
</section>

<section class="section bg-sand topo" aria-labelledby="la-how">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="eyebrow">How we work here</p>
        <h2 id="la-how" class="section-title">Built around how Los Angeles searches</h2>
      </div>
    </div>
    <div class="numbered">
      {num("01", "We map your real radius first", "We check where your profile ranks from a grid of points across the metro, not from one search at your desk. Everything after that is built on that map.")}
      {num("02", "We target neighborhoods, not the metro", "Nobody searches for a roofer in Los Angeles. They search Sherman Oaks, El Segundo, Highland Park, so we build your site and profile around the names people type.")}
      {num("03", "We set the profile up the way Google expects", "Plenty of LA contractors run out of a truck or a garage. Google calls that a service area business, and setting it up wrong caps your reach before any content work begins.")}
      {num("04", "We put your license where people can see it", "California requires a CSLB license for most contracting work, and any homeowner can look yours up. Putting the number on your site and profile gives Google and your customer something they can check.")}
    </div>
  </div>
</section>

<section class="section bg-white" aria-labelledby="la-work">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="eyebrow">The work</p>
        <h2 id="la-work" class="section-title">What running an LA campaign involves</h2>
      </div>
      <p class="section-intro">Every item links to the application.</p>
    </div>
    <div class="cards">
      {ncard("Google Business Profile", "Categories, services, service area, photos, posts, and the Q and A most owners never touch.")}
      {ncard("Location pages", "One page per city you want to win, each written for that area.")}
      {ncard("Citations and NAP", "Your name, address, and phone matched across the directories Google cross checks.")}
      {ncard("Review generation", "A follow-up sequence that asks every finished customer at the right moment.")}
      {ncard("Monthly reporting", "Where you rank across the grid, how it moved, and what came in.")}
      {ncard("Your website", "Built for the way local search works. Every client gets one.")}
    </div>
  </div>
</section>

<section class="section bg-sand" aria-labelledby="la-areas">
  <div class="container">
    <p class="eyebrow">Coverage</p>
    <h2 id="la-areas" class="section-title">Areas we work across LA County</h2>
    <ul class="chips">{chips}</ul>
    <p class="muted narrow">Your own radius matters more than this list. If your area is missing, ask and we will tell you honestly whether we can move it.</p>
  </div>
</section>

<section class="section bg-white" aria-labelledby="la-faq">
  <div class="container">
    <p class="eyebrow">Questions</p>
    <h2 id="la-faq" class="section-title">What LA owners ask us</h2>
    <div class="faq">
      {faq("Do you have to be based in Los Angeles to rank my business here?", "No. Every signal Google weighs is attached to your business, not ours. We work with LA companies remotely.")}
      {faq("Can one Google profile rank across all of Los Angeles?", "No listing ranks county wide. You win a core radius first, then push outward with location pages as the profile gains strength.")}
      {faq("How long before I show up in the map pack?", "We target placement inside 90 days for most areas. Dense cities take longer, and we tell you which yours is before you commit.")}
      {faq("I already have a profile and a website. Do I start over?", "You keep both. Starting fresh throws away your review history and the listing's age. We fix what exists and build from there.")}
      {faq("What does it cost?", "Campaigns start at $1,500 a month, flat, with no setup fee. Month to month.")}
    </div>
  </div>
</section>
''' + cta("Find out how far your listing actually reaches.", "We map where you rank across LA, show you which areas are winnable now, and tell you what it takes.") + '''
</main>
''' + STICKY + FOOTER + REVEAL_JS + '''
</body>
</html>
'''

files = {
  "index.html": index,
  "apply.html": apply,
  "thank-you.html": thankyou,
  "audit-thank-you.html": audit_thanks,
  "free-seo-audit.html": audit,
  "locations/los-angeles.html": la,
}
for name, content in files.items():
    p = os.path.join(SITE, name)
    with open(p, "w") as f:
        f.write(content)
    print(f"wrote {name} ({len(content.splitlines())} lines)")
