# The New Cognitive Stack

**Event:** DUCUG — Dutch Citrix User Group Conference #28
**Date:** March 18, 2026
**Location:** Oude Duikenburg, Echteld, Netherlands
**Format:** 60-minute closing session
**Speaker:** Brian Madden, VP Technology Officer & Futurist, Citrix

## Talk summary

A complete overhaul of Brian's stump speech, built from scratch in one day after the December 2025 version became entirely outdated following the November 2025 model inflection. The talk introduces the cognitive stack as a new framework for understanding AI's impact on knowledge work, demonstrates Brian's second brain as a working proof point, and maps the governance implications to enterprise workspace management.

## Core argument

Enterprise AI fails because it targets the visible 20% of knowledge work (emails, documents, meetings) while the real value lives in the invisible 80% (thinking, judgment, reasoning). The November 2025 model inflection made it possible to build AI cognitive extensions that operate at the thinking layer. Brian built one and demonstrates it live. The talk then walks down the cognitive stack layer by layer, showing skills, the irrelevance of automations, interface pathways, token economics, and why neutral workspace governance is the critical infrastructure need.

## Narrative arc

### The paradox and the invisible 80%
Opens with the disconnect: workers love AI, companies see no ROI. The reason: companies invest in the visible 20% (Copilot, chatbots, automation) while the invisible 80% (knowledge, thinking, judgment) goes untouched. "If you only perfectly automate this little 20%, you're missing the big part."

### November 2025 changed everything
Three frontier models (Opus 4.5, Gemini 3, GPT 5.2) crossed key thresholds simultaneously: sustained hours of autonomous work, error recovery, reliable tool use. Not because models got smarter — "it was all these little things that were annoying that prevented it from doing the work." Practitioner reactions (Karpathy, Ford, Willison, Cherny) shown as evidence.

### Coding as canary for knowledge work
Blog post framing: everything happening to software developers is coming for knowledge workers within 18 months. Uses Nate B. Jones "Mad Libs" technique — swapping coding terms for knowledge work terms — to make the parallel visceral.

### The February convergence
Rapid-fire headlines from February 2026: Citrini, Fortune, WSJ, Atlantic, NYT all independently converging on "the disruption has arrived." $285B SaaS market cap evaporated. "It doesn't say the AI disruption is coming. It says the AI disruption we've been waiting for has arrived. Past tense."

### The cognitive stack
Five layers: worker → cognitive extension → skills → agents → interfaces. Applies to all knowledge work, with or without AI. The top three layers (thinking) are invisible. The bottom two (doing) are visible. Enterprise AI investment concentrates at the bottom. Worker adoption happens at the top. This explains why companies see no ROI while workers love it.

### The second brain in practice
Brian's personal system: Claude Code connected to a folder of markdown files. Demonstrates a real morning session — Claude loads CLAUDE.md, follows links to thinking.md and skills index, finds blog drafts, provides full context. Key insight: "I did not write this file. It wrote it for future versions of itself." Model portability demonstrated — switched to Gemini when Claude was down, worked immediately.

### Skills
Text files that tell AI how to do things. "Skills are sort of almost discovered as opposed to invented." Not engineering — "if you can write instructions for a colleague, you can write a skill." Skills appreciate as models improve. Demonstrated real skills: connect the dots, daily briefing, podcast screenshot integration, work buckets.

### The automations rant
"I hate automations." Walks down the stack to agents and subverts the audience's expectation. "How repeatable are your jobs that you're automating all this kind of stuff?" Automations are a bottom-of-stack concern. When you have the brain, the claws figure themselves out.

### Interfaces — the four pathways
Modern apps via APIs/MCP. Web apps via browser control (demonstrated Claude controlling Chrome). Legacy apps via computer-using agents (OSWorld: humans 72%, AI now 75%). Direct file access. Agent-to-agent communication via shared folders. "Legacy applications is like all of them."

### Token economics
Real personal data: 285M tokens consumed in ~3 weeks. Pre-second brain: 100K tokens/day. Post: 5-10M/day. Subscription escalation from 20€ to 200€. Corporate API cost: ~$954/month. Had his AI build a dashboard in 4 minutes 27 seconds as proof point.

### The token squeeze and governance
50-100x token increase per worker when cognitive extensions become mainstream. All compute capacity pre-sold through ~2030. Not all tokens are equal. Every request must be routed by complexity, sensitivity, and nature. Excel routing example: same task costs 200K tokens via CUA or 1K tokens by reasoning in context. "Something needs to be making these decisions in real time for every worker, hundreds of times a day."

### Who decides
Not the worker (doesn't care about cost). Not Microsoft (sells the tokens). Not AI labs (consumes them). Requires a neutral party with workspace context. This is what Citrix does and has done for 35 years.

## Key quotes

- "I can AI the crap out of this, I can do it perfectly. And I still haven't really changed the way the thinking happens, which is where all the money is."
- "Skills are sort of almost discovered as opposed to invented."
- "Which half of my job do you want me to not do?"
- "The company that spends the most tokens in the most smart way is going to win."
- "Your offspring, grandchild AI is going to be reading these folders someday. Make it really good instructions."
- "Legacy applications is like all of them."
- "This is not something that's coming into knowledge work. This is here and available now."

## What's new in this talk

This represents a major evolution from Brian's December 2025 stump speech:
- **Cognitive stack** replaces the 7-stage evolution model as the organizing framework
- **Second brain demonstration** replaces abstract examples — Brian lives the thesis
- **Skills** introduced as a concept for the first time on stage
- **Token economics** with real personal data, new section
- **Automations subversion** — new rhetorical move
- **Coding as canary** — new section bridging developer experience to knowledge work
- **Brains talking to each other** — first time describing multi-person cognitive extension communication
- **Token routing as governance** — first time presenting the Excel decision tree externally

## Related content

- [[frameworks/cognitive-stack]] — the five-layer framework introduced in this talk
- [[reference/blog-posts/2026-02-19-coding-as-leading-indicator]] — the coding-as-canary blog post referenced
- [[reference/blog-posts/2026-03-12-skills-are-all-you-need]] — the skills blog post
- [[reference/blog-posts/2026-02-25-cognitive-stack]] — the cognitive stack blog post
- [[reference/speeches/2025-12-04-ai-think-tank-paris]] — the previous stump speech this replaces
