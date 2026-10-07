---
title: How to Automate Inbound
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: ''
author: Tomasz Tunguz <blog@tomtunguz.com>
date_published: '2026-10-06'
date_captured: '2026-10-07'
ingest_method: email
model: claude-sonnet-5
---

# How to Automate Inbound

## Insights

- Vercel built an AI agent to run the top of its sales funnel (inbound lead qualification), starting as a 20%-time side project for one engineer, built on a 125-line prompt written by the team's top SDR encoding qualification rules.
- Rollout followed a human-in-the-loop apprenticeship model: the agent initially did research, qualification, and drafting but couldn't send messages; a human reviewed 100% of early output, then tapered to a 1-in-100 sample once the agent proved competent — mirroring how a manager trains a new human hire.
- As the business scaled upmarket into enterprise and added product complexity, the prompt grew to 1000 lines, but the team found the model inconsistently followed embedded rules that were actually deterministic logic, not judgment calls.
- The solution was architectural: splitting the system into explicit hard-coded rules (now 14, e.g., Salesforce lookup to route leads with open opportunities to account executives) versus model-based judgment for the remaining ambiguous cases — plus a second "escalation agent" that monitors for rule breaches and either fixes or approves exceptions.
- This mirrors a broader pattern the author found across 14 production agent workflows: 65% of workflow nodes end up as pure deterministic code, with only 14% remaining fully agentic — suggesting mature AI systems trend toward less (not more) open-ended model reasoning over time.
- Organizational effect: the SDR team overseeing the agent was promoted to outbound roles ahead of schedule, with the stated rationale that human value lies in conversation, not email-based qualification work. Cost cited: ~$1,000/year in inference and infrastructure to run the entire inbound function.

## Quote

> The value of humans is talking to humans. — Jeanne DeWitt Grosser, COO of Vercel
