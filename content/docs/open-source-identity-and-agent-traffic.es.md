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

## Perfiles detallados

### 1. Web Bot Auth (Cloudflare)
- **Enfoque:** Autenticación criptográfica sobre HTTP.
- **Por qué importa para AEO:** Implementa el Internet-Draft del IETF [draft-ietf-webbotauth-httpsig-protocol](https://datatracker.ietf.org/doc/draft-ietf-webbotauth-httpsig-protocol/) y el [RFC 9421](https://www.rfc-editor.org/rfc/rfc9421). Permite que los servidores de origen verifiquen matemáticamente las peticiones HTTP firmadas de proveedores como OpenAI, sin mantener listas blancas de direcciones IP frágiles.
- **Repositorio:** [github.com/cloudflare/web-bot-auth](https://github.com/cloudflare/web-bot-auth)

### 2. AgentCake
- **Enfoque:** Observación de agentes a nivel de sesión.
- **Por qué importa para AEO:** A diferencia de las herramientas tradicionales de grabación de sesiones, que esperan movimientos de ratón humanos, AgentCake modela los recorridos programáticos del DOM y las evaluaciones rápidas de selectores propias de los agentes de navegador de IA.
- **Repositorio:** [github.com/tartini-ai/agent-traffic-analytics](https://github.com/tartini-ai/agent-traffic-analytics)

### 3. mintlify/agent-traffic y Botscent
- **Enfoque:** Clasificación de peticiones en el perímetro.
- **Por qué importa para AEO:** El clasificador de Mintlify aporta un componente de middleware esencial para separar la analítica entre tráfico humano y sintético, mientras que Botscent ofrece una biblioteca mínima integrable.
- **Repositorios:** [github.com/mintlify/agent-traffic](https://github.com/mintlify/agent-traffic) y [github.com/nalinbhardwaj/botscent](https://github.com/nalinbhardwaj/botscent)

### 4. AgentReady
- **Enfoque:** Auditoría heurística en fase temprana.
- **Por qué importa para AEO:** Útil para que los desarrolladores comprueben en local la accesibilidad básica para agentes (mediante `npx is-agentic`). Se trata de un proyecto en fase inicial sin licencia oficial declarada en la API de GitHub.
- **Repositorio:** [github.com/agentready-org/standard](https://github.com/agentready-org/standard)

---

## Recomendación Práctica

- Utilice **[Web Bot Auth](https://github.com/cloudflare/web-bot-auth)** para la validación perimetral de peticiones firmadas.
- Clasifique su tráfico de logs con **[mintlify/agent-traffic](https://github.com/mintlify/agent-traffic)**.
- Para comprender los recorridos de los agentes, integre **[AgentCake](https://github.com/tartini-ai/agent-traffic-analytics)** o **[mintlify/agent-traffic](https://github.com/mintlify/agent-traffic)** en la canalización de observabilidad.
- Para auditorías locales rápidas por CLI, pruebe **[AgentReady](https://github.com/agentready-org/standard)** (`npx is-agentic`), teniendo en cuenta su fase temprana de desarrollo.
