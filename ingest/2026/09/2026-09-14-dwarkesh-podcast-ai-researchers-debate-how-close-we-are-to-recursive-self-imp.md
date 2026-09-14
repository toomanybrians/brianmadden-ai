---
title: AI researchers debate how close we are to recursive self-improvement
source: Dwarkesh Podcast
source_id: dwarkesh-podcast
source_url: https://www.dwarkesh.com/p/john-beren-charlie
author: Dwarkesh Patel
date_published: '2026-09-11'
date_captured: '2026-09-14'
ingest_method: feed
model: claude-sonnet-5
---

# AI researchers debate how close we are to recursive self-improvement

## Insights

- Three researchers debate why AI might *not* reach dramatic self-improvement by 2036: possible failure modes include a persistent "sim-to-real" generalization gap (an AI version of Moravec's paradox — hard problems solved, but generalization to messy reality stalls), an inability of models to learn to propose their own objectives without going off the rails, or heavy regulation.
- A recurring framing: research tasks split into "cumulative" ones (like RSI itself, where each discovery — attention, MoE, GRPO — gets permanently baked into a training script) versus "non-stationary" real-world tasks (running a business, legal work) that require continual relearning and can't easily be simulated in a data center.
- Distillation is argued to be the main force working against model-provider consolidation: any RL-learned behavior can be cheaply copied if you have the right prompt distribution, and Chinese labs are reportedly buying access to Western frontier models via router/proxy services to harvest realistic prompts for exactly this purpose.
- Model providers appear to be racing through domains (coding → finance → PowerPoint/office work) building high-value skills directly into weights, even though in principle a sufficiently capable in-context learner wouldn't need this — done partly for runtime efficiency and partly because task-specific data is cheap to add given surplus compute/parameters.
- Panelists flag a major unresolved bottleneck: models are estimated to be roughly a millionfold less sample-efficient than humans at learning from real experience, and it's unclear whether current "sim-to-real" transfer is strong enough to close this gap without direct weight updates from real-world interaction.
- One participant (Schulman) argues the last durable human role in AI development isn't technical execution but objective-specification — deciding what "helpful" or "aligned" behavior means — since this can't be automated away even once AIs handle all optimization.

## Quote

> Alignment can be decomposed into specification of the objective... and then actually achieving or optimizing the objective you've defined. — John Schulman
