---
title: "Agentenkarten und A2A-Protokoll für fertige Standorte."
date: 2026-04-12
weight: 63
category: "Architecture"
description: "Wie Agentenkarten und A2A freiberuflichen Agenten dabei helfen, Funktionen zu entdecken, sicher zusammenzuarbeiten und mit fertigen Websites zu interagieren."
summary: "Agentenkarten teilen anderen Agenten mit, was Ihre Website tun kann. Das A2A-Protokoll ermöglicht den direkten Austausch von Aufgaben von Agent zu Agent. Zusammen machen sie Ihre Website in Multi-Agent-Workflows auffindbar und kollaborativ."
keywords:
  - "JSON-Agentenkarte"
  - "A2A-Protokoll"
  - "Agent-zu-Agent-Protokoll"
  - "Agentenzusammenarbeit"
  - "Implementierung einer Agentenkarte"
  - "Multi-Agent-Erkennung"
---
Mit Agentenkarten und dem A2A-Protokoll (Agent-zu-Agent) können Sie Ihre Website so programmieren, dass autonome Agenten sie erkennen und mit ihr zusammenarbeiten, ohne dass Sie jede Integration manuell erstellen müssen. Eine Agentenkarte beschreibt, was Ihre Website tun kann. Das A2A-Protokoll definiert, wie Agenten Aufgaben und Ergebnisse austauschen.

Zusammen sorgen sie dafür, dass Ihre Site an Multi-Agent-Workflows teilnimmt und nicht mehr ein passiver Endpunkt ist, den einzelne Agenten isoliert abfragen.

## Was enthält eine Agentenkarte?

Eine Agentenkarte ist eine JSON-Datei (agent-card.json), die sich im Stammverzeichnis Ihrer Website befindet. Es dient als maschinenlesbares Fähigkeitsmanifest, das anderen Agenten mitteilt, wer Sie sind, was Sie tun können, wie Sie sich authentifizieren und welche Protokolle Sie unterstützen.

Die Hauptfelder: Name (der Name Ihres Dienstes), Beschreibung (was Ihr Dienst in einem Satz tut), URL (Ihre Basis-URL), Funktionen (eine strukturierte Liste von Aktionen, die Ihre Site ausführen kann), Protokolle (welche Kommunikationsstandards unterstützt werden, wie z. B. MCP, REST, A2A), Authentifizierung (wie sich Agenten authentifizieren sollten) und Kontakt (wo Probleme gemeldet werden können).

Jede Funktion in der Liste enthält einen Namen, eine Beschreibung, ein Eingabeschema und ein Ausgabeschema. Anhand dieser Informationen entscheiden Agenten, ob Ihre Website ihnen bei ihrer aktuellen Aufgabe helfen kann.

## Warum Agentenkarten für die Entdeckung wichtig sind

In einem Multi-Agent-Workflow muss ein koordinierender Agent Dienste finden, die bestimmte Teilaufgaben bewältigen können. Ohne Agentenkarten muss der Koordinator anhand des Inhalts der Seite raten. Mit Agent Cards liest der Koordinator ein strukturiertes Manifest und trifft innerhalb von Millisekunden eine fundierte Routing-Entscheidung.

Mit Agentenkarten ist auch eine Weiterempfehlung möglich. Ein Agent, der Ihre Website erfolgreich nutzt, kann seine Agentenkarte an andere Agenten weitergeben, die ähnliche Funktionen benötigen. Dadurch entsteht ein Entdeckungsmechanismus durch Mundpropaganda innerhalb des Agenten-Ökosystems.

## Grundlagen des A2A-Protokolls

Das A2A-Protokoll standardisiert die Art und Weise, wie Agenten Aufgaben austauschen. Ein Agent sendet eine Aufgabenanfrage (was getan werden muss, welche Eingaben verfügbar sind, welche Einschränkungen gelten). Der empfangende Agent bearbeitet die Aufgabe und gibt ein strukturiertes Ergebnis zurück.

Das Protokoll übernimmt die Aufgabenlebenszyklusverwaltung: Aufgabenerstellung, Statusaktualisierungen, Abschluss und Fehler. Es unterstützt auch lang andauernde Aufgaben, bei denen das Ergebnis nicht sofort verfügbar ist.

Für Ihre Site bedeutet die Implementierung von A2A, dass Aufgabenendpunkte verfügbar gemacht werden, die strukturierte Anfragen akzeptieren und strukturierte Antworten zurückgeben. Das Format folgt der A2A-Spezifikation von Google mit typisierten Aufgabenobjekten und Statusaufzählungen.

## Schritt-für-Schritt-Umsetzung

### Schritt 1: Erstellen Sie agent-card.json. Schreiben Sie die JSON-Datei mit der Beschreibung und den Funktionen Ihres Dienstes. Geben Sie genau an, was jede Funktion tut, welche Eingaben sie erfordert und welche Ergebnisse sie liefert. Platzieren Sie es im Stammverzeichnis Ihrer Domain.

### Schritt 2: A2A-Aufgabenendpunkte hinzufügen

Stellen Sie Endpunkte bereit, die Aufgabenanforderungen akzeptieren und Aufgabenergebnisse zurückgeben. Eine minimale Implementierung ist erforderlich: POST /a2a/tasks (eine neue Aufgabe erstellen), GET /a2a/tasks/{id} (den Status der Aufgabe prüfen) und GET /a2a/tasks/{id}/result (das vollständige Ergebnis abrufen).

### Schritt 3: Verbinden Sie sich mit MCP

Wenn Sie bereits über einen MCP-Server verfügen, können Ihre A2A-Aufgabenendpunkte intern an MCP-Tools delegieren. Die A2A-Schicht übernimmt die Kommunikation zwischen Agenten, während MCP die eigentliche Ausführung des Tools übernimmt.

### Schritt 4: Öffentlich registrierenFügen Sie Ihre Agentenkarte in MCP-Datensätze und Agentenverzeichnisse ein, damit Agenten außerhalb Ihres direkten Netzwerks Ihren Service entdecken können.

## Zusammenarbeit in Echtzeit mit WebSockets

Standardmäßige Anfrage-Antwort-Muster funktionieren für einfache Aufgaben. Mehrstufige kollaborative Arbeitsabläufe profitieren von WebSocket-Verbindungen.

Ein WebSocket-Endpunkt in /ws/agent-collaboration ermöglicht es zwei Agenten, eine dauerhafte Verbindung für Arbeitsabläufe aufrechtzuerhalten, die eine Roundtrip-Aushandlung erfordern: Überprüfen mehrerer Verfügbarkeitsslots, Vergleichen von Optionen, Anpassen von Parametern basierend auf Zwischenergebnissen.

Dies ist besonders nützlich für Geschäftsabläufe, bei denen ein Agent in einer koordinierten Reihenfolge Lagerbestände reservieren, Versandoptionen überprüfen, Rabattregeln anwenden und die Zahlungsberechtigung bestätigen muss.

## Agent-Sandbox für Sicherheit

Wenn externe Agenten Aufgaben in Ihrer Infrastruktur ausführen, verhindert Sandboxing, dass sie auf Ressourcen außerhalb ihres autorisierten Bereichs zugreifen.

WASM-basiertes Sandboxing führt vom Agenten übermittelte Vorgänge in isolierten Umgebungen mit definierten Speichergrenzen, CPU-Grenzwerten und Netzwerkzugriffsbeschränkungen aus.

Für die meisten Websites wird Sandboxing relevant, wenn Sie Ausführungsendpunkte bereitstellen, die komplexe Eingaben akzeptieren, oder wenn Sie Agenten erlauben, benutzerdefinierte Logik in Ihrem System auszuführen.

## Vergleich: MCP vs. A2A

| Aussehen | PCM | A2A |
|
---|
---|
---|
| Zweck | Agent-Tool-Kommunikation | Agent-zu-Agent-Kommunikation |
| Entdeckung | Werkzeugschemata | Agentenkarten |
| Interaktionsmuster | Einzelne Anfrage-Antwort | Aufgabenlebenszyklus mit Statusverfolgung |
| Das Beste für | Direkte Ausführung von Werkzeugen | Mehrstufige kollaborative Arbeitsabläufe |
| Seine Umsetzung | JSON-RPC-Server | Aufgabenendpunkte plus Agentenkarte |

Beide Protokolle ergänzen sich. MCP kümmert sich um die Tools. A2A übernimmt die Zusammenarbeit zwischen Agenten, die diese Tools verwenden. Der [AEO-Multi-Agent-Artikel](/es/docs/multi-agent-aeo/) erklärt, wie orchestrierte Arbeitsabläufe von diesen Protokollen abhängen. Der [MCP vs. API-Leitfaden](/es/docs/mcp-vs-api-for-agents/) behandelt die Tool-Zugriffsschicht im Detail.

---

## Häufig gestellte Fragen

**Wie lange dauert die Erstellung einer Agentenkarte?**
30 Minuten für eine einfache Agentenkarte mit 3 bis 5 Funktionen. Die JSON-Struktur ist einfach.

**Benötige ich sowohl MCP als auch A2A?**
Nicht unbedingt. Beginnen Sie mit MCP, wenn Ihr Hauptbedarf darin besteht, dass Agenten Ihre Tools anrufen. Fügen Sie A2A hinzu, wenn Sie möchten, dass Agenten als Peers in Multi-Agent-Workflows mit Ihrem Dienst zusammenarbeiten.

**Was ist der Unterschied zwischen einer Agentenkarte und llms.txt?**
llms.txt ist eine menschen- und maschinenlesbare Übersicht Ihrer Website in Markdown. Eine Agentenkarte ist ein rein maschinenlesbares Funktionsmanifest in JSON. Beide dienen der Entdeckung, Agentenkarten sind jedoch strukturierter und protokollspezifischer.

**Können Agenten meine Website ohne Agentenkarte entdecken?**
Ja, über llms.txt, Schema-Markup oder direktes Seiten-Crawling. Eine Agentenkarte beschleunigt die Entdeckung und ermöglicht die A2A-Zusammenarbeit, aber sie ist nicht die einzige Möglichkeit zur Entdeckung.

**Ist A2A nur für große Unternehmen?**
Nein. Jede Website, die Brokeraktionen anzeigt, kann A2A-Gewinne erzielen. Sogar ein kleiner Dienst mit einem Buchungsendpunkt kann über eine einfache Agentenkarte und einen Aufgabenendpunkt an Arbeitsabläufen mit mehreren Agenten teilnehmen.## Verwandte Anleitungen

* [Agent-Handelsarchitektur](/es/docs/agentic-commerce/)

## Primäre Referenzen

* [A2A-Protokollspezifikation](https://github.com/a2aproject/A2A/blob/main/docs/specification.md)
* [Modellkontextprotokollspezifikation](https://modelcontextprotocol.io/specification/2025-06-18/basic/index)