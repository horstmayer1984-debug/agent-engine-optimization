---
title: "Open Source for Agent Engine Optimization (AEO)"
metaTitle: "Open Source AEO Tools: Repositories, Specs, and Models"
description: "Curated rankings and catalog of open-source tools, specifications, models, and datasets for Agent Engine Optimization (AEO). Verified data as of Nov 22, 2026."
summary: "Directory of open-source AEO tools across six categories: llms.txt, crawlers, structured data, MCP interfaces, bot verification, and local test models."
keywords:
  - "Open Source AEO"
  - "llms.txt tools"
  - "Firecrawl"
  - "Model Context Protocol"
  - "Web Bot Auth"
  - "AEO benchmarks"
date: 2026-11-22
weight: 208
category: "Open Source"
---

# Open Source for Agent Engine Optimization (AEO)

The ecosystem for Agent Engine Optimization relies heavily on transparent, open-source software: specifications, parser libraries, crawler emulators, execution protocols, and local testing models.

This directory collects, evaluates, and ranks open-source repositories from GitHub, Hugging Face models, and standard specifications that enable web architectures to become agent-ready.

> **Research Status:** November 22, 2026. All GitHub stars, licenses (SPDX), and push timestamps (Europe/Berlin) reflect official API queries dated November 22, 2026.
> 
> *Note on Methodology:* Rankings represent editorial evaluations prioritizing practical utility for AEO, maintenance activity, and adoption. They do not constitute formal benchmark awards or sponsored listings.

---

## The Six Open-Source AEO Categories

Explore our detailed comparative rankings across the six foundational pillars of AEO tooling:

1. **[Machine-Readable Files (llms.txt and Relatives)](/docs/open-source-machine-readable-files/)**  
   Generators, linters, and specifications for `llms.txt` and developer documentation hubs (featuring claude-seo, OpenGSO, and official reference specs).

2. **[Crawlers and Extractors: Seeing What Agents See](/docs/open-source-crawlers-and-extractors/)**  
   Tools that simulate how LLMs parse and clean web content into structured Markdown (featuring Firecrawl, Crawl4AI, and Jina Reader).

3. **[Structured Data with Schema.org and JSON-LD](/docs/open-source-structured-data/)**  
   TypeScript definitions, official vocabularies, and extraction auditors for machine-readable entities (schemaorg, schema-dts, extruct).

4. **[Agent Interfaces: MCP, WebMCP, and Agent Browsers](/docs/open-source-agent-interfaces/)**  
   The execution layer: browser automation engines, official Model Context Protocol SDKs, and browser integration trials (browser-use, Playwright MCP, WebMCP).

5. **[Detecting and Verifying AI Agent Visits](/docs/open-source-identity-and-agent-traffic/)**  
   Cryptographic signature verification (Web Bot Auth / RFC 9421) and specialized agent traffic analytics (AgentCake, mintlify/agent-traffic).

6. **[Models, Datasets, and Local Testing Environments](/docs/open-source-models-datasets-and-local-tests/)**  
   Embeddings, rerankers, local inference runtimes (llama.cpp, MLX), and academic evaluation benchmarks (GEO-bench, Mind2Web).

---

## Core Research Papers and Standards

Foundational standards and academic evaluations governing AEO architectures:

- **Generative Engine Optimization (GEO):** Aggarwal et al., [arXiv:2311.09735](https://arxiv.org/abs/2311.09735). Accompanying code: [GEO-optim/GEO](https://github.com/GEO-optim/GEO) (Apache-2.0, 352 stars, last activity October 30, 2025, 03:55 Europe/Berlin).
- **Critical Evaluation 2026:** [arXiv:2607.14035](https://arxiv.org/abs/2607.14035) — demonstrating that widely cited "+40% visibility" claims apply only under constrained laboratory conditions.
- **Understanding ChatGPT Citations:** [arXiv:2610.15382](https://arxiv.org/abs/2610.15382).
- **GEOHunter (Syndicated Manipulation):** [arXiv:2611.26564](https://arxiv.org/abs/2611.26564) (November 19, 2026).
- **llms.txt Specification:** [AnswerDotAI/llms-txt](https://github.com/AnswerDotAI/llms-txt) and [llmstxt.org](https://llmstxt.org/).
- **HTTP Message Signatures:** [RFC 9421](https://www.rfc-editor.org/rfc/rfc9421) and IETF draft [draft-ietf-webbotauth-httpsig-protocol](https://datatracker.ietf.org/doc/draft-ietf-webbotauth-httpsig-protocol/).
- **Model Context Protocol:** [MCP Specification](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) and [MCP Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices).
- **WebMCP (W3C Draft):** [webmachinelearning/webmcp](https://github.com/webmachinelearning/webmcp).

---

## Additional Monitored Repositories

The following repositories were tracked during our November 22, 2026 research audit:

| Repository | URL | Stars (22.11.2026) | License | Last Activity (Europe/Berlin) | Focus |
| :--- | :--- | :--- | :--- | :--- | :--- |
| modelcontextprotocol/servers | https://github.com/modelcontextprotocol/servers | 92,155 | NOASSERTION | 19.11.2026, 17:41 | Reference MCP server registry |
| modelcontextprotocol/modelcontextprotocol | https://github.com/modelcontextprotocol/modelcontextprotocol | 9,744 | NOASSERTION | 22.11.2026, 01:31 | Core protocol specifications |
| firecrawl/llmstxt-generator | https://github.com/firecrawl/llmstxt-generator | 540 | None in API | 17.06.2025, 14:37 | Generator utility |
| firecrawl/create-llmstxt-py | https://github.com/firecrawl/create-llmstxt-py | 327 | None in API | 02.06.2025, 16:25 | Python CLI tool |
| SecretiveShell/Awesome-llms-txt | https://github.com/SecretiveShell/Awesome-llms-txt | 112 | MIT | 18.10.2026, 10:46 | Curated catalog |
| langchain-ai/mcpdoc | https://github.com/langchain-ai/mcpdoc | 1,029 | MIT | 20.08.2026, 07:34 | MCP documentation tools |
| coleam00/mcp-crawl4ai-rag | https://github.com/coleam00/mcp-crawl4ai-rag | 2,267 | MIT | 25.07.2025, 16:17 | Crawl4AI MCP integration |
| executeautomation/mcp-playwright | https://github.com/executeautomation/mcp-playwright | 5,682 | MIT | 13.12.2025, 05:28 | Playwright server |
| ServiceNow/WorkArena | https://github.com/ServiceNow/WorkArena | 281 | NOASSERTION | 28.09.2026, 20:31 | Enterprise agent benchmark |
| invertase/docs.page | https://github.com/invertase/docs.page | 684 | Apache-2.0 | 19.11.2026, 11:04 | Docs publishing platform |
