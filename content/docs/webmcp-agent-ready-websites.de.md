---
title: "WebMCP für agentenbereite Websites."
metaTitle: "WebMCP für agentenbereite Websites: Leitfaden."
date: 2026-05-17
weight: 109
category: "Architecture"
description: "WebMCP ermöglicht es Websites, native Browser-Tools KI-Agenten zur Verfügung zu stellen. Erfahren Sie, wann Sie WebMCP verwenden sollten und wie es sich von MCP unterscheidet."
summary: "Ein praktischer Leitfaden zu WebMCP für agentenbereite Websites, der native Browser-Tools, MCP-Unterschiede, Formulare, Bereitstellungsmuster und AEO-Auswirkungen behandelt."
keywords:
  - "WebMCP"
  - "WebMCP vs. MCP"
  - "Agentenfähige Websites"
  - "Browser-Agenten"
  - "AI Agent-Webtools"
---
# WebMCP für agentenbereite Websites

WebMCP ist wichtig, weil es Websites die Möglichkeit bietet, Tools auf Seitenebene direkt Browser-Agenten zur Verfügung zu stellen, anstatt Agenten zu zwingen, Aktionen aus Screenshots, der DOM-Struktur oder fragilen Schaltflächenbeschriftungen abzuleiten. Für AEO ist WebMCP eine Brücke zwischen menschenorientierten Webseiten und maschinenausführbaren Aktionen.

## Was ist WebMCP?

In den WebMCP-Materialien von Chrome wird WebMCP als eine browserseitige Möglichkeit für Websites beschrieben, den Zweck von Anwendungsfunktionen zu verdeutlichen und Browser-Agenten strukturierte Funktionen bereitzustellen. In der Anleitung von Chrome wird ausdrücklich darauf hingewiesen, dass WebMCP kein Ersatz für MCP ist. Beide lösen unterschiedliche Probleme.

Primärquellen:

- [Chrome: Wann WebMCP und MCP verwendet werden sollten](https://developer.chrome.com/blog/webmcp-mcp-usage)
- [Chrome Lighthouse: Registrierte WebMCP-Tools](https://developer.chrome.com/docs/lighthouse/agentic-browsing/registered-webmcp-tools)
- [WebMCP Puppenspieler-Leitfaden](https://pptr.dev/guides/webmcp)

## WebMCP vs. MCP

| Frage | PCM | WebMCP |
|
---|
---|
---|
| Wo ist es tätig? | Serverumgebung oder -tool | Kontext der Browserseite |
| Hauptberuf | Verbinden Sie Agenten mit Tools, APIs, Daten und Workflows | Teilen Sie Browser-Agenten mit, welche Aktionen eine Seite unterstützt |
| Gut für | Backend-Aktionen, Datenzugriff, Business-Tools | Formulare, Seitenaktionen, Zahlungsschritte, Reservierungen |
| Entdeckungsmethode | MCP Server kündigt Tools an | Seite registriert Tools deklarativ oder mit JavaScript |
| AEO-Funktion | Ausführungsschicht für APIs und Dienste | Ausführungsschicht für Webschnittstellen |

Der [MCP vs. API-Leitfaden] (/docs/mcp-vs-api-for-agents/) erklärt MCP auf der Serverseite. WebMCP fügt eine Ebene auf Seitenebene für Websites hinzu, bei denen der Browser noch Teil der Benutzerreise ist.

## Warum WebMCP AEO ändert

Auf vielen Websites gibt es bereits Aktionen: einen Termin buchen, ein Produkt in den Warenkorb legen, ein Angebot anfordern, den Lagerbestand filtern, ein Support-Ticket einreichen. Das Problem besteht darin, dass diese Aktionen normalerweise nur als UI-Elemente sichtbar sind.

Ein Browser-Agent kann versuchen, die Seite wie eine Person zu bedienen, aber das ist fragil. Die Beschriftungen ändern sich. Es treten Manieren auf. Die Felder sind ausgeblendet. A/B-Tests verändern das DOM. WebMCP bietet der Site die Möglichkeit, die Aktion direkt anzugeben: Dieses Formular bucht einen Termin, diese Felder sind erforderlich, diese Aktion muss verwendet werden, wenn der Benutzer eine Reservierung wünscht.

Das ist ein stärkeres [Ausführungsschicht](/es/docs/execution-layer/)-Signal als eine Schaltflächenbeschriftung allein.

## Implementierungsmuster

In der Lighthouse-Dokumentation von Chrome heißt es, dass Tools mit deklarativen Attributen in Formularen oder mit einer zwingenden JavaScript-API wie „navigator.modelContext.registerTool“ registriert werden können.

| Muster | Das Beste für | Beispiel |
|
---|
---|
---|
| Tools für deklarative Formulare | Vorhandene Formulare mit klaren Aktionen | `book_appointment`, `request_quote` || Zwingende Registrierung | Dynamische Anwendungen und komplexe Aktionen | Inventarsuche, Warenkorbmutation |
| MCP-Server | Browserunabhängige Backend-Workflows | Kundensuche, Rechnungserstellung |
| Hybrid | Websites mit API- und Web-UI-Aktionen | E-Commerce, Reservierungen, SaaS-Panels |

Bei den meisten Websites sollte die erste nützliche WebMCP-Aktion ein Formular mit geringem Risiko sein: Lead-Anfrage, Terminanfrage, Support-Pfad oder Produktfilter.

## Was macht ein gutes WebMCP-Tool aus?Der Toolname sollte handlungsorientiert und stabil sein. Die Beschreibung sollte dem Agenten mitteilen, wann er es verwenden soll und welches Ergebnis zu erwarten ist.

Schwach:

```text
toolname="submit"
tooldescription="Submits the form"
```

Besser:

```text
toolname="request_audit"
tooldescription="Request an AEO readiness audit for a website. Use when the user wants a human review of AI search, crawler, and execution-layer readiness."
```

Agenten benötigen Absichten, erforderliche Eingaben und erwartete Ergebnisse. Das [Agent Buttons and Action Outline Guide] (/docs/agent-buttons-action-schema/) behandelt das gleiche Prinzip für Aktionsanweisungen über WebMCP hinaus.

## SEO- und AEO-Auswirkungen

WebMCP ist kein traditioneller Rankingfaktor. Betrachten Sie es als Zeichen der Umsetzbarkeit und nicht als Abkürzung zu Rankings.

Die nützliche SEO/AEO-Sequenz ist:

1. Machen Sie die Seite crawlbar und indexierbar.
2. Fügen Sie klare Inhalte, Titel, Gliederungen und interne Links hinzu.
3. Veröffentlichen Sie Erkennungsdateien als [llms.txt](/es/docs/programming-llms-txt/).
4. Fügen Sie WebMCP-Tools für hochwertige Aktien hinzu.
5. Probieren Sie Lighthouse Agent Navigation Audits aus.
6. Überwachen Sie das Ausfüllen von Formularen und die von Agenten ausgelösten Ereignisse.

Wenn der Seiteninhalt schwach ist, kann WebMCP das Problem nicht beheben. Hilft Agenten, Maßnahmen zu ergreifen, sobald sie die Seite verstanden haben.

## Risiken

Geben Sie sensible Aktionen nicht ohne Bestätigung und Genehmigung preis. Eine native Browseraktion sollte es einem Agenten nicht ermöglichen, ohne entsprechende Zustimmung die Abrechnung zu ändern, Daten zu löschen oder Käufe abzuschließen.

Zu guten Geländer gehören:

- klare Werkzeugbeschreibungen
- Ausdrückliche Bestätigung für Aktionen mit hohem Risiko
- Serverseitige Validierung
- Audit-Protokoll
- Tarifbegrenzungen
- Menschliche Überprüfung für regulierte Aufgaben

## Häufig gestellte Fragen

### Ist WebMCP dasselbe wie MCP?

Nein. MCP verbindet Agenten mit Tools und Systemen. WebMCP hilft Websites dabei, Aktionen auf Seitenebene für Browser-Agenten bereitzustellen.

### Sollten alle Websites WebMCP implementieren?

Noch nicht. Beginnen Sie mit Websites, auf denen Agenten Formulare, Reservierungen, Filter oder andere Browseraktionen ausfüllen müssen.

### Verbessert WebMCP das Ranking?

Es gibt keine offizielle Behauptung, dass WebMCP ein Rankingfaktor ist. Sein Wert liegt in der Handlungsfähigkeit des Agenten, nicht im herkömmlichen SEO-Ranking.

### Was soll ich zuerst umsetzen?

Beginnen Sie mit einer Aktion mit geringem Risiko, z. B. der Anforderung eines Angebots, der Buchung eines Termins oder der Eröffnung eines Supportpfads.

### Wie teste ich WebMCP?

Verwenden Sie die Chrome-Browsing-Agent-Audits und Browser-Tools von Lighthouse, die registrierte WebMCP-Tools auflisten können.