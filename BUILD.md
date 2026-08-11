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
   unchanged) but it raises `NotImplementedError` — no mailbox exists yet
   (D1/D8 not done). Still genuinely blocked on Workspace setup, not a
   design gap anymore; (b) going forward Brian plans to subscribe to *new*
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

- [x] D1 — Workspace + aliases + MX · lock naming · carve-out note sent
- [x] D2 — scaffold structure on `v2` · CLAUDE.md reviewed by Brian
      (scaffolding done; Brian's review of CLAUDE.md/AGENTS.md still open)
- [x] D3 — sources.yaml curated (51 sources, 50 with a live feed_url)
      (Substack follows → brianmaddenai account is a manual action on
      Brian's Substack, not Claude Code work — still outstanding, tracked
      in open decision #7)
- [x] D4 — ingest skill built, feed-fetch/dedup verified against all 56
      sources; extraction itself untested end-to-end pending an API key
      (see session log)
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
