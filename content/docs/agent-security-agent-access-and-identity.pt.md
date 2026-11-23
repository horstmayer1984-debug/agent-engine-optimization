---
title: "Acesso e Identidade de Agentes: Como identificar e liberar agentes legítimos"
metaTitle: "Acesso e Identidade de Agentes: Web Bot Auth e RFC 9421"
description: "Como sites identificam agentes assinados criptograficamente, ajustam proteções antibot e atribuem identidades exclusivas."
summary: "Análise de acesso e identidade de agentes: Web Bot Auth, políticas da Cloudflare, ChatGPT Wallet e identidades exclusivas."
keywords:
  - "acesso de agentes"
  - "identidade de agentes"
  - "Web Bot Auth"
  - "RFC 9421"
  - "Cloudflare"
date: 2026-11-22
weight: 202
category: "Segurança"
---

# Acesso e Identidade de Agentes: Como identificar e liberar agentes legítimos

A proteção antibot moderna precisa barrar raspagens abusivas e ataques, mas sem bloquear agentes pessoais que compram em nome de clientes reais.

A governança exige validação criptográfica (Web Bot Auth / RFC 9421) e identidades segregadas para agentes.

> **Status da pesquisa:** 22 de novembro de 2026. Horários em Europe/Berlin.

---

## Fatos da Pesquisa (22 de novembro de 2026)

### 1. ChatGPT Wallet e Liberação de Agentes Assinados
A OpenAI requer explicitamente que lojas não bloqueiem os agentes Dots. No Cloudflare, configura-se em **Personal Agents** o item **"dots, OpenAI"** como **Allow (do not block)**, ou via regra WAF com Bot Detection ID `129220581` (ChatGPT Operator).

- **Post:** [@ChatGPT](https://x.com/ChatGPT/status/2121283151729496235), 13/11/2026, 17:44 Europe/Berlin (~1M visualizações).
- **Fontes:** [OpenAI ChatGPT Wallet](https://openai.com/index/introducing-chatgpt-wallet/), [OpenAI Dots](https://openai.com/index/introducing-dots/) e [OpenAI Agent Access](https://developers.openai.com/commerce/agent-access).
- **Protocolo:** [RFC 9421](https://www.rfc-editor.org/rfc/rfc9421), cabeçalhos `Signature`, `Signature-Input`, `Signature-Agent` (`"https://chatgpt.com"`).

### 2. Políticas Granulares na Cloudflare
Desde 4 de novembro de 2026, administradores podem definir regras específicas (Allow, Block, Block on pages with ads) para cada agente pessoal suportado ([Changelog Cloudflare](https://developers.cloudflare.com/changelog/post/2026-11-04-personal-agent-policies/)).

### 3. Assinatura Comprova o Provedor, Não o Usuário
Web Bot Auth autentica o operador da infraestrutura, mas não o cliente final. A Cloudflare lançou a iniciativa "Trusted Agent Delegation" ([Blog Cloudflare](https://blog.cloudflare.com/trusted-agent-delegation/), [draft-ietf-webbotauth-httpsig-protocol](https://datatracker.ietf.org/doc/draft-ietf-webbotauth-httpsig-protocol/)).

### 4. Identidade Própria para Agentes
- Alerta [@Cloudflare](https://x.com/Cloudflare/status/2118288470275674172): logins compartilhados comprometem logs de auditoria.
- Soluções de mercado: [Okta CIMD](https://www.okta.com/blog/product-innovation/okta-cimd-ai-agent-identity/), [Auth0](https://www.okta.com/newsroom/articles/auth0-may-2026-product-innovations/) e [Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/agent-identities).

### 5. WorkOS Agent Vault
Abordagem oposta que armazena senhas humanas para uso direto por agentes ([WorkOS](https://workos.com/docs/agent-vault)).

---

## Artigos Planejados (Em Breve)

- *Web Bot Auth Explicado: Como Verificar Agentes Assinados como ChatGPT Dots* (Em Breve)
- *Reconfiguração de Defesas Antibot Sem Bloquear Compras Legítimas* (Em Breve)
