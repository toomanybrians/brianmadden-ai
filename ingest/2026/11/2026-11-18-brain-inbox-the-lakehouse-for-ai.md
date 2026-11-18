---
title: The Lakehouse for AI
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: ''
author: Tomasz Tunguz <blog@tomtunguz.com>
date_published: '2026-11-17'
date_captured: '2026-11-18'
ingest_method: email
model: claude-sonnet-5
---

# The Lakehouse for AI

## Insights

- Lance/LanceDB is positioned as a "lakehouse" data layer specifically built for AI training and inference workloads, distinct from traditional data stack tools, handling unstructured, multimodal data at massive scale.
- Production use cases cited span extreme scale: Exa stores 35PB across 100B web pages with sub-five-minute crawl-to-search latency; Adobe manages 40-50PB across 800K tables and 220B daily events.
- Companies describe adopting this format because existing data infrastructure couldn't simultaneously handle unstructured data, column appends, distributed reads, and ad-hoc SQL together (per Runway's CTO).
- NVIDIA's Cosmos team reportedly trains directly on Lance tables across tens of thousands of GPUs, suggesting the format is becoming load-bearing infrastructure for frontier-scale model training, not just storage.
- Adobe frames the architectural question as whether "AI-native data" needs separate infrastructure from the rest of the data stack, and answers no — same lakehouse, same governance contract.
- Business signal: LanceDB's revenue grew 10x year-over-year since its Series A, with open-source downloads reaching 120M+, and it just raised a $57.5M Series B from multiple VC firms including the author's firm.

## Quote

> "Where should the AI-native data live? Our answer is in the same lakehouse, under the same contract as everything else." — Adobe platform team
