---
title: "Prompt Injection y Contenido Manipulado: Defensa de la capa de lectura"
metaTitle: "Prompt Injection en AEO: Black-Hat GEO y Tool Poisoning"
description: "Cómo el texto oculto, la inyección indirecta de instrucciones y el envenenamiento de herramientas desvían agentes de IA."
summary: "Análisis de prompt injection: hallazgos de Unit 42 sobre Black-Hat GEO, análisis de 1Password sobre MCP e investigación de IBM LLMON."
keywords:
  - "prompt injection"
  - "Black-Hat GEO"
  - "envenenamiento de herramientas"
  - "OWASP LLM01"
date: 2026-11-22
weight: 204
category: "Seguridad"
---

# Prompt Injection y Contenido Manipulado: Defensa de la capa de lectura

Los agentes no solo extraen texto, sino que ejecutan intenciones. Esto expone el sistema a inyecciones indirectas de instrucciones, texto invisible y envenenamiento de descripciones de herramientas MCP.

> **Estado de la investigación:** 22 de noviembre de 2026. Fechas en Europe/Berlin.

---

## Datos e Investigaciones (22 de noviembre de 2026)

### 1. Campaña de Black-Hat GEO detectada por Unit 42
Unit 42 identificó 26 sitios fraudulentos con texto oculto (`display: none`) para desviar agentes hacia estafas de inversión ([@Unit42_Intel](https://x.com/Unit42_Intel/status/2120264510350991832), [IOCs de la campaña](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-11-06-IDPI-campaign.txt)).

### 2. Envenenamiento de herramientas MCP
Alterar la descripción en lenguaje natural de una herramienta basta para manipular al LLM sin código ejecutable malicioso ([Thread @1PasswordDev](https://x.com/1PasswordDev/status/2122472408619852202), [OWASP MCP Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html)).

### 3. Tasa de éxito del 22,9 % en pruebas empíricas
Un estudio sobre doce frameworks concluyó que el 22,9 % de los ataques de tool poisoning tuvieron éxito, sin defensas nativas en los frameworks ([arXiv:2611.03555](https://arxiv.org/abs/2611.03555)).

### 4. Aislamiento de datos con IBM LLMON
IBM Granite 4.1 incorpora LLMON para separar instrucciones de datos pasivos ([Hugging Face Blog](https://huggingface.co/blog/ibm-granite/llmon-an-llm-native-markup-language-now-in-granite)).

### 5. OWASP Top 10 y Políticas de Google
- Prompt Injection encabeza el listado de [OWASP GenAI Top 10](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/).
- Google sanciona estrictamente el texto oculto en sus [Políticas contra Spam](https://developers.google.com/search/docs/essentials/spam-policies).

---

## Artículos previstos (Próximamente)

- *Inyección indirecta de instrucciones: Cómo el texto oculto desvía agentes* (Próximamente)
- *Tool Poisoning en MCP: Cuando una descripción se convierte en exploit* (Próximamente)
- *Black-Hat GEO es Prompt Injection* (Próximamente)
