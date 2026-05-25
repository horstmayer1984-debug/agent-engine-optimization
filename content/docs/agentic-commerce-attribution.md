---
title: "Agentic Commerce Attribution: Measuring AI Referrals and Intent"
date: 2026-05-25
weight: 151
category: "Guide"
description: "Learn how agentic commerce changes attribution, why AI referrals are harder to measure, and what merchants should log across discovery, cart, and checkout."
summary: "A practical guide to agentic commerce attribution, covering AI referrals, UCP context, agent-origin sessions, intent data, analytics gaps, and AEO metrics."
keywords:
  - agentic commerce attribution
  - AI referral tracking
  - UCP context
  - agentic commerce analytics
  - AI shopping attribution
---

# Agentic Commerce Attribution: Measuring AI Referrals and Intent

Agentic commerce attribution is the practice of connecting an AI-assisted recommendation, cart, or checkout session back to the agent, surface, user intent, and merchant outcome. It is harder than classic referral tracking because the user's decision may form inside an AI system before a normal website visit exists.

## Why attribution is changing

Classic ecommerce analytics assumes the buyer clicks a link, lands on a page, browses, adds to cart, and buys. Agentic commerce breaks that path. The agent may research products, compare offers, build a cart, and send only the final action or referral to the merchant.

PayPal's merchant research notes that businesses are preparing for AI systems that influence discovery before the shopper reaches the site. Google also frames UCP and Universal Cart as infrastructure for agentic commerce across Google surfaces.

This is why [AEO measurement](/docs/aeo-kpis-measurement/) needs more than rankings and clicks.

## What merchants should attribute

| Signal | Why it matters |
|---|---|
| AI source or agent surface | Shows where discovery happened |
| User intent category | Distinguishes research, cart, reorder, support, or refund |
| Product IDs shown to agent | Connects catalog exposure to sales |
| Cart creation source | Reveals whether cart formed on-site or off-site |
| Checkout handoff | Shows where purchase completed |
| Mandate or authorization reference | Links intent to payment where supported |
| Fulfillment outcome | Connects agent-origin transactions to delivery and returns |

The [five levels of agentic commerce](/docs/five-levels-agentic-commerce/) model is useful because attribution maturity changes at each level.

## The UTM problem

UTM tags still help when an AI assistant sends a user to a page. But they are weak when the agent is not simply referring a visitor.

Agentic journeys may need:

- signed context objects
- cart references
- product candidate lists
- mandate IDs
- consent state
- platform identifiers
- merchant-of-record confirmation

This is closer to transaction tracing than campaign tracking.

## AEO metrics for agentic commerce

| Metric | What it tells you |
|---|---|
| Agent-referred sessions | How often AI systems send traffic |
| Agent-origin cart rate | Whether agents can build carts successfully |
| Structured catalog coverage | How much inventory is machine-readable |
| Agent checkout completion | Whether handoff or native checkout works |
| Policy rejection rate | Whether policies block agent transactions |
| Post-purchase exception rate | Whether agent-origin orders create more refunds or support issues |

Tie these metrics to the [execution layer](/docs/execution-layer/), not only content reporting.

## Implementation checklist

1. Preserve normal referral and UTM tracking.
2. Add agent-origin event names in analytics.
3. Log user-agent, verified bot status, and source platform where available.
4. Store cart source and cart handoff path.
5. Map product IDs to the data exposed in feeds, schema, and APIs.
6. Track checkout failures separately for agent-origin sessions.
7. Connect order, refund, and support data back to the source context.

The [Universal Commerce Protocol guide](/docs/universal-commerce-protocol/) explains where commerce-context exchange may fit.

## FAQ

### Are AI referrals visible in Google Analytics?

Some are visible as normal referrers or campaign traffic. Others may appear as direct, bot, partner, or platform-mediated traffic unless the integration preserves context.

### Is attribution only a marketing problem?

No. In agentic commerce, attribution also affects fraud, dispute evidence, merchant policy, and post-purchase support.

### What is the first metric to add?

Track agent-origin sessions and cart starts separately from normal organic, paid, and direct traffic.

### How does this relate to AEO?

AEO needs to prove that agent-readable infrastructure creates discovery, cart activity, completed actions, and reliable outcomes.

## Sources

Primary sources: [PayPal Agentic Commerce Pulse findings](https://www.paypal.com/us/brc/article/agentic-commerce-pulse-report-findings), [PayPal on AI storefronts](https://www.paypal.com/us/brc/article/ai-storefront-what-merchants-need-to-know), and [Google UCP and Universal Cart update](https://blog.google/products-and-platforms/products/shopping/shopping-updates-google-marketing-live/).
