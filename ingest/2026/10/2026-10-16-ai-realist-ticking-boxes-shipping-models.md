---
title: Ticking Boxes, Shipping Models
source: The AI Realist
source_id: ai-realist
source_url: https://www.airealist.ai/p/ticking-boxes-shipping-models
author: Julien Simon
date_published: '2026-10-15'
date_captured: '2026-10-16'
ingest_method: feed
model: claude-sonnet-5
---

# Ticking Boxes, Shipping Models

## Insights

- Doctolib's patient-facing language ("encrypted end to end and hosted in France") describes only storage and transit; it never addresses the moment a US-supplied model (Microsoft, Google, or Anthropic) must decrypt and read patient data to generate a response — a gap the piece calls "compliance theater" rather than a violation.
- French and EU health-data regulations (HDS certification, EEA storage rules) don't actually require immunity from US law or SecNumCloud qualification for private companies — only for the State itself, which took nearly six years to migrate its own Health Data Hub off Azure.
- The regulatory bar keeps moving: the 2018 HDS standard had no location requirement, the 2024/2026 standard added an EEA storage rule, and stronger "European-sovereignty requirements" are promised by 2027 with no specifics yet — meaning compliant architectures today may require rebuilding later.
- Closed AI models (Anthropic, Microsoft, Google) offer no guaranteed EU-only inference routing in many cases (e.g., no Paris-only Bedrock option for Claude Opus), and Anthropic isn't on the EU-US Data Privacy Framework list, unlike Microsoft, Google, and AWS.
- Doctolib's announced pivot to "sovereign" open-weight models (with Nvidia's minority investment) addresses who reads the data but not the underlying chip dependency — open-weight models still largely run on Nvidia hardware, so sovereignty claims may just shift reliance from a US software vendor to a US chip vendor.
- The piece frames this as illustrative of a broader "Builder Tax": European cloud alternatives (e.g., Scaleway with ~60 services vs. 200+ at hyperscalers) lack feature parity, so companies building "sovereign" infrastructure spend engineering time closing gaps rather than building product.

## Quote

> "Doctolib hosts all health data in the European Union and the UK [...] under its sole control. The same applies to its AI models."
