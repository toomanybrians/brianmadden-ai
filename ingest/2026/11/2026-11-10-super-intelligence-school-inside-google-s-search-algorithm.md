---
title: Inside Google's Search Algorithm
source: Super Intelligence School
source_id: super-intelligence-school
source_url: https://sischool.substack.com/p/inside-googles-search-algorithm
author: Super Intelligence School
date_published: '2026-11-09'
date_captured: '2026-11-10'
ingest_method: feed
model: claude-sonnet-5
---

# Inside Google's Search Algorithm

## Insights

- Google's internal "Content Warehouse" documentation, made public in 2024, reportedly contains approximately 2,596 modules and 14,014 attributes describing aspects of how search ranking works internally.
- The documentation includes fields covering website authority, document quality, semantic embeddings, link data, historical search interaction data, and ranking adjustments — suggesting a far more granular ranking system than the commonly cited "200 ranking factors."
- A field called `siteFocusScore` appears to encode site-level topical/subject focus, implying Google tracks how narrowly or broadly a site is scoped on a given subject.
- `contentEffort` is described as tied to an LLM-based estimation of the effort behind a piece of content — indicating Google may use AI models to assess how much work went into producing a page.
- `lastLongestClicks` is tied to "NavBoost," a system that appears to use historical user interaction/click data (e.g., dwell time, click behavior) as a ranking signal.

## Quote

> contentEffort points to an LLM-based effort estimation.
