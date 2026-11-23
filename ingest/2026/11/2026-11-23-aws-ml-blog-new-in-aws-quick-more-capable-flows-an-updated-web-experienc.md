---
title: 'New in AWS Quick: More capable flows, an updated web experience, and agents
  that work together'
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/new-in-aws-quick-more-capable-flows-an-updated-web-experience-and-agents-that-work-together/
author: Hillary Lovric
date_published: '2026-11-21'
date_captured: '2026-11-23'
ingest_method: feed
model: claude-sonnet-5
---

# New in AWS Quick: More capable flows, an updated web experience, and agents that work together

## Insights

- AWS Quick's "Flows" feature now lets users build multi-step business process automations entirely through chat — describing a process in natural language generates an orchestration of agents, skills, tools, and data connections, with a visual diagram for verification.
- Flows now support deterministic (fixed-formula) steps alongside AI-drafted content, aiming to make automated processes consistent and auditable rather than purely generative — explicitly positioned as solving the problem of individual-held tacit process knowledge not transferring to teammates.
- New "multi-agent orchestration" lets one request trigger several specialized agents (each with separate instructions/knowledge/context) working in parallel, with answers combined into a single response that shows each agent's contribution.
- The web app redesign emphasizes persistent/async agent work (tasks continue after closing the browser, resumable via "Mission Control") and a priority-ordered "feed"/daily briefing surfacing emails and messages needing a response.
- New governance/admin controls ship in this release: configurable content-safety and PII guardrails for prompts (preview), group-based permission and usage-limit profiles tied to identity-provider groups, and admin control over which data-source types/connectors users can create or share.
- New connectors added for Meta Ads and Amplitude via MCP servers, with write actions (e.g., campaign creation, budget changes) requiring explicit user permission; customer quote claims no increase in headcount but ~4x more people regularly working with data at one company (Pomelo) and 80 hours/month saved on a single use case.

## Quote

> Before, every analysis or automation depended on the data team. Today, people across every area explore information, make decisions, and build their own agents and flows.
