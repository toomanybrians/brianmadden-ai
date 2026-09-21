---
title: At Least 45 Days
source: The AI Realist
source_id: ai-realist
source_url: https://www.airealist.ai/p/at-least-45-days
author: Julien Simon
date_published: '2026-09-20'
date_captured: '2026-09-21'
ingest_method: feed
model: claude-sonnet-5
---

# At Least 45 Days

## Insights

- AWS added Moonshot's Kimi K3 to Bedrock at Moonshot's own pricing just 10 days after a joint NSA/CISA/FBI advisory stated Moonshot had used significant Claude data to train K3 without disclosure.
- Sometime between Sept 3–9, 2026, AWS quietly split its Bedrock lifecycle policy into two pages with no changelog entry: a "Legacy" page for pre-Sept-7 models (12-month floor, 6-month notice) and a new page for models launched after, which introduced a shorter 45-day notice tier alongside the standard 6-month one.
- Of 128 Bedrock model cards checked, only Kimi K3 carries the 45-day notice with no minimum retention floor; all 18 other cards from advisory-named Chinese labs (DeepSeek, Qwen, MiniMax, Z.AI, Moonshot's own other models) retain the old 12-month/6-month terms because they launched before the policy split.
- By contrast, OpenAI's GPT-6 Astra, launched Sept 8 under the same new policy regime, got the full 12-month floor and 6-month notice — suggesting the shortened term isn't simply about being newly launched or open-weight.
- Microsoft's comparable Foundry/Fireworks lifecycle pages explicitly publish retirement terms, dates, and a stated rationale ("compliance or security issues" triggers emergency retirement), whereas AWS gives K3 a uniquely short exit window without stating why or acknowledging the advisory.
- Separately, Anthropic reported Moonshot silently forwarded customer requests to Claude instead of processing them with Kimi — a routing/trust issue AWS says can't occur on Bedrock since data stays inside AWS's own infrastructure boundary.
- The piece frames this as part of a broader AWS pattern of imprecise, hedged public disclosure (drawing a parallel to how AWS worded a data-center drone-strike incident) — technically accurate statements that avoid stating the operative facts plainly.

## Quote

> Everything is written down precisely in Seattle, in a place where nobody will read it.
