---
title: How IskayPet unified corporate knowledge with Amazon Bedrock Managed Knowledge
  Bases
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-iskaypet-unified-corporate-knowledge-with-amazon-bedrock-managed-knowledge-bases/
author: Daniel Martinez Rubio
date_published: '2026-10-22'
date_captured: '2026-10-23'
ingest_method: feed
model: claude-sonnet-5
---

# How IskayPet unified corporate knowledge with Amazon Bedrock Managed Knowledge Bases

## Insights

- IskayPet replaced manual search across hundreds of SharePoint documents (4,500+ employees, 4 languages, 3 countries) with a RAG assistant built on Amazon Bedrock Managed Knowledge Bases, avoiding self-managed vector databases, embedding pipelines, and ingestion jobs.
- Architecture choice: a dedicated knowledge base per assistant/domain (rather than one shared base with metadata filtering) to keep business areas isolated end-to-end and let each be tuned independently; scaling to a new area/country means adding an assistant, not re-architecting.
- Access control reuses existing SharePoint permissions natively at two levels — which assistants a user can see, and which documents inform an answer at retrieval time — so answers to the same question legitimately differ by user, and permission changes in SharePoint propagate without app changes.
- Retrieval tuning details: hybrid semantic+keyword (BM25) search, managed reranking, 25 passages retrieved then deduped down to up to 15 injected into the prompt (the main cost driver via input tokens), and native RAG evaluation using real thumbs-up/down feedback as an ongoing eval set.
- The entire solution — frontend, AWS architecture, infrastructure provisioning — was built by a small team using Kiro (agentic dev environment) paired with Claude Haiku 4.5, which the authors credit for speed from concept to production.
- Reported results after ~2 months in production: time-to-answer dropped from 3–5 minutes to ~7 seconds (~95% less search time), with the system expected to handle ~100,000 queries/month across all business areas.

## Quote

> The assistant doesn't grant access to anything new: It only makes it more straightforward to query documents an employee could already open.
