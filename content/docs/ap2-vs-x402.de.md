---
title: "AP2 vs. x402: Autorisierungsschicht versus Abrechnungsschicht."
date: 2026-05-08
weight: 120
category: "Architecture"
description: "Vergleich von AP2 und x402 für AI-Agent-Zahlungen: Mandate, Vertrauen, Autorisierung, HTTP 402-Abwicklung, Stablecoins und Hybrid-Stacks."
summary: "Ein Vergleich von AP2 und Googles x402, der erklärt, warum AP2 eine Vertrauensschicht und x402 eine Zahlungsabwicklungsschicht ist."
keywords:
  - "AP2 vs. x402"
  - "Agenten-Zahlungsprotokoll"
  - "x402-Zahlungsprotokoll"
  - "Autorisierung von KI-Agenten"
---
#AP2 vs. x402: Autorisierungsschicht vs. Zahlungsabwicklungsschicht

AP2 und x402 ergänzen sich besser als direkte Ersatzprodukte. AP2 antwortet, ob ein Agent berechtigt war, eine Zahlung vorzunehmen. x402 antwortet, wie eine geschützte HTTP-Ressource eine Zahlung anfordern und überprüfen kann. Ein seriöser Agent-Trading-Stack benötigt möglicherweise beides.

Die Verwirrung entsteht durch das Wort „Zahlung“. Bei AP2 geht es um Erlaubnis, Prüfung und Verantwortung. Bei x402 geht es um Siedlung und Zugang.

## Die Kurzversion

| Kriterium | AP2 | x402 |
|
---|
---|
---|
| Hauptfunktion | Zeigt die Autorisierung und Absicht des Benutzers | Zahlung per HTTP anfordern und verifizieren |
| Hauptartefakt | Befehle und kryptografischer Beweis | HTTP 402-Zahlungsanforderung und Zahlungsnachweis |
| Beste Passform | Agentenzahlung, delegierter Handel, Überprüfbarkeit | Kostenpflichtige APIs, MCP-Tools, Datenzugriff, Mikrotransaktionen |
| Bezahlbahn | Unabhängige Zahlungsmethode | Basiert oft auf Stablecoins und erweitert sich durch Ökosystemunterstützung |
| Kernrisiko angesprochen | Darf dieser Agent das kaufen? | Wurde diese Ressource bezahlt? |

## Wofür AP2 entwickelt wurde

Google hat AP2 eingeführt, um Agentenzahlungen plattformübergreifend sicherer zu machen. Das zentrale Thema ist nicht nur die Ausführung von Zahlungen. Es ist eine Autorisierung.

Ein Händler, Emittent oder Zahlungsabwickler benötigt den Nachweis, dass ein Mensch einem Agenten Handlungsvollmacht erteilt hat. Die Beweise müssen auch mit dem endgültigen Auto übereinstimmen. Wenn der Benutzer Laufschuhe für weniger als 120 US-Dollar bestellt hat, sollte der Agent nicht stillschweigend eine Jacke für 230 US-Dollar kaufen.

AP2 begegnet diesem Problem mit Mandatskonzepten. Das Protokoll zeichnet die Benutzerabsicht und den Zahlungskontext auf eine Weise auf, die später überprüft werden kann. Mit dem neuesten AP2-Update von Google wurden auch Lösungen für autonome Transaktionen eingeführt, bei denen der Mensch je nach vorheriger Genehmigung möglicherweise nicht genau zum Zeitpunkt der Zahlung anwesend ist.

Das ist eine Schicht des Vertrauens.

## Wofür x402 konzipiert ist

x402 löst ein konkreteres und sehr praktisches Problem: Wie kann ein Server eine Zahlung anfordern, bevor er Zugriff auf eine Ressource gewährt?

Ein Client fordert eine Ressource an. Der Server antwortet mit HTTP 402 Zahlung erforderlich und Zahlungsdetails. Der Kunde zahlt oder legt einen Zahlungsbeleg bei. Der Server überprüft die Ressource und gibt sie zurück.

Dieses Muster ist besonders für Agenten nützlich, da kleine, automatisierte Transaktionen in herkömmlichen Zahlungssystemen umständlich sind. Ein Agent sollte kein Konto erstellen und ein Abonnement aushandeln, nur um eine API-Antwort zu erwerben.

## Warum AP2 und x402 kombiniert werden können

In einem Hybrid-Stack kann AP2 die Autorisierung nachweisen, während x402 die Abwicklung übernimmt.

Beispielablauf:

1. Ein Benutzer autorisiert einen Agenten, Premium-Marktdaten bis zu einem definierten Budget zu erwerben.2. AP2 erfasst Benutzerabsichten und Autorisierungsgrenzen.
3. Der Agent ruft einen geschützten Datenendpunkt auf.
4. Der Endpunkt gibt eine Zahlungsanforderung x402 zurück.
5. Der Agent rechnet über x402 innerhalb der autorisierten Grenzen ab.
6. Der Händler oder Dienst behält den Nachweis sowohl der Autorisierung als auch der Zahlung.

Dieser Stapel ist stärker als jede der Schichten allein.

## Wo AP2 stärker ist

AP2 ist am stärksten, wenn die Transaktion rechtliche, Compliance-, Betrugs- oder Haftungsrisiken birgt.

Zu den guten Anwendungsfällen für AP2 gehören:1. Einzelhandelskäufe, die von einem Assistenten getätigt werden
2. Agentenbasierte Akquise
3. Reisebuchung
4. Versicherungspolice-Service
5. Einkäufe mit hohem Wert mit zuvor genehmigten Einschränkungen
6. Zahlungen von Agent zu Agent, wenn es um Haftung geht

## Wo x402 stärker ist

x402 ist am stärksten, wenn die Transaktion klein, digital und direkt mit dem Zugriff auf Ressourcen verbunden ist.

Zu den guten Anwendungsfällen für x402 gehören:

1. Bezahlte API-Aufrufe
2. Aufruf des MCP-Tools
3. Premium-Webinhalte für Agenten
4. Datenpakete
5. Rückschluss auf Anfrage
6. Maschinenlesbare Forschungsdateien

## AEO-Auswirkungen

AEO-Teams müssen Zahlungs- und Autorisierungsanforderungen in maschinenlesbarer Form anzeigen.

Dokumentieren Sie für jede zu zahlende Maßnahme Folgendes:

1. Ob die Aktion eine Benutzerautorisierung erfordert
2. Ob eine autonome Ausführung zulässig ist
3. Welche Zahlungsprotokolle werden unterstützt?
4. Wenn die Zahlung x402 akzeptiert wird
5. Welche Vollmacht bzw. welcher Berechtigungsnachweis ist erforderlich?
6. Wie mit Fehlern und Rückerstattungen umgegangen wird
7. Wie ein Agent den Abschluss überprüft

Diese Dokumentation sollte von [llms.txt](/llms.txt), dem [Protokollzentrum](/es/docs/protocols/) und den relevanten Aktionsseiten verlinkt werden.

## Häufig gestellte Fragen

**Ist AP2 besser als x402?**
AP2 eignet sich am besten für Autorisierung und Verantwortlichkeit. x402 eignet sich am besten für die direkte HTTP-Zahlungsabwicklung. Sie lösen verschiedene Schichten.

**Verwendet AP2 x402?**
AP2 ist unabhängig von der Zahlungsmethode und kann mit verschiedenen Schienen arbeiten. x402 kann als Abwicklungsmechanismus in AP2-kompatiblen Flüssen verwendet werden.

**Sollten API-Anbieter AP2 implementieren?**
Die meisten API-Anbieter sollten zuerst x402 oder MPP in Betracht ziehen. AP2 wird wichtiger, wenn die API-Aktion über eine delegierte Autorität, ein hohes Risiko oder ein Kaufmandat verfügt.

**Sollten E-Commerce-Händler x402 implementieren?**
In den meisten Fällen nicht als erstes Protokoll. E-Commerce-Händler benötigen in der Regel mehrere Handels- und Autorisierungsebenen, bevor sie eine reine Abrechnung pro Anfrage vornehmen können.

## Quellen

Wichtige Referenzen: [Google Cloud AP2-Ankündigung](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol/), [Google AP2 FIDO Alliance-Update](https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/), [x402-Dokumentation](https://docs.x402.org/faq) und [x402 Linux Foundation-Ankündigung](https://www.linuxfoundation.org/press/linux-foundation-is-launching-the-x402-foundation-and-welcoming-the-contribution-of-the-x402-protocol).

## Verwandte Leitfäden* [Agent-Commerce-Architektur](/es/docs/agentic-commerce/)
* [Agent-Zahlungsprotokolle](/es/docs/agent-payment-protocols-compared/)