---
title: "Prompt Injection e Conteúdo Manipulado: Proteção da camada de leitura"
metaTitle: "Prompt Injection em AEO: Black-Hat GEO e Tool Poisoning"
description: "Como textos ocultos, injeções indiretas e envenenamento de ferramentas desviam agentes de IA, e o que evitar no código-fonte."
summary: "Análise de injeção de prompt: descobertas da Unit 42 sobre Black-Hat GEO, envenenamento de ferramentas MCP e IBM LLMON."
keywords:
  - "prompt injection"
  - "Black-Hat GEO"
  - "envenenamento de ferramentas"
  - "OWASP LLM01"
date: 2026-11-22
weight: 204
category: "Segurança"
---

Modelos de linguagem interpretam textos como instruções. Ataques de injeção indireta utilizam texto oculto e descrições manipuladas de ferramentas para sequestrar o fluxo lógico dos agentes.

> **Status da pesquisa:** 22 de novembro de 2026.

---

## Evidências da Pesquisa (22 de novembro de 2026)

### 1. Black-Hat GEO em 26 Sites de Fraude
A Unit 42 localizou 26 páginas usando estilos CSS para ocultar comandos que forçam agentes a redirecionar usuários para plataformas falsas ([Unit 42](https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/)).

### 2. Envenenamento de Ferramentas MCP
Basta corromper o texto de descrição de uma ferramenta MCP para enganar o modelo ([1Password](https://1password.com/blog/where-mcp-fits-and-where-it-doesnt)).

### 3. Taxa de Sucesso de 22,9%
Estudo com 12 frameworks revelou 22,9% de vulnerabilidade a tool poisoning sem proteções integradas ([arXiv:2611.03555](https://arxiv.org/abs/2611.03555)).

### 4. IBM LLMON e OWASP
- IBM Granite 4.1 separa comandos de dados ([IBM Blog](https://huggingface.co/blog/ibm-granite/llmon-an-llm-native-markup-language-now-in-granite)).
- Injeção de prompt lidera o ranking [OWASP LLM01](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/).

---

## Artigos Planejados (Em Breve)

- *Injeção Indireta de Prompt: Como Textos Ocultos Desviam Agentes* (Em Breve)
- *Envenenamento de Ferramentas MCP na Cadeia de Suprimentos* (Em Breve)
