---
title: "MCP vs. A2A: Welches Agentenprotokoll benötigen Sie?"
date: 2026-05-17
weight: 131
category: "Architecture"
description: "Vergleichen Sie MCP und A2A, wie sie sich unterscheiden, wann die einzelnen Protokolle verwendet werden sollten und warum agentenbereite Systeme oft so viel Zugriff benötigen."
summary: "Ein praktischer Vergleich zwischen MCP und A2A für Entwickler, der Tools, Aufgabenteilung, Erkennung, Transport und Multiagentenarchitektur abdeckt."
keywords:
  - "MCP vs. A2A"
  - "Modellkontextprotokoll vs. Agent2Agent"
  - "Vergleich des Agentenprotokolls"
  - "A2A-Protokoll"
  - "MCP-Protokoll"
---
#MCP vs. A2A: Welches Agentenprotokoll benötigen Sie?

MCP und A2A lösen unterschiedliche Probleme. MCP verbindet einen KI-Agenten mit Tools, Daten und Ressourcen. A2A verbindet einen Agenten mit einem anderen, sodass diese Aufgaben und Ergebnisse austauschen können. Wenn Ihr System nur Zugriff auf Tools benötigt, kann MCP ausreichend sein. Wenn mehrere Agenten die Arbeit zwischen Anbietern oder Diensten koordinieren müssen, wird auch A2A relevant.

## Der grundlegende Unterschied

Google beschreibt A2A als offenes Protokoll für Agenten-Interoperabilität und sagt ausdrücklich, dass es MCP ergänzt. Die offiziellen MCP-Architekturdokumente beschreiben MCP als eine Möglichkeit für Clients und Server, Tools, Ressourcen und Eingabeaufforderungen auszutauschen.

Primärquellen:

- [Google Developer Blog: A2A-Ankündigung](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/)
- [Übersicht über die MCP-Architektur](https://modelcontextprotocol.io/docs/learn/architecture)
- [Google Developer Blog: A2A an die Linux Foundation gespendet](https://developers.googleblog.com/google-cloud-donates-a2a-to-linux-foundation/)

| Frage | PCM | A2A |
|
---|
---|
---|
| Wer spricht mit wem? | Agent-Client-zu-Server-Tools | Von Agent zu Agent |
| Hauptobjekt | Werkzeug, Ressource, Hinweis | Aufgabe |
| Das Beste für | Zugriffsmöglichkeiten | Koordinationsarbeit |
| Discovery-Modell | Werkzeugschemata | Agentenfunktionen und Aufgabenverwaltung |
| Typisches Beispiel | „Bestellstatus abrufen“ | „Bitten Sie das Reisebüro, die Reiseroute zu planen“ |

## Verwenden Sie MCP, wenn

MCP ist die beste erste Wahl, wenn ein Agent Folgendes benötigt:

- Dokumente lesen
- Datenbankgestützte Tools aufrufen
- Produktinformationen erhalten
- begrenzte Aktionen auslösen
- mit den Fähigkeiten eines Systems über eine konsistente Schnittstelle arbeiten

Aus diesem Grund erscheint MCP so häufig in der [Ausführungsebene](/es/docs/execution-layer/) und im [MCP vs. API-Leitfaden](/es/docs/mcp-vs-api-for-agents/).

## Verwenden Sie A2A, wenn

A2A ist nützlich, wenn:

- Ein Agent delegiert die Arbeit an einen anderen
- Agenten verschiedener Lieferanten müssen zusammenarbeiten.
- Eine Aufgabe hat ihren eigenen Lebenszyklus und Status
- Das Ergebnis kann einige Zeit dauern
- Mehrere Spezialisten wirken an einem Arbeitsablauf mit

Beispiele:

- Der Beschaffungsagent delegiert die Steueranalyse
- Reisebüro beauftragt die Hotelauswahl
- Der Supportmitarbeiter delegiert die Identitätsüberprüfung
- Der Orchestrierungsagent koordiniert die Erfüllung, Zahlung und Nachrichtenübermittlung.

Der [Multi-Agent-AEO-Leitfaden] (/es/docs/multi-agent-aeo/) erklärt, warum dies wichtig ist, wenn Arbeitsabläufe von Einzelschrittanrufen weggehen.

## Warum viele Systeme beides brauchen

| Schicht | Wahrscheinliches Protokoll |
|
---|
---|
| Agent liest oder führt ein Tool aus | PCM |
| Agent delegiert einen Auftrag an einen anderen Agenten | A2A |
| Agent zahlt für eine Dienstleistung | x402, UCP, ACP oder andere Zahlungsschicht |
| Agent entdeckt wichtige Dokumente auf der Website | „llms.txt“, interne Links, strukturierte Seiten | Ein Reisesystem könnte die Hotelverfügbarkeit über MCP offenlegen, A2A für die Zusammenarbeit mit einem Flugbuchungsagenten nutzen und einen Händler oder ein Zahlungsprotokoll für die Zahlung nutzen. Die Protokolle häufen sich; Sie müssen nicht konkurrieren.

## Architekturbeispiel

Stellen Sie sich einen B2B-Beschaffungsworkflow vor:

1. Ein koordinierender Agent erhält eine Kaufanfrage.
2. Nutzen Sie A2A, um einen Sicherheitsprüfer um eine Anbieterrisikoanalyse zu bitten.
3. Der Sicherheitsüberprüfungsagent verwendet MCP-Tools, um Richtliniendokumente zu lesen und Beweise zu überwachen.
4. Der Koordinator verwendet MCP erneut, um Preise und Integrationen zu überprüfen.
5. Ein anderes Protokoll wickelt die genehmigte Transaktion ab.Wenn Sie nur MCP verwenden, können Sie Tools verfügbar machen. Wenn Sie nur A2A verwenden, können Agenten Jobs austauschen, benötigen aber dennoch die zugrunde liegenden Tools. Ausgereifte Systeme benötigen beide Schichten.

## Entscheidungstabelle

| Wenn Sie brauchen... | Beginnen Sie mit... |
|
---|
---|
| Ein Agent ruft Ihre Produkttools | an PCM |
| Zusammenarbeit zwischen Agenten zwischen Unternehmen | A2A |
| Aufgabenstatus und Delegation | A2A |
| Der schnellste Weg zur sinnvollen Integration | PCM |
| Multi-Agent-Workflow-Orchestrierung | MCP plus A2A |

## Häufig gestellte Fragen

### Ist A2A ein Ersatz für MCP?

Nein. Googles eigene Ankündigung besagt, dass A2A MCP ergänzt.

### Welches Protokoll sollte ein kleines Unternehmen zuerst implementieren?

Im Allgemeinen MCP, da es sofort nützliche Tools und Daten bereitstellt. Fügen Sie A2A hinzu, wenn die Delegation zwischen Agenten zu einer echten Workflow-Anforderung wird.

### Ersetzt A2A Agentenkarten?

Nein. Die Erkennung von Agentenfunktionen und die gemeinsame Nutzung von Protokollen sind verwandte, aber unterschiedliche Anliegen. Weitere Informationen finden Sie im [Agent Card Guide](/es/docs/agent-cards-a2a-protocol/).

### Können MCP und A2A dieselbe Geschäftslogik verwenden?

Ja. Dieselben internen Dienste können MCP-Tools und A2A-Task-Handler über verschiedene Protokolloberflächen übertragen.

## Fazit

MCP stellt Agenten Tools zur Verfügung. A2A bietet Peer-Agenten an. Wenn Ihre Roadmap von Einzelagentenaktionen zu koordinierten Multiagenten-Workflows übergeht, planen Sie beides ein.