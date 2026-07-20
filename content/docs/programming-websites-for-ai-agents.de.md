---
title: "So programmieren Sie Websites für KI-Agenten: 5 Elemente."
metaTitle: "So programmieren Sie Websites für KI-Agenten."
date: 2026-04-12
weight: 60
category: "Architecture"
description: "Bereiten Sie Ihre Website für Agenten mit llms.txt, OpenAPI-Spezifikationen, MCP-Endpunkten, semantischem HTML und Agentenkarten vor. Inklusive Sandboxing."
metaDescription: "Prepare los sitios web para agentes con llms.txt, OpenAPI, puntos finales MCP, HTML semántico, tarjetas de agente y patrones seguros para producción."
summary: "Websites sind agentenbereit, indem sie llms.txt für die Erkennung, OpenAPI-Spezifikationen mit agentenfreundlichen Beschreibungen, MCP-Server für dynamischen Toolzugriff, semantisches HTML für die Extraktion und Agentenkarten für die A2A-Zusammenarbeit hinzufügen."
keywords:
  - "Website-Programmierung für KI-Agenten."
  - "Implementierung von llms.txt"
  - "MCP-Serverkonfiguration"
  - "JSON-Agentenkarte"
  - "Agentenbereite Website-Entwicklung"
  - "WebSocket-Agent-Endpunkte"
---
Websites sind agentenbereit, indem sie klare REST-APIs, llms.txt, MCP-Endpunkte, semantisches HTML und Sicherheitsebenen hinzufügen, sodass autonome KI-Agenten ohne benutzerdefinierten Sticky-Code erkennen, verstehen und handeln können. Nachfolgend sind die fünf wesentlichen technischen Elemente sowie zwei neue Muster aufgeführt, die Produktionssysteme im Jahr 2026 benötigen werden.

## 1. Erstellen Sie llms.txt als Agenten-Sitemap

Platzieren Sie eine Markdown-Datei in /llms.txt im Stammverzeichnis Ihrer Site. Sie dient für KI-Agenten dem gleichen Zweck wie die robots.txt-Datei für Suchcrawler: Sie teilt dem Agenten mit, was Ihre Website bietet, wo sie zu finden ist und wie er mit ihr interagieren kann.

Eine nützliche llms.txt enthält den Namen Ihres Produkts oder Ihrer Dienstleistung und eine Beschreibung in einem Satz, eine Liste der wichtigsten Seiten mit ihrem Zweck, verfügbare API-Endpunkte mit kurzen Beschreibungen, Authentifizierungsanforderungen sowie etwaige Einschränkungen oder Geschwindigkeitsbegrenzungen.

Agenten suchen nach llms.txt, bevor sie die gesamte Website crawlen. Eine Site ohne solche zwingt den Agenten dazu, zu erraten, was verfügbar ist. Eine Seite mit einer klaren und aktuellen llms.txt wird schneller entdeckt und besser verstanden.

Halten Sie es auf dem neuesten Stand. Eine llms.txt, die Endpunkte beschreibt, die nicht mehr vorhanden sind, schadet dem Vertrauen mehr, als wenn überhaupt keine llms.txt vorhanden ist. Das [llms.txt-Programmierhandbuch](/es/docs/programming-llms-txt/) behandelt das Format im Detail.

## 2. Schreiben Sie OpenAPI-Spezifikationen mit agentenfreundlichen Beschreibungen

Wenn Ihre Site API-Endpunkte verfügbar macht, dokumentieren Sie diese mit OpenAPI-Spezifikationen, die vollständige Beispiele für Anfragen und Antworten, detaillierte Fehlerschemata mit spezifischen Fehlercodes und Meldungen, Eingabevalidierungsregeln mit erforderlichen Typen, Bereichen und Feldern sowie Beschreibungen in einfacher Sprache darüber enthalten, was jeder Endpunkt tut und wann er verwendet werden soll.

Die meisten OpenAPI-Spezifikationen sind für menschliche Entwickler geschrieben, die auf fehlenden Kontext schließen können. Agenten können keine Schlussfolgerungen ziehen. Sie müssen jeden Parameter dokumentieren, jeden Fehlerfall beschreiben und jede Einschränkung explizit machen.

Ein häufiger Fehler besteht darin, prägnante einzeilige Beschreibungen wie „Reservierung erstellen“ zu schreiben. In einer agentenfreundlichen Beschreibung heißt es: „Erstellt eine Reservierung für das angegebene Datum und die angegebene Uhrzeit. Erfordert ein gültiges Datum im ISO 8601-Format, einen Zeitbereich ab dem Ende der verfügbaren Slots und eine Kontakt-E-Mail. Gibt ein Bestätigungsobjekt mit der Reservierungs-ID und der Stornierungsfrist zurück. Schlägt mit 409 fehl, wenn der Slot bereits belegt ist.“

## 3. Stellen Sie einen MCP-Server für die dynamische Tool-Erkennung bereit

Das Model Context Protocol (MCP) ist der neue Standard dafür, wie KI-Agenten Tools entdecken und aufrufen. Anstatt Integrationen für jede KI-Plattform zu programmieren, werden deren Fähigkeiten über einen einzigen MCP-Server bereitgestellt, den jeder kompatible Agent erkennen und nutzen kann. MCP verwendet JSON-RPC 2.0 für die Kommunikation. Ihr Server kündigt verfügbare Tools (Funktionen, die der Agent aufrufen kann), Ressourcen (Daten, die der Agent lesen kann) und Eingabeaufforderungen (Vorlagen, die der Agent verwenden kann) an. Agenten erkennen diese Funktionen dynamisch zur Laufzeit.

Ein minimaler MCP-Server stellt Ihre wichtigsten Geschäftsaktivitäten als Tools zur Verfügung: Verfügbarkeit prüfen, Preise abrufen, Reservierungen erstellen, Anfragen senden. Jedes Tool verfügt über ein schriftliches Schema, das Ein- und Ausgänge definiert.Die Investition ist bescheiden. Die Erstellung eines einfachen MCP-Servers in Python oder Node.js für eine Site mit 3–5 Hauptaktionen dauert 2–4 Stunden. Der Vorteil besteht darin, dass jeder MCP-fähige Agent sofort mit Ihrer Site interagieren kann.

## 4. Verwenden Sie semantisches HTML, das ohne JavaScript auskommt

Agenten führen normalerweise kein JavaScript aus. Sie erhalten das Roh-HTML und extrahieren Informationen aus der Dokumentstruktur. Wenn Ihre kritischen Inhalte clientseitig über React, Vue oder Angular ohne serverseitiges Rendering gerendert werden, sehen Agenten eine leere Seite.

Verwenden Sie native HTML-Elemente mit klarer Semantik. Schaltflächenelemente für Aktionen, Formularelemente für Eingaben, Tabellenelemente für strukturierte Daten, Kopfelemente für Hierarchie. Fügen Sie Aria-Label-Attribute hinzu, wenn der Zweck des Elements nicht aus seinem Inhalt ersichtlich ist.

Der Server verarbeitet alle kritischen Informationen. Produktnamen, Preise, Verfügbarkeit, Spezifikationen und Kontaktdaten sollten in der ersten HTML-Antwort enthalten sein und nicht asynchron geladen werden.

Versuchen Sie, Ihre Seite mit Curl abzurufen und zu prüfen, ob in der Antwort wichtige Informationen sichtbar sind. Wenn nicht, können Agenten es auch nicht sehen.

## 5. Veröffentlichen Sie eine Agentenkarte für die A2A-Zusammenarbeit

Eine Agentenkarte ist eine JSON-Datei (agent-card.json), die sich im Stammverzeichnis Ihrer Site befindet und die Funktionen, Authentifizierungsanforderungen und unterstützten Protokolle Ihrer Site für die Agent-zu-Agent-Kommunikation beschreibt.

Das A2A-Protokoll (Agent to Agent) verwendet Agentenkarten zur Erkennung. Wenn ein Agent einen Dienst finden muss, überprüft er die Agentenkarte, um festzustellen, ob die Site hilfreich sein kann, welche Funktionen verfügbar sind und wie die Authentifizierung erfolgt.

Eine einfache Agentenkarte enthält den Namen und die Beschreibung Ihres Dienstes, unterstützte Protokolle (MCP, REST, A2A), verfügbare Funktionen wie strukturierte Liste, Authentifizierungsmethode und Endpunkt sowie Kontaktinformationen für die Fehlerberichterstattung.

Durch die Veröffentlichung einer Agentenkarte verdoppelt sich Ihre Auffindbarkeit in Workflows mit mehreren Agenten, da Agenten, die Ihre Website entdecken, sie anderen Agenten im selben Workflow empfehlen können.

Die [A2A Agent and Guide Cards] (/docs/agent-cards-a2a-protocol/) decken die vollständige Spezifikation ab.

## Neues Muster: Agent-SandboxProduktionsagentensysteme müssen isoliert werden. Wenn ein externer Agent Code ausführt oder Daten in Ihrer Infrastruktur verarbeitet, muss er eingedämmt werden.

WASM-basiertes Sandboxing (ähnlich wie Cloudflare Workers) ermöglicht es Agenten, nicht vertrauenswürdige Vorgänge in isolierten Umgebungen mit definierten Ressourcengrenzen auszuführen. Dadurch wird verhindert, dass sich ein Agent, der sich schlecht verhält, auf andere Benutzer auswirkt oder unbegrenzte Ressourcen verbraucht.

Für die meisten Websites ist Sandboxing nicht unbedingt erforderlich. Dies wird wichtig, wenn Sie Ausführungsendpunkte bereitstellen, die komplexe Eingaben akzeptieren, oder wenn mehrere externe Agenten gleichzeitig mit Ihrem System interagieren.

## Neues Muster: Echtzeit-WebSocket-Endpunkte

Standard-REST-APIs funktionieren für einzelne Anfrage-Antwort-Interaktionen. Mehrstufige Agenten-Workflows profitieren von WebSocket-Verbindungen, die den Status während der gesamten Sitzung beibehalten.Ein WebSocket-Endpunkt in /ws/agent-session ermöglicht es einem Agenten, eine dauerhafte Verbindung für Arbeitsabläufe aufrechtzuerhalten, die mehrere aufeinanderfolgende Schritte umfassen: Überprüfen der Verfügbarkeit, Auswählen von Optionen, Bestätigen von Details und Abschließen der Transaktion. Jeder Schritt erfolgt über dieselbe Verbindung mit gemeinsamem Sitzungsstatus.

Dies verhindert ungewöhnliches Verhalten, das auftritt, wenn Agenten mehrere unabhängige REST-Aufrufe durchführen und den Kontext zwischen ihnen verlieren.

## Vergleich: Traditionelle Architektur versus agentenoptimierte Architektur

| Aussehen | Traditionelle Website | Agentenoptimierte Website |
|
---|
---|
---|
| Entdeckung | robots.txt und Sitemap | llms.txt plus Agentenkarte plus MCP-Registrierung |
| Interaktion | Browserbasierte menschliche Benutzeroberfläche | MCP plus REST plus WebSocket |
| Sicherheit | Statische API-Schlüssel | Agentenspezifische Authentifizierung plus Agentengebühren |
| Datenlieferung | HTML zum Rendern | Strukturiertes JSON plus semantisches HTML |
| Erfolgsmetrik | Seitenaufrufe und Klicks | Abschluss und Aufbewahrung von Agentenaufgaben |

Der [Leitfaden zur Ausführungsebene] (/docs/execution-layer/) erläutert die Architekturprinzipien. Der [AEO-Implementierungsleitfaden] (/docs/implement-aeo/) deckt den gesamten Optimierungspfad ab.

---

## Häufig gestellte Fragen

**Benötige ich alle fünf Elemente, um für die Tätigkeit als Agent bereit zu sein?**
Beginnen Sie mit llms.txt und semantischem HTML (der Leseebene). Fügen Sie OpenAPI- und MCP-Spezifikationen hinzu, wenn Sie API-Endpunkte haben. Fügen Sie die Agentenkarte hinzu, wenn Sie A2A-Sichtbarkeit wünschen.

**Wie lange dauert die Bereitstellung eines einfachen MCP-Servers?**
Zwei bis vier Stunden für eine Site mit 3 bis 5 Hauptaktionen, vorausgesetzt, Sie müssen vorhandene API-Endpunkte optimieren.

**Funktionieren Agenten weiterhin ohne einen MCP-Server?**
Ja, mit REST-API und strukturierter HTML-Extraktion. MCP macht Entdeckung und Interaktion standardisierter und zuverlässiger, aber das ist nicht die einzige Möglichkeit.

**Ist WebSocket-Unterstützung für einfache Websites erforderlich?**Nein. WebSockets sind wichtig für mehrstufige Transaktionsworkflows. Einfache Content-Sites und Single-Action-Endpunkte funktionieren gut mit Standard-REST.

**Wie teste ich, ob meine Website für Agenten bereit ist?**
Stellen Sie Ihre Seiten mit Curl wieder her (ohne JavaScript). Überprüfen Sie Ihre llms.txt auf Richtigkeit. Validieren Sie Ihre OpenAPI-Spezifikation. Testen Sie Ihren MCP-Server mit einem unterstützten Client. Stellen Sie KI-Assistenten Fragen, die Ihre Website beantworten soll.

## Primäre Referenzen

* [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
* [Schema.org-Dokumentation](https://schema.org/docs/documents.html)