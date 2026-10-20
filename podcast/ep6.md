---
title: "EP 6: Why AI agents aren't in the enterprise yet"
date: "2026-10-16"
show: "Citrix AI Hotsheet"
hosts: [Brian Madden, Dave Brear]
format: Podcast (Brian's own show)
authority_level: 5
file_type: podcast
substack_subtitle: "Why enterprises aren't running AI agents, and the AI second brain as a harness"
tags: [ai-agents, enterprise-ai, trust-and-judgment, agent-governance, second-brain, harness, harness-engineering, knowledge-factory, always-on-agents, claw-likes, workspace, ai-bubble, open-weight-models, mcp, saas-chatbots, talent-pipeline]
staleness_threshold: stable
tier: 2
status: not-reviewed-by-human
model: claude-sonnet-5-5
---

# EP 6: Why AI agents aren't in the enterprise yet

*Citrix AI Hotsheet · Brian Madden & Dave Brear · October 16, 2026*

## Listen

- **Show home:** https://citrixaihotsheet.riverside.com/e/why-ai-agents-aren-t-in-the-enterprise-yet
- **Apple Podcasts:** https://podcasts.apple.com/us/podcast/why-ai-agents-arent-in-the-enterprise-yet/id1896776524?i=1000797118103
- **Spotify:** https://open.spotify.com/show/033jRLrUknFhvyEVCgzc3f
- **Amazon Music:** https://music.amazon.com/podcasts/c527d556-b9a1-42e9-b4f8-88062d81af4f/citrix-ai-hotsheet
- **YouTube:** https://www.youtube.com/watch?v=79A2YHUAzfQ
- **Substack show notes (canonical):** https://www.brianmadden.ai/p/citrix-ai-hotsheet-ep-6-why-enterprises

## Description

Every AI lab is selling always-on agents. When Brian asked enterprise CIOs how they govern theirs, they told him the question sounds absurd. Brian and Dave on why trust and judgment are the blocker, not guardrails. Then Dave explains why he stopped building his own harness, and why your IP belongs in the harness, not the model.

Two main topics this episode, and the second one grew out of the first.

**Why enterprises aren't running AI agents**

Every AI lab is selling agents: multi-agents, always-on agents, agents with their own sandboxes. OpenAI dots, Meta Muse, Microsoft Autopilot, and the rest of what Ethan Mollick calls the claw-likes. Brian spent time with CIOs, CTOs, and CISOs at the WSJ Technology Council Summit, and when he asked how they govern the agents running in their environment, the answer was that the question sounds absurd. They've done a project or two that proved AI works. Many already run an AI gateway and can see every token. What they can't see is the path from "agents will help your workers" to anything they'd actually deploy.

Dave's diagnosis is trust and judgment. AI shows up first where judgment is low and playbooks exist, like HR and IT chatbots. Agents compress execution to almost nothing and magnify judgment, so the good calls of strong people and the bad calls of weak people both get bigger. His example: leaders walk into a QBR with a printed stack of prep that someone else pulled together. AI now gives everyone that same preparation. What's left is knowing which questions to ask.

Brian goes further than he has before. He's argued for a long time that agents are just another kind of worker, governed with the same guardrails. He still believes that, but guardrails were never the limiting factor. Even with every guardrail in place, how do you know the agent shares your intentions? And the capabilities the benchmarks measure (how well AI uses a computer) aren't the capabilities a business cares about (how trustworthy it is, and how likely it is to not try to hack you).

Dave adds the cost nobody's counting: if agents do the junior work, where do the next leaders come from? Brian closes the segment with an idea from David Jack. The company's second brain already holds how the organization works: which apps to use, who to ask when something breaks, what the requirements are. Agents could read it to learn how to do their job, and be verified against it afterward.

**The second brain as a harness**

Every SaaS app now has a chatbot that knows its own data and nothing about you. Dave's workaround: he plans in his second brain, which knows what lives in Gainsight, Looker, and Power BI. Then it writes the prompts he pastes into each tool, narrowing step by step like a set of Russian dolls, and pulls the results back for him to think with. Brian realizes he'd been doing it backwards, trying to give each chatbot more context, when the second brain should brief them instead. That's also safer, since nobody knows what model or data agreement sits behind each sidebar chatbot.

Brian argues this human gateway between systems is going to last a while. Connecting everything through MCP is solvable, but it's a project, and IT teams buried in patching put it at priority number 9,000.

Then Dave explains why he backed out of the custom UI he'd built for his second brain. He'd accidentally been building his own harness, and the harnesses in Claude Code and GitHub Copilot are far better than anything he could make. The work worth doing is extending the vendor's harness with what's specific to you: which systems hold which data, which are reachable, how you like to work, your skills.

Brian walks through what a harness is (the model is the brain, the harness is the body), why harness quality moves benchmark results, and how Claude now manages his parallel threads for him instead of the other way around. His conclusion: put your IP in the harness, not the model. If the bubble pops or a lab disappears, you swap in an open-weight model and keep going. And going back to a talk he gave at BriForum 2012, the Windows desktop was a harness all along, connecting the worker to apps, data, security, and policy.

## Topics covered

- Why enterprises aren't running AI agents: customers asked how they govern agents in their environment say the question sounds absurd
- What CIOs, CTOs and CISOs at the WSJ Technology Council Summit said: AI is real, but handing everyone Copilot is not the value
- AI gateways show the spend and the models, but not what to do about them
- Dave: trust and judgment are the blocker; AI shows up first where playbooks exist, like HR and IT chatbots
- Agents compress execution and magnify judgment, good and bad
- The QBR example: AI removes the preparation gap, so judgment is the scarce thing
- Which capability? Benchmarks measure computer use; businesses care about trustworthiness
- The "claw-likes" (OpenAI dots, Meta Muse, Microsoft Autopilot, Ethan Mollick's term) and why they recalibrated Brian's view
- Guardrails were never the limiting factor
- The talent pipeline problem when agents do the junior work
- The second brain as guardrails for agents, and as the thing you verify them against (an idea from a colleague, David Jack)
- Every SaaS app's chatbot knows its own data and nothing about you
- Dave's babushka-doll prompting: the second brain as a briefing engine for each tool's chatbot
- Why not just turn on MCP: priority number 9,000, and the human worker as the gateway between systems
- Dave backs out of the custom UI he built for his second brain after hitting the harness wall
- What a harness is: the model is the brain, the harness is the body; harness quality moves benchmark results
- Dave's wider definition of a harness: the map of data sources, the environment, skills and a master prompt
- Brian's terminal windows versus Dave's UI
- Markdown versus HTML as the format for second brains
- Claude threads talking to each other, and Claude managing parallel agents instead of eight terminal windows
- Harness engineering as its own segment, with knowledge factories as part of the harness
- Put your IP in the harness, not the model: swapping Gemini 4 Argon, Opus and GPT-6 in the same harness, and the bubble-pop tie-in
- Is the second brain a harness?
- BriForum 2012: the Windows desktop was a harness
- Why agents aren't more prolific in the enterprise: they don't have the right harnesses to control them yet

## Chapters

*(Timestamps are copied from the Substack show notes — verify against Riverside before final upload.)*

- 0:00 — Welcome: six weeks is six years
- 0:30 — Agents everywhere, and customers asking what we're talking about
- 1:44 — CIOs at the WSJ Technology Council Summit
- 2:31 — You don't get value just by handing out Copilot
- 3:20 — The AI gateway shows the spend. So what?
- 4:44 — Dave: trust and judgment
- 6:19 — Why chatbots came first
- 8:36 — Dave: the QBR stack of printed prep
- 10:33 — Which capability? Benchmarks vs. trust
- 12:00 — Brian doesn't let agents run amok on his desktop
- 12:37 — The claw-likes: OpenAI dots, Meta Muse, Autopilot
- 13:32 — Guardrails were never the limiting factor
- 14:31 — Dave: what happens to the talent pipeline
- 15:18 — The second brain as guardrails for agents
- 18:36 — Using the second brain to verify agents
- 19:32 — Dave briefs every SaaS chatbot from his second brain
- 20:08 — Every SaaS app's chatbot knows nothing about you
- 20:52 — Gainsight, Looker, Power BI: prompts that narrow like Russian dolls
- 24:02 — Don't give the SaaS chatbot your context
- 25:07 — The second brain as a briefing engine
- 25:45 — Dave hits the harness wall
- 26:59 — Sanctioned second brains inside Citrix
- 27:51 — Why not just turn on MCP?
- 29:30 — Priority number 9,000
- 29:50 — The human gateway between systems
- 31:21 — Dave: the harness includes your environment
- 33:07 — What a harness is: the brain and the body
- 35:19 — Dave was building his own harness
- 36:07 — Brian's terminal vs. Dave's beautiful UI
- 38:10 — Markdown vs. HTML
- 40:22 — Claude threads talking to each other
- 40:56 — The mark of a good harness
- 41:40 — Harness, not model: eight terminal windows and a Paris view
- 43:52 — Your second brain is part of the harness
- 44:43 — Harness engineering as its own segment
- 45:52 — Put your IP in the harness, not the model
- 47:31 — Same harness, different models
- 48:04 — Is the second brain a harness?
- 48:43 — BriForum 2012: the desktop was a harness
- 50:17 — Agents don't have the right harnesses yet
- 50:32 — Wrap

## Links mentioned

- [WSJ Technology Council Summit (September 2026)](https://leadershipinstitute.wsj.com/technology/event/technology-council-summit-september-2026/) — where Brian spoke with CIOs, CTOs and CISOs
- [Ethan Mollick on the "claw-likes" (X post)](https://x.com/emollick/status/2105000480569212984)
- [Why Markdown isn't the format AI should use (YouTube short)](https://www.youtube.com/watch?v=3DGN5kuG2xQ)
- [Brian: What Will Knowledge Work Be in 18 Months? Look at What AI Is Doing to Coding Right Now (Citrix, 2026)](https://www.citrix.com/blogs/2026-02/what-will-knowledge-work-be-in-18-months-look-at-what-ai-is-doing-to-coding-right-now)
- [Brian: How to build an AI strategy that survives the bubble pop (Citrix, 2026)](https://www.citrix.com/blogs/2026-07/how-to-build-an-ai-strategy-that-survives-the-bubble-pop)
- [Brian: The Desktop Has Dissolved—Now Where Does Work Live in 2025? (Citrix, 2025)](https://www.citrix.com/blogs/2025-05/the-desktop-has-dissolved-now-where-does-work-live-in-2025)
- [Citrix SecurSpaces](https://www.citrix.com/platform-flex/securspaces.html)
- [NetScaler AI Gateway](https://docs.netscaler.com/en-us/citrix-adc/current-release/ai-gateway.html)
- [EP 5: AI Knowledge Factories — Company-Wide Second Brains](https://www.youtube.com/watch?v=z_9wLRgjh24) · [Substack show notes](https://www.brianmadden.ai/p/citrix-ai-hotsheet-episode5-ai-knowledge)
- Brian's second brain: https://brianmadden.ai
- Dave's second brain: https://davebrear.ai

---

## Transcript

**Brian Madden**
Hello, it's October 16th, 2026, and you're listening to the Citrix AI Hotsheet Podcast. My name is Brian Madden with Citrix, and I'm joined as always by my Citrix colleague Dave Brear. It's been about six weeks since our last episode, and I feel like in the world of AI, even corporate enterprise AI, six weeks is like six years.

So I want to jump right into our main topic. Dave, like you, I spend a lot of time talking to customers and understanding where they are with AI: AI and their workers, AI and their users, everything. There's all this narrative about AI agents. Agents, agents, agents, right? Everything's about agents. Now it's about multi-agents. Now all of the AI labs are giving their agents virtual sandboxes to operate in, so they're always-on agents. It's all about agents doing work and connecting that work into your environment, and it feels like the whole world is moving in that direction.

Then I look at what we're doing internally and I think, my gosh, are we behind? What's going on? And when I talk to customers about this, I ask, "Where are you with AI agents running in your environment? How do you govern them? What are you doing?" And they're just like, "What are you even talking about right now?"

**Dave Brear**
We're not. Yeah, absolutely. And just to your point about six weeks being a long time: for the last few years, I can't remember ever feeling so out of the loop when I come back from a simple week's vacation. I come back and the landscape has completely changed. So yeah, I think we've got a lot to talk about.

**Brian Madden**
Okay, well, here we are as your Sherpas, to use the word our colleague Rick Dehlinger uses.

So let's get into it. About a month ago I was in New York City at the WSJ Technology Council Summit. It was about AI agents and AI in the enterprise, and all of the attendees were CIOs, CTOs, or CISOs of very legitimate, large, global companies. I had a lot of conversations with them, and whether it was the sessions or the hallway conversations, it was all kind of the same. They're like, "Look, we get that AI is real." We've gone beyond "is it proving value?"

I think everyone understands that you don't get value in the enterprise just by delivering Copilot to all of your workers. I'm not saying Copilot isn't valuable, but you can't just say, "Here, you all have Copilot, check, next project." They get that. And I think they understand, like we talked about on the last show, that if you build new business processes around AI and transform them, and spend a lot of work with forward-deployed engineers re-engineering things, you get value. Everyone understands that. All the CIOs I talked to have done a project or two where they can see, "Okay, yes, AI provides value for us."

I also feel like a lot of people are using some kind of AI gateway or MCP gateway. At Citrix we have our NetScaler AI Gateway, other vendors have their things, and that lets you centralize your connections to AI. All the AI a company provides to its workers can run through a gateway, so you can see which users are using it, what models they're using, token spend, model routing. A lot of people have that today. Not everyone. And by the way, if you're a Citrix customer, it's a checkbox. Turn it on.

But that's not the point. People have that today, and the CIOs are like, "Okay, I can see all the spend and all the models and everything that's happening, but what do I do with this? Does a lot of spend mean we're doing really well and I should enable more of it? Or does a lot of spend mean I need to dial this back?" Everyone gets that AI is capable of providing value. But how do I actually incorporate it into the day-to-day running of my business? How do I look at all the processes my workers are doing today, figure out what's a waste of time and what's good time, and make that work?

The AI labs say that's where agents come in, working alongside your workers. And there's just no real pathway from the marketing platitude of "agents can help your workers" to "how do I actually make that happen in my environment?"

**Dave Brear**
Yeah. I think it's an intersection of trust and judgment that's stopping this. If you look at where AI is being deployed in enterprises, it's for well-trodden pathways, well-trodden workflows. It's a centralized chatbot to handle HR and IT queries. It's those kinds of things, where the judgment required is lower because there are playbooks to follow, and the trust is therefore higher.

What stops us pushing out agents to act on individuals' behalf more widely is that right now there's a lack of trust that an AI agent will act appropriately on my behalf. And at an enterprise level, judgment is something that comes with experience and seniority. AI agents can compress execution and make it cost almost nothing from a user's perspective, but they really magnify judgment. People with seniority, good judgment, and good instincts are going to get magnified, and they're really going to go out and be impactful. But there are also people with less good judgment who need more guidance, and just setting an AI agent loose is going to magnify their bad judgment at the same time.

**Brian Madden**
I like that. AI can increase the velocity, whether that's of good decisions or bad decisions.

**Dave Brear**
Yeah, absolutely.

**Brian Madden**
It's interesting what you said about starting with the things that don't require a lot of judgment, like chatbots. Having AI chatbots, and I'm using finger quotes, has been a thing for ten years, since long before LLMs. Part of the reason that was easier (finger quotes again, I'll just finger quote throughout this whole conversation) is that a customer service rep doesn't need a lot of judgment. There are playbooks, there are scripts, there are flowcharts. It's almost like an expert system from the nineties rather than a judgment-based system. So that's easier for AI to do.

But when you get into true knowledge work (I was going to say what we talked about last show with the knowledge factories, but even before that), knowledge work is based on imprecise information and having, I think they call it taste, to understand: "I've got all this imprecise information, I have to balance all these things. What playbook am I running? How do I know what to do? What decisions do I make?" It's hard enough to trust your human employees to make all the right calls. So the idea that an agent is going to act like that, especially today's agents, when everything in the news is about how agents are extremely tenacious and will do whatever it takes to get what they perceive as their goal done...

I guess this comes full circle. When I'm talking to customers and asking where they are with agents, I feel like I'm having sophisticated conversations with enterprise customers: "How do you manage your regulated environment and your controls, and what the agents are allowed to see and not allowed to see?" And they're like, "We don't, because we don't do that. What you're saying sounds absurd."

**Dave Brear**
Absolutely. A way of thinking about this for me: I was in a QBR a couple of weeks ago, and leadership turns up with a printed stack of preparation materials. On the surface, those leaders have very different resources to me. They ask what they want the data to show, somebody goes away, pulls that data, prepares it for them, and they come in heavily prepared. They open up their data and away they go.

But the reality is that AI agents, and AI in general, make that something I can do too. I can ask the same questions, I can have AI agents pull the data for me, and we can turn up to that meeting with a similar level of preparation. So the difference in resources for execution has been completely removed.

What qualifies me to ask the right questions, the good questions, is the real commodity here. It's the judgment. It's understanding what the right questions are to ask. Have we missed anything in the data that makes my preparation different from theirs? Individuals need to trust that when an agent executes on their behalf, it's doing it the way they would. Leaders need to trust that when you scale everybody up, the average and the superb employees, and magnify their impact with AI, it's not going to upset the apple cart of their whole business operating model.

For me, that's why it's going to take time for agents to really proliferate. Even though the capability is there, the trust and the judgment need to be proven at a smaller scale before either the employee or the business will feel comfortable rolling them out.

**Brian Madden**
It's funny. You say the capability is there, but it makes me think, which capability? AI is created by scientists and technologists, so all of the benchmarks are "look how good AI is at using a computer," or "look how good AI is at this kind of task." So the capabilities are going up, up, up. But the capability a business cares about is: how trustworthy is it? How reliable is it? How likely is it to not try to hack me?

As you were talking about with the QBR (and it doesn't have to be a QBR), we have human managers with a lot of experience in the industry and the company who know what's important and what's not. You say, "Here's all the uncertainty and all the information and everything we need to know," and the manager can pluck out the priorities and how to navigate things. Yes, a junior employee can use AI to get the same answers, but how do we know those answers are the same ones a senior person would want? Then take that same approach another level down to the AI agent itself, autonomously doing its thing. There's no way.

I'd say this about myself. I don't have AI agents that run amok in my desktop computing environment. They don't touch all the applications. I have the ability to pull data from applications and they can read some things here and there, but everything they're doing is with me, in conversation. I'm having conversations with it and we're talking about it. But the idea that I'm going to let an agent go do things for me? I just feel like we're farther away from that than the narrative suggests.

Since our last show, always-on agents are the big thing, and we've seen them everywhere. There's OpenAI dots, there's Meta Muse. I think Muse is the big one that everyone is losing their mind over online right now. It's a personal agent. These are all based on OpenClaw. Microsoft has Autopilot, which is a similar thing, also built on OpenClaw. Ethan Mollick, by the way, calls these things the "claw-likes": all these always-on agents built on OpenClaw principles or using the OpenClaw open source project as a foundation.

So there are all these claw-likes, and consumers out in the world are running Meta Muse, and it's running around doing things for them and failing in hilarious ways. The idea that that comes into the enterprise? I think we're so far away from it that it's actually recalibrated my worldview.

I was really big on "AI agents are just another type of worker. You manage them with the same guardrails. You can put guardrails on human workers, you can put guardrails on agents." I still believe that's absolutely true. You absolutely can put guardrails around agents. But that doesn't mean enterprises are going to use them, because the limiting factor was never the guardrails. Yes, the guardrails are a baseline prerequisite. I'm obviously not letting an agent come anywhere near anything corporate if it doesn't have guardrails and I can't record it and all that. But even with all the guardrails, how do I know this little robot buddy is living on planet Earth with the same intentions I have?

**Dave Brear**
And that's before we've even talked about the impact on an enterprise of farming out the junior and entry-level work that would normally be the talent pipeline for the industry. If agents do all these things for us, maybe our leaders don't need their staff to prepare that briefing for them. Then where are the next leaders coming from, the ones who learn by being their hands? It's more than just technology, and it's more than just trust. It's also about what letting something run amok in your business does to things you wouldn't even think about as a first-order effect of deploying it.

**Brian Madden**
I had a conversation with another colleague, David Jack, who you know too, about the second brain. We talked in our last episode about the corporate second brain, and how within Citrix we call these knowledge factories. David Jack is our man within Citrix for conceptualizing, operating, and engineering all of that. One of the conversations I had with him recently was about using the second brain as guardrails for the agents.

What I mean is this. I've written quite a bit in the past, and maybe we've talked about it on previous episodes, about how if you look at what's happening in software development with AI, it's a preview of what's going to happen in knowledge work. Software developers were the first ones to have always-on agents, and all those things eventually make their way into knowledge work. You can continue that analogy and say that whatever knowledge workers are doing now is a preview of how agents are going to operate in the future.

So how does that tie together here? We're using AI as a second brain. Famously (well, famously in my world), Dave, you're the one who showed me we could do that, almost a year ago now. You're using AI as a second brain, I'm using it as a second brain, and the knowledge factories companies are starting to build internally are group-level, departmental-level second brains.

Listen to the last episode if you want the full details, but the second brain holds the truth layer of what our enterprise is. And it's not just which facts are true, it's how you do your job. What applications do you use? How does this process work? When this breaks, who do you ask? What are the requirements? What are the guidelines? How does everything work?

So we had this conversation with David. When a junior employee comes into a company, they almost don't know what to do. In our case, at Citrix, you log into our application portal and there are, I don't know, 10,000 applications on there. That's cool. I use like five. Are there others I should be using? I don't even know. The AI version of that is agents. Everything has an MCP server, you give an AI agent free rein, and it starts connecting to MCP servers and finding things on its own. And it's like, "Whoa, dude. What are you trying to do right now?" "Well, I need to make this report." "Okay, here's how you do that."

The second brain contains that information about how the organization works and how things should operate. So I feel like there's an opportunity for AI agents to use the second brain themselves. I always thought about the second brain as being consumed by humans, but AI agents could use it too, to learn what to do and how to do their job as an agent.

Then I was thinking you could take it one step further. Yes, use it for the guardrails, but also use it for verification. As the agent is operating and doing its thing, whether you're looking at the outputs or even recording the session and watching it work, you can compare what it did against what's in the second brain and make sure the agent is actually doing the right thing. In this whole conversation about how you even know the agents are doing the right thing (air quotes), the second brain could help both guide them and verify them. Directionally that makes sense to me. But we're not there.

**Dave Brear**
Absolutely. And in a crude way, this is exactly how I'm using my second brain today. We have a bunch of systems where we don't have MCP connections, or where I can't let my agent talk to those data sources directly. But those tools all have their own version of a chatbot, a copilot, a wingman, whatever, and we can talk to those and get insights from the data that's in them. It's detached from the fact that my second brain has a ton of relevant context. So what I've taken to doing is...

**Brian Madden**
Sorry, I want to interrupt you, because I want to underscore what you just said. You're smiling right now, but I'm so frustrated by this. I just want to make sure people are following.

**Dave Brear**
Yeah, it's frustrating.

**Brian Madden**
Every SaaS app on planet Earth now has its own little AI buddy chatbot sidebar. Everything has a chatbot built in. Those chatbots are good, and they know everything about that application, but they don't know the rest. I have a second brain with my whole context and everything I'm doing, and then there's the chatbot in our corporate SaaS tools, and it doesn't know any of my context. So it's kind of worthless to me, because it doesn't know what I'm doing. It only knows how to use this dumb application. I've largely ignored them.

**Dave Brear**
So let me tell you how I've solved this horrible problem. I had a conversation with my second brain and told it about all the places where stuff might be. We're a Gainsight customer, so Gainsight, Looker, Power BI, whatever, and I told it exactly what type of information is in each of them. With Gainsight, our CRM tool, I've been quite descriptive about all the different fields that are in there. So it understands what data lives in each of these tools.

Then I start my thinking in my second brain: "Right, I really want to dig into this problem." Between the two of us, we decide, "We're probably going to get some good information from over here, some good information from over here, and we're definitely going to get something from over here as well." Together we come up with a strategy for how we're going to prompt each of the individual little wingmen in all these other tools. It gives me prompt one for the CRM tool. I paste that in and give it the results back, and it goes, "That's interesting. Here's the follow-up prompt for the CRM tool." Then, "Great. Now here's one for Power BI. Paste that into Power BI."

**Brian Madden**
Wait. So you're querying your second brain and saying, "I have these three corporate tools with dumb agents in them. Hey, second brain, I've got to do some work on this customer. Give me the prompt I should take to that thing."

**Dave Brear**
Yeah, exactly. But only after... we've talked before about compression versus expansion workflows, and this is very much an expansion workflow. I'm probably having a very long chat about what I'm trying to do here. What kind of information am I looking for? What's my working hypothesis, the thing I'm trying to prove, disprove, or support? What's the issue I'm trying to investigate?

**Brian Madden**
And that's with your second brain.

**Dave Brear**
That's with my second brain. Then it goes, "Okay, this is the plan. We're going to speak to X, Y, and Z." It's a babushka-doll set of decreasing prompts. We start wide with a dataset, then we query a subset of those accounts, then we query a subset of that, and we end up with a small list at the end. Then we take that and compare it with the telemetry data that's in another system, and do the same thing there. Once I've got all that information in my second brain, I do my thinking, and I come up with something that combines all of it.

But it's frustrating that I can't just say, "Go out and do this." I can't speak to each of these tools individually, because first of all they have no idea what the others are doing, and also all the context in my second brain is locked in there and completely useless unless I use it this way.

**Brian Madden**
Sorry, I was going to say that's kind of good. Just assume I've got air quotes around everything I say on this entire show. But it's kind of good, because I don't know what the random chatbot on the side of our SaaS application is. If it's a corporate SaaS application, I assume it's secure and vetted, but who knows what model it is, who knows what agreement it has, who knows if it's saving all the conversations or whatever.

I was always thinking about this backwards. I was always trying to give the chatbot in the SaaS app as much context as it needed to do well for me. That's kind of dangerous and backwards. You're just giving it simple queries to get results, and taking the results from the SaaS app into your second brain, rather than trying to make the SaaS app's AI work like a little mini second brain for that SaaS app.

**Dave Brear**
Exactly. In an ideal world we'll be able to connect these things in a far more seamless way, and my context, the knowledge factory company context, and all the different systems will all add together. But right now my second brain is, as often as not, a briefing engine for something else. That might be a human I need to send something to: "Explain this thing I need done," and then I'm checking it, tweaking it, making it sound more like me, and sending it out. Or it's queries going to other systems.

And as I say that, I have a thought that might take us onto another topic, so slow me down if you want to stay on this a bit longer. We've talked before about how I've been designing different user interfaces for my second brain. I coded a graph view with investigation boards and all kinds of ways of looking at data. They were useful to a point, but I hit a massive brick wall, which is relevant to what we're talking about. The interface was really useful and compelling, but I found myself spending far more time trying to overcome the shortcomings of the harness underneath it. I can use the same models for my second brain when I'm using Claude Code or GitHub Copilot or whatever, but their harnesses are just so much better than anything I could create. I was spending so much time trying to rebuild the harness that I've largely backed all of this out.

**Brian Madden**
Okay, let's put a pin in that, because I want to ask you about it. But I want to close the loop on the previous topic first.

For newer listeners: Dave and I both have AI second brains approved by Citrix, running inside the Citrix corporate system on the Citrix corporate AI subscriptions with all the guardrails. These aren't personal Claude subscriptions. They're sanctioned. So we're allowed to have our corporate information in there, customers and all that, because it's in the corporate silo. Same with these applications. We're not talking about personal apps. These are our actual corporate CRM, contracting, telemetry, all of it. It's all corporate, within the Citrix silo.

**Dave Brear**
Mm-hmm.

**Brian Madden**
A lot of these applications have MCP servers too. And to your point, Dave, maybe prompting our second brain to extract what we need from these other business apps is temporary, because we should have MCP servers set up. That's the frustration I was starting the show with. In my mind I'm like, "Hey, it's all Citrix, we're all internal, we're all behind the firewall. Just turn on MCP. What's the problem?"

As a sidebar, I've also said this to a lot of people. Cloud Software Group is a big, multi-thousand-employee, multi-billion-dollar company. We're a real company with a lot of safety and security guardrails and compliance. So there are a lot of things we can or can't do, which is sort of frustrating, but it's also exactly what all of our customers are dealing with. Figuring out how to solve this properly helps us understand how customers are going to solve it properly.

So in my mind, why can't we just turn on all these MCP connections to models we already own? And this goes back to the roundtables I mentioned at the beginning. I asked customers, "Do you have AI agents running in your enterprise? Are your users working with them?" And they come back with, "I'm so busy. I have so much on my plate with general security, the velocity of patching, the velocity of changes. There's so much I have to deal with, and that's priority zero. 'I want to connect your AI system to this application, can you verify it' is priority number 9,000."

So where I'm going with this is that the human worker, with human knowledge and human judgment, acting as the human gateway between different systems, is probably going to be a thing for a while. In theory these things can all talk to each other, but even if you connect them through your corporate-controlled MCP gateway that logs tokens and does DLP or whatever, it's not that simple. Yes, that's all solvable. But it's a project. It requires people to stop and think about it, practice, and build a plan. And with everything else happening so fast, they just don't have time to do that project right now.

The AI industry narrative is that all these things can talk to each other, and there are a million vendors popping up claiming to solve exactly this problem. But just because a problem can be solved in theory with technology that exists in the universe doesn't mean companies are going to solve it anytime soon. So what you're describing is going to be a thing individual knowledge workers deal with for a while.

**Dave Brear**
Absolutely. And tying it back to where I was going: I realized the AI harness is something I'd have to rewrite from the ground up, and there was little value in that. So I've come back. But in coming back, I've also expanded my concept of what a harness actually is.

I thought we had the models, and then a harness that was entirely provided by a vendor like Microsoft or Anthropic. But I think the harness also includes the map of which data sources are available to it, which of them are offline, which are reachable, how we interact with them, and the operating rules around all of that. So the harness extends to my understanding of the working environment as well.

So I'm not investing time rebuilding a harness from the ground up. I'm investing that same time in extending the harness with my environment and workflow. I know the CRM has this data, telemetry has that data, and everything in between. I'm filling in that understanding with skills and a master prompt, to expand the harness so it's useful in my environment. And right now a lot of that harness work is bridging systems. "Bridging" actually sounds like a scary word from a security perspective, and I'm not doing anything I shouldn't. But I am allowing the context from all those unrelated systems to come in. For me, that's the harness work worth investing in.

**Brian Madden**
Okay, I've got a lot of questions. First, let's level-set on what a harness is. The analogy I've been using is that the AI model itself is like a brain. Tokens go in, tokens come out, and that's it. The model by itself can't do anything. So the AI labs and vendors aren't just building models. They're building the wrapper, or the harness, around the model that determines how it interacts with the world.

The first harness was a chat interface: a conversation history, you type this, now I type. Then we had Cowork, we had coding interfaces, and now we have the claw-likes. You could say the harness is the body you put the brain in. Same brain, but you could put it in a bipedal human-style body, a car, or an airplane, and which body it's in controls what it's able to do in the world.

A couple of other points. There are open source harnesses, GitHub projects for different harnesses. So you might love Claude Opus 5.5 but use it through one of those open source harnesses that you have more control over, instead of as a chatbot or through Cowork. And there are benchmarks showing that the quality of the harness really affects how well the model functions. Same base model, same context window, same settings. Actually, the settings are part of the harness too, like how hard it tries. The model spits something out, and the harness might come back and say, "Try harder, spend more tokens." So changing your harness can really affect how good the model is.

**Dave Brear**
And that disparity is what sent me running back to something I'm not developing myself, from a harness perspective.

**Brian Madden**
So you were building your own harness.

**Dave Brear**
I was, and it only occurred to me halfway through that that's what I was doing. I was focused on the user interface. I wanted it to show this, and I wanted it to show that, but then it wouldn't respond the way I wanted when I asked it a question. And I realized I was spending all my time inventing functionality that GitHub Copilot just does. So why am I doing this? Because I want a nice UI. But if I bear with it, I'm sure somebody's going to solve fluid UI, to use the term we were talking about earlier before this, long before I create a good harness. So I'm stepping back.

**Brian Madden**
Okay, this is a great conversation for me, because I didn't realize that was what you were doing. It didn't occur to me that it was a thing.

For those listening: a lot of us at Citrix use our Citrix SecurSpaces product as our agent workspace for knowledge work, and we run our second brains there. Dave, you showed me yours a month or so ago, and it had this beautiful UI. You could pull conversations, drag things in, see the sources. It was gorgeous. I was super jealous.

Meanwhile I'm using my second brain via, like, a DOS prompt. It's not literally DOS, it's PowerShell or whatever, but it's text in, text out. I have a voice-to-text thing and I'm talking to it, but fundamentally I'm just using a bunch of terminal windows, and you have this whole beautiful interface. I was going to ask Claude (again, my corporate, behind-the-Citrix-firewall Claude), "Hey, my coworker has a really cool interface. I want one too. Can you build it for me?" I just haven't had time.

So what I'm hearing is: you build a UI, and that's cool, but then you want this, and this, and now do this, change that, and all of a sudden you're like, "Dang, I'm building my own harness now." And the data shows harness quality really affects model quality. So congratulations, you just built a worse version, with more work, of something that already exists.

**Dave Brear**
Yep. So I've gained more by going back to the DOS-style system you're talking about. But I'm putting a lot of trust in somebody solving the UI down the line, and I think we already see that in what the native Claude apps are doing and in new ways of visualizing data. I saw something the other day where somebody asked whether Markdown is actually the right format for second brains, or whether it should be HTML. They made the case that HTML might be more appropriate because it's so rich and you can display things however you want. So I'm trusting that somebody else will solve that over time, and I'm happy sticking with my older workflow for now.

**Brian Madden**
I saw that same thing. My wife and I like to watch the late-night comedy shows, The Daily Show and Jimmy Kimmel and so on, on YouTube on the living room TV. But it's my YouTube account, so it always has my recommendations. Just the other night, there was that video about why Markdown isn't the format AI should use. I was like, "What?" I was going to add it to my watch-later list from the Apple remote, but then she ran out to refill her wine or something, and I started watching it. And I'm like, "My gosh, HTML! Whoa, this blows my mind." She walks back in and I'm reacting like I just saw the most mind-blowing thing ever, and she's just like, "You are such a nerd."

But it was interesting. HTML is richer than Markdown. Yes, HTML can be bloated, but it doesn't have to be. And we're not super token-limited anymore as token prices come down and context windows get longer. That's a different conversation. But it's interesting to me that the actual UIs, which are part of the harnesses the vendors provide, are getting really good now. Now there's Claude Docs, and Claude itself has multiple windows open.

Have you ever been running multiple processes in Claude and asked it to check with the other processes? I'll say, "I've got another thread over here," and it's like, "I see another thread doing something, I'll wait." And I said, "Actually, I think that thread's working on something else. Can you ask that thread what it's doing?" And it's like, "Sure." And I was like, "Whoa, that works." Then you go into the conversation history and you literally see, "Hi, I'm thread whatever. I'm working on this. What are you doing?" You see them talking to each other and figuring it out.

**Dave Brear**
That, for me, is the mark of a good harness. When you think of something new you want to do and you ask it, you don't hit "Well, you didn't think about that when you were writing the system prompt, Dave, so no, I can't do that for you." It just does it, or maybe it does something that surprises you. It's like my first uses of Claude Code last year, when it got really good over Christmas. You ask it to do something and boom, you've got a tool at the other end that does exactly that. "Wow, I thought I needed to solve a problem, and it solved it." Nobody taught it how to do that. The harness was just good enough to respond. That's what a good harness does.

**Brian Madden**
And that's the harness, not the model. Harness technology, for lack of a better word, is evolving too. We might think "it's getting better" and accidentally attribute the improvement to better models, when it might be that harness engineering is improving.

I think back to when I first learned about the second brain, obviously from you. I think we talked about this on one of the shows. I went nuts. I actually got a second monitor and was running eight Claude windows. These were all terminal windows, but I was using iTerm so I could give them different colors and all that. After about six weeks I took the second monitor out, because (a) I have this beautiful window with a view of a Paris street, so why block it with a monitor? And (b) I was spending all my time managing them. I was forgetting which window was what, they were sitting there waiting for my input, and it was just too much. I couldn't do it.

Now I notice Claude manages these for me. If I'm doing some process, it's like, "Okay, I'm going to kick this off in a subagent, and this one too, and why don't you start working on that and let me know when you're done, and I'll be over here." It's like the old Yakov Smirnoff joke: with Claude, Claude manages you. I don't manage Claude agents anymore. I don't manage those fleets. It's telling me, "Why don't you go do this with your dumb little human head, and I'll be over here working, and I'll pull it together." Claude opens multiple windows, tracks everything, and brings it to my attention.

So even at the very simple level, trying to manage multiple Claude agents in their own PowerShell windows at the same time was too much for my feeble human brain. Letting the agent do it through a modern harness is much more efficient and effective, and I'm not reinventing the wheel and slowing myself down.

**Dave Brear**
Absolutely. And let me restate the point that started this discussion, because I don't think I made it clearly. Since coming back, I've updated my understanding of a harness. It's not just the thing the LLM providers give us. There are elements of my second brain that I see as part of the harness: these are the tools available to us, these are the ways I like to work, these are the skills I've developed. I'd rather spend time building that side of the harness to tailor it to my environment and my usage. It's the model, plus the capabilities the frontier providers give it, plus the additional harness briefing we provide in our second brain through skills and system instructions.

**Brian Madden**
I wonder if this is what companies are going to build themselves. Remember when AI first came out (this time around, in 2022 with LLMs), it was all about customizing your own models. It was about RAG and training your own models, and everyone said, "I'm going to train my own model because I want my own dataset, or I want it to work my way." People have largely stopped doing that, especially for general-purpose models, because the next model always came out and was better than any customization a company could do.

But I wonder if harnesses could be their own segment. Harness engineering. Maybe that's almost what we're doing at Citrix. Going back to what we run on SecurSpaces, which again is a real product you can buy and use too, that's how we run our second brains internally and our corporate knowledge spaces.

**Dave Brear**
And the knowledge factories we were talking about. They're part of the harness. Yes, absolutely.

**Brian Madden**
Exactly. That's a harness. What David Jack is building is essentially a harness. And this is interesting too, because, boy, where's your IP? Forget the model. Put your IP in the harness.

And this leads back to what happens when the bubble pops. I wrote a blog about this a few months ago. A lot of people believe the pace of investment and the economics are going to pop at some point. I don't know if it's next week or next year, but at some point the economy might collapse and AI investment might vanish, and people will focus hard on where the actual ROI is once a lot of the hype dies down. Maybe some of these AI companies go out of business.

What I wrote in that article was that there are open-weight models, and because their weights are open, they'll always be available. Even if you're using a closed frontier model from a commercial lab, you might want to be ready to use open-weight models in case something happens to that lab, or in case you need sovereignty. What's nice about open models is you can run them in your own data center, or with a provider in your own country or sovereign area. So if you really put your investment into the harness, you can in theory swap models out willy-nilly, and that's fine, because your IP, the structure, how it works with your company, the security, the guardrails, all of that is in the harness, not the model.

**Dave Brear**
Absolutely. The coding harness I'm using for my second brain lets me put in whatever model I want. I was messing about with the Gemini... I've forgotten the name of it.

**Brian Madden**
Gemini 4. Argon or something?

**Dave Brear**
Yeah, there are two releases of it. Gemini 4 Argon, that's it. I was messing about with Argon, running the same workflows on my same harness with Argon versus Opus versus GPT-6. That is indeed the way this is going.

**Brian Madden**
I guess the second brain in general is just a harness.

**Dave Brear**
You could say it's a combination. I think we probably stray beyond the definition of a harness, because beyond the harness there's the environment, and the environment is where the model, the harness, and the data all meet and interact. The second brain definitely has environmental bits in it too. But yes, you're right, huge parts of the second brain are harness. I have a folder-based approach, and there's an underscore system folder right at the top with my skills and briefings. That is absolutely harness, pure and simple.

**Brian Madden**
You start thinking about the workspace and the definition of a workspace. I gave a talk at BriForum 2012, fourteen years ago. That sounds obscure, but I brought it back in a blog post a while ago, which is how I remember it: the elements of a workspace. We look at the Windows desktop and call it a desktop, but it has a lot of components. It has a UI, applications, a security context, data, a profile, preferences, all of that.

So you could almost argue that the Windows desktop was a harness for connecting the worker to data, apps, device, security, and policy. That becomes fungible, or disintermediated, as you evolve toward different UIs. And whatever we're talking about here is kind of the same thing. If you ask what the modern digital workspace is in the AI world, it's this. There are MCP connections to data, maybe applications you're connecting to on the desktop, in the cloud, wherever, and it's all coming together. I feel like the digital workspace of the future is this AI harness something-something, all coming together.

I feel like I need to go lie down and think about this for a while.

**Dave Brear**
Yeah, absolutely. I think there's also a connection back to why AI agents aren't more prolific in the enterprise. The answer probably comes back to: they just don't have the right harnesses to control them yet.

**Brian Madden**
Yeah. I think that's a perfect spot to end today's episode. I have a lot of ideas for future conversations. We can explore more of this together, maybe in some blog posts. This is a fascinating topic. Thank you for blowing my mind today, Dave.

**Dave Brear**
Happy to do that.

**Brian Madden**
Thank you all for listening. We won't go six weeks next time. We'll be back in the middle of November to pick up where we left off, though I'm sure our thinking will have evolved quite a bit and we'll have lots of fun experiment results to share. So thank you all so much for listening, and we'll be back soon.

**Dave Brear**
Thank you, bye.
