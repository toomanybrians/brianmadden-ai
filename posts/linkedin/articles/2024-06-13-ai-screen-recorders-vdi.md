---
title: "AI Screen Recorders + VDI: The ultimate secure, compliant, & powerful desktop?"
date: "2024-06-13"
authority_level: 5
file_type: linkedin-article
tags: [vdi, daas, ai-screen-recording, security, compliance, euc, microsoft-recall]
related_frameworks: [workspace-as-control-plane]
original_url: "https://www.linkedin.com/pulse/ai-screen-recorders-vdi-ultimate-secure-compliant-powerful-madden-fa5dc/"
staleness_threshold: stable
---

# AI Screen Recorders + VDI: The ultimate secure, compliant, & powerful desktop?

*Brian Madden—June 2024*
*Published: https://www.linkedin.com/pulse/ai-screen-recorders-vdi-ultimate-secure-compliant-powerful-madden-fa5dc/*

*Header image: Architectural diagram showing the flow from multiple inputs (DEX Analysis, HVD/Cloud Remote Desktop) through Screen & Text arriving at AI processing, with outputs to Compliance, Workforce Analysis, and other analytics. ILKI logo.*

I recently wrote about the upcoming Microsoft Recall feature, a forthcoming service that runs on your Windows computer and takes screenshots every few seconds which are processed by AI, allowing you to use an LLM to ask about past computing activities. While Microsoft is in the process of sorting out some security issues before its general release, I strongly believe that the enterprise use case for this technology will be massive, and that in a few years we'll see technologies like this become accepted and common at work. (For example, Apple just announced many new features leveraging AI-powered capabilities which access what's happening locally on a device. I'll do a full article on that next week.)

In my article on Recall (and my subsequent guest appearance on the Impact of AI: Explored podcast), I outlined how I envision the evolution of AI-powered screen recorders at work:

1. The security issues will get sorted out.
2. They will get smarter, from "what was that website with the pink logo I saw last week?" to full AI-powered assistants with human-level analytics of all activities on the device.
3. The value for companies will be centralizing this collected intelligence and analytics across their entire workforce.
4. This will be so valuable that market forces will require that all companies do this.

I then outlined several benefits and use cases for companies which I won't detail here, but the potential for companies is massive: security, business analytics, employee performance analysis, project and enterprise status, workforce management, and countless others.

## The quickest path to this? VDI!

One of the downsides of Microsoft Recall is that it requires a "Copilot+ PC", which means this capability won't come along until a hardware refresh cycle takes place and then it will only be available on certain devices. (Of course other vendors could offer similar products with different requirements, and screen recording and analysis solutions for enterprises have existed for decades.)

Back in May I wrote an article, "Why the enterprise desktop still matters in 2024", with the main takeaway being that the Windows desktop is still the easiest "aggregation point" for everything a company needs to deliver to an employee. And for more than a decade, VDI / DaaS has been sold as an effective way to "secure" that desktop, primarily by separating the enterprise security from the client endpoint. (I realize I'm steamrolling lots of nuance with that statement, but the gist is still largely true today. This is why private equity and big cloud providers are paying billions even in the 2020s for Citrix, VMware EUC, Cameyo, Frame, etc.)

## AI-powered screen recorders + VDI/DaaS is extremely attractive

Getting to the core point of this article, the opportunity is huge for AI-powered screen recorders to plug-in to the existing remote display delivery pipeline of today's VDI and DaaS solutions. This would have several advantages, including:

- The delivery technology exists today. There are existing APIs and methods to hook the protocol.
- Desktops already in the cloud can be "cloud-local" to the AI processing and storage facilities.
- The concept of recording a VDI desktop has existed for decades, and no one has freaked out about it.
- Employees are conceptually more comfortable with the remote desktop being a "work" thing, and less creeped out about it being tracked or recorded versus their client device.
- This recording technology would work across all applications, all endpoints, and all usage scenarios.
- The ability to secure this capability would not depend on the client endpoint.

This is the ultimate security solution which would be more effective than today's piecemeal solutions for DLP (data loss prevention). Rather than having a networking appliance that's trying to decrypt and sniff packets, or a security agent sitting between the browser and the app backend, or some web service connected to the database tier, why not just look at the screen?

I could envision multiple engines being hooked into the screen flow, each doing a different thing and provided by a different specialized vendor. For example:

- A **Compliance** product could look for sensitive and personally identifiable information and watch to ensure it's not sent outside the company. This would work via any app—corporate email, Slack, website, etc. It could also blur sensitive information based on the employee's conditional access level or the trust level of the client environment.
- A **DEX** (digital employee experience) product could look for performance issues: app crashes, alerts, slow times between click and launch, frustrated clicking, etc.
- A **Workforce Analytics** product could analyze what the employee is doing, understand if they're finding what they need or clicking around too much looking for things, track how they interact and with whom, etc.
- An **Archiving** product could do legal archiving, knowing that "everything" must go into the record (even if it's a personal app or site) while also knowing what not to put in the record. (e.g. Don't archive things the user typed but didn't send.)

These are just some quick ideas off the top of my head—there are certainly dozens more.

While VDI isn't strictly needed for each of these, they are all made easier when VDI is used. The non-VDI alternative would look like Microsoft Recall. You'd have to record the screens locally, then either store and process them locally, or compress and send them up to some service. Each of these would add more touch points, transmissions, and require more client processing capabilities. Or, just leverage the existing stream from the current VDI solution.

These capabilities don't have to be offered by the VDI/DaaS vendor itself, rather, the VDI vendor simply needs to provide a framework which third parties can plug-in to as needed and do what they do best. The result is the VDI vendor doesn't have to offer some half-baked compliance solution, and the top tier compliance vendor doesn't have to figure out how to install screen recording agents on a million different laptops. Win/win.

All of this can be integrated with other existing trust signals. (Where is the employee? What level of authentication did they use? What's the client device trust level?) This can be passed on to the various AI processors which allow capabilities to be dynamically tuned as needed. e.g. A client device moves to a public location, and instantly all PII (personally identifiable information) is blurred.

It's probable that things like this will be part of all devices everywhere in the future, but by focusing on VDI / DaaS use cases, this is something that could be in place relatively quickly and easily (both in terms of vendors providing these capabilities and the ability for companies to adopt them). I hope we soon see capabilities like this offered as subscription add-ons, so a customer can just click the "HIPAA compliance pack" for an extra $10/user/month and be all set.

Maybe 2024 really is the year of VDI after all?

*This text and header image are AI Influence Level 0: Human conceived & created with no AI assistance.*
