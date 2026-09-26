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

PHOENIX = {
  "slug": "local-seo-phoenix",
  "city": "Phoenix",
  "short": "Phoenix",
  "region": "the Valley",
  "title": "Local SEO Agency in Phoenix | LocalScaling",
  "meta": "Local SEO for Phoenix service businesses. We get contractors, clinics, and practices into the Google map pack and the search results under it, city by city across the Valley. Starting at $1,500/mo.",
  "eyebrow": "Serving the Valley",
  "h1": "Local SEO agency in Phoenix",
  "lede": "We get local service businesses into the map pack and the search results under it, in the Valley cities their customers search from. Phoenix is one metro made of many cities, and people search by the name of the one they live in.",

  "why_eyebrow": "Why Phoenix is different",
  "why_h2": "The Valley is a set of cities, and each one searches by name",
  "why_paragraphs": [
    "People here say they live in the Valley, then they name the city. Mesa, Chandler, Gilbert, Scottsdale, Glendale, Peoria. Each has its own city hall and its own name in the search bar. A pest control company in Mesa will not show on the map for a homeowner in Peoria, and a dental practice in Scottsdale will not show for a family in Goodyear, however strong the profile.",
    ("pull", "One profile reaches one part of the Valley. The rest of it needs pages with each city's name on them."),
    "Then there is the heat. Air conditioners, pools, and roofs all get tested in the same summer weeks, and a monsoon storm sends whole neighborhoods looking for help on the same night. In the cooler months the winter visitors come back, and some trades get busier just as others slow down. Google decides who shows up in each rush based on what your profile and site looked like before it started.",
    "The Valley also keeps building outward. New neighborhoods at the edges fill with families who have no plumber, dentist, or accountant yet, and they find one by searching the name of the town they just moved to.",
  ],

  "search_example": "pest control Mesa",
  "pack_rows": [("Your business", "Pest control service · 0.9 mi"), ("Another company", "Pest control service · 2.2 mi"), ("Another company", "Pest control service · 3.6 mi")],
  "organic_rows": [("Pest and scorpion control in Mesa", "yourbusiness.com"), ("Pest control companies in Mesa", "a directory"), ("Another company", "anothercompany.com")],
  "both_intro": "When someone in the Valley searches for what you do, Google shows the map first and the regular results under it, and both are drawn around the city they are searching from. A business that holds a spot in both, in that city, gets the call.",

  "how_h2": "Built around how the Valley searches",
  "how": [
    ("We measure your real reach first", "We check where your profile ranks from a grid of points across the metro, from the West Valley to the East Valley. A search from your own office says almost nothing about the rest. The plan is built on the grid."),
    ("We build a page for each city you serve", "Nobody in Gilbert searches for an electrician in Phoenix. They type Gilbert, and a family in Surprise types Surprise. Your site and profile are built around the names people actually use."),
    ("We set the profile up the way Google expects", "A lot of Valley businesses run from a truck or a home office. Google calls that a service area business. Set it up wrong and your reach is capped before any page gets written."),
    ("We plan around your busy season", "Summer and monsoon season for some trades, the winter months for others. The profile, the pages, and the review push are in place before your rush begins, because the rankings in July come from the work done in spring."),
  ],

  "included": [
    ("Google Business Profile", "The right categories, the services people search for, a service area drawn around the cities you actually work, photos, and posts. This is what wins the map."),
    ("City pages", "One page for each Valley city you want to win, written for that city. These are what put you in the results under the map."),
    ("Listings that match", "Your name, address, and phone the same on every directory Google compares, including the Arizona and trade ones."),
    ("Review generation", "A follow-up that asks every finished customer at the right moment, all year, including the slow months."),
    ("Monthly reporting", "Where you rank on the grid, city by city, how that moved, and how many people called."),
    ("Your website", "Built for local search from the start, with a page for every city and every service. Every client gets one."),
  ],

  "areas_h2": "Areas we work across the Valley",
  "areas": ["Downtown Phoenix","Arcadia","Biltmore","Desert Ridge","Ahwatukee","Laveen","Paradise Valley","Scottsdale","Tempe","Mesa","Chandler","Gilbert","Queen Creek","Glendale","Peoria","Surprise","Goodyear","Avondale","Cave Creek","Fountain Hills"],
  "areas_note": "This list is where we start. Your own reach decides the plan, so if your city is missing, ask and we will tell you straight whether it is winnable.",
  "more_cities": ["local-seo-los-angeles", "local-seo-houston"],

  "faq": [
    ("Do you need to be in Phoenix to rank my business here?", "No. What Google weighs is your location, your profile, your reviews, and your site. We run Valley campaigns remotely and the work is the same."),
    ("Can one profile cover Phoenix, Scottsdale, and the East Valley?", "No single listing reaches the whole Valley. You win the cities closest to you first, then reach further out with city pages as the profile gets stronger."),
    ("How long until I see results?", "Usually three to six months to start seeing big results. Some cities move sooner than others, and we tell you which yours is before you commit."),
    ("We are slow all summer. Is it worth running the whole year?", "Yes. The slow months are when the work gets done, so the rankings are there when the busy months arrive. Reviews from last season keep working through this one."),
    ("Our office is in one city and we work in five. Do we need more addresses?", "No. The other cities are covered by your service area and by a page for each one. A second listing needs a real staffed office, and a virtual office or a mailbox can get the whole profile suspended."),
    ("What does it cost?", "Campaigns start at $1,500 a month, flat, with no setup fee. Month to month."),
  ],

  "cta_h": "Find out which Valley cities you can win.",
  "cta_p": "We map where you rank from one side of the Valley to the other, show you which cities are winnable now, and tell you what it takes.",
}

PAGES = [LOS_ANGELES, HOUSTON, PHOENIX]
