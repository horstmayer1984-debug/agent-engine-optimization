---
title: "Agentic Commerce Protocol (ACP): What Merchants Need to Know"
date: 2026-05-17
weight: 133
category: "Architecture"
description: "Learn what the Agentic Commerce Protocol is, where ACP fits in AI checkout, and how merchants should compare it with broader commerce protocols."
summary: "A practical ACP guide for merchants, covering in-context selling, AI checkout, payment scope, and how ACP differs from UCP and MCP."
keywords:
  - Agentic Commerce Protocol
  - ACP protocol
  - AI checkout
  - agentic commerce
  - ChatGPT checkout
---

# Agentic Commerce Protocol (ACP): What Merchants Need to Know

The Agentic Commerce Protocol is the protocol layer Stripe documents for enabling in-context selling on AI agents. In practical terms, ACP is about checkout inside an agent experience: a user discovers a product in an AI surface, keeps the purchase flow in context, and the merchant connects to that flow without rebuilding the whole storefront around a human browser session.

## What official docs say

Stripe's agentic commerce documentation tells businesses to enable in-context selling on AI agents using the Agentic Commerce Protocol. Stripe's launch announcement also describes ACP as an open standard codeveloped with OpenAI. That places ACP squarely in the transaction experience layer rather than the full search, product-data, or multi-agent orchestration stack.

Primary sources:

- [Stripe docs: Agentic commerce](https://docs.stripe.com/agentic-commerce)
- [Stripe newsroom: Instant Checkout and ACP](https://stripe.com/newsroom/news/stripe-openai-instant-checkout)

## ACP compared with nearby protocols

| Protocol | Main job |
|---|---|
| ACP | In-context checkout for AI-agent experiences |
| UCP | Broader commerce lifecycle and capability negotiation |
| MCP | Tool and data access for agents |
| x402 | Machine payment flow for HTTP resources |

The [UCP vs ACP vs MCP guide](/docs/ucp-vs-acp-vs-mcp/) covers the broader comparison. ACP is best understood as a focused commerce-experience protocol, not a replacement for every other part of an agent-ready stack.

## When ACP matters

ACP becomes relevant when:

- buyers discover products inside AI conversations
- merchants want checkout to happen without a clumsy redirect path
- the AI surface is becoming a real sales channel
- the merchant already has product data, pricing, and policy information clean enough for automated buying

That last point is easy to underestimate. Checkout does not rescue bad product data. The [ChatGPT product recommendations SEO checklist](/docs/chatgpt-product-recommendations-seo/) explains what needs to happen before selection.

## What merchants should prepare first

| Readiness area | Why it matters |
|---|---|
| Product data | Agents need facts before they recommend or buy |
| Price and availability | Stale data breaks trust immediately |
| Returns and shipping | Buyer constraints often include both |
| Fraud controls | Agent-driven orders still need risk handling |
| Order confirmation | The result must be deterministic and auditable |

ACP may reduce friction at checkout, but the [execution layer](/docs/execution-layer/) still needs reliable backend state transitions.

## ACP vs traditional ecommerce checkout

| Traditional checkout | ACP-style flow |
|---|---|
| Buyer navigates storefront | Buyer may stay in the AI interface |
| Session and UI dominate | Protocol and structured state dominate |
| Conversion depends on page flow | Conversion depends on context plus data quality |
| Human reads all details | Agent may pre-filter options |

This is why old checkout analytics alone are not enough. Merchants need to track discovery, recommendation, handoff, checkout completion, and post-purchase correctness as one chain.

## Risks and limits

Do not treat any protocol as automatic revenue. ACP depends on:

- platform adoption
- merchant integration quality
- user trust
- correct product information
- checkout policies that still make sense when an agent acts for a buyer

For regulated products or high-consideration purchases, human confirmation may remain necessary even if the checkout surface becomes agent-native.

## FAQ

### Is ACP the same thing as agentic commerce?

No. Agentic commerce is the broader market shift. ACP is one protocol approach for in-context selling on AI agents.

### Does ACP replace UCP?

No. ACP is focused on checkout experience, while UCP covers a wider commerce lifecycle.

### Should every merchant implement ACP now?

Not automatically. First confirm that AI-assisted shopping is a meaningful channel for your category and that your data foundation is ready.

### What is the best first step?

Fix product data, product schema, policy clarity, and checkout determinism before adding new protocol surfaces.

## Bottom line

ACP matters because checkout is moving closer to the conversation. Merchants that want to sell through AI surfaces need more than good copy: they need clean product facts, reliable operations, and checkout flows built for machine mediation.
