---
title: "Formatting and mechanical style guide"
authority_level: 1
file_type: style-guide
tags: ["formatting", "typography", "style-guide", "mechanics"]
staleness_threshold: stable
description: "Mechanical formatting conventions for AI-generated content in this pipeline — punctuation, typography — distinct from me/voice.md's reasoning/tone guidance."
tier: 2
status: reviewed
---

# Formatting and mechanical style guide

This is deliberately separate from [me/voice.md](voice.md). Voice is about
*how Brian thinks and argues* — reasoning style, phrases, tone. This file
is about *mechanics* — punctuation and typography rules that apply to any
AI-generated text in this pipeline (Brian's own voice or the
`brianmadden.ai` AI byline), the way a house style guide is separate from
an author's actual voice. Conflating the two would make voice.md harder to
use for its actual job.

Grows the same way `sources.yaml`'s `lens`/`pov` fields do: added when
Brian actually states a preference (often while hand-editing generated
output), not pre-populated speculatively.

## Punctuation

- **Em dashes have no surrounding spaces.** `word—word`, not `word — word`.
  (Brian's correction, 2026-08-11 — caught while editing a published
  draft, replacing a spaced em-dash aside with parentheses.)

## Tense

- **Predictions and forecasts use explicit future tense ("will"), not the
  futurate present.** "This will play out as X," not "This plays out as
  X." The futurate present borrows the certainty of an already-happening
  fact and lends it to something that's actually just a forecast — it
  makes a prediction read as more inevitable than it has any right to be.
  Reserve present tense for facts and things already true; use "will" for
  anything that's actually a forecast. (Brian's correction, 2026-08-11 —
  caught in his own edit: "judgment and governance stay human longest" →
  "judgment and governance will stay human the longest.")

## Sentence structure

- **No fragment-style openers.** Don't lead a summary/description with a
  dropped-subject fragment — "Closing keynote to an audience of app
  management practitioners," not a complete sentence. Write a real,
  human-friendly lead sentence instead, even though fragment ledes have
  become a common tic in AI-generated summaries. (Brian's correction,
  2026-08-14 — caught reviewing a sample talk-summary intro.)

## Byline and point of view

- **Content posted under the `brianmadden.ai` byline refers to Brian in
  the third person**, even when recapping something Brian said or did
  ("Brian gave the closing keynote at..."), never first person as if
  Brian himself were narrating, and never the AI writing as if *it* were
  Brian. The AI byline is a distinct voice describing Brian's work, not a
  ghostwriter impersonating him. (Brian's correction, 2026-08-14 — same
  talk-summary review as above.)

## Substack rendering

- **No inline code (backtick) formatting in anything published to
  Substack.** Substack's editor renders pasted inline code in an
  oversized, visually odd Courier face — confirmed, not a guess. Use
  **bold** for a short label/identifier at the start of a bullet (e.g. a
  tracked-thread slug), and *italics* for an inline file/path reference.
  A `.md` file reference should also be a real Markdown link, not bare
  text — see the next rule. (Brian's correction, 2026-08-16.)
- **A tracked-thread's kebab-case slug (`inference-allocation-as-supply-
  risk`) is bookkeeping, not vocabulary — it never appears inside a
  sentence of prose, bolded or not.** The rule above only ever meant the
  "Threads being tracked" bullet list at the bottom of the brief, where a
  slug legitimately labels its own line. When referencing a tracked
  thread from inside Part 1's prose, describe it in plain English (a real
  noun phrase a human would say out loud) the same way you'd describe any
  other idea — never drop the raw slug into the sentence, bolded or not.
  (Brian's correction, 2026-08-26 — the Aug 16 rule got over-applied: by
  Aug 17 body paragraphs were bolding slugs mid-sentence throughout the
  brief, e.g. "the **inference-allocation-as-supply-risk** thread," and
  it climbed to 17 such instances by Aug 26. Confirmed by counting
  bolded-kebab-slug occurrences across every published brief this
  month — zero through Aug 14, then present in every issue from Aug 17
  on.)
- **Any `.md` file mentioned inline gets linked to its actual GitHub file**,
  pointed at the `main` branch (`GITHUB_BASE` in `skills/brief/brief.py`) —
  not `v2`. Until the v2 launch PR merges, these links 404; Brian's
  explicitly fine with that for the few days until then, since `main` is
  where the link actually resolves once merged, and it needs no further
  edit at that point. (Brian's call, 2026-08-16.)
- **The fixed footer below the closing `---` on every published post is
  italicized** (the whole paragraph, links included) — visually marks it
  as boilerplate/meta text, distinct from the brief's own content above
  it. (Brian's call, 2026-08-16.)

## Self-consciousness

- **Don't narrate the pipeline's own state to the reader** — no "this
  issue is bigger than normal because it's clearing a backlog," no
  explaining why the format looks unusual this time. Say what happened;
  don't apologize for or account to the reader for how the piece came
  together. (Brian's correction, 2026-08-24 — cut from both the opening
  paragraph and a section intro of the first *Deeper Thinking* issue.)
- **Section-explainer lines read as plain prose, integrated into the
  flow — not set off in italics.** Italicizing "here's what this section
  is" makes it read as a publisher's aside rather than part of the piece
  itself. (Brian's correction, 2026-08-24, same session — he stripped the
  italics from every explainer line in the first *Deeper Thinking* issue
  and folded them into normal sentences.)

## Audience-specific sections

- **Internal/canon-only sections don't carry over to human-facing
  surfaces.** A canon file's "Key frameworks" link list (or similar
  AI-to-AI navigational aids) belongs in the brain — drop it, don't just
  reformat it, when generating a version for a human reader (e.g. a
  Substack post). Human-facing surfaces should read as if written for a
  person dropping in, not as a rendering of the machine-readable version.
  (Brian's correction, 2026-08-14 — same talk-summary review.)
