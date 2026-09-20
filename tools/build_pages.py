"""Generates the six site pages from shared head, nav, footer, and form snippets.
Run from anywhere: python3 tools/build_pages.py
Edit copy here, not in the generated HTML, or the next run overwrites it."""
import os, sys
SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(SITE, "tools"))

STYLE_VERSION = "20260917i"  # bump when styles.css changes so browsers fetch the new file
FORM_APPLY = "https://formspree.io/f/mgoqbjbw"
FORM_AUDIT = "https://formspree.io/f/mnpnqnyd"

LOGO = '''<svg viewBox="0 0 214 48" fill="none" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="LocalScaling"><path d="M22 3C13.7 3 7 9.6 7 17.9C7 24.4 10.4 33.2 14.6 39.4C17.2 43.2 19.8 45.5 22 45.5C24.2 45.5 26.8 43.2 29.4 39.4C33.6 33.2 37 24.4 37 17.9C37 9.6 30.3 3 22 3Z" stroke="#002c0a" stroke-width="3.2" stroke-linejoin="round" fill="none"/><circle cx="22" cy="18" r="5" stroke="#002c0a" stroke-width="3.2" fill="none"/><text x="48" y="32" font-family="League Spartan, sans-serif" font-weight="800" font-size="24" fill="#002c0a" letter-spacing="-0.4">LocalScaling</text></svg>'''

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
        <p>Local SEO for contractors, clinics, practices, and other local service businesses. One operator, month to month.</p>
      </div>
      <nav class="footer-col" aria-label="Pages">
        <h3>Pages</h3>
        <a href="/">Home</a>
        <a href="/free-seo-audit">Free audit</a>
        <a href="/apply">Apply</a>
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
      window.open('https://www.google.com/search?q=' + q, '_blank', 'noopener');
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
    <p class="cta-note">Free, no call, in your inbox within 24 hours.</p>
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

# ---------------- SHARED ILLUSTRATIONS ----------------
PIN_SM = '<svg class="pack-pin" viewBox="0 0 24 30" aria-hidden="true"><path d="M12 2C7.03 2 3 6.03 3 11c0 6.5 9 17 9 17s9-10.5 9-17c0-4.97-4.03-9-9-9z"/><circle cx="12" cy="11" r="3"/></svg>'

def serp_card(search, pack_rows, organic_rows, note, you="Your business"):
    rows = ""
    for i, (name, sub) in enumerate(pack_rows):
        top = i == 0
        tag = '<span class="pack-tag">Map pack</span>' if top else '<span class="pack-stars" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9734;</span>'
        rows += f'<div class="pack-row{" top" if top else ""}">{PIN_SM}<div><div class="pack-name">{name}</div><div class="pack-sub">{sub}</div></div>{tag}</div>'
    orgs = ""
    for i, (title, url) in enumerate(organic_rows):
        top = i == 0
        tag = '<span class="pack-tag">Search result</span>' if top else ''
        orgs += f'<div class="org-row{" top" if top else ""}"><div><div class="org-url">{url}</div><div class="org-title">{title}</div></div>{tag}</div>'
    return f'''<div class="pack serp" aria-label="Illustration of a Google results page with {you.lower()} in the map pack and in the search results under it">
        <div class="pack-search"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.5" y2="16.5"/></svg>{search}</div>
        <p class="pack-label">Map</p>
        <div class="pack-rows">{rows}</div>
        <p class="pack-label pack-label-2">Listings under the map</p>
        <div class="org-rows">{orgs}</div>
        <p class="pack-note">{note}</p>
      </div>'''


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
  "LocalScaling gets local service businesses to the top of Google Maps and the search results under it. Starting at $1,500/mo, month to month. Built for contractors, clinics, practices, and the trades.",
  "/",
).replace("<body>", "<body class=\"has-sticky\">") + NAV + f'''
<main id="main">
<section class="hero topo" aria-labelledby="hero-title">
  <div class="container hero-grid">
    <div>
      <p class="eyebrow">Local SEO for service businesses</p>
      <h1 id="hero-title">More calls.<br>More jobs.<br><em>Zero ad spend.</em></h1>
      <p class="lede">We get local service businesses to the top of Google Maps and the search results under it, in the neighborhoods they serve. Contractors, clinics, practices, and the trades. Stop renting leads and start owning them.</p>
      <div class="hero-actions">
        <a href="/free-seo-audit" class="btn btn-clay">Get a free audit</a>
        <a href="/apply" class="text-link">Or apply to work with us</a>
      </div>
      <p class="cta-note"><strong>Free.</strong> No call required. Sent to your inbox within 24 hours.</p>
      <ul class="hero-facts">
        <li>{TICK}Starting at $1,500/mo</li>
        <li>{TICK}Month to month</li>
        <li>{TICK}No setup fee</li>
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

<div class="trades" aria-label="Who we work with">
  <div class="container trades-inner">
    <strong>Built for local services</strong>
    <span>Plumbing</span><span>HVAC</span><span>Roofing</span><span>Electrical</span><span>Dental</span><span>Medical</span><span><a href="/local-seo-for-accountants">Accounting</a></span><span>Legal</span>
  </div>
</div>

<section class="test" aria-labelledby="test-title">
  <div class="container">
    <div class="test-card reveal">
      <div>
        <p class="eyebrow">The ten second test</p>
        <h2 id="test-title">Are you on the map and in the results right now?</h2>
        <p>Type your trade and city. We'll open the real Google result in a new tab so you can see who holds the map and who holds the listings under it today.</p>
      </div>
      <form id="testForm" class="test-form" novalidate>
        <div class="field-row">
          <div class="field">
            <label for="tTrade">Your trade</label>
            <input type="text" id="tTrade" name="trade" placeholder="plumber, dentist, CPA" autocomplete="off" required>
          </div>
          <div class="field">
            <label for="tCity">Your city</label>
            <input type="text" id="tCity" name="city" placeholder="Dallas" autocomplete="off" required>
          </div>
        </div>
        <button type="submit" class="btn btn-clay">Check Google</button>
        <div id="testResult" class="test-result" aria-live="polite">
          <strong>Were you in the map pack and on the first page?</strong>
          <div class="choices">
            <button type="button" id="choiceYes" class="btn btn-secondary btn-sm">Yes</button>
            <button type="button" id="choiceNo" class="btn btn-secondary btn-sm">No</button>
          </div>
          <div id="testYes" class="answer">Good. The audit will show you how to hold both spots and push your radius outward. <a href="/free-seo-audit" class="text-link">Get the free audit</a></div>
          <div id="testNo" class="answer">That is where the calls are going. The audit shows you who holds each spot, why, and what it takes to change it. <a href="/free-seo-audit" class="text-link">Get the free audit</a></div>
        </div>
        <p class="test-note">Opens Google in a new tab. Nothing is sent to us.</p>
      </form>
    </div>
  </div>
</section>

<section class="section bg-sand" aria-labelledby="both-title">
  <div class="container audit-split">
    <div class="reveal">
      <p class="eyebrow">Two spots on one page</p>
      <h2 id="both-title" class="section-title">The map gets the call. The listing under it closes the deal.</h2>
      <p class="section-intro">When someone searches for what you do, Google shows the map first and the regular results under it. People glance at the map, then scroll to see who else is there. A business that holds a spot in both gets the call more often than one that holds either alone.</p>
      <p class="section-intro">We work both. Your Google Business Profile wins the map. Your website wins the listing under it. The audit checks where you stand in each.</p>
      <a href="/free-seo-audit" class="btn btn-primary">See where you stand</a>
    </div>
    <div class="reveal reveal-2">
      {serp_card("emergency plumber near me", [("Your business", "Plumber · 0.6 mi"), ("Another plumber", "Plumber · 1.4 mi"), ("Another plumber", "Plumber · 2.2 mi")], [("Emergency plumber in your city, open now", "yourbusiness.com"), ("Plumbers near you", "a directory"), ("Another plumber", "anotherplumber.com")], "Same search, two places to show up. We work both.")}
    </div>
  </div>
</section>

<section class="section bg-white" aria-labelledby="audit-title">
  <div class="container audit-split">
    <div class="reveal">
      <p class="eyebrow">Start with the audit</p>
      <h2 id="audit-title" class="section-title">See what is costing you calls before you spend a dollar.</h2>
      <p class="section-intro">Every engagement starts with a free audit of your profile, your website, your listings, and the businesses above you on the map and in the results. You keep it whether or not we ever work together.</p>
      <a href="/free-seo-audit" class="btn btn-primary">Request your audit</a>
    </div>
    <div class="sheet reveal reveal-2">
      <div class="sheet-head"><h3>Local audit</h3><span>What we check</span></div>
      <ul class="sheet-list">
      {sheet_row("Primary category and services", "Set up for the searches people run in your city")}
      {sheet_row("Name, address, and phone", "Matching on Google, Apple, Yelp, and the rest")}
      {sheet_row("Service and city pages", "One page per service and per area, and Google can find them")}
      {sheet_row("Reviews", "Count, rating, and recency next to the businesses above you")}
      {sheet_row("Who is above you", "Who holds the map pack, who holds the listings under it, and what they do differently")}
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
      {step("1", "Free local audit", "We check your profile, your site, your listings, and your reviews, on the map and in the results. You see what is costing you calls before you spend anything.")}
      {step("2", "We build both", "Your profile and listings for the map. A page for every service and city on your site for the results under it. All done for you.")}
      {step("3", "You get the calls", "Leads go straight to your phone. Each month you get a plain report of what moved and what came in.")}
    </div>
  </div>
</section>

<section class="section bg-white manifesto" aria-labelledby="who-title">
  <div class="container manifesto-grid">
    <div class="reveal">
      <p class="eyebrow">Who we are</p>
      <h2 id="who-title">A small shop, on purpose.</h2>
      <p>We only work with local service businesses: contractors, clinics, practices, and the trades. Anyone whose customers search for them nearby and call. Online stores, restaurants, and retail are a different job, and we leave that job to someone else.</p>
      <p><strong>One operator.</strong> The person who builds your plan is the person who runs it.</p>
      <p><strong>Month to month.</strong> No setup fee and no long contract.</p>
      <p><strong>Plain reporting.</strong> Each month you see what moved and what came in, in plain English.</p>
      <p class="close">If you want one operator who knows your market, apply. If you want the cheapest package you can find, we're not it.</p>
      <a href="/apply" class="btn btn-primary">Apply now</a>
    </div>
    <aside class="facts-card reveal reveal-2" aria-labelledby="facts-title">
      <h3 id="facts-title">The short version</h3>
      <dl class="facts">
        <div class="fact"><dt>Retainer</dt><dd>Starting at $1,500/mo</dd></div>
        <div class="fact"><dt>Term</dt><dd>Month to month</dd></div>
        <div class="fact"><dt>Setup fee</dt><dd>None</dd></div>
        <div class="fact"><dt>Who runs it</dt><dd>One operator</dd></div>
        <div class="fact"><dt>Reporting</dt><dd>Monthly, plain English</dd></div>
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
      {service(ICON_PAGES, "Service and city pages", "One page for each service and each area you cover. These are what put you in the results under the map.")}
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
      {faq("Do you need to be in my city to rank my business?", "No. Every signal Google weighs belongs to your business: your location, your profile, your reviews, your site. We work remotely and the math does not change.")}
      {faq("How long until I see results?", "Usually three to six months to start seeing big results. Some areas move sooner, dense cities take longer, and we tell you which yours is before you commit.")}
      {faq("I already have a profile and a website. Do I start over?", "No. You keep your profile and your site. We fix what is holding them back and build from there.")}
      {faq("What does it cost?", "Campaigns start at $1,500 a month, flat, with no setup fee. Month to month.")}
    </div>
  </div>
</section>
''' + cta("Ready to own your local market?", "Start with the free audit. We show you where you are losing calls and what it takes to fix it.") + '''
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
            <input type="text" id="fbiz" name="business" placeholder="Smith & Sons LLC" autocomplete="organization" required>
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
    <h1 id="audit-h1">See where you're losing calls.</h1>
    <p class="lede">We check your business against the three ranking above you and email you what we find. Free, no call, within 24 hours.</p>

    <p class="block-title">What we check</p>
    <ul class="audit-list">
      <li>{TICK}Google Business Profile</li>
      <li>{TICK}Name, address, and phone across listings</li>
      <li>{TICK}Service and city pages on your site</li>
      <li>{TICK}Reviews next to the businesses above you</li>
      <li>{TICK}Who holds the map and the results, and why</li>
    </ul>

    <p class="audit-fit">For local service businesses: contractors, clinics, practices, and the trades. Not for online stores, restaurants, or retail.</p>
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
        <input type="text" id="fbiz" name="business" placeholder="Smith & Sons LLC" autocomplete="organization" required>
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
          <label for="ftrade">Industry</label>
          <select id="ftrade" name="industry" required>
            <option value="" disabled selected>Select one</option>
            <optgroup label="Trades and home services">
              <option value="Plumbing">Plumbing</option>
              <option value="HVAC">HVAC</option>
              <option value="Electrical">Electrical</option>
              <option value="Roofing">Roofing</option>
              <option value="Restoration">Restoration</option>
              <option value="Landscaping">Landscaping</option>
              <option value="Cleaning">Cleaning</option>
              <option value="Pest control">Pest control</option>
              <option value="Other trade">Other trade</option>
            </optgroup>
            <optgroup label="Health">
              <option value="Dental">Dental</option>
              <option value="Medical or clinic">Medical or clinic</option>
              <option value="Chiropractic or physical therapy">Chiropractic or physical therapy</option>
              <option value="Other health">Other health</option>
            </optgroup>
            <optgroup label="Professional services">
              <option value="Accounting or finance">Accounting or finance</option>
              <option value="Legal">Legal</option>
              <option value="Insurance">Insurance</option>
              <option value="Other professional service">Other professional service</option>
            </optgroup>
            <option value="Other local service">Other local service</option>
          </select>
        </div>
      </div>

      <details class="more-fields">
        <summary>Add more detail <span>(optional)</span></summary>
        <div>
      <div class="field">
        <label for="fgbp">Google Business Profile link</label>
        <p class="hint" id="fgbp-hint">Find your business on Google Maps, tap Share, and paste the link here.</p>
        <input type="text" id="fgbp" name="gbp_link" placeholder="maps.app.goo.gl/..." inputmode="url" aria-describedby="fgbp-hint">
      </div>

      <div class="field-row">
        <div class="field">
          <label for="fsearch">Search you want to win</label>
          <input type="text" id="fsearch" name="target_search" placeholder="emergency plumber Dallas">
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

    <p class="form-footer">No sales call unless you ask for one. Prefer email? Send your business name, website, and city to <a href="mailto:info@localscaling.com">info@localscaling.com</a></p>
  </div>
</div></main>
''' + FOOTER + FORM_JS % {"form": "auditForm", "ids": "['fname', 'femail', 'fbiz', 'fsite', 'fcity', 'ftrade']", "next": "/audit-thank-you"} + """
<script>
  (function () {
    var want = new URLSearchParams(location.search).get('industry');
    var sel = document.getElementById('ftrade');
    if (!want || !sel) return;
    for (var i = 0; i < sel.options.length; i++) {
      if (sel.options[i].value === want) { sel.value = want; break; }
    }
  })();
</script>
""" + '''
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
  "Local SEO for Los Angeles service businesses. We get contractors, clinics, and practices into the Google map pack and the search results under it across LA County, one service area at a time. Starting at $1,500/mo.",
  "/locations/los-angeles",
).replace("<body>", "<body class=\"has-sticky\">") + NAV + f'''
<main id="main">
<section class="hero-simple topo" aria-labelledby="la-title">
  <div class="container">
    <nav class="crumb" aria-label="Breadcrumb"><a href="/">Home</a><span class="crumb-sep" aria-hidden="true">/</span><span aria-current="page">Los Angeles</span></nav>
    <p class="eyebrow">Serving LA County</p>
    <h1 id="la-title">Local SEO agency in Los Angeles</h1>
    <p class="lede">We get local service businesses into the map pack and the search results under it, in the parts of LA their customers actually search from. LA is not one market, and treating it like one is why most campaigns here stall.</p>
    <div class="hero-actions">
      <a href="/free-seo-audit" class="btn btn-clay">Get a free audit</a>
      <a href="/apply" class="text-link">Or apply to work with us</a>
    </div>
    <p class="cta-note"><strong>Free.</strong> No call required. Sent to your inbox within 24 hours.</p>
    <ul class="hero-facts">
      <li>{TICK}Starting at $1,500/mo</li>
      <li>{TICK}Month to month</li>
      <li>{TICK}Local services only</li>
    </ul>
  </div>
</section>

<section class="section bg-white" aria-labelledby="la-why">
  <div class="container">
    <p class="eyebrow">Why LA is different</p>
    <h2 id="la-why" class="section-title">Distance decides who shows up</h2>
    <div class="prose narrow">
      <p>Google builds the map pack around wherever the person is standing when they search, and your office address matters less than most owners think. A plumber in Van Nuys will not show for a homeowner in Santa Monica, and a dentist in Pasadena will not show for a patient in Torrance, however strong the profile. Los Angeles County is bigger than some states.</p>
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
      {num("01", "We map your real radius first", "We check where your profile ranks from a grid of points across the metro. One search from your own desk tells you almost nothing. Everything after that is built on the map.")}
      {num("02", "We target neighborhoods", "Nobody searches for a roofer or a dentist in Los Angeles. They search Sherman Oaks, El Segundo, Highland Park, so we build your site and profile around the names people type.")}
      {num("03", "We set the profile up the way Google expects", "Plenty of LA businesses work from a truck or from home. Google calls that a service area business, and setting it up wrong caps your reach before any content work begins.")}
      {num("04", "We put your credentials where people can see it", "Contractors have a CSLB number, clinics and practices have a state board. Any customer can look it up. Putting it on your site and profile gives Google and your customer something they can check.")}
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
      {faq("Do you have to be based in Los Angeles to rank my business here?", "No. Every signal Google weighs belongs to your business: your location, your profile, your reviews, your site. We work with LA companies remotely and nothing about that changes.")}
      {faq("Can one Google profile rank across all of Los Angeles?", "No listing ranks county wide. You win a core radius first, then push outward with location pages as the profile gains strength.")}
      {faq("How long until I see results?", "Usually three to six months to start seeing big results. Some areas move sooner, dense LA cities take longer, and we tell you which yours is before you commit.")}
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


# ---------------- INDUSTRY TEMPLATE ----------------
from industries import PAGES as INDUSTRY_PAGES

def chip_list(items):
    return "".join(f'<li class="chip">{c}</li>' for c in items)

def fit_col(title, items, good):
    icon = TICK if good else '<svg viewBox="0 0 24 24" aria-hidden="true"><line x1="6" y1="6" x2="18" y2="18"/><line x1="18" y1="6" x2="6" y2="18"/></svg>'
    lis = "".join(f'<li><span class="fit-icon {"yes" if good else "no"}">{icon}</span>{i}</li>' for i in items)
    return f'<div class="card reveal"><h3>{title}</h3><ul class="fit-list">{lis}</ul></div>'

def pack_card(c):
    rows = ""
    for i, (name, sub) in enumerate(c["pack_rows"]):
        top = i == 0
        tag = '<span class="pack-tag">Top result</span>' if top else '<span class="pack-stars" aria-hidden="true">&#9733;&#9733;&#9733;&#9733;&#9734;</span>'
        rows += f'<div class="pack-row{" top" if top else ""}">{PIN_SM}<div><div class="pack-name">{name}</div><div class="pack-sub">{sub}</div></div>{tag}</div>'
    return f'''<div class="pack" aria-label="Illustration of a Google map pack with your firm in the top spot">
        <div class="pack-search"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.5" y2="16.5"/></svg>{c["pack_search"]}</div>
        <p class="pack-label">Google Maps results</p>
        <div class="pack-rows">{rows}</div>
        <p class="pack-note">{c["pack_note"]}</p>
      </div>'''

def year_timeline(c):
    months = ["Jan","Feb","Mar","Apr","May","Jun","Jul","Aug","Sep","Oct","Nov","Dec"]
    w = 720; left = 10; span = (w - 20) / 12
    labels = "".join(f'<text x="{left + span*i + span/2:.0f}" y="122" text-anchor="middle" class="tl-month">{m}</text>' for i, m in enumerate(months))
    segs = ""
    for start, end, cls, title in c["timeline"]:
        x = left + span*(start-1); wd = span*(end-start+1)
        segs += f'<rect x="{x:.0f}" y="46" width="{wd:.0f}" height="40" rx="8" class="tl-seg {cls}"/>'
        segs += f'<text x="{x + wd/2:.0f}" y="71" text-anchor="middle" class="tl-text {cls}">{title}</text>'
    start_x = left + span*(c["timeline_start"]-1) + span/2
    stack = "".join(f'<li class="tl-item {cls}"><span class="tl-when">{months[start-1]} to {months[end-1]}</span><span class="tl-what">{title}</span></li>' for start, end, cls, title in c["timeline"])
    return f'''<figure class="timeline">
      <ol class="tl-stack" aria-hidden="true">{stack}</ol>
      <svg viewBox="0 0 {w} 140" role="img" aria-label="{c["timeline_alt"]}">
        {segs}
        <line x1="{start_x:.0f}" y1="14" x2="{start_x:.0f}" y2="42" class="tl-line"/>
        <text x="{start_x:.0f}" y="10" text-anchor="middle" class="tl-start">Start here</text>
        <line x1="{left}" y1="100" x2="{w-10}" y2="100" class="tl-axis"/>
        {labels}
      </svg>
      <figcaption>{c["timeline_caption"]}</figcaption>
    </figure>'''

def intent_table(c):
    rows = "".join(f'<tr><td><span class="intent-q">{q}</span></td><td>{want}</td><td><span class="intent-page">{page}</span></td></tr>' for q, want, page in c["intent"])
    return f'''<div class="table-wrap">
      <table class="intent">
        <thead><tr><th scope="col">What they type</th><th scope="col">What they want</th><th scope="col">The page that wins it</th></tr></thead>
        <tbody>{rows}</tbody>
      </table>
    </div>'''

def industry_page(c):
    """c is a dict from tools/industries.py. Every new industry page is a new
    dict rendered through this function."""
    audit_link = "/free-seo-audit?industry=" + c["industry_value"].replace(" ", "%20")
    how = "".join(num(f"0{i+1}", t, b) for i, (t, b) in enumerate(c["how"]))
    why = "".join(
        (f'<p class="pull">{para[1]}</p>' if isinstance(para, tuple) else f"<p>{para}</p>")
        for para in c["why_paragraphs"]
    )
    leaks = "".join(f'''
      <li class="leak reveal"><strong>{t}</strong><span>{b}</span></li>''' for t, b in c["leaks"])
    faqs = "".join(faq(q, a) for q, a in c["faq"])
    included = "".join(f'''
      <div class="card card-link reveal">
        <h3><a href="{audit_link}">{t}</a></h3>
        <p>{b}</p>
      </div>''' for t, b in c["included"])
    page = head(c["title"], c["meta"], "/" + c["slug"]).replace("<body>", '<body class="has-sticky">') + NAV
    page += f'''
<main id="main">
<section class="hero hero-ind topo" aria-labelledby="ind-title">
  <div class="container">
    <nav class="crumb" aria-label="Breadcrumb"><a href="/">Home</a><span class="crumb-sep" aria-hidden="true">/</span><span aria-current="page">{c["crumb"]}</span></nav>
    <div class="hero-grid">
      <div>
        <p class="eyebrow">{c["eyebrow"]}</p>
        <h1 id="ind-title">{c["h1"]}</h1>
        <p class="lede">{c["lede"]}</p>
        <div class="hero-actions">
          <a href="{audit_link}" class="btn btn-clay">Get a free audit</a>
          <a href="/apply" class="text-link">Or apply to work with us</a>
        </div>
        <p class="cta-note"><strong>Free.</strong> No call required. Sent to your inbox within 24 hours.</p>
        <ul class="hero-facts">
          <li>{TICK}Starting at $1,500/mo</li>
          <li>{TICK}Month to month</li>
          <li>{TICK}Local services only</li>
        </ul>
      </div>
      {pack_card(c)}
    </div>
  </div>
</section>

<section class="section bg-white" aria-labelledby="ind-why">
  <div class="container">
    <p class="eyebrow">{c["why_eyebrow"]}</p>
    <h2 id="ind-why" class="section-title">{c["why_h2"]}</h2>
    <div class="prose narrow">
      {why}
    </div>
    {year_timeline(c)}
  </div>
</section>

<section class="section bg-sand" aria-labelledby="ind-both">
  <div class="container audit-split">
    <div class="reveal">
      <p class="eyebrow">Two spots on one page</p>
      <h2 id="ind-both" class="section-title">The map gets the call. The listing under it closes the deal.</h2>
      <p class="section-intro">{c["both_intro"]}</p>
      <p class="section-intro">We work both. Your Google Business Profile wins the map. Your website wins the listing under it. The audit checks where you stand in each.</p>
      <a href="{audit_link}" class="btn btn-primary">See where you stand</a>
    </div>
    <div class="reveal reveal-2">
      {serp_card(c["pack_search"], c["pack_rows"], c["organic_rows"], "Same search, two places to show up. We work both.", you="Your firm")}
    </div>
  </div>
</section>

<section class="section bg-white topo" aria-labelledby="ind-leaks">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="eyebrow">Where the calls go missing</p>
        <h2 id="ind-leaks" class="section-title">{c["leaks_h2"]}</h2>
      </div>
      <p class="section-intro">{c["leaks_intro"]}</p>
    </div>
    <ol class="leaks">
      {leaks}
    </ol>
    <p class="leaks-cta"><a href="{audit_link}" class="btn btn-primary">Check mine for free</a></p>
  </div>
</section>

<section class="section bg-white" aria-labelledby="ind-how">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="eyebrow">How we work with {c["short"]}</p>
        <h2 id="ind-how" class="section-title">{c["how_h2"]}</h2>
      </div>
    </div>
    <div class="numbered">
      {how}
    </div>
  </div>
</section>

<section class="section bg-sand" aria-labelledby="ind-searches">
  <div class="container">
    <p class="eyebrow">Searches you can win</p>
    <h2 id="ind-searches" class="section-title">{c["searches_h2"]}</h2>
    {intent_table(c)}
    <p class="chips-label">More everyday searches</p>
    <ul class="chips">{chip_list(c["searches"])}</ul>
    <p class="chips-label">Specialty searches with less competition</p>
    <ul class="chips">{chip_list(c["specialty_searches"])}</ul>
    <p class="muted narrow">{c["searches_note"]}</p>
  </div>
</section>

<section class="section bg-white" aria-labelledby="ind-work">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="eyebrow">The work</p>
        <h2 id="ind-work" class="section-title">What a campaign for {c["short"]} includes</h2>
      </div>
      <p class="section-intro">One flat retainer covers all of it.</p>
    </div>
    <div class="cards">
      {included}
    </div>
  </div>
</section>

<section class="section bg-sand" aria-labelledby="ind-fit">
  <div class="container">
    <p class="eyebrow">Is this for you</p>
    <h2 id="ind-fit" class="section-title">{c["fit_h2"]}</h2>
    <div class="cards cards-2" style="margin-top:36px;">
      {fit_col("A good fit", c["fit_yes"], True)}
      {fit_col("Not a fit", c["fit_no"], False)}
    </div>
  </div>
</section>

<section class="section bg-white" aria-labelledby="ind-faq">
  <div class="container">
    <p class="eyebrow">Questions</p>
    <h2 id="ind-faq" class="section-title">What {c["short"]} ask us</h2>
    <div class="faq">
      {faqs}
    </div>
  </div>
</section>
'''
    page += cta(c["cta_h"], c["cta_p"]) + "\n</main>\n" + STICKY + FOOTER + REVEAL_JS + "\n</body>\n</html>\n"
    return page

files = {
  "index.html": index,
  "apply.html": apply,
  "thank-you.html": thankyou,
  "audit-thank-you.html": audit_thanks,
  "free-seo-audit.html": audit,
  "locations/los-angeles.html": la,
}
for cfg in INDUSTRY_PAGES:
    files[cfg["slug"] + ".html"] = industry_page(cfg)
for name, content in files.items():
    p = os.path.join(SITE, name)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w") as f:
        f.write(content)
    print(f"wrote {name} ({len(content.splitlines())} lines)")
