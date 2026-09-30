---
title: 'How to Use Claude Opus 5.5: The Complete Guide 📚'
source: Linas's Newsletter
source_id: linas-newsletter
source_url: https://linas.substack.com/p/how-to-use-claude-opus-5-5
author: Linas Beliūnas
date_published: '2026-09-29'
date_captured: '2026-09-30'
ingest_method: feed
model: claude-sonnet-5
---

# How to Use Claude Opus 5.5: The Complete Guide 📚

## Insights

- Anthropic's Claude Opus 5.5 (released Sept 22, 2026) is now the default model in Claude Code on all paid plans and tops the Artificial Analysis Intelligence Index; the touted "40% cheaper" figure only holds at default settings — token prices actually dropped just 20% ($4/M input, $20/M output), with the rest of the savings coming from using fewer tokens per task if configured properly.
- Reported performance gains include auditing/fixing a 200,000-line codebase in under 3 hours (vs 20+ hours for Opus 5), and Quantium cutting a coding task from 38 prompts/4 days to 11 prompts/3 hours.
- On factual reliability, 16 of 18 Opus 5.5 earnings-research reports had no invented figures/quotes, versus zero clean reports from Fable 5.1 or Opus 5.
- Three common usage mistakes erase the cost/quality gains: running at max effort (nearly doubles output tokens, erasing savings — medium effort already matches or beats old Opus 5 at high on evals); carrying over old prompt habits like "think carefully" phrasing (unnecessary, and chain-of-thought requests are now blocked and billed as of Sept 24); and trusting unattended agent runs, since the model may end a turn with a "progress report" that looks like task completion but isn't.
- There's a documented quality/security gap: Opus 5.5 code showed 44% more concurrency problems per line than Opus 5 (per Sonar), and only 33.5% of its fixes passed security checks once memorized answers were excluded (per Endor Labs) — meaning targeted verification is needed for these weak spots.
- Recommended operating habits: start at medium effort, give the model the full task in one message with a clear stopping condition, specify exactly when it should stop and ask for input, and verify outputs specifically where the model is weakest.

## Quote

> Anthropic has finally made frontier-level AI cheaper, and most teams will still end up paying close to full price.
