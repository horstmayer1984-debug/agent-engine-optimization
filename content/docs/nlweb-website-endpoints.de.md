---
title: "NLWeb-Website-Endpunkte: Lesbare Schnittstellen."
metaTitle: "NLWeb-Website-Endpunkte für Agenten."
date: 2026-06-28
weight: 173
category: "Architecture"
description: "NLWeb stellt Websites mit Endpunkten in natürlicher Sprache für Menschen und KI-Agenten bereit. Finden Sie heraus, wie Schema.org-, RSS-, MCP- und Site-Daten verwendet werden."
summary: "Eine praktische Einführung in NLWeb-Website-Endpunkte, warum sie für von Agenten lesbare Websites wichtig sind und wie Inhalte und Daten vorbereitet werden."
keywords:
  - "NLWeb-Website-Endpunkte"
  - "NLWeb für KI-Agenten"
  - "maschinenlesbare Website-Endpunkte"
  - "Web-API für natürliche Sprache"
  - "NL Web MCP"
---
# NLWeb-Website-Endpunkte

NLWeb ist ein Open-Source-Microsoft-Projekt zum Hinzufügen natürlichsprachlicher Schnittstellen zu Websites. Dies ist wichtig für agentenbereite Websites, da es vorhandene Websitedaten wie Schema.org und RSS in Endpunkte umwandelt, die Menschen und KI-Agenten bedienen können. Es ist eine praktische Brücke zwischen Inhalt, Suche und Tools im MCP-Stil.

## Was ist NLWeb?

Das [Microsoft NLWeb-Repository](https://github.com/microsoft/NLWeb) beschreibt NLWeb als eine Möglichkeit, Konversationsschnittstellen für Websites zu erstellen. In der README-Datei heißt es, dass es MCP nativ unterstützt, Schema.org- und RSS-ähnliche halbstrukturierte Formate verwendet und offene Protokolle sowie Implementierungscode bereitstellt.

Das macht NLWeb für Websites relevant, die möchten, dass Agenten strukturierte Fragen stellen, anstatt Seiten blind zu durchsuchen.

NLWeb sollte nicht als magische SEO-Ebene behandelt werden. Es ähnelt eher dem Schnittstellenmuster einer Website: eine Möglichkeit, das eigene Wissen und die Protokolle der Website durch Zugriff in natürlicher Sprache offenzulegen.

## Warum NLWeb eine neue Chance für Keywords ist

Die meisten Websites denken immer noch in drei Ebenen:

1. HTML-Seiten für Menschen.
2. Sitemaps für Suchmaschinen.
3. API für Entwickler.

NLWeb zielt auf eine vierte Ebene ab: Endpunkte in natürlicher Sprache für KI-gestützte Agenten und Benutzer.

| Schicht | Hauptbenutzer | Typisches Format |
|
---|
---|
---|
| Website | Menschlicher Besucher | HTML |
| Sitemap | Such-Tracker | XML |
| Strukturierte Daten | Suchsysteme und künstliche Intelligenz | Schema.org JSON-LD |
| NLWeb-Endpunkt | Ein Mensch oder ein KI-Agent stellt eine Frage zu einer Aufgabe | Von Site-Daten unterstützte Schnittstelle in natürlicher Sprache |
| MCP-Tool | Agent, der eine strukturierte Aktion benötigt | Werkzeugschema und Endpunkt |

Informationen zur zugehörigen Architektur finden Sie unter [MCP-Ressourcen, Tools und Nachrichten](/es/docs/mcp-resources-tools-prompts/) und [MCP vs. API für Agents](/es/docs/mcp-vs-api-for-agents/).

## Welche Websites sollten NLWeb zuerst sehen?

NLWeb ist am interessantesten für Websites mit umfangreichen und durchsuchbaren Daten:

1. E-Commerce-Kataloge.
2. Reiseinventar.
3. Immobilienanzeigen.
4. Jobbörsen.
5. Dokumentationsportale.
6. Lokale Verzeichnisse.
7. Unterstützen Sie Wissensdatenbanken.
8. Ereignisdatenbanken.

Diese Seiten enthalten bereits strukturierte Fakten. NLWeb bietet ihnen einen konversationsorientierten, für Agenten lesbaren Weg zur Genesung.

## So bereiten Sie sich auf NLWeb vor

Auch wenn Sie NLWeb noch nicht implementieren, bereiten Sie die Datenschicht vor:

1. Verwenden Sie auf allen Seiten und strukturierten Daten konsistente Entitätsnamen.
2. Halten Sie das Schema.org-Markup an den sichtbaren Inhalten ausgerichtet.
3. Pflegen Sie saubere Feeds von Produkten, Artikeln, Ereignissen, Auflistungen oder Dokumenten.
4. Erstellen Sie stabile kanonische URLs für jede wichtige Entität.
5. Aktualisierungshäufigkeit und Verfügbarkeitsregeln für Dokumente.
6. Entscheiden Sie, welche Datenbroker Abfragen durchführen können und welche Daten eine Authentifizierung erfordern.7. Ordnen Sie potenzielle Fragen Quelldatenfeldern zu.

Dies überschneidet sich mit [AI Agent Website Programming](/es/docs/programming-websites-for-ai-agents/) und [Agent-Ready Web Applications](/es/docs/agent-ready-web-apps/).

## NLWeb vs. Scraping| Frage | Geschabt | Endpunkt im NLWeb-Stil |
|
---|
---|
---|
| Kontrolliert die Website die Form der Antwort? | Im Allgemeinen nicht | Ja |
| Kann der Agent eine bestimmte Frage stellen? | Indirekt | Ja |
| Ist die Ausgabe mit den Quelldaten verknüpft? | Oft zerbrechlich | Kontrollierbarer |
| Ist es einfacher, die Zugriffsrichtlinie durchzusetzen? | Härter | Einfacher, wenn es gut gestaltet ist |
| Ersetzt es normale Seiten? | Nein | Nein |

Der strategische Vorteil ist die Kontrolle. Wenn Agenten Ihre Website trotzdem überprüfen, ist ein strukturierter Endpunkt möglicherweise sicherer und genauer, als sie zu zwingen, visuelle Seiten zu durchsuchen.

## Häufig gestellte Fragen

### Ist NLWeb ein offizieller Webstandard?

NLWeb ist ein Open-Source-Microsoft-Projekt mit offenen Protokollen und Implementierungscode. Betrachten Sie es als einen neuen Ansatz, nicht als einen etablierten universellen Standard.

### Ersetzt NLWeb Schema.org?

Nein. NLWeb verlässt sich auf Daten von Websites wie Schema.org und RSS-ähnlichen Formaten. Gut strukturierte Daten sind nach wie vor wichtig.

### Ist NLWeb dasselbe wie MCP?

Nein. NLWeb kann MCP unterstützen, aber MCP ist ein Protokoll für den Austausch von Tools und Kontext. NLWeb konzentriert sich auf Website-Schnittstellen in natürlicher Sprache.

### Sollten jetzt alle Websites NLWeb implementieren?

Nein. Beginnen Sie mit Websites, bei denen Benutzer oder Agenten detaillierte Fragen zu strukturierten Daten auf der Website stellen müssen.

## Quellen

Primär- und Referenzquellen: [Microsoft NLWeb GitHub-Repository](https://github.com/microsoft/NLWeb), [NLWeb README-Rohquelle](https://raw.githubusercontent.com/microsoft/NLWeb/main/README.md), [Model Context Protocol-Dokumentation](https://modelcontextprotocol.io/docs/getting-started/intro), [Schema.org](https://schema.org/) und [Microsoft NLWeb Structured Data-Dokumentation](https://modelcontextprotocol.io/docs/getting-started/intro). Google](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data).