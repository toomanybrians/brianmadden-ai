---
title: The Huawei-DeepSeek Symbiosis
source: SemiAnalysis
source_id: semianalysis
source_url: https://newsletter.semianalysis.com/p/huawei-deepseek
author: Bryan Shan
date_published: '2026-10-21'
date_captured: '2026-10-22'
ingest_method: feed
model: claude-sonnet-5
---

# The Huawei-DeepSeek Symbiosis

## Insights

- DeepSeek and Huawei have a mutually dependent relationship: Huawei has domestic AI chips (Ascend) but no frontier model lab to prove them out, while DeepSeek has models but limited access to Nvidia compute — each fills the other's gap, formalized through DeepSeek's September 2025 release of Ascend support across six of its kernel/compiler repos (TileLang, DeepGEMM, DeepEP, TileKernels, FlashMLA, DeepSelect).
- The piece frames this as becoming structural rather than opportunistic: it predicts that by 2027-2028 DeepSeek will likely run primarily on Huawei's stack, driven by both external pressure (US restrictions) and internal pressure (China's push for a fully domestic AI chip ecosystem).
- Technical benchmarking shows Huawei's Ascend 950PR hardware is "~5 years behind" Nvidia's A100 in raw capability, but its software/compiler stack (CANN) is described as "right at the frontier" — Huawei's own kernels hit 99.7% of theoretical ceiling on BF16 GEMM, rivaling DeepSeek's own DeepGEMM optimizations.
- Collaboration is bidirectional at the engineering level: Huawei's chip architecture (e.g., accumulator/buffer design) is forcing DeepSeek to redesign core model execution logic (attention computation, KV-cache memory layout), while DeepSeek's workload needs are shaping Huawei's firmware roadmap (e.g., planned fixes for HBM contention in its DeepEP port).
- A quoted/unverified DeepSeek investor transcript claims it currently takes four Huawei accelerator cards to match one Nvidia card, and that Huawei hardware lags roughly two years in time-to-market, though the software ecosystem gap is closing fast.
- The article flags a risk: this deep, bespoke DeepSeek-Huawei co-optimization may make Ascend hardware highly effective for DeepSeek specifically while leaving it poorly supported for other users/configurations (e.g., non-ARM/x86 host compatibility issues, missing CI, hardcoded dependencies).

## Quote

> It takes four Huawei accelerator cards to match one NVIDIA card, and Huawei is also roughly two years behind in bringing its hardware to market. — Liang Wenfeng
