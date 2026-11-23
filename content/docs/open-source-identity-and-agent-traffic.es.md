---
title: "Detección y Verificación de Visitas de Agentes: Mejores herramientas open source"
metaTitle: "Herramientas para verificar tráfico de agentes IA (2026)"
description: "Herramientas open source para identificar y verificar tráfico de agentes: Web Bot Auth, AgentCake, mintlify/agent-traffic, Botscent y AgentReady."
summary: "Guía práctica para detectar agentes: verificación criptográfica RFC 9421, repetición de sesiones y clasificación de tráfico."
keywords:
  - "Web Bot Auth"
  - "AgentCake"
  - "mintlify agent-traffic"
  - "verificación de agentes"
date: 2026-11-22
weight: 213
category: "Código Abierto"
---

# Detección y Verificación de Visitas de Agentes: Mejores herramientas open source

Los análisis web convencionales no distinguen eficazmente entre usuarios humanos y agentes autónomos.

> **Estado de la investigación:** 22 de noviembre de 2026. Datos oficiales de la API de GitHub (Europe/Berlin).

---

## Tabla Comparativa: Identificación de Agentes

| Rango | Herramienta | Categoría | Utilidad para AEO | Licencia | Estrellas (22.11.2026) | Última Actividad (Europe/Berlin) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | [Web Bot Auth](https://github.com/cloudflare/web-bot-auth) | Verificación de firma | Valida criptográficamente peticiones de agentes legítimos (RFC 9421). | Apache-2.0 | 186 | 21.11.2026, 20:46 |
| **2** | [AgentCake](https://github.com/tartini-ai/agent-traffic-analytics) | Analítica y Replay | Analítica y repetición de sesiones específica para agentes de IA. | MIT | 91 | 21.11.2026, 15:03 |
| **3** | [mintlify/agent-traffic](https://github.com/mintlify/agent-traffic) | Clasificador | Clasifica peticiones en agentes, rastreadores y humanos. | MIT | 88 | 10.11.2026, 19:43 |
| **4** | [Botscent](https://github.com/nalinbhardwaj/botscent) | Librería de detección | Detección ligera basada en comportamiento. | MIT | 35 | 11.11.2026, 17:13 |
| **5** | [AgentReady](https://github.com/agentready-org/standard) | Test de preparación | Chequeo rápido mediante `npx is-agentic`. Licencia no especificada. | Sin datos | 65 | 11.11.2026, 23:50 |

---

## Recomendación Práctica

- Utilice **[Web Bot Auth](https://github.com/cloudflare/web-bot-auth)** para la validación perimetral de peticiones firmadas.
- Clasifique su tráfico de logs con **[mintlify/agent-traffic](https://github.com/mintlify/agent-traffic)**.
