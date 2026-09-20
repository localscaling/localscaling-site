"""City page content. One dict per city, rendered by city_page() in
build_pages.py. To add a city: copy LOS_ANGELES, change every value, append it
to PAGES, run the build. Every claim stays qualitative. Neighborhood names,
license boards, and anything else factual must be checked before it goes in.
No stats, no client names, no results. Timing is three to six months."""

LOS_ANGELES = {
  "slug": "local-seo-los-angeles",
  "city": "Los Angeles",
  "short": "LA",
  "region": "LA County",
  "title": "Local SEO Agency in Los Angeles | LocalScaling",
  "meta": "Local SEO for Los Angeles service businesses. We get contractors, clinics, and practices into the Google map pack and the search results under it across LA County, one service area at a time. Starting at $1,500/mo.",
  "eyebrow": "Serving LA County",
  "h1": "Local SEO agency in Los Angeles",
  "lede": "We get local service businesses into the map pack and the search results under it, in the parts of LA their customers actually search from. LA is not one market, and treating it like one is why most campaigns here stall.",

  "why_eyebrow": "Why LA is different",
  "why_h2": "Distance decides who shows up",
  "why_paragraphs": [
    "Google builds the map pack around wherever the person is standing when they search, and your office address matters less than most owners think. A plumber in Van Nuys will not show for a homeowner in Santa Monica, and a dentist in Pasadena will not show for a patient in Torrance, however strong the profile. Los Angeles County is bigger than some states.",
    ("pull", "One profile cannot cover 88 cities. Any agency selling you all of LA is selling you a ranking that geography will not permit."),
    "So we start by measuring how far your listing already reaches. Some cities sit inside that reach today. The rest need a location page and a longer runway. That map decides the plan.",
  ],

  "search_example": "emergency plumber Sherman Oaks",
  "pack_rows": [("Your business", "Plumber · 0.8 mi"), ("Another plumber", "Plumber · 1.6 mi"), ("Another plumber", "Plumber · 2.9 mi")],
  "organic_rows": [("Emergency plumber in Sherman Oaks, open now", "yourbusiness.com"), ("Plumbers in Sherman Oaks", "a directory"), ("Another plumber", "anotherplumber.com")],
  "both_intro": "When someone in LA searches for what you do, Google shows the map first and the regular results under it, and both are drawn around the neighborhood they are standing in. A business that holds a spot in both, in that neighborhood, gets the call.",

  "how_h2": "Built around how Los Angeles searches",
  "how": [
    ("We map your real radius first", "We check where your profile ranks from a grid of points across the metro. One search from your own desk tells you almost nothing. Everything after that is built on the map."),
    ("We target neighborhoods", "Nobody searches for a roofer or a dentist in Los Angeles. They search Sherman Oaks, El Segundo, Highland Park, so we build your site and profile around the names people type."),
    ("We set the profile up the way Google expects", "Plenty of LA businesses work from a truck or from home. Google calls that a service area business, and setting it up wrong caps your reach before any content work begins."),
    ("We put your credentials where people can see it", "Contractors have a CSLB number, clinics and practices have a state board. Any customer can look it up. Putting it on your site and profile gives Google and your customer something they can check."),
  ],

  "included": [
    ("Google Business Profile", "Categories, services, service area, photos, posts, and the Q and A most owners never touch. This is what wins the map."),
    ("Location pages", "One page per city you want to win, each written for that area. These are what put you in the results under the map."),
    ("Citations and NAP", "Your name, address, and phone matched across the directories Google cross checks."),
    ("Review generation", "A follow-up sequence that asks every finished customer at the right moment."),
    ("Monthly reporting", "Where you rank across the grid, how it moved, and what came in."),
    ("Your website", "Built for the way local search works. Every client gets one."),
  ],

  "areas_h2": "Areas we work across LA County",
  "areas": ["Santa Monica","Sherman Oaks","Pasadena","Glendale","Burbank","Long Beach","Torrance","Culver City","Van Nuys","Woodland Hills","Studio City","Encino","Northridge","El Segundo","Redondo Beach","Silver Lake","Highland Park","Whittier","Downey","San Pedro"],
  "areas_note": "Your own radius matters more than this list. If your area is missing, ask and we will tell you honestly whether we can move it.",

  "faq": [
    ("Do you have to be based in Los Angeles to rank my business here?", "No. Every signal Google weighs belongs to your business: your location, your profile, your reviews, your site. We work with LA companies remotely and nothing about that changes."),
    ("Can one Google profile rank across all of Los Angeles?", "No listing ranks county wide. You win a core radius first, then push outward with location pages as the profile gains strength."),
    ("How long until I see results?", "Usually three to six months to start seeing big results. Some areas move sooner, dense LA cities take longer, and we tell you which yours is before you commit."),
    ("I already have a profile and a website. Do I start over?", "You keep both. Starting fresh throws away your review history and the listing's age. We fix what exists and build from there."),
    ("What does it cost?", "Campaigns start at $1,500 a month, flat, with no setup fee. Month to month."),
  ],

  "cta_h": "Find out how far your listing actually reaches.",
  "cta_p": "We map where you rank across LA, show you which areas are winnable now, and tell you what it takes.",
}

HOUSTON = {
  "slug": "local-seo-houston",
  "city": "Houston",
  "short": "Houston",
  "region": "the Houston metro",
  "title": "Local SEO Agency in Houston | LocalScaling",
  "meta": "Local SEO for Houston service businesses. We get contractors, clinics, and practices into the Google map pack and the search results under it, suburb by suburb, from the Loop to the Grand Parkway. Starting at $1,500/mo.",
  "eyebrow": "Serving the Houston metro",
  "h1": "Local SEO agency in Houston",
  "lede": "We get local service businesses into the map pack and the search results under it, in the suburbs and neighborhoods their customers actually search from. Houston is a ring of towns that each search on their own, and a campaign built for one address stalls at the Beltway.",

  "why_eyebrow": "Why Houston is different",
  "why_h2": "The suburbs are the market, and each one searches by name",
  "why_paragraphs": [
    "Houston is spread across a huge area, and most of the people who live here live outside the Loop. Ask someone where they are from and they say Katy, Pearland, Cypress, or The Woodlands before they say Houston. They search the same way. An electrician in Katy will not show on the map for a homeowner in Clear Lake, and a clinic in The Heights will not show for a family in Sugar Land, however good the profile.",
    ("pull", "A profile pinned to one address reaches one slice of the metro. The rest of it needs pages with the suburb's name on them."),
    "Then there is the weather. Air conditioners fail in the same weeks for everyone, and a storm sends the whole city looking for a roofer or a restoration crew at once. Google decides who shows up in those weeks based on what your profile and site looked like months earlier, so the build happens before the season.",
    "The last difference is language. A large share of Houston households speak Spanish at home. For some trades a Spanish page on the site and a Spanish reply to reviews earn calls an English only campaign never sees. We check whether that is true for your trade before we suggest it.",
  ],

  "search_example": "ac repair Katy",
  "pack_rows": [("Your business", "HVAC contractor · 1.2 mi"), ("Another company", "Air conditioning repair service · 2.4 mi"), ("Another company", "HVAC contractor · 4.1 mi")],
  "organic_rows": [("AC repair in Katy, same day service", "yourbusiness.com"), ("AC repair companies in Katy", "a directory"), ("Another company", "anothercompany.com")],
  "both_intro": "When someone in Houston searches for what you do, Google shows the map first and the regular results under it, and both are drawn around the suburb they are standing in. A business that holds a spot in both, in that suburb, gets the call.",

  "how_h2": "Built around how Houston searches",
  "how": [
    ("We measure your real reach first", "We check where your profile ranks from a grid of points across the metro, from the Loop out past the Grand Parkway. One search from your own office tells you almost nothing. Everything after that is built on the grid."),
    ("We build pages for the suburbs by name", "Nobody in Pearland searches for a roofer in Houston. They search Pearland, and a family in Cypress searches Cypress, so your site and profile are built around the names people type."),
    ("We set the profile up the way Google expects", "Plenty of Houston businesses run from a truck or from home. Google calls that a service area business, and setting it up wrong caps your reach before any content work begins."),
    ("We put your license where people can check it", "Electricians and air conditioning contractors hold a state license, plumbers hold one from their own board, and clinics have a state board. Any customer can look it up. Putting it on your site and profile gives Google and the customer something they can verify."),
  ],

  "included": [
    ("Google Business Profile", "The right categories, the services people search for, a service area drawn around where you actually work, photos, and posts. This is what wins the map."),
    ("Suburb pages", "One page per suburb or neighborhood you want to win, each written for that area. These are what put you in the results under the map."),
    ("Listings that match", "Your name, address, and phone the same on every directory Google compares, including the Texas and trade specific ones."),
    ("Review generation", "A follow-up sequence that asks every finished customer at the right moment, in English or Spanish."),
    ("Monthly reporting", "Where you rank on the grid, suburb by suburb, how that moved, and how many people called."),
    ("Your website", "Built for local search from the start, with a page for every suburb and every service. Every client gets one."),
  ],

  "areas_h2": "Areas we work across the Houston metro",
  "areas": ["The Heights","Montrose","River Oaks","Midtown","Memorial","Uptown","Bellaire","West University Place","Meyerland","Spring Branch","Westchase","Energy Corridor","Clear Lake","Kingwood","Sugar Land","Katy","Cypress","Pearland","The Woodlands","Pasadena"],
  "areas_note": "Your own reach matters more than this list. If your area is missing, ask and we will tell you honestly whether we can move it.",

  "faq": [
    ("Do you have to be based in Houston to rank my business here?", "No. Every signal Google weighs belongs to your business: your location, your profile, your reviews, your site. We work with Houston companies remotely and nothing about that changes."),
    ("Can one Google profile rank across the whole metro?", "No listing ranks from the Loop to the Grand Parkway. You win a core reach first, then push outward with suburb pages as the profile gains strength."),
    ("How long until I see results?", "Usually three to six months to start seeing big results. Some suburbs move sooner, the dense parts inside the Loop take longer, and we tell you which yours is before you commit."),
    ("Our trucks go all over the metro. Do we need a second office?", "Only if it is a real one. A second listing needs a staffed address with real hours, and a mailbox or a rented desk gets the whole account suspended. Until then the suburbs are covered by pages and by the service area on your profile."),
    ("Should our site have a Spanish version?", "For some trades in some parts of the metro, yes, and we will tell you which. When it makes sense we build the pages properly, in Spanish someone would actually speak, and we set up the review replies to match."),
    ("What does it cost?", "Campaigns start at $1,500 a month, flat, with no setup fee. Month to month."),
  ],

  "cta_h": "Find out which parts of Houston you can actually win.",
  "cta_p": "We map where you rank across the metro, show you which suburbs are winnable now, and tell you what it takes.",
}

PAGES = [LOS_ANGELES, HOUSTON]
