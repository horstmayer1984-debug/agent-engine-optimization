---
title: "Google ADK 2.0 und deterministische Agent-Workflows."
metaTitle: "Deterministische Agent-Workflows von Google ADK 2.0."
date: 2026-07-02
weight: 194
category: "Architecture"
description: "Google ADK 2.0 legt Wert auf deterministische Arbeitsabläufe für vertrauenswürdige Agenten. Erfahren Sie, was es für AEO, Ausführungswege und Genehmigungen bedeutet."
summary: "Ein AEO-Leitfaden zu Google ADK 2.0, deterministischen Arbeitsabläufen, diagrammbasierter Orchestrierung, Human-in-the-Loop-Kontrollen und Aktionen vertrauenswürdiger Agenten."
keywords:
  - "GoogleADK 2.0"
  - "deterministische Agenten-Workflows"
  - "Agenten-Entwicklungskit"
  - "Agenten-Orchestrierung"
  - "AEO-Ausführungsschicht"
---
# Google ADK 2.0 und deterministische Agenten-Workflows

Google ADK 2.0 ist für AEO wichtig, da es das Agentendesign in Richtung deterministischer Arbeitsabläufe vorantreibt, bei denen der Pfad bekannt, beobachtbar und wiederherstellbar ist. Das ist genau das, was Websites brauchen, wenn Agenten vom Lesen von Seiten zum Abschließen von Reservierungen, Käufen, Supportanfragen und Geschäftsprozessen übergehen.

## Was Google angekündigt hat

Google hat am 1. Juli 2026 [Why we build ADK 2.0](https://developers.googleblog.com/why-we-built-adk-20/) veröffentlicht. Das zentrale Argument ist einfach: Große Sprachmodelle sind für die Argumentation nützlich, aber Produktionsagenten benötigen auch eine deterministische Ausführung, wenn der Workflow klar ist.

Google kündigte außerdem [ADK Go 2.0](https://developers.googleblog.com/announcing-adk-go-20/) mit einer diagrammbasierten Workflow-Engine, integrierter menschlicher Unterstützung, dynamischer Orchestrierung, Wiederholungsversuchen, Status und Fortsetzungsverhalten an.

## Warum deterministische Arbeitsabläufe wichtig sind

Viele Webaufgaben sollten nicht improvisiert werden. Eine Rückerstattung, eine Zahlung, eine Angebotsanfrage, ein Versicherungsanspruch oder eine Support-Eskalation erfordert einen vorhersehbaren Weg.

| Agentenverhalten | Gut für | Risiko |
|
---|
---|
---|
| Freiformargumentation | Recherche, Vergleich, Zusammenfassung | Unklarer Ausführungspfad |
| Werkzeugaufruf | Daten abrufen oder einen Schritt ausführen | Missbrauch von Werkzeugen ohne Einschränkungen |
| Deterministischer Workflow | Bekannte mehrstufige Prozesse | Erfordert anfängliche Modellierung |
| Menschlicher Arbeitsablauf im Kreislauf | Riskante oder irreversible Handlungen | Langsamer, aber sicherer |

Die [Ausführungsschicht](/es/docs/execution-layer/) sollte deterministische Pfade für wichtige Geschäftsaktionen bevorzugen.

## AEO-Auswirkungen für Websites

ADK 2.0 bekräftigt eine Faustregel: Lassen Sie Agenten Ihren Arbeitsablauf nicht anhand von Schaltflächen und Marketingtexten erraten. Veröffentlichen Sie den Workflow.

Das bedeutet Folgendes zu definieren:

- Zulässige Aufgabenzustände
- Tickets erforderlich
- Validierungsregeln
- Genehmigungstore
- Wiederholungslogik
- Stornierungsrouten
- Letzte Bestätigungsnachrichten
- Audit-Protokolle

Dies verbindet sich mit [Agent UX und Human-in-the-Loop Design] (/es/docs/agent-ux-human-in-the-loop/), [Multi-Agent AEO] (/es/docs/multi-agent-aeo/) und [Agent-Ready Web Apps] (/es/docs/agent-ready-web-apps/).

## Beispiel: Terminbuchung

| Schritt | Deterministische Anforderung |
|
---|
---|
| Wählen Sie Dienst | aus Verwenden Sie eine stabile Service-ID, nicht nur den Seitentext |
| Verfügbarkeit prüfen | Aktuelle Zeitfenster zurückgeben |
| Benutzerdaten sammeln | Erforderliche Felder validieren |
| Richtlinie anzeigen | Preis- und Widerrufsregeln für Rücksendungen |
| Reservierung bestätigen | Erfordern explizite Benutzergenehmigung |
| Ergebnis zurückgeben | Geben Sie die Reservierungs-ID und die nächsten Schritte an |

Ein Agent kann darüber nachdenken, welcher Dienst für den Benutzer geeignet ist. Der Reservierungsbestätigungsweg sollte nicht erfunden werden.

## So prüfen Sie Ihre Website

1. Wählen Sie einen hochwertigen Workflow.
2. Schreiben Sie die genaue Zustandsmaschine für diesen Workflow.3. Identifizieren Sie, wo Ihre Website derzeit auf visuelle Vorschläge angewiesen ist.
4. Fügen Sie bei Bedarf maschinenlesbare Tags, Schemata, APIs oder MCP-Tools hinzu.
5. Fügen Sie Genehmigungstore vor unumkehrbaren Aktionen hinzu.
6. Zeichnen Sie jeden für den Agenten relevanten Zustandsübergang auf.
7. Probieren Sie die Wege des Scheiterns aus, nicht nur die Wege des Erfolgs.

## Häufig gestellte Fragen

### Ist deterministisches Workflow-Design nur etwas für Entwickler?

Nein. Produkt-, SEO-, Rechts-, Support- und Betriebsteams sollten dabei helfen, zu definieren, welche Aktionen eine Genehmigung erfordern und welche Status gültig sind.### Ersetzt ADK 2.0 LangGraph oder andere Frameworks?

Nein. Es handelt sich um einen anderen Weg der Agentenentwicklung. Die nützliche Lehre aus AEO ist das Designprinzip: deterministische Ausführung für bekannte Arbeitsabläufe.

### Warum wirkt sich das auf SEO aus?

Klassisches SEO bringt Benutzer auf Seiten. Der SEO-Agent benötigt diese Seiten und Workflows auch, um von automatisierten Assistenten genutzt werden zu können.

### Was ist der erste zu modellierende Workflow?

Beginnen Sie mit der Aktion mit dem höchsten Wert, die ein Agent sinnvollerweise ausführen könnte: Buchung, Angebotsanfrage, Produktvergleich, Zahlung, Support-Ticket oder Demo-Anfrage.

## Quellen

Hauptquellen: [Google Developer Blog: Warum wir ADK 2.0 erstellt haben](https://developers.googleblog.com/why-we-built-adk-20/) und [Google Developer Blog: ADK Go 2.0](https://developers.googleblog.com/announcing-adk-go-20/).