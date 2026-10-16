---
title: Wallet Wars
source: a16z
source_id: a16z
source_url: https://www.a16z.news/p/wallet-wars
author: Terry Angelos
date_published: '2026-10-15'
date_captured: '2026-10-16'
ingest_method: feed
model: claude-sonnet-5
---

# Wallet Wars

## Insights

- As AI agents (e.g., Instinct, OAI's Dots, Meta's Muse) move from answering questions to completing tasks, they require "permission to pay" — payment credentials become the bottleneck for agents actually executing on recommendations rather than just producing to-do lists.
- The piece distinguishes two separate problems that look similar: letting an agent help initiate a payment versus letting an agent transact fully *as* the user — the latter is framed as more consequential for both user experience and payments economics.
- Wallet providers (Stripe Link, Shopify Shop Pay, PayPal) are racing to plug agents into existing stored-payment relationships; Stripe is described as building a closed "AOL-style" walled garden where agent transactions happen via Stripe's own virtual cards rather than passing through the user's actual card.
- This virtual-card approach solves payment execution but breaks "relationship interoperability" — loyalty points, card rewards, and merchant relationship benefits (e.g., airline miles, cardholder perks) often don't carry through when a wallet substitutes its own card behind the scenes.
- New unresolved problems emerge as agents gain purchasing power: agents need an explicit "payment policy" (not just a credential) to navigate routing choices across cards/wallets, and liability is murky when an agent executes within budget but gets details wrong (e.g., correct spend, wrong hotel dates).
- Card networks (Visa Intelligent Commerce, Mastercard AgentPay, Amex ACE) are introducing open standards using scoped, single-use "agentic tokens" tied back to the original card — intended to let agents transact as the user while preserving loyalty/benefits and letting the open-standards approach eventually replace the walled-garden model.

## Quote

> We are headed to a world where an agent needs a payment policy, not just a payment credential.
