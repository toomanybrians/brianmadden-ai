---
title: "Everyone wants to provide your AI. Nobody wants to help you manage it."
date: "2025-11-13"
authority_level: 5
file_type: citrix-blog-post
tags: [ai-governance, workspace-governance, ai-fragmentation, enterprise-ai, security, control-plane]
related_frameworks: [workspace-as-control-plane]
original_url: "https://www.citrix.com/blogs/2025/11/13/everyone-wants-to-provide-your-ai-nobody-wants-to-help-you-manage-it/"
staleness_threshold: stable
---

# Everyone wants to provide your AI. Nobody wants to help you manage it.

[Original post](https://www.citrix.com/blogs/2025/11/13/everyone-wants-to-provide-your-ai-nobody-wants-to-help-you-manage-it/)

Nov 13, 2025

Have you ever thought about how many different AIs a typical knowledge worker encounters in a single day? Here's my quick list:

- Personal AI platform tool of choice (ChatGPT, Copilot, Gemini, Grok, Claude, etc.)
- Company-provided AI tool (Same list, but probably a different tool)
- AI buddy bolted onto their web browser (Atlas+ChatGPT, Edge+Copilot, Chrome+Gemini, Comet+Perplexity, Dia, etc.)
- AI tools provided by their device/OS (Windows Copilot, Samsung/Google Gemini, Apple Intelligence, etc.)
- AI built-in to just about every application they use. (probably all different, one per app)
- Plus all the other company-provided AI tools (Chatbots for HR and IT support, enterprise search, etc.)
- Plus any other random AI-powered tools the worker finds on their own (voice typing assistants, note takers, screen memory tools, audio transcriptions, etc.)

A typical knowledge worker could easily have 5+ different AI implementations in daily use. Each one works differently, and has its own interface, policies, and data handling. None of them talk to each other.

And they're all controlled by different entities.

## Where the AI lives matters

When AI is built into applications, the app vendor controls everything. Gmail's AI follows Google's rules. Salesforce's AI follows Salesforce's rules. Microsoft Copilot follows Microsoft's rules.

When AI lives in your OS, Microsoft or Apple controls it. They decide what it can see, what it can access, how it's governed. You inherit the guardrails and telemetry components that they choose to expose.

When AI lives in your browser, you're depending on the browser maker to set the boundaries and secure it.

When AI lives as standalone tools like ChatGPT or Claude, you're back to managing another SaaS product with enterprise admin features bolted on.

Each one creates a governance silo with its own admin console, policy language, and security model.

## You can't standardize on just one

A lot of people ask questions like, "Which AI should we adopt?" But that's not the right question anymore.

You're going to have AI from all these sources whether you want it or not. Microsoft is baking Copilot into Windows and Office. Google is baking Gemini into Workspace and Chrome. Every SaaS app is racing to add AI features. Device manufacturers are adding NPUs and on-device AI capabilities. Workers are using whatever AI helps them get their work done. Fragmentation is reality.

Trying to "standardize on one AI" is like trying to "standardize on one app" in 2010. So the real question isn't which source to choose, it's where you establish your governance boundary.

## The abstraction wars (2025 edition)

We've seen this before. Applications started on client/server, then moved to the web, then to mobile, then to SaaS. Each transition fragmented the landscape, and each vendor tried to own the stack. Eventually someone won by providing the abstraction layer that worked across all of them.

The same thing is happening with AI right now. Every vendor is trying to be your AI layer, and every layer has valid use cases. The winner won't be the best AI model or the most integrated AI feature. The winner will be whomever provides the governance abstraction that works across all the layers.

## Most governance strategies are broken

I'm seeing enterprises try to solve this in predictable ways:

1. Block certain AI tools.
2. Mandate others.
3. Create policies for each layer separately.
4. Deploy DLP that tries to catch data leakage after the fact.
5. (Bonus) Each of these comes from a different department / source in the company.

This doesn't work because you're not focusing on one source, so even the best governance at one layer still leaves policy holes at the others. So instead of governing AI by controlling (or limiting) the layer it lives in, you need governance that works across layers.

## The workspace is your governance boundary

This is where the concept of the workspace becomes critical. Not the workspace as "a collection of apps," but the workspace as I defined it recently: the place where apps, identity, security, and context converge.

The workspace as a concept is bigger than the apps, OS, or device. It's where work actually happens, and the only place where you can apply consistent governance across all the AI implementations your workers are actually using.

Think about what you need to govern AI in the workspace:

- Identity: Who or what is performing the work and accessing the AI? (Human or AI agent)
- Access control: What data can this AI touch? What apps can it use?
- Policy enforcement: Can it copy data? Upload files? Access certain systems?
- Audit trail: What did it do? What data did it access? What was the output?
- Context: What task is being performed? What's the business justification?

All of these are intertwined. A change in device posture could change the context, which changes what the worker can see, which changes what the AI working on their behalf can show them, etc. This means a single AI can't get the full context to adequately control its behavior via its narrow view of the larger workspace. This can only be done from the outside, at the workspace level, since that's where all these layers come together and where the actual work is done.

## What you actually need

Even though the AI technology is new, the governance is familiar. You need:

- Consistent policies across all AI implementations, not separate ones for each vendor/platform.
- Runtime access controls that work regardless of where the AI comes from.
- Audit trails that show the complete picture of what AI is doing with your data.
- The ability to revoke access cleanly when a worker (human or AI) leaves.

Where AI lives determines its capabilities, but where you govern it determines your risk.

Luckily we've all been building this infrastructure for decades, and we're now fortunate that the same workspace that delivers secure access for humans can deliver secure access for AI.

## The question you should be asking

Rather than asking "which AI should we adopt?", start asking "where do we establish our governance boundary?"

AI is showing up in every layer of your EUC stack. The question is whether you have a unified way to govern it or whether you're going to manage dozens of disconnected AI implementations with no common policy surface.

At Citrix, we think about the workspace as that governance layer. We're not trying to force everyone into one AI vendor or make sudden and drastic changes to how EUC is managed. Instead, we focus on the control plane that works across whatever AI implementations your workers actually use. This way of securing the fractured, worker-focused AI landscape will be critical in the coming years.

Let AI live where it works best. Govern it where work happens.
