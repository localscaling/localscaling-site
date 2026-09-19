"""Industry page content. The pack card, the year timeline, and the intent
table are illustrations, not data. Keep them that way.

Industry page content. One dict per industry, rendered by industry_page()
in build_pages.py. To add an industry: copy ACCOUNTANTS, change every value,
append it to PAGES, run the build. Keep every claim qualitative. No stats,
no client names, no results. Timing is three to six months."""

ACCOUNTANTS = {
  "slug": "local-seo-for-accountants",
  "title": "Local SEO for Tax Accountants and CPAs | LocalScaling",
  "meta": "Local SEO for tax accountants, CPAs, and bookkeeping firms. We get your practice into the Google map pack in the neighborhoods you serve, ahead of tax season. Starting at $1,500/mo.",
  "crumb": "Tax accountants and CPAs",
  "eyebrow": "Local SEO for accountants",
  "h1": "Local SEO for tax accountants and CPAs",
  "lede": "Most people pick an accountant the way they pick a plumber. They search, they look at the map, they call one of the first three. We get your practice into those three spots in the neighborhoods you serve.",
  "short": "accountants",
  "industry_value": "Accounting or finance",

  "pack_search": "CPA near me",
  "pack_rows": [("Your firm", "Certified public accountant · 0.4 mi"), ("Another firm", "Accountant · 1.1 mi"), ("Another firm", "Tax preparation service · 2.3 mi")],
  "pack_note": "Three spots. Most people never scroll past them.",

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
    ("We build a page for each service", "You probably do tax preparation, bookkeeping, payroll, business returns, and IRS representation. Each one gets its own page, written for the person searching for it. A single services page ranks for none of them."),
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
    ("Google Business Profile", "The right primary category, services listed the way people search for them, and posts through tax season."),
    ("Service pages", "One page for each service you want more of, written for the person typing the search."),
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

PAGES = [ACCOUNTANTS]
