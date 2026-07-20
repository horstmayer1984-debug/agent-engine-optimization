---
title: "Den Kundenservice durch Workflows verändern."
date: 2026-03-22
weight: 24
category: "Industry"
description: "So strukturieren Sie Wissensdatenbanken, Lösungsendpunkte, Eskalationspfade und kanalübergreifenden Support, damit KI-Agenten dies tun können."
summary: "Der Kundensupport wird unsichtbar, wenn KI-Agenten auf strukturierte Wissensdatenbanken zugreifen, Lösungsmaßnahmen auslösen und mit vollem Kontext eskalieren können. Hier erfahren Sie, wie Sie dieses System aufbauen."
keywords:
  - "Kundendienstmitarbeiter"
  - "KI-Support-Workflows"
  - "autonome Auflösung"
  - "Unterstützung der Wissensdatenbankoptimierung"
  - "Kletter-API"
  - "Mehrkanal-KI-Unterstützung"
---
# Den Kundenservice mit Agenten-Workflows verändern

Die meisten Interaktionen mit dem Kundendienst wiederholen sich: Passwort-Zurücksetzungen, Prüfungen des Lieferstatus, Rückerstattungsanfragen, Funktionserklärungen. Ein menschlicher Agent erledigt sie in 5 bis 15 Minuten. Ein KI-Agent könnte sie in Sekundenschnelle lösen, wenn die unterstützende Infrastruktur auf die Interaktion mit Maschinen ausgelegt ist.

Bei Veränderung geht es nicht darum, die menschliche Unterstützung zu ersetzen. Dabei geht es darum, dem eigenen KI-Assistenten des Kunden zu ermöglichen, sich direkt mit seinen Supportsystemen zu verbinden, die Antwort zu finden und die Lösung auszuführen, ohne dass eine der Parteien ein menschliches Eingreifen erfordert.

Dies funktioniert nur, wenn Wissensdatenbanken maschinenlesbar sind, Lösungspfade als Endpunkte bereitgestellt werden, die Eskalation mit vollständigem Kontext automatisiert ist und das System über alle Kanäle hinweg funktioniert.

## Wissensdatenbanken benötigen eine semantische Struktur, keine Schlüsselwortsuche

Herkömmliche Hilfezentren suchen nach passenden Wörtern. Ein Kunde gibt „Anmeldung nicht möglich“ ein und das System gibt Artikel zurück, die diese Wörter enthalten. Dies bricht ab, wenn ein KI-Agent dasselbe Problem anders beschreibt: „Authentifizierungsfehler nach Passwortänderung auf dem mobilen Client.“

Die Lösung ist eine semantische Suche, die durch strukturierte Inhalte unterstützt wird. Jeder Hilfeartikel muss:

- Formulieren Sie das Problem oben in einem klaren Satz
- Listen Sie die genauen Bedingungen auf, unter denen diese Lösung gilt (Produktversion, Plattform, Kontotyp).
- Geben Sie die Lösung in nummerierten Schritten mit expliziten Eingaben und erwarteten Ergebnissen an
- Definieren Sie, wann diese Lösung nicht anwendbar ist (Randfälle, Voraussetzungen)
- Link zu verwandten Artikeln für angrenzende Probleme

Vermeiden Sie internen Jargon. Wenn Ihr Team das Konfigurationspanel intern „Mission Control“ nennt, sollte im Hilfeartikel „Configuration Panel (intern Mission Control genannt)“ stehen, damit sich Menschen und Agenten auf die Terminologie einigen können.

## Lösungsendpunkte: Agenten erlauben, das Problem zu lösen

Das Erklären einer Lösung ist die Leseebene. Die Fixausführung ist die [Ausführungsschicht](/es/docs/execution-layer/).

Stellen Sie für jede allgemeine Supportaktion einen dokumentierten Endpunkt bereit:

- Passwort zurücksetzen: Benutzer-ID akzeptieren, Bestätigung mit temporärem Zugangslink zurücksenden
- Rückerstattungsanfrage: Bestell-ID akzeptieren, Berechtigung validieren, Rückerstattung veranlassen, Rückgabestatus
- Abonnementänderung: Plan-ID, Wirksamkeitsdatum, Rücksendebestätigung und anteiliger Betrag akzeptieren
- Lieferstatus: Bestell-ID akzeptieren, aktuellen Status mit voraussichtlicher Lieferung zurücksenden
- Ticketerstellung: Akzeptiert Problembeschreibung, Kategorie, Priorität, Rückgabeticket. IDE. Jeder Endpunkt sollte Eingabevalidierung, eindeutige Fehlerantworten und Ratenbegrenzung umfassen. Ein Agent, der eine Rückerstattung direkt aktivieren kann, erspart sowohl dem Kunden als auch seinem Support-Team einen 10-minütigen Anruf.

## Automatisierte Skalierung mit vollständigem Kontext

Wenn ein Agent ein Problem nicht lösen kann, muss es eskaliert werden. Die entscheidende Anforderung: Die Eskalation muss den vollständigen Kontext dessen enthalten, was versucht wurde und warum es fehlgeschlagen ist.

Zu einer guten Kletternutzlast gehören:

- Kundenkennung
- Beschreibung des Problems (wie vom Agent verstanden)
- Abwicklungsmaßnahmen versucht
- Bei jedem Schritt empfangene Fehlercodes
- relevante Kontodaten (Bestellhistorie, Abonnementstatus)
- nächste vorgeschlagene Aktion für den menschlichen AgentenDadurch entfällt der schlimmste Teil der Eskalation des Supports: Der Kunde wiederholt sein Problem von Grund auf. Der menschliche Agent erhält ein komplettes Diagnosepaket und kann das Problem sofort beheben.

Erstellen Sie es als automatisierten Ticketing-Endpunkt, den der KI-Agent aufruft, wenn seine Lösungsroute fehlschlägt. Der [Multi-Agent AEO-Artikel] (/docs/multi-agent-aeo/) erklärt, wie diese Übergaben in orchestrierten KI-Workflows funktionieren.

## Kontinuität zwischen den Kanälen

Der KI-Agent eines Kunden initiiert möglicherweise eine Support-Interaktion auf Ihrer Website, muss die Identität über Ihre mobile App überprüfen und erhält eine E-Mail-Bestätigung. Das Supportsystem muss den Agenten auf allen Kanälen erkennen und den Interaktionskontext aufrechterhalten.

Dies erfordert:

– eine dauerhafte Sitzungs- oder Interaktions-ID, die über alle Kanäle hinweg funktioniert
- Authentifizierung per Web, Mobilgerät und E-Mail
- Statuspersistenz (der Agent sollte den Workflow beim Kanalwechsel nicht neu starten)
- Konsistentes API-Verhalten unabhängig vom Einstiegspunkt

Wenn Ihr Web-Support und Ihr mobiler Support separate Systeme mit separaten Datenbanken sind, werden Agenten-Workflows an der Kanalgrenze unterbrochen.

## Messung der Unterstützung in einem Agenturmodell

Herkömmliche Support-Metriken (durchschnittliche Bearbeitungszeit, erste Reaktionszeit, CSAT-Scores) wurden für menschliche Interaktionen entwickelt. Agentenunterstützung erfordert unterschiedliche Maßnahmen:

- Autonome Lösungsrate: Wie viel Prozent der Probleme haben Agenten ohne menschliche Beteiligung gelöst?
- Auflösungsgenauigkeit: Waren die autonomen Auflösungen korrekt?
- Qualität der Eskalation: Haben Agenten bei der Eskalation genügend Kontext bereitgestellt?
- durchschnittliche Zeit bis zur Lösung: von der Agentenanfrage bis zur bestätigten Lösung
- Fehlerpunktanalyse: Wo werden Agenten-Workflows am häufigsten unterbrochen?

Diese Kennzahlen zeigen Ihnen, wo Sie Ihre maschinenorientierte Support-Infrastruktur verbessern können. Das [AEO Readiness Audit](/es/docs/audit/) umfasst die Bewertung des Supportsystems.

---

## Häufig gestellte Fragen**Was ist autonome Lösung im Kundenservice?**
Autonome Lösung bedeutet, dass der KI-Agent eines Kunden eine Verbindung zu seinen Supportsystemen herstellt, das Problem identifiziert und die Lösung ohne menschliches Eingreifen einer der Parteien ausführt.

**Wie sollten Wissensdatenbanken für KI-Agenten strukturiert sein?**
Jeder Artikel benötigt eine klare Problemstellung, anwendbare Bedingungen, nummerierte Lösungsschritte mit expliziten Ein- und Ausgaben sowie definierte Randfälle. Die semantische Suche sollte das Keyword-Matching ersetzen.

**Was sind Auflösungsendpunkte?**
API-Endpunkte, die es KI-Agenten ermöglichen, Support-Aktionen direkt auszuführen: Passwort-Resets, Rückerstattungsanfragen, Abonnementänderungen, Lieferstatusprüfungen und Ticketerstellung.

**Wie funktioniert die Eskalation mit KI-Agenten?**
Wenn ein Agent ein Problem nicht lösen kann, ruft er einen Eskalationsendpunkt auf, der ein Ticket mit dem vollständigen Diagnosekontext erstellt: Problembeschreibung, versuchte Schritte, empfangene Fehler und vorgeschlagene nächste Aktion.

**Welche Kennzahlen sind für den Agenten-Kundenservice wichtig?**
Autonome Lösungsrate, Lösungsgenauigkeit, Eskalationskontextqualität, mittlere Lösungszeit und Fehlerpunktanalyse ersetzen herkömmliche Metriken wie die durchschnittliche Bearbeitungszeit.

## Primäre Referenzen* [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
* [Schema.org-Dokumentation](https://schema.org/docs/documents.html)