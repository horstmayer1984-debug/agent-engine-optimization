---
title: "The 5 Levels of Agentic Commerce: A Lifecycle Model"
date: 2026-05-23
weight: 149
category: "Framework"
description: "Understand the five levels of agentic commerce across discovery, intent, delegation, cart, payment, policy, fulfillment, and loyalty."
summary: "A lifecycle model for agentic commerce autonomy, showing why payments are only one stage and how UCP, AP2, identity, policy, cart, and fulfillment fit together."
keywords:
  - 5 levels of agentic commerce
  - five levels of agentic commerce
  - agentic commerce levels
  - autonomous commerce
  - self-driving commerce
  - agentic commerce lifecycle
---

# The 5 Levels of Agentic Commerce

The five levels of agentic commerce describe how shopping moves from human-controlled checkout to autonomous buying. But the important point is that each stage of the commerce lifecycle matures at a different speed. Discovery may already be semi-agentic, while payment, policy, fulfillment, and dispute handling still need stronger identity, authorization, and audit trails.

## Why payments are only one part of agentic commerce

Most agentic commerce discussion starts with payments. That is understandable, because payment creates the most obvious risk. But commerce is not just payment.

An agentic commerce journey can include:

- product discovery
- referral and attribution
- intent capture
- delegation and authorization
- policy checks
- cart building
- payment authorization
- fulfillment
- returns, refunds, loyalty, and support

This matters for [Agent Engine Optimization](/docs/what-is-aeo/) because a merchant can be agent-ready in one stage and completely unready in another. A store may have structured product data, but no agent-safe cart. Another may support tokenized payment, but no machine-readable return policy.

## Stripe's five-level model

Stripe's 2025 annual letter describes five levels of agentic commerce, moving from simple form filling to anticipated purchases. The useful version for merchants is:

| Level | Autonomy pattern | What the human does | What the agent does |
|---|---|---|---|
| 1 | Form completion | Chooses what to buy | Fills payment and shipping details |
| 2 | Descriptive search | Describes a situation | Finds and explains options |
| 3 | Persistent preference | Chooses from personalized options | Remembers constraints and preferences |
| 4 | Delegated buying | Sets budget and rules | Searches, evaluates, and buys |
| 5 | Anticipation | Reviews or receives outcome | Predicts need and purchases without a prompt |

Stripe also notes that the industry is still near the boundary of Levels 1 and 2 overall. That is a useful baseline, but it hides a key detail: discovery is moving faster than payment.

## The lifecycle heatmap

The better way to assess agentic commerce is by lifecycle stage. This table is an editorial maturity estimate based on current protocol capabilities and public product announcements, not a universal measurement for every merchant.

| Lifecycle stage | Current autonomy | Why |
|---|---:|---|
| Discovery | Level 2 to 3 | AI systems already compare products, attributes, reviews, and preferences |
| Referral and attribution | Level 1 to 2 | Links can carry context, but standards for agent-origin attribution are still early |
| Intent | Level 1 | AP2-style mandates formalize user intent, but broad live adoption is still developing |
| Delegation | Level 1 | Identity and authorization protocols exist, but end-to-end merchant support is uneven |
| Policy | Level 1 | Merchants are starting to define what agents may do, often outside shared standards |
| Cart | Level 1 to 2 | UCP now includes cart-building capabilities, but merchant-owned checkout still matters |
| Payment | Level 1 | Most flows still keep the human close to the final purchase decision |
| Fulfillment and loyalty | Level 1 | UCP supports order events and identity linking, but autonomous post-purchase flows are early |

The [delegation economy framework](/docs/delegation-economy-agent-autonomy/) explains the autonomy spectrum. This page applies that spectrum to commerce operations.

## What changed in 2026

Several developments make this topic urgent:

- Google launched the [Universal Commerce Protocol](https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/) as an open standard for agentic commerce across discovery, buying, and post-purchase support.
- UCP documentation describes commerce lifecycle capabilities such as catalog lookup, cart building, identity linking, checkout, and order management.
- Google introduced [Universal Cart](https://blog.google/products-and-platforms/products/shopping/google-shopping-cart/) as a shopping hub across Google surfaces.
- AP2 documentation describes verifiable digital credentials, checkout mandates, payment mandates, and audit trails for agent payments.
- The FIDO Alliance formed an Agentic Authentication Technical Working Group to work on trusted AI-agent interactions and commerce.
- Mastercard describes Verifiable Intent as a trust layer aligned with AP2 and UCP.

Taken together, these moves show that agentic commerce is moving from discovery into infrastructure. The system is still fragmented, but the pieces are becoming more concrete.

## Level 1: AI-assisted commerce

At Level 1, the human still chooses. The agent removes friction.

Examples:

- filling shipping and payment details
- comparing product specs
- summarizing reviews
- surfacing return policies
- explaining product differences

For merchants, Level 1 requires strong [AI search optimization](/docs/ai-search-optimization/), structured product data, accurate availability, and pages that agents can parse.

## Level 2: Agent-researched commerce

At Level 2, the agent researches and narrows the market. The human still approves the final decision.

This is where many AI shopping experiences sit today. The agent can compare many SKUs, summarize tradeoffs, and recommend a shortlist. The merchant's job shifts from persuading a visitor inside a funnel to being machine-readable before the visitor arrives.

Required merchant assets:

- product schema
- current inventory
- clear variants
- price and shipping rules
- return policy
- compatibility data
- reviews and trust signals

The [product structured data guide](/docs/product-structured-data-ai-shopping/) covers the product-data layer.

## Level 3: Delegated task commerce

At Level 3, the human delegates a bounded task:

"Buy replacement coffee beans under 20 dollars."

The agent can act if the purchase fits the user's constraints. This requires intent, authorization, spend limits, merchant eligibility, and a clear success state.

Protocols start to matter here. [AP2 vs x402](/docs/ap2-vs-x402/) explains how authorization and payment protocols differ. [UCP vs ACP vs MCP](/docs/ucp-vs-acp-vs-mcp/) shows why commerce, checkout, and context standards do not solve the same problem.

## Level 4: Policy-governed autonomous commerce

At Level 4, agents manage complex buying tasks within policy. This is more likely to appear first in B2B procurement, subscriptions, replenishment, travel rules, and controlled categories than in emotional consumer purchases.

Examples:

- replenishing approved inventory
- renewing software seats within budget
- booking travel inside company policy
- selecting suppliers from an approved vendor list
- reordering consumables based on usage

The merchant now needs machine-readable policies, identity checks, deterministic cart logic, and reliable post-purchase status. This is where the [execution layer](/docs/execution-layer/) becomes a business requirement.

## Level 5: Anticipatory commerce

At Level 5, the agent buys before the user explicitly asks because it knows the need, budget, timing, and allowed vendors.

This is still the most speculative level. It needs:

- persistent agent identity
- delegated authority
- secure credentials
- liability rules
- dispute evidence
- audit trails
- merchant policy support
- safe cancellation and refund paths

Without those controls, Level 5 is not commerce infrastructure. It is risk.

## What merchants should build now

| Priority | Why it matters |
|---|---|
| Clean product and offer data | Agents need facts before they can compare |
| llms.txt and sitemap hygiene | Discovery systems need entry points |
| Policy pages in machine-readable form | Agents need constraints, not vague prose |
| Real-time catalog and inventory | Agents cannot rely on stale product data |
| Cart and checkout compatibility | Autonomous flows need stable transaction states |
| Identity and authorization planning | Delegation requires proof of who authorized what |
| Post-purchase event visibility | Agents need delivery, refund, and support status |

The [agentic commerce execution guide](/docs/agentic-commerce-execution/) goes deeper into the transaction layer, while [Universal Commerce Protocol](/docs/universal-commerce-protocol/) explains UCP's role.

## What is still unsolved

The hard problems are not only technical.

| Gap | Why it blocks higher autonomy |
|---|---|
| Cross-protocol identity | Agent, user, wallet, merchant, and PSP may all see different parts of the flow |
| Liability | Mistaken purchases need clear responsibility |
| Chargebacks and evidence | Networks and merchants need a reliable transaction record |
| Merchant policy | Stores need to decide which agents may buy, when, and under what terms |
| Attribution | Merchants need to know which agent surface created demand |
| User trust | People need boundaries, review rights, and revocation |

FIDO's 2026 work is important because authentication and delegated authority are becoming commerce infrastructure, not just login infrastructure.

## FAQ

### What are the five levels of agentic commerce?

They move from agent-assisted form completion to descriptive search, persistent preference, delegated buying, and anticipatory purchases. The higher the level, the more authority moves from human clicks to agent action.

### Why is the lifecycle model better than one score?

Because each stage matures at a different speed. Discovery can be Level 3 while payment is still Level 1. A merchant should not assume readiness in one stage means readiness everywhere.

### Is agentic commerce mostly about payments?

No. Payments are one stage. Discovery, intent, authorization, policy, cart, fulfillment, refunds, and loyalty all need to become agent-compatible.

### Which protocols matter most?

UCP addresses commerce interoperability across the journey. AP2 focuses on secure payment authorization and mandates. MCP and A2A support agent context and agent-to-agent coordination. Card-network and identity work adds trust and accountability.

### What should ecommerce teams do first?

Start with structured product data, clear policies, crawlable pages, llms.txt, reliable inventory, and clean checkout states. Those foundations help now, even before fully autonomous checkout is common.

## Sources

Primary and reference sources: [Stripe 2025 annual letter](https://assets.stripeassets.com/fzn2n1nzq965/IpU9Th5UvfMD586WbQ5om/6526df9ce888411cf12f843328386698/Stripe-annual-letter-2025-mobile.pdf), [Google UCP announcement](https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/), [Google Universal Cart announcement](https://blog.google/products-and-platforms/products/shopping/google-shopping-cart/), [UCP documentation](https://ucp.dev/), [AP2 documentation](https://ap2-protocol.org/), [FIDO Agentic Authentication Working Group announcement](https://fidoalliance.org/fido-alliance-to-develop-standards-for-trusted-ai-agent-interactions/), and [Mastercard Verifiable Intent](https://www.mastercard.com/europe/en/news-and-trends/stories/2026/verifiable-intent.html).
