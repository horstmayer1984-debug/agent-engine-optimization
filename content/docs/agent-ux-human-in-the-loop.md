---
title: "Agent UX and Human-in-the-Loop Design: Building Interfaces for Both Humans and Agents"
date: 2026-04-12
weight: 86
category: "Guide"
description: "Agent-responsive design makes interfaces bilingual for humans and machines. Semantic HTML, WebSocket endpoints, structured feedback, and approval flows that serve both audiences."
summary: "Modern interfaces must serve two audiences simultaneously: human users and AI agents. Agent-responsive design uses semantic HTML, structured endpoints, and feedback loops to satisfy both."
keywords:
  - agent UX design
  - human in the loop agents
  - agent responsive design
  - dual interface design
  - agent approval workflows
---

Agent-responsive design makes interfaces work for two audiences simultaneously: human users who browse visually and AI agents who parse structurally. The best implementations do not require separate interfaces. They build one system that serves both through clean architecture.

## The dual-audience challenge

A product page needs to persuade a human buyer with visual design, brand storytelling, and emotional triggers. The same page needs to inform an AI agent with structured specifications, accurate pricing, and explicit availability.

These are not contradictory goals, but they are different goals. The mistake is optimizing for one audience and assuming the other is satisfied.

A page with beautiful imagery and compelling narrative but no structured data serves humans and excludes agents. A page with raw JSON endpoints and no visual design serves agents and excludes humans. The goal is a unified page that carries both layers.

## Semantic HTML as the foundation

Agents ignore JavaScript-rendered content in most cases. They parse the raw HTML. Semantic elements (heading hierarchy, table elements, list elements, form elements, button elements) provide the structural information agents need.

Use native HTML elements rather than styled divs. A button element tells an agent that a clickable action exists. A div styled to look like a button tells the agent nothing.

Add aria-label attributes where the element's purpose is not obvious from its content. An agent parsing your page benefits from the same accessibility practices that screen readers use.

Server-render all critical content. If your product name, price, and availability require JavaScript to appear, agents cannot see them. The [programming websites for agents guide](/docs/programming-websites-for-ai-agents/) covers the technical requirements.

## Human-in-the-loop approval flows

Not every agent action should complete autonomously. Design approval flows that pause for human confirmation on high-stakes decisions.

The approval flow has three components: the agent proposes an action (displayed to the human in clear, structured terms), the human reviews and approves or rejects, and the system executes or cancels based on the human decision.

For your site's endpoints, this means supporting asynchronous workflows. An agent submits a booking request. Your system returns a pending status with a task ID. The human reviews. Your system updates the status to confirmed or rejected. The agent polls the task ID and receives the final status.

This pattern works for purchase approvals above a spending threshold, legal document submissions, account modifications, and any action that benefits from human judgment.

## Structured feedback interfaces

Both humans and agents need to report problems. But they report differently.

Human feedback: a comment box, a star rating, a support ticket. Unstructured, rich in context, requires interpretation.

Agent feedback: a structured endpoint that accepts a page URL, expected data, actual data found, and error classification. No interpretation needed.

Build both. The human feedback form on the visible page. The agent feedback endpoint documented in your llms.txt and Agent Card. Both feed into the same improvement process through your [feedback loops](/docs/agent-feedback-loops/).

## WebSocket endpoints for live sessions

Standard REST APIs work for stateless interactions. Multi-step agent workflows benefit from WebSocket connections that maintain session state.

A WebSocket endpoint at /ws/agent-session lets an agent maintain context across a sequence of actions: browsing products, narrowing selection, checking availability for the top choice, and completing a purchase. Each step happens on the same connection with shared state.

For the human parallel: the same underlying session logic can power a guided purchase flow in the browser UI, using the same business logic through a different interface.

## Designing for graceful degradation

Your interface should work at every capability level: full human browser experience (JavaScript, CSS, images, interaction), reduced browser experience (slow connection, no JavaScript), agent experience (raw HTML, structured data, endpoints), and basic agent experience (just the HTML text content).

Each layer serves a different client. Design so that removing a layer does not break the layers below it. If your JavaScript fails, the HTML should still contain essential information. If your endpoints are down, the HTML should still be readable.

The [AEO implementation guide](/docs/implement-aeo/) covers the content layer structure.

---

## FAQ

**What is agent-responsive design?**
An interface design approach that serves both human users and AI agents through a single architecture. Semantic HTML provides the agent-readable layer. Visual design provides the human layer. Both share the same underlying data.

**Do I need separate interfaces for agents?**
Not usually. One well-structured page with semantic HTML, schema markup, and documented endpoints serves both audiences. Separate interfaces become relevant only for complex transactional workflows.

**What is the role of human-in-the-loop in AEO?**
It provides a safety net for high-stakes agent actions. The agent proposes, the human approves, the system executes. This builds trust and prevents costly errors from fully autonomous systems.

**How do WebSocket endpoints help agents?**
They maintain session state across multi-step workflows, preventing context loss between sequential REST calls. This is particularly valuable for purchase flows and complex service interactions.

**Should I prioritize human UX or agent UX?**
Both. If forced to choose a starting point, human UX with semantic HTML gives you both audiences. Agent-specific endpoints (MCP, WebSocket) can be added incrementally.
