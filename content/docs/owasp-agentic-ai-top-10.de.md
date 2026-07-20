---
title: "OWASP Agentic AI Top 10 und AEO-Sicherheit."
date: 2026-05-17
weight: 117
category: "Guide"
description: "OWASP Agentic AI Top 10 erklärt die Risiken autonomer Agenten. Finden Sie heraus, wie AEO-Teams mit Agentur, Tools und Speicher umgehen sollten."
summary: "Ein praktischer AEO-Sicherheitsleitfaden basierend auf den OWASP Top 10 für Agentenanwendungen, mit Kontrollen für Tools, Speicher, Identität, Berechtigungen und Überwachung."
keywords:
  - "Top 10 der OWASP-KI-Agenten"
  - "KI-Sicherheitsagent"
  - "AEO-Sicherheit"
  - "Risiken von KI-Agenten"
  - "autonome Agenten-Governance"
---
#OWASP Agentic AI Top 10 und AEO-Sicherheit

OWASP Agentic AI Top 10 ist für AEO wichtig, da agentenbereite Websites Aktionen, Tools, APIs, Speicher und Zahlungen offenlegen. Diese Fähigkeiten schaffen nur dann einen Wert, wenn sie kontrolliert werden. Eine Site, die es Agenten ermöglicht, ohne Autorisierung, Einschränkungen, Aufsicht und Wiederherstellungspfade zu agieren, ist nicht für Agenten geeignet. Es ist einfach bloßgelegt.

## Was OWASP veröffentlicht hat

Das Gen AI Security-Projekt von OWASP veröffentlichte die Top 10 Agent Applications 2026 als Rahmen für Sicherheitsrisiken in autonomen und Agent-KI-Systemen. Es richtet sich an Systeme, die in allen Arbeitsabläufen planen, handeln und Entscheidungen treffen.

Primärquellen:

- [OWASP Top 10 für Agent-Anwendungen 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [Microsoft Security: OWASP Top 10 Risiken in Agent AI](https://www.microsoft.com/en-us/security/blog/2026/03/30/addressing-the-owasp-top-10-risks-in-agentic-ai-with-microsoft-copilot-studio/)

## Warum das zum AEO gehört

Die [Ausführungsschicht](/es/docs/execution-layer/) ermöglicht es Agenten, Dinge zu tun: Arbeitsabläufe reservieren, kaufen, aktualisieren, abrufen, vergleichen und aktivieren. Gerade deshalb ist Sicherheit wichtig.

Das traditionelle Risiko von SEO besteht hauptsächlich in Reputation und Indexierung. Das AEO-Risiko umfasst:

- unerlaubte Handlungen
- übermäßige Entscheidungsfreiheit
- Missbrauch von Werkzeugen
- Gedächtnisvergiftung
- Kontextleck
- unsichere Delegation
- Zahlungsfehler
- irreversible Zustandsänderungen

Das Ziel besteht nicht darin, den Agentenzugriff zu verhindern. Das Ziel besteht darin, die richtigen Aktionen mit den richtigen Kontrollen anzuzeigen.

## AEO-Sicherheitskontrollkarte

| AEO-Oberfläche | Sicherheitsfrage | Minimale Kontrolle |
|
---|
---|
---|
| Öffentlicher Inhalt | Können Agenten ihm vertrauen? | Quellen, Daten, Klarheit der Entität |
| llms.txt | Agenten sicher führen? | Verknüpfen Sie nur stabile und relevante Ressourcen |
| MCP-Tools | Wer kann sie anrufen? | Zulassung und Geltungsbereich |
| WebMCP-Tools | Können Browser-Agenten Formulare missbrauchen? | Bestätigungen und Validierungen |
| Zahlungsendpunkte | Können die Kosten vermieden werden? | Budgets, Idempotenz, Einnahmen |
| Agentenspeicher | Kann ein bösartiger Kontext bestehen bleiben? | Isolation und Ablauf |
| Aufzeichnungen | Können Maßnahmen geprüft werden? | Agent-ID, Benutzer-ID, Tool, Ergebnis |

Der [Agent Observability Guide](/es/docs/agent-observability-guardrails/) behandelt die Überwachung ausführlicher.

##Übermäßige Entscheidungsfreiheit

Übermäßige Handlungsfähigkeit liegt vor, wenn ein Agent mehr tun kann, als der Benutzer oder das Unternehmen beabsichtigt hat. In AEO-Begriffen ist dies der Unterschied zwischen „Verfügbarkeit prüfen“ und „Buchen und Bezahlen ohne Bestätigung“.

Begrenzte Berechtigungen verwenden:

- Vor dem Schreiben nur lesen
- Angebot vor dem Kauf
- Anfrage vor Bestätigung
- Sandkasten vor der Produktion
- menschliche Zustimmung angesichts irreversibler Handlungen

Im [MCP-Autorisierungsleitfaden] (/docs/mcp-authorization-oauth-ai-agents/) wird erläutert, wie Bereiche dazu beitragen, die Tools einzuschränken.

## Tool- und Workflow-RisikenAgent-Tools sollten als Produktions-APIs und nicht als Demo-Verknüpfungen konzipiert werden.

Zu einem guten Werkzeugdesign gehört:

- getippte Einträge
- schriftliche Ausgaben
- Klare Fehlermeldungen
- Eingabevalidierung
- Idempotenzschlüssel
- Tarifbegrenzungen
- Wiederholungsregeln
- Audit-Protokoll
- Zugriff mit den geringsten Privilegien

Wenn ein Tool Geld ausgeben, Kundendaten ändern oder Gerichtsverfahren auslösen kann, sind strengere Kontrollen erforderlich als bei einem Endpunkt für öffentliche Inhalte.

## Gedächtnis- und Kontextrisiken

Agenten können Kontext durch Aufgaben übermitteln. Das schafft Bequemlichkeit und Risiko.

Zu den Problemen gehören:- Speicher durch schädliche Inhalte vergiftet
- veraltete Anleitung
- Leckage zwischen Clients
- Anweisungen, die im wiederhergestellten Inhalt versteckt sind
- Veraltete Policendaten

Für AEOs sollten öffentliche Seiten so verfasst sein, dass Agenten Fakten, Marketingaussagen, Anweisungen und Einschränkungen unterscheiden können. Verstecken Sie Bedienungsanleitungen nicht in dekorativen Inhalten.

## Vertrauenssignale für den Agenten

Vertrauenssignale müssen sowohl für Menschen als auch für Maschinen sichtbar sein:

- klare organisatorische Identität
- Kontaktseite
- Datenschutzrichtlinie
- Sicherheits- oder Compliance-Seite, sofern relevant
- Aktualisierungstermine für sensible Inhalte
- Quellenlinks für Tatsachenbehauptungen
- Dokumentierte Werkzeugberechtigungen
- API-Status- oder Gesundheitsinformationsseite

Das [AEO-Bereitschaftsaudit] (/es/docs/audit/) muss Sicherheitskontrollen umfassen, bevor ein Agent-Workflow mit hohem Risiko aktiviert wird.

## Häufig gestellte Fragen

### Ist OWASP Agentic AI Top 10 nur für Entwickler?

Nein. Es ist nützlich für Produkt-, Sicherheits-, Rechts- und SEO/AEO-Teams, da die Offenlegung von Agenten Auswirkungen auf Inhalte, Tools, Arbeitsabläufe und Governance hat.

### Was ist der größte Sicherheitsfehler von AEO?

Gewähren Sie Agenten weitreichenden Schreibzugriff, bevor Sie Bereiche, Commits, Limits und Protokolle entwerfen.

### Reduziert die Sicherheit die Agentensichtbarkeit?

Gute Sicherheit kann das Vertrauen stärken. Agenten bevorzugen Systeme mit vorhersehbaren Berechtigungen und behebbaren Fehlern.

### Sollte jede Agentenaktion eine menschliche Zustimmung erfordern?

Nein. Aktionen mit geringem Risiko können automatisch erfolgen. Maßnahmen, die risikoreich, teuer, reguliert oder irreversibel sind, sollten einer stärkeren Bestätigung bedürfen.

### Wie sollten Teams beginnen?

Inventarisieren Sie jede Agentenaktion, klassifizieren Sie Risiken und fügen Sie dann Kontrollen hinzu, bevor Sie den Zugriff auf die Ausführungsebene erweitern.