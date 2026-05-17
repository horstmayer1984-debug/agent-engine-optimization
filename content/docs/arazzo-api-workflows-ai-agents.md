---
title: "Arazzo API Workflows for AI Agents"
metaTitle: "Arazzo API Workflows for AI Agents: AEO Guide"
date: 2026-05-17
weight: 115
category: "Architecture"
description: "Arazzo defines machine-readable API workflows on top of OpenAPI. Learn why it matters for AI agents, MCP, and execution-layer SEO."
summary: "A practical guide to Arazzo for AI agents, explaining workflow descriptions, OpenAPI sequencing, success criteria, and AEO implementation patterns."
keywords:
  - Arazzo specification
  - API workflows for AI agents
  - OpenAPI Arazzo
  - agent-ready APIs
  - execution layer SEO
---

# Arazzo API Workflows for AI Agents

Arazzo matters for AEO because OpenAPI describes individual API operations, but agents often need workflows. A booking, quote, checkout, or onboarding task may require several API calls in the right order. Arazzo gives teams a machine-readable way to describe those sequences.

## What Arazzo is

The OpenAPI Initiative describes Arazzo as a specification for expressing sequences of API calls and their dependencies to achieve an outcome. It complements OpenAPI rather than replacing it.

Primary sources:

- [OpenAPI Initiative: Arazzo Specification](https://www.openapis.org/arazzo-specification)
- [Arazzo Specification](https://spec.openapis.org/arazzo/latest.html)
- [OpenAPI Specification](https://spec.openapis.org/oas/v3.1.0.html)

## Why OpenAPI alone is not enough

OpenAPI is excellent at describing endpoints. It tells a developer or machine what operations exist, what parameters they accept, and what responses they return.

But many real tasks need order:

1. Search available services.
2. Select one service.
3. Check available slots.
4. Create a booking.
5. Confirm the booking.

If an agent only sees individual endpoints, it must infer the sequence. That can work for simple APIs, but it becomes fragile when dependencies, tokens, state, or validation rules are involved.

## OpenAPI vs Arazzo vs MCP

| Layer | Main job | Agent benefit |
|---|---|---|
| OpenAPI | Describes API operations | Understand available endpoints |
| Arazzo | Describes workflows across operations | Understand how to complete a task |
| MCP | Exposes callable tools and resources | Invoke actions through an agent interface |

The [MCP vs API guide](/docs/mcp-vs-api-for-agents/) explains the tool layer. Arazzo helps document the workflow logic behind those tools.

## Where Arazzo fits in AEO

AEO is strongest when agents can move through this sequence:

1. Discover the service.
2. Understand capabilities.
3. Read constraints.
4. Execute the workflow.
5. Verify the result.

Arazzo supports steps 2 through 5 by making multi-step workflows explicit. It is especially useful for the [execution layer](/docs/execution-layer/), where an agent needs to do more than fetch content.

## Strong use cases

| Use case | Why Arazzo helps |
|---|---|
| Ecommerce checkout | Cart, shipping, taxes, payment, confirmation happen in sequence |
| B2B quote request | Eligibility, configuration, pricing, and submission depend on each other |
| Travel booking | Availability, fare rules, passenger data, and confirmation are ordered |
| SaaS onboarding | Workspace, user, billing, and permission setup has dependencies |
| Support escalation | Ticket creation, classification, attachment, and routing need state |
| Financial workflow | Disclosures, eligibility, and consent must happen before action |

The [agent-ready web app checklist](/docs/agent-ready-web-apps/) covers how to design the underlying product surface.

## What to include in an Arazzo workflow

At minimum, document:

- workflow goal
- required inputs
- ordered steps
- source OpenAPI operations
- dependencies between steps
- success criteria
- outputs
- error states
- retry and idempotency expectations

The success criteria are especially important. Agents need to know what "done" means.

## Example workflow shape

For an appointment booking API:

| Step | Operation | Output used later |
|---|---|---|
| 1 | `list_services` | `service_id` |
| 2 | `list_available_slots` | `slot_id` |
| 3 | `create_booking` | `booking_id` |
| 4 | `get_booking` | confirmed status |

Without workflow documentation, an agent may call the wrong endpoint first or miss the confirmation step.

## Implementation path

1. Clean up your OpenAPI document.
2. Pick three high-value workflows.
3. Write Arazzo descriptions for those workflows.
4. Test them with an agent or workflow runner.
5. Link the workflow docs from API docs and `llms.txt`.
6. Wrap the same workflows as MCP tools when useful.

This keeps the system grounded: OpenAPI describes operations, Arazzo describes sequencing, MCP exposes callable tools.

## FAQ

### Does Arazzo replace OpenAPI?

No. It complements OpenAPI by describing workflows that use OpenAPI operations.

### Is Arazzo only for AI agents?

No. It is useful for documentation, SDK generation, testing, and compliance. AI agents are one strong use case.

### Do I need Arazzo before MCP?

Not always. For simple tools, MCP may be enough. For multi-step workflows, Arazzo helps make the process explicit.

### What is the SEO angle?

Arazzo is not a ranking factor. It improves execution-layer readiness by making workflows machine-readable.

### Which workflows should be documented first?

Start with workflows tied to revenue, support resolution, booking, onboarding, or compliance-sensitive actions.
