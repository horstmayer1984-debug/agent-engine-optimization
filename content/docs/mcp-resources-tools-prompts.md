---
title: "MCP Resources vs Tools vs Prompts: The Practical Difference"
date: 2026-05-23
weight: 135
category: "Guide"
description: "Compare MCP resources, tools, and prompts. Learn what each feature does, when to use it, and how to design clearer agent integrations."
summary: "A practical comparison of MCP resources, tools, and prompts for developers building agent-readable systems and Model Context Protocol integrations."
keywords:
  - MCP resources
  - MCP tools
  - MCP prompts
  - Model Context Protocol features
  - agent integrations
---

# MCP Resources vs Tools vs Prompts: The Practical Difference

MCP resources provide context, tools perform actions, and prompts provide reusable instructions. The difference matters because poor MCP design makes agents unreliable: data should not be exposed as an action, actions should not be hidden in prompts, and prompts should not replace structured capability definitions.

## The short version

The Model Context Protocol has several server features. Three of the most important are documented as [resources](https://modelcontextprotocol.io/docs/concepts/resources), [tools](https://modelcontextprotocol.io/docs/concepts/tools), and [prompts](https://modelcontextprotocol.io/docs/concepts/prompts).

Use them like this:

- resources: "Here is context you may read."
- tools: "Here is something you may do."
- prompts: "Here is a workflow template the user may choose."

For wider context, see [MCP vs API for agents](/docs/mcp-vs-api-for-agents/), [MCP Registry](/docs/mcp-registry-guide/), and the [developer guide to AEO](/docs/developers-guide-aeo/).

## Comparison table

| Feature | Best use | Who usually initiates it | Example |
|---|---|---|---|
| Resources | Expose data and context | Client or host application | File, schema, product catalog, README |
| Tools | Execute actions or computations | Model, with user/client control | Create ticket, query database, calculate quote |
| Prompts | Offer reusable workflows | User-controlled command or selection | "Review this code" or "Draft release notes" |

This split keeps integrations understandable. Agents can reason better when capability boundaries are obvious.

## What MCP resources are for

Resources are for context. The MCP specification says resources let servers share data such as files, database schemas, or application-specific information. Each resource has a URI and may include metadata such as MIME type, size, title, and annotations.

Good resource examples:

- `file:///project/README.md`
- database schema
- product catalog snapshot
- API endpoint documentation
- current project configuration
- policy document

Resources should be stable enough for a model to inspect or reference. They should not mutate business state by being read.

## What MCP tools are for

Tools are for actions. The official tools specification says MCP servers can expose tools that language models may invoke to interact with external systems, such as APIs, databases, or computations.

Good tool examples:

- `create_issue`
- `get_order_status`
- `calculate_shipping_quote`
- `search_inventory`
- `submit_refund_request`
- `run_lighthouse_audit`

Tools need schemas, validation, rate limits, access control, and audit logs. The [agent observability guardrails](/docs/agent-observability-guardrails/) page is relevant here.

## What MCP prompts are for

Prompts are reusable templates. They help users or clients trigger a known workflow with arguments. A prompt might gather instructions for code review, content drafting, onboarding, or support triage.

Prompts are useful when:

- the workflow is repeatable
- the user should intentionally select it
- the instruction pattern benefits from consistency
- the output is language-heavy rather than action-heavy

Do not hide execution in prompts. If something changes state, it belongs in a tool with confirmation and logging.

## Design mistakes to avoid

| Mistake | Why it causes problems | Better design |
|---|---|---|
| Exposing actions as resources | Reading data may trigger side effects | Use tools for actions |
| Using prompts as API wrappers | Model may infer parameters loosely | Use a tool with schema |
| Putting all context in tool descriptions | Descriptions become bloated | Expose resources |
| Making every file a resource | Too much context noise | Prioritize relevant resources |
| No output schema for tools | Harder for clients to validate results | Use structured outputs where possible |

## AEO implications

Agent-readable websites face the same design problem as MCP servers: separate content, instructions, and actions.

For example:

- a pricing page is a resource-like public context
- a checkout API is a tool-like action
- a buyer guide is a prompt-like workflow aid

Clear separation helps AI agents understand what they can read, what they can recommend, and what they can execute. That is the practical foundation of [Agent Engine Optimization](/docs/what-is-aeo/).

## Implementation checklist

1. List every thing the agent may read.
2. List every action the agent may perform.
3. List repeated workflows users may invoke.
4. Assign each item to resource, tool, or prompt.
5. Add schemas for tools.
6. Add useful metadata for resources.
7. Keep prompts user-controlled.
8. Document permissions and risks.

## FAQ

### Can one MCP server expose resources, tools, and prompts?

Yes. Many useful servers will expose all three, but each feature should have a clear role.

### Are resources safer than tools?

Usually, because resources are meant for reading context. They can still expose sensitive data if access control is weak.

### Should prompts be invoked automatically by the model?

Prompts are generally designed to be user-controlled or explicitly selected. Automatic action should be handled carefully through tools and permissions.

### What is the biggest MCP design rule?

Keep side effects in tools, context in resources, and reusable instructions in prompts.

## Bottom line

Good MCP design is mostly clean boundaries. When resources, tools, and prompts each do their own job, agents become easier to trust, debug, and improve.
