---
title: How U.S. Hunger connects leaders and data using Amazon Quick
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/how-u-s-hunger-connects-leaders-and-data-using-amazon-quick/
author: Rick Whitted
date_published: '2026-10-21'
date_captured: '2026-10-22'
ingest_method: feed
model: claude-sonnet-5
---

# How U.S. Hunger connects leaders and data using Amazon Quick

## Insights

- U.S. Hunger (nonprofit, 500% growth over four years vs. 15-20% headcount growth) uses Amazon Quick to let non-technical leaders (CEO, COO, chief of staff) query organizational data directly rather than filing requests with the technology team — a self-service BI/analytics pattern enabled by generative AI chat interfaces.
- Technical architecture: SQL Server data from a proprietary platform (Impact Manager) refreshes nightly into Quick's in-memory engine (SPICE) via scheduled jobs; planned expansion adds Boomi integration pulling NetSuite, Salesforce, Paylocity, and other systems into Amazon Redshift, which then feeds Quick.
- "Quick Spaces" (shared workspaces with documents, KPI definitions, and analyses) is described as the turning point that made the tool feel enterprise-grade rather than personal — enabling leaders to work from shared definitions and pick up on each other's financial models/framing without scheduling meetings.
- Use cases spanning the org: drafting/refining reporting instructions via AI chat with inline commenting, research via "Quick Research" (with version history) to connect policy questions to internal survey data, and financial planning using a Space containing a decade of audits/cash-flow documents for pattern comparison.
- Only 17 colleagues across leadership, tech, program, finance, and compliance have access — illustrating a lean-team deployment model rather than org-wide rollout.
- Strategic ambition beyond internal use: turning the nonprofit's proprietary applicant data (300,000+ records) into a "national hunger-data resource" for researchers/public access plus a paid enterprise data offering to fund the mission, partly motivated by the USDA ending its Household Food Security Reports.
- CEO frames the human-AI relationship explicitly: subject-matter experts still supply context, check AI-generated answers, and make final decisions — positioned as augmentation, not automation.

## Quote

> "This is not about bringing humans into the AI loop. It's about bringing AI into the human loop." — Rick Whitted
