---
title: Selective Availability
source: The AI Realist
source_id: ai-realist
source_url: https://www.airealist.ai/p/selective-availability
author: Julien Simon
date_published: '2026-09-11'
date_captured: '2026-09-14'
ingest_method: feed
model: claude-sonnet-5
---

# Selective Availability

## Insights

- A joint NSA/CISA/FBI advisory (Sept 8, 2026) on Chinese AI distillation includes a recommendation that US AI providers "subtly alter responses" for suspected malicious distillation attempts — degrading answers (less reasoning depth, stylistic changes) while deliberately not informing the account holder they've been switched to a downgraded model.
- The detection signals the advisory lists for flagging suspected distillers (new-account burst usage, cache-optimized traffic patterns) closely resemble ordinary enterprise production traffic patterns — meaning legitimate paying customers could be misidentified and silently degraded, with no disclosed false-positive rate anywhere in the document.
- Of the advisory's 17 recommended mitigations, 12 only work against traffic hitting a provider's own API infrastructure; they do nothing against a model whose weights have already been downloaded and run elsewhere — yet the advisory names GPT-oss-20b (OpenAI's own openly licensed, undownloadable-restriction-free model) as an example of a distilled model, which its own framework can't actually address.
- The advisory's "don't tell" instruction is narrower in its stated scope (China-based/confirmed malicious distillation users) but reads more broadly in isolation, and explicitly exempts only "AI safety researchers and third-party evaluators" from the secrecy — ordinary enterprise buyers are not covered and can't easily self-verify via their own evaluations (a cited 2025 survey found ~23% of production AI teams don't evaluate their agents at all).
- The piece contrasts this with the US government's own 2000 decision to end GPS "Selective Availability," which was publicly announced by the President with a specific end date — versus the 2026 advisory's silent, unannounced, reversible-in-secret degradation of AI outputs, which leaves no visible record for the affected customer.
- Existing legal/regulatory levers (Entity List export controls, Pentagon/DoD contractor bans on DeepSeek) don't reach ordinary US enterprises deploying Chinese-origin open-weight models in their own business; no current rule restricts that, leaving the "quietly degrade and don't disclose" advisory as the only mechanism operating in that gap — but only against traffic that stays on a vendor's hosted API.

## Quote

> A change built to fool a lab's test pipeline would fool a customer's tests too.
