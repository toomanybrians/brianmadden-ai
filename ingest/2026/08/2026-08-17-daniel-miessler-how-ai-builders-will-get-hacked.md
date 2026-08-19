---
title: How AI Builders Will Get Hacked
source: Daniel Miessler
source_id: daniel-miessler
source_url: https://danielmiessler.com/blog/how-ai-builders-get-hacked?utm_source=rss&utm_medium=feed&utm_campaign=website
author: daniel@danielmiessler.com (Daniel Miessler)
date_published: '2026-08-17'
date_captured: '2026-08-17'
ingest_method: feed
model: claude-sonnet-5
---

# How AI Builders Will Get Hacked

## Insights

- Miessler argues the dominant future hacking vector for AI builders won't be sophisticated exploits, but simple negligence: fast-moving builders leaving forgotten, unpatched, or misconfigured deployments exposed on the internet.
- The speed of AI-assisted building is itself the risk — people now build and tear down applications within minutes or hours, increasing the odds that something vulnerable stays publicly accessible without anyone tracking it.
- He recommends a two-part defense: (1) a continuously maintained inventory of every public-facing asset a builder/company has deployed, and (2) automated, continuous basic security testing against that inventory (checking for known-vulnerable stack components and properly functioning authentication).
- As AI itself gets better at security testing/attacking, exploitation of these unmonitored exposures will happen faster, raising the urgency of automated defense over manual, periodic review.
- Provides a ready-to-use prompt for having an AI system build the asset-inventory and security-testing infrastructure, including continuous cloud-based execution, securing the testing system itself, and alerting on issues.
- Frames this as advice for both individual "personal AI builders" and companies, treating the risk as scaling with how easy AI has made rapid deployment.

## Quote

> I think the main way personal AI builders (and companies) will get hacked in the coming years will be building too fast and leaving stuff dangling on the internet.
