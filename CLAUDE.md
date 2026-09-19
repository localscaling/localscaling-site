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
- Industry pages: one dict per industry in `tools/industries.py`, rendered by
  `industry_page()`. Copy the accountants dict, change every value, add it to
  `PAGES`, build. Link the new page from the industries band. The audit link
  carries `?industry=` so the form preselects. Content stays qualitative: no
  stats, no client names, no results. No "X, not Y" contrast sentences, the
  anti-AI review flags them
- URLs are flat and read like the search: `/local-seo-for-accountants`,
  `/local-seo-los-angeles`. No `/industries/` or `/locations/` folders. A live
  URL never changes without a permanent redirect in `vercel.json`
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
