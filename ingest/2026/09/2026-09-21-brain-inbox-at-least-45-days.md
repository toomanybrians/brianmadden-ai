---
title: At Least 45 Days
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://julsimon.substack.com/p/at-least-45-days
author: Julien Simon from The AI Realist <julsimon@substack.com>
date_published: '2026-09-20'
date_captured: '2026-09-21'
ingest_method: email
model: claude-sonnet-5
---

# At Least 45 Days

## Insights

- AWS added Moonshot's Kimi K3 to Bedrock at Moonshot's own pricing days after a US government advisory (NSA/CISA/FBI) alleged Moonshot had extracted data from a Claude model to train K3 — a fact AWS's launch post did not mention.
- Sometime between Sept 3–9, 2026, AWS quietly split its Bedrock model lifecycle policy into "Legacy" (pre-Sept 7 models, guaranteed 12 months on-shelf + 6 months' notice) and a new page for later models with variable, per-model terms and no public criteria for which models get which term — with no changelog entry documenting the change.
- Of 128 Bedrock model cards audited, only two launched under the new policy; K3 is the only one given the minimum available terms (no minimum shelf life, just 45 days' notice), while OpenAI's GPT-6 Astra got 12 months/6 months notice under the new page. All 18 other Chinese-origin models named in the advisory (DeepSeek, Qwen, MiniMax, Z.AI) retain the old 12-month/6-month terms because they launched before the policy split.
- AWS markets Bedrock-hosted K3 as fully self-contained ("not shared with the model provider"), directly addressing a separate Anthropic report (Sept 10) that Moonshot's own API had silently forwarded customer requests to Claude instead of processing them with Kimi — implying AWS's hosting was partly a response to trust concerns about Moonshot's own infrastructure.
- Comparison to Microsoft's Foundry/Azure model lifecycle policy: Microsoft publishes explicit terms (12-month lifecycle for non-Microsoft labs, 60-day GA notice, explicit "emergency retirement" clause for compliance/security issues) and prints exact retirement dates for third-party models like Kimi via Fireworks — contrasted with AWS's undocumented, unexplained shortening of terms specifically for K3.
- Author frames this against a legal backdrop: the FY2026 defense authorization act already forced a 30-day removal of DeepSeek from Pentagon systems, and a pending Senate bill could add Moonshot to similar restrictions — meaning a short contractual notice period isn't legally required now but could preemptively ease removal from commercial systems later.

## Quote

> Sell the model, keep the exit short, and don't explain the rule.
