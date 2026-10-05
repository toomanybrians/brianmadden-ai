---
title: '"The most common failure isn''t a bad model": CoreWeave''s Richard Ahlfeld
  on physical AI'
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://link.mail.beehiiv.com/v2/c/5118342efa049889ab588060eb7bb37d1ba023892bfcc4b1f04069d96b2f9b1ed67f333a082930859060fca53dc4e1e0c124efe5bb5d8309bd84205a3c0a84b39bf89607d0caaa1407eeae91dc0c11b0f141fe569571ce48eec3781bb9be3a469aa438836ca690ab74a593f61a0682f28d2cfefe313f754798811dfa1a76aa82aeb1d986aa89733d548cc0edfa64209bcfaa6d520894e6e4be0727e4702ac1b7/8f243dfe36f729ee
author: Superintelligence <superintel@mail.beehiiv.com>
date_published: '2026-10-04'
date_captured: '2026-10-05'
ingest_method: email
model: claude-sonnet-5
---

# "The most common failure isn't a bad model": CoreWeave's Richard Ahlfeld on physical AI

## Insights

- CoreWeave's Richard Ahlfeld argues the dominant failure mode in physical AI isn't model architecture or compute — it's training data that never captured the rare, consequential moments (e.g., flawless driving data is useless for predicting failures). Embedded domain engineers add value by judging which edge cases deserve synthetic coverage versus which anomalies are real signal.
- NEURA Robotics' approach (via its "NEURA Gym" facility) treats data quality as more important than data volume, running a daily loop of real-robot task attempts, evaluation, targeted data collection, and retraining rather than accumulating generic data at scale.
- CoreWeave draws a hard governance line for agents in physical AI systems: agents working purely on data/models (feature engineering, algorithm tuning) can run fully unsupervised, but any agent action that touches physical hardware or recommends recalibration requires human review — enforced by design (an "allow, ask, deny" permission hierarchy) plus mandatory traceable artifacts (metrics, lineage) so review isn't a rubber stamp.
- Synthetic/simulated data is deemed credible only where physics is well-modeled (lighting, geometry, motion) — demonstrated by fixing a humanoid robot's low-light navigation failures using NVIDIA's Cosmos world model. It remains unreliable for granular materials, liquids, soft materials, and erratic human behavior, where physical testing stays unavoidable.
- On the Aston Martin F1 radio-processing case, reliability was validated via word-error-rate and LLM-based scoring in Weights & Biases Weave, then live-tested at two actual races before full deployment — illustrating a validate-in-controlled-settings-then-test-live methodology for high-stakes, time-critical AI decisions.
- Ahlfeld proposes "time-to-first working model" (currently months) as the key metric for whether physical AI is becoming repeatable; the goal is for customer engineers to eventually run follow-on projects without CoreWeave's involvement, though data ownership is clear while model/code ownership terms are set per engagement.

## Quote

> The most common failure isn't a bad model, it's a training set that never contained the moments that matter. — Richard Ahlfeld
