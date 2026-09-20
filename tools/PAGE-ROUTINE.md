# Page routine

Runs on this Mac from the desktop app's scheduled tasks. Every run builds one
city page and one industry page, reviews them, and publishes them. This file
is the whole procedure. The scheduled task's prompt says "follow
tools/PAGE-ROUTINE.md" and nothing else of substance, so change the procedure
here, never in the task prompt.

## 0. Gate

    cd "/Users/noah/Documents/Local Scaling/site"
    git pull --ff-only origin main
    python3 tools/routine_gate.py

WAIT means stop, say why in one line, and end the run. GO prints the next
city and the next industry. Build both. Never pick a different one.

## 1. Read the rules

Read `CLAUDE.md` in this folder, then `tools/industries.py` and
`tools/cities.py` for the shape of a page, then the two most recent entries in
`tools/page-queue.json` under `done` so the new pages do not repeat their
angles. Read the hub `LESSONS.md` one folder up for anything about the site.

## 2. Research, ten minutes per page, ideas only

For the industry, search `local seo for <industry>` and read the top four or
five ranking pages. For the city, search `local seo <city>` and read the top
four or five. For each page note: the section order, the objections it
answers, the FAQ questions it asks, and any illustration or graphic it uses.
Take structure and angles. Take no sentences, no stats, no client names, no
claims. Every page we write is qualitative.

Facts that go on a city page must be checked, in this order of care:

- Neighborhood and suburb names: fifteen to twenty, real, spelled the way
  locals spell them. Confirm each against a map.
- Anything about licensing or state boards: only if confirmed on the state's
  own site. Otherwise leave it out.
- Geography claims (sprawl, distinct sub-markets, commute patterns): keep them
  general and true. "Houston is spread across a huge area" is fine. A square
  mileage figure is not, unless you have it from an official source and it
  earns its place.

Facts that go on an industry page:

- Google Business Profile category names must be real categories. Check them
  against the current category list.
- Seasonality, buying triggers, and what the client is worried about: write
  what is true of the trade in general. No percentages, no survey numbers.
- Specialty search phrases: real phrases people type. Vary them. Do not copy
  the accountants list.

## 3. Write the two dicts

Copy the newest dict in `tools/industries.py` and in `tools/cities.py`.
Change every value. Every value. A dict with a leftover line from the last
page is a bug. Keep the shape, including the illustrations: the results card
search phrase, the pack rows, the organic rows, the timeline (industry only),
the intent table (industry only), the fit and not-fit lists (industry only),
the areas list (city only).

Write like the operator: short sentences, plain words, first person plural,
no hype. The specific rules that trip the review:

- No em or en dashes, no curly quotes, straight apostrophes only
- No "X, not Y" contrast sentences and no "not just X but Y"
- No sentence that ends with a tacked-on -ing phrase
- No Title Case headings
- No AI vocabulary. The script has the list
- Prices are "starting at $1,500 a month". Timing is "usually three to six
  months to start seeing big results". No guarantee anywhere
- Vary the example trades on a city page. Never two pages in a row with a
  plumber as the example

If the competitor research showed a graphic idea that is honest, fits the
existing components, and the page is better for it, add it as an addition.
Never remove an existing illustration. If it needs new CSS, add it under
the industry or city block in `styles.css` and bump `STYLE_VERSION`.

## 4. Build and review

    python3 tools/build_pages.py
    python3 tools/review_page.py <city-slug>.html <industry-slug>.html

Fix every finding in the dict, never in the HTML, rebuild, review again.
Zero findings and a hub lint PASS on both pages before moving on. If a
finding cannot be fixed without breaking the copy, stop and report it.

## 5. Look at both pages

Start a server and take screenshots at desktop and phone width:

    python3 -m http.server 8765 --bind 127.0.0.1 --directory "$PWD" &

Check the hero, the results card, the timeline or areas list, the cards, the
FAQ, and the footer. Fix anything broken. Stop the server.

## 6. Link the new pages

Add the industry to the industries band on the home page if its name is
there as plain text. Cities are linked from each other: add the new city to
the areas note of no other page, but add a "More cities" line at the bottom
of the new city page only if there are three or more city pages. Rebuild.

## 7. Record and publish

    python3 tools/routine_gate.py --done city "<City>" <city-slug>
    python3 tools/routine_gate.py --done industry "<industry>" <industry-slug>
    git add -A
    git commit -m "Add <City> and <industry> pages"

If `publish` in `tools/page-queue.json` is true:

    git push origin main

then wait for Vercel and fetch both live URLs until they return 200 and
contain the H1. If `publish` is false, stop after the commit and say so.

Commit messages end with the attribution line the session provides.

## 8. Report

One message. Two live URLs, or two file paths if unpublished. Three lines on
what the research changed about each page. Any fact you could not confirm
and left out. Nothing else.

## 9. Lessons

If something about the process was wrong or slow, add a dated lesson to the
hub `LESSONS.md` in the format it uses. Do not add a lesson for a run that
went as planned.
