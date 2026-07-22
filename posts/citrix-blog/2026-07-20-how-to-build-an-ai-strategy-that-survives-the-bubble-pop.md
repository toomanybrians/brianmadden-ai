---
title: "How to build an AI strategy that survives the bubble pop"
date: 2026-07-20
url: https://www.citrix.com/blogs/2026/07/20/how-to-build-an-ai-strategy-that-survives-the-bubble-pop/
tags: [ai-bubble, invariants, open-weight-models, second-brain, knowledge-factory, workspace-as-control-plane, token-economics, data-portability, futurism]
authority_level: 5
file_type: blog
staleness_threshold: stable
---

# How to build an AI strategy that survives the bubble pop

Over the past few weeks, noise that there's an AI investment bubble which is about to burst has picked up. In this post, I'll dig into what that might look like and how you can think about your company's AI strategy to successfully navigate whatever happens next.

(Quick program note: we discussed this topic on the Citrix AI Hotsheet podcast last week (audio | video), and it was the main topic of my keynote at the Arrow Forum 2026 in Germany last Thursday which has been integrated into my public knowledge repo "second brain" that you can query and integrate into your own AI. So if you want the latest without waiting for me to write a blog post, check those out!)

## Will the bubble pop? And when?

Last month I wrote a blog post discussing how (as Citrix's futurist) I think about the future. The important takeaway for today is that because predicting the future is impossible (and reckless), a futurist's actual job is to think through a broad range of futures, work out what things would be true across all potential future paths, and then plan for those. (We call those "invariants": things that are true no matter what.)

I mention this because if you're planning for the future properly, then whether there's an AI investment bubble, and when or if it bursts, shouldn't actually change your strategy or plans. This is one of the most important aspects of my role at Citrix and something I've written about extensively over the past year.

So keep that in mind for this post: I'm not saying there is or isn't a bubble, or that it will or won't pop soon. Instead, this post focuses on one (of many) future scenarios where there is a bubble and it does burst, and it looks at how the AI strategy that you've (hopefully) built survives that pop moving forward.

## What will a bubble burst look like?

The general narrative of AI progress is "capabilities will increase, costs will decrease, and there's no end in sight." So a bubble burst, regardless of how it happens, means (1) AI capabilities stop increasing and/or (2) AI costs stop decreasing.

People are quick to point out that, "Even if the bubble pops and the frontier AI labs go out of business, we'll at least still have access to all the infrastructure they built." This makes sense at a glance and mirrors what happened with past bubbles. (Railroads' collapse left all the rail infrastructure behind, the dot-com burst left the dark fiber, etc.)

However it's not guaranteed that AI would follow that same pattern. Sure, the chips, datacenters, and AI models which exist today would in theory be available even if the AI labs vanished tomorrow. But that doesn't mean that whatever entities remain will be able to serve them as they are today. For example:

- It's unclear if serving today's models is profitable for the large AI providers. Post bubble pop, assuming the technical capabilities to serve the frontier models still exist, access could be several orders of magnitude more expensive and/or slower.
- If the whole AI economy collapses (which could also bring down the larger global economy), the controlling governments (mainly US and China) might decide the frontier models have national security relevance, and they could block, limit, and/or control who has access. (The US government recently set that precedent with Mythos, Fable, and GPT-5.6. It's fair to expect more.)
- It's possible that even if current models exist, future progress slows or pauses. (You might be able to access capabilities that exist today, but not be able to count on the familiar pace of improvements.)
- Some combination of the above. For example, the government allowing some entity to serve mid-tier models to the public while reserving frontier models for government, national security, and/or favored company use.

## Building for uncertainty: why open-weight models matter

If you want to future-proof your plans today, you need to stop planning for the hypothetical future capabilities of AI and start focusing on what you can do with the current capabilities of models that you can reasonably assume will exist after the bubble pops. The way to do that is by looking at the models whose weights have been released (called "open-weight" models), which means they can be downloaded and served independently of whether the AI labs which created them are around.

To be clear, I'm not suggesting that you switch to running open-weight models for all your workflows today. (Though it's probably not a bad idea to at least try them so you're familiar with the process and capabilities. You can access open-weight models online and use them just like ChatGPT: you don't have to run them on your own hardware.) In terms of capabilities, the latest open-weight models sit roughly in between Sonnet and Opus, meaning it's reasonable to assume that anything you can do with Sonnet today, you'll also be able to do post bubble pop with open-weight models.

The current best downloadable open-weight model is GLM-5.2 from Chinese lab Z.ai, MIT-licensed. There are also several other very capable Chinese models available, including some with big claims made just in the past few days. One is Kimi K3, the latest from Chinese lab Moonshot and made available last week. Early testers suggest it's in the Opus-to-Fable capability range. However, its weights have not yet been released. (They're scheduled for release next week, but a lot can happen in a week, so we'll see.) And just a few hours ago, Alibaba previewed Qwen3.8, which they claim is second only to Fable 5 (though there are no published benchmarks yet). Alibaba is also claiming they'll release the weights "soon", though they've not historically released weights for their flagship models. So again, we'll see.

By the way, using a Chinese model doesn't automatically mean you're sending all your data to China. Since these models can be downloaded and run anywhere, you can access them from hosting providers around the world.

There are US open-weight models too, from Thinking Machines, NVIDIA, Google, and others, and while they're improving fast, they're not as capable as the Chinese open-weight models today. (This could change instantly if (1) Anthropic or OpenAI decided or was forced to release the weights of any of their higher-end models, or (2) China decided to stop releasing the weights of their best models.)

One final thing that's important to know about open-weight models is just because they're "open" and "downloadable" doesn't mean they run on your laptop or on a workstation under your desk. While slimmed-down versions of these models designed to run on lesser hardware exist (with proportionally lower speed and capabilities), the full capability, full-speed Opus/Sonnet/Fable level open-weight models require ~$300,000+ datacenter-class hardware with datacenter-class power and cooling. This is absolutely possible for hyperscalers, hosting companies, and even large enterprises, but not something you're running in your basement.

## What can you do with the current capabilities of open-weight models?

If the only future you can reliably plan for is based on open-weight models that exist today, the next logical question is "what can I do with those?" Luckily the leading open-weight models in the Sonnet/GPT-5.5 class range are extremely capable.

Models in this range are already in wide use because they're significantly cheaper than higher-capability models. For Sonnet itself, it's roughly half the cost of Opus and a third the cost of Fable, so it's quickly become the go-to workhorse for many daily enterprise AI needs. For example, I've been using Sonnet as my interface to my AI second brain, and many of the various AI-powered workflows we use internally at Citrix don't need more than Sonnet-class capabilities. (This is because the type of AI use which provides actual ROI today is typically AI managing and orchestrating administrative and work processes, rather than some kind of sophisticated frontier model magic synthesis. Today's Sonnet-class models are the perfect balance of capability, speed, and cost.)

## Here's your actual strategy

Now that we've covered the post-pop landscape, let's look at what your actual strategy can be. The thinking behind it is simple: what should you do now to prepare for whichever future shows up? (Remember, even though this post is about what to do if the AI bubble pops, there's also a chance it doesn't pop. So you need to be ready for both scenarios.)

- Build your second brain. (Why | How to get started) Sonnet-class models are more than capable of powering it, and the second brain context architecture is (by design) portable across AI models.
- Also build the organizational version of it. (We've been calling this a "knowledge factory" in the podcast and discussed this in episodes 3 and 4.) It's essentially getting your company's collective context organized, reconciled, and queryable.
- Govern the workspace, not the AI model. Regardless of whichever models survive, AI and workers will still need identity, guardrails, auditing, and a secure place to operate. That's the workspace-as-control-plane thesis I've been writing about for the past 18 months, and it also applies regardless of which AI model you use.
- Get serious about model routing and token economics. AI tokens aren't free in any near future scenario. Knowing which work needs which level of intelligence at which cost is going to be important no matter what. (It's worth mentioning that there are commercial and geopolitical reasons to subsidize tokens, even for open-weight model hosting, so unless you're hosting the model yourself, don't assume the price you pay today is the price you'll pay tomorrow.)
- Keep your data portable. Don't lock your workers' or organization's knowledge context into any one vendor's system. The same corpus should be able to point at a frontier API today, a self-hosted open model tomorrow, or whatever comes after.

The bottom line is no one knows if/when/how the AI bubble will pop. So the only rational strategy for you is to build on those invariants (the things you know will exist in all futures), including AI models no one can take away from you, running on hardware you can own, working against data you control and context you've built. If you do this, the AI bubble headlines become what most AI news already is: interesting bar conversations, but nothing that changes your plans.

Do that work now.

## Read more & connect

Join the conversation and discuss this post on LinkedIn. You can find all my posts on my author page (or via RSS).
