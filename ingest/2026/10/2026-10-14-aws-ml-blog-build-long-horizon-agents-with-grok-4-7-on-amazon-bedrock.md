---
title: Build long-horizon agents with Grok 4.7 on Amazon Bedrock
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/build-long-horizon-agents-with-grok-4-7-on-amazon-bedrock/
author: Suheel Farooq
date_published: '2026-10-13'
date_captured: '2026-10-14'
ingest_method: feed
model: claude-sonnet-5
---

# Build long-horizon agents with Grok 4.7 on Amazon Bedrock

## Insights

- Grok 4.7 is now available on Amazon Bedrock with a configurable "reasoning effort" parameter (low/medium/high/xhigh) that trades off token cost against task accuracy on a per-request basis, not just per-agent.
- In AWS's own evaluation (72 tool-calling agent runs across three designed-to-require-search tasks), xhigh reasoning hit 18/18 correct, while low reasoning hit 15/18 using roughly one-eighth the output tokens — framed as a usable cost/accuracy dial rather than a single "best" setting.
- Reasoning effort changed how much the model deliberated, not how much it explored: tool-call counts stayed flat (~17-19 per run) across all effort levels, while output tokens rose from ~1,184 (low) to ~9,147 (xhigh).
- The piece argues extra reasoning effort matters most for tasks requiring weighing multiple candidate answers against each other (optimization, hypothesis testing, constraint satisfaction) rather than tasks with a single lookup/execution path.
- Vendor-reported benchmarks (from SpaceXAI/xAI) show Grok 4.7's largest gains over 4.6 concentrated in "sustained work" categories like multi-hour terminal tasks (20.3%→37.6%) and clinical/legal/coding agent benchmarks — not uniform across all categories.
- AWS recommends operational practices for production agents: monitor output-token/tool-call volume per effort level as a proxy quality signal, set effort differently for planning vs. mechanical sub-steps, and use separate routing profiles/service tiers to balance cost, latency, and data residency.

## Quote

> SpaceXAI trained Grok 4.7 to work longer on more difficult tasks and to know when to check its own work.
