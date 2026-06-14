# The Last Chapter of EUC

**Event:** EUCTech 2026 (Oslo-Kiel cruise)
**Date:** June 3, 2026
**Location:** Aboard the Oslo-Kiel cruise, Norway
**Format:** ~45-minute keynote (Day 1)
**Speaker:** Brian Madden, VP Technology Officer & Futurist, Citrix

Also published as a special solo edition of the Citrix AI Hotsheet podcast (Episode 2, June 13, 2026) — audio and video. Full transcript: `podcast/ep2.md`.

## Talk summary

A keynote for end-user computing veterans on where the EUC industry stands in the summer of 2026 and where it's heading. Brian argues that the "AI isn't worth it" narrative has become the "AI is too expensive" narrative, and that both are diffusion stories, not capability stories. He reframes knowledge work around the invisible 80%, walks the updated seven-step roadmap for how AI enters work, then audits every EUC primitive — translating each into its AI-era successor. The close: "The Last Chapter of EUC" is the last chapter of book one. Book two is the next 30 years, and EUC pros are the ones who get to write it.

## Core argument

Enterprise AI ROI is elusive because of diffusion (how fast organizations absorb what AI can do), not capability. The fix for knowledge work is to reach the invisible 80% — thinking, judgment, reasoning — not just the visible 20% of emails, documents, and transcripts that IT has always managed. Most EUC primitives don't disappear; they transform. The mechanics carry over, the unit of delivery changes, and the job gets bigger.

## Narrative arc

### Capabilities vs. diffusion
The narrative flipped from "is AI even good?" to "AI is too expensive," with companies imposing usage and spend caps. That flip is evidence AI works. Two clocks: capabilities (still climbing) and diffusion (hitting a wall). Most "AI ROI" complaints are diffusion problems. AI-caused congestion: a worker who produces more doesn't help if the business can't absorb the output — the bottleneck just moves, the same way developers can now write code faster than it can be reviewed, tested, and secured.

### The invisible 80%
Emails, documents, and transcripts are the visible outputs of knowledge work — maybe 20%. The real bulk is invisible: thinking, reasoning, judgment, the experience that comes from years in a role. IT lives in the visible 20%; the invisible 80% is where the business-transformation consultancies live. AI has to transform all of work, so EUC has to step outside its 20% bubble. This is why AI hasn't produced instant ROI.

### How AI enters work — the seven steps (2026 edition)
An update to the seven-stage roadmap Brian first published in June 2025. Every worker is somewhere on this path:

1. Faster search — a better Google, one-and-done prompts. Where most workers (and most AI skeptics) still are.
2. Thinking partner — back-and-forth, uploading documents, dictating. Enabled by smarter models, longer context, and document upload.
3. Cognitive extension (the second brain) — flip it: instead of bringing papers to the AI, give the AI access to everything, in a context vault it reads and writes. Brian started in January 2026; roughly 1% of workers are here.
4. Multi-tool agent — connect the AI to the world: MCP, connectors, browser control, and computer-using agents for desktop apps. OSWorld: median human ~72-74, AIs now in the 80s. Not to automate — to extend the knowledge worker's reach across all their tools and data.
5. Fleet of AIs — multiple AIs working and talking to each other and to other systems' AIs.
6. The pod — the new unit of work: a worker plus their AIs. Work is no longer bounded to business hours; AIs act, flag, and escalate on their own. Three worker types emerge: cognitive owners (context and judgment, the source of expertise), cognitive operators (run the fleet), and cognitive curators (maintain context and skills).
7. The published self — an optional fork: publish your context vault so others can subscribe (brianmadden.ai, MCP at brianmadden.ai/mcp). Underpins a future of blended expert contexts inside companies.

### The current EUC model and the audit
The current model assumes one person, one screen, one set of apps, one set of hours. AI breaks those assumptions. But most of EUC transitions over rather than disappearing. Each primitive translated into its AI-era successor:

- VDI stays — used by humans and AI workers. Grounded in "AI is not eating all software": the shallow / middle / deep software pyramid. Shallow UX-wrappers struggle, middle horizontal SaaS gets squeezed, deep regulated systems of record (Epic, SAP, Oracle, mainframes) don't move. AI uses these apps; it doesn't replace the deep ones.
- Image management becomes skill management; app virtualization and layering become skill virtualization and layering; profile management becomes context management. Same inheritance and layering mechanics (resultant set of policies), a new atomic unit (a knowledge nugget or a skill).
- Group policy becomes agent policy.
- Session recording becomes agent observability — and, beyond that, cognitive observability. A new security vector: layered context vaults can go rogue or be poisoned, so you need to trace what context shaped the AI's judgment, not just govern the agent.
- Performance management becomes token management. Token routing and efficiency: the Excel example — the same task at 200K tokens (a computer-using agent driving Excel), 100K (browser automation), 10K (reading the .xlsx XML directly), 5K (a Python script), 2K (reasoning in context), or zero (handing it to a human). Plus where the model runs (cloud, on-prem, device) and device-trust and PII checks.
- Endpoint management stays — but endpoints become wearables and ambient devices, and the AI generates the UI on demand wherever you are.
- The Citrix receiver / workspace client becomes the cognitive workspace — icons for tasks and knowledge sources, not apps.
- The control plane stays and gets bigger. Something has to manage the humans, agents, cognition, models, routing, and security.

The throughline: the words change (agent, cognitive, skills, context) but how and why we do the work doesn't. The core IT skills transfer. The job gets bigger.

### Book one and book two
"The Last Chapter of EUC" is the last chapter of book one — the past 30 years, all spent on the visible 20%. Book two is the next 30 years, on the invisible 80%: thinking, reasoning, judgment, taste. Page one of book two is step three — build your own second brain. "You have to manage one before you can manage thousands." Then connect it to apps, to other AIs, and let it work without you. Book two doesn't have a title yet, and EUC pros are the ones who get to write it.

## Key formulations

- "It's still a story about ROI — but the AI is working, it's actually working too well, and now it's too expensive."
- "It's not that AI can't do it. It's that companies can't absorb it."
- "Emails and documents and transcripts aren't the knowledge work itself. They're the outputs of knowledge work."
- "You have to manage one before you can manage thousands."
- "This is the last chapter — but it's the last chapter of book one. We are the ones who are going to write book two."

## Related content

- `frameworks/7-stage-roadmap.md` — the seven-step roadmap (2026 edition) walked in the talk
- `frameworks/invisible-80-percent.md` — the invisible 80% of knowledge work
- `frameworks/post-application-era.md` — why AI uses apps rather than replacing the deep ones
- `podcast/ep2.md` — full transcript (published as Citrix AI Hotsheet EP 2)
