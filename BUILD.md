# BUILD.md — v2 rebuild journal

The working memory of the brianmadden.ai v2 rebuild. Every session (human +
Claude Code) starts by reading `CLAUDE.md`, this file, and
`docs/brianmadden-ai-v2-architecture-and-launch-plan.md` — and ends by
updating the log below. Chat threads are disposable; this file is not.

## Kickoff prompts (by session)

**Bootstrap a new session with `/maintain`** (added 2026-08-15,
`.claude/skills/maintain/SKILL.md`) — reads `MAINTAINER.md`, the live
sections of this file (Decisions made, Open decisions, Day plan, the last
2 session-log entries — not the whole journal), and real `git status`, then
reports back before anything else runs. This is the automated version of
the manual pattern below, which stays here as the historical record of the
convention it replaces, not as a prompt to keep re-typing.

General pattern for any new thread, pre-`/maintain`: **"Read MAINTAINER.md
and BUILD.md, then let's pick up where we left off."** MAINTAINER.md has the
operating rules; BUILD.md's session log has the actual state. The specific
prompts below are kept as a historical record of what each day's session was
asked to do, not as a template to re-run.

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
2. ~~Daily Brief cadence: weekdays.~~ — **confirmed 2026-08-16**, weekdays
   only, no change from the working assumption.
3. ~~Exact briefing publish time (Paris morning? US-morning for reach?).~~
   — **resolved 2026-08-16.** Splits into two different times that the
   original phrasing conflated: the automated pipeline's run time (when
   ingest + brief generation actually kicks off) vs. the post going live
   on Substack (a manual step — "Pipeline pushes drafts; human publishes,"
   per the Aug 9 decisions above — happens whenever Brian actually clicks
   publish, not something to schedule). Only the first is a real decision:
   **08:00 Paris time, weekdays**, the natural D6 cron trigger — Brian's
   reasoning, not much breaks overnight so an 8am run mostly captures the
   previous day's news anyway, and he expects to review and hit publish
   himself sometime in the 9-11am Paris window most mornings. That
   9-11am window is a habit, not a locked requirement.
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
   so. **2026-08-18 update:** the `x-timeline` source (see #7 below) already
   pulls the full home timeline of everyone the `brianmaddenai` X account
   follows in one call, not per-person entries — so if Levie's covered on
   X there, no separate `sources.yaml` row is needed regardless of whether
   he's also on LinkedIn. Brian checking now whether his X posts mirror his
   LinkedIn closely enough to skip a LinkedIn-specific entry entirely.
   ExecAI Insider Weekly stays with `feed_url: null` — real source,
   email-only, needs the email-ingestion path from #7 below, not a feed poll.
   ~~The other half of D3, moving Substack follows to the `brianmaddenai`
   account, is still outstanding — manual action on Brian's Substack
   account, not something this session can do.~~ **Closed 2026-08-18:**
   Brian checked the "Brian Madden" human Substack account — zero follows
   there, nothing to migrate. See #7 — the Substack picture just got
   bigger.
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

8. **Canon governance — largely resolved 2026-08-14, both residuals now
   built 2026-08-15.** Dedicated session: five-levels archived via the new
   `status: archived` mechanism, knowledge factory + three waves entered
   canon, 55 stale items pruned from `developing-thinking.md`,
   `brief.py` taught to skip archived frameworks. See the 2026-08-14
   canon-governance session entry. ~~Still open from this decision:~~
   **both closed 2026-08-15 — see that session entry for the full build:**
   (a) ~~the recurring staleness-triage tool~~ — built as `skills/triage/`,
   one LLM call cross-checking `developing-thinking.md`'s "What's
   connecting"/"Scratchpad" sections and active frameworks against
   `me/published-thinking.md`, writing
   `outputs/canon-triage/staleness-candidates.md` (mirror image of
   `promotion-candidates.md`), run for real (6 items + 1 framework flagged
   out of ~90/10 candidates); (b) ~~a mechanism to track "most
   front-of-mind" thinking~~ — built as a `## Right now` curated pointer
   section near the top of `developing-thinking.md` (Brian's chosen design
   over a per-item tag convention), replacing the inline "most
   front-and-center" markers from 2026-08-14 as the durable version of the
   D5-era "true top-of-mind flagging" idea. Original write-up kept below
   for the record. Raised by Brian at the end of the D4 session, after the
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

9. ~~`brain@` as a personal flagging inbox, not just a newsletter sink~~
   — **designed 2026-08-16, run live for real 2026-08-17.** See the
   2026-08-16 session entry below for the original build against a real
   6-message sample, and the 2026-08-17 entry for the first live run: 7
   real flags processed (2 follow-reminders queued, 1 screenshot
   OCR-transcribed, 2 pasted-article extractions, 1 already-tracked), no
   dry-run-only gaps found. Original write-up kept below for the record.
   ~~(flagged 2026-08-15, design TBD, not built).~~ Brian's started emailing
   `brain@brianmadden.ai` directly from `b@bmad.com` — sources to follow,
   one-time articles to ingest, ideas for later — a different shape of
   input than the newsletter mail `fetch_entries_email()`/`extract()`
   already handle well. Needs its own handling, not just the existing
   "extract insights, decide NOT_RELEVANT or not" path: at minimum, a
   personal flag email probably needs to be *routed* (new source to add
   to `sources.yaml`? one-off ingest note? a `developing-thinking.md`
   candidate? something for the future staleness-triage/promotion
   surfaces?) rather than uniformly extracted-or-skipped like a
   newsletter. Undesigned — whoever picks this up should look at a real
   sample of what Brian's actually sent before designing the routing
   logic, same discipline as every other prompt-tuning pass in this repo.

   **Two sub-questions Brian asked directly, answered in chat
   2026-08-15; the sender-verification answer was acted on 2026-08-16
   (see below), the push-vs-poll answer still stands as-is (not built,
   recommendation unchanged):**
   - **Can Gmail push rather than the pipeline polling?** Yes — real,
     documented mechanism: `users.watch()` registers a Cloud Pub/Sub
     topic; Gmail publishes a notification (double-base64-encoded,
     carrying the mailbox's new `historyId`, not the message itself) to
     that topic on every mailbox change, which a subscriber (a Cloud
     Function, or a Pub/Sub push subscription hitting any HTTPS
     endpoint — a Cloudflare Worker or a GitHub Actions
     `repository_dispatch` receiver both qualify) can react to, then
     call `history.list` to see what actually changed. Real cost: a
     GCP Pub/Sub topic to provision, and **the watch registration
     itself expires and must be renewed at least every 7 days**
     (Google's own recommendation is renewing daily) — a second
     scheduled job just to keep the first one alive, plus a real
     receiving endpoint that has to exist and stay up. For a
     once-a-day brief, this buys lower latency (minutes instead of
     up to a day) at real added operational surface. Recommendation:
     not worth it yet — Day 6's plain cron/Actions poll (still not
     built) is simpler, and nothing in the pipeline currently needs
     brain@ mail acted on faster than the next scheduled run. Revisit
     if a real use case needs near-real-time reaction (e.g. an
     interactive `ask@` flow), not for the daily-brief ingestion path.
   - **Can the sender actually be verified, or is `From:` trivially
     spoofed?** Both true at once: the raw `From:` header is spoofable
     at the SMTP envelope level (anyone can put `b@bmad.com` there),
     but Gmail's receiving MTA independently evaluates SPF/DKIM/DMARC
     for every message and stamps the verdict into the message's own
     `Authentication-Results` header — real, inspectable via the
     Gmail API (`payload.headers`), not something the sender controls.
     A message only counts as "really from `b@bmad.com`" if that
     header shows `dkim=pass` with a signing domain matching `bmad.com`
     (SPF pass alone is weaker — it authenticates the sending server,
     not the domain in `From:`, and doesn't survive forwarding).
     Trusting the bare `From:` string the way `check_unrecognized_email_senders()`
     briefly did in an earlier, since-reverted design (see the
     2026-08-13 session entries above) is exactly the gap a spoofed
     message could exploit if `brain@` ever starts triggering something
     more consequential than "write an ingest note." A `brain+trigger@`
     plus-address is a reasonable *additional* layer (an unpublished,
     unguessable address is a real bar on its own) but isn't a
     substitute for the DKIM check — plus-addressing alone doesn't
     stop someone who's seen the address once (a reply-all, a leaked
     draft) from reusing it. Recommendation if/when this gets built:
     require DKIM-pass-on-bmad.com for anything auto-actioned beyond
     writing a quarantined ingest note (which is already low-stakes
     and human-reviewed downstream), and treat a plus-address as
     obscurity on top of that, not instead of it.

10. **A web visualizer / dashboard for `developing-thinking.md` and open
    questions (flagged 2026-08-15, not scoped, "dunno if there's much
    value").** Brian floated this as a maybe, not a commitment — some
    kind of tool to browse developing-thinking's live threads, open
    questions, and (once it exists) the staleness-triage/promotion
    queues, rather than reading raw markdown. Explicitly unscoped: not
    clear yet whether this means a static-rendered page, something
    interactive, or isn't worth building at all relative to just reading
    the files. Revisit once open decision #8's residual pieces (the
    staleness-triage tool, front-of-mind-vs-background tracking) exist —
    a visualizer for a system that doesn't have those surfaces yet has
    less to show.

11. **Substack published-article formatting tweaks — resolved and built
    2026-08-16.** ~~(flagged 2026-08-15, specifics pending from
    Brian).~~ Specifics arrived same day as #9's build: inline code
    (backticks) renders oversized/odd in Substack's editor. Fixed at the
    source — see the 2026-08-16 session entry below and
    `me/style-guide.md`'s new "Substack rendering" section.

12. **Port the private brain's deeper monthly-maintenance skill (flagged
    2026-08-15, tabled — needs Brian's work login + better internet than
    he had that day).** Came up designing `/review-thinking`'s two
    cadences (see that session entry): Brian's private `bmad` brain
    already has a skill for a fuller monthly maintenance pass, and he'd
    rather port that real thing in than have this repo grow its own
    parallel version long-term. `/review-thinking`'s `full`/`monthly`
    mode (built 2026-08-15) is an explicit stopgap in the meantime — walks
    every item, not just triage flags, but isn't the real ported skill.
    Whoever picks this up: get the actual skill content from the private
    repo (needs Brian's work login), diff it against what
    `/review-thinking` already does, and decide whether it replaces the
    full-mode branch entirely or the two stay complementary.

13. ~~A weekly "how my thinking has changed" recap post~~ — **built
    2026-08-24.** Brian's actual ask, from a voice memo: not a fully
    automated post, a *ceremony* — a prep doc he reads first (week's
    daily-brief stories recapped, the promotion-candidates and
    staleness-candidates queues surfaced), then a live conversation
    walking through both queues and asking for his real takeaways, then
    a drafted **Weekly Update** post. Landed as
    `.claude/skills/weekly-update/SKILL.md` (`/weekly-update`) —
    deliberately not a script pipeline like `brief.py`/`triage.py`,
    since the whole point is Brian live in the loop, not unattended
    synthesis. Reuses `review-thinking`'s mechanics for the
    developing-thinking.md portion rather than duplicating them, and
    for the first time gives `promotion-candidates.md` (20 entries, all
    still unreviewed as of this build) an actual resolution mechanism —
    promote or reject during the ceremony, both remove the entry;
    "not yet" leaves it queued. New pieces: `outputs/weekly-updates/`
    (prep doc + finished post + `.last_run.json`, `outputs/README.md`
    updated), `skills/weekly/render.py` (Substack-paste HTML, reusing
    `skills/brief/render.py`'s generic helpers, own disclosure/footer
    for the dual byline), and a new `last_reviewed` frontmatter field on
    `me/developing-thinking.md` (documented in
    `docs/frontmatter-schema.md`) — separate from `updated`, bumped every
    ceremony run even in a quiet week where nothing else changed, so
    Brian's "timestamp the review even if nothing changed" ask has a
    real field to land in. Byline and Substack-placement questions
    (raised but left open in Workstream E of
    `docs/substack-as-primary-home.md`) asked directly and resolved the
    same session: dual byline (`brianmadden.ai` + Brian Madden), folded
    into the existing Substack structure rather than a new Section for
    now. **Run for real the same session** — see the 2026-08-24 session
    entry below for the full account: 20-item promotion-candidates
    backlog and 9-item staleness queue both cleared, two frameworks
    revised, three real writing candidates logged, first-ever finished
    Weekly Update post drafted and rendered.

14. **MCP spec 2026-07-28 ("MCP 2.0") — no action needed in this repo,
    flagged for the server repo (2026-08-18).** Brian asked whether
    anything needs to change for MCP 2.0. Researched directly (MCP's own
    blog, `blog.modelcontextprotocol.io`) rather than guessing: the
    2026-07-28 spec is real and substantial — a move from a stateful,
    session-based protocol to a stateless request/response core, plus
    header-based routing, cacheable list results, Multi Round-Trip
    Requests replacing held-open streams for elicitation/sampling, and
    authorization hardening (RFC 9207 issuer validation, a shift from
    Dynamic Client Registration to Client ID Metadata Documents). Old
    behavior (Roots, Sampling, Logging, DCR, the legacy HTTP+SSE
    transport) is deprecated with a 12-month minimum support window, not
    removed outright. This repo (`brianmadden-ai`) is content only — the
    actual MCP server (`mcp.brianmadden.ai`, a Cloudflare Worker reading
    Cloudflare KV) lives in the separate `brianmadden-ai-server` repo,
    not accessible from here. Nothing here needs to change. Whenever
    Brian's next in that repo: check what SDK/spec version the Worker
    currently speaks against 2026-07-28, particularly if it relies on
    session IDs or the old elicitation/sampling request shape — not
    urgent given the 12-month deprecation runway, but worth knowing.

15. **Thread matching in `brief.py` is exact-slug-only — the first Weekly
    Update run (2026-08-24) found a real, concrete cost of that gap, not
    just a theoretical one.** Flagged in `skills/brief/README.md`'s known
    limitations since D5, but this session's promotion-candidates review
    found it wasn't hypothetical: four separately-flagged threads
    (`emergent-agent-coordination-via-shared-storage`,
    `reasoning-trace-as-attack-surface`, `skills-as-supply-chain`,
    `agent-to-agent-contagion-via-shared-artifacts`) turned out to cite
    the *same* underlying evidence (the OpenAI/Hugging Face incident,
    Anthropic's 100k+-run finding) through four different names, and
    three more (`labs-as-compute-landlords`,
    `open-weight-floor-is-subsidized`, `labs-withholding-frontier-from-
    api`) were the same pattern at a smaller scale. Brian's proposed fix,
    asked directly this session: not a second LLM call for dedup, but a
    `prompt.md` change instructing the model to explicitly check new
    candidate threads against the existing tracker for semantic overlap
    before naming a "new" one — the model already sees the tracker's
    contents every day (per `skills/brief/README.md` step 3), it's just
    never been asked to actively cross-check against it. Scoped, cheap,
    no new architecture. Not built this session — flagged for whoever
    picks up `skills/brief/prompt.md` next.

16. **39 of 85 registered sources (nearly all `*.substack.com`-hosted
    feeds) have failed with `403 Forbidden` on every single automated
    run since the pipeline went live 2026-08-19 — silently, never
    flagged before this session.** Brian noticed today's briefing looked
    email-heavy and asked to verify the pipeline was actually working.
    It mostly was — the "brain-inbox" label is legitimate, not a sign of
    a narrower pipeline than intended — but pulling the real Actions logs
    (all 5 runs so far) found a genuine, unflagged bug: same ~39 hosts,
    same `403`, every day, plus one dead YouTube feed (404, stale channel
    ID) and the not-yet-wired `x-timeline` source (BUILD.md's own
    documented gap, not new). Tested directly: the same feed URLs return
    `200` from a non-GitHub-Actions network with the identical
    "bot" User-Agent string, ruling out a simple header fix. A live web
    search confirmed the likely cause is well-documented and not
    something a code change here can fix: Cloudflare's bot protection
    (which fronts Substack) commonly blocks datacenter/cloud-provider IP
    ranges, including GitHub Actions runners, regardless of headers —
    real workarounds are a residential/rotating proxy, an RSS-proxy
    service, or being allowlisted by the site owner (not something we
    control on Substack's end). **Brian's own proposed fix, which matches
    infrastructure this pipeline already runs reliably every day: route
    these ~39 publications through the existing `brain@` email path
    instead of RSS** — subscribe to each via the `brianmaddenai` Substack
    account with "email me new posts" on, same mechanism already
    carrying The Deep View/Superintelligence/AlphaSignal in as
    `brain-inbox` entries. This is real, manual work only Brian can do
    (subscribing + enabling email delivery per publication in Substack's
    own UI), not something this session could action — logged here so
    it isn't lost, not built. The alternative Brian also floated —
    running ingest from a residential IP instead of GitHub Actions —
    would work too but gives up the unattended-pipeline design (D6);
    email-routing is the smaller change and reuses proven infrastructure.
    Once even a handful migrate, `sources.yaml` rows should flip from
    `feed_url` to `ingest_method: email` with a `sender` field, same
    shape the 11 already-migrated newsletters use.

    **Built the same session, not blocked on the above:** `ingest.py` now
    writes `ingest/.last_run_sources.json` every full run — one record
    per registered source (`ok`/`error`/`skipped`, with reason and entry
    counts) — and `brief.py` renders it into a new "Sources checked
    today" section at the bottom of every Daily Brief (both the
    technical version and, since publish.py copies the dense body
    near-verbatim, the Substack-published one). This is the actual fix
    for "how would I know if the checking stopped working" — a source
    going quiet is now a visible line on the page itself the next
    morning, not something that requires pulling Actions logs the way
    this session had to. Retroactively reconstructed and applied to
    today's 2026-08-25 briefs from the real run's log data (no live
    Gmail/feed calls involved in the reconstruction) so Brian could see
    the real thing, not a mocked example. Also fixed in the same pass:
    the `skipped` reason now distinguishes true documentation-only
    entries (auto-registered from a real `brain@` ingestion, already
    covered via the shared `brain-inbox` source and attributed by
    `sender`) from a genuine gap (no `feed_url` and no `sender` at all)
    — today all 11 skips were the former, but the distinction matters
    for whenever that's no longer true.

    **Separately, also found and fixed:** today's published subtitle was
    the hardcoded generic fallback ("Today's AI and future-of-work
    reading...") — not a prompt-design problem as it first looked, but a
    real failure: the subtitle model call (`claude-fable-5`, 2048
    `max_tokens`) returned empty on today's unusually dense 5-story
    brief, same "thinking ate the whole budget" failure shape BUILD.md
    already documented for `brief.py`'s own Opus call, just never hit on
    this call before. Confirmed against all 5 prior runs — a first-time
    failure, not a recurring pattern. Bumped to 8192 in `publish.py`
    (`skills/brief/publish.py`), regenerated today's subtitle for real
    (a real, specific one on the first try), patched
    `outputs/published/2026/08/2026-08-25.md`'s frontmatter, and
    re-rendered + re-sent the HTML to Brian. The silent-fallback design
    itself (log a stderr warning, publish anyway) is unchanged and still
    the right call for a one-line subtitle — but it's worth noting the
    warning alone didn't surface this either; Brian spotted it by eye in
    the published post, same pattern as the sources issue above.

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
- [x] ~~Weekend — back-catalog bootstrap batch job~~ — **closed as moot,
      2026-08-16.** The Aug 9 plan (yt-dlp + transcripts + distillation
      into a new `posts/history/`) was superseded by two things that
      happened since: `me/career.md`'s 2026-08-12 clarification that the
      ~2,000-post EUC-era BrianMadden.com archive stays out of this repo
      on purpose (different era, not blended in), and the 2026-08-14
      Substack-import session that already solved the "~90-item AI-era
      back catalog" problem a different way (RSS feed fixes in the
      separate `brianmadden-ai-server` repo, not a new pipeline here).
      Checked the one remaining candidate gap — `interviews/` — against
      bmad.com's full live link list (131 links) before closing this:
      already comprehensive (Reworked, CIO, VMblog, Marketing AI
      Institute, The Economist, 5 podcast appearances, all dated and
      summarized). Brian recalled a Quartz piece too; checked bmad.com,
      this repo, and a live web search — no Quartz link found anywhere,
      and Brian doesn't have the URL either. Dropped, not chased further;
      revisit only if the actual link ever surfaces.
- [x] D6 — workflows automated. **Built and proven live, 2026-08-19/20**,
      the day the deferral note above said to revisit it: `daily-pipeline.yml`
      runs ingest → brief → publish → email unattended every weekday at
      06:00 UTC (08:00 Paris), triggered for real via `workflow_dispatch`
      first to prove it end to end. Found and fixed a real bug doing
      that first run: a push made with the default `GITHUB_TOKEN` doesn't
      cascade into other `on:push` workflows (GitHub's own loop
      prevention), so `check-docs.yml`/`sync-to-cloudflare-kv.yml` silently
      never fired for the automated commit — fixed with explicit
      `workflow_dispatch` calls from within the pipeline itself. See the
      2026-08-19/20 session entry for the full account, including the
      ingest-extraction validation bug the first real run also surfaced.
- [~] D7 — Substack publication live, **first real post published**
      2026-08-11 (manually, end to end: generate → Brian edits → status
      synced → rendered → pasted in by hand) — ahead of schedule, same
      pattern as D4/D5 landing early. Moving Brian's Substack follows to
      the `brianmaddenai` account (the other half of open decision #7) —
      **closed 2026-08-18**, moot: his personal account had zero follows
      to migrate. As of D6 above, the draft now reaches Brian by email
      automatically every morning too, not just committed to the repo —
      narrows what's actually left here to just the session-cookie
      draft-*push* client (posting to Substack itself is still 100%
      Brian, by hand — no API exists for it, D7's original scope).
- [x] ~~D8 — email lanes wired~~ — **narrowed and closed 2026-08-18.**
      Brian's call: cancel the `ask@` Q&A lane indefinitely — no near-term
      use case, not worth building against a hypothetical. The intake
      lane (`brain@`) was already fully done (open decisions #7a and #9);
      that was the only real half of D8 left. See 2026-08-18 session
      entry.
- [x] ~~D9 — 10–15 core canon assets seeded~~ — **stale checkbox, closed
      2026-08-16.** Never explicitly checked off, but effectively done
      well before today via the ongoing framework/canon work: `frameworks/`
      has 11 files (10 active + 1 archived, confirmed by listing the
      directory), `me/` has all 8 core identity/thinking/voice files.
      Matches or exceeds the original "10-15 core framework assets"
      target.
- [~] D10 → launch — daily dry run, review over coffee. **Underway as of
      2026-08-20**: D6's cron is live and will run for real tomorrow
      morning without anyone triggering it; today's manual run was itself
      the first dry run, and it's what surfaced the ingest-validation bug
      (see session entry). Not closing this yet — "daily, reviewed over
      coffee" needs a few real unattended mornings to actually claim.
- [~] Launch week — announcement essay + first public brief + landing swap.
      **Landing swap done, 2026-08-20** (~08:00 UTC): `www.brianmadden.ai`
      finished activating on Substack's side (confirmed live, real
      publication content, not a placeholder), and the
      `brianmadden-ai-server` Worker deploy went out immediately after —
      `brianmadden.ai` now 301s to `https://www.brianmadden.ai/`, verified
      with a real GET (an earlier HEAD-request check misleadingly showed
      a cached 200 first; GET is what real traffic sends). `/mcp` still
      works, `mcp.brianmadden.ai` still works. What's still actually open
      here: the announcement essay and first public brief, neither
      started.

## Session log

*Entries from 2026-08-09 (pre-repo) through 2026-08-18 (the day before
launch) were trimmed on 2026-08-24 — this file had grown to ~270KB across
41 dated entries and started breaking naive full-file reads. Nothing is
lost: the full text is in git history (`git log -p -- BUILD.md`, or
`git show <commit>:BUILD.md` for any point in time). It wasn't split into
a separate tracked file either — the actual decisions from that era
already live above in Decisions made / Open decisions, and the session-
by-session build narrative (what got read, what got tested) has little
future value now that the pipeline it describes is built and running;
git is the right tool for that archaeology on the rare occasion it's
needed, not a standing file nobody reads. This log now starts at launch
day.*

### 2026-08-19 — Claude Code session (launch day: v2 merged to `main`, D6
proven live, ingest bug found and fixed, `pages/` + email delivery built,
domain cutover started) — session ran past midnight UTC into 2026-08-20

The day Brian flagged on 2026-08-18 as his big block of time for the v2
merge and D6. All of it happened, plus more than planned — this entry is
long because a genuinely large amount landed in one continuous session.
Read the Day-plan checkboxes above for the short version; this is the
account of how each one actually went.

**The merge (PR #3).** Before opening it, discovered `main` hadn't
actually been "untouched" the whole build the way the working assumption
had it — 4 small fix commits landed there directly during August (MCP-
reference cleanup, YouTube URL formatting, an `llms.txt` count fix),
never absorbed into `v2`. Real merge conflict in exactly one file
(`llms.txt`, both sides had independently bumped the same count/version
lines); traced every one of `main`'s changes and confirmed `v2`'s version
was a strict, more-current superset, so resolved in `v2`'s favor rather
than hand-merging. Everything else auto-merged clean. Brian reviewed and
clicked merge himself; the KV sync and `check-docs` both ran clean on the
resulting 427-file diff. Cleaned up afterward: `v2` deleted both locally
and on `origin` (its job — one launch PR — was done). Also built ahead of
the merge, same session: `daily-pipeline.yml` (D6's workflow), and a new
`pages/` canon directory (see below) — both landed on `v2` before the PR
opened.

**D6, proven live — and a real bug found doing it.** Triggered the new
cron workflow for real via `workflow_dispatch` right after the merge,
per Brian's own ask ("run today's daily briefing from the GitHub action
to actually test it all works"). It worked — 17 ingest notes, a full
Daily Brief — but `check-docs.yml` and `sync-to-cloudflare-kv.yml` never
fired for the resulting commit. Root cause, confirmed via the GitHub API
(zero check-runs on that commit): a push authenticated with the default
`GITHUB_TOKEN` deliberately does not cascade into other `on:push`
workflows — GitHub's own loop-prevention behavior, not a bug in either
workflow. Fixed by having `daily-pipeline.yml` explicitly `gh workflow
run` both downstream workflows itself right after a real commit (needed
`actions: write` added to its permissions, and `workflow_dispatch` added
to `check-docs.yml`, which only had `push`/`pull_request` triggers
before). Manually triggered the KV sync once by hand to get that first
day's content live immediately while the fix was being built.

**The ingest-extraction bug** — found because Brian actually read the
brief's opening paragraph and asked "what happened here." Three items
that day had no real content, and the brief said so ("two were stubs...
one came through as a headline with no body"). Diagnosed three distinct
failure modes, all through the same gap: `extract()` in
`skills/ingest/ingest.py` wrote back whatever the model returned without
validating it matched the expected shape. Daniel Miessler's prompt-
injection-worm post: the feed had a real ~8000-char article (re-fetched
and confirmed directly), but the extraction call came back completely
empty — `if body is None` doesn't catch an empty string. Prof G: the
model wrote `NOT_RELEVANT` correctly but appended it after an
explanatory paragraph instead of as the whole response, and
`text.startswith("NOT_RELEVANT")` only catches the sentinel at the very
start. Moonshots: the prompt only said "say so plainly" for stub
content with no defined machine-readable output for that case, so the
model wrote prose instead of a sentinel and nothing caught that it
wasn't a real note. Fixed properly, not patched around: added a second
sentinel, `INSUFFICIENT_CONTENT`, to `skills/ingest/prompt.md` for the
relevant-but-too-thin case (previously only `NOT_RELEVANT` existed, for
off-topic) with an explicit "sentinel alone, no prose explanation either
way" instruction; `extract()` now checks, in order, an empty response
(skip + log), either sentinel appearing anywhere in the text rather than
a `startswith` match (skip), and a catch-all requiring the response
start with the expected `## Insights` header (skip + log) — so a future
prompt-following slip fails closed instead of writing something
malformed. Verified against the real broken cases: Moonshots and Prof G
now correctly produce no note at all; Miessler's post — genuinely
substantive the whole time — now extracts properly. Then went further,
since Brian asked for it: reverted the tracker/last-run state to its
pre-flawed-run baseline (a `git checkout` from the parent commit), deleted
the 3 broken notes, re-ran extraction for real on the corrected content,
and regenerated the entire 2026-08-19 Daily Brief from scratch against
the clean 16-note set (`brief_date` forced to `"2026-08-19"` via a
one-off script, since `brief.py`'s CLI has no `--date` override and real
time had rolled past midnight by then) — the stub-flagging opening
paragraph is gone entirely from the result, nothing left to caveat.
One real slip in the middle of this: a follow-up commit (the PKCE fix,
below) accidentally bundled in the stale reverted-tracker state alongside
the unrelated change — a staging mistake, not a design issue — corrected
with a new commit rather than amending, consistent with this repo's
don't-rewrite-history convention.

**`pages/` — new tier-2 canon directory**, declared in this file
alongside the existing canon dirs: standalone Substack pages that aren't
mirrors of already-published content elsewhere. Built the About page
through several real rounds: an initial AI draft, then Brian rewrote the
opening substantially in his own voice (dictated by voice memo — real
transcription noise like "brand bed dot com" for bmad.com, "yields" for
URL — worth remembering if a future session hits garbled dictated text
in a commit, that's why), then ~23 links added per his direction (his
LinkedIn, the BrianMadden.com "eulogy" post, the BriForum 20th-
anniversary post, `sources.yaml` on GitHub, the Daily Briefing Substack
tag page, both second-brain LinkedIn essays, the Riverside podcast home,
his starter-prompt gist), then reconciled again against edits he made
live on the actual Substack About page (emoji, a Citrix link, a real
source for the TechTarget acquisition, `bmad.com` dropped from "Other
links" as redundant with the nav bar). Status flipped from
`not-reviewed-by-human` to `reviewed-and-updated` once Brian confirmed
it — literally the schema-correct term for "human touched the machine
draft," which is what he was actually asking about when he called it
"co-written or whatever."

A parallel "Connect your AI" page was drafted in `pages/` too, then
**retired** once it became clear `mcp.brianmadden.ai` (the server repo)
already serves a human-readable connect walkthrough or the live MCP
protocol handler depending on the request's `Accept` header — a second,
separately-maintained copy on Substack (with zero subscribers to justify
the reach benefit) would just drift out of sync. Instead, merged the
better parts into the real `pages/mcp-connect.md` in
`brianmadden-ai-server`: added the homepage's animated demo widget there
too (the `{{demo}}` placeholder turned out to be generic across any page
in `build-pages.mjs`, not homepage-specific — cheap to add), fixed a
stale `me/synthesis.md` reference (renamed to `me/published-thinking.md`
in the v2 rebuild, never updated here), replaced a vague capabilities
sentence with the real tool list from the server repo's own README, and
— per Brian's ask, so a confused human landing on an AI-protocol page
isn't left going "what the fuck" — added an explicit title
("Connect your AI to brianmadden.ai") and a one-line human escape hatch
pointing at `brianmadden.ai/about`.

**Email delivery, built from a standing start.** Brian asked for the
rendered HTML of any `pages/*.md` file without needing a chat session
each time — built `skills/pages/render.py` (same technique as
`skills/brief/render.py`, minus the brief-specific disclosure/tracker
machinery). Then asked to have it *emailed*, which needed real new
capability: `brain@`'s Gmail OAuth token only had `gmail.modify`
(read + label), never `gmail.send`. Brian added the scope in Google
Cloud Console and re-authed himself; built `skills/lib/gmail_send.py`
(mirrors the existing token-refresh pattern rather than importing all of
`ingest.py`) and wired `--send`/`--to` into both `render.py` and
`skills/brief/publish.py`. Along the way, Brian caught a real privacy
gap before it went further than one commit: `b@bmad.com` (his personal
address) had been hardcoded as the default recipient in freshly-written,
about-to-be-public source. Consolidated it behind one `BRIAN_EMAIL` env
var instead — also used for `ingest.py`'s existing brain@-flag sender
verification, which had the same address hardcoded as
`PERSONAL_FLAG_SENDER` (now `personal_flag_sender()`, reading the env
var lazily so it still works correctly whether `.env` is loaded before
or after the constant would otherwise have been evaluated). Per Brian's
explicit ask, the fix commit doesn't dwell on "removing an exposed
address" in its message — folded in as ordinary configuration work,
though the change itself is real and complete. Old git history still has
the literal address in one earlier commit; Brian was explicit that's
fine to leave, not worth rewriting history over.

With that working, `daily-pipeline.yml` was extended (same session) to
run `publish.py --send` right after `brief.py`, so the rendered,
Substack-ready draft lands in Brian's inbox automatically every weekday
morning — not just committed to the repo, which was D6's original,
narrower scope. Guarded on today's brief file actually existing, so a
quiet day (no new notes, `brief.py` writes nothing) doesn't error out
trying to publish nothing. Separately fixed the "Use secure flows"
warning Google Cloud's Project Checkup was showing on the OAuth client:
`skills/lib/gmail_get_refresh_token.py` used a loopback redirect
(correct) but never sent a PKCE code challenge (RFC 7636) — added it,
and folded `gmail.send` into the default scope request so a future
re-auth asks for both scopes in one pass.

**The domain cutover — started, not finished.** `brianmadden.ai` itself
lives in the separate `brianmadden-ai-server` repo, not this one — a
real architectural fact worth remembering for whoever picks this thread
back up. Substack requires hosting on a `www` subdomain, not the bare
apex (confirmed from their own docs, not assumed), with the apex 301-
redirecting to it — and `www.brianmadden.ai` was already bound to the
existing Worker (the code that redirects `www → apex`, the *opposite*
direction), so this wasn't just a DNS change. Sequence: Brian added the
custom domain in Substack's own settings and got a CNAME target; removed
`www.brianmadden.ai` as a Custom Domain binding on the Worker in
Cloudflare's dashboard (Workers & Pages → the Worker → **Domains** tab —
note this is its own top-level tab in the current dashboard, not nested
under Settings, which cost a round of confusion); added the CNAME
(**DNS only** — un-proxied, Substack's own explicit requirement,
confirmed to matter since a proxied setup breaks their TLS handling).
Substack's side now shows "verified," waiting to finish activating
(their own docs say up to 36 hours; often faster in practice).

Before writing the Worker's apex-redirect code, checked real usage at
`bmad.com/mcp-stats` (a live dashboard, found while investigating —
worth remembering it exists) rather than guessing whether the legacy
`brianmadden.ai/mcp` endpoint mattered: 114 tool calls in 30 days, a
real mix of clients (Claude Desktop, Codex, Grok, a stray `curl`), zero
of them `StartMCP` (the unrelated "Second Brain Starter" generic tool,
also served from the apex at `/start`). Result: `/mcp` stays alive
deliberately — it already has a soft migration notice built in
(`MIGRATION_NOTICE` in `src/index.ts`, pre-existing, not built this
session) telling non-`mcp.brianmadden.ai` clients to update their
connector — while `/start` is retired outright (genuinely zero usage)
and everything else at the apex 301s to `https://www.brianmadden.ai/`,
no path preserved. Code written and dry-run-deployed clean
(`wrangler deploy --dry-run`), **not yet pushed** — deploying before
`www.brianmadden.ai` actually resolves to Substack would send visitors
to a domain that isn't live yet. A background poll (re-checking every 3
minutes) is watching for `www.brianmadden.ai` to stop redirecting to the
bare `substack.com` homepage, which is today's live signal that it's
still mid-activation.

**Also touched, smaller:** confirmed (live, via Substack's own support
docs) that GA4/GTM/Meta-pixel/X-pixel/Parse.ly are the only analytics
integrations Substack's Settings actually supports — no native Plausible/
Fathom, but GTM's Custom HTML tag is a real path to run one indirectly
if Brian wants privacy-first analytics without Google in the loop
directly; Substack's own built-in stats need no setup at all if that's
enough. Spun off a separate MCP-architecture-review thread with a
self-contained briefing prompt (real usage data, the routing code, what
to actually evaluate) rather than reviewing it inline here — Brian's own
call, correctly flagging it as a different kind of task than today's
infrastructure work.

**State for whoever (or whatever session) picks this back up:** `main`
is fully live now — v2's entire tier structure, the daily cron, email
delivery, all of it. The one genuinely unfinished piece from today is
the Worker deploy for the apex redirect, blocked purely on Substack's
own activation timing, not on anything left to decide or build. Check
`www.brianmadden.ai` directly before assuming it's still pending — the
answer might already be yes by the time this is read.

### 2026-08-20 — same session, continued (domain cutover completed; MCP
tool fixes from a parallel review session, coordinated and shipped
together)

**The cutover finished.** `www.brianmadden.ai` finished activating on
Substack's side a few hours after the previous entry was written
(watched for it via a background poll re-checking every 3 minutes,
rather than manually refreshing). Confirmed it was real content, not a
placeholder, before doing anything else. Pushed the
`brianmadden-ai-server` Worker change immediately after. Verified live
with real GET requests (not `-I`/HEAD, which misleadingly showed a
cached 200 on the apex right after deploy — GET is what actual browser
and MCP-client traffic sends, and that correctly showed the 301):
`brianmadden.ai` → 301 → `https://www.brianmadden.ai/`; `www` serving
the real publication; `brianmadden.ai/mcp` still answering; `mcp.
brianmadden.ai` still rendering the connect page for browsers. `brianmadden.ai`
is genuinely the Substack now.

**A second, unplanned thread of work landed in the same deploy.** Brian
had separately spun up a parallel Claude Code session (prompted with a
self-contained MCP-architecture-review brief this session wrote) to
evaluate the actual MCP tool set — not "does the code run" but "is this
the right interface," using real `/mcp-stats` usage data (114 calls/30
days, real search queries logged) as the basis rather than guessing.
That session found and fixed five real things in `src/index.ts`,
independently: `get_current_thinking` was reading `file:context/thinking.md`,
a KV key that doesn't correspond to any real content path — it had
apparently been silently returning "not found" on every one of its 12
calls in the last 30 days. `get_file`'s tool description pointed at
`me/synthesis.md`, renamed to `me/published-thinking.md` in the v2
rebuild and never updated (same stale reference this session separately
found and fixed in `pages/mcp-connect.md` the same day — a good sign
the rename genuinely needs a repo-wide check someday, not just
opportunistic catches). `get_framework`'s tool description was a
hand-maintained list that had already drifted, missing 4 of 10 active
frameworks — replaced with a list built dynamically from KV at `init()`,
filtered to skip anything frontmatter-flagged `status: archived`.
`search` was doing ~170 sequential KV reads per query (one file at a
time) and returning only the bare matching line — parallelized via
`Promise.all` and expanded to a few lines of context per match. Every
client now gets real orientation via MCP's native `instructions` field
on connect (previously that slot only ever carried the migration
notice for legacy-host clients — proper loading instructions required a
tool call, `get_loading_instructions`, that only 12 of 114 real calls
in 30 days actually made).

Found this the practical way: went to commit "everything" in the server
repo per Brian's ask and discovered a much bigger diff sitting
uncommitted than the routing change alone — both sessions had been
working in the same checkout in parallel. Rather than guessing at intent
or overwriting, messaged the other session directly (`SendMessage` /
`ListAgents` — real cross-session coordination, not simulated) to
confirm scope, ask whether it wanted to deploy itself, and check for
anything not yet confident enough to ship. It confirmed: five changes,
complete, fine to ship as part of this session's eventual push, and
flagged one honest gap — everything it had verified was static (`tsc`,
`oxlint`, `wrangler deploy --dry-run`), no live runtime test against a
real MCP handshake. Worth remembering as a pattern: a second AI session
reviewing its own work and naming what it *hadn't* verified, unprompted,
rather than overclaiming confidence.

Closed that gap before shipping rather than skipping it: no `wrangler
login` in this session (confirmed — `--remote` mode failed with a 400
auth error), so used `wrangler dev` in local mode instead, which turned
out to already have a real — if stale, pre-v2-rename — content snapshot
cached in local KV persistence from some earlier local session. Seeded
one additional fixture (`file:me/developing-thinking.md`, the corrected
key) by hand and ran a real MCP `initialize` → `tools/list` →
`tools/call` sequence over HTTP against the running dev server.
Confirmed all of it works: `instructions` field carries the full new
text with the migration notice correctly appended, `get_current_thinking`
retrieves the seeded content at the new key (old key would have hit the
"not found" fallback), `search` returns real multi-file, multi-line
results with no errors. Reported the result back to the other session
and to Brian, then shipped both sets of changes in one commit and one
deploy — `924cf6c`, pushed and live as of this entry.

**Worth remembering for next time a parallel session touches the same
repo:** this worked because both sessions left real state to find (a
clean uncommitted diff, not half-finished) and were reachable for a real
exchange rather than assumed-and-guessed-at. The coordination itself
cost two message round-trips, not a redesign.

Two more real things surfaced once the cutover was actually live and
D6 had run completely unattended for the first time:

**`brain@` ingested its own outgoing mail.** Brian caught it directly —
today's automated run pulled in yesterday's own Daily Briefing email and
an About-page email as "newsletters." Root cause:
`fetch_entries_email()`'s Gmail query never actually had `in:inbox` in
it, despite its own docstring claiming "polls the whole inbox" — Gmail's
default search scope without an `in:` qualifier is all mail except
Spam/Trash, which includes Sent. The moment `gmail_send.py` started
sending brain@'s own emails today, the very next ingest run picked them
back up from brain@'s Sent folder. Fixed the query, deleted the 2
resulting bogus notes, and removed a `brain-brianmadden-ai` entry that
had auto-registered in `sources.yaml` — the same bug registering brain@
as a source of itself. Checked whether the 2026-08-20 brief needed
regenerating the way 2026-08-19's did; it didn't — the redundant content
never surfaced prominently in what the model actually synthesized.

**Disclosure line reworded**, Brian's own wording: "I wrote this post
myself" → "I generated this post", and "that's me, not Brian" → "that's
me, the AI, not Brian" — clearer on first read. Dynamic parts (the
review-status clause, the commit-permalink-vs-blob-link fallback)
untouched. Ships on the next post rendered; today's 2026-08-20 brief was
already rendered and emailed with the old wording before this landed —
re-running `render.py --date 2026-08-20` picks up the new copy if Brian
wants it before pasting into Substack.

**End of day.** Both repos clean, nothing uncommitted. `main` is live,
D6 ran fully unattended end to end for the first time today, the domain
cutover is done and verified, and every real issue found today — the
ingest-validation bug, the cross-workflow trigger gap, the self-ingestion
loop — got fixed at the root rather than patched around, with the fixes
themselves logged here alongside the incidents that surfaced them.

### 2026-08-20 — new `/maintain` session (Workstream E doc recovered and committed)

That "end of day" claim above turned out to be off by one file. This
session's `/maintain` bootstrap found `docs/substack-as-primary-home.md`
uncommitted — a full "Workstream E — publication structure: Sections,
tags, static pages" section, ~95 lines. File mtime (01:42 local) placed
it eight minutes *after* the prior entry's "end of day" commit
(`73324a8`, 01:34) — genuine trailing work from that same session that
never got staged or logged, not concurrent/other-session drift.

Content is real, not a stub: a live audit of Substack's actual
publication settings (every post so far bylined "brianmadden.ai,"
including Brian's own talks/podcast episodes/essay — wrong, and it
breaks author-based filtering before it starts; duplicate archive
entries on the Hotsheet episodes) plus a decided structure — two
Sections ("Daily Briefing" for AI output, "From Brian" for
human-authored content, with per-type tags inside the latter only) and
static pages for `/books` and `/frameworks` instead of tag streams for
those. Ends with an explicit action-item list: fix bylines, de-duplicate
the archive, build the two Sections in Substack's settings, retag the
back catalog. All of that is design-only — nothing applied in Substack
yet.

Committed as-is, no content changes — this entry is the missing log
line, not a review of the decision itself. Brian's said he'll pick up
the actual Substack UI work (bylines, dedup, building the Sections) in
the next few days; nothing else pending, today's 2026-08-20 brief is
already out. Repo is clean again after this commit.

### 2026-08-21 — `/maintain` session (Workers KV cap diagnosed and fixed;
archived-framework filter bug found and fixed)

Bootstrap found `main` diverged from `origin/main` by one commit each
way — local had the trailing Workstream E doc commit, origin had that
morning's automated `daily-pipeline.yml` run (10 ingest notes, the
2026-08-21 brief). No file overlap; merged clean before doing anything
else, per this file's own standing caution about concurrent sessions.

**Brian forwarded a Cloudflare alert** ("Workers KV operations are
nearing the daily cap," 50% then 90% within a day) and asked whether to
just subscribe to the Workers Paid plan or ignore it. Investigated
before answering rather than treating it as a yes/no billing question —
found the actual cause in `brianmadden-ai-server/src/index.ts`: the
`search` MCP tool did a KV `list` + a `get` for *every single file in
the whole corpus* (171 files) on every search call, and
`listActiveFrameworks()` (which builds `get_framework`'s tool
description on every session `init()`) did a smaller version of the
same fan-out. Yesterday's parallel MCP-review session (2026-08-20 entry
above) had already flagged this exact pattern as "170 sequential KV
reads per query" and "fixed" it by making the reads concurrent via
`Promise.all` — which fixed latency but not the operation count, so the
underlying cost stayed exactly as large. The timing lines up: the
domain cutover went live the day before (2026-08-20), so real traffic
hitting `search` for the first time is a very plausible trigger for
blowing through the free-tier daily read cap.

**The actual fix, built and shipped after Brian approved it:**
- `brianmadden-ai`: `sync-to-cloudflare-kv.yml` gained a step that
  builds one consolidated `file:path -> content` JSON blob (171 files,
  ~2.2MB, well under KV's 25MB value limit) from the full checkout and
  pushes it as a single `search-index` KV key on every sync run.
- `brianmadden-ai-server`: `search`, `list_files`, and
  `listActiveFrameworks` all now read that one key once per session
  (cached on the `BrainMCP` instance via a new `getContentIndex()`
  method) instead of hitting KV per file. A session that uses all three
  tools now costs 1 KV read total, down from ~154.

Shipped with care about sequencing, since the Worker code now depends
on `search-index` existing: pushed the content-repo workflow change
first, manually triggered `workflow_dispatch` to force a full sync
(confirmed in the run log: "Built search index: 171 files" / KV PUT
returned `OK`) *before* pushing the Worker change, so there was no
window where `search` would've silently returned empty. Pushed the
server-repo change, watched `deploy.yml` auto-deploy
(`Current Version ID: dae88234`), then verified live against the real
running server — not just "the deploy succeeded" — with a real MCP
`initialize` → `tools/call` sequence over HTTP: `search` for "factory
electrification" returned real 19-file results, `list_files` and
`get_framework` both returned real content.

**Second bug found via that same live smoke test, unrelated to the KV
fix, fixed the same session at Brian's request:**
`listActiveFrameworks()`'s archived-framework filter checked
`content.slice(0, 600)` for `"status: archived"` — a fixed byte
cutoff, not frontmatter-aware. `frameworks/five-levels-of-ai-in-
knowledge-work.md` (the one framework actually archived, per this
file's canon-governance rules) has that flag at byte offset 655, just
past the cutoff, so `get_framework`'s tool description had been
silently advertising it as active since the code shipped 2026-08-20 —
confirmed live before fixing. Replaced the byte-count guess with a
regex that parses the actual frontmatter block between the `---`
delimiters. Shipped the same way (push → auto-deploy → live
verification with a fresh session), including chasing down one false
alarm: the first post-deploy check still showed the archived framework
in the list, which looked like a code bug but was Cloudflare edge
propagation lag — a retry a couple minutes later, same fresh-session
check, showed the fix live and correct (10 active frameworks, the
archived one gone).

**Everything from both fixes is live and verified working as of this
entry.** Both repos clean. Nothing else picked up this session yet —
the KV-cap thread came in as a follow-up question during `/maintain`
bootstrap, ahead of picking a task from BUILD.md's own flagged
priorities (D7 residual, D10, launch-week essay/brief, Workstream E's
Substack UI actions — all still open, untouched this session).

### 2026-08-24 — `/maintain` session (Weekly Update built and run for
real: BUILD.md open decision #13 closed, 20-item promotion-candidates
backlog cleared, first issue drafted)

Bootstrap found a clean `main` (this was the session that also did the
BUILD.md trim and GOVERNANCE.md rewrite earlier the same day — see the
two commits immediately prior to this entry). Brian's ask, from a voice
memo: a weekly review ceremony — read a recap, talk it through live, go
through whatever's queued up (promotion candidates, staleness flags),
land on real takeaways, and produce a "Weekly Update" post. This is open
decision #13, flagged 2026-08-18 and never built.

**Design, decided in chat before writing anything:** two things were
genuinely Brian's call, asked directly via `AskUserQuestion` — byline
(dual: `brianmadden.ai` + Brian Madden, since the content is a real
collaboration, not either voice alone) and Substack placement (fold into
the existing structure for now, no new Section, revisit once there are
real issues to judge readership by — closes the question Workstream E of
`docs/substack-as-primary-home.md` left explicitly open). Everything else
followed from the repo's existing patterns: reuse `review-thinking`'s
developing-thinking.md mechanics rather than duplicate them, no
`weekly.py` script since the ceremony is inherently interactive (unlike
`brief.py`/`triage.py`, nothing here runs unattended), a small
`skills/weekly/render.py` for the one genuinely reusable piece
(Substack-paste HTML).

**Built:** `.claude/skills/weekly-update/SKILL.md` (14 steps, later grew
an extra one mid-run — see below), `skills/weekly/render.py` +
`skills/weekly/README.md`, `outputs/weekly-updates/` (new tier-3
location, `outputs/README.md` updated), a new `last_reviewed`
frontmatter field on `me/developing-thinking.md` distinct from `updated`
(documented in `docs/frontmatter-schema.md`), `.gitignore` entry for the
rendered HTML. `docs/substack-as-primary-home.md` and this file's own
open decision #13 updated to record the byline/placement resolution.

**Then run for real, live, in the same sitting — the first-ever pass over
both queues since the pipeline launched.** No prior `.last_run.json`, so
the window defaulted to 7 days back (Aug 17-24). Brian's scope call,
given mid-run: the story recap covers last week only (Aug 17-21, since
today's brief starts next week's window), but the promotion-candidates
backlog gets cleared in full regardless of age — a first-run backlog
clear, not a strict per-week slice.

The promotion queue had grown to 20 entries, never worked before. Walked
through in grouped batches (my read first, Brian's call on each group)
rather than one-by-one cold:
- **4 threads consolidated into 1** `developing-thinking.md` entry
  (shared artifacts as the undetected agent-to-agent channel) — they'd
  been tracked separately only because the pipeline's thread-matching is
  exact-slug-only and never actually recognized the overlap (see new
  open decision #15 above).
- **3 threads consolidated into 1** at Brian's own framing ("AI labs
  control every lever beneath your strategy").
- **5 threads promoted separately** (routing-seat-to-payments,
  personalization-in-weights-vs-files, deployer-opacity, human-approval-
  worse-than-automated-policy, open-ended-research-failure-shape) — two
  extended live with Brian's own additions (the OSS/startup routing
  layer via Merge's 75x-fewer-tokens claim; the Chinese-model-censorship
  "what else is hidden" point, which became its own new
  `developing-thinking.md` paragraph attributed directly to him).
- **1 thread's disposition became a real design question**, which Brian
  asked outright: does something "true and real but not groundbreaking"
  belong in `developing-thinking.md` at all? Answered with precedent from
  the 2026-08-14 triage (which already cuts "dated market/news
  snapshots") — landed as a supporting addition to the existing "Compute
  scarcity and token governance" section instead of a standalone entry,
  proposed as the general rule going forward.
- **2 threads folded as one-line notes** into existing sections ("The
  cognitive stack," "The 2031 worker-shape forecast").
- **2 threads dropped** with no canon addition — Brian: "meh… whatever
  you think," delegated and applied with a light touch, not silently
  ignored.
- **1 thread held open** (`machine-speed-vs-human-absorption`), tied to
  an unresolved staleness-queue item it turned out to be the evidence
  base for.

The staleness queue (fresh `triage.py` run: 7 developing-thinking items,
2 frameworks) went the same way, all approved in one batch after Brian
reviewed the grouped summary ("yeah go ahead with all of it"): 4 cuts
(already-published elsewhere — the authoring-recipe residual from one cut
kept as a scratchpad line), 3 "promote" decisions logged as real writing
tasks rather than drafted blind (human clock speed as the invariant —
which also resolves the held-open promotion-candidate above; the
second-brain selection-bias failure mode; "you can only see one step
ahead"), and 2 framework revisions (`bitter-lesson.md` corrected against
its own later-published knowledge-factory revision; `post-application-
era.md` qualified with the three-tier/"UIs not systems of record"
formulation) — both frameworks flipped to `status: reviewed-and-updated`,
not archived.

Brian's front-of-mind check-in added three new `## Right now` bullets
(Chinese-model risk, harness-vs-model, distributed/local models and
whether Wave 3 is closer than the roadmap says — he wants to actually
test the new 27B open-weight model directly, not just read its benchmark
position) and, mid-run, a genuinely new idea that became step 7 of the
skill: this ceremony is a natural place to surface blog-post/podcast
candidates, since the "promote" writing tasks already are exactly that.
Landed a "Worth a future post or episode" section in the finished post
listing five candidates.

**A real formatting miss, caught before commit, not after:** every new
passage written this session used spaced em-dashes, against
`me/style-guide.md`'s no-spaces rule — fixed programmatically across all
five touched files. The finished Weekly Update post also initially used
backtick `.md` references, which the same style guide's Substack-
rendering section says renders oddly — converted to italicized real
GitHub links before the final render. Both logged plainly in
`governance-log.md` as misses, not silently corrected.

**Finished and rendered:** `outputs/weekly-updates/2026/08/2026-08-24-prep.md`
(the prep doc) and `2026-08-24.md` (the dual-byline post, `status:
reviewed`), HTML rendered via `skills/weekly/render.py`, sent to Brian.
`outputs/weekly-updates/.last_run.json` written for the first time.
`developing-thinking.md` frontmatter bumped (`updated`, new
`last_reviewed` field, `status: reviewed-and-updated`).
`python3 scripts/check_doc_accuracy.py` clean, 0 warnings. `_index.json`
updated surgically (word counts, `updated` date) — confirmed it doesn't
track `outputs/` at all, so no new entries needed there.

**Still open:** the three logged writing tasks (human clock speed,
second-brain failure mode, one-step-ahead skepticism) aren't drafted —
real follow-up sessions, not today. The `machine-speed-vs-human-
absorption` promotion-candidate stays queued, tied to the human-clock-
speed write-up. The fuzzy-matching fix (new open decision #15) isn't
built.

**Same session, second round — real product feedback after seeing the
first draft, not more queue-clearing:** Brian reacted to the finished
issue with four real asks, all actioned the same sitting:

1. **Named it.** "Weekly Update" becomes **Deeper Thinking** — his own
   choice, over a shortlist ("Second Thoughts," "Loose Threads") offered
   via `AskUserQuestion`. Landed everywhere the old name appeared (skill
   description, `SKILL.md` body, `README.md`s, post frontmatter/title) —
   the internal skill/directory name stayed `weekly-update`, matching how
   the Daily Brief's own directory is `skills/brief/` regardless of its
   public name.
2. **Automated the "initial recap."** New
   `skills/weekly/gather.py` — deterministic assembly of the prep doc (no
   LLM call beyond re-running `triage.py`), wired into
   `daily-pipeline.yml` as a Fridays-only step (`date -u +%u` check, not a
   cron-string match, so it also behaves correctly on a manual
   `workflow_dispatch` test) that runs after that day's Daily Brief and
   emails the result via the same `gmail_send` helper `publish.py`
   already uses. Deliberately doesn't run the interactive ceremony
   itself — Brian still has to sit down for that part, whenever he
   actually does. `git add` in the workflow's commit step gained
   `outputs/weekly-updates/` and `outputs/canon-triage/` (the latter was
   a real gap — `triage.py`'s output was never in the daily commit path
   before).
3. **Rewrote the post's structure**, per four specific asks: an honest
   boilerplate line clarifying the daily stories are the AI's picks, not
   Brian hand-selecting each one; "What moved in the thinking" converted
   from dense paragraphs to bullets grouped under sub-headings for
   at-a-glance scanning; a brand-new "Where my head's at right now"
   section (Brian's idea) that quotes the live `## Right now` bullets and
   links straight to `developing-thinking.md` on GitHub — making the
   "second brain edited in public" thesis literal instead of asserted;
   and an explainer line added to "Brian's takeaways" saying plainly
   where that section's content comes from.
4. **Rewrote "Worth a future post or episode" in plain language.** The
   original five entries were accurate but, Brian's words, "too AI
   science fancy pants" — dense internal shorthand a real reader wouldn't
   want to click into. Rewritten with his own example as the template:
   `"Harnesses vs. models—worth a real position, not just a tracked
   thread"` became a plain hook + one-sentence explanation of why it
   matters (`"The harness might matter more than the model. A cheap,
   low-quality model wrapped in a really good harness... can beat an
   expensive frontier model with a bad one."`). Applied to all five.

Brian's closing framing for this round, worth keeping verbatim as the
bar for future issues: could this be "an anchor that real people
actually read," not just an internal audit artifact with a byline on it.

**Caught the same em-dash/backtick misses again on the rewrite** —
rewriting the post file fresh (via `Write`, not `Edit`) reintroduced both
issues fixed earlier in the session, since the fix wasn't durable across
a full rewrite. Fixed the same way (programmatic regex pass), and this
time also simplified `skills/weekly/render.py` itself: removed its
injected `DISCLOSURE`/`FOOTER` constants entirely, since Deeper Thinking's
opening explanation and closing footer are now written directly into the
body at draft time (varies naturally issue to issue) rather than bolted
on identically at every render — the Daily Brief's render.py keeps its
own injection because that body never carries its own authorship
explanation; Deeper Thinking's does, every issue, by construction.

`python3 scripts/check_doc_accuracy.py` and `_index.json`/workflow-YAML
validity all re-checked clean after this round. Still not committed —
same reasoning as above, now covering the second round too.

### 2026-08-25 — `/maintain` session (source-checking bug found and made
visible; subtitle empty-response bug found and fixed)

Bootstrap found local 3 commits behind `origin/main` (today's automated
run plus the 2026-08-24 afternoon `me/voice.md` reconciliation) while
Monday's Weekly Update build was still sitting uncommitted locally.
Confirmed local had no unique commits, so stashed (`-u`), fast-forwarded,
popped. One real conflict: `outputs/technical-briefings/promotion-
candidates.md` — today's automated run had reappended all 19 entries
Monday's session already cleared, because that clearing was never pushed
before today's run read the file. Resolved by keeping Monday's cleared
state plus the 2 genuinely-new entries today's run added
(`git-host-as-agent-control-point`, `governance-derived-from-political-
theory`); `governance-log.md` auto-merged cleanly (pure appends on both
sides). Nothing else conflicted.

Brian's actual ask: look at today's briefing, the subtitle read generic
("doesn't really seem to talk about today"), and the sources looked
email-heavy — verify the pipeline is actually checking everything it's
supposed to, and build a standing way to see that going forward rather
than taking it on faith. Both turned out to be real, not misreadings —
see open decision #16 above for the full account of what was found and
built:

- **Sources:** 39 of 85 registered sources (~46%) have failed with `403
  Forbidden` on every automated run since launch, silently, never
  flagged. Diagnosed as likely Cloudflare-blocking-GitHub-Actions-IPs
  (confirmed via a live web search, not guessed) rather than a fixable
  header/code issue. Recommended fix (Brian's own idea, matching
  infrastructure already proven reliable): migrate those Substacks to
  the `brain@` email path, same as the newsletters that already work
  that way. Real manual work only Brian can do — logged, not built.
  What *was* built: `ingest.py` now records a full per-source
  success/error/skip outcome every run
  (`ingest/.last_run_sources.json`), and `brief.py` renders it into a
  new "Sources checked today" section at the bottom of every brief —
  the actual answer to "how would I know if this stopped working,"
  since it's now a fact on the page rather than something requiring an
  Actions-log dig. Retroactively reconstructed from today's real run
  log (no live network/Gmail calls) and applied to today's already-
  committed technical and published briefs, so Brian could see the real
  thing rather than a synthetic example.
- **Subtitle:** today's published subtitle was the hardcoded generic
  fallback — root cause was an empty response from the subtitle model
  call (2048 `max_tokens` insufficient for an unusually dense brief,
  same failure shape already documented elsewhere in this file for
  `brief.py`'s own synthesis call), not a prompt-design problem. Bumped
  to 8192 in `publish.py`, regenerated today's subtitle for real (a
  specific, on-topic one on the first try), patched the published
  file's frontmatter, re-rendered and re-sent the corrected HTML.

Both fixes verified: `python3 -m py_compile` on all three touched
scripts, `python3 scripts/check_doc_accuracy.py` clean (0 warnings).
`skills/brief/render.py`'s HTML render tested against the new section
directly (renders correctly, no markdown-escaping issues from the em-
dashes/bold-list format).

**Same session, continued after Brian's go-ahead to commit — three more
things landed, all from Brian's own follow-up asks:**

1. **`/maintain` now syncs with `origin` as step 1**, before reading
   anything — `.claude/skills/maintain/SKILL.md` gained an explicit
   fetch/fast-forward/stash-and-resolve procedure, directly modeling
   what this session had to do reactively at its own start (3 commits
   behind, Monday's work still uncommitted locally). Real conflicts get
   real judgment, not an automatic pick of either side; local commits
   `origin` doesn't have stop the sync and get flagged rather than
   auto-pushed or auto-rebased. Steps renumbered 1-6 accordingly.

2. **Ran a real local catch-up ingest to confirm the 403 diagnosis and
   backfill what was missed.** Brian subscribed the blocked Substacks to
   `brain@` via the `brianmaddenai` account (per open decision #16's
   recommendation) but email delivery takes days to start flowing, so he
   asked for a local run in the meantime — `python3
   skills/ingest/ingest.py --since-days 3`, run from this machine rather
   than GitHub Actions. **Result: 0 of 85 sources failed** (vs. 40 on
   this morning's automated run) — conclusive confirmation the block is
   GitHub-Actions-IP-specific, not anything about the feeds or code
   themselves. Found one more real bug along the way: the first attempt
   crashed entirely partway through (`on-with-kara-swisher`'s episode)
   with a `UnicodeDecodeError` inside `subprocess.run()`'s own stderr
   decoding of ffmpeg's output (real non-UTF-8 bytes in a real ffmpeg
   run) — a `ValueError` subclass the surrounding `except RuntimeError`
   in `_split_audio_for_transcription()` doesn't catch, so it took down
   the whole run instead of just that one episode, before ever reaching
   most of the previously-blocked sources later in `sources.yaml`'s
   order. Fixed with `errors="replace"` on that `subprocess.run()` call
   (`skills/ingest/ingest.py`) — stderr is only ever used truncated for
   a diagnostic message, so lossy decoding costs nothing real. Re-ran
   clean: 32 new entries found, 20 new ingest notes written (the crashed
   first attempt had already written 8 of them before dying; dedup
   correctly skipped those on the retry).
3. **Regenerated today's Daily Brief from the complete set, not just the
   catch-up delta.** Backed up the morning's thin 5-source brief and
   published post, removed them so `brief.py`'s already-briefed dedup
   wouldn't exclude those 5 notes, then re-ran `brief.py` + `publish.py`
   fresh against all 32 of today's ingest notes together — one coherent
   synthesis instead of two fragmented ones. Caught a new thread the
   broken run would have missed entirely: `harness-as-the-named-value-
   layer` crossed the promotion threshold on this run (real evidence
   from the newly-ingested SemiAnalysis/AlphaSignal content), now
   queued in `promotion-candidates.md`. `update_tracker()`'s existing
   same-day dedup guard (`last_seen == run_date`) prevented double-
   counting any thread that recurred in both today's original 5-note
   brief and this fuller 32-note one. New subtitle generated correctly
   on the real (fixed) code path. Both regenerated files sent to Brian;
   originals kept as local backups (not committed) in case of comparison
   need, not carried into the repo.

`python3 scripts/check_doc_accuracy.py` re-checked clean after all of
the above.

**One more follow-up, same session:** Brian's direct ask after seeing
the 403 diagnosis — auto-flip a source's `sources.yaml` row from
`feed_url` to `ingest_method: email` the moment a real email from that
publication actually arrives, rather than leaving the migration as a
manual sources.yaml edit for each of the ~39 sources once his Substack
subscriptions start delivering. Built as two new functions in
`skills/ingest/ingest.py`: `find_feed_source_for_email_sender()` matches
a real email's sender address against existing feed_url-based rows with
no `sender` yet (by domain for a custom-domain publication, e.g.
`news@alphasignal.ai`, or by subdomain-token for a `*.substack.com` one,
checking both a per-publication sending subdomain and a shared
`substack.com`-apex-with-local-part pattern since the real Substack
send-address format can't be verified without a live example);
`flip_source_to_email()` rewrites just that one entry's block in
`sources.yaml` in place (feed_url nulled, `sender` and `ingest_method:
email` inserted) rather than a full-file YAML re-dump, preserving every
other entry's comments and this entry's own hand-written `note`/`lens`/
`pov` untouched — same reasoning `auto_register_email_source()` already
established for why this file is never blindly re-serialized. Wired in
ahead of `auto_register_email_source()`'s existing call site: a match
flips the existing row; no match falls through to the existing
register-a-new-row behavior unchanged. Unit-tested directly against a
copy of the real `sources.yaml` (not the live file) — both plausible
Substack sender-address shapes matched `marcus-on-ai` correctly,
`alphasignal.ai` (already flipped) and an unrelated address both
correctly didn't match, the resulting block parses as valid YAML with
only the target entry's `feed_url`/`sender`/`ingest_method` lines
changed, and the file-end boundary case (flipping the last feed-based
entry in file order) works. `sources/sources.yaml`'s header comments
gained a matching dated note. Not yet exercised against a real inbound
email (none of Brian's new Substack subscriptions have started
delivering yet) — first real trigger will be the actual test.
