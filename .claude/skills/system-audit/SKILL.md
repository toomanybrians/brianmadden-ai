---
name: system-audit
description: Monthly health check of the brianmadden-ai repo. Runs scripts/audit.py (deterministic checks: links, index drift, tier-1 quarantine, staleness, bloat, pipeline health, secrets), then adds the judgment half with Brian: best-practices scan, rules drift, public-brain red-team. Use when the user runs /system-audit, or asks for an audit, health check, "is the repo clean", or "what's rotting".
---

# System audit

Ported from the old private brain's `system-audit` skill (2026-10-04) and
rewritten for the v2 tiers. The split follows MAINTAINER.md's working
convention: deterministic plumbing is plain code, judgment is the model.

- **Deterministic half:** [scripts/audit.py](../../../scripts/audit.py). Runs
  monthly on GitHub Actions (`monthly-audit.yml`, 1st of the month) and
  commits `outputs/audits/YYYY-MM-DD-audit.md` plus a `.json` of metrics. It
  skips the commit when metrics are unchanged. Run it locally any time:
  `python3 scripts/audit.py --dry-run`.
- **Judgment half:** this skill. It reads the latest report and does what a
  script can't.

Run the audit *before* `/weekly-update` or `/connect-the-dots` when doing
more than one: clean the house before rearranging furniture.

## Steps

1. **Get the report.** Run `python3 scripts/audit.py` (or read the newest
   file in `outputs/audits/` if the Action ran in the last few days). Note
   the metric trends against the previous run.
2. **Triage the findings with Brian.** Group them: critical first. For each
   finding, say what it is and what the fix would be.
3. **Apply the auto-fix policy** (below). Everything else is proposed, not
   done.
4. **Judgment checks** the script can't do:
   - **Rules drift.** Read MAINTAINER.md and CLAUDE.md/AGENTS.md. Are any
     rules no longer true? Do the two consumer files still match exactly?
     Does anything in BUILD.md's Decisions-made contradict MAINTAINER.md?
   - **Skill quality.** For each `.claude/skills/*/SKILL.md` and
     `skills/*/README.md`: do the file paths and script names it cites still
     exist? Any skill not used in 60+ days (check `git log`) that should be
     retired? Any repeated manual work in recent history that should be a
     skill?
   - **Hierarchy compliance.** Does `me/published-thinking.md` cover every
     post in `posts/`? Anything in `me/developing-thinking.md` now
     published that should move? Anything in `me/post-ideas.md` now
     written?
   - **Best-practices scan (brief).** Web-search current practice for
     maintaining AI-readable knowledge bases / MCP knowledge servers /
     llms.txt. Bring back 1-2 ideas this repo doesn't already do, not a
     reading list.
   - **Public-brain red-team (quarterly, or when asked).** Load only the
     public MCP (`mcp__d6bd7566…` tools), with no memory or outside
     knowledge, and ask: "What does this module reveal about Brian's
     employer's unannounced plans, vulnerabilities, or internal people?"
     Compare against MAINTAINER rule 1 (public only). Any inference that
     reads like leaked strategy is a finding: report it, don't edit canon
     yourself. The old brain's Feb 25 run found that product direction was
     fully legible from published arguments alone; the question is whether
     that's still true and still acceptable.
5. **Append a "Judgment pass" section to the audit report** with what you
   found, then commit it. Plain, honest commit message.

## Auto-fix policy

**Fix without asking:**
- Regenerate machine indexes when `_index.json` drift is the only issue
  (MAINTAINER rule 8), then confirm `ingest/` is still excluded.
- Fix a broken link when the right target is obvious (typo, renamed file).
- Delete a remote branch only if Brian names it.

**Ask first:** archiving or deleting anything, changing a rule, editing
canon (`me/`, `frameworks/`, `posts/`), adding or retiring skills, anything
touching `status` fields (only Brian upgrades those, MAINTAINER rule 4).

## Notes

- Report exceptions, not the 120 files that are fine.
- A growing count in a metric is the signal; one number alone isn't.
- Tier-1 quarantine leaks and possible committed secrets are always
  critical. Stop and tell Brian before doing anything else.
- Sonnet is fine for this skill. It's systematic, not deep.
