---
title: "Código Abierto para Agent Engine Optimization (AEO)"
metaTitle: "Herramientas Open Source para AEO: Repositorios y Modelos"
description: "Rankings seleccionados y directorio de herramientas de código abierto, especificaciones, modelos y conjuntos de datos para AEO. Datos al 22/11/2026."
summary: "Directorio de herramientas open source para AEO: llms.txt, crawlers, datos estructurados, interfaces MCP, verificación de bots y modelos."
keywords:
  - "código abierto AEO"
  - "herramientas llms.txt"
  - "Firecrawl"
  - "Model Context Protocol"
  - "Web Bot Auth"
date: 2026-11-22
weight: 208
category: "Código Abierto"
---

El ecosistema de AEO se apoya en especificaciones abiertas, librerías de extracción, servidores MCP y modelos de evaluación local.

Este directorio reúne y clasifica las herramientas más relevantes para la optimización de sitios web ante agentes autónomos de IA.

> **Estado de la investigación:** 22 de noviembre de 2026. Datos de GitHub consultados vía API el 22/11/2026 (Europe/Berlin).
>
> *Nota metodológica:* Los rankings son evaluaciones editoriales que priorizan la utilidad práctica para AEO, la actividad de mantenimiento y la adopción. No constituyen premios formales de benchmark ni listados patrocinados.

---

## Las seis categorías de código abierto para AEO

1. **[Archivos legibles por máquinas (llms.txt y afines)](/es/docs/open-source-machine-readable-files/)**  
   Herramientas para generar y auditar `llms.txt` (claude-seo, OpenGSO, especificación oficial).

2. **[Crawlers y Extractores: Ver lo que ven los agentes](/es/docs/open-source-crawlers-and-extractors/)**  
   Conversión de páginas en Markdown limpio y estructurado (Firecrawl, Crawl4AI, Jina Reader).

3. **[Datos Estructurados con Schema.org y JSON-LD](/es/docs/open-source-structured-data/)**  
   Tipos TypeScript, vocabularios y comprobación de entidades (schemaorg, schema-dts, extruct).

4. **[Interfaces de Agentes: MCP, WebMCP y Navegadores](/es/docs/open-source-agent-interfaces/)**  
   Protocolos de ejecución y herramientas de prueba (browser-use, Playwright MCP, WebMCP).

5. **[Identidad y Tráfico de Agentes](/es/docs/open-source-identity-and-agent-traffic/)**  
   Verificación criptográfica de peticiones (Web Bot Auth) y analítica de tráfico (AgentCake, mintlify/agent-traffic).

6. **[Modelos, Datasets y Pruebas Locales](/es/docs/open-source-models-datasets-and-local-tests/)**  
   Modelos de embeddings, rerankers y benchmarks de evaluación (GEO-bench, Mind2Web).

---

## Publicaciones y Estándares de Referencia

- **Artículo seminal sobre GEO:** Aggarwal et al., [arXiv:2311.09735](https://arxiv.org/abs/2311.09735). Código asociado: [GEO-optim/GEO](https://github.com/GEO-optim/GEO) (Apache-2.0, 352 estrellas, última actividad el 30.10.2025, 03:55 Europe/Berlin).
- **Evaluación crítica de 2026:** [arXiv:2607.14035](https://arxiv.org/abs/2607.14035) — demuestra que las afirmaciones ampliamente citadas de «+40 % de visibilidad» solo se aplican en condiciones de laboratorio restringidas.
- **Understanding ChatGPT Citations:** [arXiv:2610.15382](https://arxiv.org/abs/2610.15382).
- **GEOHunter (manipulación sindicada):** [arXiv:2611.26564](https://arxiv.org/abs/2611.26564) (19 de noviembre de 2026).
- **Especificación llms.txt:** [AnswerDotAI/llms-txt](https://github.com/AnswerDotAI/llms-txt) y [llmstxt.org](https://llmstxt.org/).
- **Firmas de Mensajes HTTP:** [RFC 9421](https://www.rfc-editor.org/rfc/rfc9421) y el borrador IETF [draft-ietf-webbotauth-httpsig-protocol](https://datatracker.ietf.org/doc/draft-ietf-webbotauth-httpsig-protocol/).
- **Model Context Protocol:** [especificación MCP](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) y [MCP Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices).
- **WebMCP (borrador del W3C):** [webmachinelearning/webmcp](https://github.com/webmachinelearning/webmcp).

---

## Repositorios adicionales monitorizados

Los siguientes repositorios se registraron durante la auditoría de investigación del 22 de noviembre de 2026:

| Repositorio | URL | Estrellas (22.11.2026) | Licencia | Última actividad (Europe/Berlin) | Enfoque |
| :--- | :--- | :--- | :--- | :--- | :--- |
| modelcontextprotocol/servers | https://github.com/modelcontextprotocol/servers | 92.155 | NOASSERTION | 19.11.2026, 17:41 | Registro de referencia de servidores MCP |
| modelcontextprotocol/modelcontextprotocol | https://github.com/modelcontextprotocol/modelcontextprotocol | 9.744 | NOASSERTION | 22.11.2026, 01:31 | Especificaciones centrales del protocolo |
| firecrawl/llmstxt-generator | https://github.com/firecrawl/llmstxt-generator | 540 | None in API | 17.06.2025, 14:37 | Utilidad generadora |
| firecrawl/create-llmstxt-py | https://github.com/firecrawl/create-llmstxt-py | 327 | None in API | 02.06.2025, 16:25 | Herramienta CLI en Python |
| SecretiveShell/Awesome-llms-txt | https://github.com/SecretiveShell/Awesome-llms-txt | 112 | MIT | 18.10.2026, 10:46 | Catálogo seleccionado |
| langchain-ai/mcpdoc | https://github.com/langchain-ai/mcpdoc | 1.029 | MIT | 20.08.2026, 07:34 | Herramientas de documentación MCP |
| coleam00/mcp-crawl4ai-rag | https://github.com/coleam00/mcp-crawl4ai-rag | 2.267 | MIT | 25.07.2025, 16:17 | Integración MCP de Crawl4AI |
| executeautomation/mcp-playwright | https://github.com/executeautomation/mcp-playwright | 5.682 | MIT | 13.12.2025, 05:28 | Servidor Playwright |
| ServiceNow/WorkArena | https://github.com/ServiceNow/WorkArena | 281 | NOASSERTION | 28.09.2026, 20:31 | Benchmark de agentes empresariales |
| invertase/docs.page | https://github.com/invertase/docs.page | 684 | Apache-2.0 | 19.11.2026, 11:04 | Plataforma de publicación de documentación |
