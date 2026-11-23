---
title: "Agent-Zugang und Identität: Gute Agents erkennen und sicher durchlassen"
metaTitle: "Agent-Zugang und Identität: Web Bot Auth und RFC 9421"
description: "Wie Websites signierte, verifizierbare Agents erkennen, Bot-Schutzregeln anpassen und Agents eigene Identitäten geben statt geliehener Logins."
summary: "Analyse von Agent-Zugang und Identität: Web Bot Auth, Cloudflare Personal Agents, ChatGPT Wallet und dedizierte Agent-Logins."
keywords:
  - "Agent-Zugang"
  - "Agent-Identität"
  - "Web Bot Auth"
  - "RFC 9421"
  - "Cloudflare Personal Agents"
  - "ChatGPT Dots"
date: 2026-11-22
weight: 202
category: "Sicherheit"
---

Websites stehen vor einer neuen Herausforderung: Der klassische Bot-Schutz muss Scraping und bösartige Angriffe abwehren, darf aber zahlende Kunden nicht aussperren, wenn diese autonome persönliche KI-Agents für Recherchen und Einkäufe einsetzen.

Ein zukunftssicherer Agent-Zugang stützt sich auf kryptografische Signaturen, granulare Edge-Regeln und eigene Agent-Identitäten statt geliehener Mitarbeiter-Logins.

> **Stand der Recherche:** 22. November 2026. Alle genannten Zahlen, Zeitangaben (Europe/Berlin) und Quellen beruhen auf der verifizierten Recherche.

---

## Aktuelle Entwicklungen (Recherche 22. November 2026)

### 1. ChatGPT Wallet zwingt Shops, signierte Agents durchzulassen
OpenAI fordert Website- und Shopbetreiber ausdrücklich auf, persönliche Browser-Agents (Dots) nicht durch Sicherheitsfilter zu blockieren. In der Dokumentation wird der konkrete Schritt in Cloudflare beschrieben: Unter **Personal Agents** muss der Eintrag **„dots, OpenAI“** auf **Allow (do not block)** gesetzt werden. Alternativ nennt OpenAI eine WAF-Regel mit der Bot-Detection-ID `129220581` (ChatGPT Operator).

- **X-Post:** [@ChatGPT](https://x.com/ChatGPT/status/2121283151729496235), 13.11.2026, 17:44 Europe/Berlin, rund 1 Mio. Impressionen (Stand 22.11.2026).
- **Primärquellen:** [OpenAI, Introducing ChatGPT Wallet](https://openai.com/index/introducing-chatgpt-wallet/), [OpenAI, Introducing Dots](https://openai.com/index/introducing-dots/) und [OpenAI, Help ensure cloud browser access to your site](https://developers.openai.com/commerce/agent-access).
- **Protokoll:** Web Bot Auth basierend auf [RFC 9421](https://www.rfc-editor.org/rfc/rfc9421) (HTTP Message Signatures) mit den Headern `Signature`, `Signature-Input`, `Signature-Agent` (`"https://chatgpt.com"`) und dem Schlüsselverzeichnis `https://chatgpt.com/.well-known/http-message-signatures-directory`.

### 2. Cloudflare lässt Personal Agents einzeln steuern
Seit dem 4. November 2026 können Administratoren unterstützte Personal Agents individuell konfigurieren (**Allow**, **Block** oder **Block on pages with ads**). Standardmäßig erben Personal Agents die übergeordnete AI-Agents-Richtlinie.

- **Changelog:** [Granular access controls for the top Personal Agents, 4.11.2026](https://developers.cloudflare.com/changelog/post/2026-11-04-personal-agent-policies/)
- **Blog:** [See the agents, set the terms, 4.11.2026](https://blog.cloudflare.com/personal-agents-visibility-control/)
- **Dokumentation:** [AI Crawler and Agent access policies](https://developers.cloudflare.com/bots/additional-configurations/block-ai-bots/) sowie [Web Bot Auth bei Cloudflare](https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/).

### 3. Die Signatur zeigt den Betreiber, nicht den Kunden
Web Bot Auth belegt kryptografisch, dass eine Anfrage von der Infrastruktur eines Anbieters (wie OpenAI) stammt. Sie sagt jedoch nichts darüber aus, welcher Endnutzer die Aktion veranlasst hat und ob diese berechtigt ist. Cloudflare hat hierzu die Initiative „Trusted Agent Delegation“ vorgestellt.

- **Blog:** [Agents aren’t humans (but they kinda are), 5.11.2026](https://blog.cloudflare.com/trusted-agent-delegation/)
- **Post:** [@Cloudflare](https://x.com/Cloudflare/status/2118392403874701407), 5.11.2026, 18:18 Europe/Berlin
- **Standards:** IETF-Entwurf [draft-ietf-webbotauth-httpsig-protocol](https://datatracker.ietf.org/doc/draft-ietf-webbotauth-httpsig-protocol/) und [RFC 9421](https://www.rfc-editor.org/rfc/rfc9421).

### 4. Eigene Identitäten für Agents statt geliehener Logins
Führende Identity-Provider fordern, Agents als eigenständige Identitäten zu behandeln, anstatt ihnen bestehende Mitarbeiter-Logins zu überlassen.

- **Risiko geliehener Logins:** [@Cloudflare](https://x.com/Cloudflare/status/2118288470275674172), 5.11.2026, 11:25 Europe/Berlin warnt davor, dass Aktionen von Agents sonst unter fremdem Namen in Audit-Logs auftauchen.
- **Lösungen:** [Okta zu Agent Identity / CIMD](https://www.okta.com/blog/product-innovation/okta-cimd-ai-agent-identity/) und [@okta](https://x.com/okta/status/2107909146351669528), 7.10.2026, 21:01 Europe/Berlin. Weitere Ansätze bieten [Auth0](https://www.okta.com/newsroom/articles/auth0-may-2026-product-innovations/) und [Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/agent-identities).

### 5. WorkOS geht den umgekehrten Weg
Mit Agent Vault ermöglicht WorkOS Nutzern, bestehende Logins zentral zu hinterlegen, mit denen sich der Agent authentifiziert. Dies steht im direkten Gegensatz zu kryptografisch isolierten Agent-Identitäten.

- **Quellen:** [WorkOS Agent Vault Dokumentation](https://workos.com/docs/agent-vault) und [WorkOS-Blog](https://workos.com/blog/agent-vault).

---

## Geplante Artikel (Demnächst)

- *Web Bot Auth erklärt: So erkennst du signierte Agents wie ChatGPT Dots* (Demnächst)
- *Bot-Schutz neu einstellen, ohne zahlende Agents auszusperren* (Demnächst)
- *Eigene Identitäten für Agents statt geliehener Mitarbeiter-Logins* (Demnächst)
- *Die Signatur zeigt den Betreiber, nicht den Kunden* (Demnächst)
- *Schritt-für-Schritt-Anleitung: Personal Agents in Cloudflare einzeln freischalten* (Demnächst)
