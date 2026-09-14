---
title: "You can't transform the AI you can't see"
date: 2026-09-14
url: https://www.citrix.com/blogs/2026/09/14/you-cant-transform-the-ai-you-cant-see/
tags: [shadow-ai, ai-visibility, ai-governance, workspace-as-control-plane, agent-identity, knowledge-factory, mcp-security, netscaler]
authority_level: 5
file_type: blog
staleness_threshold: stable
tier: 2
status: reviewed
---

# You can't transform the AI you can't see

Most companies treat their AI problems as strategy problems, which they attempt to address in the traditional ways: by creating committees, evaluating platforms, and running pilots … all in the hopes of finding a clear answer to which AI models, vendors, and use cases they should actually commit to.

Meanwhile, AI has already come into every company from every direction. Workers are using it via personal accounts on unmanaged devices. SaaS applications now ship with AI assistants built in. Individual departments are starting pilots with their own token sources. IT has bought everyone Copilot licenses, (though they're unsure what they're being used for or whether it's even worth it. The workers wonder the same thing.) And even for companies that put up all the "proper" security guardrails, workers just point their phones at their laptop screens and snap whatever's there to run through their own personal AI subscriptions anyway.

All this is happening now, before most companies have fully figured out their AI strategies. So rather than asking, "Which AI platform should we standardize on?" The actual questions you should be asking are, "What AI is running in your company right now?" "What data does it reach?" "Whose identity is it using?" And, "Who can see it?"

Most companies still can't answer those seemingly basic questions. And until they can, every other AI decision is being made blind.

## Why AI is different from last decade's shadow IT

Most people's first instinct is to treat this as "the next round of shadow IT," which provides comfort. The thinking is, "Hey! We have a playbook for the consumerization of IT, and this is just more of that." It's a big relief.

But the reality is that AI is different this time.

Regardless of whether companies actually believe that, the social pressure to speed-run AI adoption means they're spending real money trying to find the right kind of AI for their workers. But no matter what they do, workers keep using their own personal AI for work things. The shadow AI gap isn't closing even though companies are following the consumerization playbook perfectly.

Fortunately, the path forward is actually pretty clear once you reframe the reality on the ground: AI is here. You're not going to block it or remove it. Your only real choice is whether you can see it or not.

## Start with visibility

Most business AI conversations focus on "transformation." Transformation implies new platforms, workflows, and ways of working that most companies frankly just aren't ready for. But workers are ready, and they're experiencing more and more "AI Moments" where they catch themselves thinking, "Wow, AI was really good at that." Unfortunately most workers are having this experience via personal AI subscriptions they're also using for work, whether or not it's sanctioned. They've been using AI like this for years by now. They have first-hand experience of how much better it gets every month. They know this trendline will continue and are constantly mulling over which bits of their work they'll try to hand over to the next model.

That said, all these workers thinking about their own personal AI transformations still means the company will eventually have to do a proper top-down system, process, and workflow transformation. That'll happen in every organization sooner or later.

So is there a logical first step to take today? Yes, and it's simple. You can't redesign work you can't see. The amazing "transformation" everyone is talking about (including me)—whether you undertake it in 6 weeks or 6 months or 6 years—can't even begin until you've done the unglamorous work first. So that's something you can tackle now regardless.

That first step is visibility. You need visibility to know what's actually happening with AI in your company. This visibility isn't an alternative to transformation. It's just step one of the transformation itself and a step you can actually take this quarter before you've fully committed to a platform, model, or vision. Your immediate goal needs to be getting visibility and governance of the AI already running in your company. Even if you don't fully know what that means yet, just making this a "real project"—starting the abstract discussions about AI visibility—is a great first step towards AI transformation.

This is more important than just focusing on AI purely from the security angle (lock it down, compliance check, done), as that could lead you to chasing the wrong problem while real business value is being captured by AI that's accumulating somewhere else.

The good news is that implementing visibility doesn't require new ideas. It's the same access, governance, and control playbooks we've run in IT for decades. Let's walk through each of these playbooks, pointed to AI.

## Access: know what's connecting and who it really is

Your first play is discovery. If your company pays for AI (an enterprise account with a model provider, a cloud AI service, any of the many copilots) then that traffic can be routed through infrastructure you already run. (Such as NetScaler AI Gateway or MCP Gateway, both features of NetScaler you can just turn on.) Once enterprise AI traffic starts going through a single gateway, you can see it. That gives you an initial snapshot of which people use which apps with which models, how much, and how often. Most companies who do this are surprised by the results in both directions: the AI tools they pay for are barely touched, while AI services nobody approved are everywhere.

The next play is identity, which is one of the areas where AI is genuinely different from previous tech waves. When an AI agent does something in a typical corporate environment, it usually acts as the person who launched it. It inherits every permission that person randomly accumulated over the years, and it enthusiastically uses whatever route it can to get the job done. I cannot imagine any company wants random AI agents exploring the full extent of an employee's access on their own initiative.

The fix is straightforward: give agents their own accounts, with their own restricted rights, just like you would for any service that acts on the system. Vendors are also just starting to release products to address this specifically, like cryptographic agent identities, task-scoped permissions, and agent directories.

But that fix is now a platitude. In the real world, you'll never convince your CISO and IT to give all your workers additional user accounts for their AI agents. We now live in a world where swarms of AI agents spontaneously working together to route around the corporate guardrails that limited their permissions now actively happens.

Unsurprisingly, most companies can't provision a single restricted-rights non-human account, let alone thousands. If you make "figure out how AI will login to our systems" an actual project, you'll do more for your AI security than almost anything else on this list.

Once you sort out your agent identity approach, isolating agents will be more straightforward. Agents can run in their own sessions, with their own identity and their own boundary, while still appearing to the worker seamlessly, right alongside their other applications. In practice it's a simple configuration change: give the agent its own Citrix DaaS session and publish it to the human worker via HDX and seamless windows. The worker AI use experience doesn't change, just the security boundary does.

## Governance: record it, meter it, and act on what you see

Because AI agents are just software programs operating in your own environment, you can record everything they do: simulated keystrokes, mouse movements, screens, etc. You can turn on every security option you have for them. (If PII or other sensitive information must not be captured, it can be redacted at the source before it's observed, transmitted, or viewed.) The result is a complete, replayable record of what the AI did, available to an auditor from day one.

Token consumption is also now a real thing that needs to be governed. It's no longer enough to only track how many (and what type) of tokens each worker burned. Now you need to know things like which apps they use and why each model was chosen. But once you consolidate all your AI app usage through a single NetScaler gateway, you can get real answers to questions like this (as well as having a central point to apply cost, intelligence, DLP, or other controls).

Centralizing your AI traffic also means you can act on what you (or your AI) sees something suspicious. If a session shows an agent operating with a human's credentials, you can alert on it, record it, shadow it live, disconnect it, or log the user off. Those triggers already exist in most enterprise environments. You just have to configure them for a new kind of event.

## Control: govern the AI protocols

Enterprise app makers are stumble-racing towards new AI strategies and ways to provide AI interaction with their apps. There's convergence around MCP, which does a lot of useful things, but to recycle the old joke: the "S" in "MCP" stands for "security." That doesn't mean companies can't use it. It just means they have to wrap their own security layer around it.

This isn't new. When HTTP came out, it didn't have security either. But the web still became safe for credit card payments because HTTP got wrapped in something that handled identity and encryption, and people learned to look for the padlock before typing in a card number.

MCP is in the pre-padlock stage right now. From the enterprise standpoint, the playbook is the same as it was for the web. Don't wait for the protocol to grow up. Deliver it through infrastructure you have today that already does identity, inspection, and policy. If MCP traffic runs through a gateway that knows who the client is, what it's allowed to reach, and what's in the payload, the protocol's immaturity isn't a problem.

The same logic applies at every layer you control. The device, network, egress point, browser, app, session, and data layer each give you a place to see and shape what AI is doing. (These are all layers that Citrix secures as well.) Most companies spent decades building controls at all of those layers for human workers. You don't have to change them, just aim them at AI too. In many cases you don't even need to buy anything new to do it.

## None of this requires a "migration"

The opening plays of the enterprise AI agent playbook are the same no matter how quickly the future unfolds. Think about how everything you provide to human workers might be provided to AI agents working on their behalf.

Nothing here requires a migration. There's no re-platforming. You're not forced to integrate AI in ways your existing apps can't support. Your regulated systems of record stay exactly where they are, running exactly as they do today. The published desktop your workers use is the same desktop their AIs use.

In many companies, especially in established, regulated industries, random AI will never be allowed to wander and run amok across existing apps, infrastructure, and workflows that have to stay. But "stay" means only that this existing infrastructure stays the same. How it's used will change significantly, as your existing EUC estate will become the connective tissue between your existing systems and the AI that works across them. It will feed the AI its raw material and receive the AI's outputs back. The controls you run today for your human workers are the same controls you'll run tomorrow for your human workers and AI agents.

Again, none of the approaches outlined here require you to be right about the future. But that doesn't mean you can wait. Companies have burned two years waiting for the models to be good enough. They are now (and not only the frontier ones). Even the mid-tier and open-weight models anyone can get today are genuinely capable at the whole job: computer use, app use, reasoning, long-horizon work… all of it. The models can do the work. What they're missing is the 80% of knowledge work that lives in people's heads, and that's an organizational knowledge problem to solve, not a model to wait for.

Most people feel (understandably) overwhelmed, but continuing to do nothing is not a smart option. Doing nothing means the AI in your building keeps running exactly as it is, growing at frontier speed, totally unobserved. Every month that passes is another month of activity nobody governed, analyzed, or learned from.

Fortunately the decision you need to make is low-risk, because everything described here is a configuration, not a transformation: create an account, publish an app, set some policies, wire up some guardrails & triggers. AI is advancing much faster than any enterprise can adopt it, so committing to a single platform can rightfully feel dangerous. But nothing here is committing you to one. If your strategic direction changes in six months, or the model you standardized on is superseded, or the board decides on something else entirely—you just have to delete an account and a published app. You haven't lost six months walking a path you now have to walk back.

## Visibility is the on-ramp, not the destination

Everything I wrote so far is framed as governance, and it is. But each of those governance points is also a point of observation. Once you've instrumented your company to govern AI, you've instrumented it to see something no company has ever been able to see clearly: how the work actually happens.

Consider what a company really knows about its own work today. It sees the artifacts of knowledge work: the docs, email, transcripts, chat messages, files, etc. That's what every knowledge management system, search tool, and enterprise AI assistant is built on top of. But all those artifacts aren't the knowledge work. They're the evidence that knowledge work happened.

The actual work is the judgment, reasoning, and sequences of small decisions a skilled person makes without writing any of it down, as well as the workarounds nobody documented because nobody ever officially sanctioned them. That part has never been digitized, and it's why just pointing AI at your shared doc repository produces confident-sounding answers that anyone doing the actual job knows are wrong.

Once you've instrumented your EUC estate for AI governance, you can start to see what matters: which applications people move between, where the same information gets re-entered three times, which tasks take twenty minutes and shouldn't, where the process on paper diverges from the one people actually follow, etc. Understanding and addressing these are the real questions, and so much more complex than, "Is our AI usage compliant?" But how your company addresses these real questions will define how successful your company will be with AI.

And once you start to get answers to these "real" questions, what do you do with that data? This is where the real transformation starts to take place. I've been calling the destination the knowledge factory—the AI second brain built at the scale of a department or a company, which I went deep on in a recent episode of the Citrix AI Hotsheet.

It's a canonical layer containing the tacit knowledge of how your organization actually works, but digitized, version-controlled, and machine-readable for the first time. It's quite literally the new source code of the business and potentially the most sensitive thing your company has ever put in one place. (Which you're going to ask IT to protect.)

That's the whole point of this post: your company's canon needs the exact same access, governance, and control discipline you already implemented for the AI agents operating in your existing estate. The governance you build to see the AI in your estate today is the same governance the factory runs on.

So visibility isn't a box you check and file away. It is your on-ramp to reorganizing the work itself around AI. This is the real transformation. The companies who get there first will be the ones who instrumented themselves first. I'll go deeper on how you actually build that factory in the next post. (I have real-world first-hand experience here. We are building them within Citrix.) But the prerequisite is the same no matter what path you ultimately take, and you can start this quarter. You can't improve, reorganize, or even reason about work you can't see.

So start seeing.
