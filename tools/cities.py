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

DALLAS = {
  "slug": "local-seo-dallas",
  "city": "Dallas",
  "short": "Dallas",
  "region": "the Dallas side of the Metroplex",
  "title": "Local SEO Agency in Dallas | LocalScaling",
  "meta": "Local SEO for Dallas service businesses. We get contractors, clinics, and practices into the Google map pack and the search results under it, from Oak Cliff to Frisco. Starting at $1,500/mo.",
  "eyebrow": "Serving Dallas and its suburbs",
  "h1": "Local SEO agency in Dallas",
  "lede": "We get local service businesses into the map pack and the search results under it, in the Dallas neighborhoods and suburbs their customers search from. The Metroplex is one name on a map and dozens of markets in the search bar.",

  "why_eyebrow": "Why Dallas is different",
  "why_h2": "Every suburb searches by its own name",
  "why_paragraphs": [
    "Most people in the Dallas area live outside the city limits. Plano, Frisco, McKinney, Richardson, Garland, Irving. Each is its own city with its own name, and people type that name when they search. A roofer in Garland will not show on the map for a homeowner in Frisco, and a physical therapy clinic in Lakewood will not show for a family in Carrollton, however strong the profile.",
    ("pull", "A profile tied to one address reaches one part of the Metroplex. Every suburb past that needs a page with its own name on it."),
    "Fort Worth is the other half of DFW, and it searches as its own market. A company that wants both needs a plan for each side, and most should win the side they are on first.",
    "Then there is the weather. Spring storms bring hail across North Texas, and a single evening can send whole neighborhoods looking for a roofer, a glass company, or an auto body shop. Summer heat tests every air conditioner at once. Google decides who shows up in those weeks from what your profile and site looked like before the storm.",
    "The northern suburbs also keep growing. New subdivisions fill with families who have no dentist, electrician, or insurance agent yet, and they find one by searching the name of the town they just moved to.",
  ],

  "search_example": "roof repair Frisco",
  "pack_rows": [("Your business", "Roofing contractor · 1.1 mi"), ("Another company", "Roofing contractor · 2.3 mi"), ("Another company", "Roofing contractor · 3.8 mi")],
  "organic_rows": [("Hail damage roof repair in Frisco", "yourbusiness.com"), ("Roofers in Frisco", "a directory"), ("Another company", "anothercompany.com")],
  "both_intro": "When someone in the Dallas area searches for what you do, Google shows the map first and the regular results under it, and both are drawn around the suburb or neighborhood they are searching from. A business that holds a spot in both, in that place, gets the call.",

  "how_h2": "Built around how Dallas searches",
  "how": [
    ("We measure your real reach first", "We check where your profile ranks from a grid of points across the Dallas side of the Metroplex, from Oak Cliff up to the northern suburbs. A search from your own office tells you almost nothing about the rest. The plan is built on the grid."),
    ("We build a page for each suburb you serve", "Nobody in McKinney searches for a dentist in Dallas. They type McKinney, and a family in Mesquite types Mesquite. Your site and profile are built around the names people actually use."),
    ("We get ready before storm season", "For roofers, restoration crews, and anyone else the spring storms keep busy, the profile, the pages, and the review push are in place before hail season. The rankings you have the morning after a storm come from work done months earlier."),
    ("We put your license where people can check it", "In Texas, air conditioning and heating contractors are licensed by the state, and clinics and practices have their own boards. Any customer can look a license up. Putting it on your site and profile gives Google and the customer something to verify."),
  ],

  "included": [
    ("Google Business Profile", "The right categories, the services people search for, a service area drawn around the suburbs you actually work, photos, and posts. This is what wins the map."),
    ("Suburb and neighborhood pages", "One page for each place you want to win, written for that place. These are what put you in the results under the map."),
    ("Listings that match", "Your name, address, and phone the same on every directory Google compares, including the Texas and trade ones."),
    ("Review generation", "A follow-up that asks every finished customer at the right moment, and keeps asking after the busy season ends."),
    ("Monthly reporting", "Where you rank on the grid, suburb by suburb, how that moved, and how many people called."),
    ("Your website", "Built for local search from the start, with a page for every suburb and every service. Every client gets one."),
  ],

  "areas_h2": "Areas we work across Dallas and its suburbs",
  "areas": ["Uptown","Oak Lawn","Deep Ellum","Lower Greenville","Lakewood","Lake Highlands","Preston Hollow","Oak Cliff","Bishop Arts District","Highland Park","University Park","Plano","Frisco","McKinney","Allen","Richardson","Garland","Irving","Carrollton","Mesquite"],
  "areas_note": "This list is where we start. Your own reach decides the plan, so if your suburb is missing, ask and we will tell you straight whether it is winnable.",
  "more_cities": ["local-seo-los-angeles", "local-seo-houston", "local-seo-phoenix"],

  "faq": [
    ("Do you need to be in Dallas to rank my business here?", "No. What Google weighs is your location, your profile, your reviews, and your site. We run Dallas campaigns remotely and the work is the same."),
    ("Can one profile cover Dallas and Fort Worth?", "No single listing reaches across the whole Metroplex. You win the area around your address first, then reach further with suburb pages as the profile gets stronger. Fort Worth is usually a separate push."),
    ("How long until I see results?", "Usually three to six months to start seeing big results. Some suburbs move sooner than others, and we tell you which yours is before you commit."),
    ("Our office is in Dallas and most of our work is in Collin County. Is that a problem?", "No. Your service area and a page for each suburb cover the places you drive to. A second listing needs a real staffed office, and a virtual office or a mailbox can get the whole profile suspended."),
    ("Every roofer in town shows up after a hailstorm. How do we stand out?", "By being ready before it hits. Recent reviews, true hours, real photos of your crew, and a page for each suburb are what Google has to go on when the searches spike. They cannot be built the morning after."),
    ("What does it cost?", "Campaigns start at $1,500 a month, flat, with no setup fee. Month to month."),
  ],

  "cta_h": "Find out which Dallas suburbs you can win.",
  "cta_p": "We map where you rank across the Dallas side of the Metroplex, show you which suburbs are winnable now, and tell you what it takes.",
}

SAN_DIEGO = {
  "slug": "local-seo-san-diego",
  "city": "San Diego",
  "short": "San Diego",
  "region": "San Diego County",
  "title": "Local SEO Agency in San Diego | LocalScaling",
  "meta": "Local SEO for San Diego service businesses. We get contractors, clinics, and practices into the Google map pack and the search results under it, from North County to the South Bay. Starting at $1,500/mo.",
  "eyebrow": "Serving San Diego County",
  "h1": "Local SEO agency in San Diego",
  "lede": "We get local service businesses into the map pack and the search results under it, in the San Diego neighborhoods and county towns their customers search from. The county splits into regions that rarely cross into each other, and people search that way too.",

  "why_eyebrow": "Why San Diego is different",
  "why_h2": "Canyons, mesas, and regions that search on their own",
  "why_paragraphs": [
    "Locals talk about the county in pieces. North County, East County, the South Bay, the beach towns, and the neighborhoods of the city itself. Canyons and freeways cut the city into pockets, and a drive that looks short on a map can take a long time at five o'clock. An electrician in Chula Vista will not show on the map for a homeowner in Carlsbad, and a dental office in Clairemont will not show for a family in El Cajon, however strong the profile.",
    ("pull", "One profile reaches one part of the county. Every region past that needs pages with its own names on them."),
    "The weather changes a few miles inland. The coast stays mild under the marine layer, and the inland valleys get real summer heat. A cooling company, a pool service, or a pest control crew sees a different year in Santee than in Pacific Beach, and the pages for each should say so.",
    "San Diego is also a military town, and families move in and out all year. A family that just arrived at a new base has no dentist, no mechanic, and no accountant here yet. They find one by searching the name of the neighborhood they just rented in.",
    "In the South Bay many households speak Spanish at home. For some trades a Spanish page and Spanish review replies earn calls an English only campaign never sees. We check whether that is true for your trade before we suggest it.",
  ],

  "search_example": "electrician Chula Vista",
  "pack_rows": [("Your business", "Electrician · 1.0 mi"), ("Another company", "Electrician · 2.1 mi"), ("Another company", "Electrical installation service · 3.4 mi")],
  "organic_rows": [("Panel upgrades and EV chargers in Chula Vista", "yourbusiness.com"), ("Electricians in Chula Vista", "a directory"), ("Another company", "anothercompany.com")],
  "both_intro": "When someone in San Diego searches for what you do, Google shows the map first and the regular results under it, and both are drawn around the neighborhood they are searching from. A business that holds a spot in both, in that neighborhood, gets the call.",

  "how_h2": "Built around how San Diego searches",
  "how": [
    ("We measure your real reach first", "We check where your profile ranks from a grid of points across the county, from Oceanside down to the border. A search from your own office says almost nothing about the rest. The plan is built on the grid."),
    ("We build pages region by region", "Nobody in Encinitas searches for a dentist in San Diego. They type Encinitas, and a family in La Mesa types La Mesa. We start with the region you are in and add the next one as the profile gets stronger."),
    ("We write for the coast and for inland", "Where the work changes with the climate, the pages change with it. A page for Escondido talks about the heat, and a page for Point Loma talks about salt air and damp. Only where that is true for your trade."),
    ("We put your license where people can check it", "California contractors hold a license from the Contractors State License Board, and anyone can look one up on the board's site. Clinics and practices have their own state boards. Putting the number on your site and profile gives Google and the customer something to verify."),
  ],

  "included": [
    ("Google Business Profile", "The right categories, the services people search for, a service area drawn around the regions you actually work, photos, and posts. This is what wins the map."),
    ("Neighborhood and town pages", "One page for each place you want to win, written for that place. These are what put you in the results under the map."),
    ("Listings that match", "Your name, address, and phone the same on every directory Google compares, including the California and trade ones."),
    ("Review generation", "A follow-up that asks every finished customer at the right moment, in English or Spanish."),
    ("Monthly reporting", "Where you rank on the grid, region by region, how that moved, and how many people called."),
    ("Your website", "Built for local search from the start, with a page for every area and every service. Every client gets one."),
  ],

  "areas_h2": "Areas we work across San Diego County",
  "areas": ["La Jolla","Pacific Beach","Point Loma","North Park","Hillcrest","Mission Valley","Clairemont","Kearny Mesa","Mira Mesa","Rancho Bernardo","Carmel Valley","Del Mar","Encinitas","Carlsbad","Oceanside","Escondido","Poway","La Mesa","El Cajon","Chula Vista"],
  "areas_note": "This list is where we start. Your own reach decides the plan, so if your neighborhood is missing, ask and we will tell you straight whether it is winnable.",
  "more_cities": ["local-seo-los-angeles", "local-seo-houston", "local-seo-phoenix", "local-seo-dallas"],

  "faq": [
    ("Do you need to be in San Diego to rank my business here?", "No. What Google weighs is your location, your profile, your reviews, and your site. We run San Diego campaigns remotely and the work is the same."),
    ("Can one profile cover North County and the South Bay?", "No single listing reaches the whole county. You win the region around your address first, then reach further with town pages as the profile gets stronger."),
    ("How long until I see results?", "Usually three to six months to start seeing big results. Some neighborhoods move sooner than others, and we tell you which yours is before you commit."),
    ("A lot of our customers are military families who move every few years. Is that a problem?", "It is a steady source of new customers. Every move brings a family that needs a new provider and searches for one. Recent reviews and a page for the neighborhoods near the bases help you be the one they pick."),
    ("Should our site have a Spanish version?", "For some trades in some parts of the county, yes, and we will tell you which. When it makes sense we build the pages properly, in Spanish someone would actually speak, and we set up the review replies to match."),
    ("What does it cost?", "Campaigns start at $1,500 a month, flat, with no setup fee. Month to month."),
  ],

  "cta_h": "Find out which parts of San Diego you can win.",
  "cta_p": "We map where you rank across the county, show you which neighborhoods are winnable now, and tell you what it takes.",
}

CHICAGO = {
  "slug": "local-seo-chicago",
  "city": "Chicago",
  "short": "Chicago",
  "region": "Chicagoland",
  "title": "Local SEO Agency in Chicago | LocalScaling",
  "meta": "Local SEO for Chicago service businesses. We get contractors, clinics, and practices into the Google map pack and the search results under it, from Rogers Park to Beverly and out into the suburbs. Starting at $1,500/mo.",
  "eyebrow": "Serving Chicago and its suburbs",
  "h1": "Local SEO agency in Chicago",
  "lede": "We get local service businesses into the map pack and the search results under it, in the Chicago neighborhoods and suburbs their customers search from. Chicago is a city of neighborhoods, and people search it one neighborhood at a time.",

  "why_eyebrow": "Why Chicago is different",
  "why_h2": "People here search by neighborhood",
  "why_paragraphs": [
    "Ask someone in Chicago where they live and they name a neighborhood. Logan Square, Bridgeport, Rogers Park, Beverly. They search the same way. A dentist in Lincoln Park will not show on the map for a family in Hyde Park, and a heating company in Portage Park will not show for a homeowner in Evanston, however strong the profile.",
    ("pull", "The city is dozens of small markets laid along the lake. One profile reaches a few of them."),
    "Past the city limits the suburbs run out in every direction, into DuPage, Lake, Will, Kane, and McHenry counties, and east into Northwest Indiana. Each town searches by its own name, and Indiana is a different state with its own rules. Most businesses should win the side of the region they are on first.",
    "Winter decides a lot. One cold snap sends half the city looking for a furnace repair or a plumber for a frozen pipe on the same night, and heavy summer storms send people looking for help with a wet basement. Google decides who shows up on those nights from what your profile and site looked like before the weather turned.",
    "Much of the city is older housing. Two-flats, bungalows, greystones, and brick that needs tuckpointing. The searches follow the buildings, and a page that names the work an old Chicago house needs reads like it came from someone who has been inside one.",
  ],

  "search_example": "dentist Logan Square",
  "pack_rows": [("Your business", "Dentist · 0.6 mi"), ("Another practice", "Dentist · 1.2 mi"), ("Another practice", "Cosmetic dentist · 1.9 mi")],
  "organic_rows": [("Family dentist in Logan Square", "yourbusiness.com"), ("Dentists in Logan Square", "a directory"), ("Another practice", "anotherpractice.com")],
  "both_intro": "When someone in Chicago searches for what you do, Google shows the map first and the regular results under it, and both are drawn around the neighborhood or suburb they are searching from. A business that holds a spot in both, in that place, gets the call.",

  "how_h2": "Built around how Chicago searches",
  "how": [
    ("We measure your real reach first", "We check where your profile ranks from a grid of points across the city and the suburbs you serve, from Rogers Park down to Beverly. A search from your own office tells you almost nothing about the rest. The plan is built on the grid."),
    ("We build a page for each neighborhood and suburb", "Nobody in Oak Park searches for a dentist in Chicago. They type Oak Park, and a family in Andersonville types Andersonville. Your site and profile are built around the names people actually use."),
    ("We get ready before winter", "For heating, plumbing, roofing, and anyone else the cold keeps busy, the profile, the pages, and the review push are in place by the fall. The rankings you have on the first frozen night come from work done months earlier."),
    ("We put your license where people can check it", "In Illinois, roofing contractors are licensed by the state's Department of Financial and Professional Regulation, and anyone can look a license up on its site. Clinics and practices have their own boards. Putting the number on your site and profile gives Google and the customer something to verify."),
  ],

  "included": [
    ("Google Business Profile", "The right categories, the services people search for, a service area drawn around the neighborhoods and suburbs you actually work, photos, and posts. This is what wins the map."),
    ("Neighborhood and suburb pages", "One page for each place you want to win, written for that place. These are what put you in the results under the map."),
    ("Listings that match", "Your name, address, and phone the same on every directory Google compares, including the Illinois and trade ones."),
    ("Review generation", "A follow-up that asks every finished customer at the right moment, and keeps asking after the winter rush ends."),
    ("Monthly reporting", "Where you rank on the grid, neighborhood by neighborhood, how that moved, and how many people called."),
    ("Your website", "Built for local search from the start, with a page for every area and every service. Every client gets one."),
  ],

  "areas_h2": "Areas we work across Chicago and its suburbs",
  "areas": ["Lincoln Park","Lakeview","Wicker Park","Bucktown","Logan Square","West Loop","River North","Pilsen","Bridgeport","Hyde Park","Bronzeville","Andersonville","Rogers Park","Portage Park","Jefferson Park","Beverly","Evanston","Oak Park","Naperville","Schaumburg"],
  "areas_note": "This list is where we start. Your own reach decides the plan, so if your neighborhood or suburb is missing, ask and we will tell you straight whether it is winnable.",
  "more_cities": ["local-seo-los-angeles", "local-seo-houston", "local-seo-phoenix", "local-seo-dallas", "local-seo-san-diego"],

  "faq": [
    ("Do you need to be in Chicago to rank my business here?", "No. What Google weighs is your location, your profile, your reviews, and your site. We run Chicago campaigns remotely and the work is the same."),
    ("Can one profile cover the city and the suburbs?", "No single listing reaches all of Chicagoland. You win the area around your address first, then reach further with neighborhood and suburb pages as the profile gets stronger."),
    ("How long until I see results?", "Usually three to six months to start seeing big results. Some neighborhoods move sooner than others, and we tell you which yours is before you commit."),
    ("We are in the suburbs and want customers in the city too. Can we reach them?", "Yes, in steps. The towns around your address come first. The city neighborhoods closest to you come next, each with its own page. A second listing needs a real staffed office, and a virtual office or a mailbox can get the whole profile suspended."),
    ("Winter is our busy season. When should we start?", "Before it. Spring or summer is best, so the profile and pages have months to settle before the first cold snap. Starting later still helps, mostly with the winter after."),
    ("What does it cost?", "Campaigns start at $1,500 a month, flat, with no setup fee. Month to month."),
  ],

  "cta_h": "Find out which parts of Chicago you can win.",
  "cta_p": "We map where you rank across the city and the suburbs you serve, show you which neighborhoods are winnable now, and tell you what it takes.",
}

SAN_ANTONIO = {
  "slug": "local-seo-san-antonio",
  "city": "San Antonio",
  "short": "San Antonio",
  "region": "the San Antonio area",
  "title": "Local SEO Agency in San Antonio | LocalScaling",
  "meta": "Local SEO for San Antonio service businesses. We get contractors, clinics, and practices into the Google map pack and the search results under it, from Stone Oak to Southtown and out to New Braunfels. Starting at $1,500/mo.",
  "eyebrow": "Serving San Antonio and the towns around it",
  "h1": "Local SEO agency in San Antonio",
  "lede": "We get local service businesses into the map pack and the search results under it, in the San Antonio neighborhoods and nearby towns their customers search from. The city keeps growing outward past its loops, and people search by the part of town they live in.",

  "why_eyebrow": "Why San Antonio is different",
  "why_h2": "Small cities inside a big one",
  "why_paragraphs": [
    "San Antonio has small cities inside it. Alamo Heights, Olmos Park, Terrell Hills, Castle Hills, Leon Valley, and Windcrest each sit within the larger city with their own names, and the people who live there search with those names. An AC company in Leon Valley will not show on the map for a homeowner in Windcrest, and a physical therapy clinic in Stone Oak will not show for a family in Southtown, however strong the profile.",
    ("pull", "Every new subdivision past 1604 is one more place name someone will type into Google."),
    "The city keeps spreading. Loop 410 and Loop 1604 ring it, and much of the newer building sits past 1604, out toward Alamo Ranch, Helotes, and Stone Oak. Up I-35 the suburbs run northeast through Live Oak, Universal City, and Schertz toward New Braunfels, and Boerne sits to the northwest in the Hill Country. Each one searches by its own name.",
    "Summers are long and hot, and an air conditioner that quits in July is an emergency. Heavy rain can flood low water crossings in a few hours. Google decides who shows up on those days from what your profile and site looked like before them.",
    "San Antonio is a military city. Joint Base San Antonio covers Fort Sam Houston, Lackland, and Randolph, and families arrive all year with no plumber, no vet, and no accountant here yet. They find one by searching the neighborhood they just moved into.",
  ],

  "search_example": "ac repair Stone Oak",
  "pack_rows": [("Your business", "Air conditioning contractor · 0.9 mi"), ("Another company", "HVAC contractor · 1.8 mi"), ("Another company", "Air conditioning repair service · 2.7 mi")],
  "organic_rows": [("AC repair and replacement in Stone Oak", "yourbusiness.com"), ("AC repair in Stone Oak", "a directory"), ("Another company", "anothercompany.com")],
  "both_intro": "When someone in San Antonio searches for what you do, Google shows the map first and the regular results under it, and both are drawn around the neighborhood or town they are searching from. A business that holds a spot in both, in that place, gets the call.",

  "how_h2": "Built around how San Antonio searches",
  "how": [
    ("We measure your real reach first", "We check where your profile ranks from a grid of points across the city and the towns you serve, from Helotes over to Converse. A search from your own office says little about the rest. The plan is built on the grid."),
    ("We build a page for each neighborhood and town", "Nobody in Boerne searches for an electrician in San Antonio. They type Boerne, and a family in Alamo Heights types Alamo Heights. Your site and profile are built around the names people actually use."),
    ("We are ready before the heat", "For cooling, plumbing, pest control, and anyone else the summer keeps busy, the profile, the pages, and the review push are in place by spring. The calls you get in July come from work done months before."),
    ("We put your license where people can check it", "In Texas, air conditioning and refrigeration contractors are licensed by the Texas Department of Licensing and Regulation, and anyone can look a license up on its site. Clinics and practices have their own state boards. Putting the number on your site and profile gives Google and the customer something to verify."),
  ],

  "included": [
    ("Google Business Profile", "The right categories, the services people search for, a service area drawn around the parts of town you actually work, photos, and posts. This is what wins the map."),
    ("Neighborhood and town pages", "One page for each place you want to win, written for that place. These are what put you in the results under the map."),
    ("Listings that match", "Your name, address, and phone the same on every directory Google compares, including the Texas and trade ones."),
    ("Review generation", "A follow-up that asks every finished customer at the right moment, in English or Spanish."),
    ("Monthly reporting", "Where you rank on the grid, area by area, how that moved, and how many people called."),
    ("Your website", "Built for local search from the start, with a page for every area and every service. Every client gets one."),
  ],

  "areas_h2": "Areas we work across San Antonio and nearby towns",
  "areas": ["Alamo Heights","Olmos Park","Terrell Hills","Monte Vista","Tobin Hill","Southtown","King William","Dignowity Hill","Medical Center","Stone Oak","Shavano Park","Leon Valley","Helotes","Alamo Ranch","Windcrest","Live Oak","Universal City","Schertz","Boerne","New Braunfels"],
  "areas_note": "This list is where we start. Your own reach decides the plan, so if your part of town is missing, ask and we will tell you straight whether it is winnable.",
  "more_cities": ["local-seo-los-angeles", "local-seo-houston", "local-seo-phoenix", "local-seo-dallas", "local-seo-san-diego", "local-seo-chicago"],

  "faq": [
    ("Do you need to be in San Antonio to rank my business here?", "No. What Google weighs is your location, your profile, your reviews, and your site. We run San Antonio campaigns remotely and the work is the same."),
    ("Can one profile cover the whole city?", "No single listing reaches from Helotes to Schertz. You win the area around your address first, then reach further with neighborhood and town pages as the profile gets stronger."),
    ("How long until I see results?", "Usually three to six months to start seeing big results. Some parts of town move sooner than others, and we tell you which yours is before you commit."),
    ("We are in Alamo Heights. Should our pages say Alamo Heights or San Antonio?", "Both. People who live there search by the small city's name, and people nearby search for San Antonio. Your profile uses your real address, and your site gets a page for each name you want to win."),
    ("Our customers stretch from the city up to New Braunfels. Where do we start?", "Where you are. The neighborhoods around your address come first, then the towns along the way, each with its own page. A second listing up the highway needs a real staffed office, and a virtual office or a mailbox can get the whole profile suspended."),
    ("What does it cost?", "Campaigns start at $1,500 a month, flat, with no setup fee. Month to month."),
  ],

  "cta_h": "Find out which parts of San Antonio you can win.",
  "cta_p": "We map where you rank across the city and the towns you serve, show you which areas are winnable now, and tell you what it takes.",
}

AUSTIN = {
  "slug": "local-seo-austin",
  "city": "Austin",
  "short": "Austin",
  "region": "the Austin area",
  "title": "Local SEO Agency in Austin | LocalScaling",
  "meta": "Local SEO for Austin service businesses. We get contractors, clinics, and firms into the Google map pack and the search results under it, from Hyde Park to Circle C and up to Round Rock. Starting at $1,500/mo.",
  "eyebrow": "Serving Austin and the Hill Country towns around it",
  "h1": "Local SEO agency in Austin",
  "lede": "We get local service businesses into the map pack and the search results under it, in the Austin neighborhoods and nearby towns their customers search from. New people arrive here all the time, and they find every service they need by searching the name of the place they just moved to.",

  "why_eyebrow": "Why Austin is different",
  "why_h2": "A city full of people with no one to call yet",
  "why_paragraphs": [
    "Austin keeps filling with people who just got here. They have no family dentist, no electrician, and no lawyer they trust, and nobody to ask. So they search, and they read the reviews harder than someone who grew up here would. The businesses they find in their first year are often the ones they keep.",
    ("pull", "Someone who moved to Leander last month types Leander. They do not type Austin."),
    "The growth runs along I-35. North of the city it reaches Pflugerville, Round Rock, and Georgetown, south it reaches Buda and Kyle, and west it climbs into the Hill Country toward Lakeway and Bee Cave. Each of those towns is its own search. A law firm in Round Rock will not show on the map for a family in Kyle, and an electrician near Mueller will not show for a homeowner in Circle C, however strong the profile.",
    "Inside the city the river splits it. Locals talk about north and south of the river, and the older central neighborhoods like Hyde Park, Travis Heights, and Tarrytown have very different homes and needs from the new subdivisions at the edges. A page for each part of town lets you speak to the people who live there.",
    "The weather adds its own rushes. Summers are long and hot, heavy rain can flood creeks fast, and a rare hard freeze can send the whole city looking for help at once. Google decides who shows up on those days from what your profile and site looked like before them.",
  ],

  "search_example": "family lawyer Round Rock",
  "pack_rows": [("Your firm", "Family law attorney · 0.8 mi"), ("Another firm", "Family law attorney · 1.9 mi"), ("Another firm", "Law firm · 3.2 mi")],
  "organic_rows": [("Divorce and custody lawyer in Round Rock", "yourfirm.com"), ("Family lawyers in Round Rock", "a directory"), ("Another firm", "anotherfirm.com")],
  "both_intro": "When someone in the Austin area searches for what you do, Google shows the map first and the regular results under it, and both are drawn around the neighborhood or town they are searching from. A business that holds a spot in both, in that place, gets the call.",

  "how_h2": "Built around how Austin searches",
  "how": [
    ("We measure your real reach first", "We check where your profile ranks from a grid of points across the city and the towns you serve, from Cedar Park down to Buda. A search from your own desk tells you very little about the rest. The plan is built on the grid."),
    ("We build a page for each neighborhood and town", "Nobody in Georgetown searches for a dentist in Austin. They type Georgetown, and a family in Travis Heights types Travis Heights. Your site and profile are built around the names people actually use."),
    ("We write for the newcomer", "Someone new to town reads more before they call. Your pages answer what they would have asked a neighbor: who you are, what you do, the areas you cover, and what working with you is like. Your reviews do the rest."),
    ("We put your license where people can check it", "In Texas, electricians and electrical contractors are licensed by the Texas Department of Licensing and Regulation, and anyone can search a license on its site. Health, legal, and financial practices answer to their own state bodies. A number on your site and profile gives Google and the customer something to verify."),
  ],

  "included": [
    ("Google Business Profile", "The right categories, the services people search for, a service area drawn around the parts of town you really work, photos, and posts. This is what wins the map."),
    ("Neighborhood and town pages", "One page for each place you want to win, written for the people who live there. These are what put you in the results under the map."),
    ("Listings that match", "Your name, address, and phone the same on every directory Google compares, including the Texas and industry ones."),
    ("Review generation", "A follow-up that asks every happy customer at the right moment, so new arrivals have plenty of recent reviews to read."),
    ("Monthly reporting", "Where you rank on the grid, area by area, how that moved, and how many people called."),
    ("Your website", "Built for local search from the start, with a page for every area and every service. Every client gets one."),
  ],

  "areas_h2": "Areas we work across Austin and nearby towns",
  "areas": ["Hyde Park","Clarksville","Tarrytown","Travis Heights","Bouldin Creek","Zilker","Mueller","Allandale","Crestview","Circle C Ranch","West Lake Hills","Round Rock","Cedar Park","Leander","Georgetown","Pflugerville","Lakeway","Bee Cave","Kyle","Buda"],
  "areas_note": "This list is where we start. Your own reach decides the plan, so if your part of town is missing, ask and we will tell you straight whether it is winnable.",
  "more_cities": ["local-seo-los-angeles", "local-seo-houston", "local-seo-phoenix", "local-seo-dallas", "local-seo-san-diego", "local-seo-chicago", "local-seo-san-antonio"],

  "faq": [
    ("Do you need to be in Austin to rank my business here?", "No. What Google weighs is your location, your profile, your reviews, and your site. We run Austin campaigns remotely and the work is the same."),
    ("Can one profile cover Austin, Round Rock, and Kyle?", "No single listing reaches that far. You win the area around your address first, then reach further with town pages as the profile gets stronger."),
    ("How long until I see results?", "Usually three to six months to start seeing big results. Some parts of town move sooner than others, and we tell you which yours is before you commit."),
    ("Our office is in Cedar Park. Should our pages say Cedar Park or Austin?", "Both, each on its own page. People who live there search for Cedar Park, and people further in search for Austin. Your profile keeps your real address, and your site gets a page for each name you want to win."),
    ("We are south of the river and a lot of our customers are north. Is that a problem?", "Your service area and a page for each part of town cover the places you go. A second listing needs a real staffed office, and a virtual office or a mailbox can get the whole profile suspended."),
    ("What does it cost?", "Campaigns start at $1,500 a month, flat, with no setup fee. Month to month."),
  ],

  "cta_h": "Find out which parts of Austin you can win.",
  "cta_p": "We map where you rank across the city and the towns you serve, show you which areas are winnable now, and tell you what it takes.",
}

JACKSONVILLE = {
  "slug": "local-seo-jacksonville",
  "city": "Jacksonville",
  "short": "Jacksonville",
  "region": "the Jacksonville area",
  "title": "Local SEO Agency in Jacksonville | LocalScaling",
  "meta": "Local SEO for Jacksonville service businesses. We get contractors, clinics, and agencies into the Google map pack and the search results under it, from Riverside to the Beaches and down to Mandarin. Starting at $1,500/mo.",
  "eyebrow": "Serving Jacksonville, the Beaches, and the towns around them",
  "h1": "Local SEO agency in Jacksonville",
  "lede": "We get local service businesses into the map pack and the search results under it, in the Jacksonville neighborhoods and nearby towns their customers search from. The city covers a huge area, and people here search by the side of the river they live on and the name of their neighborhood.",

  "why_eyebrow": "Why Jacksonville is different",
  "why_h2": "One city spread across a whole county",
  "why_paragraphs": [
    "Jacksonville and Duval County merged into one government decades ago, so the city reaches from the farmland out west to the Atlantic. On paper it is one place. In search it is dozens. A family in Mandarin types Mandarin, and a homeowner in Arlington types Arlington. An insurance agency in Riverside will not show on the map for someone in Oceanway, however strong the profile.",
    ("pull", "Someone in Neptune Beach types Neptune Beach. Jacksonville is the place over the bridge."),
    "The St. Johns River runs through the middle, and the bridges decide where people are willing to drive. Locals sort the city into the Northside, the Westside, the Southside, Arlington, and the Beaches. Atlantic Beach, Neptune Beach, and Jacksonville Beach are their own cities, and Ponte Vedra Beach and Nocatee to the south sit in St. Johns County. Orange Park and Fleming Island to the southwest are in Clay County. Each one searches by its own name.",
    "Every hurricane season, people here watch the forecast and start making calls. Roofers, tree crews, insurance agents, and restoration companies all get busy around a storm, and so does anyone who fixes what water and wind leave behind. Google decides who shows up on those days from what your profile and site looked like before them.",
  ],

  "search_example": "home insurance agent Mandarin",
  "pack_rows": [("Your agency", "Insurance agency · 0.7 mi"), ("Another agency", "Insurance agency · 1.8 mi"), ("Another agency", "Insurance broker · 3.0 mi")],
  "organic_rows": [("Home and flood insurance in Mandarin", "youragency.com"), ("Insurance agents in Mandarin", "a directory"), ("Another agency", "anotheragency.com")],
  "both_intro": "When someone in the Jacksonville area searches for what you do, Google shows the map first and the regular results under it, and both are drawn around the neighborhood or town they are searching from. A business that holds a spot in both, in that place, gets the call.",

  "how_h2": "Built around how Jacksonville searches",
  "how": [
    ("We measure your real reach first", "We check where your profile ranks from a grid of points across the city and the towns you serve, from Fernandina Beach down to Nocatee. A search from your own office tells you very little about the other side of the river. The plan is built on the grid."),
    ("We build a page for each neighborhood and town", "Nobody in Fleming Island searches for a dentist in Jacksonville. They type Fleming Island, and a family in San Marco types San Marco. Your site and profile are built around the names people actually use."),
    ("We treat the Beaches as their own market", "The beach cities sit across the Intracoastal from the rest of town, and people there search close to home. If you want that work, it gets its own pages, its own reviews from beach customers, and its own spot on the grid."),
    ("We are ready before storm season", "For roofing, tree work, insurance, restoration, and anyone else a storm keeps busy, the profile, the pages, and the review push are in place by late spring. The calls that come in with a storm go to the businesses Google already trusts."),
  ],

  "included": [
    ("Google Business Profile", "The right categories, the services people search for, a service area drawn around the parts of town you really cover, photos, and posts. This is what wins the map."),
    ("Neighborhood and town pages", "One page for each place you want to win, written for the people who live there. These are what put you in the results under the map."),
    ("Listings that match", "Your name, address, and phone the same on every directory Google compares, including the Florida and industry ones."),
    ("Review generation", "A follow-up that asks every happy customer at the right moment, so each part of town has recent reviews from its own people."),
    ("Monthly reporting", "Where you rank on the grid, area by area, how that moved, and how many people called."),
    ("Your website", "Built for local search from the start, with a page for every area and every service. Every client gets one."),
  ],

  "areas_h2": "Areas we work across Jacksonville and nearby towns",
  "areas": ["Riverside","Avondale","Ortega","San Marco","San Jose","Springfield","Murray Hill","Mandarin","Arlington","Southside","Deerwood","Baymeadows","Oceanway","Atlantic Beach","Neptune Beach","Jacksonville Beach","Ponte Vedra Beach","Nocatee","Orange Park","Fleming Island"],
  "areas_note": "This list is where we start. Your own reach decides the plan, so if your part of town is missing, ask and we will tell you straight whether it is winnable.",
  "more_cities": ["local-seo-los-angeles", "local-seo-houston", "local-seo-phoenix", "local-seo-dallas", "local-seo-san-diego", "local-seo-chicago", "local-seo-san-antonio", "local-seo-austin"],

  "faq": [
    ("Do you need to be in Jacksonville to rank my business here?", "No. What Google weighs is your location, your profile, your reviews, and your site. We run Jacksonville campaigns remotely and the work is the same."),
    ("Can one profile cover the whole city and the Beaches?", "No single listing reaches from Oceanway to Ponte Vedra Beach. You win the area around your address first, then reach further with neighborhood and town pages as the profile gets stronger."),
    ("How long until I see results?", "Usually three to six months to start seeing big results. Some parts of town move sooner than others, and we tell you which yours is before you commit."),
    ("Our office is on the Westside and we want Southside customers. Is the river a problem?", "It makes the map harder, since Google weighs distance. Pages for the Southside neighborhoods you cover, a service area that includes them, and reviews from customers there are how you reach across. A second listing needs a real staffed office, and a virtual office or a mailbox can get the whole profile suspended."),
    ("We are in Orange Park. Should our pages say Orange Park or Jacksonville?", "Both, each on its own page. People who live there search for Orange Park, and people across the county line search for Jacksonville. Your profile keeps your real address, and your site gets a page for each name you want to win."),
    ("What does it cost?", "Campaigns start at $1,500 a month, flat, with no setup fee. Month to month."),
  ],

  "cta_h": "Find out which parts of Jacksonville you can win.",
  "cta_p": "We map where you rank across the city, the Beaches, and the towns you serve, show you which areas are winnable now, and tell you what it takes.",
}

FORT_WORTH = {
  "slug": "local-seo-fort-worth",
  "city": "Fort Worth",
  "short": "Fort Worth",
  "region": "Tarrant County and the towns around it",
  "title": "Local SEO Agency in Fort Worth | LocalScaling",
  "meta": "Local SEO for Fort Worth service businesses. We get contractors, clinics, and law firms into the Google map pack and the search results under it, from Fairmount to Keller and out to Weatherford. Starting at $1,500/mo.",
  "eyebrow": "Serving Fort Worth, the Mid-Cities, and Tarrant County",
  "h1": "Local SEO agency in Fort Worth",
  "lede": "We get local service businesses into the map pack and the search results under it, in the Fort Worth neighborhoods and nearby towns their customers search from. Fort Worth is half of DFW on a map, and in the search bar it behaves like its own region.",

  "why_eyebrow": "Why Fort Worth is different",
  "why_h2": "The west side of the Metroplex searches on its own",
  "why_paragraphs": [
    "People here say Fort Worth, and they mean it. Most of the city sits in Tarrant County, with its own courts, its own suburbs, and its own sense of where home ends. Someone in Benbrook looking for a contractor wants one close by, and a company across the county in Mesquite rarely shows up for them on the map.",
    ("pull", "A family in Keller types Keller. Fort Worth is where they drive for a night out at the Stockyards."),
    "Between the two big cities sit the Mid-Cities: Hurst, Euless, Bedford, and their neighbors. People there search by their own town name, and the map can pull in businesses from either direction. A clinic in North Richland Hills will not show for a patient in Mansfield, however strong the profile, and a firm near Sundance Square will not show for someone in Southlake.",
    "The growth keeps pushing outward. North along I-35W toward Alliance and Saginaw, south toward Burleson, southwest toward Benbrook, and west into Parker County toward Weatherford. New neighborhoods fill with families who have no plumber, dentist, or lawyer yet, and they find one by searching the name of the place they just moved to.",
    "The ground matters too. North Texas clay swells when it rains and shrinks in a dry summer, so foundations, driveways, and sprinkler lines all take a beating, and the busy weeks for those trades follow the weather. Google decides who shows up in those weeks from what your profile and site looked like before them.",
  ],

  "search_example": "foundation repair Keller",
  "pack_rows": [("Your business", "Foundation repair service · 0.9 mi"), ("Another company", "Foundation repair service · 2.1 mi"), ("Another company", "Contractor · 3.4 mi")],
  "organic_rows": [("Foundation repair in Keller, free inspection", "yourbusiness.com"), ("Foundation repair companies in Keller", "a directory"), ("Another company", "anothercompany.com")],
  "both_intro": "When someone in the Fort Worth area searches for what you do, Google shows the map first and the regular results under it, and both are drawn around the neighborhood or town they are searching from. A business that holds a spot in both, in that place, gets the call.",

  "how_h2": "Built around how Fort Worth searches",
  "how": [
    ("We measure your real reach first", "We check where your profile ranks from a grid of points across Fort Worth and the towns you serve, from Saginaw down to Burleson. A search from your own office tells you very little about the next town over. The plan is built on the grid."),
    ("We build a page for each neighborhood and town", "Nobody in Southlake searches for a dentist in Fort Worth. They type Southlake, and a family in Ryan Place types Ryan Place. Your site and profile are built around the names people actually use."),
    ("We pick a side of the Metroplex", "Most businesses here should win the Fort Worth side first. If you also want Dallas work, it gets its own plan once the west side is holding, because one profile cannot stretch across both."),
    ("We put your license where people can check it", "In Texas, electricians and air conditioning contractors are licensed by the Texas Department of Licensing and Regulation, and anyone can look a license up on its site. Lawyers, clinics, and other practices answer to their own state bodies. A number on your site and profile gives Google and the customer something to verify."),
  ],

  "included": [
    ("Google Business Profile", "The right categories, the services people search for, a service area drawn around the towns you really work, photos, and posts. This is what wins the map."),
    ("Neighborhood and town pages", "One page for each place you want to win, written for the people who live there. These are what put you in the results under the map."),
    ("Listings that match", "Your name, address, and phone the same on every directory Google compares, including the Texas and industry ones."),
    ("Review generation", "A follow-up that asks every happy customer at the right moment, so each town you serve has recent reviews from its own people."),
    ("Monthly reporting", "Where you rank on the grid, town by town, how that moved, and how many people called."),
    ("Your website", "Built for local search from the start, with a page for every area and every service. Every client gets one."),
  ],

  "areas_h2": "Areas we work across Fort Worth and nearby towns",
  "areas": ["Near Southside","Fairmount","Ryan Place","Arlington Heights","Rivercrest","Tanglewood","Wedgwood","Stockyards","Alliance","Saginaw","Keller","Southlake","North Richland Hills","Hurst","Euless","Bedford","Benbrook","Burleson","Mansfield","Weatherford"],
  "areas_note": "This list is where we start. Your own reach decides the plan, so if your part of town is missing, ask and we will tell you straight whether it is winnable.",
  "more_cities": ["local-seo-los-angeles", "local-seo-houston", "local-seo-phoenix", "local-seo-dallas", "local-seo-san-diego", "local-seo-chicago", "local-seo-san-antonio", "local-seo-austin", "local-seo-jacksonville"],

  "faq": [
    ("Do you need to be in Fort Worth to rank my business here?", "No. What Google weighs is your location, your profile, your reviews, and your site. We run Fort Worth campaigns remotely and the work is the same."),
    ("Can one profile cover Fort Worth and Dallas?", "No single listing reaches across the whole Metroplex. You win the area around your address first, then reach further with town pages as the profile gets stronger. Dallas is usually a separate push."),
    ("How long until I see results?", "Usually three to six months to start seeing big results. Some towns move sooner than others, and we tell you which yours is before you commit."),
    ("We are in the Mid-Cities. Should our pages say Fort Worth or our town?", "Both, each on its own page. People nearby search for Bedford or Euless, and people further out search for Fort Worth. Your profile keeps your real address, and your site gets a page for each name you want to win."),
    ("Our shop is in Fort Worth and a lot of our work is out in Parker County. Is that a problem?", "Your service area and a page for each town you drive to cover it. A second listing needs a real staffed office, and a virtual office or a mailbox can get the whole profile suspended."),
    ("What does it cost?", "Campaigns start at $1,500 a month, flat, with no setup fee. Month to month."),
  ],

  "cta_h": "Find out which parts of Fort Worth you can win.",
  "cta_p": "We map where you rank across Fort Worth and the towns you serve, show you which areas are winnable now, and tell you what it takes.",
}

PAGES = [LOS_ANGELES, HOUSTON, PHOENIX, DALLAS, SAN_DIEGO, CHICAGO, SAN_ANTONIO, AUSTIN, JACKSONVILLE, FORT_WORTH]
