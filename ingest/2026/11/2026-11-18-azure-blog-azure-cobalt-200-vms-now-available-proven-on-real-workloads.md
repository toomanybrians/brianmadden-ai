---
title: Azure Cobalt 200 VMs now available, proven on real workloads and built for
  the agentic era
source: Azure Blog
source_id: azure-blog
source_url: https://azure.microsoft.com/en-us/blog/azure-cobalt-200-vms-now-available-proven-on-real-workloads-and-built-for-the-agentic-era/
author: Arun Kishan
date_published: '2026-11-17'
date_captured: '2026-11-18'
ingest_method: feed
model: claude-sonnet-5
---

# Azure Cobalt 200 VMs now available, proven on real workloads and built for the agentic era

## Insights

- Microsoft positions Cobalt 200 (Arm-based, custom silicon, TSMC 3nm, 132 Neoverse V3 cores) explicitly for "agentic AI workloads" — naming agent sandboxes, tool execution, file search, and code compilation as target use cases, not just generic cloud compute.
- Claimed performance gains over Cobalt 100 are workload-specific: up to 1.5x (web serving, AI agent tool execution), 1.6x (Java), 1.9x (database), and internally reported 1.3–4.15x on Microsoft's own chip-design (EDA) workloads — wide variance suggests benchmarks are workload-dependent rather than uniform.
- New VM families (Mpsv4 high-memory, Lpsv5 storage-optimized with up to 23TB local NVMe) are marketed partly around "vector search and agent memory stores" and "large-scale vector search for agentic AI" — signals Azure sees agent memory/retrieval infrastructure as a distinct, growing compute category.
- Customer quotes (OpenAI/ChatGPT, Databricks, Snowflake, Amadeus, InMobi) all report concrete throughput/latency gains from moving workloads to Arm-based Cobalt chips, reinforcing an industry-wide shift toward custom Arm silicon for cloud-scale AI and data workloads, not just Microsoft's internal infra.
- Two selectable processor modes (Deterministic 3.2GHz vs. Opportunistic up to 3.6GHz) let customers trade predictability for peak throughput — a tuning knob aimed at latency-sensitive agentic/transactional workloads vs. clustered/distributed-systems consistency needs.
- Microsoft frames this as a "systems approach" co-optimizing silicon, networking, power, and rack design — underscoring that hyperscaler competitiveness in the agentic-AI era is increasingly about vertically integrated infrastructure stacks, not just chip specs.

## Quote

> Cobalt has helped us sustain ChatGPT's growth... We saw higher throughput and lower latency on Cobalt 200. — Vadim Filanovsky, OpenAI
