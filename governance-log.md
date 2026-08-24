# Governance log

Audit trail for all content synced to brianmadden.ai. Every commit gets an entry showing what was checked and cleared before publishing.

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
