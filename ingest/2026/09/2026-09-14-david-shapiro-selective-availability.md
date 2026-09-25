---
title: Selective Availability
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://julsimon.substack.com/p/selective-availability
author: Julien Simon from The AI Realist <julsimon@substack.com>
date_published: '2026-09-11'
date_captured: '2026-09-14'
ingest_method: email
model: claude-sonnet-5
---

# Selective Availability

## Insights

- A joint NSA/CISA/FBI advisory on Chinese AI distillation recommends that US AI providers "subtly alter responses" for suspected malicious distillation attempts (e.g., reduced reasoning depth, stylistic changes) without informing the affected account — even though the detection signals used (high-volume new accounts, cache-optimized usage patterns) overlap heavily with normal enterprise production traffic.
- Twelve of the advisory's seventeen recommended mitigations only function against traffic hitting a provider's own API infrastructure (rate limiting, logging, output degradation); they do nothing against a model once its weights are downloaded and run elsewhere — yet the advisory never states this limitation.
- The advisory names OpenAI's own open-weight model (GPT-oss-20b, Apache 2.0 licensed, ungated, ~6.5M downloads/month) as one used by a Chinese company for distillation, illustrating that the document's own evidence sits partly outside the reach of its own recommended defenses.
- The advisory's evidentiary basis is entirely public sourcing (company blog posts, a NIST taxonomy, White House memos, a social media post) — no independent government evidence (telemetry, seizures, indictments) is cited, and it gives no false-positive rate for its detection/degradation approach.
- Comparison to the 2000 US decision to end GPS "Selective Availability" degradation: that policy was named, dated, publicly announced, and endable-with-notice; the AI advisory's degradation approach is explicitly designed to avoid detection by both the targeted distillers and the paying customers who might be caught by mistake.
- Existing US policy avenues (executive order, Entity List, Defense Authorization Act) target government/military use of specific Chinese AI systems but leave no rule governing a private company that downloads and self-hosts open-weight Chinese (or affected) models — the advisory functions as informal guidance rather than binding regulation.

## Quote

> "If this one starts on your account, it's built not to be noticed."
