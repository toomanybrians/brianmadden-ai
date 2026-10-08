---
title: 'Beyond hours saved: Building the business case for agentic automation'
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/beyond-hours-saved-building-the-business-case-for-agentic-automation/
author: Manish Ballal
date_published: '2026-10-07'
date_captured: '2026-10-08'
ingest_method: feed
model: claude-sonnet-5
---

# Beyond hours saved: Building the business case for agentic automation

## Insights

- The standard RPA-era ROI formula (hours saved × labor cost − build cost) undercounts agentic automation's value because it assumes stable processes, rule-based tasks, no human oversight needed, and that saved hours automatically convert to P&L savings — often they just refill with backlog instead.
- Proposes an "Agentic Value Model" with four value pools beyond time savings: exception/error-handling costs (AWS cites rework costing 1.5–4x original transaction cost, errors driving 2–15% of operational cost), decision quality at scale, and change-resilience/maintenance economics (agents shift maintenance burden into evals/prompts/monitoring rather than eliminating it).
- Cites McKinsey's "1:3:5" pattern — for every $1 on agentic tech, successful transformations spend $3 on process redesign and $5 on capability-building/adoption — and notes most companies invert this ratio.
- Worked claims-triage example shows released "capacity" (~$1.26M) only becomes real savings if headcount/contractor spend actually falls (~half captured via attrition in the illustration) — otherwise it's not real P&L value unless redeployed to a measurable outcome.
- Offers a 2x2 prioritization matrix (task complexity vs. decision risk): low/low stays on RPA, high complexity/low risk is a throughput play, high complexity/high risk needs human-in-loop decision-quality justification, low complexity/high risk just needs better guardrails, not agents.
- Cites McKinsey finding that ~two-thirds of enterprises have piloted agents but fewer than 10% have scaled to tangible value; recommends framing investment as a portfolio of 3-5 workflows with explicit stop rules/break-even targets rather than single pilots.
- References three AWS customer deployments (Kitsa, dLocal, Genpact) using Amazon Quick Automate as illustrative evidence for the value pools, alongside promotion of Amazon Quick/Quick Automate as the vendor's product for this workflow.

## Quote

> We assume the value of automation lives in the task, but in agentic automation most of it lives around the task.
