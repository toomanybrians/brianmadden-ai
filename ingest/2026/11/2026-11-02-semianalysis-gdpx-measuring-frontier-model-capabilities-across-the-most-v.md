---
title: 'GDPx: Measuring Frontier Model Capabilities Across the Most Valuable Domains'
source: SemiAnalysis
source_id: semianalysis
source_url: https://newsletter.semianalysis.com/p/gdpx-measuring-frontier-model-capabilities
author: Max Kan
date_published: '2026-11-02'
date_captured: '2026-11-02'
ingest_method: feed
model: claude-sonnet-5
---

# GDPx: Measuring Frontier Model Capabilities Across the Most Valuable Domains

## Insights

- SemiAnalysis built GDPx, a new benchmark testing frontier AI models on 11 high-value domains (chip design, cybersecurity, biology, finance, legal, quant trading, recursive self-improvement, hardware design, materials science, alignment, software engineering) — deliberately excluding broad-economy sectors like government, real estate, and insurance, on the thesis that AI value will concentrate rather than diffuse evenly.
- Even the best-scoring model achieves only ~12% on GDPx, and finance/legal tasks are hard enough that every model scores 0% under binary grading — positioned as evidence that "frontier-level" capability is still far from saturating real expert work.
- Models show significant "spikiness": no single model dominates across domains (e.g., Opus 5.5 leads quant trading/hardware/chip design, Gemini 4 Carbon leads biology and edges software engineering, GPT-6 Astra wins RSI and materials science), and safety classifiers measurably suppress scores in cyber, biology, and alignment for some models.
- The piece argues OpenAI's GDPval (from Sept 2025) is now "woefully inadequate" because it predates agentic AI — its tasks are static, single-shot, context-spoonfed, and lack realistic work environments (no need to search through files, data rooms, or systems to gather context), which is described as the central missing ingredient in evaluating real work.
- GDPx tasks instead embed models in large simulated realistic environments built from real transactions/vulnerabilities/engineering projects (e.g., a ~4,000-file M&A deal room, live cyber infrastructure built on real zero-days, CAD/CAM/PCB software environments, actual chip tapeout data) sourced via partnerships with 14 specialized RL-environment startups.
- Detailed finance and chip-design case studies show models failing in enterprise-relevant ways: misjudging which documents are authoritative, missing second-order financial implications (contingent liabilities, tax triggers), failing basic accrual-accounting mechanics, and in hardware tasks producing designs that aren't manufacturable or don't preserve functional/parametric relationships under revision.

## Quote

> GDPx is a true frontier-level benchmark: even the best model scores just 12%.
