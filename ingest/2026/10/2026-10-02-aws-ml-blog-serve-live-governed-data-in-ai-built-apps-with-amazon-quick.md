---
title: Serve live, governed data in AI-built apps with Amazon Quick
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/serve-live-governed-data-in-ai-built-apps-with-amazon-quick/
author: Wei Kuo
date_published: '2026-10-01'
date_captured: '2026-10-02'
ingest_method: feed
model: claude-sonnet-5
---

# Serve live, governed data in AI-built apps with Amazon Quick

## Insights

- Amazon Quick Apps previously baked in business-intelligence data as static snapshots at build time; the new "Live Data in Apps" feature lets AI-built apps re-run SQL queries live against governed QuickSight datasets every time a user opens them, rather than showing stale figures frozen at publish.
- Security/governance is enforced per-viewer, not per-app: queries execute under the identity of whoever is viewing, so existing row-level and column-level security rules apply automatically, and two users with different data access see different results in the same app.
- The build workflow is natural-language driven — a business user describes the app, an agent discovers relevant datasets, writes the SQL, and requires explicit per-dataset consent from both the builder and, later, each new viewer before querying live data.
- Technical constraints exist: only SPICE or Direct Query datasets from a single data source can be combined in one app, large query results trigger "narrow the query" errors instead of silent truncation, and users without row-level access simply can't get the app to build.
- The framing positions this as replacing manual, recurring reporting labor (someone pulling data, charting it, pasting into Slack weekly) with self-service apps non-technical "business operations owners" can build and share without IT/DevOps involvement.
- Access requires a paid tier (minimum "Reader Pro/Professional" role) and authenticated Quick users only — no anonymous or public access to apps using live datasets.

## Quote

> Data authority stays in one place. The Quick Sight query engine enforces authorization against each viewer's identity.
