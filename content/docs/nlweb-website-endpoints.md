---
title: "NLWeb Website Endpoints: Machine-Readable Interfaces for Agents"
metaTitle: "NLWeb Website Endpoints for Agents"
date: 2026-06-28
weight: 173
category: "Architecture"
description: "NLWeb gives websites natural-language endpoints for humans and AI agents. Learn how it uses Schema.org, RSS, MCP, and site data."
summary: "A practical introduction to NLWeb website endpoints, why they matter for agent-readable websites, and how to prepare content and data."
keywords:
  - NLWeb website endpoints
  - NLWeb for AI agents
  - machine-readable website endpoints
  - natural language web API
  - NLWeb MCP
---

# NLWeb Website Endpoints

NLWeb is an open-source Microsoft project for adding natural-language interfaces to websites. It matters for agent-ready sites because it turns existing site data, such as Schema.org and RSS, into endpoints that can serve humans and AI agents. It is a practical bridge between content, search, and MCP-style tools.

## What NLWeb is

The [Microsoft NLWeb repository](https://github.com/microsoft/NLWeb) describes NLWeb as a way to build conversational interfaces for websites. Its README says it natively supports MCP, uses Schema.org and RSS-like semi-structured formats, and provides open protocols plus implementation code.

That makes NLWeb relevant for sites that want agents to ask structured questions instead of scraping pages blindly.

NLWeb should not be treated as a magic SEO layer. It is closer to a website interface pattern: a way to expose the site's own knowledge and records through natural-language access.

## Why NLWeb is a new keyword opportunity

Most websites still think in three layers:

1. HTML pages for humans.
2. Sitemaps for search engines.
3. APIs for developers.

NLWeb points to a fourth layer: natural-language endpoints for agents and AI-assisted users.

| Layer | Main user | Typical format |
|---|---|---|
| Website | Human visitor | HTML |
| Sitemap | Search crawler | XML |
| Structured data | Search and AI systems | Schema.org JSON-LD |
| NLWeb endpoint | Human or AI agent asking a task question | Natural-language interface backed by site data |
| MCP tool | Agent that needs a structured action | Tool schema and endpoint |

For related architecture, see [MCP Resources vs Tools vs Prompts](/docs/mcp-resources-tools-prompts/) and [MCP vs API for Agents](/docs/mcp-vs-api-for-agents/).

## Which sites should watch NLWeb first

NLWeb is most interesting for sites with rich, queryable data:

1. Ecommerce catalogs.
2. Travel inventory.
3. Real estate listings.
4. Job boards.
5. Documentation portals.
6. Local directories.
7. Support knowledge bases.
8. Event databases.

These sites already contain structured facts. NLWeb gives them a path toward conversational and agent-readable retrieval.

## How to prepare for NLWeb

Even if you do not implement NLWeb yet, prepare the data layer:

1. Use consistent entity names across pages and structured data.
2. Keep Schema.org markup aligned with visible content.
3. Maintain clean feeds for products, articles, events, listings, or docs.
4. Create stable canonical URLs for every important entity.
5. Document update frequency and availability rules.
6. Decide which data agents may query and which data requires authentication.
7. Map possible questions to source data fields.

This overlaps with [Programming Websites for AI Agents](/docs/programming-websites-for-ai-agents/) and [Agent-Ready Web Apps](/docs/agent-ready-web-apps/).

## NLWeb vs scraping

| Question | Scraping | NLWeb-style endpoint |
|---|---|---|
| Does the site control the answer shape? | Usually no | Yes |
| Can the agent ask a focused question? | Indirectly | Yes |
| Is the output tied to source data? | Often fragile | More controllable |
| Is access policy easier to enforce? | Harder | Easier if designed well |
| Does it replace normal pages? | No | No |

The strategic benefit is control. If agents are going to query your site anyway, a structured endpoint can be safer and more accurate than forcing them through visual pages.

## FAQ

### Is NLWeb an official web standard?

NLWeb is an open-source Microsoft project with open protocols and implementation code. Treat it as an emerging approach, not a settled universal standard.

### Does NLWeb replace Schema.org?

No. NLWeb builds on site data such as Schema.org and RSS-like formats. Good structured data still matters.

### Is NLWeb the same as MCP?

No. NLWeb can support MCP, but MCP is a protocol for tools and context exchange. NLWeb is focused on natural-language website interfaces.

### Should every website implement NLWeb now?

No. Start with sites where users or agents need to ask detailed questions against structured site data.

## Sources

Primary and reference sources: [Microsoft NLWeb GitHub repository](https://github.com/microsoft/NLWeb), [NLWeb README raw source](https://raw.githubusercontent.com/microsoft/NLWeb/main/README.md), [Model Context Protocol documentation](https://modelcontextprotocol.io/docs/getting-started/intro), [Schema.org](https://schema.org/), and [Google structured data documentation](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data).
