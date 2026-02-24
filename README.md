# brianmadden.ai

brianmadden.ai is my published thinking on AI and the future of knowledge work, packaged so any AI assistant can load it and reason with my perspective. Connect it to your AI, and it can draw on my frameworks, arguments, and current thinking during your normal conversations.

I recently wrote about building a [personal AI knowledge system](https://www.linkedin.com/pulse/i-built-second-brain-using-ai-its-changed-way-work-future-madden-0tote/) and about why I think [experts should publish structured knowledge modules](https://www.linkedin.com/pulse/hey-creators-stop-publishing-content-start-your-second-brian-madden-ca0ae) that people can plug into their own AI. brianmadden.ai is that idea, applied to my own work.

It's made of two things:

* All my published content: [Citrix blog posts](https://www.citrix.com/blogs/?s=bmadden&type=author), LinkedIn articles and posts, speech and podcast transcripts, interview transcripts, and my standalone frameworks & big ideas.
* Files that tell any AI how everything connects. Which ideas are authoritative versus still developing. How a new blog post extends or challenges an earlier argument. What I'm currently thinking about topics I've already written about publicly. A knowledge hierarchy that tells the AI what to prioritize and where to be careful.

That second part is what makes this a knowledge *system* rather than a content dump. When I publish a new article and it connects to something I wrote six months ago, that connection gets captured. So it's not just "here's another article," it's "here's how this changes the picture." Instead of searching my content, your AI gets a map to the architecture of my thinking.

On its own, brianmadden.ai is just text files. It only becomes useful when someone points their own AI at it—Claude, ChatGPT, Copilot, Gemini, whatever you already use. Your AI handles the conversation and applies its own safety guardrails. brianmadden.ai provides the source material. It's very similar to a web server in that regard, serving structured knowledge to AIs rather than web pages to humans.

So this is not a chatbot. A chatbot is frozen in time. This updates as my thinking evolves, sometimes several times a day. And it's not a digital twin—it doesn't simulate me or pretend to be me. It's a living reference library that your AI loads and draws from during your normal conversations.

## Why this exists

Once I started using my personal AI knowledge system, I wanted to add in perspectives from certain coworkers and experts I respect. While hunting down YouTube transcripts and blogs to paste in, I thought, "this would be so much easier if everyone just published their knowledge as modules I could plug in!"

So I decided to do that with my own knowledge and thinking, which is what this repo is.
## How do you use it? Connect your AI.

brianmadden.ai has a custom MCP server. Add this as a connector in your AI tool's settings:

```
brianmadden.ai/mcp
```

That's it! Your AI can now draw from my full body of work during normal conversations. There's no app to install, no account to create, and no subscription to manage. (As a future concept, these types of things could be subscription based, but mine is free.)

The brianmadden.ai MCP server draws from all the content in this repo. So you can browse it here if you want to see what's inside. The MCP server is always up to do, so whenever anything new is added or changed, that's also reflected via MCP.

Step-by-step instructions for different tools (Claude, ChatGPT, Copilot, Cursor, and others) are at [brianmadden.ai/connect](https://brianmadden.ai/connect).

Once you're connected, try things like:
- "Apply Brian's invisible 80% framework to [your company/industry]"
- "What would Brian Madden think about [your AI strategy question]?"
- "What's Brian's current thinking on [enterprise AI, workspace governance, personal AI systems]?"
- "I'm preparing a presentation on the future of work. What's the most counterintuitive argument I should build around?"

## What's inside

- All my published blog posts, Linkedin articles & posts, speech transcripts, podcast transcripts, and interviews from the past several years
- A 30,000-word synthesis distilling the intellectual foundation across all published work
- A "current thinking" file that captures where my head is right now—updated frequently
- AI loading instructions, knowledge hierarchy, and engagement rules
- A published [governance document](GOVERNANCE.md) that defines what goes in, what stays out, and how the publishing process works

Everything in brianmadden.ai is already public. The module adds structure and AI accessibility, not new content.

## About me

I'm Brian Madden, a technology officer and futurist at Citrix. I have 32 years in end-user computing and digital workplace. I've written 6 books, 2,000+ articles, and given over 1,000 talks globally. Originally from Ohio (Go Browns!), I now live inParis. 🇫🇷

I explore how AI is reshaping knowledge work. My core thesis: the real AI transformation is happening worker-by-worker, not top-down. The invisible 80% of knowledge work—the judgment, reasoning, and tacit expertise that lives in workers' heads—is where the action is. Enterprise AI automates the scaffolding. A second brain amplifies the cognition.

- More details about this repo and how to use it: [brianmadden.ai](https://brianmadden.ai) 
- Follow me on [LinkedIn](https://www.linkedin.com/in/bmadden/)
- I write about these topics at [Citrix blog](https://www.citrix.com/blogs/?s=bmadden&type=author)
- My personal website: [bmad.com](https://bmad.com)

## License

The ideas are mine. The content is public. Use brianmadden.ai to inform your thinking, apply my frameworks, and build on my work. Attribution appreciated but not required for personal use. If you're publishing or redistributing, credit the source.
