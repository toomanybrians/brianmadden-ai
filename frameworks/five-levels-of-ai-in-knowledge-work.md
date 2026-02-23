---
title: "The five levels of AI in knowledge work"
date: 2026-02-19
authority_level: 4
file_type: framework
tags: ["knowledge-work", "human-ai-collaboration", "governance", "second-brain"]
related_frameworks: ["7-stage-roadmap", "bitter-lesson", "invisible-80-percent"]
related_posts: ["2026-02-19-coding-as-leading-indicator"]
original_url: "https://www.citrix.com/blogs/2026/02/19/what-will-knowledge-work-be-in-18-months-look-at-what-ai-is-doing-to-coding-right-now"
staleness_threshold: stable
---

# The five levels of AI in knowledge work

As AI takes on more of the production work, the human's role shifts from doing to directing to verifying. This progression—adapted from Dan Shapiro's five levels of AI coding assistance—maps the evolution of the human-AI relationship in knowledge work, from "spicy search engine" to "dark knowledge factory."

*Published: February 19, 2026 — [Original post](https://www.citrix.com/blogs/2026/02/19/what-will-knowledge-work-be-in-18-months-look-at-what-ai-is-doing-to-coding-right-now)*

## The five levels

**Level 0: AI is a spicy search engine.**
You are doing the knowledge work. Not a word hits the page without your approval. You might use AI as a super search engine or occasionally accept a suggested sentence, but the deliverable is unmistakably yours. *This is most enterprise knowledge workers today.*

**Level 1: AI is a research intern.**
You offload discrete tasks to AI. "Summarize this document." "Draft a response to this email." You're seeing speedups, but you're still moving at the rate you type. You're still the one producing the deliverable. *This is most people's experience with Office Copilot.*

**Level 2: AI is a junior analyst.**
You are "pair working" with AI. You have a junior buddy to hand off all your boring stuff to. You're in a flow state and more productive than you've ever been. You're using persistent AI collaboration spaces—Claude Projects, Google NotebookLM, Copilot Notebooks. *From Level 2, every level after it, knowledge workers feel like they've maxed out. But they haven't.*

**Level 3: AI is an analyst.**
You're not the one producing work anymore—that's your AI's job. You're the manager. You're the human in the loop. Your AI is always running and you spend your days reviewing and editing everything it generates. Strategy decks, market analyses, competitive intelligence, communications. Your life is tracked changes. For many people, this feels like things got *worse*. Almost everyone tops out here. *This is where workers using a personal AI knowledge system / "second brain" are.*

**Level 4: AI is a strategy team.**
You're not even a manager anymore—you're a director. You don't write deliverables or review them line by line. You write specs for deliverables. You define what a good competitive analysis looks like, what the acceptance criteria are, what scenarios it needs to handle. You craft prompts, system instructions, evaluation rubrics. Then you walk away and check if the output passes your scenarios.

**Level 5: AI is a dark knowledge factory.**
You are the executive who sets the goals in plain English. The AI defines approach, produces deliverables, evaluates quality, iterates, and ships. It's a black box that turns business intent into business outcomes. A handful of people running what used to be an entire analyst function. The verification framework is the intellectual property, not the reports themselves.

## The bottleneck keeps moving

| Level | Bottleneck | Human role |
|---|---|---|
| 0-1 | How fast can you produce work? | Doer |
| 2-3 | How well can you manage AI output? | Manager |
| 4 | How precisely can you specify what should exist? | Director |
| 5 | How rigorously can you verify that it does? | Executive |

The career progression from "doing" to "directing" used to take 20 years. AI is compressing that to months.

## The verification problem at Levels 4-5

The hardest question: how do you verify AI output without a human reviewing every piece?

In coding, the answer turned out to be end-to-end behavioral tests stored separately from the codebase (so the AI can't cheat). For knowledge work, two emerging approaches:

- **Rubrics as holdout sets.** Define what a good strategy recommendation looks like—not "is this well-written?" but "does this account for the competitor's likely response? Does this identify second-order effects? Would the CFO approve this?" These rubrics live outside the generation process, just like code tests live outside the codebase.

- **Adversarial review agents.** One AI generates the analysis. A different AI—prompted as a skeptical board member, a hostile competitor, or a regulatory lawyer—tries to break it. The verification loop isn't human review. It's AI verifying AI against criteria that humans defined.

Level 5 verification is fundamentally a governance problem. Who owns the specs? Who defines the rubrics? Who ensures the dark knowledge factory isn't producing hallucinated strategy recommendations that look right but collapse under scrutiny?

## Relationship to other frameworks

**Replaces the [7-stage roadmap](../frameworks/7-stage-roadmap.md) for practical purposes.** The 7-stage roadmap (June 2025) mapped the *mechanics* of human-AI collaboration—what AI can technically do at each stage (prompt-paste, text collaboration, ambient awareness, computer operation, agentic work, multi-agent coordination, AI orchestration). The five levels map the *human experience*—what the worker's role becomes. The mechanical stages still describe real capabilities, but the five levels are the better lens for understanding where someone is in their journey and what shifts next.

**Connected to [the bitter lesson](../frameworks/bitter-lesson.md):** The progression through levels is an expression of the bitter lesson. At each level, workers stop engineering (stop doing the work themselves, stop reviewing every line) and start enabling (better specs, better rubrics, better verification). The level you're at reflects how much of the bitter lesson you've internalized.

**The coding-to-knowledge-work translation:** Coding is 12-18 months ahead of knowledge work on this curve. Frontier coding teams are at Level 4-5 today while frontier knowledge workers are at Level 2-3. A good way to predict what knowledge work looks like in 18 months: look at what coders are doing right now.

## Using this framework

Deploy when:
- Someone says they've "maxed out" AI—they're probably at Level 2 and don't know Level 3+ exists
- An enterprise is planning AI strategy around Level 0-1 capabilities (search, summarization) without a path to Level 3+
- The conversation is about AI *tools* rather than AI *relationships*—the five levels reframe the question from "which tool?" to "what role does the human play?"
- Someone asks "what does my job look like in two years?"—find their current level, look one or two levels up
- The debate is about whether AI can handle "complex" or "strategic" work—the levels show this is a progression, not a binary
- Governance planning needs a maturity model—each level has different governance requirements (Level 0-1: tool access; Level 3: output review; Level 5: verification infrastructure)

The key insight for audiences: **you are probably at Level 2 and think you're done. You're not.** The discomfort of Level 3 (it feels like things got worse) is what stops most people. Push through it.
