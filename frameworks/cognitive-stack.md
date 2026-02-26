---
title: "The cognitive stack"
date: 2026-02-25
authority_level: 4
file_type: framework
tags: ["cognitive-stack", "agents", "delegation", "claws", "skills-hierarchy", "enterprise-ai-strategy", "second-brain"]
related_frameworks: ["delegation-not-automation", "invisible-80-percent", "five-levels-of-ai-in-knowledge-work"]
related_posts: ["2026-02-25-cognitive-stack", "2025-12-18-workers-dont-want-to-build-automations-they-want-to-delegate"]
original_url: "https://www.citrix.com/blogs/2026/02/25/understanding-the-cognitive-stack-why-your-ai-strategy-is-focused-on-the-wrong-layer/"
staleness_threshold: stable
---

# The cognitive stack

A five-layer model showing how intelligence organizes itself to coordinate complex work—from human intent down to mechanical execution. The enterprise AI industry is spending billions on the bottom two layers. The real transformation lives at the top.

*Published: February 25, 2026 — [Original post](https://www.citrix.com/blogs/2026/02/25/understanding-the-cognitive-stack-why-your-ai-strategy-is-focused-on-the-wrong-layer/)*
*Extends: the delegation-not-automation thesis (formalizes the skills hierarchy into a named framework)*
*Incorporates: Karpathy's "claws" concept for personal AI agents*

## The five layers

1. **The worker:** States intent and exercises judgment. "Get the pre-reads to all participants before March 6." The human decides what matters, what's urgent, and what the goal actually is.
2. **The cognitive extension ("the brain"):** The thing the worker actually talks to. Holds full context: who the participants are, preferred formats, what's sensitive, what happened last time. Plans the approach and sequences the work.
3. **Skills:** What the brain knows how to do. Coherent chunks of capability—process a transcript, draft an email, research a competitor, check a calendar. Each handles a meaningful piece of work with some autonomy.
4. **Agentic sub-processes:** How skills get executed. The agents that reach into systems, navigate interfaces, call APIs, coordinate with other agents. This is where the "agent" hype lives—and it's the second lowest-value layer.
5. **Workflow automation:** The simplest, most mechanical layer. Scripts, RPAs, CUAs, API calls, webhooks. Important plumbing, but interchangeable commodity infrastructure.

## Two trajectories colliding

The bottom-up trajectory: RPA and automation vendors started at layer 5 and have been climbing upward for decades. Each time automations hit a ceiling requiring judgment, they moved up a layer. Exception handling, decision logic, now AI for ambiguous cases.

The top-down trajectory: AI companies entered from layer 1. LLMs that understand intent can reason about tasks and decompose work on their own. Workers describe what they want in natural language and the system figures out the steps.

These trajectories overlap in the middle (layers 3 and 4). Both modern AI companies and legacy automation vendors cover the skills and agentic layers. But humans prefer to connect at the intelligence layer—the delegation thesis holds that workers don't care about automations and agents. They want to tell their AI what they want and have it happen.

## Claws, not brains

Karpathy coined "claws" for personal AI agents—a play on OpenClaw. The analogy is precise: claws are appendages. They grip, manipulate, and reach into systems. But they serve the brain, which decides what needs to happen, in what order, and with what judgment.

This maps directly onto the stack: layers 4-5 are claws, layer 2 is the brain, and layer 3 (skills) is the interface between them. The worker sits above, exercising judgment. The claws execute below. The brain orchestrates.

## Why the industry is building from the wrong end

Agent marketplaces, orchestration engines, workflow designers, automation studios—all investing at layers 4-5. But no amount of investment at the bottom produces the cognitive layer where transformation actually happens. You can't make task workers incrementally smarter until one of them figures out how to be the VP.

The cognitive layer (layer 2) is where the invisible 80% of knowledge work operates. It's the governed cognitive extension that holds context, translates intent into action, and makes everything below invisible. That's the layer nobody has figured out yet.

## Maps to organizational structure

The cognitive stack mirrors how organizations already work. Corporate org charts have more thinking at the top and more doing at the bottom. Work starts with intent and flows down. This isn't a new idea—it's the shape intelligence naturally takes when coordinating complex work.

## Using this framework

Deploy when:
- Evaluating AI investments: ask "which layer are you buying?" Most products live at layers 4-5
- The "agents" conversation needs reframing: agents are claws (layers 4-5), not the brain (layer 2). The transformation is at the top, not the bottom
- Someone asks why second brains work: they start at layer 2 where context and judgment live, then reach down into systems as needed. Agents become invisible infrastructure
- Challenging bottom-up AI strategies: "you'll never transform your way to the future by deploying increasingly smarter agents"
- Explaining why corporate AI initiatives stall: they're optimizing layers 4-5 while the cognitive layer (layer 2) remains unbuilt
- The pitch is about agent orchestration: redirect to the question of who builds the brain layer—the governed cognitive extension where context lives and intent gets translated into action
