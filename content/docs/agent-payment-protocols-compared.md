---
title: "Agent Payment Protocols Compared: x402, ACP, MPP, AP2, TAP, Agent Pay"
metaTitle: "Agent Payment Protocols Compared"
date: 2026-05-08
weight: 118
category: "Architecture"
description: "A practical comparison of x402, ACP, MPP, AP2, Visa TAP, Mastercard Agent Pay, UCP, and Nevermined for AI agent payments."
summary: "Comparison guide for agent payment protocols in 2026, covering settlement, checkout, authorization, cards, sessions, and agent infrastructure."
keywords:
  - agent payment protocols
  - x402 vs ACP vs MPP
  - AP2 agent payments
  - AI agent payments
  - agentic commerce protocols
---

# Agent Payment Protocols Compared: x402, ACP, MPP, AP2, TAP, Agent Pay

Agent payment protocols are splitting into three layers in 2026: settlement, commerce orchestration, and trust. x402 is strongest for lightweight HTTP payments and stablecoin settlement. ACP and UCP cover the shopping journey. MPP targets recurring machine payments. AP2, Visa TAP, and Mastercard Agent Pay focus on authorization, identity, and card network trust.

This matters for Agent Engine Optimization because payments are no longer just a checkout detail. If an AI agent can discover your offer but cannot pay, authorize, or verify the transaction, your site is visible but not executable.

## Quick comparison

| Protocol or system | Main backers | Best fit | Payment focus | Typical role in the stack |
|---|---|---|---|---|
| x402 | Coinbase, Cloudflare, Stripe, Linux Foundation ecosystem | Pay per request APIs and agent services | HTTP 402 settlement, often stablecoins | Settlement layer |
| ACP | OpenAI and Stripe | In context checkout through AI agents | Merchant checkout and shared payment tokens | Commerce flow |
| MPP | Stripe and Tempo | Ongoing machine payments and API usage | Sessions, streaming, usage based billing | Machine payment layer |
| AP2 | Google and payments partners | Proving user intent and authorization | Cryptographic mandates and trust | Authorization layer |
| UCP | Google and commerce partners | Agentic shopping journeys | Discovery, catalog, checkout, post purchase | Commerce protocol layer |
| Visa TAP | Visa ecosystem | Merchant trust in AI agents | Agent identity and credential signals | Trust and card rail bridge |
| Mastercard Agent Pay | Mastercard | Card based agent transactions | Tokenized agentic payments | Card network layer |
| Nevermined | Nevermined | Monetizing agent APIs, MCP tools, protected assets | Plans, entitlements, x402, card and stablecoin flows | Infrastructure platform |

## What changed by May 2026?

The market no longer has one obvious payment standard. It has a stack.

x402 moved from crypto native experiment to broader infrastructure after the Linux Foundation announced the x402 Foundation with Coinbase contributing the protocol. Stripe published Machine Payments documentation and introduced MPP with Tempo. OpenAI and Stripe made ACP the commerce layer behind Instant Checkout. Google pushed AP2 as an authorization protocol and later moved AP2 toward standards governance through the FIDO Alliance. Visa and Mastercard brought card network trust models into the agent payment conversation.

The practical takeaway is simple: merchants should not ask, "Which single protocol wins?" They should ask, "Which layer does this protocol solve?"

## Settlement layer: x402

x402 revives the HTTP 402 Payment Required pattern for agent and API payments. A client requests a protected resource, the server returns payment requirements, the client attaches payment proof, and the server grants access after verification.

x402 is strong when the product is small, digital, API based, or priced per request. A weather endpoint, premium data feed, MCP tool, inference call, or machine readable report can charge per invocation without account creation.

Its limitation is also clear. x402 settles value. It does not solve the whole shopping journey by itself. A merchant still needs product discovery, policy disclosure, fraud controls, refunds, identity, tax, support, and dispute handling.

Read the site guide: [x402 Agent Payments](/docs/x402-agent-payments/).

## Commerce layer: ACP and UCP

ACP and UCP sit closer to the shopping journey than x402.

ACP, developed by OpenAI and Stripe, is designed around agent initiated checkout. Stripe describes agentic commerce as a way for buyers, agents, and businesses to transact securely, with shared payment tokens and catalog handling in the flow.

UCP is broader. It is positioned as a common commerce language for agentic shopping across discovery, catalog interaction, checkout, and post purchase support. That makes it less like a payment rail and more like a commerce protocol surface.

For ecommerce teams, ACP and UCP are more relevant than x402 when the problem is a normal retail purchase rather than a paid API request.

## Machine payment layer: MPP

MPP, co authored by Stripe and Tempo, is aimed at agents paying businesses and other agents without a human in the loop. Its strongest use case is not one isolated payment. It is recurring, ongoing, or metered activity.

That maps well to autonomous systems. Agents do not always know their exact number of future calls. They may need a budget, a time window, a rate limit, and reconciliation after the work is done.

If x402 is clean for one request, MPP is interesting for a run of requests.

## Authorization layer: AP2

AP2 is Google’s answer to the trust problem: how does a merchant know that a user authorized the agent to buy this item under these conditions?

Google describes AP2 as an open protocol for securely initiating and transacting agent led payments across platforms. Its core concept is the mandate: cryptographically verifiable evidence that captures user intent, cart details, and payment authorization.

AP2 is less about the payment rail and more about accountability. It can work with cards, wallets, and crypto settlement rails. That makes it complementary to x402 rather than a pure replacement.

## Card network layer: Visa TAP and Mastercard Agent Pay

Visa TAP and Mastercard Agent Pay solve a different problem: how existing card networks adapt to agent initiated commerce.

Visa TAP gives merchants a way to distinguish legitimate AI agents from suspicious automated traffic and to pass credential and agent context through the commerce flow. Mastercard Agent Pay uses tokenization concepts already used in card commerce and applies them to agentic payments.

These systems matter because many merchants will not begin with stablecoins. They will begin with cards, existing processors, tokenized credentials, and fraud systems they already trust.

## Platform layer: Nevermined

Nevermined is not just a protocol. It is infrastructure for paid access to agent APIs, MCP tools, and protected assets. Its documentation describes support for x402 flows, Stripe checkout, stablecoins, plans, and entitlement checks.

That makes Nevermined relevant for teams that want a practical agent payment layer without building every component themselves.

## Which protocol should a business choose?

| Business type | First protocol to evaluate | Why |
|---|---|---|
| Paid API or data provider | x402 or MPP | Per request and metered usage are natural fits |
| Ecommerce merchant | ACP or UCP | Product discovery and checkout matter more than raw settlement |
| Enterprise procurement workflow | AP2 plus existing payment rails | Authorization and auditability are central |
| Card heavy retailer | Visa TAP or Mastercard Agent Pay | Existing card networks remain the operating base |
| MCP tool provider | x402, MPP, or Nevermined | Tools need paid access, entitlement, and retry safe flows |

## AEO implications

For AEO, the winning pattern is a hybrid stack.

A site should publish machine readable product or service data, expose deterministic action paths, document payment and authorization requirements, and make the result verifiable. Payment protocols only help after the agent can understand what the site offers and which action is safe to take.

Internal next steps: read [AI Agent Protocols](/docs/protocols/), [Execution Layer](/docs/execution-layer/), and [x402 MCP A2A Full Stack](/docs/x402-mcp-a2a-full-stack/).

## FAQ

**What is the best agent payment protocol in 2026?**
There is no single best protocol. x402 is strongest for lightweight HTTP settlement, ACP and UCP are stronger for commerce flows, MPP fits ongoing machine payments, and AP2 focuses on authorization and trust.

**Is x402 better than ACP?**
x402 and ACP solve different layers. x402 handles payment settlement over HTTP. ACP handles agent initiated checkout and merchant integration.

**Is AP2 a payment rail?**
AP2 is better understood as an authorization and trust protocol. It can support different payment methods and settlement rails.

**Will Visa and Mastercard compete with x402?**
They compete in some use cases, but they also solve different adoption problems. Card networks help existing merchants support agent payments without moving first to crypto native rails.

**What should merchants implement first?**
Most merchants should start with structured product data, clear policies, and agent readable checkout requirements. Protocol choice should follow the business model.

## Sources

Primary sources used for this article include [Linux Foundation on the x402 Foundation](https://www.linuxfoundation.org/press/linux-foundation-is-launching-the-x402-foundation-and-welcoming-the-contribution-of-the-x402-protocol), [x402 documentation](https://docs.x402.org/faq), [Stripe on ACP](https://stripe.com/newsroom/news/stripe-openai-instant-checkout), [Stripe Machine Payments](https://docs.stripe.com/payments/machine), [Stripe MPP announcement](https://stripe.com/blog/machine-payments-protocol), [Google Cloud AP2 announcement](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol/), [Google AP2 FIDO update](https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/), [UCP documentation](https://ucp.dev/), [Visa TAP developer page](https://developer.visa.com/capabilities/trusted-agent-protocol/overview), [Mastercard Agent Pay announcement](https://www.mastercard.com/news/press/2025/april/mastercard-unveils-agent-pay-pioneering-agentic-payments-technology-to-power-commerce-in-the-age-of-ai/), and [Nevermined documentation](https://nevermined.ai/docs/getting-started/how-it-works).
