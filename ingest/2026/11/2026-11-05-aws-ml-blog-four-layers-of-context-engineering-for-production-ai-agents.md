---
title: 'Four layers of context engineering for production AI agents: How Deep Insight
  applies them in working code'
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/four-layers-of-context-engineering-for-production-ai-agents-how-deep-insight-applies-them-in-working-code/
author: Yoonseo Kim
date_published: '2026-11-04'
date_captured: '2026-11-05'
ingest_method: feed
model: claude-sonnet-5
---

# Four layers of context engineering for production AI agents: How Deep Insight applies them in working code

## Insights

- The piece frames "context engineering" as a four-layer discipline for production AI agents: architectural isolation (separate contexts per sub-agent), prompt-based output limits, filesystem externalization (pointers in context, data in files), and independent verification/safeguards — each layer compensating for gaps in the others.
- In the reference implementation (Deep Insight, an open-source multi-agent data analysis system on Strands Agents SDK + Bedrock AgentCore), combining a single write-and-execute tool cut per-script context tokens by ~95%, and on-demand skill loading shrank system prompt size by ~97%.
- A concrete architectural pattern: a Supervisor/Coordinator hierarchy shares only a minimal state object (last message, compressed "clues," a checklist, and a brief history log) between agents rather than full conversation history, keeping even the heaviest agent under 25K tokens.
- The filesystem is used as an inter-agent communication bus (e.g., all_results.txt, calculation_metadata.json, citations.json, audit_findings.json), letting agents hand off detailed work products without passing them through each other's context windows.
- Verification is treated as a distinct, necessary layer: a Validator independently re-executes Coder calculations against a tolerance threshold, and an Auditor cross-checks the final report against verified citations post-hoc, with limited automatic retries.
- Cost optimization is folded into context engineering: selective prompt/tool caching is applied per-agent based on call-frequency patterns, claimed to cut input token costs up to 90% on repeated calls; a SummarizingConversationManager serves as a last-resort overflow safeguard.

## Quote

> As the number of tokens in the context window increases, the model's ability to accurately recall information from that context decreases (Context rot).
