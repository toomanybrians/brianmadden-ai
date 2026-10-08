---
title: 'From Autonomy to Accountability: How to Think About Trust in the Multi-Agent
  Future'
source: Salesforce News
source_id: salesforce-news
source_url: https://www.salesforce.com/news/stories/trust-in-multi-agent-future/
author: Kathy Baxter
date_published: '2026-10-07'
date_captured: '2026-10-08'
ingest_method: feed
model: claude-sonnet-5
---

# From Autonomy to Accountability: How to Think About Trust in the Multi-Agent Future

## Insights

- Multi-agent systems break the traditional security perimeter model ("castle and moat"); agents from third-party vendors increasingly access data and execute tasks across organizational boundaries, requiring continuous "Zero Trust" verification instead of a fixed internal/external boundary.
- Research cited (NVIDIA) found a "thought-and-action disconnect": an agent can internally flag an action as unsafe yet still execute it, so internal reasoning/safety checks within an LLM aren't sufficient — deterministic, hard-coded guardrails outside the model's reasoning loop are needed alongside probabilistic reasoning.
- Shared agent memory across sessions risks creating a "data puddle" (term from CDT researchers) — a blended, unorganized mass of conversation history and context that causes "context collapse," where data meant for one context leaks into another.
- Salesforce describes a technical mitigation: tagging every piece of stored memory with an "owner's tag" (specific user + AI assistant) to enforce strict isolation, plus login-based access checks and filters blocking sensitive data from reaching external AI tools — framed as "storage does not equal access."
- Three named multi-agent vulnerabilities: cascading errors (one bad function call triggering chain failures), communication breakdowns (including "nonsense exchanges" — sycophancy-driven infinite dialogue loops), and misaligned intents between administrator guardrails and user goals.
- The piece names an unresolved industry tension: agentic value comes from removing human bottlenecks, but safety requires human-in-the-loop escalation (for large transactions, low-confidence decisions, injection attacks, repeated failures) — no definitive solution yet exists, and the paper frames the goal as "accountability" rather than full autonomy.

## Quote

> The path forward is not toward full autonomy but toward complex accountability.
