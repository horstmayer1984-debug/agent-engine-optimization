---
title: "MCP-Autorisierung: OAuth für KI-Agenten."
metaTitle: "MCP-Autorisierung für KI-Agenten: OAuth-Leitfaden."
date: 2026-05-17
weight: 114
category: "Architecture"
description: "Die MCP-Autorisierung definiert, wie KI-Agenten über HTTP auf eingeschränkte Tools zugreifen. Erfahren Sie mehr über OAuth, geschützte Ressourcenmetadaten."
summary: "Ein praktischer Leitfaden zur MCP-Autorisierung für KI-Agenten, der OAuth-Flows, Metadaten geschützter Ressourcen, Client-Registrierung, Bereiche und OAO-Vorbereitung abdeckt."
keywords:
  - "MCP-Autorisierung"
  - "MCP-OAuth"
  - "Autorisierung von KI-Agenten"
  - "Geschützte Ressourcenmetadaten"
  - "Agentenzugriffskontrolle"
---
#MCP-Autorisierung: OAuth für KI-Agenten

Die MCP-Autorisierung ist wichtig, da Agent-Tools häufig eingeschränkten Zugriff benötigen. Öffentliche Tools sind frei auffindbar, tatsächliche Arbeitsabläufe benötigen jedoch Identität, Einwilligung, Bereiche und Prüfpfade. In der MCP-Autorisierungsspezifikation wird erläutert, wie HTTP-basierte MCP-Transporte die Autorisierung im OAuth-Stil für eingeschränkte MCP-Server verwenden können.

## Was die MCP-Spezifikation sagt

Die Model Context Protocol-Autorisierungsspezifikation definiert Autorisierungsfunktionen auf Transportebene für HTTP-basierte Transporte. Die aktuelle Spezifikation verweist auf OAuth, Metadaten geschützter Ressourcen, dynamische Client-Registrierung und Sicherheitsanforderungen.

Primärquellen:

- [MCP-Autorisierungsspezifikation](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [MCP-Roadmap 2026](https://modelcontextprotocol.io/development/roadmap)
- [MCP vs. API-Leitfaden auf dieser Website](/es/docs/mcp-vs-api-for-agents/)

## Warum die Autorisierung ein AEO-Problem ist

Die [Ausführungsebene](/es/docs/execution-layer/) ist nicht sinnvoll, wenn jede Aktion öffentlich ist oder jede Aktion erfordert, dass ein Mensch die Anmeldeinformationen manuell kopiert. Agenten benötigen kontrollierten Zugriff.

Beispiele:

- Ein Beschaffungsagent überprüft den Vertragspreis
- Ein Supportmitarbeiter liest den Ticketstatus
- Ein Reisebüro ändert eine Reservierung
- Ein Finanzagent holt Rechnungen ein
– Ein Entwickleragent öffnet ein Bereitstellungstool

Jeder Workflow braucht eine klare Antwort: Für wen ist der Agent tätig, was kann er tun, wie lange dauert der Zugriff und wie kann der Zugriff widerrufen werden?

## Öffentliches MCP vs. eingeschränktes MCP

| MCP-Servertyp | Beispiel | Genehmigung erforderlich |
|
---|
---|
---|
| Schreibgeschützt öffentlich | Produktkatalog, Dokumentensuche, öffentliche Preise | Im Allgemeinen keine |
| Öffentliche Aktion | Newsletter-Abonnement, öffentliche Eintragsanfrage | Reibungsarme Anti-Missbrauchskontrollen |
| Benutzerbereich lesen | Kontodaten, Bestellstatus | OAuth und Benutzereinwilligung |
| Benutzerbereich schreiben | Reservierung, Zahlung, Stornierung | Robuste Bereiche, Bestätigung, Prüfprotokolle |
| Verwaltungstool | Implementierung, Abrechnungskonfiguration | Menschliche Zustimmung und strenge Richtlinien |

Die meisten Unternehmen sollten mit schreibgeschützten oder risikoarmen öffentlichen Aktionen beginnen, bevor sie nur für Benutzer verfügbare Tools bereitstellen.

## Wichtige Autorisierungskonzepte

| Konzept | Bedeutung von Agenten |
|
---|
---|
| Ressourcenbesitzer | Der Benutzer oder die Organisation, für die der Agent agiert |
| MCP-Client | Der Agent-Client, der Zugriff anfordert |
| Autorisierungsserver | Das System, das Token gewährt |
| Geschützte Ressourcenmetadaten | Maschinenlesbare Informationen über Autorisierungsserver |
| Geltungsbereich | Spezifische Berechtigungen wie das Lesen von Bestellungen oder das Erstellen von Reservierungen |
| Zugriffstoken | Für MCP-Anfrage verwendete Anmeldeinformationen | Diese Konzepte sind nicht neu, aber Agenten machen sie wichtiger, da der Akteur in einem Browser nicht mehr immer ein Mensch ist.

## Checkliste für die Bereitstellung

1. MCP-Tools nach Risiko klassifizieren.
2. Halten Sie öffentliche Erkennungstools von eingeschränkten Tools getrennt.
3. Definieren Sie den Umfang nach Aktion, nicht nach einem breiten Produktbereich.
4. Veröffentlichen Sie Autorisierungsmetadaten dort, wo Kunden sie finden können.
5. Verwenden Sie Token mit kurzer Laufzeit für Aktien mit höherem Risiko.
6. Notieren Sie die Agentenidentität, die Benutzeridentität, den Toolnamen, die Eingabezusammenfassung und den Ergebnisstatus.
7. Fügen Sie eine menschliche Bestätigung für irreversible oder kostspielige Maßnahmen hinzu.Der [Agent Guardrails and Observability Guide](/es/docs/agent-observability-guardrails/) erweitert dies auf die Betriebsüberwachung.

## Scope-Design-Beispiel

| Schlechte Reichweite | Bessere Zielfernrohre |
|
---|
---|
| `account_access` | `orders.read`, `orders.cancel`, `invoices.read` |
| `Buchung` | `availability.read`, `booking.create`, `booking.cancel` |
| `admin` | `users.invite`, `billing.read`, `settings.update` |

Agenten funktionieren am besten, wenn Bereiche explizit sind. Sicherheitsteams arbeiten am besten, wenn die Bereiche den Geschäftsaktivitäten entsprechen.

## AEO-Dokumentationsanforderungen

Wenn Ihre Site eingeschränkte MCP-Tools anbietet, sollte Ihre öffentliche Dokumentation Folgendes erläutern:

- Welche Tools gibt es?
- welche Tools öffentlich sind
- Genehmigungspflichtig
- Welche Umfänge werden angefordert
- wenn ein menschlicher Bestätigungsschritt erforderlich ist
- wie Anmeldungen und Widerrufe funktionieren

Fügen Sie Links zu diesen Dokumenten aus [llms.txt](/es/docs/programming-llms-txt/) hinzu, damit Agenten das Zugriffsmodell erkennen können, bevor sie versuchen, die Tools aufzurufen.

## Häufige Fehler

| Fehler | Warum es scheitert |
|
---|
---|
| Ein breites Token für alle Tools | Zu viel Entscheidungsfreiheit und schwache Überprüfbarkeit |
| Keine Dokumentation der öffentlichen Leistungsfähigkeit | Agenten können den Zugriff nicht planen |
| Langlebige Token für Schreibaktionen | Größerer Schaden bei Kompromittierung |
| Ohne Widerruf | Benutzer können den delegierten Zugriff nicht stoppen |
| Agentenidentität als Benutzeridentität behandeln | Verwischt die Verantwortung |

## Häufig gestellte Fragen

### Benötigen alle MCP-Server OAuth?

Nein. Für schreibgeschützte öffentliche Server ist möglicherweise keine Autorisierung erforderlich. Dies gilt in der Regel für eingeschränkte oder benutzerspezifische Tools.

### Ist die MCP-Autorisierung für die Produktion bereit?

Die Spezifikation existiert und wird weiterentwickelt. Teams sollten sich an die aktuelle Version halten und die Client-/Server-Kompatibilität überprüfen, bevor sie in der Produktion verwendet werden.

### Was sind geschützte Ressourcenmetadaten?

Mithilfe von Metadaten können MCP-Clients die Autorisierungsserver identifizieren, die einer geschützten Ressource zugeordnet sind.

### Wie wirkt sich das auf AEO aus?

Agenten nutzen eher Dienste, die die verfügbaren Tools, Berechtigungen und Zugriffsabläufe klar beschreiben.

### Sollten Agenten Administratorzugriff haben? Nur in streng kontrollierten internen Umgebungen mit strengen Registrierungen, Genehmigungen und Widerrufen.