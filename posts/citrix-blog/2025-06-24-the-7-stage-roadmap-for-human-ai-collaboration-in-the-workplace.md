---
title: "The 7-stage roadmap for human-AI collaboration in the workplace"
date: "2025-06-24"
authority_level: 5
file_type: citrix-blog-post
tags: [ai-agents, human-ai-collaboration, computer-using-agents, workspace-as-control-plane, ai-in-the-workplace, frameworks]
related_frameworks: [7-stage-roadmap, workspace-as-control-plane]
original_url: "https://www.citrix.com/blogs/2025/06/24/the-7-stage-roadmap-for-human-ai-collaboration-in-the-workplace/"
staleness_threshold: stable
---

# The 7-stage roadmap for human-AI collaboration in the workplace

[Original post](https://www.citrix.com/blogs/2025/06/24/the-7-stage-roadmap-for-human-ai-collaboration-in-the-workplace/)

June 24, 2025

I spend the majority of my time at Citrix exploring, discussing, and planning for AI's impact on knowledge work. But lately I've noticed there's no shared understanding of what this means, which makes conversations around this type of AI evolution difficult.

So in this post, I'm sharing a practical framework I've started using recently: seven stages of progression for how human workers will use and collaborate with AI in the workspace. These stages take us from the simple LLM use we started seeing a few years ago to a future with fully autonomous AI agents orchestrating complex tasks across the enterprise.

Use these seven stages as a way to frame your thinking about how your workers are using AI, how the technology and its use will evolve over the next few years, and how you'll respond, support, and secure them in each stage.

## Stage 1: Simple tasks, "prompt and paste" (2023)

The first stage of AI use by knowledge workers was shortly after ChatGPT was released in late 2022. Workers started using ChatGPT (and similar tools) on their own, leveraging AI for relatively simple "one and done" tasks like summarizing documents, drafting emails, and translating text. Workers use a simple workflow where they type a prompt into a webpage or app, get the answer, and copy it into the app that needs it. This first stage is where workers are just starting to dabble with AI, using it as a low-effort assistant for short and simple tasks.

## Stage 2: Deeper thinking, true collaboration (2024-2025)

This second stage is similar to the first, but with the subtle difference that people are using AI for more complex cognitive tasks. Now they're uploading stacks of documents, presentations, reports, and meeting transcripts and using AI to process them deeply. Instead of just asking for a single summary or email, people are engaging the AI in multi-turn discussions to develop strategy documents, build project plans, analyze data, and write code. AI use in this stage isn't just simple throwaway tasks, this is real work.

Stage 2 of workplace AI use enables workers to do things that they couldn't have done before. It's not about doing tasks faster or with less effort, it's expanding capabilities and starting to turn workers into superworkers.

This stage of AI use is partially due to advancements in LLMs (more connectors & document types, context windows that support millions of words, bigger and more sophisticated models), but also partially due to workers becoming better and more advanced AI users, with a better understanding of how to get the most out of an LLM.

Interestingly many people don't realize Stage 2 even exists, since the "mechanics" (copying/pasting with standalone AI apps) looks similar to outsides from Stage 1. But anyone paying attention knows that in the hands of a competent worker, the way LLMs are used today bears little resemblance to how they were used two years ago.

This stage is where workers start to bifurcate into "AI superhumans" and "workers who might get left behind." Stage 2 is also where companies should start to worry, because lots of corporate data is going into the models, and lots of knowledge worker "thinking" is being outsourced to the models.

## Stage 3: The AI watches your screen (2H 2025)

In Stage 3, AI gains the ability to see what's on a worker's screen and offer contextual help based on that. This sounds scary and very sci-fi, but it's real today. Microsoft Copilot Vision on Windows chats with the user about what's on their screen in real time and can highlight what it's talking about. (This is different and much more powerful than Microsoft Recall which is more about screen shot archiving.) Google Gemini in Chrome lets users chat about the web page they're currently viewing. New browsers like Dia and Brave thread AI assistance into every page someone visits.

This is the shift from AI being reactive to being ambient. Instead of copy and paste, a worker just asks, "What should I do here?" and the AI knows what the "here" is since it sees what they see. In this world, the AI doesn't have to wait to be prompted. (Flashback to Clippy tapping on the screen.)

Stage 3 introduces serious privacy and trust concerns. If AI can see the screen, what data is it seeing? Where's that data being processed? Is it being stored or used to train the model? Who's responsible for all this? Are your users doing this? Can you stop them? How would you even know?

A lot of evolution will happen here around data boundaries (Is the endpoint really the "end" point? Local OCR versus off-box vision processing, watermarking, realtime masking of sensitive panes, on-prem and on-device models, etc.)

## Stage 4: The AI uses your computer for you (2026)

Once AI can see the screen, it's not a big leap for it to start using the computer directly by operating the mouse and keyboard. These types of AI usage scenarios are generally known as computer-using agents (CUAs). They can navigate the UI and perform tasks just like a human would, including opening apps, copying data, filling out forms, clicking buttons, and more. CUAs will ultimately be more flexible and capable than traditional RPA tools, as they can be instructed via plain language and don't require specific tech skills to operate them.

Looking at the big picture, the shift in Stage 4 is that people will assign tasks directly to a workspace instead of a person.

Early versions of CUAs are available today, including OpenAI Operator, Anthropic Claude Computer Use, Google Project Mariner, Microsoft Copilot Studio, as well as open source projects like UI-TARS. Even though these tools often get stuck or make dumb mistakes, they're getting better every day. In fact there are benchmarks which track how good they are, including OSWorld and Windows Agent Arena. (Various agents have improved from single-digit scores up into the 40% range over the past few months. Humans typically score in the 70s.)

Some people in the AI community believe that CUAs will be a short-lived novelty, as AI agents operating GUIs built for humans are inefficient, and a better implementation is for agents to bypass the GUI entirely by working directly with APIs. While that's ideal in theory, it overlooks the practical dynamics of enterprise heterogeneity, where thousands of long-tail, rarely-updated apps with no APIs are deeply embedded in the processes of the workplace operation. This massive sunk integration cost (in people, process, and technology) isn't getting ripped and replaced overnight, and the gentlest, most-likely path for AI to enter this world will be AI operating the same apps via the same GUIs alongside human workers.

AI agents operating existing computer GUIs can be scary, with fears like "AI will take my job!" The reality is that these CUAs will initially only be capable of doing simple tasks. Even when they hit 100% on the benchmarks, that just means they're really good at using a computer—it doesn't mean they know how to do all the other parts of your job. (e.g. They have mastered *how* to click, and even *what* and *when* to click, but they don't know *why* to click.)

CUAs will require "scaffolding" from humans, where the human workers outline the basic framework and context, and the CUAs perform the individual tasks to fill in the spaces. ("Scaffolding" is going to be something you hear a lot as AI agents become more capable.)

AI agents will steadily improve throughout this stage, though people won't yet trust them to operate completely on their own. They will run in the context of the human worker (e.g. they're using the human's login account) with direct human oversight.

## Stage 5: AI uses your computer without you watching it (2026+)

As peoples' trust in computer-using agents improves, they'll start letting the agents run on their own without direct oversight. Again, this will happen over time, with people trusting their agents to perform ever more complex and longer-running tasks.

Even though these Stage 5 AI agents use the computer on its own, they're still task-based. The human worker still provides the scaffolding, and the AI performs the steps. As the AI agents improve, the human workers will be able to provide higher and broader guidance in their scaffolding with ever-increasing gaps.

This stage will require new infrastructure to manage and monitor the human-AI interaction: sandboxing, auditing, checkpoints, session recording, task scheduling, flow control, and other operational and security structures. This is also the stage where the agents get their own login identities which will allow them to be audited, secured, and monitored more strictly. (For example, Microsoft has recently announced Entra ID for AI Agents.)

AI agents getting their own identities means they'll be able to operate a workspace without a human. Just like human knowledge workers, the AI agents and the workspace they're operating don't need to be in the same place, as an AI agent could use HDX to remotely connect to a Windows or Linux workspace to operate apps just like any human knowledge worker.

The mental shift that will take place here will be that rather than assigning tasks to a person, you'll build the environment (the secure workspace) for that task to run.

## Stage 6: Multi-agent AI communication (2027?+)

In the next stage, multiple AI agents start talking to each other. One agent kicks off another, which handles a subtask and returns the result. They begin to coordinate, with workflows becoming chains of interacting agents, all running semi-autonomously. Human workers are still providing the scaffolding, again with larger spaces for the increasingly capable AI agents to do ever more complex tasks.

This is the stage where AI agents will start to move out of the workspaces that humans use. There will still be agents that GUIs built for humans, but they'll coordinate with bigger thinking models running elsewhere. (Maybe the NPU on the laptop will handle the local interaction with the workspace while the core reasoning agent runs elsewhere.)

Trust and reliability will still be key, and humans will still provide quite a bit of oversight. The AI still needs somewhere to run, and there's still a "workspace" behind the scenes which is where all the apps, context, and security comes today.

Workers continue their evolution from doers to orchestrators, designing the scaffolding and supervising autonomous AI execution. (Think of this like a typical career progression: as you move from a junior manager to a senior manager to director, you have bigger "gaps" in the scaffolding you provide to your team, because your workers are also higher level and can do more complex tasks with less oversight and direction. This will be the same with AI progression.)

## Stage 7: AI-orchestrated work (2028?+)

The final stage I'll explore today happens when AI orchestrates large-scale workflows across people, agents, and systems. Building upon the multi-agent, multi-system coordination from the previous step, agents in Stage 7 will start to engage with the human workers as needed. (Following the same career progression analogy from above, this stage is like humans moving from senior director to VP—they still provide the scaffolding of broad strategy, governance, and goal-setting, but more and more of their time is also as an escalation point, status check, and ensuring their team is operating smoothly.) In this world, the workspace still exists. Apps, data, security, identity, context, and a control plane to make sense of it all—that hasn't changed.

Any UIs needed by humans will be generated by AI in whatever form makes sense for that human in that moment. *This does not mean the keyboard, mouse, or laptop are going away!* If a worker wants to use that interface, great! It will be available. But if a worker wants to video chat with an avatar representing the AI, that's available too. Or if they want to talk to it via earbuds while on the go. Or use it via the screen on their phone, their tv, or whatever device is in front of them at the moment, that's all possible, and the AI will ensure the necessary application or UI elements are available to the worker. (I envision this like CEO-level where there's a whole staff of people to make sure they have everything they need to make the best use of their time at any given moment.)

There will certainly be "traditional" enterprise apps in the background underpinning all this. In fact this Stage 7 ability for AI to dynamically shift the UIs into whatever form the human wants will be here well before an enterprise's ability to migrate off their current application stack. (Which is fine. For decades the "right" play for enterprises has been to wrap their reliable old applications in modern delivery tech.)

The orchestration layer that manages the human-AI interaction at Stage 7 will be the "hard part" for enterprises, and certainly a bigger investment (in time, effort, and money) than the AI models themselves.

## What about AI apps and other IT-led initiatives?

Throughout all these stages, IT will continue to introduce AI in the familiar top-down ways—buying SaaS apps with AI features, embedding copilots into everything, and commissioning custom enterprise AI-powered apps. These projects matter, but they fit inside existing procurement, change-management, and compliance frameworks. They're essentially new applications with AI inside, subject to the same life-cycle controls as any other enterprise software.

The seven-stage model isn't about which team (IT or end users) "owns" AI. It's about *how* knowledge work is getting done—the progression from humans using tools directly, to humans guiding agents, to agents acting semi-independently within the same digital workspace environments. This is not a separate category of AI initiatives, it's the changing nature of interaction between people, tasks, and digital systems. As agents get more capable, they'll use *everything*—apps (with and without AI), internal tools, external SaaS—just as a human worker would. The challenge isn't which apps are "AI-enabled," it's whether you're ready to support *AI as a worker* in your existing workspace model.

## What this means for you

The specific progression and timing through these seven stages will vary by company, industry, geography, department, and individual worker. (The specific boundaries between each stage are blurry too.) What matters is not the exact labels, but the overall trajectory. This is the new roadmap for how AI will reshape knowledge work in the years to come.

Many workers are already well into Stage 2 and experimenting with Stage 3, and we can only assume that future stages will be here sooner than most people expect. The key to success, especially for the later stages (5+), is for your company to be structurally ready. It's not about whether and when the technology arrives, it's whether your environment can absorb it when it does.

This doesn't mean you need to build your own LLM or launch a moonshot AI initiative. (If you want to, that's fine, but as mentioned above that's a different initiative than these seven stages.) You just need a clear view of how work is being done, how workers and agents interact, and how the dynamic will continue to shift. The priority now is to design for disposability, as the tools, agents, and orchestrations you implement today will be obsolete in 18 months. Workers and work will adapt fast, and you need an architecture that can keep up.

The biggest challenges will be cultural, not technical. Risk and security teams will push back on autonomous agents, autonomy levels will be capped, and new questions will emerge about which work is scaffolding from humans versus AI-led process execution.

Luckily this will evolve over time and you don't need to solve for Stage 7 today, but you need to ask and understand:

- What work is being done?
- Where is it happening?
- Who (or what) is doing it?
- Can you observe it?
- Can you control it?

The issue isn't whether AI can perform the work. It's whether you can see it, trust it, and govern it. AI adoption will press forward (messily!) through technical fragility, organizational friction, and constant reinvention. Your orchestration framework and control plane will matter more (and be a bigger investment) than the agents themselves.

## This is what we think about at Citrix

You don't need new systems or workspaces to support the AI usage outlined in the seven stages above. These agents will use the same tools your human workers use today: the same apps, desktops, browsers, and SaaS platforms.

That's why the same secure workspace model applies at every stage: enforce policy, control access, monitor activity, and maintain visibility, regardless of who or what is doing the work.

Citrix already provides that foundation. For over 30 years, we've secured human work. Now we're applying that same model to AI workers.

You can start today with the tools you already have. The apps may change. The workers will evolve. But the workspace stays consistent. Citrix will continue to provide the control plane to manage & secure it all.
