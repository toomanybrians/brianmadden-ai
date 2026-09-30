---
title: Prompt engineering fundamentals for Amazon Quick
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/prompt-engineering-fundamentals-for-amazon-quick/
author: Daiquan Nkere
date_published: '2026-09-29'
date_captured: '2026-09-30'
ingest_method: feed
model: claude-sonnet-5
---

# Prompt engineering fundamentals for Amazon Quick

## Insights

- Positions prompt engineering as a distinct, learnable skill layer within Amazon Quick, with the claim that output quality difference comes from prompt structure, not underlying model capability.
- Introduces multiple named frameworks for different tasks: CRISPE (Context/Constraints, Role, Intent/Inputs, Steps/Scope, Perspective/Presentation, Evaluation criteria) for complex general prompts; RADAR for knowledge retrieval; ARCHITECT for configuring custom chat agents (mapped directly to agent-builder UI fields); QUEST for agent queries.
- Emphasizes few-shot examples (showing exact desired output format) as more reliable than descriptive instructions for getting consistent structured output.
- Describes a concrete enterprise use case — automating RFI (Request for Information) questionnaire processing from messy multi-tab Excel files into structured CSV — as a flow built using the CRISPE pattern, claimed to cut processing from hours to minutes.
- Frames prompt engineering as an organizational practice, not just individual skill: recommends building shared "prompt libraries," tracking metrics (iterations, time saved), and distributing effective prompts across teams.
- Notes that enterprise retrieval prompts benefit from explicit metadata (document names, space names, acronym definitions) to disambiguate internal jargon for the retrieval system.

## Quote

> The difference isn't the AI's capability. It's how you communicate your needs.
