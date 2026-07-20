---
title: "Einholen von MCP: menschlicher Input für Arbeitsabläufe."
date: 2026-05-23
weight: 134
category: "Architecture"
description: "Mit MCP Elicitation können Server über den Client strukturierte Eingaben vom Benutzer anfordern. Erfahren Sie, wann es hilft, worum Sie nicht bitten sollten und wie."
summary: "Ein praktischer Leitfaden zum Erhalten von MCP, strukturierter Benutzereingabe, Annahme-/Ablehnungs-/Abbruchabläufen, Human-in-the-Loop-Design und AEO-Workflow-Auswirkungen."
keywords:
  - "MCP-Erhebung"
  - "provozieren/erschaffen"
  - "menschliche Agenten auf dem Laufenden"
  - "MCP-Benutzereingabe"
  - "Sicherheit des Agenten-Workflows"
---
# Einholen von MCP: Menschlicher Input für sicherere Agenten-Workflows

Mit MCP Elicitation kann ein MCP-Server während der Ausführung eines Workflows strukturierte Informationen vom Benutzer über den Client anfordern. Dies ist nützlich, wenn ein Agent fehlende Details benötigt, sollte aber nicht für vertrauliche Informationen verwendet werden. Ein gutes Get-Design macht Agenten-Workflows sicherer, da Benutzer Anfragen annehmen, ablehnen oder stornieren können, anstatt eine versteckte Automatisierung durchlaufen zu müssen.

## Was verdient MCP?

Die offizielle [MCP-Abrufspezifikation] (https://modelcontextprotocol.io/docs/concepts/elicitation) beschreibt eine Standardmethode für Server, um über den Client zusätzliche Informationen vom Benutzer anzufordern. Die Server senden eine „elicitation/create“-Anfrage mit einer Nachricht und einem eingeschränkten JSON-Schema für die erwartete Antwort.

Der Benutzer kann auf drei Arten reagieren:

- mit Daten akzeptieren
- Rückgang
- Abbrechen

Dieses einfache Reaktionsmodell ist wichtig. Bietet dem Kunden eine klare Möglichkeit, die Benutzerkontrolle zu behalten.

Informationen zur zugehörigen Architektur finden Sie unter [MCP vs. Agent API](/es/docs/mcp-vs-api-for-agents/), [Agent UX und Human-in-the-Loop-Design](/es/docs/agent-ux-human-in-the-loop/) und [MCP-Autorisierung mit OAuth](/es/docs/mcp-authorization-oauth-ai-agents/).

## Warum es Erhebung gibt

Agenten beginnen oft mit unvollständigen Anweisungen. Einem Server fehlt möglicherweise ein Feld, bevor er eine Aufgabe abschließen kann.

Beispiele:

- „Welchem Projekt soll diese Nummer zugewiesen werden?“
- „Welches Datum soll der Bericht abdecken?“
- „Welche Lieferadresse soll verwendet werden?“
– „Auf welche Umgebung soll die Bereitstellung abzielen?“
- „Über welchen zugelassenen Lieferanten soll die Bestellung erfolgen?“

Ohne einen standardmäßigen Eingabefluss können Server inkonsistente Eingabeaufforderungsmuster erfinden oder das Modell zum Raten auffordern. Durch die Erhebung erhält diese Interaktion einen strukturierten Verlauf.

## Elicitation vs. normale Chat-Fragen

| Funktion | Normale Chat-Frage | MCP erhalten |
|
---|
---|
---|
| Herkunft anfordern | Assistent oder Benutzer | MCP-Server über Client |
| Antwortformat | Freitext | Strukturiertes Schema |
| Benutzeroptionen | Reagiert normalerweise oder ignoriert | Akzeptieren, ablehnen, stornieren |
| Validierung | Modellabhängig | Der Client kann Felder validieren |
| Sicherheitshaltung | Variiert | Spec warnt vor Anfragen nach sensiblen Daten |

Bei der Erhebung geht es nicht einfach darum, „dem Benutzer eine Frage zu stellen“. Es handelt sich um eine standardisierte Eingabeaufforderung, die innerhalb des Arbeitsablaufs eines Agenten strukturiert ist.

## Welche Server sollten nicht anfragen

Die MCP-Spezifikation besagt, dass Server get nicht zum Anfordern vertraulicher Informationen verwenden sollten. Vermeiden Sie in der Praxis folgende Anfragen:

- Passwörter
- private Schlüssel
- Zahlungskartennummern
- Zugangscodes zur einmaligen Nutzung
- Rohzugriffstoken
- vertrauliche personenbezogene Daten
– Geheimnisse, die zu einem sicheren Tresor gehören. Wenn ein Workflow eine vertrauliche Autorisierung erfordert, verwenden Sie einen geeigneten Authentifizierungsfluss und keinen Get. Die [Ausführungsschicht](/es/docs/execution-layer/) hängt von vertrauenswürdigen Grenzen ab.

## Gute Anwendungsfälle

| Anwendungsfall | Gutes Empfangsfeld | Schlechtes Abrufen des Feldes |
|
---|
---|
---|
| Support-Triage | Prioritätsstufe | Kundenpasswort |
| Umsetzung | Zielumgebung | Cloud-Root-Schlüssel |
| Akquisitionen | Zugelassener Lieferant | Vollständige Kartennummer |
| Inhaltsveröffentlichung | Artikelkategorie | CMS-Administratorkennwort |
| Reiseplanung | Bevorzugter Flughafen | Passscan |

Das Muster ist einfach: provozieren Sie unempfindliche, nicht geheime Vorlieben und Entscheidungen.

## AEO-AuswirkungenFür agentenlesbare Unternehmen ist die Erreichbarkeit wichtig, da nicht alle Aktionen vollständig autonom sein können. Manchmal ist das beste Benutzererlebnis eine klare Pause:

„Ich kann weitermachen, aber ich brauche eine genehmigte Option.“

Websites und APIs, die sich darauf vorbereiten, können Folgendes veröffentlichen:

- klare Handlungsvorgaben
- erlaubte Parameterwerte
- Bestätigungsregeln
- Kletterwege
- Beispiele für gültige Einträge
- Fehlermeldungen, die Agenten verstehen können

Dadurch werden vage menschliche Formen in agentenfreundliche Arbeitsabläufe umgewandelt. Der Leitfaden [AI Agent Programming Websites] (/es/docs/programming-websites-for-ai-agents/) behandelt weitere dieser Vorbereitungsarbeiten.

## Design-Checkliste

1. Fragen Sie nur nach den minimal fehlenden Informationen.
2. Zeigt an, welcher Server die Informationen anfordert.
3. Verwenden Sie Etiketten, die Benutzer verstehen können.
4. Validieren Sie Eingaben, bevor Sie sie senden.
5. Bieten Sie Ablehnungs- und Stornierungsoptionen an.
6. Bitten Sie niemals um Geheimnisse, indem Sie Geheimnisse erlangen.
7. Notieren Sie den Anfragetyp, den Server und das Ergebnis.
8. Halten Sie risikoreiche Aktien hinter der Bestätigung.

## Häufig gestellte Fragen

### Ist der Erhalt von MCP ein Formular?

Sie können eine formularähnliche Benutzeroberfläche generieren, aber das Protokoll selbst definiert das strukturierte Anforderungs- und Antwortmuster, nicht eine bestimmte Schnittstelle.

### Kann Elicitation verschachtelte Objekte anfordern?

Die Spezifikation beschränkt Schemata auf einfachere flache Strukturen mit primitiven Werten. Dies macht die Client-Bereitstellung einfacher und sicherer.

### Sollte Elicitación Zahlungsdaten erfassen?

Nein. Zahlungsdaten und andere Geheimnisse müssen durch Autorisierung oder sichere Zahlungsströme erfolgen, nicht durch Akquise.

### Warum ist das für Websitebesitzer wichtig?

Agentenbereite Arbeitsabläufe benötigen klare Momente, in denen Agenten Menschen nach fehlenden Optionen fragen können, anstatt zu raten. Durch die Erhebung erhält dieses Muster eine Standardform.

## Fazit

MCP Elicitation ist eine kleine Funktion mit einer großen Design-Lektion: Sichere Agenten sollten klar fragen, wann sie menschliche Eingaben benötigen, und Benutzer sollten eine echte Möglichkeit haben, Nein zu sagen.