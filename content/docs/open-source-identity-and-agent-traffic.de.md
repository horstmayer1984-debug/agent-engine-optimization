---
title: "Agent-Besuche erkennen und verifizieren: Die besten Open-Source-Tools im Ranking"
metaTitle: "KI-Agenten Traffic-Analyse & Verifikation Tools (2026)"
description: "Ranking der besten Open-Source-Tools zur Erkennung und Verifikation von KI-Agents: Web Bot Auth, AgentCake, mintlify/agent-traffic, Botscent und AgentReady."
summary: "Praxisleitfaden zur Erkennung von KI-Agents: Signaturprüfung nach RFC 9421, Session-Replay, Traffic-Klassifizierung und Readiness-Checks."
keywords:
  - "Web Bot Auth"
  - "AgentCake"
  - "mintlify agent-traffic"
  - "Botscent"
  - "AgentReady"
  - "Agent-Traffic Verifikation"
date: 2026-11-22
weight: 213
category: "Open Source"
---

Klassische Web-Analytics-Lösungen stoßen an ihre Grenzen, wenn autonome KI-Agents Websites ansteuern: Sie verfälschen Verweildauern, erzeugen ungewohnte Klickpfade oder werden fälschlicherweise als bösartige Scraper geblockt. Zudem fälschen Angreifer zunehmend die User-Agents bekannter Modelle.

Dieses Ranking vergleicht spezialisierte Open-Source-Werkzeuge zur Identifikation, Signaturprüfung und Verhaltensanalyse von KI-Agents.

> **Stand der Recherche:** 22. November 2026. GitHub-Sterne, Lizenzen und Zeitstempel (`pushed_at` in Europe/Berlin) stammen aus der offiziellen GitHub-API-Abfrage vom 22.11.2026.

---

## Ranking-Tabelle: Agent-Erkennung und Traffic-Analyse

| Rang | Tool | Kategorie | Nutzen für AEO | Lizenz | Sterne (22.11.2026) | Letzte Aktivität (Europe/Berlin) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | [Web Bot Auth](https://github.com/cloudflare/web-bot-auth) | Signaturprüfung (RFC 9421) | Prüft kryptografisch, ob eine Anfrage von einem echten, signierten Agent stammt. | Apache-2.0 | 186 | 21.11.2026, 20:46 |
| **2** | [AgentCake](https://github.com/tartini-ai/agent-traffic-analytics) | Traffic-Analyse / Replay | Unterscheidet in der Analyse verlässlich zwischen Agents und Menschen (inkl. Session-Replay). | MIT | 91 | 21.11.2026, 15:03 |
| **3** | [mintlify/agent-traffic](https://github.com/mintlify/agent-traffic) | Traffic-Klassifikation | Sortiert eingehende Zugriffe präzise in autonome Agents, Such-Crawler und menschliche Besucher. | MIT | 88 | 10.11.2026, 19:43 |
| **4** | [Botscent](https://github.com/nalinbhardwaj/botscent) | Erkennungsbibliothek | Schlanke Bibliothek zur verhaltensbasierten Erkennung automatisierter Agents. | MIT | 35 | 11.11.2026, 17:13 |
| **5** | [AgentReady](https://github.com/agentready-org/standard) | Readiness-Check | Schneller Check auf Agent-Readiness, u. a. via `npx is-agentic`. Lizenz in GitHub-API nicht angegeben. | keine Angabe | 65 | 11.11.2026, 23:50 |

---

## Kurzbeschreibung je Tool

### 1. Web Bot Auth (Cloudflare)
- **Fokus:** Kryptografische Signaturprüfung.
- **Nutzen für AEO:** Implementiert den IETF-Entwurf [draft-ietf-webbotauth-httpsig-protocol](https://datatracker.ietf.org/doc/draft-ietf-webbotauth-httpsig-protocol/) und [RFC 9421](https://www.rfc-editor.org/rfc/rfc9421). Erlaubt dem Server, eingehende Anfragen anhand digitaler Signaturen eindeutig verifizierten Agent-Betreibern zuzuordnen.
- **Repository:** [github.com/cloudflare/web-bot-auth](https://github.com/cloudflare/web-bot-auth)

### 2. AgentCake
- **Fokus:** Session-Replay für autonome Browser-Agents.
- **Nutzen für AEO:** Visualisiert die Pfade, die autonome Agent-Systeme auf der Website nehmen, und hilft zu verstehen, wo Automatisierungen abbrechen.
- **Repository:** [github.com/tartini-ai/agent-traffic-analytics](https://github.com/tartini-ai/agent-traffic-analytics)

### 3. mintlify/agent-traffic & Botscent
- **Fokus:** Sortierung von Datenströmen.
- **Nutzen für AEO:** Ermöglichen die saubere Trennung von menschlichem Traffic und maschinellen Anfragen in Logging- und Analytics-Systemen.
- **Repositories:** [github.com/mintlify/agent-traffic](https://github.com/mintlify/agent-traffic) und [github.com/nalinbhardwaj/botscent](https://github.com/nalinbhardwaj/botscent)

### 4. AgentReady
- **Fokus:** Frischer Readiness-Check.
- **Nutzen für AEO:** Ermöglicht die unkomplizierte Ausführung lokaler Audits via CLI. *Hinweis:* Es handelt sich um ein noch sehr junges Projekt; in der GitHub-API war am 22.11.2026 keine Lizenz hinterlegt (keine Lizenz erfinden).
- **Repository:** [github.com/agentready-org/standard](https://github.com/agentready-org/standard)

---

## Für wen welches Tool?

- **Kryptografische Absicherung:** Setzen Sie auf **[Web Bot Auth](https://github.com/cloudflare/web-bot-auth)** zur Verifikation signierter Header.
- **Analytics und Session-Replay:** Nutzen Sie **[AgentCake](https://github.com/tartini-ai/agent-traffic-analytics)** oder **[mintlify/agent-traffic](https://github.com/mintlify/agent-traffic)** zur Traffic-Klassifizierung.
- **Schneller lokaler Smoke-Test:** Probieren Sie **[AgentReady](https://github.com/agentready-org/standard)** aus.
