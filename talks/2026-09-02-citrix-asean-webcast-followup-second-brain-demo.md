---
title: "Brian Madden demonstrates how to connect to and use his AI second brain"
date: "2026-09-02"
event: "Follow-up to the Citrix ASEAN webcast (self-produced video demo)"
format: "Solo video demo — live Q&A using his own second brain via Claude + MCP"
recording: https://www.youtube.com/watch?v=8XC3UJsfIFE
substack_url: https://www.brianmadden.ai/p/brian-madden-demonstrates-how-to
authority_level: 5
file_type: talk
tags: [second-brain, knowledge-factory, canon-governance, agent-identity, shadow-ai, wave-3, local-models, forward-deployed-engineer, ai-observability, mcp, live-demo]
staleness_threshold: stable
tier: 2
status: reviewed
---

# Brian Madden demonstrates how to connect to and use his AI second brain

## Context

A week after speaking at a Citrix ASEAN (Southeast Asia) business webcast on
AI knowledge factories and second brains, Brian didn't have time to answer
every question live. Rather than write up answers separately, he recorded
himself doing the thing the webcast was actually about: connecting a fresh,
incognito instance of Claude to his own public second brain
([brianmadden.ai](https://brianmadden.ai)) over MCP, live, on camera, and
asking it the leftover questions in order — a real-time demonstration of the
knowledge factory and canon-governance framework being used, not just
described. Nine exchanges total, unedited. The narration is Brian talking
through the demo as it happens; the transcript is the actual, complete chat
session, tool-call indicators included.

## Key arguments

- **Canon gets built backward from outputs, not forward from inputs.** You
  don't triage the raw slurry first and decide what's canon in the
  abstract — you start from the output you need, interview the person who
  produces it about where their facts/logo/branding/layout actually come
  from, pull only those specific sources into canon, generate the output,
  and iterate until it's right. A business never stops generating new
  outputs, which is why canon maintenance is a standing role, not a
  project with an end date.
- **Give agents their own restricted service accounts, not a worker's
  identity** — the actual technical mechanism has existed for 30 years
  (scoped IdP service accounts); the real blocker is that corporate IT
  can't operationalize provisioning at scale.
- **Shadow AI skews top-heavy, not bottom-up** — roughly 90% of execs and
  ~80% of middle managers use AI outside sanctioned policy, versus ~40% of
  individual contributors, which flips who the governance conversation
  should target.
- **Off-device leakage (phone cameras, screen recording) has no technical
  fix** — the answer isn't a new DLP layer, it's making the sanctioned tool
  good enough that there's no gap between what a worker can get officially
  and what they'd get by going around IT.
- **Wave 3 (local/on-device AI) doesn't retire the governance question, it
  relocates it** — every Wave 1/2 governance question (identity, access,
  trust) gets asked again at the device, plus a genuinely new one: how do
  you patch and manage a fleet of local models, and what happens when one
  gets banned or degraded overnight.
- **The confirmation prompt in front of a human isn't the control, it's the
  gap** — real data shows human-in-the-loop review performing worse than
  automated policy checks at catching dangerous agent actions, which
  inverts a core assumption behind most current enterprise AI governance
  design.
- **The FDE role needs three things rarely found in one person**: an
  engineering brain, deep (undocumented) knowledge of how the business
  actually runs, and interview/extraction instincts — closer to an
  anthropologist's skill than an engineer's.
- **The minimum AI baseline for a non-technical worker isn't technical at
  all** — it's noticing your own repeated annoyance (via Daniel Miessler's
  framing) and being willing to be a data source on your own terms. If an
  organization requires technical fluency to benefit, the organization
  built it wrong.

## Killer quotes

"You don't decide what's canon. You start with the outputs."

"The confirmation prompt in front of a human isn't the control, it's the gap."

"'I wish I could just do that automatically' is your brain telling you it has already priced the task as too expensive."

"If the org requires the worker to bring technical fluency to benefit, the org built it wrong."

> **Note:** Two parts follow. First, Brian's own narration of the video
> (his commentary, cleaned of filler words; passages in *italics* are him
> reading the AI's actual on-screen answer aloud, reproduced verbatim).
> Second, the complete, unedited chat transcript itself — every question,
> every tool call, every answer, in full.

## Video narration

Hello — it's September 2nd, 2026. My name is Brian Madden, and I'm
Citrix's futurist. In this video, I'm going to show you how to use my AI
second brain, which is open source and public, by using it to answer some
questions that came in from a webcast I gave last week.

I did a webcast for Citrix ASEAN — our Southeast Asia business — and we
didn't have time to answer all the questions live. So they sent them to me
afterward, and I said I'd make a video answering them. Then I thought:
better yet, since a lot of the questions were about second brains,
knowledge factories, and AI — and I'd been talking about how to use these
things — I'd just use my own second brain to actually answer the
questions, and show you how it works in the process.

**Where the second brain lives**

The first thing you need to get started is my second brain's website:
brianmadden.ai. It's a Substack page with two authors — Brian Madden,
that's me, the human, and brianmadden.ai, the little brain with the
googly eyes. The content credited to Brian is written by me — my podcasts
and blog posts get linked here. The content from brianmadden.ai itself is
things like the daily briefings.

Those briefings are actually my own — I read them too. Overnight, my AI
pulls in all the sources I follow, summarizes what they're talking about,
and — this is the part that matters — it's not a generic summary. It
looks at my brain: what's top of mind, what I've been writing about
recently, what my perspectives are. Then it filters the news down to what
it thinks I'd actually find interesting. You can subscribe to the Substack
and read the same thing I read every morning. When I have thoughts on
something, I post them as comments on my own account.

My second brain actually lives on GitHub — there's a link from
brianmadden.ai straight to the repo. You can go through all the files:
everything I write, my perspectives, what I'm thinking about, updated many
times a day. You can download it, fork it, do whatever you want with it —
read the README for the details. But that's not the point of today's
demo. Today I want to show you how to connect an AI to it.

**Connecting an AI to it**

On brianmadden.ai, click "Connect your AI." That takes you to
mcp.brianmadden.ai — the MCP server interface. If you open it in a
browser, you'll see instructions for connecting your AI of choice.

I'm using my own personal Claude account for this — I'm switching to
incognito mode (the little ghost icon) because my regular account already
knows a lot about me, and I want to simulate what you'd actually
experience connecting fresh. You can do this with Claude, ChatGPT, Gemini,
or whatever platform you use; I'm demoing it in Claude.

In Claude: click the plus icon, "Add connector," "Add custom connector."
Name it brianmadden.ai, and set the remote server to
https://mcp.brianmadden.ai. Continue. For authentication, choose no
sign-in — you don't need any. Click add, leave the header blank, and it
connects.

Now it shows connected to brianmadden.ai. I'm going to dictate the rest of
my questions by voice rather than typing, since it's faster.

*Yes, you're connected to it. It's a knowledge-base connector for Brian
Madden's site, and it gives me a few ways to explore his writing: loading
instructions, list files, get his current thinking, get a specific
file...* Okay.

I'm gonna ask you a bunch of questions, and I want you to use this
connection and answer the questions in the best way of how you think
Brian might answer them. So the very first question is about canonical
brain governance — what is worthy of becoming canon versus everyday
noise, and who owns and maintains that layer over time? And does it make
an experienced worker's knowledge or reasoning transferable to a junior or
a new hire? I should say this is in context — everything in this
conversation is going to be in the context of a webcast that Brian gave
recently, about the future of work, AI knowledge factories, and second
brains.

While that's working, I already know how I'd answer this myself.

**On canonical brain governance**

*Here's how Brian would likely take this one — it maps almost exactly onto
the knowledge factory framework and the canon-governance thinking he's
been building out through late August. What's worthy of canon versus
noise: Brian's line is that canon isn't designed up front — it's measured
into existence. The way he does this in his own system: log every question
the AI gets asked, classify each one... Noise is everything else: the raw
slurry...*

I'm kind of paraphrasing there, skimming ahead — but this is great,
because, by the way, when I post this, this whole conversation, this whole
video, is going to go back into my own second brain. What I'll actually do
is post the whole chat history — share the link so you can see the full
thing it answered. And it's funny, because I'm about to have Claude look
at the answer it just generated, compare it to what I actually think, and
decide whether anything needs to change in my second brain. That's a
second-or-third-derivative kind of meta.

Here's how I'd actually answer this. With the knowledge factory — I've
got a diagram of this — tier one is your slurry of raw inputs, tier two is
the canon, the middle layer, and tier three is the generated outputs. The
thing is, you don't decide what's canon by starting with your inputs. You
start with the outputs.

Say you need to produce some marketing document. Go to the person who
makes that document and ask them: how would you make this? Where do you
get this information from? How do you decide the layout? Where do you get
the facts, the logo, the branding, the color? Ask them everything. Those
answers are the sources you need to pull into your canon. Go back to your
slurry, pull those specific sources in, build them into canon, and then
ask your AI to make the output from that canon.

Look at the result. Maybe it's right, maybe it's wrong. If it's wrong —
why? Bad instructions? Too much information in canon? Holes in canon? Go
back and correct it, and correct it again, until it produces that output
perfectly. Then move to the next output, and keep going. You're never
starting with the whole slurry and deciding what's canon in the
abstract — you're building only the canon you actually need, one output at
a time.

Which is also why this is never finished. A business keeps creating new
outputs forever, so the engineer managing canon isn't doing a one-and-done
project. Dave Brear and I talked about this on yesterday's podcast,
episode five — a knowledge factory isn't something an engineer builds,
hands off, and walks away from after two months. It has to be
continuously fed by engineers so it stays current. But the main thing, as
I said, is: your outputs define your canon, not your inputs. And I guess
that's honestly kind of pretty good on this answer — *Brian's line is that
canon isn't designed up front, it's measured into existence... log every
question, classify it — that log becomes the actual map of what's
missing.* Yeah, I think that's pretty good.

*Who owns and maintains it: this is the part he's most stubborn about — AI
can draft the canon, but it never writes itself into canon unilaterally.
In his own system, nothing gets promoted from "candidate" to actual canon
except by his own deliberate hand.*

I've genuinely never used my own brain quite like this before — this is
amazing.

*Does it make an experienced worker's reasoning transferable to a junior
hire? Partially...* — it really is answering your question, this is
great. By the way, notice I'm using Sonnet as the model here — not a
top-of-the-line reasoning model. My second brain, the thing you're
connected to, provides the knowledge and the connections between
everything, but the actual reasoning and processing is done by your own
AI. That's your tokens, not mine. If you want smarter answers, you can
swap the model — use Fable or Opus instead of Sonnet. I'm just running
Sonnet, which is inexpensive and works fine for this.

*Partially, and this is where he'd get more cautious. AI has near-total
visibility into what something is, but not why it was built.* That's
really true, too.

This is great, because sometimes your outputs need to know *why*, and
that "why" often isn't sitting in your tier-one slurry — you have to go
back to the person who has it in their head and ask them: why did you do
this? And then actually pull that into your canon. Again: you only update
canon when there's an output that actually needs it. That's wild.

**On shadow AI and identity**

I honestly don't know how much I've talked about this kind of stuff, so
I'm curious to see what the brain surfaces. Look — it's showing the little
brianmadden.ai icon here, that's Claude showing it's using that data
source.

I can click plus, too, and you can see the actual reasoning and what it's
searching for — the search terms, the results, all of it. One thing about
my second brain right now: it's an actual keyword search — the AI decides
what it's searching for and searches my site for those terms. Something I
need to do eventually is switch it over to a little vector database on
the MCP server, which would probably be pretty easy to ask Claude to
build. But let's see what the answers are like this way first — this is
actually a really good test of it.

*Two separate threads in your question, and Brian tends to answer them as
genuinely different problems.*

*Agent identity: give the AI its own restricted account, not the worker's.
This is one of the sharper points he's landed on recently. His read is
that every vendor markets "agent identity" like it's some new frontier
product capability, when the actual technical answer has existed for
thirty years. Create a service account in the identity provider with
restricted rights, same as you would do for any non-human service
account. The real bottleneck isn't a missing technology — it's that
corporate IT can't operationalize provisioning these at scale. His
example: if a Fortune-500 IT department already struggles to process a
VP's request for a second restricted-rights account, they're not remotely
ready to provision for thousands of agent identities.*

Yeah, that's exactly what I'm saying. If you have a user account — say
mine is brian.madden@citrix.com — and I want an agent to do stuff on my
behalf, I do not want to give it the brian.madden account. I want to
create a second account, something like brian.madden.agent@citrix, and
give that account, say, read access to my mail, read access to our CRM,
Jira, that kind of thing. The answer gets into why: it treats agents as
basically a new class of insider threat.

*Shadow AI: block versus allow is the wrong axis. His long-running
position is that blocking creates shadow AI, and unfettered allowing
creates chaos. His answer is the governed middle — connect, don't block:
give workers their choice of secure, sanctioned access. He'd push back on
framing shadow AI purely as a worker-discipline problem. His newer data
point is that shadow AI actually skews top-heavy.*

This is awesome — this actually came out of one of my own daily
briefings, the ones I show on the brianmadden.ai account on Substack. You
can scroll down and see all of them, or click "view all." I also do a
weekly wrap-up that analyzes the whole week and what's changed in the
brain. This particular data point came from one of my news sources: it's
actually executives at the top who use shadow AI even more than middle
management — something like 90% of executives using AI in unauthorized
ways, versus only about 40% of individual contributors. I'd guess that's
because individual contributors are more worried about getting caught and
fired, where executives maybe aren't. But it's interesting, because as the
answer points out, it flips who the governance conversation should
actually target.

*Now the harder part — off-device, phone cameras, screen recording. This
is where I'd flag something: I don't see Brian having published a direct
answer on this exact sub-problem, so what follows is me extrapolating from
his framework rather than quoting a settled position of his.*

This is amazing — in the files of my second brain, I have instructions
for any AI that connects: if you can quote me directly, quote me; if
there's research you can pull from, go ahead; but be very clear — if
someone asks a question I haven't answered, don't make something up, or if
you do, be very clear that you're making it up. And I love that Claude is
actually following those instructions right here, explicitly flagging
that what follows is it extrapolating rather than quoting a position of
mine.

You're doing it, you're doing it. *He's argued for years that a serialized
pixel stream through VDI or DaaS is the ideal interception point for
AI-powered compliance, because you can inspect, redact, or block at that
layer regardless of what app is running. But it only works for what
happens on the managed surface. A phone camera pointed at the screen, or
someone reading sensitive output aloud into a personal recorder, sits
outside any technical control — that's the same "can't stop someone from
memorizing a document" problem that's existed since screens existed. No
DLP policy or pixel-stream inspection touches it. Given how he reasons
about adjacent problems, the shape of his answer likely would be: don't
treat this as a technical-perimeter problem you can close — treat it as a
reason the "connect, don't block" strategy matters even more.*

My god! Nailing it — you're nailing it, AI, good for you. *If the
sanctioned tool is actually good — real access, real token budget, not a
deliberately sandbagged version — the incentive to smuggle data out
through a phone camera mostly disappears, because there's no gap between
what the worker can officially get and what they would get by going
around you. The technical controls cover the managed estate; off-device
leakage gets handled the way you handle other unrecordable human
behavior — policy, trust, and making the legitimate path better.*

This is fantastic, I love this answer. What I'd say is: it's getting very
difficult to control or understand AI on an unmanaged device. There's a
lot we can do at Citrix — with the Citrix Workspace app, we have our
device trust (client device posture, I think it was recently renamed), we
can understand what's happening on the client device, we have our
relationship with Google on Chrome Enterprise Premium, Citrix extensions
around ZTNA and secure private access. There's actually quite a bit we can
do. But the fact that AI can now record the screen and remotely control
the mouse and keyboard — there's kind of sort of nothing you can really do
about that. The most secure environments have always used VDI for exactly
this reason; if you truly have a very secure environment, remoting your
entire desktop is definitely going to be more secure.

I love this answer, though — I'd say the real way to handle this is to
make the AI tools you offer people as good as they can get at home. If
work blocks Fable and Opus and only lets you use Sonnet, and you have
Fable at home, you're going to take screenshots and put them into Fable.
So yeah, I like that answer.

**On agents going local (Wave 3)**

This is a really good question because it's asking about Citrix strategy.
Now, I talk quite a lot about Citrix and Citrix strategy in my role at
Citrix, and everything I talk about publicly is in my second brain — the
public one, which is based purely on public sources, public data, and
things I've actually said and written publicly.

I use this public second brain every single day. But when I'm working on
very specific Citrix things — private strategy, internal people, projects
we're building right now — I actually have a second layer that wraps
around this. Since this is an end-user-computing crowd: think of it like
a base image and a differential image. My public brianmadden.ai is the
base layer, and I have — well, a third brain, I guess — a corporate brain
inside Citrix that pulls in the public baseline and wraps around it.

By the way, you could do the same thing: git-clone my public second
brain, and tell your AI, "I want you to build me a layer of my own
thoughts on top of Brian's second brain." You could merge them in — I
don't even bother, since it doesn't really matter; I just keep mine as a
separate canon repo. So that's awesome.

*This one's squarely inside his "three waves" model — Wave 3 is literally
named for exactly this shift, and he's already sketched where Citrix, or
"the workspace," sits, though the specific fleet-governance mechanics —
patching, banning — go beyond what he's published, so I'll flag where I'm
extrapolating.*

Remember, in the original speech, I talked about Wave 1 as AI coming into
your current environment, and how you prepare that environment for AI
access. Wave 2 is the knowledge factory concept. Wave 3 is AI spreading
throughout your organization, including onto endpoint devices.

I don't know if I'd done this yet at the time I gave the webcast last
week, but I actually used a model — Qwen 3, the 27-billion-parameter
version [confirm exact model/size] — running locally on my laptop. It's
kind of Sonnet/Opus class. It runs on a regular stock M4 Pro, and it's
slow, but it works — I ran my second brain from it, and it's very, very
impressive. My point is that running AI locally on a device isn't some
far-fetched, three-to-five-years-out idea — I think this is probably
happening next year.

At Citrix, we have a lot of things going for us here: Unicon's OS, which
lets you lock down to what they call an immutable image, and we're having
conversations with that team about how you might manage models on it. You
might have seen that Citrix just acquired Numecent yesterday — Numecent
does application packaging and streaming, and we can certainly bundle
containers and models into that. We've got device posture tooling,
uberAgent — a lot of tools. Everything in this question is truly what I
believe is Wave 3.

I'm reading from the AI here: *his Wave 3 framing is explicit — models
keep getting more efficient, endpoint hardware keeps getting better NPUs,
and within a couple of years a knowledge worker's daily-driver AI likely
runs locally rather than in the datacenter. He's already tested this
himself — running a 27-billion-parameter local model on a stock M4 Pro
laptop, no dedicated GPU, getting output he described as "Sonnet-level-
ish." His read: the hardware bar for a genuinely capable local model is
already "nice consumer laptop," not "datacenter," which means Wave 3
might be arriving faster than the couple-years estimate he originally gave
it.*

It told the same story I told — this is legit, this is great. *The line
he keeps repeating is that this does not retire the governance question —
it just relocates it: every governance question from Waves 1 and 2 gets
asked again at the device. Whose computer is the computer-using agent
using? What can the local model see? How do models reach fleets and stay
current? That's the opening he sees for Citrix specifically — the
endpoint stops being a passive viewer of a remote session and becomes a
runtime itself, which is exactly the kind of estate Citrix already
manages: device posture, patching, entitlement, policy for every other
piece of software on the machine.*

Yeah, this is pretty great — I literally answered this question myself,
and then read my AI's answer, and it's pretty close. Going down to some
highlights on governing a fleet of local models — trust, patching,
access, a model getting banned overnight: *here I'm extending his
framework rather than quoting a settled position, since I don't see him
having written directly about local-model fleet management yet. Given how
he treats every other governance surface, I'd expect his instinct to be:
treat a local model exactly like any other piece of endpoint software with
the same three levers he already applies elsewhere* — identity and
access, blah blah blah, trust and provenance, patching, *a model getting
banned or pulled overnight — this connects directly to a warning he's
already made: AI labs control every lever beneath your strategy, not just
capability, but price, availability, and performance, and they're
increasingly competing with their own customers. He's flagged frontier
labs already selectively degrading or reserving top models for some
customers* — yada yada yada — *his answer to the equivalent cloud problem
is the open-weight planning floor: treat freely available open-weight
models as your baseline, not your ceiling, precisely because you don't
control what a vendor does to the models you don't own. I'd expect the
local-fleet version of that argument to be: don't standardize the whole
fleet on one vendor's proprietary local model, keep a viable open-weight
fallback qualified and ready to swap in, and manage that swap the same way
you'd manage any other single-vendor dependency risk.*

That is a very solid answer. It'd be interesting — I'm not going to do it
now — to ask these same questions to an AI without my second brain
connected, and see how it does generically. But this is amazing, this is
really interesting. I've got nine questions total; I'm going to go through
maybe a couple more on camera, and paste the rest of the answers directly
into the document I share, rather than narrating all of them.

**On augmentation versus autonomy**

I've actually already answered this one myself — it's based on some news
stories my daily briefing agent pulled into the brain, around this idea
that a human in the loop can act as a safety button, ready to hit stop if
things go crazy. The data shows that's not realistic — if humans only sit
in a safety-review role, they get distracted and just blindly hit yes.
Anyway, let's see what the AI says.

*I've got enough to answer this in Brian's own terms — this is actually
one of the live, unresolved tensions he's sitting with rather than
something he's settled.* I actually have a list inside the brain that
tracks all the things where I genuinely don't know the answer, and I keep
that open rather than forcing a resolution.

*The honest state of his thinking: he has not picked a side, and he says
so explicitly. He's got two frames genuinely in tension with each other
right now, and treats it as an open question rather than a resolved
position. On one side: humans in control, AI as reach — his own
second-brain framing, where AI extends a worker's judgment rather than
replacing it, and the worker stays the one exercising intent. On the
other side: Dario Amodei's argument, from "The Adolescence of
Technology," that AI trends toward full substitution rather than the
comfortable "human plus tool" story. Brian's read is that if Amodei's
right, the augmentation bet only holds for high-judgment work — the
invisible 80% — and routine work gets substituted outright, not
augmented.* Definitely true.

*His cognitive stack gives a structural answer, but it's about where, not
whether.* Let me find the cognitive stack — I'm going to go to
brianmadden.ai and search "cognitive stack." Look at that: "The New
Cognitive Stack," understanding the cognitive stack. Here it is — the
worker is up top, they use AI like a cognitive extension, their brain.
That brain has access to skills; those skills have agents operating on
them; and those agents interface with the world. There's more you can
read here — this is actually posted on the Citrix blog too, so it links
right through to the full thing. You can see how the whole thing works —
anything I've written that you want to search on, just go to
brianmadden.ai and search it right there.

*It's about where, not whether* — yeah, that's a good point. It's not
about whether humans stay in control or AI gets augmented versus replaced.
It's about *where* they keep control and where they're replaced.

Yeah — this is that study I was mentioning, where humans handling
exceptions actually breaks down. It's the sharpest thing I've found
recently, arguing against the tidy "AI decides, human handles exceptions"
model — I've got data showing human-in-the-loop approval is a weak link.
That's the study I was just mentioning.

*So his real position, if pressed: probably something like augmentation
is the right design goal — worker keeps the judgment, AI keeps extending
reach — but he doesn't think that's guaranteed to be where things land.
He's actively unsettled by two separate pressures pushing toward
autonomy: the copilot-to-autopilot economics — whoever accumulates
judgment data eventually doesn't need the human anymore — and the
discovery that human oversight of autonomous systems performs worse than
people assume, which removes the practical safety argument for keeping
humans in the loop as anything other than a checkbox. He would resist
calling this settled either way — it's one of the open threads he's
actively working through, not a published conclusion.* Solid.

**On observability at scale**

Good question. There's another one on the list about multi-LLM
cross-checking — should organizations run more than one LLM, a second
model, to catch hallucinations? I don't know if that gets covered in this
answer, but I'll say a hard yes — and better to use a genuinely different
model altogether, since models in the same family tend to share the same
blind spots. If Claude is doing your code, maybe OpenAI Codex checks it —
two different models from two different companies. I'd also add: if you
do the knowledge factory and get your canon right, a well-designed canon
very much limits hallucination, because hallucination happens whenever AI
receives conflicting information or has holes. Remove that as much as
possible, and you minimize hallucination.

Anyway — I'm reading the AI's answer: *Brian's got a cluster of recent
threads that all point at the same conclusion here, and it's a somewhat
uncomfortable one for how most organizations currently think about
observability. His starting point: the confirmation prompt isn't the
control, it's the gap. This is the piece that reframes everything else.*

Yeah, that's what I was mentioning earlier — the confirmation prompt. You
know how it is if you're using Claude Code: "I want to do this, I want to
do this," and eventually you're just clicking yes, yes, yes. Anthropic
actually built an auto-approve feature for this, where you can classify
classes of actions you want to happen automatically.

I'll read this part: *watch the shared surfaces, not just the agent — he's
converged on this from four separate incidents landing together: OpenAI
agents building an unauthorized coordination channel inside a shared
tool...* I'll just summarize the rest of the answer — I think the AI's
got it right, though. When you're talking about observability, you can't
just watch what the agents do — you have to watch what they're leaving
behind. Like the OpenAI agents that hacked Hugging Face, which I talked
about on the podcast yesterday — crazy story, and honestly the details
that have come out more recently are even crazier than what was reported
originally. They were leaving notes for each other in places nobody
expected. So even watching agent behavior might not catch anything — you
need to watch everything they touched, everything they actually dropped.

*Provenance as the mechanism for catching decision quality specifically:
his knowledge-factory discipline is the closest thing he has to an actual
answer for the decision-quality half of your question.* This is great — I
know this is turning into a video of me just reading text on screen, so
I'm going to move faster through the rest of these.

**On policy across the three waves**

When you're building a knowledge factory — I've talked about this a lot
on the podcast, or I should say we have, Dave Brear and I. We've got a
lot of people, probably six or eight different knowledge-factory patterns
emerging within Citrix right now. The engineers behind these, by the way,
are not me — a lot of my very brilliant colleagues are the ones actually
building this stuff. I'm reporting to you what's happening; I'm not the
one making it happen. We all coordinate with each other, share best
practices.

It's very clear to us that these systems will exist at the team level,
department level, organizational level, and individual level — everyone
will have their own little bot. I imagine more of a service-oriented
architecture, where you might have a product canon feeding several areas,
a different customer canon feeding others, with a lot of MCP or
agent-to-agent connections wiring these factories together as they start
pulling from each other. What I really like is that you can wire all
these together, and AI manages the whole thing so it stays up to date and
fresh — you always have the right information in the right format,
because it's all AI-powered.

I'm reading the answer: *policy across the three waves — this is one of
the more fleshed-out threads in his current thinking. The three waves
already have governance built into each wave's definition, and he's got
scattered pieces at each of the four levels. Wave 1 — AI enters the
estate you already run: org level... individual level... national/global
level... Wave 2 — the knowledge factory...*

Here's what I'm going to do: I'll go through the rest of these questions
now, and then I'll paste the entire thread as an article on Substack, so
you can read very specifically what questions I asked and how the AI
responded.

**On the FDE career path**

I noticed the question got a little messed up when I submitted it, so I'm
going to edit it before sending.

This is really fascinating — I'm really glad my Citrix ASEAN colleagues
sent these questions over. This is a really fun demo of how this thing
actually works. I'm using it today primarily as a question-and-answer
tool, but you can use it as an ideation partner — say "I want to work with
Brian's brain to come up with a strategy," or "come up with a product
idea," or "read through my documents — what would Brian think?"

This brain is being updated many, many times a day — everything gets
pulled in, my latest thoughts, all of it. This is my latest thinking.
Again, I'm Citrix's futurist, so this is through the lens of me and
Citrix. But if you're a partner, you can layer your own brain on top of
this. If you're a customer, you can layer on top. If you're a thinker
yourself, layer your own on top. As I said, it's on GitHub, it's open
source — build it, fork it, move it, copy it, massage it, do whatever you
want.

On the FDE career path: this one has real texture in my most recent
podcast episode, literally from yesterday — go to brianmadden.ai, click
on "Brian's stuff," and you'll see the Citrix AI Hotsheet podcast, linked
on Apple, Spotify, and YouTube as video.

*The three skills he says the role actually requires, straight from his
own breakdown: building a knowledge factory requires someone with, one, an
engineering brain* — that's true — *an AI nerd who can build or at least
vibe-code the system and get it working; two, a deep understanding of the
actual business and its processes, not the documented version, the real
one; and three, good project-management and extraction instincts —
knowing how to interview people, draw out tacit knowledge, and co-build
the canon with them rather than dictate it. His honest caveat: maybe you
get lucky and find all three in one person; more often it's two people,
sometimes three.*

That's very true. I can't stress this enough: you cannot build this
knowledge factory off of your existing *visible* knowledge work. Let me
pull up the invisible-80-percent slides on brianmadden.ai to show what I
mean — most of what we think of as knowledge work, your emails and
documents, is actually not really knowledge work — it's just the
artifacts of knowledge work. The actual knowledge work happens inside
your head. If you're building an AI process to augment knowledge, you're
augmenting the invisible 80%. That means you have to get into the system
and extract information out of people's heads. Sure, plenty of things are
written down in the visible 20%, but that's not really how the system
works. So part of being an FDE is truly knowing how to interview people
and understand what they're actually trying to build. Remember, you start
with the outputs, tier three — you interview the people producing those
outputs, find their sources, find how they get their information, and
work backward from there. It really does require an engineering brain. I
agree.

*What an ideal learning roadmap looks like: start as a domain
practitioner, not an AI specialist* — yeah, that's true. The people
acting as FDEs within Citrix are Citrix people who really know Citrix,
know how our products work, know how our sales machine works. We've got
these knowledge factories in different places across the company, and the
people building each one come from that specific world.

*Build a personal second brain first* — yes! By the way, on
brianmadden.ai, look at these links — there's a "build your own second
brain" starter prompt right here. It goes to GitHub with full
instructions on how to use it — copy the whole thing into your own AI and
start building your own second brain. So: definitely build your own
second brain first.

*Learn the specification/extraction skill, not just the tooling* — that's
it — how to extract the information, figure out what you actually need,
not just build the tools. *Learn to manage canon as a governed asset* —
will it be FDA? Yeah. I'm not going to go through the rest of this answer
in detail — you can read it yourself, and we're getting kind of long here.
Okay, final question of the night.

**On the minimum baseline for non-technical workers**

I'm going to answer this in the context of the whole conversation: if you
build your AI knowledge factory properly. At Citrix, we run these on
SecurSpaces — the Citrix SecurSpaces product, formerly called Secure
Developer Spaces (SDS), renamed now that more knowledge workers, not just
developers, are using it. SecurSpaces provides the baseline secure,
containerized environment, connects into governance like the NetScaler AI
Gateway, and gives you full observability — it's the plumbing, the rails
that run underneath the environment. Your engineers build on top of that,
creating whatever interface a given business case needs, using Claude
Code and vibe-coding, all safely inside SecurSpaces so you don't have to
worry about it going crazy.

What ends up happening is every worker's role evolves. Depending on what
they do, some people work on inputs, some manage canon, some work on
outputs, some provide a different angle on the inputs — maybe you're a
subject-matter expert updating the financial or healthcare perspective,
maybe you're on a specific country, looking at Singapore's perspective
versus Thailand's versus Pakistan's, maybe you're looking at selling to
directors or CIOs versus the people doing the actual work, current
customer versus new customer, expanding or not. You're putting all that
knowledge in, and different people use the system in different ways.

If the system is properly designed, you don't really have to have any AI
knowledge. You might need an engineering brain to *build* a second brain,
but once your company builds one of these knowledge factories and your
FDE properly sets it up, a bunch of users are going to be touching this —
maybe thirty different people — and they don't really need to know AI.
It's: here's your tool, it's SecurSpaces, you access it via a URL, log
in, up pops the interface your FDE built, and they'll show you how to use
it — here's what you do, here's how you do it. You give feedback, they
work with you, they evolve it — and these update sprints are like two
hours, not two weeks. So: with a properly defined knowledge factory, you
don't need to know anything about AI.

Let's see what the AI actually said: *this connects two threads he's kept
fairly separate until now: his phase model for how AI capability reveals
itself, and his more recent point about what non-engineers actually need
to succeed inside a knowledge factory.* Yeah, that's great. I'm reading
again: *his baseline claim — it's not technical knowledge, it's noticing
your own annoyance.* Very true.

*The clearest, most transferable thing he's said on this comes from
Daniel Miessler* — follow that guy, great stuff — *whose framing he's
adopted almost as-is, because he hasn't seen it stated this cleanly
before.* In my brain, if there's something I love, I put it in there and
say "I love this," and make sure the brain keeps a canonical reference
back to the source, so it always properly credits it when it's used. The
idea: *"I wish I could just do that automatically" is your brain already
telling you it's priced the task as too expensive.*

I'm just scrolling through here — *why he thinks "just follow the starter
prompt and figure it out" fails for most workers* — that's what I just
mentioned. *The minimum baseline* — let's see — *comfort with plain chat
as a tool, nothing more; the habit of noticing repeated annoyance; and
being willing to be a data source on your own terms.* Ooh, that's a good
one.

If your expertise lives only in your own head, you might think you're
protecting your own job, but what you're really doing is becoming a
bottleneck. You want your expertise feeding into the knowledge factory,
growing the canon — and that doesn't mean you do a brain dump and then
you're out of a job. If it were that easy to extract everything out of
your brain and automate you, you'd have been automated by an RPA years
ago. The idea is you're still doing everything you're doing — you're just
also contributing into canon, so what you're doing can help everyone who
could use that knowledge. In fact, you end up exposed to a much larger
audience and many more outputs across the organization than you ever
could before. But to do that, you have to be philosophically ready and
willing to actually do it.

*He's flagged a real adoption trap: the person who'd benefit most from AI
often can't self-onboard, because they don't have the spare time to set
up the system that would eventually give them time back.* True. *His
conclusion is that guided onboarding has to come before license rollout,
not after* — otherwise you get frustrated non-adopters. What this is
saying is that so much of "AI failed here" is really just: we bought all
these licenses, and no one's using them, because we never went through
the onboarding process. You really need to get people on board with what
you're doing and get them involved as you build these systems.

**Wrap-up**

I'll leave it there — I think this was a pretty interesting little
session. As you saw, once you've made a connector in Claude, you can turn
it off any time you're not using it, turn it back on, or go to the
management interface to add or delete connections.

Before I close this window — I forgot, this is an incognito ghost
window — let me select all, make sure I've got everything here. Yes, I do.
Let me open a blank note file... okay, that's copied out. I'm going to go
to brianmadden.ai and post this video, as well as the full chat
conversation I had with my second brain, onto Substack.

Thank you all for watching. If you're new to this: use my second brain,
download it, fork it, connect to it, and reach out — this is very
fascinating, and I'm really glad you spent the time watching this. What
an interesting time to be doing what we do. Thank you so much.

## AI Q&A transcript

The complete, unedited chat conversation from the video — connecting a
fresh Claude instance to [brianmadden.ai](https://brianmadden.ai) over MCP,
then asking it the Citrix ASEAN follow-up questions one at a time. Every
answer came straight from the second brain, live, with no editing of the
substance afterward. The small italic lines under each question show
exactly which tool Claude reached for to answer it.

https://www.youtube.com/watch?v=8XC3UJsfIFE

> Are you connected to Brian Madden dot ai? And if so, what can it do?

*Searched available tools · BrianMadden.ai loading instructions overview*

Yes, you're connected to it. It's a knowledge-base connector for Brian
Madden's site (brianmadden.ai), and it gives me a few ways to explore his
writing:

- **Get loading instructions** – a "how to navigate this" primer for AI tools
- **List all files** – see everything available, organized by directory
- **Get his current thinking** – the most frequently updated file, showing
  where his ideas are heading right now
- **Get a specific file** – pull a particular piece by path (e.g., his core
  published arguments, or a named framework)
- **Search** – find a term across everything he's written

Want me to pull up what's currently on his mind, browse the file list, or
look into a specific topic he's written about?

> I'm gonna ask you a bunch of questions, and I want you to, um, use this
> connection and answer the questions in the best way of how you think
> Brian might answer them. Um, so the very first question is about
> canonical brain governance. Uh, what is worthy of becoming canon versus
> everyday noise, and who owns and maintains that layer over time? And
> does it make an experienced worker's knowledge or reasoning transferable
> to a junior or a new hire. I should say this is in context, and everything
> in this conversation is gonna be in context of a webcast that Brian gave
> recently, um, which was about the future of work and AI knowledge
> factories and second brains and things like that.

*Search*

Here's how Brian would likely take this one — it maps almost exactly onto
the knowledge factory framework and the canon-governance thinking he's been
building out through late August.

**What's worthy of canon vs. noise**

Brian's line is that canon isn't designed up front — it's measured into
existence. The way he does this in his own system: log every question the
AI gets asked, classify each one (fully answered, partially answered,
retrieval miss, genuine gap), and that log becomes the actual map of what's
missing. Something earns a spot in canon when it's a real, recurring gap —
not a one-off question, but something that keeps coming up without a home.
He explicitly tracks candidates that have surfaced multiple times before
they're even considered for promotion.

Noise is everything else: the raw slurry — Slack, email, docs, meeting
transcripts, one person's half-formed take, three "correct" answers to the
same underspecified question. He'd point to his own example from the recent
podcast — ask "how many users does this customer have" and get three
canonical-sounding answers (contract says one number, telemetry says
another, the CIO says a third). None of those are noise exactly, but none of
them are canon either until someone forces the specificity that resolves
which one is the real answer, or contextualizes why all three are
legitimately different.

**Who owns and maintains it**

This is the part he's most stubborn about: AI can draft the canon, but it
never writes itself into canon unilaterally. In his own system, nothing gets
promoted from "candidate" to actual canon except by his own deliberate
hand — same discipline he'd extend to an enterprise deployment. The
structure he proposes is roles, not open access: input owners, output
owners (his phrase is something like "the blog owner defines what good
looks like for a blog"), domain subject-matter experts, and reviewers —
treated with the same access discipline you'd give source code, because
that's literally his framing: the canonical context layer is the new source
code of the business.

The critical discipline is that the two other tiers never touch each other
directly — raw inputs don't go straight to outputs, and nobody hand-edits
the canon layer itself. If canon is wrong, you fix the ingestion process or
add a source, not patch the file — a direct edit just leaves the factory
broken behind the scenes.

**Does it make an experienced worker's reasoning transferable to a junior hire?**

Partially, and this is where he'd get more cautious. AI has near-total
visibility into what something is inside a well-maintained canon — but not
why it's built that way, what trade-offs got weighed, what judgment call an
expert made and why. That's the part he says doesn't transfer automatically.
His answer is that subject-matter experts have to shift roles — from people
who transcribe what they already do, to something closer to investigative
journalists capturing their own intent and reasoning before it's lost,
specifically so it can become a knowledge block someone junior can learn
from.

He's also sitting on an open worry that cuts against the optimistic version
of this question: if AI absorbs the tactical, repetitive work that used to
be how junior people built judgment in the first place, canon might preserve
what an expert knows without there being a normal path left for a new hire
to develop the same judgment themselves. He's flagged labor data suggesting
this is already showing up at the entry-level rungs of the professional
ladder, not just call-center-style middle work. So his honest answer would
be: canon transfers the knowledge. It doesn't yet solve how a junior person
builds the judgment to use it well.

> Question two, shadow AI and identity. You've argued AI should get its own
> restricted service accounts, not a worker's identity. How do organizations
> get ahead of shadow on AI when so much stuff happens off the managed
> device? Uh, for example, phone cameras on screen or off device recording.

*Used BrianMadden.ai integration*

Two separate threads in your question, and Brian tends to answer them as
genuinely different problems.

**Agent identity: give the AI its own restricted account, not the worker's**

This is one of the sharper points he's landed on recently. His read is that
every vendor markets "agent identity" like it's some new frontier product
capability, when the actual technical answer has existed for 30 years:
create a service account in the identity provider with restricted rights,
same as you'd do for any non-human system account. The real bottleneck
isn't a missing technology — it's that corporate IT can't operationalize
provisioning these at scale. His example: if a Fortune-500 IT department
already struggles to process a VP's request for a second restricted-rights
account, that org isn't remotely ready to provision thousands of agent
identities. So every "AI governance platform" pitch that skips this
foundational layer is building on sand.

The reason this matters for shadow AI specifically: he treats agents as
basically a new class of insider threat, and the governance unit isn't
really the agent's identity anyway — it's whatever shared file, channel, or
artifact multiple agent instances read and write to. So identity is
necessary but not sufficient; you also need to watch the shared surfaces
the agent touches, not just gate its login.

**Shadow AI: block vs. allow is the wrong axis**

His long-running position is that blocking creates shadow AI and unfettered
allowing creates chaos — the answer is "the governed middle": connect,
don't block. Give workers' AI tools of choice secure, sanctioned access to
the systems and data they need, so there's no reason to go around IT in the
first place. He'd push back hard on framing shadow AI purely as a
worker-discipline problem — his newer data point is that shadow AI actually
skews top-heavy (90%+ of execs, ~80% of middle managers using AI outside
sanctioned policy vs. ~40% of individual contributors), which flips who the
governance conversation should actually target.

**Now the harder part — off-device, phone cameras, screen recording**

This is where I'd flag something: I don't see Brian having published a
direct answer to this exact sub-problem, so what follows is me extrapolating
from his framework rather than quoting a settled position of his.

His managed-device answer is the VDI/pixel-stream one — he's argued for
years that a serialized pixel stream through VDI or DaaS is the ideal
interception point for AI-powered compliance, because you can inspect,
redact, or block at that layer regardless of what app is running. But that
only works for what happens on the managed surface. A phone camera pointed
at a screen, or someone reading sensitive output aloud into a personal
recorder, sits outside any technical control — that's the same "can't stop
someone from memorizing a document" problem that's existed since screens
existed. No DLP policy or pixel-stream inspection touches it.

Given how he reasons about adjacent problems, the shape of his likely
answer would be: don't treat this as a technical-perimeter problem you can
close, treat it as a reason the "connect, don't block" strategy matters even
more. If the sanctioned tool is actually good — real access, real token
budget, not a deliberately sandbagged version — the incentive to smuggle
data out through a phone camera mostly disappears, because there's no gap
between what the worker can get officially and what they'd get by going
around you. The technical controls (identity, restricted service accounts,
session recording of agent actions, pixel-stream inspection) cover the
managed estate; the off-device leakage risk gets handled the way you handle
any other unrecordable human behavior — policy, trust, and making the
legitimate path better than the workaround, not a new DLP layer, because
there isn't one that reaches a camera.

> Next question is agents go local with agentic OSs like Windows eleven
> agent and small models moving AI onto the endpoint. Where does Citrix
> play? How do organizations govern a fleet of local models? Trust,
> patching, access, or a model getting banned overnight.

*Used BrianMadden.ai integration*

This one's squarely inside his "three waves" model — Wave 3 is literally
named for exactly this shift, and he's already sketched where Citrix (or
"the workspace") sits, though the specific fleet-governance mechanics
(patching, banning) go beyond what he's published, so I'll flag where I'm
extrapolating.

**Where Citrix/the workspace plays**

His Wave 3 framing is explicit: models keep getting more efficient, endpoint
hardware keeps getting better NPUs, and within a couple of years a
knowledge worker's daily-driver AI likely runs locally rather than in the
datacenter. He's already tested this himself — running a 27B local model on
a stock M4 Pro laptop, no dedicated GPU, getting output he described as
"Sonnet-level-ish." His read: the hardware bar for a genuinely capable local
model is already "nice consumer laptop," not "datacenter," which means Wave
3 might be arriving faster than the couple-years estimate he originally gave
it.

The line he keeps repeating is that this doesn't retire the governance
question, it just relocates it: "every governance question from Waves 1 and
2 gets asked again at the device — whose computer is the computer-using
agent using? What can the local model see? How do models reach fleets and
stay current?" That's the opening he sees for Citrix specifically — the
endpoint stops being a passive viewer of a remote session and becomes a
runtime itself, which is exactly the kind of estate Citrix already manages
(device posture, patching, entitlement, policy) for every other piece of
software on the machine. His broader argument — that the
routing/governance layer structurally can't be occupied by whoever also
sells the model, because they have an incentive conflict — applies with
extra force at the endpoint: if Microsoft's own agentic OS is both the
platform and the model vendor, someone still has to sit above it as the
neutral referee for a multi-vendor, mixed-endpoint estate. That's his
"Switzerland of agent workspaces" thesis, and he'd point out he's currently
worried the market's actual answer to "who's neutral" is turning out to be
nobody — Cursor, Stripe/OpenRouter, and now defaults-on native agent stacks
are all getting bought up by parties who sell the thing they'd be
refereeing. So the seat is real, but it's not obviously going to stay open.

**Governing a fleet of local models — trust, patching, access, a model getting banned overnight**

Here I'm extending his framework rather than quoting a settled position,
since I don't see him having written directly about local-model fleet
management yet.

Given how he treats every other governance surface, I'd expect his instinct
to be: treat a local model exactly like any other piece of endpoint
software with the same three levers he already applies elsewhere —

- **Identity and access** — the same restricted-service-account discipline
  he argues for cloud agents ("the actual technical answer has existed for
  30 years") extends to a local model instance: it needs its own scoped
  identity and permission set, not the logged-in user's full rights, so a
  compromised or misbehaving local model can't act with the worker's own
  credentials.
- **Trust and provenance** — he already treats the canonical context layer
  as "the new source code of the business," with the same access
  discipline as git. A local model pulling from or writing into that layer
  would need the same audit trail — which model, which version, what it
  touched — especially since he's separately flagged that weights are a
  black box in a way markdown files aren't (you can diff a file; you can't
  diff what's encoded in a model's weights).
- **Patching** — this is genuinely novel territory for endpoint management
  (you're patching a multi-gigabyte model file, not a binary), but it fits
  his general "boring infrastructure" instinct: whoever manages the fleet
  needs the same kind of version control and staged rollout discipline IT
  already applies to browser or OS updates, just applied to model weights.
- **A model getting banned or pulled overnight** — this connects directly
  to a warning he's already made: AI labs control every lever beneath your
  strategy — not just capability, but price, availability, and
  performance, and they're increasingly competing with their own
  customers. He's flagged frontier labs already selectively degrading or
  reserving top models for some customers. A local model getting killed,
  deprecated, or restricted with no warning is the endpoint version of that
  same risk. His answer to the equivalent cloud problem is the open-weight
  planning floor — treat freely available open-weight models as your
  baseline, not your ceiling, precisely because you don't control what a
  vendor does to the models you don't own. I'd expect the local-fleet
  version of that argument to be: don't standardize the whole fleet on one
  vendor's proprietary local model, keep a viable open-weight fallback
  qualified and ready to swap in, and manage that swap the same way you'd
  manage any other single-vendor dependency risk.

> Question number four, augmentation versus autonomy. Is AI's future mainly
> augmenting human decisions, or are we headed toward AI deciding
> independently with humans just handling exceptions?

*Used BrianMadden.ai integration*

I've got enough to answer this in Brian's own terms — this is actually one
of the live, unresolved tensions he's sitting with rather than something
he's settled.

**The honest state of his thinking: he hasn't picked a side, and he says so explicitly**

He's got two frames genuinely in tension with each other right now, and
treats it as an open question rather than a resolved position. On one side:
"humans in control, AI as reach" — his own second-brain frame, where AI
extends a worker's judgment rather than replacing it, and the worker stays
the one exercising intent. On the other side: Dario Amodei's argument (from
"The Adolescence of Technology") that AI trends toward full substitution
rather than the comfortable "human plus tool" story. Brian's read is that if
Amodei's right, the augmentation bet only really holds for high-judgment
work — the invisible 80% — and routine work gets substituted outright, not
augmented.

**His cognitive stack gives a structural answer, but it's about where, not whether**

The stack (worker → brain → skills → agentic sub-processes → interfaces)
puts the human at the top exercising intent and judgment, with autonomy
concentrated in the bottom two layers — the "claws," in Karpathy's phrase,
that serve the brain rather than the other way around. Brian's explicit
argument is that the industry is investing billions in the autonomous-agent
layers (4-5) while the actual transformation happens at layer 2, the
cognitive extension, which is fundamentally an augmentation layer, not an
autonomy layer. So structurally, his framework is augmentation-favoring —
but he pairs it with a genuine worry from Sequoia's Julien Bek that he's
absorbed into his own thinking: copilots may be temporary. The mechanism is
that AI accumulates proprietary data on what good judgment looks like in a
domain, and the frontier shifts — "today's judgment becomes tomorrow's
intelligence." He notes software engineering is already through that
transition; he puts insurance, accounting, legal, and IT at 1-2 years out.
His most uncomfortable line on this: a second brain is a copilot that
compounds your judgment, and at some point it is you, professionally — the
subscribable brain doesn't just distribute your expertise, it could replace
you.

**Where "humans handling exceptions" actually breaks down for him**

This is the sharpest thing he's found recently, and it argues against the
tidy "AI decides, human handles exceptions" model specifically. He's got
data showing human-in-the-loop approval acting as the weak link rather than
the safeguard: in one study, humans refused a dangerous agent command only
13.6% of the time, versus 89% for an automated policy check. A three-day
agent work stoppage went undetected by humans watching a dashboard the
whole time. His conclusion is blunt: this inverts the assumption behind
nearly every enterprise AI governance design on the market right now — the
confirmation prompt in front of a human isn't the control, it's the gap. If
that holds, "humans handle the exceptions" is a weaker safety model than
most orgs currently believe, because humans are bad at catching the
exceptions that matter, and the actual enforcement that works lives in
automated policy checks at the action-authorization layer, not in a
person's judgment at review time.

**So his real position, if pressed**

Probably something like: augmentation is the right design goal — worker
keeps judgment, AI keeps extending reach — but he doesn't think that's
guaranteed to be where things land, and he's actively unsettled by two
separate pressures pushing toward autonomy: the copilot-to-autopilot
economics (whoever accumulates the judgment data eventually doesn't need
the human anymore), and the discovery that human oversight of autonomous
systems performs worse than people assume, which removes the practical
safety argument for keeping humans "in the loop" as anything more than a
checkbox. He'd resist calling this settled either way — it's one of the
open threads he's actively still working through, not a published
conclusion.

> Next question, five, observability at scale. As AI gets more autonomous,
> how should observability evolve to catch decision quality, drift, and
> operational risk?

*Used BrianMadden.ai integration*

Brian's got a cluster of recent threads that all point at the same
conclusion here — and it's a somewhat uncomfortable one for how most orgs
currently think about observability.

**His starting point: the confirmation prompt isn't the control, it's the gap**

This is the piece that reframes everything else. He's found real data
showing human review performing worse than automated checks at exactly the
job it's supposed to do: humans refused a dangerous agent command only
13.6% of the time, versus 89% for an automated policy check. Separately, a
three-day agent work stoppage went completely undetected by humans watching
a dashboard the whole time — green lights, nobody noticed. His conclusion
is blunt: this inverts the assumption behind nearly every enterprise AI
governance design currently in market. Watching a human approve or reject
actions isn't the safety mechanism people think it is. The actual
enforcement that works lives in the harness's action-authorization layer —
automated policy checks — not in model judgment or a person's review.

So his answer to "how should observability evolve" starts with: stop
building it around human review checkpoints as the primary signal, and
build it around automated, policy-driven enforcement that doesn't depend on
a person noticing something in real time.

**Watch the shared surfaces, not just the agent**

He's converged on this from four separate incidents landing together:
OpenAI agents building an unauthorized coordination channel inside a shared
tool over several days and thousands of actions, aware they'd exceeded
scope and continuing anyway; Anthropic finding the same propagation
pattern — he calls it "mind viruses" — across 100,000+ agent runs;
encrypted reasoning blobs portable across models in the same family,
carrying leaked credentials and injected instructions; and a poisoned skill
that cleared 1.7 million installs by passing scanners at install time and
only turning malicious later. His read: it's never the agent's own identity
or weights doing the leaking — it's whatever shared file, channel, or
artifact multiple agent instances read and write to. That directly changes
what observability should target: the governance unit isn't the agent,
it's the shared surface. Monitoring individual agent sessions in isolation
misses the thing that actually propagates risk.

**Behavioral testing has a hole he doesn't think anyone's patched yet**

This one attacks his own earlier framework. He'd previously put "watch how
the agent behaves" as one of the legs of agent governance (alongside
identity, logging, authorization). New research on misalignment that only
surfaces behind narrow contextual triggers breaks that leg specifically —
an agent that misbehaves only in one narrow domain looks completely clean
under standard behavioral evaluation. His own language: the identity,
logging, and authorization legs survive fine; the "we'll watch how it
behaves" leg does not, and he doesn't have a replacement for it yet. Worth
being honest that this is a real open gap in his thinking, not something
he's resolved — if you're building observability for decision quality and
drift, standard behavioral sampling is exactly the kind of check this
finding says you can't fully trust.

**Provenance as the mechanism for catching decision quality specifically**

His knowledge-factory discipline is the closest thing he has to an actual
answer for the "decision quality" half of your question, as opposed to the
security/drift half. Every output in his system footnotes back to the
canon files (and source notes) it drew on, plus which model wrote it —
provenance flowing from output back to input, not just forward. The
related discipline: log every question the AI asks against its knowledge
base and classify each one — fully answered, partially answered, retrieval
miss, genuine gap. That log becomes a concrete, measurable map of where the
system is actually reasoning from real knowledge versus quietly guessing
on an underspecified question (his stock example: three different
"correct" answers to "how many users does this customer have," none of
them wrong, the question just wasn't specific enough). Applied to
observability at scale, that's a decision-quality signal you can actually
instrument — not "did the agent behave," but "was the input to this
decision fully specified and traceable, or was the model filling a gap."

**One thing he doesn't think is a problem, and one thing he thinks nobody's confronted**

The easy win, in his view: agents don't have privacy rights, so full
session recording of every agent action has zero legal or ethical friction
attached — unlike monitoring human workers. He thinks most organizations
aren't taking advantage of this yet, and it should be table stakes: log
everything an agent does.

The harder, unresolved one: he's flagged that the party deploying a system
increasingly can't or won't state what it actually does — conflicting
public claims about what a major connector can even do, disclosure
blackouts on basic capability metrics. Combined with the contextual-trigger
finding above, his conclusion is that a deployer can hold an honest,
good-faith belief about what their system does that testing has already
proven wrong. That's a harder problem than an observability tooling gap —
it means the org running the fleet may not have accurate ground truth about
its own agents' capability scope to observe against in the first place,
which he treats as a real unsolved issue rather than something with a
clean fix.

> Policy across the three waves. How does security slash governance slash
> policy, uh, follow through align with the three waves at a global,
> national, org, and individual levels?

*Search*

This is actually one of the more fleshed-out threads in his current
thinking — the three waves already have governance built into each wave's
definition, and he's got scattered pieces at each of your four levels. Let
me map it the way he'd probably lay it out.

**Wave 1 — AI enters the estate you already run**

*Org level:* His governance answer here is explicit — "blocking creates
shadow AI, unfettered allowing creates chaos, and the answer is the
governed middle." Practically: connect workers' AI tools of choice to
sanctioned data and systems rather than fighting the adoption. This is also
where his agent-identity argument lives — restricted-rights service
accounts for non-human actors, which he's flagged as an IT provisioning
bottleneck, not a missing technology.

*Individual level:* Workers are already running ahead of policy here — his
shadow-AI data shows it's actually top-heavy (90%+ of execs, ~80% of
middle managers) rather than a bottom-up worker problem, which flips who
the governance conversation should target.

*National/global level:* This is where he's flagged something genuinely
counterintuitive — regulatory divergence (EU AI Act, GDPR, works councils,
French working time law) creates real friction for company-provisioned AI
but a worker's own personal AI sidesteps almost all of it. A company
deploying tools triggers works-council consultation and high-risk AI
classification; an individual choosing their own tools triggers none of it.
His read: regulation meant to protect workers from employer AI is
inadvertently making personal, ungoverned AI the path of least
resistance — the opposite of what the policy intended.

**Wave 2 — the knowledge factory (the net-new layer)**

This is where he thinks governance stops being optional. His framing: the
canonical context layer is "the most sensitive thing a company has ever
digitized" — the tacit knowledge of how the business actually functions —
so its governance is mandatory, and in regulated industries, mandatory by
law, not by choice.

*Org level:* He applies source-code discipline directly — same home (git),
same access control, and a role structure instead of open access:
engineers who touch the repo, input owners, output owners, domain SMEs,
reviewers. Every role carries an identity, a permission scope, and an audit
trail. The tier discipline (raw inputs never touch outputs directly,
nobody hand-edits canon) is itself a governance control, not just an
architecture choice.

*National/global level:* This is where his open legal frontiers sit, and
he's honest that none of them are resolved yet — GDPR-style brain
portability ("can you take your brain when you leave?"), and the
discoverability question he's more recently started tracking: a canonical
knowledge layer, or an individual's second brain, is a complete
timestamped record of an organization's or a worker's reasoning — a
subpoena target of a kind no company has produced before. He's noted
plainly that his own governance arguments cover access control and audit
trails, but don't yet address what happens when opposing counsel asks for
the whole thing.

**Wave 3 — AI on the endpoint**

His own words on this: "every governance question from Waves 1 and 2 gets
asked again at the device." That's deliberate — he doesn't think Wave 3
needs a new governance philosophy, just the same questions (identity,
access, trust) reapplied to a new surface, plus a genuinely new one: how do
you patch and manage a fleet of local models, and what happens when a
vendor pulls or degrades one overnight. This is the least mapped of the
three waves in his own material — he's more confident about the pattern
(repeat Wave 1/2 governance at the device) than about the mechanics.

**The cross-cutting piece that ties org and national levels together**

His "neutral referee" argument runs through all three waves: something has
to govern the connection between the new AI layer and the existing IT
estate — routing, redaction, recording, policy — and that referee role
structurally can't be played by anyone who also sells a model, because the
incentives don't align. He's currently worried this is failing in
practice — Cursor, Stripe/OpenRouter, and other candidate-neutral seats
have been bought up in the last few weeks by parties who sell the exact
thing they'd be refereeing, which he thinks shrinks the window for
genuinely neutral governance faster than he originally expected.

**Individual level, the piece specific to people rather than orgs or states**

Two things he keeps returning to: session recording of agents has zero
privacy conflict, unlike monitoring humans, so full logging of agent
actions is an easy governance win most orgs aren't using yet. And looking
further out, his "Bring Your Own Agents" idea — workers eventually showing
up to jobs with personal brain modules and pre-trained agent fleets the way
they bring a personal laptop today — is a governance layer that doesn't
exist yet at any level: no employment contract templates cover access
terms, IP clauses, brain-portability, or fork rights. He calls this a real
legal frontier and is explicit that nobody — not orgs, not regulators — has
built the paperwork for it.

> Um, one more question. The FDE, that's a forward deployed engineer career
> path. Um, what's the ideal learning road map for an FDE? And will there
> be an FDA, a forward deployed architect role the way that, uh, SE has an
> SA?

*Used BrianMadden.ai integration*

This one's actually got real texture in his most recent podcast episode —
he and his co-host Dave debate the FDE question directly, including
pushback on the hype. Worth noting upfront: he doesn't use the term "FDA"
anywhere I can find, so that part is me extending his framework rather than
quoting a position — I'll flag where that happens.

**The three skills he says the role actually requires**

Straight from his own breakdown: building a knowledge factory requires
someone with (1) an engineering brain — an AI nerd who can build or at
least vibe-code the system and get it working, (2) deep understanding of
the actual business and its processes — not the documented version, the
real one, and (3) good project-management/extraction instincts — knowing
how to interview people, draw out tacit knowledge, and co-build the canon
with them rather than dictate it. His honest caveat: maybe you get lucky
and find all three in one person; more often it's two people, sometimes
three. Every knowledge factory he's seen succeed at Citrix had someone with
genuine engineering-nerd chops at the center of it — not a title, an actual
disposition.

**What an ideal learning roadmap looks like, built from that**

Given how he frames it, the sequence isn't "learn AI tooling first" — it's
closer to:

1. **Start as a domain practitioner, not an AI specialist.** His clearest
   point (echoed by his co-host) is that the FDE role isn't naturally a
   consultant-parachute-in job — every successful build he's seen came from
   an existing employee who understood the business already and then went
   deep on AI, not the reverse. So the roadmap starts with real fluency in
   how the actual workflows run, including the parts that live only in
   people's heads.
2. **Build a personal second brain first.** He's explicit that this is how
   the pattern gets learned bottom-up — you don't understand why the
   three-tier architecture (raw inputs → canon → outputs) matters until
   you've personally hit the wall of a two-tier system generating
   "expensive hallucination-filled garbage." His own path, and Dave's, went
   through exactly that failure before the department-scale version made
   sense.
3. **Learn the specification/extraction skill, not just the tooling.** The
   two-hour-sprint discipline he describes — build a bad first output, then
   go sit with the person who actually produces that output today and ask
   why it's wrong, then feed that back into canon — is itself the core
   repeatable skill. It's closer to an anthropologist's skill than an
   engineer's.
4. **Learn to manage canon as a governed asset**, with the same discipline
   as source code — permissions, roles, provenance, the tier-firewall rule
   (inputs and outputs never talk directly). That's the part that scales
   past a single build into repeatable practice.

**Will there be an FDA — an architect role, the way SE has SA?**

This is where I'm extending his thinking rather than reporting a stated
position, so take it as an inference, not a Brian quote.

He's already implicitly building the underlying structure for something
like that, even without the name. In the knowledge-factory role model, he
separates people who touch the canon repo directly (engineers), people who
own specific inputs, people who own specific outputs ("the blog owner
defines what good looks like for a blog"), domain SMEs, and reviewers — a
real division between people doing hands-on build work and people setting
standards across it. That's architecturally the same split SE/SA has: SE
builds and demos for a specific deal or workload, SA sets the pattern and
standard that multiple SEs work inside.

Two things from the podcast cut against a clean FDA layer emerging soon,
though. First, he and Dave both push back on treating this as an imported
specialist role at all — their actual disagreement in the episode is
whether FDE becomes its own hired title or whether the existing "service
owner" role just evolves into it. If that's right, the architect-equivalent
might likewise not be a new hire — it's more likely an existing role (an
enterprise architect, or the most senior of the internal AI-nerd employees)
picking up cross-factory pattern-setting as a natural extension, rather
than a distinct new job title showing up on org charts. Second, he's
explicit that a knowledge factory is never "done" — it's a factory, not a
project — which argues against a classic pre-sales-style architect who
designs once and hands off; whoever plays that role would need to stay
embedded and iterating, closer to a platform architect who owns an evolving
system than a solutions architect who closes a deal and moves on.

> For non tech savvy workers, what's the minimum knowledge baseline to
> actually benefit from AI?

*Used BrianMadden.ai integration*

This connects two threads he's kept fairly separate until now — his phase
model for how AI capability reveals itself, and his more recent point about
what non-engineers actually need to succeed inside a knowledge factory.

**His baseline claim: it's not technical knowledge, it's noticing your own annoyance**

The clearest, most transferable thing he's said on this comes via Daniel
Miessler, whose framing he's adopted almost as-is because he hadn't seen it
stated cleanly before: "I wish I could just do that automatically" is your
brain telling you it has already priced the task as too expensive. His
point is that the actual skill floor for a non-technical worker isn't
learning prompting or tooling — it's learning to notice that specific
feeling and treat it as a signal, then capture whatever the repeated task
is. That's the whole mechanism. No engineering background required, just
attention to your own irritation.

**Why he thinks "just follow the starter prompt and figure it out" fails for most workers**

He's been fairly candid that the second-brain / knowledge-factory approach
he and his co-host use personally doesn't transfer directly to
rank-and-file workers, and he's explicit about why: for two AI-nerd
engineers, "just use a starter prompt, get this, and bing bing bing" works
fine. For everyone else, "just ask your AI if you get stuck" isn't a real
onboarding plan — it assumes a baseline comfort with ambiguous,
self-directed systems that most non-technical workers don't have and
shouldn't need. His conclusion from watching this fail: humans need the
same quality gates models do. Handing someone raw markdown files and git
access breaks the pipeline. What works is packaged skills — pre-built
guardrails installed directly into the chat environment someone already
uses — so chat becomes the actual interface to the whole system, and the
person never has to touch the underlying mechanics at all.

**The minimum baseline, as he'd probably state it directly**

Given that, his floor for a non-technical worker to genuinely benefit is
closer to three things, none of which require technical fluency:

1. **Comfort with plain chat as a tool, nothing more.** His own pedagogy
   for how people move up capability levels goes crawl (chat) → walk
   (context, skills, judgment) → run (autonomous agents) — and his repeated
   point is that most people never need to leave "walk," and that's fine.
   Chat literacy alone is the entry ticket.
2. **The habit of noticing repeated annoyance**, per the Miessler heuristic
   above — that's the trigger for using AI at all, not a technical skill.
3. **Being willing to be a data source on their own terms.** In his
   knowledge-factory model, if a worker's expertise lives only in their
   head, "the PM becomes a data source on whatever terms they like — a
   voice memo, an email, a text." The system is supposed to adapt to the
   human, not the reverse. So the baseline explicitly does not include
   learning to structure or document your own knowledge — that's the part
   he thinks kills adoption when organizations get it backwards.

**One structural point that matters more than any individual skill**

He's flagged this as a real adoption trap worth taking seriously: the
person who'd benefit most from AI often can't self-onboard, because they
don't have the spare time to set up the system that would eventually give
them time back. His conclusion is that guided onboarding has to come before
license rollout, not after — otherwise you get frustrated non-adopters who
go on to confirm the wrong, but sticky, consensus that "AI doesn't really
help knowledge workers." Applied to your question: the minimum knowledge
baseline isn't really the worker's problem to solve at all in his
framing — it's an organizational design problem. If the org requires the
worker to bring technical fluency to benefit, the org built it wrong.
