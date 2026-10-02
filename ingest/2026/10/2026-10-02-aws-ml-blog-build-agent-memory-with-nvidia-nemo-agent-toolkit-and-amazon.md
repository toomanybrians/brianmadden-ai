---
title: Build agent memory with NVIDIA NeMo Agent Toolkit and Amazon S3 Vectors
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-agent-memory-with-nvidia-nemo-agent-toolkit-and-amazon-s3-vectors/
author: Venkata Sistla
date_published: '2026-10-01'
date_captured: '2026-10-02'
ingest_method: feed
model: claude-sonnet-5
---

# Build agent memory with NVIDIA NeMo Agent Toolkit and Amazon S3 Vectors

## Insights

- NVIDIA's NeMo Agent Toolkit (NAT) is a framework-agnostic open-source layer (works with Strands, LangChain, LlamaIndex, CrewAI) offering orchestration, profiling, evaluation, and automated hyperparameter optimization for agent systems — positioning memory as one piece of a broader agent-ops stack rather than a standalone feature.
- NAT's memory subsystem is pluggable (MemoryEditor interface); AWS built a custom provider using Amazon S3 Vectors rather than relying on NAT's built-in options (Mem0, MemMachine, Redis, Zep), citing need for elastic scale, strong write consistency, and cost efficiency (pay only for storage/writes/queries, no idle compute, up to 2 billion vectors per index).
- An "auto_memory_agent" wrapper lets agents capture and retrieve memory automatically without the LLM needing to explicitly call memory tools — reducing prompt/tool-design burden for persistent context.
- The architecture supports multi-agent coordination via shared metadata (team_id, agent_id, is_shared) within a single vector index, plus a memory consolidation pattern where an LLM periodically distills accumulated "episodic" memories into generalized "semantic" knowledge to keep retrieval efficient.
- AWS frames performance benefits (improved groundedness, reduced token usage, reduced duplicate agent work, modest latency increase) explicitly as "directional expectations, not benchmarked measurements" — a notable admission of unverified claims in vendor content.
- Deployment guidance favors Amazon EKS for teams wanting full operational control (scaling, networking, IAM via IRSA), while noting Amazon Bedrock AgentCore as a fully managed alternative — signaling AWS is positioning infrastructure choice as a deliberate trade-off, not a default.
- Responsible-use notes flag real risks: avoid storing PII in memory metadata, redact/tokenize sensitive fields before embedding, and use per-tenant indexes with least-privilege IAM for isolation.

## Quote

> These are directional expectations, not benchmarked measurements.
