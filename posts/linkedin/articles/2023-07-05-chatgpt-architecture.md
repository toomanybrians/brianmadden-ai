---
title: "A look at ChatGPT's architecture. A lot for enterprise admins to like!"
date: "2023-07-05"
authority_level: 5
file_type: linkedin-article
tags: [chatgpt, enterprise-it, architecture, llm, ai-management]
related_frameworks: []
original_url: "https://www.linkedin.com/pulse/chatgpt-more-like-standard-enterprise-app-than-you-think-brian-madden/"
staleness_threshold: stable
---

# A look at ChatGPT's architecture. A lot for enterprise admins to like!

*Brian Madden—July 2023*
*Published: https://www.linkedin.com/pulse/chatgpt-more-like-standard-enterprise-app-than-you-think-brian-madden/*

*Header image: ChatGPT conceptual architectural diagram showing the flow from User Interface through API, Input Validation, Sanitization, Tokenization, AI Model Server, Detokenization, Formatting, Compliance Checks, and back out through the API to the User Interface.*

Last week I wrote about how AI is much more than ChatGPT, and showed how the ChatGPT application fits within the AI taxonomy. Today I want to dig into the architecture of how an app like ChatGPT works, since we'll most likely need to start supporting apps like ChatGPT in the future.

While ChatGPT is just a "single application" to the layperson, those of us in the enterprise IT world recognize it as a fairly typical client/server app which is more of a collection of multiple applications, services, and interfaces working together to deliver the end-user functionality we called ChatGPT.

I put this diagram together to show a conceptual architectural flow of the various components that make up the ChatGPT app. (In principle this would apply to any larger language model-based app.)

Every user interaction with ChatGPT follows this high-level flow:

1. **User Interface.** This is where the user interfaces with the GPT. ChatGPT today uses either a web-based UI or an iOS app. In addition to the core chat interface, the UI layer is also responsible for wrapping that GPT core into the things that make it an "app", like conversation history, context retention, and settings for which GPT is used and how it behaves.
2. **API Endpoint.** Typically an HTTPS interface which sits between the UI and the back-end systems. This is what lets ChatGPT interface with anything out in the world. The API passes text back and forth, handles authentication, and has mechanisms for handling errors, maintaining session information, enforcing rate limits, etc.
3. **Input Validation.** Ensures the text coming in passes some basic syntax tests: does it fit within the specs (not too long), is not empty, doesn't contain illegal characters, etc.
4. **Input Sanitization.** A security check that removes or escapes anything that could be harmful, including both the meaning of the content (does it comply with the policies for prohibited content), as well as checking for technical compliance issues, (like SQL injection or other security risks).
5. **Tokenization.** Converts the incoming text stream into the tokens which is what the GPT AI model actually processes. (Tokens are just numbers which represent groups of characters which is what the AI model actually processes. They don't know anything about text.)
6. **AI Model Server.** This is where the actual AI model (gpt-3.5, gpt-4, etc.) runs which does what most people perceive as the actual work. Everything is token-based at this point, as the model does not "understand" words or text at all. It simply takes an input stream of tokens (which are just numbers) and produces a probabilistic prediction for an output sequence of tokens based on the patterns it learned from its massive pretraining.
7. **Detokenization.** Runs the tokenization process in reverse, converting the stream of tokens (numbers) from the model's output back into text.
8. **Formatting.** Cleans up the text and makes sure its in the format the user needs. This could be mundane things, adding or removing white space or newlines, escaping text or code blocks, or generally making the response look right.
9. **Compliance Checks.** Checks the text against whatever policies are in place to guide what content is acceptable. This is where the platform checks for hate speech, illegal activities, trade secrets, personally identifiable information (PII), etc.
10. **API Endpoint.** The resulting text is sent out via the same API interface that the initial query came in.
11. **User Interface.** Finally, whatever interface the user typed their query into a few seconds prior now shows the results.

Again, this is a simplified conceptual diagram, but by looking at all the steps together, you can see how ChatGPT looks pretty similar to any standard client/server enterprise app, which is great, because...

## All these client/server components mean we can manage ChatGPT like an enterprise app

The popularity of ChatGPT can be scary to IT admins. It's this decade's "consumerization of IT" challenge, where our users just go out and do corporate things via new consumer cloud apps while we try to wrap our heads around everything.

The good news is that even though the architecture I walked through used ChatGPT as an example, any large language model with a conversational interface has similar components and flow. (So this would also apply when using Gmail's Smart Compose or Microsoft 365 Copilot in Teams meeting summarization features.)

All this means that as these models and apps start to make their way into the enterprise, you'll be able to manage, maintain, and monitor them just like any other client/server cloud-based app. You'll be able to tune what runs where, just like any app, based on the security, privacy, performance, and cost needs. Some components may run in the cloud with other parts on prem. Some you'll operate yourself, others will be consumed as a service. Some you build, some you buy. Again, it's really no different than anything you're doing now.

All of the typical service management, SLA, governance, compliance, business continuity, and change management procedures you have now will also apply to your LLMs and other AI-based applications. So, more dashboards and more APIs! Yay?

Obviously this high level overview is just scratching the surface of how an AI is managed. In my next few articles, I'll dig deeper into how you map this to your existing teams. We'll look at how this impacts an org chart, what runs where, how you start to wrap your head around risk, and the first steps you can take today to get ready.

We all know that the AI apps are coming to the enterprise. While users gush, vendors spin up new offerings, and policymakers argue, we IT professionals will keep the lights on. We've been doing it for decades, and from our point of view, these rounds of apps are no different.

*This article is AI Influence Level 0: Human conceived & created.*
