---
title: "Full-text source ingestion — podcast transcripts and X — planning doc"
type: proposal, in progress
author: Brian + Claude
date: 2026-08-12
status: brainstorming, not decided
tier: canon (candidate — planning doc, not yet a settled architecture)
---

# Full-text source ingestion: podcast transcripts and X

Started 2026-08-12, prompted by Brian asking whether today's Artificial
Intelligence Show note was really just based on show notes (checked:
yes — the note is a breadth-first list of ~6 topics with no depth on any
one of them, the exact shape you'd expect from a show-notes-only
extraction, not a transcript). Two related but separate gaps, both
already flagged as known v1 limitations (`skills/ingest/README.md`)
without a real design — this is that design.

## The governing constraint, unchanged and non-negotiable

MAINTAINER.md rule 2 already covers this: **never store the full text of
third-party content.** Ingest notes capture source, author, link, date,
and insights in Brian's own words; quotes stay under 25 words, always
attributed. Everything below is an *extension* of the existing ingest
architecture to two new raw-content types (audio, X posts) — not a new
policy. The existing pipeline already has the right shape for this:
`fetch_entries()` pulls full content into memory, feeds it to one
extraction call, and only the model's neutral insight bullets get
written to disk. Raw content is never persisted. Transcripts and X post
text need to follow the exact same discipline — ephemeral input to the
extraction call, discarded immediately after, never git-tracked.

**One new wrinkle worth naming explicitly: audio files.** Transcribing a
podcast means downloading the MP3 at least temporarily. That file must
live in a true scratch location (Python `tempfile`, or equivalent —
outside the repo working tree entirely, not a repo-relative "scratch"
folder that could get swept into a `git add`) and get deleted immediately
after transcription. This is the same rule as everything else, just
applied to a new content shape.

## Workstream E — podcast (and YouTube) transcripts

**Two source shapes, need different handling:**

1. **Sources that already publish full transcripts** (a transcript page,
   or a `<podcast:transcript>` tag in the RSS feed per the Podcasting 2.0
   namespace — `feedparser` doesn't surface this automatically, needs
   explicit namespace handling). For these, ingestion is a straightforward
   extension of the existing `fetch_entries()` pattern: fetch the
   transcript URL/tag content instead of (or in addition to) the show
   notes, feed the full transcript into the same extraction call. **No new
   credentials needed** — this is buildable now, in this repo, same as
   everything else this session.
2. **Sources with audio only, no published transcript** (likely most of
   the 11 podcast sources in `sources.yaml`). Needs: download the audio
   enclosure (RSS `<enclosure>` already gives the URL, `feedparser`
   surfaces it), run it through a transcription service, extract from the
   result, discard the audio and the raw transcript text. **Needs a new
   credential** — a transcription API key — which isn't provisioned
   anywhere yet, same class of blocker as the Gmail ingestion path (open
   decision #7a) was until Workspace existed.

**Transcription service — not decided, Brian's call:**

- **OpenAI's Whisper API** — simplest, cheap, no local compute burden,
  matches the "just works" philosophy `ANTHROPIC_API_KEY` already has for
  the rest of the pipeline. Straightforward `requests` call, same shape as
  `skills/lib/llm.py`'s `openrouter` path (external API, no new SDK
  dependency needed beyond what's already there).
- **Local Whisper** (`faster-whisper` / `whisper.cpp`) — no per-minute
  cost, but real setup (a model download, real compute time per episode
  — a 60-minute episode takes real wall-clock time even on decent
  hardware), and ties the pipeline to whatever machine runs it rather
  than being portable to GitHub Actions later (Day 6 automation).
- **AssemblyAI / Deepgram** — dedicated transcription services, add
  speaker diarization and other features neither of the above give for
  free, but a third provider/credential to manage for a feature this
  pipeline doesn't currently need (nobody's asked for "who said what").

**Decided 2026-08-12: OpenAI Whisper API for now, built swappable from
day one.** Same pattern as `skills/lib/llm.py` — a new
`skills/lib/transcribe.py` with one `transcribe()` entry point, provider
chosen via `TRANSCRIBE_PROVIDER` env var / `--transcribe-provider` CLI
flag (mirroring `LLM_PROVIDER`), `openai` as the first and only real
provider for now. Call sites (`skills/ingest/ingest.py`) never import an
SDK directly, same discipline as the text-generation path. Not yet
built — waiting on Brian's OpenAI API key. Whether OpenRouter can serve
as a second provider later depends on it actually exposing a
Whisper-compatible transcription endpoint, which hasn't been checked —
note the abstraction doesn't require deciding that now, only that adding
a provider later is one function + one registry entry, not a rewrite of
call sites (exactly how `lib/llm.py already works for `openrouter`
alongside `anthropic`).

**Podcast-by-podcast transcript check, 2026-08-12 (real research, not
assumed):**

| Source | Transcript? | How |
|---|---|---|
| `80000-hours-podcast` | **Yes, confirmed** | RSS feed itself carries a `<podcast:transcript url="..." type="text/plain"/>` tag per episode — direct plain-text URL, easiest possible case, no parsing needed |
| `dwarkesh` | **Yes, confirmed** | Publishes transcripts on dwarkesh.com itself (not in the RSS feed — needs fetching the episode page, not just the feed) |
| `lex-fridman` | **Yes, confirmed** | Publishes transcripts on lexfridman.com itself, same shape as Dwarkesh — own site, not the RSS feed |
| `ezra-klein-show` | **Yes, confirmed** | NYT posts transcripts at nytimes.com/ezra-klein-podcast |
| `hard-fork` | **No first-party source found** | Only third-party transcript sites turned up, no NYT-hosted transcript page |
| `the-artificial-intelligence-show` | **No** | Confirmed no `<podcast:transcript>` tag in the feed — this is the source that prompted the whole check, and it's show-notes-only |
| `moonshots` | **No first-party source found** | Only third-party sites (podscripts.co, podscribe) turned up |
| `bg2` | **No first-party source found** | Only third-party sites (spoken.md, metacast.app) turned up |
| `on-with-kara-swisher` | **No first-party source found** | Only a third-party site (podscripts.co) turned up |
| `no-priors` | **No first-party source found** | Only third-party sites (metacast.app, podscribe) turned up |
| `hbr-ideacast` | **No first-party source found** | Only a third-party site (metacast.app) turned up |

Check complete, 2026-08-12: 4 of 11 sources (80000-hours-podcast,
dwarkesh, lex-fridman, ezra-klein-show) have real first-party transcripts
— buildable now, no new credentials, a good pilot batch (similar spirit
to Workstream C's podcast-episodes-first recommendation in the Substack
plan). The other 7 all fall into the "transcribe" bucket once that path
exists (audio → Whisper), not the "published" bucket. Third-party
transcript sites exist for most of the 7 (podscripts.co, spoken.md,
metacast.app, podscribe) but weren't evaluated as a source — using
someone else's transcription of the audio raises its own questions
(accuracy, their terms of service, another dependency) rather than being
a clean substitute for either a first-party transcript or running our
own transcription; not pursued in this pass.

**sources.yaml additions needed:** a `transcript_mode` field per podcast
source (`published` / `transcribe` / `none`), and for `published` sources,
however the transcript is actually reachable (a URL pattern, or a flag to
check the RSS feed's `<podcast:transcript>` tag) — the table above is a
real starting point, not a guess, but the 5 unchecked sources still need
the same pass before this field can be filled in completely.

**Cost/latency reality check:** transcribing adds real time and money per
episode that RSS-only ingest doesn't have today — a 60-90 minute episode
is a meaningfully bigger, slower, costlier fetch than parsing show notes.
Worth watching actual per-episode cost/time once real transcription runs
happen, not assuming it's negligible.

## Workstream F — X / Twitter

**Decided 2026-08-12: yes, pursue this. Brian is setting up a paid X
developer account and API key** (separate from the OpenAI key above),
under the `brianmaddenai` account — mirrors how that account already
follows Substack publications as the public source registry (open
decision #7 in `BUILD.md`); same pattern, second platform.

**The real cost picture (researched 2026-08-12, not assumed):** the free
tier closed and the flat $200/mo (Basic) and $5,000/mo (Pro) tiers closed
to new signups as of February 2026. Pay-per-use is now the default:
general reads are $0.005/post, but reads of *your own account's data* —
which the home timeline counts as — are priced separately and lower,
$0.001/resource, under what X calls "Owned Reads." Real friction either
way: a paid developer account from day one (no free trial), a payment
method on file.

**The key finding: one endpoint replaces per-person polling entirely.**
X API v2's `GET /2/users/:id/timelines/reverse_chronological` — the
"home timeline" — returns posts from the accounts the authenticated user
follows, exactly like opening the X app. Confirmed available under the
current pricing model, and priced at the cheaper Owned Reads rate. This
means: `brianmaddenai` follows the right people once (a curation task,
same shape as the Substack follow list), and ingest polls *one* endpoint
per run rather than one call per tracked person — no per-person
`fetch_entries_x_user()` loop needed, no separate list of handles to
maintain in `sources.yaml` beyond "these are the people the account
follows." Simpler than the per-user-polling design floated before this
was checked.

**Design, updated:** `fetch_entries_x()` in `skills/ingest/ingest.py`
polls the home timeline once per run (same `since_days`-style windowing
`fetch_entries()` already does for RSS, applied to the timeline's own
chronological order), normalized to the same entry shape everything else
uses. Not yet built — waiting on the X developer account and key. Who
`brianmaddenai` follows *is* the source list here, unlike every other
source type where `sources.yaml` is the registry — worth deciding whether
that's tracked in `sources.yaml` too (a `type: x` entry per person, for
`lens`/`pov` and consistency) or left implicit in the X follow list
itself. Not decided.

**Fallback (Brian's own suggestion): manual daily paste.** If the API
route doesn't happen or a specific person isn't worth automating for,
Brian pastes their recent posts in and this goes through the exact same
extraction pipeline as everything else — the pasted text is the ephemeral
input to one extraction call, never itself committed; only the resulting
insight note is. This is worth building as a small standalone entry point
(a `--paste` mode on `ingest.py`, or a tiny separate script) regardless of
whether the API path happens, since it's useful for any source that isn't
worth automating.

## What's actually blocked vs. buildable now

- **Buildable now, no new credentials:** published-transcript podcast
  ingestion for the 4 confirmed sources (80000-hours-podcast, dwarkesh,
  lex-fridman, ezra-klein-show); the manual-paste fallback for X. Both
  can happen in this repo, this session, whenever picked up.
- **Blocked on Brian provisioning a credential — in progress as of
  2026-08-12, not done yet:** audio transcription (OpenAI API key,
  decided) and the X home-timeline path (paid X developer account +
  key, decided). Neither needs a *different repo* the way the MCP/
  Cloudflare work does — unlike Workstreams A/B in
  `docs/substack-as-primary-home.md`, this doesn't strictly need a new
  conversation, just needs the credentials in hand first. Explicitly
  fine to pick up in a different thread once they're ready, per Brian's
  own preference — this doc is written so that thread doesn't need this
  conversation's context.

## X developer account setup — what Brian needs to do, 2026-08-12

Researched, not guessed (X's developer portal has changed shape several
times). Two things need to happen at `console.x.com`, logged in as the
`brianmaddenai` account:

1. **Sign up for developer access and add a payment method** (no free
   tier since Feb 2026 — see Workstream F above). Create a **Project**,
   then an **App** inside it.
2. **In the App's "User authentication settings," enable OAuth 2.0**,
   set app permissions to **Read** (no write/post access needed for
   this), app type **confidential client** (a script/server, not a
   public/mobile app), and set a callback/redirect URL (any placeholder
   works if there's no real web server yet — e.g. `http://localhost:8080/callback`).
   Under "Keys and tokens," this generates a **Client ID** and
   **Client Secret** — these can be grabbed today and dropped in `.env`
   (new vars, e.g. `X_CLIENT_ID` / `X_CLIENT_SECRET`, matching the
   existing `.env.example` convention).

**What's still open, and likely needs a short follow-up together rather
than being a solo portal task:** the home-timeline endpoint needs a
*user-context* access token — one actually authorized by the
`brianmaddenai` account, not just an app-level credential. Since
`brianmaddenai` is both the account being read *and* the account that
owns the app, X's portal may let the OAuth authorization happen
entirely within the same session (self-authorizing your own app) without
a real external redirect — but this isn't confirmed for the current
portal UI. If it does work that way, grab the resulting **Access Token**
and **Refresh Token** (request the `tweet.read`, `users.read`, and
`offline.access` scopes — that last one is what keeps the integration
from needing manual re-authorization every couple of hours) and those go
in `.env` too. If the portal instead requires a full external OAuth
redirect flow, that's better done together via a short script than
guessed at blind — flag it here rather than now.

## Open, not decided

- Whether OpenRouter (or another provider) is worth adding to
  `skills/lib/transcribe.py` later — not needed to start building with
  `openai` as the only provider.
- Whether X-followed people get their own `sources.yaml` entries (for
  `lens`/`pov` parity with every other source type) or stay implicit in
  the X follow list itself.
- Whether any of the 7 no-first-party-transcript podcast sources are
  worth transcribing via Whisper given the cost/latency reality, or
  better left as show-notes-only indefinitely — a per-source judgment
  call once the transcription path actually exists and its real
  cost/time per episode is known.
