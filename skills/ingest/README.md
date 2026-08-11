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

# whole registry, last 7 days, up to 5 items/source (defaults)
python3 skills/ingest/ingest.py

# one source, for testing/tuning
python3 skills/ingest/ingest.py --source ethan-mollick --dry-run

# wider window, fewer per source
python3 skills/ingest/ingest.py --since-days 14 --max-per-source 2

# one-off run against a different provider/model (see "Providers" below)
python3 skills/ingest/ingest.py --provider openrouter --llm-model deepseek/deepseek-chat-v3 --dry-run
```

`--dry-run` still calls the API (that's the point — it's for reading real
extraction output while tuning `prompt.md`) but prints notes to stdout
instead of writing them to disk. Without `ANTHROPIC_API_KEY` set, the script
still fetches and dedupes every feed and reports what it *would* extract —
useful for checking the plumbing without spending tokens.

## How it works

1. Load `sources/sources.yaml`. Skip any source with no `feed_url` (email-only
   sources like ExecAI Insider Weekly — see `fetch_entries_email()` below).
2. Fetch each feed (`requests` + `feedparser`), filter to entries published
   within `--since-days`, cap at `--max-per-source`.
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

## Known limitations (v1)

- **Podcasts and YouTube get whatever text their RSS show-notes provide** —
  no audio transcription. A thin show-notes entry produces a thin note.
  Real transcript-based ingestion is future work, not this skill.
- **Email-only sources aren't ingested yet.** `fetch_entries_email()` in
  `ingest.py` is a stub — it documents the intended Gmail-API path against
  `brain@brianmadden.ai` but raises `NotImplementedError`, since that
  mailbox doesn't exist yet (BUILD.md Day 1/8). Tracked as open decision #7a.
- **No automation yet.** This runs manually from a terminal. Cron/GitHub
  Actions wiring is Day 6.
