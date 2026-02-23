---
title: "The Evolution and Future of End-User Computing"
date: "2024-11-26"
event: EUC Forum Winter Meeting 2024
location: London, UK
audience: EUC practitioners, IT professionals
format: Keynote with slides
recording: https://www.youtube.com/watch?v=wFgfFT3ILZo
authority_level: 5
file_type: talk
tags: [ai-agents, windows-desktop, computer-using-agents, workspace-as-control-plane, vdi, euc-history, agentic-ai, microsoft-recall, citrix, workplace-ai, vdi-for-agents]
staleness_threshold: stable
---

# EUC Forum Winter Meeting 2024 — November 26

## Talk details

**Title:** The evolution and future of end-user computing

**Abstract:** Ten reasons why AI agents will enter the enterprise through Windows desktops. Brian argues that agentic AI will use the same tools humans use rather than requiring native rebuilds, and that remoted Windows desktops provide the security, compliance, scalability, and audit trails needed to bring AI into the workforce. Covers the Windows Agent Arena, Claude computer use, Microsoft Recall's evolution, and why this transition period will last far longer than anyone expects.

> **Note:** This transcript was machine-generated from a YouTube video and may contain errors including misheard words, incorrect names, and inaccurate technical terms. Please refer to the [original video](https://www.youtube.com/watch?v=wFgfFT3ILZo) before quoting.

## Transcript

**Neil (Emcee):** Now we're into the next part of the event. We've done the updates and everything like that. Now we roll out some of the superstars of this era. We've got Brian first.

Brian's got a massive track record of years and years of doing these sort of events. Actually, I met Brian many times and tried to explain to him and his colleague Gabe Knuth about cricket. I don't know if you remember that. We took you to a cricket ground actually. I was in Leeds. The Leeds Rhinos was the rugby, yes. You did a great job of explaining cricket.

**Brian:** Yeah, exactly.

**Neil:** This is what explaining cricket is like. We've been talking for a long time and I haven't learned anything yet.

**Brian:** Yeah, yeah, exactly.

**Neil:** And then I started talking about Test matches—they're five days long. How could you have something that lasts five days? But that's in the past. So it's brilliant to have Brian here to talk about the evolution and future of EUC. He's written all these slides. Well, most of these slides. He wrote most of these slides last night.

**Brian:** It's Brian's usual way.

**Neil:** I'll leave him. He's got an hour going. He's got 42 minutes and 18 seconds. So I'll shut up and let you get on. Right on.

**Brian:** Thanks, Neil. Thanks to all of you. Thanks to the EUC Forum. This is my first time speaking in the UK since COVID, right? Like it was virtual and this. So it's great. I really appreciate the opportunity to be here. Neil's correct—these slides I was working on on the train over here. This is new content. That's what you don't hear. It's just created here. You get brand new, world premiere content.

So the talk that I submitted months and months ago is called The Evolution and Future of EUC. My name is Brian Madden. I am currently unemployed—which is, I'm sorry—I'm an independent consultant based in Paris. So I live in Paris now, which means I'm here not jet-lagged, which is kind of nice.

We're going to talk about the evolution and future of EUC. Of course, that's going to inevitably lead us to some topics around artificial intelligence.

This presentation is AI Influence Level 0. That QR code's got the explanation. I believe we should disclose how much AI is helping us with the presentations. This presentation—AI Level 0—all human created with no AI involved. Any images that were used with AI have been marked as so.

Anyway, we're talking about AI. What is this AI thing? To me, the term AI means a lot of things. So I sort of define AI and break it down to a couple of different categories. There's AI research. These are people who are moving the science of the field forward—building the models, tuning the models, submitting papers to scientific journals and things like this, doing theory work. This is not me, by the way. This might be some of what you're working on.

But when we think about AI in the world of EUC, it's not usually this. There's consumer AI. This is what LinkedIn is full of—prompt guides, practical LLM usage, AI for dummies, all these kinds of things.

I think there's a type of AI which I will call operational AI—again, not really EUC related, but this is what a lot of our companies are doing. You know, if you're a financial institution, you're using it to look at fraud. If you're a healthcare organization, you're using it to figure out patient care. Legal applications doing case law, things like that. This is where AI is part of your core business.

And then the last piece of AI is the term I sort of made up. I'm not trying to take credit for this. I'm saying don't blame me if you hear something else. I call it workplace AI. Workplace AI is like the extension of the digital workspace. This is the employee-facing AI. So when all of your employees or workers start using AI on their own, they're using ChatGPT, Microsoft Copilot. They're auto-creating documents and summarizations and this kind of stuff. This is AI that affects the workplace. This is typically managed by IT.

This workplace AI is really the world that I live in. We all live in consumer AI as well because we're all using ChatGPT to like write us dirty lyrics for songs and this kind of stuff. But the workplace AI is what affects our day jobs. As we think about the end user computing and the future of end user computing, workplace or workspace AI is really part of that conversation.

This is the world. My background—I'm now officially over 30 years in IT. I started in May of 1994. My past few years I've been really focusing on workplace AI. I've been writing quite a bit. I've been writing on LinkedIn mostly, but I've written several articles over the past year or so about workplace AI. Kind of like the stuff I was doing on brianmadden.com, looking at vendors, looking at strategies, things like that.

I also created a website called strategyguide.ai, which is kind of my personal site where I'm trying to figure out what this workplace AI is, how do we deal with it, how do we deal with employees and workers, all that sort of thing. So that exists. You can look at that. Not really what I'm talking about today, but that's what I've been doing.

This workplace AI is how I've been spending my time for the past couple of years—trying to figure out where end user computing is going and how AI is going to impact that. That's really what I'm talking about today. Over the years, end user computing has evolved. These are just some of the things. When we began we talked about remote desktops—that was like Citrix in the 90s—got to remote apps, app publishing, VDI, unified endpoint management, SaaS applications, SASE, zero trust, like all these things. These technologies are part of the EUC umbrella.

We saw the same thing from what we called it. Even EUC was not a term that we used 30 years ago. It was "Any app, any device, anywhere." It was digital workplace. It was the future of work, whatever those terms are going to be.

I think right now we're very much going into a world that people are calling the intelligence age. And that to me means if we're thinking differently about the future of end-user computing, the technologies are going to probably evolve along with it. Like AI agents, for example, is what I've been mostly interested in most recently.

So AI agents—a direction we're heading with end-user computing as we're entering this intelligence age. This is called agentic AI, which is a college term for AI agents. So when you hear agentic AI, you can sound smarter. There's a lot of ways to sound smart in the AI world just by throwing around acronyms and terms. So in that sense, it's not that different than what we've been doing for the past 30 years.

But AI agents is really what I want to talk about today. I'm not going to talk about the whole future of EUC or everything where it's going and what all the companies are doing. I've just been kind of going down a deep rabbit hole myself about agentic AI or AI agents. To me it's super fascinating and really interesting and going to impact the future of end-user computing.

So today I'm going to talk about agentic AI as my chosen topic. When I think about the future of EUC, here's kind of where my brain goes. And I'm not inventing this stuff, right? I'm reading about AI and AI advancements just like all of you. I just happen to be thinking about it through the lens of end-user computing.

Sam Altman has a website. It's IA—because it's the intelligence age—so ia.samaltman.com. And he posted on there about AI agents. He wrote: "AI models will soon serve as autonomous personal assistants who carry out specific tasks on our behalf, such as recording, coordinating medical care, et cetera."

So this is something a lot of people are starting to talk about—what AI agents are going to mean for how humans interact with computers moving forward. As an example, you know, if you use ChatGPT today, you can use it to help you with lots of things. Like I'm going to go see Wicked in Paris tonight. There's two of us and I want you to find a restaurant. ChatGPT can search and pick restaurants and maybe figure out where it is and that sort of thing. But it's not making the reservation for me or doing anything. It's just helping me collect some information.

So that's sort of where we are today. The idea is in a world that has AI agents or agentic AI, I give it a similar prompt. I say like figure out a dinner option for tonight. Then this AI agent is able to go and look at my calendar. It sees I'm going to see Wicked, where Wicked is. It sees I've got two people on the invite, or maybe it's got the receipt for the tickets. It knows the theater, it knows the time, it finds a restaurant, it contacts the restaurant and actually makes the reservation—whether it's through an API or through one of these reservation websites, maybe it's faking a voice and actually calling the restaurant. It will add it onto my calendar.

So the idea is the agent, the AI agent, is actually doing work on my behalf versus just providing me with information. This is a very simple example for personal life. But if we think about this as an AI agent, like how does this thing exist? How would we build this? Now, for most of us as consumers, we're not building it. Like Apple gives it to us or Google or Microsoft or some other company that's worth billions of dollars that you've never heard of, and they're going to build it for us. But how would they actually build that? What would that look like?

This is AI-generated. I prompted ChatGPT to give me a simplified version of native AI infrastructure. You can look at this—your security scanner, custom data, like location, GUI emulator, ethics review, failover mechanisms, custom analysis (like what I just said, where that agent goes in your calendar and figures out what you're seeing—Wicked—and finds a restaurant). It would look like this on the back end. It really would.

So from the consumer standpoint, other people are building that in the apps that we use. But this is what's really happening in the back end if you think about it. Okay, that's how they build it for the public. But how would we build this like in the enterprise? What if we wanted to take this agentic AI and bring it into our enterprise? Now we have to build this thing.

So what do we need to think about to make agents that can sort of act on behalf of our workers and do things like our workers do? We have to think about all the app integration because I don't only work in one application. I've got multiple apps, websites, plugins, that kind of thing. I got to think about the application runtime. This app's Windows, this is the back end, this is SaaS, this is web. I got to figure out how I'm interacting with the apps to launch them. I have to figure out the security context and the guardrails—who the user is and what they're able to see and not see. I have to think about the user interface. I have to think about provisioning—where is this app being deployed to, who has access to it, how does it all run. I have to think about how it's interacting with all the hardware it's running on. I have to think about the configuration, containers, all this kind of stuff.

These are all the things. If I want to build an AI agent for my enterprise, I have to think about all this stuff. At first this might seem like it's a lot to sort of deal with. But then you start to realize—wait a minute—we already have a place that brings all this together. It's the Windows desktop.

You may have seen—I've used these slides for like 15 years. Same category, same colors. Like all the things that come together on the Windows desktop—the Windows desktop is my app integration, it's my app container, it's my UI, my security context, my application runtimes, my plugins, my hardware interface, the configuration provisioning target. It does all this stuff today.

So it's like if I want to make an AI agent that operates in my enterprise, I already have one location where all this stuff is pulled together and it's already sort of talking to each other.

If I think about the desktop, what's nice is I can look at all the applications and things I'm doing on my desktop and kind of blow them up and then imagine that AI agents could use the desktop as their way to talk to each other. So one agent can go to the desktop, can use one application. That application gets data from a different application. A different agent uses that application. A different agent uses the first application. Another one uses another application which goes to the third one. All these things that I want agents to do—if they're really going to emulate me as a human to do the things I do—they need to use the tools that I use, which is the Windows desktop and the Windows applications and all that sort of thing.

And that way it's almost like the Windows desktop becomes the API—the API for all the AI agents that I might want to use or build in my enterprise. So suddenly it's interesting because the Windows desktop becomes critical in this world that we're thinking about.

Which is funny because like—this elephant in the room—you know, Windows is dead, right? Isn't the future of Windows, like, is there a future of Windows? And you know, if you look at the data, look at this—it's from just last year. Windows, gosh, 14--15 years ago had almost 100% market share and now it only has like 75% market share. So obviously Windows is going to die. I mean, look at the data.

Now, I guess if we want to zoom out, it doesn't go all the way to zero here, so we have to zoom out a little bit. It doesn't get to zero. I ran out of room.

So everyone's like, Windows is dying. Look at the market share. AI PCs are going nowhere. Intel is screwed. This is the end. The new way of doing things. And I'm like, boring. I have heard this story before.

And frankly, if you look at the current trends, sure it's trending down. But that goes through like 2060. That means the future is not Windows in the coffin. Like, I'm going to be in the coffin before Windows is in the coffin. Gosh, it's sobering. Let's just kind of look a little bit down the road a little more.

But you know, there's a joke I've used for like 15 years—which is when this happens. It was a hypothetical joke always in the past. But when this happens, you know, we joke about that cockroaches can survive nuclear explosions. Hostess Twinkies have a shelf life that's infinity, and you can put them in your bunker. And we also know that if this ever happens in some far distant future, there's still going to be devices running the Microsoft Windows operating system.

So I think Windows itself is kind of not going anywhere for a long time, despite reports of its imminent demise, right? Because Java—remember?—Windows is always going to die. Java is going to kill Windows. Windows apps are dead because of Java. Windows web apps are killing. Flash is killing. Ajax is killing. Silverlight is going to kill Windows. HTML5 is killing Windows. SaaS is killing Windows. Linux apps on desktops. Chrome OS is killing Windows. Mobile apps are killing Windows. Progressive web apps. Cloud. Universal Windows Platform. Electron. Internet-native is going to kill all these things.

I mean, any of us who have been working—I've been working 30 years—30 years of Windows death. Everything comes every two years: "Oh, you guys are screwed. Windows is about to die. We got a better way to do it."

And so now it's like, hey, this AI is going to come out and you all are screwed because AI is going to kill Windows. And I'm just like, yeah, whatever, man. I've heard this before.

I don't think that it's killing Windows because the reason is we just talked about—to build AI native agents that are doing all the things all my employees are doing, I got to build this like for every app and every employee. Are you out of your mind if you think that's the way? We already have this. It's already done. We in IT have done the hard work to integrate applications and security and guardrails and permissions and boundaries and zero trust and all of this work.

This is why AVD, Cloud PC, Parallels, Cameyo, Citrix, Omnissa—all these products exist in 2025—because we already have a Windows desktop that collects all this stuff together and it works.

You know, we talk about the competition. Like what was VDI's competition? Citrix's competition wasn't VMware. VMware's wasn't Citrix. It was the current way of doing things. The competition is the current way, which is already done. So that's why I think it's going to happen.

Now it's interesting here because if we're talking about AI agents, these AI agents are taking out applications, right? Like Java was targeting Windows apps. Ajax was targeting Windows apps. Well, agentic AI doesn't target Windows apps. It targets the humans. And that's different because now we're targeting actual human beings.

And it's kind of interesting for us because the path of least resistance is for the AI to use the tools that the humans use. And in that case, that means giving the AI access to the Windows desktop.

My belief—full confidence as I can say this—is that our future in end-user computing, the way that AI agents enter the enterprise, is first going to enter this enterprise by these AI agents using Windows desktops. And I believe that the method for deploying those Windows desktops to those AI agents is to virtualize them and deliver them remotely, which suddenly puts us all in this room in like a kind of a cool and pivotal and critical space in the world of EUC.

Because, you know, there were a lot of times in my career where I thought like, oh, I'm just a Windows desktop engineer and like the cool stuff is happening in the cloud or in virtualization or native or whatever. But the enterprise just churns and churns and churns on the Windows desktop. And if we want to use AI to start replacing things that humans are doing, it's going to be on the Windows desktop.

So I've been writing about this a little bit. I wrote an article on LinkedIn back in May—so that's what, six months ago now—about Microsoft Recall. You all are probably familiar with Recall. The point of this article was not about Recall itself, but I argued, oh, you think this Recall thing is scary now? You ain't seen nothing yet. This is just the tip of the iceberg.

I also argued in that article that you don't have a choice to opt out. I mean, yes, you do. Well, now you technically don't, because if you uninstall Recall, the binaries are still there. But even in the future, when Microsoft fixes that, you don't have an opportunity to opt out because your manager, your boss, your competitors—other people are going to be using these things.

In this article six months ago, I wrote that Recall is going to evolve over time. First, it's going to take screenshots, snapshots. It's going to start to understand what you're doing. So rather than just being a search engine and search interface for everything you've ever seen on your computer, it's going to start to understand the context of what actions are happening. Next it'll start to integrate with other Microsoft Copilots. Next it'll start to actually doing things for you, maybe in an interactive way. At first we actually see it moving the mouse and typing. Maybe eventually it starts doing things on its own. It'll do more and more and more of your job over time. Maybe the boring parts at first, maybe the mundane parts, and then we see where it goes.

Yeah, this is six months ago and the article was about this—it's not about you know, recording screenshots so you can remember what purple logo you saw yesterday. That's a party trick. That's not the real depth of where we're going with Recall.

The same thing is true with, you know, now we looked. Okay, so this is from last month: introducing Copilot Labs and Copilot Vision. So this is another step that Microsoft is doing. This is very limited right now. It's only in the Edge browser. It's only on certain websites. It only can do certain things. But you know, drip, drip, drip. We're getting there, we're getting there, we're getting there.

Simon Willison, who's one of my favorite AI personalities and influencers, whatever they're called—he posted this a month ago where he did an example where he used a large language model to look at his screen. He just recorded a video of going through a bunch of invoices and it pulled all the data out of the invoices and put it in a spreadsheet for him. All that processing—he prompted it. He just gave it the video and used a text prompt to tell it what he wanted it to do. And it cost 1/10th of one cent in compute to do that.

It's a little Mickey Mouse example. It's kind of nonsensical. But again, drip, drip, drip—it's coming and it's starting to work that way.

We see even more of the announcements now. I feel like agentic AI this month only has been so like in all the news. OpenAI is going to launch something called Operator—an AI agent that can do tasks for you. Copilot cannot read your screen. As I just mentioned, Copilot Vision can. Claude computer use—go to YouTube and type Claude computer use demo and you see tons and tons and tons of YouTubers just asking it to do things. Go give it a prompt because this computer use—this is where Claude now can actually use your computer.

They say probably should do it in a VM that's maybe not logged into anything you care about. But it goes on itself and it's okay. It's not super great. It's kind of slow. It gets stuck and makes mistakes. But drip, drip, drip, it's coming.

And there's plenty of examples like go to YouTube, find my channel and like what are the top five Brian Madden videos on YouTube? That's my prompt. And it goes YouTube, prompt, search. You can watch it—step, step, step. This is real today. You all can use this.

Project Astra is Google's version of this. The Copilot agents with Microsoft is pushing. Drip, drip, drip. These things are coming. It doesn't matter if you believe in AI or not. It doesn't matter if you think they're good or not. They are going to exist and it's going to make it really wild for us.

You know, there's the models are getting better and faster. Also, a lot of people—this is a whole different rabbit hole—but you know, your human brain does not fire every neuron for every thought. You have different sections of the brain and that's why you can see what activates when you're scared or excited or thinking hard or doing math or whatever.

A lot of people think that the models are going to grow this way also—where you don't have like one big GPT7 LLM with like 20 trillion parameters. It's more like specialized ones. This is the general purpose one. This is events reasoning. There's LLMs now that can identify what's on the screen. When you use a whole ChatGPT just to parse a screen, that's like kind of killing an ant with a sledgehammer. It's kind of overkill. It's slow. It's expensive.

There's very small LLMs. They can figure out what the UI elements are on a screen in just a few milliseconds—in other words, faster than frame rates. So they can watch interactively live on video what you're doing.

There are LLMs that can figure out user intent from that. So they again, small, efficient. They can watch the mouse, the clicks, what's happening and figure, oh, this person is trying to send an email. Oh, this person's trying to create a spreadsheet. Oh, this person is trying to like do a financial analysis.

These models are models that exist. All this is in arXiv. Just put that whole thing into Google. I don't even know what it means. It's like some scientific paper Dewey decimal system. And so you can find these papers that way better than like URLs.

So these models exist. You know, Microsoft is doing this. There's something called the Windows Agent Arena. Have you heard of this? These are for Windows agents. This is a GitHub project and you can download like custom Windows images with apps installed and everything. And then there's a task list of what an agent can do. And then you can like write your own agent, train your own agent, play with your own agents. They get scores of how successful they are.

Now they're only like 15%, 17%, but it's like 17% now. It was 16% last month. It was 14% two months ago. Drip, drip, drip. It's happening. They're getting more and more.

There's another paper about studying this Cloud computer use I mentioned that is really out right now—studying what it can do, what it can't do, how to get past these things, how we actually let these things use our computer. It's starting to happen.

And so I believe that these AI agents using your computer is the best way—is the way that they're going to enter our workforce.

So that's kind of my core thesis. That's what I want to spend the rest of the time kind of going through here today.

My core thesis is:

One, AI agents will be the new knowledge workers.
Two, they will use Windows desktops.
Three, those desktops will be remoted.
And four, this model will last longer than we think.

Now I'm looking at this from a technology standpoint. The ethics of replacing humans with machines—of course, this has been in the blue-collar factory world forever. It's been in other worlds forever. It's now starting to enter our world, which is like a little bit uncomfortable. But you know, automation did not take over factories overnight. It was a little bit, little bit, little bit, and it got more and more and more. Now there's some factory jobs, there's some robots. Different companies have different approaches. There's no really one-size-fits-all approach.

I don't think all of us are screwed and we don't have jobs anymore. I don't think that it's the end of humanity. Maybe it is. I don't know. But whether it is or not doesn't matter what we think. It's going to happen the way that it goes.

So I'm just kind of saying if these AI agents are getting better and better and better, I can sort of get out in front of it and think about how it works in my company or I can keep my head in the sand and ignore it. I'm spending my time right now just thinking about it and what that's going to mean.

So we can discuss over the next months and years on Bluesky. Anyone—I got into Bluesky because of Ruben Spruijt. Thank you. And it's like really kind of lighting up now. We can discuss on Bluesky in the next months whether these are real.

But I'm saying for what I'm saying today, I'm going with the belief that like, I think that's going to happen. This model will last longer than we think.

We're going to see also—I'm saying AI agents are going to use your Windows desktops and people are like, no, I mean like, you know, they should run native. They don't need a Windows desktop. It's a lot of overhead. You know, just to get all this kind of stuff. Also, it's overhead. A human is overhead.

The most expensive VDI desktop 24/7 is still like one-hundredth of the cost of your cheapest knowledge worker. And if I have to choose where to save the money—on the VDI or the human? So I think that it's, you know, there's this period of transition where maybe they will use—the agents will use our existing desktops—and people think, yeah, but in the future they can talk natively directly to each other. Sure.

In the future, Java apps will be everything or HTML5 will be everything or SaaS will be everything. We still have Windows apps today. I think this transition period when our AI agents are using Windows desktops is going to be a lot longer than we think just because of the way that corporations operate and like the way things sort of evolve.

So I'm going to go through 10 points. I have like 10 reasons why I think these things are true—the agents will be important, that they're going to use Windows, they should promote that Windows and it's going to be around for a long time. So in random order:

**Number one: AI agents should use Windows.** AI agents will use VDI because of the familiarity and existing infrastructure. I mean, flat out, it's this whole thing from before. Like, this is the Windows desktop today. If I want to design an AI agent from scratch, I'm building this now, you know? The Windows desktop already integrates all my apps, all my—I mean, by definition, my human workers are using a desktop and they're doing all their work. So this other thing over here where I'm going to build a native AI agent—so like everything needs an API. Oh, this information I get from this plugin which runs on Windows and it's old and it's Excel and it's this power—like if we're looking at going after what humans are doing, the humans are doing everything on Windows today. This is the way it already works. It's already secure. It's already compliant. Like by definition it's what we are using today.

So the lowest path of resistance to bring AI into that is to let the AI work in the exact same way with the exact same tools that we're using today. So this is, I feel like the most logical on-ramp to the technology.

**Secondly, it's the minimal disruption to the existing workflows.** Not just workflows. I mean, I get this email, I go to this database, I download this, I put this in here, I get this—here's my stock photography library. I talk to this person, I email this. All of those workflows exist today. So if I use those existing workflows without rewriting new applications, new scripts, new training, then that's a very easy entry point for me.

And there's precedent for this, right? Remember this—like Citrix in the 1990s. The benefit. Why do we use Citrix in the 90s? MAPS, right? Management, access, performance, security. Centralized management because I have only one server instead of lots of endpoints. Access from anywhere, from any device. Good performance, even over slow connections. Good security—there's no data at rest in the endpoint.

This technology—by the way, why we still use like Cloud PC and AVD today—is because of this. But why does it work? There's a better way. SaaS native apps, mobile native, all these things are better. Yeah, but the Windows desktop was done. Like, why does Citrix exist? Why does terminal service exist? Why does all terminal service—my—why does all this stuff exist though? Because like we can use the remoting technology to like modernize our old school applications. And we all in this room have been doing that for 25 years.

And we're like, yeah, that's—of course if I can wave a magic wand and have all like brand new fresh cloud-native apps, of course I would do that. But like my whole system and company is built around the existing way. I can just modernize it slightly. That's what AI does. When you put your AI agent onto your existing desktop, you get the benefits of AI and agentic AI without having to like reinvent everything from scratch.

**I believe that knowledge worker emulation will happen via UI automation.** So this is the same thing as AI watching what the humans do, watching how the mouse moves, watching. Like there's no real way. Have you ever done these projects where you try to figure out like your company's organizational behavior? Like let's map our processes and figure out how the company works. It's never right. It's all theoretical, but it never goes that way.

But if you put AI in all your desktops and just like watched all your employees work for a week and then could analyze that, you would really know how the company works. Probably you could do it with 1/3 of the employees also. But that's the thing. This is the way that our organizations exist today—is the actions we take place on our desktops. This is where you point AI to understand what's happening in the organization. Oh yeah, Windows, of course.

**The fourth, boy, security and compliance—for me, is a big one.** Because everyone talks about these AI agents. How do you trust an AI agent? You have to trust it's not going to go haywire. How do you trust that it has the right data, that it has the right permissions, that it's not emailing secret data out of the door?

We already have protocols to support all that because humans are not trustworthy. I mean, didn't we just find—who was it? A company just announced, oh, it was Macy's. Some employee hid $154 million of shipping charges from the accountants, which is literally what they made in profit that year. And they basically have no profit because some employers are trying to do good. But oops.

My point is though, is that all the fears about how AI is going to operate, what's it going to do—I don't really understand it. We have all these protections for humans. We have data loss prevention, we have auditing, we have screen recording, we have alerts, we have management, we have file permissions and ACLs and all of these things. They exist already.

And so we can have our agents use the existing infrastructure, all the security we put in place, everything we put in place without having to, again, rebuild that completely from scratch. We also have the same visibility and control of all the AI agent activities—literally screen recording. If you have an AI agent that's some API and is created as running in the cloud in some container, you don't see it and you say, oh yeah, take this data source and put it here, put it here, put it here. How do you audit that? How do you check it?

Well, in this case, we've got screen recorders, we've got session recorders. The business owner who knows that business application can look at the video of the AI using that business application just like they look at a human and they can say, oh yeah, it's working right. It's not working right. It's doing it. It's not doing it wrong. We have to retrain this. Everything that we do to have our human users operate, we can now do with the AI without having to change any of our modes of operation or rebuild things from scratch.

We have flexible, scalable resource management by running these VDIs or whatever they're accessing in the cloud. All the benefits of VDI. Human workers tend to work in like long chunks—like 8 hours a day, between 8:00 and 5:00 PM. Well, the AI doesn't need to work 8 hours a day. It can work 10 seconds, 200 seconds, 4 minutes. It can work at night. It can work in the day.

I mean, heck, if you have VDI, you're paying for unlimited usage. You know, human signs out at 6:00 PM, AI signs in and keeps on going. You're paying for that VM anyway. You can scale up, you can scale down, you can move it between clouds, you can move it to the workload. You can treat your AI workloads just like you treat desktop workloads today, which we are really, really good at managing. We're good at auditing, we're good at streamlining, we're good at understanding the costs.

We are really good at managing desktops and desktops in the cloud and scaling those. Why not use that same infrastructure for our AI that also goes to where we place our workloads.

People talk about AI PCs. Oh, you need a graphics processor, a GPU or an NPU or something like that inside your computer. Now you can like look at the screen and do things. Well, yes, but now I have to buy new computers for everybody and it has to run locally. Well, do I need that? I mean, isn't this what the whole VDI thing was for in the first place?

I don't have to run my AI in a desktop VM. Maybe I've got a remote desktop and I've got my human user on the other side. I'm already taking the pixels and transmitting those down to that user. Well, maybe I can actually cleave off some pixels. I want a stream that's going to go to my screen and text archiving utility. I'm going to take another screen and send it to my DEX analytics to figure out, you know, what the performance is like. I'm going to take another screen and send it off to my workforce analysis to understand the intent of what my workers are doing and how people are interacting and applications are using.

I'm going to send another one and you know, to archive it for compliance and like save things and look for credit cards and DLP and all this kind of stuff. None of this stuff has to run inside my VM, right. I don't have to do VM sizing. I don't have to change the way the VM is. But all I'm doing now is that human on the end—replace it with the AI agent.

The agent does not need to run inside your VM. The agent may be by a different box that has all the GPUs and runs your agents in there. Maybe that's AI Agent as a Service. Maybe you're hiring someone. Maybe your data stays here and the agent is in a different part of the world. Maybe you are. Like maybe Adobe has agents that are really good at Photoshop and Microsoft—like the legal department—runs their own agents.

And so now I can remote my Windows desktop, just like I'm remoting to users. I'm using HDX, RDP, whatever the protocols are, and there's just an agent on the other end that's doing the work instead of a human. So it gives us the flexibility and we don't have to completely reinvent our architecture of our VDI and sizing and understand all of those things. It's a very simple entry point.

Again, the implementation. I get continuity with my existing ways of doing business and very simple implementation. This is so important because a lot of people can sort of play with AI a little bit and you're like, yeah, I get it, I use it to help me here and help me here. But how do you scale that? How do I deploy that to my whole company? How do I get all my employees to understand it? It's really hard.

People are like, oh, I want to use an LLM. I'm going to get all your data, clean it up, tag it all. Now train it. Now train this thing. Like what? How long does this project take? How much does this cost? When do I see results? It's too complicated.

But here, if I'm looking at everything that all my human workers are doing, I can have an AI agent come in and just do it. There's like one or two little tasks that are like really easy for it to do. It can do that. I can look at screen recordings. I can train it the same way. I can archive it. I can understand it. I don't have to build a whole new project with a whole new department. I can just very tiptoe in and let me see—is there things that AI agents can do that fit within my existing structures?

And I think that's what's going to happen. If all these red boxes are like tasks—when people talk about like looking at AI and how AI can help you within an organization, it's not like AI replaces this job as a product marketer. AI can do tasks. You look at every single job, everything that a human worker does, and they probably have like 200 individual small tasks. Well, some of those tasks might be easy enough, or just boring or not interesting, that an AI actually could do them.

So we're not trying to have the AI agent replace all humans. We're saying let's identify the easy, low-hanging fruit that we can do, give those to the AI and now the humans have more capacity to do whatever you want. Are they doing more work with their free time? Are they doing better quality work? Are they doing deeper thinking? Are they doing—but you've got the flexibility though.

And again, you don't have to make AI better than your best employee. You don't have to make it as good as your worst employee. You just have to make it be able to competently do things that you're paying humans to do that they don't enjoy, that's error-prone, that's mundane and repetitive, and just let the AI start to do that. And you can integrate this with your existing way of working without having to rip and replace and build, you know, these massive projects around these AI things you may never even see if they work.

**So the final sort of couple of points I have:** Maintenance and ongoing training and updating is very straightforward if your AI agents use Windows. Because again, this doesn't change from the way that you do it today, right? You already have a method for application updates. Maybe it's the business app owner who knows that and they partner with you and you package it and you push it out and you've got ring one, ring two, ring zero. That's all in place. Keep on using that. Don't change it for AI.

The way you train—not the AI—is the way you train your employees. How do you train them about new applications and changes and new policies and stuff? The way that you monitor your employees to make sure that they're doing good quality work. The way you do change management within all their devices. The way your employees engage with the help desk and the help desk troubleshoots things. The way that you audit to understand what your employees are doing.

Oh, you can audit twice. There you go.

All of this stuff. This is the way you're doing everything today if you let AI agents use Microsoft Windows desktops. Then you don't have to change any of that. And you can. It's not just for you and IT as I said—it's the business owners. It's legal. You can have session records. You can have. You can look at all the audits, the zero trust, the all the guardrails are in place. You have those exact same guardrails.

**And then the third, I guess, is you know, 2025 is your video.** This is kind of a running joke now. This is a talk I gave at the beginning of the year where it said 2024 is the year of VDI. But 2024 is almost over. So really it's 2025 if you want the future of EUC.

But I was sort of joking though. Because like, you know, there's that old joke about, oh, it's the year of VDI. Har, har, har. And everyone would say to me, I remember when you said it was the year of VDI. And I was like, I wrote a book called The VDI Delusion. I guarantee you, I never said any year was the year of VDI.

But when I gave this talk in Den Bosch earlier this year, I kind of said, you know, with AI agents and AI starting to use computers, you want that Windows desktop to be always running and available anytime, and so it should be in the cloud. And I was like, actually, if you're looking at a way to onboard AI agents into your environments, VDI seems to be the way to go. And it's actually interesting because we have this ability to where now AI agents can like have their own desktops. Maybe the humans don't even share, like you might have 1000 employees and right now you've got 1000 Citrix licenses. Maybe you have 2000 Citrix licenses in a year and you only still have 1000 employees.

And it's kind of funny. You're like, oh my gosh, but that's like Microsoft licensing. And by the way, try to solve that with Microsoft licensing. Like what licenses do non-humans use for like Windows?

So, but it's I mean for real though. It's kind of funny because like you're like, well, yeah, but I gotta have Microsoft licensing and it's expensive and I got VDI licensing and these charges and that all could be like a couple hundred a month. Yes, but again, that's just like 1/100th of what an employee costs.

And so if I can let the AI do things and it's a couple hundred bucks and if again the AI can use the computer all day, all night, I can get per-minute pricing and just turn it on. It'll turn itself on as it's got a task to do and then turn itself off again. It becomes pretty interesting.

So to me, this is really why I believe—and I put these 10 here so you can like for, well we used to say tweetability. What is it on Bluesky? Butterfly ability? I don't know. But this to me is like the 10 reasons why I believe that when AI agents enter the workforce—again, how soon do AI—the AIs are not good right now. This is not necessarily like happening right now. But this is what we're seeing—drip, drip, drip—and how things progress.

When AI agents enter the workforce, I believe it's not going to be people building native experiences. In personal life, sure, I think Apple and Google are going to make things on your phone that help you find that restaurant for Wicked. But in the corporate world, the entry point is going to be your Windows desktop. And I think remoting that Windows desktop is the way to do it.

So that's it. Two seconds left. I told you I finished exactly on time.

**Neil:** That's absolutely brilliant and really good description of where we are. But in 2060 we'll have an EUC Forum here. I'll still be emceeing. I'll be 94 then, so I'll probably be thinking about retiring by then. But I'm still be about, I'm sure. So put that in the diaries now if it will allow you. You can use AI to put it in the diary. We'll see you in 2060.

---

That's how you can follow me nowadays. And yeah, this is a lot of fun. We'll be talking more about this in my afternoon session. Thank you all so much for your time today.
