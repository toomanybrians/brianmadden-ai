---
name: weekly-update
description: Weekly Wrap Up (named "Deeper Thinking" at launch, renamed by Brian on Substack 2026-08-26) — the lower-frequency companion to the Daily Brief. A live ceremony with Brian that recaps the stories since the last one, clears the promotion-candidates and staleness-candidates queues, captures his real takeaways, and drafts a dual-byline "Weekly Wrap Up" post. Use when the user runs /weekly-update, or asks for a weekly review, a Weekly Wrap Up issue, or "what's changed since last time" walkthrough.
---

# Weekly Wrap Up ceremony

The internal skill/directory name stayed `weekly-update` (matches how the
Daily Brief's own skill directory is `skills/brief/` even though its
public name is "Daily Briefing" — the mechanism's name and the product's
name don't have to match). The actual publication is called **Deeper
Thinking** — Brian's own name, chosen 2026-08-24 over a shortlist that
included "Second Thoughts" and "Loose Threads." The name is doing real
work: it's the literal claim of one of this ceremony's own recurring
promote-candidates ("AI makes knowledge work deeper, not faster"), and it
contrasts cleanly with the Daily Brief's speed.

This is `me/developing-thinking.md`'s D5-era open ask (`BUILD.md` open
decision #13, "a weekly 'how my thinking has changed' recap post") and
Workstream E's deferred Substack question, both closed 2026-08-24: dual
byline (Brian + brianmadden.ai). Substack placement: Brian is now leaning
toward a dedicated Section of its own (revised 2026-08-24 from the
original "fold into existing structure" call, made the same day before
the first issue was even finished) — still unbuilt (manual Substack UI
work, same category of gap as the rest of Workstream E), but don't assume
"no Section" going forward.

Unlike `brief.py`/`triage.py`, the actual ceremony is **not a script that
runs unattended.** Brian's own framing was explicit: he wants to read a
recap, talk it through live, and give his own reactions — the value is
the conversation, not just the artifact. This skill is that conversation,
in the same spirit as [review-thinking](../review-thinking/SKILL.md), and
reuses that skill's mechanics for the developing-thinking.md portion
rather than duplicating them.

**One part of the pipeline does run unattended, added 2026-08-24, Brian's
own ask:** [skills/weekly/gather.py](../../../skills/weekly/gather.py)
assembles the prep doc deterministically (no LLM call of its own beyond
re-running `triage.py`) and, with `--send`, emails it to Brian. Wired into
`daily-pipeline.yml` to run on Fridays, after that day's Daily Brief. It
does **not** run the interactive ceremony — steps 4 onward below still
need Brian live, whenever he actually sits down with the emailed prep
doc, not necessarily the same day it lands.
[skills/weekly/render.py](../../../skills/weekly/render.py) is the other
reusable script — Substack-paste HTML for the finished post.

## Cadence

Variable, not fixed weekly — Brian's own words: "since I last did this...
ideally a week, could be a few days, could be a few weeks." Driven by
`outputs/weekly-updates/.last_run.json` (same `{"last_run_utc": "..."}`
shape as `outputs/technical-briefings/.last_run.json`), read at the start
of every run — by both `gather.py` and this ceremony. No prior run
recorded → default the window to 7 days back. `gather.py`'s automated
Friday run and the live ceremony share the same clock: whichever runs
last (usually `gather.py`, since it's unattended) sets the window the
other picks up from next time.

## Steps

1. **Check for an existing same-batch prep doc before regenerating.**
   `gather.py`'s Friday run may have already written and emailed
   `outputs/weekly-updates/YYYY/MM/YYYY-MM-DD-prep.md` earlier — if a prep
   doc exists from since the last live ceremony ran (check its `date`
   against `outputs/weekly-updates/.last_run.json`... but note `gather.py`
   updates that same file, so in practice: if a prep doc's file date is
   after the *ceremony's* last run — track this separately if needed, or
   just ask Brian whether he's already seen a prep email), read that
   file instead of re-gathering from scratch. Re-run `triage.py` anyway
   if more than a day or two has passed since the prep doc was written —
   a stale staleness-queue snapshot defeats the point (same non-negotiable
   as `review-thinking` step 1). If no recent prep doc exists (Brian
   triggering this ad hoc, off the Friday cadence), gather fresh — same
   logic `gather.py` runs, described there.

2. **Present the prep doc to Brian before discussing anything.** If it
   arrived by email days ago, don't assume he remembers the details —
   summarize the scale (how many stories, how many queue items) and let
   him set the pace, same as the first live run did.

3. **Walk the promotion-candidates queue, one entry at a time, in the
   order the file lists them.** For each: show Brian the thread (what
   recurred, how many times, the actual notes), ask what he wants to do,
   apply immediately:
   - **Promote** — draft the addition into `me/developing-thinking.md`'s
     "What's connecting" section together, in his words as much as
     possible, dated today. Then delete that entry from
     `promotion-candidates.md` — promoted is resolved, not still queued.
   - **Reject** — delete the entry from `promotion-candidates.md`, no
     addition anywhere. Rejected is also resolved.
   - **Not yet** — leave the entry in place, still open. Don't force a
     decision on something he's genuinely unsure about.
   - **Consolidate** — if two or more entries turn out to be the same
     underlying story (the pipeline's thread-matching is exact-slug-only,
     per `BUILD.md` open decision #15 — this happens), say so before
     asking for a decision on each separately, and propose merging them
     into one canon entry instead.
   With a real backlog (more than a handful of entries), don't grind
   through them one cold call at a time — group them by an honest read
   first (obvious near-duplicates, clean promotes, genuine judgment
   calls, low-interest ones) and give Brian that read before asking for
   decisions; he can always ask for strict one-by-one instead. Same
   non-negotiable either way: never batch-apply, never promote or reject
   without his live call on that specific entry or group.

4. **Walk the staleness-candidates queue the same way `review-thinking`
   already does** (its steps 1-2, applied here rather than duplicated) —
   quoted item, category, reasoning, his decision (cut / promote / leave
   as-is / archive a framework), applied live. If a promotion-candidate
   from step 3 and a staleness-candidate here turn out to be evidence for
   the same underlying write-up (happened on the first real run — a
   tracked "machine speed vs. human absorption" thread was the evidence
   base for a staleness-flagged "human clock speed is the invariant"
   promote-candidate), resolve them together, not separately.

5. **Ask directly for his takeaways on the week's stories** — not "does
   this look right," but what actually struck him, what he'd push back
   on, what he wants people to know he thinks about it. This is the part
   only he can supply; don't draft placeholder reactions and ask him to
   approve them backwards. If the prep doc's "Comments you left this
   week" section has anything in it (built 2026-08-26, after Brian
   commented directly on a Daily Brief and asked for it to feed the
   ceremony), treat those comments as a real takeaway already in his own
   words, not just background color — surface them here rather than
   asking him to re-articulate a reaction he already wrote down live.

6. **Surface content candidates — topics worth a future blog post or
   podcast episode.** Added 2026-08-24, Brian's own idea mid-first-run:
   this ceremony already produces exactly the raw material for "what
   should I write/talk about next" — every "promote" decision from steps
   3-4 that got logged as a follow-up writing task *is* a content
   candidate, plus anything from step 5's takeaways or the week's stories
   that clearly has legs but doesn't belong in `developing-thinking.md`
   itself. List them in the post (step 9) — but see that step's specific
   voice instruction: these need to read as an approachable hook, not a
   dense internal note.

7. **Update `## Right now`**, same as `review-thinking` step 4 — ask
   what's most front-of-mind independent of anything flagged above.

8. **Bump the review timestamp even if nothing else changed.** Add (or
   update) a `last_reviewed: YYYY-MM-DD` field in
   `me/developing-thinking.md`'s frontmatter — deliberately separate from
   `updated`, which per existing convention only moves when content
   actually changes. `last_reviewed` records "a human looked at this and
   confirmed it still holds," which is real signal on its own even in a
   week where every candidate was "keep as-is." If any content actually
   changed this run (steps 3-4 almost always mean it did), bump `updated`
   too and flip `status` to `reviewed-and-updated` — Brian was live for
   every edit, so this isn't the machine upgrading its own status, it's
   recording his direct approval of specific diffs, same rule
   `render.py`'s hand-edit detection already applies elsewhere.

9. **Draft the Weekly Wrap Up post itself**, collaboratively — not a
   mechanical rehash of the prep doc, and not written in the pipeline's
   own internal shorthand. Brian's explicit ask (2026-08-24, reacting to
   the first draft): this should read as something a real person would
   want to read, not "too AI science fancy pants." Structure, with a
   one-line explainer under each heading so a reader who's never seen
   this format before understands what they're looking at — **written as
   plain prose, not set off in italics** (Brian's own light copyedit,
   2026-08-24, first issue: he stripped the italics from every explainer
   line and folded them into normal-flowing sentences — italicizing them
   made them read as a publisher's aside rather than part of the piece).
   **Also cut, same edit: any self-referential commentary about the
   pipeline's own state** ("this issue is bigger than a normal one will
   be because it's clearing a backlog," "this list is bigger than a
   normal issue's will be") — say what happened, don't narrate why the
   format looks unusual this time:

   - **Opening paragraph** — what Weekly Wrap Up is, in plain terms,
     varies naturally issue to issue rather than being a fixed
     boilerplate string. First issue's version: "the daily is fast... this
     is slow, on purpose."
   - **What happened this week** — the week's biggest stories, condensed
     from the prep doc's list, not the full daily-brief detail. Explainer:
     be honest that these are the AI's picks from each day's "worth
     Brian's attention" list, not stories Brian hand-selected — don't
     overclaim his personal curation of each one.
   - **What moved in the thinking** — promotions, cuts, framework
     revisions, **as one continuous nested bullet list** — a bolded
     top-level bullet per category (Consolidated / Promoted / Cut /
     Frameworks revised), each with its own items nested underneath, not
     alternating bold-paragraph-then-separate-list blocks. Brian's
     explicit ask, twice (the second time specifically converting the
     bold-header-plus-list pattern into one true nested list) — for
     at-a-glance scannability. Explainer: how the promotion/staleness
     queues work and why this list exists.
   - **Where my head's at right now** — the current `## Right now`
     bullets, quoted, with a real link to
     `me/developing-thinking.md` on GitHub and an explanation of why that
     file is public and worth linking to (it's the tangible proof of "a
     second brain, edited in public," not an abstract claim). Brian's
     idea, added 2026-08-24: this section is the connective tissue
     showing readers how the whole system fits together, not just news +
     reactions in isolation.
   - **Brian's takeaways** — his actual words from step 5, with a short
     explainer that this part is entirely his, unprompted.
   - **Worth a future post or episode** — content candidates from step 6,
     but **rewritten in plain, approachable language with a short preview
     explanation, not dense internal shorthand.** Brian's own example of
     the transformation: `"Harnesses vs. models — worth a real position,
     not just a tracked thread"` (too dense) becomes something like `"The
     harnesses are almost more important than the models. A low quality
     model with a really good harness will beat a good model with a bad
     harness."` (a real hook + a one-sentence plain explanation of why it
     matters). Every item needs this treatment — this is the section most
     likely to actually get read and shared, so it's worth the extra
     drafting effort.
   - **Closing footer** — written directly into the body (not injected by
     `render.py`, which does no disclosure/footer injection for this
     format — see that file's own docstring for why), matching the Daily
     Brief's footer in spirit: brianmadden.ai self-description, link to
     bmad.com ("Who's Brian?"), link to the GitHub repo. Keep it roughly
     consistent issue to issue for brand recognition across the whole
     publication, but it's plain text in the body, not a fixed constant —
     fine to vary slightly.

   Frontmatter: `title`/`substack_title`: `"Weekly Wrap Up: [date range]"`
   (Substack's own slug doesn't change when a post's display title is
   edited later — confirmed 2026-08-26 renaming the first issue — so get
   the title right at draft time rather than relying on a later rename).
   `tier: 3`, `file_type: weekly-update`, `status:
   reviewed` (Brian was live for the whole thing — this isn't
   `not-reviewed-by-human` the way an unattended daily brief starts; if he
   substantively rewrites a passage himself, that's `reviewed-and-updated`
   instead, per the existing status rule), `authority_level`, `model`,
   `byline: [brianmadden.ai, Brian Madden]`, `sources` (the prep doc plus
   everything it drew on). Write to
   `outputs/weekly-updates/YYYY/MM/YYYY-MM-DD.md`.

   **Before finalizing: check for spaced em-dashes and backtick file
   references.** Both were real misses on the first draft of the first
   issue. `me/style-guide.md` requires em-dashes with no surrounding
   spaces (`word—word`) everywhere in this repo, and — specific to
   anything published to Substack — no inline-code backticks for file
   names (they render oddly in Substack's editor; use *italics* with a
   real GitHub link instead, e.g. `*[developing-thinking.md](github
   url)*`). Run a quick grep for both patterns before rendering:
   ```
   grep -n ' — \| -- ' outputs/weekly-updates/YYYY/MM/YYYY-MM-DD.md
   grep -n '`' outputs/weekly-updates/YYYY/MM/YYYY-MM-DD.md
   ```

10. **Render for Substack paste-in:**
    ```
    python3 skills/weekly/render.py --date YYYY-MM-DD
    ```
    Writes the gitignored `.html` next to the `.md`, same copy-paste
    convention as the Daily Brief. Posting to Substack itself is still
    100% manual — no posting API exists, same as every other output.

11. **Update `outputs/weekly-updates/.last_run.json`** to now, so the next
    run's window starts here (whether the next run is `gather.py`'s next
    Friday or another live ceremony).

12. **Housekeeping:**
    - `_index.json` — surgical text edit only for any new/changed entries
      (developing-thinking.md's word count, revised frameworks' word
      counts), never a full `json.dump()` round-trip (same caution
      `review-thinking` already documents — a full re-dump reformats
      unrelated entries and pollutes the diff). Confirmed 2026-08-24:
      `outputs/` isn't tracked in `_index.json` at all, so no new entries
      are needed there for the weekly-updates files themselves.
    - If any framework's `status` or content changed, update
      `CLAUDE.md`/`AGENTS.md`/`README.md` active-framework counts (only
      if a `status: archived` transition happened),
      `llms.txt`, `COLLECTIONS.md`, and run
      `python3 scripts/check_doc_accuracy.py`.
    - `governance-log.md` entry — same discipline as every other session
      touching canon content.
    - Log the session in `BUILD.md`: what the week's window was, what got
      promoted/cut/archived, what Brian's takeaways were, what's still
      open in either queue, and any follow-up writing tasks (promotes,
      content candidates) that still need drafting.

13. **Report back:** a short summary — what got promoted, cut, archived,
    what's still pending in both queues, and a pointer to the rendered
    post ready for Substack.

## What this doesn't do

Never edits `me/developing-thinking.md`, `promotion-candidates.md`, or a
framework's `status` without Brian's live decision on that specific item
— identical non-negotiable to `review-thinking` and `triage.py`. Never
publishes to Substack itself — that stays a manual paste-and-click step,
same as the Daily Brief. `gather.py`'s automated Friday run never makes
any of these decisions either — it only assembles and emails the prep
doc, exactly the same read-only gathering the live ceremony's own first
steps do.

## Known limitations (v1)

- **First real run had no prior `.last_run.json`** — window defaulted to
  7 days, which happened to line up with the 10 daily briefs that existed
  since launch (2026-08-11 through 2026-08-24). A genuinely variable gap
  (Brian's "could be a few weeks") is untested until it actually happens.
- **Partial automation, added 2026-08-24.** `gather.py` on Fridays
  handles the deterministic prep-and-email step. The interactive ceremony
  itself (steps 3 onward here) still needs a live Claude Code session —
  nothing schedules or reminds Brian to actually run `/weekly-update`
  after the email lands. If that gap turns out to matter in practice,
  a `schedule`-skill reminder is the natural next piece, not a change to
  this ceremony.
- **`gather.py` and this ceremony share one `.last_run.json`, which has a
  real edge case:** if Brian doesn't run the live ceremony before the
  *next* Friday's `gather.py` run, that next prep doc's window starts
  from the previous Friday (gather.py's own last run), not from whenever
  the live ceremony actually happens to catch up — meaning a skipped week
  could show up compressed into a later prep doc's "stories" list, or
  get missed if `gather.py` overwrites the clock before the backlog's
  been cleared. Not yet stress-tested; watch the first few real Fridays.
- **Byline mechanics on Substack are still manual.** Frontmatter records
  `byline: [brianmadden.ai, Brian Madden]`, but actually setting two
  contributors on the Substack post (and, if Brian follows through on
  wanting a dedicated Section, creating that Section) is manual editor
  work, same category of gap Workstream E already flagged for tags/
  Sections generally.
