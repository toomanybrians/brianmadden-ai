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

## Audience-specific sections

- **Internal/canon-only sections don't carry over to human-facing
  surfaces.** A canon file's "Key frameworks" link list (or similar
  AI-to-AI navigational aids) belongs in the brain — drop it, don't just
  reformat it, when generating a version for a human reader (e.g. a
  Substack post). Human-facing surfaces should read as if written for a
  person dropping in, not as a rendering of the machine-readable version.
  (Brian's correction, 2026-08-14 — same talk-summary review.)
