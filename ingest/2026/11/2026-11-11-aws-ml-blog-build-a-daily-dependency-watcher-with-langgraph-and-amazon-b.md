---
title: Build a daily dependency watcher with LangGraph and Amazon Bedrock AgentCore
  web search
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-a-daily-dependency-watcher-with-langgraph-and-amazon-bedrock-agentcore-web-search/
author: Sundar Raghavan
date_published: '2026-11-10'
date_captured: '2026-11-11'
ingest_method: feed
model: claude-sonnet-5
---

# Build a daily dependency watcher with LangGraph and Amazon Bedrock AgentCore web search

## Insights

- AWS launched a Web Search API inside Amazon Bedrock AgentCore that lets agents get current web results via a single signed API call, using existing AWS credentials — no separate search API key to manage. Queries are served from an AWS-operated web index, not routed to a third-party search engine, which AWS frames as a data-exposure/privacy control for enterprises worried about leaking internal work through search queries.
- Architectural pattern demonstrated: keep "rules the model can't change" (date windows, domain blocklists, search budget, evidence checks) enforced in code/tooling rather than relying on the LLM to self-govern — the model only chooses what to search for and drafts findings, but can't widen the search scope.
- The example implements a post-hoc "evidence check" on agent-generated findings: verifying cited URLs actually came from the agent's own searches, that package names and CVE IDs appear in the source text, and that sources fall inside the time window — explicitly catching hallucinated citations/IDs, but not verifying severity, exploitation status, or recommended actions (AWS recommends human review before acting).
- Demonstrated parallelism via LangGraph's "fan out" (Send API): three research branches (npm, PyPI, container images) ran concurrently in 36 seconds versus 99 seconds sequentially — a concrete illustration of agent orchestration speedup through parallel sub-agent branches.
- Two deployment/governance modes are offered: direct API calls (app enforces its own rules, needs one IAM permission) versus AgentCore Gateway (a platform/admin team enforces one shared source policy — e.g., blocklist — across many agents or MCP clients like Claude, "hidden from the agent, which can't lift it").
- A state/memory mechanism ("keep_new" checked against a persistent store) deduplicates findings across daily runs so the same advisory isn't re-reported — framed as necessary infrastructure for a recurring/scheduled agent rather than a one-off query.

## Quote

> The policy sits on the gateway target, hidden from the agent, which can't lift it.
