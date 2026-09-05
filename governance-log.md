# Governance log

Audit trail for all content synced to brianmadden.ai. Every commit gets an entry showing what was checked and cleared before publishing.

---

## 2026-09-05 (continued) — CHANGELOG.md: added the Sept 2 second-brain demo milestone

**What changed:** Brian asked for one more milestone in `CHANGELOG.md`: the
Citrix ASEAN webcast follow-up video (2026-09-02), where he connected a
fresh, incognito Claude instance to his own public second brain live on
camera and worked through nine leftover Q&A questions — already fully
documented in canon at
`talks/2026-09-02-citrix-asean-webcast-followup-second-brain-demo.md`
(tier 2, `status: reviewed`, existing file, untouched). Rewrote the
existing "September 2" changelog entry to lead with this (Brian's own
framing: "the first time I actually used it myself, and it was legit")
rather than folding it under the podcast note that was already there for
the same day; both now sit under one dated section. Pulled one detail
straight from the talk's own narration for a nice connecting thread: on
camera, still running plain keyword search, Brian says he should
eventually switch the MCP server to a vector database — two days before
the 2026-09-04 milestone already in this file made that true. `_index.json`
word count corrected for the longer file.

**Why:** Direct request, no research needed beyond confirming which
existing talk file matched his description ("Citrix Asian speech" →
Citrix ASEAN; "video... for Q&A... live in camera" →
the second-brain-demo talk file, identified by content, not by asking).

**No canon content touched** — the talk file itself already existed and
was already `reviewed`; this only added a pointer to it from the new
changelog.

**Automated checks:** em-dash check clean; `_index.json` validated as
JSON; `python3 scripts/check_doc_accuracy.py` clean.

**Result: COMMITTED AND PUSHED.**

## 2026-09-05 — New CHANGELOG.md; first `outputs/essays/` draft on the vector-database build

**What changed:**
- `CHANGELOG.md` (new, root-level, no frontmatter — same convention as
  `README.md`/`GOVERNANCE.md`) — a hand-curated, headline-only history of
  the brain's own build, starting at Day Zero (2026-08-09, the day Brian
  decided to rebuild) and running through today's `semantic_search`/
  Vectorize milestone. Spans both repos: content/pipeline milestones from
  this repo, and the vector-database milestone from
  `brianmadden-ai-server` (a separate repo this session cloned read-only
  to verify dates and commit detail — no write access used or needed
  there). Nine milestones total, each dated and sourced against real git
  history in both repos rather than BUILD.md's prose account of itself.
- `outputs/essays/2026-09-04-semantic-search.md` (new, tier 3,
  `status: not-reviewed-by-human`) — the first file in a new `essays/`
  subdirectory for one-off long-form pieces outside the Daily
  Brief/Weekly Wrap Up cadence. A magazine-style writeup of the
  `semantic_search` build for Substack: the old exact-substring `search`
  tool's limitation, what a vector database actually does and why it's
  fast, how it runs on Cloudflare (Workers AI embeddings, Vectorize, KV,
  a cron trigger), and the three real bugs `brianmadden-ai-server`'s own
  commit history surfaced (a chunking assumption that broke on
  bullet-list files, a reindex job silently discarding its own progress
  on interruption, and two literal NUL bytes in a chunk-id hash that
  never broke anything functionally but flagged the file as binary to
  git). Sourced directly from three commits in the server repo (frontmatter
  `sources:` field), not paraphrased from memory.
- Index wiring for `CHANGELOG.md`: `_index.json` (new entry, plus
  corrected word counts on `CLAUDE.md`/`AGENTS.md` after the tree edit
  below), `llms.txt` (new "History" section), `CLAUDE.md`/`AGENTS.md`
  (repo-structure tree — kept identical, per the parity rule),
  `README.md` ("What's inside" bullet), `outputs/README.md` (new
  `essays/` subdirectory entry). `outputs/essays/` itself is Tier 3 and
  deliberately **not** indexed in `_index.json`, consistent with every
  other `outputs/` subdirectory.

**Why:** Brian asked (dictated, informally) for two things: a change
tracker covering the brain's own build history since he first decided to
rebuild it, headline milestones only, not every commit; and a
magazine-style article about today's vector-database addition, explaining
the old limitation, how vector search actually works, how it runs on
Cloudflare, and a real before/after example, for eventual Substack
publication. Both were read from this session's own research, not
invented: milestone dates and the vector-database technical detail come
from real commit history and code in both repos, cross-checked against
`BUILD.md`'s own account rather than trusting it blind (this session's
`/maintain` bootstrap found `BUILD.md` had no mention of the
vector-database work at all — confirming it happened in the separate
server repo, not this one, which is why that repo was added read-only
this session).

**No canon content touched.** `me/`, `frameworks/`, `posts/`, `talks/`,
`podcast/`, `interviews/`, `pages/` untouched. Nothing here is Brian's
stated position on anything — it's the pipeline's own build history and
one technical explainer, both explicitly `not-reviewed-by-human` until
Brian edits them.

**Automated checks:** `_index.json` edited surgically (not regenerated
wholesale, to avoid reformatting unrelated entries) and validated as
JSON; `python3 scripts/check_doc_accuracy.py` clean, including the
top-level-tree check that would have caught a missed `CLAUDE.md`/
`AGENTS.md` update for the new root file. Em-dash check
(`grep -n ' — \| -- '`) run against both new files per `me/style-guide.md`
and corrected — first drafts used spaced em-dashes throughout, same
mistake the 2026-09-04 Weekly Wrap Up session caught and fixed in its own
draft.

**Result: COMMITTED AND PUSHED** — Brian hasn't reviewed the essay draft
yet (`status: not-reviewed-by-human`, as with any first-pass draft); the
changelog and index wiring are mechanical/factual and not waiting on a
voice review the way a Substack-bound piece is.

## 2026-09-04 — Brian's live reaction to the Weekly Wrap Up prep doc, applied to canon

**What changed:**
- `me/developing-thinking.md` — two new "What's connecting" arguments
  (agent oversight converging on how we supervise humans, now that
  chain-of-thought legibility is eroding; and the bottleneck argument
  that says remove the human from the loop and lands back on "what's
  left for humans?"). One new Scratchpad item (Meta's two-tier Muse
  Spark pricing as the first published price on a customer's own usage
  data, with Brian's own per-worker rescaling and his caveat that it
  prices the data, not the true cost of inference). One dated note on
  the three-waves section flagging that "waves" implies a sequence he
  doesn't mean. `Right now` bullet on human-in-the-loop repointed at the
  new fuller argument. Dates bumped.
- `frameworks/bitter-lesson.md` — new "The third correction: it's a
  sequencing claim, not a standing one" section, plus a rewritten "Using
  this framework" that retires the "IT is trying to capture institutional
  knowledge — the bitter lesson says AI may not need it" deployment
  trigger. This closes the framework flag that has been sitting in
  `outputs/canon-triage/staleness-candidates.md`.
- `me/post-ideas.md` (new, tier 2, `authority_level: 5`) — a curated
  queue of pieces Brian is considering writing, seeded with four:
  compute-availability, the bottleneck argument, agent
  unmonitorability, and knowledge-worker productivity measurement.
- `outputs/technical-briefings/promotion-candidates.md` (tier 3) —
  status updates on three queued threads: one promoted, one dismissed,
  one still deferred but with its destination named.
- Index wiring for the new file: `_index.json`, `llms.txt`, `CLAUDE.md`,
  `AGENTS.md`.

**Why:** Brian dictated a live reaction while reading today's Weekly Wrap
Up prep doc. Everything above is his call, transcribed and applied —
including the two he declined (the entry-level-white-collar-ladder thread,
dismissed as true-but-not-novel; and the Hugging Face material, already
covered on the podcast). The bitter-lesson resolution is his: the
framework isn't wrong, it's a claim about *later* — you build the
knowledge factory with FDEs now, and the system starts cutting pieces out
once the factory automates.

**Public-content check:** clear. Everything added is Brian's own reasoning
about publicly-reported events (Meta's published API pricing, CrowdStrike's
shipped product, OpenAI's own public statements about Astra and
monitorability) plus his own published posts. No Citrix-proprietary,
confidential, or NDA'd material. No third-party text reproduced beyond
short attributed characterizations.

**One judgment call flagged for Brian:** `me/post-ideas.md` was created as
a **public** tier-2 file, on this repo's public-by-default rule and
because `developing-thinking.md` already says things like "likely Brian's
next post" in public. Brian raised the possibility that a post-ideas list
belongs on the private brain instead. If he'd rather it be private, the
file and its four index references come back out cleanly.

**Not added to `COLLECTIONS.md`:** deliberate. That file groups content by
theme for "everything about X" queries; a queue of unwritten pieces has no
theme to sit under and would only dilute the groupings.

**Automated checks:** `python3 scripts/check_doc_accuracy.py` clean.
`_index.json` parses. `CLAUDE.md`/`AGENTS.md` verified still identical
apart from their cross-reference line.

**Result: COMMITTED** — see the commit that includes this entry. The
public/private question on `me/post-ideas.md` was resolved by continuing:
Brian reviewed the summary of what was built, including that file, and
gave no objection — read as confirmation to keep it public, on this
repo's public-by-default rule, not as a decision he didn't make.

---

## 2026-09-04 (continued) — resolved the four flagged staleness items;
drafted and rendered the Weekly Wrap Up post

**What changed:**
- `me/developing-thinking.md` — four items removed from "What's
  connecting": the 2031 worker-shape forecast + its Aug 24 wage note (cut,
  fully captured in `frameworks/2031-worker-shape.md`), the September 2
  canon-built-backward note (cut, fully folded into
  `frameworks/knowledge-factory.md`, which already carries the same
  September 2 video link), the harness-vocabulary note (cut, folded into
  `frameworks/cognitive-stack.md` instead), and the "Switzerland of agent
  workspaces" thesis (cut outright — Brian's explicit call, not a
  rewrite: "there's nothing that I am that interested in right now").
- `frameworks/cognitive-stack.md` — new "Vocabulary update: 'harness' for
  the differentiating middle" section adopting "harness" as the name for
  layers 3-4, with the industry-convergence evidence from the cut
  developing-thinking note.
- `outputs/technical-briefings/promotion-candidates.md` — the two
  resolved entries from the earlier entry today (`agents-defeating-
  chain-of-thought-monitoring`, promoted; `ai-erodes-entry-level-white-
  collar-ladder`, dismissed) deleted outright, per the actual
  `/weekly-update` ceremony convention (resolved entries are deleted, not
  left annotated) — the earlier entry in this log recorded them with
  status annotations only; this entry corrects that to match convention.
- `outputs/canon-triage/staleness-candidates.md` — regenerated fresh via
  `triage.py` now that the four flagged items are resolved; 5 new
  developing-thinking items and 2 frameworks flagged on this run, not
  yet reviewed by Brian.
- `outputs/weekly-updates/2026/09/2026-09-04.md` (new) — the drafted
  Weekly Wrap Up post itself, `status: reviewed` (Brian live for the
  whole ceremony), plus its rendered `.html` (gitignored, Substack
  paste-in only).
- `outputs/weekly-updates/.last_run.json` — bumped to now.
- `_index.json` — word counts updated for `developing-thinking.md` and
  `cognitive-stack.md`.

**Why:** direct continuation of the same live session. Brian asked for
one-line summaries of the four staleness items plus a recommendation,
confirmed the cut on all four (three by not objecting to the
recommended action, one — Switzerland — explicitly), then asked for the
Weekly Wrap Up post itself. This is the `/weekly-update` ceremony's
steps 3-4 and 9-13, run inline rather than as a separate invocation of
the skill, since the queue-walking (steps 3-4) and the takeaway-gathering
(step 5) had already happened across the two live reactions in this
session.

**Public-content check:** clear — same basis as the earlier entry
today; nothing new introduced beyond Brian's own reasoning about already-
public events and his own published posts.

**Automated checks:** `python3 scripts/check_doc_accuracy.py` clean.
`_index.json` parses. Em-dash and backtick pre-render checks run against
the weekly-update draft per the skill's own checklist — no spaced
em-dashes, no inline-code backticks. `render.py` ran clean.

**Result: COMMITTED** — see the commit that includes this entry.

---

## 2026-09-02 — Podcast production defaults to this repo, not the private work brain

**What changed (process, not content):**
- `MAINTAINER.md`: new Working-conventions bullet declaring that podcast
  episode processing (transcript cleanup, publishing-asset drafting,
  checklists) now happens natively in `brianmadden-ai` from the first
  transcript onward, instead of being drafted in Brian's private/work
  second brain and mirrored over after the fact.
- `podcast/bible.md` (new): the production reference for future
  episodes — the two-canonical-links rule (Substack for human listeners,
  this repo for AI/machine consumption), Riverside's real field/character
  constraints (researched live this session, see below), the
  publishing-prep doc format, the publish checklist, and the index/stats
  checklist to run every time an episode lands. Deliberately excluded
  from `_index.json`/`COLLECTIONS.md`/`llms.txt` — maintainer/production
  reference, not consumer module content, same treatment as
  `MAINTAINER.md`/`BUILD.md`.

**Why:** Brian did episode 5's processing on the private work brain as
usual, then noted mid-session that it should really happen on the public
brain going forward, since the podcast is public content from the moment
it's recorded — there's no private-first step to justify, unlike content
that starts as internal material and gets promoted later. He then asked,
separately, where the canonical link and transcript should actually live
(Riverside's own transcript is auto-generated and rough; its description
field is capped at ~4,000 characters). Researched Riverside's hosting
product directly (their help docs, and the live ep5 episode page) rather
than guessing: confirmed the publish form has exactly one text field
(Description, no transcript upload), and the public "Transcript" tab is
Riverside's own uncorrected AI transcription — mangled ("La Riangre" for
*la rentrée*, "Dave Brer" for Dave Brear) — with no bulk-replace path,
only manual word-by-word correction inside Riverside's own editor. That
settles the canonical-link question: Substack (`brianmadden.ai`) stays
the human-facing canonical link (already live, already working, no
character limit); this repo stays the canonical machine-readable source
per `CLAUDE.md`'s own stated purpose ("built for AI consumption via
MCP... not humans browsing files"). Not a choice between the two — they
serve different audiences and both were already in place for ep5.

**No canon content touched.** Process documentation only —
`MAINTAINER.md` and a new maintainer-reference file. No `me/`,
`frameworks/`, `posts/`, `talks/`, `podcast/epN.md`, `interviews/`, or
`pages/` file changed.

**Automated checks:** `python3 scripts/check_doc_accuracy.py` clean (no
top-level tree change — `podcast/bible.md` is nested inside an existing
directory, not a new top-level entry).

**Result: COMMITTED AND PUSHED** — see the commit that includes this
entry.

---

## 2026-08-24 — Reconciled me/voice.md against the private source

**What was synced:**
- Updated `me/voice.md`: the private source and this file had each accumulated content the other lacked. Folded in the private side's fuller phrase/word-avoidance lists, a "Format-specific notes" section (LinkedIn feed posts vs. articles), the "Four-stage post-application realization" framing, and the "boring infrastructure as a feature" analogy. Nothing removed from the existing public version.
- One internal cross-reference in the source material (pointing at a private-only file) was replaced with a plain description rather than carried over.
- Landed concurrently with the "AI-tell phrases" edit below (both touched `me/voice.md`'s "Words Brian avoids" section, on different lines) — merged cleanly, both changes present in the file as committed.

**Automated checks:**
- Wiki-links (`[[`): none found in the merged content — CLEAR
- Internal names: none found (this file has never referenced any) — CLEAR
- Private-system path references: none found — CLEAR
- Em-dashes / heading case: consistent with existing conventions — CLEAR

**Manual review notes:** this file has always been generic communication-style guidance with nothing Citrix-specific or otherwise sensitive in it; the merge is additive only.

**Result: CLEAR TO COMMIT**

---

## 2026-08-24 — voice.md: added "load-bearing" and "receipts" as AI-tell phrases to avoid

**What was synced:**
- Added a bullet to `me/voice.md`'s "Words Brian avoids" section flagging AI-commentary-tell phrases — phrases that read as generic AI output narrating itself rather than Brian's own language, even in content explicitly labeled AI-written (the Daily Briefing included). Triggered by Brian noticing "load-bearing" in the 2026-08-24 Daily Briefing and manually removing it before publishing on Substack; he separately flagged "receipts"/"they have the receipts" as the same category (also found in the 2026-08-13 briefing, left as-is there — published historical record, not retroactively edited per the fossil-record principle).
- Framed as an open-ended bucket ("watch for more of these and add them here as they turn up") rather than a closed list, since Brian's framing suggested this is a pattern he'll keep noticing, not a one-off fix.

**Automated checks:**
- `python3 scripts/check_doc_accuracy.py`: OK, 0 warnings — CLEAR
- No wiki-links, internal names, or `bmad/` paths introduced — CLEAR

**Manual review notes:**
- Pure voice-guide tuning, no public-safety content involved.
- `_index.json`'s `word_count` for `me/voice.md` (551) was already stale before this edit and isn't checked by `check_doc_accuracy.py` — left as-is rather than guess a new number against an undocumented counting methodology.
- Today's committed briefing files (`outputs/technical-briefings/2026/08/2026-08-24.md`, `outputs/published/2026/08/2026-08-24.md`) still read "load-bearing" — Brian's edit was made directly in Substack's editor when pasting, not synced back to the repo's committed copy. Left unchanged pending Brian's call on whether to sync it.

**Result: CLEAR TO COMMIT**

---

## 2026-08-24 — GOVERNANCE.md rewritten for v2: dropped v1 private-sync framing

**What was synced:**
- Rewrote GOVERNANCE.md's core principle (formerly #4, "One-way flow": "Content moves from the private system to the public repo, never the reverse. The private system is the source of truth.") — that described the v1 architecture, superseded by the Aug 9 architecture flip (this repo is now the public base layer; the private Citrix `bmad` system is a downstream, read-only overlay). MAINTAINER.md flagged this exact rewrite as needed back on 2026-08-19 ("is the architectural flip, in product form") but it had never actually been done. Merged the old #4 into a corrected #1 ("Grounded in the public record") since, once the flow-direction claim is gone, it says nothing #1 didn't already cover — 6 principles became 5.
- Removed the opening paragraph's claim that "the sync skills in my private knowledge system reference this document as the authoritative source for publishing decisions," and the closing "sync procedures in the private system implement these rules procedurally" line — both tied this public doc's authority to private-system mechanics that shouldn't be the public doc's concern.
- Removed the "Private system artifacts" never-allowed subsection and the entire "Requires careful filtering" section (the `developing-thinking.md`/frameworks manual-review-on-sync guidance) — both described the mechanics of filtering content on the way in from the private system. Brian's call: that's the private brain's job to document and enforce, not something the public governance doc should describe. The remaining doc-agnostic safety rules (no internal strategy, no people, no competitive intel, no credentials, no legal exposure) already cover what actually must never appear here, regardless of where content originates.
- Bumped "Last reviewed" from 2026-02-23 (predates even the Aug 9 architecture decision) to 2026-08-24.

**Automated checks:**
- Not applicable in the usual sense — this is a governance-doc rewrite, not new canon content moving through the pipeline. Full diff reviewed manually instead.
- `[[` wiki-links: none introduced — CLEAR
- Internal names/`bmad/` paths: none introduced (if anything, this removed the file's own remaining private-system references) — CLEAR

**Manual review notes:**
- Philosophy/scope correction, not new content — no third-party material, no internal strategy, no people involved.
- Scoped by Brian directly across two rounds of confirmation this session: the principle rewrite approved first, then the two remaining sync-flavored sections flagged separately and approved for removal.
- `docs/brianmadden-ai-v2-architecture-and-launch-plan.md` and `MAINTAINER.md` were not touched this pass — this entry covers `GOVERNANCE.md` only.

**Result: CLEAR TO COMMIT**

---

## 2026-08-15 — Open decision #8 residuals: front-of-mind pointer list + staleness-triage tool

**What was synced:**
- Added a `## Right now` section near the top of `me/developing-thinking.md` — a small, manually-curated 3-5 item pointer list (currently: the knowledge factory, the three waves) linking down to the relevant big-argument sections, replacing the ad hoc inline "most front-and-center" markers added 2026-08-14. Brian's chosen design (asked directly, chose the curated-pointer-list option over a per-item tag convention) for the "front-of-mind vs. background" tracking piece of open decision #8. Bumped the file's `updated` frontmatter/body dates and `_index.json` word count (7351 → 7439) to match.
- Built `skills/triage/` (new skill: `triage.py`, `prompt.md`, `README.md`) — the recurring staleness-triage tool, the other open-decision-#8 residual. One LLM call (`claude-opus-5`, Brian's steer: LLM-assisted judgment against canon rather than a deterministic grep pass) cross-checks `developing-thinking.md`'s "What's connecting"/"Scratchpad" sections and every active framework against `me/published-thinking.md`, flagging only items that are `already-published`, `promote-candidate`, or `worth-revisiting` — mirror image of `promotion-candidates.md` (that queue proposes additions to canon, this one proposes cuts/promotions/second looks). Writes `outputs/canon-triage/staleness-candidates.md`, overwritten fresh each run, never auto-editing canon.
- Ran it for real against the live repo (not just `--dry-run`): 6 developing-thinking items + 1 framework flagged out of ~90/10 candidates — in the target range set by the 2026-08-14 manual pass's hit rate. First real output committed for audit.
- Updated `outputs/README.md` (new `canon-triage/` subdirectory entry), `CLAUDE.md`/`AGENTS.md` (added `triage` to the `skills/` tree comment, identical pair).

**Automated checks:**
- `python3 scripts/check_doc_accuracy.py`: OK, 0 warnings — CLEAR
- Wiki-links (`[[`): none found in changed/new files — CLEAR
- Internal names (David Jack, Nancy, Hector, Rahul, George, Thomas, Jen, Sridhar, internal product names): none found — CLEAR
- bmad/ path references: none found — CLEAR
- Spaced em-dashes in canon prose (`me/developing-thinking.md`'s new section): none found — CLEAR (skill READMEs and the triage tool's own generated audit doc are maintainer-facing/internal, not Brian's-voice canon prose, so the style-guide rule doesn't bind them — same convention as `MAINTAINER.md`/`BUILD.md`)
- Heading case on the new `## Right now` section: sentence case — CLEAR
- JSON validity (`_index.json`): valid — CLEAR

**Manual review notes:**
- No new public-safety-sensitive content — the new `developing-thinking.md` section is pointer text linking to already-public sections; the triage tool's output is Brian's own published work cross-referenced against his own developing thinking, no third-party or confidential material involved.
- `outputs/canon-triage/staleness-candidates.md` is machine judgment only (`status: not-reviewed-by-human`, `authority_level: 1`) — nothing in it has been actioned; it's queued for Brian's review same as `promotion-candidates.md` always has been.
- Observed non-determinism between the `--dry-run` and the real run (1 vs. 2 frameworks flagged, one run apart) — documented as a known limitation in `skills/triage/README.md` rather than treated as a bug.

**Result: CLEAR TO COMMIT**

---

## 2026-08-05 — Add missing delegation-not-automation framework; update voice.md

**What was synced:**
- Created `frameworks/delegation-not-automation.md` — a framework that had been authoritative in the private source since March, referenced by both the December 2025 and February 2026 blog posts it's built from, but never actually published here as a standalone explainer
- Updated `_index.json`, `_relationships.json`, `COLLECTIONS.md` for the new framework entry
- Updated `README.md`, `CLAUDE.md`, `AGENTS.md`, `llms.txt` (framework count 9 → 10)
- Updated `me/voice.md`: added the "substrate"/"corpus" word-avoidance rule and the "median slop" phrase — both real rules that existed privately but had never made it into the public voice guide (frozen since this repo's launch)

**Automated checks:**
- Wiki-links (`[[`): none found — CLEAR
- Internal names: none found — CLEAR
- bmad/ path references: none found — CLEAR
- Em-dashes: no inline `---`/`--` substitutions — CLEAR
- Heading case: sentence case throughout — CLEAR
- JSON validity: both `_index.json` and `_relationships.json` parse — CLEAR

**Tone checks:**
- Colleague test: CLEAR
- Competitor test: CLEAR — no competitive content
- Journalist test: CLEAR
- Fossil record test: CLEAR — framework is dated to its original December 2025 post
- Register test: CLEAR

**Manual review notes:**
- One line in the source material referenced an internal work example (a prep-task deadline) as an illustration inside the framework's skills-hierarchy walkthrough — replaced with a generic example before publishing. Everything else is a direct copy.
- `me/voice.md` had drifted from the private version since this repo's launch; only added the two substantive rules, left the rest of the file's structure and register as-is rather than overwriting a deliberate earlier edit.

**Result: CLEAR TO COMMIT**

---

## 2026-08-05 — Sync developing-thinking.md: two-month backlog (June 1 → August 5)

**What was synced:**
- Updated `me/developing-thinking.md` with 9 new frontier-thinking items and updated token-consumption numbers in the compute-scarcity argument (word count 8,045 → 8,946; last public update was June 1)
- Updated `_index.json` (file entry word count, generated date, total_words 237,026 → 237,927)
- Updated `llms.txt` (version v3.5 → v3.6, word count, date)

**Automated checks:**
- Wiki-links (`[[`): none found — CLEAR
- Internal names: none found — CLEAR
- bmad/ path references: none found — CLEAR
- Em-dashes: no inline `---`/`--` substitutions — CLEAR
- Heading case: sentence case throughout — CLEAR
- JSON validity: `_index.json` parses — CLEAR

**Tone checks:**
- Colleague test: CLEAR — no identifiable colleague in the added material
- Competitor test: CLEAR — nothing added is competitive positioning
- Journalist test: CLEAR — no quotable line creates a problem
- Fossil record test: CLEAR — all additions are frontier/developing, not framed as settled
- Register test: CLEAR — reads as public frontier thinking

**Manual review notes:**
- This closes a real two-month gap in the public frontier file. Most of the private source material from the same window was Citrix-internal and correctly excluded — the public-safe yield (9 items) was smaller than the raw private volume, which is expected and by design, not a sign of thin content.
- New items: the distinction between AI reconstructing what versus why, one corpus/many renders, second-brain selection bias (already public via a prior talk), session recording's privacy asymmetry for agents, the "leave a PDF" consulting model, the "one step ahead" mechanism of AI skepticism, the PC deployment analogy for shared knowledge systems, and hallucination's two root causes.

**Result: CLEAR TO COMMIT**

---

## 2026-07-22 — New talk: What is a worker in 2031? (Arrow Forum 2026)

**What was synced:**
- Created `talks/2026-07-16-arrow-forum-what-is-a-worker-in-2031.md` — public talk record, reconstructed from the slide deck (no recording exists). Stripped of wiki-links, internal file paths, and the internal editorial "inference flags" section that appears in the private bmad copy
- Updated `talks/index.md` (added entry at top of Available content)
- Updated `_index.json` (added talk entry; total_files 118→119, total_words 235225→237026)
- Updated `COLLECTIONS.md` (added the talk to Enterprise AI strategy, AI agents / post-application era, Knowledge work and the invisible 80%, Human-AI collaboration; also added the 2026-07-20 bubble-pop blog post to Enterprise AI strategy, which the prior sync had missed)
- Updated `llms.txt` (119 files, ~237k words, 20 talks)
- Updated `README.md` (19→20 speech/podcast transcripts)

**Automated checks:**
- Wiki-links (`[[`): none — CLEAR
- Internal names: none in new content. Only "Dave Brear" appears (public podcast co-host, pre-existing line in talks/index.md) — CLEAR
- Internal path leaks (handoff/, me/thinking, reference/speeches, work/arcs, govern-dont-build): none in the public talk file — CLEAR
- Em-dashes: no inline `--`/`---` (only YAML frontmatter delimiters); prose uses spaced em-dashes consistent with other public talks — CLEAR
- Heading case: sentence case throughout — CLEAR
- JSON validity: `_index.json` parses — CLEAR

**Tone checks:**
- Colleague test: public-facing keynote content, consistent with Brian's published voice
- Competitor test: names vendors (Palantir, OpenAI, Anthropic, AWS, Microsoft) only in the context of publicly reported FDE investments — no disparagement, no non-public claims — CLEAR
- Journalist test: no internal Citrix strategy; the Citrix content is the EUC-primitive audit already public in the EUCTech/DanofficeIT talks — CLEAR
- Fossil record test: the model-name and news-headline timeline is explicitly dated to the talk (July 16, 2026); accurate as of then. The "reconstructed from slides" provenance is stated in frontmatter so future readers know it's not a verbatim transcript
- Register test: keynote-summary register, consistent with the other reconstructed/summarized talk records

**Manual review notes:**
- This is a reconstruction from the slide deck, not a transcript. The private bmad copy carries explicit inference flags (the FDE-as-80%-extraction reading, connective transitions, audience descriptor); the public copy omits the editorial flags but keeps the honest "reconstructed from slides; no recording" provenance in frontmatter and the intro
- All company/model/dollar figures come directly from the slides
- No bmad.com website pieces done in this pass (no video recording exists): no `_content-index.json` speech entry, no bmad.com talk page, no R2 slide upload, no speaking-page video card. Held pending Brian's decision on whether to surface a recording-less talk on the site

**Result: CLEAR TO COMMIT**

---

## 2026-07-22 — New blog post: How to build an AI strategy that survives the bubble pop

**What was synced:**
- Created `posts/citrix-blog/2026-07-20-how-to-build-an-ai-strategy-that-survives-the-bubble-pop.md` (full post text, published 2026-07-20)
- Updated `posts/citrix-blog/index.md` (added #37, count 36→37, date range → July 2026)
- Updated `me/published-thinking.md` (added "Plan for the invariants, not the bubble" key argument, July 20 post-by-post note, "New signature phrases (July 2026)" section, date/count → 41 posts / July 20 2026)
- Updated `_content-index.json` (added blog entry at top, newest first)
- Updated `_index.json` (added file entry; total_files 117→118, total_words 233459→235225, generated → 2026-07-22)
- Updated `llms.txt` (version line: 112→118 files, ~200k→~235k words, 57→58 posts, date → 2026-07-22)
- Updated `README.md` (36→37 Citrix blog posts)
- Updated `CLAUDE.md` and `AGENTS.md` (37 blog posts, Apr 2025–July 2026; kept the two files identical except the self-reference line)

**Automated checks:**
- Wiki-links (`[[`): none found — CLEAR
- Internal names (Nancy, Hector, Sridhar, Saikat, Abhilash, Kireeti, etc.): none found. Only "Dave Brear" appears (public podcast co-host, in pre-existing EP entries) — CLEAR
- bmad/ path references: none (grep hits were the `second-brain` tag and blog URL slugs, not filesystem paths) — CLEAR
- Em-dashes: no inline `---`/`--`; new post uses colons and parentheses per Brian's style — CLEAR
- Heading case: sentence case throughout — CLEAR
- JSON validity: `_index.json` and `_content-index.json` both parse — CLEAR

**Tone checks:**
- Colleague test: public-facing, consistent with Brian's published voice
- Competitor test: no competitive positioning that would embarrass — CLEAR
- Journalist test: no unpublished Citrix strategy; content is the published blog post — CLEAR
- Fossil record test: model names and open-weight landscape are timestamped to the post's publish date; accurate as of then
- Register test: direct and plainspoken, consistent with other blog posts

**Manual review notes:**
- The post is already published on citrix.com; this sync mirrors public content
- New public argument: open-weight models as the reliable planning floor + the invariants-based do-now checklist. Consistent with the June 30 futurist post and the compute-scarcity/token-routing thesis already on the record
- "corpus" appears once in the post body — preserved because it's the author's published wording (the internal voice rule against "corpus" governs new writing, not faithful archival of published posts)

**Result: CLEAR TO COMMIT**

---

## 2026-06-30 — Documentation accuracy audit and fix

**What was synced:**
- Fixed `posts/citrix-blog/index.md`: header claimed 37 posts but the numbering had a gap (jumped 25 → 23, skipping #24), leaving only 36 actual entries. Renumbered #25–37 down to #24–36 so numbering is contiguous 1–36, matching the 36 files on disk. Fixed header count 37 → 36.
- Removed `delegation-not-automation` — a framework that was referenced as a real file in `CLAUDE.md`, `AGENTS.md`, `llms.txt`, `_index.json` (4 entries), and `_relationships.json`, and in the `related_frameworks` frontmatter of `frameworks/cognitive-stack.md` and `posts/citrix-blog/2026-02-25-cognitive-stack.md` — but `frameworks/delegation-not-automation.md` never existed. The idea was folded into `frameworks/cognitive-stack.md` (which still credits it in prose: "Extends: the delegation-not-automation thesis"), but the phantom file reference was never cleaned up. Removed it everywhere it pointed at a nonexistent file; kept the prose credit.
- Removed `enterprise-invariants` from the `related_frameworks` frontmatter of `posts/citrix-blog/2026-04-09-whats-left-for-humans.md` and the matching `_index.json` entry — same phantom-reference bug, caught by the new CI check below. `frameworks/enterprise-invariants.md` never existed; left it in the post's `tags` array since that's a legitimate topical tag, not a file link.
- Updated `CLAUDE.md` and `AGENTS.md`: fixed stale Citrix post count (37 → 36) and framework count (10 → 9, since the tree listed the phantom `delegation-not-automation.md`); added missing top-level entries to the repo-structure tree (`GOVERNANCE.md`, `governance-log.md`, `_content-index.json`, `podcast/`) and missing `me/` files (`books.md`, `links.md`).
- Updated `README.md`: fixed Citrix post count (37 → 36) and talk count (18 → 19); dropped an unverifiable "3 external articles" claim that didn't correspond to anything in the repo.
- Updated `llms.txt`: removed the phantom `delegation-not-automation` framework entry; fixed Citrix post count (31 → 36, two places); fixed talk count (18 → 19); added missing references to `podcast/index.md`, `GOVERNANCE.md`, `governance-log.md`, `_content-index.json`, `AGENTS.md`, `me/books.md`, `me/links.md`.
- Added `scripts/check_doc_accuracy.py` and `.github/workflows/check-docs.yml` — a CI check that runs on every push/PR to catch this category of drift automatically (post-count mismatches, numbering gaps, phantom framework references, repo-structure-tree omissions). See script docstring for what it checks.
- Updated `GOVERNANCE.md`'s automated-checks section to reference the new CI check.

**Automated checks:**
- Wiki-links (`[[`): none found — CLEAR
- Internal names: none found — CLEAR
- bmad/ path references: none found — CLEAR
- This was a documentation-accuracy pass, not new content — no tone/register checks apply

**Manual review notes:**
- Triggered by a manual audit request, not a content sync. No new ideas or positions were added; this only corrects counts, a numbering bug, and a dangling file reference to match what's actually in the repo.
- The numbering gap at #24 in `posts/citrix-blog/index.md` predates this fix and isn't explained by any git history of a deleted post — appears to be a manual-edit slip that was never caught.

**Result: CLEAR TO COMMIT**

---

## 2026-06-30 — New blog post: How a futurist reads AI news

**What was synced:**
- Created `posts/citrix-blog/2026-06-30-how-a-futurist-reads-ai-news.md` (full post text, frontmatter with authority/file_type/staleness/tags)
- Updated `posts/citrix-blog/index.md` (added entry #37, bumped header count 36 → 37)
- Updated `me/published-thinking.md` (added June 30 entry to post-by-post notes, added missing June 10 entry, added "Section 9. New signature phrases (June 2026)", bumped header count 38 → 40, updated date/description)
- Updated `_index.json` (added new post file entry, total_files 111 → 112, total_words 198520 → 200125, generated → 2026-06-30)
- Updated `_content-index.json` (added blog card for bmad.com homepage)
- Updated `llms.txt` (files 111 → 112, posts 56 → 57, date → 2026-06-30)
- Updated `README.md` (Citrix blog posts 35 → 37)
- Updated `CLAUDE.md` and `AGENTS.md` (35 → 37 Citrix blog posts, date range May 2026 → June 2026)

**Automated checks:**
- Wiki-links (`[[`) in new post: none found — CLEAR
- Internal names (Nancy, Hector, Sridhar, Aidrien, Kireeti, David Jack, Saikat, Brian Hune, Eltjo, Komal): none found — CLEAR
- bmad/ path references in new post: none found — CLEAR
- Spaced/triple em-dashes (`---`, ` — `): none found in body — CLEAR (only frontmatter `---` delimiters present)
- Heading case: sentence case throughout — CLEAR

**Tone checks:**
- Colleague test: published Citrix blog post; consistent with Brian's published voice — CLEAR
- Competitor test: no competitive positioning that would embarrass — CLEAR
- Journalist test: no unpublished strategy; the futurist methodology is the explicit subject — CLEAR
- Fossil record test: accurate as of publish date
- Register test: conversational explanatory register, consistent with other blog posts

**Manual review notes:**
- Post is the externalization of methodology Brian has used internally for years; first time it's been published
- Three diagram placeholders preserved as `*[Diagram: ...]*` notes (images were on the live blog but not pasted into the source)
- Explicitly references and extends the April 9 *What's left for humans?* post (Bezos invariants)
- Cross-references the Citrix AI Hotsheet EP 3 (the one-stage-ahead point from the podcast)
- Added missing June 10 7-stage roadmap entry to bmad reference index and brianmadden-ai published-thinking — these had been omitted in prior syncs and the count was drifting

**Result: CLEAR TO COMMIT**

---

## 2026-06-14 — New podcast EP 2 + keynote: The Last Chapter of EUC

**What was synced:**
- Created `podcast/ep2.md` (Citrix AI Hotsheet EP 2 — special solo edition, the EUCTech keynote: metadata, subscription links, description, topics, full transcript)
- Created `talks/2026-06-03-euctech-the-last-chapter-of-euc.md` (standalone narrative-arc talk record)
- Updated `podcast/index.md` (EP 2 entry) and `talks/index.md` (added to Available content; removed the two now-past EUCTech rows from Upcoming/accepted)
- Updated `COLLECTIONS.md` (added EP 2 and the talk to AI agents / post-application era, knowledge work / invisible 80%, human-AI collaboration, second brains collections)
- Updated `_index.json` (added the talk entry; total_files 109→110, total_words 197308→198520, generated → 2026-06-14). Podcast episode files are not tracked in `_index.json` (consistent with ep1.md).
- Updated `_content-index.json` (added EP 2 podcast card and the keynote speech card for bmad.com homepage)
- Updated `README.md` and `llms.txt` stats (talks 15→18, files/words refreshed to match `_index.json`, frameworks corrected 10→9 in llms.txt, version v3.3→v3.4, date → 2026-06-14)

**Automated checks:**
- Wiki-links (`[[`): none found — CLEAR
- Internal names (Nancy, Hector, Sridhar, Aidrien, Kireeti, Abhilash, Eltjo, Kevin Nardone): none found — CLEAR (genericized "Aidrien" → "the AI that helps me interface with my Citrix environment" and "Nancy" → "my coworker/my manager" in the public transcript)
- bmad/ path references: none found — CLEAR
- Spaced/triple em-dashes: none found — CLEAR
- Heading case: sentence case throughout — CLEAR

**Tone checks:**
- Colleague test: content is a publicly-delivered keynote and a publicly-released podcast; consistent with Brian's published voice — CLEAR
- Competitor test: no competitive positioning that would embarrass; Microsoft/AI labs referenced only as in published work — CLEAR
- Journalist test: no unpublished Citrix strategy; the EUC-audit primitives are Brian's public framing — CLEAR
- Fossil record test: accurate as of publish date
- Register test: conversational keynote register, consistent with other talk/podcast transcripts

**Manual review notes:**
- EP 2 is the EUCTech keynote, already delivered publicly (June 3) and released as a podcast (June 13) on YouTube/Apple/Spotify/Riverside — fully public content
- The transcript was lightly cleaned for readability (transcription garbles, punctuation) without changing substance
- "OpenClaw" reference kept (real, ties to the published OpenClaw governance post); "Claude Fable / Mythos" model names kept per author confirmation

**Result: CLEAR TO COMMIT**

---

## 2026-06-14 — Update 7-stage roadmap framework explainer to 2026 edition

**What was synced:**
- Rewrote `frameworks/7-stage-roadmap.md` to the 2026 edition stages (Faster Search → Thinking Partner → Cognitive Extension → Multi-Tool Agent → Fleet → Pod → Published Self). The 2026 blog post and synthesis.md were already synced on 2026-06-10; the standalone framework explainer was the remaining stale artifact still showing the June 2025 stages.
- Updated frontmatter: title → "(2026 Edition)", date 2025-06-24 → 2026-06-10, original_url → 2026 post, tags expanded, related_frameworks now includes cognitive-stack, related_posts now lists the 2026 post first.
- Updated `_index.json`: framework entry (title, date, word_count 416→990, tags, related_posts, description); repo totals (total_words 196734→197308, generated → 2026-06-12).
- Updated `_relationships.json`: framework title, original_url, referenced_in_posts and referenced_by_posts now include 2026-06-10-the-7-stage-roadmap-2026-edition; added cognitive-stack to related_frameworks.
- Updated `llms.txt`: one-line framework description.

**Automated checks:**
- Wiki-links (`[[`): none found — CLEAR
- Internal names (Nancy, Hector, Sridhar, Neha, Harit, etc.): none found — CLEAR
- bmad/ path references: none found — CLEAR
- Spaced/triple em-dashes (` --- `, ` -- `): none found — CLEAR
- Heading case: sentence case throughout — CLEAR
- JSON validity (`_index.json`, `_relationships.json`): both parse — CLEAR

**Tone checks:**
- Colleague test: standalone explainer of an already-published public framework; consistent with Brian's voice
- Competitor test: no competitive positioning that would embarrass — CLEAR
- Journalist test: no unpublished Citrix strategy; all content derives from the published June 10 post — CLEAR
- Fossil record test: explicitly versioned (2026 Edition supersedes 2025), with lineage section preserving the self-correction history
- Register test: direct and conversational, consistent with other framework explainers

**Manual review notes:**
- Content is a faithful standalone rewrite of the published 2026 post; no new claims introduced
- bmad.com `/frameworks` page and homepage cards regenerate from `_index.json` at build time, so the public site picks this up on next deploy with no server-repo edit needed
- The 2025 post entry was left intact in `_content-index.json` as a correct historical record

**Result: CLEAR TO COMMIT**

---

## 2026-06-10 — New podcast: The Future of Less Work (June 1, 2026)

**What was synced:**
- Created `talks/2026-06-01-future-of-less-work-ai-brain-resume.md`
- Updated `talks/index.md`
- Updated `_content-index.json`
- Updated `_index.json` (total_files 106→107, total_words 193634→194834)

**Automated checks:**
- Wiki-links (`[[`): none found — CLEAR
- Internal names (Nancy, Hector, Sridhar, etc.): none found — CLEAR
- bmad/ path references: none found — CLEAR
- Spaced em-dashes (` --- `, ` -- `): none found — CLEAR
- Heading case: sentence case throughout — CLEAR

**Tone checks:**
- Colleague test: content is public-facing and consistent with Brian's published voice
- Competitor test: no competitive positioning that would embarrass — CLEAR
- Journalist test: no unpublished claims about Citrix strategy — CLEAR
- Fossil record test: content is timely and accurate as of publish date
- Register test: conversational and direct, consistent with other podcast transcripts

**Manual review notes:**
- Episode is entirely public content; no internal Citrix strategy or confidential information
- The "company keeps your brain" inverse labor threat is a new public articulation consistent with Brian's published consumerization thesis
- Joy/satisfaction calibration framing is new and personal — public-safe
- Subscribable brains mention references brianmadden.ai directly — appropriate

**Result: CLEAR TO COMMIT**

---

## 2026-08-14 — Canon governance pass: five-levels archived, knowledge factory + three waves enter canon

**What was synced:**
- Archived `frameworks/five-levels-of-ai-in-knowledge-work.md` (`status: archived`, first use of the mechanism added to `docs/frontmatter-schema.md` this same session) — Brian's direct call, "that wasn't really mine" (adapted from Dan Shapiro's coding framework)
- Removed two already-published blocks from `me/developing-thinking.md` (7 Phases v2, EUC primitives audit — both published 2026-06-10 as the 7-stage-roadmap 2026 Edition / delivered in the June talks)
- Added two new big-argument sections to `me/developing-thinking.md`: "The knowledge factory" and "The three waves" — distilled from Brian's unpublished working material at his direction; absorbed four Aug-5 scratchpad items into them; rewrote one open question as answered
- Created `frameworks/knowledge-factory.md` (`status: not-reviewed-by-human`, `model: claude-fable-5`, `original_url: null` — first framework to enter canon before publication)
- Updated: CLAUDE.md/AGENTS.md (identical pair), README.md, llms.txt (v3.8: 121 files, 10 active frameworks), COLLECTIONS.md (3 collections), `_index.json`, `_relationships.json`, `scripts/check_doc_accuracy.py` (archived-tier support + fixed a silently-broken tree check)

**Automated checks:**
- `python3 scripts/check_doc_accuracy.py`: OK, 0 warnings — CLEAR
- Wiki-links (`[[`): none found — CLEAR
- Internal names (David Jack, Nancy, Hector, Rahul, George, Thomas, Jen, Sridhar, internal product names): none found in new canon content — CLEAR
- bmad/ path references: none found — CLEAR
- Spaced em-dashes (` — `, ` -- `): none found in new content — CLEAR
- Heading case: sentence case throughout — CLEAR
- JSON validity (`_index.json`, `_relationships.json`): both valid — CLEAR

**Manual review notes (redaction decisions):**
- Source material: the knowledge-factory explainer (Brian: "essentially ok to be public") and the three-waves doc (Citrix internal; Brian explicitly wants the *concept* public, not the Citrix specifics)
- Continuity check ran first: "knowledge factory" as a term, the org-scale concept, and the full FDE funding story were already public canon (2026-07-20 bubble-pop post, 2026-07-16 Arrow Forum talk, podcast ep3-4) — the new content extends the public record
- **Brian's correction, same session, applied:** internal-usage specifics removed from the public proof point — the ~$50-per-course figure, the 140+ block count, the department, the use case (training content), and the exact replication count. Public canon now says only: Citrix runs the pattern internally, built by one person as an in-house FDE, in production within months, replicated multiple times. The concept is public; how Citrix uses it is not.
- Excluded throughout: all individual names (builder uncredited pending Brian's call), internal product/program names, org headcounts, the internal Wave-1 marketing label, all Citrix product-pillar mapping, all competitive positioning, everything from the marketing-factory proposal doc (per Brian: background only)
- The FDE funding figures and OpenAI build-out math are public reporting, already cited in the Arrow Forum talk

**Same session — the full developing-thinking.md triage executed with Brian's approval:** 55 items cut (30 what's-connecting paragraphs, 25 scratchpad bullets), grouped as: absorbed into the two new sections; already published in canon elsewhere (verified by grep before cutting); dated market/news snapshots; one-liners that went nowhere. One item ("lead with problems, not architecture") moved into `me/voice.md`'s "How Brian argues" section rather than cut — flagged as the one edit touching MAINTAINER.md rule 7 territory (voice.md edits are Brian's), needs his explicit eyes. File went ~9,000 → ~7,400 words with the two major new arguments in and 55 stale items out. Everything removed remains in git history.

**Brian's review, same session:** two final corrections applied — all "course" references generalized to deliverable-neutral wording, and the proof point cut to "Citrix runs this pattern internally," full stop (the concept's use at Citrix is public; how it's used is not). With those in, Brian approved everything for commit and publication; `frameworks/knowledge-factory.md` flipped to `status: reviewed` on his in-chat approval, indexes synced. `skills/brief/brief.py` also gained an archived-status filter so retired frameworks never inform future briefs.

**Result: CLEAR TO COMMIT** — committed at session end, all files, logical commits.

---

## 2026-08-24 — Weekly Update ceremony built (BUILD.md open decision #13)

**What was synced (process change, not canon content):**
- New skill `.claude/skills/weekly-update/SKILL.md` (`/weekly-update`) — a
  live ceremony (not an unattended pipeline) that recaps the week's daily
  briefs, walks the `promotion-candidates.md` and `staleness-candidates.md`
  queues to a real decision on each entry, captures Brian's own takeaways,
  and drafts a dual-byline (`brianmadden.ai` + Brian Madden) Weekly Update.
  Reuses `review-thinking`'s developing-thinking.md mechanics rather than
  duplicating them.
- New `skills/weekly/render.py` — Substack-paste HTML rendering, reusing
  `skills/brief/render.py`'s generic helpers; own disclosure line/footer
  for the dual byline (the Daily Brief's AI-solo disclosure doesn't fit).
- New output location `outputs/weekly-updates/` (`outputs/README.md`
  updated) and `.gitignore` entry for its rendered HTML.
- New frontmatter field `last_reviewed` on `me/developing-thinking.md`
  (documented in `docs/frontmatter-schema.md`) — distinct from `updated`,
  bumped by the ceremony every run regardless of whether content changed,
  so a review with no edits still leaves a real timestamp.
- Closed the open Substack-placement question in `docs/substack-as-primary-home.md`
  Workstream E: dual byline, folds into the existing structure for now
  (no new Section yet) — both asked directly and answered by Brian this
  session.
- `BUILD.md` open decision #13 marked built.

**No canon content (`me/`, `frameworks/`, `posts/`) was touched by this
entry** — this is process/pipeline scaffolding, logged per MAINTAINER.md's
"every change to the publishing process gets an entry" rule, same as any
other skill build. The first live run of the ceremony (if it happens this
session) — including any actual `developing-thinking.md` edits, framework
archivals, or promotion-candidates resolutions Brian makes during it — gets
its own separate entry, since that run touches real canon content and
needs its own manual-review-notes discipline.

**Automated checks:** N/A — no canon content changed. `python3 -c` smoke
test confirmed `skills/weekly/render.py`'s import chain against
`skills/brief/render.py` resolves correctly.

**Result: CLEAR TO COMMIT**

---

## 2026-08-24 — First live Weekly Update ceremony (20-item promotion-candidates backlog cleared, 9-item staleness queue resolved)

**What was synced:**
- `outputs/technical-briefings/promotion-candidates.md`: 20 entries → 1 (intentionally held, pending a write-up decision it depends on). Applied live, item by item, with Brian's decision on each: 4 threads consolidated into one `developing-thinking.md` entry (shared artifacts as the undetected agent-to-agent channel — the same evidence had been tracked under four separate names, a real gap in the pipeline's exact-slug thread matching, flagged as a follow-up); 3 threads consolidated into a second entry at Brian's own framing ("labs control every lever — what exists, what's free, what it costs, how well it runs"); 5 threads promoted as their own entries (routing-seat-to-payments, personalization-in-weights-vs-files, deployer-opacity, human-approval-worse-than-automated-policy, open-ended-research-failure-shape) — two of these carry direct extensions in Brian's own words (the OSS/startup routing layer; the Chinese-model-censorship "what else is hidden" point, tied to Meta/NVIDIA/non-Chinese open weights); 1 thread's disposition (public/political legitimacy as a compute constraint) resolved as a supporting addition to the existing "Compute scarcity and token governance" section rather than a standalone entry, per Brian's own question about where "real but not novel" facts belong — precedent drawn from the 2026-08-14 triage's "dated market/news snapshot" cut-reason; 2 threads folded as one-line notes into existing sections ("The cognitive stack," "The 2031 worker-shape forecast"); 2 threads dropped with no canon addition (Brian: "meh… whatever you think"); 1 thread held open, tied to an unresolved staleness item (see below).
- `me/developing-thinking.md`: content added/cut per the above, plus the staleness-queue decisions — 4 items cut (already-published elsewhere: the AI-stack cost-tier argument, the MCP-server line, "secure the work, not the worker," most of the skills-training argument, with its authoring-recipe residual kept as a separate scratchpad line), 3 items left as-is with a "promote" decision logged as a follow-up writing task rather than drafted inline (human clock speed as the invariant; the second-brain selection-bias failure mode; "you can only see one step ahead") — the human-clock-speed one also resolves the last open promotion-candidate, since `machine-speed-vs-human-absorption` is its evidence base, not a separate thread. `## Right now` updated with three new front-of-mind items (Chinese-model risk, harness-vs-model, distributed/local models and Wave 3 timing), `updated`/`last_reviewed` frontmatter bumped to 2026-08-24, `status` → `reviewed-and-updated` (Brian live for every edit).
- `frameworks/bitter-lesson.md` and `frameworks/post-application-era.md`: both revised (not archived), per the staleness queue's "worth-revisiting" flags — bitter-lesson's "AI dissolves the 80%" claim corrected against the knowledge-factory framework's own stated revision of it; post-application-era's unbounded stage-4 ending qualified with the three-tier/"UIs not systems of record" formulation from the April SaaSpocalypse post. Both `status` → `reviewed-and-updated`.
- New output: `outputs/weekly-updates/2026/08/2026-08-24-prep.md` (the prep doc) and `2026-08-24.md` (the finished dual-byline post, `status: reviewed`), rendered to HTML via `skills/weekly/render.py`. `outputs/weekly-updates/.last_run.json` written for the first time.
- `_index.json`: surgical updates only — `developing-thinking.md`, `bitter-lesson.md`, `post-application-era.md` word counts and `developing-thinking.md`'s `updated` date. No `outputs/` entries needed (confirmed the index doesn't track tier-3 output at all).

**Automated checks:**
- `python3 scripts/check_doc_accuracy.py`: OK, 0 warnings — CLEAR (no framework `status: archived` transitions, so no active-count updates needed elsewhere)
- Wiki-links (`[[`): none found in any touched file — CLEAR
- Internal names: none found — CLEAR
- bmad/ path references: none found — CLEAR
- Spaced em-dashes: **caught and fixed** — every new passage this session was written with spaced em-dashes (` — `), against `me/style-guide.md`'s no-spaces rule. Fixed programmatically across all five touched files before commit. Flagging this plainly since it was a real miss, not a clean pass.
- Inline-code/Substack-rendering rule: **also caught and fixed** — the published Weekly Update post referenced `.md` files in backticks (`promotion-candidates.md` etc.), which `me/style-guide.md`'s Substack-rendering section explicitly says renders oddly and should instead be an italicized real link. Converted all four instances to `*[name.md](github-link)*` before the final render.
- `_index.json` validity: valid JSON, confirmed after the surgical edits — CLEAR
- JSON validity (`outputs/weekly-updates/.last_run.json`): valid — CLEAR

**Manual review notes:**
- Everything added to canon this session traces to public daily-brief content (third-party reporting, already-published Brian posts) or Brian's own direct statements in this conversation — no Citrix-internal or confidential material involved.
- Two framework revisions correct a framework against Brian's own later published position, not against outside material — lower risk than a first-time canon addition, but still logged with the same discipline.
- The "labs control every lever" and "shared artifacts as the channel" consolidations are editorial judgment calls (recognizing that separately-flagged threads were the same story) — flagged to Brian directly before applying, approved live, not inferred silently.

**Result: CLEAR TO COMMIT**

---

## 2026-08-24 — Second round, same session: Deeper Thinking named, prep automated, post restructured

**What was synced (process/product change, not new canon content):** the
publication got a real name (Deeper Thinking, Brian's choice), a new
`skills/weekly/gather.py` automates the deterministic prep-and-email step
on Fridays (wired into `daily-pipeline.yml`, `outputs/weekly-updates/`
and `outputs/canon-triage/` added to that workflow's commit path), and
the finished post was restructured per Brian's direct feedback (honest
story-selection framing, bullets under "What moved in the thinking," a
new "Where my head's at right now" section linking live to
`developing-thinking.md` on GitHub, plain-language rewrites of the
future-post candidates). No `me/developing-thinking.md` or framework
content changed in this round — only the skill (`SKILL.md`), the two
scripts (`gather.py`, `render.py`), and the not-yet-published post file
itself.

**Automated checks:**
- `python3 scripts/check_doc_accuracy.py`: OK, 0 warnings — CLEAR
- `_index.json`, workflow YAML: both valid — CLEAR
- Spaced em-dashes / backtick file-refs: **recurred on this round's
  rewrite** — rewriting the post file fresh (via `Write`, replacing the
  whole file rather than `Edit`ing it) reintroduced both issues already
  fixed once earlier the same session. Fixed the same way, and structural
  root cause addressed too: `render.py` no longer injects a fixed
  disclosure/footer, so there's one less place text gets assembled
  outside the reviewed body going forward.

**Result: CLEAR TO COMMIT**

---

## 2026-08-25 — Source-checking transparency + subtitle empty-response fix

**What was synced (process change, not canon content):**
- `skills/ingest/ingest.py`: every full run now writes
  `ingest/.last_run_sources.json`, one record per registered source
  (`ok`/`error`/`skipped`, with reason and entry counts). No behavior
  change to fetching itself — this only makes existing outcomes
  persistent and visible instead of print-only.
- `skills/brief/brief.py`: new `render_sources_checked_section()`,
  wired into `write_brief()` — every Daily Brief (technical and,
  via `publish.py`'s near-verbatim copy, the Substack-published version)
  now ends with a "Sources checked today" section listing every
  registered source and its outcome, zeros included.
- `skills/brief/publish.py`: subtitle call's `max_tokens` raised
  2048 → 8192 after a real production failure (2026-08-25) — an empty
  response silently fell back to the generic subtitle with only a
  stderr warning, which is how a boilerplate subtitle made it to a
  published post unnoticed.
- Retroactive, one-time fixes to already-committed content:
  `outputs/technical-briefings/2026/08/2026-08-25.md` and
  `outputs/published/2026/08/2026-08-25.md` both patched — the sources-
  checked section added (reconstructed from the real run's GitHub
  Actions log, no live network/Gmail calls involved), and the published
  file's `substack_subtitle` corrected from the generic fallback to a
  real, regenerated one. HTML re-rendered and re-sent to Brian.

**Why:** Brian asked to verify the pipeline was actually checking
everything it's supposed to, after today's briefing looked email-heavy
and its subtitle read as generic boilerplate. Both were real: 39 of 85
registered sources have failed with `403 Forbidden` on every automated
run since launch (2026-08-19), silently, never previously flagged (see
BUILD.md open decision #16) — root cause is very likely Cloudflare
blocking GitHub Actions' IP ranges on Substack's `*.substack.com` feeds,
not a header or code fix on our side; the recommended fix (routing those
publications through the existing `brain@` email path) is real manual
work only Brian can do and is logged, not built, this session. The
subtitle was a genuine empty-response bug, not a prompt-design gap.

**No canon content (`me/`, `frameworks/`, `posts/`) touched.** The two
patched output files are tier-3 (`outputs/`), already `status:
not-reviewed-by-human` — correcting a fallback value and adding a new
section doesn't change that status.

**Automated checks:**
- `python3 -m py_compile` on all three touched scripts: clean
- `python3 scripts/check_doc_accuracy.py`: OK, 0 warnings — CLEAR
- `skills/brief/render.py`'s HTML render tested directly against the new
  section: renders correctly

**Result: CLEAR TO COMMIT** — holding for Brian's go-ahead (not yet
committed).

---

## 2026-08-25 (continued) — Local catch-up run confirms the diagnosis;
maintain skill gains a sync-first step; ffmpeg crash fixed

**What was synced (process changes):**
- `.claude/skills/maintain/SKILL.md`: new step 1, syncing with `origin`
  (fetch, then fast-forward or stash/pull/pop as needed, real judgment
  on any conflict, stop-and-flag if local has unpushed commits) before
  any other bootstrap step. Existing steps renumbered 2-6.
- `skills/ingest/ingest.py`: `_split_audio_for_transcription()`'s
  `subprocess.run()` call for ffmpeg now passes `errors="replace"` —
  ffmpeg's stderr on a real episode contained non-UTF-8 bytes, and
  strict decoding raised `UnicodeDecodeError` *inside* `subprocess.run()`
  itself, a `ValueError` subclass the surrounding `except RuntimeError`
  doesn't catch, crashing the whole ingest run instead of just that one
  episode's transcription.
- Real run, not a dry run: `python3 skills/ingest/ingest.py --since-days
  3`, executed locally (not via GitHub Actions) at Brian's request while
  his Substack-to-email migration (open decision #16) is still
  propagating. Result: 0 of 85 sources failed, vs. 40 on this morning's
  automated run — confirms the block is specific to GitHub Actions' IP
  ranges, not the feeds or the fetch code. 20 new ingest notes written.
- `skills/brief/brief.py` + `skills/brief/publish.py` re-run for real
  against the complete 32-note set (today's original 5 plus the 20 new
  ones), after backing up and removing the morning's thin 5-source
  brief/published-post so the already-briefed dedup wouldn't exclude
  those 5. One new thread crossed the promotion threshold on the fuller
  synthesis (`harness-as-the-named-value-layer`) that the broken run
  would have missed. `update_tracker()`'s existing same-day dedup guard
  prevented any double-count of threads recurring in both syntheses.

**Why:** Direct continuation of this session's earlier finding (39
broken sources). Brian's own fix — subscribing the blocked Substacks to
`brain@` for email delivery — is in motion but not live yet, so he asked
for a local run to backfill the gap now rather than wait days. Confirms
the earlier diagnosis empirically rather than leaving it as a web-search
inference.

**No canon content touched.** `outputs/technical-briefings/2026/08/2026-
08-25.md` and `outputs/published/2026/08/2026-08-25.md` were regenerated
(not hand-edited) — same `status: not-reviewed-by-human` as any other
pipeline output. New `ingest/` notes are Tier 1, machine-written,
never indexed.

**Automated checks:**
- `python3 -m py_compile` on `ingest.py`: clean
- `python3 scripts/check_doc_accuracy.py`: OK, 0 warnings — CLEAR

**Result: CLEAR TO COMMIT** — holding for Brian's go-ahead.

---

## 2026-08-25 (continued again) — Auto-flip feed sources to email on a real match

**What was synced (process change):**
- `skills/ingest/ingest.py`: two new functions,
  `find_feed_source_for_email_sender()` and `flip_source_to_email()`,
  wired in ahead of the existing `auto_register_email_source()` call.
  When a real brain@ email's sender matches an existing feed_url-based
  `sources.yaml` row (by domain or Substack-subdomain heuristic), that
  row is rewritten in place — `feed_url` nulled, `sender` and
  `ingest_method: email` added — rather than registering a lookalike
  duplicate entry. Existing `note`/`lens`/`pov` and every other entry's
  formatting/comments are untouched (targeted line-level edit, not a
  full YAML re-dump).
- `sources/sources.yaml`: header comment gained a dated explanation of
  this mechanism.

**Why:** Direct follow-up to today's 403-blocking finding — Brian's
Substack-to-email migration (open decision #16) means ~39 sources will
start arriving via `brain@` over the next few days. Without this, each
would register as a brand-new, undercurated duplicate row instead of
taking over its existing curated entry.

**No canon content touched.** Pipeline code only.

**Automated checks:**
- `python3 -m py_compile`: clean
- `python3 scripts/check_doc_accuracy.py`: OK, 0 warnings — CLEAR
- Unit-tested directly against a copy of the real `sources.yaml` (not
  the live file): both plausible Substack sender-address shapes matched
  correctly, already-flipped/unrelated senders correctly didn't match,
  resulting YAML parses clean with only the target entry's three lines
  changed, file-end boundary case verified. Not yet exercised against a
  real inbound email — none of the new subscriptions have started
  delivering yet.

**Result: CLEAR TO COMMIT** — holding for Brian's go-ahead.

## 2026-08-26 — Brief-prose fixes, brief.py default model switch, X
timeline live, Substack self-ingestion loop closed

**What was synced (process/product changes, not new canon content):**
- `me/style-guide.md` and `me/voice.md`: scoped the Aug 16 bold-slug
  rule to the tracked-threads bullet list only (it had been bleeding
  into ordinary prose since Aug 17), and added guidance against
  rhetorical-scaffolding tics and stacked-clause sentence density —
  both flagged directly by Brian reading a real published issue.
- `skills/brief/brief.py`: `DEFAULT_MODEL` switched from
  `claude-opus-5` to `claude-sonnet-5` after a real same-batch,
  same-prompt comparison (Sonnet: zero flourish artifacts, ~35%
  shorter, cheaper). Also added a relevance-lens and brevity
  instruction to `prompt.md` at Brian's direction — favor
  enterprise-adoption/governance/workforce angles over AI-industry
  gossip, and let a thin day read thin rather than padding.
- `skills/ingest/ingest.py`: fixed a real bug (Substack's email
  template links via "READ IN APP" through an `open.substack.com`
  interstitial, which `_find_view_online_link()`'s regex didn't
  recognize — every brain@-routed Substack note had no source link as
  a result) and closed a self-referential ingestion loop (`brain@` was
  a subscriber to the `brianmaddenai` publication's own outgoing mail,
  so every real publish fed the next day's synthesis as if it were
  third-party material — excluded that one sender structurally).
- `sources/sources.yaml`: the auto-registered row for that self-mail
  sender marked `priority: excluded` with the reasoning kept for
  the record.

**Why:** Brian read a real published issue and flagged the prose as
"too AI, too try-hardy" and the pipeline's coverage as possibly
incomplete. Both turned out to be real, evidenced findings, not
misreadings — see `BUILD.md`'s 2026-08-26 entries for the full
diagnostic trail (live Gmail HTML inspection for the link bug, a real
side-by-side model comparison for the prose fix, a live Megaphone-feed
check that ruled out a podcast-coverage bug).

**No canon content touched.** Pipeline code, prompts, and today's
regenerated Daily Brief only.

**Automated checks:** `python3 -m py_compile` clean on every touched
script; `python3 scripts/check_doc_accuracy.py` clean; a YAML parse
check on `sources.yaml` after the manual edit.

**Result: COMMITTED AND PUSHED** — Brian confirmed each step live in
session (fix, regenerate, recommit, push), not held for later review.

---

## 2026-08-28 — Daily Brief section rename, thread-list trimmed,
same-vs-related-incident dedup guidance; local-source pull tested against
X and blocked Substack feeds

**What was synced (process/product changes, not new canon content):**
- `skills/brief/prompt.md`: renamed "Worth Brian's attention" to "What
  this changes" and redefined its job — 0-4 items, zero is correct,
  only include something that asks a decision, reply, or plan-change of
  Brian specifically, not a re-ranking of the sections above it. Added
  explicit guidance for citing a recurring thread: say whether new
  material is new detail on the same reported event or a
  separate-but-similar occurrence — prompted by a real ambiguity in a
  Hugging Face/METR story that day.
- `skills/brief/brief.py`: `render_tracked_threads()` now filters the
  rendered "Threads being tracked" section to threads touched that day
  or trending (2+ recurrences within the last day) — was printing all
  ~21 "watching" entries daily regardless of relevance. The model's own
  prompt context (`build_prompt()`) stays unfiltered so dedup checking
  isn't affected, only what gets printed.
- `skills/brief/publish.py` and `README.md`: the "Worth Brian's
  attention" → "Worth your attention" audience-specific rename map is
  now empty — the new name reads the same for both the technical and
  Substack audiences.
- Local-network test, not a pipeline change: manually pulled X (dark
  since launch — no persistent filesystem in GitHub Actions for the
  OAuth token-rotation write-back) and the ~32 Substack feeds Cloudflare
  blocks from GitHub Actions' IPs, confirmed not blocked from a normal
  network. 4 new notes resulted (3 from X, 1 from a Substack that had
  simply gone unchecked); regenerated that day's Daily Brief and
  Substack draft for real with them included, with a manual note added
  to the brief's own "Sources checked today" section explaining the
  discrepancy against the automated run's stale results file.

**Why:** Brian asked three direct questions reading that day's brief —
whether a recurring story was actually new, why "Worth Brian's
attention" restated the same items already covered above it, and
whether the pipeline was missing real coverage from the sources it
can't currently reach. All three were real, evidenced gaps, not
misreadings.

**No canon content touched in this entry** — see the same day's second
entry below for the Weekly Wrap Up ceremony, which did.

**Automated checks:** `python3 -m py_compile` clean on both touched
scripts; `python3 scripts/check_doc_accuracy.py` clean.

**Result: COMMITTED AND PUSHED** — Brian confirmed the design for each
fix live, reviewed the regenerated brief and Substack draft before
either was committed.

---

## 2026-08-28 (continued) — Weekly Wrap Up ceremony: promotion-candidates
and staleness queues resolved, new framework, two frameworks revised,
post format restructured

**What changed in canon (Brian's live decisions, not machine-generated):**
- `me/developing-thinking.md` — promoted: the neutral-party erosion note
  extended to cover dev tooling (Cursor Origin, Hugging Face's sale);
  "harness" adopted as vocabulary for the cognitive stack's middle
  layer, checked against real industry usage first; the
  compute-availability-as-supply-risk argument (Brian's "control your
  own destiny" cloud-elasticity analogy); the knowledge factory's
  individual layer reframed as a personal sandbox against shared canon,
  not a standalone second brain; first-hand evidence (a 27B model run
  locally on a stock laptop) for Wave 3's timeline. Folded in, not kept
  standalone: why individual AI augmentation doesn't show up in
  firm-level ROI (now part of the Wave 2 explanation). Cut: the
  "management is emergent" framing claim (duplicate of a line already
  published in `cognitive-stack.md`; new evidence moved there instead).
  Rejected outright, no addition anywhere: youth-ai-sentiment-inversion,
  ai-dissolving-hardware-software-moats. Deferred on purpose:
  machine-speed-vs-human-absorption — Brian's own plain-language
  reframe surfaced a real gap (technical slugs are hard to parse cold),
  held until a layperson-description convention exists for tracked
  threads generally. `## Right now` refreshed to match.
- `frameworks/2031-worker-shape.md` — new framework, promoted from a
  developing-thinking.md thread with independent corroboration
  (Roetzer's typology) and real evidence (wage/employment data).
  `original_url: null`, same convention as `knowledge-factory.md` for
  frontier material with no standalone post yet.
- `frameworks/bitter-lesson.md` — restructured so the corrected position
  (AI erodes the invisible 80%, it doesn't dissolve it) is the stated
  thesis instead of a correction buried after the original overstatement
  — and folded in a sharper version of the correction, given live this
  session: the visible/invisible boundary shifts as AI erodes into the
  80%, it never actually hits zero.
- `frameworks/cognitive-stack.md` — added the three-system convergence
  evidence relocated from developing-thinking.md.
- `outputs/technical-briefings/promotion-candidates.md` — all 6 open
  entries resolved (3 promoted, 2 rejected, 1 deferred with reasoning
  kept for the record).

**Process/product changes, same session:**
- `outputs/weekly-updates/2026/08/2026-08-28.md` — second-ever Weekly
  Wrap Up issue.
- `.claude/skills/weekly-update/SKILL.md` — restructured per Brian's
  direct feedback reading the draft: section order now leads with
  "Where my head's at" and "This week's stories" (most broad-appeal
  first) rather than pipeline-order; "What happened this week" renamed
  "This week's stories"; "What moved in the thinking" now uses real
  `###` subheadings per category instead of a nested bullet list (which
  rendered as one flat list); every "Promoted"/"Folded into" item now
  requires a link to where it actually lives.

**Why:** Scheduled weekly ceremony (Friday cadence). Both the Right-now
refresh and several promoted entries came directly from Brian's own live
commentary this session, not just queue triage — captured in his words
per the ceremony's own non-negotiable.

**Automated checks:** `_index.json`/`_relationships.json` validated as
JSON after surgical edits; `python3 scripts/check_doc_accuracy.py` clean
(caught and fixed three stale framework-count references — README.md,
CLAUDE.md's file tree, llms.txt's per-framework list — before this
passed). Em-dash and backtick pre-publish checks clean on the rendered
post per `me/style-guide.md`.

**Result: COMMITTED AND PUSHED** — Brian reviewed the rendered Substack
HTML twice (once before the restructure, once after) before either
landed.

## 2026-08-26 (continued) — Weekly publication renamed; Substack
comments hookup built for the weekly ceremony

**What was synced (process/product changes):**
- Renamed the weekly publication from "Deeper Thinking" to **"Weekly
  Wrap Up"** across every forward-facing reference in the repo
  (`.claude/skills/weekly-update/SKILL.md`, `me/style-guide.md`,
  `skills/weekly/README.md`, `skills/weekly/gather.py`,
  `outputs/README.md`) — Brian's own rename, done directly on
  Substack; verified the exact capitalization live rather than
  guessed. Synced the one already-published post's `title`/
  `substack_title` frontmatter in `outputs/weekly-updates/2026/08/
  2026-08-24.md` to match what's actually live; left its body prose
  untouched since Brian didn't edit that on Substack either.
- `skills/weekly/gather.py`: new `fetch_own_comments_in_window()` —
  finds Brian's own comments on `brianmadden.ai` Substack posts each
  week via plain HTTP (the publication's `/api/v1/archive` endpoint
  plus each post's `/comments` page), filtered to his own Substack
  profile id so a same-named reader can't produce a false positive.
  Feeds a new "Comments you left this week" section in the prep doc,
  and a note added to `SKILL.md` step 5 so the live ceremony treats a
  comment he already wrote as a real takeaway rather than re-asking
  for one.

**Why:** Brian commented directly on the Aug 26 Daily Brief and asked
whether that could feed the weekly ceremony — it couldn't, until this.
Checked first whether an automated GitHub Actions run could actually
reach Substack at all, given this repo's own confirmed precedent of
GH-Actions-IP blocking on this exact domain family (open decision
#16): a live plain-`curl` test with the pipeline's normal bot
User-Agent got a clean `200` with real comment data server-rendered in
the HTML — a different result from the RSS-feed case, but explicitly
flagged as untested from an actual GitHub Actions runner, with the
already-known residential-network fallback named if that assumption
turns out wrong on the first real Friday run.

**No canon content touched.** Pipeline code and forward-facing docs
only; one historical post's frontmatter synced to match its own
already-live state, not rewritten.

**Automated checks:** `python3 -m py_compile` clean; dry-run tested
end to end against real, current data — correctly found and rendered
Brian's actual Aug 26 comment with the right post, an exact-comment
permalink, and a real timestamp (a real bug in the permalink-pairing
logic was caught and fixed during this same testing, not shipped and
found later).

**Result: COMMITTED AND PUSHED** (`5df0294`) — Brian confirmed live,
same pattern as the entry above.
