---
title: "Código Aberto para Agent Engine Optimization (AEO)"
metaTitle: "Ferramentas Open Source para AEO: Repositórios e Modelos"
description: "Classificações e diretório de ferramentas open source, especificações, modelos e bases de dados para AEO. Dados de 22/11/2026."
summary: "Diretório de ferramentas open source para AEO: llms.txt, crawlers, dados estruturados, interfaces MCP, verificação de bots e modelos."
keywords:
  - "código aberto AEO"
  - "ferramentas llms.txt"
  - "Firecrawl"
  - "Model Context Protocol"
  - "Web Bot Auth"
date: 2026-11-22
weight: 208
category: "Código Aberto"
---

# Código Aberto para Agent Engine Optimization (AEO)

O ecossistema de AEO depende diretamente de software de código aberto: formatos padronizados, motores de extração, servidores de ferramentas (MCP) e modelos locais de teste.

> **Status da pesquisa:** 22 de novembro de 2026. Dados de GitHub e Hugging Face verificados via API em 22/11/2026.

---

## As seis categorias open source para AEO

1. **[Arquivos Legíveis por Máquinas (llms.txt e correlatos)](/pt/docs/open-source-machine-readable-files/)**  
   Ferramentas e especificações para `llms.txt` (claude-seo, OpenGSO e especificação de referência).

2. **[Crawlers e Extratores: O que os agentes veem](/pt/docs/open-source-crawlers-and-extractors/)**  
   Extração e conversão de páginas em Markdown limpo (Firecrawl, Crawl4AI, Jina Reader).

3. **[Dados Estruturados com Schema.org e JSON-LD](/pt/docs/open-source-structured-data/)**  
   Vocabulários oficiais e validação de entidades para agentes (schemaorg, schema-dts, extruct).

4. **[Interfaces de Agentes: MCP, WebMCP e Navegadores](/pt/docs/open-source-agent-interfaces/)**  
   Camada de execução com automação de navegador e SDKs MCP (browser-use, Playwright MCP, WebMCP).

5. **[Identidade e Tráfego de Agentes](/pt/docs/open-source-identity-and-agent-traffic/)**  
   Verificação de assinaturas (Web Bot Auth) e análise de tráfego de bots (AgentCake, mintlify/agent-traffic).

6. **[Modelos, Bases de Dados e Testes Locais](/pt/docs/open-source-models-datasets-and-local-tests/)**  
   Embeddings, rerankers e ambientes de validação (llama.cpp, GEO-bench, Mind2Web).

---

## Padrões e Referências

- **Paper Fundamental de GEO:** [arXiv:2311.09735](https://arxiv.org/abs/2311.09735).
- **Especificação llms.txt:** [llmstxt.org](https://llmstxt.org/).
- **RFC 9421:** [HTTP Message Signatures](https://www.rfc-editor.org/rfc/rfc9421).
