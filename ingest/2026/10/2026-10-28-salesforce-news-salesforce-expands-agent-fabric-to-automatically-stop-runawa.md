---
title: Salesforce Expands Agent Fabric to Automatically Stop Runaway Costs and AI
  Agent Failures Before They Impact Customers
source: Salesforce News
source_id: salesforce-news
source_url: https://www.salesforce.com/news/stories/agent-fabric-catch-failures-control-ai-costs/
author: Salesforce News
date_published: '2026-10-27'
date_captured: '2026-10-28'
ingest_method: feed
model: claude-sonnet-5
---

# Salesforce Expands Agent Fabric to Automatically Stop Runaway Costs and AI Agent Failures Before They Impact Customers

## Insights

- Salesforce's Agent Fabric (its cross-platform AI "control plane") is adding Agent Evals and API Evals: automated test generation and continuous evaluation of agents, LLMs, and MCP servers in production against quality thresholds, with automated interventions (including an "Agent Kill Switch") when results fall short.
- New cost-control features — FinOps Dashboard, Model Wallet, and Cost Optimization Policies — give budget owners a unified view of AI spend and hard caps that block requests before exceeding budget; Salesforce claims up to 75% token-usage reduction via semantic caching, payload compression, and response trimming (based on test scenarios, not guaranteed production results).
- Stated rationale: agents can fail silently (wrong answers, runaway token costs) and fewer than half of organizations with agents reportedly evaluate them on live traffic; 96% of enterprises are said to run agents across more than one platform, increasing the governance burden.
- Discovery/governance is being extended beyond Salesforce's native platform support via a Custom Agent Scanner (for internal/behind-firewall/third-party environments) and Open Policies for Federated API Gateways (unifying policy enforcement across Azure, Apigee, and Kong gateways).
- Customer quotes (ASICS, Capita, GE Appliances, Newell Brands) frame the core enterprise pain point as lack of centralized visibility/ownership over agents built ad hoc across the organization, and the value proposition as being able to see, govern, and shut down agents centrally.
- Rollout is staggered: several features (Custom Agent Scanner, Agent Kill Switch base version, FinOps Dashboard, Model Wallet, Cost Optimization Policies, Open Policies for Gateways) are available now, while Agent Evals, API Evals, and the "Triggered" Kill Switch remain in beta until November 2026 with general availability targeted for January 2027.

## Quote

> "Enterprises can only scale agents as fast as they can keep them accurate and on budget." — Andrew Comstock, SVP & GM, MuleSoft & Agent Fabric
