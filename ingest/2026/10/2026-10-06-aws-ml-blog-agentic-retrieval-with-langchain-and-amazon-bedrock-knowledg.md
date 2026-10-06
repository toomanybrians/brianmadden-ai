---
title: Agentic retrieval with LangChain and Amazon Bedrock Knowledge Bases
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/agentic-retrieval-with-langchain-and-amazon-bedrock-knowledge-bases/
author: Manideep Reddy Gillela
date_published: '2026-10-05'
date_captured: '2026-10-06'
ingest_method: feed
model: claude-sonnet-5
---

# Agentic retrieval with LangChain and Amazon Bedrock Knowledge Bases

## Insights

- Standard RAG retrieval encodes a multi-part question into one embedding vector, which structurally can only approximate the "average" of several intents — demonstrated concretely: a 6-intent comparison question retrieved only 4 of 6 sub-intents at 5 results, requiring 10 results (19% of the corpus) to cover all 6, with duplication and waste.
- AWS's Bedrock Managed Knowledge Base now offers "agentic retrieval" (AgenticRetrieveStream API) that decomposes a complex question into sub-queries, runs retrieval per sub-query, judges whether evidence is sufficient, and re-plans/iterates if not — versus the single-shot Retrieve API.
- This is a managed/opaque service feature, not a LangChain retriever: it's exposed in langchain-aws as a standalone function (not fitting LangChain's synchronous BaseRetriever interface), requiring a RunnableLambda wrapper to use in a chain — a concrete integration friction point.
- Trace events reveal the planner's steps (SpeculativeRetrieval, Planning, Retrieval, FullDocumentExpansion, result) but the convenience helper function discards these traces; developers must call the raw boto3 API directly to inspect the actual query decomposition.
- Cited benchmark (AWS's own evaluation on MuSiQue, a multi-hop QA benchmark): agentic retrieval improved recall over single-shot retrieval, with largest gains on hardest multi-hop questions and under 5 points of gain on single-hop questions — i.e., decomposition only helps when there's something to decompose.
- Practical cost/latency tradeoffs are explicit: agentic retrieval costs more per call (multiple model invocations) and has higher latency; AWS's stated guidance is to route by query shape (cheap single-shot path for most traffic, planner reserved for multi-part/comparative/cross-knowledge-base questions) rather than defaulting to agentic for everything.

## Quote

> The limitation is structural: one vector cannot represent six intents, and there is no step in the process that asks whether the returned evidence is enough to answer the question.
