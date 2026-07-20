---
title: "Agentenschaltflächen, API und Aktionsschema für AEO."
date: 2026-04-12
weight: 57
category: "Architecture"
description: "Erfahren Sie, wie Agentenschaltflächen, APIs und Aktionsschemata sichere nächste Schritte für KI-Agenten bereitstellen."
summary: "Agentenschaltflächen, Aktionsschemata und API-Endpunkte verwandeln statische Inhaltsseiten in Oberflächen, auf denen KI-Agenten echte Geschäftstransaktionen ausführen können. Hier finden Sie den vollständigen Implementierungsleitfaden."
keywords:
  - "Implementierung der Agent-Schaltfläche"
  - "AEO-Maßnahmenplan"
  - "Mögliches Aktionsschema"
  - "Agent-Transaktions-API"
  - "AEO-Terminalsicherheit"
---
Eine Seite mit Inhalten, die ein Agent lesen kann, ist hilfreich. Eine Inhaltsseite, über die ein Agent agieren kann, ist nützlich. Dokumentierte Agentenschaltflächen, Aktionsschemata und API-Endpunkte machen den Unterschied. Sie verwandeln statische Veröffentlichungsoberflächen in Transaktionsschnittstellen, über die autonome Systeme die Verfügbarkeit prüfen, Angebote anfordern, Termine buchen und Einkäufe abschließen können.

## Was sind eigentlich Agenten-Buttons?

Eine Agentenschaltfläche ist keine visuelle Schaltfläche, die für menschliche Klicks konzipiert ist. Es handelt sich um einen klar dokumentierten Aktionspfad, der einem Agenten mitteilt: Diese spezifische Aufgabe kann hier ausgeführt werden, dies sind die erforderlichen Eingaben und dies ist der anzurufende Endpunkt.

Der visuelle Button auf der Seite dient dem menschlichen Besucher. Das zugrunde liegende Schema und die Endpunktdokumentation dienen dem Agenten. Beide zielen auf denselben Geschäftsprozess ab, jedoch über unterschiedliche Schnittstellen.

## Aktionsschema mit PotentialAction umsetzen

Schema.org stellt den Typ PotentialAction speziell zur Beschreibung der auf einer Seite verfügbaren Aktionen bereit. Nutzen Sie es, um Agenten mitzuteilen, was sie tun können.

Für eine Serviceseite mit Terminbuchung umfasst die Schemastruktur: den Aktionstyp (ReserveAction oder ScheduleAction), die Ziel-URL (Ihr Buchungsendpunkt), die erforderlichen Eingabeeigenschaften (Datum, Uhrzeit, Servicetyp, Kontaktinformationen) und den Ergebnistyp (Buchung mit Bestätigungsnummer).

Für eine einkaufbare Produktseite verwenden Sie BuyAction mit der Ziel-URL, die auf Ihren Warenkorb oder Checkout-Endpunkt verweist, geben Sie Eigenschaften für die Mengen- und Variantenauswahl sowie den Ergebnistyp ein, der die Bestellbestätigung beschreibt.

Verwenden Sie für eine Angebotsanfrage QuoteAction (oder eine generische Aktion mit einem Anzeigenamen), wobei die Ziel-URL auf den Endpunkt Ihres Angebots verweist, und geben Sie Eigenschaften für die Spezifikationen ein, die das Angebot erfordert.

Das Grundprinzip: Jedes Aktionsschema muss einem realen, funktionalen Endpunkt entsprechen. Fügen Sie keine Aktionsschemata für Funktionen hinzu, die noch nicht vorhanden sind. Agenten, die eine Aktion versuchen und scheitern, verlieren auf Ihrer Website Priorität.

## Erstellen der API-Endpunkte

Aktionsendpunkte müssen nicht vom ersten Tag an REST-APIs der Enterprise-Klasse sein. Sie müssen strukturierte Informationen akzeptieren, die Geschäftsaktion ausführen und eine strukturierte Antwort zurückgeben.

Ein minimaler Endpunkt akzeptiert eine JSON-Nutzlast mit den erforderlichen Feldern, validiert die Eingabe, löst den Geschäftsprozess aus (sendet eine E-Mail, erstellt einen Datensatz, ruft eine externe API auf) und gibt eine JSON-Antwort mit dem Status, der Commit-ID und den nächsten Schritten zurück. Für Teams ohne Backend-Entwicklungsressourcen können n8n- oder Make.com-Webhook-Endpunkte dieses Muster gut bewältigen. Erstellen Sie einen Webhook, der JSON akzeptiert, fügen Sie Validierungsschritte hinzu, stellen Sie eine Verbindung zu Ihren Geschäftstools (Kalender, CRM, E-Mail) her und geben Sie eine strukturierte Antwort zurück.

Sicherheitsanforderungen für Endpunkte mit Agentenkontakt: Validieren Sie alle Eingaben mit den erwarteten Typen und Bereichen. Anfragen zur Preisobergrenze, um Missbrauch vorzubeugen. Erfordern Sie eine Authentifizierung für jeden Endpunkt, der den Status ändert. Protokollieren Sie alle Anfragen zu Prüfzwecken. Geben Sie klare Fehlermeldungen zurück, die den Agenten helfen, zu verstehen, was schief gelaufen ist.

## Schaltflächen mit Endpunkten verbinden

Fügen Sie auf jeder Seite, auf der eine Aktion verfügbar ist, drei Dinge hinzu:Ein für menschliche Besucher sichtbarer Aufruf zum Handeln (eine Schaltfläche oder ein Link mit Klartext wie „Verfügbarkeit prüfen“ oder „Angebot anfordern“).

Aktionsschema im Seiten-Markup, das den Endpunkt, die Eingaben und die erwartete Ausgabe beschreibt.

Endpunktdokumentation (entweder inline oder verknüpft), die das genaue Anforderungsformat, die erforderlichen Header und die Antwortstruktur angibt.

Diese dreischichtige Ebene stellt sicher, dass sowohl Menschen als auch Agenten die Aktion über ihre jeweiligen Schnittstellen finden und nutzen können.

## Best Practices für die Sicherheit

Stellen Sie niemals beschreibbare Endpunkte ohne Authentifizierung bereit. Selbst einfache Webhook-Endpunkte sollten einen API-Schlüssel oder ein API-Token im Anforderungsheader erfordern.

Implementieren Sie eine Eingabevalidierung, die fehlerhafte Anfragen zurückweist, bevor sie Ihre Geschäftslogik erreichen. Ein Agent, der ein ungültiges Datumsformat sendet, sollte eine eindeutige Fehlermeldung und keinen Systemabsturz erhalten.

Verwenden Sie idempotente Schlüssel für jede Aktion, die einen Zustand erstellt oder ändert. Wenn dieselbe Anfrage zweimal eintrifft (üblich bei Wiederholungsversuchen durch Agenten), sollte die zweite Anfrage dasselbe Ergebnis zurückgeben, ohne dass eine doppelte Reservierung oder Bestellung erstellt wird.

Zeichnen Sie jede Agenteninteraktion auf. Zeitstempel, Anforderungsnutzlasten, Antwortnutzlasten und Quellagenten-ID. Dies ist wichtig für [Rückkopplungsschleifen](/es/docs/agent-feedback-loops/), die die Genauigkeit im Laufe der Zeit verbessern.

Der [Artikel zur universellen Steuerungsebene](/es/docs/universal-control-plane/) deckt die vollständige Governance-Architektur für agentenseitige Endpunkte ab.

##Agent-Transaktionen testen

Bevor Sie live gehen, testen Sie jeden Endpunkt mit diesen Prüfungen:

Kann der Endpunkt anhand der Aktionsübersicht auf der Seite ermittelt werden? Analysieren Sie die Seite wie ein Agent und stellen Sie sicher, dass das Schema auf eine funktionierende URL verweist.

Akzeptiert der Endpunkt das dokumentierte Eingabeformat und gibt das dokumentierte Ausgabeformat zurück? Senden Sie eine gültige Anfrage und überprüfen Sie, ob die Antwort mit der Schemabeschreibung übereinstimmt. Verarbeitet der Endpunkt ungültige Eingaben korrekt? Senden Sie fehlerhafte Anfragen und stellen Sie sicher, dass die Fehlerantworten strukturiert und informativ sind.

Behandelt der Endpunkt doppelte Anfragen sicher? Senden Sie dieselbe gültige Anfrage zweimal und stellen Sie sicher, dass keine doppelten Aktionen erstellt werden.

Reagiert der Endpunkt innerhalb einer akzeptablen Latenz? Agenten laufen normalerweise nach 10 bis 30 Sekunden ab. Ihr Endpunkt sollte innerhalb dieses Zeitfensters gut reagieren.

---

## Häufig gestellte Fragen

**Ersetzen Agententasten menschliche Gesichtstasten?**
Nein. Sie existieren nebeneinander. Der visuelle Knopf dient menschlichen Besuchern. Das Aktionsschema und der Endpunkt dienen den Agenten. Beide lösen den gleichen Geschäftsprozess aus.

**Was ist PotentialAction in Schema.org?**
Eine Gliederungsart, die eine auf einer Seite verfügbare Aktion beschreibt. Es umfasst den Aktionstyp, die Ziel-URL, erforderliche Eingaben und das erwartete Ergebnis. Agenten nutzen es, um herauszufinden, was sie auf Ihrer Website tun können.

**Wie kann ich agentenseitige Endpunkte sichern?**
Erfordern Sie eine Authentifizierung (API-Schlüssel oder Token), validieren Sie alle Eingaben, implementieren Sie eine Ratenbegrenzung, verwenden Sie idempotente Schlüssel für Statusänderungsaktionen und protokollieren Sie alle Anforderungen.**Kann ich No-Code-Tools für Agent-Endpunkte verwenden?**
Ja. n8n und Make.com unterstützen Webhook-Endpunkte, die strukturiertes JSON akzeptieren, Geschäftslogik ausführen und strukturierte Antworten zurückgeben. Sie verarbeiten die grundlegendsten Agententransaktionsmuster.

**Was passiert, wenn meine Maßnahmenskizze eine Funktion beschreibt, die vorübergehend nicht verfügbar ist?**
Geben Sie eine klare und strukturierte Fehlerantwort zurück, die die Nichtverfügbarkeit erläutert und angibt, wann der Dienst voraussichtlich wieder aufgenommen wird. Lassen Sie keine fehlerhaften Aktionsschemata auf Seiten, auf denen die Funktion nicht mehr vorhanden ist.

## Verwandte Anleitungen

* [AI-Agent-Protokolle](/es/docs/protocols/)

## Primäre Referenzen

* [Google-Richtlinien für strukturierte Daten](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
* [Schema.org-Dokumentation](https://schema.org/docs/documents.html)