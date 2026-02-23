---
title: "Microsoft Recall: An analysis of the issues & prediction of the evolution of the AI workplace"
date: "2024-05-28"
authority_level: 5
file_type: linkedin-article
tags: [microsoft-recall, workplace-ai, employee-surveillance, privacy, ai-workplace-evolution, employer-employee-relationship]
related_frameworks: []
original_url: "https://www.linkedin.com/pulse/microsoft-recall-analysis-issues-prediction-evolution-brian-madden-zoync/"
staleness_threshold: stable
---

# Microsoft Recall: An analysis of the issues & prediction of the evolution of the AI workplace

*Brian Madden—May 2024*
*Published: https://www.linkedin.com/pulse/microsoft-recall-analysis-issues-prediction-evolution-brian-madden-zoync/*

*Header image: DALL-E generated image with "Microsoft Recall" text and "Scary, Amazing, Just a preview of what's coming next. Buckle up!" with ILKI logo.*

People are nervous about the upcoming Microsoft Windows "Recall" feature. For now, it stays local to your computer. But once companies realize the power of AI watching and collaborating across all their employees, features like Recall will become centralized and mandatory. Welcome to the (near) future where free market capitalism drives AI policy!

Last week, Microsoft previewed an upcoming Windows feature called "Recall", which takes continuous screenshots of your Windows 11 computer that are stored and analyzed via AI. You can then interact with them via an LLM to go back in time to recall things you did—find old links, names of people, that guy on LinkedIn with the good AI articles, ideas you discussed at meetings, etc.

The people of LinkedIn seem to be excited about the potential awesomeness of this feature, while also being nervous and creeped out. (Both are certainly understandable!)

In this article, I'm going to cover:

- Security & privacy fears, and how they could evolve
- The evolution of the employer / employee relationship
- Features like Recall are going to become inevitable in the future.

## Recall security fears

June 2 UPDATE: When I originally posted this article, I wrote that because the Recall archive stays local on your PC, security fears were overblown. I was wrong about that. Kevin Beaumont blows apart Recall's security here.

## Recall privacy concerns

There are three categories of privacy concerns:

1. **Compliance privacy** (GDPR, CCPA issues like customer information appearing on screen which is then saved into the Recall data archive without proper consent.)
2. **Employer privacy** (Legal protection against discovery.)
3. **Personal privacy** (Companies seeing what employees are doing on their laptops.)

Let's look at each of these separately.

### Compliance issues

There are all sorts of privacy frameworks around the world (GDPR, CCPA, etc.) which require companies to only store personal details that are needed, allow for disclosure for what's stored and why, and provide a way for people to opt out of this storage.

Microsoft Recall could be problematic here because if it's recording everything, even a random email from a random person with their contact information in the signature could be captured and saved for processing and future Recall.

This should be easy to address, as I would think it would be easy enough to provide an API for this which allows security & privacy vendors to hook into this process to ensure compliance and scrub info as needed. I assume companies like OneTrust are already developing the "OneTrust GDPR Toolkit for Microsoft Recall" or whatever.

### Employer / company privacy

I imagine that companies would also worry about privacy in the context of legal discovery. We already know that email and text message communications are discoverable in legal cases, and that companies use voice conversations and services like Signal to communicate in ways that can't be exposed by a legal case.

I would imagine that lawyers' heads are exploding over the concept of recording all the screens of everything that every employee does on their computers. Now a company could get into trouble based on something an employee typed and then deleted before sending or saving!

### Employee / personal privacy issues

While Recall can be temporarily disabled and/or prevented from recording certain windows, having something watching and recording everything you do just feels a bit creepy. It's even scarier to know that an AI-powered searchable playback interface exists for everything you've done on your computer, forever.

Companies can already decrypt BitLocker-protected content on employee devices, and they often have agreements which allow them to monitor employees' activities on corporate-owned devices. So it's not a stretch to imagine that companies would implement policies which allowed them to access employees' Recall archives.

Workplace AI technologies such as Recall will drastically shift the employee-employer relationship in the next few years. To understand this, let's first look at how Recall will evolve in the near future, and then what it will mean for companies and employees.

## How Microsoft Recall will evolve

Today's version of Recall stores its archive locally on the PC, and the primary interface for interacting with previous content is driven by a human. (e.g. a person interactively types or asks, "What was that company I saw yesterday with the pink logo?")

Over time, the Recall engine will become smarter, start doing bits of your work for you, move off your laptop to a central location, and then finally link all activities of all employees together.

### Recall gets smarter and more powerful

I can envision that the evolution of Recall looks something like this:

1. Recall's AI will start to understand what you're doing, rather than being a search interface for everything that's ever been on your screen.
2. Recall will start to integrate with other Microsoft Copilots, such as Office and Windows, to offer little hints and helpful actions here and there.
3. Over time, Recall will start to actually do things for you, maybe in an interactive way at first (you see it typing and moving the mouse).
4. Eventually, Recall starts doing more and more of your job. (Maybe all the boring parts?)

You can see this as a gentle evolution to the standard "AI agent" that everyone is talking about. Microsoft is just priming the pumps now, both in terms of capabilities as well as our comfort with touchy concepts.

Recall will get smarter and more valuable as the underlying AI models become more powerful. This is the "Sam Altman approved" AI-powered product, where each new release of the core model improves the product built on it rather than Sherlocking it.

### Recall becomes centralized

Today, the Recall archive stays local to the computer it's running on. I've already addressed Microsoft's publicly stated reasons for this (privacy & security), though I'd argue the real reasons Recall is currently local-only are:

1. It's so new and scary that this is the only way that Microsoft will get anyone to accept it.
2. Microsoft needs to give people a reason to buy the new Copilot+ PCs.
3. Microsoft's millions of Azure GPUs are already fully utilized training GPT-5 and running all the Copilots.

So, Recall being local-only for now makes sense. But clearly this is just temporary, as there are simply too many drawbacks to having every instance of Recall being its own little disconnected island. For example, downsides of Recall being local-only include:

- If you lose, break, or upgrade your computer, you lose all your Recall history.
- If you use multiple devices, you need to remember which one you were using in order to be able to ask about something.
- All the other downsides of files, content, and context being locked to a single, physical device. (Hasn't Microsoft spent the past decade of Azure marketing drilling the downsides of this into all of us?)

Obviously, it's ludicrous to even be making this point in 2024, and Recall today is clearly limited by keeping it locked to a specific device. That will change, (if for no other reason than Microsoft will eventually release Copilot++ PCs which they'll need to sell us all over again).

## Employer / employee relationships

All the things I love about Recall as an individual are the things that terrify me about Recall as an employee.

While the evolution of Recall I outlined above is fairly obvious, what's less clear is the evolution of the employee-to-employer relationship which will happen alongside it.

The immediate question (even today) is whether employers will have access to Recall's data streams. While the privacy & ethical issues initially seem similar to existing ones—employers already have access to employee emails, OneDrive files, meeting transcripts, etc.—there's something different about companies having access to the iterative process employees use to create their work outputs.

Recall is different for three reasons:

### Recall lets the company see how much "effort" employees put into work

Do companies pay knowledge workers for their effort or their output? This question really bubbled up during the pandemic, though society has yet to resolve it, so we need to think about it again in the context of AI tools like Recall.

Companies have not historically been able to measure how much effort knowledge workers expend to create their work products. As a proxy, they measure things like work product output or how many hours an employee is in the office.

For employees who are really efficient and can do their jobs in 25 hours per week instead of 40, working from home means they have 15 extra hours per week when compared to their less efficient coworkers. But if an efficient employee's company starts using a future version of Recall which is centralized and has the ability to track working hours, what happens when the employer finds out they're only putting in 25 hours a week of effort? Is their salary reduced? Are they given more work? Or should they just crank up the productivity theater and make it look like they're working 40 hours a week?

### Recall lets the company judge employee work style

Even though Microsoft has largely walked back their 2020-era "Productivity Score" messaging—apparently someone caught a couple episodes of Black Mirror as most old links now redirect to "Microsoft Adoption Score" content—the concept of quantifying employee productivity into a score is definitely a thing that companies think about (even if they don't say it out loud).

Regardless of what it's called or whether employers attempt to quantify it today, the reality is that humans work in many ways. If you told two different employees to create the same report and watched their process, they'd likely go about it in very different ways.

This is different than the efficiency metric discussed in the previous section. Two employees spending the same amount of time to create the same level and quality of output would (in theory) have the same productivity scores, and they would (in theory) be valued equally by the employer. But it's possible that the analysis of their processes might make one of them appear "better" to an employer or AI watching over their shoulder.

For example, when I personally need to create work products with a lot of writing, I typically might research a bunch of things and do an initial brain dump, then go for a long walk or run, then come back to put it all together and write the final prose. Microsoft Recall would report that I didn't work for 2 hours, compared to someone who sat at their desk that entire time. But after 30 years of working, I can guarantee that without that processing time, I'd just flail around for those hours and it would either take longer or reduce the quality of the final output. Trying to "look smart" all the time would be exhausting, and productivity theater to the max.

Luckily most employers understand that this level of employee tracking (especially for knowledge worker jobs) is counter productive. After all, you don't need an AI Copilot to track how much time employees spend doing various tasks on their computers. The real risk for an AI tracker is due to the analysis of how employees are creating their work products. For example, if a company asks an employee to create an agenda for an upcoming training workshop, the first step the employee might take is to dump a bunch of details into an LLM and ask it to create the first draft of an agenda. (In fact, I would argue that's a generally-accepted best practice that workplace AI experts recommend for all employees.)

But I could absolutely envision a future scenario where a company is looking to stack rank their employees or reduce headcount by thinking, "Hey, Brian just asks ChatGPT to do everything we ask him to do, why don't we just fire Brian and use ChatGPT instead?"

This could lead to employees trying to "do more on their own" in order to prove their value as human, even though this might go against a company's published best practices of using the tools they provide. What if an employee googles too much? What if they read too much? Who decides what's too much? People could drive themselves mad trying to adjust their performance in ways they believe the AI and the company would value the most.

Even if a company has policies against tracking this kind of stuff, the Recall archive of past actions is slowly being built. Employees would still worry that one day layoffs will come and the company will have to pick 10% to lay off, and you don't want your actions over the past 2 years to result in your name being on the list, "Hey Business Copilot, give me a list of the least efficient 10% of employees."

### Recall lets the company see everything employees do, including micro-infractions

The final employee fear about Recall which I'll mention now is that if an employer's AI is watching everything, it would be trivially easy to find policy infractions, no matter how small, if the company wants to fire someone for cause or otherwise punish them.

This concept has been entering the mainstream conversation more recently in the context of surveillance societies with AI-powered cameras, but just knowing that a future manager of mine could theoretically say, "Hey Recall, build me a dossier of infractions to get Brian fired" does not sit well.

## Despite these drawbacks & cautions, this Recall future is inevitable

Even though there are many potential downsides and complexities for mass centralized use of Recall capabilities, the benefit for companies will be massive, and this type of work future is inevitable. Even if some companies attempt to tread slowly or hold back, market pressures will eventually force this to everyone.

To understand why, think about this future from a business owner or the company's standpoint. Let's assume a future where there's some kind of Recall-like AI-powered feature which records every action every employee takes across all their work devices. Further imagine there's an overarching AI which analyzes all of that together.

I can envision several advantages and new capabilities which would be enabled for the business, including:

- Identifying redundant and overlapping projects and efforts. This can be for little things, like an employee starts writing something in Word, and AI Clippy pops up and says, "Did you know this doc already exists? Here you go!"
- Understanding workflows, tracking and codifying what really happens in the companies, rather than the "official" documented processes that people think.
- Detecting bottlenecks and delays. Maybe one person doesn't return their emails quickly which ends up negatively impacting another project.
- Auto creating shared project spaces, dashboards, reports, etc.
- Sentiment and culture analysis, detecting trends of negative sentiments, trends by department, geo, etc.
- Automated compliance and risk management, overlook everything for potential issues. (Unless legal specifically doesn't want to call this out, as mentioned already.)
- Auto-created repositories of best practices. (And the AI can actually know which practices are the most valuable.)
- Understanding if projects are really profitable or not, true efforts, measuring the previously unmeasurable.
- Dynamic workforce allocation, detect which projects are overstaffed, move people to understaffed projects, understand the best people for every project, build the right teams, understand which projects need which skills at the exact right moment.
- Idea tracking, from brainstorming sessions by one group, to some random person's notes from another team.
- Figuring out hidden skills and talents. Someone in finance is really good at solving complex tech issues, a random PM makes presentations, who's good at leading meetings, etc.
- Who's really important and undervalued? (And vice-versa.)
- Identifying individual employee habits, when they're productive, helping to schedule meetings and pick attendees in a way that leads to the best outcomes, not just based on when everyone is free.

I could imagine a future role at a company that's directing all this. There would still be people managers, but now a director could be an actual director (like an orchestra or film director) and make the big decisions while the AI and lower level managers make it happen.

As a business owner, the advantages would be massive. Regardless of how they're measured—increased revenue, faster time to market, getting the same work done with fewer people, or just better-quality work across the board—the value this capability would be huge.

## Think employees would never want that? Meh, employees are coin-operated

People push back on this with objections like, "That sounds horrible, employees would never accept that!" I would counter with, "Businesses don't care what employees want."

If employees got what they wanted, we wouldn't have cubicles, worthless meetings and BS jobs, or mandatory team building. Companies have long realized they can smooth over rough policies and non-aligned ideals with money and benefits.

Maybe you read this article now and think that a company recording and analyzing everything you do all the time is horrible and you would never work there. What if the company offered to double your current salary? What if they tripled it? What if they told you that you only had to work 4 days a week?

Imagine this in a job posting:

> At our company, we leverage AI to the max. If you work here, in any position, we will give you a work laptop, work phone, and whatever other devices you want. We are going to run AI software on these devices which records your screen and captures and watches everything you do. Every meeting and phone call you have will be transcribed and recorded. All of this will be fed into a centralized AI that will help make us more efficient. It will offer advice and suggestions and over time start doing things for you. It will help collaborate and coordinate with colleagues. We expect that you do all work-related tasks on these devices, and we expect that you do not do any personal tasks on them. These AIs will always run and cannot be disabled. Because this is a big ask that sounds scary, we will compensate you accordingly. You will be able to work from anywhere. We will triple the salary you had at your last job. Our standard work week is 28 hours. You can make this work however you want, e.g. four 7-hour days per week, with every weekend a three-day weekend.

I could make an argument that for publicly-traded companies whose primary fiduciary responsibility is to maximize the rate of return on capital to their shareholders, it's a dereliction of duty for them NOT to go down a path like this.

The most fascinating thing about this concept is that it's not some crazy far off future. This technology is essentially available today, or very soon (months, not years). This isn't a sci-fi vision that requires technological breakthroughs to maybe happen one day. Also this doesn't have to be a tech company, as literally any company could do this today. A trucking company, healthcare, consulting, accounting, software company: anyone who has a lot of office or knowledge workers could put this in place in 2024.

Will employees balk at this? Probably? Maybe? Definitely? But not all employees, and I bet for the ones who do, there will be a huge stack of resumes looking for 2-3x salaries with 70% of the working hours.

## The future AI-powered workplace and next steps

Even if the future doesn't follow the exact path outlined here, and even if Microsoft Recall doesn't evolve like this, a future like this is happening. (And you can bet Microsoft will be involved.) Even if a company says, "Not us!", a competitor will say, "Sounds great!" and change the dynamics of their industry. Even if a government says "Not us!", another jurisdiction will say, "We're open for business!" and change the dynamics of that work environment.

As I wrote almost a year ago, the coming wave of workplace AI surfaces many of the issues of the Consumerization of IT, but with a scope and intensity we haven't seen yet. Microsoft Recall, Copilots, GPTs, and similar technologies are revolutionizing workplace processes, collaboration, and how we discover unknown efficiencies.

Much like the digital workplace transformations taking place already, these conversations are not limited to IT, but must include HR and senior leadership as companies consider the philosophical underpinnings of what they want their relationships with human employees to be, and how they think about ethics, privacy, and employee operations.

What a wild ride these next few years will be!

*This text is AI Influence Level 0: Human conceived & created.*
