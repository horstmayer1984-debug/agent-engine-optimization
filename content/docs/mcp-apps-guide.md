---
title: "MCP Apps: Interactive Interfaces for Agent Workflows"
date: 2026-05-17
weight: 135
category: "Architecture"
description: "Learn what MCP Apps are, how interactive UI components work inside MCP hosts, and when websites or tools should use them."
summary: "A practical MCP Apps guide covering inline UI, secure rendering, use cases, and how the extension changes agent-facing product design."
keywords:
  - MCP Apps
  - MCP UI
  - interactive agent interfaces
  - Model Context Protocol apps
  - agent workflows UI
---

# MCP Apps: Interactive Interfaces for Agent Workflows

MCP Apps are an official Model Context Protocol extension that lets tools return interactive user interfaces, not just text or structured data. That matters because some agent workflows need charts, approval forms, dashboards, or multi-step controls inside the conversation itself. MCP Apps keep the workflow in context while giving users a richer interface when plain text is not enough.

## What official MCP docs say

The MCP project announced MCP Apps as its first official extension in January 2026. Official docs describe interactive HTML interfaces rendered inside MCP hosts, with sandboxing and a secure communication bridge between the app and host.

Primary sources:

- [MCP blog: MCP Apps live announcement](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/)
- [MCP Apps overview](https://modelcontextprotocol.io/extensions/apps/overview)
- [MCP extensions overview](https://modelcontextprotocol.io/extensions)

## Why MCP Apps exist

Text is enough for many tool responses:

- a lookup result
- a status
- a simple recommendation

But text becomes clumsy for:

- charts
- visual comparisons
- approval workflows
- design canvases
- forms with several dependent fields
- dashboards with live state

MCP Apps add a UI layer without forcing users to leave the host experience.

## MCP Apps vs normal web apps

| Question | Standalone web app | MCP App |
|---|---|---|
| Where does it render? | Separate site or tab | Inside the MCP host |
| Is conversation context preserved? | Usually no | Yes |
| Best for | Full products | Workflow fragments and tool-linked UI |
| Communication | Browser app APIs | MCP plus app bridge |
| User journey | Context switch | Inline continuation |

MCP Apps are not a replacement for every web app. They are useful when the interface is part of an agent-mediated task rather than the whole product.

## AEO implications

The [execution layer](/docs/execution-layer/) often needs a human checkpoint. MCP Apps can make that checkpoint practical:

- approve a refund
- inspect a quote
- choose between options
- review a chart
- confirm a risky action

That connects naturally to [agent UX and human-in-the-loop design](/docs/agent-ux-human-in-the-loop/), where the question is not "human or agent" but "which parts need which interface?"

## When to use MCP Apps

Use them when:

- a tool result needs visual interpretation
- the next step requires structured human input
- you want to preserve conversational context
- the UI is subordinate to a tool workflow

Do not use them when:

- a simple text answer is enough
- the experience needs a full standalone product shell
- the host ecosystem you target does not support the extension yet

## Security and implementation

Official docs describe sandboxed rendering and a secure message bridge. That means teams still need to think carefully about:

- what data enters the UI
- which tool calls the UI can trigger
- whether approval is required
- how state is logged
- how host support varies

The [MCP authorization guide](/docs/mcp-authorization-oauth-ai-agents/) remains relevant because rich UI does not remove the need for strict permissions.

## FAQ

### Are MCP Apps part of core MCP?

They are an official extension, not the core protocol itself.

### Do MCP Apps replace a website?

No. They are best for inline workflow UI, not for replacing all public web experiences.

### Which clients support them?

Host support varies. The MCP docs maintain a client support matrix for official extensions.

### What is the best first use case?

Approval flows and small dashboards are strong starting points because they need more than text but less than a full product UI.

## Bottom line

MCP Apps matter because agent workflows still need moments of human judgment. They bring useful interface fragments into the same place where the agent is already working.
