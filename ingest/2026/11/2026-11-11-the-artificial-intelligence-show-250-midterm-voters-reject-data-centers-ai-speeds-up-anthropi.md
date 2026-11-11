---
title: '#250: Midterm Voters Reject Data Centers, AI Speeds Up Anthropic’s Research,
  Celebrating 250 & Nvidia’s Spy Probe'
source: The Artificial Intelligence Show
source_id: the-artificial-intelligence-show
source_url: https://podcast.smarterx.ai/shownotes/250
author: The Artificial Intelligence Show
date_published: '2026-11-10'
date_captured: '2026-11-11'
ingest_method: feed
model: claude-sonnet-5
content_basis: transcript
---

# #250: Midterm Voters Reject Data Centers, AI Speeds Up Anthropic’s Research, Celebrating 250 & Nvidia’s Spy Probe

## Fit with Brian's work

**Fit: direct.** Several threads run straight through his active frameworks — compute scarcity and token governance, the cognitive stack's layer-selection argument, enterprise spending data on agents vs. humans, and a host's own second-brain build that mirrors his knowledge-factory thesis.

- The data-center backlash and its predicted fallout (price hikes, usage caps) is a live instance of his **compute-availability/"control your own destiny"** argument — supply constraints, not pure pricing, becoming the binding limit on token access.
- The Menlo Ventures enterprise spending data (agents = 80% of OpenRouter tokens, 7x human usage) is hard evidence for the **cognitive stack** critique that industry spend and consumption concentrate at the bottom layers (agents/interfaces) rather than the brain layer.
- LinkedIn's model-swap and Zapier's agent+deterministic hybrid are concrete validations of his **routing-as-governance / layer-selection** thesis — pick the cheapest layer that does the job, reserve agentic judgment for what needs it.
- HubSpot's "headless" trial and usage-based credit pricing extends the **post-application era / SaaSpocalypse** thesis into a live example of a mid-tier SaaS vendor hedging against AI dissolving its UI layer.
- A host's from-scratch second brain (SQLite database, Codex-written deterministic collection code, AI only for judgment tasks like transcription and theming) is independent convergent evidence for the **knowledge factory's** Tier 1/Tier 2/Tier 3 discipline, built without any awareness of Brian's architecture.
- The METR/Anthropic RSI findings and Sergey Brin's "RSI treadmill" comments bear on the **bubble-pop planning and "separating what's real" threads** — frontier labs reporting internally accelerating progress just as compute politics threatens supply.

## Insights

### Compute scarcity and the data-center backlash
- Voters backed restrictions on data centers in 40 of 41 local ballot measures in the 2026 US midterms; several winning gubernatorial candidates (Gina Inajosa-TX, Keisha Lance Bottoms-GA, Amy Acton-OH, spellings unverified) campaigned on pausing or taxing data-center buildout.
- Hosts predict this constrains compute supply enough to raise consumer AI subscription prices or cut usage allowances, and speculate it could accelerate marketing AI subscriptions ($1,000–$2,000/month tiers) as direct hiring alternatives rather than productivity tools.
- OpenAI responded during the same window with a "National Community Compact" and "Compute Campus Policy Blueprint," rebranding data centers as "Compute Campuses" and pledging local job creation, energy cost-sharing, and community input at future owned-and-operated sites.
- A speaker frames the political dynamic as leverage rather than an existential block: Democrats understand AI's economic/national-security importance and will extract concessions, but infrastructure already greenlit or broken ground (committed 2025–2026) is unlikely to stop; impact lands mainly on 2028–2029 projects.

### RSI and frontier-pace acceleration
- METR's evaluation at Anthropic (Aug 12–Oct 29, 2026) found AI has roughly doubled the pace of internal AI R&D; an Anthropic co-founder/chief architect confirmed the conclusions but declined to disclose mechanisms, calling them commercially sensitive and a "roadmap" risk for competitors.
- The claimed acceleration is characterized as two years of model progress (Claude 2.1 to Sonnet 4.5) compressed into roughly half the time.
- Google's Sergey Brin reportedly said Gemini models are already helping build their successors ("getting onto the RSI treadmill"), and a Google DeepMind researcher described post-training demand shifting from raw chips to "Argon quota" as evidence the loop has tightened.
- An anonymous but reportedly trusted X account ("Pliny," spelling unverified) speculates labs are using unguardrailed internal model versions to reverse-engineer internet software and feed reconstructed source code into training pipelines — a claim, not confirmed, about a new training-data source beyond text/image/video scraping.
- Hosts note both METR and Brin still describe this as AI-assisted acceleration (humans + AI), not yet autonomous self-improvement — an important distinction from full RSI.

### Enterprise AI spending and token consumption (Menlo Ventures report)
- Enterprise AI spending reached $177B annualized pace in 2026 vs. $33B the prior year, per Menlo's survey of ~400 US enterprise decision-makers representing over $4B in spend.
- Agents now account for 80% of all tokens on OpenRouter — roughly 7x human-driven usage — cited as the clearest proxy for where consumption is concentrating.
- Anthropic, OpenAI, and Google together command 69% of enterprise deployment dollars (up from 50% last year); Anthropic and OpenAI alone account for 86% of enterprise LLM API spend (up from 67%).
- Anthropic's share of that spend grew from 40% to 55%, OpenAI's from 27% to 31%, while Google's fell from 21% to 9% — attributed by a host to Google's models underperforming this year, with newer releases (Argon) possibly shifting this.
- Companies spent 4.7x their prior year's level on average, versus a planned 1.9x — spending is running well ahead of budgeted intent.
- Coding tools and enterprise chatbots account for 76% of AI application spending in the surveyed cohort; 55% of incremental spend comes from new budget lines rather than redirected existing software budgets.
- Menlo found limited evidence that companies are replacing core systems of record (Salesforce, Workday) with AI outright — spend is additive, not yet substitutive, at the systems-of-record layer.

### Cost control and layer-selection in practice
- LinkedIn reportedly flattened the cost of its AI hiring-assistant tool despite rising usage by replacing OpenAI models with smaller, cheaper in-house-trained models for the same task — a live example of model-swap routing for cost control.
- Zapier CEO Wade Foster claims a hybrid architecture — agent handles judgment/setup, deterministic automation handles repeatable execution, with fallback to the agent if a step breaks — cuts costs by up to 71% versus pure agentic execution.
- HubSpot is reportedly considering a "headless" strategy letting customers analyze HubSpot data directly via ChatGPT or Claude instead of native tooling, while testing usage-credit pricing (e.g., per email sent or ticket resolved) layered on top of seat pricing.
- Hosts flag unresolved tension in the headless/credit model: it risks "variable cost hell" for customers and could push them toward building in-house alternatives rather than paying per-unit-of-work fees — and note the dynamic applies to any SaaS vendor (Salesforce, Workday), not just HubSpot.

### A convergent second-brain build
- One host describes building a personal context system: a SQLite database aggregating voice memo transcripts, ChatGPT/Claude conversation logs (preserving speaker and platform), Google Docs notes, X bookmarks, and photographed handwritten notes, built with Codex.
- The design deliberately maximizes deterministic code for ingestion/maintenance (scheduled scripts, no token usage) and reserves AI specifically for judgment tasks: transcribing handwriting, triaging which document sections belong in the database, and thematic search over the archive.
- The host explicitly credits the idea to Zapier's deterministic-plus-agent framing from the same episode's cost-control segment, describing the project as still in progress but already functional and stored in a private GitHub repo.
- Separately, a host describes testing OpenAI's "Dots" personal agent proactively resurfacing unfinished tasks unprompted, and reflects that centralizing such proactive agents inside a company (rather than leaving each worker to self-build) could compress the timeline toward near-fully-automated ("self-driving") companies much sooner than expected, while expressing hesitation about how to discuss or deploy that responsibly.

## Quote

> "Everything looks different to me right now... I just can't look at 2027 the same right now." — a host
> "You can't unsee the future once you see it." — a host
> "It's a whack-a-mole game." — a host, on SaaS vendors trying to block AI computer-use workarounds

## Not captured

Nvidia CEO Jensen Huang affair/espionage investigation and its corporate-governance fallout; the AI-in-education segment (Google's Gemini rollout to schools, a school president's essay on rethinking curricula); the episode's 250th-anniversary retrospective and AI Academy promotional content.
