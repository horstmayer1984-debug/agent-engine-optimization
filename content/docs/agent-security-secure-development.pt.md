---
title: "Desenvolvimento Seguro na Era da IA: Proteção de credenciais e agentes de código"
metaTitle: "Desenvolvimento Seguro com IA: Vazamentos de Secrets e Phishing"
description: "Como assistentes de código expõem segredos, isolamento de agentes de teste, phishing de código de dispositivo e cópias maliciosas."
summary: "Análise de segurança no desenvolvimento com IA: vazamentos no Claude Code, testes da GitGuardian e phishing de código de dispositivo."
keywords:
  - "desenvolvimento seguro"
  - "agentes de código"
  - "vazamentos Claude Code"
  - "GitGuardian"
  - "device-code phishing"
date: 2026-11-22
weight: 207
category: "Segurança"
---

# Desenvolvimento Seguro na Era da IA: Proteção de credenciais e agentes de código

Assistentes de código agilizam a entrega mas criam riscos severos de vazamento de credenciais locais e exploração automatizada de repositórios.

> **Status da pesquisa:** 22 de novembro de 2026.

---

## Casos Recentes (22 de novembro de 2026)

### 1. Vazamentos de Tokens no Claude Code
Apiiro encontrou **1.122 repositórios públicos** com credenciais expostas em `.claude/settings.local.json` após uso da opção "Don't ask again" ([The Hacker News](https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html), [GitLab](https://about.gitlab.com/blog/prevent-leaks-from-claude-code-dont-ask-again-file/)).

### 2. Descoberta de Secrets em Minutos
Laboratório GitGuardian demonstrou que um build do ARTEX capturou 8 de 9 segredos ocultos, mesmo deletados do Git ([GitGuardian](https://blog.gitguardian.com/an-artex-build-ships-no-secret-scanner-in-our-lab-it-found-the-secrets-anyway/), [Microsoft](https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/)).

### 3. Phishing de Código de Dispositivo
Alerta da Microsoft sobre sequestro de permissões de desenvolvedores via fluxos de autenticação de dispositivos ([Microsoft Security](https://www.microsoft.com/en-us/security/blog/2026/11/17/the-risks-of-device-code-authentication-for-ai-coding-agents/)).

### 4. Cópias Maliciosas de ARTEX
Imagem Docker infectada com backdoor root foi baixada cerca de 8.000 vezes ([BadByte](https://badbyte.io/artex-backdoor-docker-image/)).

---

## Artigos Planejados (Em Breve)

- *Vulnerabilidades em Vibe Coding: Limpeza de `.env`, `.git` e Logs* (Em Breve)
- *Por Que a Lógica de Autenticação Não Deve Ser Gerada Exclusivamente por IA* (Em Breve)
