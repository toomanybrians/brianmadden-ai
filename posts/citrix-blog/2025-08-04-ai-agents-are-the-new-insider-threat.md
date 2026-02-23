---
title: "AI agents are the new insider threat. Secure them like human workers."
date: "2025-08-04"
authority_level: 5
file_type: citrix-blog-post
tags: [ai-agents, security, identity, ai-agent-identity, insider-threat, workspace-as-control-plane]
related_frameworks: [7-stage-roadmap, workspace-as-control-plane]
original_url: "https://www.citrix.com/blogs/2025/08/04/ai-agents-are-the-new-insider-threat-secure-them-like-human-workers/"
staleness_threshold: stable
---

# AI agents are the new insider threat. Secure them like human workers.

[Original post](https://www.citrix.com/blogs/2025/08/04/ai-agents-are-the-new-insider-threat-secure-them-like-human-workers/)

August 4, 2025

Last week, security researchers demonstrated they could trick AI coding agents into running destructive commands by hiding malicious instructions in documentation. This wasn't some complex zero-day exploit—it was essentially just classic social engineering. (Except the "person" being socially engineered was an AI agent, which means it had perfect memory and zero skepticism, so the malicious instructions were followed dutifully!)

If this sounds absurdly simple, that's because it is, with several examples circulating recently. This perfectly illustrates why we need to think of AI agents as being no different than human workers, applying the same guardrails and security protections to both.

## AI agents are autonomous workers, not tools

For decades, we've built sophisticated trust models for human workers which compensate for our flawed, emotional, and fallible behaviors. We've created entire security frameworks around the ways that humans can be compromised: access controls, DLP, session monitoring, authentication systems, behavioral analytics, etc.

Now that we're starting to think about deploying AI agents that can read, write, execute code, access applications, and make decisions, we need to realize that these aren't tools anymore, they're autonomous workers operating inside our systems. So we need to treat them like any other worker who can be compromised.

Sure, the specific attack vectors are different—prompt injection instead of phishing or poisoned training data instead of social engineering—but the fundamental risk is the same. You have an autonomous entity with privileged access that can be manipulated to act against your interests.

## If your AI doesn't have an identity, your attacker will give it one

In my 7-stage roadmap for human-AI collaboration, one of the differences between Stage 4 (AI uses your computer) and Stage 5 (AI uses your computer without you watching) is that AI agents will need their own identities, rather than running via the logged-on human worker's credentials, service accounts, or a shared API key anyone can use.

This will be a non-negotiable requirement, as having AI agents running without their own identities is no different than having workers in your building without badges. Sure, they might be doing legitimate work, but without an ID, you can't track what they're doing, limit where they can go, or even know they're there.

Luckily the industry is waking up to this. Microsoft recently announced Entra Agent ID, dedicated, first-class identity objects specifically for AI agents. It's their recognition that AI agents need to be treated like employees in your identity system, not just background processes hiding behind a human's credentials.

Without a defined identity, an attacker can effectively assign one. They can make your AI agent do whatever they want, and you wouldn't even know it's not following your instructions. The agent becomes a perfect insider threat that never sleeps, never questions orders, and operates stupidly fast.

## The AI agent attack surface is massive (and growing)

Consider all the ways human workers can be compromised:

- Phishing emails that trick them into revealing credentials
- Social engineering that manipulate them into breaking protocol
- Malware on their devices that captures their actions
- Insider threats where they intentionally cause harm

Now consider the AI agent equivalent:

- Prompt injection attacks that override the AI's instructions
- Data poisoning that corrupts the AI's decision-making
- Adversarial inputs that cause the AI to malfunction
- Supply chain attacks through compromised models, training data, or applications

The researchers who compromised the AI coding agents didn't need sophisticated tools. They just needed to understand that AI agents, like humans, trust their inputs. If you give them bad data, they'll act on it, except unlike humans, they'll do it perfectly, consistently, and without hesitation.

## Why traditional security doesn't work here

The knee-jerk reaction is to try to "fix" the AI: make it smarter, add more filters, train it to detect malicious inputs, etc. This is like trying to create a human who can never be phished. It's a fool's errand. (Though many hours of HR training videos certainly try!)

The other common approach is to restrict what AI can do: limit its access, constrain its actions, and wrap it in so many controls that it becomes useless. This is like hiring an amazing worker and locking down their work environment so tight that they can't actually get their job done.

Neither approach works because they're trying to solve the wrong problem. The issue isn't that AI can be compromised, it's that we're not treating AI compromise as inevitable and building our security accordingly.

## The solution: Treat AI agents like you treat humans

As AI enters your workplace, it's important to understand that identity, access, and intent are no longer just human concepts, and that moving forward they will be part of every worker—human or AI—in your digital workplace.

When a human worker logs into your systems:

- Their identity is verified
- Their access is controlled by role-based permissions
- Their actions are logged and monitored
- Anomalous behaviors trigger alerts
- Sensitive actions require additional authorization
- Their sessions can be recorded and audited

When an AI agent operates in your systems, it needs:

- A verified identity (for the agent, not the human the agent is working on behalf of)
- Role-based access controls (what can this specific AI do?)
- Complete action logging (every decision, every output)
- Behavioral analytics (is this AI acting normally?)
- Authorization workflows (human approval for sensitive operations)
- Session recording (what did the AI see and do?)

Again, this isn't about making AI "safer" per se, it's about acknowledging that AI agents, like humans, operate in unsafe ways in an unsafe world, and appropriate controls need to be built around that.

## Secure the work, regardless of who (or what) does it

The good news is that if you treat your AI agents like humans, then you're already most of the way down the path of securing them in your environment. This is how we think about AI agents at Citrix. We've spent 35 years building guardrails for secure workspaces operated by human workers. Now those same controls—identity management, access control, session monitoring, anomaly detection—need to extend to AI workers.

The principle remains the same: secure the work itself, not just the worker. Whether that worker is human or AI, in the office or remote, using a managed device or their own—the work needs to be secured at the point where it happens.

AI agents will be first-class workers. They'll get identities, access controls, monitored, and contained. All just like human workers.

At the end of the day, it doesn't do much good to worry about whether AI agents can be compromised. They can and they will be. Instead, ensure you have the controls in place to detect, contain, and respond when it happens. That's how you prevent your AI agents from becoming your next insider threat.
