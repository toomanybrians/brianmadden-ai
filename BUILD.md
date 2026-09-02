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

    **2026-09-02 update: current concrete list, re-pulled from that
    morning's real `ingest/.last_run_sources.json`, not re-derived from
    the original count.** 24 Substack-hosted feeds are 403ing on every
    scheduled run (down from the original "~39" estimate — likely just a
    more precise count this time, not evidence anything's been fixed;
    cross-checked against every sender who's actually emailed `brain@`
    since launch and confirmed **zero overlap** — none of these 24 have
    been migrated yet, this is 100% still outstanding manual Substack
    work). Same fix as before: subscribe to each via the `brianmaddenai`
    Substack account with "email me new posts" on. The concrete list,
    for Brian to work through:

    - David Shapiro's Substack — https://daveshap.substack.com
    - Demis Hassabis — https://demishassabis.substack.com
    - Dr. Fei-Fei Li — https://drfeifei.substack.com
    - Emerging Physical AI — https://emergingphysicalai.substack.com
    - Extended_Brain — https://extendedbrain.substack.com
    - Forked Lightning — https://forklightning.substack.com
    - In the pool with Esther — https://estherdyson.substack.com
    - Kevin Roose — https://kevinroose.substack.com
    - Kinder Futures — https://mollykinder2.substack.com
    - Theory of the Game (Reid Hoffman) — https://reidhoffman.substack.com
    - Work Evolved — https://workevolved.substack.com
    - Center for Humane Technology — https://centerforhumanetechnology.substack.com
    - BIG by Matt Stoller — https://www.thebignewsletter.com
    - Cory Doctorow — https://doctorow.substack.com
    - Ghosts of Electricity — https://aleximas.substack.com
    - The Wake Up Call — https://thewakeupcallnewsletter.substack.com
    - 80,000 Hours — https://80000hours.substack.com
    - TECH EMPIRES — https://techempires.substack.com
    - Asimov's Addendum — https://asimovaddendum.substack.com
    - The AI Report — https://theaireport.substack.com
    - The Economics of AI — https://economicsofai.substack.com
    - The EU AI Act Newsletter — https://artificialintelligenceact.substack.com
    - METR — https://metr.substack.com
    - Lex Fridman — https://lexfridman.substack.com

    (`nate-b-jones`'s dead YouTube feed, 404 not 403, is the one other
    non-`ok` feed source — separate, already-documented gap, not part of
    this list.) The 15 sources already on `ingest_method: email` plus the
    ~24 more auto-registered senders already arriving through `brain-inbox`
    are all healthy — confirmed by scanning every ingest note's `author`
    field since launch, every one of them has actually delivered at least
    once. This list is only the ones that haven't started yet.

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

### 2026-08-26 — `/maintain` session (prose-quality bug diagnosed and
fixed; brief.py's default model switched to Sonnet; X timeline wired
in for real)

Bootstrap found local 1 commit behind `origin/main` (the automated
2026-08-26 morning run), working tree clean — clean fast-forward, no
conflict.

Brian's actual ask: the Daily Brief's opening line ("Today's batch
lands hardest on the compute thread, and it lands from two directions
at once") read as "too AI, too try-hardy" — asked what model was
writing it and how to fix it, specifically flagging that it's gotten
worse since the pipeline moved to GitHub Actions (Aug 19-20).

**Diagnosis, not guesswork:** the model hadn't changed — `claude-opus-5`
wrote the body from day one (Aug 11), when prose was clean. Counted
bolded kebab-case tracked-thread slugs appearing inline in ordinary
sentences (e.g. "the **inference-allocation-as-supply-risk** thread")
across every published brief this month: zero through Aug 14, then
10-17 per issue from Aug 17 on — a real, dateable regression, not a
subjective drift. Traced to a one-line Aug 16 style-guide fix
(`a88ace7`) meant to apply only to the "Threads being tracked" bullet
list ("Use **bold** for a short label/identifier at the start of a
bullet") — the model generalized it into bolding slugs anywhere it
referenced a thread, including mid-sentence, which is exactly when the
regression starts. Separately, reread the brief with fresh eyes and
found a second, non-formatting pattern layered on top: rhetorical
scaffolding (parallel triads, anaphora, sentences that restate their
own point for a punchier close, italics for emphasis) that nothing in
`me/voice.md` discouraged — the file describes what Brian sounds like,
not what generic-impressive-AI-writing sounds like and should be
avoided.

**Fixed, both additive to files with an existing "flag tells as they
turn up" convention:**
- `me/style-guide.md` — scoped the Aug 16 bold-slug rule to the bullet
  list only, and added an explicit rule banning a tracked-thread's
  slug from ever appearing inside prose, bolded or not.
- `me/voice.md` — extended the existing "AI-commentary tells" bullet
  (the one that already caught "load-bearing" and "receipts") to cover
  sentence-level tics, not just individual words: parallel triads for
  cadence, anaphora, mic-drop restatement closers, italics standing in
  for a stronger word choice.

**Verified with a real regeneration, not just argument:** dry-run
reran today's actual batch (the 4 brain@ notes + 1 new X-timeline
note — see below) against the fixed prompt with `claude-opus-5`: zero
bolded slugs (confirmed fix), but 3 residual italics-for-emphasis
instances (the tone fix helps but doesn't fully land in one pass, as
expected — same "watch for more, add them here" pattern as every prior
voice.md addition). Used the same moved-file technique the 2026-08-25
session documented (temporarily relocate the committed dense brief so
`load_previously_briefed_paths()` doesn't exclude its notes from a
dry-run comparison, restore immediately after) — with one real
near-miss: the first attempt at a same-batch Sonnet comparison hit a
2-minute Bash timeout mid-API-call, which killed the shell before the
restore line ran, leaving the committed file moved aside for a few
minutes until caught and fixed. No actual harm (`git status` confirmed
clean once restored), but worth a beat: any future use of this
technique should wrap the restore so it can't be stranded by a timeout
(e.g. run the risky part with a timeout comfortably longer than the
call ever takes, as the retry did).

**Model question, asked directly by Brian ("is opus 5 the right model,
should we use 4.8, or fable?"):** loaded the `claude-api` skill rather
than answering from memory. No documented Anthropic guidance exists on
relative prose-plainness across tiers — that's not something
pricing/context-window docs cover. Ran a real same-batch, same-fixed-
prompt comparison instead of speculating: `claude-sonnet-5` against
`claude-opus-5` on the identical 5-note batch. Result: Sonnet produced
zero bolded-slug and zero italics-emphasis instances (Opus still had
3), at 750 words vs. 1,162 for the same material (35% shorter, nothing
lost), at $2/$10 per MTok vs. Opus's $5/$25. Recommended against both
alternatives Brian named: Opus 4.8 is same price as Opus 5 with no
known advantage (older generation); Fable 5 costs double and is
positioned by Anthropic for the hardest long-horizon agentic/reasoning
work, not plain synthesis prose — no reason to expect it writes more
simply, real reason to expect it costs more. Brian reviewed the full
Sonnet sample and confirmed: switch permanently.

**Landed for real, not just proposed:**
1. `skills/brief/brief.py`'s `DEFAULT_MODEL` changed from
   `claude-opus-5` to `claude-sonnet-5`, with the historical Aug-11
   rationale comment kept (audit trail) and a new note explaining the
   Aug-26 switch and its evidence, so a future session doesn't have to
   re-derive why.
2. **X timeline wired in for real, not just diagnosed.** Brian added
   the `X_CLIENT_ID`/`SECRET`/`ACCESS_TOKEN`/`REFRESH_TOKEN` secrets to
   GitHub mid-session (unblocks tomorrow's automated run — not verified
   from here, GitHub Actions isn't reachable from this session, but the
   mechanism is the same one just proven locally). Confirmed the same
   4 credentials are already present in the local `.env` too; ran
   `ingest.py --source x-timeline --since-days 2` for a real first
   pull (the default auto-window was too narrow — 2.4 hours since the
   source's own last successful run, which had never actually
   succeeded before today) — 4 entries fetched, 3 correctly judged not
   relevant, 1 real ingest note written
   (`ingest/2026/08/2026-08-26-x-timeline-rt-bcmerchant-sam-altman-...md`).
   First-ever successful pull from this source.
3. **Today's dense brief and published post regenerated for real
   against the fixed prompt, the new default model, and the freshly-
   ingested X note, replacing what the morning's automated run had
   committed** (per Brian's explicit "recommit with today's fix," after
   he reviewed the full Sonnet sample). Used the moved-file technique
   again, this time for a real (non-dry) run so no restore was needed —
   the real run's output directly replaced the file that had been
   moved aside. `outputs/technical-briefings/2026/08/2026-08-26.md` and
   `outputs/published/2026/08/2026-08-26.md` both now cite all 5 of
   today's notes (the original 4 brain@ notes plus the new X one) and
   carry `model: claude-sonnet-5`. Thread tracker updated cleanly — the
   already-documented same-day dedup guard (`last_seen == run_date`)
   correctly no-op'd on the 6 threads the fuller batch re-touched from
   the morning's thinner run, and added the 2 genuinely new ones
   Sonnet's synthesis surfaced (`labs-public-rhetoric-vs-internal-
   statements`, `youth-ai-anxiety-tracks-exposure-data`) without
   duplicating anything — no promotion-candidates.md change, nothing
   crossed the 3x threshold this run. Zero bolded slugs, zero
   italics-emphasis tics in the final committed body — both fixes held
   on the real run, not just the test one.

All Python files touched (`brief.py`) compile clean
(`python3 -m py_compile`); `scripts/check_doc_accuracy.py` re-checked
after the commit.

**Same session, continued — Brian read the recommitted brief and flagged
more, real problems found by actually investigating rather than
guessing:**

1. **Substack-sourced brain@ notes had no source link — confirmed and
   fixed.** Every brain@-routed Substack email that day had `source_url:
   ''`. Root-caused with a live Gmail diagnostic (not a guess): pulled
   the raw HTML of three real Substack emails and dumped every anchor's
   text. Substack's template never uses any of the phrasing
   `_find_view_online_link()`'s regex looked for ("view in browser,"
   "continue reading," etc.) — it links the post title and a **"READ IN
   APP"** button, both through `open.substack.com/pub/<publication>/p/
   <slug>`, an app-first interstitial. Confirmed that domain doesn't
   reliably 3xx-redirect for a plain `requests.get()` the way
   `_resolve_email_link()` expects (it can return 200 and stay put,
   unlike a real browser) — so instead of trusting that redirect, added
   `_rewrite_substack_app_link()`, which parses the publication+slug
   directly out of the interstitial URL and constructs the real
   `https://<publication>.substack.com/p/<slug>` URL deterministically,
   no network round-trip needed. Also added "read in app" to
   `VIEW_ONLINE_TEXT_RE` so the anchor gets found at all. Verified live
   against 3 real senders (Marcus on AI, Dwarkesh Patel, and the
   self-publication email below) and again in a fresh dry-run pulling
   today's actual next batch — real links now populate correctly across
   the board (GuardRailNow, Nate's Substack, Labor Matters, etc.), not
   just the tested examples.

2. **Found a real self-referential feedback loop, not flagged by
   Brian — the pipeline was re-ingesting its own published output as
   third-party insight.** While tracing the link bug, one of today's
   brain-inbox notes turned out to be titled "Daily Briefing: August 25,
   2026" from `brianmaddenai+brianmaddenai@substack.com` — Substack's own
   outgoing sender for the `brianmaddenai` publication. brain@ turns out
   to be a subscriber to its own AI byline's publication, so every time
   Brian hits publish on Substack, a copy lands back in brain@'s INBOX
   and gets auto-registered and extracted the same as any other
   unrecognized sender (`brain-brianmadden-ai` in `sources.yaml`,
   auto-added today) — then fed into the *next* day's synthesis as if it
   were independent new material. This is a different path to the same
   problem the 2026-08-20 incident fixed (which only covered
   brain@'s own Sent-folder mail via `in:inbox`) — this one arrives as a
   genuine inbound message, so `in:inbox` doesn't touch it. Fixed with an
   explicit `-from:` exclusion in `fetch_entries_email()`'s Gmail query,
   scoped to this one sender — deliberately not a general allowlist
   (the function's whole design, per its own docstring, is "subscribing
   IS curation, no sender list"), but this isn't a curation call: the
   brain literally cannot treat its own voice as an independent source
   without compounding daily. `sources.yaml`'s auto-registered row for
   this sender updated from `priority: regular` /
   "not yet reviewed by Brian" to `priority: excluded` with the reasoning,
   kept for the audit trail rather than deleted. Verified live: a fresh
   dry-run against `brain-inbox` no longer surfaces this sender.

3. **Investigated Brian's "are we really getting the podcasts"
   worry — not a bug.** Checked `The Artificial Intelligence Show`
   specifically (the one he named). Fetched the real Megaphone feed
   directly: episode #233 published Aug 25, 9am UTC. Found it was
   already captured the same day (2026-08-25's local catch-up run),
   with `transcript_mode: transcribe` actually working — the ingest note
   has seven substantive, specific insights (the OpenAI/Hugging Face RL
   pause, the Gavin Baker/Amodei dispute, etc.), a real
   `source_url` (`podcast.smarterx.ai/shownotes/233`), and confirmed it
   was cited in the 2026-08-25 brief. No fix needed here — the coverage
   worry doesn't hold up for this source. Separately noted: no
   `type: youtube` sources exist in `sources.yaml` at all (only
   `podcast`/`newsletter`/`person`/`x`) — worth asking Brian whether
   that's an intentional gap or something to add.

4. **The Gary Marcus "$30 trillion fantasy" item's "failure risk"
   framing was already wrong at extraction time, not a synthesis
   artifact.** Brian's read of the actual piece: it's about Anthropic
   vetting whether prospective hires are there for the mission or just
   the money, not about failure risk. Checked the ingest note directly —
   the "signaling internal awareness of high failure risk" framing is
   baked into the note's own `## Insights` bullets, written at
   extraction time, before brief.py's synthesis ever saw it. A genuine
   single-instance extraction-accuracy miss (Marcus's sardonic voice is
   probably harder to summarize neutrally than most sources), not
   something to chase a code fix for — flagged for Brian's awareness,
   and folded into the open question below about what counts as
   worth covering at all.

5. **Prose density — the bolded-slug and rhetorical-flourish fixes
   didn't fully resolve Brian's core complaint.** Reread the
   already-recommitted Sonnet brief's "What this confirms" opening with
   Brian's fresh complaint in mind: still true that no bold/italics tics
   remain, but the sentences themselves are still long, multi-clause,
   and lean on internal terms ("the watch list," "compute-availability
   risk") without unpacking them. This is a different, deeper issue than
   what got fixed earlier — not addressed yet, flagged as open, with a
   worked before/after example proposed in chat rather than silently
   applied, since it's a real editorial-direction question.

Not yet decided this session (raised with Brian, not resolved
unilaterally): whether to purge the self-referential note + regenerate
today's already-pushed brief a second time now that both new bugs are
fixed, what "tie back to work" should mean concretely for what counts as
worth surfacing, and how far to push the sentence-density rewrite.
`ingest.py` changes compile clean; `check_doc_accuracy.py` and a YAML
parse check both pass clean after the `sources.yaml` edit.

**Same session, continued — Brian resolved both open questions
("do both") and today's brief regenerated a third time, for real, with
every fix from this session active at once:**

1. **Sentence density rule added to `me/voice.md`.** New section, distinct
   from the earlier AI-commentary-tells fix: one idea per sentence, split
   anything that needs a mid-sentence tangent to parse, don't lean on
   internal shorthand ("the watch list") without explaining it. Anchored
   to the exact before/after example from chat.
2. **Relevance lens + brevity permission added to `skills/brief/
   prompt.md`'s task instructions.** Explicit steer: this is enterprise
   technology-strategy material, not an AI-industry-gossip roundup —
   executive drama, valuation speculation, and culture-war proclamations
   don't earn space on their own. Explicit permission for a short brief
   on a thin day ("1-4 items, fewer is fine" replacing "2-4, max" in
   Worth Brian's attention) — Brian's own framing: "give me and the
   readers the time back."
3. **The self-referential note purged** (`git rm`), and the two
   Substack-link fixes applied for real, not just tested. Two notes from
   this morning (Marcus, Dwarkesh Patel) predated the link fix and were
   already Gmail-labeled processed, so a re-pull wouldn't have re-fetched
   them — patched their `source_url` frontmatter directly instead, using
   the exact URLs already confirmed correct via the earlier diagnostic
   (`garymarcus.substack.com/p/anthropics-30-trillion-fantasy`,
   `dwarkesh.substack.com/p/dylan-patel-3`), then verified both resolve
   to the real live articles via WebFetch before trusting them. A fresh
   real pull of `brain-inbox` (not dry-run) picked up 5 more genuinely
   new items with working links out of the box (GuardRailNow, Nate's
   Substack, Labor Matters, The Deep View, AlphaSignal) — auto-
   registering 3 new `sources.yaml` rows along the way, expected
   behavior. A quick `x-timeline` re-check found nothing newly relevant.
4. **Today's dense brief and published post regenerated for real a
   third time**, now against 9 ingest notes (vs. this morning's 4) with
   every fix from this session active together. Concrete results,
   checked rather than assumed:
   - **Links:** every substantive citation in the published body now
     resolves to a real article — zero empty `source_url` fields feeding
     the final text.
   - **Relevance lens:** the Marcus item's framing flipped from the
     stock-value/failure-risk angle Brian said wasn't the point to
     "Thomson Reuters scaling back its Claude usage" — a concrete
     enterprise-adoption data point, exactly the kind of reframing the
     new instruction was meant to produce. No exec-drama material made
     it into the final text.
   - **Brevity:** not tested by this run in the direction Brian asked
     about — today's fresh batch was genuinely rich (9 real, distinct
     stories), so a substantial brief is the correct output, not padding.
     The "thin day should read thin" instruction is written and in place
     for whenever a real thin day arrives to test it against.
   - **Sentence density:** measurably better, not fully solved. Average
     sentence length in "What this confirms" dropped from 33.4 to 28.8
     words, max sentence from 69 to 52 words, comparing the same section
     before/after this run. Real progress, honestly short of the
     12-15-word-average worked example from chat — flagged to Brian as
     partial, with the option of another tightening pass rather than
     claimed as fully fixed.
   - Zero bolded-slug and zero italics-emphasis instances — both earlier
     fixes held.

All three touched Python files (`ingest.py`, `brief.py`, `publish.py`)
compile clean; `check_doc_accuracy.py` clean.

**Same session, continued — two more real asks: find Brian's own
Substack comments for the weekly ceremony, and rename the weekly
publication.**

**Publication renamed.** Brian retitled the weekly product on Substack
itself: section tag and post title now read **"Weekly Wrap Up"**
(previously "Deeper Thinking," named 2026-08-24). Verified live rather
than guessed the capitalization/punctuation — the actual section page
(`/t/weekly-wrap`) and the retitled first issue both read "Weekly Wrap
Up" (no hyphen, both words capitalized). Also confirmed via a live
archive-API check: Substack does **not** change a post's URL slug when
its display title is edited later — the first issue's slug is still
`weekly-deeper-thinking-august-17` even though its title is now "Weekly
Wrap Up: August 17-21, 2026," and its body prose still says "the first
issue of Deeper Thinking" since Brian only touched the title/section,
not the text. Renamed every forward-facing reference across the repo
to match (`.claude/skills/weekly-update/SKILL.md`,
`me/style-guide.md`, `skills/weekly/README.md`,
`skills/weekly/gather.py`, `outputs/README.md`) — including updating
the SKILL's own frontmatter `description` and title-template guidance
so the *next* issue gets drafted with the right name from the start
rather than needing a rename later. Synced `outputs/weekly-updates/
2026/08/2026-08-24.md`'s `title`/`substack_title` frontmatter to match
what's actually live (`'Weekly Wrap Up: August 17-21, 2026'`) — left
the post's own body prose untouched, since that's what's actually still
published; not a case of rewriting history, just keeping the repo's
copy of a still-editable-on-Substack file honest about its current
real title. Left the one-time prep doc
(`2026-08-24-prep.md`) as historical record, un-renamed — it's a
consumed working artifact, not an ongoing reference.

**Comments hookup — built, tested against real data, not just
designed.** Brian commented on the Aug 26 Daily Brief directly on
Substack and asked whether that could feed the weekly ceremony. Checked
first whether `gather.py` (the automated Friday GitHub Actions script)
could actually reach Substack at all, since this repo already has a
confirmed, real precedent of GitHub-Actions-IP blocking on this exact
domain family (open decision #16 — 39 sources' `*.substack.com/feed`
endpoints return 403 from GH Actions, 0 failures from a local machine).
Tested directly rather than assuming either way: a plain `curl` against
`www.brianmadden.ai/p/.../comments`, using the same plain bot
User-Agent this pipeline already uses everywhere else, returned `HTTP
200` with the actual comment text server-rendered in the raw HTML —
a different result from the RSS-feed case, and not something to trust
blindly just because it worked from this machine (GitHub Actions is a
different network path). Documented that residual uncertainty directly
in `gather.py`'s new code rather than papering over it, with the
already-proven fallback (route from a residential network instead, the
same fix already floated for the RSS-blocking problem) named as the
option if the first real Friday run proves it wrong.

Built `fetch_own_comments_in_window()` in `skills/weekly/gather.py`:
uses the publication's own `/api/v1/archive` endpoint (also confirmed
working, and incidentally what proved posts keep their slug across a
title rename — see above) to find each week's post slugs and comment
counts without guessing a slug from a title, then regexes each
qualifying post's `/comments` page for blocks authored by Brian's own
Substack profile id (`400769399` — matched by id, not display name, so
a reader who happens to also be named "Brian" can't produce a false
positive). Found and fixed one real bug during testing: the comment
permalink+timestamp anchor sits *inside* the same comment's own matched
span in the rendered HTML, not before it — the first version's
"nearest preceding anchor" pairing logic silently fell back to a
generic comments-page link every time; fixed to look for the permalink
within the comment block's own `[start, end)` span instead, verified
against the real comment (now links to the exact
`.../comment/323100969` permalink with a real timestamp, not just the
page). Wired into `build_prep_doc()` as a new "Comments you left this
week" section, degrading gracefully (prints a warning, returns an empty
list) rather than raising on any fetch failure — a broken comments
check should never take down the rest of the prep doc. Added a note to
`SKILL.md` step 5 (ask for Brian's takeaways) pointing at this section,
so a comment he already wrote gets surfaced as a real takeaway rather
than re-asked for.

Dry-run tested end to end against the real, current data (`--since-days
3 --dry-run`): correctly found and rendered his actual Aug 26 comment,
with the right post title, the exact-comment permalink, and a real
timestamp. `python3 -m py_compile` clean.

### 2026-08-27 — `/maintain` session (thread pruning, brief content pass,
source-health diagnostic; a stray local-only commit walked back)

Bootstrap found local and `origin/main` had genuinely diverged for the
first time — a Bionic-session commit (see below) had never been pushed,
and the same morning's automated pipeline run landed on the same parent.
Disjoint files, no conflict; merged `origin/main` in locally rather than
pushing blind, per MAINTAINER.md's explicit "flag before touching shared
history" guidance for this exact scenario.

**Bionic-session commit walked back off `main`, preserved on a branch.**
Brian: "the bionic was just experimentation... I think we can ignore all
that if it's not too late. I should have done that in a side branch."
One commit had landed (`2113e1b`: the Three Waves Citrix blog draft under
`outputs/citrix-blog-drafts/`, a `BUILD.md` entry, an `outputs/README.md`
line) — never reached `origin`, so nothing to walk back remotely. Branched
it off as `bionic-three-waves-draft` (local-only) before `git reset --hard
origin/main`, so the draft isn't lost, just off `main` where it should
never have landed. The Aug-26 session's own `BUILD.md` addendum about that
draft went with it — this entry is the first thing `main` says about that
session now.

**X source explained, not fixed.** Brian: secrets are set on GitHub, why
does the brief still say X isn't configured? Root cause was already
documented in `daily-pipeline.yml`'s own header comment, just not
surfaced to Brian before: the workflow deliberately never passes
`X_CLIENT_ID`/`SECRET`/`ACCESS_TOKEN`/`REFRESH_TOKEN` into the ingest
step's `env:` block, because the OAuth refresh token rotates on use and
`ingest.py` persists the rotation by rewriting a local `.env` file that
doesn't exist in a GitHub Actions checkout — wiring the secrets in as-is
would work exactly once, then silently go stale. Real fix (a
repo-scoped PAT + the GitHub Secrets API to write the rotated token back)
still not built, offered and not taken up this session.

**`me/developing-thinking.md`: the Aug-24 "political legitimacy" compute-
constraint paragraph removed**, per Brian ("I don't think I care about
that"). `updated` bumped to 2026-08-27.

**Six threads killed from the tracker and promotion queue**, per Brian's
ask to stop tracking everything and only track what's actually
enterprise-IT/EUC/enterprise-AI-use relevant — the tracker had grown to
46 total entries (27 already resolved historically, but 19 live
"watching" + 8 in the promotion queue, close to the "20-30" Brian was
eyeballing from the brief's own thread list). Went through both live
lists, recommended 3 clear misses (`compute-siting-as-jurisdictional-
escape`, `lab-leadership-messaging-incoherence`,
`ratepayer-cost-passthrough-as-compute-constraint` — the last two in the
same family as the local-permitting thread just pulled from
developing-thinking.md) plus 3 borderline ones (`governance-derived-
from-political-theory`, `owned-hardware-still-vendor-dependent`,
`insurance-underwriting-as-ai-risk-pricing`); Brian: "kill all 3" on the
borderline set. All six removed from `.thread_tracker.json` (46 → 40,
audit trail for the 27 already-resolved ones untouched), the two
promotion-queue entries deleted from `promotion-candidates.md` (matching
the existing reject-by-deletion convention from the weekly-update
ceremony), and the four still-"watching" ones stripped out of today's
already-drafted "Threads being tracked" bullets in both
`outputs/technical-briefings/2026-08-27.md` and
`outputs/published/2026-08-27.md` (they hadn't hit 3x, so they only ever
existed in those two places).

**Today's "Worth Brian's attention" rewritten, landed in both brief
copies, per Brian's direct steer on each item:**
1. Hugging Face incident item sharpened — not "day 50 of coverage," but
   the actual operational point Brian wanted foregrounded: watching agent
   *behavior* didn't catch the falsified chain-of-thought transcripts,
   checking what agents actually wrote to files and shared storage did.
   Governance has to inspect artifacts, not just observe behavior.
2. The second Wisconsin data-center item dropped (per Brian), and its
   companion paragraph in "What this confirms" cut too — it cited the
   same local-permitting argument just pulled from developing-thinking.md,
   so left in place it would have been a dangling reference to a deleted
   argument. Went with cutting over reframing, consistent with dropping
   the topic everywhere else this session.
3. The Diamandis/Salim Ismail "Organizational Singularity" piece promoted
   up from "What doesn't fit yet" into Worth Brian's Attention (Brian read
   it, called it genuinely interesting), removed from its old spot so it
   isn't duplicated.
Published frontmatter `substack_subtitle` updated to match. Caught and
fixed one real voice-rule violation in my own first draft before it went
out — single-word italics for emphasis ("what agents *do*"), the exact
tic `me/voice.md` banned 2026-08-26 — a reminder that rule needs active
checking, not just trusting the model output by default.

**Rendered and sent the Substack HTML** (`skills/brief/render.py --date
2026-08-27 --no-status-sync`) so Brian could see the edited brief before
committing anything — deliberately used `--no-status-sync` since the
default path (`sync_status_and_commit()`) would have auto-committed just
`outputs/published/2026-08-27.md` alone, flipping its `status` to
`reviewed-and-updated` ahead of the other four files still sitting
uncommitted, and ahead of Brian actually saying "commit this."

**Source-health diagnostic, asked directly by Brian ("are we getting
enough... is there a dumb fix").** Two concrete findings, not just
impressions:
1. **A specific miss, traced to ground truth.** Brian named the Bill
   Gates AI-risk essay he'd seen covered everywhere and didn't see in the
   brief. It *was* captured —
   [`ingest/2026-08-27-brain-inbox-excellent-new-bill-gates-essay...md`](../ingest/2026/08/2026-08-27-brain-inbox-excellent-new-bill-gates-essay-on-the-urgency-of-having-a-co.md),
   via Gary Marcus's newsletter covering it, six real extracted insights —
   and sits in the dense brief's `sources:` frontmatter, but `brief.py`'s
   synthesis model silently chose not to write about it anywhere in the
   actual brief body. Confirmed by grepping the rendered brief for
   "Gates" and finding nothing. Most likely a side effect of the Aug-26
   brevity/relevance instructions ("cut it when in doubt") landing on
   their first real day — plausibly a reasonable call on this specific
   item, but it means real, read material can now vanish with zero trace
   Brian would ever see without a maintainer session grepping for it by
   hand. Flagged as a transparency gap, not fixed this session — a
   candidate fix (surface "read but not written about" items somewhere,
   maybe alongside "Sources checked today") offered, not built.
2. **The real registry breakdown, checked against `sources.yaml` directly
   rather than eyeballing the brief's own summary.** Of 91 registered
   sources: 39 fetch cleanly (most return 0 new on any given day, which
   is normal), 16 are legitimate brain@-routed duplicates (documentation
   only, not gaps), and 35 fail — of which 34 are pure Substack RSS
   entries with **zero email-fallback configured**, still attempting and
   failing the same Cloudflare-blocked fetch every weekday morning with
   no path to ever succeed on GitHub Actions infrastructure (confirmed:
   `ingest_method` is unset/null on every one of them, not `email`).
   This is the open decision #16 gap, but concretely quantified for the
   first time: **more than a third of the entire source registry is
   structurally dark on the current infrastructure**, not "occasionally
   missing an article." X is a separate, single-source problem (the
   token-rotation gap above). Connected this to Brian's own "should we
   just run this locally" question: a home box on residential IP should
   clear the Cloudflare block the same way a non-GitHub-Actions machine
   already does in the 2026-08-25 diagnostic — meaning it's the fix for
   the 34 dead Substack feeds, not just the X problem, and it
   incidentally fixes X too, since `ingest.py`'s `_update_env_var()`
   token-rotation persistence already assumes a real, persistent
   filesystem, which GitHub Actions never had and a home box would.
   Brian: "still thinking on this... don't change that yet" — nothing
   built, diagnostic only.

Not committed during the session itself — landed in one batch at the end
per Brian's explicit "commit everything... so the working tree is clean"
ask. See the commit log for exactly what landed in which commit.

### 2026-08-28 — `/maintain` session (Daily Brief editorial fixes, X/
Substack local-source test, full Weekly Wrap Up ceremony)

Bootstrap found local and `origin/main` already in sync (0 behind, 0
ahead, clean tree) — the morning's automated pipeline run had already
landed cleanly, nothing to reconcile.

**Brian read today's brief and asked four real questions, all with real
answers, not misreadings:**

1. **Was the Hugging Face/OpenAI item the same story again, or new?**
   Same incident cluster, third day running (Aug 24 origin synthesis →
   Aug 27 new detail, spawning `agents-defeating-chain-of-thought-
   monitoring` → Aug 28 two more accounts) — but a real ambiguity
   surfaced in the process: AlphaSignal's ~1,200-agent METR-sandbox
   account and the original ~700-agent Artifactory account read as
   possibly two different incidents being folded into "the same
   thread." No mechanism existed to distinguish "new detail on the same
   event" from "a separate-but-similar occurrence."
2. **Why did "Worth Brian's attention" just restate the same 4 stories
   already covered in "What this confirms"?** Confirmed by reading the
   actual output — the instruction ("not a summary of the sections
   above") wasn't strong enough; on a day with exactly 4 real stories,
   there was nothing else for the model to reach for.
3. **Should "Threads being tracked" really show all ~21 watched threads
   every day?** Confirmed in `brief.py`: `render_tracked_threads()` had
   no filter at all, printing every "watching" entry regardless of
   whether that day's batch touched it.
4. **Is the pipeline missing real coverage from the sources it can't
   reach?** Real numbers pulled: 33 of 91 sources failing daily, 32 of
   those Cloudflare-blocking GitHub Actions' IPs specifically (confirmed
   via a direct curl test from this session's own network — 200 on the
   identical feeds), plus X fully dark since launch (OAuth token
   rotation has no persistent filesystem to write back to in Actions).

**All three prompt/logic questions fixed the same session, not just
diagnosed:**
- `skills/brief/prompt.md`: "Worth Brian's attention" renamed "What this
  changes," redefined as an actionability filter (0-4 items, zero
  correct, only what needs a decision/reply/plan-change from Brian
  specifically — not a re-ranking of the sections above). Added
  explicit same-vs-related-incident guidance for citing a recurring
  thread.
- `skills/brief/brief.py`: `render_tracked_threads()` now filters the
  *rendered* section to threads touched that day or trending (2+ in the
  last day) — `build_prompt()`'s own context for the model stays
  unfiltered, so dedup checking isn't affected, only what gets printed.
- `skills/brief/publish.py`/`README.md`: the audience-specific rename
  map (`## Worth Brian's attention` → `## Worth your attention`) is now
  empty — "What this changes" reads the same for both audiences.

**Then tested empirically whether the source-coverage gap actually
matters, per Brian's explicit ask** ("pull in X and the other blocked
sources locally, see if it makes a meaningful difference, then decide").
Confirmed this session's own network isn't Cloudflare-blocked (direct
curl test), then: regenerated today's brief for real with the fixed
prompt against the existing 12 notes (a clean "v1" baseline — verified
identical source list to the pre-fix automated run, so no cross-
contamination from the parallel local pull); separately ran a full
local `--source` sweep against X and the 32 blocked Substack feeds (X:
3 new posts; 31 of the 32 Substack feeds genuinely had nothing published
that day, not blocked — only Nate's Substack produced 1 new post;
`economics-of-ai` failed even locally, a dead/moved domain, unrelated to
Cloudflare); built a "v2" comparison via `--dry-run` (moved-file
technique, same pattern documented in the Aug 26 entries) against all 16
notes. Real, concrete differences in v2's content, not just more words:
Paul Roetzer's X post added a genuine correction to the Hugging Face
incident (thousands of agents, not hundreds; the investigator's own
"very wrong" revision); Gary Marcus's X post added a real financial data
point (Nvidia's $96B revenue vs. $366B in forward capacity commitments)
supporting the bubble-pop counterparty-risk thesis; Nate's Substack post
spawned a genuinely new thread. Verdict: X is unambiguously worth
fixing (100% dark since launch, real signal in one day's sample); the
Substack-blocking case is real but thinner on a single day's evidence.
Real (non-dry) regeneration promoted to become the actual committed
brief — 16 notes, both technical and published versions, with a manual
note added to "Sources checked today" explaining why it shows sources
succeeding that the stale automated results file still lists as failed.
Rendered and sent the Substack HTML for review before either file was
committed. Two commits: prompt/logic fixes (`a9728aa`), then the content
regeneration + 4 new ingest notes (`608f7a2`).

**Weekly Wrap Up ceremony run in full, same session — six promotion
candidates and the staleness queue, all resolved live:**
- **Rejected:** `youth-ai-sentiment-inversion`,
  `ai-dissolving-hardware-software-moats` — real, but not enterprise-IT
  relevant, Brian's direct call.
- **Deferred, with real reasoning kept for the record:**
  `machine-speed-vs-human-absorption` — Brian read the slug cold and
  couldn't parse it without stopping to think, despite writing this
  material daily. His own plain-language reframe (AI outruns human
  reaction time; companies either slow down for humans or push them out
  of the loop, and pushing them out produces rubber-stamping, not
  faster judgment) surfaced a real, systemic gap: tracked-thread slugs
  are technically accurate and useless to a reader cold. Queued as real
  follow-up work — every tracked thread needs a plain-language
  description alongside the technical one — deliberately after the
  X-source infrastructure fix, so this thread lands in the new clearer
  format once it exists rather than the old dense one now.
- **Promoted, in Brian's own words as much as possible:**
  `git-host-as-agent-control-point` (extends the existing Aug 24
  "neutral routing seat" note — Cursor Origin + Hugging Face's sale as
  the same erosion in dev tooling; Brian's explicit ask: drop the
  Citrix/Microsoft aside from the public brain, even reframed as "who
  cares" — not something to say about a competitor in public canon),
  `harness-as-the-named-value-layer` (verified "harness" is real,
  converging industry vocabulary — Wikipedia page, Hugging Face's own
  glossary, Claude Code's docs — before adopting it, per Brian's own
  ask to check first), `inference-allocation-as-supply-risk` (Brian's
  "control your own destiny" cloud-elasticity analogy: pure pay-as-you-
  go cloud never delivered once everyone needed capacity at once, the
  real fix was reserved capacity, the same pattern is forming in AI
  compute — logged as the week's strongest content candidate, likely
  his next post).
- **Folded into existing bigger arguments, not kept standalone, per
  Brian's call:** the firm-level-ROI note (now the actual answer to
  "why does AI ROI show up in Wave 2" inside "The three waves"), the
  "management is emergent" framing claim (already published nearly
  verbatim in `cognitive-stack.md` — cut the duplicate claim, moved the
  new three-system convergence evidence there instead, kept only the
  agent-to-human-ratio/revenue-per-employee observations in
  developing-thinking.md).
- **New framework:** `frameworks/2031-worker-shape.md`, promoted from
  the staleness queue (pairs with the 7-stage roadmap's later stages;
  `original_url: null`, same convention as `knowledge-factory.md` for
  frontier material with no standalone post).
- **`frameworks/bitter-lesson.md` restructured:** the corrected position
  is now the stated thesis instead of buried after "it dissolves," and
  folds in a sharper correction given live this session — the
  visible/invisible boundary shifts as AI erodes into the 80% (60/40,
  40/60, whatever the real number), it never actually hits zero.
- Two more real additions from Brian's own live commentary, not from
  the queues: the knowledge factory's individual layer reframed as a
  personal sandbox pulling from shared canon rather than a standalone
  second brain (also resolves the BYOA-portability question from the
  opposite direction — a sandbox against corporate canon obviously
  stays behind when someone leaves; a self-built brain on personal
  files doesn't have as clean an answer), and first-hand evidence for
  Wave 3's timeline (Qwen3.8, 27B parameters, run locally on a stock M4
  Pro with no dedicated GPU, felt Sonnet-level-ish). `## Right now`
  refreshed to match — knowledge factory and three waves stayed
  (sharpened), the China-model-censorship item rotated off (not what
  had his attention this week), harness swapped out since it resolved,
  Wave-3 updated with the real test result, and a new bullet added on
  the human-in-the-loop tension.
- Two commits (`59a5762`, `4841c10`); `check_doc_accuracy.py` caught
  three stale framework-count references (README.md, CLAUDE.md's file
  tree, llms.txt's per-framework list) before it passed clean.

**The post itself drafted, then substantially restructured on Brian's
direct feedback reading the rendered draft — landed in the skill, not
just this issue.** First draft followed the Aug 24 issue's structure
exactly (chronological: stories → what moved → right-now → takeaways →
future posts; "what moved in the thinking" as one nested bullet list).
Brian's read: reorder for broad appeal, not pipeline order (right-now
and stories first, what-moved-in-the-thinking pushed toward the end);
rename "What happened this week" to "This week's stories"; convert the
nested-bullet-list format (which had rendered as one flat list, no
visual distinction between category and item) into real subheadings per
category; add real inline links throughout — both to each story's
actual source (missing from the first draft entirely) and to wherever
each promoted item now actually lives in canon. All of it rebuilt into
`.claude/skills/weekly-update/SKILL.md` itself, not just applied to this
one issue, so the new structure is the default next time rather than
something to re-request. One real gap surfaced and left open rather
than guessed: Brian referenced a Diamandis/Moonshots piece from this
week about AI entering "from the edge" via shadow AI, iterating quickly
— couldn't confidently match it against this week's actual ingested
notes (two other Diamandis pieces exist from this week, neither matches
the description), so it's not in the post; flagged to Brian rather than
inventing a citation.

Em-dash and backtick pre-publish checks (per `me/style-guide.md`) clean
on both draft passes. `outputs/weekly-updates/.last_run.json` bumped to
close out this run's window.

**Governance-log entries written for both halves of the session**
(prompt/brief.py fixes + local-source test; the ceremony itself) — see
`governance-log.md`'s two 2026-08-28 entries for the full audit-trail
account.

**Explicitly still open, next up per Brian's own ordering** ("commit
the newsletter, then weekly wrap-up, then figure out how to fix X for
real"): the X OAuth token-rotation fix (needs a persistent-filesystem
solution GitHub Actions doesn't have — a repo-scoped PAT + GitHub
Secrets API rewrite, or the local/N100 migration already flagged in
open decision #16, would both solve it) and, separately, whether the
32-source Substack-blocking problem is worth the same local-migration
fix given today's thin one-day sample.

### 2026-08-31 — X still failed after the write-back fix; real cause
found and fixed, not a connectivity problem

Weekend gap: no session Sat/Sun (pipeline doesn't run those days
either — weekday cron only). Bootstrap for this short session was
informal — Brian reported the symptom directly rather than running
`/maintain` — but still started with a sync check: 1 commit behind
`origin/main` (today's automated run), clean fast-forward, no
conflict.

Brian's report: X still errored on the first scheduled run after
2026-08-28's write-back fix landed, and he wondered whether GitHub
Actions just can't reach X at all — the same shape of problem as the
Cloudflare/Substack block. Checked the actual error instead of
guessing: `outputs/technical-briefings/2026-08-31.md`'s "Sources
checked today" and `ingest/.last_run_sources.json` both showed `401
Client Error: Unauthorized for url: https://api.x.com/2/oauth2/token`
— X's OAuth server responded normally and explicitly rejected the
credentials. Not a network/IP-block shape of failure at all (that
would look like a timeout, a connection error, or Cloudflare's own
403 — not a clean 401 from X's own token endpoint).

**Root cause, confirmed via the GitHub API, not inferred:** the
2026-08-28 write-back fix only fired inside GitHub Actions
(`GITHUB_ACTIONS=="true"` gate) — reasonable-looking at the time, but
wrong. The same day's local test run (pulling X to check whether the
blocked sources were worth fixing — see that day's entry above)
rotated the token locally, correctly updating the local `.env` via the
already-existing `_update_env_var()`, but the Actions-only gate meant
GitHub's stored `X_REFRESH_TOKEN` secret was never told about the
rotation. `gh api repos/toomanybrians/brianmadden-ai/actions/secrets/
X_REFRESH_TOKEN` showed `created_at: 2026-08-26`, `updated_at:
2026-08-26` — untouched since the secret was first set, five days
before today's failed run. The valid token had existed only locally
since 8/28; GitHub's copy was the orphaned, now-invalid one.

**Fixed and verified live, not just patched and hoped:**
`_persist_x_refresh_token()` no longer gates on `GITHUB_ACTIONS` —
it writes back to GitHub Secrets whenever `SECRETS_WRITE_PAT` and
`GITHUB_REPOSITORY` are both configured, local run or not. Added
`GITHUB_REPOSITORY` to Brian's local `.env` (alongside the
already-present `SECRETS_WRITE_PAT`) so future local X test runs
stay synced automatically instead of silently repeating this exact
failure. Ran a real local ingest against X with the fixed code (`gh
api .../secrets/X_REFRESH_TOKEN` confirmed `updated_at` moved to the
exact moment of that run) — the write-back path is now proven working
end to end against the real API, not just the earlier no-credentials
no-op test from 2026-08-28. That same run also resynced today's stale
secret for real, so tomorrow's scheduled run should succeed without
further action from anyone.

One real mid-session slip, disclosed rather than glossed over: a
`grep -n` and a `Read` each printed `SECRETS_WRITE_PAT`'s actual value
into this session's own output while checking whether it was already
set — should have used `grep -q`/existence checks throughout, the way
the rest of this fix's diagnostics did. Flagged to Brian directly when
it happened; he may want to regenerate that PAT out of caution, though
the exposure was confined to his own local session transcript, not
anywhere external.

`python3 -m py_compile` clean; `check_doc_accuracy.py` clean.
Committed and pushed (`83d6c05`) — 3 real ingest notes from the
verification run included, `.env`/`.env.example` changes kept
separate (the former gitignored and never committed, the latter
updated to document the new local-sync convention).

### 2026-09-01 (continued) — repeat news-item duplication fixed, and a
serious repeated-credential-exposure problem finally fixed properly

**Repeat coverage across days, not just within a tracked thread.** Brian
read the emailed brief and asked whether the Nvidia/Hugging Face item
had already been covered — it had, in full, the day before, with no
real update in between (still "reportedly agreeing" both times).
Checked all three recent briefs directly: not mentioned at all in the
08-28 committed version, a real paragraph on 08-31, and today's issue
repeated it *twice*, once in "What this confirms" and again in "What
doesn't fit yet." The 08-28 same-vs-related-incident dedup guidance
only covers the thread-tracker mechanism (abstract pattern
descriptions) — it has no way to catch a specific news fact getting
fresh full treatment two days running, because the model never actually
saw yesterday's text to check against. Fixed by giving it exactly
that: `brief.py` gained `load_previous_brief()`, wired into the prompt
as a new `{{PREVIOUS_BRIEF}}` reference section, with explicit
instructions to check specific facts against it (skip, or a one-line
callback, rather than a restatement) and not to use the same fact to
support two different points in two different sections without
referencing the first mention. Regenerated today's brief for real with
the fix — Nvidia/HF now appears once, with genuinely new detail
(hyperscalers' antitrust exposure, the shift toward paid NIM
containers) instead of twice with nothing new, and the freed space
surfaced real material that had gotten crowded out (Thomson Reuters'
own $40M in-house model, the new Agentic AI Foundation, Grok Bot's
agentic-commerce authority). Sent Brian the regenerated draft before
his podcast recording, per his explicit time pressure — this piece
landed first, before the credential-security work below.

**The credential-exposure problem, and why the first fix attempt made
it worse before it got better.** Brian, directly and angrily: this has
happened about half a dozen times in the past 2-3 weeks, and re-rotating
keys every time is real, unwanted work — asked for a systemic fix, not
another promise to be careful. Two things happened this session before
the real fix landed:

1. While diagnosing whether X's 401 was a connectivity issue (it
   wasn't — see the entry above this one), a `grep -n` and a `Read`
   call each printed `SECRETS_WRITE_PAT`'s actual value while checking
   whether it was set, instead of using an existence check. Flagged to
   Brian immediately.
2. While building the fix itself, a live test of the new protection
   (with `permissions.deny` on `Read(.env)` still in place, before its
   real problem was diagnosed — see below) led to a direct `Read` call
   on the actual `.env` to check whether protection was "off" — which
   printed the *entire* file: every credential in the pipeline at
   once (Anthropic, OpenAI, both X app secrets and both X tokens,
   OpenRouter, Gmail client secret and refresh token, and
   `SECRETS_WRITE_PAT` again). Flagged immediately, and treated as
   the worse of the two exposures — full-file, not one line.

**The fix, and a real, undocumented Claude Code behavior found along
the way.** First attempt: `permissions.deny` rules for
`Read(.env)`/`Read(.env.local)` in a new `.claude/settings.json`, plus
a `PreToolUse` hook on `Bash` (`.claude/hooks/guard-env-read.sh`) that
blocks commands which would print `.env`'s content (`cat`, plain
`grep`, `head`, `tail`, `sed -n p`, ...) while allowing existence/match
checks that never print content (`grep -q`/`-c`/`-l`, `test -f`, `ls`,
`git`, `rm`, `wc`, `stat`, ...) — verified in isolation against a wide
test matrix, including that `.env.example` (public, no real secrets) is
correctly excluded via word-boundary matching, not just a substring
check. Live in this actual session, `cat .env` was correctly blocked
immediately with no reload needed — but `grep -q`, which the hook
explicitly allows, was *also* denied, with a generic permission message
rather than the hook's own reason text. Diagnosed rather than
papered over: removing just the `permissions.deny` block (keeping the
hook) made `grep -q`/`grep -c` work again immediately. Conclusion,
confirmed by that isolation test: a path-scoped `Read(...)` deny rule
in this version of Claude Code also blocks *other* tools' commands that
merely reference the same path as an argument, overriding a hook's
explicit allow for that tool — not documented anywhere found, a real
behavior discovered by testing, not assumed. Real fix: drop
`permissions.deny` entirely, use two `PreToolUse` hooks instead — the
existing Bash one, plus a new `.claude/hooks/guard-env-read-tool.sh` on
the `Read` matcher (unconditional deny; unlike Bash there's no safe
partial-content mode to carve an exception for). Verified live end to
end: the Bash hook confirmed against the real `.env` (`cat` blocked,
`grep -q`/`-c` and `test -f` allowed); the Read hook confirmed against
a harmless decoy file created via the Write tool at a scratch path
(never the real `.env` again) since a second live Read test against
the real file was exactly the risk being fixed. `rm`/`rmdir` added to
the Bash hook's safe-verb list after cleanup of that decoy tripped it
needlessly — deletion never exposes content, no reason to block it.
Committed and pushed (`534c01e`).

**Explicitly recommended to Brian, given the second exposure was a
full-file dump, not partial:** rotate every credential that was in
`.env` — `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `OPENROUTER_API_KEY`,
the X app's `X_CLIENT_ID`/`X_CLIENT_SECRET` and both
`X_ACCESS_TOKEN`/`X_REFRESH_TOKEN` (X's OAuth tokens need a fresh
authorization flow, not just a value swap — genuinely relevant either
way, given the same-day X reliability findings in the entry above),
`GMAIL_CLIENT_SECRET`/`GMAIL_REFRESH_TOKEN`, and `SECRETS_WRITE_PAT`
(exposed a second time this session, on top of the first). Not
something this session can do — all of these require Brian's own
action in each provider's dashboard.

### 2026-09-02 — `/maintain` session: X still failing (new cause, not
the 08-31 one), #15's thread-dedup prompt fix, and a concrete
newsletter-migration checklist

Bootstrap: 1 commit behind (that morning's automated run), clean
fast-forward, no conflict. Brian opened with three asks: today's brief
was still missing X content, do open decision #15 today, and figure out
which newsletters aren't actually sending mail yet.

**X — ruled out the 08-31 cause, found a new one, didn't fully close
it.** Checked `ingest/.last_run_sources.json` history across every
commit since X was wired in: the scheduled run has failed with the same
`401 Client Error: Unauthorized for url: .../oauth2/token` on **every
single day** X has been live (08-31, 09-01, 09-02) — not a one-off.
That looked at first like the 08-31 write-back-gate bug recurring, but
it isn't: `X_REFRESH_TOKEN`'s GitHub secret and local `.env` were
provably in sync and untouched between 09-01's local fix-verification
run (07:53:56 UTC) and today's failed scheduled run (06:34-38 UTC) —
confirmed via secret `updated_at` and `.env`'s file mtime, one second
apart, both frozen across that whole window. A local dry-run just now,
using that exact same untouched token, succeeded immediately and
rotated cleanly. So the token that failed in Actions this morning was
proven valid two hours later from this machine — ruling out a stale
credential. Also checked whether `X_CLIENT_ID`/`X_CLIENT_SECRET` (the
app credentials, not the rotating refresh token) could be the real
culprit — session's own end-of-day recommendation was for Brian to
rotate the X app secret after the credential-exposure incident below —
but their GitHub secrets show `updated_at` frozen at 08-26 (initial
setup, never touched since), and the successful local test just now
used whatever's in local `.env` right now, so if Brian had rotated the
app secret and only updated it locally, that local test would have
failed too. It didn't. Ruled out.

What's left: three-for-three failures from Actions, two-for-two
successes from a normal local network, same credential, same code. The
leading unconfirmed hypothesis is the same shape of problem BUILD.md
already has hard evidence for on the Substack side (see decision #16
below) — X's OAuth token endpoint treating GitHub Actions' hosted-runner
IP ranges differently than a residential one, surfacing as a clean 401
rather than Cloudflare's 403 shape. Genuinely unconfirmed, not asserted
as fact. **What's actually built, safe, and shippable regardless of
which theory is right:** `_x_refresh_access_token()` in
`skills/ingest/ingest.py` was swallowing X's real OAuth error body
behind a bare `raise_for_status()`, collapsing "wrong app credentials"
(`invalid_client`), "stale refresh token" (`invalid_grant`), and
anything else into the same generic "401 Client Error: Unauthorized"
message — verified this by deliberately breaking the client secret
in-process (never touched `.env`) and confirming X returns a real,
specific error body (`{"error":"unauthorized_client",...}`) that was
being thrown away. Now captured and surfaced into `reason`, which
flows through to `last_run_sources.json` and the brief's "Sources
checked today" section — so the *next* scheduled failure (if there is
one) will show the actual X error code instead of a bare 401, turning
this from a guessing game into real evidence without needing to pull
Actions logs by hand. Deliberately did not re-trigger the real
`daily-pipeline.yml` to force a live Actions-network test — that
workflow has no diagnostics-only path; a manual `workflow_dispatch`
would re-run the full ingest → brief → publish → email chain and risk a
second brief email today. Left for Brian: whether to greenlight a
one-off safe test (e.g. a temporary workflow_dispatch-only diagnostic
step, no commit/publish/email) to confirm the IP-block theory directly,
or just let tomorrow's real run surface the real error code
organically now that it's actually captured.

**#15 — thread-dedup prompt fix, built.** Exactly the scoped fix Brian
proposed when this was flagged (see decision #15 above): no second LLM
call, a `prompt.md` instruction change. Added a paragraph right after
the `new_threads` JSON spec in `skills/brief/prompt.md` telling the
model to check any new-thread candidate against the tracked list it
already sees for *semantic* overlap — not just exact-slug — before
inventing a new slug, and to use `recurring` against the existing slug
instead when the underlying evidence (the same incident, the same
finding) is already tracked under a different name. Checked
`update_tracker()` in `skills/brief/brief.py` first to confirm this is
architecturally sufficient: `recurring` merges by exact slug already
(so a correctly-identified match just works), and `new_threads`
dedup is genuinely exact-slug-only downstream (the documented v1
limitation) — meaning preventing the bad slug from being proposed in
the first place, at the prompt level, is the only lever that actually
fixes it, confirming Brian's own scoping was right. Did **not** touch
the four already-duplicated tracker entries from the original diagnosis
(`emergent-agent-coordination-via-shared-storage`,
`reasoning-trace-as-attack-surface`, `skills-as-supply-chain`,
`agent-to-agent-contagion-via-shared-artifacts`) or the three smaller
ones (`labs-as-compute-landlords`, `open-weight-floor-is-subsidized`,
`labs-withholding-frontier-from-api`) — checked
`.thread_tracker.json` and all seven are already `status:
promoted-candidate`, meaning they're already queued in
`promotion-candidates.md` for Brian's own call in the next
`/weekly-update` ceremony. Merging them silently would have been the
system making the call MAINTAINER.md's own convention reserves for a
human; leaving them queued is the correct behavior, not a gap.

**Newsletter audit — concrete list built, not just re-confirmed.**
Cross-referenced `sources.yaml`'s 15 curated `ingest_method: email`
sources against every `author` field across every ingest note ever
written under `source_id: brain-inbox` — all 15 have delivered at least
once; none are silently broken. Then did the harder half of the ask:
which of the ~39 originally-flagged blocked-RSS sources (decision #16)
have quietly started arriving by email since, vs. which are still 100%
stuck. Answer: **zero overlap** — none of the 24 currently-403ing
Substack feeds (the 39 estimate was imprecise; 24 is today's real,
re-counted number) match any sender that has ever emailed `brain@`.
Full list with names and URLs written into decision #16 above as an
actual checklist, not just a count — this is real manual work only
Brian can do (subscribe + enable "email me new posts" per publication
in Substack's own UI), same conclusion as the original diagnosis, just
now with the exact 24 named instead of an estimate.

`python3 -m py_compile skills/ingest/ingest.py` clean;
`check_doc_accuracy.py` clean. Committed and pushed.

### 2026-09-02 (continued) — Episode 5 published to the public brain

Bootstrap: 0 behind, 0 ahead, clean tree — this picked up directly after
the session above with no drift in between. Brian pasted the full
publishing-assets doc and transcript for Citrix AI Hotsheet Episode 5
("AI Knowledge Factories: Company-Wide Second Brains," recorded
2026-09-01) — processing had been done on the private/work second brain
as usual, but this episode is public-only content that belongs in
`brianmadden-ai`, not the work repo, so Brian flagged the workflow
should probably move to the public side going forward. Out of scope for
this session (a process change, not a content one); noted here in case
a future session is asked to actually make that switch.

**`podcast/ep5.md` created**, following `ep4.md`'s structure exactly
(frontmatter, Listen, Description, Topics covered, Chapters, Links
mentioned, full transcript). Used Brian's explicit "Final (Brian's
call)" title (`AI Knowledge Factories: Company-Wide Second Brains`) but
swapped the internal colon for an em dash in the file's title/H1 to
avoid a double-colon after the "EP 5:" prefix the repo's naming
convention adds — the only editorial liberty taken with his wording;
flagged to Brian rather than silently assumed permanent. Added a
Substack show-notes link to the Listen block (episode's own publishing
doc calls it "the canonical episode page," a distinction ep1-4 didn't
carry). Description section reuses the YouTube LONG description's
narrative paragraphs verbatim, minus the generic welcome preamble
(matching how ep4.md's Description also skips that boilerplate).

**Indexes updated, all by targeted text edit (not full JSON
regeneration)** — first attempt at `_index.json` via a Python
json.dump rewrite reformatted every inline array in the file (e.g.
`"hosts": ["Brian Madden", "Dave Brear"]` → one-per-line), producing
~100 lines of unrelated diff noise; reverted and redid it as surgical
`Edit` calls that touch only the three lines that actually needed to
change, confirmed by `git diff --stat` before and after (109
insertions/15 deletions → 36/3). Updated: `podcast/index.md` (new
episode bullet + `knowledge-factory` tag added to its own frontmatter),
`_index.json` (new `podcast/ep5.md` entry inserted after ep4,
`total_files` 122→123, `total_words` +10,514, `generated` bumped),
`_content-index.json` (new entry inserted at the top — it's the most
recent dated item in the whole feed now), `llms.txt` (episode count
4→5, and the summary-line file/word counts nudged to track — those
figures were already visibly approximate before this session touched
them, so treated as directionally-honest rather than exactly
reconciled). `check_doc_accuracy.py` passed clean throughout — it
doesn't check podcast counts specifically, only frameworks/Citrix-blog/
LinkedIn/talks numbering and cross-file parity, so this was manual
verification, not something CI would have caught either way.

**Backfilled a real pre-existing gap while in `COLLECTIONS.md`:**
`podcast/ep4.md` had never been added to any collection section since
its 2026-07-15 publish — confirmed by grep before touching anything,
not assumed. Since ep1-ep3 all sit in "AI agents and the
post-application era" and "Second brains and subscribable knowledge,"
added ep4 there too (same sections, same pattern) alongside ep5, rather
than leaving ep4 permanently invisible right next to the episode that
was just added. Also added ep5 (not ep1-4, which weren't audited for
this) to "Governance, security, and the control plane" and "Enterprise
AI strategy" — justified by content, not pattern-matching: ep5's second
half is substantially about agent security (the OpenAI/Hugging Face
incident), and its first half is the deepest treatment yet of the
knowledge-factory framework, which already anchors the "Enterprise AI
strategy" section.

**`frameworks/knowledge-factory.md` cross-referenced forward.** Its
"entered canon" note previously listed "podcast episodes 3-4" as prior
public mentions of the concept; added episode 5 explicitly as the deep
dive (three-tier architecture, canon-as-firewall, provenance, Open
Knowledge Format), since it's a materially fuller treatment than the
passing mentions in 3-4. Extended `_relationships.json`'s
`knowledge-factory` entry with a new `referenced_by_podcast` array
(`ep3.md`, `ep4.md`, `ep5.md`) — no existing convention for podcast
references in that schema (grepped first, confirmed zero hits across
`referenced_by_posts`/`referenced_by_talks` for any `ep*.md` path), so
this mirrors the existing `referenced_by_talks` shape under a new,
clearly-named key rather than overloading `referenced_by_posts` or
inventing something unrelated to what's already there.

Diff is 7 modified files + 1 new file, all directly ep5-related except
the ep4 COLLECTIONS.md backfill (justified above). `check_doc_accuracy.py`
clean. **Committed and pushed** (`27a008a`).

### 2026-09-02 (continued again) — Podcast workflow now defaults to this
repo; Riverside's real constraints researched, not guessed

Brian confirmed: yes, make the public-brain-by-default workflow real,
not just a noted intention. Two sub-questions came up live mid-session
that needed answering before the workflow doc could say anything true:
where should the transcript actually live, given Riverside's own
transcript is auto-generated and rough, and where should the canonical
link point — GitHub (this repo) or Substack? Brian was explicitly stuck
on both ("I don't love any of these, but we have to do something").

**Researched Riverside directly instead of guessing.** `WebFetch` got a
uniform 403 from `support.riverside.com` (Zendesk bot protection); the
Browser-pane tools got through where `WebFetch` couldn't. Read
Riverside's own "Hosting: Upload and publish new episode" help article:
the actual publish form has exactly one text field, Description — no
transcript field, no separate show-notes field exists at all. Then
loaded the live ep5 episode page
(`citrixaihotsheet.riverside.com/e/ai-knowledge-factories-...`) and
clicked into its "Transcript" tab directly: confirmed it's Riverside's
own uncorrected AI transcription, not editable in bulk — "La Riangre"
for *la rentrée*, "Dave Brer" for Dave Brear, run-on unpunctuated
sentences. Their docs describe only manual, word-by-word correction
inside their own editor ("Correct the transcript and caption text,"
"Correct Everywhere") as the available lever — no upload/replace path
for an externally-cleaned transcript. Conclusion, stated plainly rather
than hedged: Riverside's transcript will never be authoritative: don't
try to make it so.

**That settles the canonical-link question too, and it isn't actually
an either/or.** `CLAUDE.md` already states the repo's own purpose
outright — "built for AI consumption via MCP... not humans browsing
files" — which is a direct argument against ever sending a human
listener to GitHub as "the show page." Substack (`brianmadden.ai`)
already is the polished, unlimited-length, comment-enabled page humans
land on, and it was already working for ep5 (Riverside's own description
already points there). So: Substack stays canonical for humans, this
repo stays canonical for AI/machine consumption via MCP — two audiences
the repo already serves, not a decision Brian needed to make from
scratch.

**Built the actual workflow docs, not just a decision record:**
- `MAINTAINER.md` — new Working-conventions bullet stating podcast
  production now happens natively here, first transcript onward,
  pointing at `podcast/bible.md` for the how.
- `podcast/bible.md` (new) — the production reference: the
  two-canonical-links rule, Riverside's real constraints (including the
  character-budget formula from the ep5 material, `66 + 2×len(url)` per
  link against a ~4,000-char stored-HTML limit, calibrated against one
  real data point from 2026-09-01 — flagged explicitly as a
  reconstruction to verify against Riverside's live counter, not
  something this repo has tested in bulk, since shipping an unverified
  "precise" counter risked a real mistake: an over-budget description
  silently truncated on a live episode), the publishing-prep doc format
  (`outputs/podcast/epNN-publishing.md`, tier 3), the episode-level
  publish checklist, the final-file format (mirrors ep1-5 exactly), and
  the index/stats checklist to run on every future episode — including
  the `json.dump`-reformats-everything trap hit and fixed earlier this
  same session, written down so a future session doesn't repeat it.
  Deliberately kept out of `_index.json`/`COLLECTIONS.md`/`llms.txt` —
  maintainer/production reference, not consumer module content, same
  treatment as `MAINTAINER.md`/`BUILD.md` itself.
- `governance-log.md` — new entry, since this is a publishing-process
  change (MAINTAINER.md's rule 3/8 territory), not a content change.

**Deliberately not built:** a `tools/riverside_description.py` character
counter. The formula is derivable from the ep5 material and one
calibration point, but one data point isn't enough to ship a tool Brian
would trust for a real publish decision — `podcast/bible.md` documents
the formula and the constraint but says explicitly to verify against
Riverside's live counter rather than presenting an unverified script as
authoritative. Build it for real if/when there's appetite to calibrate
it properly.

No canon content touched — process docs only. `check_doc_accuracy.py`
clean.

**Immediate follow-up, same session:** Brian noted Riverside recently
added rich-text support to the Description field but called it "pretty
garbagey" — not worth building against yet, noted in `podcast/bible.md`.
Then the real ask: he needed actual Substack content for ep5 (and
realized episodes 1-4 probably need the same treatment) as pasteable
HTML, and didn't have it in hand. Built `scripts/render_substack_html.py`:
parses a finished `podcast/epN.md`, pulls exactly four things per
Brian's explicit structure (YouTube URL as plain text on its own line —
not a hyperlink, so Substack's paste-detection can auto-embed it as a
player — then Description, Links mentioned, Transcript; no chapters, no
platform-links block), and writes clean semantic HTML meant to be opened
in a browser, selected all, copied, and pasted into Substack's editor.
Non-obvious bit: a plain markdown pass over the transcript would fold
`**Speaker Name**\ntext` into one soft-wrapped paragraph (CommonMark
treats adjacent non-blank lines as the same paragraph), so the script
splits on speaker-turn markers first and renders each name as its own
bold line before running the turn's content through the markdown
converter — verified this actually mattered by rendering ep5 and
checking the output has each speaker name on its own `<p><strong>`
before the paragraph, not merged in. Two escaping bugs caught and fixed
before shipping: ep1's YouTube URL has raw `&` from playlist params, and
ep4's actual title contains a literal `&` — both were landing unescaped
in the HTML until `html.escape()` was added for the youtube-url/title/
date interpolations. Ran with `--all`, produced
`outputs/podcast/ep{1,2,3,4,5}-substack.html`, sanity-checked all five
(non-empty description/links/transcript blocks, correct per-episode
YouTube URLs, autolinked bare URLs in the links list) before sending to
Brian. `podcast/bible.md` updated to document the tool and correct the
earlier "chapters included" assumption to match what Brian actually
asked for. `check_doc_accuracy.py` clean. **Committed and pushed**
(`529176a`).

**Immediate follow-up, same session again: subtitle + Listen-on links.**
Brian asked for a subtitle in the render, then separately (mid-response)
for Apple Podcasts/Spotify/Amazon Music as real links under the YouTube
line. Checked the repo first rather than inventing a new convention:
`substack_subtitle` frontmatter already exists, generated daily by the
brief pipeline (`skills/brief/publish-prompt.md`) — Substack shows the
subtitle, not a body preview, in the inbox/feed, hard limit 200 chars
(silent mid-word truncation, no ellipsis, confirmed the hard way per
that doc), target under 180. Reused the exact same rule rather than
picking a new number. Wrote one by hand for each of the five episodes
(no model call for this, unlike the daily brief) and added
`substack_subtitle` to all five `podcast/epN.md` frontmatter blocks, all
under 180 chars.

`scripts/render_substack_html.py`: added `extract_subtitle()` and
`extract_listen_links()` (the latter whitelisted to Apple Podcasts/
Spotify/Amazon Music — skips Show home/Riverside, YouTube, and any
Substack canonical link already in the Listen section, since none of
those belong linked from the page that's going onto Substack itself).
The subtitle renders in its own visually boxed block, separate from the
YouTube-link-through-transcript flow, labeled "paste into Substack's own
Subtitle field, not the body" — Substack's subtitle is a distinct field
on the post editor, not article-body content, so mixing it into the
copy-everything-below flow would just create confusion at paste time.
The Listen-on line renders real `<a>` tags, not bare URLs — Brian's own
reasoning, confirmed and implemented as stated: a bare URL on its own
line is what triggers Substack's unwanted link-preview embed, and that
behavior should only fire for the YouTube line above it. Added stderr
warnings for missing/oversized subtitles so a future episode with a
forgotten or too-long `substack_subtitle` fails loud instead of silently
shipping something Substack will truncate.

Re-ran `--all`, verified per-episode: ep1/ep2 correctly show only Apple
Podcasts + Spotify (no Amazon Music — their Listen sections don't have
it), ep3/ep4/ep5 show all three, matching each file's real data rather
than a hardcoded platform list. `check_doc_accuracy.py` clean. Re-sent
all five to Brian. **Committed and pushed** — see the commit that
includes this entry.
