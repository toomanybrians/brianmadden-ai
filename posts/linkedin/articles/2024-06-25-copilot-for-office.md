---
title: "I've been using Copilot for Office for months. Here's how it works and what it can do today."
date: "2024-06-25"
authority_level: 5
file_type: linkedin-article
tags: [copilot, microsoft-365, workplace-ai, enterprise-ai, product-review]
related_frameworks: []
original_url: "https://www.linkedin.com/pulse/ive-been-using-copilot-office-months-heres-how-works-what-madden-nqu6c/"
staleness_threshold: stable
---

# I've been using Copilot for Office for months. Here's how it works and what it can do today.

*Brian Madden—June 2024*
*Published: https://www.linkedin.com/pulse/ive-been-using-copilot-office-months-heres-how-works-what-madden-nqu6c/*

*Header image: Slide showing "All real Copilot benefits, according to Microsoft's website." AIL0 / created by the author.*

"Copilot" is an umbrella brand Microsoft uses for LLM-powered orchestration tools which add & integrate AI / GPT functionality into existing Microsoft products. There are currently more than 130 different tools under the Copilot brand. Naming conventions are all over the place. For example, the Copilot functionality in Microsoft Word is variously referred to as "Copilot in Word", "Copilot for Microsoft 365", and even just plain "Microsoft Copilot".

I've been using Copilot for the various Office products for a few months, and in this article, I'm going to explain what it's like and how it works for those of you who haven't tried it. (Note this is not a proper "review", rather I'm just telling stories about my experience with it.)

In this article, when I say "Copilot", I'm specifically referring to the Copilot functionality in Microsoft Word, Excel, PowerPoint, Outlook, and Teams.

## What does Microsoft say you do with Copilot?

Microsoft's marketing materials have huge lists of things you can do with Copilot. I won't retype them all here, but you can check the features for yourself directly from Microsoft.

In layperson's terms, Copilot is essentially "ChatGPT integrated with Microsoft Office apps." When you enable Copilot (which you can do on a user-by-user basis as a $30/month add-on to an existing Office 365 subscription), a new Copilot icon appears in your Office apps. Clicking that opens a sidebar with a ChatGPT-like chatbot interface directly in the Office app, which lets you ask questions about the document that you're currently working on.

Various Office apps also have other integrations. For example, when you start a new paragraph in Word, a Copilot icon will appear in the left margin, or when you start a new email in Outlook, a message in the blank email body asks if you want Copilot to help write the email. Those are just convenience shortcuts though, mainly to remind you that Copilot is there and giving you a quick way to engage with it. The actual functionality is identical regardless of whether you use the sidebar or one of the integrated shortcuts.

## What can you actually do with Copilot?

I've been using Copilot every day for several months—not as a fake test, but as a paid subscriber as part of ILKI's corporate Microsoft 365 subscription. Based on that, I can summarize Copilot like this: "Early preview, has potential, not there yet."

That said, Copilot is clearly the future, and it will be important for every organization to understand and leverage it. So even though the functionality is quite limited today, I still believe it's worth getting Copilot subscriptions for a few employees to start using and learning about it. But I can't imagine rolling it out in anything close to a "production" capacity to all your users yet.

## Things to keep in mind before trying / judging Copilot

Based on using Copilot for awhile, here are some important things to know that everyone evaluating it should know.

- Copilot is cloud-based, and as far as I can tell, everything it does runs in the cloud. For example, Copilot cannot interact with a local-only document, rather, you need to have the document stored in OneDrive or SharePoint, because even though you chat with Copilot locally, when it's analyzing or editing the document, it's accessing the cloud copy of it on the backend.
- Copilots can find everything. Remember Microsoft Delve, and how employees found secrets that they had access to but didn't know about? This is like that, but with AI-powered search. So make sure your access rights are dialed in before employees start asking Copilot "What secrets is management hiding from me?"
- The various Copilots use both OpenAI and Microsoft proprietary models. Which exact model(s) could vary and change.
- Copilot changes often. The release cycles are continuous and frequent. (Even the information in this article could be different by the time you're reading it.) If you played with Copilot a month ago, things could be different now.
- Some Copilot updates are baked into new versions of the Office apps (which require an app update to get), while others are transparency applied to back-end cloud services updates.
- The Copilot experience is different using local Office apps versus the web apps.
- The Copilot experience varies depending on the language. (The LLMs are better with some languages than others, and some features only work in some languages.)
- The Copilot experience varies depending on the region it's being used in. For example, Microsoft must respect different regulations in Europe versus the US. Also, different regions have access to different compute clusters, different underlying models, etc.
- The general speed and performance of Copilot can vary for random reasons, such as availability and load of nearby cloud compute, maintenance, rain, etc. Even as a regular user, my experience differs day-to-day. Something that worked yesterday might not work today, etc.

A rapidly evolving product + huge demand growth + global cloud load-balancing + product which generates stochastic outputs = lots of gritted teeth when I demo it to someone.

## Thoughts on Copilot today

So, applying the standard disclaimer that my experience might not be the same as yours based on all the points above, what's it like using Microsoft Copilot daily today?

As I mentioned previously, the actual capabilities of Copilot today are quite limited compared to its potential and what you might expect. Even doing many of the things Microsoft mentions in their Copilot marketing material often requires taking very specific non-intuitive steps. I'm sure this is temporary. Microsoft is jokily known for shipping buggy and incomplete "version 1" products, and while Copilot doesn't have traditional version numbers, Copilot today is solidly a "Microsoft v1." But Microsoft is also known to keep plugging away until their products eventually get there, and I expect these limitations will not exist in the next year or two.

The way to frame what Copilot can (and can't) do today is to make this your mantra: **Copilot is based on an LLM which works with text. If you want to do something with or about text, Copilot can probably do it. Everything else is very limited or not possible.**

For example, the oft demoed "create a PowerPoint from this Word doc" is really doing something like this under the hood:

1. Use Copilot's text processing capabilities to summarize the document to create a PowerPoint-ready outline of the presentation text content.
2. Send that outline to the PowerPoint Designer to which then generates the slides.

I should point out that Designer is not a Copilot feature, rather, it's a "smart designer" slide creation/beautification capability which is part of standard Microsoft 365 subscriptions.

So while it's cool that a Copilot prompt of "convert this document into a presentation" works, Copilot isn't really "making your slides", rather it's just creating the text, and the Designer is the thing actually making the slides. That may seem like splitting hairs, and really who cares? I ask Copilot to create a presentation, and I get a presentation. What's the beef?

The issue is that because Copilot didn't actually make the slides, you can't really use Copilot to do anything to the slides once they already exist. Asking Copilot to "change the color scheme" of the slides, or to "replace the images with ones of a sports theme", results in Copilot responding that this request is not something it knows how to do. (Funny that whenever Copilot tells you it can't do something, it will then give you a list of the exact phrases you can use for the relatively limited subset of things it can do. It feels a lot like using Siri.)

You'll run into similar limitations with Copilot across the entire Office ecosystem. When Microsoft says that Copilot can write emails for you, they literally mean just the writing part. I cannot type "Send an email to Vincent about the meeting" in the Copilot chat box in Outlook. (Actually, there isn't even a general Copilot chat interface in Outlook.) Instead, I need to follow the standard manual process—start a new message, fill in the To:, Subject:, etc., and then when I have the blinking cursor in the email body, that's where Copilot wakes up to help draft or rewrite the text.

Even if I start with the Copilot chatbot interface on office.com, and say, "Send an email to Vincent to schedule the meeting tomorrow," Copilot will just respond with a very generic email which I then need to copy and paste into my email app. It can't create the email, and it doesn't know the context even though Vincent and I just had a chat conversation via Teams discussing a meeting topic and time for tomorrow.

Apart from Copilot's ability to look up the proper email address, (which it provides in a footnote), there's no real added value here versus just using any one of the public LLMs via some website. This AI will not be discovering 500,000 new proteins.

The same is true in Word. While the Copilot sidebar lets you summarize or ask questions about the document content, and an in-line Copilot icon gives quick access to a pop-up for it to generate, edit, or rewrite text, Copilot can't really do anything apart from editing text in the document itself. As an example, for this article you're reading right now, I initially wrote it in markdown, then pasted into Word to prepare it for posting to LinkedIn. I asked Copilot to convert the lines that start with ## to Heading 2 styles, and to replace straight quotes with curly quotes, but both of those resulted in the response, "Unfortunately, I cannot make changes to the document itself, but I can answer general questions or those related to the document."

## Copilot squeezes a lot out of "just" wrangling text

Even with those limitations, Copilot can squeeze quite a bit of capability out of the "only works with text" limitation of today. At the high level, this means it can:

- Generate text from prompts
- Edit text
- Summarize text

Each of those bullets has many practical applications within the Office suite. For example, the simple skill of "edit text" enables users to:

- Add or remove sections of documents
- Offer suggestions for improvements to documents
- Rewrite text to change length or tone

Similarly, the simple skill of "summarizing text" enables:

- Summarizing Word docs & PDFs
- Enabling you to ask questions about the content of a document (or any long text section, email, PPTX, etc.)
- Summarizing Teams meetings (creating meeting summaries, that cool "catch me up" feature when people join late, etc.)
- Summarizing email conversations
- Scanning your inbox and telling you what emails are important (Copilot just looks at all your recent unread emails which are nothing more than, wait for it... long text to summarize!)
- Generating the slide content (nested lists of bullets) from other things (meetings, Word docs).

Even Excel suffers from similar limitations. (Which, at least in the French version I use, even Microsoft labels the Copilot experience in Excel as a "preview".) I had a spreadsheet with three separate tabs that represented three different future scenarios—a potential "good, better, best" case analysis, and I hoped Copilot could tell me what the differences in assumptions were across those three sheets. Unfortunately it could not, as the only way it can interact with Excel sheets is if you select extremely simple regions and convert them into tables, which you can then ask questions about. (The "good" capabilities, like generating charts or doing data analytics, are already existing features of Excel that Copilot just launches for you, similar to the Designer feature in PowerPoint.)

## Final thoughts

I'll close by reiterating that I'm sure Copilot is going to be awesome in a few years. But based on what I've experienced today, it seems extremely limited and not much better than just using an existing web-based or other standalone LLM tool. In fact for that good-better-best analysis I wanted to do, since Copilot couldn't handle it, I just saved it as a CSV and uploaded it to ChatGPT, Claude, and Mistral, and all three of them were able to do the full analysis for me. (The new Claude Sonnet 3.5 was the best.)

Most of the publicly-available LLMs only cost around $20/month which is 33% cheaper than Copilot, and apart from saving a few steps of copying-and-pasting, they really seem to have more functionality. (Also Copilot is really slow, especially compared to Claude and Mistral.)

So for now, Office Copilot, yawn, but of course I'll keep my subscription because I'm interested in following the evolution over the next several years. I'll keep you updated when as needed.

*This article is AI Influence Level 0: Human conceived and created, with no AI involvement.*
