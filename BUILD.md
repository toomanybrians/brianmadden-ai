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

1. Commit `ingest/` Tier-1 notes publicly, or keep pipeline-local?
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
6. **Per-source trust/lens on the ingest pipeline (flagged 2026-08-10,
   design TBD).** Brian wants the ingest skill to treat sources differently
   based on his personal read of them — some he respects and specifically
   wants dissenting takes from; some are "meh"; some he thinks are wrong
   most of the time but occasionally surface a real nugget worth catching.
   Open question: a quantitative rating per source, a free-text lens/note
   per source, or both? This is distinct from `authority_level` in
   [docs/frontmatter-schema.md](docs/frontmatter-schema.md), which scores
   *our own output* for consuming AIs — this would live on `sources.yaml`
   entries and shape how the ingest skill *extracts and frames* insights
   from a given source (e.g., "surface disagreement," "skim for nuggets,
   discount the framing"). Design when the ingest skill (D4) is actually
   being built — flagged now so it isn't lost.
7. **Substack + email newsletter ingestion (flagged 2026-08-10, design
   TBD; partially actioned same day — see session log).** Brian has a
   personal Substack account with a bunch of subscriptions, now largely
   folded into `sources.yaml` (30 added — see log). Two things still open:
   (a) a separate pile of non-Substack email newsletters Brian wants
   ingested by pointing them at `brain@brianmadden.ai` and pulling via an
   app key (Gmail API, consistent with §5's existing plan for the
   `ask@`/intake lanes) rather than RSS polling — the ingest skill needs an
   email-source path alongside the feed-poll path, not just more
   `sources.yaml` rows; (b) going forward Brian plans to subscribe to *new*
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

## Day plan (checklist — details in the plan doc §8)

- [ ] D1 — Workspace + aliases + MX · lock naming · carve-out note sent
- [x] D2 — scaffold structure on `v2` · CLAUDE.md reviewed by Brian
      (scaffolding done; Brian's review of CLAUDE.md/AGENTS.md still open)
- [x] D3 — sources.yaml curated (51 sources, 50 with a live feed_url)
      (Substack follows → brianmaddenai account is a manual action on
      Brian's Substack, not Claude Code work — still outstanding, tracked
      in open decision #7)
- [ ] D4 — ingest skill running manually
- [ ] D5 — briefing skill, voice iteration
- [ ] Weekend — back-catalog bootstrap batch job
- [ ] D6 — workflows automated (workflow_dispatch during build; cron via main)
- [ ] D7 — Substack publication + draft-push client tested
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
