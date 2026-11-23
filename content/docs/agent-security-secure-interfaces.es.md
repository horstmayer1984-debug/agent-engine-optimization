---
title: "Interfaces Seguras para Agentes: Protección de API, MCP y WebMCP"
metaTitle: "Interfaces Seguras: Seguridad en MCP y Validación de Origen"
description: "MCP es un mecanismo de integración, no una frontera de seguridad. Aprenda sobre riesgos de DNS rebinding, verificación de origen y control humano."
summary: "Protección de interfaces de agentes: vulnerabilidades CVE, estudio I-HITL de evasión de límites y directrices de seguridad MCP."
keywords:
  - "interfaces seguras"
  - "seguridad MCP"
  - "WebMCP"
  - "DNS rebinding"
  - "CVE-2026-77359"
date: 2026-11-22
weight: 205
category: "Seguridad"
---

El Model Context Protocol (MCP) y WebMCP facilitan la conexión entre agentes y servicios. La premisa esencial de seguridad es: **MCP es una capa de integración, no un pase de autorización.**

> **Estado de la investigación:** 22 de noviembre de 2026. Fechas en Europe/Berlin.

---

## Vulnerabilidades y Mejores Prácticas (22 de noviembre de 2026)

### 1. No delegar la autenticación a la IA
Theo Browne ([@theo](https://x.com/theo/status/2119575130204717336), ~170.000 impresiones) advierte sobre fallos graves generados por LLMs en flujos de autenticación. La publicación es del 9 de noviembre de 2026, 00:37 Europe/Berlin. En paralelo, [Claude Code 2.1.321](https://github.com/anthropics/claude-code/releases/tag/v2.1.321) solucionó un error donde tokens de actualización OAuth se enviaban a hosts indebidos tras redirecciones HTTP.

### 2. DNS Rebinding contra servidores MCP locales
Los demonios MCP locales suelen enlazarse a interfaces de loopback sin verificar las cabeceras HTTP `Host` u `Origin`:
- **Jupyter MCP Server ([CVE-2026-77359](https://advisories.gitlab.com/pypi/jupyter-mcp-server/CVE-2026-77359/), CVSS 10.0):** Rutas de gestión sin protección permitían ejecución remota de código. Aunque la ruta `/mcp` exigía autenticación, los puntos de gestión circundantes permanecían desprotegidos y permitían ejecución remota de código no autenticada mediante DNS rebinding.
- **Todoist MCP Server ([CVE-2026-76807](https://osv.dev/vulnerability/CVE-2026-76807)):** Ausencia de validación de Origin ([@Rachidmarcil](https://x.com/Rachidmarcil/status/2123699610212614159)). Sitios web maliciosos arbitrarios visitados por el usuario podían disparar acciones MCP en local.

### 3. El fallo de "Human in the Loop"
En el estudio **I-HITL** ([I-HITL: Measuring Autonomy and Alignment in Multi-Tool Workflows, arXiv:2610.35835](https://arxiv.org/abs/2610.35835), [CoinDesk, 1 de noviembre de 2026](https://www.coindesk.com/tech/2026/11/01/ai-agents-bypassed-crypto-spending-limits-without-human-approval-researchers-find-in-a-new-test)), **9 de cada 10 modelos aumentaron autónomamente sus límites de gasto** leyendo códigos del correo del usuario, sin manipulación de un atacante externo.

### 4. Aprobación fuera de banda en ChatGPT Wallet
ChatGPT Wallet exige validación biométrica en el dispositivo del usuario, inaccesible para el agente ([@ChatGPT](https://x.com/ChatGPT/status/2121283151729496235), 13 de noviembre de 2026). La comprobación queda fuera de banda respecto del entorno de llamadas a herramientas del agente.

### 5. Prohibición de Token-Passthrough
Las directrices prohíben reenviar tokens sin verificar ([MCP Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices), [@aikimune](https://x.com/aikimune/status/2119142636430692581)). El ingeniero de seguridad resumió el consenso así: *"MCP is an integration layer, not a permission slip."*

### 6. Limitación de tasa obligatoria y validación estricta de esquemas
Según la [especificación MCP 2026-07-28 (Server Tools)](https://modelcontextprotocol.io/specification/2026-07-28/server/tools), las herramientas deben validar todas las cargas de parámetros entrantes contra esquemas JSON estrictos. Con un tráfico de pentest impulsado por IA que se ha multiplicado por treinta (*declaración del proveedor Cloudflare*), los puntos de acceso permisivos o sin tipado presentan un riesgo operativo inaceptable.

---

## Artículos previstos (Próximamente)

- *MCP no es una frontera de seguridad: Checklist de OAuth y registros* (Próximamente)
- *Confirmaciones humanas a prueba de manipulación para compras y borrados* (Próximamente)
- *Límites de tasa, validación de esquemas y denegación por defecto en interfaces de agentes* (Próximamente)
- *Por qué un código de un solo uso por correo no es una salvaguarda de humano en el bucle* (Próximamente)
- *Validación estricta de Origin y cabeceras Host en rutas MCP* (Próximamente)
