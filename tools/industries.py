"""Industry page content. The results card, the year timeline, and the intent
table are illustrations, not data. Keep them that way.

Industry page content. One dict per industry, rendered by industry_page()
in build_pages.py. To add an industry: copy ACCOUNTANTS, change every value,
append it to PAGES, run the build. Keep every claim qualitative. No stats,
no client names, no results. Timing is three to six months."""

ACCOUNTANTS = {
  "slug": "local-seo-for-accountants",
  "title": "Local SEO for Tax Accountants and CPAs | LocalScaling",
  "meta": "Local SEO for tax accountants, CPAs, and bookkeeping firms. We get your practice into the Google map pack and the search results under it, in the neighborhoods you serve, ahead of tax season. Starting at $1,500/mo.",
  "crumb": "Tax accountants and CPAs",
  "eyebrow": "Local SEO for accountants",
  "h1": "Local SEO for tax accountants and CPAs",
  "lede": "Most people pick an accountant the way they pick a plumber. They search, they glance at the map, they scroll the listings under it, and they call one of the first few. We get your practice into both places in the neighborhoods you serve.",
  "short": "accountants",
  "industry_value": "Accounting or finance",

  "pack_search": "CPA near me",
  "pack_rows": [("Your firm", "Certified public accountant · 0.4 mi"), ("Another firm", "Accountant · 1.1 mi"), ("Another firm", "Tax preparation service · 2.3 mi")],
  "organic_rows": [("Tax accountant and CPA in your city", "yourfirm.com"), ("Top accountants near you", "a directory"), ("Another firm", "anotherfirm.com")],
  "pack_note": "Three spots. Most people never scroll past them.",
  "both_intro": "When someone searches for an accountant, Google shows the map first and the regular results under it. People glance at the map, then scroll to see who else is there. A firm that holds a spot in both gets the call more often than one that holds either alone.",

  "timeline": [(1, 4, "peak", "Phones ring"), (5, 8, "quiet", "Reviews, planning, city pages"), (9, 12, "build", "Profile, pages, listings")],
  "timeline_start": 9,
  "timeline_alt": "A twelve month timeline. Searches peak from January to April. The profile, pages, and listings are built from September to December so they are in place before the peak.",
  "timeline_caption": "The shape of an accountant's year. Google decides who shows up in January based on what it saw in the fall, so the build happens in the fall.",

  "intent": [
    ("CPA near me", "Someone ready to call this week", "Your Google Business Profile"),
    ("small business accountant [city]", "An owner comparing two or three firms", "A service page"),
    ("tax preparer [city]", "A person with a deadline and a shoebox", "A service page and the profile"),
    ("bookkeeping services [city]", "A business tired of doing it themselves", "A service page"),
    ("accountant in [the town next door]", "A neighbor who does not know you exist", "A city page"),
    ("CPA for dentists", "A practice that wants someone who knows their world", "A specialty page"),
  ],

  "why_eyebrow": "Why accounting is different",
  "why_h2": "Referrals built your firm. Search decides who grows it.",
  "why_paragraphs": [
    "Referrals still bring the best clients. They no longer bring enough of them. The person a client refers still looks you up before calling, and the person with no referral goes straight to the map. If you are not in the top three, they call someone who is.",
    "Then there is the calendar. Searches for a tax preparer climb every January and fall away in April. Google decides who shows up in that window months earlier, based on what your profile, your reviews, and your website looked like in the fall.",
    ("pull", "The firms that fill up in March did the work in October."),
    "The last difference is trust. Nobody hands their finances to a name on a map without checking. Your license, your reviews, and a site that explains what you do in plain language carry more weight here than in almost any other local search.",
  ],

  "leaks_h2": "Six things we find on most accounting firm profiles",
  "leaks_intro": "None of them is dramatic. Together they are the difference between page one and nowhere.",
  "leaks": [
    ("The wrong primary category", "Listed as a generic business or financial service instead of accountant, CPA, or tax preparation service. Google can only rank you for what you say you are."),
    ("One page called Services", "Tax prep, bookkeeping, payroll, and business returns all on one page. Google ranks whole pages, so a page that covers four services ranks for none of them."),
    ("Reviews that stop in April", "A burst of reviews at filing time and silence for eight months. Google reads the gap as a business that went quiet."),
    ("An old suite number on the directories", "The firm moved years ago. The old address is still on half the listings Google checks, and the mismatch drags the profile down."),
    ("No page for the towns next door", "You take clients from four cities. Your site mentions one. The other three are searching and finding someone else."),
    ("A site that says contact us", "The person who found you wants to book a consultation. The page gives them a phone number and a form with no reason to fill it in."),
  ],

  "how_h2": "Built around how people find an accountant",
  "how": [
    ("We pick the right category and stick to it", "Google has separate categories for accountant, certified public accountant, tax preparation service, and bookkeeping service. The primary one decides which searches you can win. We choose it for the work you want more of, which is often different from the work you do most."),
    ("We build a page for each service", "You probably do tax preparation, bookkeeping, payroll, business returns, and IRS representation. Each one gets its own page, written for the person searching for it. Those pages are what put you in the results under the map. A single services page ranks for none of them."),
    ("We put your credentials where Google and clients can see them", "Your CPA license, your state board registration, and your firm registration go on the site and on the profile, and they match. It is one of the few trust signals a search engine can check."),
    ("We ask for reviews when clients are happiest", "Right after a return is filed, while the relief is fresh. A follow-up that goes out at that moment turns good work into public proof, and keeps it coming after April."),
    ("We do the work in the right order", "Category and listings first, because everything else sits on them. Then service pages, then city pages, then reviews. Starting with content on a profile that is set up wrong wastes the content."),
    ("We report what you can bank", "Each month you see where you rank across your area, how that moved, and how many people called or booked. Traffic numbers stay off the report because nobody pays you in traffic."),
  ],

  "searches_h2": "What your next client is typing",
  "searches": ["business tax accountant", "accountant for self employed", "IRS help near me", "payroll services", "tax planning for small business", "quarterly taxes help", "S corp accountant", "catch up bookkeeping"],
  "specialty_searches": ["accountant for real estate investors", "CPA for dentists", "CPA for contractors", "startup accountant", "nonprofit accounting", "expat tax accountant", "forensic accountant", "multi state tax accountant", "restaurant bookkeeping", "trucking company accountant"],
  "searches_note": "Add your city to any of these and that is the search. The specialty ones have fewer firms competing and better clients behind them. Each one needs its own page, and that is most of the work.",

  "included": [
    ("Google Business Profile", "The right primary category, services listed the way people search for them, and posts through tax season. This is what wins the map."),
    ("Service pages", "One page for each service you want more of, written for the person typing the search. This is what wins the listing under the map."),
    ("City pages", "One page for each town you take clients from, so the neighbors can find you too."),
    ("Listings that match", "Your firm name, address, and phone matched across the directories Google checks, including the accounting ones."),
    ("Review generation", "A follow-up that asks right after filing, when clients are relieved, and keeps asking through the year."),
    ("Your website", "Built for local search, with your credentials up front, a way to book, and a structure that gets stronger every year."),
  ],

  "fit_h2": "Who this works for",
  "fit_yes": [
    "A firm with an office, or a defined area you take clients from",
    "One to a handful of partners who want more local clients",
    "You already do good work and have clients who would say so",
    "You can start before tax season, so the work lands in time",
  ],
  "fit_no": [
    "A fully remote firm with no local presence to rank",
    "You need results by this April and it is already February",
    "You want blog posts by the dozen instead of clients",
    "You want the cheapest option. We are not it",
  ],

  "faq": [
    ("We work with clients remotely. Can you still rank us locally?", "Yes, as long as you have a real office address or a defined service area. Google ranks you around that, and remote clients come on top of it."),
    ("How long until we see results?", "Usually three to six months to start seeing big results. For accountants the timing matters more than the length. Start in the fall so the work lands before January."),
    ("We tried SEO before and nothing happened. Why would this be different?", "Most accounting firm SEO is blog posts on a profile that was set up wrong. We fix the category, the listings, and the pages first. That is the part that moves the map, and it is usually the part that was skipped."),
    ("Our website already looks professional. Is that not enough?", "A good looking site and a site that ranks are different things. Google cannot see design. It reads categories, pages, listings, and reviews. Plenty of beautiful firm sites are invisible on the map."),
    ("How do we compete with the big national chains?", "Nobody beats a national chain on the head terms, so we skip them. You win your own city and the specialty searches the chains ignore, which is where the better clients are anyway. A local firm with the right pages beats a national brand on a local search more often than you would think."),
    ("Do you write tax content for our site?", "We write service pages and city pages. We do not give tax advice on your site, and anything technical goes past you before it publishes."),
    ("We have two offices. Does that change things?", "Each office gets its own profile, its own page, and its own reviews. Google treats them as two businesses, so we do too."),
    ("What does it cost?", "Campaigns start at $1,500 a month, flat, with no setup fee. Month to month."),
  ],

  "cta_h": "Fill your calendar before January.",
  "cta_p": "Start with a free audit of your profile, your reviews, and the three firms ranking above you.",
}

DENTISTS = {
  "slug": "local-seo-for-dentists",
  "title": "Local SEO for Dentists and Dental Practices | LocalScaling",
  "meta": "Local SEO for dentists. We get your practice into the Google map pack and the search results under it for the neighborhoods your patients live in, for the services you want more of. Starting at $1,500/mo.",
  "crumb": "Dentists",
  "eyebrow": "Local SEO for dentists",
  "h1": "Local SEO for dentists and dental practices",
  "lede": "A new patient picks a dentist on a phone, in about a minute. They search, look at the map, read a few reviews, and scroll the listings under it. We get your practice into both places for the neighborhoods your patients live in and the services you want more of.",
  "short": "dentists",
  "industry_value": "Dental",
  "you": "Your practice",

  "pack_search": "dentist near me",
  "pack_rows": [("Your practice", "Dentist · 0.6 mi"), ("Another practice", "Dental clinic · 1.3 mi"), ("Another practice", "Cosmetic dentist · 2.1 mi")],
  "organic_rows": [("Family dentist in your city, new patients welcome", "yourpractice.com"), ("Best dentists near you", "a directory"), ("Another practice", "anotherpractice.com")],
  "pack_note": "Three spots. Most patients pick from these.",
  "both_intro": "When someone searches for a dentist, Google shows the map first and the regular results under it. They read the reviews on the map, then scroll to see who has a real website. A practice that holds a spot in both gets the booking more often than one that holds either alone.",

  "timeline": [(1, 2, "peak", "New benefits"), (3, 4, "quiet", "Steady"), (5, 7, "build", "Profile and pages"), (8, 8, "peak", "School"), (9, 10, "quiet", "Reviews"), (11, 12, "peak", "Benefits rush")],
  "timeline_start": 5,
  "timeline_alt": "A twelve month timeline. New patient searches bump in January and February when insurance benefits reset, in August before school starts, and in November and December when unused benefits are about to expire. The profile and pages are built from May to July so they are in place before the busy stretches.",
  "timeline_caption": "The shape of a dental practice's year. Demand never really stops, but it bumps in August and again when unused benefits expire in December. A build that starts in late spring is in place for both.",

  "intent": [
    ("dentist near me", "Someone new to the area, or in pain, choosing today", "Your Google Business Profile"),
    ("emergency dentist [city]", "A person with a broken tooth who will call the first open office", "A service page and the profile"),
    ("dental implants [city]", "A patient comparing three practices on a big decision", "A service page"),
    ("Invisalign [city]", "An adult who has been thinking about it for a year", "A service page"),
    ("pediatric dentist [city]", "A parent picking for two or three kids at once", "A service page"),
    ("dentist in [the suburb next door]", "A family fifteen minutes away who does not know you exist", "A city page"),
  ],

  "why_eyebrow": "Why dentistry is different",
  "why_h2": "Patients choose from the map, and they choose fast",
  "why_paragraphs": [
    "Most people do not shop for a dentist until something forces them to. A move, a new insurance plan, a cracked tooth on a Saturday. When it happens they open Google Maps, look at the three practices closest to them, and read the reviews. The whole decision takes a minute. If you are not in that map, you are not in the decision.",
    "Reviews carry more weight here than in almost any other local search. Nobody lets a stranger work in their mouth on the strength of a logo. Patients read what other patients said, and Google reads the same reviews to decide who ranks. A practice with recent, specific reviews wins both.",
    ("pull", "A practice that is booked out has no reason to be on page two. Google does not know you are good until your patients say so where it can read it."),
    "Then there is the calendar. Dental demand never fully stops, but it bumps when benefits reset in January, when school is about to start, and when unused benefits are about to expire in December. Google decides who shows up in those weeks based on what your profile, your reviews, and your website looked like months earlier.",
  ],

  "leaks_h2": "Six things we find on most dental practice profiles",
  "leaks_intro": "Each one is small. Together they are the difference between the map and nowhere.",
  "leaks": [
    ("The practice and the dentist competing with each other", "The office has a profile and so does the doctor, with a different name and a different phone. Google cannot tell which one is the business, so it trusts neither."),
    ("A category that undersells you", "Listed as a dental clinic when the searches you want are cosmetic dentist, pediatric dentist, or emergency dental service. Google can only rank you for what you say you are."),
    ("One page called Services", "Cleanings, implants, Invisalign, veneers, and emergencies on one page. Google ranks whole pages, so a page about everything ranks for nothing."),
    ("Reviews with no words in them", "Dozens of five star ratings and no text. Patients skip them and Google learns nothing about what you do or where you are."),
    ("An old phone number on the directories", "The practice changed its number or moved down the road years ago. The old details are still on half the listings Google checks, and the mismatch drags the profile down."),
    ("No way to book from the page", "The person who found you at ten at night wants an appointment. The site offers a phone number and office hours, so they book with the practice that had a button."),
  ],

  "how_h2": "Built around how people find a dentist",
  "how": [
    ("We fix the profile before anything else", "One profile for the practice, one for each dentist if it earns its place, and the same name and phone on both. Then the right primary category for the patients you want, the services listed the way people search for them, and photos of the actual office."),
    ("We build a page for each service", "Implants, Invisalign, veneers, crowns, emergencies, kids, sedation. Each one gets its own page, written for the patient searching for it. Those pages are what put you in the results under the map."),
    ("We put your credentials where Google and patients can see them", "Your state dental board license, your degrees, and your memberships go on the site and on the profile, and they match. A patient can check them, and so can a search engine."),
    ("We ask for reviews when patients are happiest", "At the front desk after a good visit, with a text that makes it a two tap job. The ask mentions the service, so the review does too, and Google learns what you are good at."),
    ("We do the work in the right order", "Profile and listings first, because everything else sits on them. Then service pages, then pages for the suburbs you draw from, then reviews. Content on a profile that is set up wrong is content nobody sees."),
    ("We report what you can bank", "Each month you see where you rank across your area for the searches that matter, how that moved, and how many people called or booked. Traffic stays off the report because nobody pays you in traffic."),
  ],

  "searches_h2": "What your next patient is typing",
  "searches": ["dentist open Saturday", "dentist that takes my insurance", "teeth cleaning near me", "tooth extraction cost", "dentist accepting new patients", "wisdom teeth removal", "root canal near me", "dental crown same day"],
  "specialty_searches": ["emergency dentist open now", "dental implants", "Invisalign dentist", "pediatric dentist", "sedation dentist", "veneers", "dentures near me", "TMJ dentist", "sleep apnea dentist", "dentist that takes Medicaid", "Spanish speaking dentist", "dentist for anxious patients"],
  "searches_note": "Add your city or suburb to any of these and that is the search. The specialty ones have fewer practices competing and higher case values behind them. Each one needs its own page, and that is most of the work.",

  "included": [
    ("Google Business Profile", "The right primary category, services listed the way patients search for them, photos of the real office, and posts through the busy stretches. This is what wins the map."),
    ("Service pages", "One page for each treatment you want more of, written for the patient typing the search. This is what wins the listing under the map."),
    ("City pages", "One page for each suburb or neighborhood you draw patients from, so the families fifteen minutes away can find you too."),
    ("Listings that match", "Your practice name, address, and phone matched across the directories Google checks, including the dental and insurance ones."),
    ("Review generation", "A follow-up that asks after a good visit, mentions the treatment, and keeps asking all year instead of in bursts."),
    ("Your website", "Built for local search, with your credentials up front, online booking, and a structure that gets stronger every year."),
  ],

  "fit_h2": "Which practices this is for",
  "fit_yes": [
    "A practice with one office, or a few, and a defined area you draw patients from",
    "One or a handful of dentists who want more of a particular kind of case",
    "You already do good work and have patients who would say so",
    "You can give it three to six months before you judge it",
  ],
  "fit_no": [
    "A practice with no fixed address, or one that is about to move",
    "You want new patients next week. That is an ads job",
    "You want blog posts by the dozen instead of patients",
    "You are shopping on price. There are cheaper options and they are not us",
  ],

  "faq": [
    ("We have several dentists. Does each one need a profile?", "Sometimes. Google allows a profile for the practice and one for each practitioner. They help when a dentist is known by name or has a specialty. They hurt when they carry a different phone number or address. We set them up so they support the practice instead of competing with it."),
    ("How long until we see new patients?", "Usually three to six months to start seeing big results. Fixing the profile and listings moves the map first. Service pages and reviews take longer and keep building."),
    ("We are already busy. Why would we need this?", "Busy with the wrong cases, or busy this year. A practice that ranks for implants and Invisalign chooses its schedule. A practice that only ranks for its own name fills up with whoever walks in, and that changes the day a chain opens down the road."),
    ("Can we compete with the big dental chains?", "On the map, yes. Google ranks the closest, best reviewed, best described practice, and a chain location is one profile like yours. You win your own neighborhoods and the specialty searches the chains do not bother with."),
    ("Do you write about treatments on our site?", "We write service pages and city pages. Anything clinical goes past you before it publishes, and we make no claims about outcomes."),
    ("What about the reviews we cannot control?", "You reply to every one, and we help you do it without confirming anyone was a patient. A calm reply to a bad review does more for the next reader than five more good ones."),
    ("We are opening a second location. What changes?", "Almost everything doubles. The new office gets its own profile, its own page, and its own reviews from day one, and the two never share a phone number. Google treats them as two businesses, and so do we."),
    ("What does it cost?", "Campaigns start at $1,500 a month, flat, with no setup fee. Month to month."),
  ],

  "cta_h": "Fill the schedule with the cases you want.",
  "cta_p": "Start with a free audit of your profile, your reviews, and the three practices ranking above you.",
}

PLUMBERS = {
  "slug": "local-seo-for-plumbers",
  "title": "Local SEO for Plumbers and Plumbing Companies | LocalScaling",
  "meta": "Local SEO for plumbers. We get your plumbing company into the Google map pack and the search results under it, in the towns your trucks drive to, for the jobs you want more of. Starting at $1,500/mo.",
  "crumb": "Plumbers",
  "eyebrow": "Local SEO for plumbers",
  "h1": "Local SEO for plumbers and plumbing companies",
  "lede": "Most plumbing calls start with a search on a phone, often with water on the floor. People look at the map, tap the first plumber who looks open and trusted, and scroll the listings under it when the job is bigger. We get your company into both places in the towns your trucks already drive to.",
  "short": "plumbers",
  "industry_value": "Plumbing",
  "you": "Your company",

  "pack_search": "plumber near me",
  "pack_rows": [("Your company", "Plumber · 0.7 mi"), ("Another company", "Plumber · 1.5 mi"), ("Another company", "Drainage service · 2.6 mi")],
  "organic_rows": [("Water heater replacement in your town", "yourcompany.com"), ("Plumbers near you", "a directory"), ("Another company", "anothercompany.com")],
  "pack_note": "Three spots. In an emergency, most people call one of these.",
  "both_intro": "When someone searches for a plumber, Google shows the map first and the regular results under it. The person with a burst pipe calls from the map. The person pricing a new water heater or a sewer line scrolls down and reads. A company that holds a spot in both gets the emergency and the big job.",

  "timeline": [(1, 2, "peak", "Cold snaps, heaters"), (3, 5, "quiet", "Remodels, repipes"), (6, 9, "build", "Profile and pages"), (10, 10, "quiet", "Reviews"), (11, 12, "peak", "Holiday drains")],
  "timeline_start": 6,
  "timeline_alt": "A twelve month timeline. Calls climb in January and February with cold snaps and water heater failures, stay steady through spring with remodels and repipes, and climb again in November and December with holiday drains and the first freezes. The profile and pages are built from June to September so they are in place before the winter rush.",
  "timeline_caption": "The shape of a plumber's year in a cold climate. Emergencies never stop, but the winter weeks are the loud ones. A build that starts in summer is in place before the first freeze.",

  "intent": [
    ("plumber near me", "Someone with water on the floor who will call the first number that looks right", "Your Google Business Profile"),
    ("emergency plumber [city]", "A homeowner late at night who wants a person to answer", "The profile and a service page"),
    ("water heater replacement [city]", "A household comparing two or three quotes this week", "A service page"),
    ("sewer line repair [city]", "A big job, and a customer who reads everything before calling", "A service page"),
    ("slab leak detection", "Someone who just found a warm spot on the floor", "A service page"),
    ("plumber in [the town next door]", "A homeowner twenty minutes away who has never heard of you", "A city page"),
  ],

  "why_eyebrow": "Why plumbing is different",
  "why_h2": "Half your calls cannot wait, and the other half shop around",
  "why_paragraphs": [
    "An emergency search is over in a minute. Nobody with a burst pipe reads five websites. They open the map, look for a plumber who is close, open now, and has recent reviews, and they tap call. If you are not one of the first three at that moment, the job goes to someone who is.",
    "The bigger jobs work the other way. A water heater, a repipe, a sewer line, a remodel. The customer takes a day or a week, gets quotes, and reads the sites of the companies they found. That is where the listings under the map carry the weight.",
    ("pull", "The map wins the burst pipe. Your website wins the repipe."),
    "Then there are the ads. Many plumbing searches show paid listings above the map, and they stop the day the budget does. The map and the results under it keep sending calls whether or not you paid this month, and that is the part we build.",
  ],

  "leaks_h2": "Six things we find on most plumbing company profiles",
  "leaks_intro": "Each one looks minor. Together they are why the phone rings for the company down the road.",
  "leaks": [
    ("A service area drawn around the whole state", "Or a home address showing on the map when the business runs from trucks. Google ranks you around a real place, and a service area that claims everywhere reaches nowhere in particular."),
    ("Hours that do not match the phone", "The profile says open 24 hours and the phone goes to voicemail at night, or it says closed when you do take emergency calls. Both lose the job, and the first one earns bad reviews."),
    ("One page called Services", "Drains, water heaters, leaks, sewer lines, and gas lines on one page. Google ranks whole pages, so a page about every job ranks for none of them."),
    ("Stock photos of someone else's van", "Customers want to see the truck that will park in their driveway. A profile with real photos of your crew and your work gets chosen over one with none."),
    ("A different phone number on every directory", "Old ad tracking numbers and a line from before the move, scattered across the listings Google checks. The mismatch drags the profile down."),
    ("Reviews that stopped when the office manager left", "Someone used to ask. Nobody does now. Google reads the gap as a business that went quiet, and so do customers."),
  ],

  "how_h2": "Built around how people find a plumber",
  "how": [
    ("We set up the service area the way Google expects", "Most plumbing companies work from trucks, so the profile is set up as a service area business, the address is handled correctly, and the towns listed are the ones you really drive to."),
    ("We pick the categories that match the work", "Plumber is the primary. Secondary categories such as drainage service, septic system service, or gas installation service go on only when they are a real part of the business that a customer could hire on its own."),
    ("We build a page for each job", "Water heaters, drain clearing, leak detection, sewer lines, repipes, gas lines. Each one gets its own page, written for the person searching for it. Those pages are what put you in the results under the map, and they bring the bigger tickets."),
    ("We make calling you the easiest thing on the page", "A call button at the top on a phone, hours that are true, and your license number where your state issues one. The person in a hurry should be able to call in one tap."),
    ("We ask for reviews at the truck", "The tech asks before leaving, while the customer is still relieved, and a text follows with a link that names the job. The review mentions the work, so Google learns what you do and where you do it."),
    ("We report calls", "Each month you see where you rank across your service area, how that moved, and how many people called. Traffic stays off the report because nobody pays you in traffic."),
  ],

  "searches_h2": "What your next customer is typing",
  "searches": ["plumber open now", "leaking pipe repair", "toilet repair near me", "garbage disposal installation", "low water pressure fix", "water heater not working", "clogged kitchen sink", "sump pump replacement"],
  "specialty_searches": ["tankless water heater installation", "sewer camera inspection", "hydro jetting", "slab leak detection", "whole house repipe", "gas line installation", "water softener installation", "backflow testing", "trenchless sewer repair", "well pump repair", "commercial plumber", "bathroom remodel plumbing"],
  "searches_note": "Add your town to any of these and that is the search. The specialty ones have fewer plumbers competing and bigger tickets behind them. Each one needs its own page, and that is most of the work.",

  "included": [
    ("Google Business Profile", "A service area set up correctly, the right categories, true hours, real photos of your crew, and posts through the busy weeks. This is what wins the map."),
    ("Service pages", "One page for each job you want more of, written for the person typing the search. This is what wins the listing under the map."),
    ("City pages", "One page for each town your trucks cover, so the homeowners twenty minutes away can find you too."),
    ("Listings that match", "One name, one address, and one phone number across the directories Google checks, including the home service ones."),
    ("Review generation", "A text that goes out after every job, sent while the tech is still on site, that names the work and keeps coming all year."),
    ("Your website", "Built for local search, with a call button up top, your license where it applies, and a structure that gets stronger every year."),
  ],

  "fit_h2": "Which plumbing companies this is for",
  "fit_yes": [
    "A shop with trucks on the road and a defined area you serve",
    "One truck or a small fleet, with room for more work",
    "Someone answers the phone when it rings, day or night",
    "You can give it three to six months before you judge it",
  ],
  "fit_no": [
    "You are booked solid and cannot take more calls",
    "You want the phone ringing this week. That is an ads job",
    "You want to rank in towns your trucks will not drive to",
    "You want blog posts by the dozen instead of booked jobs",
  ],

  "faq": [
    ("We work out of our trucks with no storefront. Can we still show on the map?", "Yes. Google calls that a service area business. The profile is set up around where you work, your home address stays hidden, and you rank around the area you serve."),
    ("How long until the phone rings more?", "Usually three to six months to start seeing big results. Fixing the profile and listings moves the map first. Service pages and reviews take longer and keep building."),
    ("Should we stop paying for ads?", "Keep them running while this builds, if they pay for themselves. Ads stop the day the budget does. Once the map and your pages are bringing calls, you can decide how much ad spend you still need, and we show you the numbers to decide with."),
    ("We only want the bigger jobs. Can you do that?", "Yes, within reason. The categories and pages decide which searches you win, so we build more around water heaters, sewer lines, and repipes if that is the work you want. You will still get some drain calls, and they turn into the big jobs later."),
    ("Can we compete with the big franchise brands?", "On the map, yes. A franchise location is one profile like yours, and Google ranks the closest, best reviewed, best described plumber. You win your own towns and the specialty searches the franchises do not bother with."),
    ("Do we need a profile for every town we cover?", "No. One profile for each real, staffed location. The other towns are covered by your service area and a page for each one. A fake address for a second profile is the quickest way to lose the first one."),
    ("Do you write about plumbing on our site?", "We write the service pages and city pages. Anything technical goes past you before it publishes, and we make no promises about prices or arrival times you have not set."),
    ("What does it cost?", "Campaigns start at $1,500 a month, flat, with no setup fee. Month to month."),
  ],

  "cta_h": "Be the plumber they call first.",
  "cta_p": "Start with a free audit of your profile, your reviews, and the three plumbers ranking above you.",
}

PAGES = [ACCOUNTANTS, DENTISTS, PLUMBERS]
