---
title: "How to Implement x402 on Your Website or API for Agent Payments"
date: 2026-04-12
weight: 71
category: "Architecture"
description: "Step-by-step guide to adding x402 payment middleware to your website or API. Covers the 402 response format, payment validation, integration with llms.txt and Agent Cards."
summary: "x402 makes your API instantly agent-monetizable. When an agent requests content or compute, your server returns 402, the agent pays with USDC, and access is granted. Here is the implementation guide."
keywords:
  - implement x402
  - x402 middleware
  - HTTP 402 implementation
  - agent payment API
  - x402 developer guide
  - USDC micropayments API
---

Implementing x402 makes your website or API instantly agent-monetizable. When an AI agent requests content or compute, your server returns HTTP 402 with structured payment terms. The agent pays with USDC. Access is granted. All in one stateless HTTP round trip.

## The implementation in five steps

### Step 1: Add middleware that checks for payment

Insert middleware before your protected endpoints. It checks for the X-PAYMENT header on incoming requests. If the header is present and valid, the request proceeds. If missing or insufficient, the middleware returns a 402 response.

This middleware sits between your web server and your business logic. It does not change how your endpoints work internally.

### Step 2: Structure the 402 response

When payment is missing, return a 402 status code with a JSON body containing: price (the amount required), currency (USDC), chain (the blockchain to pay on, Base is the default), payee (your wallet address), description (what the payment grants access to), and expiry (how long the payment terms remain valid).

The structured response is what allows agents to auto-pay. A plain 402 without this JSON body gives the agent nothing to work with.

### Step 3: Validate incoming payments

When an agent retries with an X-PAYMENT header, validate the payment on-chain. Use the Coinbase Developer Platform SDK or a direct RPC call to verify that the payment was made to the correct address for the correct amount on the correct chain.

Validation should complete within the request lifecycle. Do not make the agent wait for a separate confirmation flow.

### Step 4: Grant access and log the transaction

Once payment is validated, process the original request normally and return the response. Log the transaction: agent identifier, amount paid, endpoint accessed, response returned, timestamp.

These logs feed into your [feedback loops](/docs/agent-feedback-loops/) and revenue analytics.

### Step 5: Publish your x402 endpoints in discovery files

Add your paid endpoints to your llms.txt with pricing information. Include them in your agent-card.json capabilities list with the payment requirement noted. If you have an MCP server, add a payment_required field to the relevant tool descriptions.

This ensures agents discover not just what your site can do, but what it costs to use each capability.

## Combining x402 with card payments

Nevermined's agent card payments (launched April 9, 2026) enable agents to pay with delegated Visa or Mastercard authority while merchants receive settlement through standard payment processors like Stripe or Adyen.

This hybrid approach lets you accept both crypto micropayments (for agents with wallets) and traditional card payments (for agents with delegated card authority) through the same endpoint.

## Comparison: traditional API monetization vs x402

| Method | Setup time | Agent friction | Revenue model | Minimum viable payment |
|---|---|---|---|---|
| API keys with subscriptions | Days | High (account creation) | Monthly fees | Dollars per month |
| x402 | Hours | Zero | Pay per request | Fractions of a cent |

## Common mistakes

Returning a plain 402 without the structured JSON body. Agents cannot auto-pay if they do not receive structured payment terms. Always include the full JSON spec.

Not publishing x402 endpoints in discovery files. If agents do not know an endpoint requires payment before calling it, the 402 response feels like an error rather than a transaction opportunity.

Setting prices too high for micropayment use cases. The power of x402 is enabling payments that were previously too small to process. A data query that costs 5 dollars will get fewer agent calls than one that costs 0.01 dollars and scales on volume.

The [x402 overview](/docs/x402-agent-payments/) explains the strategic context. The [agent-ready web apps checklist](/docs/agent-ready-web-apps/) covers the broader developer setup.

---

## FAQ

**How long does x402 implementation take?**
Basic middleware for a single endpoint takes 1 to 2 hours. Adding payment validation and logging adds another 2 to 4 hours. Full integration with llms.txt and Agent Cards takes a day.

**Which programming languages have x402 middleware available?**
Node.js, Python, Go, and Cloudflare Workers have pre-built middleware. The protocol is simple enough to implement in any language that can return HTTP responses and make RPC calls.

**Do I need a crypto wallet?**
Yes, to receive payments. A simple USDC wallet on Base is sufficient. You can convert received USDC to fiat through any exchange or payment processor that supports stablecoin settlement.

**Can I set different prices for different endpoints?**
Yes. Each endpoint can return its own 402 response with different pricing. A simple data query might cost 0.001 dollars while a complex computation costs 1 dollar.

**What if an agent does not support x402?**
The agent receives a 402 response it cannot process and moves on. You can offer alternative access methods (API keys, subscriptions) for non-x402 clients while keeping x402 as the primary agent payment path.
