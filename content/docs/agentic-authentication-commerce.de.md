---
title: "Agentenauthentifizierung für den Handel: FIDO, AP2 und Absicht."
metaTitle: "Agentenauthentifizierung für den Handel."
date: 2026-05-25
weight: 152
category: "Architecture"
description: "Erfahren Sie, wie sich die Agentenauthentifizierung für den Handel entwickelt, wie FIDO, AP2 und Verifiable Intent den delegierten Einkauf unterstützen und was sie tun sollten."
summary: "Ein Leitfaden zur Agentenauthentifizierung im Handel, der FIDO-Arbeitsgruppen, AP2-Vorschriften, überprüfbare Absichten von Mastercard, Identität, Datenschutz und Händlervertrauen abdeckt."
keywords:
  - "Agenten-Authentifizierungshandel"
  - "FIDO-Agent-Authentifizierung"
  - "Überprüfbare Absicht"
  - "AP2-Agentenzahlungen"
  - "Handel mit Agentenidentitäten"
---
# Agentische Authentifizierung für den Handel

Die Agentenauthentifizierung ist die Vertrauensebene, die zeigt, dass ein Benutzer einen KI-Agenten zum Handeln autorisiert hat. Das ist wichtig, weil der Handel echtes Geld, Lagerbestände, Loyalität und Verantwortung bewegt. AP2-, Verifiable Intent- und FIDO-Agent-Authentifizierungsarbeiten konzentrieren sich auf ein Kernanliegen: Delegierte Absichten explizit, überprüfbar, privat und überprüfbar zu machen.

## Warum eine normale Anmeldung nicht ausreicht

Traditionelles Bezahlen setzt die Anwesenheit des Menschen voraus. Sie loggen sich ein, klicken auf „Kaufen“, authentifizieren sich und bezahlen. Agentenhandel ändert das. Der Agent kann innerhalb der Regeln des Benutzers suchen, einen Warenkorb erstellen und diesen ausführen.

Das wirft neue Fragen auf:

-Wer hat den Agenten autorisiert?
- Was genau durfte der Agent tun?
- War der Benutzer anwesend oder nicht?
- Hat der Händler die gleiche Absicht erhalten, die der Benutzer angegeben hat?
- Welche Beweise liegen vor, wenn die Transaktion strittig ist?

In der [AP2-Dokumentation](https://ap2-protocol.org/) wird dies als Bedarf an überprüfbaren Absichten und Prüfprotokollen dargelegt.

## Was macht FIDO?

Die FIDO Alliance kündigte Arbeiten zu vertrauenswürdigen KI-Agenteninteraktionen und -Handel an. Beinhaltet eine technische Arbeitsgruppe zur Agentenauthentifizierung, die sich darauf konzentriert, wie Benutzer Aktionen mit starker Authentifizierung, Datenschutz und Sicherheit an KI-Agenten delegieren können.

Google kündigte außerdem an, dass es AP2 an FIDO spenden wird und dass das überprüfbare Absichts-Framework von Mastercard zum gleichen Standardpfad beitragen wird.

Für Händler ist das Signal klar: Agentenidentität und delegierte Authentifizierung werden zur Geschäftsinfrastruktur.

## AP2 vs. überprüfbare Absicht vs. FIDO

| Schicht | Rolle |
|
---|
---|
| AP2 | Zahlungsautorisierungsprotokoll mit Zahlung und Zahlungsmandaten |
| Nachprüfbare Absicht | Vertrauensschicht, die Identität, Absicht und Aktion in einem datenschutzrechtlich geschützten Datensatz verknüpft |
| FIDO | Normungsgremium für Authentifizierungs- und Agenteninteraktionsarbeit |
| Handelssysteme | Richtlinien-, Zahlungs-, Compliance- und Supportentscheidungen durchsetzen |

Dies verbindet sich mit [AP2 vs. x402](/es/docs/ap2-vs-x402/) und [Visa TAP vs. Mastercard Agent Pay](/es/docs/visa-tap-mastercard-agent-pay/).

## Auswirkungen auf die Händlerimplementierung

Händler sollten sich auf die Speicherung und Validierung vorbereiten:

- Agentenidentität oder verifizierter Agentenstatus
- Benutzerautorisierungsstatus
- Absichtsumfang
- Warenkorb-Referenz
- Zahlungsauftragsreferenz
- politische Entscheidung
- Prüfereignisse mit Zeitstempel
- Widerrufs- und Stornierungsstatus

Dies ist nicht nur eine kostenpflichtige Funktion. Es betrifft Support, Betrug, Rückerstattungen, Loyalität und Compliance.

## Authentifizierungsvorbereitungstabelle

| Händlerfrage | Warum ist es wichtig |
|
---|
---|
| Können wir eine menschliche Sitzung von einer Agentensitzung unterscheiden? | Politik und Risiko unterscheiden sich || Können wir überprüfen, wer den Agenten autorisiert hat? | Der delegierte Einkauf erfordert einen Nachweis |
| Können wir den Umfang der Absicht erkennen? | Agenten müssen innerhalb der Grenzen bleiben |
| Können wir Prüfungsnachweise speichern? | Streitigkeiten brauchen Fakten |
| Können Benutzer die Agentenberechtigung widerrufen? | Die Kontrolle muss beim Benutzer verbleiben |

Die Seite [Beweise von Agentengeschäftsstreitigkeiten](/es/docs/agentic-commerce-dispute-evidence/) befasst sich mit der Prüfungsebene.

## Häufig gestellte Fragen

### Ist die Agentenauthentifizierung dasselbe wie die Zahlungsauthentifizierung?Nein. Bei der Zahlungsauthentifizierung wird eine Zahlungsaktion überprüft. Bei der Agent-Authentifizierung müssen außerdem Delegation, Umfang, Agent-Identität und Benutzerabsicht überprüft werden.

### Warum ist FIDO wichtig?

FIDO hat Erfahrung in der Entwicklung offener Authentifizierungsstandards. Seine neuen Arbeitsgruppen können dem Agentenhandel dabei helfen, fragmentierte proprietäre Vertrauenssysteme zu vermeiden.

### Ist dies für alle Händler verfügbar?

Noch nicht. Die meisten Händler sollten zunächst Produktdaten, Richtlinien und Checkout-Beobachtbarkeit vorbereiten und gleichzeitig AP2, Verifiable Intent und FIDO-Einführung überwachen.

### Wie wirkt sich das auf AEO aus?

Agenten benötigen vertrauenswürdige Ausführungspfade. Die Authentifizierung ist eine der Türen zwischen lesbarem Inhalt und sicherem Handeln.

## Quellen

Top-Quellen: [FIDO zu vertrauenswürdigen Interaktionen mit KI-Agenten](https://fidoalliance.org/fido-alliance-to-develop-standards-for-trusted-ai-agent-interactions/), [Google AP2-Spende an FIDO](https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/), [AP2-Dokumentation](https://ap2-protocol.org/) und [Mastercard Verifiable Intent](https://www.mastercard.com/europe/en/news-and-trends/stories/2026/verifiable-intent.html).