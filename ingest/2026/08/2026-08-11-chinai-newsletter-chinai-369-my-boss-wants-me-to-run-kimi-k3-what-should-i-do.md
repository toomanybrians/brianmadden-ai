---
title: 'ChinAI #369: My Boss Wants Me to Run Kimi K3, What Should I Do?'
source: ChinAI Newsletter
source_id: chinai-newsletter
source_url: https://chinai.substack.com/p/chinai-369-my-boss-wants-me-to-run
author: Jeffrey Ding
date_published: '2026-08-03'
date_captured: '2026-08-11'
ingest_method: feed
model: claude-sonnet-5
---

# ChinAI #369: My Boss Wants Me to Run Kimi K3, What Should I Do?

## Insights

- "Open-source" LLMs like Kimi K3 only release model weights, not source code or training pipeline — a meaningfully different concept than open-source software, which limits what "free" actually means for enterprise adopters.
- K3 requires a minimum of 16 H200 GPUs just to load, and Moonshot's recommended deployment is a 64-accelerator super-node (~17M RMB), putting it firmly in data-center/enterprise-only territory — unlike its predecessor K2, which enthusiasts could compress and run on a Mac Studio.
- The underlying economics of large models inverts traditional software economics: development is extremely costly but replication is free, while every inference run burns real money in electricity and compute — unlike traditional software where operation is nearly free after development.
- This creates a practical governance problem for organizations: employees or managers may assume a "free, open" model means no infrastructure cost, when in practice compute and power requirements (45kW at full load) can exceed what most organizations, let alone individuals, can provision.
- Independent assessment by UK AI Security Institute and NIST's CAISI found K3 notably weak at converting discovered vulnerabilities into working exploits, prompting speculation about whether Moonshot deliberately limited its cyber capabilities — relevant to enterprise risk calculus around deploying capable open-weight models.

## Quote

> The recipe is truly free, but the kitchen is truly unaffordable.
