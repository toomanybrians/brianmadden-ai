---
title: How Octave built a secure multi-tenant AI foundation on Amazon Bedrock
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-octave-built-a-secure-multi-tenant-ai-foundation-on-amazon-bedrock/
author: Urvish Saraiya
date_published: '2026-10-20'
date_captured: '2026-10-21'
ingest_method: feed
model: claude-sonnet-5
---

# How Octave built a secure multi-tenant AI foundation on Amazon Bedrock

## Insights

- Octave (quality management SaaS for 14,000+ customers in medical devices, pharma, food manufacturing) chose to build a horizontal AI foundation before shipping any single AI feature, betting that dozens of planned use cases would otherwise each require rebuilding isolation and retrieval infrastructure from scratch.
- The core design tension was reconciling AI's need to read across a customer's full document history with strict per-tenant data isolation requirements — solved by pushing isolation into runtime (AgentCore's per-session microVMs, per-user OAuth token vaults) rather than relying on application-code checks.
- Embedding model selection (Cohere Embed v4) was evaluated against Octave's own corpus rather than public benchmarks, and testing found 512-dimension embeddings held accuracy while cutting OpenSearch storage ~66% versus the 1,536 default — a tradeoff the team says no public leaderboard would have surfaced.
- Untrusted ingested content (email attachments, scanned PDFs) was treated as a defense-in-depth problem: Bedrock Guardrails applied at three pipeline points, input tagging to mark attachment content as data not instruction, PII masking, and sandboxed extraction with no network egress — rather than attempting to filter malicious content outright.
- The AI system (Complaint Triage Assistant) is scoped to surface historical context and precedent only; the human handler still makes the triage decision — a deliberate line Octave did not automate past, attributed to regulatory accountability.
- Claimed results after reported first production cycle: 50% reduction in deployment time per new AI use case, development cycles shrinking "from months to weeks," and semantic search shipping two quarters ahead of schedule — these are vendor/customer-reported figures, not independently verified.

## Quote

> A quality handler still makes the call. In an industry where that call carries regulatory weight, that boundary shaped what got automated.
