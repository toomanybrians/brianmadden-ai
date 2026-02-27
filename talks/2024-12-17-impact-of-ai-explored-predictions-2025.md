---
title: "The 2025 AI revolution: predictions and impact"
date: "2024-12-17"
event: "Impact of AI: Explored podcast"
hosts: James O'Regan, Gerjon Kunst
location: EUC Forum, London (recorded in person)
format: Podcast guest appearance
recording: https://www.youtube.com/watch?v=KJLp-KSbSu8
authority_level: 5
file_type: talk
tags: [ai-agents, computer-using-agents, windows-desktop, vdi, claude-computer-use, open-source-models, workplace-ai, shadow-ai, ai-predictions, non-human-licensing, physical-ai]
staleness_threshold: stable
---

# Impact of AI: Explored - December 17, 2024

## Episode details

**Title:** The 2025 AI Revolution: Predictions & Impact

**Context:** Brian's second appearance, recorded in person at EUC Forum in London. At this point he was still an independent consultant. The conversation is a year-end review and forward look, with heavy focus on AI agents entering the enterprise through Windows desktops, the Claude computer use demo, non-human licensing questions, and the democratization of AI through open-source models.

**Key arguments made:**
- 2025 will be the year of AI agents, and they'll enter the enterprise through Windows desktops
- The easiest path to agentic AI is letting AI use existing computer environments rather than building new cloud-native agent infrastructure
- Desktop environments already have all the security, compliance, and connectivity infrastructure that agents need
- Non-human user licensing is a completely unsolved problem that someone needs to crack
- Open-source models running on consumer hardware (MacBooks, $4-5K GPU boxes) mean AI can't be gatekept the way search engines were
- "It's not model collapse, it's not end of scaling—it's just going in a million directions and a million dimensions all at the same time"
- AI on phones and native voice interfaces are changing how people interact (Brian using ChatGPT voice for French practice in Paris)
- Shadow AI is now pervasive among non-tech workers: "I am really kind of blown away by how many of my friends are using AI at work on the download"
- Physical AI and humanoid robots are coming faster than expected
- VDI is having a resurgence driven by AI agent needs

> **Note:** This is a condensed transcript highlighting Brian's key arguments, not a verbatim word-for-word record. The full episode is ~45 minutes of conversation. Refer to the [original video](https://www.youtube.com/watch?v=KJLp-KSbSu8) for the complete discussion.

## Transcript

Hi everyone, welcome to the latest Impact of AI Explored. We are here live at EUC Forum in London and we have brought back Brian Madden, in person this time instead of remotely. Hello. Hey Brian, how are you doing?

I'm well. I live in Paris now so I'm not jet-lagged. That's nice. I'm just recovering because I just got back from Ignite.

So how are you, Gerjon? Great, excited to be here and looking forward to talking to you. Live, Brian. Last time we spoke digitally, that was fun, was a really good episode. And this episode should be even more fun.

Yeah, we have six more months of experience in AI.

And in AI, that's a lifetime. It is, it is. You'll see in our presentation later, we did a tweet from like one day and it was like ten announcements just from ten different companies. It's insane the rate of change.

So we wanted to kind of—this is the last episode of 2024, we'll be back in 2025. But what we wanted to talk about is where we're at, and actually I wanted to talk more about what you were talking about in your session earlier on about AI agents, because it seems like 2025 is going to be all about AI agents. And for me, that's where things get interesting. We're not—it's not passive anymore. They're doing things, they're interacting. It takes it to the next level. We've had chat, we've had voice, whereas now they're going to be doing actions. And we talked previously about how we still need that human interaction but we are giving more control away. So you just laid it out, which I think was really interesting, about how we've always talked about Windows desktops and that they will become obsolete, but you actually laid out a whole thesis about Windows desktops and their importance with AI agents. Do you want to lay that out?

Yeah, certainly. Great show, guys, by the way. I'd love to be like a second-time guest now. This is awesome.

You're our most featured guest.

Super. Yeah, you know, the AI agents, to your point, that's just all the news. We're recording this in November of 2024 and it seems like every company is talking about agent-like AI that can take actions on your behalf. And I think the easy way to think about this is just like little examples. Like there's a lot of things where I'm like, "Oh, I'm going to order Five Guys Burgers via DoorDash." I get the same thing always. I want to be—hey, I'm not going to say that loud because our phones are going to wake up—but like, "Hey assistant, give me two burgers from Five Guys." And like, any kind of reasonably smart AI that knows me and looks at my order history and my computer—it ought to be able to do that on my behalf somehow.

And I don't know how that works exactly. Some people are talking about agents that run in the cloud and they can talk to DoorDash's API or the agents can start to do things. There's no real architecture defined for this; it's just that AI can take action on your behalf. And I kind of feel like, when I start thinking about that as a concept for work—because all my AI stuff is about the office, the enterprise, the EUC lens—well, how do we do that at work?

Like every human job, there's probably 200 little tasks you do if you wrote down every little thing. And they're all different—some require your brain and some don't. Like expense reports is just go through, find receipts, put them in. An AI agent should be able to do my expenses. That would be amazing.

The low-hanging fruit, right? Oh God, that would be so good.

But I think about it—it's not going to be like the easiest way to do my expense report, through Expensify or some API, because it needs access to all my things. I need my Windows desktop to do my expense report because it's my photo library with a receipt, it's my calendar to see I was at this thing, it's my credit card to download the statement, start to match. How do you do it? You find the expense and search your email box for it, fingers crossed you have a receipt, then you search your photos for it. AI can do that, but I feel like the AI agent to really do that properly needs to do it on my desktop. It actually needs to take control of my mouse and keyboard because it needs my photos, my email, my Amex account, all these things.

So what you're kind of talking about is the example we've seen at the moment, Anthropic's computer use, which is a very early-stage use case of what you were talking about, essentially.

Yeah. Like I feel like the path to AI agents or agentic AI, the path to that is to let AI use our computer. People were like, "Oh my gosh, you mean you want AI to use a Windows desktop? Are you out of your mind? Windows is old and bloated and we've been trying to kill Windows!" And I'm like, yeah, we have been trying to kill Windows for like 30 years. Windows was going to be dead because of Java and HTML and Chrome and web apps and mobile. All these things were going to kill Windows and here it is, about to be 2025, and we still have millions and millions of enterprise Windows desktops.

So my thinking is, if you want AI agents to start performing actions that human workers perform, you give the agent the Windows desktop. The idea that you're going to set up some agent working in a Docker container in the cloud and it's going to have a connector into this app and a connector into here and then you got to build all this new security infrastructure and connector infrastructure—it's crazy. Whereas it's all encapsulated in a Windows desktop already. We don't need to reinvent the wheel.

And if you think about the expense report example, it is going to all these web services and brokers and load balancers, it's going through my security software. It's all there but it's done because I already have the expense app, my credit card app, my photos—it's already collected together on the desktop.

And what I told you before we started is, we do this at customers. We try AI agents for proof of values or just to fiddle around with it. But the moment—if you have Copilot for Microsoft 365 you have a button that says "AI agent," you click on that, that's easy. Then you go to Copilot Studio, that's also easy. Then you have to build a chatbot and then you have to use Power Automate to make connections and you have to have APIs and security in place. Then it gets really complicated really fast. And then everybody is thinking, "This shouldn't be this hard," but it really is that hard at the moment.

Like all the RPA vendors are now AI agent vendors, which is fine, they have a good pathway. But really, my whole thing—the whole point of my talk—was I'm not saying this is right around the corner because Claude computer use is a great example. People can go to YouTube and type in "Claude computer use demo." It makes mistakes, it's kind of dumb, it's like the older versions of ChatGPT. And everyone has this litmus test where they ask some crazy PhD question and it gets it wrong and I'm like, well, most humans get it wrong too. We're the ones training these things so there's going to be imperfections.

Especially if you want to crawl, walk, run—we already have existing infrastructure for all of our human users to do all their jobs. All of us have some tasks that are simple and AI can do, like my expense report example. Maybe an AI agent can do that today, maybe that's going to be in three or six months. An AI agent is going to be able to make my expense report way sooner than it's able to create a PowerPoint presentation for me. If I could have it do like the two easiest tasks today, that's great, I only have 198 to do. People say, "Well, I don't need AI for that." And I'm like, yeah, I don't need AI for my expense reports either, but it's going to do two today, three next month, five the month after that. And then suddenly I have four or five extra hours in a week where I can do more work, do less work, do deeper work, sleep.

And as you said, it's not working as good now, but drip drip drip, it's going to suck less. It's going to keep improving. And in six months we don't know how good it's going to get because the AI development is not going like this [flat], it's going like this [up].

You know, Ethan Mollick always says you're using the worst AI in the world at this moment. So we have no idea what six months looks like.

And it's exponentially increasing. And we have these crazy high expectations—I'm sure all three of us are not median employees, we're above the median, which means the average employee is like worse than us. So if the AI is dumber than us, hey, half the people in the world are dumber than me. All our listeners are probably above average. It's the old thing with self-driving cars where a self-driving car doesn't have to be better than the best human driver, it has to be better than the worst human driver. And the same with agents—it just has to be better than my worst employee, not my best employee, to provide value.

Now, looking back at this year. Is there something that stood out as a pivoting moment in 2024?

That's a great question. ChatGPT has been publicly released for less than two years still. It's not even November 30th yet. Under two years. That's crazy.

For me, a few things happened this year. Obviously AI agents—that's really just the past couple months where it started to hit hard. I think the other thing I realized is I was definitely one of the ones waiting for ChatGPT-5, ChatGPT-6. Like, going from 1 to 2 to 3 to 4 went from preschool kid to high school to college to grad student. And I'm realizing that the foundational models—there's a lot they can do to change the way they work. They can change all these tweaks under the hood, don't change the core model but change the content they've brought in. Things like multimodal, because we now can do voice on desktop. Reasoning. The Canvas, which is the interactive one.

So they've tweaked it. We haven't had a jump with the model but we've tweaked the way we can use it and utilize it. It's definitely a better user experience. It's like in the old days of processors—we just put more megahertz and made it go faster, then we had larger address spaces, then we had coprocessors, then multiple cores, multiple types. You start expanding up and there's still a lot of growth to go in these core models, but also start going out.

And recognizing that we're not seeing model collapse. We're not seeing end of scaling. It's just going in a million directions and a million dimensions all at the same time.

I think for next year, the democratization of AI. Open-source models you can run on your own. For $5,000 you can have a box that does a lot of stuff that is basically unrestrained, really darn close to what leading models are doing. You can customize it, no guardrails, whatever you want. The core technologies you can truly do on your own in your basement. And a MacBook M2 or M3 can run fairly complex models on your laptop. You can take it with you.

The other thing is physical AI. Robots in factories, Tesla Optimus, humanoid robots that can walk around and lift 50 pounds for under $50,000. Ones folding laundry and emptying the dishwasher. In our lifetimes there will be home humanoid assistants. Pretty wild.

For me, most of my work is thinking about this through the lens of end-user computing. How do we protect, how do we enable, what's an organization look like. I've never been so unsure of the future while being so excited about the future.
