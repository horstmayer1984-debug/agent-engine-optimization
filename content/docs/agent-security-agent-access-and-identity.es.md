---
title: "Acceso e Identidad de Agentes: Reconocimiento y verificación de agentes de IA"
metaTitle: "Acceso e Identidad de Agentes: Web Bot Auth y RFC 9421"
description: "Cómo los sitios web reconocen agentes firmados criptográficamente, configuran la protección antibot y asignan identidades dedicadas."
summary: "Análisis de acceso e identidad de agentes: Web Bot Auth, políticas de Cloudflare, ChatGPT Wallet e identidades dedicadas."
keywords:
  - "acceso de agentes"
  - "identidad de agentes"
  - "Web Bot Auth"
  - "RFC 9421"
  - "Cloudflare"
date: 2026-11-22
weight: 202
category: "Seguridad"
---

# Acceso e Identidad de Agentes: Reconocimiento y verificación de agentes de IA

Los sitios web deben actualizar sus defensas perimetrales: es imperativo bloquear scrapers y ataques automatizados, pero sin cerrar la puerta a clientes legítimos que compran mediante agentes personales de IA.

Un esquema de acceso seguro se basa en la verificación criptográfica de firmas, políticas granulares en el edge y la creación de identidades dedicadas para agentes en lugar de reutilizar credenciales humanas.

> **Estado de la investigación:** 22 de noviembre de 2026. Fechas y datos verificados en Europe/Berlin.

---

## Tendencias Actuales (Investigación del 22 de noviembre de 2026)

### 1. ChatGPT Wallet exige admitir agentes firmados
OpenAI solicita expresamente que los sistemas antibot no bloqueen a los agentes Dots. En Cloudflare, la guía de OpenAI indica configurar en **Personal Agents** la opción **"dots, OpenAI"** como **Allow (do not block)**, o aplicar una regla WAF con el identificador Bot Detection ID `129220581` (ChatGPT Operator).

- **Publicación en X:** [@ChatGPT](https://x.com/ChatGPT/status/2121283151729496235), 13/11/2026, 17:44 Europe/Berlin (~1 millón de impresiones).
- **Fuentes oficiales:** [OpenAI, Introducing ChatGPT Wallet](https://openai.com/index/introducing-chatgpt-wallet/), [OpenAI, Introducing Dots](https://openai.com/index/introducing-dots/) y [OpenAI, Help ensure cloud browser access](https://developers.openai.com/commerce/agent-access).
- **Protocolo:** Web Bot Auth con [RFC 9421](https://www.rfc-editor.org/rfc/rfc9421), encabezados `Signature`, `Signature-Input`, `Signature-Agent` (`"https://chatgpt.com"`) y directorio de claves públicas en `https://chatgpt.com/.well-known/http-message-signatures-directory`.

### 2. Control granular de Personal Agents en Cloudflare
Desde el 4 de noviembre de 2026, Cloudflare permite autorizar o bloquear agentes personales de forma individual (**Allow**, **Block**, **Block on pages with ads**).

- **Registro de cambios:** [Granular access controls for Personal Agents, 4/11/2026](https://developers.cloudflare.com/changelog/post/2026-11-04-personal-agent-policies/)
- **Documentación:** [AI Crawler and Agent access policies](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/) y [Web Bot Auth en Cloudflare](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/).

### 3. La firma identifica al operador, no al cliente
Web Bot Auth garantiza que la petición proviene de un operador reconocido (ej. OpenAI), pero no la identidad del usuario final ni sus permisos de gasto. Cloudflare ha lanzado la iniciativa "Trusted Agent Delegation" para abordar este desafío.

- **Blog técnico:** [Agents aren’t humans (but they kinda are), 5/11/2026](https://blog.cloudflare.com/trusted-agent-delegation/)
- **Estándares:** Borrador IETF [draft-ietf-webbotauth-httpsig-protocol](https://datatracker.ietf.org/doc/draft-ietf-webbotauth-httpsig-protocol/) y [RFC 9421](https://www.rfc-editor.org/rfc/rfc9421).

### 4. Identidades dedicadas para agentes frente a inicios de sesión prestados
- **Riesgo:** [@Cloudflare](https://x.com/Cloudflare/status/2118288470275674172), 5/11/2026 señala que operar agentes con cuentas de empleados vulnera la trazabilidad de auditoría.
- **Implementaciones:** [Okta Agent Identity / CIMD](https://www.okta.com/blog/product-innovation/okta-cimd-ai-agent-identity/), [Auth0](https://www.okta.com/newsroom/articles/auth0-may-2026-product-innovations/) y [Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/agent-identities).

### 5. Enfoque alternativo: WorkOS Agent Vault
WorkOS ofrece Agent Vault, donde los usuarios almacenan credenciales directas para que los agentes inicien sesión ([WorkOS Docs](https://workos.com/docs/agent-vault)).

---

## Artículos previstos (Próximamente)

- *Web Bot Auth explicado: Cómo verificar agentes firmados como ChatGPT Dots* (Próximamente)
- *Ajuste de protección antibot sin bloquear clientes de agentes que pagan* (Próximamente)
- *Identidades propias para agentes frente a inicios de sesión compartidos* (Próximamente)
- *La firma muestra al operador, no al cliente* (Próximamente)
