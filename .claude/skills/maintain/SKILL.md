---
name: maintain
description: Bootstrap a maintainer session on the brianmadden-ai repo — reads MAINTAINER.md and the live parts of BUILD.md, checks real git state, and reports back where things stand before doing anything else. Use when the user runs /maintain, or at the start of any session where the user is going to build/ingest/publish on this repo rather than query it as a knowledge module.
---

# Maintainer mode bootstrap

This repo does double duty: `CLAUDE.md`/`AGENTS.md` are consumer-facing —
instructions for *other people's* AIs loading Brian's public knowledge
module. This skill is the other side — orienting *this* session (the one
building, ingesting, or publishing) without loading the consumer module or
re-typing the standing kickoff prompt BUILD.md has documented since Day 2:
*"Read MAINTAINER.md and BUILD.md, then let's pick up where we left off."*

`BUILD.md` is a long, append-only session journal (it will only keep
growing) — don't read the whole thing every time. Read the parts that
describe *current* state, not the full history.

## Steps

1. **Read `MAINTAINER.md` in full.** It's short and is the operating
   constitution — non-negotiable rules, tier definitions, working
   conventions. Changes rarely; safe to read in full every time.

2. **Read the live sections of `BUILD.md`, not the whole file:**
   - `## Decisions made` and `## Open decisions` — grep/sed these out by
     heading rather than reading start-to-finish:
     ```
     sed -n '/^## Decisions made/,/^## Day plan/p' BUILD.md
     ```
     This is the actual current state of every standing question.
   - `## Day plan (checklist...)` section — same sed call's tail, or:
     ```
     sed -n '/^## Day plan/,/^## Session log/p' BUILD.md
     ```
     Shows what's checked off and what's next at a glance.
   - The **last 2 dated session-log entries** — don't read the whole
     `## Session log`. Find the entry headers and read from the
     second-to-last one to end of file:
     ```
     grep -n '^### ' BUILD.md | tail -3
     ```
     then `Read` from that line to EOF (or use `tail -n +<line>`). This
     gets you the most recent real narrative — what just happened, what's
     uncommitted, what's flagged as next — without re-reading months of
     history.
   - If the session's task needs older context (e.g. "why did we design
     the thread-tracker this way"), grep BUILD.md for the relevant term
     instead of reading it front-to-back.

3. **Check real git state — don't trust BUILD.md's account of what's
   committed.** BUILD.md has been factually wrong about git state before
   (a "pushed to origin" claim that wasn't true; sessions finding
   concurrent uncommitted work from other threads). Run:
   ```
   git status
   git log --oneline -8
   ```
   If `git status` shows uncommitted changes the most recent session-log
   entries don't account for, say so plainly rather than assuming they're
   this session's own doing — this repo has a real history of concurrent
   sessions editing the same working tree.

4. **Report back before doing anything else.** Summarize: what's done,
   what's currently uncommitted (if anything) and why, what the live open
   decisions/threads are, and what the natural next steps look like per
   BUILD.md's own flagged priorities. Then ask what to work on — this
   skill orients, it doesn't pick the next task.

5. **Suggest a distinctive session title, right after the report.** Every
   `/maintain` session starts out named literally "Maintenance" — there is
   no tool that lets a session rename itself (checked directly, 2026-08-15:
   `set_session_title` explicitly refuses to target the current session,
   and the `"self"` convention `archive_session` accepts doesn't work for
   it either — "Session self not found"). Left alone, every maintainer
   session looks identical in the sidebar for as long as it's running, even
   though sessions that end up with real content eventually get a
   descriptive title. Don't wait for that — propose one now, in the same
   turn as the step 4 report: today's date plus a short, concrete hint
   drawn from what orientation actually found (the most relevant open
   decision number, the day-plan item that's obviously next, an
   uncommitted-change flag — whatever's most distinctive about *this*
   session's starting state, not a generic label). Example: "Maintenance —
   Aug 15 (open decision #8)" or "Maintenance — Aug 15 (uncommitted Gmail
   fix)". State the suggested title plainly and ask Brian to set it via the
   sidebar — never claim to have renamed it, since that action isn't
   available to do on your own.

## What this replaces

The manual kickoff prompt documented at the top of `BUILD.md` ("Read
MAINTAINER.md and BUILD.md, then let's pick up where we left off"). That
text stays in `BUILD.md` as the historical record of the convention; this
skill is the automated version of running it.

## What this doesn't do

Doesn't read `docs/brianmadden-ai-v2-architecture-and-launch-plan.md` by
default — that's the original architecture doc, mostly superseded by
`BUILD.md`'s own Decisions-made/Open-decisions sections for day-to-day
work. Pull it in only if the session's task is genuinely architectural and
the summarized state isn't enough.
