---
title: "Referenzrahmen und Agentenbewertung: AEO-basiert."
metaTitle: "Benchmarks zur Agentenbewertung auf AEO-Basis."
date: 2026-04-12
weight: 84
category: "Guide"
description: "Frameworks zur Agentenbewertung messen Aufgabenautonomie, Genauigkeit, Kosten, Latenz und Erfolg während des gesamten Lebenszyklus. Tun."
metaDescription: "Utilice puntos de referencia de evaluación de agentes para medir la autonomía, la precisión, el costo, la latencia y el éxito de las tareas durante todo."
summary: "Die Bewertung der Agentenleistung geht über die Genauigkeit hinaus. Moderne Frameworks messen Autonomie, Kosteneffizienz, Latenz und die Erledigung realer Aufgaben. Hier erfahren Sie, wie Sie eine Bewertungspraxis aufbauen."
keywords:
  - "Frameworks zur Agentenbewertung"
  - "KI-Agent-Benchmarks"
  - "AEO-Agententest"
  - "Agentenpräzisionsmessung"
  - "LangChain-Bewertungen"
  - "Kennzahlen zur Agentenleistung"
---
Frameworks zur Agentenbewertung messen nicht nur die Genauigkeit, sondern auch Autonomie, Kosten, Latenz und Erfolg realer Aufgaben während des gesamten Lebenszyklus des Agenten. Sie verwandeln AEO vom Rätselraten in eine datengesteuerte Optimierung, indem sie genau zeigen, wo die Interaktionen der Agenten mit Ihrer Website erfolgreich sind und wo sie scheitern.

## Warum die Bewertung für AEOs wichtig ist

Wenn ein Agent mit Ihrer Site interagiert, hängt das Ergebnis sowohl von den Fähigkeiten des Agenten als auch von der Struktur Ihrer Site ab. Bewertungsrahmen helfen Ihnen, die beiden zu trennen. Wenn Agenten Ihre Preise immer wieder nicht ermitteln können, liegt das Problem an Ihren strukturierten Daten. Wenn Agenten korrekt auschecken, aber das falsche Produkt empfohlen wird, liegt das Problem an Ihrer Entitätszuordnung.

Ohne Bewertung kann diese Unterscheidung nicht getroffen werden. Jeder Ausfall sieht von außen gleich aus.

## Die fünf Dimensionen der Agentenbewertung

### Genauigkeit

Ruft der Agent korrekte Informationen von Ihrer Website ab? Vergleichen Sie die vom Agenten extrahierten Daten mit ihrer wahren Quelle. Produktnamen, Preise, Verfügbarkeit, Spezifikationen und Versicherungsbedingungen müssen genau übereinstimmen.

Messen Sie die Genauigkeit pro Seite und pro Datenfeld. Eine Website kann bei den Produktnamen zu 98 Prozent korrekt sein, bei den Versandrichtlinien jedoch nur zu 75 Prozent. Diese Spezifität zeigt Ihnen, worauf Sie sich bei der Verbesserung konzentrieren sollten.

### Autonomie

Wie viele Schritte kann der Agent ohne menschliches Eingreifen abschließen? Eine vollständig autonome Interaktion (Erkennung, Extraktion, Aktion, Zahlung, Verifizierung) erzielt eine höhere Punktzahl als eine, die in Schritt drei die Zustimmung eines Menschen erfordert.

Für AEO misst dies, wie gut Ihre Ausführungsebene End-to-End-Agent-Workflows unterstützt. Der [Leitfaden zur Ausführungsebene](/es/docs/execution-layer/) erläutert die Infrastrukturanforderungen.

### Rentabilität

Wie viel kostet jede Agenteninteraktion an Token, API-Aufrufen und Verarbeitungszeit? Hohe Kosten pro Interaktion hemmen den Agentenverkehr. Websites mit sauberen, komprimierten Daten senken die Agentenkosten und ziehen eine höhere Nutzung an.

Context Engineering (siehe [Context Engineering Guide](/es/docs/context-engineering-aeo/)) verbessert direkt die Rentabilität, indem es die Datenmenge reduziert, die Agenten verarbeiten müssen.

### Latenz

Wie lange dauert jede Interaktion? Agenten laufen normalerweise nach 10 bis 30 Sekunden ab. Wenn Ihre Endpunkte innerhalb von 200 Millisekunden reagieren, werden die Arbeitsabläufe der Agenten reibungslos abgeschlossen. Wenn sie innerhalb von 8 Sekunden antworten, können Agenten aufgeben oder es erneut versuchen.

Messen Sie die Latenz pro Endpunkt und pro Interaktionsschritt. Identifizieren Sie Engpässe, die mehrstufige Arbeitsabläufe verlangsamen.

### AufgabenabschlussrateDie ultimative Metrik. Wie viel Prozent der Agenten-Workflows, die Ihre Website betreffen, werden erfolgreich abgeschlossen? Ein Workflow, der mit der Produkterkennung auf Ihrer Website beginnt, aber nicht zur Kasse geht, gilt als unvollständig.

Verfolgen Sie den Abschluss nach Workflow-Typ. Vergleichsworkflows, Einkaufsworkflows und Abfrageworkflows können sehr unterschiedliche Erfolgsraten aufweisen, wobei jeder auf unterschiedliche Optimierungsmöglichkeiten abzielt.

## Aufbau einer BewertungspraxisBeginnen Sie mit der manuellen Auswertung. Führen Sie alle zwei Wochen 20 repräsentative Abfragen durch KI-Assistenten durch und dokumentieren Sie die Ergebnisse. In welchen Suchanfragen wird Ihre Website erwähnt? Sind die extrahierten Informationen korrekt? Kann der Agent die beabsichtigte Aufgabe erledigen?

Eskalieren Sie zur automatisierten Bewertung. Erstellen Sie Testskripte, die Agenteninteraktionen simulieren, Daten von Ihren Seiten extrahieren, versuchen, Endpunkte aufzurufen, und die Ergebnisse mit Ihren Erwartungen vergleichen. Führen Sie sie täglich durch.

Fügen Sie Regressionstests hinzu. Wenn Sie den Inhalt, das Schema oder die Endpunkte ändern, führen Sie den Evaluierungssatz erneut aus, um sicherzustellen, dass keine Probleme vorliegen. Die Veränderungen, mit denen die Beamten konfrontiert sind, haben weitreichende Auswirkungen, die bei Tests am Menschen nicht immer offensichtlich sind.

## Evaluierungstools im Jahr 2026

LangChain Evals bietet Bewertungsketten, die die Abrufgenauigkeit, Antwortqualität und den korrekten Einsatz von Tools testen. Integrieren Sie es in Ihre vorhandenen LangChain- oder LangGraph-Agent-Implementierungen.

Ragas konzentriert sich auf die Recovery-Augmented-Generation-Bewertung. Misst Kontextrelevanz, Antworttreue und Antwortrelevanz. Nützlich, um zu bewerten, wie gut Agenten Ihre Inhalte nutzen.

TruLens bietet eine verfolgungsbasierte Auswertung, die dem gesamten Argumentationspfad eines Agenten folgt. Nützlich, um zu verstehen, warum ein Agent eine bestimmte Entscheidung bezüglich Ihres Inhalts getroffen hat.

Der [AEO-KPI-Leitfaden](/es/docs/aeo-kpis-measurement/) deckt den breiteren Messrahmen ab.

## Vergleich: Ad-hoc-Tests versus strukturierte Bewertung

| Fokus | Ad-hoc-Tests | Strukturierte Auswertung |
|
---|
---|
---|
| Häufigkeit | Wenn etwas kaputt geht | Kontinuierlich (automatisiert täglich plus manuell alle zwei Wochen) |
| Abdeckung | Was auch immer Sie ausprobieren möchten | Systematisch über alle wichtigen Seiten und Endpunkte hinweg |
| Regressionserkennung | Langsam, oft übersehen | Sofort, automatisiert |
| Optimierungsleitfaden | Vage (etwas stimmt nicht) | Spezifisch (dieses Feld auf dieser Seite ist zu 73 % korrekt) |

## Häufiger Fehler

Es wird nur die Genauigkeit bewertet und Kosten und Latenz werden ignoriert. Ein Agent, der perfekt extrahiert, aber 15 Sekunden pro Seite benötigt, wird durch einen ersetzt, der in 2 Sekunden ausreichend extrahiert. Optimieren Sie, um das vollständige Bild zu erhalten.

---

## Häufig gestellte Fragen

**Wie oft sollte ich Agenteninteraktionen mit meiner Website auswerten?**Tägliche automatisierte Auswertung. Manuelle Auswertung alle zwei Wochen. Regressionstests nach jeder wesentlichen Inhalts- oder Endpunktänderung.

**Mit welchem Bewertungstool sollte ich beginnen?**
Beginnen Sie bei den meisten AEO-Implementierungen zusätzlich zu den grundlegenden automatisierten Pull-Tests mit manuellen Tests (Durchführen von Abfragen durch KI-Assistenten). Fügen Sie LangChain Evals oder Ragas hinzu, wenn Sie eine detailliertere Analyse benötigen.

**Was ist ein gutes Präzisionsziel?**
95 Prozent oder mehr für kritische Datenfelder (Preise, Verfügbarkeit, Spezifikationen). 90 Prozent für Nebenfelder (Beschreibungen, Empfehlungen). Unter 85 Prozent weisen auf strukturelle Probleme hin.

**Wie bewerte ich Agenteninteraktionen, die ich nicht beobachten kann?**
Überwachen Sie Serverprotokolle, um Agentenverkehrsmuster zu erkennen. Verfolgen Sie die Endpunktnutzung durch Nicht-Browser-Benutzeragenten. Nutzen Sie die Feedback-Schleifen-Architektur, um von Agenten gemeldete Probleme zu erfassen.**Gilt die Auswertung nur für Seiten mit hohem Agentenverkehr?**
Nein. Selbst Websites mit minimalem Agentenverkehr profitieren von der Bewertung, da sie strukturelle und inhaltliche Probleme aufdeckt, die sich auch auf menschliche Benutzer und KI-Zitate auswirken.

## Primäre Referenzen

* [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
* [Schema.org-Dokumentation](https://schema.org/docs/documents.html)