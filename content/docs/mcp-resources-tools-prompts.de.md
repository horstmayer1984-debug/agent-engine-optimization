---
title: "MCP-Ressourcen vs. Tools vs. Eingabeaufforderungen."
date: 2026-05-23
weight: 135
category: "Guide"
description: "Vergleichen Sie MCP-Ressourcen, Tools und Eingabeaufforderungen. Erfahren Sie, was die einzelnen Funktionen bewirken, wann Sie sie verwenden und wie Sie klarere Agentenintegrationen entwerfen."
summary: "Ein praktischer Vergleich von MCP-Ressourcen, Tools und Eingabeaufforderungen für Entwickler, die agentenlesbare Systeme erstellen und Kontextprotokollintegrationen modellieren."
keywords:
  - "PCM-Ressourcen"
  - "MCP-Tools"
  - "MCP-Indikationen"
  - "Funktionen des Modellkontextprotokolls"
  - "Agentenintegrationen"
---
# CCM-Ressourcen vs. Tools vs. Eingabeaufforderungen: Der praktische Unterschied

MCP-Ressourcen stellen Kontext bereit, Tools führen Aktionen aus und Eingabeaufforderungen stellen wiederverwendbare Anweisungen bereit. Der Unterschied ist wichtig, weil ein schlechtes MCP-Design Agenten nicht vertrauenswürdig macht: Daten sollten nicht als Aktion offengelegt werden, Aktionen sollten nicht in Eingabeaufforderungen ausgeblendet werden und Eingabeaufforderungen sollten strukturierte Fähigkeitsdefinitionen nicht ersetzen.

## Die Kurzversion

Das Modellkontextprotokoll weist mehrere Servermerkmale auf. Drei der wichtigsten sind als [Ressourcen](https://modelcontextprotocol.io/docs/concepts/resources), [Tools](https://modelcontextprotocol.io/docs/concepts/tools) und [Nachrichten](https://modelcontextprotocol.io/docs/concepts/prompts) dokumentiert.

Benutzen Sie sie so:

- Ressourcen: „Hier ist ein Kontext, den Sie lesen können.“
- Werkzeuge: „Hier ist etwas, was Sie tun können.“
- Meldungen: „Hier ist eine Workflow-Vorlage, aus der der Benutzer auswählen kann.“

Weitere Informationen finden Sie unter [MCP vs. Agent API](/es/docs/mcp-vs-api-for-agents/), [MCP-Registrierung](/es/docs/mcp-registry-guide/) und im [AEO-Entwicklerhandbuch](/es/docs/developers-guide-aeo/).

## Vergleichstabelle

| Funktion | Beste Verwendung | Wer startet normalerweise | Beispiel |
|
---|
---|
---|
---|
| Ressourcen | Daten und Kontext offenlegen | Client- oder Hostanwendung | Datei, Schaltplan, Produktkatalog, README |
| Werkzeuge | Aktionen oder Berechnungen ausführen | Modell, mit Benutzer-/Client-Steuerung | Ticket erstellen, Datenbank konsultieren, Angebot berechnen |
| Wegbeschreibung | Bereitstellung wiederverwendbarer Workflows | Benutzergesteuerter Befehl oder Auswahl | „Diesen Code überprüfen“ oder „Versionshinweise entwerfen“ |

Diese Aufteilung macht die Integrationen verständlich. Agenten können besser argumentieren, wenn die Grenzen ihrer Fähigkeiten offensichtlich sind.

## Wozu dienen MCP-Ressourcen?

Ressourcen dienen dem Kontext. Die MCP-Spezifikation besagt, dass Ressourcen es Servern ermöglichen, Daten wie Dateien, Datenbankschemata oder anwendungsspezifische Informationen gemeinsam zu nutzen. Jede Ressource verfügt über einen URI und kann Metadaten wie MIME-Typ, Größe, Titel und Anmerkungen enthalten.

Gute Beispiele für Ressourcen:

-`file:///project/README.md`
- Datenbankschema
- Schnappschuss des Produktkatalogs
- API-Endpunktdokumentation
- aktuelle Projektkonfiguration
- Richtliniendokument

Ressourcen müssen stabil genug sein, damit ein Modell sie überprüfen oder referenzieren kann. Sie sollten den Geschäftsstatus beim Lesen nicht ändern.

## Wofür werden MCP-Tools verwendet?

Werkzeuge sind für Aktionen da. Die offizielle Tool-Spezifikation besagt, dass MCP-Server Tools bereitstellen können, die Sprachmodelle aufrufen können, um mit externen Systemen wie APIs, Datenbanken oder Berechnungen zu interagieren.

Gute Beispiele für Tools:

- `create_issue`
- `get_order_status`
- `calculate_shipping_quote`
- `search_inventory`
-`submit_refund_request`
- `run_lighthouse_audit`

Die Tools benötigen Schemata, Validierung, Ratenbegrenzungen, Zugriffskontrolle und Prüfprotokolle. Die Seite [Agent Observability Guardrails](/es/docs/agent-observability-guardrails/) ist hier relevant.

## Wozu dienen MCP-Eingabeaufforderungen? Die Eingabeaufforderungen sind wiederverwendbare Vorlagen. Sie helfen Benutzern oder Kunden, einen bekannten Workflow mit Argumenten auszulösen. Eine Nachricht kann Anweisungen zur Codeüberprüfung, zum Schreiben von Inhalten, zum Onboarding oder zur Support-Triage sammeln.

Die Anweisungen sind nützlich, wenn:

- Der Arbeitsablauf ist wiederholbar
- Der Benutzer muss es absichtlich auswählen
- Das Unterrichtsmuster profitiert von der Konsistenz
- Das Ergebnis hat viel Sprache statt TatenVerstecken Sie die Ausführung nicht in den Eingabeaufforderungen. Wenn sich etwas ändert, gehört es zu einem Tool mit Bestätigung und Registrierung.

## Designfehler, die es zu vermeiden gilt

| Fehler | Warum es Probleme verursacht | Bestes Design |
|
---|
---|
---|
| Aktionen als Ressourcen verfügbar machen | Das Auslesen von Daten kann Nebenwirkungen verursachen | Werkzeuge für Aktionen nutzen |
| Nachrichten als API-Wrapper verwenden | Das Modell kann Parameter | vage ableiten Verwenden Sie ein Werkzeug mit Umriss |
| Fügen Sie den gesamten Kontext in die Werkzeugbeschreibungen ein | Beschreibungen werden aufgeblasen | Ressourcen verfügbar machen |
| Machen Sie jede Datei zu einer Ressource | Zu viel Kontextrauschen | Priorisieren Sie relevante Ressourcen |
| Ohne Ausgabeschema für Werkzeuge | Für Kunden wird es schwieriger, Ergebnisse zu validieren | Verwenden Sie nach Möglichkeit strukturierte Ergebnisse |

## AEO-Auswirkungen

Von Agenten lesbare Websites stehen vor demselben Designproblem wie MCP-Server: separate Inhalte, Anweisungen und Aktionen.

Zum Beispiel:

- Eine Preisseite ist ein öffentlicher Kontext, der einer Ressource ähnelt
- Eine Zahlungs-API ist eine Tool-ähnliche Aktion
- Ein Einkaufsführer ist eine schnelle Hilfe für den Arbeitsablauf

Eine klare Trennung hilft KI-Agenten zu verstehen, was sie lesen, was sie empfehlen und was sie ausführen können. Das ist die praktische Grundlage der [Agent Engine Optimization](/es/docs/what-is-aeo/).

## Checkliste für die Bereitstellung

1. Listen Sie alles auf, was der Agent lesen kann.
2. Listen Sie alle Aktionen auf, die der Agent ausführen kann.
3. Listen Sie die sich wiederholenden Workflows auf, die Benutzer aufrufen können.
4. Weisen Sie jedes Element einer Ressource, einem Tool oder einer Nachricht zu.
5. Fügen Sie Schaltpläne für Werkzeuge hinzu.
6. Fügen Sie nützliche Metadaten für Ressourcen hinzu.
7. Sorgen Sie dafür, dass die Eingabeaufforderungen vom Benutzer kontrolliert werden.
8. Dokumentieren Sie Berechtigungen und Risiken.

## Häufig gestellte Fragen

### Kann ein MCP-Server Ressourcen, Tools und Nachrichten offenlegen?

Ja. Viele nützliche Hosts stellen alle drei zur Verfügung, aber jede Funktion sollte eine klare Funktion haben.

### Sind Ressourcen sicherer als Werkzeuge?

Normalerweise, weil Ressourcen dazu gedacht sind, den Kontext zu lesen. Sie können dennoch sensible Daten preisgeben, wenn die Zugriffskontrolle schwach ist.

### Sollte das Modell automatisch Eingabeaufforderungen aufrufen?

Eingabeaufforderungen sind im Allgemeinen so konzipiert, dass sie vom Benutzer gesteuert oder explizit ausgewählt werden können. Automatische Aktionen müssen mithilfe von Tools und Berechtigungen sorgfältig gehandhabt werden.

### Was ist die wichtigste MCP-Designregel?

Behalten Sie Nebenwirkungen in Tools, Kontext in Ressourcen und wiederverwendbare Anweisungen in Eingabeaufforderungen bei.## Fazit

Bei einem guten MCP-Design geht es vor allem um klare Grenzen. Wenn Ressourcen, Tools und Eingabeaufforderungen jeweils ihre eigene Aufgabe erfüllen, ist es einfacher, Agenten zu vertrauen, sie zu debuggen und zu verbessern.