---
title: "AI just created 10,000 accidental citizen developers in your company. Welcome to the post-application era!"
date: "2025-10-01"
authority_level: 5
file_type: citrix-blog-post
tags: [post-application-era, citizen-development, shadow-ai, app-proliferation, workspace-governance, software-economics]
related_frameworks: [post-application-era, workspace-as-control-plane]
original_url: "https://www.citrix.com/blogs/2025/10/01/welcome-to-the-post-application-era/"
staleness_threshold: stable
---

# AI just created 10,000 accidental citizen developers in your company. Welcome to the post-application era!

[Original post](https://www.citrix.com/blogs/2025/10/01/welcome-to-the-post-application-era/)

Oct 01, 2025

Back in the nineties, we had a simple rule of thumb for estimating how many different apps a company would have to manage: One app for every ten users. (e.g. a 5,000-person company had about 500 apps, etc.)

The total app count was reasonable enough that IT could vet each application, understand its security implications, manage its lifecycle, and sleep reasonably well at night.

In 2025, people are starting to realize that ratio no longer applies.

## The app creation dam has broken

Last week, I built a competitive analysis dashboard in twelve minutes. I didn't need to file a ticket with IT or hire a developer. I just described what I wanted to Claude, and it built the app while I watched. I now use it daily, and IT has no idea it exists. (Well, unless they read this blog, I guess.)

This is happening thousands of times a day in every enterprise. Last week, Paul Roetzer shared Amjad Masad's vision for Replit where "everyone is empowered to create apps and software in real-time to solve problems." This is awesome for workers, but scary for IT!

Masad also talked about how the cost of creating apps is approaching zero. When a random HR worker can build the org chart software that perfectly fits their needs in three days instead of subscribing to a package that costs tens of thousands of dollars annually, why would they ever buy off-the-shelf SaaS again?

## A 10x increase in the number of apps!

With the barrier of entry to create apps being lowered, we can envision a world where every employee creates many different apps. So instead of the old ratio of ten employees per app, we could now see ten apps per employee. In other words, a 1,000-person company goes from 100 apps to 10,000!

Frankly that's just a conservative guess. Some of your power users are probably creating dozens of micro-apps: workflow automations, data analyzers, report generators, communication bots. They're not calling them "apps" because they built them in five minutes during a coffee break, but functionality-wise, they're apps. They process data, make decisions, integrate with other systems, and run autonomously. (If it walks like a duck and talks like a duck...)

## The economics have fundamentally changed

We're witnessing the complete inversion of software economics. I like how the founders of Blitzy talk about this, that in a world where you can regenerate entire codebases overnight, the code itself becomes worthless. The value moves to the specification, the intent, and the problem description. (e.g. All the parts that your rank-and-file workers can easily define.)

When software approaches zero cost, the constraint isn't budget or technical skill—it's only limited by a worker's imagination. Every worker becomes a potential developer. Every problem becomes an opportunity for a custom solution. Every frustration with existing tools spawns a replacement.

## These aren't "applications" in the traditional sense

Obviously, these AI-generated apps don't really look like traditional apps in the IT sense, as:

- They're ephemeral, created for a specific task, maybe used once, or maybe becoming essential.
- They're undocumented, with no requirements specs, no architecture diagrams, no security reviews, and no clear understanding of what they actually do.
- They're highly interconnected and tangled, calling APIs, scraping screens, sending emails, and access databases or other MCP sources using whatever credentials the creator has access to.
- They're constantly evolving and never static, as workers iterate on them continuously, asking AI to "make it do this too." (Plus, the AI platforms continuously update models and add more features which constantly update the apps based on them.)
- They're invisible, running in browser tabs, ChatGPT conversations, or wherever the worker happened to create them.

This isn't really shadow IT, as "shadow" IT implies there's still a bright side where "official" IT lives. This is more like "alternate universe" IT, filled with applications that exist alongside your managed environment.

## The traditional IT response won't work

The knee-jerk reaction from IT is to lock everything down: block the AI tools, restrict API access, and require approval for any automation.

Good luck with that.

That's like asking workers to go back to horses after they've discovered cars. Your best people, (who've tasted the 10x productivity gain with AI), will either circumvent your restrictions or leave for companies that embrace this new reality. (Not to mention your more AI-forward competitors who figure this out will eat your lunch.)

The other extreme (let chaos reign!) is equally untenable. These thousands of informal apps touch customer data, financial systems, and intellectual property, making decisions that affect your business. They need some level of governance, security, and reliability.

## A new model: manage the environment, not the apps

This is why we keep talking about the same themes at Citrix: In a world of infinite apps, you can't manage each one individually. You need to manage the environment where they run.

For example:

- You can't vet 10,000 apps, but you can secure the workspace where they operate.
- You can't document every workflow, but you can monitor and record what's happening.
- You can't approve every automation, but you can control what data and systems they can access.
- You can't train workers on every app, but you can provide guardrails that keep them safe.

Again, this isn't about preventing innovation. It's about creating a safe space for it to flourish.

## How to start thinking about this in your company

The companies who thrive in this new world won't be the ones that successfully prevent workers from creating apps. They'll be the ones who successfully enable it while maintaining security and governance, beginning with some shifts in thinking:

### 1. Accept the new economics

Software creation costs approaching zero means behavior will change dramatically. Stop thinking about "build versus buy," and start thinking about "build versus build again versus build differently." When creating an app costs less than the meeting to discuss creating it, everything changes!

### 2. Redefine what an "application" means

If a worker asks AI to analyze last quarter's sales data every Monday morning, which AI does via some sort of scheduled automation, is that an app? (Yes.) Start recognizing and accounting for these micro-applications in your planning.

### 3. Shift from app-level to environment-level security

Stop trying to secure each application and start securing the runtime environment. This could be containers for AI workflows, sandboxed execution spaces, and session-based controls.

### 4. Embrace radical observability

You need to know what's running, what data it's touching, and what decisions it's making—even if you don't know the app exists. This means comprehensive monitoring at the workspace level, not the application level.

### 5. Create easy (supported) paths for citizen development

Give workers official, secure ways to create their automations. This could be AI agents that operate within Citrix sessions, approved AI tools with proper data governance, or designated development workspaces with appropriate guardrails.

### 6. Prepare for the app lifecycle to hyper compress

Apps might be created, used, and retired in the span of hours. Your governance model needs to account for this.

### 7. Recognize the value shift

As the Blitzy folks say, when code generation is free, value moves up the stack. The ability to clearly specify problems, validate solutions, and ensure quality becomes more valuable than coding skills. Your best "developers" will probably end up being the people who understand the business problems most deeply.

## Oh, and BTW, this is already happening

While you're reading this, your workers are building apps. They're not waiting for permission. They're not following your SDLC. They're solving problems and automating tasks with whatever tools they can access.

The question isn't whether you'll have 10,000 apps to manage. (You already do, you just can't see them yet!) The question is whether you'll create an environment where those apps can be productive and safe, or whether they'll remain in the shadows, ungoverned and unmanaged.

As Masad said in his talk, in this new world, "ideas become wealth." When software creation costs nothing, the winners won't be those with the largest IT budgets or the most developers. They'll be the ones who can harness the creative potential of every worker while maintaining appropriate controls.

The companies who figure this out will be fundamentally different organizations who are more agile, more innovative, and more capable of adapting to whatever comes next. You just need to be ready for a world where the constraint isn't technology or budget—it's imagination and governance. Welcome to the post-application era!
