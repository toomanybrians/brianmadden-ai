---
authority_level: 5
file_type: talk
staleness_threshold: stable
date: 2026-07-16
event: Arrow Forum 2026
location: Germany
audience: Arrow channel partners, resellers, and enterprise IT
format: ~40-minute keynote
source: Reconstructed from the slide deck; no recording exists
tags: [euc-2031, ai-bubble, open-weight-models, forward-deployed-engineers, diffusion-gap, seven-stage-roadmap, second-brain, knowledge-factory, token-economics, invisible-80-percent, futurism]
---

# What is a worker in 2031?

**Event:** Arrow Forum 2026
**Date:** July 16, 2026
**Location:** Germany
**Format:** ~40-minute keynote
**Speaker:** Brian Madden, VP Technology Officer & Futurist, Citrix

Reconstructed from the slide deck (no audio or video recording exists). This keynote is the main-stage version of the argument published four days later as the blog post "How to build an AI strategy that survives the bubble pop" (`posts/citrix-blog/2026-07-20-how-to-build-an-ai-strategy-that-survives-the-bubble-pop.md`) and discussed on Citrix AI Hotsheet EP4.

## Talk summary

You can't predict what a worker looks like in 2031, but you can identify what's true across every plausible path there and build for that. Two things are near-certain: AI capabilities keep climbing, and AI diffusion (how fast organizations absorb what AI can already do) stays slow. The gap between them is the whole opportunity, and closing it is about to become the biggest expansion of IT's job in a generation. When you interrogate the assumptions hiding inside "AI capabilities will keep increasing," most don't survive a bubble pop or a government export control — except one: Sonnet-class open-weight models are real today and will exist no matter what. So plan on those. Then close the diffusion gap yourself, because that's exactly what the industry is now paying forward-deployed engineers billions to do: reach the invisible 80% of knowledge work and make it legible. For EUC, every current primitive translates into a cognitive-era successor, and the job gets bigger, not smaller.

## Core argument

A futurist doesn't predict which future arrives; they work with probabilities and build for what's true across all of them. Stress-test the things everyone "knows" about the next five years and only one capability assumption survives every scenario — Sonnet-class open-weight models exist and can't be taken away. Diffusion, meanwhile, is slow, but forward-deployed engineers can close the gap, and the whole industry is now funding exactly that. The winning move for an organization is to do the FDE's job in-house: reach the invisible 80% of knowledge work and make it visible. EUC's primitives don't disappear in that world — they transform, and the control plane gets bigger.

## Narrative arc

### The frame: what do we know about the next five years?
The talk opens on "What is a worker in 2031?" and reframes it as "what happens in the next five years of work?" The spine of the talk is a running list Brian returns to and revises:

1. AI capabilities will continue to increase
2. AI diffusion is slow
3. Closing the AI diffusion gap will greatly expand IT
4. Knowing how to close the diffusion gap will be the key to the future of IT and work

### Capabilities vs. diffusion — the diffusion gap
Two clocks. Capabilities: what AI can do, still climbing. Diffusion: how fast AI is absorbed into organizations, slow. The space between the curves is the diffusion gap. Nearly eight in ten companies report using gen AI, yet just as many report no significant bottom-line impact — the problem isn't capability, it's absorption.

### The invisible 80%
Knowledge work is ~20% visible (emails, documents, meeting transcripts, chats) and ~80% invisible (thinking, reasoning, judgment). Traditional IT only ever operated in the visible 20% — the invisible 80% was "not our problem." AI changes the mandate: IT after AI has to reach the invisible 80%, aiming to make 100% of knowledge work visible and supportable.

### The satirical "AI strategy"
How do companies plan to get there today? "Develop an AI strategy": (1) the CEO declares "we are an AI-first company," (2) buy Copilot licenses for every worker, (3) ??? . The missing step 3 is the point — buying licenses is not a plan for closing the diffusion gap.

### What a futurist actually does
A futurist does not predict the future. A futurist works with probabilities and thinks about all possible futures. So take the assumptions built into each "thing we know" and stress-test them.

### Interrogating "AI capabilities will continue to increase"
Two assumptions hide inside it: (1) technical progress will continue — probably, not guaranteed; (2) the most advanced models will be available — but only if the US government allows them, only if they still exist after a bubble pop, and only if the Chinese government allows them. A timeline of recent headlines shows how fast frontier access is given and taken away:

- 7 April — Anthropic releases Mythos Preview to ~50 companies
- 9 June — Anthropic releases Fable 5 and Mythos 5
- 12 June — US government forces Anthropic to cut off those models
- 16 June — Chinese lab Zhipu releases GLM-5.2 as a full open-weight model (Opus 4.8 / GPT-5.5 class)
- 17 June — Chinese lab DeepSeek closes its first external round (~$6.5B)
- 25 June — US government "asks" OpenAI to limit GPT-5.6 to trusted partners
- 30 June — US government allows Anthropic to release Fable 5 and Mythos 5
- 9 July — US government allows OpenAI to release GPT-5.6

Frontier access is now a policy variable, not a given. And "even if the bubble pops, the technology still exists and is available" is itself an assumption that may not hold for AI the way it held for railroads and dark fiber.

### The resolution: Sonnet-class is real and guaranteed to exist
The one thing that survives every asterisk: open-weight models. GLM-5.2 is already released, MIT-licensed, and in the Opus 4.8 / GPT-5.5 class. So item 1 gets rewritten: from "AI capabilities will continue to increase" to "Sonnet-class AI is real, and guaranteed to exist." That's the reliable floor — no government and no bubble can take it away.

### Interrogating "AI diffusion is slow" — enter the FDE
Diffusion has a mechanism for change: forward-deployed engineers (FDEs). The money pouring into them:

- 5 May — Palantir Q1: US commercial up 133% YoY, CEO credits the FDE model
- 11 May — OpenAI announces a Deployment Company: $4B+ investment, 150 FDEs on day one, partnered with BCG, McKinsey, Capgemini, Accenture
- 11 June — Anthropic and DXC align to train tens of thousands of FDEs
- 30 June — AWS announces $1B to build its own FDE organization
- 2 July — Microsoft announces "Microsoft Frontier Company," $2.5B / 6,000 FDEs
- 15 July — Anthropic and Blackstone set up "Ode," $1.5B funding

An FDE is a Forward Deployed Engineer. How do you get one to close your diffusion gap? Option A: hire one of those firms. Option B: figure out what an FDE actually does, and do it yourself. What they do maps onto the 20/80/100 picture — they go into the organization and turn the invisible 80% into visible, encoded, usable knowledge. So item 2 gets rewritten: "AI diffusion is important; FDEs can speed it up."

### How to close the gap: understand how AI use evolves
The mechanism is the seven-stage roadmap, with the context vault at the center from Stage 3 on:

1. Faster search — a better Google, one-and-done prompts.
2. Thinking partner — back-and-forth, uploading documents, dictating.
3. Cognitive extension — the context vault / second brain. Give the AI access to everything instead of bringing documents to it.
4. Multi-tool agent — the AI reaches into the world: computer-using agents, browsers, APIs, MCPs, custom connectors.
5. Fleet — multiple AIs coordinating with each other and with other systems' AIs.
6. Pod — the self-running pod of agents; the new unit of work is a human plus their AIs, running beyond business hours.
7. Published self (optional fork) — publish your context vault so others' AIs can subscribe to it.

At the Pod stage, three worker types emerge:
- Cognitive owners — context plus judgment; the source of expertise.
- Cognitive operators — run the agent fleets.
- Cognitive curators — maintain the context vaults and skill libraries.

### The per-worker token ladder
Daily token consumption per worker climbs by stage: 100K (faster search) → 1M (thinking partner) → 10M (cognitive extension) → 100M (multi-tool agent) → 1B (fleet) → 10B (self-running pod), and "as few as possible" for the published self. Moving a workforce up the stages is a 10x-per-stage compute event, which is why token management becomes a first-class problem.

### The current EUC model and the audit
The current EUC model assumes work is one person, one screen, one set of apps, one set of hours. AI changes every one of those. But EUC mostly transitions rather than disappears:

- VDI stays — now used by humans and AI workers. Grounded in "AI is not eating all software": shallow UX-wrappers (Zapier, Canva, Figma, Resend) struggle; middle horizontal SaaS (Salesforce, Workday, Snowflake, Box) gets squeezed; deep regulated systems of record (Epic, SAP, Oracle, Guidewire, Fiserv, Amadeus, industrial control systems, mainframes) don't move.
- Image management becomes skill management; app virtualization becomes skill virtualization; profile management becomes context (brain) management. Same layering mechanics, new atomic unit.
- Group policy becomes agent policy.
- Session recording becomes agent observability, and beyond that cognitive observability.
- Performance management becomes token management, including token routing (the same task can cost 200K, 100K, 10K, 5K, 2K, or zero tokens depending on the method).
- Endpoint management becomes cognitive endpoint management.
- The receiver / workspace client becomes the cognitive workspace.
- The control plane stays — and gets bigger.

The organizing picture is a company / department / group context-vault hierarchy, extended to coworkers, consultants, and influencers, all under one control plane. What we do gets bigger.

### The close: build your own brain
Workers still need to work. Work still needs to happen somewhere. Somebody has to make that somewhere work — safely, observably, cost-effectively. That somebody is EUC/IT, and the job is bigger than it has ever been.

What next? Make the jump to Stage 3. Build your own brain:
- "You have to feel it before you can govern it."
- "You have to have one before you can manage thousands."

The final version of the running list: (1) Sonnet / GPT-5.5 class models will be available, (2) AI second brains are transformational, (3) the company knowledge-factory pattern, (4) an FDE-type approach is needed.

## Key formulations

- "What is a worker in 2031?"
- "A futurist does NOT predict the future. A futurist works with probabilities."
- "Nearly eight in ten companies report using gen AI — yet just as many report no significant bottom-line impact."
- "The CEO declares we're an AI-first company. Buy Copilot licenses for everyone. Then... ???"
- "Sonnet-class AI is real, and guaranteed to exist."
- "You better figure out what an FDE does."
- "You have to feel it before you can govern it."
- "You have to have one before you can manage thousands."

## Related content

- `posts/citrix-blog/2026-07-20-how-to-build-an-ai-strategy-that-survives-the-bubble-pop.md` — the blog version of the assumptions / open-weight argument
- `frameworks/7-stage-roadmap.md` — the roadmap walked in the talk
- `frameworks/invisible-80-percent.md` — the invisible 80% of knowledge work
- `frameworks/post-application-era.md` — why AI uses apps rather than replacing the deep ones
- `talks/2026-06-03-euctech-the-last-chapter-of-euc.md` — the closest comparable keynote (same roadmap, same EUC audit)
