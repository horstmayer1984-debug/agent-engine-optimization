---
title: "Leitfaden zur Interoperabilität des Agent Trading Protocol."
date: 2026-05-25
weight: 159
category: "Architecture"
description: "Vergleichen Sie, wie UCP-, AP2-, MCP-, A2A-, x402- und Kartennetzwerk-Vertrauensschichten bei Erkennung, Warenkorb, Kasse und Erfüllung zusammenpassen."
summary: "Eine praktische Interoperabilitätskarte für Agent-Commerce-Protokolle, die zeigt, wie sich Erkennung, Kontext, Autorisierung, Zahlung, Koordination und Compliance unterscheiden."
keywords:
  - "Interoperabilität des Agentenhandelsprotokolls"
  - "CPU AP2 MCP A2A x402"
  - "Handelsprotokolle für Agenten"
  - "KI-Handelsarchitektur"
  - "Zahlungsprotokolle für Agenten"
---
# Interoperabilität des Agentenhandelsprotokolls

Der Agentenhandel läuft nicht über ein einziges Protokoll. UCP unterstützt die Zusammenarbeit von Geschäftssystemen, AP2 übernimmt die überprüfbare Zahlungsautorisierung, MCP stellt Tools und Kontext bereit, A2A koordiniert Agenten, x402 verarbeitet maschinennative Zahlungsanfragen und Kartennetzwerk-Vertrauensschichten fügen Identitäts- und Zahlungskontrollen hinzu. Der Trend geht zur Interoperabilität, nicht zum Protokollmonopol.

## Warum Protokollüberschneidungen erwartet werden

Der Handel hat viele Lebenszyklusphasen. Erkennung, Warenkorb, Kasse, Erfüllung, Rückerstattung, Authentifizierung und Agentenkoordination sind unterschiedliche Probleme.

Es ist nicht zu erwarten, dass ein einziges Protokoll sie alle lösen kann.

Die bestehende Seite [UCP vs. ACP vs. MCP](/es/docs/ucp-vs-acp-vs-mcp/) vergleicht drei Hauptmuster. Diese Seite bildet den breiteren Agentenhandels-Stack ab.

## Protokollrollenzuordnung

| Protokoll oder Schicht | Hauptrolle | Handelsphase |
|
---|
---|
---|
| UCP | Handelsfähigkeit, Warenkorb, Kasse, Interoperabilität nach dem Kauf | Entdeckung während des Auftragslebenszyklus |
| AP2 | Autorisierung und nachweisbare Zahlungsmandate | Absicht, Zahlung, Zahlung |
| PCM | Zugriff auf Tools und Kontext | Interne und externe Agenten-Workflows |
| A2A | Koordination zwischen Agenten | Käuferagenten, Händler, Plattformen und Dienstleistungen |
| x402 | Natives HTTP-Zahlungsanforderungs- und Abrechnungsmuster | API, Inhalte und automatische Zahlungen |
| Überprüfbare Absicht/TAP/Agentenzahlung | Vertrauen, Identität, Tokenisierung und Verantwortung | Autorisierungs- und Zahlungsrisiko |

Der [Vergleich der Agent-Zahlungsprotokolle](/es/docs/agent-payment-protocols-compared/) erläutert die Zahlungsseite ausführlicher.

## Beispielablauf

Ein Maklerkauf könnte so ablaufen:

1. Der Agent erkennt Produkte über Seiten, Feeds, Schemata oder UCP-Katalogfunktionen.
2. Der Agent vergleicht Optionen anhand strukturierter Richtlinien- und Produktdaten.
3. Der Agent erstellt einen Warenkorb über UCP oder Merchant API.
4. Die Absicht des Benutzers wird durch Befehle im AP2-Stil oder eine vergleichbare Vertrauensschicht erfasst.
5. Die Zahlung erfolgt mit Karten, Wallets, x402, Stablecoins oder Kontoguthaben.
6. Erfüllungsereignisse werden vom Agenten nach der Zahlung aktualisiert.
7. Streitbeweise verknüpfen die Absicht des Benutzers, die Aktion des Agenten, den Warenkorb, die Zahlung und die Lieferung.

Dies erklärt, warum [Agent Engine Optimization](/es/docs/what-is-aeo/) Arbeit sowohl auf der Leseebene als auch auf der Ausführungsebene erfordert.

## Was Händler nicht tun sollten

Warten Sie nicht darauf, dass ein Standard „siegt“. Entwerfen Sie stattdessen interne Systeme nach stabilen Konzepten:

- Produktidentität
- Benutzerabsicht
- Warenkorbstatus
- Zahlungsautorisierung
- Agentenidentität
- Handelspolitik
- Bestellstatus
- Audit-Trail

Ordnen Sie diese Konzepte dann im Laufe ihrer Reife den Protokollen zu.

## Interoperabilitäts-Checkliste| Internes Objekt | Müssen sich dem Protokoll stellen |
|
---|
---|
| Produkt | Schema, Feed, API-Katalog, UCP |
| Warenkorb | UCP Cart API oder Business Cart |
| Absicht | AP2-Mandat oder überprüfbare Absicht |
| Zahlung | AP2, Kartentoken, Geldbörse, x402, Kontoguthaben |
| Agent | Identität, Authentifizierung, Richtlinie |
| Bestellen | Compliance-Ereignisse und Status-API |
| Prüfung | Gemeinsame Beweisspur |

Die Seite [Beweise für Agentengeschäftsstreitigkeiten](/es/docs/agentic-commerce-dispute-evidence/) deckt die Prüfungsebene ab.

## Häufig gestellte Fragen

### Wird UCP AP2 ersetzen?Nein. UCP und AP2 lösen unterschiedliche Probleme. UCP konzentriert sich auf kommerzielle Interoperabilität; AP2 konzentriert sich auf sichere Zahlungsautorisierungen und -mandate.

### Konkurriert X402 mit AP2?

Manchmal können sie im selben Zahlungsgespräch erscheinen, aber sie sind unterschiedlich. x402 ist eine native HTTP-Zahlungsverhandlung; Bei AP2 geht es um Autorisierung und überprüfbare Absichten im Zusammenhang mit Agentenzahlungen.

### Wo passt MCP hinein?

MCP unterstützt Agenten bei der Nutzung von Tools und Kontext. Es kann Geschäftsabläufe unterstützen, ersetzt jedoch nicht den Checkout oder die Checkout-Protokolle.

### Was sollten Händler zuerst umsetzen?

Beginnen Sie mit der internen Konsistenz der Objekte: Produkt, Warenkorb, Absicht, Kasse, Richtlinie, Bestellung und Prüfung. Danach werden Protokollintegrationen einfacher.

## Quellen

Primärquellen: [UCP-Dokumentation](https://ucp.dev/), [AP2-Dokumentation](https://ap2-protocol.org/), [Google AI und UCP Commerce Update](https://blog.google/products-and-platforms/products/shopping/shopping-updates-google-marketing-live/), [Model Context Protocol-Dokumente](https://modelcontextprotocol.io/docs/concepts/tools), [Cloudflare x402-Ankündigung](https://blog.cloudflare.com/x402/) und [Intent Verifiable Mastercard](https://www.mastercard.com/europe/en/news-and-trends/stories/2026/verifiable-intent.html).