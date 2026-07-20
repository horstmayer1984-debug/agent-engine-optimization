---
title: "Lighthouse Agent Navigation Audit Guide."
metaTitle: "Lighthouse Agentic Navigation Audit: AEO-Leitfaden."
date: 2026-05-17
weight: 110
category: "Guide"
description: "Chrome Lighthouse umfasst jetzt experimentelle Agent-Navigationsprüfungen. Finden Sie heraus, was llms.txt, WebMCP und Audits bedeuten."
summary: "Ein praktischer Leitfaden für Chrome Lighthouse-Agentennavigation-Audits, einschließlich llms.txt-Prüfungen, WebMCP-Tool-Sichtbarkeit, Bewertung und nächster AEO-Schritte."
keywords:
  - "Leuchtturm-Agent-Navigation"
  - "Prüfen Sie llms.txt"
  - "WebMCP-Audit"
  - "Navigation durch SEO-Agenten"
  - "AEO-Prüfung"
---
#Lighthouse Agent Navigation Audit Guide

Die Agenten-Navigationskategorie von Chrome Lighthouse ist wichtig, da sie Überprüfungen der Agentenbereitschaft in einen herkömmlichen Entwickler-Audit-Workflow integriert. Die aktuellen Tests sind experimentell, zeigen aber, wohin die Reise geht: KI-Agenten benötigen maschinenlesbare Zusammenfassungen, auffindbare Tools und deterministische Interaktionsoberflächen.

## Was hat sich geändert?

Chrome für Entwickler dokumentiert jetzt Lighthouse-Audits für die Agentennavigation. Zu den dokumentierten Prüfungen gehören ein „llms.txt“-Audit und ein Informationsaudit für registrierte WebMCP-Tools. Laut Chrome ist die Kategorie experimentell und basiert auf vorgeschlagenen Standards. Daher sollte sie als frühe Diagnoseebene und nicht als Endbewertung behandelt werden.

Primärquellen:

- [Chrome: Lighthouse-Audit llms.txt](https://developer.chrome.com/docs/lighthouse/agentic-browsing/llms-txt)
- [Chrome: Lighthouse Agent Navigation Score](https://developer.chrome.com/docs/lighthouse/agentic-browsing/scoring)
- [Chrome: Registrierte WebMCP-Tools-Prüfung](https://developer.chrome.com/docs/lighthouse/agentic-browsing/registered-webmcp-tools)

## Was Audits beweisen

| Prüfung | Was es bedeutet | Praktische AEO-Antwort |
|
---|
---|
---|
| llms.txt | Überprüft, ob das Site-Stammverzeichnis eine maschinenlesbare Zusammenfassung | bereitstellt Veröffentlichen Sie eine prägnante „llms.txt“ mit wichtigen Links |
| Registrierte WebMCP-Tools | Listet die Tools auf, die die Seite Browser-Agenten zur Verfügung stellt | Klare Werkzeugnamen und Aktionsbeschreibungen hinzufügen |
| Agenten-Navigationskategorie | Zeigt Zustimmungs-/Ablehnungssignale und Informationsaufbereitung | Verwendung als technische Checkliste, nicht als Ranking-Score |

Die „llms.txt“-Dokumentation von Chrome macht einen wichtigen Unterschied: Eine fehlende Datei kann als „Nicht anwendbar“ markiert werden, da die Datei optional ist, Serverfehler werden jedoch gekennzeichnet. Das bedeutet, dass eine kaputte „llms.txt“ schlimmer ist als gar keine Datei.

## Warum dies für AEOs wichtig ist

Das [AEO Readiness Audit](/es/docs/audit/) überprüft bereits Erkennung, Leseschicht, Ausführungsschicht und Vertrauen. Lighthouse bietet Entwicklern eine einfache Möglichkeit, einige dieser Signale in einer vertrauten Tool-Umgebung zu erfassen.

Es ist kein Ersatz für eine vollständige AEO-Prüfung. Hilft Entwicklern bei der Validierung bestimmter technischer Teile:

- Stellt der Site-Root „llms.txt“ sauber bereit?
- Sind Seitenaktionen als WebMCP-Tools sichtbar?
- Sind während des Browsertests Signale zur Bereitschaft experimenteller Agenten sichtbar?

## So bereiten Sie llms.txt vor

Für die Agentennavigation sollte „llms.txt“ kurz und nützlich sein. Es handelt sich nicht um einen Klon der Sitemap.

Eine praktische Akte muss Folgendes enthalten:

- Zweck der Website
- Grundkonzepte
- beste Homepages
- Schlüsseltools oder -dienste
- maschinenlesbare Ressourcen
- Aktualisierungsdatum

Der [llms.txt-Leitfaden](/es/docs/programming-llms-txt/) erklärt, wie man ihn strukturiert. Die Hauptregel ist einfach: Helfen Sie dem Agenten zu verstehen, was er zuerst lesen soll.

## So bereiten Sie WebMCP-Tools vorDie Prüfung der registrierten WebMCP-Tools ist informativ. Wenn keine registrierten Werkzeuge vorhanden sind, ist die Liste leer. Dies ist nicht automatisch ein Fehler, sondern zeigt, ob die Seite Aktionen auf eine Art und Weise bereitstellt, die für den Browser-Agenten benutzerfreundlich ist.

Zu den guten ersten Tools gehören:

- Audit anfordern
- Vereinbaren Sie einen Termin
- Angebot anfordern
- In den Warenkorb legen
- Verfügbarkeit prüfen
- Support-Ticket einreichen
- Produkte vergleichen

Der [WebMCP-Leitfaden](/es/docs/webmcp-agent-ready-websites/) beschreibt, wann Tools auf Seitenebene im Vergleich zu serverseitigem MCP verwendet werden sollten.

## Vorgeschlagener Workflow| Schritt | Aktion | Ausgabe |
|
---|
---|
---|
| 1 | Führen Sie Lighthouse auf der Startseite und in wichtigen Vorlagen aus | Empfehlungsagenten für Navigationszeichen |
| 2 | „llms.txt“-Antwortfehler beheben | Stabile maschinenlesbare Root-Zusammenfassung |
| 3 | WebMCP zu einer Aktionsseite mit geringem Risiko hinzufügen | Registriertes Werkzeug sichtbar |
| 4 | Wiederholen Sie Leuchtturm | Erkennung bestätigen |
| 5 | Serverseitige Protokolle für Agentenaktionen hinzufügen | Messschicht |

Dieser Workflow verbindet die technische Validierung mit der [Ausführungsschicht](/es/docs/execution-layer/). Das Bestehen eines Audits ist weniger wichtig als der Nachweis, dass ein Agent eine nützliche Aufgabe erledigen kann.

## Was man nicht tun sollte

Fügen Sie keine gefälschte „llms.txt“-Datei hinzu, nur um eine Prüfung zu bestehen. Registrieren Sie keine generischen WebMCP-Tools wie „submit_form“ ohne eine aussagekräftige Beschreibung. Legen Sie keine risikoreichen Aktionen offen, da die Prüfung vorhanden ist.

Die beste Implementierung der Agentennavigation ist langweilig: klare Inhalte, stabile Aktionen, explizite Berechtigungen und gute Protokollierung.

## Häufig gestellte Fragen

### Ist der Lighthouse Agent Navigation Score ein Rankingfaktor?

Das sagt keine offizielle Quelle. Betrachten Sie es als Zeichen experimenteller Bereitschaft und nicht als Google-Ranking-Faktor.

### Ist llms.txt erforderlich?

In der Chrome-Dokumentation heißt es, dass dies derzeit optional ist. Eine fehlende Datei ist möglicherweise nicht anwendbar, während Serverfehler möglicherweise gemeldet werden.

### Sollte ich jedem Formular WebMCP hinzufügen?

Nein. Beginnen Sie mit hochwertigen Aktionen mit geringem Risiko, bei denen die Ausführung von Agenten den Benutzern helfen würde.

### Wie unterscheidet sich das von einem normalen SEO-Audit?

Traditionelle SEO-Audits konzentrieren sich auf Crawlbarkeit, Geschwindigkeit, Metadaten und Inhalte. Bei der Überprüfung der Agentennavigation geht es darum, ob Agenten die Website verstehen und darauf reagieren können.

### Was soll nach der Umsetzung gemessen werden?

Verfolgen Sie von Agenten ausgelöste Aktionen, Formularvervollständigungen, Fehler, ungültige Anfragen und Seiten, die Agenten lesen, bevor sie handeln.