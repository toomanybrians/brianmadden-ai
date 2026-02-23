---
title: "Generative AI in the enterprise: lots of hype, little practical advice. A World AI Cannes Festival report."
date: "2024-02-13"
authority_level: 5
file_type: linkedin-article
tags: [generative-ai, enterprise-ai, conference-report, hype, use-cases, waicf]
related_frameworks: []
original_url: "https://www.linkedin.com/pulse/generative-ai-enterprise-lots-hype-little-practical-advice-madden-fketc/"
staleness_threshold: stable
---

# Generative AI in the enterprise: lots of hype, little practical advice. A World AI Cannes Festival report.

*Brian Madden—February 2024*
*Published: https://www.linkedin.com/pulse/generative-ai-enterprise-lots-hype-little-practical-advice-madden-fketc/*

*Header image: Adrien Huerre and Brian at the World AI Cannes Festival, Feb 8, 2024.*

A slide from a session at last week's World Artificial Intelligence Cannes Festival (WAICF) led with, "76% of IT decision makers think Generative AI will be significant, if not transformative, for their organizations." I certainly agree with this sentiment, as I've been studying enterprise AI for the past year and recently joined consulting firm ILKI as their AI Tech Lead.

This slide was from a session whose title promised "Real-world tactics for implementing and succeeding with Generative AI". Awesome! This is exactly why ILKI CTO Adrien Huerre and I attended this conference!

The speaker continued, explaining that productivity gains, streamlined processes, and cost savings were the Top 3 ways Gen AI would make an impact, underscoring that attendees can "Use Gen AI to implement business processes which were previously impossible / unthinkable!"

I was ready for the real-world tactics that would reveal which productivity gains, how processes would be streamlined, and what costs savings would be achieved. Unfortunately, the only specifics I heard were to (1) order Dell servers, (2) download some language models, (3) and "play around and see for yourself what they can do."

What a wild hype bubble when vendors can get customers to buy servers first and then figure out what do to with them second!

Sadly, this pattern of "Set up the problem / Be disappointed in the lack of real answers" was repeated throughout the show. In another session titled, "Beyond the Hype -- The Value of AI around the Office Environment", the speaker warned about the dangers of hallucinations when using LLMs for data analytics. (He didn't offer an answer, rather he just mentioned you need to be careful.) A few minutes later, he talked about using LLMs to generate millions of individually-personalized customer emails. During the Q&A, I asked him about the dangers of inappropriate emails due to LLM hallucinations, and he responded, "you need to test 100 or 200 to make sure your model is basically working, but other than that, it's pretty much just hope for the best!" He literally made the fingers crossed "good luck" sign as he delivered the line with a straight face.

In a session titled "AI in the C-suite", an attendee asked, "Where should a middle-sized company start?" The McKinsey speaker's complete answer was, "The first step is to understand how AI and Gen AI can help your strategic objectives. Focus on limited domains, use a principled approach, and make sure those models are embedded in your business processes and change control processes."

I could go on, but you get the point. The agenda of this conference looked good, with plenty of office-focused session titles that included terms like "practical", "beyond the hype", and "real world". But in reality, these sessions were filled with meaningless jargon, platitudes, and nonsensical hype.

I don't think this is a fault of the conference, per se. Rather instead it just highlights that these seemingly easy questions don't have easy answers.

## My easy questions which are actually difficult

Last week on LinkedIn, I commented with a few questions about enterprise AI that I was hoping to learn about at this conference:

- How can enterprise organizations leverage AI and Gen AI in ways that are more than a party trick? What can you do with it?
- What are some examples which provide real value? What's the real use case?
- How do you begin to figure this out? What are practical first steps?
- What are actual companies doing?
- What should we avoid?

My experience after spending a few days in Cannes is that these seemingly easy questions are actually pretty hard.

## Enterprise Generative AI: A technology, looking for a solution, in search of a problem

Part of what makes my questions difficult is they're somewhat generic. I'm asking what a technology can do, rather starting with the more traditional/proper consultative approach of "what problem are you trying to solve?"

"AI" has been around for decades, and enterprises have been successfully leveraging AI in various narrow forms for just a long. Everything changed when ChatGPT was released in late 2022 and thrust Generative AI into the public. Most of us played with it a home, showed it to our friends, and proudly exclaimed, "THIS IS GOING TO CHANGE EVERYTHING!"

And now we're in that place where Gen AI is getting all the press. It's getting all the VC funding. It's constantly in the news. 76% of IT decision makers are saying it's going to be transformative for their organizations. So let's go! We're ready! Let's get started with some of that amazing transformation! Where do I sign up?

## First it's tactical, then it's everywhere

Most technology adoption cycles begin by solving specific, tactical problems, and then slowly fill in the gaps until they're ubiquitous. The Gen AI cycle is a bit different since everyone got access to ChatGPT, thought it was cool, thought "this will change everything!" and then tried to actually start using it at work.

The reality of Gen AI is that it's not ready for "everything" yet. We're learning that the world's best dirty limerick generator, while it does know a lot about most things, also happily makes up answers when it doesn't. It's actually quite a bit more useful at a bar than the office.

So now we have this technology which is mostly awesome, but somewhat of a wild card, and we're trying to get it a job. This is exactly backwards for how it should be. We have a technology in search of a use case.

## Today's enterprise AI: Keep it tight

My main takeaway from the World AI Cannes Festival 2024 is that today's Generative AI use cases in the business world are still extremely narrow and tactical. My list (and this is certainly not complete, even for today) of where Gen AI can help companies, in a generic sense today, looks something like this:

- Source code generation (GitHub Copilot)
- Cloud automation (Azure Copilot)
- Enterprise Search (Move beyond keyword matching and get into context & sentiment)
- Adaptive education (Convert between documents, text, videos, short form, long form, custom examples, etc.)
- Analytics (Have a conversation with your data, generate visualizations)
- Idea generation (Just as a brainstorming starting point)
- Marketing copy (Not direct emails, but generating content ideas)
- Language translation
- Content and document summarization & interrogation

There's one thing these all have in common today: They require a knowledgeable human in the loop before you can push the "execute" button.

For example, I do a lot of Python coding. GitHub Copilot is amazing and saves me time. (I estimate I write new code about 50% faster now.) But it occasionally produces code with errors. So I've learned that while I can use it to generate code, I need to treat everything it writes as a first draft, and visually read through each line to check for sanity.

At the WAICF conference this week, a Microsoft evangelist talked about Azure Copilot and said the same thing. While it provides an amazing natural language interface to manage your Azure estate, it can occasionally go haywire, so someone with actual knowledge needs to read through and verify all the scripts it writes before running them.

The same applies for brainstorming and marketing copy generation. LLMs are great as starting points, but they're not yet ready to generate stuff that goes directly into production or out into the world without a human in the loop. Of course this will change over time. We'll learn how to layer and sequence models, so one can check the other, with confidence thresholds that exceed the logic of humans. But for now, we need to treat these as very efficient rough draft creation systems.

## Was WAICF worth it?

Absolutely! Even though I didn't get answers to my questions, and I hard rolled my eyes in several sessions, visiting WAICF was hugely valuable for me:

- I met some incredibly interesting and smart people.
- I'm learning what the actual hard questions are and the right questions to ask.
- I'm starting to understand where the focused tactical starting points of real AI use in the enterprise are.
- I got about 20 ideas for future articles.

My focus at ILKI will continue to be the corporate adoption of AI and Gen AI, especially as it applies to "regular" companies. Sure, huge corporations with thousands of developers will be able to build their own models and do all sorts of wild, custom things. But there are thousands of "everyday" companies who can't throw dozens of developers at their own models, yet who want to use AI and Gen AI to increase productivity, streamline processes, and save money.

These types of organizations are my focus, what I'm digging into at ILKI, and what I'll be sharing in future LinkedIn articles. In the meantime, if you're in Paris and want to connect to talk about the actual things companies are doing to prepare for AI and Gen AI, please reach out. Let's figure this out together!

*This text is AI Influence Level 0: Human conceived & created.*
