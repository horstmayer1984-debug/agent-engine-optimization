---
title: "x402 vs. ACP vs. MPP: Zahlungsschicht, Zahlungsschicht, Zahlungsschicht."
metaTitle: "x402 vs. ACP vs. MPP: Vergleich der Protokolle."
date: 2026-05-08
weight: 119
category: "Architecture"
description: "Vergleichen Sie x402, ACP und MPP für KI-Agentenzahlungen, einschließlich HTTP-Mikrozahlungen, Agentenzahlungen, Sitzungen, Streaming, Fiat-Währungen und Stablecoins."
summary: "Ein praktischer Leitfaden zu den Unterschieden zwischen x402, ACP und MPP für Agent Commerce und automatische Zahlungen."
keywords:
  - "x402 vs. ACP vs. MPP"
  - "Automatisches Zahlungsprotokoll"
  - "Agentenhandelsprotokoll"
  - "Mikrozahlungen für KI-Agenten"
---
#x402 vs. ACP vs. MPP: Zahlungsschicht, kostenpflichtige Schicht, automatische Zahlungsschicht

x402, ACP und MPP gelten oft als Konkurrenten, lösen aber unterschiedliche Zahlungsprobleme. x402 ist ein einfaches Abrechnungsmuster für HTTP-Ressourcen. ACP ist ein Händler-Zahlungsprotokoll für vom Agenten initiierte Käufe. MPP ist ein automatischer Zahlungsstandard für Sitzungen, gemessene Nutzung und laufende Agentenaktivität.

Der einfachste Weg, sie zu vergleichen, besteht darin, zu fragen, was der Makler kauft.

Wenn der Agent eine API-Antwort kauft, passt x402. Wenn der Agent ein Produkt von einem Händler kauft, passt ACP. Wenn der Agent während einer laufenden Aufgabe wiederholt zahlt, wird der MPP interessanter.

## Zentraler Unterschied

| Frage | x402 | AKP | MPP |
|---|---|---|---|
| Was wird gelöst? | Bezahlung für geschützte HTTP-Ressourcen | Der Agent hat die Zahlung veranlasst | Automatische Zahlungen im Laufe der Zeit |
| Primärkäufermuster | API-Client oder -Agent | Einkäufer, der für einen Benutzer handelt | Agent-, Service- oder Maschinen-Workflow |
| Einheit mit dem besten Preis-Leistungs-Verhältnis | Eine Anfrage oder eine Ressource | Eine Bestellung oder ein Warenkorb | Sitzung, Streaming, Abonnement, gemessene Nutzung |
| Zahlungsmodell | Liquidation von Common Stable Coins | Händler-Checkout und Checkout-Zugangsdaten | Fiat oder Krypto über automatische Zahlungssitzungen |
| Bestes Beispiel | Zahlen Sie 0,01 USDC für einen API-Aufruf | Kaufen Sie ein Produkt innerhalb eines KI-Assistenten | Bezahlen Sie kontinuierlich für die API-Nutzung |

## Was macht x402 gut?

x402 ist attraktiv, weil es das Protokoll nah am Web hält. Ein Server kann mit HTTP 402 Payment Required antworten, den Preis und die Zahlungsanforderungen angeben und dann die Zahlung überprüfen, bevor er die Ressource bereitstellt.

Für Agenten-Workflows ist dies möglich. Eliminiert die Kontoeinrichtung, Abonnementverhandlung und Bereitstellung von API-Schlüsseln bei kleinen digitalen Transaktionen.

Zu den guten Anwendungsfällen für x402 gehören:

1. Kostenpflichtige MCP-Tools
2. Premium-Datenendpunkte
3. Rückschluss auf Anfrage
4. Maschinenlesbare Berichte
5. Paywalls für für Agenten zugängliche Inhalte
6. API-Aufrufe, bei denen der Preis vor der Ausführung bekannt ist.

Die Schwäche liegt nicht in der technischen Eleganz. Die Schwäche ist der Umfang. x402 beschreibt nicht die gesamte Einkaufsreise, den Warenkorbstatus, Retouren, Steuern, die Abwicklung oder den Kundenservice.

## Was ACP gut macht

ACP ist für den Agentenhandel konzipiert. OpenAI und Stripe haben es für Fälle entwickelt, in denen ein KI-Assistent einem Benutzer hilft, einen Händler zu entdecken, zu bewerten und bei ihm einzukaufen. Die Agent-Commerce-Dokumentation von Stripe zielt auf gemeinsame Zahlungstokens, Produktkatalogverwaltung und kontextbezogene Verkäufe ab. Das ist ein anderes Problem als x402. Ein Einzelhandelskauf ist nicht nur eine Zahlung. Beinhaltet Inventar, Varianten, Versand, Steuern, Fragen zu registrierten Händlern, Bestellbestätigung, Stornierung und Rücksendungen.

Der ACP ist stärker, wenn der Agent innerhalb eines Verbraucherkaufstroms agiert.

## Was MPP gut macht

MPP von Stripe und Tempo ist für automatisierte Zahlungen konzipiert, bei denen der Agent keinen einzigen Anruf tätigt. Sie können im Rahmen einer Sitzung arbeiten, eine Ressource weiterhin nutzen oder im Laufe der Arbeit wiederholt bezahlen.

Das passt gut zu autonomen Systemen. Agenten kennen nicht immer die genaue Anzahl anstehender Anrufe. Möglicherweise benötigen sie nach Abschluss des Auftrags ein Angebot, einen Zeitrahmen, eine Preisobergrenze und eine Abstimmung.

MPP passt konzeptionell am besten zu:1. Fortgesetzte Nutzung der API
2. Agentenabonnements
3. Nutzungsbasierte Abrechnung
4. Zahlungen mit Streaming-Geräten
5. Ein delegiertes Budget für einen autonomen Arbeitsablauf

## Wie Sie drei zusammenarbeiten können

Ein realistischer Stack kann mehr als ein Protokoll verwenden.

Ein KI-Agent kann einen Händler über eine Händleroberfläche entdecken, ACP für die Zahlung verwenden, sich bei der Autorisierung auf AP2- oder Kartennetzwerkkontrollen verlassen und während des Untersuchungsschritts einen externen Datenanbieter über x402 oder MPP bezahlen.

In einem Entwickler-Workflow kann ein Agent kostenpflichtige MCP-Tools über x402 für isolierte Anfragen aufrufen und dann für eine lang laufende Datenaufgabe mit wiederholter Verwendung zu MPP wechseln.

Die wichtige Designregel ist die Trennung von Belangen.

## Was sollten Entwickler zuerst implementieren?

| Sie betreiben | Beginnen Sie mit | Grund |
|---|---|---|
| Eine kostenpflichtige API | x402 | Der Endpunkt kann den Preis festlegen und jede Anfrage überprüfen |
| Eine SaaS-API mit wiederkehrender Verwendung | MPP | Angelegenheit der sitzungs- und nutzungsbasierten Abrechnung |
| Ein E-Commerce-Shop | AKP | Der Bezahlvorgang ist das eigentliche Problem |
| Ein Datenmarkt | x402 und MPP | Manche Vermögenswerte werden einmalig erworben, andere werden vermessen |
| Eine KI-Agentenplattform | ACP, MPP und x402 | Unterschiedliche Verkäufer erfordern unterschiedliche Zahlungsmethoden |

## AEO-Implementierungshinweise

Für AEO muss die Protokollunterstützung sichtbar sein, bevor die Zahlung versucht wird.

Fügen Sie eine maschinenlesbare Seite oder einen maschinenlesbaren Endpunkt hinzu und geben Sie Folgendes an:

1. Unterstützte Zahlungsprotokolle
2. Akzeptierte Münzen oder Schienen
3. Minimale und maximale Upload-Größe
4. Rückerstattungs- oder Stornierungsbedingungen
5. Authentifizierungsanforderungen
6. Fehlercodes
7. Idempotenzregeln
8. Kontakt- oder Streitweg

Dadurch wird die Zahlung von einem versteckten Zahlungsereignis in eine für den Agenten lesbare Funktion umgewandelt.

## Häufig gestellte Fragen

**Ersetzt MPP x402?**Nicht direkt. MPP eignet sich am besten für Sitzungen und Dauergebrauch. x402 bleibt für eine einfache Abwicklung auf Anforderungsebene sauberer.

**Ist ACP nur für ChatGPT?**
ACP wurde mit OpenAI und Stripe für den Agent-Commerce entwickelt, das Protokoll ist jedoch als Open-Commerce-Standard und nicht als reine ChatGPT-Funktion positioniert.

**Kann ein Händler x402 und ACP zusammen verwenden?**
Ja. Ein Händler könnte ACP für Zahlungen und x402 für kostenpflichtigen API-Zugriff, Premium-Daten oder Agentendienste verwenden.

**Welches Protokoll eignet sich am besten für Mikrozahlungen mit Stablecoins?**
x402 ist die eindeutigste Wahl für leichte Stablecoin-Mikrozahlungen über HTTP. Stripe Machine Payments unterstützt auch automatisierte Zahlungen mit Krypto-Abwicklung auf der Stripe-Infrastruktur.

## Quellen

Top-Referenzen: [x402-Dokumentation](https://docs.x402.org/faq), [Ankündigung der Linux Foundation x402 Foundation](https://www.linuxfoundation.org/press/linux-foundation-is-launching-the-x402-foundation-and-welcoming-the-contribution-of-the-x402-protocol), [Stripe ACP-Ankündigung](https://stripe.com/newsroom/news/stripe-openai-instant-checkout), [Stripe Agent Commerce-Dokumentation](https://docs.stripe.com/agentic-commerce), [Stripe Machine Payments-Dokumentation](https://docs.stripe.com/payments/machine) und [Stripe MPP Werbung](https://stripe.com/blog/machine-payments-protocol).

## Verwandte Anleitungen

* [Agent-Commerce-Architektur](/es/docs/agentic-commerce/)
* [Agent-Zahlungsprotokolle](/es/docs/agent-payment-protocols-compared/)
* [Ausführungsebene](/es/docs/execution-layer/)