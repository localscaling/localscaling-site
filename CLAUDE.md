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

## Design, approved 2026-09-17

- Font: Plus Jakarta Sans for everything. The logo keeps League Spartan
- Palette: white and pale green-gray sections, deep green bands and buttons,
  one amber accent on eyebrow dashes, step numbers, and the map pin. Amber is
  never a button fill, the dark-on-gold contrast was rejected
- One primary action, the free audit, in solid green with white text. Apply is
  the secondary action everywhere
- Layout stays: left-aligned hero with the map illustration, trades band, ten
  second test, audit checklist, three steps, small-shop prose with facts card,
  six service cards, accordion FAQ, guarantee band, dark footer
- Keep copy short. One or two sentences per card or answer
- Every text and control color pair passes WCAG AA. Check ratios before
  changing a token

## Rules that apply here

- No invented proof. No testimonials, logos, counts, or results until the
  operator supplies real ones
- Prices are "starting at", never fixed
- Run the anti-AI-writing review and `python3 ../ops/knowledge_lint.py --file`
  on every page before calling it done
- Preview with a local server and screenshots at desktop and phone width, and
  publish a hosted preview link for the operator. The app browser pane is not
  reliably visible to them
