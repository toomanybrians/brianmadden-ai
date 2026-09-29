---
title: Implementing synthetic monitoring using Amazon Nova Act
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/implementing-synthetic-monitoring-using-amazon-nova-act/
author: Sarath Krishnan
date_published: '2026-09-28'
date_captured: '2026-09-29'
ingest_method: feed
model: claude-sonnet-5
---

# Implementing synthetic monitoring using Amazon Nova Act

## Insights

- AWS positions Amazon Nova Act (a multimodal LLM that reads UI screenshots) as a replacement for selector-based browser automation (Selenium/Playwright), arguing vision-based agents adapt to UI changes that would break traditional DOM-locator scripts.
- Claimed accuracy: "over 90% accuracy on browser workflows" in early enterprise customer use, but AWS itself flags this isn't perfect — recommends teams test on their own sites and build retry logic for failed adaptations, and notes single-attempt execution can still produce false alerts.
- Architecture combines Nova Act with Amazon Bedrock AgentCore Runtime (serverless execution, session isolation) and AgentCore Browser tool (isolated remote browser per test run via Firecracker microVMs), scheduled via EventBridge and alerted via SNS — explicitly framed as eliminating browser-farm/server management overhead.
- Cost structure is usage-based across five components (runtime invocations, browser sessions, Nova Act inference calls, scheduler invocations, notifications); a sample 6-step ecommerce journey run every 5 minutes generates ~8,640 invocations and ~207,360 Nova Act action/assertion calls per month.
- Security model relies on ephemeral, one-session-per-microVM isolation with full memory sanitization by default (no persistent cookies/cache) to prevent state-leakage false positives — persistent browser profiles exist but are explicitly discouraged for synthetic monitoring use.
- Explicit guidance against over-monitoring: recommends starting with 3-5 critical journeys and validating meaningful outcomes rather than exhaustive page/element coverage, to avoid alert fatigue and false positives from overly granular assertions.

## Quote

> Even small UI changes can break tests and require constant maintenance.
