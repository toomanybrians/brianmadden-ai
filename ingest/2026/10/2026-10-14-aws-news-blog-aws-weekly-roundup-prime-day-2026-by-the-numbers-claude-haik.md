---
title: 'AWS Weekly Roundup: Prime Day 2026 by the numbers, Claude Haiku 5.5, Amazon
  Nova 2.5 Sonic, and more (October 13, 2026)'
source: AWS News Blog
source_id: aws-news-blog
source_url: https://aws.amazon.com/blogs/aws/aws-weekly-roundup-prime-day-2026-by-the-numbers-claude-haiku-5-5-amazon-nova-2-5-sonic-and-more-october-13-2026/
author: Daniel Abib
date_published: '2026-10-13'
date_captured: '2026-10-14'
ingest_method: feed
model: claude-sonnet-5
---

# AWS Weekly Roundup: Prime Day 2026 by the numbers, Claude Haiku 5.5, Amazon Nova 2.5 Sonic, and more (October 13, 2026)

## Insights

- Claude Haiku 5.5 launched on Amazon Bedrock at ~75% lower cost than Haiku 4.5 and is the first Haiku model with "effort controls," letting developers tune cost against intelligence per task rather than fixing one setting for an entire workload; positioned to run as parallel subagents (routing, classification, small code edits) under an Opus model handling higher-level judgment.
- Amazon Nova 2.5 Sonic is a speech-to-speech voice model with improved reasoning, instruction-following, and tool-calling accuracy, lower latency, 7 languages, controllable turn-taking, and a 256K context window — aimed at multi-step voice tasks (e.g., an agent looking up an order, checking return eligibility, and initiating a return in one conversation). Pairs with the now-GA Strands Bidi Agents framework.
- Strands Box, a new open-source (Apache 2.0, developer preview) agent sandbox, combines OS-level containment with a policy language ("Dogwood") that can condition permissions on an agent's prior actions (e.g., rate-limiting specific actions over time) and keeps real credentials out of the agent's runtime environment via an egress gateway — a direct response to agents executing shell commands/APIs with less human approval.
- Amazon GuardDuty RDS Protection now analyzes query-level behavior (not just login anomalies) on Aurora/RDS PostgreSQL to detect data exfiltration and destruction, targeting the scenario where an attacker with valid stolen credentials generates queries indistinguishable from normal application traffic.
- AWS Continuum for Penetration Testing (public preview) moves security testing into the CI/CD pipeline as a deploy-time gate, surfacing severity/remediation guidance inline and automatically re-testing fixes, rather than running pentesting as a separate, delayed process.
- Postman's "Agent Mode" running on Amazon Bedrock is cited as serving 40 million developers, offered as a real-world example of an agentic feature operating at production scale rather than demo scale.

## Quote

> let the agent post to the incident channel, but no more than three times every 10 minutes
