---
title: 'Nobody Wrote the Rules: How AI Actually Gets Made'
source: GuardRailNow
source_id: guardrailnow
source_url: https://guardrailnow.substack.com/p/nobody-wrote-the-rules-how-ai-actually
author: The AI Risk Network. AI Safety
date_published: '2026-11-20'
date_captured: '2026-11-23'
ingest_method: feed
model: claude-sonnet-5
---

# Nobody Wrote the Rules: How AI Actually Gets Made

## Insights

- Large language models aren't rule-based systems; they're trained by predicting the next word across trillions of words of text, adjusting billions of internal parameters in the process — no one specifies what the model should "want" or value.
- After initial training, models are further shaped into assistants via reward-based tuning, where human or automated scorers rate outputs as good or bad, reinforcing certain behaviors without explicit rule-writing.
- Anthropic's "Golden Gate Claude" experiment (May 2024) demonstrated that researchers can sometimes locate a specific internal concept inside a model and amplify it — but this was described as a rare, narrow success.
- Anthropic itself stated that the concepts it has successfully mapped represent only "a small subset" of what the model has learned, and that fully mapping a model's internals would require more computing power than training it did.
- Anthropic's interpretability ("tracing") methods reportedly capture only "a fraction" of what the model actually computes, even on short prompts.
- Current AI safety practice is described as relying mainly on observing model behavior (testing outputs) rather than understanding the internal reasoning that produces those outputs.

## Quote

> Nobody writes down what the model should want. What comes out works, and nobody can fully read it.
