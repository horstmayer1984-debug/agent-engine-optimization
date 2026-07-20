---
title: "UCP, ACP und MCP: die drei Protokolle, die fördern werden."
metaTitle: "UCP vs. ACP vs. MCP: Vergleich der Protokolle."
date: 2026-04-14
weight: 90
category: "Framework"
description: "MCP stellt Kontext bereit, UCP kümmert sich um die Handelslebenszyklen, ACP ermöglicht den nativen ChatGPT-Checkout. Wie sich die drei Protokolle unterscheiden."
metaDescription: "Compare MCP, UCP y ACP en el intercambio de contexto, los ciclos de vida del comercio, el pago, el uso de herramientas y cuándo encaja cada protocolo."
summary: "Im Jahr 2026 werden drei Protokolle die Agenteninfrastruktur dominieren. MCP verbindet Agenten mit Daten. UCP übernimmt den gesamten Handelslebenszyklus. ACP ermöglicht die Zahlung innerhalb von ChatGPT. Hier erfahren Sie, wann Sie die einzelnen Elemente verwenden sollten."
keywords:
  - "UCP vs. ACP vs. MCP"
  - "Handelsprotokolle für Agenten"
  - "Universelles Handelsprotokoll"
  - "Agentenhandelsprotokoll"
  - "Vergleich des Modellkontextprotokolls"
  - "Agent-Protokollstapel 2026"
---
Im Jahr 2026 dominieren drei Protokolle die Infrastrukturebene der Agent Engine Optimization. Jedes löst ein anderes Problem. Die Wahl des Falschen verschwendet Entwicklungszeit. Durch die Wahl der richtigen Kombination erhalten Agenten einen vollständigen Weg vom Datenzugriff bis zum Abschluss der Transaktion.

MCP (Model Context Protocol) verbindet Agenten mit ihren Daten. UCP (Universal Commerce Protocol) verwaltet den gesamten Handelslebenszyklus. ACP (Agent Commerce Protocol) ermöglicht die direkte Zahlung innerhalb von ChatGPT, ohne dass der Käufer Ihre Website besucht.

## MCP: Agenten Zugriff auf ihre Daten und Tools gewähren

Anthropic hat MCP entwickelt und auf die Linux Foundation portiert. Es handelt sich um ein vertikales Integrationsprotokoll. Ein MCP-Server stellt seine internen Datenquellen, Dokumente und Tools über eine standardisierte JSON-RPC-Schnittstelle den KI-Agenten zur Verfügung.

MCP beantwortet eine Frage: Was kann mir dieses System sagen und welche Tools kann ich verwenden? Es ermöglicht Agenten, Ihr CMS abzufragen, Dokumente abzurufen, Datenbankeinträge zu überprüfen und interne Funktionen aufzurufen. Sie wickelt Zahlungen, Zahlungsströme und Geschäftstransaktionen nicht selbst ab.

Verwenden Sie MCP, wenn Agenten auf Ihre Unternehmensdaten (Produktkataloge, Dokumentation, Wissensdatenbanken) zugreifen müssen, wenn Sie möchten, dass jeder MCP-fähige Agent Ihre Tools ohne eine benutzerdefinierte Integration entdecken und verwenden kann, und wenn die Interaktion eher lesend oder abfragend als transaktional erfolgt.

Die technische Implementierung ist ein JSON-RPC 2.0-Server, der Tools (Funktionen, die Agenten aufrufen können), Ressourcen (Daten, die Agenten lesen können) und Nachrichten (Vorlagen, die Agenten verwenden können) ankündigt. Der [MCP vs. API-Leitfaden] (/docs/mcp-vs-api-for-agents/) behandelt die Implementierung im Detail.

## UCP: Verwalten Sie den gesamten Handelslebenszyklus

Google hat UCP in Zusammenarbeit mit Shopify, Target, Walmart, Etsy und Wayfair entwickelt. Es wurde im Januar 2026 auf NRF eingeführt. UCP ist das Protokoll für den gesamten Handelslebenszyklus: Bestandsüberprüfung, Preisverhandlung, Zahlungsautorisierung, Bestellversand und Erfüllungsverfolgung.

Die wichtigste technische Neuerung ist das Capability Statement. Ihr Shop veröffentlicht eine JSON-Manifestdatei unter /.well-known/ucp, die den Agenten genau mitteilt, welche Transaktionen, Rabatte, Zahlungsmethoden und Richtlinien unterstützt werden. Der Agent liest dieses Manifest, bevor er eine Interaktion versucht, sodass Sie nie raten müssen.

UCP arbeitet mit dem Agent Payments Protocol (AP2) für kryptografische Zahlungsmandate und Prüfprotokolle. Zusammen ermöglichen sie es Agenten, den Lagerbestand zu überprüfen, Preise zu validieren, Zahlungen zu autorisieren, Bestellungen aufzugeben und die Erfüllung über einen einzigen standardisierten Ablauf zu verfolgen. Verwenden Sie UCP, wenn Sie Produkte oder Dienstleistungen über ein Geschäft verkaufen, wenn Sie möchten, dass Agenten, die im Google AI-Modus oder Gemini arbeiten, mit Ihnen Transaktionen abwickeln, und wenn Sie den gesamten Kauflebenszyklus benötigen, von der Entdeckung bis zur Bestätigung der Ausführung.

Der [Agent Trade Execution-Artikel] (/docs/agentic-commerce-execution/) erklärt, wie UCP in E-Commerce-Architekturen funktioniert.

## ACP: Zahlung innerhalb von ChatGPT

OpenAI hat ACP in Zusammenarbeit mit Stripe entwickelt. Es handelt sich um ein Open-Source-Protokoll, das speziell dafür entwickelt wurde, Reibungsverluste zu minimieren, indem Zahlungen direkt über die ChatGPT-Schnittstelle abgewickelt werden.Der Schlüsselmechanismus ist SharedPaymentToken. Die Zahlungsdaten des Käufers werden sicher an den Händler weitergegeben, ohne dass der Käufer ChatGPT verlässt. Der Agent kümmert sich um die Produktauswahl, das ACP-Protokoll kümmert sich um den sicheren Austausch von Zahlungstokens und die Transaktion wird nativ innerhalb der Konversation abgeschlossen.

Verwenden Sie ACP, wenn Ihr primärer agentengesteuerter Vertriebskanal ChatGPT ist, wenn Sie eine Zahlung ohne Weiterleitung durchführen möchten (der Käufer besucht Ihre Website nie) und wenn Sie Stripe als Zahlungsabwickler verwenden (ACP lässt sich nativ in die Stripe-Infrastruktur integrieren).

## Wie die drei Protokolle zusammenarbeiten

Die Protokolle sind keine Konkurrenten. Verschiedene Schichten desselben Stapels dienen.

MCP stellt die Datenschicht bereit. Ein Agent verwendet MCP, um auf Ihren Produktkatalog zuzugreifen, Spezifikationen zu überprüfen und Dokumentation abzurufen.

UCP stellt die Business-Schicht bereit. Sobald der Agent über die benötigten Daten verfügt, wickelt UCP die Transaktion ab: Bestandsreservierung, Preisvalidierung, Zahlungsautorisierung und Versand der Bestellung.

ACP stellt die Schnittstellenschicht speziell für ChatGPT bereit. Bindet das Zahlungserlebnis mithilfe sicherer Zahlungstokens in die ChatGPT-Konversation ein.

Eine vollständige, für Agenten bereite Infrastruktur könnte alle drei nutzen: MCP für den Datenzugriff, UCP für den Geschäftslebenszyklus in Google-basierten Agenten-Workflows und ACP für native ChatGPT-Transaktionen.

## Protokollvergleich

| Aussehen | PCM | UCP | AKP |
|
---|
---|
---|
---|
| Entwickler | Anthropo (Linux Foundation) | Google mit Shopify und Partnern | OpenAI mit Streifen |
| Hauptzweck | Zugriff auf Daten und Tools | Vollständiger Handelslebenszyklus | Zahlung im Chat |
| Technische Basis | JSON-RPC 2.0 | Kapazitätserklärung plus AP2 | Geteilter Zahlungstoken |
| Zahlungsverwaltung | Keine native Zahlung | Ja, über AP2 | Ja, über Stripe |
| Wo Agenten Transaktionen durchführen | Jede MCP-kompatible Umgebung | Google AI-Modus, Zwillinge | ChatGPT |
| Entdeckungsmechanismus | Schemata von Werkzeugen und Ressourcen | /.well-known/ucp manifest | ACP-Endpunktregistrierung || Das Beste für | Datenabfragen, Zugriff auf Tools | E-Commerce, Reservierungen, Dienstleistungen | ChatGPT Native Sales |
| Implementierungsaufwand | 2 bis 4 Stunden für Basisserver | 1 bis 2 Wochen für den gesamten Lebenszyklus | Tage, erfordert Stripe-Integration |

## Strategischer Entscheidungsrahmen

Wenn Sie möchten, dass Agenten auf Ihre Daten und Tools zugreifen, implementieren Sie zuerst MCP. Es lässt sich am schnellsten implementieren und bedient das breiteste Spektrum an Agenten.

Wenn Sie Produkte oder Dienstleistungen verkaufen und möchten, dass Agenten des Google-Ökosystems diese kaufen: Fügen Sie UCP mit einer Fähigkeitserklärung in /.well-known/ucp hinzu.

Wenn ChatGPT ein wichtiger Vertriebskanal für Ihr Unternehmen ist: Fügen Sie ACP mit Stripe-Integration hinzu.

Wenn Sie eine maximale Abdeckung wünschen: Setzen Sie alle drei um. MCP für die Datenschicht, UCP für den Handel im Google-Ökosystem, ACP für den ChatGPT-Handel. Die zugrunde liegende Geschäftslogik wird gemeinsam genutzt. Lediglich die Protokollschnittstellen unterscheiden sich.

Die [Artikel zum x402-Protokoll] (/docs/x402-agent-payments/) behandeln die ergänzende Mikrozahlungsschicht, die mit allen drei Protokollen zusammenarbeitet.

---

## Häufig gestellte Fragen

**Benötige ich alle drei Protokolle?**
Nein. Beginnen Sie mit MCP, um auf Daten zuzugreifen. Fügen Sie UCP oder ACP hinzu, je nachdem, welche KI-Plattformen Ihren Umsatz steigern. Die meisten Unternehmen beginnen mit einem Handelsprotokoll und fügen das zweite hinzu, wenn der Kanal dies erfordert.**Können UCP und ACP auf derselben Site koexistieren?**
Ja. Sie bedienen unterschiedliche Ökosysteme von Agenten. UCP kümmert sich um von Google betriebene Agenten. ACP verwaltet ChatGPT. Die gleichen Produktdaten und die gleiche Geschäftslogik dienen beiden über unterschiedliche Protokollschnittstellen.

**Gilt MCP nur für technische Produkte?**
Nein. Jedes Unternehmen, das über Daten verfügt, auf die Agenten zugreifen müssen, profitiert von MCP. Ein Restaurant mit Speisekarte, ein Hotel mit Zimmerverfügbarkeit, ein Berater mit Leistungsbeschreibungen. MCP macht Agenten alle strukturierten Informationen zugänglich.

**Welches Protokoll wurde im April 2026 am häufigsten angenommen?**
MCP hat die größte Akzeptanz (Hunderttausende von Websites). UCP ist das dominierende Handelsprotokoll mit erheblicher Unterstützung für den Einzelhandel. ACP ist neuer, wächst aber innerhalb des ChatGPT-Ökosystems schnell.

**Was ist eine Leistungserklärung?**
Ein unter /.well-known/ucp veröffentlichtes JSON-Manifest, das den Agenten genau mitteilt, was Ihr Shop unterstützt: welche Transaktionstypen, Zahlungsmethoden, Rabattregeln und Richtlinien verfügbar sind. Agenten lesen es, bevor sie eine Interaktion versuchen.

## Primäre Referenzen

* [Modellkontextprotokollspezifikation](https://modelcontextprotocol.io/specification/2025-06-18/basic/index)
* [MCP-Server-Grundelemente](https://modelcontextprotocol.io/specification/2025-06-18/server/index)