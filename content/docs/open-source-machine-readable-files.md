---
title: "The Best Open Source Tools for llms.txt: Rankings and Comparison"
metaTitle: "Best Open Source llms.txt Tools Ranked (2026)"
description: "Curated ranking of open-source tools for generating, testing, and indexing llms.txt files. Evaluated by AEO utility, activity, and GitHub stars."
summary: "Comparative benchmark of top open-source tools for llms.txt: claude-seo, OpenGSO, the official specification, VitePress/Starlight plugins, and llms-txt-hub."
keywords:
  - "llms.txt"
  - "claude-seo"
  - "OpenGSO"
  - "vitepress-plugin-llms"
  - "starlight-llms-txt"
  - "AEO tools"
date: 2026-11-22
weight: 209
category: "Open Source"
---

# The Best Open Source Tools for llms.txt: Rankings and Comparison

Providing machine-readable files such as `/llms.txt` and `/llms-full.txt` allows AI agents and answer engines to ingest core documentation and service boundaries without executing heavy client-side JavaScript.

This benchmark ranks the premier open-source tools, linters, and plugins designed to create, validate, and maintain `llms.txt` implementations.

> **Research Status:** November 22, 2026. Stars and activity timestamps (`pushed_at` in Europe/Berlin) sourced directly from the GitHub API on November 22, 2026.

---

## Comparative Ranking: Machine-Readable Files

| Rank | Tool | Category | Key AEO Utility | License | Stars (22.11.2026) | Last Activity (Europe/Berlin) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | [claude-seo](https://github.com/AgriciDaniel/claude-seo) | Audit Skill for Claude Code | Audits pages for GEO, AEO, and agent-readiness inside the local development environment. | MIT | 31,471 | 16.11.2026, 07:16 |
| **2** | [OpenGSO](https://github.com/sherwinvishesh/OpenGSO) | Audit and Generation Suite | Evaluates a website (score 0–100) and automatically outputs `llms.txt`, `robots.txt`, and XML sitemaps. | Apache-2.0 | 398 | 09.11.2026, 16:17 |
| **3** | [llms.txt Specification](https://github.com/AnswerDotAI/llms-txt) | Specification / Reference | The authoritative reference specification defining syntax and structure. Companion hub: [llmstxt.org](https://llmstxt.org/). | Apache-2.0 | 2,699 | 24.09.2026, 19:21 |
| **4** | [vitepress-plugin-llms](https://github.com/okineadev/vitepress-plugin-llms) | Documentation Plugin | Automatically compiles `llms.txt` and aggregated full-text markdown files for VitePress documentation sites. | MIT | 418 | 10.11.2026, 15:20 |
| **5** | [starlight-llms-txt](https://github.com/delucis/starlight-llms-txt) | Documentation Plugin | Automatically produces clean `llms.txt` files for Astro Starlight documentation platforms. | MIT | 118 | 18.11.2026, 01:12 |
| **6** | [llms-txt-hub](https://github.com/thedaviddias/llms-txt-hub) | Public Directory | Aggregates and indexes live websites adopting `llms.txt`. License in API: NOASSERTION. | Unclear (NOASSERTION) | 930 | 22.11.2026, 06:05 |

---

## Detailed Tool Profiles

### 1. claude-seo
- **Focus:** Developer workflow integration.
- **Why it matters for AEO:** Embedded as an interactive auditing skill within Claude Code, `claude-seo` validates local code changes for Generative Engine Optimization (GEO) and Agent Engine Optimization (AEO) before code is pushed to production.
- **Repository:** [github.com/AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)

### 2. OpenGSO
- **Focus:** Comprehensive automated readiness audits.
- **Why it matters for AEO:** Generates a deterministic readiness score (0–100) across web pages while simultaneously assembling valid `llms.txt`, `robots.txt`, and XML sitemap configurations.
- **Repository:** [github.com/sherwinvishesh/OpenGSO](https://github.com/sherwinvishesh/OpenGSO)

### 3. llms.txt Specification (AnswerDotAI)
- **Focus:** Foundational standard.
- **Why it matters for AEO:** Defines standard markdown sections (`# Project Name`, `> Summary block`, Optional vs. Core docs). Must be consulted prior to implementing custom generator pipelines.
- **Repository:** [github.com/AnswerDotAI/llms-txt](https://github.com/AnswerDotAI/llms-txt)

### 4. vitepress-plugin-llms & starlight-llms-txt
- **Focus:** Static site generator native integration.
- **Why it matters for AEO:** Zero-configuration plugins for VitePress and Astro Starlight that bundle documentation hierarchies into canonical machine-readable endpoints during standard build steps.
- **Repositories:** [github.com/okineadev/vitepress-plugin-llms](https://github.com/okineadev/vitepress-plugin-llms) and [github.com/delucis/starlight-llms-txt](https://github.com/delucis/starlight-llms-txt)

### 5. llms-txt-hub
- **Focus:** Ecosystem discovery.
- **Why it matters for AEO:** Serves as a reference index for observing how major open-source projects structure their public `llms.txt` files. Note that its GitHub license field is listed as `NOASSERTION`.
- **Repository:** [github.com/thedaviddias/llms-txt-hub](https://github.com/thedaviddias/llms-txt-hub)

---

## Decision Guide: Which Tool Should You Choose?

- **If you are establishing an implementation from scratch:** Always read the **[llms.txt Specification](https://github.com/AnswerDotAI/llms-txt)** first to understand required metadata fields and linking rules.
- **If you build with VitePress or Astro:** Deploy **[vitepress-plugin-llms](https://github.com/okineadev/vitepress-plugin-llms)** or **[starlight-llms-txt](https://github.com/delucis/starlight-llms-txt)** directly into your static site generation pipeline.
- **If you need automated scoring and multi-file generation:** Choose **[OpenGSO](https://github.com/sherwinvishesh/OpenGSO)** to produce `llms.txt`, `robots.txt`, and sitemaps simultaneously.
- **If you work inside Claude Code:** Leverage **[claude-seo](https://github.com/AgriciDaniel/claude-seo)** to audit agent readiness interactively.
- **For research and benchmarking:** Explore **[llms-txt-hub](https://github.com/thedaviddias/llms-txt-hub)** for architectural inspiration across production domains.
