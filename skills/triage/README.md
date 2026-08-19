# triage skill

Reads `me/developing-thinking.md`'s "What's connecting" and "Scratchpad"
sections, plus every active `frameworks/*.md` file, against the full
authority record (`me/published-thinking.md`), and writes a review queue to
`outputs/canon-triage/staleness-candidates.md`. See
[MAINTAINER.md](../../MAINTAINER.md) for the tier rules this exists inside.

This is the mirror image of [skills/brief](../brief)'s
`promotion-candidates.md`: that queue proposes *additions* to canon, this
one proposes *cuts, promotions, or a second look* at what's already there.
Built for BUILD.md open decision #8 (canon governance) — see the
2026-08-14 canon-governance session for why per-item dating on
`developing-thinking.md` doesn't work (most of its content arrived in a
handful of historical batch syncs, not one item at a time, so there's no
real date to backfill) and content cross-checks are the only honest
staleness signal left.

## Running it

```bash
export ANTHROPIC_API_KEY=sk-...   # or repo-root .env, see .env.example
pip install -r requirements.txt

python3 skills/triage/triage.py             # real run, writes the report
python3 skills/triage/triage.py --dry-run   # read output without writing (still calls the API)

# different provider/model for one run
python3 skills/triage/triage.py --provider openrouter --llm-model deepseek/deepseek-chat-v3 --dry-run
```

No polling window — unlike `ingest`/`brief`, this doesn't process what's
*new* since a last run. It re-reads the *entire current state* of both
sections and every active framework each time, because the question isn't
"what changed" but "what's still true of what's already there." Run it
whenever — after a run of ingest/brief activity, before a canon-review
session, or just periodically. Wiring it into a recurring cadence is Day
6's job (workflow automation), same as `ingest`/`brief`.

## How it works

1. Extract the raw text of `developing-thinking.md`'s "What's connecting"
   and "Scratchpad" sections. Deliberately not split into individual items
   in code — both sections mix `- ` bullets with bare bold-lead paragraphs,
   so a regex itemizer would be fragile. The model identifies items itself
   and quotes each one's own opening words in its output, the way a human
   skimming the file would.
2. Load every `frameworks/*.md` file whose frontmatter isn't
   `status: archived` (archived ones are already retired, no need to
   re-flag them) — full text, not just descriptions, since judging overlap
   with the published record needs the actual argument.
3. One call through `skills/lib/llm.py`, `prompt.md` as the template. The
   model reads all of it against `me/published-thinking.md` and reports
   only items that are actionable — `already-published` (substance is
   fully covered elsewhere, cite where), `promote-candidate` (mature enough
   to graduate into a real framework or published-thinking writeup), or
   `worth-revisiting` (dated, went nowhere, or the field's visibly moved
   past it). Anything still genuinely developing gets no mention at all —
   silence is the "keep" signal, same principle as `brief.py`'s promotion
   threshold only flagging what crossed it.
4. Plain code wraps the model's output with frontmatter and a fixed intro
   paragraph explaining what the file is (so that framing can't drift
   run to run) — `outputs/canon-triage/staleness-candidates.md`,
   **overwritten fresh every run**, not appended to. Unlike
   `promotion-candidates.md` there's no recurrence count to track across
   runs; this is a snapshot of "what does the record say about the current
   canon today," not a log of repeated sightings.

## What it doesn't do

**Never edits `me/developing-thinking.md` or `frameworks/*.md`.** A flagged
item only actually leaves the file, or a framework only actually gets
`status: archived`, if Brian does it himself — same non-negotiable as
`promotion-candidates.md`, `docs/frontmatter-schema.md`'s status rules, and
every other machine-surfaces-human-decides surface in this repo.

## Model

Defaults to `claude-opus-5`, same reasoning as `brief.py`'s Opus default —
judging whether an idea is genuinely redundant with published work (versus
just thematically related) is real judgment, and this runs occasionally,
not per-item, so the cost multiplier is small. Override with `--llm-model`
/ `LLM_MODEL`, or switch providers with `--provider` — see
[skills/lib/llm.py](../lib/llm.py).

## Known limitations (v1)

- **Conservative by prompt instruction, not by measurement.** `prompt.md`
  asks the model to flag only a short list and points at the 2026-08-14
  manual pass's hit rate (a handful out of ~90) as the target — nothing
  enforces that mechanically. Watch the first few real runs for
  over-flagging before trusting it unattended. First real run
  (2026-08-15) landed at 7 developing-thinking items + 1-2 frameworks
  out of ~90/10 candidates — in the right range.
- **Borderline calls vary run to run.** The `--dry-run` and the real run
  on 2026-08-15 agreed on all 7 developing-thinking flags but differed on
  one framework (`post-application-era.md` flagged as `worth-revisiting`
  on one run, not the other) — the same non-determinism any single LLM
  judgment call has. Not a bug; treat a flag near the margin as "worth a
  look," not gospel, and don't read a framework's absence on one run as a
  clean bill of health if a prior run flagged it.
- **`published-thinking.md` and active frameworks are the only authority
  corpus.** Doesn't read raw `posts/`, `talks/`, or `podcast/` text —
  per Brian's steer (2026-08-15), everything actually published is assumed
  to already be distilled into `published-thinking.md`, so that file (not
  the ~106K words of raw post text) is the cross-check target. If that
  assumption ever stops holding — a post's argument that never made it
  into published-thinking.md's summary — this tool won't catch the overlap.
- **"What I'm unsure about" (open questions) is out of scope.** Scoped
  deliberately to "What's connecting" and "Scratchpad," the two sections
  the original open-decision diagnosis identified as the ~90-item ungrouped
  pile. The open-questions list is small and already curated by Brian
  directly; revisit if it grows the same way.
- **No automation yet.** Runs manually from a terminal. Day 6 wires up
  cron for the whole pipeline, this included.
