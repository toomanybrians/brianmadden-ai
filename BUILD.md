# BUILD.md — v2 rebuild journal

> ## ⚠ THIS FILE IS PUBLIC. THINK BEFORE YOU WRITE HERE.
>
> This repo is public on GitHub, and so is **every past version of this file**.
> Before adding anything, ask: *would I be fine with this on a conference slide,
> in a journalist's inbox, and in my employer's HR inbox?*
>
> **Never record:** compensation or other personal finances · employer-internal <!-- public-ok: the banner names the forbidden topics -->
> strategy, people, customers or disagreements · private network, machine or
> account details · credentials, or where they live · private details about
> other people · offhand personal quotes you wouldn't say on stage.
>
> Write **decisions and outcomes**, not asides. Deleting a line later does **not**
> remove it from git history. `scripts/check_public_safe.py` runs on every commit
> and in CI, but it only catches patterns, not judgment. The judgment is yours.

The working memory of the brianmadden.ai v2 rebuild. Every session (human +
Claude Code) starts by reading `CLAUDE.md`, this file, and
`docs/brianmadden-ai-v2-architecture-and-launch-plan.md` — and ends by
updating the log below. Chat threads are disposable; this file is not.

## Kickoff

**Bootstrap a new session with `/maintain`** (`.claude/skills/maintain/SKILL.md`):
reads `.claude/lessons.md`, `MAINTAINER.md`, the live sections of this file
(Decisions made, Open decisions, Day plan, the last 2 session-log entries,
not the whole journal), and real `git status`, then reports back before
anything else runs. Before `/maintain` existed the manual pattern was:
**"Read MAINTAINER.md and BUILD.md, then let's pick up where we left off."**
The per-day kickoff prompts for Days 2, 4 and 5 were trimmed on 2026-10-04
(`git log -p -- BUILD.md` has them).

## Decisions made (Aug 9, 2026)

- Architecture flipped: this repo is the public base layer; a separate
  private overlay sits downstream of it.
- Same repo, long-lived `v2` branch, one launch PR; `main` + MCP server stay
  untouched until cutover.
- One Substack publication, two bylines (Brian Madden / brianmadden.ai) -- the human and
  the AI brain, sections for Daily Brief · Factory Notes · The Book · Q&A. Pipeline pushes
  drafts; human publishes.
- Email: Google Workspace 1 seat; bmad@ + ask@ + secret intake alias; two
  separate lanes; ask lane read-only with approval queue.
- Compute: GitHub Actions + personal Anthropic API key (+ OpenRouter for
  open-weight experiments).
- Launch target: first week of September (re-entry week). Build cadence:
  ~1 hr/day during August.
- Naming decision: public AI byline/account is 'brianmadden.ai' (handle brianmaddenai), primary email brain@, human byline unchanged.

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
   `brain@brianmadden.ai` directly from his personal address — sources to follow,
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
     at the SMTP envelope level (anyone can put his address there),
     but Gmail's receiving MTA independently evaluates SPF/DKIM/DMARC
     for every message and stamps the verdict into the message's own
     `Authentication-Results` header — real, inspectable via the
     Gmail API (`payload.headers`), not something the sender controls.
     A message only counts as "really from Brian's personal address" if that
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

12. ~~Port the private brain's deeper monthly-maintenance skill~~ — **done
    2026-10-04.** Ported as `/system-audit` (with `scripts/audit.py` and a
    monthly GitHub Action) and `/connect-the-dots`, rewritten for the v2
    tiers. `/review-thinking`'s full/monthly mode stays as the lighter
    on-demand pass; whether to retire it into `/weekly-update` is an open
    question from the first `/system-audit` run.

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

16. ~~**Substack feeds failing with `403 Forbidden` on every automated
    run**~~ — **closed 2026-09-28.** 39 of 85 registered sources (nearly all
    `*.substack.com` feeds) failed on every run since launch, unnoticed until
    Brian questioned an email-heavy briefing. Cause: Cloudflare bot
    protection (which fronts Substack) blocks datacenter IP ranges, GitHub
    Actions runners included, regardless of headers. Fix (2026-09-25): the
    daily pipeline moved to a self-hosted runner on a residential
    connection, where the same feeds returned 13/13 `200`. Eight dead
    Substack sources were pruned the same day; a 09-28 live check of all 37
    registered Substack feeds found nothing else to prune (two slow ones,
    `metr` and `asimovs-addendum`, left in place). Remaining known flake:
    `nate-b-jones`'s YouTube feed fails intermittently, left as-is because
    his Substack covers the same ground.

17. **Belief-currency inside canon: "we treat all my writing as canon, but
    my writing evolves" (raised by Brian 2026-09-04, flagged for later, not
    designed).** Brian's own framing, reacting to the Weekly Wrap Up prep
    doc: the knowledge factory model has inputs, a middle tier of canonical
    knowledge blocks, and outputs — and he wants the same shape applied to
    *himself*, internally. "Right now there's a lot of stuff mixed together
    and we sort of treat all my writing as canon, but my writing evolves
    over time, and certainly some of the things I wrote a year ago were
    things I don't really believe anymore." He also named a second, smaller
    gap in the same breath: "a whole bunch of random little things that
    aren't ideas necessarily, but just little things I believe" — currently
    homeless, or dumped undifferentiated into the Scratchpad.

    Findings from this session, so whoever picks it up doesn't re-derive
    them:

    - The tier-1/2/3 split (MAINTAINER.md) is about *provenance*, not
      *currency*. It says where content came from and whether a human
      checked it. It says nothing about whether Brian still believes it.
      That's the actual gap — not a missing tier, a missing axis.
    - **The staleness triage never looks at the oldest, highest-authority
      material.** `skills/triage/` reads `me/developing-thinking.md`'s
      "What's connecting"/"Scratchpad" plus active `frameworks/` as its
      *subjects*, and reads `me/published-thinking.md` only as the
      *reference* it checks them against. So the file that carries
      `authority_level: 1`, is synthesized from posts going back to June
      2020, and is presented to consuming AIs as Brian's standing position
      is the one file nothing ever triages. That is precisely the material
      Brian says he no longer fully believes.
    - `posts/` correctly isn't triaged — a post from 2024 says what it
      says, and CLAUDE.md's freshness section already tells consumers to
      date it rather than caveat it. The problem isn't the historical
      record, it's `published-thinking.md`, which reads as *current
      position* while being *derived from the archive*. Those two things
      have been conflated since v1.
    - `frameworks/` got a real currency mechanism on 2026-08-14
      (`status: archived`, plus `brief.py` skipping archived files).
      `published-thinking.md` has no per-argument equivalent — it's one
      ~10K-word file, so there's nothing to flip a status on. Any fix
      probably has to make its individual arguments addressable first.
    - The "little things I believe" gap is real but smaller, and partly
      already solved by accident: the Scratchpad is exactly that pile. What
      it lacks is any distinction between "unfinished argument," "durable
      small belief," and "note I'll never use again."

    Not designed, deliberately. Brian's instruction was to flag it, not to
    solve it today. Worth doing as its own session, the way canon
    governance (#8) was — and it's plausibly the same session as #12 (the
    ported monthly-maintenance skill), since a deeper periodic pass is
    where a published-thinking triage would actually run.

## Day plan (checklist — details in the plan doc §8)

- [x] D1 — Workspace + aliases + MX · lock naming
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

*Entries from 2026-08-19 through 2026-09-14 were trimmed on 2026-10-04
(this file was ~3,900 lines, 79% of it session log). Same deal as the
August trim: nothing is lost, `git log -p -- BUILD.md` or
`git show <commit>:BUILD.md` has it all, and the decisions from that era
live in Decisions made / Open decisions above. In one paragraph: launch day
08-19 (v2 merged to `main`, pipeline live); 08-20 domain cutover and
`mcp.brianmadden.ai`; 08-21 Workers KV cap fixed; 08-24 first Weekly Wrap
Up built and run; 08-25 to 08-28 source-checking, prose-quality and Daily
Brief editorial fixes, X sourcing wired in; 08-31 to 09-04 X auth failures
chased through several causes until it recovered, duplicate news items
fixed, podcast production moved into this repo (Episode 5); 09-10 X
timeline sourcing fixed and `brain@` skip-labels audited; 09-13 Wrap Up for
Sep 5-11; 09-14 new blog post covered.*

### 2026-09-25 — `/maintain` + home box: pipeline moved to a self-hosted runner; X root cause found

Sync was clean: 3 behind (automated 09-22/23/24 runs), fast-forwarded,
nothing ahead, tree clean. Brian set up an always-on home machine ("the
box" below), the thing the 2026-09-10 entry parked the "run it locally"
decision on. The pipeline itself doesn't need Claude Code (plain Python on
the API key).

**Decision (the one parked 2026-09-10): a self-hosted runner, not a local
cron script.** Keeps `daily-pipeline.yml` the single definition, logs stay
in Actions, secrets stay in GitHub Secrets (MAINTAINER.md rule). The
workflow runs on the self-hosted runner with a persistent virtualenv in
place of `setup-python`, and `ffmpeg` is installed on the box for podcast
transcription. Added `runner-smoke-test.yml`: manual-only dry run of X + one
Substack feed, commits nothing. Needed because a full `workflow_dispatch`
at that hour would have re-generated and re-emailed the 09-24 brief (UTC
date).

**Substack block: fixed.** 13/13 remaining RSS-polled Substack feeds
`403` from Actions (09-24 run), 13/13 `200` from the box; smoke test ran
a real extraction through the runner. See the note under open decision
#16.

**X: the IP-block theory is wrong.** The smoke test still got `401
unauthorized_client` from the residential network. History: every
scheduled run since at least 09-08 failed identically, while local runs
using `.env` succeeded (09-10's local run is the last write to the
`X_REFRESH_TOKEN` secret). A dry run on the box using `.env` pulled 48
timeline entries and wrote the rotated refresh token back to Secrets.
The difference is the app credentials: the `X_CLIENT_ID` /
`X_CLIENT_SECRET` secrets (last set 2026-08-26) don't match `.env`.
**Not yet fixed:** replacing those two secrets was blocked by the
session's permission check, so it's left for Brian to run himself (the
command is in the session). Until he does, X will keep failing in the
scheduled run. Also: the Mac's `.env` `X_REFRESH_TOKEN` is now stale
(the box rotated it). Don't run X from the Mac; the box and Secrets are
the live copies.

**Update, same session: X fixed.** Brian replaced the `X_CLIENT_ID` /
`X_CLIENT_SECRET` secrets from a local `.env` (22:48 UTC). The re-run
smoke test on the runner pulled 47 timeline entries and wrote 7 notes
(dry run). The next scheduled run is X's first working one since at least
09-08. **Also pruned 8 dead Substack sources** from `sources.yaml`
(122 → 114), on Brian's call; he's unsubscribing on Substack himself.
5 had no post in 2+ months (demis-hassabis, fei-fei-li, kevin-roose,
cory-doctorow, the-ai-report) and 3 feeds were empty
(emerging-physical-ai, tech-empires, lex-fridman-2). Kevin Roose is still
covered through Hard Fork. Doctorow's real output is pluralistic.net, if
he's wanted back.

### 2026-09-25 (continued) — first home-runner run verified; brief + subtitle moved to Opus 5.5

**First scheduled run on the self-hosted runner: clean.** 22 min (up from ~9, more to
process), every step green. Sources 79 ok / 45 skipped / **1 error**
(down from 16; the one left is `nate-b-jones`'s YouTube 404, the old
known dead feed). X worked on a scheduled run for the first time since at
least 09-08: 38 entries, 5 notes, rotated token written back to Secrets at
06:30 UTC. New sources already contributed (redwood-research, khe-hy,
future-focused, discover-ai). **Open:** the run's Substack auto-discovery
added `ground-level-ai` and `opinion-ai-2` as RSS rows, but both already
arrive by email (`sharon-goldman`, `opinion-ai`), so their posts may be
double-ingested. I suggested removing the two new RSS rows; waiting on
Brian's answer.

**Model change (Brian's call): `brief.py` and `publish.py` now default to
`claude-opus-5-5`.** Same-batch dry run on the day's 33 notes against the
Sonnet 5 brief that was emailed: 1,795 vs. 1,046 words, 25 vs. 16 links,
0 italics-for-emphasis and 0 bolded slugs in prose for both (so the Aug 26
Opus 5 tics didn't come back), and a different lead story. Brian read both
and picked Opus 5.5. `publish.py` has only written the subtitle since
08-14 (the body passes through), so the Fable 5 subtitle call moves to
the same model. Opus 5.5's sample subtitle was 176 chars (limit 200).
`skills/brief/README.md` fixed too: it still said Opus 5 for the brief,
which had been wrong since 08-26. Ingest stays on Sonnet 5 (high volume).
Triage (`claude-opus-5`) not changed yet.

**Cross-route dedupe (same session).** Found while answering Brian's
question about email vs. RSS: 61 of September's 495 notes (~12%) were
second copies of posts that arrived both by RSS and as brain@ email. Exact
link matching missed every custom-domain publication, because RSS links
the custom domain and the email path rebuilds the link on
`<pub>.substack.com`. Worst: Hard Reset 10, Exponential View 8,
Interconnects 6. `ingest.py` now dedupes on key sets (`dedupe_keys()`): a
near-exact URL key (query and fragment kept; YouTube and no-priors need
them) plus, for `/p/<slug>` links, a slug + normalized-title key.
Duplicate emails are now labeled `AI/Skipped` instead of sitting unlabeled
and being re-fetched every run. Replayed over September: catches 58 of
61. The 3 misses are 80,000 Hours (podcast site and Substack use
different slugs) and one email with no link; I left those alone rather
than match on title alone. No new false positives (the 6 other replay
hits are the Levie LinkedIn notes that share a profile URL, and the old
check flags the same 6). Brian is turning off Substack email delivery to
brain@ for publications that have RSS, so RSS becomes the single route
for those. That also makes the `ground-level-ai` / `opinion-ai-2` RSS
rows the right ones to keep. **Open side issue:** some notes credited to
`david-shapiro` share titles with Last Week in AI and Prof G, which looks
like email attribution going wrong, not routing. Not investigated.

**Four small open items closed (same session).** (1) **The "David
Shapiro" attribution bug was bigger than it looked:** every one of the 27
`ingest_method: email` rows ran the same whole-inbox read, capped at 20,
so overflow past brain-inbox's 20 got filed under the next email row in
file order. 130 notes were misattributed (40 under david-shapiro).
Sender fields were always right; only `source`/`source_id` were wrong.
Fixed: only `brain-inbox` reads the inbox now (`BRAIN_INBOX_SOURCE_ID`),
the cap is 100, and the 130 notes are refiled under brain-inbox
(frontmatter only; filenames unchanged because published briefs link to
them). **Found alongside it:** `flip_source_to_email()` had set 26 rows
to email-only with `feed_url: null`, so once Brian turned off Substack
email delivery they would have stopped arriving entirely. Removed the
flip. All 26 feeds were verified from the box (all 200) and 25 went back
to RSS. Emerging AI has renamed itself Opinion AI (its feed 301s to
opinionai.substack.com, already `opinion-ai-2`), so it's documentation
with a `renamed_to` note. (2) **nate-b-jones isn't dead, it's flaky:**
same channel ID, 404/500 on 17 of 24 runs since 08-25 on both runner
types, 200 when retried by hand. YouTube feeds now get 4 attempts with
backoff, alternating with the uploads playlist (UU…). (3) **Doctorow is
back** as `pluralistic` (pluralistic.net/feed/). (4) **Stale X token:**
the `X_REFRESH_TOKEN` line is removed from local `.env` files. Local runs now skip X cleanly, and `.env.example`
says why. **Left alone:** uncommitted `outputs/weekly-updates/` and
`outputs/canon-triage/` changes that appeared at 13:55, from what looks
like a concurrent `/weekly-update` session, not this one.

### 2026-09-25 (Weekly Wrap Up session) — `/maintain` + `/weekly-update`, window Sep 14–25

Sync clean (0/0). Ran concurrently with the attribution-fix session above;
the uncommitted `outputs/weekly-updates/` and `outputs/canon-triage/`
changes it noticed were this session's `gather.py` run. `gather.py`
bumps `.last_run.json` itself at gather time, so step 11 of the skill is
already done by step 1. Worth knowing if a ceremony is ever abandoned
halfway: the clock has already moved.

**Promotion queue (7 → 0).** No new entries. Folded in, as dated
September 25 additions:
- compute-physical and hyperscaler-lifecycle-terms (Kimi K3 / Harvey)
  → the August 28 compute-availability entry;
- pacing-as-antitrust-cover → the September 13 slowdown entry;
- agent-oversight-lacks-enforcement and agentic-commerce → the August 24
  human-in-the-loop entry.

Brian's reframe on agentic commerce: the enterprise worry isn't bots
spending, it's bots running amok. Rejected: hiring-freeze-vs-net-jobs and
agent-swarm Navier-Stokes (not his beat).

**Staleness queue (5).**
- Compute and "now execute" were flagged as post candidates, but both
  are already Next up in `post-ideas.md`, so no change.
- Trimmed "now execute" to its unpublished half (the Sep 14 post
  covered the on-ramp).
- Cut token economics down to the consumer/enterprise pricing gap.
- Cut the shadow-AI bridge Scratchpad item (published).
- **Rewrote `frameworks/bitter-lesson.md`** around the sequencing claim.

**Right now:** rewritten around "governance and integration into the
enterprise":
- WSJ CIO conference: everyone asks, nobody has answers.
- CIOs "getting it" from each other; the question is starter projects →
  enterprise.
- Knowledge factory, kept.

**Post:** `outputs/weekly-updates/2026/09/2026-09-25.md`, rendered. Brian
asked for curation over completeness: 5 governance/integration stories,
not 10. No lines about pipeline work (his call).

**Follow-ups:**
- Possible post on the WSJ questions ("how would you even know AI is
  helping; starter projects → enterprise"). Not added to `post-ideas.md`.
- The post's two new hooks (Fable lost deals on data retention, not
  capability; the harness beats the model) aren't in `post-ideas.md`
  either.

**Process questions Brian raised:**
- Should the ceremony run on a branch/fork? Recommended no: nothing
  reaches origin until the final push anyway, and a branch only moves
  the `promotion-candidates.md` conflict to merge time. Use a worktree
  only if a ceremony will be left half-done for days.
- Is there ingest retention? There was none; built this session (below).

**Ingest retention (same session): `scripts/prune_ingest.py` built, not
yet run or wired in.**
- Deletes dated notes under `ingest/YYYY/MM/` whose `date_captured` (or
  filename date) is older than `--days` (default 30). It never touches
  `brain-flags/`, `README.md` or the state files.
- Pruned notes stay in git history, and the brief disclosure links point
  at commits, so they keep working.
- Dedupe is safe because ingest only looks at entries newer than its last
  run. The exception is a manual `--since-days` backfill longer than the
  retention window.
- Dry run on 2026-09-25: would delete 321 of 884 notes (all captured
  before 08-26).
- The first real run was blocked by the session's permission check
  (irreversible delete), so this is left for Brian:
  - Option 1: run `python3 scripts/prune_ingest.py` himself and commit.
  - Option 2: approve adding it as a step before "Commit and push" in
    `daily-pipeline.yml`. `git add -A -- ingest/` already picks up the
    deletions.
- Once it's live, update `ingest.py`'s `handle_brain_flag` docstring,
  which still calls dated notes "a permanent historical log."

**Update, same session: wired in.** Brian approved a daily step:
"Prune ingest notes older than 30 days" runs after publish and before
"Commit and push" in `daily-pipeline.yml` (`continue-on-error: true`).
Monday 2026-09-28's run will be the first real prune, a bigger batch than
usual (~330+ notes). After that it's a day's worth each run. Checked
first: nothing links to ingest notes on `main`. The pipeline's fallback
disclosure link points at the technical brief, and briefs cite ingest
paths only as plain frontmatter text. `ingest.py`'s `handle_brain_flag`
docstring updated to match.

**Post ideas added (same session, Brian's call).** Three new Warm entries
in `me/post-ideas.md`: the WSJ CIO questions, the best model losing deals
over data retention rather than capability, and the harness beating the
model. The WSJ entry notes that it overlaps the productivity-measurement
and execute-now entries and may end up as the opening of one of them.
~~**Pre-existing glitch, not fixed:** the unmonitorability entry under Warm
has no `###` heading, so it reads as part of the slowdown entry above it.~~
— fixed a025d5d, three commits later the same week.

### 2026-09-28 — `/maintain` + open decision #16 follow-up (dormant Substack check, nate-b-jones diagnosis, 12 vendor sources added)

Sync clean (0/0). Brian asked to revisit #16's dormant-Substack angle now
that the home runner is live, plus three side questions: is nate-b-jones's
YouTube feed ever going to work, are podcast transcripts real, and can we
add vendor blogs (MSFT/AWS/others) now that non-Substack polling is
reliable.

**Dormant Substack check: nothing to prune.** Live-fetched all 37
registered Substack feeds directly (not from cached run data) and read
each one's actual latest-post date. None are dead — the real dead ones
were already pruned 2026-09-25 (8 sources, see that entry). Two are
notably slow (`metr` 45 days, `asimovs-addendum` 38 days) but neither
crosses even the old 60-day bar. Brian's call: leave both. #16 itself
looks closed now — the 2026-09-25 runner move fixed the block, and
today's check found no fresh dormancy to act on.

**nate-b-jones YouTube: diagnosed, not fixed, on purpose.** Pulled real
history from `ingest/.last_run_sources.json` across 26 tracked runs going
back to 08-25: 7 successes (~27%), spread across both the old
single-attempt code and the new 09-25 retry-with-backoff code — it does
work sometimes, it's not dead. The 4-attempt retry logic has only
actually executed once for real (09-28, since it was built mid-day
09-25 after that morning's run already happened) and it still failed all
4 attempts within ~21 seconds. Tested live the same session: 10/10
requests succeeded instantly from a residential connection hours later —
so the outage is a narrow time-window thing (most likely early-UTC
YouTube edge behavior), not a constant block, and 21 seconds of backoff
doesn't span it. Also surfaced: `nate-s-substack` (his newsletter) is
already tracked separately and posts daily, so his written thinking isn't
actually being missed when the video feed fails, only the video-specific
content. Brian's call: leave as-is, no code change — the redundancy makes
this low-stakes.

**Podcast transcripts: confirmed real, not just documented.** 11 podcast
sources, 10 on `transcribe` (real audio via `gpt-4o-transcribe`), 1
(`80000-hours-podcast`) on `published` (real `<podcast:transcript>` tag).
Spot-checked today's Moonshots ingest note against what show notes alone
would produce — panel-discussion-level specificity and a direct quote,
consistent with a real transcript, not just an episode description.

**12 vendor/company blog sources added, `sources.yaml`
(17cdfaa).** New `type: company` (documented in the header alongside the
existing `type: x`, which had never been added to that comment). Every
`feed_url` was live-fetched and verified the same day — real 200s, real
recent entries, not guessed from a URL pattern. Azure Blog, Microsoft 365
Copilot Blog, Microsoft Research Blog, Microsoft AI news
(news.microsoft.com), AWS News Blog, AWS Machine Learning Blog, Google
Cloud Blog, Google DeepMind Blog, OpenAI News, Salesforce News, Hugging
Face Blog, and Anthropic News. Each carries a `pov` steering extraction
toward substance over marketing — validated for real with a `--dry-run`
on `azure-blog`, which correctly flagged a customer stat as
"vendor-sourced claim, not independently verified" rather than repeating
it uncritically.

**Anthropic is the one real caveat.** No official RSS feed exists —
confirmed by checking `anthropic.com/news` for a feed link (none) and
researching known community alternatives. Routed through a public
RSSHub instance (`rsshub.bestblogs.dev/anthropic/news`) instead — not
Anthropic's own infrastructure, so it can go stale or disappear without
notice. Verified live with a real `--dry-run` (pulled a genuine, current
Anthropic post, correctly attributed as coming through the mirror, not
misrepresented as official). If it breaks, the existing "Sources checked
today" brief section will surface it, same mechanism as every other
source; fallback is Brian pasting posts in by hand, same shape as other
no-feed sources (e.g. `aaron-levie-linkedin`).

**Searched for and did not find a working feed (official or
community-maintained-and-live) for:** xAI, Mistral, Cohere, Perplexity,
IBM, Meta AI. Flagged rather than forced in — revisit if any of these
ship an official feed later, or if a specific community mirror is found
to be reliably live.

### 2026-10-04 — `/maintain`: monthly audit, skills ported, stats dashboard, search fixes, BUILD.md trim

- **Ported from an older private brain, rewritten for the v2 tiers:**
  `scripts/audit.py` + `monthly-audit.yml` (1st of the month, hosted runner,
  commits `outputs/audits/` only when metrics change), `/system-audit`,
  `/connect-the-dots`, `/brain-analytics`, and `.claude/lessons.md` (read by
  `/maintain` step 2). Skills specific to the private brain were deliberately
  not ported. First audit baseline fixed: a dead link in
  `me/published-thinking.md`, the TechRadar post missing from `_index.json`,
  `me/books.md` marked stable by decision; `me/style-guide.md`,
  `pages/about.md`, `podcast/bible.md` are intentionally unindexed.
- **KV sync** now excludes `.claude/` and `outputs/audits/`; the stale keys
  were deleted by hand. The GitHub repo is public, so this keeps the MCP
  surface clean but does not make those files private.
- **Stats dashboard (server repo):** `bmad.com/mcp-stats` now redirects to
  `mcp.brianmadden.ai/stats`, behind a password (fails closed, throttled
  login). Rebuilt with 7/30/90-day ranges, deltas, content gaps, most-read
  files, a weekday x hour heatmap, and click-to-expand search rows. Recording
  now also stores zero-result searches, files read and hour of day (the
  result count had been passed to `log()` and dropped). A first-login bug
  (the form posts `Origin: null` under `no-referrer`) was fixed same day.
  `/brain-analytics` was rewritten to use the new JSON endpoint: the
  Analytics Engine dataset it first queried had been dead since logging moved
  to KV. Known limit: KV counters can lose an update under concurrent calls.
- **`semantic_search` returned every hit twice** (the index holds duplicate
  vectors per chunk), so 8 requested results were 4 distinct passages. Fixed
  at query time (over-fetch 20, dedupe, trim); orphan vectors likely remain.
- **Red-team of the public MCP** (first `/system-audit` run): no finding that
  reads as leaked strategy.
- **BUILD.md trimmed** (~3,900 lines to a few hundred): kickoff prompts and
  session entries 08-19 through 09-14 removed, #12 and #16 collapsed. A
  sensitivity pass found no Citrix-proprietary content and no secret values,
  but did find private-network and runner details, a personal financial aside, a
  personal email address, named colleagues, and details of the private brain.
  All removed or generalized in the kept text. **The old text is still in
  public git history**; scrubbing it would mean rewriting history of a public
  repo, which was left as Brian's call.


### 2026-10-04 (later) — Citrix blog platform migration: links fixed

Citrix moved its blog platform (Adobe Edge Delivery). New scheme: posts at
`/blogs/YYYY-MM/slug`, author page at `/blogs/authors/brian-madden`; the old
`?s=bmadden&type=author` search link and the author RSS feed are gone, and some
old `/YYYY/MM/DD/slug/` URLs 404 instead of redirecting. Matched all 38 posts by
title against Citrix's live `/query-index.json` and fetched each new URL before
rewriting. Fixed in this repo (361 links, 66 files), `brianmadden-ai-server`,
and the plugin README; `audit.py` now flags any old-format link. Left alone:
`outputs/` and `ingest/` (historical), the dormant `bmad.com` mkdocs repo.
Old-to-new lookup: `outputs/link-migration/2026-10-04-citrix-url-map.csv`.
Still to fix by hand (Brian): LinkedIn, the Substack About page (two links),
40 of 49 published Substack issues, and Apple Podcasts show notes for Hotsheet
episodes 1-5. No replacement exists for Citrix's author RSS feed.

**Public-safety gates added (same day).** A sensitivity review of this file found
personal and operational detail that shouldn't live in a public repo (see the trim
note above). Layers now in place: a loud banner at the top of this file and a
widened rule 1 in MAINTAINER.md; `scripts/check_public_safe.py` (pattern lint over
added lines) run by a `.githooks/pre-commit` hook (enable per clone with
`git config core.hooksPath .githooks`), by `check-docs.yml` in CI, and by the monthly
audit as a critical check; and `.claude/hooks/remind-public-repo.sh`, which injects a
reminder into a Claude session whenever it writes to a maintainer journal. The lint
catches patterns, not judgment, and a line can be waived with an inline `public-ok`
marker plus a reason.


### 2026-10-05 — `/maintain`: Node 20 deprecation warning in daily pipeline

The daily run's annotation said `actions/checkout@v4` targets Node 20 and was
being forced onto Node 24. It was the only third-party action in use, across all
five workflows; bumped to `actions/checkout@v5` (Node 24 native). No other
actions to update. Verify on the next weekday run that the annotation is gone.
