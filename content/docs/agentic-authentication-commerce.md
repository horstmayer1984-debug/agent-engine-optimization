---
title: "Agentic Authentication for Commerce: FIDO, AP2, and Verifiable Intent"
metaTitle: "Agentic Authentication for Commerce"
date: 2026-05-25
weight: 152
category: "Architecture"
description: "Learn how agentic authentication is emerging for commerce, how FIDO, AP2, and Verifiable Intent support delegated buying, and what merchants should prepare."
summary: "A guide to agentic authentication in commerce, covering FIDO working groups, AP2 mandates, Mastercard Verifiable Intent, identity, privacy, and merchant trust."
keywords:
  - agentic authentication commerce
  - FIDO agentic authentication
  - Verifiable Intent
  - AP2 agent payments
  - agent identity commerce
---

# Agentic Authentication for Commerce

Agentic authentication is the trust layer that proves a user authorized an AI agent to act. It matters because commerce moves real money, inventory, loyalty, and liability. AP2, Verifiable Intent, and FIDO's agentic authentication work are converging around one core need: make delegated intent explicit, verifiable, private, and auditable.

## Why normal login is not enough

Traditional checkout assumes the human is present. They log in, click buy, authenticate, and pay. Agentic commerce changes that. The agent may search, build a cart, and execute within a user's rules.

That raises new questions:

- Who authorized the agent?
- What exactly was the agent allowed to do?
- Was the user present or not present?
- Did the merchant receive the same intent the user gave?
- What evidence exists if the transaction is disputed?

The [AP2 documentation](https://ap2-protocol.org/) frames this as a need for verifiable intent and audit trails.

## What FIDO is doing

The FIDO Alliance announced work on trusted AI agent interactions and commerce. It includes an Agentic Authentication Technical Working Group focused on how users can delegate actions to AI agents with strong authentication, privacy, and security.

Google also announced that it is donating AP2 to FIDO, and Mastercard's Verifiable Intent framework is being contributed into the same standards path.

For merchants, the signal is clear: agent identity and delegated authentication are becoming commerce infrastructure.

## AP2 vs Verifiable Intent vs FIDO

| Layer | Role |
|---|---|
| AP2 | Payment authorization protocol with checkout and payment mandates |
| Verifiable Intent | Trust layer that links identity, intent, and action in a privacy-preserving record |
| FIDO | Standards body for authentication and related agentic interaction work |
| Merchant systems | Enforce policy, checkout, fulfillment, and support decisions |

This connects to [AP2 vs x402](/docs/ap2-vs-x402/) and [Visa TAP vs Mastercard Agent Pay](/docs/visa-tap-mastercard-agent-pay/).

## Merchant implementation implications

Merchants should prepare to store and validate:

- agent identity or verified agent status
- user authorization status
- intent scope
- cart reference
- payment mandate reference
- policy decision
- timestamped audit events
- revocation and cancellation states

This is not just a payment feature. It affects support, fraud, refunds, loyalty, and compliance.

## Authentication readiness table

| Merchant question | Why it matters |
|---|---|
| Can we tell a human session from an agent session? | Policy and risk differ |
| Can we verify who authorized the agent? | Delegated buying needs proof |
| Can we see the intent scope? | Agents must stay within constraints |
| Can we store audit evidence? | Disputes need facts |
| Can users revoke agent authority? | Control must remain with the user |

The [agentic commerce dispute evidence](/docs/agentic-commerce-dispute-evidence/) page goes deeper into the audit layer.

## FAQ

### Is agentic authentication the same as payment authentication?

No. Payment authentication verifies a payment action. Agentic authentication also needs to verify delegation, scope, agent identity, and user intent.

### Why does FIDO matter?

FIDO has experience building open authentication standards. Its new working groups can help agentic commerce avoid fragmented proprietary trust systems.

### Is this ready for every merchant?

Not yet. Most merchants should first prepare product data, policies, and checkout observability while monitoring AP2, Verifiable Intent, and FIDO adoption.

### How does this affect AEO?

Agents need trusted execution paths. Authentication is one of the gates between readable content and safe action.

## Sources

Primary sources: [FIDO on trusted AI agent interactions](https://fidoalliance.org/fido-alliance-to-develop-standards-for-trusted-ai-agent-interactions/), [Google AP2 donation to FIDO](https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/), [AP2 documentation](https://ap2-protocol.org/), and [Mastercard Verifiable Intent](https://www.mastercard.com/europe/en/news-and-trends/stories/2026/verifiable-intent.html).
