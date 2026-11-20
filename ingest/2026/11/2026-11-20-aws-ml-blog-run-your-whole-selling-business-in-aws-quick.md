---
title: Run your whole selling business in AWS Quick
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/run-your-whole-selling-business-in-aws-quick/
author: Josh Anderson
date_published: '2026-11-19'
date_captured: '2026-11-20'
ingest_method: feed
model: claude-sonnet-5
---

# Run your whole selling business in AWS Quick

## Insights

- AWS Quick (an AI business assistant) now integrates with a new "Selling Partner plugin" that connects to live Amazon Seller Central data (listings, inventory, sales) via one sign-in, rather than requiring manual export/reconciliation of reports.
- Permissions are granular: sellers grant None/View/Edit access per data category rather than all-or-nothing, which is framed as a trust/adoption mechanism for AI agents touching business data.
- AWS explicitly states seller data is not used to train models and stays within the seller's chosen AWS Region — a direct response to enterprise data-governance concerns about agentic AI tools.
- The tool is positioned as synthesis/decision layer across fragmented data sources (Brand Analytics, ad reports, inventory health, other storefronts, email, accounting) rather than another dashboard to check.
- Demonstrated agent use cases (inventory launch planning, post-launch diagnostic health checks) show the system doing causal diagnosis (e.g., distinguishing traffic vs. conversion problems) and flagging low-confidence conclusions, including an explicit limit: it labels fee-adjusted margin rather than presenting it as true gross margin without cost-of-goods data.
- Sellers can build custom agents from plain-language descriptions in minutes, suggesting a broader trend toward self-service agent creation without coding, demoed live by a customer (Proof Culture) who said connecting data, not the AI itself, was the historically hard part.

## Quote

> The hard part was never the AI. The hard part was getting my selling data into it. — Richard Brown, Proof Culture
