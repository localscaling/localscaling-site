"""Paid search landing pages. One dict per trade, rendered by ad_page() in
build_pages.py. These pages are noindex and stay out of the sitemap: they
exist for Google Ads traffic only, so the industry pages keep the organic job.

Each page puts the audit form on the first screen, has no menu, and matches
the ad group of the same trade in ads/google/google-seo-01. Keep the copy in
step with that campaign's ads: same offer, same price line, same 24 hours.
"""

PAGES = [
    {
        "slug": "hvac-seo-audit",
        "industry": "HVAC",
        "plural": "HVAC companies",
        "eyebrow": "Free SEO audit for HVAC companies",
        "h1": "Local SEO for HVAC companies",
        "lede": "When the heat or the air goes out, homeowners search on a phone and call a company from the map. We get yours onto Google Maps and into the results under it, in the towns you already serve.",
        "search": "ac repair Phoenix",
    },
    {
        "slug": "plumber-seo-audit",
        "industry": "Plumbing",
        "plural": "plumbers",
        "eyebrow": "Free SEO audit for plumbers",
        "h1": "Local SEO for plumbing companies",
        "lede": "A burst pipe gets one search and one call, usually to a plumber on the map. We get your company onto Google Maps and into the results under it, in the towns you already serve.",
        "search": "emergency plumber Dallas",
    },
    {
        "slug": "roofer-seo-audit",
        "industry": "Roofing",
        "plural": "roofers",
        "eyebrow": "Free SEO audit for roofers",
        "h1": "Local SEO for roofing companies",
        "lede": "After a storm, homeowners look up roofers on Google and call the ones on the map first. We get your company onto Google Maps and into the results under it, in the areas you already cover.",
        "search": "roof repair Tampa",
    },
    {
        "slug": "electrician-seo-audit",
        "industry": "Electrical",
        "plural": "electricians",
        "eyebrow": "Free SEO audit for electricians",
        "h1": "Local SEO for electricians",
        "lede": "When the power goes out or a panel needs work, people search for an electrician and call one from the map. We get your company onto Google Maps and into the results under it, in the towns you already serve.",
        "search": "panel upgrade Austin",
    },
    {
        "slug": "moving-company-seo-audit",
        "industry": "Moving",
        "plural": "moving companies",
        "eyebrow": "Free SEO audit for moving companies",
        "h1": "Local SEO for moving companies",
        "lede": "People planning a move compare the movers on the map and the first few results before they ask for quotes. We get your company into both, in the cities you already serve.",
        "search": "local movers Denver",
    },
    {
        "slug": "contractor-seo-audit",
        "industry": "Contractor",
        "plural": "contractors",
        "eyebrow": "Free SEO audit for contractors",
        "h1": "Local SEO for contractors",
        "lede": "Homeowners planning a project compare contractors on the map and read the sites under it before they call anyone. We get your company into both, across your service area.",
        "search": "kitchen remodel Charlotte",
    },
]

# Form versions. Each trade gets one page per version: version "a" lives at the
# trade slug, "b" at the slug plus "-b". Split clicks between them with a Google
# Ads experiment and keep the version with the lower cost per qualified lead.
# Phone is optional on both. Google Business Profile link and target search
# moved to the thank-you page.
FORM_VARIANTS = {
    "a": {"suffix": "", "count_word": "Five", "fields": ["name", "email", "business", "website", "city"]},
    "b": {"suffix": "-b", "count_word": "Three", "fields": ["email", "website", "city"]},
}
