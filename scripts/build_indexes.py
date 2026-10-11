#!/usr/bin/env python3
"""
Build the machine-readable surfaces of brianmadden-ai from the files themselves.

MAINTAINER.md rule 8 ("machine indexes stay honest") says these must be
regenerated when content changes. This is the script that does it, so no
count, word total or date in the repo depends on someone remembering it:

  1. _index.json      Full manifest: one entry per indexed file, with word
                      counts and updated dates computed from the file.
  2. Stat mentions    Every hand-written sentence that quotes a repo-size
                      number (README "What's inside", the llms.txt header and
                      bullets, the CLAUDE.md / AGENTS.md loading order and repo
                      tree). They're listed in STAT_MENTIONS below; add a line
                      there when a new one turns up.
  3. llms-full.txt    The core canon (CLAUDE.md, me/*, active frameworks)
                      concatenated in loading order, for AIs without MCP.

  2b. _relationships.json  Frameworks <-> posts <-> talks, from each file's
                      related_frameworks / related_posts frontmatter.

  2c. Dates           Body "Last updated" lines in developing/published thinking, and
                      the "(updated YYYY-MM-DD)" tag on llms.txt bullets, follow each
                      file's frontmatter (`last_reviewed`, else `updated`).

It also *checks* (never edits) things that need a human: _content-index.json
(curated feed) coverage, and "Last updated" lines that disagree with
a file's own `updated` frontmatter.

Usage:
  python3 scripts/build_indexes.py            # show what would change
  python3 scripts/build_indexes.py --write    # apply it
  python3 scripts/build_indexes.py --check    # exit 1 if anything is stale (CI)

Never touches ingest/ (tier 1). Date fields (`generated`, llms.txt "updated")
only move when something else changed, so --check is stable day to day.
Requires PyYAML (requirements.txt).
"""

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
TODAY = datetime.date.today().isoformat()

CANON_DIRS = ["me", "frameworks", "posts", "talks", "podcast", "interviews", "pages"]
ROOT_DOCS = ["CLAUDE.md", "AGENTS.md", "README.md", "GOVERNANCE.md", "COLLECTIONS.md", "CHANGELOG.md", "llms.txt"]
# Deliberately outside the curated surfaces (see scripts/audit.py, same list).
UNINDEXED = {"podcast/bible.md", "me/style-guide.md", "pages/about.md", "pages/bio.md", "pages/books.md"}
# Order of root files in _index.json (matches the existing manifest).
ROOT_ORDER = ["AGENTS.md", "CLAUDE.md", "GOVERNANCE.md", "COLLECTIONS.md", "README.md", "CHANGELOG.md", "llms.txt"]
# Frontmatter keys copied into an index entry, in output order, after the core fields.
EXTRA_KEYS = ["date", "updated", "original_url", "substack_url", "publication", "description", "related_frameworks",
              "related_posts", "event", "location", "audience", "conference_theme", "other_speakers", "format",
              "show", "hosts", "recording", "slides", "status", "last_reviewed"]
FULL_ORDER = ["CLAUDE.md", "me/profile.md", "me/published-thinking.md", "me/developing-thinking.md", "me/voice.md"]


def read(rel):
    return (ROOT / rel).read_text()


def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return {}, text
    try:
        fm = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        fm = {}
    return (fm if isinstance(fm, dict) else {}), text[m.end():]


def norm(v):
    """YAML turns bare dates into date objects; the index stores ISO strings."""
    if isinstance(v, (datetime.date, datetime.datetime)):
        return v.isoformat()[:10]
    if isinstance(v, list):
        return [norm(x) for x in v]
    return v


def indexed_paths():
    paths = list(ROOT_DOCS)
    for d in CANON_DIRS:
        paths += [str(p.relative_to(ROOT)) for p in sorted((ROOT / d).rglob("*.md"))]
    paths = [p for p in paths if p not in UNINDEXED and (ROOT / p).exists()]
    root_rank = {p: i for i, p in enumerate(ROOT_ORDER)}
    root = sorted((p for p in paths if "/" not in p), key=lambda p: root_rank.get(p, 99))
    return root + sorted(p for p in paths if "/" in p)


def build_entry(rel, old):
    fm, body = split_frontmatter(read(rel))
    fm = {k: norm(v) for k, v in fm.items()}
    entry = {
        "path": rel,
        "title": fm.get("title") or old.get("title") or Path(rel).stem,
        "authority_level": fm.get("authority_level"),
        "file_type": fm.get("file_type"),
        "tags": fm.get("tags") or [],
        "word_count": len(body.split()),
        "staleness_threshold": fm.get("staleness_threshold"),
    }
    for k in EXTRA_KEYS:
        if k in fm and not (k == "status" and fm[k] != "archived"):
            entry[k] = fm[k]
    if "original_url" not in entry and fm.get("url"):  # newer posts use `url:`
        entry["original_url"] = fm["url"]
    return entry


def compute_stats(entries):
    def n(pattern, exclude=("index.md",)):
        return len([p for p in (ROOT / pattern[0]).glob(pattern[1]) if p.name not in exclude])

    fw = [e for e in entries if e["path"].startswith("frameworks/")]
    archived = len([e for e in fw if e.get("status") == "archived"])
    citrix = n(("posts/citrix-blog", "*.md"))
    articles = n(("posts/linkedin/articles", "*.md"))
    feed_posts = sum(read(str(p.relative_to(ROOT))).count("linkedin.com/feed/update")
                     for p in (ROOT / "posts/linkedin/posts").glob("*.md"))
    words = sum(e["word_count"] for e in entries)
    pt = next(e["word_count"] for e in entries if e["path"] == "me/published-thinking.md")
    return {
        "files": len(entries),
        "words": words,
        "words_k": round(words / 1000),
        "frameworks_active": len(fw) - archived,
        "frameworks_archived": archived,
        "citrix_posts": citrix,
        "linkedin_articles": articles,
        "linkedin_feed_posts": feed_posts,
        "posts_total": citrix + articles,
        "talks": n(("talks", "*.md")),
        "podcast_episodes": n(("podcast", "ep*.md")),
        "published_thinking_words_k": round(pt / 1000),
    }


# (file, regex with ONE group around the value to rewrite, stat key). To track a
# new hand-written number, add a line. A pattern that stops matching is reported.
STAT_MENTIONS = [
    ("llms.txt", r"\((\d+) files,", "files"),
    ("llms.txt", r"~(\d+)k words", "words_k"),
    ("llms.txt", r"(\d+) frameworks, \d+ posts", "frameworks_active"),
    ("llms.txt", r"frameworks, (\d+) posts", "posts_total"),
    ("llms.txt", r"posts, (\d+) talks", "talks"),
    ("llms.txt", r"Index of (\d+) Citrix blog posts", "citrix_posts"),
    ("llms.txt", r"Index of (\d+) LinkedIn articles", "linkedin_articles"),
    ("llms.txt", r"(\d+) speech and podcast-appearance transcripts", "talks"),
    ("llms.txt", r"Full text of all (\d+) Citrix blog posts", "citrix_posts"),
    ("llms.txt", r"Full text of (\d+) LinkedIn long-form articles", "linkedin_articles"),
    ("README.md", r"(\d+) published \[Citrix blog posts\]", "citrix_posts"),
    ("README.md", r"\), (\d+) LinkedIn articles", "linkedin_articles"),
    ("README.md", r"LinkedIn articles and (\d+) short", "linkedin_feed_posts"),
    ("README.md", r"(\d+) speech and podcast-appearance transcripts", "talks"),
    ("README.md", r"the (\d+)-episode Citrix AI Hotsheet", "podcast_episodes"),
    ("README.md", r"(\d+) standalone frameworks", "frameworks_active"),
    ("README.md", r"A (\d+),000-word synthesis", "published_thinking_words_k"),
    ("CLAUDE.md", r"\((\d+) Citrix blog posts", "citrix_posts"),
    ("CLAUDE.md", r"\+ (\d+) LinkedIn articles", "linkedin_articles"),
    ("CLAUDE.md", r"Brian's (\d+) active frameworks", "frameworks_active"),
    ("CLAUDE.md", r"Standalone framework explainers \((\d+) active", "frameworks_active"),
    ("CLAUDE.md", r"\d+ active, (\d+) archived\)", "frameworks_archived"),
    ("CLAUDE.md", r"# Citrix blog posts \((\d+) posts", "citrix_posts"),
    ("AGENTS.md", r"\((\d+) Citrix blog posts", "citrix_posts"),
    ("AGENTS.md", r"\+ (\d+) LinkedIn articles", "linkedin_articles"),
    ("AGENTS.md", r"Brian's (\d+) active frameworks", "frameworks_active"),
    ("AGENTS.md", r"Standalone framework explainers \((\d+) active", "frameworks_active"),
    ("AGENTS.md", r"\d+ active, (\d+) archived\)", "frameworks_archived"),
    ("AGENTS.md", r"# Citrix blog posts \((\d+) posts", "citrix_posts"),
    ("posts/citrix-blog/index.md", r"Full text of my (\d+) Citrix blog posts", "citrix_posts"),
]
# "Last updated" lines in the body of a file, kept equal to that file's own freshness date.
# Freshness = `last_reviewed` (Brian looked at it) else `updated`. Pipeline-flagged
# scratchpad items bump `updated` but are not Brian's thinking yet, so for
# developing-thinking the human date wins.
DATE_MENTIONS = [
    ("me/developing-thinking.md", r"\*\*Last updated:\*\* ([A-Z][a-z]+ \d+, \d{4})"),
    ("me/developing-thinking.md", r"\*Last updated: ([A-Z][a-z]+ \d+, \d{4})\.\*"),
    ("me/published-thinking.md", r"\*\*Last updated:\*\* ([A-Z][a-z]+ \d+, \d{4})"),
]
UPDATED_MENTION = ("llms.txt", r"updated (\d{4}-\d{2}-\d{2})\)")


def apply_mentions(texts, stats, problems):
    """texts: {file: text}. Returns {file: new_text} for files that changed."""
    out = {}
    for file, pattern, key in STAT_MENTIONS:
        text = out.get(file, texts.get(file))
        if text is None:
            continue
        m = re.search(pattern, text)
        if not m:
            problems.append(f"{file}: pattern for '{key}' no longer matches ({pattern}); update STAT_MENTIONS")
            continue
        if m.group(1) != str(stats[key]):
            text = text[:m.start(1)] + str(stats[key]) + text[m.end(1):]
        out[file] = text
    return {f: t for f, t in out.items() if t != texts[f]}


CORE = ["me/developing-thinking.md", "me/career.md", "me/profile.md", "me/published-thinking.md", "me/voice.md"]


def build_relationships(entries):
    """Frameworks <-> posts <-> talks, derived from each file's own frontmatter."""
    by = {e["path"]: e for e in entries}
    stem = lambda p: Path(p).stem
    posts = [e for e in entries if e["path"].startswith("posts/") and not e["path"].endswith("index.md")]
    talks = [e for e in entries if e["path"].startswith("talks/") and not e["path"].endswith("index.md")]
    fws = [e for e in entries if e["path"].startswith("frameworks/")]
    rel = {"frameworks": {}, "posts": {}, "talks": {}, "core": {}}
    for e in fws:
        s = stem(e["path"])
        rel["frameworks"][s] = {
            "path": e["path"], "title": e["title"], "original_url": e.get("original_url", ""),
            "referenced_in_posts": e.get("related_posts", []),
            "related_frameworks": e.get("related_frameworks", []),
            "referenced_by_posts": [stem(p["path"]) for p in posts if s in p.get("related_frameworks", [])],
            "referenced_by_talks": [stem(t["path"]) for t in talks if s in t.get("related_frameworks", [])],
        }
    for e in posts:
        rel["posts"][stem(e["path"])] = {
            "path": e["path"], "title": e["title"],
            "implements_frameworks": e.get("related_frameworks", []), "original_url": e.get("original_url", "")}
    for e in talks:
        d = {"path": e["path"], "title": e["title"], "event": e.get("event", ""), "location": e.get("location", ""),
             "date": e.get("date", "")}
        if e.get("recording"):
            d["recording"] = e["recording"]
        d["implements_frameworks"] = e.get("related_frameworks", [])
        rel["talks"][stem(e["path"])] = d
    for p in CORE:
        e = by[p]
        rel["core"][p] = {"title": e["title"], "authority_level": e["authority_level"],
                          "related_frameworks": e.get("related_frameworks", [])}
    return rel


def freshness(entry):
    return entry.get("last_reviewed") or entry.get("updated")


def pretty(iso):
    d = datetime.date.fromisoformat(iso)
    return f"{d.strftime('%B')} {d.day}, {d.year}"


def apply_dates(texts, entries, edited, problems):
    """Body 'Last updated' lines and the '(updated YYYY-MM-DD)' tag on llms.txt bullets."""
    by = {e["path"]: e for e in entries}
    for file, pattern in DATE_MENTIONS:
        text = edited.get(file, texts[file])
        m = re.search(pattern, text)
        fresh = freshness(by[file])
        if not m:
            problems.append(f"{file}: date pattern no longer matches ({pattern})")
        elif fresh and m.group(1) != pretty(fresh):
            edited[file] = text[:m.start(1)] + pretty(fresh) + text[m.end(1):]
    text = edited.get("llms.txt", texts["llms.txt"])
    lines = text.split("\n")
    for i, line in enumerate(lines):
        m = re.match(r"- \[([^\]]+)\]\(https://github\.com/[^)]*/blob/main/[^)]+\)(: .*)$", line)
        if not m or m.group(1) not in by or not freshness(by[m.group(1)]):
            continue
        base = re.sub(r" \(updated \d{4}-\d{2}-\d{2}\)$", "", line)
        lines[i] = f"{base} (updated {freshness(by[m.group(1)])})"
    if "\n".join(lines) != text:
        edited["llms.txt"] = "\n".join(lines)


def build_full():
    parts = ["# brianmadden.ai: core canon in one file\n",
             "Generated by scripts/build_indexes.py. Do not edit; edit the source files. This is the core canon "
             "(CLAUDE.md, profile, published thinking, developing thinking, voice, then each active framework) in "
             "loading order, for AIs that can fetch one file but not run MCP. Posts, talks, podcast and interviews "
             "are not included: use llms.txt, _index.json or the MCP server for those.\n"]
    fws = []
    for p in sorted((ROOT / "frameworks").glob("*.md")):
        fm, _ = split_frontmatter(p.read_text())
        if fm.get("status") != "archived":
            fws.append(str(p.relative_to(ROOT)))
    for rel in FULL_ORDER + fws:
        parts.append(f"\n\n{'=' * 78}\nFILE: {rel}\n{'=' * 78}\n\n{read(rel).strip()}\n")
    return "".join(parts)


def checks(entries, advice):
    """Things only a human can fix: report, never edit, never fail --check."""
    content = json.loads(read("_content-index.json"))
    urls = {c["url"].rstrip("/") for c in content}
    for e in entries:  # match by URL: the feed uses the site's headline, which can differ from our title
        if e["path"].startswith("posts/citrix-blog/") and not e["path"].endswith("index.md") \
                and e.get("original_url", "").rstrip("/") not in urls:
            advice.append(f"_content-index.json has no entry for blog post '{e['title']}'")


def run(args):
    """One pass. Returns True if it wrote something (so --write can go again)."""
    old_index = json.loads(read("_index.json"))
    old_by_path = {e["path"]: e for e in old_index["files"]}
    entries = [build_entry(p, old_by_path.get(p, {})) for p in indexed_paths()]
    stats = compute_stats(entries)

    problems, advice, changes = [], [], []
    new_index = {**{k: v for k, v in old_index.items() if k != "files"},
                 "total_files": stats["files"], "total_words": stats["words"], "files": entries}
    index_changed = json.dumps({**new_index, "generated": ""}, sort_keys=True) != \
        json.dumps({**old_index, "generated": ""}, sort_keys=True)

    texts = {f: read(f) for f in {m[0] for m in STAT_MENTIONS} | {UPDATED_MENTION[0]}}
    edited = apply_mentions(texts, stats, problems)
    texts.update({f: read(f) for f, _ in DATE_MENTIONS if f not in texts})
    apply_dates(texts, entries, edited, problems)
    full = build_full()
    new_rel = build_relationships(entries)
    old_rel = json.loads(read("_relationships.json"))
    rel_changed = new_rel != old_rel
    full_changed = not (ROOT / "llms-full.txt").exists() or read("llms-full.txt") != full

    anything = index_changed or rel_changed or bool(edited) or full_changed
    if anything:  # dates move only when content moved
        new_index["generated"] = TODAY
        f, pat = UPDATED_MENTION
        t = edited.get(f, texts[f])
        m = re.search(pat, t)
        if m and m.group(1) != TODAY:
            edited[f] = t[:m.start(1)] + TODAY + t[m.end(1):]
        elif not m:
            problems.append(f"{f}: updated-date pattern no longer matches")
    checks(entries, advice)

    old_paths, new_paths = set(old_by_path), {e["path"] for e in entries}
    if index_changed:
        changed = [e["path"] for e in entries if old_by_path.get(e["path"]) != e]
        changes.append(f"_index.json: {len(changed)} entries changed, {len(new_paths - old_paths)} added, "
                       f"{len(old_paths - new_paths)} removed; totals {stats['files']} files / {stats['words']:,} words")
    for f in sorted(edited):
        changes.append(f"{f}: stat mentions updated")
    if rel_changed:
        d = {k: len(set(new_rel[k]) ^ set(old_rel.get(k, {}))) for k in new_rel}
        changes.append(f"_relationships.json: regenerated (added/removed keys per section: {d})")
    if full_changed:
        changes.append("llms-full.txt: regenerated")

    print("Stats:", ", ".join(f"{k}={v}" for k, v in stats.items()))
    for c in changes:
        print("  would change ->" if not args.write else "  changed ->", c)
    for p in problems:
        print("  BROKEN:", p)
    for a in advice:
        print("  advisory:", a)
    if not changes:
        print("Everything is up to date.")

    if args.write and anything:
        (ROOT / "_index.json").write_text(json.dumps(new_index, indent=2, ensure_ascii=False) + "\n")
        (ROOT / "_relationships.json").write_text(json.dumps(new_rel, indent=2, ensure_ascii=False) + "\n")
        for f, t in edited.items():
            (ROOT / f).write_text(t)
        (ROOT / "llms-full.txt").write_text(full)
    if args.check and (anything or problems):
        sys.exit(1)
    return args.write and anything


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--write", action="store_true", help="apply changes")
    ap.add_argument("--check", action="store_true", help="exit 1 if anything is stale")
    args = ap.parse_args()
    # Writing llms.txt / README changes their own word counts in _index.json, so repeat
    # until a pass changes nothing (always converges in 2 passes).
    for _ in range(5):
        if not run(args):
            break


if __name__ == "__main__":
    main()
