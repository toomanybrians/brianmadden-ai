---
title: "Why enterprise AI agents disappoint (and why the fix is not 'better agents')"
date: 2026-05-07
url: https://www.citrix.com/blogs/2026/05/07/why-enterprise-ai-agents-disappoint-and-why-the-fix-is-not-better-agents/
authority_level: 4
file_type: blog-post
tags: [agents, cognitive-stack, crawl-walk-run, skills, second-brain, token-routing]
staleness_threshold: stable
description: "Enterprise agent pilots are stalling because companies are skipping from 'crawl' (chat) to 'run' (autonomous agents) without 'walk' (context, skills, judgment). Even after you can run, you still mostly walk — successful AI use is choosing the right cognitive-stack layer per task. Includes the four-layer Excel example with token costs."
---

# Why enterprise AI agents disappoint (and why the fix is not "better agents")

The past few weeks have seen an explosion of talk about AI agents in the workplace, with everyone talking about how we're moving past chatbots and rigid workflows towards true autonomous agents which do actual work. [Google Next was all about agents](https://cloud.google.com/blog/products/ai-machine-learning/partner-built-agents-available-in-gemini-enterprise), [OpenAI announced workspace agents](https://openai.com/index/introducing-workspace-agents-in-chatgpt/), [Anthropic introduced enterprise controls for Cowork](https://claude.com/blog/cowork-for-enterprise), and [Microsoft dropped a slew of posts about agents in the enterprise](https://www.microsoft.com/en-us/worklab/ai-at-work/). They're all basically telling the same story: that autonomous AI is about to do your job, your team's job, and your company's entire back office operations.

Meanwhile in userland, most knowledge workers are still just using AI as a fancy answer engine.

When I talk to customers, it seems all I hear about are [stalled pilots](https://www.citrix.com/blogs/2025/08/27/everyones-wrong-about-why-enterprise-ai-is-failing/), Copilot deployments that don't meet expectations, and feelings that agent demos from conferences don't translate to anything close to what a company could actually run in production. (I love [this 18-minute segment from The Artificial Intelligence Show podcast](https://www.youtube.com/watch?v=SHHEqF5-doE) on this topic.)

The problem isn't about agents, per se. It's that most people view agents as the ultimate goal of AI, and now that agents are becoming real(ish), people want to jump right to them even though they haven't taken the intermediate steps to get there.

I've written [over](https://www.citrix.com/blogs/2025/07/16/why-ai-agents-will-use-the-same-desktops-and-apps-as-human-workers/) and [over](https://www.citrix.com/blogs/2025/08/04/ai-agents-are-the-new-insider-threat-secure-them-like-human-workers/) that agents need to be viewed like human workers, rather than software tools. After all, in order to be successful, agents need the same things as humans: context, guidance on judgement, understanding of the established way of working, etc. (Deploying an agent without this is like handing a new hire a laptop & login and saying, "Now go do my job.") AI agents without this fail for the same reasons a human would.

## Crawl … Run! (Wait, did we skip "walk"?)

You know that phrase, "crawl, walk, run." It can apply to AI in the enterprise too. Crawl is using AI via a chat interface. (Where most are today.) Run is having AI agents do useful work throughout the company. (What everyone is talking about now.) So what happened to walking?

Walking is where you teach AI how you actually work, what context matters, and what good looks like. It's where you build skills, capture how decisions get made, and give AI memory that persists between sessions. (I laid the full version of this progression in my [7-stage roadmap for human-AI collaboration](https://www.citrix.com/blogs/2025/06/24/the-7-stage-roadmap-for-human-ai-collaboration-in-the-workplace/). Each stage builds on the one before it, and you can't skip steps.)

You can't skip steps!!

## What does walking look like?

I use [the cognitive stack](https://www.citrix.com/blogs/2026/02/25/understanding-the-cognitive-stack-why-your-ai-strategy-is-focused-on-the-wrong-layer/) to illustrate how AI is entering the knowledge workplace. Worker interaction with AI is at the top. Context, [skills](https://www.citrix.com/blogs/2026/03/12/skills-are-all-you-need/), and judgment are in the middle. Agents are at the bottom.

Everyone understands the top part, since human workers telling AI what they want to do is how most of us have been using AI for years. And everyone understands the bottom part (even if only in fantasy) where AI agents go into the real world and do real work. But how do you connect those two together? That's the walking part.

I argue that the reason people are having challenges with agents in the workplace is because they're skipping from crawl to run. In other words, they tell AI what they want (crawl), and they've empowered AI with logins and agency and tools (run), but they haven't given AI the skills or context (walk).

At this point you're probably thinking that I'll spend the rest of this post explaining why the walking step is important. But no! I mean, yes, walking is important. But also:

## Even after you learn how to run, you still mostly walk everywhere

Just because can see a "run" future where AI agents do all sorts of real work, remember that most people spend more time crawling and walking than they do running. Sure, running is fastest, but it's also tiring, you get sweaty, and it's easier to fall.

Successfully leveraging AI in the enterprise is going to be about applying the right approach to each task. Let's say you need to analyze some data. (A spreadsheet, customer list… whatever.) You can do that analysis at any layer of the stack. So which layer do you choose? (Remembering that each layer down costs more than the one above it while also requiring the layers above it.)

The easiest and simplest (crawl) is you just do it yourself. You open Excel, paste in the data, and write some formulas. There's no AI involved. It's cheap (no tokens), fast, and reliable because you're the one doing it.

One layer deeper, you paste the data into your LLM and have AI reason over it in the context window. Maybe that costs 1,000 tokens. The more context you give the AI, the better chance you have of getting the results you want.

Deeper still, you can use a [skill](https://www.citrix.com/blogs/2026/03/12/skills-are-all-you-need/), (maybe a Python script you built once and reuse). The cost per run isn't going to be any more than in-context reasoning, though this one has a dependency: the skill had to be built with context and judgment, and it has to be maintained. And it required the layers above it.

Finally, you could go all the way down to "run" and have a [computer using agent](https://www.anthropic.com/news/3-5-models-and-computer-use) do it, where AI operates Excel like a human would, pasting in the data, clicking cells, writing formulas, and doing the whole thing autonomously. It might cost 200,000 tokens, it's slower, and it's more likely to make mistakes. (But hey, you're "running" with an agent!) But using an agent here only works if it has the context, skills, and judgment from the layers above to know what "good" looks like. Without those layers, you'll spend 200,000 tokens to do something the layers above could've done for 1,000, or for free by just opening Excel yourself.

## Don't focus on agents before you've solidified the layers in between

Yes, agents can be a destination. Eventually. But you need to do the work on the middle layers first. I've written about that work from several angles: the [second brain](https://www.linkedin.com/pulse/i-built-second-brain-using-ai-its-changed-way-work-future-madden-0tote/) approach of capturing how you actually work and think, using [skills to teach AI to do recurring work](https://www.citrix.com/blogs/2026/03/12/skills-are-all-you-need/), and [making the invisible 80% of your work visible](https://www.citrix.com/blogs/2026/01/13/the-invisible-80-what-corporate-led-ai-transformations-cant-see/).

Once you've built out all the layers of your cognitive stack, agents stop being the only destination, instead becoming just one of many approaches in your AI arsenal, (alongside in-context reasoning, skills, and just doing things yourself). The future of AI in the enterprise isn't about racing to deploy agents. It's balancing the right effort, the right tool, and the right type of token for each task.

The companies who figure this out will "run" circles around the ones racing straight to agents. They'll spend a fraction of the tokens, deliver higher quality work, and reach for an agents only when actually warranted. The ones racing straight to agents will burn tokens, dollars, and effort [wondering why their pilots stalled](https://www.citrix.com/blogs/2025/08/27/everyones-wrong-about-why-enterprise-ai-is-failing/).

Crawl before you walk. Walk before you run. Run fast when you need to, but never forget how to walk and crawl.
