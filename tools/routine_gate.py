"""Decides whether the page routine should run today and which pages are next.

    python3 tools/routine_gate.py          prints GO or WAIT and the next city and industry
    python3 tools/routine_gate.py --done city "Houston" local-seo-houston
                                           records a finished page and moves the queue

The queue and the ledger live in tools/page-queue.json. The routine is
scheduled daily and this gate enforces the cadence, so the interval is exact
and does not drift at month ends."""
import json, sys, datetime, os

HERE = os.path.dirname(os.path.abspath(__file__))
Q = os.path.join(HERE, "page-queue.json")
q = json.load(open(Q))
today = datetime.date.today()

if len(sys.argv) >= 5 and sys.argv[1] == "--done":
    kind, name, slug = sys.argv[2], sys.argv[3], sys.argv[4]
    key = "cities" if kind == "city" else "industries"
    if name in q[key]:
        q[key].remove(name)
    q["done"].append({"type": kind, "name": name, "slug": slug, "date": today.isoformat()})
    q["last_run"] = today.isoformat()
    json.dump(q, open(Q, "w"), indent=2)
    print(f"recorded {kind}: {name} at /{slug}")
    sys.exit(0)

if q["last_run"]:
    last = datetime.date.fromisoformat(q["last_run"])
    gap = (today - last).days
    if gap < q["cadence_days"]:
        print(f"WAIT {q['cadence_days'] - gap} more day(s). Last run {q['last_run']}.")
        sys.exit(0)
if not q["cities"] or not q["industries"]:
    print("WAIT queue empty. Add cities or industries to tools/page-queue.json.")
    sys.exit(0)
print("GO")
print(f"city: {q['cities'][0]}")
print(f"industry: {q['industries'][0]}")
print(f"publish: {q['publish']}")
