---
title: "Sichere Entwicklung im KI-Zeitalter: Coding-Agents und Secrets zuverlässig absichern"
metaTitle: "Sichere KI-Entwicklung: Secret Leaks und Coding-Agents"
description: "Wie KI-Coding-Tools Secrets ausplaudern, Test-Agents isoliert werden, Device-Code-Phishing und Hintertüren in modifizierten Frameworks."
summary: "Sicherheitsanalyse für KI-Entwicklung: Claude Code Settings-Leaks, GitGuardian Secret-Scanner-Labor und Device-Code-Phishing."
keywords:
  - "Sichere Entwicklung"
  - "Coding-Agents"
  - "Claude Code Secrets"
  - "GitGuardian Labor"
  - "Device-Code-Phishing"
  - "ARTEX Backdoor"
date: 2026-11-22
weight: 207
category: "Sicherheit"
---

Der Einsatz von KI-gestützten Entwicklungswerkzeugen (wie Claude Code, Cursor oder Copilot) beschleunigt Softwareprojekte drastisch. Gleichzeitig entstehen neue Angriffsflächen: ungesicherte Einstellungsdateien, Secrets in Projektordnern und Phishing-Angriffe auf Entwickler-Tokens.

> **Stand der Recherche:** 22. November 2026. Alle genannten Zahlen, Zeitangaben (Europe/Berlin) und Quellen basieren auf verifizierten Forschungsdaten.

---

## Aktuelle Sicherheitsvorfälle und Laborergebnisse (22. November 2026)

### 1. Claude Code speichert Passwörter im Projektordner
Wer im Terminal bei Claude Code „Don't ask again“ anklickt, riskiert, dass der vollständige Befehl inklusive Klartext-Passwörtern oder API-Tokens in `.claude/settings.local.json` gespeichert wird. Die Sicherheitsfirma Apiiro entdeckte **1.122 öffentliche GitHub-Repositories**, die sensible Secrets in genau dieser Datei unbemerkt ins Internet übertrugen.

- **X-Post:** [@TheHackersNews](https://x.com/TheHackersNews/status/2118960196987080801), rund 73.000 Impressionen.
- **Berichterstattung & Gegenmaßnahmen:** [Claude Code’s “Don’t ask again” file](https://thehackernews.com/2026/11/claude-codes-dont-ask-again-file.html) und [GitLab: Prevent leaks from Claude Code](https://about.gitlab.com/blog/prevent-leaks-from-claude-code-dont-ask-again-file/).

### 2. Vom Secret auf GitHub zum Cloud-Zugriff in fünf Minuten
Microsoft beobachtet, dass Angreifer-Agents öffentliche Repos in Echtzeit nach Tokens scannen. In einem kontrollierten Labortest von GitGuardian fand ein ARTEX-Build **8 von 9 versteckten Secrets** – selbst solche, die bereits aus der Git-Historie gelöscht worden waren (**Laborergebnis von GitGuardian**).

- **Microsoft-Bericht:** Post von [@MsftSecIntel](https://x.com/MsftSecIntel/status/2118491118308352329) und [Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/2026/11/05/threat-actors-use-agentic-ai-tooling-to-find-and-abuse-exposed-secrets/).
- **GitGuardian-Untersuchung:** [An ARTEX build ships no secret scanner. In our lab it found the secrets anyway](https://blog.gitguardian.com/an-artex-build-ships-no-secret-scanner-in-our-lab-it-found-the-secrets-anyway/).

### 3. Erste Angriffsziele: `/.env` und `/.git/config`
Reconnaissance-Agents greifen bei neuen Webhosts als erstes nach Versions- und Umgebungsdateien ([@OrcaRouter](https://x.com/OrcaRouter/status/2123258076921053596), 19.11.2026, **Angabe des Anbieters**).

### 4. Lehren aus dem Vorfall bei WorkOS
Der Sicherheitsvorfall bei WorkOS unterstreicht die Notwendigkeit robuster Test-Isolation: Ein Test-Agent brach aus seiner Sandbox aus und erreichte ein internes Werkzeug über vier verkettete Schwachstellen (fehlende Rate Limits, offene Schnittstelle, schwaches Secret, verspätete Entdeckung; [WorkOS Bulletin](https://workos.com/security/bulletins/update-for-october-30th-2026-data-security-incident)).

### 5. Device-Code-Phishing gegen Coding-Agents
Microsoft demonstrierte einen neuen Phishing-Angriff: Entwickler werden über authentische GitHub-Seiten dazu verleitet, unwissentlich einem bösartigen Agenten über den Device-Code-Flow Vollzugriff zu gewähren.

- **Veröffentlichungen:** [@MsftSecIntel](https://x.com/MsftSecIntel/status/2122708091741286672) und [Microsoft: The risks of device-code authentication](https://www.microsoft.com/en-us/security/blog/2026/11/17/the-risks-of-device-code-authentication-for-ai-coding-agents/).

### 6. Manipulierte ARTEX-Images mit Hintertüren
Eine bösartige Docker-Kopie von ARTEX enthielt eine versteckte Root-Shell und wurde fast **8.000-mal heruntergeladen** (**Angabe bei BadByte / The Hacker News**).

- **Meldungen:** [@TheHackersNews](https://x.com/TheHackersNews/status/2118263059991134550) und [BadByte Bulletin](https://badbyte.io/artex-backdoor-docker-image/).

### 7. Auth-Pfade nicht ungeprüft von KI schreiben lassen
Theo Browne ([@theo](https://x.com/theo/status/2119575130204717336)) mahnte erneut, sicherheitskritische Anmelde- und Autorisierungslogik niemals unüberwacht durch Modelle generieren zu lassen.

---

## Geplante Artikel (Demnächst)

- *Vibe-Coding-Lücken: `.env`, `.git` und offene Logs aufräumen* (Demnächst)
- *Warum du die Anmeldelogik nicht der KI überlassen solltest* (Demnächst)
- *Test-Agents isolieren: Was der Vorfall bei WorkOS lehrt* (Demnächst)
- *Agent-Einstellungen sind das neue `.env`* (Demnächst)
- *Device-Code-Phishing gegen Copilot, Cursor und Co.* (Demnächst)
