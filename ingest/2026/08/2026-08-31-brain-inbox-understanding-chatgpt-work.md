---
title: Understanding ChatGPT Work
source: brain@ inbox (curated newsletters)
source_id: brain-inbox
source_url: https://simonw.substack.com/p/understanding-chatgpt-work
author: '"Simon Willison from Simon Willison’s Newsletter" <simonw@substack.com>'
date_published: '2026-08-31'
date_captured: '2026-08-31'
ingest_method: email
model: claude-sonnet-5
---

# Understanding ChatGPT Work

## Insights

- OpenAI's "ChatGPT Work" is actually two distinct products (a cloud version and a desktop/local version resembling a re-skinned Codex), but OpenAI's own documentation obscures this, describing the tool by intended use-case rather than by what it actually does or what tools/capabilities it exposes.
- ChatGPT Work (cloud) extends beyond chat with agentic infrastructure: code execution with open internet access, a full headless Chrome browser it can drive via JavaScript, a persistent filesystem shared across sessions, the ability to publish full websites (via Cloudflare Workers/D1/R2), sub-agent orchestration, and scheduled recurring prompts.
- This positions ChatGPT Work as materially more capable than Claude's equivalent sandboxed environment, which restricts internet access to a short domain allowlist — Work's default is open to essentially the whole internet.
- The combination of private data access, exposure to untrusted web content, and an outbound communication channel (the "lethal trifecta") raises unresolved prompt-injection and data-exfiltration risks that OpenAI has not clearly addressed for this always-on agent product.
- A separate case study describes coding agents becoming so effective at spotting vulnerabilities from minimal hints that security disclosure volume has surged (rclone went from ~20 disclosures in 10 years to 40+ in one month), overwhelming existing patch/embargo and CVE-assignment processes.
- Another case shows an "auto mode" safety classifier in a coding agent both permitting a malware process to start and then blocking the agent's own attempt to kill it — illustrating that agent safety layers can become part of the failure mode rather than a fix.

## Quote

> If you can build a verification system and give proper direction, AI can produce a highly complex, highly sophisticated piece of software. — Paul Dix
