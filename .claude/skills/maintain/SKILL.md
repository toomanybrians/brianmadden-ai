---
name: maintain
description: Bootstrap a maintainer session on the brianmadden-ai repo — syncs the repo with origin first, reads MAINTAINER.md and the live parts of BUILD.md, checks real git state, and reports back where things stand before doing anything else. Use when the user runs /maintain, or at the start of any session where the user is going to build/ingest/publish on this repo rather than query it as a knowledge module.
---

# Maintainer mode bootstrap

This repo does double duty: `CLAUDE.md`/`AGENTS.md` are consumer-facing —
instructions for *other people's* AIs loading Brian's public knowledge
module. This skill is the other side — orienting *this* session (the one
building, ingesting, or publishing) without loading the consumer module or
re-typing the standing kickoff prompt BUILD.md has documented since Day 2:
*"Read MAINTAINER.md and BUILD.md, then let's pick up where we left off."*

`BUILD.md` is an append-only session journal — don't read the whole thing
every time. Read the parts that describe *current* state, not the full
history. As of 2026-08-24, its pre-launch entries (2026-08-09 through
2026-08-18) were trimmed rather than archived to a separate file — that
era's actual decisions already live in Decisions made / Open decisions
above, and git history (`git log -p -- BUILD.md`) has the full text if
the session-by-session narrative is ever genuinely needed. `BUILD.md`
itself now starts at launch day (2026-08-19) and will grow from
there — expect another trim eventually, same reasoning as this one (see
the note at the top of `## Session log`).

## Steps

1. **Sync the repo with `origin` before reading anything.** `main` gets
   real commits from outside this session — the automated
   `daily-pipeline.yml` run every weekday morning, and other maintainer
   sessions — so a session that reads `BUILD.md` before syncing can be
   reading a stale copy without knowing it (confirmed the hard way,
   2026-08-25: a session started 3 commits behind origin with a prior
   session's work still sitting uncommitted locally, and had to untangle
   both reactively mid-task instead of up front). Do this before step 2:
   ```
   git fetch origin
   git rev-list HEAD..origin/main --count   # commits behind
   git rev-list origin/main..HEAD --count   # commits ahead (local-only)
   ```
   - **Behind, 0 ahead, working tree clean:** `git pull --ff-only`. Safe,
     no judgment call.
   - **Behind, 0 ahead, working tree has uncommitted changes:** stash,
     fast-forward, restore, in that order —
     ```
     git stash push -u -m "pre-sync stash: <short description>"
     git pull --ff-only
     git stash pop
     ```
     A real conflict here (a file both origin and the stashed changes
     touched) needs actual judgment, not an automatic pick of "ours" or
     "theirs" — read both sides and reason about which content is
     current before resolving, the same way you'd resolve any merge
     conflict. `outputs/technical-briefings/promotion-candidates.md` is
     a known repeat offender: the automated pipeline appends to it daily,
     so any uncommitted local session that already reviewed/cleared
     entries will conflict with same-day automated appends. Report what
     you found and how you resolved it in the step-4 summary — don't
     resolve silently.
   - **Ahead by any amount (local commits `origin/main` doesn't have):**
     stop and flag it in the step-4 report rather than pushing or
     rebasing automatically — this hasn't happened yet in this repo's
     history and deserves Brian's eyes before anything touches shared
     history.

2. **Read `MAINTAINER.md` in full.** It's short and is the operating
   constitution — non-negotiable rules, tier definitions, working
   conventions. Changes rarely; safe to read in full every time.

3. **Read the live sections of `BUILD.md`, not the whole file:**
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
     instead of reading it front-to-back. If it's not there and predates
     launch, it may have been trimmed — check git history instead:
     `git log -p -- BUILD.md` or `git log --all -S'<term>' -- BUILD.md`
     to find the commit that mentions it.

4. **Check real git state — don't trust BUILD.md's account of what's
   committed.** Step 1 already synced with `origin`, so this is now
   about local nuance the sync itself doesn't narrate: anything the
   stash-pop left uncommitted, any conflict resolution made, and
   BUILD.md's own account of what landed (it's been factually wrong
   before — a "pushed to origin" claim that wasn't true). Run:
   ```
   git status
   git log --oneline -8
   ```
   If `git status` shows uncommitted changes the most recent session-log
   entries don't account for, say so plainly rather than assuming they're
   this session's own doing.

5. **Report back before doing anything else.** Summarize: what step 1's
   sync did (fast-forwarded cleanly? stashed and resolved a conflict?
   found local commits ahead and stopped?), what's done, what's
   currently uncommitted (if anything) and why, what the live open
   decisions/threads are, and what the natural next steps look like per
   BUILD.md's own flagged priorities. Then ask what to work on — this
   skill orients, it doesn't pick the next task.

6. **Suggest a distinctive session title, right after the report.** Every
   `/maintain` session starts out named literally "Maintenance" — there is
   no tool that lets a session rename itself (checked directly, 2026-08-15:
   `set_session_title` explicitly refuses to target the current session,
   and the `"self"` convention `archive_session` accepts doesn't work for
   it either — "Session self not found"). Left alone, every maintainer
   session looks identical in the sidebar for as long as it's running, even
   though sessions that end up with real content eventually get a
   descriptive title. Don't wait for that — propose one now, in the same
   turn as the step 5 report: today's date plus a short, concrete hint
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
