---
title: Forecasting space weather risks on power grids
source: Microsoft Research Blog
source_id: microsoft-research-blog
source_url: https://www.microsoft.com/en-us/research/blog/forecasting-space-weather-risks-on-power-grids/
author: Rohan Kannan
date_published: '2026-09-30'
date_captured: '2026-10-01'
ingest_method: feed
model: claude-sonnet-5
---

# Forecasting space weather risks on power grids

## Insights

- A Microsoft Research intern project built an end-to-end ML pipeline that forecasts geomagnetic storm risk for all 66,935 continental US substations, 30-60 minutes ahead, by combining solar-wind data, physics-based indices (AE, Dst), and local geology/grid data.
- The system used a network of 50 AI agents to explore features, validation strategies, and model configurations during development — an example of AI being used to build the research pipeline itself, not just the end product.
- Performance was uneven across event severity: 76.5% detection for major events, 81.2% for severe events, but only 64.1% for extreme events, with false-alarm rates rising alongside severity — a real precision/recall tradeoff disclosed openly rather than glossed over.
- The gradient-boosting model beat the long-standing Burton equation (a classic empirical model) on only 62.2% of peak-activity hours — a modest, not overwhelming, improvement over existing physics-based methods.
- Full inference across all 66,935 substations runs in ~333 milliseconds, enabling rapid scenario testing, but the authors are explicit that further validation with utility partners and real operational data is needed before any deployment.
- Framed as a research demonstration, not an operational tool — a grid operator "closer analysis" aid, not an automated control decision, with future work focused on longer forecast horizons, international scaling, and asset-level granularity.

## Quote

> Further validation with utilities and operational data would be needed before the system could be used in grid operations.
