---
title: "Smolagents-Tool-Aufruf: AEO-Leitfaden."
metaTitle: "Smolagents Tool Calling: AEO-Leitfaden für Agenten."
date: 2026-06-28
weight: 179
category: "Guide"
description: "Hugging Face Smolagents zeigen, wie Code-Agenten und Tool-Call-Agenten funktionieren. Finden Sie heraus, was das bedeutet."
summary: "Ein praktischer Leitfaden zu Smolagenten aus der AEO-Perspektive, der CodeAgent, ToolCallingAgent, Schemata, Sandboxing und Website-Tools abdeckt."
keywords:
  - "Smolagents-Tool-Aufruf"
  - "Umarmendes Gesichtssmolagentikum"
  - "CodeAgent vs. ToolCallingAgent"
  - "AEO-Agent-Tools"
  - "KI-Agent-Tool-Schemata"
---
# Smolagents-Tool-Aufrufe

Smolagents sind für AEO wichtig, weil sie es leicht machen, den Unterschied zwischen codebasierten Agenten und strukturierten Tool-Calling-Agenten zu erkennen. Websites, die klare Tools, Schemata und sichere Ausführungspfade bereitstellen, sind für alle Agentenstile einfacher zu verwenden als Websites, die auf visuellen Vermutungen basieren.

## Was sind Smolagenzien?

Die Hugging Face-Dokumentation beschreibt [smolagents](https://huggingface.co/docs/smolagents/index) als eine Open-Source-Python-Bibliothek zum Erstellen von Agenten mit minimalen Abstraktionen. In ihren Dokumenten werden zwei Hauptagententypen hervorgehoben: „CodeAgent“, der Aktionen als Code schreibt, und „ToolCallingAgent“, der JSON-ähnliche strukturierte Toolaufrufe verwendet.

Das GitHub-Plugin hat auch das Hugging Face-Agenten-Ökosystem aufgetaucht, einschließlich [huggingface/agents-course](https://github.com/huggingface/agents-course). Das Hugging Face-Plugin zeigte den [First Agent Template Space] (https://hf.co/spaces/agents-course/First_agent_template), der rund um Smolagents und Tools beschriftet ist.

## CodeAgent vs. ToolCallingAgent für AEO

| Agententyp | Wie es funktioniert | Website-Anforderung |
|
---|
---|
---|
| Code-Agent | Generieren Sie Code zum Aufrufen von Tools oder Berechnen | Klare Beispiele, sichere Sandboxes, deterministische Ergebnisse |
| Tool Call Agent | Strukturierte Aufrufe an Tools ausgeben | Toolnamen, JSON-Schemas, Validierung, Fehlermeldungen |
| Browser-Agent | Visuelle Seiten bedienen | Semantische Benutzeroberfläche, Beschriftungen, stabile Formen, klare Zustände |

Eine AEO-Strategie sollte alle drei unterstützen, sofern relevant: Dokumente für Code-Agenten, Schemata für Tool-Aufrufer und eine zugängliche Benutzeroberfläche für Browser-Agenten.

## Was für Agenten-Anruftools zu veröffentlichen ist

1. Werkzeugnamen, die die Aktion beschreiben.
2. Geben Sie Schemata mit Pflichtfeldern ein.
3. Ausgabeschemata mit Erfolgs- und Fehlerzuständen.
4. Ratenlimits und Authentifizierungsregeln.
5. Regeln der menschlichen Zustimmung.
6. Beispiele, die zum Produktionsverhalten passen.
7. Versionshinweise, wenn sich Tools ändern.

Anleitungen auf Protokollebene finden Sie unter [MCP-Ressourcen vs. Tools vs. Eingabeaufforderungen](/es/docs/mcp-resources-tools-prompts/) und [MCP vs. Agent-API](/es/docs/mcp-vs-api-for-agents/).

## Auswirkungen auf die Website

smolagents ist kein Website-Optimierungstool. Es ist ein Zeichen dafür, wie Agentenentwickler denken. Sie wollen keine vagen Seiten. Sie brauchen konkrete Maßnahmen.

| Seitentyp | Verbesserte Agentenliste |
|
---|
---|
| API-Dokumente | Fügen Sie Vorgangsbeispiele, Fehler und Authentifizierungsstatus hinzu. |
| Preisseite | Plangrenzen in einer Vergleichstabelle veröffentlichen. |
| E-Commerce-Seite | Anzeigevarianten, Lagerbestand, Preis, Versand und Retouren. |
| Support-Seite | Leiten Sie Vorfälle nach Typ und erforderlichen Daten weiter. |

Das praktische Ziel ist die [Ausführungsschicht](/es/docs/execution-layer/): Agenten müssen vom Lesen einer Seite zum Abschließen einer begrenzten Aufgabe mit Validierung und Wiederherstellung übergehen.

## Häufig gestellte Fragen

### Sind Smolagente nur für Entwickler? Die Bibliothek richtet sich an Entwickler, die Auswirkungen wirken sich jedoch auf Vermarkter, Produktteams und Dokumentationseigentümer aus, da Agenten bessere Website-Schnittstellen benötigen.

### Sollte eine Website Agenten Python-Code zugänglich machen?

Im Allgemeinen nicht. Öffentliche Websites sollten stabile Daten, APIs, Dokumente und Tools bereitstellen. Die Codeausführung gehört in kontrollierte Umgebungen.

### Was ist sicherer: Code-Agenten oder JSON-Tool-Aufrufe?Strukturierte Toolaufrufe sind in der Regel einfacher zu validieren. Codeagenten können flexibler sein, erfordern jedoch eine robuste Testumgebung.

### Wie hängt das mit AEO zusammen?

AEO erleichtert Agenten das Erkennen, Interpretieren, Ausführen und Überprüfen von Inhalten und Aktionen.

## Quellen

Primärquellen: [Smolagents-Dokumentation](https://huggingface.co/docs/smolagents/index), [Smolagents-Agent-Referenz](https://huggingface.co/docs/smolagents/reference/agents), [Hugging Face Agent Course Repository](https://github.com/huggingface/agents-course) und [First Agent Template Space](https://hf.co/spaces/agents-course/First_agent_template).