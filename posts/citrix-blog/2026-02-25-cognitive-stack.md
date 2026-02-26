---
title: "Understanding the cognitive stack: why your AI strategy is focused on the wrong layer"
date: "2026-02-25"
authority_level: 5
file_type: citrix-blog-post
tags: [cognitive-stack, agents, delegation, claws, skills-hierarchy, enterprise-ai-strategy, personal-ai-knowledge-systems, second-brain]
related_frameworks: [delegation-not-automation, invisible-80-percent, five-levels-of-ai-in-knowledge-work]
original_url: "https://www.citrix.com/blogs/2026/02/25/understanding-the-cognitive-stack-why-your-ai-strategy-is-focused-on-the-wrong-layer/"
staleness_threshold: stable
---

# Understanding the cognitive stack: why your AI strategy is focused on the wrong layer

[Original post](https://www.citrix.com/blogs/2026/02/25/understanding-the-cognitive-stack-why-your-ai-strategy-is-focused-on-the-wrong-layer/)

*Brian Madden—February 25, 2026*

2025 was often declared as "the year of the agent," and it seemed like every vendor, analyst, and keynote talked about them. So I thought it was interesting that once I started using AI to manage a [second brain](https://www.linkedin.com/pulse/i-built-second-brain-using-ai-its-changed-way-work-future-madden-0tote/), I stopped thinking about agents entirely.

My AI still fires them up constantly. It loves them! But from my perspective, I just interact with the brain part of my AI. If my AI needs to spawn an agent to go do something, it does. (Invisibly, & in the background.) So it's not that agents disappeared, but rather that they became infrastructure.

## Claws, not brains

Andrej Karpathy recently [coined "claws"](https://simonwillison.net/2026/Feb/21/claws/) as the term for personal AI agents. "Just like LLM agents were a new layer on top of LLMs, Claws are now a new layer on top of LLM agents, taking the orchestration, scheduling, context, tool calls and a kind of persistence to a next level."

The name is a play on OpenClaw (the AI-powered automation platform that went viral, which I [wrote about](https://www.citrix.com/blogs/2026/02/04/openclaw-and-moltbook-preview-the-changes-needed-with-corporate-ai-governance/) a few weeks ago). It's also a perfect analogy: claws are appendages. They grip, manipulate, and reach into systems. While they might handle low-level operations on their own, they ultimately serve the brain, which is the cognitive engine that decides *what* needs to happen, in what order, and with what judgment.

Back in December I [wrote that workers don't want to build automations, they want to delegate](https://www.citrix.com/blogs/2025/12/18/workers-dont-want-to-build-automations-they-want-to-delegate/). I was describing a hierarchy from intent down to execution, but I didn't have the right framing for it yet. The claws-and-brains distinction makes it concrete enough to name: there's a full cognitive stack at work here, but unfortunately...

## The industry is building from the wrong end

The bottom of this cognitive stack is simple. Workflow automations are basically fancy scripts: take a process, define the steps, run them. Since this was kind of simple, it makes sense that's where the industry started too.

But simple automations break the moment something requires judgment. So over the years, RPA vendors started moving up the stack to add in some intelligence. (Exception handling, decision logic, and now a little AI to handle the ambiguous cases.) Each time the automation hit a ceiling, the answer was to move up a bit more.

This was fine until the AI companies blew it up by entering from the other direction, They started from the top and worked their way down. LLMs that understand intent can reason about tasks and then figure out steps on their own. This top-down approach enabled workers to describe what they wanted in natural language and the system would decompose the work.

These two trajectories overlap in the middle of the stack, as today we see the skills and agentic layers covered by both modern AI companies and legacy RPA and automation vendors. So who's going to win? (Rhetorical, obviously humans prefer to connect at the intelligence layer. The whole point of my December article was that humans don't care about automations and agents. They just want to tell their AI what want and having it happen. The AI can figure out how to waterfall it down to the agent / claw that actually does the work.

That's what a second brain actually is. Workers start with a cognitive layer that holds their full context: who they work with, what's sensitive, what's urgent, how they think, what they've written, what they know, etc. When it needs to reach down into some real world system ([whether modern, web, SaaS, or legacy](https://www.citrix.com/blogs/2025/12/10/ai-will-be-the-interface-to-knowledge-work-heres-how-well-get-there/)), it will spawn an agent. When it needs a specific connector, it will find (or build) one. But in terms of value, these agents are disposable. The intelligence is the product.

## The cognitive stack

I put together the following diagram to illustrate this. There's a lot going on here, so let me walk you through it.

[IMAGE]

1. *The worker:* States intent & exercises judgment. "Get the pre-reads to all participants before March 6." The human decides what matters, what's urgent, and what the goal actually is.
2. *The cognitive extension ("the brain"):* The thing you actually talk to. It holds your full context: who the participants are, the preferred format, what's sensitive, what happened in the last meeting, etc. It plans the approach and sequences the work.
3. *Skills:* What the brain knows how to do. Coherent chunks of capability: process a meeting transcript, draft an email, research a competitor, check a calendar. Each one handles a meaningful piece of work with some autonomy.
4. *Agentic sub-processes:* How skills get executed. The agents that actually reach into systems, navigate interfaces, call APIs, coordinate with other agents. This is where all that "agent" hype lives, and it's the second dumbest / lowest value layer!
5. *Workflow automation:* Just one possible execution tool. Scripts, RPAs, CUAs, API calls, webhooks... whatever it is, it's the simplest, most mechanical layer. While this is important plumbing, it's an interchangeable commodity infrastructure layer.

Interestingly this cognitive stack maps to how organizations already work, [as I touched on last week](https://www.citrix.com/blogs/2026/02/19/what-will-knowledge-work-be-in-18-months-look-at-what-ai-is-doing-to-coding-right-now).

If you look at a corporate org chart, there's more thinking at the top and more doing at the bottom. Work starts with intent and flows down from there. This isn't a new idea, it's the just the shape intelligence naturally takes when coordinating complex work.

What's wild to me is the enterprise AI industry is spending billions on the bottom two layers of this stack. Agent marketplaces, orchestration engines, workflow designers, automation studios... these are all claws and skills. But the real transformation lives at the top (the brain layer), which is where the worker lives and where everything below is invisible—[the invisible 80%](https://www.citrix.com/blogs/2026/01/13/the-invisible-80-what-corporate-led-ai-transformations-cant-see/) of knowledge work that corporate AI transformations can't see.

You see why focusing on the bottom is a problem? Sure, it's the easy part because it's the visible point. But no one's strategy for building a great organization is to keep making the task workers incrementally smarter until one of them figures out how to be the VP. Yet that's essentially most peoples' enterprise AI strategy right now! Just keep improving the automations, keep adding intelligence to the agents, keep climbing up the stack until a magical "POOF" which somehow causes this bottom-up approach to produce the cognitive layer that actually transforms work.

It's just not going to happen. It can't. You have to start at the top. (This is why that "second brain" thing works.)

## What this means for enterprise AI strategy

If you're evaluating AI investments right now (obv this is everyone), the cognitive stack gives you a simple question to ask: which layer are you buying?

Most of what's on the market today lives at layers four and five (the bottom two). Agent platforms, automation studios, orchestration engines, and workflow designers and necessary plumbing which is genuinely needed. But it's the bottom of the stack, and no amount of investment there produces the cognitive layer where the actual transformation happens. (You'll never to transform your way to the future by deploying increasingly smarter agents!)

The harder question is who builds layer two ("the brain")—the governed cognitive layer where context lives, intent gets translated into action, and the invisible 80% of knowledge work actually operates. That's the layer nobody has figured out yet. That's the layer worth figuring out.
