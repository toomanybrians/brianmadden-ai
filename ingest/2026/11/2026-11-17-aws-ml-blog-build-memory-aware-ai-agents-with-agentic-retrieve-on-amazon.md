---
title: Build memory-aware AI agents with Agentic Retrieve on Amazon Bedrock Managed
  Knowledge Base
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-memory-aware-ai-agents-with-agentic-retrieve-on-amazon-bedrock-managed-knowledge-base/
author: Peng Yang
date_published: '2026-11-16'
date_captured: '2026-11-17'
ingest_method: feed
model: claude-sonnet-5
---

# Build memory-aware AI agents with Agentic Retrieve on Amazon Bedrock Managed Knowledge Base

## Insights

- AWS has added a `memoryConfiguration` option to Bedrock Managed Knowledge Base's `AgenticRetrieveStream` API, letting a single call combine document retrieval (with per-user ACL filtering) and conversational memory (via AgentCore memory) — previously applications had to build their own session store, fact-extraction pipeline, and relevance-injection logic.
- The retrieval "planner" autonomously decides when to query long-term memory and what to ask, rather than memory being injected unconditionally — e.g., it fetched a previously-stated office location to personalize a PTO policy answer in one traced example, but found nothing for a different user and returned a generic answer instead.
- Identity is split into two distinct claims from a verified Cognito ID token: email drives document-level access control (ACLs), while a stable, non-reassignable user ID (`sub`) drives memory isolation — conflating these (e.g., using a mutable/reassignable email for memory) risks one user inheriting another's history.
- Security is enforced at two layers: the knowledge base "fails closed" on ACL errors (returns fewer results, not more), and IAM condition keys scope memory read/write operations to the calling user's session tag as a defense-in-depth backstop against application bugs — demonstrated by a trace showing AccessDeniedException when one user's session attempted to bind to another's memory.
- Memory operations are explicitly "best-effort": failures surface in the trace but don't fail the whole request, and long-term fact extraction is asynchronous (observed ~81 seconds after a conversation turn in testing) — meaning newly stated facts aren't guaranteed to be retrievable in the immediate next conversation.
- Practical constraints noted: only one knowledge base retriever config and one memory namespace path per request (though up to five KBs and five metadata filters are allowed), stated conversation IDs must stay stable to avoid fragmenting summaries, and a full turn with ACLs plus memory took 4–10 seconds in AWS's own tests, driven mostly by planning iterations rather than memory lookups.

## Quote

> ACL-aware retrieval is filtering, not authorization.
