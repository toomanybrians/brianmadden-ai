---
title: Rethinking access control for RAG with Amazon Quick and Amazon Bedrock
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/rethinking-access-control-for-rag-with-amazon-quick-and-amazon-bedrock/
author: Amit Choudhary
date_published: '2026-10-07'
date_captured: '2026-10-08'
ingest_method: feed
model: claude-sonnet-5
---

# Rethinking access control for RAG with Amazon Quick and Amazon Bedrock

## Insights

- Describes a two-stage ACL architecture for RAG systems (Amazon Quick, Bedrock Knowledge Bases): Stage 1 uses pre-synced ACL attributes stored in the vector index for fast candidate filtering; Stage 2 makes real-time API calls to the authoritative source (e.g., Google Drive) to verify permissions before passing content to the LLM.
- Frames the core enterprise RAG security problem as three distinct failure modes of the common "replicate-and-filter" approach: the AI system isn't the permissions source of truth, synced ACLs go stale between sync cycles (e.g., Confluence doesn't emit events on group membership changes), and connectors lag behind evolving data-source permission models (e.g., new SharePoint/Google Drive sharing mechanics).
- Real-time verification uses admin-provided service account credentials to generate user-specific access tokens via impersonation, checking live permissions rather than cached/replicated ACL data.
- Justifies keeping the cached pre-filtering stage on cost grounds — real-time API calls against every document in an index at query time would be prohibitively expensive at scale.
- Positions this alongside Bedrock Guardrails (content filtering, grounding/hallucination checks) as part of a broader "responsible AI" control layer, though the ACL mechanism is the post's substantive focus.
- Cites Mondelēz International (35,000+ employees, four regions) as a customer reference for the access-control evaluation and rollout.

## Quote

> A single unauthorized document surfaced in an AI response could expose confidential strategy documents, unreleased financial data, or sensitive HR information.
