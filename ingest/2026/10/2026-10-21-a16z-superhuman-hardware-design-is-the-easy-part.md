---
title: Superhuman Hardware Design Is The Easy Part
source: a16z
source_id: a16z
source_url: https://www.a16z.news/p/superhuman-hardware-design-is-the
author: Christian Keil
date_published: '2026-10-20'
date_captured: '2026-10-21'
ingest_method: feed
model: claude-sonnet-5
---

# Superhuman Hardware Design Is The Easy Part

## Insights

- Frontier AI models are already generating CAD, custom PCB designs, and COTS part sourcing instructions, with benchmarks (CAD Arena, EE Bench, LuxoBench) showing steady improvement — but current output isn't yet "primetime" ready for real hardware engineering.
- The author frames hardware engineering as a 101-to-501 difficulty ladder: COTS part sourcing → custom part fabrication → complex assembly with stacked tolerances → external vendor coordination → mass-scale manufacturing — each level requires distinct skills AI must separately master.
- The core bottleneck is the "lossy" digital-to-physical interface: writing designs into atoms (CNC machining, assembly variability) and reading real-world data back into digital systems are both inherently hard, unlike pure digital design tasks.
- Real-world measurement is constrained by five factors: non-uniform/changing physical conditions, data sparsity, high cost of precise measurement, inherent process latency (e.g., thermal cycling can't be sped up indefinitely), and qualitative data (user comfort, preference) that resists quantification.
- Predicts AI will likely master hardware *design* soon, shifting the real bottleneck to design-for-manufacturing, testing, and iteration — stages requiring heavy physical-world interaction that are harder to compress.
- Expects increased demand for manufacturing/supply-chain infrastructure (machining, PCB fab, parts sourcing, testing software) as more people gain AI-assisted engineer-level design skills, plus AI labs needing to build "process knowledge" pipelines (akin to master machinists' tacit expertise) via real-world data collection, citing Periodic Labs' autonomous physical-experiment lab as a model.
- Argues that discovering end-user preferences may be the most irreducible step even for a superhuman hardware engineer — infinite design iteration doesn't tell you what customers actually want.

## Quote

> Superhuman hardware engineers are coming soon, perhaps very soon.
