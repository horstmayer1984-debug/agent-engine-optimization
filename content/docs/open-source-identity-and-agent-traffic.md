---
title: "Detecting and Verifying AI Agent Visits: Top Open Source Tools Ranked"
metaTitle: "AI Agent Traffic Analytics & Verification Tools (2026)"
description: "Rankings of open-source tools for identifying and verifying AI agents: Web Bot Auth, AgentCake, mintlify/agent-traffic, Botscent, and AgentReady."
summary: "Comparative guide for agent detection: RFC 9421 signature verification, session replay analytics, traffic classification, and readiness linters."
keywords:
  - "Web Bot Auth"
  - "AgentCake"
  - "mintlify agent-traffic"
  - "Botscent"
  - "AgentReady"
  - "agent traffic verification"
date: 2026-11-22
weight: 213
category: "Open Source"
---

As autonomous browser agents and multi-agent systems interact with websites, traditional web analytics (Google Analytics, server log parsers) fail to accurately categorize non-human traffic. Furthermore, malicious bots frequently spoof agent User-Agents.

This benchmark evaluates the leading open-source libraries and analytics engines engineered to detect, classify, and cryptographically verify AI agent visits.

> **Research Status:** November 22, 2026. GitHub stars, licenses, and push timestamps (`pushed_at` in Europe/Berlin) sourced directly from the GitHub API on November 22, 2026.

---

## Comparative Ranking: Agent Identification and Analytics

| Rank | Tool | Category | Key AEO Utility | License | Stars (22.11.2026) | Last Activity (Europe/Berlin) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | [Web Bot Auth](https://github.com/cloudflare/web-bot-auth) | Signature Verification (RFC 9421) | Cryptographically authenticates whether an incoming HTTP request originates from an authentic signed agent operator. | Apache-2.0 | 186 | 21.11.2026, 20:46 |
| **2** | [AgentCake](https://github.com/tartini-ai/agent-traffic-analytics) | Traffic Analytics / Replay | Distinguishes agents from human visitors and provides specialized session replay for autonomous browsing agents. | MIT | 91 | 21.11.2026, 15:03 |
| **3** | [mintlify/agent-traffic](https://github.com/mintlify/agent-traffic) | Traffic Classifier | Accurately sorts inbound web requests into autonomous agents, automated search crawlers, and human users. | MIT | 88 | 10.11.2026, 19:43 |
| **4** | [Botscent](https://github.com/nalinbhardwaj/botscent) | Detection Library | Lightweight programmatic library implementing behavioral heuristics for identifying agentic bots. | MIT | 35 | 11.11.2026, 17:13 |
| **5** | [AgentReady](https://github.com/agentready-org/standard) | Readiness Scanner | Automated agent-readiness scanner executable via `npx is-agentic`. Emerging standard; license omitted in GitHub API. | Unspecified in API | 65 | 11.11.2026, 23:50 |

---

## Detailed Tool Profiles

### 1. Web Bot Auth (Cloudflare)
- **Focus:** Cryptographic authentication over HTTP.
- **Why it matters for AEO:** Implements the IETF Internet-Draft [draft-ietf-webbotauth-httpsig-protocol](https://datatracker.ietf.org/doc/draft-ietf-webbotauth-httpsig-protocol/) and [RFC 9421](https://www.rfc-editor.org/rfc/rfc9421). Allows origin web servers to mathematically verify signed HTTP requests from providers like OpenAI without maintaining fragile IP address whitelists.
- **Repository:** [github.com/cloudflare/web-bot-auth](https://github.com/cloudflare/web-bot-auth)

### 2. AgentCake
- **Focus:** Session-level agent observation.
- **Why it matters for AEO:** Unlike traditional session recording tools that expect human mouse movements, AgentCake models the programmatic DOM traversals and rapid selector evaluations characteristic of AI browser agents.
- **Repository:** [github.com/tartini-ai/agent-traffic-analytics](https://github.com/tartini-ai/agent-traffic-analytics)

### 3. mintlify/agent-traffic & Botscent
- **Focus:** Edge request classification.
- **Why it matters for AEO:** Mintlify's classifier provides an essential middleware component to split analytics into human vs. synthetic traffic, while Botscent provides a minimal embeddable library.
- **Repositories:** [github.com/mintlify/agent-traffic](https://github.com/mintlify/agent-traffic) and [github.com/nalinbhardwaj/botscent](https://github.com/nalinbhardwaj/botscent)

### 4. AgentReady
- **Focus:** Early-stage heuristic auditing.
- **Why it matters for AEO:** Useful for local developers checking basic accessibility for agents (via `npx is-agentic`). Note that this is an early-stage project without an official license declared in the GitHub API.
- **Repository:** [github.com/agentready-org/standard](https://github.com/agentready-org/standard)

---

## Decision Guide: Which Tool Should You Choose?

- **For cryptographic verification:** Deploy **[Web Bot Auth](https://github.com/cloudflare/web-bot-auth)** alongside your edge gateway to verify signed headers before granting agent-level privileges.
- **To understand agent user journeys:** Integrate **[AgentCake](https://github.com/tartini-ai/agent-traffic-analytics)** or **[mintlify/agent-traffic](https://github.com/mintlify/agent-traffic)** into your application observability pipeline.
- **For quick local CLI audits:** Test with **[AgentReady](https://github.com/agentready-org/standard)** (`npx is-agentic`), keeping in mind its early development status.
