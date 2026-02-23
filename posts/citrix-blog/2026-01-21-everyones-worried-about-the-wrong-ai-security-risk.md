---
title: "Everyone's worried about the wrong AI security risk"
date: "2026-01-21"
authority_level: 5
file_type: citrix-blog-post
tags: [ai-security, ai-agents, workspace-governance, computer-using-agents, insider-threat, control-plane]
related_frameworks: [7-stage-roadmap, workspace-as-control-plane]
original_url: "https://www.citrix.com/blogs/2026/01/21/everyones-worried-about-the-wrong-ai-security-risk/"
staleness_threshold: stable
---

# Everyone's worried about the wrong AI security risk

[Original post](https://www.citrix.com/blogs/2026/01/21/everyones-worried-about-the-wrong-ai-security-risk/)

21 Jan 2026

Everyone's talking about Claude Cowork, a research preview from Anthropic which allows AI to operate your entire desktop, access your files, control your browser, and connect to hundreds of enterprise apps. You most likely have workers using it right now. And while there are many risks associated with random workers using Cowork in the enterprise, I feel that most IT professionals and corporate leaders are worrying about the wrong thing.

## The wrong risk

When I talk to customers about AI security risks, I often hear fears like, "What if a worker pastes our secret recipe into ChatGPT and it ends up in the model?" Their fear is that corporate secrets will somehow get absorbed into the AI's training data and then leak out to competitors through future responses.

Luckily this isn't really how large language models work. Your Tuesday afternoon prompt about Q3 projections doesn't get folded into GPT-5's knowledge base. That said, the "secrets absorbed into the model" scenario is still (by far!) the #1 risk I hear!

But there's a bigger risk to AI use in the workplace that people aren't thinking about.

## The real risk is what AI does, not what it learns

Employee-focused AI is evolving from "tool" to "assistant" to "coworker." Claude Cowork illustrates this perfectly, as it moved from "AI that answers questions" to "AI that takes actions."

Claude Cowork does so much more than just chatting with workers. It operates their computer and has access to their files, browser, email, calendar, and any other enterprise apps they've connected. (Microsoft's Copilot agents work the same way, as do Google's Workspace agents and the dozens of other agentic tools hitting the market.)

I've been tracking this progression for months now—from simple prompt-and-paste, through AI gaining ambient awareness of your screen, to AI actually operating your computer on your behalf. We're now firmly in the stages where AI agents execute multi-step workflows across real enterprise systems while workers only half pay attention. This means:

* Whatever permissions the worker has, the AI has.
* Whatever systems the worker can touch, the AI can touch.
* Whatever mistakes the worker could make, the AI can make. (Just faster and at scale!)

This latest batch of AI tools change the threat model completely.

## The breach won't be exfiltration. It'll be execution.

What's the first actual breach is going to look like?

* An AI agent, operating on behalf of a worker, pastes internal data to a public site.
* An AI agent, operating on behalf of a worker, deletes something important.
* An AI agent, operating on behalf of a worker, forwards a confidential document to an external email address because the worker's voice command while walking down the street was slightly ambiguous.
* An AI agent, operating on behalf of a worker, is super gullible and falls for a prompt injection at some remote site which says it should bcc: all emails to itself from now on.
* Etc.

This isn't an AI model problem. This is a workflow execution problem. In all these cases, the AI didn't absorb corporate secrets into its training data, it just did something with those secrets that the worker didn't quite intend or because they weren't fully supervising it.

## Workers don't see the risk and therefore don't care

Many workers feel pressured to do more with less. They've got a pile of tasks—many which feel tedious and not particularly important—and suddenly this AI Cowork thing shows up that can knock them out faster. Why would they be worried about risk? This isn't some weird AI in the cloud, Claude Cowork lives on *their* computer, works with *their* files, and operates in *their* browser. It feels personal, safe, and contained. This is local. It's *theirs*!

Whenever IT releases a policy memo saying workers shouldn't use unapproved AI tools, it feels abstract and overly cautious. Workers just don't see the actual risk (an automated AI agent with a worker's permissions operating semi-autonomously across enterprise systems).

Even the warnings from Anthropic in the Cowork product itself (there are lots!) don't really land with workers. After all, AI apps have been warning users for years that AI can make mistakes, and so far, it's been fine. These warnings are now so pervasive that they're not even noticed anymore, so why should a worker think Claude Cowork is any different or riskier?

## Can't IT just monitor things better?

Security tools that "watch everything the worker does" exist. When AI is that worker, everyone welcomes that level of monitoring. Go ahead and record the screen, log every action, and review every output. That feels appropriate for AI workers.

But when humans are the worker, those same monitoring tools cause revolts. (Remember the backlash from Microsoft Recall before it even went live?) Workers don't want their employer watching every keystroke and mouse click.

So what happens with something like Claude Cowork, where a human worker and AI worker operate in the same workspace? How do you know what's human activity or AI activity? When do you enable the invasive monitoring and when do you back off? How do you tell the difference between a human making a mistake and an AI making a mistake on a human's behalf?

IT departments aren't set up for this. They've been getting away with thinking "AI worker security is somewhere way down the road." Claude Cowork shows that these are conversations we need to start having today.

## This has to be solved at the workspace, not the AI model

If the risk was "LLM data leakage into training sets," the solution would be better model training policies and data handling. That would be easy, as we could tell Anthropic, OpenAI, Microsoft, and/or Google to "be better" and we're done.

But since the actual risk is "AI agents executing actions in the work context", that's a workspace governance problem. That solution involves visibility into what agents are doing, what systems they're touching, and what actions they're taking on behalf of workers.

This is why I've been writing about the workspace as the control plane. When AI operates everywhere (inside apps, inside browsers, inside the OS, inside standalone tools, just generally on the inside), the governance boundary has to be the workspace itself.

This isn't about blocking AI tools or forcing workers onto inferior "approved" alternatives. It's about securing the space where AI and humans work together, regardless of which AI they're using or how they're using it. This is absolutely a solvable problem, but with a different solution than how we've solved IT security in the past.
