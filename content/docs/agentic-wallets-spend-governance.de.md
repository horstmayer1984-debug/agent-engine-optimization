---
title: "Agentenportfolios und Ausgabensteuerung: Wie KI-Agenten."
metaTitle: "Agentenportfolios und Ausgabensteuerung."
date: 2026-05-25
weight: 153
category: "Architecture"
description: "Erfahren Sie, wie Agent-Wallets, Ausgabenlimits, Tokenisierung, Prüfprotokolle und Richtlinienkontrollen Zahlungen ermöglichen."
summary: "Ein praktischer Leitfaden für Agenten-Wallets und Kostenmanagement, einschließlich Fireblocks, AP2, Mastercard Agent Pay, delegierte Autorität, Stablecoins und Prüfungskontrollen."
keywords:
  - "Agentenportfolios"
  - "Governance ausgeben"
  - "AI-Agent-Zahlungen"
  - "delegierte Geldbörsen"
  - "Zahlungskontrollen für Agenten"
---
# Agentenportfolios und Ausgabensteuerung

Mit Agent Wallets können KI-Agenten innerhalb der von einem Benutzer oder einer Organisation festgelegten Regeln bezahlen. Die Ausgabenverwaltung ist die Kontrollebene: Budgets, Handelslimits, Token-Umfänge, Prüfprotokolle, Compliance-Prüfungen und Widerruf. Ohne diese Kontrollen sind Agentenzahlungen für den routinemäßigen Handel zu riskant.

## Warum sich Geldbörsen verändern

Eine menschliche Geldbörse geht davon aus, dass eine Person jeden Kauf genehmigt. Eine Agenten-Wallet bedeutet, dass eine Person oder ein Unternehmen begrenzte Befugnisse an die Software delegiert.

Das schafft ein neues Designproblem:

– Der Agent benötigt genügend Autorität, um eine Aufgabe abzuschließen.
- Der Benutzer muss darauf vertrauen können, dass der Agent nicht zu viel ausgeben kann.
- Der Händler benötigt einen Nachweis, dass der Agent zum Kauf berechtigt ist.
- Der Emittent, PSP oder Wallet-Anbieter benötigt einen Prüfpfad.

Die Agentic Payments Suite und Mastercard Agent Pay von Fireblocks weisen auf diese Änderung hin.

## Ausgaben-Governance-Kontrollen

| Kontrolle | Beispiel |
|
---|
---|
| Betragslimit | Der Agent kann bis zu 50 $ pro Einkauf ausgeben |
| Kommerzieller Bereich | Agent kann nur bei zugelassenen Lieferanten kaufen |
| Kategorieumfang | Der Agent kann Büromaterial kaufen, keine Elektronik |
| Zeitfenster | Die Vollmacht erlischt nach sieben Tagen |
| Zweck | Agent kann eine SKU-Familie auffüllen |
| Genehmigungsschwelle | Über einem Grenzwert ist eine menschliche Überprüfung erforderlich |
| Widerruf | Der Benutzer kann die Agent-Token- oder Wallet-Gewährung deaktivieren |
| Audit-Trail | Jede Aktion erfasst die Absicht, die Zahlung und das Ergebnis |

Diese Steuerelemente sind für die [Ausführungsschicht](/es/docs/execution-layer/) unerlässlich.

## Kartentoken vs. Stablecoin-Wallets

| Modell | Stärke | Einschränkung |
|
---|
---|
---|
| Kartennetzwerk-Tokenisierung | Akzeptanz von Familienunternehmen, Emittentenkontrollen, Streitbeilegungsregeln | Benötigen Sie Autorisierungszeichen und Agentenidentität |
| Stablecoin-Wallet | Programmierbare Abwicklung und native Maschinenflüsse | Erfordert Compliance-, Verwahrungs- und Abstimmungskontrollen |
| Kontoguthaben | Nützlich für SaaS und API | Auf eine Plattform beschränkt |
| Banküberweisung/Bahnen in Echtzeit | Gut für Märkte mit schnellen Rechnungszahlungen | Verfügbarkeit und Rückerstattungslogik variieren |

Der [Vergleich der Agentenzahlungsprotokolle](/es/docs/agent-payment-protocols-compared/) bildet die Protokollschicht ab. Diese Seite konzentriert sich auf die Wallet-Kontrollebene.

## Geschäftliche Auswirkungen

Händler sollten damit rechnen, mehr Transaktionen zu erhalten, wenn:

- Ein Agent handelt im Namen eines Benutzers
- Das Zahlungsinstrument hat einen Geltungsbereich
- dem Antrag einen Absichtsnachweis beifügt
- Richtlinienbeschränkungen wirken sich auf die Autorisierung aus
- Streitigkeiten hängen von den Aufzeichnungen der Agenten ab

Das bedeutet, dass Zahlungssysteme mehr Kontext speichern sollten als eine normale Kartenautorisierung.

## Was jetzt vorbereitet werden muss

1. Fügen Sie Felder für die Agentenidentität und die Autorisierungsreferenz hinzu.2. Erfassen Sie Warenkorb-, Checkout- und Fulfillment-Ereignisse gemeinsam.
3. Entscheiden Sie, welche Produkte von den delegierten Vertretern gekauft werden können.
4. Definieren Sie Hochrisikokategorien, die eine menschliche Bestätigung erfordern.
5. Überprüfen Sie die Betrugsregeln für von Agenten durchgeführte Transaktionen.
6. Halten Sie Rückerstattungs- und Stornierungserklärungen maschinenlesbar.

Der Artikel [Fireblocks Agentic Payments Suite](/es/docs/fireblocks-agentic-payments-suite/) behandelt ein Beispiel für eine Infrastruktur.

## Häufig gestellte Fragen

### Ist ein Agent Wallet ein normales digitales Wallet?Nein. Es handelt sich um eine delegierte Wallet oder Zahlungseinrichtung, bei der ein KI-Agent innerhalb expliziter Grenzen agieren kann.

### Können Agent-Wallets Karten verwenden?

Ja. Mastercard beschreibt Agent-Token und Agent Pay für bestimmte Kartennetzwerkzahlungen. AP2 enthält auch Karten- und x402-Beispiele.

### Können Agent-Wallets Stablecoins verwenden?

Ja. Fireblocks beschreibt Agent-Wallets für Stablecoin-Zahlungen innerhalb definierter Limits und Prüfpfade.

### Was ist das größte Risiko?

Unbegrenzte Autorität. Agent-Wallets erfordern strenge Ausgabenlimits, Verwendungszwecke, Sperrung und zuverlässige Protokolle.

## Quellen

Primärquellen: [Ankündigung der Fireblocks Agentic Payments Suite](https://www.prnewswire.com/news-releases/fireblocks-joins-x402-foundation-launches-agentic-payments-suite-302777251.html), [AP2-Dokumentation](https://ap2-protocol.org/), [Mastercard Verifiable Intent](https://www.mastercard.com/europe/en/news-and-trends/stories/2026/verifiable-intent.html) und [Mastercard AI-Powered Purchasing Whitepaper](https://www.mastercard.com/content/dam/mccom/eu/news-and-trends/business-thought-leadership/digital-payments/pdfs/Get_ready_for_AI-powered_shopping_experiences.pdf).