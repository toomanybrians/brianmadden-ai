---
title: The $899 Mac mini comes with 16 GB of memory, less than I'd start a new agent
  computer with. Buy the memory and storage you need, without overpaying or falling
  short.
source: Nate’s Substack
source_id: nate-s-substack
source_url: https://natesnewsletter.substack.com/p/computer-for-ai-agents
author: Nate
date_published: '2026-10-20'
date_captured: '2026-10-21'
ingest_method: feed
model: claude-sonnet-5
---

# The $899 Mac mini comes with 16 GB of memory, less than I'd start a new agent computer with. Buy the memory and storage you need, without overpaying or falling short.

## Insights

- AI agents running on a personal computer act as concurrent users, consuming memory, processes, and disk space alongside the human owner — framed as "roommates" with no established house rules.
- Hardware upgrades (faster chip, more RAM, bigger drive) don't solve the underlying problem: orphaned dev servers, unprioritized concurrent jobs, and accumulating per-experiment environments that never get cleaned up.
- Recommends diagnosing actual agent resource behavior first — what gets left running, what gets left behind, and how much of that is still useful work — before buying new hardware.
- Proposes a practical management stack: a read-only audit prompt, mandatory job-end cleanup (save results, close leftover servers), staged load-testing of concurrent heavy jobs, and offloading background queues to a repurposed old machine (accessible remotely via Tailscale).
- Tools referenced for implementation: Ollama, LM Studio, Docker Desktop, Tailscale.
- Positions the real decision as a cost comparison between keeping, reconfiguring, moving, or replacing a machine, based on first-year cost — not simply "buy more power."

## Quote

> Your agents have become roommates, and most of us never worked out the house rules.
