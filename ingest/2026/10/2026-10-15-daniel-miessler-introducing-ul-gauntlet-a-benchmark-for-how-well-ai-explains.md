---
title: Introducing UL Gauntlet, a Benchmark for How Well AI Explains
source: Daniel Miessler
source_id: daniel-miessler
source_url: https://danielmiessler.com/blog/introducing-ul-gauntlet?utm_source=rss&utm_medium=feed&utm_campaign=website
author: daniel@danielmiessler.com (Daniel Miessler)
date_published: '2026-10-15'
date_captured: '2026-10-15'
ingest_method: feed
model: claude-sonnet-5
---

# Introducing UL Gauntlet, a Benchmark for How Well AI Explains

## Insights

- UL Gauntlet is a new benchmark that grades AI models on explanation quality rather than factual correctness, using David Deutsch's criterion that a good explanation is "hard to vary" — every part must do work and be testable.
- Models answer 14 open (often unsettled) questions closed-book, in six structured sections (Answer, Evidence, Uncertainty, Experiment, Falsifier, Sources), capped at 600 words; answers that run over are cut before grading.
- Grading uses three top models (one per lab) as judges, with identities anonymized and shuffled, and a rule disqualifying a judge's grade on any answer from its own lab, to reduce self-bias.
- First results (10 models, 5 labs, 30 effort settings): Claude Opus 5.5 at max effort scored highest (3.15/4), but its lead over Claude Fable at xhigh (3.07) fell within the statistical margin of error — a tie.
- More reasoning effort doesn't reliably improve explanation quality: some models (Sonnet) improve steadily with effort, others (Fable, Astra, Sol) peak at lower effort and degrade at higher settings; Opus at max used ~21x the tokens of Fable at xhigh for an equivalent score.
- The benchmark's judges are themselves AI models whose grades are "advisory" pending calibration against the human (Daniel's) own reads — an acknowledged current limitation, along with limited statistical power to distinguish closely-scored models.
- Questions are designed to be public (answers can't be inferred from the question), but model answers and judge verdicts stay private specifically to prevent future models from training on them.

## Quote

> A good explanation is hard to vary. Change a load-bearing detail and it stops explaining anything.
