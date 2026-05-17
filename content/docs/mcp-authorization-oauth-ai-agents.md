---
title: "MCP Authorization: OAuth for AI Agents"
metaTitle: "MCP Authorization for AI Agents: OAuth Guide"
date: 2026-05-17
weight: 114
category: "Architecture"
description: "MCP authorization defines how AI agents access restricted tools over HTTP. Learn OAuth, protected resource metadata, and AEO implications."
summary: "A practical guide to MCP authorization for AI agents, covering OAuth flows, protected resource metadata, client registration, scopes, and AEO readiness."
keywords:
  - MCP authorization
  - MCP OAuth
  - AI agent authorization
  - protected resource metadata
  - agent access control
---

# MCP Authorization: OAuth for AI Agents

MCP authorization matters because agent tools often need restricted access. Public tools can be discovered freely, but real workflows need identity, consent, scopes, and audit trails. The MCP authorization specification explains how HTTP-based MCP transports can use OAuth-style authorization for restricted MCP servers.

## What the MCP spec says

The Model Context Protocol authorization specification defines authorization capabilities at the transport level for HTTP-based transports. The current specification references OAuth, protected resource metadata, dynamic client registration, and security requirements.

Primary sources:

- [MCP authorization specification](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [MCP 2026 roadmap](https://modelcontextprotocol.io/development/roadmap)
- [MCP vs API guide on this site](/docs/mcp-vs-api-for-agents/)

## Why authorization is an AEO issue

The [execution layer](/docs/execution-layer/) is not useful if every action is public or every action requires a human to manually copy credentials. Agents need controlled access.

Examples:

- a procurement agent checks contract pricing
- a support agent reads ticket status
- a travel agent modifies a booking
- a finance agent retrieves invoices
- a developer agent opens a deployment tool

Each workflow needs a clear answer: who is the agent acting for, what may it do, how long does access last, and how can access be revoked?

## Public MCP vs restricted MCP

| MCP server type | Example | Authorization need |
|---|---|---|
| Public read-only | Product catalog, docs search, public pricing | Usually none |
| Public action | Newsletter signup, public quote request | Low-friction anti-abuse controls |
| User-scoped read | Account data, order status | OAuth and user consent |
| User-scoped write | Booking, payment, cancellation | Strong scopes, confirmation, audit logs |
| Admin tool | Deployment, billing settings | Human approval and strict policy |

Most businesses should start with public read-only or low-risk public actions before exposing user-scoped tools.

## Key authorization concepts

| Concept | Meaning for agents |
|---|---|
| Resource owner | The user or organization the agent acts for |
| MCP client | The agent client requesting access |
| Authorization server | The system that grants tokens |
| Protected resource metadata | Machine-readable information about authorization servers |
| Scope | Specific permission such as read orders or create booking |
| Access token | Credential used for the MCP request |

These concepts are not new, but agents make them more important because the actor is no longer always a human in a browser.

## Implementation checklist

1. Classify MCP tools by risk.
2. Keep public discovery tools separate from restricted tools.
3. Define scopes by action, not by broad product area.
4. Publish authorization metadata where clients can discover it.
5. Use short-lived tokens for higher-risk actions.
6. Log agent identity, user identity, tool name, input summary, and result status.
7. Add human confirmation for irreversible or expensive actions.

The [agent observability and guardrails guide](/docs/agent-observability-guardrails/) expands this into operational monitoring.

## Example scope design

| Bad scope | Better scopes |
|---|---|
| `account_access` | `orders.read`, `orders.cancel`, `invoices.read` |
| `booking` | `availability.read`, `booking.create`, `booking.cancel` |
| `admin` | `users.invite`, `billing.read`, `settings.update` |

Agents work better when scopes are explicit. Security teams work better when scopes map to business actions.

## AEO documentation requirements

If your site offers restricted MCP tools, your public documentation should explain:

- what tools exist
- which tools are public
- which require authorization
- what scopes are requested
- whether a human confirmation step is required
- how logs and revocation work

Add links to those docs from [llms.txt](/docs/programming-llms-txt/) so agents can discover the access model before trying to call tools.

## Common mistakes

| Mistake | Why it fails |
|---|---|
| One broad token for all tools | Too much agency and weak auditability |
| No public capability documentation | Agents cannot plan access |
| Long-lived tokens for write actions | Higher damage if compromised |
| No revocation path | Users cannot stop delegated access |
| Treating agent identity as user identity | Blurs accountability |

## FAQ

### Does every MCP server need OAuth?

No. Public read-only servers may not need authorization. Restricted or user-scoped tools usually do.

### Is MCP authorization production-ready?

The specification exists and is evolving. Teams should follow the current version and verify client/server compatibility before production use.

### What is protected resource metadata?

It is metadata that helps MCP clients identify the authorization servers associated with a protected resource.

### How does this affect AEO?

Agents are more likely to use services that clearly describe available tools, permissions, and access flows.

### Should agents get admin access?

Only in tightly controlled internal environments with strong logging, approval, and revocation.
