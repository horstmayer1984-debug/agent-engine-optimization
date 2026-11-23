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

Los agentes no solo extraen texto, sino que ejecutan intenciones. Esto expone el sistema a inyecciones indirectas de instrucciones, texto invisible y envenenamiento de descripciones de herramientas MCP.

> **Estado de la investigación:** 22 de noviembre de 2026. Fechas en Europe/Berlin.

---

## Datos e Investigaciones (22 de noviembre de 2026)

### 1. Campaña de Black-Hat GEO detectada por Unit 42
Unit 42 identificó 26 sitios fraudulentos con texto oculto (`display: none`) para desviar agentes hacia estafas de inversión ([@Unit42_Intel](https://x.com/Unit42_Intel/status/2120264510350991832), [IOCs de la campaña](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-11-06-IDPI-campaign.txt)). Unit 42 clasifica formalmente esta técnica como inyección indirecta de instrucciones basada en la web y Black-Hat GEO. La alerta es del 10 de noviembre de 2026, 22:17 Europe/Berlin; el texto invisible también emplea microtipografías.

- **Publicación de investigación:** [Fooling AI Agents: Web-Based Indirect Prompt Injection Observed in the Wild](https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/).

### 2. Envenenamiento de herramientas MCP
Alterar la descripción en lenguaje natural de una herramienta basta para manipular al LLM sin código ejecutable malicioso ([Thread @1PasswordDev](https://x.com/1PasswordDev/status/2122472408619852202), [OWASP MCP Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html)). El hilo es del 17 de noviembre de 2026, 00:30 Europe/Berlin (~132.000 impresiones). Basta con manipular la descripción en lenguaje natural para inducir la filtración de datos sensibles o acciones no previstas, sin binarios maliciosos.

- **Detalle del tool poisoning:** [https://x.com/1PasswordDev/status/2122473198147313902](https://x.com/1PasswordDev/status/2122473198147313902).
- **Orientación de 1Password:** [Where MCP fits and where it doesn’t](https://1password.com/blog/where-mcp-fits-and-where-it-doesnt).

### 3. Tasa de éxito del 22,9 % en pruebas empíricas
Un estudio sobre doce frameworks concluyó que el 22,9 % de los ataques de tool poisoning tuvieron éxito, sin defensas nativas en los frameworks ([MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study, arXiv:2611.03555](https://arxiv.org/abs/2611.03555)). Ninguno de los doce frameworks evaluados incorporaba una defensa intencional e integrada contra descripciones envenenadas.

### 4. Aislamiento de datos con IBM LLMON
IBM Granite 4.1 incorpora LLMON para separar instrucciones de datos pasivos ([LLMON: An LLM-Native Markup Language, now in Granite 4.1 3B and 8B](https://huggingface.co/blog/ibm-granite/llmon-an-llm-native-markup-language-now-in-granite)). LLMON indica al transformer que interprete el contenido externo recuperado estrictamente como datos pasivos y no como instrucciones ejecutables. IBM aclara que se trata de un comportamiento aprendido, no de un control de seguridad garantizado matemáticamente. Aplica a los modelos Granite 4.1 de 3B y de 8B.

### 5. La inyección de instrucciones sigue sin resolverse (OWASP LLM01)
- Prompt Injection encabeza el listado de [OWASP GenAI Top 10](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) y permanece en el puesto LLM01.
- Los vectores de ocultación documentados incluyen texto blanco sobre fondo blanco ([@Pksingh900](https://x.com/Pksingh900/status/2116788637019124196), 1 de noviembre de 2026, 08:05 Europe/Berlin), texto alternativo oculto en imágenes, capas de comentarios en PDF e invitaciones a reuniones.

### 6. Resiliencia emergente de los modelos y postura de los buscadores
- **Observaciones de campo:** Se han notificado casos ocasionales en los que un modelo reconoce instrucciones adversarias (por ejemplo, [@NoemiTitarenco](https://x.com/NoemiTitarenco/status/2119947195860361318), 10 de noviembre de 2026, 01:16 Europe/Berlin, donde un agente detectó e ignoró instrucciones ocultas en una página de Slack).
- Google sanciona estrictamente el texto oculto en sus [Políticas contra Spam](https://developers.google.com/search/docs/essentials/spam-policies). Esas políticas también prohíben el cloaking y la manipulación engañosa, y advierten de que intentar manipular los motores de respuesta con texto invisible puede acarrear acciones manuales severas.

---

## Artículos previstos (Próximamente)

- *Inyección indirecta de instrucciones: Cómo el texto oculto desvía agentes* (Próximamente)
- *Tool Poisoning en MCP: Cuando una descripción se convierte en exploit* (Próximamente)
- *Contenido limpio para agentes: lo que nunca debe aparecer en el código fuente* (Próximamente)
- *Black-Hat GEO es Prompt Injection* (Próximamente)
- *Auditar las descripciones de herramientas como dependencias de terceros* (Próximamente)
- *GEOHunter: cómo los sindicatos de GEO patrocinado manipulan los motores de respuesta (arXiv:2611.26564)* (Próximamente)
