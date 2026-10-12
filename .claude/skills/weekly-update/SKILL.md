---
name: weekly-update
description: Weekly Wrap Up (named "Deeper Thinking" at launch, renamed by Brian on Substack 2026-08-26) — the lower-frequency companion to the Daily Brief. Brian reacts live (talking, dictating, restacking); the AI recaps the stories since the last one, files the promotion-candidates and staleness-candidates queues with default dispositions, drafts a dual-byline "Weekly Wrap Up" post, and hands back a short list of exceptions for Brian to veto (the standing flow since 2026-10-12). Also the single review pass for me/developing-thinking.md (it absorbed the retired /review-thinking on 2026-10-11): args "quick" runs just the queues and front-of-mind check with no post, args "deep" or "monthly" adds an every-item walk. Use when the user runs /weekly-update (or the old /review-thinking), or asks for a weekly review, a Weekly Wrap Up issue, a "what's changed since last time" walkthrough, to review the staleness/triage candidates, or what's front-of-mind right now.
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
the conversation, not just the artifact. This skill is that conversation.
Since 2026-10-12 the conversation is his *reactions*, not his filing
decisions: see "The standing flow" below.

**This is the one review pass for `me/developing-thinking.md`.** It
absorbed the standalone `/review-thinking` skill on 2026-10-11 (Brian's
call: one weekly-ish pass for everything, not two overlapping ceremonies;
the old skill is in git history). `triage.py` surfaces candidates and
applies no judgment; this skill is where the AI applies a disposition to
each one and Brian reviews by exception, in the same sitting.

## Modes, chosen by `args`

- **Full (default, no args).** Every step below, ending in the drafted
  post.
- **Quick (`args` mentions "quick" or "review").** The old
  `/review-thinking` quick pass: skip `gather.py`, the story recap, the
  takeaways, content candidates, the post and its render (steps 2, 5, 6,
  9, 10, and the `.last_run.json` bump in 11). Run `triage.py` fresh
  (step 1), file both queues (steps 3-4), update `## Right now` (step 7),
  bump `last_reviewed` (step 8), do housekeeping and report (steps 12-13).
  Meant to run any time Brian wants a pass, not on a schedule.
- **Deep (`args` mentions "deep" or "monthly").** Everything in Full or
  Quick (Brian says which), plus the every-item walk in step 4b.

**One part of the pipeline is scripted, but run manually, not
unattended:** [skills/weekly/gather.py](../../../skills/weekly/gather.py)
assembles the prep doc deterministically (no LLM call of its own beyond
re-running `triage.py`) and, with `--send`, emails it to Brian. Added
2026-08-24 wired into `daily-pipeline.yml` to run automatically on
Fridays; **changed 2026-09-04 to manual-only** (Brian's call — an
auto-run right after that day's Daily Brief always missed whatever he
did in reaction to Friday's own post, since restacking or commenting on
it happens after he's read the email, not before it's sent). Brian now
reads Friday's post as normal, then runs `gather.py` himself — usually by
just starting this ceremony, since step 1 below runs it as part of
kicking off — whenever he's actually ready to sit down with it, so the
prep doc reflects everything he's flagged, not a few-hours-stale
snapshot. It does **not** run the interactive ceremony — steps 3 onward
below still need Brian live.
[skills/weekly/render.py](../../../skills/weekly/render.py) is the other
reusable script — Substack-paste HTML for the finished post.

## Cadence

Variable, not fixed weekly — Brian's own words: "since I last did this...
ideally a week, could be a few days, could be a few weeks." Driven by
`outputs/weekly-updates/.last_run.json` (same `{"last_run_utc": "..."}`
shape as `outputs/technical-briefings/.last_run.json`), read at the start
of every run — by both `gather.py` and this ceremony. No prior run
recorded → default the window to 7 days back. Since `gather.py` is now
manual-only (2026-09-04), the common case is one atomic session: Brian
starts `/weekly-update`, step 1 below runs `gather.py` fresh, and the
live ceremony continues right after — no more separate "unattended run
sets the clock, live session picks it up later" gap to reason about.

## The standing flow: the AI files, Brian reviews by exception

Brian's call, 2026-10-12, after a trial run on 2026-10-11. The
item-by-item walk was where the effort went, and most of it was
classification (promote, fold or reject; which file does this go in),
which the AI does well. What only Brian can supply is what he believes,
what he will say publicly, and what he cares about. So the flow is:

- **Brian's part:** react. Talk, dictate, restack, flag. Skim one diff
  and a short "needs you" list. Veto by exception. Say "approved" to
  finish.
- **The AI's part:** gather and triage, present the week, take his
  reactions as dictation, apply a disposition to every queue item, draft
  the post, run housekeeping, commit locally, and hand back the
  exception list.

Rules of the flow:

1. **Dispositions are applied by default, not asked about.** Fold into an
   existing entry is the default; promote to a new entry only when Brian
   has stated the claim himself; reject when it's outside his beat;
   keep only when a decision truly depends on something that hasn't
   happened yet. A queue that never empties is the chore this flow exists
   to remove. If Brian asks to walk the queue item by item, do that.
2. **His voice comes only from his words.** Right now bullets and new
   "What's connecting" entries that make a claim are written from what he
   dictated or published, as nearly in his words as possible. The AI never
   invents a position, a prediction, or a reaction for him. Evidence and
   observations can be AI-filed.
3. **Label what a machine wrote.** Every machine-filed paragraph carries an
   inline label (`October 11 addition (AI-filed): ...`); text taken from
   dictation carries `(dictated <date>)`. Review state is handled in step 8.
4. **What stays Brian's:** archiving a framework, any edit to
   `me/voice.md`, publishing to Substack (still a manual paste), and
   anything he says to hold.
5. **Sensitive third-party material goes to Brian first.** Competitors and
   named private individuals: summarize neutrally for him, hold drafts
   outside the repo (not in the working tree, where another session could
   commit them), and write them up as "what's happening in the market,"
   not as promotion. Nothing about them is committed until he has seen the
   summary.
6. **The exception list** (step 13) is the only thing Brian has to read
   closely: seven items or fewer, each with the default that was applied
   and what reversing it means. It can be empty.
7. **Commits.** Split code, ingest notes, and canon plus outputs into
   separate commits. Stage specific paths, never `git add -A`: other
   sessions work in the same checkout. Run
   `python3 scripts/check_public_safe.py --staged` before each commit.
   Push code and ingest notes straight to `main`; hold the canon commit
   (`me/`, `frameworks/`, `outputs/weekly-updates/`) until Brian says
   "approved."

## Steps

1. **Run `gather.py` fresh at the start of every session**, unless Brian
   says he already has a prep doc open from earlier today (he might, if
   he ran it separately before starting this session — check
   `outputs/weekly-updates/YYYY/MM/YYYY-MM-DD-prep.md` for today's date
   first and use that instead of re-gathering: don't regenerate something
   that already exists and hasn't gone stale). **Always re-run
   `python3 skills/triage/triage.py` fresh** (one model call) rather than
   trusting whatever is already in
   `outputs/canon-triage/staleness-candidates.md`: a stale snapshot means
   Brian would be deciding on old data. Read the freshly written file.

2. **Present the prep doc to Brian before discussing anything.** If it
   arrived by email days ago, don't assume he remembers the details —
   summarize the scale (how many stories, how many queue items) and let
   him set the pace, same as the first live run did.

3. **File the promotion-candidates queue.** Apply a disposition to every
   entry yourself, then show Brian the grouped result rather than each
   entry cold. Group near-duplicates first (the pipeline's thread-matching
   is exact-slug-only, per `BUILD.md` open decision #15, so one story often
   arrives as several entries):
   - **Fold** (the default) — add the evidence to the existing "What's
     connecting" entry, open question, or framework section it belongs to,
     as a dated "(AI-filed)" paragraph; duplicates fold into one paragraph.
   - **Promote** — a new "What's connecting" entry, only when Brian has
     stated the claim himself, in his words as much as possible, dated
     today and labeled "(dictated)".
   - **Reject** — outside Brian's beat or not worth a line; say why in the
     cleared note.
   - **Keep** — leave it queued only if a decision truly depends on
     something that hasn't happened yet.
   Resolved entries (folded, promoted, rejected) are deleted from
   `promotion-candidates.md` and the header note records where each one
   went, so a later reader can follow it. Judgment calls (a reject near his
   beat, a fold that complicates an argument) go on the exception list.

4. **File the staleness-candidates queue** the same way, in the file's order
   (developing-thinking items, then frameworks). Cut: remove it. Already
   published: point at where it lives. Promote-candidate: it's real writing
   work, so make sure it's in `me/post-ideas.md` (add an idea if missing)
   rather than drafting it inline. Worth-revisiting framework: add a dated
   update section that reconciles it with newer canon, original text
   untouched. Archiving a framework (`status: archived` + `archived_date` +
   `archived_reason`, per `docs/frontmatter-schema.md`) stays Brian's
   explicit call, never inferred. Keep-as-is is a fine outcome. If a
   promotion-candidate from step 3 and a staleness-candidate here are
   evidence for the same underlying write-up (happened on the first real
   run — a tracked "machine speed vs. human absorption" thread was the
   evidence base for a staleness-flagged "human clock speed is the
   invariant" promote-candidate), resolve them together.

4b. **Deep/monthly mode only:** after the queues, go through the *entire*
   "What's connecting" and "Scratchpad" sections of
   `me/developing-thinking.md`, item by item (including everything the
   triage pass was silent on), and every `frameworks/*.md` file, briefly
   surfacing each and asking if it's still live, needs a cut, or needs a
   second look. Slower by design. (Repo health and cross-canon synthesis
   live in `/system-audit` and `/connect-the-dots`; this is only the
   developing-thinking walk.)

5. **Ask directly for his takeaways on the week's stories** — not "does
   this look right," but what actually struck him, what he'd push back
   on, what he wants people to know he thinks about it. This is the part
   only he can supply; don't draft placeholder reactions and ask him to
   approve them backwards. If the prep doc's "What Brian flagged this
   week (restacks & comments)" section has anything in it (built
   2026-08-26 for comments, extended 2026-09-04 to also pull his
   restacks — see `skills/weekly/gather.py`'s `fetch_own_notes_in_window()`
   — after Brian reacted directly to a Daily Brief and asked for it to
   feed the ceremony), treat those as a real takeaway already in his own
   words, not just background color — surface them here rather than
   asking him to re-articulate a reaction he already wrote down live.
   Dictation is the input: take what he says as-is and file it (Right now,
   entries, post ideas). Ask a question only when the answer changes what
   gets written.

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

7. **Update `## Right now`** — ask directly what's most front-of-mind,
   independent of anything flagged above. Update the section at the top of
   `me/developing-thinking.md` to match: add, remove or reword bullets so
   it stays a genuine 3-5 item list, not a growing tracker. An item
   dropping off doesn't mean it was resolved; say so if Brian seems to be
   treating it that way.

8. **Handle review state honestly.** Machine-applied edits don't earn a
   `reviewed*` status (MAINTAINER rule 4). When a file whose `status` is
   `reviewed` or `reviewed-and-updated` gets machine-filed edits, set its
   `status` to `not-reviewed-by-human`, bump `updated`, and leave
   `last_reviewed` alone; the inline labels from the standing flow say
   which paragraphs a machine wrote. When Brian says "approved" (or edits
   the diff and then approves), flip `status` to `reviewed-and-updated`, set
   `last_reviewed` to today, and run `build_indexes.py --write` so the body
   "Last updated" lines follow. `last_reviewed` is deliberately separate from
   `updated`: it records "a human looked at this and confirmed it still
   holds," which is real signal even in a week where nothing changed, so
   bump it on its own if Brian reviewed and nothing needed editing.

9. **Draft the Weekly Wrap Up post itself** from the prep doc, the briefs,
   and Brian's dictation — not a
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

   **Section order, revised 2026-08-28 (Brian's explicit ask, reading the
   second issue's draft): most-interesting-first, not chronological-
   pipeline-order.** The first issue's order (stories → what moved →
   right-now → takeaways → future posts) buried the parts with the
   broadest appeal under pipeline bookkeeping. Current order:

   - **Opening paragraph** — what Weekly Wrap Up is, in plain terms,
     varies naturally issue to issue rather than being a fixed
     boilerplate string. First issue's version: "the daily is fast... this
     is slow, on purpose." **Set this whole paragraph in italics** (Brian
     did this by hand on the Sep 5–11 issue — it reads as the framing note
     it is), and **name brianmadden.ai as "the AI" explicitly** the first
     time it appears — Brian's edit: "me (brianmadden.ai, the AI) reading
     everything overnight...". The brain-vs-AI distinction has to be
     unambiguous from the first line; the same rule runs through the next
     bullet and the takeaways explainer.
   - **Where Brian's head is at right now** — moved to lead, right after
     the opener (was near the end in issue 1). **Title it "Where Brian's
     head is at right now," not "Where my head's at"** (Brian's Sep 5–11
     edit): the AI narrates this whole post, so "my head" is ambiguous in
     the one section that's specifically about the *human's* thinking —
     third-person "Brian's" keeps the brain-vs-AI line clean. The current
     `## Right now`
     bullets, quoted, with a real link to
     `me/developing-thinking.md` on GitHub and an explanation of why that
     file is public and worth linking to (it's the tangible proof of "a
     second brain, edited in public," not an abstract claim). Brian's
     idea, added 2026-08-24: this section is the connective tissue
     showing readers how the whole system fits together, not just news +
     reactions in isolation.
   - **This week's stories** — renamed 2026-08-28 from "What happened
     this week" (Brian's ask: read as a real title, not a log-file
     header). The week's biggest stories, condensed by actually reading
     each day's technical briefing linked in the prep doc's "This week's
     daily briefs" list (2026-09-04: the prep doc stopped pre-extracting
     story text — see `skills/weekly/gather.py`'s docstring for why — so
     this step now means opening those files directly, not skimming
     something already assembled), not the full daily-brief detail —
     **every story needs a real inline Markdown link to its actual
     source**, pulled from the relevant day's ingest note or technical
     briefing (2026-08-28 fix: issue 1's draft had none; never invent a
     URL — if a story's source genuinely has no direct link, name it
     without one rather than
     guessing). Explainer: be honest that these are the AI's picks from
     each day's "what this changes" list, not stories Brian hand-selected
     — don't overclaim his personal curation of each one.
   - **Brian's takeaways** — Brian's thinking from step 5, rendered in his
     voice. **Be honest in the explainer that this section is still
     AI-written from the conversation, not typed verbatim by Brian** —
     Brian's Sep 5–11 edit rewrote the explainer to: "Everything above is
     the pipeline's (the AI's) work. This part is Brian (the human),
     reacting to the week. (Though to be clear this was written by AI,
     based on conversations with Brian.)" Don't claim "unprompted,
     unedited," and don't say Brian "gives the takeaways live" (the footer
     used to) — both overclaim human authorship. Label the pipeline "(the
     AI)" and Brian "(the human)" here too, same discipline as the opener.
   - **What moved in the thinking** — moved later in the order 2026-08-28
     (was earlier; this is pipeline bookkeeping, not the broad-appeal
     material). Promotions, cuts, framework revisions — **2026-08-28
     structure change: a real `###` subheading per category (Promoted as
     new entries / Folded into bigger existing arguments / Cut /
     Deferred / Frameworks revised), each followed by a flat bullet
     list** — not the nested-bullet-list format issue 1 used (a bolded
     top-level bullet with sub-bullets indented underneath), which read
     as one flat list at a single visual level once rendered. **Every
     "Promoted" and "Folded into" item needs a link to where it actually
     lives now** — the specific framework file if it graduated to one, or
     `me/developing-thinking.md#`-plus-the-relevant-section-anchor
     otherwise (GitHub auto-generates anchors from headers — lowercase,
     spaces to hyphens, punctuation stripped). "Cut" and "Deferred" items
     don't need links; nothing survives there to point to. Explainer: how
     the promotion/staleness queues work and why this list exists.
   - **Worth a future post or episode** — stays last. Content candidates
     from step 6, but **rewritten in plain, approachable language with a
     short preview explanation, not dense internal shorthand.** Brian's
     own example of the transformation: `"Harnesses vs. models — worth a
     real position, not just a tracked thread"` (too dense) becomes
     something like `"The harnesses are almost more important than the
     models. A low quality model with a really good harness will beat a
     good model with a bad harness."` (a real hook + a one-sentence plain
     explanation of why it matters). Every item needs this treatment —
     this is the section most likely to actually get read and shared, so
     it's worth the extra drafting effort.

     **Don't re-pitch an idea this same issue already covered in full
     under "What moved → Promoted" (or in "Brian's takeaways") as if it
     were new here.** An idea that just entered canon *and* is worth
     writing is common — but a reader who already read the promote two
     sections up doesn't need the full hook a third time. Compress those
     into a single pointer line (e.g. "Both promotes above are also
     headed for real posts") and save the full plain-language hook
     treatment for candidates that *don't* already appear elsewhere in
     the issue — a Scratchpad item, a takeaway that didn't become a
     promote, a story with legs. Added 2026-09-13: the Sep 5–11 issue
     listed its two lead promotes (execute-now, the AI-slowdown thread)
     a third time here, and Brian flagged the repetition — the same two
     ideas reading as takeaway, then promote, then future-post is the
     failure mode to avoid.
   - **Closing footer** — written directly into the body (not injected by
     `render.py`, which does no disclosure/footer injection for this
     format — see that file's own docstring for why), matching the Daily
     Brief's footer in spirit: brianmadden.ai self-description, link to
     bmad.com ("Who's Brian?"), link to the GitHub repo. Keep it roughly
     consistent issue to issue for brand recognition across the whole
     publication, but it's plain text in the body, not a fixed constant —
     fine to vary slightly. **Two things to carry forward from Brian's Sep
     5–11 edit:** (1) describe what the AI actually does rather than
     claiming co-authorship — his version: "brianmadden.ai — Brian
     Madden's AI second brain, which reads everything he follows (blogs,
     podcasts, YouTubers, Substacks) and reports back daily," and he cut
     the old "The Weekly Wrap Up is co-written: I track the week... Brian
     gives the takeaways live" line (same overclaim the takeaways explainer
     now avoids); (2) the pipeline isn't fully open-sourced yet, so frame
     it as in progress — his wording: "The full pipeline is being
     developed now and will soon be included in his open source second
     brain, which can be explored, forked, or modified on GitHub."

   Frontmatter: `title`/`substack_title`: `"Weekly Wrap Up: [date range]"`
   (Substack's own slug doesn't change when a post's display title is
   edited later — confirmed 2026-08-26 renaming the first issue — so get
   the title right at draft time rather than relying on a later rename).
   `tier: 3`, `file_type: weekly-update`, `status:
   not-reviewed-by-human` (until Brian has read the draft; flip to
   `reviewed` on his approval, or `reviewed-and-updated` if he
   substantively rewrites a passage himself, per the existing status
   rule), `authority_level`, `model`,
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

   **Link everything the draft says Brian did** (his ask, 2026-10-12, after
   he added the restack link to the first standing-flow draft by hand). If
   a sentence says he restacked, noted, wrote, posted, recorded or said
   something, that sentence carries a link: a restack or note to its
   permalink (the prep doc's "What Brian flagged" section links each
   restack's timestamp to the note itself), a post, talk or episode to its
   canonical URL (`me/published-thinking.md`, the posts and talks indexes).
   Never invent one. When no URL is on hand, put the reference on the
   exception list for Brian to supply instead of leaving it bare. Check
   before rendering:
   ```
   grep -n -i 'restack\|i wrote\|i posted\|my note\|last week\|i said' outputs/weekly-updates/YYYY/MM/YYYY-MM-DD.md
   ```
   Every hit in Brian's voice should either carry a link or be on the
   exception list.

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
    - Run `python3 scripts/build_indexes.py --write`. It regenerates
      `_index.json` (word counts, updated dates), `_relationships.json`
      and `llms-full.txt` from the files, and rewrites every repo-size
      number in README / `llms.txt` / CLAUDE.md / AGENTS.md. Never hand-
      edit those. CI fails if they're stale. Read its "advisory" lines.
    - If any framework's `status` or content changed, update
      `CLAUDE.md`/`AGENTS.md`/`README.md` active-framework counts (only
      if a `status: archived` transition happened; the script rewrites the
      numbers, but the prose around them is still yours), `COLLECTIONS.md`,
      and run
      `python3 scripts/check_doc_accuracy.py`.
    - `governance-log.md` entry — same discipline as every other session
      touching canon content.
    - Log the session in `BUILD.md`: what the week's window was, what got
      promoted/cut/archived, what Brian's takeaways were, what's still
      open in either queue, and any follow-up writing tasks (promotes,
      content candidates) that still need drafting. Both journals are
      public history: decisions and outcomes only, no asides or quotes.
    - Commit per the standing flow (rule 7): code, ingest notes, then canon
      plus outputs; `check_public_safe.py --staged` before each.

13. **Report back with the exception list:** seven items or fewer, each
    with the default the AI applied and what reversing it means (a reject
    near his beat, a fold that complicates an argument, any change to his
    words, public-facing claims and names). Then a short summary — what
    got folded, promoted, cut, what's still queued — pointers to the diff
    and the rendered post, and what is pushed versus held. Brian says
    "approved" to finish (step 8), or vetoes items and the AI reverses
    them.

## What this doesn't do

Never upgrades a status by machine (MAINTAINER rule 4), never edits
`me/voice.md`, never archives a framework or flips a framework's `status`
without Brian's explicit call, never writes a position, prediction, or
reaction into Right now or a new entry that Brian didn't state himself, and
never publishes to Substack — that stays a manual paste-and-click step, same
as the Daily Brief. Machine edits to `me/developing-thinking.md`,
`promotion-candidates.md`, and frameworks are allowed under the standing
flow, labeled inline, with the file's status lowered until Brian approves.
`gather.py` still makes no decisions, run manually or not — it only
assembles and emails the prep doc, exactly the same read-only gathering the
ceremony's own first steps do.

## Known limitations (v1)

- **First real run had no prior `.last_run.json`** — window defaulted to
  7 days, which happened to line up with the 10 daily briefs that existed
  since launch (2026-08-11 through 2026-08-24). A genuinely variable gap
  (Brian's "could be a few weeks") is untested until it actually happens.
- **Manual trigger, changed 2026-09-04 from Friday automation.** Nothing
  schedules or reminds Brian to actually run this — he has to remember to
  read Friday's post, react to it, and then kick this off himself. That's
  a deliberate tradeoff (see `gather.py`'s docstring): automation meant
  the prep doc systematically missed Friday's own reactions, which
  mattered more than the reminder would have. If forgetting to run it
  turns out to be the bigger problem in practice, a `schedule`-skill
  reminder (not a return to auto-running `gather.py` itself) is the
  natural fix.
- **The restacks/comments feed (`fetch_own_notes_in_window()`) only
  covers Substack's "Notes" mechanism** (restacking a post, with or
  without added commentary) — every real example seen so far, but if
  Brian ever leaves a genuine reply inside a post's own comment thread
  *without* restacking, that wouldn't show up here. Worth revisiting only
  if that pattern actually shows up.
- **Byline mechanics on Substack are still manual.** Frontmatter records
  `byline: [brianmadden.ai, Brian Madden]`, but actually setting two
  contributors on the Substack post (and, if Brian follows through on
  wanting a dedicated Section, creating that Section) is manual editor
  work, same category of gap Workstream E already flagged for tags/
  Sections generally.
- **Review is per file, labeling is per paragraph.** `status` can't say which
  paragraphs Brian read, so the inline "(AI-filed)" and "(dictated)" labels
  carry that. If consuming AIs get confused by it, a per-entry marker is the
  next step.
- **Drift risk.** Machine-filed evidence can drift from what Brian would
  say. The mitigations are the rules that his voice comes only from his
  words and that judgment calls go on the exception list; the exception
  list is where drift gets caught, so keep it honest.
- **The "Start here" overview** in a prep doc is written by the AI by hand;
  `gather.py` doesn't generate it, and has no talks section, so a talk
  reaches the ceremony only if someone hand-flags a queue entry.
