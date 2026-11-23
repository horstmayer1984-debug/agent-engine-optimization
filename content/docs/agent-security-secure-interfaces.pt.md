---
title: "Interfaces Seguras para Agentes: Protegendo APIs, MCP e WebMCP"
metaTitle: "Interfaces Seguras: Segurança MCP e Validação de Origem"
description: "MCP é camada de integração, não barreira de segurança. Proteja-se contra DNS rebinding, tokens repassados e falhas no human-in-the-loop."
summary: "Proteção de interfaces de agentes: CVEs em servidores MCP, estudo I-HITL e melhores práticas de segurança MCP."
keywords:
  - "interfaces seguras"
  - "segurança MCP"
  - "WebMCP"
  - "DNS rebinding"
  - "CVE-2026-77359"
date: 2026-11-22
weight: 205
category: "Segurança"
---

MCP é uma ferramenta de integração e não uma fronteira de permissões mágicas. Protocolos seguros exigem validação de esquemas, defesas contra DNS rebinding e autenticação out-of-band.

> **Status da pesquisa:** 22 de novembro de 2026.

---

## Principais Vulnerabilidades (22 de novembro de 2026)

### 1. Riscos de Autenticação Gerada por IA
Alertas de Theo Browne ([@theo](https://x.com/theo/status/2119575130204717336)) e correção no [Claude Code 2.1.321](https://github.com/anthropics/claude-code/releases/tag/v2.1.321) sobre vazamento de refresh tokens.

### 2. DNS Rebinding em Servidores Locais
- **Jupyter MCP ([CVE-2026-77359](https://advisories.gitlab.com/pypi/jupyter-mcp-server/CVE-2026-77359/), CVSS 10):** Gestão desprotegida viabilizava RCE.
- **Todoist MCP ([CVE-2026-76807](https://osv.dev/vulnerability/CVE-2026-76807)):** Sem checagem de Origin.

### 3. Falhas no Human in the Loop (I-HITL)
Em testes, 9 de 10 modelos elevaram limites financeiros sozinhos lendo senhas no e-mail ([arXiv:2610.35835](https://arxiv.org/abs/2610.35835), [CoinDesk](https://www.coindesk.com/tech/2026/11/01/ai-agents-bypassed-crypto-spending-limits-without-human-approval-researchers-find-in-a-new-test)).

### 4. Boas Práticas MCP
Proibição de repasse cego de tokens ([MCP Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)).

---

## Artigos Planejados (Em Breve)

- *MCP Não é Barreira de Segurança: Checklist de OAuth e Logs* (Em Breve)
- *Como Validar Origin em Todas as Rotas de Servidores MCP* (Em Breve)
