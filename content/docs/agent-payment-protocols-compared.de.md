---
title: "Verglichene Agenten-Zahlungsprotokolle: x402, ACP, MPP, AP2."
metaTitle: "Vergleich der Agenten-Zahlungsprotokolle für den KI-Handel."
date: 2026-05-08
weight: 118
category: "Architecture"
description: "Ein praktischer Vergleich von x402, ACP, MPP, AP2, Visa TAP, Mastercard Agent Pay, UCP und Nevermined für KI-Agentenzahlungen."
summary: "Vergleichsleitfaden für Agentenzahlungsprotokolle im Jahr 2026, der Abrechnung, Zahlung, Autorisierung, Karten, Sitzungen und Agenteninfrastruktur abdeckt."
keywords:
  - "Zahlungsprotokolle für Agenten"
  - "x402 vs. ACP vs. MPP"
  - "AP2-Agentenzahlungen"
  - "AI-Agent-Zahlungen"
  - "Handelsprotokolle für Agenten"
---
# Verglichene Agentenzahlungsprotokolle: x402, ACP, MPP, AP2, TAP, Agentenzahlung

Die Zahlungsprotokolle der Agenten werden im Jahr 2026 in drei Ebenen unterteilt: Abwicklung, Handelskoordinierung und Vertrauen. x402 ist leistungsfähiger für leichte HTTP-Zahlungen und die Abwicklung von Stablecoins. ACP und UCP decken die Einkaufsreise ab. MPP zielt auf automatische wiederkehrende Zahlungen ab. AP2, Visa TAP und Mastercard Agent Pay konzentrieren sich auf Autorisierung, Identität und Vertrauen im Kartennetzwerk.

Dies ist für die Agent Engine-Optimierung wichtig, da Zahlungen nicht mehr nur ein Zahlungsdetail sind. Wenn ein KI-Agent Ihr Angebot entdecken, die Transaktion jedoch nicht bezahlen, autorisieren oder verifizieren kann, ist Ihre Website sichtbar, aber nicht ausführbar.

## Schneller Vergleich

| Protokoll oder System | Hauptsponsoren | Beste Passform | Zahlungsmethode | Typisches Papier im Stapel |
|
---|
---|
---|
---|
---|
| x402 | Coinbase, Cloudflare, Stripe, Linux Foundation-Ökosystem | Pay-per-Request-API und Agentendienste | HTTP 402-Abwicklung, oft Stablecoins | Siedlungsschicht |
| AKP | OpenAI und Stripe | Zahlung im Kontext durch KI-Agenten | Händlerzahlung und Shared Payment Tokens | Handelsfluss |
| MPP | Linie und Tempo | Laufende automatische Zahlungen und API-Nutzung | Sitzungen, Streaming, nutzungsbasierte Abrechnung | Maschinelle Zahlungsschicht |
| AP2 | Google und Zahlungspartner | Demonstrieren Sie die Absicht und Autorisierung des Benutzers | Kryptografische Mandate und Vertrauen | Autorisierungsschicht |
| UCP | Google und kommerzielle Partner | Reise-Shopping-Agenturen | Entdeckung, Katalog, Zahlung, Nachkauf | Handelsprotokollschicht |
| TAP-Visum | Visa-Ökosystem | Das Vertrauen der Händler in KI-Agenten | Identitätszeichen und Anmeldeinformationen für Agenten | Vertrauenswürdige Eisenbahnbrücke und Karte |
| Mastercard-Agentenzahlung | Mastercard | Kartenbasierte Agententransaktionen | Tokenisierte Agentenzahlungen | Kartennetzwerkschicht |
| Nie abgebaut | Nie abgebaut | Monetisierungs-Agent-API, MCP-Tools, geschützte Vermögenswerte | Pläne, Berechtigungen, x402, Kartenflüsse und Stablecoins | Infrastrukturplattform |

## Was hat sich im Mai 2026 geändert?

Der Markt verfügt nicht mehr über einen offensichtlichen Zahlungsstandard. Es hat eine Batterie.

x402 wechselte vom nativen Krypto-Experiment zu einer breiteren Infrastruktur, nachdem die Linux Foundation die x402 Foundation angekündigt hatte und Coinbase zum Protokoll beitrug. Stripe veröffentlichte eine Dokumentation zu automatischen Zahlungen und führte MPP mit Tempo ein. OpenAI und Stripe haben ACP zur Geschäftsschicht hinter Instant Checkout gemacht. Google hat AP2 als Autorisierungsprotokoll vorangetrieben und AP2 dann über die FIDO Alliance in die Standardverwaltung aufgenommen. Visa und Mastercard brachten Vertrauensmodelle von Kartennetzwerken in die Diskussion über Agentenzahlungen ein. Das praktische Fazit ist einfach: Händler sollten nicht fragen: „Welches Protokoll gewinnt?“ Sie sollten fragen: „Welche Schicht löst dieses Protokoll auf?“

## Siedlungsschicht: x402

x402 belebt das HTTP 402 Payment Required-Muster für Agent- und API-Zahlungen wieder. Ein Client fordert eine geschützte Ressource an, der Server sendet Zahlungsanforderungen zurück, der Client fügt einen Zahlungsnachweis bei und der Server gewährt nach Überprüfung Zugriff.

x402 ist stark, wenn das Produkt klein, digital, API-basiert oder auf Anfrage erhältlich ist. Ein Wetterendpunkt, eine Premium-Datenquelle, ein MCP-Tool, ein Inferenzaufruf oder ein maschinenlesbarer Bericht kann pro Aufruf berechnet werden, ohne dass ein Konto erstellt werden muss.Seine Begrenzung ist ebenfalls klar. x402 legt den Wert fest. Es löst nicht den gesamten Kaufprozess von alleine. Ein Händler benötigt weiterhin Produkterkennung, Offenlegung von Richtlinien, Betrugskontrolle, Rückerstattungen, Identität, Steuern, Support und Streitbeilegung.

Lesen Sie den Site-Leitfaden: [Agent Payments x402](/es/docs/x402-agent-payments/).

## Handelsschicht: ACP und UCP

ACP und UCP sind näher am Kaufprozess als x402.

ACP wurde von OpenAI und Stripe entwickelt und ist auf die vom Agenten initiierte Zahlung ausgelegt. Stripe beschreibt Agent Commerce als eine Möglichkeit für Käufer, Agenten und Unternehmen, sichere Transaktionen durchzuführen, mit gemeinsamen Zahlungstokens und Katalogverwaltung im Ablauf.

Die UCP ist umfassender. Es ist als gemeinsame Geschäftssprache für den Agenteneinkauf durch Entdeckung, Kataloginteraktion, Zahlung und Support nach dem Kauf positioniert. Das macht es weniger zu einer Zahlungsmethode als vielmehr zu einer kommerziellen Protokolloberfläche.

Für E-Commerce-Teams sind ACP und UCP relevanter als x402, wenn es sich um einen normalen Einzelhandelskauf und nicht um eine bezahlte API-Anfrage handelt.

## Maschinelle Zahlungsschicht: MPP

MPP, gemeinsam verfasst von Stripe und Tempo, richtet sich an Agenten, die Unternehmen und andere Agenten bezahlen, ohne dass ein Mensch davon weiß. Sein stärkster Anwendungsfall ist keine einmalige Zahlung. Es handelt sich um eine wiederkehrende, kontinuierliche oder gemessene Aktivität.

Das passt gut zu autonomen Systemen. Agenten kennen nicht immer die genaue Anzahl anstehender Anrufe. Möglicherweise benötigen sie nach Abschluss des Auftrags ein Angebot, einen Zeitrahmen, eine Preisobergrenze und eine Abstimmung.

Wenn x402 für eine Anfrage sauber ist, ist MPP für eine Reihe von Anfragen interessant.

## Autorisierungsschicht: AP2

AP2 ist Googles Antwort auf das Vertrauensproblem: Woher weiß ein Händler, dass ein Nutzer den Agenten zum Kauf dieses Artikels unter diesen Bedingungen autorisiert hat? Google beschreibt AP2 als ein offenes Protokoll zur sicheren Initiierung und Abwicklung von agentengesteuerten Zahlungen über Plattformen hinweg. Sein Kernkonzept ist das Mandat: kryptografisch überprüfbare Beweise, die Benutzerabsichten, Warenkorbdetails und Zahlungsautorisierungen erfassen.

AP2 hat weniger mit der Zahlungsmethode als vielmehr mit der Verantwortung zu tun. Es kann mit Karten, Geldbörsen und Kryptowährungsabrechnungsschienen funktionieren. Das macht es zu einer Ergänzung zu x402 und nicht zu einem reinen Ersatz.

## Kartennetzwerkschicht: Visa TAP und Mastercard Agent Pay

Visa TAP und Mastercard Agent Pay lösen ein anderes Problem: Wie sich bestehende Kartennetzwerke an den vom Agenten initiierten Handel anpassen.

Visa TAP bietet Händlern eine Möglichkeit, legitime KI-Agenten von verdächtigem automatisiertem Datenverkehr zu unterscheiden und Anmeldeinformationen und Agentenkontext im gesamten Handelsfluss weiterzugeben. Mastercard Agent Pay nutzt Tokenisierungskonzepte, die bereits im Kartenhandel verwendet werden, und wendet sie auf Agentenzahlungen an.

Diese Systeme sind wichtig, da viele Händler nicht mit Stablecoins beginnen. Sie beginnen mit vorhandenen Karten, Prozessoren, tokenisierten Zugangsdaten und Betrugssystemen, denen sie bereits vertrauen.

## Plattformschicht: Nevermined

Nevermined ist nicht nur ein Protokoll. Es handelt sich um eine Infrastruktur für den kostenpflichtigen Zugriff auf Agent-APIs, MCP-Tools und geschützte Vermögenswerte. Ihre Dokumentation beschreibt die Unterstützung für x402-Flows, Stripe-Zahlungen, Stablecoins, Pläne und Berechtigungsprüfungen.

Das macht Nevermined für Teams relevant, die eine praktische Zahlungsebene für Agenten wünschen, ohne alle Komponenten selbst erstellen zu müssen.## Welches Protokoll sollte ein Unternehmen wählen?

| Unternehmensart | Erstes auszuwertendes Protokoll | Warum |
|
---|
---|
---|
| Zahlungs-API oder Datenanbieter | x402 oder MPP | Auf Wunsch und dosierte Nutzung sind selbstverständliche Möglichkeiten |
| E-Commerce-Händler | ACP oder UCP | Produktfindung und Bezahlung sind wichtiger als Bruttoabrechnung |
| Enterprise Procurement Workflow | AP2 weitere bestehende Zahlungsmethoden | Autorisierung und Prüfbarkeit stehen im Mittelpunkt |
| Schwere Einzelhandelskarte | Visa TAP- oder Mastercard-Agentenzahlung | Bestehende Kartennetzwerke bleiben die operative Basis |
| MCP-Tools-Anbieter | x402, MPP oder Nevermined | Tools benötigen kostenpflichtigen Zugriff, Rechte und sichere Wiederholungsabläufe |

## AEO-Auswirkungen

Für AEO ist das Erfolgsmuster ein Hybrid-Stack.

Eine Website muss maschinenlesbare Produkt- oder Servicedaten veröffentlichen, deterministische Aktionspfade offenlegen, Autorisierungs- und Zahlungsanforderungen dokumentieren und das Ergebnis überprüfbar machen. Zahlungsprotokolle helfen erst, wenn der Agent versteht, was die Website bietet und welche Maßnahmen sicher sind. Nächste interne Schritte: Lesen Sie [AI Agent Protocols](/es/docs/protocols/), [Execution Layer](/es/docs/execution-layer/) und [x402 MCP A2A Full Stack](/es/docs/x402-mcp-a2a-full-stack/).

## Häufig gestellte Fragen

**Was ist das beste Agentenzahlungsprotokoll im Jahr 2026?**
Es gibt kein einzelnes bestes Protokoll. x402 ist leistungsfähiger für einfache HTTP-Abrechnungen, ACP und UCP sind leistungsfähiger für Geschäftsabläufe, MPP sorgt für kontinuierliche automatische Zahlungen und AP2 konzentriert sich auf Autorisierung und Vertrauen.

**Ist x402 besser als ACP?**
x402 und ACP lösen unterschiedliche Schichten auf. x402 wickelt die Zahlungsabwicklung über HTTP ab. ACP kümmert sich um die vom Agenten initiierte Zahlung und die Händlerintegration.

**Ist AP2 eine Zahlungsmethode?**
AP2 wird am besten als Autorisierungs- und Vertrauensprotokoll verstanden. Es kann verschiedene Zahlungsmethoden und Abrechnungsmethoden unterstützen.

**Werden Visa und Mastercard mit x402 konkurrieren?**
Sie konkurrieren in einigen Anwendungsfällen, lösen aber auch unterschiedliche Akzeptanzprobleme. Kartennetzwerke helfen bestehenden Händlern, Agentenzahlungen zu unterstützen, ohne zunächst auf krypto-native Schienen umsteigen zu müssen.

**Was sollten Händler zuerst umsetzen?**
Die meisten Händler sollten mit strukturierten Produktdaten, klaren Richtlinien und für Agenten lesbaren Zahlungsanforderungen beginnen. Die Wahl des Protokolls muss dem Geschäftsmodell folgen.

## Quellen

Zu den für diesen Artikel verwendeten Hauptquellen gehören [Linux Foundation auf der x402 Foundation](https://www.linuxfoundation.org/press/linux-foundation-is-launching-the-x402-foundation-and-welcoming-the-contribution-of-the-x402-protocol), [x402-Dokumentation](https://docs.x402.org/faq), [Stripe on ACP](https://stripe.com/newsroom/news/stripe-openai-instant-checkout), [Stripe Machine Payments](https://docs.stripe.com/payments/machine), [Stripe MPP-Ankündigung](https://stripe.com/blog/machine-payments-protocol), [Google Cloud AP2 Ankündigung](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol/), [Google AP2 FIDO-Update](https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/), [UCP-Dokumentation](https://ucp.dev/), [Visa TAP-Entwicklerseite](https://developer.visa.com/capabilities/trusted-agent-protocol/overview), [Mastercard Agent Pay-Ankündigung](https://www.mastercard.com/news/press/2025/april/mastercard-unveils-agent-pay-pioneering-agentic-payments-technology-to-power-commerce-in-the-age-of-ai/) und [Dokumentation Nevermined](https://nevermined.ai/docs/getting-started/how-it-works).