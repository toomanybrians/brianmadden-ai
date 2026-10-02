---
title: Uplifting conversion across the acquisition funnel with personalization using
  contextual bandits on AWS
source: AWS Machine Learning Blog
source_id: aws-ml-blog
source_url: https://aws.amazon.com/blogs/machine-learning/uplifting-conversion-across-the-acquisition-funnel-with-personalization-using-contextual-bandits-on-aws/
author: Chidi Prince John
date_published: '2026-10-01'
date_captured: '2026-10-02'
ingest_method: feed
model: claude-sonnet-5
---

# Uplifting conversion across the acquisition funnel with personalization using contextual bandits on AWS

## Insights

- Amazon Payments deployed a multi-objective contextual bandit (LinUCB, one model per funnel stage: start, submit, approve) to personalize acquisition-funnel content, combining per-stage UCB scores via weighted sum rather than optimizing a single metric — framed as solving the "seesaw problem" where optimizing one funnel stage degrades another.
- In a seven-week A/B test, one customer population saw a high single-digit percent relative lift in final-stage conversion; a second population saw no improvement (even statistically significant regression in approvals) despite thorough exploration — attributed to content pool quality, not model failure.
- Key architectural choice: batch processing (weekly SageMaker Processing job), not real-time inference — justified by delayed feedback (approvals lag days) and the claim that visitor behavior doesn't shift fast enough to need real-time updates; includes a static-baseline fallback arm to bound downside risk.
- Content scalability is handled by vetting small sets of reusable "building blocks" (images, taglines) rather than reviewing every combination, with arms as the Cartesian product — explicitly positioned as the natural complement to generative AI's ability to flood a content pool with variations.
- Author explicitly separates the two problems generative AI creates: content *production* (solved, per their earlier post) vs. content *selection* (this post's focus) — argues bandits become increasingly necessary as generative AI multiplies viable content variants faster than traditional A/B testing can evaluate them.
- Interpretability is claimed as a built-in byproduct: LinUCB's learned weight vectors let the team inspect which customer signals drove conversion for a given content arm, without added tooling.

## Quote

> This was not a model failure. Thorough exploration can confirm that a content pool contains no winner.
