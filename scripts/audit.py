#!/usr/bin/env python3
"""
Monthly system audit for brianmadden-ai (deterministic half).

Ported from the old private brain's `system-audit` skill and rewritten for
this repo's tiers. Plain code, no model calls: structural integrity, index
drift, tier-1 quarantine, staleness, bloat, pipeline health, hygiene. The
judgment half (best-practices scan, rules drift, red-team) lives in
.claude/skills/system-audit/SKILL.md and reads this script's report.

Writes outputs/audits/YYYY-MM-DD-audit.md and a sibling .json of metrics so
the next run can show trends. Never modifies anything outside outputs/audits/.

  python3 scripts/audit.py              # write the report
  python3 scripts/audit.py --dry-run    # print to stdout, write nothing

Exit code is always 0 unless the script itself breaks: findings are the
output, not a failure. (check_doc_accuracy.py is the CI gate.)
"""

import argparse
import datetime as dt
import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT_DIR = ROOT / "outputs" / "audits"

CANON_DIRS = ["me", "frameworks", "posts", "talks", "podcast", "interviews", "pages"]
ROOT_DOCS = ["CLAUDE.md", "AGENTS.md", "README.md", "GOVERNANCE.md", "COLLECTIONS.md", "llms.txt"]
# Deliberately outside the curated surfaces (declared in the file's own header).
INTENTIONALLY_UNINDEXED = {"podcast/bible.md"}
MACHINE_INDEXES = ["_index.json", "_relationships.json", "_content-index.json", "llms.txt", "COLLECTIONS.md"]
REQUIRED_FM = ["title", "date", "status"]
BLOAT_LINES = 500
STALE_DAYS = 90
SECRET_PATTERNS = [
    (r"sk-ant-[A-Za-z0-9_-]{20,}", "Anthropic key"),
    (r"sk-[A-Za-z0-9]{32,}", "OpenAI-style key"),
    (r"AKIA[0-9A-Z]{16}", "AWS access key id"),
    (r"ghp_[A-Za-z0-9]{36}", "GitHub token"),
    (r"xox[baprs]-[A-Za-z0-9-]{10,}", "Slack token"),
]

critical, warnings, suggestions = [], [], []
metrics = {}


def git(*args):
    r = subprocess.run(["git", *args], cwd=ROOT, capture_output=True, text=True)
    return r.stdout.strip()


def canon_files():
    out = []
    for d in CANON_DIRS:
        out += sorted((ROOT / d).rglob("*.md"))
    return out + [ROOT / f for f in ROOT_DOCS if (ROOT / f).exists()]


def frontmatter(path):
    text = path.read_text(errors="replace")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        k, sep, v = line.partition(":")
        if sep and not line.startswith((" ", "\t")):
            fm[k.strip()] = v.strip().strip('"')
    return fm


def rel(p):
    return str(p.relative_to(ROOT))


def check_links(files):
    """Relative markdown links in canon must resolve."""
    link = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
    broken, inbound = [], {rel(f): 0 for f in files}
    for f in files:
        for target in link.findall(f.read_text(errors="replace")):
            if re.match(r"^(https?:|mailto:|#|/)", target) or target in ("url", "path"):
                continue
            t = (f.parent / target.split("#")[0]).resolve()
            if not t.exists():
                broken.append(f"{rel(f)} -> {target}")
            elif t.is_file() and str(t.relative_to(ROOT)) in inbound:
                inbound[str(t.relative_to(ROOT))] += 1
    metrics["broken_links"] = len(broken)
    for b in broken[:25]:
        critical.append(f"Broken link: {b}")
    if len(broken) > 25:
        critical.append(f"...and {len(broken) - 25} more broken links")
    return inbound


def check_frontmatter(files):
    missing = []
    for f in files:
        if f.name == "index.md" or f.parent == ROOT or f.parts[-2] in ("me", "pages") or f.name == "bible.md":
            continue
        fm = frontmatter(f)
        if fm is None:
            missing.append(f"{rel(f)}: no frontmatter")
            continue
        gone = [k for k in REQUIRED_FM if k not in fm and not (k == "title" and "event" in fm)]
        if gone:
            missing.append(f"{rel(f)}: missing {', '.join(gone)}")
    metrics["frontmatter_problems"] = len(missing)
    for m in missing[:20]:
        warnings.append(f"Frontmatter: {m}")
    if len(missing) > 20:
        warnings.append(f"...and {len(missing) - 20} more frontmatter problems")


def check_index_drift(files):
    """Files on disk vs _index.json, both directions."""
    idx = json.loads((ROOT / "_index.json").read_text())
    indexed = {e["path"] for e in idx["files"]}
    on_disk = {rel(f) for f in files}
    unindexed = sorted(p for p in on_disk - indexed if not p.endswith("index.md") and p not in INTENTIONALLY_UNINDEXED)
    ghosts = sorted(p for p in indexed - on_disk if not (ROOT / p).exists())
    metrics["indexed_files"] = len(indexed)
    metrics["unindexed_files"] = len(unindexed)
    for p in unindexed[:15]:
        warnings.append(f"On disk but missing from _index.json: {p}")
    for p in ghosts[:15]:
        critical.append(f"_index.json lists a file that doesn't exist: {p}")
    if unindexed or ghosts:
        suggestions.append("Index drift found: regenerate the machine indexes (MAINTAINER rule 8).")


def check_quarantine():
    """Tier 1 (ingest/) must never leak into any machine index or loading surface."""
    leaks = []
    for name in MACHINE_INDEXES:
        p = ROOT / name
        if p.exists() and re.search(r"(?<![\w-])ingest/", p.read_text(errors="replace")):
            leaks.append(name)
    metrics["quarantine_leaks"] = len(leaks)
    for name in leaks:
        critical.append(f"Tier-1 quarantine: '{name}' references ingest/ (must be excluded, MAINTAINER rule 8)")


def check_staleness():
    now = dt.datetime.now(dt.timezone.utc)
    stale = []
    for f in canon_files():
        if f.name == "voice.md":
            continue
        fm = frontmatter(f) or {}
        if fm.get("staleness_threshold", "") == "stable" or fm.get("status") == "archived":
            continue
        ts = git("log", "-1", "--format=%ct", "--", rel(f))
        if not ts:
            continue
        age = (now - dt.datetime.fromtimestamp(int(ts), dt.timezone.utc)).days
        if age >= STALE_DAYS and f.parts[-2] in ("me", "frameworks"):
            stale.append((age, rel(f)))
    stale.sort(reverse=True)
    metrics["stale_me_frameworks_files"] = len(stale)
    for age, p in stale[:10]:
        warnings.append(f"Not touched in {age} days (me/ or frameworks/, not marked stable): {p}")
    dt_path = ROOT / "me" / "developing-thinking.md"
    ts = git("log", "-1", "--format=%ct", "--", "me/developing-thinking.md")
    if ts:
        age = (now - dt.datetime.fromtimestamp(int(ts), dt.timezone.utc)).days
        metrics["developing_thinking_age_days"] = age
        if age > 21:
            warnings.append(f"me/developing-thinking.md last changed {age} days ago (CLAUDE.md flags >a few weeks)")


def check_bloat(files):
    big = []
    for f in files:
        n = sum(1 for _ in f.open(errors="replace"))
        if n > BLOAT_LINES and "posts" not in f.parts and "talks" not in f.parts:
            big.append((n, rel(f)))
    big.sort(reverse=True)
    metrics["files_over_500_lines"] = len(big)
    for n, p in big[:8]:
        suggestions.append(f"{p} is {n} lines: still manageable, or split?")


def check_orphans(inbound):
    orphans = [p for p, n in inbound.items()
               if n == 0 and not p.endswith(("index.md", "CLAUDE.md", "AGENTS.md", "README.md"))
               and p.split("/")[0] == "frameworks"]
    cols = (ROOT / "COLLECTIONS.md").read_text(errors="replace")
    orphans = [p for p in orphans if Path(p).name not in cols
               and (frontmatter(ROOT / p) or {}).get("status") != "archived"]
    metrics["orphans"] = len(orphans)
    for p in orphans[:10]:
        warnings.append(f"No inbound links and not in COLLECTIONS.md: {p}")


def check_skills():
    """Every pipeline skill dir has a README; every .claude skill has SKILL.md with name+description."""
    problems = 0
    for d in sorted((ROOT / "skills").iterdir()):
        if d.is_dir() and d.name not in ("lib", "__pycache__") and not (d / "README.md").exists():
            warnings.append(f"skills/{d.name}/ has no README.md")
            problems += 1
    for d in sorted((ROOT / ".claude" / "skills").iterdir()):
        sk = d / "SKILL.md"
        if not sk.exists():
            warnings.append(f".claude/skills/{d.name}/ has no SKILL.md")
            problems += 1
        elif not re.search(r"^description:", sk.read_text(), re.MULTILINE):
            warnings.append(f".claude/skills/{d.name}/SKILL.md has no description")
            problems += 1
    metrics["skill_problems"] = problems
    metrics["claude_skills"] = len(list((ROOT / ".claude" / "skills").iterdir()))


def check_pipeline():
    """Did the daily pipeline actually commit on recent weekdays?"""
    log = git("log", "--since=14 days ago", "--format=%ad|%s", "--date=short").splitlines()
    ran = {l.split("|")[0] for l in log if "[automated]" in l}
    today = dt.date.today()
    missing = []
    for i in range(1, 15):
        d = today - dt.timedelta(days=i)
        if d.weekday() < 5 and d.isoformat() not in ran:
            missing.append(d.isoformat())
    metrics["pipeline_runs_14d"] = len(ran)
    metrics["pipeline_missing_weekdays_14d"] = len(missing)
    if missing:
        warnings.append("No automated pipeline commit on weekday(s): " + ", ".join(sorted(missing)) +
                        " (holidays, or the home runner was down)")


def check_hygiene():
    size = git("count-objects", "-vH")
    m = re.search(r"size-pack: (.+)", size)
    metrics["repo_pack_size"] = m.group(1) if m else "?"
    tracked = git("ls-files").splitlines()
    big = []
    hits = []
    for t in tracked:
        p = ROOT / t
        if not p.is_file():
            continue
        if p.stat().st_size > 5_000_000:
            big.append(f"{t} ({p.stat().st_size // 1_000_000} MB)")
        if p.suffix in (".md", ".json", ".yaml", ".yml", ".py", ".txt", ".sh") and p.stat().st_size < 2_000_000:
            text = p.read_text(errors="replace")
            for pat, label in SECRET_PATTERNS:
                if re.search(pat, text):
                    hits.append(f"{t}: looks like a {label}")
    for b in big:
        warnings.append(f"Large tracked file: {b}")
    for h in hits:
        critical.append(f"Possible secret committed: {h}")
    metrics["possible_secrets"] = len(hits)
    for name in (".env",):
        if name in tracked:
            critical.append(f"{name} is tracked by git")
    branches = [b.strip() for b in git("branch", "-r").splitlines() if "HEAD" not in b and "origin/main" not in b]
    metrics["stale_remote_branches"] = len(branches)
    for b in branches:
        suggestions.append(f"Remote branch still exists: {b}")


def previous_metrics():
    prev = sorted(OUT_DIR.glob("*-audit.json")) if OUT_DIR.exists() else []
    today = dt.date.today().isoformat()
    prev = [p for p in prev if not p.name.startswith(today)]
    return json.loads(prev[-1].read_text()) if prev else None


def render(prev):
    today = dt.date.today().isoformat()
    health = "Action required" if critical else ("Needs attention" if len(warnings) > 5 else "Good")
    L = [f"# System audit: {today}", "",
         "*Generated by `scripts/audit.py` (deterministic half). The judgment half "
         "(best practices, rules drift, red-team) is added by the `/system-audit` skill when run interactively.*", "",
         "## Summary", f"- Overall health: **{health}**",
         f"- Findings: {len(critical)} critical, {len(warnings)} warnings, {len(suggestions)} suggestions", ""]
    for title, items in (("Critical", critical), ("Warnings", warnings), ("Suggestions", suggestions)):
        L += [f"## {title}"] + ([f"- {i}" for i in items] or ["- None."]) + [""]
    L += ["## Metrics", "| Metric | Now | Previous |", "|---|---|---|"]
    for k, v in metrics.items():
        p = prev.get(k, "-") if prev else "-"
        L.append(f"| {k} | {v} | {p} |")
    L += ["", "## Next audit", "Monthly. Sooner if anything above is critical.", ""]
    return "\n".join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    files = canon_files()
    metrics["canon_files"] = len(files)
    inbound = check_links(files)
    check_frontmatter(files)
    check_index_drift(files)
    check_quarantine()
    check_staleness()
    check_bloat(files)
    check_orphans(inbound)
    check_skills()
    check_pipeline()
    check_hygiene()

    report = render(previous_metrics())
    if args.dry_run:
        print(report)
        return
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    stem = dt.date.today().isoformat() + "-audit"
    (OUT_DIR / f"{stem}.md").write_text(report)
    (OUT_DIR / f"{stem}.json").write_text(json.dumps(metrics, indent=2) + "\n")
    print(f"Wrote outputs/audits/{stem}.md ({len(critical)} critical, {len(warnings)} warnings)")


if __name__ == "__main__":
    sys.exit(main())
