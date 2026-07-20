---
title: "MCP-Anwendungen: Interaktive Schnittstellen für Workflows."
date: 2026-05-17
weight: 135
category: "Architecture"
description: "Entdecken Sie, was MCP-Anwendungen sind, wie interaktive Benutzeroberflächenkomponenten in MCP-Hosts funktionieren und wann Websites."
summary: "Ein praktischer Leitfaden für MCP-Anwendungen, der Online-Benutzeroberfläche, sicheres Rendering, Anwendungsfälle und die Art und Weise, wie die Erweiterung das agentenorientierte Produktdesign verändert, abdeckt."
keywords:
  - "MCP-Anwendungen"
  - "MCP-Benutzeroberfläche"
  - "interaktive Agentenschnittstellen"
  - "Modellkontextprotokollanwendungen"
  - "Benutzeroberfläche für Agenten-Workflows"
---
# MCP-Anwendungen: Interaktive Schnittstellen für Agenten-Workflows

MCP-Anwendungen sind eine offizielle Erweiterung des Model Context Protocol, die es Tools ermöglicht, interaktive Benutzeroberflächen und nicht nur Text oder strukturierte Daten zurückzugeben. Dies ist wichtig, da einige Arbeitsabläufe von Agenten Diagramme, Genehmigungsformulare, Dashboards oder mehrstufige Kontrollen innerhalb der Konversation selbst erfordern. MCP-Anwendungen halten den Workflow im Kontext und bieten Benutzern gleichzeitig eine umfangreichere Benutzeroberfläche, wenn einfacher Text nicht ausreicht.

## Was die offiziellen MCP-Dokumente sagen

Das MCP-Projekt kündigte MCP Apps als seine erste offizielle Erweiterung im Januar 2026 an. Die offiziellen Dokumente beschreiben interaktive HTML-Schnittstellen, die in MCP-Hosts gerendert werden, mit Sandboxing und einer sicheren Kommunikationsbrücke zwischen der Anwendung und dem Host.

Primärquellen:

- [MCP-Blog: Live-Ankündigung von MCP Apps](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/)
- [Übersicht über MCP-Anwendungen](https://modelcontextprotocol.io/extensions/apps/overview)
- [Übersicht über MCP-Erweiterungen](https://modelcontextprotocol.io/extensions)

## Warum es MCP-Anwendungen gibt

Für viele Tool-Antworten reicht der Text aus:

- ein Suchergebnis
- ein Staat
- eine einfache Empfehlung

Aber der Text wird ungeschickt, um:

- Grafiken
- visuelle Vergleiche
- Genehmigungsworkflows
- Designer-Leinwände
- Formulare mit mehreren abhängigen Feldern
- Dashboards mit Live-Status

MCP-Anwendungen fügen eine Ebene der Benutzeroberfläche hinzu, ohne dass Benutzer das Host-Erlebnis verlassen müssen.

## MCP-Apps im Vergleich zu regulären Web-Apps

| Frage | Eigenständige Webanwendung | MCP-Anwendung |
|
---|
---|
---|
| Wo wird es gerendert? | Site oder separate Registerkarte | Im MCP-Host |
| Bleibt der Kontext des Gesprächs erhalten? | Im Allgemeinen nicht | Ja |
| Das Beste für | Komplette Produkte | Workflow-Snippets und Tool-verknüpfte Benutzeroberfläche |
| Kommunikation | Browser-Anwendungs-API | MCP plus Anwendungsbrücke |
| Benutzerreise | Kontextwechsel | Online-Fortsetzung |

MCP-Anwendungen ersetzen nicht alle Webanwendungen. Sie sind nützlich, wenn die Schnittstelle Teil einer agentenvermittelten Aufgabe und nicht des gesamten Produkts ist.

## AEO-Auswirkungen

Die [Ausführungsschicht](/es/docs/execution-layer/) benötigt häufig einen menschlichen Prüfpunkt. MCP-Anwendungen können diesen Kontrollpunkt praktisch machen:

- eine Rückerstattung genehmigen
- Sehen Sie sich ein Angebot an
- Wählen Sie zwischen Optionen
- Sehen Sie sich eine Grafik an
- eine riskante Aktion bestätigen

Dies hängt natürlich mit [Benutzererfahrung von Agenten und Human-in-the-Loop-Design] (/es/docs/agent-ux-human-in-the-loop/) zusammen, wo die Frage nicht „Mensch oder Agent“ lautet, sondern „Welche Teile benötigen welche Schnittstelle?“

## Wann MCP-Anwendungen verwendet werden sollten

Verwenden Sie sie, wenn:

- Das Ergebnis eines Tools bedarf einer visuellen Interpretation
- Der nächste Schritt erfordert strukturierte menschliche Eingaben
- Sie möchten den Gesprächskontext bewahren
- Die Benutzeroberfläche ist einem Tool-Workflow untergeordnet

Verwenden Sie sie nicht, wenn:

- eine einfache Textantwort reicht aus
- Erfahrung braucht ein vollständiges und eigenständiges Produkt
– Das Ziel-Hosting-Ökosystem unterstützt die Erweiterung ## Security and Deployment noch nicht

Offizielle Dokumente beschreiben Sandbox-Rendering und eine sichere Nachrichtenbrücke. Das bedeutet, dass die Teams immer noch sorgfältig darüber nachdenken müssen:

- welche Daten gelangen in die Benutzeroberfläche
- Welches Tool kann den UI-Aufruf auslösen?
- wenn eine Genehmigung erforderlich ist
- wie der Status erfasst wird
- wie unterschiedlich der Host-Support istDer [MCP-Autorisierungsleitfaden](/es/docs/mcp-authorization-oauth-ai-agents/) ist immer noch relevant, da die umfangreiche Benutzeroberfläche die Notwendigkeit strenger Berechtigungen nicht überflüssig macht.

## Häufig gestellte Fragen

### Sind MCP-Anwendungen Teil des Haupt-MCP?

Sie sind eine offizielle Erweiterung, nicht das Kernprotokoll selbst.

### Ersetzen MCP-Anwendungen eine Website?

Nein. Sie eignen sich am besten für die Online-Workflow-Benutzeroberfläche und ersetzen nicht alle öffentlichen Web-Erlebnisse.

### Welche Kunden unterstützen Sie?

Der Host-Support variiert. Die MCP-Dokumente enthalten eine Kundensupportmatrix für offizielle Erweiterungen.

### Was ist der beste erste Anwendungsfall?

Genehmigungsabläufe und kleine Dashboards sind gute Ausgangspunkte, da sie mehr als nur Text, aber weniger als eine vollständige Produktbenutzeroberfläche erfordern.

## Fazit

MCP-Anwendungen sind wichtig, da Agenten-Workflows immer noch menschliches Urteilsvermögen erfordern. Sie bringen nützliche Schnittstellenfragmente an die Stelle, an der der Agent bereits arbeitet.