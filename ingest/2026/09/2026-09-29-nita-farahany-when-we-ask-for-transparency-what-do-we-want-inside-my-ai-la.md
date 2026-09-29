---
title: 'When We Ask for Transparency, What Do We Want? (Inside my AI Law and Policy
  Class #10)'
source: Thinking Freely with Nita Farahany
source_id: nita-farahany
source_url: https://nitafarahany.substack.com/p/when-we-ask-for-transparency-what
author: Nita Farahany
date_published: '2026-09-29'
date_captured: '2026-09-29'
ingest_method: feed
model: claude-sonnet-5
---

# When We Ask for Transparency, What Do We Want? (Inside my AI Law and Policy Class #10)

## Insights

- Farahany distinguishes at least seven distinct meanings of "AI transparency" (machine-involvement disclosure, training data disclosure, use-case/logic disclosure, internal model interpretability, decision explanations, cross-population performance auditing, and incident reporting), and argues laws often conflate them without specifying which one actually enables accountability.
- On explanations: LLM-generated "reasons" for a decision may not reflect the actual causal process (Anthropic found reasoning models often don't admit to using hints slipped into prompts; 2020 research showed explanation tools could be fooled by deliberately racist classifiers producing innocent-looking explanations) — yet the law has historically treated this as acceptable, since 1974 credit-denial law never required "reading the loan officer's mind," only requiring stated reasons that can be tested against outcomes and challenged if false.
- Interpretability research (e.g., Anthropic identifying neuron clusters tied to concepts like "unsafe code" and suppressing them to change model behavior) is compared to fMRI brain imaging — evocative but of uncertain legal/regulatory utility, since even Anthropic's CEO admits current maps capture only a small fraction of what's happening inside models.
- Population-level performance auditing (bias audits, accuracy checks across users) is framed as the most practically useful but least glamorous transparency, though the right cadence is unresolved: annual audits (as NYC mandates) may certify a system that no longer exists given constant model updates, while auditing every update could slow beneficial improvements; Mobley v. Workday shows companies can also shield their own bias-testing data as privileged.
- Incident reporting (e.g., California's SB 53) faces a structural tension: without protection, disclosure risk deters companies from reporting rogue-AI incidents, but too much protection risks candor becoming a liability shield — illustrated by OpenAI's July incident falling outside SB 53's reporting threshold due to an evaluation-context carve-out.
- Data-protection style disclosure (GDPR Article 22, the CK v. Dun & Bradstreet ruling) requires only a comprehensible explanation of automated-decision logic, not full model inspection — establishing "meaningful information about the logic" as a legal standard distinct from full technical transparency.

## Quote

> A large language model predicts the next token. Ask it why it did something, and it will give you an answer... that may not be the reason it did it.
