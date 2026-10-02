---
title: '#244: How Alibaba.com Is Building the Future of Agent-to-Agent Commerce'
source: The Artificial Intelligence Show
source_id: the-artificial-intelligence-show
source_url: https://podcast.smarterx.ai/shownotes/244
author: Paul Roetzer and Mike Kaput
date_published: '2026-10-01'
date_captured: '2026-10-02'
ingest_method: feed
model: claude-sonnet-5
---

# #244: How Alibaba.com Is Building the Future of Agent-to-Agent Commerce

## Insights

- Alibaba.com frames B2B commerce as fundamentally different from B2C for agent automation: B2B orders average ~$3,000, involve comparing ~20 decision variables (MOQ, certificates, delivery terms, Incoterms, etc.), and require ~60 steps from idea to delivered product — making it a better fit for agentic automation than consumer shopping, which Kuo argues people don't want to delegate because "killing time" (browsing) is often the point.
- Axio (named after the Harry Potter summoning charm) evolved from an AI search/sourcing tool into "Axio Work," a set of specialized agents handling market research, product design-pack generation, supplier negotiation, store operations, marketing, logistics, and compliance — reportedly used by over 10 million small businesses, consuming 1 trillion AI tokens over three months.
- Kuo describes agent capability with the formula "agent = model × harness × context" — model (Qwen plus post-training), harness (logic, guardrails, tool integrations), and context (real business/transaction data) — emphasizing that if any one factor is zero, the agent fails, and that this combination is hard to replicate elsewhere.
- Alibaba.com built "Commerce Agent Bench," an evolving internal benchmark (107 tasks currently, derived from millions of real buyer-seller conversations) to test which models/configurations perform best on real commercial tasks, framed around a "Pareto frontier" of cost, speed, and reliability trade-offs rather than abstract capability.
- Internally, Axio operates as a separate startup-like unit shipping daily updates (versus Alibaba.com's biweekly/monthly release cycle for its 26-year-old core platform), with the two now being integrated via an "AI mode" so the legacy platform itself updates daily and is built to be used by agents, not just humans.
- The long-term vision is "A2A" (agent-to-agent) commerce: buyer-side and seller-side agents negotiating and transacting directly across a large network, which Kuo describes as a multiplicative matching effect rather than today's search/ranking model that only surfaces a limited slice of suppliers to a buyer.
- Biggest challenge cited: the pace of change makes multi-year planning obsolete ("three years means forever"), with the agent-design formula itself only becoming articulable in roughly the last six months as underlying technology and model behavior evolved.

## Quote

> "We believe that the B2B will go to A2A, so agent to agent. That will be the future." — Kuo Zhang, president of Alibaba.com
