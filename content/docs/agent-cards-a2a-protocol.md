---
title: "Agent Cards and A2A Protocol: Programming Your Site for Agent-to-Agent Collaboration"
date: 2026-04-12
weight: 63
category: "Architecture"
description: "Agent Cards and the A2A protocol let autonomous agents discover your site and collaborate with it. Implementation guide with JSON structure, WebSocket patterns, and sandboxing."
summary: "Agent Cards tell other agents what your site can do. The A2A protocol enables direct agent-to-agent task exchange. Together they make your site discoverable and collaborative in multi-agent workflows."
keywords:
  - agent card json
  - A2A protocol
  - agent to agent protocol
  - agent collaboration
  - agent card implementation
  - multi agent discovery
---

Agent Cards and the A2A (Agent-to-Agent) protocol let you program your website so autonomous agents discover it and collaborate with it without you building every integration manually. An Agent Card describes what your site can do. The A2A protocol defines how agents exchange tasks and results.

Together, they make your site a participant in multi-agent workflows rather than a passive endpoint that individual agents query in isolation.

## What an Agent Card contains

An Agent Card is a JSON file (agent-card.json) placed in your site root. It serves as a machine-readable capability manifest that tells other agents: who you are, what you can do, how to authenticate, and which protocols you support.

The core fields: name (your service name), description (what your service does in one sentence), url (your base URL), capabilities (a structured list of actions your site can perform), protocols (which communication standards you support, such as MCP, REST, A2A), authentication (how agents should authenticate), and contact (where to report issues).

Each capability in the list includes a name, description, input schema, and output schema. This is what agents use to decide whether your site can help with their current task.

## Why Agent Cards matter for discovery

In a multi-agent workflow, a coordinator agent needs to find services that can handle specific subtasks. Without Agent Cards, the coordinator has to guess based on page content. With Agent Cards, the coordinator reads a structured manifest and makes an informed routing decision in milliseconds.

Agent Cards also enable recommendation. An agent that successfully uses your site can pass your Agent Card to other agents that need similar capabilities. This creates a word-of-mouth discovery mechanism within the agent ecosystem.

## A2A protocol basics

The A2A protocol standardizes how agents exchange tasks. One agent sends a task request (what needs to be done, what inputs are available, what constraints apply). The receiving agent processes the task and returns a structured result.

The protocol handles task lifecycle management: task creation, status updates, completion, and failure. It also supports long-running tasks where the result is not immediately available.

For your site, implementing A2A means exposing task endpoints that accept structured requests and return structured responses. The format follows Google's A2A specification with typed task objects and status enumerations.

## Step-by-step implementation

### Step 1: Create agent-card.json

Write the JSON file with your service description and capabilities. Be precise about what each capability does, what inputs it requires, and what outputs it produces. Place it at your domain root.

### Step 2: Add A2A task endpoints

Expose endpoints that accept task requests and return task results. A minimal implementation needs: POST /a2a/tasks (create a new task), GET /a2a/tasks/{id} (check task status), and GET /a2a/tasks/{id}/result (retrieve the completed result).

### Step 3: Connect with MCP

If you already have an MCP server, your A2A task endpoints can delegate to MCP tools internally. The A2A layer handles inter-agent communication while MCP handles the actual tool execution.

### Step 4: Register publicly

List your Agent Card in MCP registries and agent directories so that agents outside your direct network can discover your service.

## Real-time collaboration with WebSockets

Standard request-response patterns work for simple tasks. Multi-step collaborative workflows benefit from WebSocket connections.

A WebSocket endpoint at /ws/agent-collaboration lets two agents maintain a persistent connection for workflows that require back-and-forth negotiation: checking multiple availability slots, comparing options, adjusting parameters based on intermediate results.

This is particularly valuable for commerce workflows where an agent needs to reserve inventory, check shipping options, apply discount rules, and confirm payment authority in a coordinated sequence.

## Agent sandboxing for security

When external agents execute tasks on your infrastructure, sandboxing prevents them from accessing resources outside their authorized scope.

WASM-based sandboxing runs agent-submitted operations in isolated environments with defined memory limits, CPU limits, and network access restrictions.

For most sites, sandboxing becomes relevant when you expose execution endpoints that accept complex inputs or when you allow agents to run custom logic within your system.

## Comparison: MCP vs A2A

| Aspect | MCP | A2A |
|---|---|---|
| Purpose | Agent-to-tool communication | Agent-to-agent communication |
| Discovery | Tool schemas | Agent Cards |
| Interaction pattern | Single request-response | Task lifecycle with status tracking |
| Best for | Direct tool execution | Collaborative multi-step workflows |
| Your implementation | JSON-RPC server | Task endpoints plus Agent Card |

Both protocols complement each other. MCP handles the tools. A2A handles the collaboration between agents that use those tools.

The [multi-agent AEO article](/docs/multi-agent-aeo/) explains how orchestrated workflows depend on these protocols. The [MCP vs API guide](/docs/mcp-vs-api-for-agents/) covers the tool access layer in detail.

---

## FAQ

**How long does it take to create an Agent Card?**
Thirty minutes for a basic Agent Card with 3 to 5 capabilities. The JSON structure is straightforward.

**Do I need both MCP and A2A?**
Not necessarily. Start with MCP if your primary need is agents calling your tools. Add A2A when you want agents to collaborate with your service as a peer in multi-agent workflows.

**What is the difference between an Agent Card and llms.txt?**
llms.txt is a human-and-machine-readable overview of your site in Markdown. An Agent Card is a strictly machine-readable capability manifest in JSON. Both serve discovery, but Agent Cards are more structured and protocol-specific.

**Can agents discover my site without an Agent Card?**
Yes, through llms.txt, schema markup, or direct page crawling. An Agent Card accelerates discovery and enables A2A collaboration, but it is not the only discovery path.

**Is A2A only for large enterprises?**
No. Any site that exposes actions agents can perform benefits from A2A. Even a small service with a booking endpoint can participate in multi-agent workflows through a simple Agent Card and task endpoint.
