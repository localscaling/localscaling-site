# LocalScaling site

Static site, deployed by Vercel from `main`. Clean URLs are on, so `/apply`
serves `apply.html`.

## How the pages are built

- `tools/build_pages.py` generates every HTML page. Edit copy and structure
  there, then run `python3 tools/build_pages.py`. Editing the HTML directly is
  lost on the next build
- `styles.css` is the one stylesheet. Colors, type, and spacing are tokens at
  the top. Bump `STYLE_VERSION` in the generator after a CSS change so browsers
  fetch the new file
- Form endpoints live in the generator as `FORM_APPLY` and `FORM_AUDIT`. Two
  Formspree forms, one per page
- `sitemap.xml` and `robots.txt` are written by the same build from the same
  page list. Never edit them by hand. Noindex pages are left out. A page's
  lastmod moves only when its content changes, tracked in
  `tools/sitemap-ledger.json`, which is committed with the pages
- Industry pages: one dict per industry in `tools/industries.py`, rendered by
  `industry_page()`. City pages: one dict per city in `tools/cities.py`,
  rendered by `city_page()`. Copy the newest dict, change every value, add it
  to `PAGES`, build. Content stays qualitative: no stats, no client names, no
  results. No "X, not Y" contrast sentences
- `python3 tools/review_page.py <page.html>` is the anti-AI-writing review as
  a script, and it calls the hub lint. Zero findings before a page is done
- The page routine: a scheduled task on this Mac runs `tools/PAGE-ROUTINE.md`
  daily, and `tools/routine_gate.py` lets it through every four days. It
  builds the next city and the next industry from `tools/page-queue.json`,
  reviews, commits, and publishes when `publish` is true. Change the
  procedure in the runbook, the queue in the JSON, never in the task prompt
- URLs are flat and read like the search: `/local-seo-for-<industry>`,
  `/local-seo-<city>`. No folders. A live URL never changes without a
  permanent redirect in `vercel.json`. The old `/locations/los-angeles`
  redirects that way
- The footer lists Home, Free audit, and Apply only. Industry and city pages
  are linked from the industries band and from each other, not the footer

## Design, approved 2026-09-17

- Font: Plus Jakarta Sans for everything. The logo keeps League Spartan
- Palette: white and pale green-gray sections, deep green bands and buttons,
  one amber accent on eyebrow dashes, step numbers, and the map pin. Amber is
  never a button fill, the dark-on-gold contrast was rejected
- One primary action, the free audit, in solid green with white text. Apply is
  the secondary action everywhere
- Layout stays: left-aligned hero with the map illustration, industries band,
  ten second test, audit checklist, three steps, small-shop prose with facts
  card, six service cards, accordion FAQ, closing CTA band, dark footer
- Keep copy short. One or two sentences per card or answer
- Every text and control color pair passes WCAG AA. Check ratios before
  changing a token

## Rules that apply here

- No invented proof. No testimonials, logos, counts, or results until the
  operator supplies real ones
- The pitch is Google Maps and the search results under it, together. Never
  the map pack alone. Every page names both, and the home page has a section
  that shows both on one results page. The profile wins the map, the site
  wins the listing
- Prices are "starting at", never fixed
- No results guarantee anywhere. Removed 2026-09-17 at the operator's request
- Audience is every local service business: contractors and trades, clinics
  and practices, accounting, legal, insurance. Not online stores, restaurants,
  or retail. Do not lean on one trade in examples, vary them
- Timing claim: "usually three to six months to start seeing big results".
  Never a 90 day promise
- Run the anti-AI-writing review and `python3 ../ops/knowledge_lint.py --file`
  on every page before calling it done
- Preview with a local server and screenshots at desktop and phone width, and
  publish a hosted preview link for the operator. The app browser pane is not
  reliably visible to them
