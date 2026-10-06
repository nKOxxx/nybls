"""Round 6 stratum S sampler. Deterministic given YouTube's search ranking at run time.

For each registered genre query: yt-dlp ytsearch15, in returned order; keep the first two
results passing every filter in PROTOCOL.md. Writes candidates.jsonl (every result seen,
with pass/fail and the first failing filter) and SELECTED.md. Fallback query runs only if
the primary yields fewer than two survivors. No human choice anywhere.

Usage: python3 sample_videos.py            (run from bench/round6)
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
STORE = os.path.expanduser("~/.nybls/store")
GENRES = [
 (1, "whiteboard math", "linear algebra lecture whiteboard", "calculus lecture blackboard"),
 (2, "news bulletin", "evening news bulletin full", "news hour full episode"),
 (3, "French talk", "conférence TEDx français", "cours magistral français"),
 (4, "Arabic talk", "محاضرة كاملة", "تيدكس بالعربي"),
 (5, "sports highlights", "full match highlights", "extended highlights football"),
 (6, "handheld walking vlog", "walking tour vlog handheld", "city walk vlog talking"),
 (7, "dense slide keynote", "keynote slides conference talk", "conference talk slides full"),
 (8, "no-text daily vlog", "day in my life vlog", "weekly vlog"),
 (9, "guitar lesson", "guitar lesson tabs on screen", "how to play guitar lesson"),
 (10, "woodworking DIY", "woodworking project build", "diy build step by step"),
 (11, "science demonstration", "science experiment demonstration explained", "physics demo lecture"),
]
TITLE_BLOCK = re.compile(r"compilation|best of|#shorts|top 10|reaction", re.I)
MIN_S, MAX_S, MIN_H, N_PER = 300, 3600, 480, 2

def earlier_round_ids():
    ids = set(os.listdir(STORE)) if os.path.isdir(STORE) else set()
    bench = os.path.dirname(HERE)
    for root, _, files in os.walk(bench):
        if "round6" in root: continue
        for f in files:
            if f.endswith((".md", ".json", ".txt", ".py")):
                try: ids |= set(re.findall(r"\b[A-Za-z0-9_-]{11}\b", open(os.path.join(root, f), errors="ignore").read()))
                except OSError: pass
    return ids

def search(query):
    cmd = ["yt-dlp", "--skip-download", "--ignore-errors", "--no-warnings", f"ytsearch15:{query}", "--print",
           "%(id)s\t%(duration)s\t%(height)s\t%(language)s\t%(is_live)s\t%(live_status)s\t%(subtitles)j\t%(automatic_captions)j\t%(title)s"]
    out = subprocess.run(cmd, capture_output=True, text=True, timeout=900).stdout
    rows = []
    for ln in out.splitlines():
        p = ln.split("\t")
        if len(p) < 9: continue
        def jd(x):
            try: return json.loads(x) if x and x != "NA" else {}
            except json.JSONDecodeError: return {}
        subs = jd(p[6]); auto = jd(p[7])
        rows.append({"id": p[0], "duration": float(p[1]) if p[1] not in ("NA", "") else None,
                     "height": int(p[2]) if p[2] not in ("NA", "") else None, "language": p[3],
                     "live": p[4] == "True" or p[5] in ("is_live", "is_upcoming"),
                     "caption_langs": sorted(set(subs) | set(auto)), "title": p[8]})
    return rows

def failing_filter(r, used):
    if r["id"] in used: return "already in store or earlier round"
    if r["duration"] is None or not (MIN_S <= r["duration"] <= MAX_S): return f"duration {r['duration']}"
    if r["height"] is None or r["height"] < MIN_H: return f"height {r['height']}"
    if r["live"]: return "live"
    lang = (r["language"] or "").split("-")[0].lower()
    if not any(c.split("-")[0].lower() == lang for c in r["caption_langs"]) or not lang or lang == "na":
        return f"no caption track in own language ({r['language']}; have {r['caption_langs'][:5]})"
    if TITLE_BLOCK.search(r["title"]): return "title blocklist"
    return None

def main():
    used = earlier_round_ids()
    selected, cand = [], open(os.path.join(HERE, "candidates.jsonl"), "w")
    for num, genre, q, fb in GENRES:
        picked = []
        for which, query in (("primary", q), ("fallback", fb)):
            if len(picked) >= N_PER: break
            for rank, r in enumerate(search(query), 1):
                why = failing_filter(r, used) if len(picked) < N_PER else "quota filled"
                r.update(genre=num, query=query, which=which, rank=rank, fail=why)
                cand.write(json.dumps(r, ensure_ascii=False) + "\n")
                if why is None:
                    picked.append(r); used.add(r["id"])
        selected.extend(picked)
        print(num, genre, [p["id"] for p in picked], file=sys.stderr)
    cand.close()
    with open(os.path.join(HERE, "SELECTED.md"), "w") as f:
        f.write("# Stratum S selection, by the registered rule (sample_videos.py), run " + subprocess.run(["date", "-u", "+%FT%TZ"], capture_output=True, text=True).stdout.strip() + "\n\n")
        f.write("| genre | query | rank | id | duration (s) | height | lang | title |\n|---|---|---|---|---|---|---|---|\n")
        for r in selected:
            f.write(f"| {r['genre']} | {r['which']} | {r['rank']} | {r['id']} | {int(r['duration'])} | {r['height']} | {r['language']} | {r['title'][:70].replace('|', '/')} |\n")
        f.write(f"\n{len(selected)} videos. Every result seen and every exclusion reason is in candidates.jsonl. Replacements after probe failures are appended below.\n")

if __name__ == "__main__":
    main()
