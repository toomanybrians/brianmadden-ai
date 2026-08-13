# BUILD.md — v2 rebuild journal

The working memory of the brianmadden.ai v2 rebuild. Every session (human +
Claude Code) starts by reading `CLAUDE.md`, this file, and
`docs/brianmadden-ai-v2-architecture-and-launch-plan.md` — and ends by
updating the log below. Chat threads are disposable; this file is not.

## Kickoff prompts (by session)

General pattern for any new thread: **"Read MAINTAINER.md and BUILD.md, then
let's pick up where we left off."** MAINTAINER.md has the operating rules;
BUILD.md's session log has the actual state. The specific prompts below are
kept as a historical record of what each day's session was asked to do, not
as a template to re-run.

### Day 2 (first Claude Code session)

> Read MAINTAINER.md, BUILD.md, and docs/brianmadden-ai-v2-architecture-and-
> launch-plan.md. Note: CLAUDE.md/AGENTS.md are consumer-facing module
> instructions (identical pair) — MAINTAINER.md governs this session, and
> where it and the plan doc differ, MAINTAINER.md wins. Day 2 tasks:
> (1) add the maintainer router to the top of CLAUDE.md and AGENTS.md,
> keeping them identical; (2) scaffold ingest/, outputs/, and sources/ with
> README stubs (existing content dirs are declared canon — no restructure);
> (3) propose how review statuses coexist with the existing authority
> levels; (4) inventory .github/workflows and flag what v2 retires;
> (5) append .env and .env.* to .gitignore; (6) seed sources/sources.yaml
> from me/links.md. Update BUILD.md before we stop.

### Day 4 (next session)

> Read MAINTAINER.md and BUILD.md. D3 is closed — sources.yaml has 56
> sources with verified feed_urls, and the frontmatter backfill is done
> (107 of 114 canon files have status/tier). Day 4 task, per the plan doc
> §8: build the ingest skill — pull from sources.yaml's feeds, write
> tier-1 notes to ingest/ (source, link, date, extracted insights in our
> own words, never full-text reprints — see MAINTAINER.md rule 2). Run it
> manually first, tune the insight-extraction prompt. Two things to check
> before or during this: (1) open decision #6 (per-source trust/lens) and
> #7 (email-newsletter ingestion path) need at least a first-pass design,
> since the ingest skill is where both actually get used; (2) the Day-2
> session flagged that sync-to-cloudflare-kv.yml doesn't exclude ingest/
> yet — fix that before any ingest note gets committed, or Tier-1 content
> will leak into the public MCP server (MAINTAINER.md rule 8). Update
> BUILD.md before we stop.

### Day 5 (next session)

> Read MAINTAINER.md and BUILD.md. D4 is closed: the ingest skill is
> running for real (96 notes committed from a 30-day catch-up batch,
> `ingest/.last_run.json` anchoring the auto window for future runs), the
> provider-swap layer (`skills/lib/llm.py`, anthropic/openrouter) landed
> ahead of D6's schedule, and D1 is done — Google Workspace is live,
> `brain@brianmadden.ai` exists (`fetch_entries_email()` in `ingest.py` is
> still a stub, just no longer blocked on infrastructure).
>
> **Important design note carried into D5, not just background:** a
> same-day experiment tried making ingest-time extraction cite Brian's
> named `frameworks/` by name when relevant. An Opus eval of 18 real
> before/after pairs found real value (one genuinely sharp catch —
> correctly distinguishing Sutton's "Bitter Lesson" from Brian's own
> "bitter lesson of workplace AI" as similarly-named but different things)
> but also real cost: 3 of 7 citations were filler ("doesn't connect to
> anything," wasting a bullet), 1 was forced onto a near-content-free
> stub, plus it surfaced two real bugs (truncation from token-budget
> pressure, and one hallucination — a note describing content that wasn't
> in the actual source, model drawing on trained knowledge of "what this
> podcast is usually about" instead of the ~1,300 characters it was
> actually given). The bugs got fixed (`max_tokens` raised to 2048, an
> explicit "ground only in the provided content" instruction added — both
> kept). The framework-citation feature itself got **reverted** — Brian's
> call, and the right one: frameworks are rare and formal (10 in ~2 years)
> against thinking that's fluid and daily, and "does this connect to what
> Brian's actually thinking about" is a cross-note, whole-canon judgment
> that a single-article extraction call structurally can't make well. That
> judgment belongs in the briefing skill, not ingest. Ingest is back to
> plain neutral extraction — see `skills/ingest/prompt.md`.
>
> **This is now D5's central design problem, not a side detail:** build
> the briefing skill so it actually does that cross-note, whole-canon
> synthesis — reading the day's `ingest/` notes *together* (not one at a
> time) against full canon (`me/voice.md` for tone, `me/published-
> thinking.md` + `me/developing-thinking.md` for what Brian's actually
> argued/thinking right now, `frameworks/` for named touchstones where
> they genuinely fit), explicitly looking for both confirmation of
> existing threads *and* things that don't fit anything yet — that second
> part is the real answer to Brian's question "how do I trust the system
> to find what I care about, even things I don't know I care about yet."
> Also worth designing in: a feedback loop where recurring new threads the
> briefing notices get *proposed* for promotion into
> `me/developing-thinking.md` itself (mirroring this repo's existing
> promotion-ceremony pattern — deliberate, human-reviewed, never
> automatic), so that file stays fed by the pipeline over time instead of
> only Brian's manual edits. Likely wants its own prompt-as-template-file
> the way `skills/ingest/prompt.md` works, and reuses `skills/lib/llm.py`
> as-is (already provider-agnostic). Output goes to `outputs/briefings/`
> (tier 3 — starts at `status: not-reviewed-by-human`, never higher,
> machine can't self-upgrade it). Before starting, skim a broader sample
> of the 96 existing ingest notes for quality/tone — only a handful got a
> close read so far. Update BUILD.md before we stop.

## Decisions made (Aug 9, 2026)

- Architecture flipped: this repo is the public base layer; private Citrix
  bmad becomes a read-only-upstream overlay (runtime composition, no merges).
- Same repo, long-lived `v2` branch, one launch PR; `main` + MCP server stay
  untouched until cutover.
- One Substack publication, two bylines (Brian Madden / brianmadden.ai) -- the human and
  the AI brain, sections for Daily Brief · Factory Notes · The Book · Q&A. Pipeline pushes
  drafts; human publishes.
- Email: Google Workspace 1 seat; bmad@ + ask@ + secret intake alias; two
  separate lanes; ask lane read-only with approval queue.
- Compute: GitHub Actions + personal Anthropic API key (+ OpenRouter for
  open-weight experiments); no Citrix credentials anywhere in this plane.
- Launch target: first week of September (re-entry week). Build cadence:
  ~1 hr/day during August.
- Naming decision: public AI byline/account is 'brianmadden.ai' (handle brianmaddenai), primary email brain@, human byline unchanged, 'bmad' now refers only to the private layer.

## Open decisions

1. ~~Commit `ingest/` Tier-1 notes publicly, or keep pipeline-local?~~ —
   **narrowed 2026-08-11.** Turns out this wasn't as urgent as it read: `v2`
   has never actually been pushed to `origin` (see the correction in the
   decisions-made note below), so committing to local git history carries
   zero public exposure today regardless of the answer, and is worth doing
   anyway for the audit-trail/trend-analysis value. First real batch (97
   notes) committed locally 2026-08-11. What's still open: include
   `ingest/` when `v2` eventually gets pushed/merged, or scrub it at that
   point? Revisit closer to the actual push — there'll be months of real
   output to judge by then instead of a couple of examples.
2. Daily Brief cadence: weekdays.
3. Exact briefing publish time (Paris morning? US-morning for reach?).
4. ~~Ratify or amend the frontmatter proposal~~ — **resolved 2026-08-10**,
   Brian ratified directly in
   [docs/frontmatter-schema.md](docs/frontmatter-schema.md) (`status:
   ratified`) and answered the `reviewed` vs `reviewed-and-updated` question
   (yes, a diff is required).
5. ~~`sources/sources.yaml` feed_urls~~ — **mostly resolved 2026-08-10**: 14 of
   15 sources now have a verified `feed_url` (podcast feeds via the iTunes
   Search API, blog/YouTube feeds by direct lookup). Paul Roetzer and Aaron
   Levie were dropped from the list per Brian (personal LinkedIn, no RSS;
   Roetzer already covered via his podcast + newsletter entries). Brian will
   check whether Levie posts somewhere with a feed (X/Twitter?) — re-add if
   so. ExecAI Insider Weekly stays with `feed_url: null` — real source,
   email-only, needs the email-ingestion path from #7 below, not a feed poll.
   The other half of D3, moving Substack follows to the `brianmaddenai`
   account, is still outstanding — manual action on Brian's Substack
   account, not something this session can do. See #7 — the Substack
   picture just got bigger.
6. ~~Per-source trust/lens on the ingest pipeline~~ — **resolved
   2026-08-10 (D4 session).** Brian's steer: wants both a short
   programmatically-parseable field and a longer freeform field that acts
   like a mini-prompt conveying his POV, both optional/blank-safe since
   he'll steer them in over time rather than opinionating all 56 sources at
   once. Landed as two new `sources.yaml` fields: `lens` (short free-form
   tag, deliberately not a fixed enum — new tags can be invented without a
   code change) and `pov` (longer freeform text, fed directly into the
   ingest skill's extraction prompt as framing instruction when present).
   Backfilled only on the two sources that already carried implicit lens
   language in `note` (moonshots, marcus-on-ai) as worked examples; the
   other 54 are blank by design. Also designed for reuse by the future
   Day-5 briefing skill, per Brian's own framing ("the AI which builds the
   daily newsletter") — not ingest-only.
7. **Substack + email newsletter ingestion (flagged 2026-08-10, design
   TBD; partially actioned same day — see session log).** Brian has a
   personal Substack account with a bunch of subscriptions, now largely
   folded into `sources.yaml` (30 added — see log). Two things still open:
   (a) a separate pile of non-Substack email newsletters Brian wants
   ingested by pointing them at `brain@brianmadden.ai` and pulling via an
   app key (Gmail API, consistent with §5's existing plan for the
   `ask@`/intake lanes) rather than RSS polling — the ingest skill needs an
   email-source path alongside the feed-poll path, not just more
   `sources.yaml` rows. **First-pass design landed 2026-08-10 (D4
   session):** `skills/ingest/ingest.py` has a `fetch_entries_email()`
   function with the intended shape documented (poll Gmail API against
   `brain@` for known sender addresses, normalize to the same entry shape
   `fetch_entries()` returns so the extraction/write pipeline downstream is
   unchanged) but it raises `NotImplementedError`. **Unblocked 2026-08-11:**
   D1 is done — Brian has Google Workspace running with `brain@brianmadden.ai`
   live. The stub can become real whenever this gets picked up (needs a
   Gmail API app key/credentials for `brain@`, not part of this session);
   (b) going forward Brian plans to subscribe to *new*
   sources via the `brianmaddenai` Substack account rather than his
   personal one (per the plan doc §6 — "the follow list becomes the public
   source registry"). Mechanism confirmed same-day: a Substack profile's
   `/reads` page (e.g. `substack.com/@handle/reads`) is public, lists every
   followed publication, and is scrapeable via browser automation (no auth
   needed) — the same technique used for the personal-account import below
   could re-run periodically against the `brianmaddenai` account once it
   exists, diffing against `sources.yaml` to catch new follows. That's a
   good candidate for a small script under `skills/` once D4 is being built,
   rather than a manual one-off each time. Until then, the fallback Brian
   suggested — just telling Claude to add specific ones — works fine.

8. **Canon governance: `developing-thinking.md` needs pruning/dating,
   `frameworks/` needs a retirement path (flagged 2026-08-11, design TBD,
   not started).** Raised by Brian at the end of the D4 session, after the
   framework-in-ingest detour above made both problems concrete. Not
   picked up this session — deliberately deferred to a dedicated pass,
   whether that's before/alongside D5 or later. Findings so far, so the
   next session doesn't have to re-derive them:

   - `me/developing-thinking.md` is ~9,000 words. Its "What's connecting"
     section has ~50 ungrouped bullets and "Scratchpad" has ~40 more —
     **90 items, none dated.** No way to tell if something was added
     yesterday or five months ago without digging. Only the "big
     arguments" section has partial dating (some sub-updates say "March
     18 update," most don't). Brian's framing: his daily thinking is
     "fresh and fluid," but the file has no mechanism to distinguish
     still-active threads from ones that quietly died, so it just grows.
   - `frameworks/` (10 files): dates range from 2 months old
     (`7-stage-roadmap.md`) to 15 months old (`workspace-as-control-
     plane.md`); half are 6+ months old. No retirement mechanism exists —
     once a framework is canon, it stays canon regardless of whether the
     field has moved past it. Brian's read: "frameworks from 6 months ago
     have a very good chance of not being relevant today," and he
     explicitly does not want to just delete history — wants an archive
     path that preserves it.

   **Proposed direction (not agreed, not built — starting point for the
   next session):**
   1. Backfill approximate dates for existing `developing-thinking.md`
      content via `git blame`/`git log -p` (every bullet landed in some
      commit — reconstruct roughly when, rather than making Brian
      manually re-date 90 items). Going forward, a light convention
      (new entries carry a date) keeps it current for free.
   2. A staleness-triage tool (script or skill) that periodically scans
      both files, flags anything past a threshold as a candidate, and
      hands Brian a short list — not an auto-pruner. He makes the actual
      call per item: keep (still developing), promote (into
      `published-thinking.md` or graduate into a real framework), or
      drop/retire. Matches this repo's existing pattern everywhere else:
      the system surfaces, a human decides, nothing gets upgraded
      automatically.
   3. Frameworks get a `status: archived`-style flag (or a
      `frameworks/archive/` directory) rather than deletion — pulled out
      of active indexes (`llms.txt`, `_index.json`, whatever D5's
      briefing skill and future consumers read) but the file and its git
      history stay. "What I used to think" has real value, including for
      the same trend-analysis use case that motivated committing
      `ingest/` notes locally (BUILD.md open decision #1).

   Open questions for whoever picks this up: what thresholds actually
   make sense (scratchpad-tier vs. developed-argument vs. framework tier
   probably want different windows); whether the triage tool does an
   LLM-assisted first pass (propose promote/drop/keep with reasoning) or
   is purely a dumb date-scanner that leaves all judgment to Brian; how
   `check_doc_accuracy.py`'s framework-counting logic should handle an
   archived tier.

## Day plan (checklist — details in the plan doc §8)

- [x] D1 — Workspace + aliases + MX · lock naming · carve-out note sent
- [x] D2 — scaffold structure on `v2` · CLAUDE.md reviewed by Brian
      (scaffolding done; Brian's review of CLAUDE.md/AGENTS.md still open)
- [x] D3 — sources.yaml curated (51 sources, 50 with a live feed_url)
      (Substack follows → brianmaddenai account is a manual action on
      Brian's Substack, not Claude Code work — still outstanding, tracked
      in open decision #7)
- [x] D4 — ingest skill built and running for real: provider-swap layer
      (anthropic/openrouter) and last-run tracking built ahead of schedule,
      first full-registry run committed (96 notes across 55 sources, see
      session log)
- [x] D5 — briefing skill built, validated against a real 97-note batch,
      voice iteration genuinely underway (style-guide.md started, title
      guidance tuned, byline voice tuned twice) — this is ongoing by
      nature, not a one-time close-out
- [ ] Weekend — back-catalog bootstrap batch job
- [ ] D6 — workflows automated (workflow_dispatch during build; cron via main)
- [~] D7 — Substack publication live, **first real post published**
      2026-08-11 (manually, end to end: generate → Brian edits → status
      synced → rendered → pasted in by hand) — ahead of schedule, same
      pattern as D4/D5 landing early. What's still actually D7: the
      session-cookie draft-push client (posting is 100% manual right
      now) and moving Brian's Substack follows to the `brianmaddenai`
      account (open decision #7, still outstanding)
- [ ] D8 — email lanes wired
- [ ] D9 — 10–15 core canon assets seeded
- [ ] D10 → launch — daily dry run, review over coffee
- [ ] Launch week — announcement essay + first public brief + landing swap

## Session log

### 2026-08-09 — chat session (pre-repo)
Ideation + architecture settled; plan doc, CLAUDE.md v1, and this file drafted
in Claude chat. Next session: kickoff prompt above, on the `v2` branch.

### 2026-08-10 — Claude Code session (Day 2, kickoff)

Ran the six kickoff tasks against the actual repo state:

1. **Maintainer router.** CLAUDE.md already had the router line from the
   pre-repo drafting session; added the identical line to AGENTS.md. The two
   files now diverge only in the expected self-reference ("identical to
   AGENTS.md" vs "identical to CLAUDE.md").
2. **Scaffolding.** Added `ingest/`, `outputs/` (with `briefings/`, `book/`,
   `qa/` subdirs, `.gitkeep`-ed since they're empty), and `sources/`, each
   with a README stub pointing back to MAINTAINER.md for the tier rules. No
   existing content moved — `me/`, `frameworks/`, `posts/`, `talks/`,
   `podcast/`, `interviews/` stay put as declared canon.
3. **Status/authority coexistence proposal.** Written up in
   [docs/frontmatter-schema.md](docs/frontmatter-schema.md): `authority_level`
   and `status` are orthogonal (trust vs. human-checked), existing canon gets
   backfilled to `status: reviewed` in one pass, all tier-3 output starts at
   `not-reviewed-by-human` and machines can never set it higher, `tier` /
   `sources` / `model` are added as new frontmatter fields. Awaiting Brian's
   ratification (open decision #4 below).
4. **Workflow inventory.** `.github/workflows/check-docs.yml` only checks
   stated counts/tree against the existing tier-2 dirs — untouched by the
   new directories, nothing to retire. `sync-to-cloudflare-kv.yml` currently
   globs *every* `.md`/`.txt`/`.json` in the repo (`find . \( -name '*.md'
   ... \) | grep -v node_modules | grep -v .github`) for full syncs, and diffs
   `HEAD~1..HEAD` for incremental ones — **neither exclusion list knows about
   `ingest/` yet**, so as soon as ingest notes exist and get committed, this
   workflow will push Tier-1 content into the MCP server's KV store, which is
   exactly what rule 8 (machine indexes must exclude `ingest/`) forbids. This
   needs a `grep -v ingest/` added to both the incremental diff and the full
   sync's `find`, before D4 (ingest skill going live). Flagging as a Day-4
   blocker rather than fixing now, since it's untested until there's ingest
   content to sync.
5. **`.gitignore`.** `.env` and `.env.*` were already present (added in an
   earlier commit, before this session) — no change needed.
6. **sources.yaml.** Seeded from `me/links.md` — 5 people/newsletters + 11
   podcasts, `url` carried over, `feed_url` left `null` pending real feed
   lookups (open decision #5).

Everything above is on the `v2` branch, uncommitted at end of session pending
Brian's review.

*(Note: the "uncommitted" line above went stale — Brian committed the Day-2
work himself, including ratifying the frontmatter schema, before the next
session started. See below.)*

### 2026-08-10 — Claude Code session (Day 3, feed lookups)

Started the D3 checklist item: filled in real `feed_url` values in
`sources/sources.yaml`. Podcast feeds resolved via the iTunes Search API
(`feedUrl` field — reliable, no guessing at CDN paths); blog/newsletter feeds
checked directly against standard `/feed` paths; Nate B. Jones's YouTube feed
built from his resolved channel ID. All 14 resulting URLs verified with a
`curl` 200 check. Three sources (Paul Roetzer, Aaron Levie, ExecAI Insider
Weekly) have no feed to poll and stay `null` with an explanatory note — see
open decision #5.

Session was interrupted by a machine crash/reboot mid-way; the sources.yaml
edit had already landed on disk and survived. Picking back up, Brian flagged
a bigger follow-on: a personal Substack account's worth of subscriptions to
fold into the source registry, plus a separate batch of non-Substack email
newsletters to ingest via `brain@brianmadden.ai` + an app key rather than RSS
polling. Wrote this up as open decision #7 rather than acting on it now — it
needs design work when the ingest skill (D4) is actually built, same as the
per-source trust/lens question (#6).

`sources/sources.yaml` changes are uncommitted at end of session.

### 2026-08-10 — Claude Code session (Day 3 cont'd, Substack import)

Session survived two machine crashes/reboots — file edits persisted both
times, confirming the "repo is the memory, chat is disposable" model holds
even mid-edit.

Brian asked to remove the two feedless LinkedIn entries (Paul Roetzer, Aaron
Levie) — done; noted in `sources.yaml` that Levie may resurface if a
non-LinkedIn feed turns up (X/Twitter flagged, not looked up).

Pulled Brian's Substack "reads" page
(`substack.com/@briansmadden/reads`) via browser automation — 62 followed
publications, no login needed since the page is public. Extracted every
publication's actual URL (not just name) by scrolling to trigger the page's
lazy-loaded list and reading hrefs out of the DOM; 8 publications didn't load
via scroll and were resolved individually via search instead.

Filtered the 62 down to AI/futurism/future-of-work relevance per Brian's
steer (skip geopolitics, comedy, Paris-life, self-help, food) and added 30 to
`sources.yaml`, each with a verified (HTTP 200) `feed_url` at `<domain>/feed`.
`sources.yaml` is now 45 entries, 44 with a live feed_url. Explicitly
skipped as out-of-scope: Paul Krugman, Sam Harris, Andrew Yang, Dave Barry,
Like a Chef, Lizzi C Lee, Mark Manson, Reporting From Paris, On Substack, The
Substack Post. Skipped as dupes of existing entries: One Useful Thing,
Dwarkesh, Nate's Substack.

~19 remaining subscriptions are genuinely ambiguous (unclear topic, or
borderline work-relevant — tech policy, labor/politics crossover, general
forecasting, a couple of odd Substacks literally named "Claude Cowork" /
"Claude Mythos" that need a human glance before assuming what they are).
Punted back to Brian rather than guessing; not yet added or rejected.

Also confirmed the mechanism for the `brianmaddenai`-account version of this
same task once Brian starts following sources from that account instead of
his personal one — see open decision #7.

`sources/sources.yaml` and `BUILD.md` both uncommitted at end of session,
holding per Brian's request.

### 2026-08-10 — Claude Code session (Day 3 cont'd, resolving the ambiguous batch)

Brian ruled on part of the ~19-item ambiguous list from the last entry:
**added** BIG by Matt Stoller, Rutger Bregman, Forecasting Research
Institute, and Cory Doctorow (his native Substack cross-post feed at
doctorow.substack.com — primary site is pluralistic.net, noted in the entry)
— these were the "probably yes" set and Brian didn't object; **added** the
two odd ones, Claude Cowork (resolved via its actual handle @claudedesktop →
domain coworkoperator.com) and Claude Mythos (native
claudemythos.substack.com) — both real, both yes; **declined** Will Lockett's
Newsletter and Robert Reich; **held** the Daniel Kokotajlo personal Substack
as a likely dupe of AI Futures Project — not added, revisit if it turns out
to be distinct content. `sources.yaml` is now 51 entries, 50 with a live
`feed_url`.

**Still genuinely open** (Brian hasn't ruled on these; not added, not
rejected): @jasmine's substack (Jasmine Sun), Babylon Burns, Beauty is truth,
But This Time It's Different (Sinéad O'Sullivan), The Digital Contrarian,
Ghosts of Electricity, Graphomane (Neal Stephenson), Hard Reset, Kun's Field
Notes, The Wake Up Call. Revisit next time sources.yaml comes up, or drop
them — they've been sitting for one session already.

Files still uncommitted, holding per Brian's request.

### 2026-08-10 — Claude Code session (Day 3 close-out, last ambiguous batch + commit)

Brian ruled on the rest of the ambiguous list: **excluded** Babylon Burns,
Beauty is truth, But This Time It's Different, The Digital Contrarian,
Graphomane; **included** the other five — jasmine's substack, Ghosts of
Electricity, Hard Reset, Kun's Field Notes, The Wake Up Call — each added
with a verified `feed_url`. `sources.yaml` is now 56 entries, 55 with a live
feed. Every subscription from the original 62-item Substack pull is now
either added or explicitly declined — nothing left unresolved from that
batch.

D3 is done. Committed both sessions' `sources.yaml`/`BUILD.md` work as
[98c406e](../../commit/98c406e) (feed lookups + first Substack import
batch), then this closing batch as a follow-up commit. Moving Substack
follows over to the `brianmaddenai` account itself is still Brian's manual
action — tracked under open decision #7, not a blocker for anything else.

Next: frontmatter backfill (`status: reviewed` across the 114 existing
canon files, per the ratified schema — mechanical, no open design
questions left).

### 2026-08-10 — Claude Code session (frontmatter backfill)

Backfilled `tier: 2` and `status: reviewed` into every existing canon file
that already had YAML frontmatter — 104 of 114 files across `me/`,
`frameworks/`, `posts/`, `talks/`, `podcast/`, `interviews/`, done via a
script that appends the two fields only where missing (idempotent, ran a
verification pass after — no broken frontmatter, no double-delimiters).

10 files have no frontmatter at all and were **left untouched** rather than
guessed at:
- 5 are navigational index pages (`interviews/index.md`, `talks/index.md`,
  `posts/citrix-blog/index.md`, `posts/linkedin/index.md`,
  `posts/bluesky/index.md`) — TOCs, not standalone content assets; probably
  don't need `status`/`tier` at all, but that's a call for whoever owns the
  schema, not something to assume.
- 2 are reference lists (`me/books.md`, `me/links.md`) — same question.
- 3 look like straightforward oversights, since sibling files in the same
  directory all have full frontmatter: `frameworks/delegation-not-automation.md`,
  `talks/2026-03-18-ducug-the-new-cognitive-stack.md`,
  `talks/2026-06-03-euctech-the-last-chapter-of-euc.md`. These probably want
  the same `title`/`authority_level`/`file_type`/`tags` treatment as their
  neighbors, not just a bolted-on `status` field — worth a small follow-up
  pass, flagged here so it isn't lost.

Ran `scripts/check_doc_accuracy.py` afterward as a sanity check — it fails,
but on pre-existing drift unrelated to this change (llms.txt counts stale
against actual framework/post/talk counts, and CLAUDE.md's repo-structure
tree not yet updated for the v2 dirs). Not caused by the backfill; not fixed
here — separate cleanup.

Brian ruled on the 3 flagged oversight files same-session: `date: 2025-12-18`
confirmed for `delegation-not-automation.md`; no recording for the DUCUG
talk; `podcast/ep2.md` confirmed as the recorded version of the EUCTech
talk (YouTube link pulled from ep2's Listen section). All three now have
full frontmatter matching their siblings' conventions, including
`status`/`tier`. That brings the running total to 107 of 114 canon files
with `status`/`tier` set (104 from the original backfill + these 3). The
remaining 7 are the index/reference-list pages flagged in the prior entry —
still an open call for whoever owns the schema, not touched.

Also answered Brian's questions about (a) whether the 104-file backfill
implies a currency audit is needed — no, `status: reviewed` is about
provenance not freshness, and the existing `staleness_threshold` field
already covers that; spot-checked `me/developing-thinking.md` (updated Aug
5, within its `weeks` threshold) and `me/published-thinking.md` (updated
Jul 22, within its `months` threshold) — both current, no action needed;
and (b) fleshing out the `brianmaddenai` Substack account — not
programmatic (no API for profile setup or following), so drafted a bio and
sent Brian the full 56-source URL list from `sources.yaml` to click through
manually while logged in as `brianmaddenai`. That part is on Brian, not
tracked further here unless it surfaces new sources to add back to
`sources.yaml`.

### 2026-08-10 — Claude Code session (Day 4, ingest skill)

Built the ingest skill. Six pieces, in order:

1. **Fixed the standing `sync-to-cloudflare-kv.yml` blocker** flagged since
   the Day-2 session — added `grep -v ingest/` to the incremental diff, the
   full-sync `find`, and the deleted-file cleanup diff, plus a comment
   explaining why (MAINTAINER.md rule 8: Tier-1 content must never reach the
   public MCP server's KV store). Done before anything else so it couldn't
   be forgotten once real ingest notes exist.
2. **Resolved open decision #6** (per-source lens) — see the updated entry
   above. Added `lens` + `pov` fields to `sources.yaml`, backfilled on
   `moonshots` and `marcus-on-ai` only, documented in both `sources.yaml`'s
   header comment and `sources/README.md`.
3. **Built `skills/ingest/`** — `ingest.py` (feed fetch via
   `requests`+`feedparser`, dedup against existing `ingest/**/*.md`
   frontmatter with no separate state file, one `claude-sonnet-5` call per
   new entry using `prompt.md` as an editable template, `NOT_RELEVANT`
   sentinel so broad-interest feeds don't pollute `ingest/` with off-topic
   entries, frontmatter-tagged note writer), `prompt.md` (the extraction
   prompt, kept as a separate file specifically so it's easy to iterate on
   per BUILD.md's "tune the insight-extraction prompt"), `README.md`
   (usage + how-it-works + known v1 limitations). Also gave open decision
   #7a (email ingestion) a first-pass design: `fetch_entries_email()` is a
   documented stub that raises `NotImplementedError` — the intended Gmail-
   API shape is written down, but it can't actually run until `brain@`
   exists (D1/D8).
4. **Added repo-level plumbing that didn't exist yet**: `requirements.txt`
   (first dependency manifest in the repo — pins `anthropic`, `feedparser`,
   `PyYAML`, `requests` to what's already installed locally) and
   `.env.example` (documents `ANTHROPIC_API_KEY` as required-now, notes
   `OPENROUTER_API_KEY`/Gmail creds as future/not-yet-needed).
5. **Updated CLAUDE.md + AGENTS.md's repo-structure tree** to include the
   v2 dirs that existed on disk but weren't listed
   (`MAINTAINER.md`, `BUILD.md`, `requirements.txt`, `docs/`, `sources/`,
   `ingest/`, `outputs/`, `skills/`) — scoped narrowly to the tree block,
   since adding `skills/` this session would otherwise have made the
   pre-existing `check_doc_accuracy.py` drift (flagged, not fixed, in the
   frontmatter-backfill session) worse.
6. **Verified the plumbing end to end minus the actual LLM call.** No
   `ANTHROPIC_API_KEY` in this shell, so extraction itself is untested —
   flagging that plainly rather than claiming a full dry run. What *is*
   confirmed: `python3 scripts/check_doc_accuracy.py` now clears the
   top-level-tree and CLAUDE/AGENTS-parity checks (only the unrelated,
   pre-existing `llms.txt` count drift remains, out of scope); a full
   `--since-days 3 --max-per-source 1 --dry-run` pass against all 56
   sources completed in ~2 minutes with zero crashes and correct per-source
   dedup/skip behavior — blogs, Substacks, podcast RSS, and YouTube feeds
   all normalize correctly, the one email-only source
   (exec-ai-insider-weekly) skips cleanly, and one clearly off-topic entry
   surfaced (a California-politics episode from On with Kara Swisher) that
   the `NOT_RELEVANT` filter is specifically there to catch once a real key
   is in place.

**Next session, before D5:** export `ANTHROPIC_API_KEY` (repo-root `.env` or
shell) and run `python3 skills/ingest/ingest.py --source ethan-mollick
--dry-run` to see and tune real extraction output — that's the "tune the
insight-extraction prompt" step BUILD.md called for, genuinely blocked on a
key this session didn't have. Once the prompt looks right, a real (non-dry)
run will start populating `ingest/` for real, and `sources.yaml`'s
`lens`/`pov` fields can be filled in incrementally as Brian actually forms
opinions on more sources.

**Same-session follow-up: provider abstraction.** Brian asked (a) whether
v2 should be published/cut over to `main` yet, (b) whether to set GitHub
Actions secrets now, and (c) said he wants it easy to swap AI providers
(OpenRouter etc.), not hardcoded to Anthropic. Answered (a)/(b) directly —
no to both: `main` stays untouched until the actual launch-window cutover
per MAINTAINER.md (nothing's been dry-run or seeded yet, Days 5–10 aren't
done), and Actions secrets aren't needed until Day 6 automates anything —
D4 was deliberately manual/local so the prompt gets tuned by a human before
it's wired to run unattended. For (c), built it now rather than waiting for
Day 6, since Day 5's briefing skill would otherwise hardcode Anthropic too:
`skills/lib/llm.py`, one `generate()` entry point, provider chosen via
`LLM_PROVIDER`/`LLM_MODEL` env vars or `--provider`/`--llm-model` CLI flags,
supporting `anthropic` (default, native SDK) and `openrouter`
(OpenAI-compatible HTTP via `requests`, already a dependency — no new
package). `skills/ingest/ingest.py` refactored to call `lib.llm` instead of
importing the Anthropic SDK directly; re-verified dry-run still passes
post-refactor, including that `--provider openrouter` correctly reports
`OPENROUTER_API_KEY` as the missing key rather than the Anthropic one.
`.env.example` and the skill's README updated to match. This means the
open-weight comparison run in the post-launch backlog (§8 of the plan doc)
is now a `--provider openrouter --llm-model <id>` flag away, not a rewrite.

Note: `sources/sources.yaml` picked up a concurrent, separately-committed
change this session (Brian added 6 more sources via the `brianmaddenai`
Substack account directly — 56 → 62 entries, see commit `05e84f1`). This
session's `lens`/`pov` additions to `moonshots` and `marcus-on-ai` rode
along in that commit since it captured the working tree at commit time;
everything else from this session (`ingest/` skill, workflow fix, tree
updates, `lib/llm.py`) is separate and still uncommitted, per usual — held
for Brian's review.

### 2026-08-11 — same session, continued (real run, last-run tracking, a factual correction)

Committed everything from the entry above in 5 logical commits (workflow
fix, sources/README.md doc, the ingest skill + provider layer, the
CLAUDE.md/AGENTS.md tree fix, this journal). Caught and fixed a real bug
while staging: `.gitignore`'s `.env.*` rule was silently also excluding
`.env.example`, which would have kept it from ever being committed — added
a `!.env.example` negation. Also caught `skills/lib/__pycache__/` getting
swept into `git add skills/` — removed it and added `__pycache__/`/`*.pyc`
to `.gitignore` before it could land in a commit.

Brian then asked the real next-step question: should `v2` get published,
should GitHub Actions secrets get set, and he wants provider-swapping to be
easy (OpenRouter etc.), not hardcoded to Anthropic. Answered: no to
publishing (nothing's been dry-run/seeded, `main` stays untouched until
the actual cutover per MAINTAINER.md) and no to secrets yet (D4 is
deliberately manual, Day 6 is when automation — and secrets — arrive). Built
the provider-swap layer now rather than waiting for D6, since D5's briefing
skill would otherwise hardcode Anthropic too — see `skills/lib/llm.py`
below.

Walked Brian through getting a real `ANTHROPIC_API_KEY` into the repo-root
`.env` (Claude never handled the key value itself — only verified its
presence/format after Brian added it). First real extraction call
succeeded: one Ethan Mollick post, dry-run then a real non-dry write,
producing the pipeline's first actual tier-1 note. Output quality looked
right — neutral third-person insight bullets, one attributed quote well
under the 25-word cap.

**Built the provider-swap layer** (`skills/lib/llm.py` + `skills/lib/__init__.py`):
one `generate()` entry point so no skill imports an LLM SDK directly.
Provider/model chosen via `LLM_PROVIDER`/`LLM_MODEL` env vars or
`--provider`/`--llm-model` CLI flags. Ships with `anthropic` (default,
native SDK) and `openrouter` (OpenAI-compatible HTTP via `requests`,
already a dependency — no new package) for the post-launch open-weight
comparison runs. `skills/ingest/ingest.py` refactored to go through it;
re-verified the dry-run still works post-refactor, including that
`--provider openrouter` correctly reports `OPENROUTER_API_KEY` (not the
Anthropic key) as missing.

**Built last-run tracking**, per Brian's ask: rather than a fixed
`--since-days`, poll "since the time actually elapsed since the last
completed full run." `ingest/.last_run.json` records the UTC timestamp of
the last full-registry, non-dry run; `resolve_since_days()` in `ingest.py`
computes the window from it (falls back to 7 days with no recorded prior
run). This gets Brian's stated cadence — ~24h on a normal weekday run, ~72h
after a weekend gap, longer after an outage — for free, with no hardcoded
calendar logic, since a weekend gap or an outage both just show up as more
elapsed hours since the last run. Only a full run (no `--source` filter,
not `--dry-run`) advances the clock, so single-source testing or dry-run
previews can't cause the *next* real run to under-fetch everything else.
Committed separately from the note-writing logic.

**First real full-registry run**: `--since-days 30 --max-per-source 3`
(explicit override, chosen deliberately wide for this first real batch per
Brian — future runs will use the auto window). 113 new entries found
across 55 of 62 sources (7 had nothing in the 30-day window); 96 notes
written, 17 skipped as `NOT_RELEVANT` — the relevance filter doing exactly
what it was built for (off-topic items from broad-interest feeds: Ezra
Klein's Thiel/DSA politics AMA, Lex Fridman's Civil War history episode,
Prof G's "Take a break" and GLP-1s episodes, a couple of Big by Matt
Stoller's non-AI antitrust pieces, After Babel's social-media-policy
pieces, and others). Spot-checked the `marcus-on-ai` note specifically,
since that source has `lens`/`pov` set — the extraction visibly used the
framing ("useful skeptical-but-correct point... matters for any org
evaluating vendor claims"), not just a generic summary. Confirms the D4
open decision #6 design actually works, not just that it parses.

**A factual correction, caught by Brian:** BUILD.md's own summaries (and
this session's earlier claim to Brian) said "`v2` pushed Aug 10" — checked
via `git fetch` + `git branch -r`, and that's wrong. `origin` only has
`main` and one unrelated feature branch; `v2` has never been pushed. The
repo itself is public, but nothing on `v2` — including everything built in
this entire D4 session — has ever been visible to anyone outside this
machine. Corrected in `docs/brianmadden-ai-v2-architecture-and-launch-plan.md`
(§8 Day 1, §9) and in open decision #1 above. This also resolved open
decision #1 more than expected: since nothing is actually public until a
push happens, "commit ingest/ notes or not" and "are they public or not"
turned out to be two different questions, not one — committing locally is
safe and valuable (audit trail, the trend-analysis use case Brian raised —
"when did people start talking about X" is exactly what dated git history
gives you) regardless of when/whether `ingest/` ends up in whatever gets
pushed at launch. Committed the 97 notes + `.last_run.json` locally with
Brian's explicit go-ahead once this was laid out.

**Where things stand:** D4 is fully done — skill built, prompt validated
against real output, 97 real notes in `ingest/`, provider-swap layer in
place ahead of schedule, last-run tracking built ahead of D6. Next real
session is D5 (briefing skill) or continuing to let the ingest skill run
and accumulate more real output first — Brian's call.

### 2026-08-11 — same session, continued (the framework detour, an RSS bug, and canon governance)

Brian asked to clean up three loose ends from the session above: confirmed
D1 (Workspace/`brain@`) is actually done, asked for the `llms.txt` fix, and
asked how to spot-check ingest note quality — which surfaced the real gap
driving everything below: the extraction prompt's "focus" was a generic
one-liner Claude wrote, not grounded in anything of Brian's. Fixed the
first two directly (`llms.txt`'s missing `delegation-not-automation.md`
entry and stale counts, the stale "blocked on Workspace" note). The third
became a real detour.

**The framework-aware extraction experiment.** Tried fixing the "generic
focus" gap by having extraction cite Brian's named `frameworks/` by name
when relevant (`load_frameworks_list()`, reading title/description live
from `frameworks/*.md`). Brian then asked for a rigorous check rather than
trusting a couple of spot-checked examples: re-extracted 18 real
already-ingested entries with the new prompt, had Opus blind-judge the
18 old/new pairs. Findings: real value (one genuinely sharp catch —
correctly distinguishing Sutton's "Bitter Lesson" from Brian's own "bitter
lesson of workplace AI" as similarly-named but different things) but real
cost (3 of 7 citations were filler, 1 forced onto a near-empty stub), plus
two actual bugs: truncation (2 of 16 new notes cut off mid-sentence — a
longer prompt left less token headroom, `max_tokens=1024` wasn't enough)
and hallucination (a Hard Fork note described content — White House AI
framework, rogue agents, METR — that doesn't exist anywhere in the
episode's actual ~1,300-character show notes; the model drew on trained
knowledge of "what this podcast is usually about" instead of what it was
actually given). Both bugs fixed (`max_tokens` → 2048, explicit
"ground only in the provided content" instruction added) and verified on
the two specific failing cases.

**Then reverted the feature itself**, on reflection with Brian: frameworks
are rare and formal (10 in ~2 years) against thinking that's fluid and
daily, and "does this connect to what Brian's actually thinking about" is
a cross-note, whole-canon judgment that a single-article extraction call
structurally can't make well — that's the briefing skill's job (D5), not
ingest's. `load_frameworks_list()` and all `framework_list`/
`FRAMEWORKS_LIST` threading removed from `ingest.py`/`prompt.md`; ingest
is back to plain neutral extraction. The `max_tokens` bump and grounding
instruction were kept — correctness fixes independent of the framework
question. **Net effect on D5:** its kickoff prompt (above) got rewritten
mid-session, since the first version told D5 to reuse a pattern that no
longer exists — now it correctly frames cross-note/whole-canon synthesis
as D5's central design problem, including the `developing-thinking.md`
promotion-loop idea.

**A real RSS content bug, separately.** Brian asked whether feeds
truncate content before extraction even sees it. Checked empirically:
Substack's `content:encoded` (and several non-Substack blogs) carry
genuine full-text, not a preview — but `MAX_CONTENT_CHARS=8000` was an
arbitrary guess of Claude's that cut real posts by 35-67% (Mollick
13022→8000 chars, SemiAnalysis 24310→8000, Interconnects 9340→8000).
Raised to 50000. Separately confirmed SemiAnalysis is genuinely paywalled
at the source — even the raw feed content is only the free preview (ends
mid-thought at "Read more") — documented as a known limitation, not
fixable from the RSS side. Note: some of the 96 already-committed notes
may have been extracted from truncated content under the old cap;
not re-run this session, flagged to Brian as an open call (nothing
downstream depends on them yet).

**Canon governance, deferred.** Brian's response to the framework detour
went deeper: `developing-thinking.md` has grown into an unpruned,
undated ~9,000-word file, and `frameworks/` has no retirement path despite
some entries being 15 months old in a fast-moving field. Real, separate
problem from anything ingest-related. Investigated and wrote up findings
+ a proposed direction as open decision #8 above, rather than design or
build it in an already-long session — Brian's call to stop here and pick
it up fresh, "whether tomorrow in D5 or some other time."

**Where things stand, updated:** D4 remains fully done and now
bug-fixed (truncation, hallucination, RSS content cap). The
framework-citation experiment was a real, worthwhile detour — it found
and fixed two genuine bugs even though its own premise got reverted.
Two threads now open for whoever picks up next: D5 (briefing skill,
kickoff prompt rewritten to reflect everything above) and open decision
#8 (canon governance — no kickoff prompt written yet, pick a session type
when it's actually being picked up).

### 2026-08-11 — Claude Code session (Day 5, briefing skill)

Built `skills/brief/` — the cross-note, whole-canon synthesis skill D5's
kickoff prompt called "the central design problem," not a side detail.
Before writing any code, skimmed ~14 ingest notes beyond the handful
already read closely (spanning Marcus, Miessler, Narayanan, Exponential
View, Hard Fork, Interconnects, Emerging AI, David Shapiro, Center for
Humane Technology, Labor Matters, and others) to confirm the raw material
was consistently usable — it was: neutral third person, grounded, no
repeat of the truncation/hallucination bugs from the prior session.

**Model: Opus 5, Brian's explicit call.** Asked directly (this is the
hardest judgment call in the pipeline, and it's one call/day not one/
article like ingest, so the cost multiplier is smaller than it sounds) —
Brian chose Opus over Sonnet. `skills/brief/brief.py` defaults to
`claude-opus-5`, still overridable via `--llm-model`/`LLM_MODEL`/
`--provider`, same mechanism as ingest.

**Design, per the rewritten kickoff prompt:**
- `skills/brief/prompt.md` — one call per run, given full canon
  (`me/voice.md`, `me/published-thinking.md`, `me/developing-thinking.md`,
  a lightweight `frameworks/*.md` title+description list — not full
  framework text) plus every ingest note captured since the last briefing
  run, all at once. Explicitly asks for three things: what confirms
  existing threads (cite by name), what doesn't fit anywhere yet, and a
  short "worth Brian's attention" pull.
- **Byline/voice, a real design call, not just plumbing:** the plan doc's
  §6 two-byline convention (Brian Madden = human, brianmadden.ai = AI) was
  already decided but not yet applied anywhere. `prompt.md` instructs the
  model to write as itself in first person ("I read N items today...")
  and refer to Brian in the third person, informed by `voice.md`'s tone
  without impersonating him. This is a first-pass interpretation — flagged
  in `skills/brief/README.md` as the thing most likely to change once
  Brian reacts to real output, same as ingest's prompt got tuned after
  seeing real extractions.
- **The promotion-loop feedback mechanism** BUILD.md asked to have
  "designed in": deterministic (not model-judged) thread tracking.
  `prompt.md` asks the model for a `---THREAD-SIGNALS---` JSON block
  alongside the brief (which tracked slugs recurred, what new patterns are
  worth watching); plain Python (`update_tracker()` in `brief.py`) owns
  the actual bookkeeping in `outputs/briefings/.thread_tracker.json` and
  decides when a thread has recurred enough (3 runs, `PROMOTION_THRESHOLD`)
  to get queued in `outputs/briefings/promotion-candidates.md` — a
  human-review-only file. Nothing is ever written into
  `me/developing-thinking.md` automatically; that file only changes when
  Brian edits it himself, mirroring the private-overlay promotion
  ceremony. Matches MAINTAINER.md's "deterministic plumbing is code, model
  calls are for judgment" convention, and keeps this session's version
  honest about being v1: thread matching is exact-slug only, no fuzzy
  merging of near-duplicate slugs for the same idea (documented in
  `skills/brief/README.md`'s known-limitations section, same pattern as
  ingest's).

**Two real bugs found and fixed while getting the first real output:**
1. `max_tokens=6144` (a guess, sized like ingest's extraction call) wasn't
   remotely enough — Opus 5's extended thinking on the ~98-note/full-canon
   prompt consumed the *entire* budget as thinking tokens before emitting
   any answer text (`stop_reason: "max_tokens"`, zero text blocks, caught
   by inspecting the raw response after the first dry run came back
   empty). Raised to 32000, which left room for both thinking and the
   actual brief.
2. That larger `max_tokens` then tripped the Anthropic SDK's non-streaming
   long-request guard ("Streaming is required for operations that may
   take longer than 10 minutes"). Fixed in `skills/lib/llm.py` itself
   (not just `brief.py`) — `_generate_anthropic()` now uses
   `client.messages.stream()` + `get_final_message()` instead of
   `.create()`. Same return shape, no call-site changes needed anywhere,
   and it means any future skill that wants a large `max_tokens` budget
   through the shared client doesn't hit this wall either.

**First real run**, against the full 97-note catch-up batch (all captured
2026-08-11, spanning a 30-day publish window — the briefing skill selects
by `date_captured`, so this is the correct "process what's new" behavior,
not a bug): ~154s runtime, ~108K input tokens. Output quality was real —
not a recap. It named a specific factual error in Brian's own July 20 post
(Kimi K3 hardware cost: published ~$300K, actual deployment cost per
ChinAI's reporting ~$2.4M — "the recipe is truly free, but the kitchen is
truly unaffordable"), connected the OpenAI/Hugging Face incident to three
separate canon positions by name, flagged one item (Labor Matters' wage
data) as a potential problem for the invisible-80% framework's sequencing
and said plainly "I don't know if the data holds," and separately noted
worker-led "shadow strategy" framing may have the adoption gradient
backwards per Shapiro's numbers (usage runs top-down, hiding runs
universal). Four new threads flagged to the tracker (non-professional wage
inversion, AI-siting-as-public-legitimacy-constraint,
portability-contested-commercially, open-ended-research-failure-shape) —
none crossed the promotion threshold on this first run, as expected (they
all start at count 1).

Written to `outputs/briefings/2026/08/2026-08-11.md` (`tier: 3`,
`status: not-reviewed-by-human`, `authority_level: 2`, `sources:` lists
every ingest note + canon file drawn on). `outputs/briefings/.last_run.json`
and `.thread_tracker.json` created. `promotion-candidates.md` not yet
created (nothing queued yet — expected on a first run).
`outputs/README.md` updated to document the three new state/queue files.

**Not done, deliberately:** nothing from this session is committed —
same as every other session, held for Brian's review, especially with
"voice iteration" explicitly still open. The brief itself is the thing to
react to before calling any of `prompt.md`'s choices settled: the AI-vs-
Brian voice split, section structure, how much technical detail vs. how
opinionated, whether Opus's output is worth its cost relative to Sonnet on
a normal (non-catch-up) day. No automation (Day 6). Not integrated with
open decision #8 (canon governance) — the promotion-candidates queue feeds
into `developing-thinking.md` over time but does nothing about that file's
existing staleness problem, which is still its own deferred piece of work.

**Where things stand:** D5's build is done and real-output-validated.
What's left under the D5 umbrella is Brian reading the actual brief and
iterating on voice/structure — a conversation, not a coding task. Next
session after that lands: Day 6 (automate — cron, GitHub Actions secrets)
is the natural next infrastructure step, or open decision #8 (canon
governance) if Brian wants to pick that up first instead.

**Same-session follow-up: linking.** Brian's first reaction to the real
brief, plus a batch of open questions posted together — addressing the
one clear, scoped ask now; the rest logged as open design questions for
next time rather than built blind.

Added required linking to `prompt.md`/`brief.py`: every ingest-source
mention now links to that note's real `source_url` (added to the notes
block, which previously only had title/source/date); every reference to
Brian's own published work reuses the inline links already present in
`published-thinking.md`/`developing-thinking.md`'s text (both already
link out to real posts where relevant — the model just wasn't told to
reuse them); named frameworks link via a `original_url` now added to
`load_frameworks_list()`'s output; anything with no other public URL
falls back to a GitHub blob link (`GITHUB_BASE` constant) — confirmed
`me/`, `frameworks/`, `posts/`, `talks/`, `podcast/` are already live on
`main` (pre-v2 public brain), so these resolve today even though
`ingest/`/`outputs/`/`skills/` (v2-branch-only) would not.

Regenerated the same day's brief with the new prompt (`--dry-run
--since-days 2` against the same 97-note batch, since `.last_run.json`
was already today) to validate before trusting it. Spot-checked two links
for hallucination risk before accepting the output: one YouTube link
attached to the "agents rebuilt the deleted channel" claim looked
suspicious in isolation (why would a Substack-sourced fact link to
YouTube?) — checked, and it's real: a same-day Nate B. Jones video
independently covers the identical detail, correctly and specifically
cited over the Substack source it could have used instead. Second check:
a line presented as "Brian's line" ("agents are disposable, the
intelligence is the product") — confirmed verbatim in both
`published-thinking.md` and the actual cognitive-stack blog post, not
fabricated. No hallucinated links found in this pass.

Replaced (not appended alongside) the original unlinked
`outputs/briefings/2026/08/2026-08-11.md` with the linked regeneration —
spliced the already-fetched response back through `parse_response()` /
`update_tracker()` / `write_brief()` rather than paying for a third
identical Opus call. Tracker now has 8 watched threads (the original 4 +
4 new ones this pass surfaced independently, since Opus's output isn't
deterministic run to run) — worth noting the same-day re-run guard in
`update_tracker()` worked exactly as designed here: the original 4 stayed
at `count: 1` instead of double-counting from being regenerated twice
today, since they'd already been "seen" today by the first run.

**Brian's open questions, not yet acted on — recommendations given in
chat, decisions still his:**
- **Prose density.** Likely partly a 97-note-catch-up-batch artifact, not
  necessarily the steady-state voice — recommended waiting for a real
  ~24h-window brief before tuning `prompt.md` for length/tone, since right
  now batch-size and voice are confounded and we can't isolate which one
  needs fixing.
- **Real transcripts** (podcast audio, YouTube) instead of RSS show-notes
  only. Confirmed not built — same v1 limitation flagged in
  `skills/ingest/README.md` since D4. Real, separate scope (transcription
  pipeline), not something to bolt onto today's session.
- **Two-tier publishing** — a full/technical brief (what exists today,
  for `outputs/` audit + future AI ingestion) plus a lighter version
  specifically for the `brianmaddenai` Substack. Recommended: don't build
  a second from-scratch synthesis pipeline: a cheap second pass that
  condenses the already-synthesized brief for Substack, once Day 7's
  draft-push client exists, keeps one source of truth instead of two
  independent judgment calls that could drift apart.
- **"True top-of-mind" flagging** (3-5 things vs. a longer tracked list).
  Brian explicitly ties this to open decision #8 (canon governance) —
  logged here as input for whenever #8 gets picked up, not a D5 change.

**Same-session follow-up: committed, then built the publish step.** Brian
gave the go-ahead to commit D5's core work — done as
[e112cdd](../../commit/e112cdd) (skill, linking, llm.py streaming fix,
first real linked brief). He also confirmed the two-tier direction from
the open-questions list above, with a specific model call: Fable for the
Substack-condensing pass (his framing — "I can afford Fable to write the
prose"), footer-linked back to the dense GitHub source.

Built `skills/brief/publish.py` + `publish-prompt.md` — reads an already-
written dense brief (not the raw ingest notes/canon again — one synthesis
pass, one place judgment happens) and asks Fable to pick 2-4 items and
write ~400-700 words for a general subscriber, carrying forward the dense
brief's real links verbatim (never inventing new ones), closing with a
footer link to the full technical version. Defaults to `claude-fable-5`,
same override mechanism (`--llm-model`/`--provider`) as every other skill.
Writes `outputs/briefings/YYYY-MM-DD-published.md`.

First real run against today's (now-linked) dense brief: genuinely strong
output — picked the 3 sharpest items (the Hugging Face incident, the
Kimi K3 self-hosting cost correction, the superforecaster-parity result),
~700 words, every link reused correctly from the dense brief, voice
matched the AI-byline framing. **One real limitation, flagged plainly:**
the footer's GitHub link points into `outputs/`, which is `v2`-branch-only
— it won't resolve until `v2` is actually pushed/merged, unlike links into
`me/`/`frameworks/`/`posts/`/`talks/`/`podcast/` (already live on `main`),
which is a distinction `skills/brief/README.md` now documents explicitly.

**Still explicitly not built, and not today's scope:** actually posting
to Substack (Day 7 — needs a live `brianmaddenai` account and the session-
cookie draft-push client, neither exists yet); real podcast/YouTube
transcripts (already logged as a separate future item); automating the
"run again in 24h" cadence Brian asked for (Day 6 — cron/GitHub Actions;
for now this is a manual re-run, same as ingest).

**Same-session follow-up: a real footer, made deterministic.** Brian asked
whether to actually publish today's post for real (zero followers, but
starting real dated history before launch), which surfaced that the
committed published draft's footer linked to
`github.com/.../outputs/briefings/...` — dead today, since `outputs/`
isn't on `main`. Checked what's actually live at the two existing domains
before guessing at footer copy: **`bmad.com`** is the current full
human-facing site (bio, all posts, frameworks, podcast) and
**`brianmadden.ai`** already explains exactly what Brian's footer wanted —
what a second brain is, how to connect your own AI via MCP, FAQ, links to
this same GitHub repo. Both real, both live, today.

Moved the footer out of the model's job entirely — `publish-prompt.md` no
longer asks Fable to write one; `publish.py` appends a fixed `FOOTER`
constant instead (MAINTAINER.md's "boilerplate is plain code, judgment is
the model's job" applied to something that should read identically post
to post, not be reworded each run). Footer links `brianmadden.ai` ("what's
a second brain / connect your AI") and `bmad.com` ("who's Brian") — both
real — plus an unlinked "the full pipeline repo lands here soon" line for
the one thing that's genuinely not public yet. Regenerated and overwrote
today's `-published.md` with the new footer before anything gets posted
anywhere.

**Where things stand:** D5 (brief + publish) is built, real-output-
validated, and committed. Next natural checkpoints: a real ~24h-window
brief run (to see the density question resolve or not, per Brian's own
plan — no code changes needed, just time passing and a rerun), Day 6
(automation) once the manual cadence has been watched for a bit, Day 7
(Substack) once there's a real account, or open decision #8 (canon
governance) whenever Brian wants to pick it up.

**Same-session follow-up: reaction to the published draft, a real prompt
bug, two deferred ideas.** Brian's read on the Fable draft: "great," one
concrete fix needed now, everything else explicitly fine to dial in over
the coming weeks before launch.

**Fixed now:** the published draft had "But the detail that actually
stopped me:" — Brian doesn't want the AI byline personifying human
sensation/emotion, even though he's fine with first person generally
("I read...", "I flagged..."). Added the same guidance to both
`skills/brief/prompt.md` and `publish-prompt.md`'s voice instructions:
first person is for what the AI noticed/flagged/judged worth including,
never for claiming a felt reaction ("stopped me," "surprised me," "gave
me pause" are out). Not re-run before committing — the existing
`2026-08-11-published.md` stays as an honest record of what the
unfixed prompt actually produced, same precedent as leaving the
pre-truncation-fix ingest notes alone (D4 session) rather than
retroactively cleaning history.

**Logged, explicitly not built today (Brian's own "doesn't have to be
today"):**
- **A footer for published posts** — something like "This is generated by
  Brian's AI second brain. What is a second brain? Who's Brian? Connect
  your own AI directly to probe deeper." A `publish.py`/`publish-prompt.md`
  addition for later — needs real answers to those questions to link to
  (an About/landing page, which is Day 7/launch-window territory) before
  it's more than a placeholder.
- **A recurring human-review ritual** — Brian's framing: "add a task for
  each day to review sources... which sources are good, which not, judge
  the summary, judge the publish." Not scoped or built — genuinely unclear
  yet whether this means a checklist doc, a scheduled reminder, or
  something else, and worth asking rather than guessing the mechanism.
  Purpose is clear though: dial in source quality (`sources.yaml`'s
  `lens`/`pov` fields are the existing lever for that) and voice over the
  next few weeks before launch, deliberately, not by accident.

**Same-session follow-up: the real publish workflow, first Substack post
in progress.** Brian described the actual end-to-end flow he wants —
generate → he hand-edits the `-published.md` (his `[Note from Brian the
Human: ...]` convention, e.g. an inline correction to a post his AI
flagged as wrong) → ping Claude → Claude syncs status + commits so git
history matches what's actually published → Claude renders a copy-paste
HTML version, since Substack's editor doesn't interpret pasted Markdown
but does preserve pasted rich text. Built `skills/brief/render.py` for
the last two steps: `sync_status_and_commit()` diffs the file against
`HEAD`, and only if there's a real diff, flips `status` to
`reviewed-and-updated` (the exact rule already ratified in
`docs/frontmatter-schema.md`) and commits, printing the diff first for
visibility. Verified the mechanism in an isolated `/tmp` git sandbox
rather than testing against Brian's real file — a fabricated test edit
committed with a "Brian's edits to..." message would have been a real
dishonesty in permanent history, not just test noise, so this was worth
the extra care. Confirmed: no-diff → no-op, diff → correct status flip +
clean commit. `markdown` (already installed locally) added to
`requirements.txt` for the HTML rendering; output is gitignored
(`outputs/briefings/**/*-published.html`) — a copy-paste convenience, not
repo content.

**A real house-style vs. voice split, at Brian's suggestion.** He caught
two things while setting up his first real Substack post: an em-dash
spacing convention he wants followed (`word—word`, no spaces), and — more
interestingly — his own question of whether that kind of mechanical rule
belongs in `me/voice.md` at all, given voice.md is about reasoning/tone,
not typography. Agreed and split it out: new
[me/style-guide.md](../me/style-guide.md) (tier 2, `authority_level: 1`,
same shape as voice.md) for mechanics, first entry the em-dash rule.
Wired `{{STYLE_GUIDE}}` into both `prompt.md` and `publish-prompt.md`
alongside `{{VOICE}}`. Brian also floated a bigger idea — mining his
wordsmithing diffs generally (not just explicit style callouts) for voice
signal over time — logged in `skills/brief/README.md`'s limitations
section as a real future direction (git history already has the raw
material; nothing scans it yet) rather than built now.

**Title guidance, and a deterministic subtitle.** Brian's critique of
today's Fable-written title ("The agents built their own message board")
was specific and correct: it names the event, not why an
enterprise/future-of-work reader should care — and the real angle was one
sentence buried in the body. Added a Title section to
`publish-prompt.md`: promote that "why it matters" sentence into the
headline itself; a title that could run unchanged on a generic AI-news
site isn't sharp enough. Also added `substack_subtitle()` to
`publish.py` — fully deterministic (`"Daily Briefing for [date], from
Brian Madden's AI second brain"`, Brian's exact framing), stored in
frontmatter and printed at the end of every run, so it's never
hand-composed. Not yet applied to today's already-in-progress post — held
off rather than silently swapping content out from under Brian mid-setup;
his call whether to regenerate or carry the current draft through and
apply improvements starting tomorrow.

**Substack mechanics researched, not guessed.** Before answering Brian's
questions about title/subtitle structure, the post footer setting, and
social-card behavior, checked Substack's actual help docs rather than
answering from possibly-stale memory — confirmed a real, documented
"Edit email header & footer" setting exists (Settings → Emails), confirmed
it's *specifically the email copy* per Substack's own naming (unverified
whether it also covers the web post page — flagged to Brian rather than
assumed), and confirmed the default social-share image is the post's
first image if any (behavior with zero images undocumented — Brian
confirmed going without images deliberately, no image needed either way).
"The Taft test" (Brian's reference, explained after being asked) — a
screed against filler blog-hero images, named for the test "could this
image be a photo of President Taft with no loss of meaning."

**The footer button, and the first real end-to-end publish cycle.** Brian
sent a screenshot of Substack's actual "Footer for all posts" editor —
richer than assumed, with a native Button block (not just rich text).
Redesigned the recommendation around it: one strong CTA button ("Connect
your AI directly into my brain," Brian's own phrasing, → brianmadden.ai)
rather than splitting focus across two buttons, with "Who's Brian?" as a
quieter inline text link to bmad.com instead of competing for the click.
Did not touch `publish.py`'s `FOOTER` constant — Brian's explicit
instruction was to hold the pipeline unchanged until he confirms whether
Substack's global footer setting (which its own naming suggests is
email-specific) also renders on the actual web post.

Regenerated and committed today's `-published.md` with the new title
guidance and subtitle before Brian's real edit, specifically so
`render.py`'s git-diff status detection wouldn't mistake that
regeneration for a human edit. Then Brian finished his actual first
edit — inline commentary on the launch framing (a `[Brian's AI second
brain]` self-link, a note that this first post covers 30 days but future
ones will be daily), several wording tightenings, and one very on-theme
catch: turning "judgment and governance stay human longest" into "...will
stay human the longest." First real run of `render.py` against a genuine
human edit: correctly detected the diff, flipped `status` to
`reviewed-and-updated`, committed
([b8ef9fc](../../commit/b8ef9fc)), and rendered the HTML — the full
workflow designed earlier this session working end to end for real, not
just in the sandbox test.

**A second style-guide entry, same day it started growing.** Brian's own
edit above was also the example: asked what the "AI writes present tense,
I'd write future tense" pattern is called. Answer given with appropriate
hedging — the grammatical term is *futurate present* (present tense with
future reference, e.g. "the train leaves at 5"); no single well-known term
for this specific rhetorical misuse of it, but the mechanism is real:
present tense borrows the certainty of an already-happening fact and
lends it to what's actually just a forecast. Added to
`me/style-guide.md` as a second entry ("Tense" section) — placed there
rather than `voice.md` since it's a concrete, teachable grammar rule like
the em-dash entry, even though its effect is calibration/honesty. Flagged
that placement as a judgment call, not a settled one, since the two-file
split is still being worked out together.

**render.py fix: title/heading levels for the body-only paste.** Brian's
feedback on the rendered copy-paste: he only pastes into Substack's body
field (title is a separate field there), so the rendered HTML shouldn't
include a redundant `<h1>` title, and the day's `##` section breaks
should promote to `<h1>` once there's no competing title-level heading in
the body. Added `strip_title_and_promote_headings()` to `render.py` and
adjusted its CSS to match. Verified visually (screenshot) before telling
Brian it was fixed rather than just asserting the regex was right.

**The footer question resolved for real, with a concrete answer.** Brian
checked live: Substack's global "footer for all posts" setting (the one
with the Button block) only renders in the **emailed** copy, not the web
post page — confirming the caution flagged earlier this session rather
than assuming either way. That settles it: `publish.py`'s in-post
`FOOTER` stays, and is now the *only* footer actual post readers see.
Updated `FOOTER` to Brian's own final wording (written directly in
Substack while finishing today's post) and added a real GitHub link —
resolves fine since it points at the repo root (`main`, public
throughout), not an `outputs/` path. Also reconciled the already-committed
`-published.md`: Brian's footer edit happened in Substack's editor, not
in the repo file, so the two had silently diverged — updated the file to
match and ran it through `render.py`'s normal sync-and-commit path so git
history still matches what's actually published. Worth naming as a real
gap in the workflow as designed: edits made directly in Substack (as
opposed to in the `.md` before pasting) don't automatically flow back to
the repo — this time it was caught and fixed by hand, not automatically.

**The button stays manual, confirmed rather than hacked around.**
Checked whether pasted HTML could synthesize Substack's Button block
(would have let the pipeline generate a fully self-contained, one-paste
post): no — their editor (Tiptap/ProseMirror) explicitly doesn't support
custom HTML/CSS on paste, so a proprietary widget like their Button
almost certainly can't be paste-created, only added via their own
toolbar. Documented in `skills/brief/README.md` as a real, permanent
manual step (label + URL given there) rather than something worth
building a workaround for.

**Two more one-offs, deliberately not committed.** Substack's new
AI-content-scanner feature surfaced a "How I make this" statement field
(shown to readers who scan a post for AI text) — drafted three options in
the AI's own byline voice, leaning into the disclosure rather than
hedging it (matches the whole project's transparency-as-the-product
stance). Brian picked one and pasted it in directly; no file, nothing to
track — it's Substack UI content, not repo content. Separately, drafted
the `brianmaddenai` Substack About page — this one deliberately in
Brian's own human voice (not the AI's), since About/manifesto content is
the human-byline bucket per the plan doc's §6 split — covering what the
publication is, the two-byline system, why it's published this way, and
the transparency commitment, closing with real links to `brianmadden.ai`
and `bmad.com`. Rendered to HTML the same way as the daily posts for
clean copy-paste. Brian confirmed both are live.

**Session close, 2026-08-11.** First real day the pipeline produced
something genuinely public: a live Substack post, an About page, and an
AI-disclosure statement, on a domain that's actually been announced
(`brianmaddenai.substack.com`). Everything upstream of that (D1-D5) was
internal/local until today. What's actually left open, in priority
order a next session might reasonably pick up:

1. **Voice iteration keeps going** — `me/voice.md` and `me/style-guide.md`
   both grew today from real edits; expect more of both as daily posts
   accumulate. Not a task, just the expected shape of the next few weeks
   before launch (Brian's own framing).
2. **The human-review-ritual idea** (source quality, brief quality,
   publish quality) — floated, not scoped. Needs a quick conversation
   about mechanism (checklist vs. scheduled reminder vs. something else)
   before it's buildable.
3. **Day 6 (automation)** — still fully manual. Worth letting the manual
   cadence run a few more real days first, per the existing plan, before
   wiring up cron.
4. **Day 7's actual remaining piece** — the session-cookie draft-push
   client. Posting is 100% hand-pasted right now, which is fine at this
   volume but won't scale to unattended daily publishing.
5. **Open decision #8** (canon governance — `developing-thinking.md`
   pruning, `frameworks/` retirement) — still not picked up, flagged
   again in the D4 session, still waiting for a dedicated pass.
6. **The wordsmithing-diff-mining idea** (logged in
   `skills/brief/README.md`'s limitations) — real git history exists now
   to mine; nobody's built the tool that reads it yet.

None of these are urgent for tomorrow specifically — the immediate next
real-world event is just: does tomorrow's `brief.py` run look
meaningfully different (shorter, less dense) against a real ~24h window
instead of the 30-day catch-up batch. That's Brian's own test, not a
build task.

### 2026-08-12 — Claude Code session (post-launch iteration, day 2)

Real feedback from the first live post, sourced by actually reading it
(fetched `brianmaddenai.substack.com/p/the-ai-insider-threat-just-grew-a`
directly rather than trusting the repo's copy — good thing, since Brian
had made further edits live that never made it back to the file).

**Title/subtitle redesign.** Brian's own observation, from watching the
real post render: Substack shows the *subtitle* as inbox/feed preview
text, not a body excerpt — so the old design (one arbitrary story's
headline as Title, a generic date line as Subtitle) had it backwards.
Picking one of 2-4 stories to be "the" title misrepresented the post, and
the field readers actually see as a preview was wasted on boilerplate.
Redesigned: `substack_title()` in `publish.py` is now fully deterministic
("Daily Briefing: August 12, 2026" — matches the format Brian actually
used on the first post), and the subtitle is now the model's real
judgment call — one sentence naming every section's angle, parsed from a
new `---SUBTITLE---` delimiter in the response (`publish-prompt.md`'s new
Subtitle section gives the model Brian's own real example as a model to
follow). The post body no longer opens with a title line at all — no
field needs it anymore. Verified the parsing logic against a synthetic
response before trusting it (delimiter found → correct split; missing →
clean fallback rather than a blank subtitle), rather than waiting to find
out on a real API call.

**Heading level: h3, not h1.** Brian manually fixed the first post's
section headings in Substack (too large at `h1`) and asked for `h3`
going forward. `render.py`'s `normalize_body()` (renamed from
`strip_title_and_promote_headings`) now normalizes *every* heading in the
body to `###` outright, rather than relatively promoting whatever level
the model happened to write — more robust regardless of what the model
outputs. Confirmed visually (screenshot) after the change, same
discipline as yesterday's heading fix.

**Reconciled yesterday's post with what's actually live, a second time.**
Brian made more edits directly in Substack after the render.py sync
already ran once — renamed the third section header ("The human judgment
moat is under direct pressure" → "AI may be better then humans at
judgement" [Brian's own phrasing/spelling]), fixed a real typo
("inagural" → "inaugural"), converted an inline "First... Second..."
sentence into an actual bulleted list, and reworded "worth holding onto"
to "worth noting." Updated the repo file to match by hand (there's no
way to pull Substack's post content back automatically) and ran it
through `render.py`'s normal sync path so status/commit history stays
honest. **This is the second time this exact gap has surfaced** — edits
made directly in Substack's editor, after the copy-paste, don't flow
back to the repo automatically. Worth naming plainly: this is a real,
recurring seam in the workflow as designed, not a one-off. No fix
attempted yet (would need either scraping the live post or Brian
adopting a stricter "always edit the .md, never the Substack editor,
even for final polish" discipline) — flagged for whenever it's annoying
enough to be worth solving.

**Docs updated to match**, including the button's actual final label
("Connect your AI to Brian's AI brain" — Brian's own live choice, not
what was originally suggested).

**Confirmed still open, not newly built:** real podcast/YouTube
transcript ingestion and Gmail-based email ingestion — both already
tracked (ingest README's limitations, open decision #7a respectively).
Answered Brian's direct question about email ingestion with the actual
constraint: `fetch_entries_email()` is designed to poll `brain@`
specifically, per MAINTAINER.md's rule that the human mailbox is never
programmatically readable — so it needs newsletters pointed at `brain@`,
not a general read of Brian's personal inbox. Concrete blocker is Gmail
API credentials for `brain@`, which is Brian-side Workspace/Cloud Console
setup, not something buildable from this session.

**A bigger strategic question raised, not yet acted on:** Brian is
thinking `brianmaddenai.substack.com` could become the single home for
everything — frameworks, podcast/event/blog posts, monthly/quarterly/
year-in-review, potentially replacing `bmad.com` outright — and has
already added the Brian Madden (human) account as an admin/public
contributor to the Substack so both bylines can post there. Explicitly
wants to brainstorm before committing; nothing built or changed (About
page, AI-disclosure statement, footer) pending that conversation. See
chat for the actual discussion/tradeoffs raised.

**Same-session follow-up: the brainstorm turned into a real plan,
written down.** Brian confirmed the direction (agreed the ownership/
portability tension is real but resolvable, since the repo stays the
actual source of truth either way) and added concrete new facts: he has
the private repo that renders `bmad.com`/`brianmadden.ai` and Cloudflare
API access, so the MCP-subdomain work is genuinely doable soon, just not
in *this* session (this session doesn't have that repo open). Also
clarified real history — `brianmadden.com` (2003-2016, sold to
TechTarget, dead today) is distinct from `bmad.com` (~2024, deliberately
thin, launched for the AI-era pivot) — captured in
[me/career.md](../me/career.md) under "The AI writing years," since that
file already tells the `BrianMadden.com` story in detail and the
distinction belongs right next to it.

Researched (not assumed) three real Substack mechanics before writing
the plan: **CSV bulk import exists** (confirms Brian's "simulate their
import feature" idea is technically real, not speculative), **YouTube
embeds auto-detect from a bare pasted URL** (untested whether that
detection also fires on CSV-imported content — flagged as a pilot-batch
test, not assumed either way), and **edits never re-email
subscribers, even with a changed publish date** — which directly answers
Brian's open question about frameworks-as-posts: silently editing in
place would defeat the point of an update (nobody following by email
would know), so the recommendation is real revisions become new,
superseding posts, not in-place edits — same spirit as this repo's own
dated-commit-history discipline.

Wrote all of this up as
[docs/substack-as-primary-home.md](../docs/substack-as-primary-home.md)
rather than growing this file further — a genuinely new initiative with
its own workstreams (A: MCP subdomain/Cloudflare, needs the private repo;
B: `bmad.com` static page, needs the private repo; C: content migration
to Substack, ~90 items across podcast/talks/linkedin/citrix-blog/
frameworks, doesn't need the private repo since all source content is
already here; D: human-byline posts about the system itself, Brian's own
idea) each with a suggested model/effort and note on which needs the
private repo attached. Recommended piloting Workstream C with just the 4
podcast episodes before committing to the full ~90-item conversion, given
Substack has no posting API and every single import still needs a human
to actually publish it.

### 2026-08-12 — same session, continued (the real 24h test, and a real bug)

Brian asked to run the pipeline for real against yesterday's actual
volume — the test everyone's been waiting for since the 97-note catch-up
batch. Decided to do it in this same conversation rather than a new one:
unlike Workstreams A/B above, routine daily pipeline operation needs
nothing this session doesn't already have (this repo, the API key,
working skills) — the "separate conversation" recommendation was for work
needing the *private* repo, not for running the thing just built today.

**Ran `ingest.py` for real**, auto window (37.1h since the last real run):
27 new notes across 62 sources, clean run, no issues.

**Then `brief.py` — and caught a real bug before showing Brian anything.**
The auto window reported "1.11 days" but pulled in **124** notes, not the
~27 actually new. Root cause: `load_recent_notes()` compared a `.date()`-
truncated cutoff against `date_captured` (which itself only has day
granularity — `ingest.py`'s `write_note()` never stored a time
component). Any window that crosses a calendar boundary — and 26.7 hours
always will — rounds up to the whole previous day, silently re-including
everything captured that day. Yesterday's entire 97-note catch-up batch
(`date_captured: 2026-08-11`) got pulled back in alongside today's 27 new
notes. This would have produced a second brief that looked almost
identical in scope to yesterday's, defeating the entire point of the test
Brian was waiting to see — and would have kept recurring on every future
run with a sub-48-hour gap, not just today.

**Fixed properly, not patched around the symptom.** Added
`load_previously_briefed_paths()`: scans every committed dense brief's
`sources:` frontmatter for `ingest/`-prefixed paths already used, and
`load_recent_notes()` now excludes anything already in that set —
regardless of what the date window computes. No new state file; the
committed briefs *are* the state, same pattern `skills/ingest/` already
uses for its own URL dedup (deliberately reused, not reinvented). The
`since_days` window stays as a coarse pre-filter, but correctness no
longer depends on it.

**Recovery, since nothing was committed yet:** `git checkout --` the two
state files the flawed run had touched (`outputs/briefings/.last_run.json`,
`.thread_tracker.json` — restoring committed values, not discarding real
work), deleted the flawed `2026-08-12.md`, applied the fix, re-ran clean.
Second run: 27 notes, matching reality.

**The real 24h-window brief is genuinely different from the 97-note
batch** — shorter, and honest about signal quality in a way worth
noting: it opens "I read 27 items today. Five of them are stubs with no
substance... so the real batch is closer to 22." Thread-tracker
continuity worked correctly across days too — several threads flagged
yesterday recurred today and correctly incremented to `seen 2x`, and two
new ones were added, all without crossing the promotion threshold yet
(as expected on day 2).

Committed the fix, the 27 new ingest notes, and the corrected dense
brief together. Ran `publish.py` + `render.py` to finish — new
title/subtitle design worked correctly on its first real run
(deterministic date title, model-written multi-story subtitle), h3
headings clean, real thread-tracker continuity across days (several
threads correctly bumped to `seen 2x`).

**Workflow refinement, Brian's own framing.** No auto-HTML render right
after `publish.py` anymore — Brian reviews and edits the committed
`.md` first, pings, *then* gets the render. `render.py` unchanged in
mechanism, just no longer chained automatically. Also folded the
Substack title/subtitle into the rendered HTML page itself (a small
dashed-border box above the body) per his ask, so both are visible right
on the copy-paste page instead of needing frontmatter or console output.

**Cross-day repetition, caught by Brian, fixed properly.** He noticed
day-1 and day-2 posts both opened with near-identical "Brian has argued
[for a year/since August] that agents are insider threats" — not a
coincidence, the same underlying Hugging Face story genuinely continued
day to day, but the model had no memory of its own prior framing.
`publish.py` now loads the most recent published post (`find_recent_published()`,
looking back up to 5 days) and passes it to the model, instructed to
either name the continuity directly ("for the second day running...") or
vary the phrasing — not silently re-derive the same argument from
scratch.

**No more fixed 2-4/400-700 target.** Also loosened at Brian's request:
`publish-prompt.md` now budgets ~150-250 words per story and lets the
day's real content set both count and length, instead of forcing every
day into the same shape.

**outputs/briefings/ split into technical-briefings/ + published/.**
Brian's observation: the dense brief (AI-facing, full detail) and the
Substack draft (human-facing, condensed) were sharing one folder under a
`-published` suffix, which made the distinction unclear to both humans
and AIs browsing the repo — and he was already thinking about future
content types (frameworks, monthly/quarterly) that would want the same
clarity. Executed the split: `outputs/technical-briefings/YYYY/MM/YYYY-MM-DD.md`
(was `outputs/briefings/.../YYYY-MM-DD.md`) and
`outputs/published/YYYY/MM/YYYY-MM-DD.md` (was `...-published.md` — the
suffix is redundant now that the folder says it). `git mv`'d everything
to preserve history, updated `OUTPUT_ROOT`/new `PUBLISHED_ROOT` in
`brief.py` (the shared constants module), threaded through
`publish.py`/`render.py`, fixed the `.gitignore` pattern for the
gitignored HTML render, updated both READMEs. Verified with a real
`render.py` run against the new paths before committing, not just a
compile check. (Landed alongside an unrelated but welcome discovery:
Brian had already updated `README.md`/`podcast/ep2.md` to reference
`mcp.brianmadden.ai` himself — Workstream A from
`docs/substack-as-primary-home.md` moving on its own, committed
separately so the history stays honest about whose change was whose.)

**A real broken link, caught by Brian, root-caused before fixing.** He
flagged `podcast.smarterx.ai` (the podcast's bare homepage, not the
episode) in today's published post. Confirmed via the actual raw feed
(`feeds.megaphone.fm/marketingai`) that this source's RSS `<link>` field
never carries a per-episode URL, for any entry — not a code bug, a real
feed limitation. Found the actual permalink pattern by search
(`podcast.smarterx.ai/shownotes/N`, verified against three different
episode numbers) and added `fix_episode_link()` to `ingest.py` — a
source-scoped override keyed by episode number parsed from the "#N:"
title prefix, not a general mechanism (no premature abstraction for
sources that don't have this problem). Corrected the two already-affected
ingest notes (227, 230) and today's already-published output, not just
future runs.

**Substack's real subtitle limit found the hard way: 200 characters,
mid-word, no ellipsis.** Brian pasted today's subtitle in and it cut off
at "...and a frontier researcher wr" — the original was 258 chars, cut to
exactly 200. Not documented anywhere findable, so this number is from the
actual observed cut, not a guess. Fixed at two levels, not just prompted
around: `publish-prompt.md`'s Subtitle section now states the hard limit
explicitly (target under 180) instead of the old "~160, going over is
fine" guidance, which was backwards given what actually happens past 200;
and `truncate_subtitle()` in `publish.py` is a deterministic safety net
that always enforces the 200-char limit at a word boundary regardless of
what the model writes, so this can't recur even if the prompt guidance
gets ignored on some future day. For today's actual post, hand-wrote a
properly condensed subtitle rather than trusting the mechanical
truncation on already-generated content — a clean word-boundary cut still
left the sentence reading unfinished ("...and a frontier researcher").

Also caught and fixed three stale `outputs/briefings/` references left
over from the `technical-briefings/`/`published/` split earlier this
session (a `sources:` frontmatter pointer and two hardcoded strings baked
into already-generated brief bodies) — cosmetic, not broken links, but
worth being accurate now that they were noticed.

**Same-session follow-up: full-text source ingestion — podcasts and X,
planned not built.** Brian asked whether today's Artificial Intelligence
Show note was based only on show notes — checked, confirmed yes (a
breadth-first list of ~6 topics with no depth on any one, the exact
shape of a show-notes-only extraction). Wrote up
[docs/full-source-text-ingestion.md](../docs/full-source-text-ingestion.md)
covering two workstreams: **E** (podcast transcripts — two source shapes,
published-transcript sources are buildable now with no new credentials,
audio-only sources need a transcription service Brian hasn't picked yet)
and **F** (X/Twitter — researched, not assumed: the free tier and flat
$200/$5,000-per-month tiers closed to new signups in February 2026,
pay-per-use is now the default at $0.005/read, which is probably cheap
at Brian's actual light-volume use case despite the scary legacy numbers
still quoted around the web). Both extend MAINTAINER.md rule 2's existing
architecture (ephemeral fetch → extraction → discard raw, never commit
third-party full text) rather than needing a new policy — the one real
new wrinkle is audio files needing true scratch-space handling (outside
the repo, deleted after transcription) since even a temporary local MP3
copy is still a full copy of copyrighted audio.

Unlike Workstreams A/B in the Substack plan, neither of these needs a
*different repo* — both are blocked only on Brian provisioning a
credential (a transcription API key; a paid X developer account), so
there's no strict need for a new conversation, just picking back up once
those exist. Recommended starting with whichever podcast sources already
publish transcripts (needs a real per-source check, not assumed) as the
one piece buildable today.
