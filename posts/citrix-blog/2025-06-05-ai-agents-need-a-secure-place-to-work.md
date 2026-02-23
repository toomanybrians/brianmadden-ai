---
title: "AI agents need a secure place to work. The Citrix workspace is ready."
date: "2025-06-05"
authority_level: 5
file_type: citrix-blog-post
tags: [ai-agents, workspace-as-control-plane, shadow-ai, computer-using-agents, security, enterprise-ai-strategy]
related_frameworks: [workspace-as-control-plane, post-application-era]
original_url: "https://www.citrix.com/blogs/2025/06/05/forget-the-model-wars-the-real-ai-race-is-in-the-workplace/"
staleness_threshold: stable
---

# AI agents need a secure place to work. The Citrix workspace is ready.

[Original post](https://www.citrix.com/blogs/2025/06/05/forget-the-model-wars-the-real-ai-race-is-in-the-workplace/)

June 5, 2025

The internet is buzzing about Mary Meeker's just-published 340-page report, *Trends—Artificial Intelligence* (PDF). If you're not familiar with Meeker's work, you should be. She's VC royalty, having led the IPOs of Netscape and Google. Her annual *Internet Trends Report* (last published in 2019) was required reading for tech investors for decades.

The 2025 Meeker report is mostly data and charts about AI: user growth, GPU CapEx, inference costs, model convergence—you name it. Because the report is so huge, the internet is full of summaries and hot takes, but unfortunately they're all pretty generic. ("Hey ChatGPT, summarize this PDF.") I read the report through the lens of what this means for the future of knowledge work and the workspace, e.g. the topics I've been exploring in this blog: the messy, real-world knowledge work done in desktops, browsers, and SaaS apps, mostly by humans, but increasingly with AI help.

The Meeker report applies to our world in four ways:

- AI agents are here, and they need a place to live.
- Inference is cheap, so shadow AI is exploding.
- Having the best model doesn't matter, but the best environment does.
- The agent is the new app, and most enterprises are not ready.

Let's dig into each of these.

## AI agents are here, and they need a place to live

A big topic in the Meeker report is the rise of agentic AI—long-running processes that act on behalf of users. These emerging tools go beyond chat and start to behave like real workers. They navigate user interfaces, submit forms, take actions, and orchestrate workflows. (In other words, they don't just generate output, they get work done.)

This is the next chapter for AI in the workspace, though it raises a fundamental question: where does this kind of AI actually run? If an AI agent needs to log in, browse, click, and perform multi-step tasks across multiple applications, it doesn't just need an API, it needs a workspace.

This is where most generic AI industry conversations break down. Everyone is focused on training models or building copilots, but almost no one is talking about the execution layer. If an agent is going to act like a human worker, it needs the same environment human workers use today: a secure, persistent, policy-controlled workspace that can host real applications, maintain state, and provide access to existing systems which haven't been modernized for APIs.

Computer-using agents (CUAs) like this are not speculation, they are real and happening today. As I highlighted in a recent keynote speech, every major AI company is now racing to build models that can process screens and browsers, understand interfaces, and operate keyboards and mice like people. Benchmarks like OSWorld and Windows Agent Arena show rapid progress, as agents progressed from single-digit scores a year ago to success rates of 40-50% for a range of human-level UI tasks. (Most humans, it should be noted, only score around 75%.)

Why is this happening? Because building native app connectors for every enterprise system is expensive, brittle, and slow. Letting agents operate in the same workspace as human workers is not only more flexible—it's often the only viable way for them to get real work done in the near term.

Fortunately that workspace already exists. (Citrix has spent decades optimizing and securing it.)

If you're starting to think about how AI agents will transform your workplace, don't just ask, "What can the model do?" Instead, start asking, "Where will that work happen?" Because the answer might already be in front of you—the same workspace (with the same guardrails) that you're already delivering to your existing workers today.

## Inference is cheap, so shadow AI is exploding

Another (mind-blowing) takeaway from the Meeker report is that the cost of inference has dropped by 99.7% over the past 2 years. ("Inference" is the process of running a model, e.g. actually using it, versus building and training it.) When inference is expensive, AI is tightly controlled by cost-conscious platform teams. When it's cheap, everyone uses it. That's the shift that's happening today.

Workers aren't waiting for permission. They're incorporating AI into their workflows on their own. (Pasting into ChatGPT, using browser extensions, installing Office plugins, asking AI for help with project plans, forecasts, and strategy visions...) This is more than a tool rollout—it's a behavior shift. And it's already happening across every department in every industry today.

This shadow AI use is both a risk and an opportunity. If workers are creating AI-augmented workflows outside of your visibility and policy controls, then you're already exposed. But if you have a secure workspace architecture in place, then you have an opportunity to meet your workers where they are. You can turn this chaos into your competitive advantage.

## Having the best model doesn't matter, but the best environment does

Another insight from the report confirms something I was starting to sense myself, that model performance is converging. A year ago everyone was buzzing about which model was best. Back then we'd subscribe to them all and switch every few weeks to get the latest and greatest. But the Meeker report confirmed that today's top LLMs are no longer miles apart, and whether you're using ChatGPT 4o, Claude 4, Gemini 2.5—it doesn't really matter.

I felt this on my own a few months ago, drastically consolidating what I used regularly because the friction of switching was too high. I was using them so much, and so deeply, that having all my history, knowledge, and custom projects in one ecosystem was more valuable than raw model performance. (And any new feature from one lab would be matched by everyone within a few months anyway.)

My experience highlights the reality about differentiation in today's environment where all the core models are "good enough." Who cares what a model can do in isolation? What can the model do in your environment, with your data, your apps, your tools, your policies, and your workflows? The smartest model in the world is useless if it can't access your system of record, or it's stuck behind three layers of disconnected UI, or it lacks session context or identity. We don't need another smart thing in a box.

To succeed here is to surround your AI with the right environment. This is another reason why the workspace matters. It brings together apps, data, context, identity, and security into a single runtime. When your workspace becomes the orchestration layer, the AI doesn't have to be perfect. It just has to do the job well enough, in the right place, with the right access.

That's the key to turning the potential of workplace AI into real impact. If you're still benchmarking models like it's a bake off, you're missing the bigger picture. AI's ability to perform in a company is not about the model, it's about the workspace you give it to operate in.

## The agent is the new app, and most enterprises are not ready

My final takeaway from the Meeker report is something it doesn't come out and say, but the hints are there: the dominant unit of enterprise software is shifting from apps to agents.

Enterprises have historically bought apps. Then we bought APIs and integrations. Now we're entering a phase where the primary object might be a persistent agent that logs in, performs tasks, and interacts with systems like a human worker.

This changes everything. An agent isn't like an app that calls an API, it navigates a UI. It doesn't just send data, it clicks buttons, fills forms, and adapts to changes. It needs access, context, and identity. It looks and behaves like a worker.

If agents are the new apps, then we need to rethink how we manage them.

Most organizations are not ready for this. They have policies for software, roles for employees, and governance processes for SaaS. But what about agents that spin up on demand? Or agents that login to legacy systems using human credentials? Or agents that need observability, policy enforcement, and identity management, just like people do?

This is another example of the things we're thinking about at Citrix. We've already built the infrastructure to manage human workers operating across devices, apps, and networks. Now we can extend that same model to AI agents and workers. Same policies. Same enforcement. Same architecture.

The agent is the new app. And the new worker. If your existing architecture can't support that shift, it's time to rethink the foundation.

## You don't need a roadmap. You need a platform.

The Meeker report is more than a celebration of AI—it's a warning shot for anyone responsible for enabling secure, productive work. AI is already in the building, augmenting human workers, and increasingly acting like a worker itself, requiring the same kinds of workspaces, access, and controls that you already manage.

If your architecture was designed around human workers and classic apps, it's time to expand that thinking to include agents, inference, and automation. That shift is already underway. It's time to start treating the workspace as a control plane—not just for people, but for how all work gets done. Citrix has helped customers navigate moments like this before. We're ready to help again.
