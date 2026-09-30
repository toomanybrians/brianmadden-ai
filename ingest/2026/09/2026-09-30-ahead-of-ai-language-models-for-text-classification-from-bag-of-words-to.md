---
title: 'Language Models for Text Classification: From Bag-of-Words to Jev'
source: Ahead of AI
source_id: ahead-of-ai
source_url: https://magazine.sebastianraschka.com/p/classifier-history-and-jev
author: Sebastian Raschka, PhD
date_published: '2026-09-29'
date_captured: '2026-09-30'
ingest_method: feed
model: claude-sonnet-5
---

# Language Models for Text Classification: From Bag-of-Words to Jev

## Insights

- Traces text classification history from bag-of-words (naive Bayes, logistic regression, XGBoost) through RNNs/CNNs with word embeddings to transformer encoders (BERT), decoders (GPT), and encoder-decoders (T5), noting accuracy benchmarks on IMDb reviews throughout (e.g., logistic regression 89.9%, LSTM 85.66%, ModernBERT ~95%, Jev 96.47%).
- Jev, a new proprietary model from TypeSafe AI, is framed as a general-purpose classification API (not fine-tuned per task) offering three interfaces — Choice (multi-class), Noul (binary/multi-label probability), and Score (ordinal rubric) — that reportedly matches GPT-5.6-class decision-making at much lower cost and latency.
- Jev's architecture and training are undisclosed, but the company claims 100% synthetic training data and a proprietary method called "Reinforcement Learning for Calibrated Decisions" (RLCD), which the author speculates may resemble the published RLCR (Reinforcement Learning with Calibration Rewards) approach that penalizes miscalibrated confidence via a Brier-score-like term.
- Calibration (aligning stated confidence with actual correctness) is presented as a distinct, often-overlooked property from raw accuracy; cross-entropy training alone doesn't guarantee calibration in practice due to overfitting on finite datasets.
- Despite a wave of quick open-source "Jev clones" (fine-tuned ModernBERT/Qwen models with similar APIs), none reportedly match Jev's breadth of task performance; the piece compares this gap to early Alpaca vs. GPT-6.
- Notes that OpenAI announced a similar "Decision API" at DevDay 2026, suggesting rapid competitive response to Jev's classification-as-a-service concept, alongside other rival tools (Contrastive Language Models, Laya) that underperform Jev on both accuracy and generalization (e.g., a "Tetris test" of real-time non-classification decision tasks).

## Quote

> One of the reasons the tech community is excited about Jev is that it is the ChatGPT moment for classification.
