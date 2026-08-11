# brief skill

Reads the `ingest/` notes captured since the last briefing run *together*,
against full canon (`me/voice.md`, `me/published-thinking.md`,
`me/developing-thinking.md`, `frameworks/`), and writes a Daily Brief to
`outputs/briefings/`. See [MAINTAINER.md](../../MAINTAINER.md) for the tier
rules this exists inside.

This is the cross-note, whole-canon synthesis step that ingest-time
extraction deliberately doesn't do — see BUILD.md's D5 kickoff and the
2026-08-11 framework-citation detour for why that judgment call was pulled
out of `skills/ingest/` and moved here instead.

## Running it

```bash
export ANTHROPIC_API_KEY=sk-...   # or repo-root .env, see .env.example
pip install -r requirements.txt

# auto window (see "Polling window" below)
python3 skills/brief/brief.py

# read real output while tuning prompt.md, without writing anything
python3 skills/brief/brief.py --dry-run

# explicit window (e.g. re-running a gap manually)
python3 skills/brief/brief.py --since-days 3

# different provider/model for one run
python3 skills/brief/brief.py --provider openrouter --llm-model deepseek/deepseek-chat-v3 --dry-run
```

`--dry-run` still calls the API and still runs the thread-tracker logic
in-memory, but prints the brief to stdout instead of writing it, and
doesn't persist the tracker, the promotion-candidates queue, or the
last-run clock — same contract as `skills/ingest/`'s `--dry-run`.

## Polling window

`--since-days` defaults to **auto**, using `outputs/briefings/.last_run.json`
the same way `skills/ingest/` uses `ingest/.last_run.json` — the window is
"however long since the briefing skill last actually ran," so a normal
day-to-day cadence naturally covers ~1 day, a weekend gap naturally covers
~3, and so on. With no recorded prior run, it falls back to 1 day. Notes are
selected by `date_captured` (when ingest wrote them), not `date_published`
— the brief's job is to react to what's newly in `ingest/`, regardless of
how old the underlying article is. This is why the very first real run
(2026-08-11) correctly pulled in the full 96-note catch-up batch — they
were all captured today, even though they span a 30-day publish window.

## How it works

1. Select `ingest/**/*.md` notes with `date_captured` inside the window.
   If there are none, no brief is written (an empty day still advances the
   clock on a real run, so tomorrow's window doesn't grow unbounded).
2. Load full canon (`me/voice.md`, `me/published-thinking.md`,
   `me/developing-thinking.md`) plus a lightweight list of
   `frameworks/*.md` titles + descriptions (not full text — the model
   doesn't need the whole framework, just enough to cite one by name where
   it genuinely fits).
3. Load `outputs/briefings/.thread_tracker.json` — patterns flagged as
   "doesn't fit yet" on previous runs, being watched for recurrence.
4. One call through `skills/lib/llm.py`, `prompt.md` as the template. The
   model gets everything from steps 1-3 at once and returns two parts: the
   brief itself (Markdown), then a `---THREAD-SIGNALS---` delimiter and a
   JSON object naming which tracked threads recurred and which new
   patterns are worth watching.
5. Plain code (not the model) updates the tracker: increments recurrence
   counts, adds new watched threads, and — this is the promotion-ceremony
   feedback loop BUILD.md's D5 kickoff asked for — appends an entry to
   `outputs/briefings/promotion-candidates.md` for any thread that's
   recurred `PROMOTION_THRESHOLD` (3) times. That file is a human-review
   queue only. **Nothing is ever written into `me/developing-thinking.md`
   automatically** — a candidate becomes canon only if Brian deliberately
   edits it in himself, same as the private-overlay promotion ceremony in
   MAINTAINER.md.
6. Writes `outputs/briefings/YYYY/MM/YYYY-MM-DD.md` — frontmatter
   (`tier: 3`, `status: not-reviewed-by-human`, `model`, `sources`: every
   ingest note + canon file the brief drew on) plus the model's brief body
   plus a deterministically-rendered "Threads being tracked" section (not
   written by the model — plain code formatting the tracker's current
   state, so the transparency section can't drift from what's actually
   tracked).

## Byline and voice

The brief is written under the `brianmadden.ai` (AI) byline, not Brian's —
see the plan doc §6's two-byline convention. `prompt.md` instructs the
model to speak in first person as the synthesizing AI ("I read N items
today...") and refer to Brian in the third person, informed by
`me/voice.md`'s tone (direct, no corporate buzzwords, comfortable with
uncertainty) without impersonating him. This is a first-pass interpretation
— voice iteration is explicitly part of D5, so expect `prompt.md` to change
after Brian reacts to real output, the same way `skills/ingest/prompt.md`
was tuned after seeing real extractions.

## Model

Defaults to `claude-opus-5` (Brian's explicit call, 2026-08-11 — this is
the hardest judgment call in the pipeline so far, and it's one call a day,
not one per article like ingest, so the cost multiplier is smaller than it
looks). Override with `--llm-model` / `LLM_MODEL`, or switch providers
entirely with `--provider` — same mechanism as `skills/ingest/`, see
[skills/lib/llm.py](../lib/llm.py).

## Publishing a condensed version

`publish.py` reads an already-written dense brief and condenses it into a
Substack-ready draft — 2-4 items, ~400-700 words, written for a general
subscriber rather than an AI or an insider. It does not re-read the raw
ingest notes or canon; it only re-renders `brief.py`'s output, so there's
one place judgment happens, not two synthesis passes that could drift
apart. Every link it keeps is reused verbatim from the dense brief (never
invented). The model doesn't write its own headline-and-nothing-else
either — `publish-prompt.md`'s Title section pushes toward the
enterprise/future-of-work angle specifically (Brian's beat), not just
naming the underlying AI-news event.

```bash
python3 skills/brief/publish.py                    # today's brief
python3 skills/brief/publish.py --date 2026-08-11   # a specific date
python3 skills/brief/publish.py --dry-run           # read output without writing
```

Defaults to `claude-fable-5` (Brian's call, 2026-08-11 — prose, not
synthesis, so a different model than `brief.py`'s Opus default).
Overridable the same way as every other skill (`--llm-model`, `--provider`).

Writes `outputs/briefings/YYYY/MM/YYYY-MM-DD-published.md` — same tier-3
frontmatter shape as the dense brief, `sources:` pointing back at it, plus
a deterministic `substack_subtitle` field (`substack_subtitle()` in
`publish.py` — "Daily Briefing for [date], from Brian Madden's AI second
brain") for pasting into Substack's own subtitle field; also printed to
stdout at the end of the run. The post's actual title is just its H1 in
the body — Fable's job, the one part that has to be written fresh daily.

A fixed `FOOTER` (not model-written — see `publish.py`) gets appended to
every post: real links to `brianmadden.ai` ("what's a second brain / how
to connect your AI") and `bmad.com` ("who's Brian"), both live today, plus
an unlinked "full pipeline lands here soon" line for the one thing that
genuinely isn't public yet (`outputs/` is `v2`-branch-only, not on `main`).
If Brian sets an equivalent footer in Substack's own global email
header/footer setting, this may become redundant for the emailed copy —
unconfirmed whether that setting also covers the web post page, so don't
remove `FOOTER` here until that's verified.

**This generates the draft only — it does not post to Substack.** That's
Day 7 (a live `brianmaddenai` Substack account plus the session-cookie
draft-push client, neither of which exists yet).

## Finalizing edits and rendering for Substack

Substack's editor doesn't interpret pasted Markdown (`**`/`#` show up
literally) but does preserve formatting pasted as rich text/HTML. The
actual publish workflow: Brian hand-edits the committed
`...-published.md` directly (e.g. an inline `[Note from Brian the Human:
...]`), then `render.py`:

```bash
python3 skills/brief/render.py                    # today's post
python3 skills/brief/render.py --date 2026-08-11   # a specific date
```

1. **Finalizes.** Diffs the file against `HEAD` (`git diff --quiet HEAD --
   <path>`). No diff, nothing happens. A diff means Brian edited it by
   hand — the frontmatter `status` flips from `not-reviewed-by-human` to
   `reviewed-and-updated` (the rule already ratified in
   `docs/frontmatter-schema.md`: that status specifically means the
   committed text differs from what the machine generated) and the change
   is committed, with the diff printed first so it's visible before it's
   locked in. This only ever moves status *toward* more-reviewed — it
   can't downgrade anything, matching MAINTAINER.md rule 4. Skip this
   check with `--no-status-sync` if you just want a render.
2. **Renders.** Converts the (now-finalized) body to a small styled HTML
   file — `outputs/briefings/YYYY-MM-DD-published.html`, **gitignored**,
   not repo content, just a copy-paste convenience regenerated on demand.
   Select-all and copy from the *rendered* page (open it in a browser),
   not the HTML source, so Substack's paste picks up formatting.

## Voice and style guide

Two separate references, loaded into both `prompt.md` and
`publish-prompt.md`:

- **[me/voice.md](../../me/voice.md)** — how Brian *thinks and argues*
  (reasoning style, phrases, tone).
- **[me/style-guide.md](../../me/style-guide.md)** — mechanical formatting
  rules (currently: no spaces around em dashes) that apply to any
  generated text regardless of whose voice it's in. Deliberately kept
  separate from voice.md rather than folded in — mechanics and reasoning
  are different kinds of feedback, and mixing them would make voice.md
  harder to use for its actual job. Grows the same opportunistic way
  `sources.yaml`'s `lens`/`pov` fields do: add a rule when Brian actually
  states one (often caught while he's hand-editing a published draft),
  not speculatively.

## Known limitations (v1)

- **Thread matching is exact-slug only.** If the model calls the same
  underlying idea `token-routing-as-governance` one day and
  `routing-tokens-by-task` the next, the tracker treats them as two
  separate threads instead of merging them. No fuzzy matching yet — a
  real gap, flagged rather than solved here.
- **The promotion threshold (3 recurrences) is a first guess, untested.**
  Nobody has watched this pipeline run for weeks yet. BUILD.md open
  decision #8 (canon governance) is the more general version of this
  question — worth revisiting together once #8 is actually picked up.
- **No automation yet.** Runs manually from a terminal, same as ingest.
  Day 6 wires up cron.
- **Not integrated with open decision #8** (developing-thinking.md
  pruning / frameworks retirement). The promotion-candidates queue feeds
  *into* that file over time but doesn't do anything about the file's
  existing staleness problem — that's a separate, deferred piece of work.
- **Wordsmithing diffs aren't mined for voice signal yet.** When Brian
  hand-edits a published draft, `render.py` captures *that a change
  happened* (status flip) but nothing yet looks at *what* changed to
  propose new `voice.md`/`style-guide.md` entries. The git history already
  has every such diff sitting in it (`git log -p` on any
  `*-published.md`) — a future pass (flagged 2026-08-11, not built) could
  periodically mine that history and propose additions the way the
  promotion-candidates queue proposes canon additions: surfaced, never
  auto-applied.
