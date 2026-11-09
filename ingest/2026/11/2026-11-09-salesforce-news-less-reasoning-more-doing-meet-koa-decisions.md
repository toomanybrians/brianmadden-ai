---
title: Less Reasoning. More Doing. Meet Koa Decisions.
source: Salesforce News
source_id: salesforce-news
source_url: https://www.salesforce.com/news/stories/koa-decisions-salesforce-decision-models/
author: Darvish Shadravan
date_published: '2026-11-06'
date_captured: '2026-11-09'
ingest_method: feed
model: claude-sonnet-5
---

# Less Reasoning. More Doing. Meet Koa Decisions.

## Insights

- Salesforce is positioning "decision models" as a distinct category from LLMs: narrow models that return a single choice (option/yes-no/score) rather than generated text, intended to offload routing/classification work that doesn't need full reasoning.
- Koa Decisions is a successor to Salesforce's existing HyperClassifier (which already routes Agentforce requests), built by fine-tuning Google's open-weight Gemma model with Salesforce's own training techniques, and adding multimodal (image/audio) input support.
- Salesforce cites a benchmark of ~26ms for its decision model vs. ~1.4 seconds for a general-purpose LLM on the same routing task, framing speed/cost efficiency as the core value proposition.
- Planned expansion goes beyond chat routing into Flows, Apex, and prompt templates for builders, plus a developer API — suggesting Salesforce wants decision models embedded as infrastructure across its platform, not just a chatbot feature.
- Claimed workflow advantage over traditional ML classifiers: adding a new category (e.g., "Returns") can work immediately without retraining, versus months-long cycles for custom predictive models — positioned as a build-speed/agility story.
- This is explicitly framed as part of an industry trend ("decision models are having a moment"), naming competitors TypeSafe AI's Jev and OpenAI's Decisions API as parallel entrants in the same category within weeks of each other.
- Koa Decisions joins a broader "Koa" family at Salesforce that also includes a separate reasoning model co-built with NVIDIA, indicating a deliberate split in Salesforce's model portfolio between fast-decision and deep-reasoning models.

## Quote

> A decision model reads the whole request at once and produces its answer in one step.
