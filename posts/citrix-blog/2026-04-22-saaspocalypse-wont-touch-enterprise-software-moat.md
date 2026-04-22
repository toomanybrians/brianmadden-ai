---
title: "The SaaSpocalypse won't touch the enterprise software moat"
date: 2026-04-22
url: https://www.citrix.com/blogs/2026/04/22/the-saaspocalypse-wont-touch-the-enterprise-software-moat/
authority_level: 4
file_type: blog-post
tags: [post-application-era, saaspocalypse, enterprise-software, boring-infrastructure, systems-of-record]
staleness_threshold: stable
description: "AI is eating software — but only a specific layer of it. The deep layer of vertical regulated systems of record (Epic, SAP, Amadeus, industrial control, bank cores) isn't going anywhere. AI dissolves UIs, not systems of record."
---

# The SaaSpocalypse won't touch the enterprise software moat

Last week Daniel Miessler published [*The Fire of Fires*](https://danielmiessler.com/blog/the-fire-of-fires), describing how he canceled six SaaS tools (Zapier, Resend, Figma, Canva, Browserbase, & Supabase), rebuilt the functionality himself using Claude Code and his personal AI harness, and used it as evidence that AI is about to burn through most of the SaaS industry. His story is clear and drives the "I canceled my SaaS" flex which is going to be all over LinkedIn for the next year.

But I don't buy his conclusion.

The story goes like this:

1. AI is eating SaaS …
2. which means SaaS is dying …
3. which means companies whose business is delivering and governing SaaS are dying. (Including Citrix and all the apps we securely deliver.)

This ["SaaSpocalypse"](https://www.linkedin.com/posts/bmadden_salesforce-just-invented-a-metric-to-measure-share-7433078775040569344) narrative is becoming mainstream: Salesforce's growth has stalled, [Workday just replaced its CEO](https://www.bloomberg.com/news/articles/2026-02-09/workday-co-founder-returns-as-ceo-amid-steep-share-decline), Snowflake [keeps missing numbers](https://www.fool.com/investing/2026/02/04/1-ai-stock-down-about-25-in-2026-is-it-a-buy/), Zoom is in a [cringey "AI-communications" pivot](https://www.zoom.com/en/blog/agentic-ai-next-evolution-zoom/), and [Block laid off 40% of its workforce and explicitly blamed AI](https://www.cnn.com/2026/02/26/business/block-layoffs-ai-jack-dorsey). The [WSJ](https://www.wsj.com/tech/ai/claude-code-cursor-codex-vibe-coding-52750531), [NYT](https://www.nytimes.com/2026/02/18/opinion/ai-software.html), and [Fortune](https://fortune.com/2026/02/06/anthropic-claude-opus-4-6-stock-selloff-new-upgrade/) have all run variants of the "AI is eating software" headline this year.

This story makes sense at a glance but falls apart if you dig deeper. AI is not eating "software" as a category, it's eating a specific layer of software.

## Miessler's SaaS list: the shallow layer

All the software Miessler writes about is pretty thin. Each is essentially just a trendy UX wrapper around a commodity core. They were all founded after 2010, are all horizontal (no specific industry focus), and don't have a real moat. So yes, now that you can vibe code a UX in a weekend, the companies who depend on UX as their moat are in trouble. (Which is Miessler's whole point. Fair.)

But Miessler's list isn't a broad cross-section of software, it's one specific bucket.

## The SaaSpocalypse victims: the middle layer

Let's look one layer deeper. SaaS vendors like Salesforce, Workday, Snowflake, Zoom, Asana, Monday, Smartsheet, Box, Dropbox, Atlassian, and parts of Adobe getting hit with the SaaSpocalypse are a level below the UX-as-moat companies Miessler canceled. This next layer are legit enterprise SaaS companies with real customer data and real integrations, but they're also still horizontal (e.g. each could be used by a hospital, refinery, or law firm), so they're not super wired into how any one industry actually operates and don't have decades of that industry's regulation or workflows baked in.

This doesn't mean all of them are toast. Salesforce is the system of record for customer relationships most places it's used, and ServiceNow is deeply wired into enterprise workflows and won't move easily. But most of the others on this list could genuinely be in trouble, as reflected in their stock prices and news headlines.

So that's two layers so far: shallow fancier-UX horizontal SaaS (toast), and enterprise horizontal SaaS without deep moats (squeezed). This is what most LinkedIn/X hot takes refer to, and why "AI is eating software" is memeable for those who aren't deep in enterprise IT.

## What really runs enterprises: the deep layer

So what's missing from the "I vibe coded my own SaaS" posts?

[Epic](https://www.epic.com) runs at every major hospital in the United States. [SAP](https://www.sap.com) runs supply chains and financial reporting for half the Fortune 500, while [Oracle EBS](https://www.oracle.com/applications/ebusiness/) and [Oracle Fusion](https://www.oracle.com/applications/) do it for the other half. [Amadeus](https://amadeus.com), [Sabre](https://www.sabre.com), and [Travelport](https://www.travelport.com) handle every airline reservation on Earth. [Guidewire](https://www.guidewire.com) and [Duck Creek](https://www.duckcreek.com) process every insurance claim in the US. Industrial control systems from [ABB](https://www.abb.com), [Honeywell](https://www.honeywell.com), [Siemens](https://www.siemens.com), and [Rockwell](https://www.rockwellautomation.com) run every refinery, power plant, water treatment facility, and factory floor. [FIS](https://www.fisglobal.com), [Fiserv](https://www.fiserv.com), [Jack Henry](https://www.jackhenry.com), and [Temenos](https://www.temenos.com) run the bank cores. [Veeva](https://www.veeva.com) and [Medidata](https://www.medidata.com) run pharma clinical trials. [Vertex](https://www.vertexinc.com) and [Avalara](https://www.avalara.com) run tax compliance. [Dassault](https://www.3ds.com), [Siemens NX](https://plm.sw.siemens.com), and [PTC](https://www.ptc.com) run aerospace and automotive design. And don't forget the countless government mainframes which have survived 40 years of "modernization" attempts.

This is the software the real economy runs on, and none of it is going to be on anyone's "vibe code and cancel subscription" weekend to-do list. (Not coincidentally, these apps are the ones Citrix has been securely delivering for decades.)

For those who haven't spent their career in enterprise IT, I'll walk through the reasons why:

1. **Regulation**: HIPAA, FDA 21 CFR Part 11, SOX, state insurance regulators, FAA, IATA, PCI, and countless safety certifications for industrial control. The value of this software isn't the code, it's that the code survived decades of audits and battle hardening. You can't vibe code a system that has to pass an FDA inspection.

2. **These systems sit on mountains of data**. There are 250 million patient records in Epic, every fare rule and codeshare agreement is in Amadeus and Sabre, and a decade+ of transaction history lives in any given SAP installation. You don't casually migrate any of that to an AI-powered experiment.

3. **Decades of workflow are also baked into these systems**. Every state-specific rule in claims adjudication, country-specific tax code in ERP, and drug interaction check in a clinical system took years to get right, and you can't just re-derive it over a weekend. (Even if you tell the AI to "think extra hard and make it really good!")

4. **Customers cannot afford these to break**. You can A/B test your CRM. You can't A/B test a hospital. Switching costs in this category aren't measured in engineering effort, they're measured in patient safety, career-ending regulatory incidents, and people literally not getting paid.

5. **The "I'll just rebuild it myself" is difficult to scale beyond a single users, let alone tens of thousands of users**. Miessler rebuilding his own version of Zapier in a weekend is fun! But a healthcare network rebuilding Epic for 80,000 employees is a decade-long implementation that costs hundreds of millions and ends careers if it goes wrong.

None of this is new to anyone who's been around awhile. In the late '90s, [neophytes thought](https://www.citrix.com/blogs/2025/09/10/if-ai-is-normal-technology-boring-infrastructure-is-your-best-strategy/) web apps were going to eat desktop software. While that turned out to be largely true for horizontal desktop apps, the vertical ones that ran companies kept running companies. (Which is why Citrix was a thing in that era too.)

## AI dissolves UIs, not systems of record

Six months ago I wrote that we're entering [the post-application era](https://www.citrix.com/blogs/2025/10/01/welcome-to-the-post-application-era/), and argued that apps are dissolving. I still believe that, and that AI and [the cognitive stack](https://www.citrix.com/blogs/2026/02/25/understanding-the-cognitive-stack-why-your-ai-strategy-is-focused-on-the-wrong-layer/) will be the primary interface for most knowledge workers. But there's a difference between AI dissolving an interface versus AI dissolving a system of record.

The Epic UI is replaceable. The Epic database is not. The SAP screens are replaceable. The thirty years of tax logic and supply chain integrations are not. The mainframe green screen is replaceable. The backend running the Social Security system is not.

The real post-application era will be AI sitting between the worker and the system of record. The worker talks to the AI, the AI [reads the chart or the transaction or the claim or the fare](https://www.citrix.com/blogs/2025/10/15/will-ai-need-to-operate-your-legacy-desktop-apps/), reasons about it, proposes the next move, and commits the action. The system of record is what the AI reads from and writes back to. The worker changes how they work, but the system of record stays put.

## How long will this last?

Given enough time, AI will become capable enough to eat the deep layer of software too. A fully AI-native, FDA-cleared healthcare operating system could eventually displace Epic, and the same story could play out in ERP, airlines, and insurance. It's not impossible.

But the word "eventually" is doing a lot of work there. Enterprise planning horizons are three to five years, and even the most optimistic view of deep layer replacement puts it at a decade of migration, during which the transition runs inside the old systems. If you hear "AI is eating software" and jump to "therefore Epic is toast," you've compressed a 15-year transition into a 15-second meme.

So yes, AI is eating software. But it's eating a specific shallow layer of it, while the deep layer the real economy runs on needs AI to work alongside it, not instead of it. That's the part of the story that doesn't make it into the "I canceled my SaaS" posts, and it's the only story when you're thinking about what kind of software infrastructure companies are going to matter for the next decade.
