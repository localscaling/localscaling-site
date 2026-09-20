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

PAGES = [ACCOUNTANTS, DENTISTS]
