---
title: "What happens when AI agents score 100% in computing using benchmarks?"
date: "2025-07-24"
authority_level: 5
file_type: citrix-blog-post
tags: [computer-using-agents, ai-agents, benchmarks, human-ai-collaboration]
related_frameworks: [7-stage-roadmap, workspace-as-control-plane]
original_url: "https://www.citrix.com/blogs/2025/07/24/what-happens-when-ai-agents-score-100-in-computing-using-benchmarks/"
staleness_threshold: stable
---

# What happens when AI agents score 100% in computing using benchmarks?

[Original post](https://www.citrix.com/blogs/2025/07/24/what-happens-when-ai-agents-score-100-in-computing-using-benchmarks/)

July 24, 2025

All the major AI labs are developing AI software agents that can operate a computer just like a person, visually parsing pixels, moving the mouse, and pressing keys. These are Computing User Agents (CUAs), and I wrote in-depth about them last week.

Today's best CUAs are able to complete about 45% of the tasks in the popular OSWorld benchmark, up from just 6% when the benchmark was created sixteen months ago. What happens when they reach 100%?

In this post, I'll explore what these benchmarks really measure, what they leave out, and how to prepare for the moment that AI UI execution becomes a solved problem.

## Understanding the CUA benchmarks

The OSWorld benchmark defines 369 real desktop tasks: file management, web browsing, multi-app workflows, and so on. Human testers are able to finish 72-74% of them, but CUAs are closing the gap fast: 17% at the beginning of 2025, 45% today, and likely human parity in 2026.

Eventually, one will hit 100%. Then what?

A perfect score only proves a CUA can navigate any UI. It still won't decide why a task matters, evaluate risk, or resolve ambiguity. The CUA execution layer is just the hands and eyes, not the brain.

## Humans provide the scaffolding

Even with 100% capable CUAs, human workers will need to:

- Set goals and intent
- Define guardrails and checkpoints
- Respond to escalations

The value won't be in the raw UI control by the CUA, it will be the scaffolding around it.

## CUAs become the universal API

That said, once CUA execution is solved, every legacy desktop app will become an intelligent API surface. A typical use case will involve multiple models working together:

- An interface agent (CUA) will be deterministic and sandboxed. There will be one per workspace instance.
- Planner / reasoning agents will decide and orchestrate which CUAs to invoke, when, and with what constraints.

CUAs plus scaffolding map directly to Stage 4 ("AI uses your computer"), and then evolve into Stages 5 ("AI uses your computer without you") and 6 ("multi-agent coordination") in the 7-stage human-AI collaboration roadmap.

Because each CUA will use existing workspaces and run with its own identity, existing IAM, DLP, session recording, and other guardrails will still apply as they do today. You won't have to reinvent your security model.

## Planning for this future

Don't get me wrong, it will be a big deal when CUAs hit 100 % execution. But this will only be a milestone, not the final destination, on the journey to AI in the workplace. When this happens, the value will shift to how well you design, secure, and govern the orchestration layer which drives the CUAs.

The scarcity (e.g. the value) will be the judgment around knowing what to do, how to do it, and what success looks like. When CUAs hit 100%, that judgement will still come from humans.

At that point, human workers will shift from doing to directing, and the org chart will start to look like a massive orchestration graph. Once CUA execution is solved, the only interface left to optimize will be your own thinking.
