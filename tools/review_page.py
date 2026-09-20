"""The anti-AI-writing review, as a script. Run it on every page before it is
called done. Exit 1 on any finding.

    python3 tools/review_page.py local-seo-houston.html [more.html ...]

Checks, drawn from Wikipedia's Signs of AI writing and this site's own rules:
  dashes        em or en dashes, curly quotes, curly apostrophes
  vocab         the AI vocabulary list (delve, crucial, seamless, and so on)
  parallel      "not just X but Y", "not only", "X, not Y" contrast sentences
  participle    sentences that end in a tacked-on -ing analysis
  titlecase     headings in Title Case
  banned        results guarantee, fixed prices, 90 day promises, client names
  facts         numbers that look like invented stats
It also runs the hub knowledge lint when it can find it."""
import re, sys, os, html, subprocess

SITE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HUB_LINT = os.path.join(os.path.dirname(SITE), "ops", "knowledge_lint.py")

VOCAB = r"\b(additionally|align(s|ed)? with|boasts?|bolster\w*|crucial|delve\w*|emphasi[sz]\w*|enduring|enhanc\w*|foster\w*|garner\w*|highlight\w*|interplay|intricate|intricacies|landscape|meticulous\w*|pivotal|robust|showcas\w*|tapestry|testament|underscor\w*|valuable|vibrant|seamless\w*|elevat\w*|unlock\w*|leverag\w*|streamlin\w*|comprehensive|dominat\w*|empower\w*|navigat\w*|journey|game.?changer|cutting.edge|state.of.the.art|world.class|top.notch|best.in.class|holistic|synerg\w*|stands? as|serves? as|refers to|commitment to|in the heart of|nestled|renowned|rich (history|heritage)|diverse array|it'?s important to note|worth noting|in conclusion|in summary|in today'?s|ever.evolving|digital presence|online presence|thrive|elevate)\b"
PARALLEL = r"\b(not just|not only|not merely|isn'?t just|aren'?t just|no .{1,25}, no .{1,25}, just)\b"
CONTRAST = r"[^.!?]*\b(, not [a-z]|not to ours|not ours\b)[^.!?]*[.!?]"
PARTICIPLE = r",\s+(ensuring|reflecting|highlighting|showcasing|underscoring|emphasizing|signaling|fostering|contributing to|cementing|solidifying)\b"
BANNED = r"\b(guarantee\w*|90 days|ninety days|money.back|no.risk)\b"
PRICE = r"(?<!starting at )(?<!start at )(?<!starts at )\$[0-9,]+(/mo| a month| per month)"

def text_of(path):
    s = open(path).read()
    s = re.sub(r"<script.*?</script>|<style.*?</style>|<svg.*?</svg>", "", s, flags=re.S)
    heads = [html.unescape(re.sub(r"<[^>]+>", "", h)).strip() for h in re.findall(r"<h[1-3][^>]*>(.*?)</h[1-3]>", s, flags=re.S)]
    t = html.unescape(re.sub(r"<[^>]+>", " ", s))
    return re.sub(r"\s+", " ", t), heads, s

def snippet(t, m, w=55):
    return "..." + t[max(0, m.start()-w):min(len(t), m.end()+w)].strip() + "..."

def review(path):
    findings = []
    t, heads, raw = text_of(path)
    for m in re.finditer(r"[—–“”‘’]", raw):
        findings.append(("dashes", snippet(raw, m, 30)))
    for m in re.finditer(VOCAB, t, flags=re.I):
        findings.append(("vocab", snippet(t, m)))
    for m in re.finditer(PARALLEL, t, flags=re.I):
        findings.append(("parallel", snippet(t, m)))
    for m in re.finditer(CONTRAST, t):
        findings.append(("contrast", m.group(0).strip()[:160]))
    for m in re.finditer(PARTICIPLE, t, flags=re.I):
        findings.append(("participle", snippet(t, m)))
    for h in heads:
        words = [w for w in h.split() if len(w) > 3 and w.isalpha()]
        caps = [w for w in words if w[0].isupper()]
        proper = {"Google Business Profile", "Google Maps"}
        if h in proper: continue
        if len(words) >= 3 and len(caps) >= len(words) - 1 and h != h.upper() and "SEO" not in h:
            findings.append(("titlecase", h))
    body = re.sub(r"<title>.*?</title>|<meta[^>]*>|<select.*?</select>", "", raw, flags=re.S)
    bt = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"<script.*?</script>|<style.*?</style>|<svg.*?</svg>", "", body, flags=re.S))))
    for m in re.finditer(BANNED, bt, flags=re.I):
        findings.append(("banned", snippet(bt, m)))
    for m in re.finditer(PRICE, bt, flags=re.I):
        findings.append(("price", "a fixed price without 'starting at': " + snippet(bt, m, 30)))
    for m in re.finditer(r"\b\d{2,3}%|\b\d[\d,]*\+ (clients|firms|businesses|reviews|calls|leads)\b|\b(over|more than) \d[\d,]* (clients|firms|businesses|reviews|calls|leads)\b", bt, flags=re.I):
        findings.append(("facts", snippet(bt, m)))
    return findings

def main(paths):
    bad = 0
    for p in paths:
        full = p if os.path.isabs(p) else os.path.join(SITE, p)
        f = review(full)
        print(f"== {p}: {'PASS' if not f else str(len(f)) + ' finding(s)'}")
        for kind, s in f:
            print(f"   [{kind}] {s}")
        bad += len(f)
        if os.path.exists(HUB_LINT):
            r = subprocess.run([sys.executable, HUB_LINT, "--file", full], capture_output=True, text=True)
            last = (r.stdout.strip().splitlines() or [""])[-1]
            print(f"   [hub lint] {last}")
            if r.returncode != 0:
                bad += 1
        else:
            print("   [hub lint] not found, skipped")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__); sys.exit(2)
    main(sys.argv[1:])
