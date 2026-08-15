---
name: review-thinking
description: Interactive review ceremony for me/developing-thinking.md — walks through the current staleness-triage flags (or, in full/monthly mode, every item) with Brian, applies whatever he decides live, and checks in on what's currently front-of-mind. Use when the user runs /review-thinking, or asks to review/walk through developing-thinking updates, the triage candidates, or what's front-of-mind right now.
---

# Developing-thinking review ceremony

This is the human-in-the-loop step that acts on what
[skills/triage/triage.py](../../../skills/triage/triage.py) surfaces.
`/maintain` orients a session to repo state and deliberately doesn't pick a
task; `triage.py` generates candidates but applies no judgment of its own —
this skill is the conversation where Brian actually decides, live, and the
edits happen in the same sitting rather than getting queued for later.

Two cadences, chosen by `args`:

- **Quick review (default — no args, or `args` doesn't mention full/monthly).**
  Walk through the current staleness-triage flags plus a front-of-mind
  check-in. Meant to run often — whenever Brian wants a pass, not on a
  fixed schedule.
- **Full review (`args` contains "full" or "monthly").** Everything quick
  review does, plus a section-by-section walk through *every* item in
  "What's connecting"/"Scratchpad" and every framework — not just what the
  model flagged — so Brian gets a chance to weigh in on things the triage
  pass stayed silent on too. This is the stopgap for "verify everything
  periodically" until the deeper monthly-maintenance skill from Brian's
  private brain gets ported in (tabled 2026-08-15 — needs his work login
  and better internet than he had that day; see BUILD.md's open decisions
  list). Don't confuse this mode with that future skill — it's a lighter
  placeholder, not the real thing.

## Steps

1. **Regenerate the triage candidates fresh, every time.** Run:
   ```
   python3 skills/triage/triage.py
   ```
   Always re-run rather than trusting whatever's already sitting in
   `outputs/canon-triage/staleness-candidates.md` — a stale snapshot means
   Brian's decisions would be acting on old data, and re-running is cheap
   (one model call). Read the freshly written file.

2. **Walk through each flagged item, one at a time, in the order the file
   lists them (developing-thinking items, then frameworks).** For each:
   - Show Brian the quoted item (or framework path), its category
     (`already-published` / `promote-candidate` / `worth-revisiting`), the
     model's reasoning and citation, and its suggested action.
   - Ask what he wants to do. Don't assume the suggested action — he may
     keep something the model flagged, or want a different edit than what
     was proposed.
   - Apply his decision immediately, in the same turn:
     - **Cut** — remove the item's paragraph/bullet from
       `me/developing-thinking.md` directly.
     - **Promote** — this is real writing work (a new framework file or a
       published-thinking addition), not a one-line edit. Don't
       auto-draft it inline as part of the walkthrough unless Brian
       explicitly says to start now — capture the decision (e.g. a short
       note where the item was, or just track it verbally for the
       end-of-session summary) and treat drafting it as its own follow-up
       task.
     - **Worth-revisiting, framework case** — ask whether he wants to
       revise the framework file's content now, archive it
       (`status: archived` + `archived_date` + `archived_reason`, per
       `docs/frontmatter-schema.md` — only Brian's call, never inferred),
       or leave it as-is for now.
     - **Keep as-is** — no edit, move to the next item. This is a fine and
       expected outcome, not a failure of the triage pass.
   - Never batch-apply a set of decisions without walking through them
     individually first — the whole point of this ceremony is Brian
     deciding each one, not rubber-stamping a list.

3. **Full/monthly mode only:** after the flagged-item walkthrough, go
   through the *entire* "What's connecting" and "Scratchpad" sections of
   `me/developing-thinking.md`, item by item (including everything the
   triage pass was silent on), and every `frameworks/*.md` file, briefly
   surfacing each one and asking if it's still live, needs a cut, or needs
   a second look. This is slower by design — it's the deeper monthly pass,
   not the everyday one.

4. **Ask directly what's most front-of-mind right now**, independent of
   whatever got flagged above. Update the `## Right now` section at the
   top of `me/developing-thinking.md` to match — add, remove, or reword
   bullets so it stays a genuine 3-5 item list (per the file's own
   description of itself), not a growing tracker. An item dropping off
   doesn't mean anything was resolved; say so if Brian seems to be
   treating it that way.

5. **Housekeeping, if anything changed:**
   - Bump `me/developing-thinking.md`'s `updated` frontmatter field and
     its "Last updated" line in the body to today's date.
   - Update `_index.json`'s matching entry (`word_count`, `updated`) with
     a **surgical text edit only** — not a full `json.dump()` round-trip.
     A full re-dump reformats unrelated array entries elsewhere in the
     file (confirmed 2026-08-15: collapsed `"hosts": ["a", "b"]` one-liners
     into multi-line blocks across ~90 unrelated entries) and pollutes the
     diff with noise that has nothing to do with this session's actual
     change.
   - If any framework's `status` changed, update the same call sites
     `scripts/check_doc_accuracy.py` checks (`CLAUDE.md`/`AGENTS.md`
     active-framework counts, `llms.txt`, `COLLECTIONS.md`) and run
     `python3 scripts/check_doc_accuracy.py` before considering the
     session done.
   - Add a `governance-log.md` entry — same automated-checks (wiki-links,
     internal names, bmad/ paths, em-dashes in canon prose, JSON validity)
     plus manual-review-notes discipline as every other session that
     touches canon content, per MAINTAINER.md's governance surfaces
     section.
   - Log the session in `BUILD.md` — what was reviewed, what was decided
     per item, what's still open (e.g. any "promote" items not yet
     drafted).

6. **Report back:** a short summary of what changed (cuts, archives,
   front-of-mind updates) and what's still pending (promotions not yet
   drafted, anything Brian said "not now" to). Don't re-litigate decisions
   already made in the walkthrough — this is a closing summary, not a
   second round of judgment.

## What this doesn't do

Never applies an edit without Brian's live decision on that specific item
— same non-negotiable as `skills/triage/triage.py` itself and every other
machine-surfaces/human-decides surface in this repo (MAINTAINER.md rule 4:
status is never upgraded by machine; the same principle extends to content
edits here). This skill executes Brian's decisions in the moment; it
doesn't make them.
