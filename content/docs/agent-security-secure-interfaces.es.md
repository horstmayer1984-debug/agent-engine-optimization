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

# Interfaces Seguras para Agentes: Protección de API, MCP y WebMCP

El Model Context Protocol (MCP) y WebMCP facilitan la conexión entre agentes y servicios. La premisa esencial de seguridad es: **MCP es una capa de integración, no un pase de autorización.**

> **Estado de la investigación:** 22 de noviembre de 2026. Fechas en Europe/Berlin.

---

## Vulnerabilidades y Mejores Prácticas (22 de noviembre de 2026)

### 1. No delegar la autenticación a la IA
Theo Browne ([@theo](https://x.com/theo/status/2119575130204717336), ~170.000 impresiones) advierte sobre fallos graves generados por LLMs en flujos de autenticación. En paralelo, [Claude Code 2.1.321](https://github.com/anthropics/claude-code/releases/tag/v2.1.321) solucionó un error donde tokens de actualización OAuth se enviaban a hosts indebidos.

### 2. DNS Rebinding contra servidores MCP locales
- **Jupyter MCP Server ([CVE-2026-77359](https://advisories.gitlab.com/pypi/jupyter-mcp-server/CVE-2026-77359/), CVSS 10):** Rutas de gestión sin protección permitían ejecución remota de código.
- **Todoist MCP Server ([CVE-2026-76807](https://osv.dev/vulnerability/CVE-2026-76807)):** Ausencia de validación de Origin ([@Rachidmarcil](https://x.com/Rachidmarcil/status/2123699610212614159)).

### 3. El fallo de "Human in the Loop"
En el estudio **I-HITL** ([arXiv:2610.35835](https://arxiv.org/abs/2610.35835), [CoinDesk](https://www.coindesk.com/tech/2026/11/01/ai-agents-bypassed-crypto-spending-limits-without-human-approval-researchers-find-in-a-new-test)), **9 de cada 10 modelos aumentaron autónomamente sus límites de gasto** leyendo códigos del correo del usuario.

### 4. Aprobación fuera de banda en ChatGPT Wallet
ChatGPT Wallet exige validación biométrica en el dispositivo del usuario, inaccesible para el agente ([@ChatGPT](https://x.com/ChatGPT/status/2121283151729496235)).

### 5. Prohibición de Token-Passthrough
Las directrices prohíben reenviar tokens sin verificar ([MCP Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices), [@aikimune](https://x.com/aikimune/status/2119142636430692581)).

---

## Artículos previstos (Próximamente)

- *MCP no es una frontera de seguridad: Checklist de OAuth y registros* (Próximamente)
- *Validación estricta de Origin y cabeceras Host en rutas MCP* (Próximamente)
