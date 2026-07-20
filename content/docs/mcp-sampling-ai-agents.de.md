---
title: "MCP-Sampling erklärt: Wie Server Anfragen stellen."
date: 2026-05-23
weight: 133
category: "Architecture"
description: "Mit MCP Sampling können Server Modellgenerationen über einen Client anfordern. Erfahren Sie, wie es funktioniert, wo es hilft und warum es wichtig ist."
summary: "Eine praktische Erklärung für MCP Sampling, die vom Server angeforderte LLM-Generationen, Client-Steuerung, Modellpräferenzen, Sicherheit und AEO-Auswirkungen abdeckt."
keywords:
  - "MCP-Probenahme"
  - "Probenahme/Erstellung einer Nachricht"
  - "Probenahme von Modellkontextprotokollen"
  - "KI-Agentenarchitektur"
  - "MCP-Server"
---
# MCP-Sampling erklärt: Wie Server die Ausgabe von KI-Modellen anfordern

Mit MCP Sampling kann ein MCP-Server den Client auffordern, während eines Workflows Modellergebnisse zu generieren. Der Server benötigt keinen eigenen Modell-API-Schlüssel. Der Kunde behält die Kontrolle über Modellzugriff, Berechtigungen, Überprüfung und endgültige Lieferung. Dies macht die Stichprobenentnahme für Agenten-Workflows nützlich, aber riskant, wenn die generierten Eingabeaufforderungen und Ergebnisse dem Benutzer nicht klar angezeigt werden.

## Was ist MCP-Probenahme?

Die offizielle [Model Context Protocol Sampling Specification] (https://modelcontextprotocol.io/docs/concepts/sampling) beschreibt Sampling als eine Möglichkeit für Server, LLM-Generationen von Sprachmodellen über Clients anzufordern. In der Protokollrevision 2025-06-18 deklarieren Clients, die es unterstützen, eine „Sampling“-Fähigkeit und Server fordern eine Generierung über „sampling/createMessage“ an.

Das klingt abstrakt, deshalb hier die einfache Version: Ein Tool-Server kann den KI-Client des Benutzers auffordern, im Rahmen eines Tool-Flows Text zu denken, zusammenzufassen, zu sortieren oder zu generieren.

Für einen breiteren Kontext siehe [MCP vs. Agent-APIs](/es/docs/mcp-vs-api-for-agents/), [MCP-Autorisierung mit OAuth](/es/docs/mcp-authorization-oauth-ai-agents/) und [MCP-Anwendungen](/es/docs/mcp-apps-guide/).

## Warum Sampling existiert

Ohne Sampling verfügt ein MCP-Server über zwei eingeschränkte Optionen:

- Rohdaten zurückgeben und warten, bis das Clientmodell weiß, was zu tun ist
- Rufen Sie direkt Ihren eigenen Modellanbieter an, was zu Kosten-, Datenschutz- und wichtigen Verwaltungsproblemen führt

Sampling schafft einen Mittelweg. Der Server kann Modellarbeit anfordern, aber der Client ist immer noch der Gatekeeper.

## Probenahme versus Werkzeuge versus Ressourcen

| MCP-Funktion | Wer kontrolliert es? Hauptzweck | Beispiel |
|
---|
---|
---|
---|
| Werkzeuge | Das Modell ruft die Serveraktion | auf Führen Sie eine Funktion aus | „Ticket erstellen“ |
| Ressourcen | Der Server macht den Kontext verfügbar | Daten für das Modell bereitstellen | „Projektskizze lesen“ |
| Wegbeschreibung | Server stellt Vorlagen bereit | Führen Sie einen benutzergesteuerten Workflow | „Nachricht zur Codeüberprüfung ausführen“ |
| Probenahme | Der Server fordert die Ausgabe an das Modell des Clients | an Während eines Workflows generieren oder begründen | „Dieses wiederhergestellte Dokument zusammenfassen“ |

Die Bemusterung ist kein Ersatz für Werkzeuge. Dies ist eine Möglichkeit, die Modellgenerierung innerhalb einer Funktion zu verschachteln.

## Beispielanwendungsfälle

Stichproben können hilfreich sein, wenn ein Server Sprachmodellergebnisse benötigt, aber nicht Eigentümer der Modellbeziehung sein soll.

Zu den nützlichen Mustern gehören:

- Fassen Sie die wiederhergestellten Dokumente zusammen
- Verfassen Sie eine Antwort, nachdem ein Tool Daten abgerufen hat
- Support-Tickets klassifizieren
- Generieren Sie eine Erklärung in natürlicher Sprache aus strukturierten Daten
- Bitten Sie das Client-Modell, den vom Benutzer bereitgestellten Kontext zu transformieren
– Bewertungsoptionen basierend auf für den Benutzer sichtbaren Kriterien. Für AEO ist dies wichtig, da Websites und von Agenten lesbare APIs möglicherweise Arbeitsabläufe unterstützen müssen, die Abruf, Ausführung und Erklärung kombinieren.

## Sicherheits- und Überprüfungsanforderungen

Die Probenahmespezifikation legt Wert auf die menschliche Überprüfung. Anwendungen sollten es einfach machen, Musteranfragen zu überprüfen, Anfragen vor dem Absenden zu bearbeiten und generierte Antworten vor der Zustellung zu überprüfen.

Das ist eine ernsthafte Forderung. Andernfalls kann das Sampling zu einem versteckten Modellaufruf werden, der von einem Server ausgelöst wird, den der Benutzer kaum versteht.| Risiko | Warum ist es wichtig | Geländer |
|
---|
---|
---|
| Versteckte schnelle Injektion | Der Server enthält möglicherweise unsichere Anweisungen | Anweisungen vor der Ausführung anzeigen |
| Datenleck | Der Kontext kann vertrauliche Informationen enthalten | Benutzern erlauben, den freigegebenen Kontext zu überprüfen |
| Kostenüberraschungen | Modellaufrufe können kostenpflichtige Token verbrauchen | Visualisierungsmodell und Kostenpolitik |
| Falsche Ausgabe | Die generierte Antwort ist möglicherweise ungenau | Überprüfung vor der endgültigen Lieferung |
| Serverüberschreitung | Der Server fordert möglicherweise unnötige Modellarbeit an | Erfordern explizite Funktionsunterstützung |

Der Leitfaden [Agent Observability Guardrails](/es/docs/agent-observability-guardrails/) erweitert diese Governance-Ebene.

## AEO-Auswirkungen

MCP Sampling belohnt sauberen Kontext. Wenn Ihre Dokumente, API-Antworten, Produktdaten oder Workflow-Beschreibungen vage sind, hat das Kundenmodell eine schwierigere Aufgabe. Wenn stichprobenbasierte Arbeitsabläufe strukturiert, prägnant und intern verknüpft sind, können sie zu besseren nachgelagerten Reaktionen führen.

Für Website-Betreiber bedeutet das:

- klare Definitionen veröffentlichen
- API-Antworten strukturiert halten
- maschinenlesbare Dokumente freilegen
- Vermeiden Sie es, wichtige Einschränkungen in Prosa zu vergraben
- Quellseiten der Wahrheit dokumentieren
- Bereitstellung stabiler Identifikatoren für Entitäten und Aktionen

Das [AEO-Entwicklerhandbuch](/es/docs/developers-guide-aeo/) ist der natürliche nächste Schritt.

## Häufig gestellte Fragen

### Erlaubt MCP Sampling einem Server, jedes gewünschte Modell aufzurufen?

Nein. Der Client kontrolliert den Zugriff auf das Modell. Der Server kann Präferenzen äußern, aber der Client entscheidet, was verfügbar und erlaubt ist.

### Ist Sampling für MCP-Server erforderlich?

Nein. Es handelt sich um eine Kundenkapazität. Viele MCP-Workflows können Tools, Ressourcen und Eingabeaufforderungen ohne Stichproben verwenden.

### Ist die Probenahme für die Produktion sicher?

Es kann mit Vorsicht verwendet werden, erfordert jedoch eine kurze Überprüfung, Kontextüberprüfung, Protokolle, Berechtigungsbeschränkungen und sinnvolle Standardeinstellungen.

### Warum ist die Probenahme für AEO wichtig?

Es zeigt, dass Agenten-Workflows Modelle dazu auffordern können, während der Ausführung über ihren Inhalt nachzudenken und nicht nur Seiten abzurufen. Strukturierte und quellengestützte Inhalte werden nützlicher.

## FazitMCP Sampling ist eine nützliche Brücke zwischen Toolausführung und Modellbegründung. Behandeln Sie es als kontrollierte Funktion und nicht als Verknüpfung im Hintergrund.