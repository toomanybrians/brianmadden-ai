---
title: Nobody Built a Bigger Model
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://read.getsuperintel.com/p/nobody-built-a-bigger-model
author: Superintelligence <superintel@mail.beehiiv.com>
date_published: '2026-08-15'
date_captured: '2026-08-17'
ingest_method: email
model: claude-sonnet-5
---

# Nobody Built a Bigger Model

## Insights

- Z.ai's GLM-5.3 release reportedly used the identical 743-billion-parameter base model as GLM-5.2 — no new pretraining — with all reported gains attributed solely to post-training (reinforcement learning/fine-tuning after the base model is built), released 59 days apart.
- Gains were extremely uneven across benchmarks from the same training run: Terminal-Bench 3.0 jumped 6.15x (4.6→28.3), while a generalist agentic test (Agents' Last Exam) moved only 23.8→28.5, and an older benchmark version moved just 81.0→88.2 — same underlying model, wildly different improvement depending on the domain.
- The piece frames this unevenness as evidence that post-training doesn't uniformly raise capability — it appears to selectively "manufacture" gains in specific narrow domains rather than lifting general competence.
- One lab has reportedly stated its post-training compute now exceeds its pre-training compute — suggesting the dominant cost/effort in model-building has shifted from building the base model to what's done to it afterward.
- All cited figures are vendor-reported on vendor-controlled test rigs with no independent verification; even the "dramatic" improved score (28.3/100) still represents mostly failure on the task.
- The clearest documented examples of this post-training-only strategy are coming from Chinese and open-weight labs, with Western frontier labs not disclosing comparable breakdowns of pre- vs. post-training compute or gains.

## Quote

> Scaling post-training is all we did for GLM-5.3.
