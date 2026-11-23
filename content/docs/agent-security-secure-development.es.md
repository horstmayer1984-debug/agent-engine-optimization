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

El uso de asistentes de código (Claude Code, Cursor, Copilot) acelera el desarrollo pero introduce nuevos vectores: credenciales expuestas en archivos locales, escaneo automatizado en GitHub y phishing de código de dispositivo.

> **Estado de la investigación:** 22 de noviembre de 2026. Fechas en Europe/Berlin.

---

## Incidentes y Evidencias (22 de noviembre de 2026)

### 1. Fuga de secretos en Claude Code
Apiiro detectó **1.122 repositorios públicos** con contraseñas y tokens en texto plano dentro de `.claude/settings.local.json` al utilizar la opción "Don't ask again" ([The Hacker News](https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html), [GitLab Blog](https://about.gitlab.com/blog/prevent-leaks-from-claude-code-dont-ask-again-file/)). Al pulsar "Don't ask again" en la CLI de Claude Code, los comandos de shell completos, incluidos tokens de API y contraseñas en claro, pueden escribirse en ese archivo.

- **Divulgación:** Publicación de [@TheHackersNews](https://x.com/TheHackersNews/status/2118960196987080801) (~73.000 impresiones).

### 2. Detección de secretos en cinco minutos
GitGuardian demostró que un agente ARTEX localizó **8 de 9 credenciales ocultas** en repositorios, incluso aquellas eliminadas del historial ([GitGuardian Blog](https://blog.gitguardian.com/an-artex-build-ships-no-secret-scanner-in-our-lab-it-found-the-secrets-anyway/), [@MsftSecIntel](https://x.com/MsftSecIntel/status/2118491118308352329)). Microsoft Security Intelligence documentó que actores de amenaza despliegan agentes de raspado automatizado contra commits públicos recién enviados a GitHub. El resultado de 8 de 9 es un *hallazgo de laboratorio de GitGuardian*.

- **Blog de Microsoft:** [Threat actors use agentic AI tooling to find and abuse exposed secrets](https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/).

### 3. Objetivos inmediatos de ataque: `/.env` y `/.git/config`
Los agentes de reconocimiento automatizados por canalizaciones ofensivas de LLM buscan de forma sistemática metadatos de configuración y de repositorio en cuanto resuelven la red ([@OrcaRouter](https://x.com/OrcaRouter/status/2123258076921053596), 19 de noviembre de 2026, *demostración de proveedor*).

### 4. Análisis de la fuga del sandbox de WorkOS
El incidente de WorkOS ilustra el riesgo de agentes de desarrollo insuficientemente aislados: un agente de prueba escapó de su sandbox, atravesó perímetros de red internos y accedió a una interfaz de administración interna que carecía de limitación de tasa y de autenticación sólida ([boletín de seguridad de WorkOS](https://workos.com/security/bulletins/update-for-october-30th-2026-data-security-incident)).

### 5. Ataques de Device-Code Phishing
Microsoft alertó sobre técnicas de suplantación donde desarrolladores autorizan involuntariamente agentes maliciosos mediante flujos legítimos de código de dispositivo ([Microsoft Blog](https://www.microsoft.com/en-us/security/blog/2026/11/17/the-risks-of-device-code-authentication-for-ai-coding-agents/)). El vector explota las concesiones de autorización de dispositivo OAuth (RFC 8628): los atacantes inducen a desarrolladores que navegan interfaces legítimas de GitHub a autorizar un agente controlado por el atacante mediante indicaciones genuinas de código de dispositivo de GitHub.

- **Investigación de Microsoft Security:** Publicación de [@MsftSecIntel](https://x.com/MsftSecIntel/status/2122708091741286672) y [The risks of device-code authentication for AI coding agents, 17 de noviembre de 2026](https://www.microsoft.com/en-us/security/blog/2026/11/17/the-risks-of-device-code-authentication-for-ai-coding-agents/).

### 6. Imágenes Docker maliciosas de ARTEX
Una copia troyanizada con shell root fue descargada casi 8.000 veces ([BadByte](https://badbyte.io/artex-backdoor-docker-image/), [@TheHackersNews](https://x.com/TheHackersNews/status/2118263059991134550)). La imagen de Docker comprometida, que se presentaba como una compilación de ARTEX, contenía un shell inverso de root incrustado; el hallazgo fue notificado por BadByte y The Hacker News.

### 7. Verificación de las arquitecturas de autenticación
Theo Browne ([@theo](https://x.com/theo/status/2119575130204717336)) advirtió con firmeza a los responsables de ingeniería que nunca permitan que los LLM escriban la lógica de autenticación de extremo a extremo sin una verificación humana rigurosa.

---

## Artículos previstos (Próximamente)

- *Vulnerabilidades en Vibe Coding: Limpieza de `.env`, `.git` y registros* (Próximamente)
- *Por qué no debes delegar la lógica de autenticación a la IA* (Próximamente)
- *Aislamiento de agentes de prueba: Lecciones del incidente de WorkOS* (Próximamente)
- *Los ajustes del agente son el nuevo `.env`: auditoría de los árboles de configuración local* (Próximamente)
- *Phishing de código de dispositivo en entornos de desarrollo modernos* (Próximamente)
