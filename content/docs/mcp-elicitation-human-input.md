---
title: "MCP Elicitation: Human Input for Safer Agent Workflows"
date: 2026-05-23
weight: 134
category: "Architecture"
description: "MCP Elicitation lets servers request structured user input through the client. Learn when it helps, what it must not ask for, and how to design safe agent workflows."
summary: "A practical guide to MCP Elicitation, structured user input, accept/decline/cancel flows, human-in-the-loop design, and AEO workflow implications."
keywords:
  - MCP Elicitation
  - elicitation/create
  - human in the loop agents
  - MCP user input
  - agent workflow safety
---

# MCP Elicitation: Human Input for Safer Agent Workflows

MCP Elicitation lets an MCP server request structured information from the user through the client while a workflow is running. It is useful when an agent needs missing details, but it should not be used for sensitive information. Good elicitation design makes agent workflows safer because users can accept, decline, or cancel requests instead of being pushed through hidden automation.

## What MCP Elicitation is

The official [MCP Elicitation specification](https://modelcontextprotocol.io/docs/concepts/elicitation) describes a standard way for servers to request additional user information through the client. Servers send an `elicitation/create` request with a message and a restricted JSON schema for the expected response.

The user can respond in three ways:

- accept with data
- decline
- cancel

That simple response model matters. It gives the client a clear way to keep the user in control.

For related architecture, read [MCP vs API for agents](/docs/mcp-vs-api-for-agents/), [agent UX and human-in-the-loop design](/docs/agent-ux-human-in-the-loop/), and [MCP Authorization with OAuth](/docs/mcp-authorization-oauth-ai-agents/).

## Why elicitation exists

Agents often start with incomplete instructions. A server may need one missing field before it can complete a task.

Examples:

- "Which project should this issue be assigned to?"
- "What date should the report cover?"
- "Which shipping address should be used?"
- "Which environment should the deployment target?"
- "Which approved vendor should the order use?"

Without a standard input flow, servers may invent inconsistent prompt patterns or ask the model to guess. Elicitation gives this interaction a structured path.

## Elicitation vs normal chat questions

| Feature | Normal chat question | MCP Elicitation |
|---|---|---|
| Request origin | Assistant or user | MCP server through client |
| Response format | Free text | Structured schema |
| User options | Usually reply or ignore | Accept, decline, cancel |
| Validation | Model-dependent | Client can validate fields |
| Security posture | Varies | Spec warns against sensitive data requests |

Elicitation is not just "ask the user a question." It is a standardized request for structured input inside an agent workflow.

## What servers should not request

The MCP spec says servers must not use elicitation to request sensitive information. In practice, avoid requesting:

- passwords
- private keys
- payment card numbers
- one-time passcodes
- raw access tokens
- confidential personal data
- secrets that belong in a secure vault

If a workflow needs sensitive authorization, use a proper auth flow, not elicitation. The [execution layer](/docs/execution-layer/) depends on trustworthy boundaries.

## Good use cases

| Use case | Good elicitation field | Bad elicitation field |
|---|---|---|
| Support triage | Priority level | Customer password |
| Deployment | Target environment | Cloud root key |
| Procurement | Approved vendor | Full card number |
| Content publishing | Article category | CMS admin password |
| Travel planning | Preferred airport | Passport scan |

The pattern is simple: elicit preferences and non-sensitive choices, not secrets.

## AEO implications

Elicitation is important for agent-readable businesses because not every action can be fully autonomous. Sometimes the best user experience is a clear pause:

"I can continue, but I need one approved choice."

Websites and APIs that prepare for this can publish:

- clear action requirements
- allowed parameter values
- confirmation rules
- escalation paths
- examples of valid inputs
- error messages agents can understand

This turns vague human forms into agent-compatible workflows. The [programming websites for AI agents](/docs/programming-websites-for-ai-agents/) guide covers more of that preparation work.

## Design checklist

1. Ask only for the minimum missing information.
2. Show which server is requesting the information.
3. Use labels users can understand.
4. Validate inputs before sending them.
5. Offer decline and cancel options.
6. Never request secrets through elicitation.
7. Log request type, server, and outcome.
8. Keep high-risk actions behind confirmation.

## FAQ

### Is MCP Elicitation a form?

It can generate form-like UI, but the protocol itself defines the structured request and response pattern, not a specific interface.

### Can Elicitation ask for nested objects?

The specification limits schemas to simpler flat structures with primitive values. That keeps client implementation easier and safer.

### Should Elicitation collect payment details?

No. Payment credentials and other secrets should use secure authorization or payment flows, not elicitation.

### Why does this matter for website owners?

Agent-ready workflows need clear moments where agents can ask humans for missing choices instead of guessing. Elicitation gives that pattern a standard shape.

## Bottom line

MCP Elicitation is a small feature with a large design lesson: safe agents should ask clearly when they need human input, and users should have a real option to say no.
