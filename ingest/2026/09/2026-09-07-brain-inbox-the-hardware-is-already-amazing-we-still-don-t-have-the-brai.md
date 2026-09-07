---
title: '"The hardware is already amazing. We still don''t have the brain": LTX''s
  Yaron Inger on world models, robots and what open weights are for'
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://link.mail.beehiiv.com/v2/c/624005d1e59ad4c0c7c3698298d291827e20cda74fc1133b0cb32cd6597c716360d1b30438ec51936187f0459576f867b4a2262493f4932ef75dee5a774884dae0c97122a6e43a17388a908f9fbbbe2cc4cb3922304ffad496c5606c9ceed7f2ae1803b2e687b6e257c5e351145fc1674577a08c42cc0aeea070f6e22bcc23234354d30d561eebddf05dd5d3cbb1717c3cd88fa9cd20b36b2088e8bce77e81d3/bd1e33c19b5aeb89
author: Superintelligence <superintel@mail.beehiiv.com>
date_published: '2026-09-06'
date_captured: '2026-09-07'
ingest_method: email
model: claude-sonnet-5
---

# "The hardware is already amazing. We still don't have the brain": LTX's Yaron Inger on world models, robots and what open weights are for

## Insights

- LTX defines a "world model" as predicting the next state of the world given context and instructions (not just the next token, as LLMs do), enabling a robot to recover from errors—like a missed grasp—rather than halting.
- Architectural changes in LTX-2.5 include a jointly fine-tuned 12B Gemma 4 text encoder (a technique the CTO says no other open-source video model has tried) and a more compressed latent space (32x32x8 vs. the industry-typical 16x16x4), paired with a new decoder that generates uncompressed keyframes to boost pixel quality without sacrificing speed.
- Business model: the model is free to use commercially below $10M in annual revenue; above that, companies buy a license, and many enterprise customers use LTX as an undisclosed white-label backbone inside their own branded products.
- An unexpected engineering result: the distilled (faster, fewer-step) version of the model now produces better video quality than the full base model, with only audio still favoring the base model—a discrepancy still being investigated.
- A four-to-five-person robotics startup (Markov Robotics) reportedly trained a manipulation task using roughly one hour of teleoperation data on top of LTX, though Markov's own site describes its data budget as "less than five hours."
- The CTO identifies long-horizon memory/context as the biggest unsolved gap: video models lose track of state and out-of-frame objects over multi-minute tasks, unlike LLMs with million-token context windows, and he considers the durable competitive moat to be release/ecosystem infrastructure and internal team culture rather than the model's technical architecture, which he expects competitors to eventually replicate.

## Quote

> The hardware is already amazing. We still do not have the brain. — Yaron Inger
