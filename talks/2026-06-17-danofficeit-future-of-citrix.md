---
authority_level: 5
file_type: talk
staleness_threshold: stable
date: 2026-06-17
event: DanofficeIT — The Future of Citrix
location: Copenhagen, Denmark
audience: DanofficeIT partners, customers, and IT professionals (~25 people, intimate roundtable format)
format: ~60-minute talk with integrated Q&A
tags: [cognitive-stack, second-brain, knowledge-work, token-economics, euc, seven-phases, ai-governance, enterprise-ai, consulting]
---

# The near future of work

**DanofficeIT — The Future of Citrix** &middot; Copenhagen, Denmark &middot; June 17, 2026

A largely similar version of this talk is available as video: [Citrix AI Hotsheet Episode 2 — The Last Chapter of EUC](https://www.youtube.com/watch?v=Bgxx4UCtb6k) (EUCTech 2026 version, ~45 min). The content is mostly the same; this DanofficeIT version includes extended Q&A and some sharper formulations that didn't appear at EUCTech.

Intimate partner event hosted by DanofficeIT. Similar core material to the EUCTech 2026 keynote, delivered in a smaller, interactive format with extended Q&A woven throughout. The audience included the DanofficeIT team, customers, and large Danish enterprise accounts including hospital regions. The conversational format surfaced sharper formulations and Q&A exchanges around second brain trust, data integrity, and the consulting business model.

## Core argument

The AI narrative has flipped from "AI doesn't work" to "AI costs too much," and both are diffusion stories, not capability stories. To get real AI ROI, organizations have to reach the invisible 80% of knowledge work — thinking, judgment, reasoning — not just the visible 20% (emails, documents, transcripts) that IT has always managed. The seven-phase roadmap is how you get there. For EUC professionals, every primitive we already know carries forward; the words change but the job gets bigger.

## Why Citrix's 37-year pattern applies to AI

Citrix has spent its entire history wrapping existing technology to give it modern capabilities — without requiring organizations to rewrite everything. In the 1990s, that meant giving Windows apps the reach of web apps. Now it means giving AI the same access to applications that human workers already have, without rewriting those applications. AI is going to navigate computers. The question is whether it does so through a governed, policy-compliant Citrix session or through an ad-hoc consumer tool with no audit trail.

## The AI narrative flip and the diffusion problem

Six weeks before this talk, the dominant story was: eight in ten companies using AI, 95% failure rate, no ROI. At time of delivery, the story had flipped: AI costs too much, companies rationing tokens, corporate reeling from AI bills. That flip is evidence AI works. Two clocks run at different speeds: capabilities (still climbing) and diffusion (hitting a wall). Most "AI ROI" disappointment is a diffusion problem.

AI-caused congestion: a knowledge worker who produces 10 reports instead of 4 doesn't help the company if the business can only absorb 4. The bottleneck moves. The CFO eventually asks: does this increase revenue or lower expenses? If neither, why are we paying for it?

## The invisible 80%

Emails, documents, and meeting transcripts are maybe 20% of knowledge work — the visible outputs, the "digital exhaust." The other 80% is invisible: thinking, reasoning, judgment, skill, experience. "A lot of knowledge work is staring out the window looking at birds." EUC and IT have lived entirely inside the visible 20%. AI changes that: AI can now do the invisible parts, which makes them digital and therefore manageable. EUC's universe just got much larger.

## The seven phases

Every worker is somewhere on this path. Key framing: **you can only see one step ahead.** Someone on Phase 1 (faster search) can kind of see Phase 2 (thinking partner) but Phase 3 (cognitive extension) looks like a different planet. People who dismiss any of this are standing at the phase where the next one still seems visible and everything beyond is incomprehensible from where they are.

1. **Faster search** — one question, one answer. Most of the world is still here.
2. **Thinking partner** — longer conversations, loading documents, real back-and-forth.
3. **Cognitive extension (second brain)** — the inversion: don't take your documents to the AI, bring your AI to your documents. The AI has access to everything in a single vault it reads and writes. Not a database — actual folders of markdown files in GitHub. Within a day or two of starting, the AI was surfacing connections across things mentioned weeks apart.
4. **Multi-tool agent** — the cognitive extension connects into actual tools: MCP, browser control, desktop computer-using agents. OSWorld benchmark: humans score ~72, models now 80-85 including mid-tier models. Not automation — extended reach.
5. **Fleet of AIs** — multiple AI systems talking to each other. Your AI talking to your organization's AI. A partner like DanofficeIT building a bot that talks to Aidrien, to Citrix APIs, and carries all of DanofficeIT's accumulated best practices for their customer base.
6. **The pod** — the new atomic unit of knowledge work: one worker plus their AI fleet, context vault, and skills, operating continuously. Three worker types emerge: cognitive owners (context and judgment, the source of expertise), cognitive operators (run the fleet), cognitive curators (maintain the skill and context libraries). The bottom two look a lot like advanced IT work.
7. **The published self (optional fork)** — take your context vault and make it subscribable. Brianmadden.ai/mcp does this: any AI tool can connect and access the full knowledge base.

## Why automations aren't the path

Task automation only touches the visible 20% — the digital exhaust. If a task were easily automatable, it would have been automated 10 years ago with RPA. The cognitive extension approach means the AI has access to everything and context about everything, so it can help with any of the work — not a scripted subset. The AI isn't told to "do the expense report." It's asked to help prepare for the DanofficeIT event — pulling schedule, emails, calendar, CRM — because it has full context and knows how to access those systems.

## Doing this in Citrix today

You can do all of this with Citrix today, without new features. Install Claude on a Citrix VDA, publish the application in Workspace. Create a second user account (e.g., "Brian Madden Robot") with read-only access. The agent logs on as that user. Session recording is on for everything the robot does — 100%, always — because **the robot doesn't have privacy rights**. Workers' session recording has caused scandals (Microsoft Recall, Facebook). The agent doesn't care. App Protection on. DLP on. Chrome Enterprise Premium with its own managed profile. The robot can read everything it needs; it can't send emails or delete calendar events. All of this is in production on existing Citrix infrastructure today.

## EUC primitives translated

Every EUC primitive carries forward into its AI-era successor — it's a find-and-replace: users, profiles, apps, policy, sessions → cognitive owners, context, skills, agent policy, agent sessions.

- VDI stays — used by humans and AI workers
- Image management → skill management
- App virtualization and layering → skill virtualization and layering; resultant set of skills and context (company-wide → departmental → individual)
- Profile management → context management
- Group policy → agent policy
- Session recording → cognitive observability (see Q&A below)
- Performance management → token management (see Q&A below)
- Endpoint management stays — AI generates the UI on demand on whatever device is nearest
- The control plane stays and gets bigger

## Token management

Token consumption scales dramatically by phase: roughly 100K/day (faster search) → 1M (thinking partner) → 10M (cognitive extension) → 100M (multi-tool agent with screenshot processing) → 1B (fleet) → 10B (always-on pods). I used 291 million tokens my first month of cognitive extension. Someone I follow reports 20-30 billion tokens daily in his agentic system.

Tokens are supply-constrained. The job of token management is to maximize economic value per token, not minimize spend. Routing: for a given task — CUA driving Excel desktop (200K tokens), browser automation (100K), read the xlsx XML directly (10K), Python script (5K), reason in context (2K), or hand it to a human (0). Which model, where it runs, device posture, PII — all factors. This routing is an IT governance layer that didn't exist two years ago.

## Q&A highlights

### On trusting your second brain's data

A concrete illustration of the integrity problem: my AI built a profile on a colleague based on meeting transcripts. Because I only record *disagreements* for the AI to process — you don't dictate conversations where everyone agrees — the AI had flagged an adversarial relationship with a colleague I'm 99% aligned with. The AI was filtering comments through this incorrect profile. I caught it only because I noticed something odd, went directly to the file, and deleted the entry.

The mechanism: **selection bias in what gets captured creates systematic distortion in the AI's model of the world.** If you only talk to your AI about problems and conflicts, it builds a problem-and-conflict-dominated worldview. The fix: file-based storage you can read, inspect, and edit directly. A vector database abstracts this away; a folder of markdown files doesn't. "These kinds of questions are absolutely the questions that we have to solve. The knowledge integrity problem was always a challenge for companies. But it was never something we in end-user computing thought about. Now it's our problem too."

### On who owns your second brain

"If a folder full of text files and a twenty-euro ChatGPT subscription can do my whole job — I want to know about that first. For real." After six months of working this way, the understanding of what the AI can and can't do, and what value I actually provide, is much clearer. Also worth noting: the context vault becomes *more* valuable as AI improves. Claude 4.5 → 4.6 → 4.7 → 4.8 — the same vault produces better outputs with each model generation. That's unusual. Most technology assets decay as AI advances; the context vault compounds.

### On the consulting business model

"The days of a consultant coming in and leaving the PDF after a project — those days are dead." What replaces it: the consultant develops a living context vault as part of the engagement, and clients' AIs plug directly into it. DanofficeIT's best practices, industry knowledge, configuration guides — available as a subscribable second brain, always current. The consulting product shifts from a deliverable at project close to an ongoing knowledge relationship.

### On cognitive observability

Session recording serves not just to observe agent behavior, but potentially as a cognitive provenance system — DNA markers on ideas, tracking where each piece of reasoning came from. Which source document, which meeting transcript, which connection did the AI make? Provenance matters in regulated industries. Research on this is active across the AI knowledge world. Session recording infrastructure is already the right scaffolding.

## Key formulations

- "If a folder full of text files and a twenty-euro ChatGPT subscription can do my whole job — I want to know about that first."
- "The days of a consultant coming in and leaving the PDF after a project — those days are dead."
- "You can only see one step ahead. Phase 3 from Phase 1 looks like a different planet."
- "My agent doesn't care if it's recorded."
- "Selection bias in what gets captured creates systematic distortion in the AI's model of the world."
- "The context vault becomes more valuable as AI gets better."
- "Find and replace: users, profiles, apps, policy, sessions → cognitive owners, context, skills, agent policy, agent sessions. It's all the same stuff."
- "I don't take my documents to the AI. I bring my AI to my documents."
- "The first book of EUC is 1990-2025. We are writing the first page of book two."
