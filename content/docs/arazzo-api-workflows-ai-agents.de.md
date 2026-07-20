---
title: "Arazzo-API-Workflows für KI-Agenten."
metaTitle: "Arazzo API-Workflows für KI-Agenten: Leitfaden."
date: 2026-05-17
weight: 115
category: "Architecture"
description: "Arazzo definiert maschinenlesbare API-Workflows auf Basis von OpenAPI. Finden Sie heraus, warum es für KI-, MCP- und SEO-Agenten auf der Ebene wichtig ist."
summary: "Ein praktischer Leitfaden von Arazzo für KI-Agenten, der Workflow-Beschreibungen, OpenAPI-Sequenzierung, Erfolgskriterien und AEO-Bereitstellungsmuster erläutert."
keywords:
  - "Arazzo-Spezifikation"
  - "API-Workflows für KI-Agenten"
  - "OpenAPI Arazzo"
  - "Agentenbereite APIs"
  - "SEO-Ausführungsebene"
---
# Arazzo API-Workflows für KI-Agenten

Arazzo ist für AEO wichtig, da OpenAPI einzelne API-Operationen beschreibt, Agenten jedoch häufig Workflows benötigen. Für eine Buchungs-, Angebots-, Zahlungs- oder Onboarding-Aufgabe sind möglicherweise mehrere API-Aufrufe in der richtigen Reihenfolge erforderlich. Arazzo bietet Teams eine maschinenlesbare Möglichkeit, diese Sequenzen zu beschreiben.

## Was ist Arazzo

Die OpenAPI-Initiative beschreibt Arazzo als eine Spezifikation zum Ausdrücken von Sequenzen von API-Aufrufen und deren Abhängigkeiten, um ein Ergebnis zu erzielen. Es ergänzt OpenAPI, anstatt es zu ersetzen.

Primärquellen:

- [OpenAPI-Initiative: Arazzo-Spezifikation](https://www.openapis.org/arazzo-specification)
- [Arazzo-Spezifikation](https://spec.openapis.org/arazzo/latest.html)
- [OpenAPI-Spezifikation](https://spec.openapis.org/oas/v3.1.0.html)

##Warum OpenAPI allein nicht ausreicht

OpenAPI eignet sich hervorragend zur Beschreibung von Endpunkten. Es teilt einem Entwickler oder einer Maschine mit, welche Vorgänge vorhanden sind, welche Parameter sie akzeptieren und welche Antworten sie zurückgeben.

Aber viele echte Aufgaben brauchen Ordnung:

1. Suchen Sie nach verfügbaren Diensten.
2. Wählen Sie einen Dienst aus.
3. Überprüfen Sie die verfügbaren Plätze.
4. Erstellen Sie eine Reservierung.
5. Bestätigen Sie die Reservierung.

Wenn ein Agent nur einzelne Endpunkte sieht, muss er auf die Reihenfolge schließen. Dies funktioniert möglicherweise für einfache APIs, wird jedoch brüchig, wenn Abhängigkeiten, Token, Zustände oder Validierungsregeln beteiligt sind.

## OpenAPI vs. Arazzo vs. MCP

| Schicht | Hauptberuf | Agentenvorteil |
|
---|
---|
---|
| API öffnen | Beschreibt API-Operationen | Verfügbare Endpunkte verstehen |
| Arazzo | Beschreibt betriebsübergreifende Arbeitsabläufe | Verstehen, wie eine Aufgabe erledigt wird |
| PCM | Macht aufrufbare Tools und Ressourcen verfügbar | Aktionen über eine Agentenschnittstelle aufrufen |

Der [MCP vs. API-Leitfaden](/es/docs/mcp-vs-api-for-agents/) erklärt die Tooling-Ebene. Arazzo hilft bei der Dokumentation der Workflow-Logik hinter diesen Tools.

## Wo Arazzo in AEO passt

AEO ist am stärksten, wenn Agenten diese Sequenz durchlaufen können:

1. Entdecken Sie den Service.
2. Verstehen Sie die Fähigkeiten.
3. Lesen Sie die Einschränkungen.
4. Führen Sie den Workflow aus.
5. Überprüfen Sie das Ergebnis.

Arazzo unterstützt die Schritte 2 bis 5, indem es mehrstufige Arbeitsabläufe explizit macht. Dies ist besonders nützlich für die [Ausführungsschicht](/es/docs/execution-layer/), wo ein Agent mehr tun muss, als nur Inhalte abzurufen.

## Starke Anwendungsfälle

| Anwendungsfall | Warum Arazzo hilft |
|
---|
---|
| E-Commerce-Zahlung | Warenkorb, Versand, Steuern, Zahlung und Bestätigung erfolgen nacheinander |
| B2B-Angebotsanfrage | Berechtigung, Konfiguration, Preise und Versand hängen voneinander ab |
| Reisebuchung | Verfügbarkeit, Tarifbestimmungen, Passagierdaten und Bestätigung werden bestellt |
| SaaS-Onboarding | Arbeitsbereichs-, Benutzer-, Abrechnungs- und Berechtigungseinstellungen weisen Abhängigkeiten auf || Unterstützen Sie das Klettern | Bedarfsstatus für Ticketerstellung, -klassifizierung, -anhang und -weiterleitung |
| Finanz-Workflow | Offenlegung, Berechtigung und Zustimmung müssen erfolgen, bevor Maßnahmen ergriffen werden |

Die [Agent-Ready Web Application Checklist] (/es/docs/agent-ready-web-apps/) behandelt die Gestaltung der zugrunde liegenden Oberfläche des Produkts.

## Was in einen Arazzo-Workflow einbezogen werden sollte

Dokumentieren Sie mindestens Folgendes:

- Workflow-Ziel
- Tickets erforderlich
- geordnete Schritte
- OpenAPI-Quelloperationen
- Abhängigkeiten zwischen Schritten
- Erfolgskriterien
- Abgänge
- Fehlerzustände
- Wiederholungsversuche und Idempotenzerwartungen

Besonders wichtig sind Erfolgskriterien. Agenten müssen wissen, was „erledigt“ bedeutet.## Beispiel für ein Workflow-Formular

Für eine Terminbuchungs-API:

| Schritt | Betrieb | Später verwendete Ausgabe |
|
---|
---|
---|
| 1 | `list_services` | `service_id` |
| 2 | `list_available_slots` | `slot_id` |
| 3 | `create_booking` | `booking_id` |
| 4 | `get_booking` | bestätigter Status |

Ohne Workflow-Dokumentation ruft ein Agent möglicherweise zuerst den falschen Endpunkt auf oder verpasst den Bestätigungsschritt.

## Bereitstellungspfad

1. Bereinigen Sie Ihr OpenAPI-Dokument.
2. Wählen Sie drei hochwertige Workflows.
3. Schreiben Sie Arazzo-Beschreibungen für diese Arbeitsabläufe.
4. Testen Sie sie mit einem Workflow-Agenten oder -Läufer.
5. Verknüpfen Sie die Workflow-Dokumente aus den API-Dokumenten und „llms.txt“.
6. Packen Sie bei Bedarf die gleichen Arbeitsabläufe wie MCP-Tools.

Dies hält das System auf dem Boden: OpenAPI beschreibt Vorgänge, Arazzo beschreibt die Sequenzierung, MCP stellt aufrufbare Tools bereit.

## Häufig gestellte Fragen

### Ersetzt Arazzo OpenAPI?

Nein. Es ergänzt OpenAPI durch die Beschreibung von Arbeitsabläufen, die OpenAPI-Operationen verwenden.

### Ist Arazzo nur etwas für KI-Agenten?

Nein. Es ist nützlich für Dokumentation, SDK-Generierung, Tests und Compliance. KI-Agenten sind ein starker Anwendungsfall.

### Brauche ich Arazzo vor MCP?

Nicht immer. Für einfache Werkzeuge kann MCP ausreichend sein. Bei mehrstufigen Arbeitsabläufen hilft Arazzo dabei, den Prozess explizit zu machen.

### Was ist der SEO-Aspekt?

Arazzo ist kein Rankingfaktor. Verbessert die Bereitschaft der Ausführungsschicht, indem Arbeitsabläufe maschinenlesbar gemacht werden.

### Welche Arbeitsabläufe sollten zuerst dokumentiert werden?

Beginnen Sie mit Workflows, die an Umsatz, Support-Lösungen, Reservierungen, Onboarding oder Compliance-relevante Aktionen gebunden sind.