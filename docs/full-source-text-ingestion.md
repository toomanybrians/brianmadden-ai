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

Recommendation, not a decision: start with the OpenAI Whisper API for the
same reason `ANTHROPIC_API_KEY` was the right first move for text — cheap,
simple, no infrastructure to stand up, easy to swap later behind its own
small abstraction (`skills/lib/transcribe.py`, mirroring how `lib/llm.py`
already keeps providers swappable) if it turns out to be wrong.

**sources.yaml additions needed:** a `transcript_mode` field per podcast
source (`published` / `transcribe` / `none`), and for `published` sources,
however the transcript is actually reachable (a URL pattern, or a flag to
check the RSS feed's `<podcast:transcript>` tag). Needs a source-by-source
pass across the 11 podcast entries to find out which are which — not
assumed, needs to actually be checked.

**Cost/latency reality check:** transcribing adds real time and money per
episode that RSS-only ingest doesn't have today — a 60-90 minute episode
is a meaningfully bigger, slower, costlier fetch than parsing show notes.
Worth watching actual per-episode cost/time once real transcription runs
happen, not assuming it's negligible.

## Workstream F — X / Twitter

**The real cost picture (researched 2026-08-12, not assumed):** the free
tier closed and the flat $200/mo (Basic) and $5,000/mo (Pro) tiers closed
to new signups as of February 2026. Pay-per-use is now the default for a
new developer account: $0.005 per post read, capped at 2M reads/month.
For light use — a handful of specific people, checked once a day — this
is probably genuinely cheap (rough estimate: ~$10-15/month at realistic
volume), not the $200-5,000/mo figures that get quoted around the web,
since those are the now-closed legacy tiers. Still real friction though:
a paid developer account from day one (no free trial), a payment method
on file, and real integration work (per-person timeline polling,
pagination, since-last-checked tracking similar to `ingest.py`'s existing
dedup).

**Design, if pursued:** treat each tracked X account the same way
`sources.yaml` treats a podcast or blog — `type: x`, a handle, and the
same `lens`/`pov` fields already available to every source. Polling is a
new `fetch_entries_x()` function alongside the existing `fetch_entries()`
and the still-stubbed `fetch_entries_email()`, normalized to the same
entry shape so the extraction/write pipeline downstream doesn't change.

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
  ingestion (Workstream E, path 1); the manual-paste fallback (Workstream
  F). Both can happen in this repo, this session, whenever picked up.
- **Blocked on Brian provisioning a credential:** audio transcription
  (needs a transcription service API key — his call which service first)
  and the X API path (needs a paid X developer account set up). Neither
  needs a *different repo* the way the MCP/Cloudflare work does — unlike
  Workstreams A/B in `docs/substack-as-primary-home.md`, this doesn't
  strictly need a new conversation, just needs Brian to have the
  credential in hand first. Can pick back up in whatever session is
  convenient once that's done.

## Open, not decided

- Transcription service choice (Whisper API vs. local vs. a dedicated
  service).
- Which of the 11 podcast sources actually publish transcripts already —
  needs a real per-source check, not assumed either way.
- Which specific people Brian wants tracked on X, and whether that's
  worth the API integration per-person vs. just using the manual-paste
  fallback for a small number of accounts.
