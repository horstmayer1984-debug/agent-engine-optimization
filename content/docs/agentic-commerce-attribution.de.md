---
title: "Attribution des Agentenhandels: Messung von Empfehlungen."
metaTitle: "Leitfaden zur Namensnennung des Agentenhandels."
date: 2026-05-25
weight: 151
category: "Guide"
description: "Erfahren Sie, wie Agent Trading die Attribution verändert, warum KI-Benchmarks schwieriger zu messen sind und was Händler aufzeichnen sollten."
summary: "Ein praktischer Leitfaden zur Agent-Commerce-Attribution, der KI-Benchmarks, UCP-Kontext, Agent-Quellensitzungen, Absichtsdaten, Analyselücken und AEO-Metriken abdeckt."
keywords:
  - "Zuschreibung des Agentenhandels"
  - "KI-Empfehlungsverfolgung"
  - "UCP-Kontext"
  - "Analyse des Agentenhandels"
  - "KI-Kaufzuordnung"
---
# Agent Commerce Attribution: Messung von Empfehlungen und KI-Absicht

Bei der Agent-Commerce-Attribution handelt es sich um die Praxis, eine Empfehlung, einen Warenkorb oder eine KI-gestützte Checkout-Sitzung mit dem Agenten, der Oberfläche, der Benutzerabsicht und dem Händlerergebnis zu verknüpfen. Es ist schwieriger als das klassische Empfehlungs-Tracking, da die Entscheidung des Benutzers bereits vor einem normalen Besuch der Website innerhalb eines Systems künstlicher Intelligenz getroffen werden kann.

## Warum sich die Namensnennung ändert

Die klassische E-Commerce-Analyse geht davon aus, dass der Käufer auf einen Link klickt, auf eine Seite gelangt, navigiert, in den Warenkorb legt und kauft. Der Agentenhandel unterbricht diesen Weg. Der Agent kann Produkte recherchieren, Angebote vergleichen, einen Warenkorb erstellen und nur die endgültige Aktion oder Empfehlung an den Händler senden.

Untersuchungen von PayPal-Händlern zeigen, dass sich Unternehmen auf künstliche Intelligenzsysteme vorbereiten, die die Erkennung beeinflussen, bevor der Käufer die Website erreicht. Google bezeichnet UCP und Universal Cart auch als Infrastruktur für den Agentenhandel auf Google-Oberflächen.

Deshalb benötigt [AEO-Messung](/es/docs/aeo-kpis-measurement/) mehr als Rankings und Klicks.

## Was sollten Händler zuordnen?

| Signal | Warum ist es wichtig |
|
---|
---|
| KI-Quelle oder Agentenoberfläche | Zeigt an, wo die Entdeckung stattgefunden hat |
| Benutzerabsichtskategorie | Unterscheiden Sie zwischen Recherche, Warenkorb, Nachbestellung, Support und Rückerstattung |
| ID der dem Agenten angezeigten Produkte | Katalogpräsenz mit Verkäufen verbinden |
| Quelle für die Warenkorberstellung | Zeigt an, ob das Auto innerhalb oder außerhalb des Geländes entstanden ist |
| Zahlungsüberweisung | Zeigt an, wo der Kauf abgeschlossen wurde |
| Befehls- oder Autorisierungsreferenz | Links mit Zahlungsabsicht, sofern unterstützt |
| Compliance-Ergebnis | Verknüpfen Sie Agenten-Ursprungstransaktionen mit Lieferungen und Retouren |

Das Modell [Fünf Ebenen des Agentenhandels] (/es/docs/five-levels-agentic-commerce/) ist nützlich, da sich die Attributionsreife auf jeder Ebene ändert.

## Das UTM-Problem

UTM-Tags sind immer noch nützlich, wenn ein KI-Assistent einen Benutzer auf eine Seite weiterleitet. Sie sind jedoch schwach, wenn der Agent einen Besucher nicht einfach empfiehlt.

Reisebüros benötigen möglicherweise:

- signierte Kontextobjekte
- Warenkorb-Referenzen
- Produktkandidatenlisten
- Befehls-ID
- Einwilligungsstatus
- Plattformkennungen
- Bestätigung vom registrierten Händler

Dies kommt der Transaktionsverfolgung näher als der Kampagnenverfolgung.

## AEO-Metriken für Agentenhandel

| Metrisch | Was es Ihnen sagt |
|
---|
---|
| Vom Agenten empfohlene Sitzungen | Wie oft senden KI-Systeme Datenverkehr?
| Gebühr für den Agent-Ursprungswagen | Wenn Agenten erfolgreich Autos bauen können |
| Strukturierte Katalogabdeckung | Wie viel Inventar ist maschinenlesbar?
| Abschluss der Agentenzahlung | Funktioniert die Überweisung bzw. native Zahlung |
| Ablehnungsrate von Richtlinien | Wenn Richtlinien Agententransaktionen blockieren || Ausnahmequote nach dem Kauf | Wenn von Agenten bezogene Bestellungen zu mehr Rückerstattungen oder Supportproblemen führen |

Verknüpfen Sie diese Metriken mit der [Ausführungsschicht](/es/docs/execution-layer/), nicht nur mit Inhaltsberichten.

## Checkliste für die Bereitstellung1. Behalten Sie die normale Referenzverfolgung und UTM bei.
2. Fügen Sie dem zu analysierenden Agenten Quellereignisnamen hinzu.
3. Notieren Sie den Benutzeragenten, den verifizierten Bot-Status und die Quellplattform, sofern verfügbar.
4. Speichern Sie den Warenkorb-Ursprung und den Warenkorb-Übertragungspfad.
5. Ordnen Sie Produkt-IDs Daten zu, die in Feeds, Schemas und APIs verfügbar gemacht werden.
6. Verfolgen Sie Zahlungsfehler separat für Agentenquellensitzungen.
7. Bestell-, Rückerstattungs- und Supportdaten mit dem Quellkontext verknüpfen.

Der [Universal Trading Protocol-Leitfaden](/es/docs/universal-commerce-protocol/) erklärt, wo der Handel in den Handelskontext eingepasst werden kann.

## Häufig gestellte Fragen

### Sind KI-Verweise in Google Analytics sichtbar?

Einige sind als normale Empfehlungen oder Kampagnenverkehr sichtbar. Andere können als direkter, Bot-, Partner- oder plattformvermittelter Datenverkehr angezeigt werden, es sei denn, die Integration bewahrt den Kontext.

### Ist die Namensnennung nur ein Marketingproblem?

Nein. Im Agentenhandel wirkt sich die Namensnennung auch auf Betrug, Streitprüfung, Handelspolitik und Support nach dem Kauf aus.

### Was ist die erste Metrik, die hinzugefügt werden soll?

Verfolgen Sie Agenten-Ursprungssitzungen und Warenkorbstarts getrennt vom regulären organischen, bezahlten und direkten Traffic.

### Wie hängt das mit AEO zusammen?

AEO muss nachweisen, dass eine von Agenten lesbare Infrastruktur die Erkennung, Warenkorbaktivität, abgeschlossene Aktionen und zuverlässige Ergebnisse fördert.

## Quellen

Top-Quellen: [Ergebnisse von PayPal Agentic Commerce Pulse](https://www.paypal.com/us/brc/article/agentic-commerce-pulse-report-findings), [PayPal auf AI Storefronts](https://www.paypal.com/us/brc/article/ai-storefront-what-merchants-need-to-know) und [Update für Google UCP und Universal Cart](https://blog.google/products-and-platforms/products/shopping/shopping-updates-google-marketing-live/).