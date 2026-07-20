---
title: "MCP Sampling Explained: How Servers Request AI Model Output"
date: 2026-05-23
weight: 133
category: "Architecture"
description: "MCP Sampling lets servers request model generations through a client. Learn how it works, where it helps, and why human review matters."
summary: "A practical explainer for MCP Sampling, covering server-requested LLM generations, client control, model preferences, security, and AEO implications."
keywords:
  - MCP Sampling
  - sampling/createMessage
  - Model Context Protocol sampling
  - AI agent architecture
  - MCP servers
---

# MCP Sampling Explained: How Servers Request AI Model Output

MCP Sampling lets an MCP server ask the client to generate model output during a workflow. The server does not need its own model API key. The client keeps control over model access, permissions, review, and final delivery. This makes Sampling useful for agentic workflows, but risky if prompts and generated outputs are not shown clearly to the user.

## What MCP Sampling is

The official [Model Context Protocol Sampling specification](https://modelcontextprotocol.io/docs/concepts/sampling) describes Sampling as a way for servers to request LLM generations from language models via clients. In the 2025-06-18 protocol revision, clients that support it declare a `sampling` capability, and servers request a generation through `sampling/createMessage`.

That sounds abstract, so here is the simple version: a tool server can ask the user's AI client to think, summarize, classify, or generate text as part of a tool flow.

For broader context, see [MCP vs API for agents](/docs/mcp-vs-api-for-agents/), [MCP Authorization with OAuth](/docs/mcp-authorization-oauth-ai-agents/), and [MCP Apps](/docs/mcp-apps-guide/).

## Why Sampling exists

Without Sampling, an MCP server has two limited choices:

- return raw data and hope the client model knows what to do
- call its own model provider directly, which raises cost, privacy, and key-management issues

Sampling creates a middle path. The server can request model work, but the client remains the gatekeeper.

## Sampling vs tools vs resources

| MCP feature | Who controls it | Main purpose | Example |
|---|---|---|---|
| Tools | Model invokes server action | Execute a capability | "Create a ticket" |
| Resources | Server exposes context | Provide data for the model | "Read project schema" |
| Prompts | Server exposes templates | Guide a user-controlled workflow | "Run code review prompt" |
| Sampling | Server asks client model for output | Generate or reason during a workflow | "Summarize this retrieved document" |

Sampling is not a replacement for tools. It is a way to nest model generation inside a capability.

## Example use cases

Sampling can help when a server needs language-model output but should not own the model relationship.

Useful patterns include:

- summarizing retrieved documents
- drafting a response after a tool fetches data
- classifying support tickets
- generating a natural-language explanation from structured data
- asking the client model to transform user-provided context
- scoring options based on user-visible criteria

For AEO, this matters because agent-readable websites and APIs may need to support workflows that mix retrieval, execution, and explanation.

## Security and review requirements

The Sampling specification emphasizes human review. Applications should make it easy to review sampling requests, edit prompts before sending, and review generated responses before delivery.

That is a serious requirement. Sampling can otherwise become a hidden model call triggered by a server the user barely understands.

| Risk | Why it matters | Guardrail |
|---|---|---|
| Hidden prompt injection | Server may include unsafe instructions | Show prompts before execution |
| Data leakage | Context may contain sensitive information | Let users review shared context |
| Cost surprises | Model calls can consume paid tokens | Display model and cost policy |
| Wrong output | Generated answer may be inaccurate | Review before final delivery |
| Server overreach | Server may request unnecessary model work | Require explicit capability support |

The [agent observability guardrails](/docs/agent-observability-guardrails/) guide expands this governance layer.

## AEO implications

MCP Sampling rewards clean context. If your docs, API responses, product data, or workflow descriptions are vague, the client model has a harder job. If they are structured, concise, and internally linked, Sampling-powered workflows can produce better downstream answers.

For website owners, this means:

- publish clear definitions
- keep API responses structured
- expose machine-readable docs
- avoid burying important constraints in prose
- document source-of-truth pages
- provide stable identifiers for entities and actions

The [developer guide to AEO](/docs/developers-guide-aeo/) is the natural next step.

## FAQ

### Does MCP Sampling let a server call any model it wants?

No. The client controls model access. The server can express preferences, but the client decides what is available and permitted.

### Is Sampling required for MCP servers?

No. It is a client capability. Many MCP workflows can use tools, resources, and prompts without Sampling.

### Is Sampling safe for production?

It can be used carefully, but it needs prompt review, context review, logging, permission boundaries, and sensible defaults.

### Why does Sampling matter for AEO?

It shows that agent workflows may ask models to reason over your content during execution, not only retrieve pages. Structured, source-backed content becomes more useful.

## Bottom line

MCP Sampling is a useful bridge between tool execution and model reasoning. Treat it as a controlled capability, not a background shortcut.
