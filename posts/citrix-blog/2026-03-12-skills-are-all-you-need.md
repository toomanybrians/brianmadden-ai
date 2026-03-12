---
title: "Skills are all you need"
date: "2026-03-12"
authority_level: 5
file_type: citrix-blog-post
tags: [skills, cognitive-stack, governance, post-application-era, knowledge-work, bitter-lesson, subscribable-brains, second-brain]
related_frameworks: [cognitive-stack, bitter-lesson, post-application-era, subscribable-brains]
original_url: "https://www.citrix.com/blogs/2026/03/12/skills-are-all-you-need/"
staleness_threshold: stable
---

# Skills are all you need

[Original post](https://www.citrix.com/blogs/2026/03/12/skills-are-all-you-need/)

*Brian Madden—March 12, 2026*

There's an emerging concept in the AI world that's important for everyone to understand: skills. I don't mean in the literal sense like "AI is skilled at summarizing documents", rather, a skill is a text file, written in plain English, that explains to AI how it should do something.

So there might be an "update the website" skill, which the AI can read to understand where the website files are, how to login, what the folder structure looks like, writing style guides, how to run tests to make sure the update is good, and how to deploy it. Once the AI knows how to find a skill, you can just tell the AI, "Hey add this to the website," and it can follow the instructions in the skill to actually perform that action.

Skills for AI are similar to skills for human workers. If you can write a doc which tells a new colleague how to do a thing, then you can write a skill for AI. (Honestly, it would be the same doc. Today's AI reads and follows skills just like humans.)

Anthropic just published a 30-page PDF on writing skills, and every major AI vendor maintains open repositories with thousands of them. (Check out the official skills repos from Anthropic, OpenAI, and Google, plus community collections like awesome-claude-skills, awesome-agent-skills, and antigravity-awesome-skills.) Browsing available skills feels like a LinkedIn Learning catalog, including things like "How to use Excel", "How to write a good project plan," or "How to properly research a product feature." (Plus literally thousands more.) Because AI models are so good at following instructions now, giving them access to well-written skills file is essentially giving them superpowers.

Skills are so fundamental to how AI will impact knowledge work that they have their own layer in my [5-layer cognitive stack](https://www.citrix.com/blogs/2026/02/25/understanding-the-cognitive-stack-why-your-ai-strategy-is-focused-on-the-wrong-layer/).

Once you understand what skills are, you understand:

- Why [the SaaSpocalypse happened](https://techstartups.com/2026/02/05/anthropics-claude-plugins-spark-285-billion-software-stock-selloff-as-ai-targets-entire-saas-workflows/). (Anthropic released skills for areas that overlapped with existing SaaS companies.)
- Why agent frameworks keep getting simpler instead of more complex. (Skills do the heavy lifting.)
- Why the [cost of building software](https://en.wikipedia.org/wiki/Product_requirements_document) collapsing to near-zero changes everything. (The expensive part (coding) is now cheap, the cheap part (writing specs) is now the most valuable thing in the process. And a skill is a spec.)

But this is just scratching the surface.

## Skills replace admin consoles, apps, and... yikes

Think about what any typical admin console actually does: it lets you set policies, configure rules, define thresholds, manage exceptions, etc. Now imagine that as a text-based instruction file: "When routing token requests, prefer the cheapest model that meets quality threshold X. Never send data classified above Y to external providers. Escalate to human when confidence drops below Z. Log all routing decisions for audit." That's a governance policy any AI can execute, version-controlled, auditable, and diffable. ("Diffable" is like tracking changes in Word, meaning you can see exactly what changed, when, and by whom.)

I actually walked through this realization in four stages in my [post-application era piece](https://www.citrix.com/blogs/2025/10/15/will-ai-need-to-operate-your-legacy-desktop-apps-or-is-direct-file-manipulation-enough/): (1) "We need Excel because Excel is important." (2) "AI will operate Excel for us." (3) "Wait, why does AI need Excel?" (4) "Just give AI the skill that describes what Excel was doing." Now we realize that apps were always just specs wrapped in a user interface, and once you remove the UI requirement, the wrapper disappears too, and all that's remaining is the skill.

## But wait, there's more!

Skills don't just replace admin consoles and apps. They replace all the ways knowledge workers create value. [Julien Bek at Sequoia wrote about this last week](https://sequoiacap.com/article/services-the-new-software/) pointing out that while the software industry is $300-500 billion, knowledge worker wages are $4-5 trillion. Skills aren't eating software, they're eating labor. So now you can understand when Mustafa Suleyman (Microsoft's AI CEO) says [all knowledge work could be automated in 12-18 months](https://fortune.com/2026/02/13/when-will-ai-kill-white-collar-office-jobs-18-months-microsoft-mustafa-suleyman/), this doesn't actually sound that crazy.

What's truly wild about skills is you don't have to sit down and deliberately write them. I've been using AI as a cognitive extension ([a second brain](https://www.citrix.com/blogs/2026/02/11/workers-second-brains-break-every-assumption-about-how-we-secure-knowledge-work/)) for a few months, and early on I told my AI to continuously mine what I'm doing for reusable skills. I dug into the file system recently and found 40-50 skill files I never deliberately wrote: how I evaluate a strategy doc, how I prep for a board meeting, how I structure a blog post, etc. And they are really good! (Way better than I could've written or articulated.) The AI just watched me work and codified the patterns.

This is why understanding the cognitive stack is so critical to understanding the future of knowledge work, and why AI, when approached from the top of the stack down, will fundamentally change work forever.

Skills are what make the "retiring VP" scenario real. (If a VP had been using AI like a cognitive extension, their skills would already be there.) And once they exist, they're shareable: a junior analyst can layer a senior partner's evaluation skills on top of their own and get the benefit of 30 years of pattern recognition immediately. Any worker could [subscribe to the skills of the three smartest people in their field](https://www.linkedin.com/pulse/hey-creators-stop-publishing-content-start-your-second-brian-madden-ca0ae/) and see their output instantly get better. This is Matrix-level skills acquisition but literally happening in real life, today. (Several of my Citrix colleagues and I work this way today.)

Now imagine scaling that across an organization, and it gets even more wild. When everyone's skills are visible, composable, and stackable, the knowledge hierarchy flattens. You can see where ten people are doing the same thing ten different ways and converge on the best version (with a simple way to redistribute that across the org). The org chart stops being a proxy for who knows what.

## Skills appreciate, software depreciates

Most software loses value over time: it needs updates, patches, migrations, and eventually a full rewrite. Skills work the opposite way. Every AI model improvement makes your existing skills more valuable, not less, because better AI executes the same instructions with better judgment.

A skill file says "here's what to do and here's how to know if you did it right." Opus 4.6 executes the that "optimize task routing" skill better than Opus 4.5 did, and Opus 5 will execute it better still. Every model generation improves the framework without anyone touching it.

This is [the bitter lesson](https://www.citrix.com/blogs/2025/09/17/the-bitter-lesson-of-workplace-ai-stop-engineering-start-enabling/) applied to enterprise tooling. You don't need to build scaffolding around AI. Just write down what you want and let intelligence figure out how.

## The governance angle

Every CISO I talk to is [struggling with AI governance](https://www.citrix.com/blogs/2026/01/21/everyones-worried-about-the-wrong-ai-security-risk/). How do you audit what an AI did? How do you enforce policy on a conversation? How do you ensure compliance when the "workflow" is a human typing into a chat box?

Skills solve this in a way nothing else does. They're text files, so they're auditable. They're in git, so they're version-controlled and diffable. They're composable, so you can layer enterprise policy skills on top of personal and team skills with enterprise compliance skills overriding personal preference skills. Skills become [the governance layer of the cognitive stack](https://www.citrix.com/blogs/2026/02/25/understanding-the-cognitive-stack-why-your-ai-strategy-is-focused-on-the-wrong-layer/) as the natural unit for controlling what AI does, how it does it, and who authorized it.

## So now what?

Skills replace apps, admin consoles, and entire categories of software. They capture expertise that used to walk out the door when people left. They appreciate with every model improvement. And they're the natural governance unit for an AI-powered workplace. All of that, from a text file. (Heh, turns out that "just understanding language" might actually be all AI needs to be extremely powerful.)

The question isn't whether to write skills. It's whether you want to be the one writing them or the one being replaced by someone who did.

I know which side I'm on.

---

This continues my series on [the post-application era](https://www.citrix.com/blogs/2025/10/01/welcome-to-the-post-application-era/), [the cognitive stack](https://www.citrix.com/blogs/2026/02/25/understanding-the-cognitive-stack-why-your-ai-strategy-is-focused-on-the-wrong-layer/), [the coding-as-leading-indicator framework](https://www.citrix.com/blogs/2026/02/19/what-will-knowledge-work-be-in-18-months-look-at-what-ai-is-doing-to-coding-right-now), and [the bitter lesson of workplace AI](https://www.citrix.com/blogs/2025/09/17/the-bitter-lesson-of-workplace-ai-stop-engineering-start-enabling/). If skills sound abstract, I built a working example: [brianmadden.ai](https://brianmadden.ai) is an AI-native knowledge system running on skills files, open for anyone to connect to.
