---
title: AI Trading Desk (Full Setup)
source: Super Intelligence School
source_id: super-intelligence-school
source_url: https://sischool.substack.com/p/ai-trading-desk-full-setup
author: Super Intelligence School
date_published: '2026-11-21'
date_captured: '2026-11-23'
ingest_method: feed
model: claude-sonnet-5
---

# AI Trading Desk (Full Setup)

## Insights

- The piece walks through an AI-assisted "trading desk" workflow: Python prices paper trades directly off real order book data, and Claude is then used to review the resulting ledger and flag notable findings.
- It illustrates a basic but often misunderstood mechanic of order books: the top-of-book price can represent a tiny available quantity, so the "best price" shown is often irrelevant to anyone trying to transact a meaningful amount.
- Larger orders eat through successive price levels — a $1,000 purchase exhausts the best offer and spills into the next price tier, meaning the effective price paid differs from the quoted price depending on order size.
- The setup runs four paper trades (from $100 to $50,000), deducting a 10-basis-point fee on each side, to show how execution cost scales — the $50,000 trade lost $182.13 overall.
- A secondary point raised is a common misreading of order book fields: treating the "number of orders" column as a multiplier on available volume (e.g., assuming five orders means 5x more liquidity) rather than understanding it as just a count of contributors to the listed total.
- The underlying resource ("the full setup") provides the working Python code and both recorded order books so a user can rerun calculations with different fee assumptions and inspect each fill against the original bid/ask data, with Claude providing a review layer over the output.
