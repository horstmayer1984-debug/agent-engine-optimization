---
title: "x402 vs ACP vs MPP: Payment Layer, Checkout Layer, Machine Payment Layer"
date: 2026-05-08
weight: 119
category: "Architecture"
description: "Compare x402, ACP, and MPP for AI agent payments, including HTTP micropayments, agent checkout, sessions, streaming, fiat, and stablecoins."
summary: "A practical guide to the differences between x402, ACP, and MPP for agentic commerce and machine payments."
keywords:
  - x402 vs ACP vs MPP
  - Machine Payments Protocol
  - Agentic Commerce Protocol
  - AI agent micropayments
---

# x402 vs ACP vs MPP: Payment Layer, Checkout Layer, Machine Payment Layer

x402, ACP, and MPP are often discussed as competitors, but they solve different payment problems. x402 is a lightweight settlement pattern for HTTP resources. ACP is a commerce checkout protocol for agent initiated purchases. MPP is a machine payment standard for sessions, metered usage, and ongoing agent activity.

The simplest way to compare them is by asking what the agent is buying.

If the agent buys one API response, x402 fits. If the agent buys a product from a merchant, ACP fits. If the agent pays repeatedly during an ongoing task, MPP becomes more interesting.

## Core difference

| Question | x402 | ACP | MPP |
|---|---|---|---|
| What is being solved? | Payment for protected HTTP resources | Agent initiated checkout | Machine payments over time |
| Primary buyer pattern | API client or agent | Shopping agent acting for a user | Agent, service, or machine workflow |
| Best unit of value | One request or one resource | One order or cart | Session, stream, subscription, metered usage |
| Payment model | Commonly stablecoin settlement | Merchant checkout and payment credentials | Fiat or crypto through machine payment sessions |
| Best example | Pay 0.01 USDC for an API call | Buy a product inside an AI assistant | Pay continuously for API usage |

## What x402 does well

x402 is attractive because it keeps the protocol close to the web. A server can respond with HTTP 402 Payment Required, specify the price and payment requirements, then verify payment before serving the resource.

For agent workflows, this is powerful. It removes account setup, subscription negotiation, and API key provisioning from small digital transactions.

Good x402 use cases include:

1. Paid MCP tools
2. Premium data endpoints
3. Per request inference
4. Machine readable reports
5. Agent accessible content paywalls
6. API calls where the price is known before execution

The weakness is not technical elegance. The weakness is scope. x402 does not describe the whole retail journey, cart state, returns, taxes, fulfillment, or customer support.

## What ACP does well

ACP is built for agentic commerce. OpenAI and Stripe developed it for cases where an AI assistant helps a user discover, evaluate, and buy from a merchant.

Stripe’s agentic commerce documentation points to shared payment tokens, product catalog handling, and in context selling. That is a different problem from x402. A retail purchase is not just a payment. It includes inventory, variants, shipping, tax, merchant of record questions, order confirmation, cancellation, and returns.

ACP is strongest when the agent is operating inside a consumer buying flow.

## What MPP does well

MPP, introduced by Stripe and Tempo, is built for machine payments where the agent does not just make one call. It may operate under a session, keep using a resource, or pay repeatedly as work continues.

That maps well to autonomous systems. Agents do not always know their exact number of future calls. They may need a budget, a time window, a rate limit, and reconciliation after the work is done.

MPP is a better conceptual fit for:

1. Ongoing API usage
2. Agent subscriptions
3. Usage based billing
4. Streaming machine payments
5. A delegated budget for an autonomous workflow

## How the three can work together

A realistic stack can use more than one protocol.

An AI agent might discover a merchant through a commerce surface, use ACP for checkout, rely on AP2 or card network controls for authorization, and pay a separate data provider through x402 or MPP during the research step.

In a developer workflow, an agent might call paid MCP tools through x402 for isolated requests, then switch to MPP for a long running data task with repeated usage.

The important design rule is separation of concerns.

## Which one should developers implement first?

| You operate | Start with | Reason |
|---|---|---|
| A paid API | x402 | The endpoint can price and verify each request |
| A SaaS API with recurring usage | MPP | Sessions and usage based billing matter |
| An ecommerce store | ACP | The checkout journey is the real problem |
| A data marketplace | x402 and MPP | Some assets are one time purchases, others are metered |
| An AI agent platform | ACP, MPP, and x402 | Different sellers will require different payment modes |

## AEO implementation notes

For AEO, protocol support should be visible before payment is attempted.

Add a machine readable page or endpoint that states:

1. Supported payment protocols
2. Accepted currencies or rails
3. Minimum and maximum charge size
4. Refund or reversal policy
5. Authentication requirements
6. Error codes
7. Idempotency rules
8. Contact or dispute path

This turns payment from a hidden checkout event into an agent readable capability.

## FAQ

**Is MPP replacing x402?**
Not directly. MPP is better for sessions and ongoing usage. x402 remains cleaner for simple request level settlement.

**Is ACP only for ChatGPT?**
ACP was built with OpenAI and Stripe for agentic commerce, but the protocol is positioned as an open commerce standard rather than a ChatGPT only feature.

**Can a merchant use x402 and ACP together?**
Yes. A merchant could use ACP for checkout and x402 for paid API access, premium data, or agent services.

**Which protocol is best for stablecoin micropayments?**
x402 is the clearest fit for lightweight stablecoin micropayments over HTTP. Stripe Machine Payments also supports machine payments with crypto settlement into Stripe infrastructure.

## Sources

Primary references: [x402 documentation](https://docs.x402.org/faq), [Linux Foundation x402 Foundation announcement](https://www.linuxfoundation.org/press/linux-foundation-is-launching-the-x402-foundation-and-welcoming-the-contribution-of-the-x402-protocol), [Stripe ACP announcement](https://stripe.com/newsroom/news/stripe-openai-instant-checkout), [Stripe agentic commerce documentation](https://docs.stripe.com/agentic-commerce), [Stripe Machine Payments documentation](https://docs.stripe.com/payments/machine), and [Stripe MPP announcement](https://stripe.com/blog/machine-payments-protocol).
