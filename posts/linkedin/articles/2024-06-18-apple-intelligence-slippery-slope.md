---
title: "Apple Intelligence is the beginning of a slippery slope that all companies need to understand today"
date: "2024-06-18"
authority_level: 5
file_type: linkedin-article
tags: [apple-intelligence, consumerization-of-it, workplace-ai, employee-culture, ai-adoption, generative-ai]
related_frameworks: []
original_url: "https://www.linkedin.com/pulse/apple-intelligence-beginning-slippery-slope-all-companies-madden-iyuyc/"
staleness_threshold: stable
---

# Apple Intelligence is the beginning of a slippery slope that all companies need to understand today

*Brian Madden—June 2024*
*Published: https://www.linkedin.com/pulse/apple-intelligence-beginning-slippery-slope-all-companies-madden-iyuyc/*

*Header image: GPT-4o generated image depicting "Apple Intelligence" and its "Impact on IT" with slightly uncanny faces and people sitting on invisible things.*

By now you're aware that Apple announced their AI plans, called "Apple Intelligence," at WWDC last week. Hundreds of opinion & analysis pieces have been written since, with people split on whether it's awesome or lame, and whether Apple is pulling ahead or falling behind. I have nothing to add there, though I'll link to Scott Galloway's perspective as it's the one I most agree with.

Instead, I want to focus on Apple Intelligence through the lens of corporate IT. When large swaths of employees get access to these capabilities over the coming months, what will the impacts to the company be? Should they be concerned? What are the risks?

Fundamentally, this is just a continuation of the "Consumerization of IT" conversation we started 15 years ago: (1) Employees get direct access to powerful new tech, (2) companies must figure out what it means and how to respond. So we can approach this in the same way too, with the first step being to understand what the actual tech is, and then think about its direct and second-order effects.

I'm not going to rehash the details of Apple Intelligence since there are already a million articles on that. Instead I'll walk through the specific things that corporate IT folks should know about.

## The IT security risk of Apple Intelligence is low

The first thing that comes to mind about employees using Apple Intelligence is the security risk. Elon Musk lit that fire when he wrote that Apple devices would be banned from his companies due to these risks. While most of what he wrote is untrue and has since been fact-checked, he succeeded in planting the seed in millions of people that Apple Intelligence is not secure and should not be trusted.

To me, the real question is, "secure compared to what?"

For companies who do not allow personal devices, or who require EMM, UEM, and/or locked down devices, they can simply block or disable these new features and carry on as usual.

For companies who allow employees to use personal devices, then Apple Intelligence can't possibly be worse than all the existing LLM apps, sites, assistants, and tools that employees already have access to and are using on their devices today.

### But it's sending data to the cloud!

These new Apple Intelligence features are "dual-stage", where there's a lighter-weight LLM which will run locally on the device, and then for scenarios where the device model isn't powerful enough, the request will automatically be "cloud bursted" to Apple's Private Cloud Compute.

For cloud and virtualization nerds like me (and probably most people reading this), this is awesome, and, quite frankly, exactly the holy grail of edge computing / cloud-bursting / modern app architectures that we've been excitedly hyping for a decade. I would think we'd be celebrating this.

Negative reactions to Apple's plans here fall into the broad "but you can't trust the cloud" category. These arguments are anachronistic and tired, and from the corporate standpoint, the remaining organizations who "can't trust the cloud" in 2024 already have x-ray security with no personal electronics going in or out, and employee BYOAI is not a thing for them.

The rest of the world is already using Azure, AWS, GCP, and others, so the real security questions about Apple Intelligence is whether it's at least as secure as the cloud things companies are already doing today. From what Apple has shared so far, their approach to security here is impressive. Apple's Security Engineering and Architecture team published a paper which explains more about how the Apple Private Cloud Compute works, including why they don't trust public clouds for this task and how their Private Cloud Compute is designed. (TLDR: stateless compute, enforceable guarantees, custom stripped-down OS, verifiable transparency, and truckloads of M2 Ultra processors.)

### What about the ChatGPT part? Is that more of a risk?

Apple has also designed a framework where Siri can reach out to third-party LLMs for requests it's not able to fulfill on its own. Apple will first launch this functionality with ChatGPT as their partner, but they mentioned that other LLM vendors (Google, etc.) will be added in the future.

Peoples' negative reactions to this have been all over the map, but they broadly sort into expected categories like, "You can't trust OpenAI," "If Siri has access to your entire device, now OpenAI will have access to your entire device," and "Now they're going to train the next GPT on your own personal data!"

Apple and OpenAI have described how this integration will work, and the things many people are afraid of do not align with those explanations. The functionality which escalates user requests to third-party LLMs on Apple devices is optional. It will behave like existing third-party integrations (browser, email client, maps, music, etc.), and the user or device manager will be able configure whether it's always allowed, allowed on a case-by-case basis with user approval, or disabled entirely.

So if you manage a bunch of Apple devices and don't trust OpenAI, you can just disable this integration. And if you have a bunch of employees with Apple devices that you can't manage, then many of them are already using the ChatGPT app and this new functionality does not introduce any new risk.

## The real risk? Employee & company culture.

Even though I believe that most of the negative security reactions to Apple Intelligence are unfounded, this doesn't mean a company has nothing to worry about and can just let employees go wild.

The bigger risk is around employee and company culture in this near future where AI assistance is personalized, ubiquitous, and "helps" people so seamlessly and smoothly that they hardly even notice it.

Over time, more and more writing output and work product will be generated by AI and not the human employee. Keep in mind that with Apple Intelligence, we're talking about iPhones, iPads, and Macs, and it has access to apps, screens, and data. Furthermore, Apple's stated goal is that their Intelligence will get to know the user and their work style, and the current chat-based "type—wait—response" loop will be a thing of the past, (due to both the ubiquity of the integration, and the instantaneous response of an on-device model).

Even for people who think, "I'm not going to succumb to AI for everything," it will be extremely difficult to resist, (or even to know you're resisting). When things are so smoothly integrated, you'll need to exert hundreds of microbursts of willpower every day. (There's a future conversation to have about AI-powered AI integrations as the ultimate dark pattern.)

Even though Apple Intelligence won't be available for months, we can see similar temptations with existing tools such as Microsoft Office Copilot. For example, in Microsoft Word, in addition to the brightly-colored icon in the ribbon, a little in-line Copilot icon literally appears anytime you start a new line. It's right there in your face: Click me. I know you want to be done with this, click me! I can write faster than you, click me!! It's just a status report that no one's going to read, click me!!! Click me!!!! CLICK ME!!!!!

Personally I don't want to use Copilot for an article I write, but I also don't want to disable that feature because I might want to use it for something else in the future, and, frankly, it's interesting to click and see how good it is. (How good is it? While the actual prose it generated sounds nothing like my writing style and is mostly generic platitudes, it also did a pretty decent job of summing up what I'd written until that point.)

In my case I would never want to risk my core product (my writings and perspectives) by attaching mediocre content to my name. But what if this was a lower stakes document—something that I didn't really want to do and "good enough" was good enough? Sure, maybe I'll click the generate button "just to see how good it is" at first. Eventually I'll start seeing points that I like, and as I get more comfortable with AI and the models get better, I'll start the slow-then-fast slide into more and more of my work output being generated by AI.

Now scale this to most employees at a company and the negative consequences are staggering:

- Employees start to rely too heavily on generative AI, leading to a lack of original thought and creativity.
- Erosion of critical-thinking skills from consistently accepting AI-generated content.
- Quality of content diminishes because AI is "so good" that employees stop closely reviewing it.
- All work product becomes more generic. The best employees become mediocre.
- Employees "phone it in" for most tasks. (Hey that's funnier now with GenAI on an iPhone.)
- This creates a self-fulfilling doom loop. (More employees using GenAI for more tasks leads to more employees using GenAI for more tasks.)
- Massive increase in productivity theater. More text is created because it's easier to create, meaning people need to rely on more AI to summarize the text.
- Eventually all original human thought is passed through an AI expander / compressor loop.
- Why are we even doing any of this?

The ultimate kicker for most of the above issues is how would the company even know? I'm not talking about the (now quaint) "consumerization of IT" angle where employees are using AI without the company knowing, rather, I'm talking about the bigger existential issue of how will the company even know that this slow decline in employee and work quality is happening? This evolution will be slow (at first) and extremely difficult to quantify, track, and manage. (Sidebar: It's already starting to happen.)

There's a lot to unpack even in those few quick bullets I just cranked out off the top of my head, not to mention all the other surrounding issues. (Helping our customers understand and address this is what my larger mission at ILKI is about, and what I'm focusing most of my time on these days. It's super interesting and complicated!)

Of course this is much bigger than Apple Intelligence. But more AI tool integration, more personalization, and increased speed all lower the barriers to use. Multiplying this by all the employees in a company is a slippery slope, and we need to get serious about how we're going to address this ASAP.

*The text of this article is AI Influence Level 0: Human conceived & created with no AI assistance. (The hero image is AIL4.)*
