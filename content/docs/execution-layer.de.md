---
title: "Die Ausführungsebene: Hier agieren KI-Agenten."
description: "Erfahren Sie, was die Ausführungsebene ist, warum KI-Agenten sie benötigen und wie Websites Aktionen, Echtzeitdaten und Überprüfungen offenlegen."
summary: "Ein Leitfaden zur Ausführungsschicht: die Infrastruktur, die es autonomen KI-Agenten ermöglicht, über APIs, Tools, Daten und Transaktionsendpunkte zu agieren."
keywords:
  - "Ausführungsschicht"
  - "Optimierung der Agent-Engine"
  - "Agentenaktionen"
  - "agentenbereite Infrastruktur"
date: 2026-03-09
weight: 3
category: "Architecture"
---
Wenn ein KI-System seinen Inhalt in einer generierten Antwort zitiert, ist das die Leseebene am Werk. Hilfsbereit, aber passiv.

Wenn ein KI-Agent seine API verwendet, um den Bestand in Echtzeit zu überprüfen, ihn mit den Budgetbeschränkungen eines Benutzers zu vergleichen und einen Kauf abzuschließen, ist das die Ausführungsebene. Aktiv, transaktional und grundlegend anders in den Anforderungen an seine Infrastruktur.

Auf der Ausführungsebene unterscheidet sich AEO von allem, was davor war. Es handelt sich nicht um ein Problem der Inhaltsoptimierung. Es handelt sich um ein **Problem der Infrastrukturarchitektur**.

---

## Welche Agenten müssen handeln?

Ein freiberuflicher Makler, der eine Aufgabe ausführt (Buchung eines Hotelzimmers für weniger als 150 Euro in Barcelona für nächsten Dienstag), benötigt:

### 1. Entdeckung

Finden Sie Dienste, die zur Art der Aufgabe passen. Dies ist teilweise ein Problem der Leseebene. Strukturierte Daten, Schema-Markup und die richtige Indizierung helfen Agenten dabei, Ihren Service zu entdecken. Aber Entdeckung allein ermöglicht kein Handeln.

### 2. Kapazität verstehen

Erfahren Sie, was Ihr Dienst leisten kann und unter welchen Einschränkungen. Der Agent benötigt eine maschinenlesbare Beschreibung seiner Fähigkeiten: welche Aktionen verfügbar sind, welche Parameter er akzeptiert, welche Ergebnisse er zurückgibt, welche Einschränkungen gelten. Dies bieten die Leistungsmanifestate und Beschreibungen der MCP-Tools.

### 3. Zugriff auf Echtzeitdaten

Informieren Sie sich über aktuelle Preise, Verfügbarkeit und Konditionen. Statische HTML-Seiten mit den Preisen von gestern funktionieren nicht. Der Agent benötigt einen Endpunkt, der aktuelle, strukturierte Daten zurückgibt, die er programmgesteuert auswerten kann.

### 4. Constraint-Matching

Bewerten Sie, ob Ihr Angebot den Anforderungen des Nutzers entspricht. Budget weniger als 150 Euro? Dienstag verfügbar? In Barcelona? Ist das Frühstück inbegriffen? Der Agent muss diese Einschränkungen mit seinen Daten vergleichen. Dies erfordert strukturierte, deterministische Daten, keine Marketingtexte.

### 5. Ausführung von Aktionen

Aktivieren Sie die Reservierung, den Kauf oder die Anfrage. Der Agent benötigt einen Transaktionsendpunkt. Hier kommen Protokolle wie UCP (für den Handel) und MCP (für den allgemeinen Tool-Zugriff) ins Spiel.

### 6. Statusprüfung

Bestätigen Sie, dass die Aktion erfolgreich war. Wurde die Reservierung vorgenommen? Der Agent benötigt beobachtbare Zustandsübergänge: verfügbar, reserviert, bestätigt. Ohne Verifizierung kann der Agent keine verlässliche Meldung abgeben.

---

## Bausteine

### Aktionspläne

Schema.org definiert Aktionstypen wie BuyAction, ReserveAction, OrderAction. Diese teilen den Agenten mit, welche Aktionen auf einer Seite oder über einen Dienst möglich sind. Die meisten Websites verwenden Schema.org nur für Informations-Markup. Die Erweiterung auf Markup auf Aktionsebene ist ein erster Schritt, der keine Backend-APIs erfordert.

### Capability ManifestsEin maschinenlesbares Dokument, das beschreibt, was ein Dienst tun kann, welche Protokolle er unterstützt und wie mit ihm interagiert wird. Stellen Sie sich das wie eine robots.txt-Datei für die Fähigkeiten des Agenten vor, mit der Ausnahme, dass nicht angegeben wird, was er verfolgen kann, sondern was er tun kann.

### Deterministische Ein- und Ausgänge

Marketingseiten dienen der menschlichen Überzeugung. Agentenbezogene Daten sollten für die maschinelle Entscheidungsfindung konzipiert sein: feste Parameter, strukturierte Antwortformate, eindeutige Werte, maschinenlesbare Fehlercodes.

Was die Website sagt:

> „Unser Premium-Plan beginnt bei nur 49 US-Dollar pro Monat und bietet alle Funktionen, die Ihr Team benötigt.“

Was der Agent braucht:

```json
{
  "plan": "premium",
  "price": { "amount": 49, "currency": "USD", "interval": "month" },
  "features": ["feature_a", "feature_b", "feature_c"],
  "limits": { "users": 50, "storage_gb": 100 },
  "trial": { "available": true, "days": 14 }
}
```

### Protokollkompatibilität**MCP (Model Context Protocol)**: Ermöglicht KI-Modellen den Zugriff auf externe Tools und Daten über eine standardisierte Schnittstelle. Ein Händler mit einem MCP-Server ermöglicht jedem MCP-fähigen Agenten die Abfrage seines Katalogs ohne eine benutzerdefinierte Integration.

**UCP (Universal Commerce Protocol)** – Standardisiert den gesamten Kaufprozess, sodass jeder Agent mit jedem Händler unter Verwendung desselben Protokolls Transaktionen durchführen kann.

**A2A (Agent zu Agent)**: Ermöglicht Agenten, Aufgaben an spezialisierte Agenten zu delegieren.

Organisationen, die diese Protokolle frühzeitig implementieren, werden zur Standardoption für die Erledigung von Agentenaufgaben.

### Zustandsübergänge

Agenten müssen überprüfen, ob die Aktionen die erwarteten Ergebnisse liefern. Dies erfordert beobachtbare Zustandsübergänge:

„verfügbar > reserviert > Zahlung ausstehend > bestätigt > erfüllt“.

Jeder Übergang muss abfragbar sein. Ohne dies können Agenten mehrstufige Arbeitsabläufe nicht zuverlässig verwalten.

### Vertrauen und Verifizierung

Ein Agent, der eine 2.000-Euro-Reise bucht, muss der Quelle vertrauen. Vertrauenssignale für Agenten unterscheiden sich von Vertrauenssignalen für Menschen. Agenten benötigen überprüfbare Händleridentitäten, kryptografisch signierte (AP2) Transaktionsbelege, konsistente und genaue Daten über alle Kontaktpunkte hinweg, eine transparente Dokumentation von Einschränkungen und Prüfpfade.

---

## Was das für Ihr Unternehmen bedeutet

Die Ausführungsschicht wird nicht über Nacht aufgebaut. Es handelt sich um eine Fähigkeit, die schrittweise entwickelt wird:

**Phase 1 (jetzt):** Überprüfen Sie die aktuelle Bereitschaft Ihres Agenten. Bewerten Sie strukturierte Daten, Schemaabdeckung, Inhaltsstruktur und vorhandenen API-Footprint.

**Phase 2 (3 bis 6 Monate):** Implementieren Sie Optimierungen der Leseebene und beginnen Sie mit der Planung der Infrastruktur der Ausführungsebene. Fügen Sie Aktionsschemata hinzu, erstellen Sie eine Funktionsdokumentation und bewerten Sie die Protokollkompatibilität.

**Phase 3 (6 bis 18 Monate):** Entwickeln Sie Funktionen auf der Ausführungsebene. Stellen Sie APIs bereit, implementieren Sie Protokollunterstützung, erstellen Sie agentenorientierte Datenendpunkte, entwickeln Sie Mechanismen zur Integritätsprüfung.[AEO Readiness Audit](/es/docs/audit/) – Beginnen Sie mit einer systematischen Bewertung.

[Was ist AEO?](/es/docs/what-is-aeo/): Vollständige Definition und Geltungsbereich.

## Häufig gestellte Fragen

### Ersetzt die Laufzeitschicht das Website-Frontend?

Nein. Menschliche Schnittstellen sind immer noch wichtig. Die Ausführungsebene fügt strukturierte Pfade hinzu, die von der Software verwendet werden können, ohne dass man erraten muss, wie eine visuelle Schnittstelle funktioniert.

### Was macht eine Aktion für Agenten sicher?

Die Aktion erfordert explizite Eingaben, Validierung, Autorisierung, stabile Zustände, begrenzte Wiederholungsversuche, eindeutige Fehler und ein überprüfbares Ergebnis.

### Sollten Teams jede interne Aktion offenlegen?

Nein. Stellen Sie nur Aktionen mit einem definierten Benutzernutzen, Berechtigungsmodell, Eigentümer, Prüfprotokoll und Failover-Prozess bereit.

## Verwandte Anleitungen

* [Agent-Handelsarchitektur](/es/docs/agentic-commerce/)

## Primäre Referenzen

* [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
* [Schema.org-Dokumentation](https://schema.org/docs/documents.html)