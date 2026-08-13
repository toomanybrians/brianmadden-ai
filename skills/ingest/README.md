# ingest skill

Pulls feeds listed in `sources/sources.yaml`, extracts insights with one
Anthropic API call per new item, and writes tier-1 notes to `ingest/`. See
[MAINTAINER.md](../../MAINTAINER.md) for the tier rules this exists inside —
this skill never writes anywhere but `ingest/`, and what it writes is never
full-text reprints.

## Running it

```bash
export ANTHROPIC_API_KEY=sk-...   # or put it in a repo-root .env, see .env.example
pip install -r requirements.txt

# whole registry, auto window (see "Polling window" below), up to 5 items/source
python3 skills/ingest/ingest.py

# one source, for testing/tuning — --source never advances the last-run clock
python3 skills/ingest/ingest.py --source ethan-mollick --dry-run

# explicit wider window, fewer per source (e.g. first-ever run, or catch-up)
python3 skills/ingest/ingest.py --since-days 30 --max-per-source 3

# one-off run against a different provider/model (see "Providers" below)
python3 skills/ingest/ingest.py --provider openrouter --llm-model deepseek/deepseek-chat-v3 --dry-run
```

`--dry-run` still calls the API (that's the point — it's for reading real
extraction output while tuning `prompt.md`) but prints notes to stdout
instead of writing them to disk, and doesn't advance the last-run clock
either. Without `ANTHROPIC_API_KEY` set, the script still fetches and
dedupes every feed and reports what it *would* extract — useful for
checking the plumbing without spending tokens.

## Polling window

`--since-days` defaults to **auto**: the time elapsed since the last
completed full-registry run, read from `ingest/.last_run.json` (see
[ingest/README.md](../../ingest/README.md)). A normal weekday-to-weekday run
naturally pulls ~1 day; a run after a weekend naturally pulls ~3; a run
after the pipeline sat broken for a week naturally pulls ~7 — no hardcoded
calendar logic, just "since it last actually ran." Only a full run with no
`--source` filter and without `--dry-run` updates that clock, so testing one
source or previewing output never causes the *next* real run to under-fetch
everything else. With no recorded prior run at all (first-ever run), it
falls back to 7 days. Pass `--since-days` explicitly any time you want a
specific window instead (bootstrapping the registry for the first time,
deliberately re-scanning further back, etc.).

## How it works

1. Load `sources/sources.yaml`. A source with `ingest_method: email` routes
   through `fetch_entries_email()` (polls `brain@brianmadden.ai` via the
   Gmail API); everything else needs a `feed_url` or is skipped.
2. Fetch each feed (`requests` + `feedparser`), filter to entries published
   within `--since-days`, cap at `--max-per-source`. Email sources use the
   same window via Gmail's `after:` search operator instead.
3. Dedupe against every `source_url` already present in `ingest/**/*.md`
   frontmatter — no separate state file, the notes on disk *are* the state.
4. For each new entry, one call through `skills/lib/llm.py` using
   `prompt.md` as the template. The prompt carries the source's `lens`/`pov`
   from `sources.yaml` (if set) as framing instruction, and can return the
   sentinel `NOT_RELEVANT` for off-topic items — those are skipped, no note
   written.
5. Write `ingest/YYYY/MM/YYYY-MM-DD-<source-id>-<slug>.md` with frontmatter
   (`title, source, source_id, source_url, author, date_published,
   date_captured, ingest_method, model`) per the shape in
   [ingest/README.md](../../ingest/README.md).

The raw entry content fetched from a feed is used only in memory to build
the extraction prompt — it is never written to `ingest/`. That's what keeps
notes from ever becoming full-text reprints (MAINTAINER.md rule 2).

## Tuning the prompt

Edit `prompt.md` directly — it's a plain-text template with `{{TOKENS}}`
filled in by `build_prompt()` in `ingest.py`. No code changes needed to
adjust tone, bullet count, relevance criteria, etc.

## Providers

`skills/lib/llm.py` is the one place any skill talks to an LLM — `ingest.py`
never imports an SDK directly. Provider + model come from `LLM_PROVIDER` /
`LLM_MODEL` env vars (default: `anthropic` / `claude-sonnet-5`), overridable
per run with `--provider` / `--llm-model`. Adding a new provider means one
function in `llm.py`, not a change to every skill that calls it. Today:
`anthropic` (native SDK, the daily pipeline) and `openrouter`
(OpenAI-compatible HTTP API via `requests`, for the open-weight comparison
runs in BUILD.md's post-launch backlog — not the default).

## Email inbox (brain@)

`fetch_entries_email()` polls the **whole** `brain@brianmadden.ai` inbox
via the Gmail API — every message not yet labeled ingested/skipped,
regardless of sender. There's exactly one `sources.yaml` entry for this,
`brain-inbox`. Needs `GMAIL_CLIENT_ID` / `GMAIL_CLIENT_SECRET` /
`GMAIL_REFRESH_TOKEN` in `.env` — see BUILD.md's brain@ Gmail walkthrough
for the Cloud Console steps, and `skills/lib/gmail_get_refresh_token.py`
for the one-time local OAuth step that produces the refresh token. Uses
`gmail.modify` scope: read + label/archive/trash, never send, never
permanent bypass-Trash deletion. A missing credential fails cleanly (same
`(entries, error)` shape as a broken feed) rather than crashing the run.

**Design, corrected 2026-08-13 (Brian's call, real design fix not just a
tweak):** an earlier version required a `sender` field per newsletter and
only looked at pre-approved senders, plus a separate "unrecognized sender"
check to surface anything else. Both removed. Subscribing a newsletter to
`brain@` already *is* the curation step — a second sender allowlist on top
of that was solving a problem that didn't exist. Relevance is now judged
exactly like every other source: the extraction prompt's `NOT_RELEVANT`
sentinel, validated live against a real inbox (correctly skipped a "Welcome
to your Google Cloud Free Trial" email while extracting real notes from
three different newsletters, each correctly attributed from its own From
header — no registry lookup involved). Each note's `author` field comes
straight from the message, so there's no need to identify or pre-register
what a newsletter even is before it can be ingested.

**Processed-mail bookkeeping — fully automatic, no Gmail-side setup.**
Every message this pipeline touches gets one of two Gmail labels applied
via `gmail_apply_label()` (best-effort — a labeling failure is logged, not
raised, since the note or the not-relevant decision it's marking is
already final by the time this runs):

- **`AI/Ingested`** — became a real tier-1 note. Also **archived**
  (`archive=True` removes the `INBOX` label — Gmail's own definition of
  archived) so handled mail clears out of the inbox on its own.
- **`AI/Skipped`** — seen, judged not relevant, no note written. Labeled
  but deliberately left **in the inbox** (not archived) — Brian can see
  what got judged not relevant and correct a bad call, and it also avoids
  a boring newsletter issue getting re-judged not-relevant (wasting a
  model call) every single run forever.

`fetch_entries_email()`'s query excludes both labels on top of the
existing frontmatter-based dedup, so a message never gets re-fetched once
handled either way. **Corrected 2026-08-13, Brian's call:** the earlier
design had Brian manually set up a Gmail filter (`AI/Inbox`, auto-archive
on arrival) — dropped. It was extra upkeep on his end for something the
pipeline can just do itself once it knows the outcome (ingested vs.
skipped) per message; a filter set on arrival can't know that yet anyway.

**`sources.yaml` auto-registration.** When a real note gets written from
an email whose sender isn't already documented in `sources.yaml`,
`auto_register_email_source()` appends a new entry for it — `id` (slugified
display name), `name`, `sender`, a `note` marking it auto-discovered and
not yet reviewed. Never for skipped/not-relevant mail, so the registry
doesn't fill up with junk. This is a **plain text append, never a full
YAML re-serialize** — re-dumping the file with PyYAML would silently
strip every hand-written comment in it. Per Brian's 2026-08-13 framing:
`sources.yaml` for email isn't a gate (the whole inbox is scanned
regardless of what's registered) — it's a reporting list of what's
actually feeding the brain, populated by what actually gets ingested
rather than maintained by hand ahead of time.

## Podcast transcripts

`enrich_with_transcript()` replaces show-notes content with a real
transcript, per a podcast source's `transcript_mode` in `sources.yaml`
(`docs/full-source-text-ingestion.md`):

- **`published`** — fetches `entry['podcast_transcript_url']` directly.
  `feedparser` surfaces the Podcasting 2.0 `<podcast:transcript>` RSS tag
  automatically as `podcast_transcript` (confirmed 2026-08-12, not
  assumed) — no scraping, no transcription cost. Currently only
  `80000-hours-podcast` has this.
- **`transcribe`** — downloads the audio enclosure to a real OS temp file
  (`tempfile`, outside the repo working tree — the same MAINTAINER.md
  rule 2 discipline as everything else, extended to audio: never
  persisted, deleted immediately after transcription whether it succeeds
  or fails) and transcribes it via `skills/lib/transcribe.py`
  (`OPENAI_API_KEY`, `gpt-4o-transcribe` by default). The other 10
  podcast sources use this.

Both fall back cleanly to the existing show-notes content on any failure
(bad URL, download error, missing credential) rather than crashing the
run over one episode.

## X (brianmaddenai home timeline)

`fetch_entries_x()` polls the reverse-chronological home timeline for the
one `x-timeline` source in `sources.yaml` — everyone the `brianmaddenai`
account follows, in one call, rather than per-person polling (who it
follows *is* the source list here). Needs `X_CLIENT_ID` / `X_CLIENT_SECRET`
/ `X_ACCESS_TOKEN` / `X_REFRESH_TOKEN` in `.env`. Access tokens are
refreshed automatically each run; if X rotates the refresh token (standard
OAuth 2.0 practice), the new one is written back into `.env` in place so
the next run doesn't fail with a stale one.

Two enrichments, both validated against real timeline data (2026-08-12):
retweets and quote-posts pull in the **full referenced post's text**, not
just the wrapper (`expansions=referenced_tweets.id` in the API call); and
posts that link elsewhere get **that page's content fetched too** (Brian's
ask), skipping links back to X itself since those are already covered by
the referenced-post expansion. Both are ephemeral input to the one
extraction call, never persisted raw, same as everything else.

## Known limitations (v1)

- **Podcast transcription adds real cost and latency per episode** — a
  60-90 minute episode is a meaningfully bigger, slower fetch than parsing
  show notes. `--max-per-source` is the only current throttle; watch
  actual cost/time once this runs for real at volume.
- **X's external-link fetch is best-effort, no paywall handling.** A
  linked article behind a paywall just yields empty/thin content, same as
  every other paywalled source this pipeline already deals with.
- **Email ingestion supports one sender per source, day-granularity
  windowing only** (Gmail search's `after:` operator, same coarseness as
  everywhere else this pipeline already does date filtering). Fine for a
  weekly newsletter; would need widening (an `OR` sender query) if a source
  ever needs multiple known addresses.
- **The `ask@` read-only Q&A lane (MAINTAINER.md rule 5, D8) isn't built.**
  It's expected to reuse the same Gmail credentials as `brain@` ingestion
  once it exists, but nothing here does that yet.
- **No automation yet.** This runs manually from a terminal. Cron/GitHub
  Actions wiring is Day 6.
- **Paywalled sources only get the free preview, even from the feed.**
  Most feeds (confirmed for Substack's `content:encoded` and several
  non-Substack blogs) carry genuine full-text, not a truncated snippet —
  `MAX_CONTENT_CHARS` exists as a generous safety cap (50000 chars), not a
  real limit in practice. But a paywalled publication's feed only ever
  contains its own free preview (confirmed on SemiAnalysis — the feed
  content itself ends mid-thought at "Read more"). No fix for this within
  RSS; the note will reflect only what the preview covers.
