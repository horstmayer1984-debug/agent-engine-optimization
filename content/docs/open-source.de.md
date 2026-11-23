---
title: "Open Source für Agent Engine Optimization (AEO)"
metaTitle: "Open Source AEO Tools: Repositories, Specs und Modelle"
description: "Kuratierte Rankings und Übersicht von Open-Source-Tools, Spezifikationen, Modellen und Datensätzen für AEO. Recherchestand: 22.11.2026."
summary: "Verzeichnis der Open-Source-Tools für AEO in sechs Kategorien: llms.txt, Crawler, strukturierte Daten, MCP-Schnittstellen, Bot-Verifikation und Modelle."
keywords:
  - "Open Source AEO"
  - "llms.txt Tools"
  - "Firecrawl"
  - "Model Context Protocol"
  - "Web Bot Auth"
  - "AEO Benchmarks"
date: 2026-11-22
weight: 208
category: "Open Source"
---

# Open Source für Agent Engine Optimization (AEO)

Das Ökosystem für Agent Engine Optimization (AEO) stützt sich maßgeblich auf Open-Source-Software: Spezifikationen für maschinenlesbare Dateien, Parsing-Bibliotheken, spezialisierte Crawler, Ausführungsprotokolle und lokale Testmodelle.

Diese Übersicht sammelt, kategorisiert und bewertet die wichtigsten GitHub-Repositories, Hugging-Face-Ressourcen und Standards für die Optimierung digitaler Präsenzen für autonome KI-Agents.

> **Stand der Recherche:** 22. November 2026. Alle genannten GitHub-Sterne, Lizenzen (SPDX-ID) und Zeitstempel (`pushed_at` in Europe/Berlin) stammen aus der offiziellen API-Abfrage vom 22.11.2026.
> 
> *Hinweis zur Methodik:* Die Reihenfolge in unseren Tabellen ist ein redaktionelles Ranking nach praktischem Nutzen für AEO, Entwicklungsaktivität und Popularität. Es handelt sich nicht um ein gemessenes Qualitätsurteil oder bezahlte Platzierungen.

---

## Die sechs Open-Source-Kategorien für AEO

Entdecken Sie unsere detaillierten Vergleichstabellen in den sechs Kernbereichen:

1. **[Maschinenlesbare Dateien (llms.txt und Verwandte)](/de/docs/open-source-machine-readable-files/)**  
   Werkzeuge, Generatoren und Referenzspezifikationen für `llms.txt` (u. a. claude-seo, OpenGSO und die offizielle Spezifikation).

2. **[Crawler und Extraktoren: Sehen, was Agents sehen](/de/docs/open-source-crawlers-and-extractors/)**  
   Tools, die Websites in sauberes, maschinenlesbares Markdown umwandeln (u. a. Firecrawl, Crawl4AI und Jina Reader).

3. **[Strukturierte Daten mit Schema.org und JSON-LD](/de/docs/open-source-structured-data/)**  
   Offizielle Vokabulare, TypeScript-Typen und Parser-Audit-Tools zur Modellierung eindeutiger Entitäten (schemaorg, schema-dts, extruct).

4. **[Agent-Schnittstellen: MCP, WebMCP und Agent-Browser](/de/docs/open-source-agent-interfaces/)**  
   Die Ausführungsebene: Browser-Automation, offizielle SDKs und Web-Standards (browser-use, Playwright MCP, WebMCP).

5. **[Identität und Agent-Traffic](/de/docs/open-source-identity-and-agent-traffic/)**  
   Kryptografische Signaturprüfung (Web Bot Auth) und Analysewerkzeuge zur Klassifizierung von Agent-Traffic (AgentCake, mintlify/agent-traffic).

6. **[Modelle, Datensätze und lokale Tests](/de/docs/open-source-models-datasets-and-local-tests/)**  
   Embeddings, Reranker, lokale Laufzeitumgebungen (llama.cpp, MLX) und akademische Benchmarks (GEO-bench, Mind2Web).

---

## Wichtige Papers und Standards

- **GEO Grundlagenpaper:** Aggarwal et al., [arXiv:2311.09735](https://arxiv.org/abs/2311.09735). Zugehöriges Repository: [GEO-optim/GEO](https://github.com/GEO-optim/GEO) (Apache-2.0, 352 Sterne, letzte Aktivität 30.10.2025, 03:55 Europe/Berlin).
- **Kritischer Überblick 2026:** [arXiv:2607.14035](https://arxiv.org/abs/2607.14035) — Die oft zitierten „+40 % Sichtbarkeit“ gelten nur unter eng definierten Testbedingungen.
- **Understanding ChatGPT Citations:** [arXiv:2610.15382](https://arxiv.org/abs/2610.15382).
- **GEOHunter (Manipulationsnetzwerke):** [arXiv:2611.26564](https://arxiv.org/abs/2611.26564) (19.11.2026).
- **llms.txt Spezifikation:** [AnswerDotAI/llms-txt](https://github.com/AnswerDotAI/llms-txt) und [llmstxt.org](https://llmstxt.org/).
- **HTTP Message Signatures:** [RFC 9421](https://www.rfc-editor.org/rfc/rfc9421) und IETF-Entwurf [draft-ietf-webbotauth-httpsig-protocol](https://datatracker.ietf.org/doc/draft-ietf-webbotauth-httpsig-protocol/).
- **Model Context Protocol:** [MCP Server Tools](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) und [MCP Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices).
- **WebMCP:** [W3C Spezifikationsentwurf](https://github.com/webmachinelearning/webmcp).

---

## Weitere in der Recherche erfasste Repositories

| Repository | URL | Sterne (22.11.2026) | Lizenz | Letzte Aktivität (Europe/Berlin) | Zweck |
| :--- | :--- | :--- | :--- | :--- | :--- |
| modelcontextprotocol/servers | https://github.com/modelcontextprotocol/servers | 92.155 | NOASSERTION | 19.11.2026, 17:41 | MCP Server Verzeichnis |
| modelcontextprotocol/modelcontextprotocol | https://github.com/modelcontextprotocol/modelcontextprotocol | 9.744 | NOASSERTION | 22.11.2026, 01:31 | Offizielle MCP-Spezifikation |
| firecrawl/llmstxt-generator | https://github.com/firecrawl/llmstxt-generator | 540 | keine Angabe | 17.06.2025, 14:37 | Generator-Tool |
| firecrawl/create-llmstxt-py | https://github.com/firecrawl/create-llmstxt-py | 327 | keine Angabe | 02.06.2025, 16:25 | Python-Skript |
| SecretiveShell/Awesome-llms-txt | https://github.com/SecretiveShell/Awesome-llms-txt | 112 | MIT | 18.10.2026, 10:46 | Linksammlung |
| langchain-ai/mcpdoc | https://github.com/langchain-ai/mcpdoc | 1.029 | MIT | 20.08.2026, 07:34 | MCP-Dokumentationstool |
| coleam00/mcp-crawl4ai-rag | https://github.com/coleam00/mcp-crawl4ai-rag | 2.267 | MIT | 25.07.2025, 16:17 | Crawl4AI MCP-Integration |
| executeautomation/mcp-playwright | https://github.com/executeautomation/mcp-playwright | 5.682 | MIT | 13.12.2025, 05:28 | Playwright Server |
| ServiceNow/WorkArena | https://github.com/ServiceNow/WorkArena | 281 | NOASSERTION | 28.09.2026, 20:31 | Unternehmens-Agent-Benchmark |
| invertase/docs.page | https://github.com/invertase/docs.page | 684 | Apache-2.0 | 19.11.2026, 11:04 | Dokumentations-Plattform |
