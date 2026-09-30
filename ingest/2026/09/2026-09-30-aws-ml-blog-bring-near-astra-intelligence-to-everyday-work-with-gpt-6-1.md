---
title: Bring near-Astra intelligence to everyday work with GPT-6.1 Sol on Amazon Bedrock
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/bring-near-astra-intelligence-to-everyday-work-with-gpt-6-1-sol-on-amazon-bedrock/
author: Tanvi Girinath
date_published: '2026-09-29'
date_captured: '2026-09-30'
ingest_method: feed
model: claude-sonnet-5
---

# Bring near-Astra intelligence to everyday work with GPT-6.1 Sol on Amazon Bedrock

## Insights

- GPT-6.1 Sol is now generally available on Amazon Bedrock, positioned as a mid-tier upgrade to GPT-6 Sol, with OpenAI claiming it approaches ("near-Astra") the capability of the top-tier GPT-6 Astra model at lower cost.
- OpenAI's benchmark claim: GPT-6.1 Sol matches GPT-6 Astra on the DeepSWE v1.1 coding benchmark at roughly one-fifth the cost per task, and beats GPT-6 Sol's best prior score by 6.4 points while using less reasoning effort.
- The framing emphasizes agent task economics explicitly: total cost of an agentic task is a function of both per-token price and reasoning quality (which determines how many steps/interactions/errors occur before task completion), not just model pricing.
- Reported improvements target agent reliability behaviors specifically — recognizing failed tool calls, restricted actions, missing information, and communicating limitations rather than proceeding on incomplete data — framed as enabling human-in-the-loop intervention at consequential decision points.
- Deployment/governance details for enterprise buyers: IAM-based access control, CloudTrail audit logging, VPC/PrivateLink network isolation, hardware-isolated inference with "zero-operator access" (AWS staff can't see prompts/completions), no training on customer inference data, and no requirement to opt into data-sharing with OpenAI.
- Abuse-detection carve-out: traffic flagged by automated classifiers is retained by AWS up to 30 days for programmatic processing, though customers can request zero data retention via their AWS account team.

## Quote

> GPT-6.1 Sol brings stronger reasoning to agentic work at a fraction of the cost per task, so your agents reach the right answer in fewer steps.
