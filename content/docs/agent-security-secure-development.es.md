---
title: "Desarrollo Seguro en la Era de la IA: Protección de credenciales y agentes de código"
metaTitle: "Desarrollo Seguro con IA: Fugas de Secrets y Phishing"
description: "Cómo los asistentes de código exponen secretos, aislamiento de agentes de prueba, phishing de código de dispositivo y forks maliciosos."
summary: "Análisis de seguridad en desarrollo con IA: fugas en Claude Code, pruebas de GitGuardian y ataques de phishing de dispositivo."
keywords:
  - "desarrollo seguro"
  - "agentes de código"
  - "fugas Claude Code"
  - "GitGuardian"
  - "device-code phishing"
date: 2026-11-22
weight: 207
category: "Seguridad"
---

# Desarrollo Seguro en la Era de la IA: Protección de credenciales y agentes de código

El uso de asistentes de código (Claude Code, Cursor, Copilot) acelera el desarrollo pero introduce nuevos vectores: credenciales expuestas en archivos locales, escaneo automatizado en GitHub y phishing de código de dispositivo.

> **Estado de la investigación:** 22 de noviembre de 2026. Fechas en Europe/Berlin.

---

## Incidentes y Evidencias (22 de noviembre de 2026)

### 1. Fuga de secretos en Claude Code
Apiiro detectó **1.122 repositorios públicos** con contraseñas y tokens en texto plano dentro de `.claude/settings.local.json` al utilizar la opción "Don't ask again" ([The Hacker News](https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html), [GitLab Blog](https://about.gitlab.com/blog/prevent-leaks-from-claude-code-dont-ask-again-file/)).

### 2. Detección de secretos en cinco minutos
GitGuardian demostró que un agente ARTEX localizó **8 de 9 credenciales ocultas** en repositorios, incluso aquellas eliminadas del historial ([GitGuardian Blog](https://blog.gitguardian.com/an-artex-build-ships-no-secret-scanner-in-our-lab-it-found-the-secrets-anyway/), [@MsftSecIntel](https://x.com/MsftSecIntel/status/2118491118308352329)).

### 3. Ataques de Device-Code Phishing
Microsoft alertó sobre técnicas de suplantación donde desarrolladores autorizan involuntariamente agentes maliciosos mediante flujos legítimos de código de dispositivo ([Microsoft Blog](https://www.microsoft.com/en-us/security/blog/2026/11/17/the-risks-of-device-code-authentication-for-ai-coding-agents/)).

### 4. Imágenes Docker maliciosas de ARTEX
Una copia troyanizada con shell root fue descargada casi 8.000 veces ([BadByte](https://badbyte.io/artex-backdoor-docker-image/), [@TheHackersNews](https://x.com/TheHackersNews/status/2118263059991134550)).

---

## Artículos previstos (Próximamente)

- *Vulnerabilidades en Vibe Coding: Limpieza de `.env`, `.git` y registros* (Próximamente)
- *Por qué no debes delegar la lógica de autenticación a la IA* (Próximamente)
- *Aislamiento de agentes de prueba: Lecciones del incidente de WorkOS* (Próximamente)
- *Phishing de código de dispositivo en entornos de desarrollo modernos* (Próximamente)
