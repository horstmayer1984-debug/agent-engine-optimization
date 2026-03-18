---
title: "The Execution Layer"
date: 2026-03-09
weight: 3
category: "Deep Dive"
---

When an AI system cites your content in a generated answer, that is the read layer working. Useful, but passive.

When an AI agent uses your API to check real-time inventory, matches it against a user's budget constraints, and completes a purchase — that is the execution layer. Active, transactional, and fundamentally different in what it requires from your infrastructure.

The execution layer is where AEO separates from everything that came before it. It is not a content optimization problem. It is an **infrastructure architecture problem**.

---

## What agents need to act

An autonomous agent completing a task — booking a hotel room under 150 euros in Barcelona for next Tuesday — needs:

### 1. Discovery

Find services that match the task type. This is partly a read-layer problem. Structured data, schema markup, and proper indexing help agents discover your service. But discovery alone does not enable action.

### 2. Capability understanding

Know what your service can do and under what constraints. The agent needs a machine-readable description of your capabilities: what actions are available, what parameters they accept, what outputs they return, what constraints apply. This is what capability manifests and MCP tool descriptions provide.

### 3. Real-time data access

Get current pricing, availability, and conditions. Static HTML pages with yesterday's prices do not work. The agent needs an endpoint that returns current, structured data it can programmatically evaluate.

### 4. Constraint matching

Evaluate whether your offering fits the user's requirements. Budget under 150 euros? Available on Tuesday? In Barcelona? Includes breakfast? The agent needs to match these constraints against your data. This requires deterministic, structured data — not marketing copy.

### 5. Action execution

Trigger the booking, purchase, or request. The agent needs a transaction endpoint. This is where protocols like UCP (for commerce) and MCP (for general tool access) come in.

### 6. State verification

Confirm that the action succeeded. Did the booking go through? The agent needs observable state transitions: available, reserved, confirmed. Without verification, the agent cannot report back reliably.

---

## The building blocks

### Action Schemas

Schema.org defines action types like BuyAction, ReserveAction, OrderAction. These tell agents what actions are possible on a page or through a service. Most websites use Schema.org for informational markup only. Extending it to action-level markup is a first step that requires no API backend.

### Capability Manifests

A machine-readable document that describes what a service can do, what protocols it supports, and how to interact with it. Think of it as a robots.txt for agent capabilities — except instead of saying what you may crawl, it says what you can do.

### Deterministic Inputs and Outputs

Marketing pages are designed for human persuasion. Agent-facing data must be designed for machine decision-making: fixed parameters, structured response formats, unambiguous values, machine-readable error codes.

What the website says:

> "Our premium plan starts at just $49/month with all the features your team needs."

What the agent needs:

```json
{
  "plan": "premium",
  "price": { "amount": 49, "currency": "USD", "interval": "month" },
  "features": ["feature_a", "feature_b", "feature_c"],
  "limits": { "users": 50, "storage_gb": 100 },
  "trial": { "available": true, "days": 14 }
}
```

### Protocol Compatibility

**MCP (Model Context Protocol)** — enables AI models to access external tools and data through a standardized interface. A merchant with an MCP server lets any MCP-compatible agent query their catalog without custom integration.

**UCP (Universal Commerce Protocol)** — standardizes the entire shopping journey so any agent can transact with any merchant using the same protocol.

**A2A (Agent-to-Agent)** — enables agents to delegate tasks to specialized agents.

Organizations that implement these protocols early become the default options for agent task completion.

### State Transitions

Agents need to verify that actions produce expected results. This requires observable state transitions:

`available > reserved > payment_pending > confirmed > fulfilled`

Each transition should be queryable. Without this, agents cannot reliably manage multi-step workflows.

### Trust and Verification

An agent booking a 2,000 euro trip needs to trust the source. Trust signals for agents are different from trust signals for humans. Agents need verifiable business identities, cryptographically signed transaction receipts (AP2), consistent and accurate data across touchpoints, transparent constraint documentation, and audit trails.

---

## What this means for your organization

The execution layer is not something you build overnight. It is a capability you develop incrementally:

**Phase 1 (now):** Audit your current agent readiness. Assess structured data, schema coverage, content structure, and existing API surface.

**Phase 2 (3 to 6 months):** Implement read-layer optimizations and begin planning execution-layer infrastructure. Add action schemas, create capability documentation, assess protocol compatibility.

**Phase 3 (6 to 18 months):** Build execution-layer capabilities. Expose APIs, implement protocol compatibility, create agent-facing data endpoints, develop state verification mechanisms.

[AEO Readiness Audit](/docs/audit/) — start with a systematic assessment.

[What is AEO?](/docs/what-is-aeo/) — full definition and scope.
