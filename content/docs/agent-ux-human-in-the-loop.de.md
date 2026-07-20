---
title: "Agent UX und Human-in-the-Loop-Design: Schnittstellenerstellung."
metaTitle: "Agent UX und Human-in-The-Loop-Design."
date: 2026-04-12
weight: 86
category: "Guide"
description: "Entwerfen Sie Agent UX mit klaren Genehmigungen, Vorschauen, Reversibilität und Status-Feedback, damit Mitarbeiter Aktionen überwachen können."
metaDescription: "Diseñe interfaces para humanos y agentes de IA con HTML semántico, aprobaciones, comentarios estructurados, mensajes de estado y flujos de trabajo."
summary: "Moderne Schnittstellen müssen zwei Zielgruppen gleichzeitig bedienen: menschliche Benutzer und KI-Agenten. Das responsive Design des Agenten nutzt semantisches HTML, strukturierte Endpunkte und Feedbackschleifen, um beides zu erfüllen."
keywords:
  - "Agenten-UX-Design"
  - "menschliche Agenten auf dem Laufenden"
  - "Responsive Design für Agenten"
  - "Dual-Interface-Design"
  - "Genehmigungsworkflows für Agenten"
---
Durch das auf Agenten reagierende Design funktionieren Schnittstellen gleichzeitig für zwei Zielgruppen: menschliche Benutzer, die visuell navigieren, und KI-Agenten, die strukturell analysieren. Die besten Implementierungen erfordern keine separaten Schnittstellen. Sie bauen ein System auf, das durch eine saubere Architektur beiden dient.

## Die Herausforderung des doppelten Publikums

Eine Produktseite muss einen menschlichen Käufer mit visuellem Design, Marken-Storytelling und emotionalen Auslösern überzeugen. Dieselbe Seite muss einen KI-Agenten mit strukturierten Spezifikationen, präzisen Preisen und expliziter Verfügbarkeit informieren.

Dabei handelt es sich nicht um widersprüchliche Ziele, sondern um unterschiedliche Ziele. Der Fehler besteht darin, für eine Zielgruppe zu optimieren und davon auszugehen, dass die andere zufrieden ist.

Eine Seite mit schönen Bildern und einer fesselnden Erzählung, aber ohne strukturierte Daten, dient den Menschen und schließt Agenten aus. Eine Seite mit einfachen JSON-Endpunkten und ohne visuelles Design dient Agenten und schließt Menschen aus. Das Ziel ist eine einheitliche Seite, die beide Ebenen enthält.

## Semantisches HTML als Basis

Agenten ignorieren in den meisten Fällen in JavaScript gerenderte Inhalte. Sie analysieren rohes HTML. Semantische Elemente (Kopfhierarchie, Tabellenelemente, Listenelemente, Formularelemente, Schaltflächenelemente) stellen die Strukturinformationen bereit, die Agenten benötigen.

Verwenden Sie native HTML-Elemente anstelle von formatierten Divs. Ein Schaltflächenelement teilt einem Agenten mit, dass eine anklickbare Aktion vorhanden ist. Ein Div, das wie eine Schaltfläche aussieht, sagt dem Agenten nichts.

Fügen Sie Aria-Label-Attribute hinzu, wenn der Zweck des Elements nicht aus seinem Inhalt ersichtlich ist. Ein Agent, der Ihre Seite analysiert, profitiert von den gleichen Zugänglichkeitspraktiken wie Screenreader.

Verarbeiten Sie alle kritischen Inhalte auf dem Server. Wenn Ihr Produktname, Ihr Preis und Ihre Verfügbarkeit die Anzeige von JavaScript erfordern, können Agenten diese nicht sehen. Der [Agent Website Programming Guide](/es/docs/programming-websites-for-ai-agents/) deckt die technischen Anforderungen ab.

##Human-in-the-Loop-Genehmigungsabläufe

Nicht alle Agentenaktionen sollten autonom abgeschlossen werden. Entwerfen Sie Genehmigungsflüsse, die bei risikoreichen Entscheidungen auf die menschliche Bestätigung warten.

Der Genehmigungsablauf besteht aus drei Komponenten: Der Agent schlägt eine Aktion vor (die dem Menschen in klaren und strukturierten Worten angezeigt wird), der Mensch überprüft und genehmigt oder lehnt ab und das System führt basierend auf der menschlichen Entscheidung aus oder bricht sie ab.

Für Ihre Site-Endpunkte bedeutet dies die Unterstützung asynchroner Arbeitsabläufe. Ein Agent sendet eine Reservierungsanfrage. Ihr System gibt den Status „Ausstehend“ mit einer Aufgaben-ID zurück. Menschliche Bewertungen. Ihr System aktualisiert den Status auf „Bestätigt“ oder „Abgelehnt“. Der Agent fragt die Aufgaben-ID ab und erhält den endgültigen Status. Dieses Muster eignet sich für Kaufgenehmigungen oberhalb eines Ausgabenschwellenwerts, für die Einreichung von Rechtsdokumenten, für Kontoänderungen und für alle Aktionen, die von menschlichem Urteilsvermögen profitieren.

## Strukturierte Feedback-Schnittstellen

Sowohl Menschen als auch Agenten müssen Probleme melden. Aber sie berichten anders.

Menschliches Feedback: ein Kommentarfeld, eine Sternebewertung, ein Support-Ticket. Unstrukturiert, kontextreich, bedarf der Interpretation.

Agenten-Feedback: Ein strukturierter Endpunkt, der die URL einer Seite, erwartete Daten, tatsächlich gefundene Daten und Fehlerklassifizierung akzeptiert. Keine Interpretation erforderlich.Baue beides. Das menschliche Feedback-Formular ist auf der Seite sichtbar. Der Feedback-Endpunkt des Agenten, dokumentiert in Ihrer llms.txt-Datei und Ihrer Agentenkarte. Beide fördern den gleichen Verbesserungsprozess durch ihre [Feedbackschleifen](/es/docs/agent-feedback-loops/).

## WebSocket-Endpunkte für Live-Sitzungen

Standard-REST-APIs funktionieren für zustandslose Interaktionen. Mehrstufige Agenten-Workflows profitieren von WebSocket-Verbindungen, die den Sitzungsstatus aufrechterhalten.

Ein WebSocket-Endpunkt in /ws/agent-session ermöglicht es einem Agenten, den Kontext durch eine Abfolge von Aktionen aufrechtzuerhalten: Produkte durchsuchen, die Auswahl eingrenzen, die Verfügbarkeit der besten Option prüfen und einen Kauf abschließen. Jeder Schritt erfolgt über dieselbe Verbindung mit gemeinsamem Status.

Für die menschliche Parallele: Dieselbe zugrunde liegende Sitzungslogik kann einen geführten Checkout-Ablauf in der Browser-Benutzeroberfläche steuern und dabei dieselbe Geschäftslogik über eine andere Schnittstelle verwenden.

## Design für elegante Degradierung

Ihre Schnittstelle sollte auf allen Funktionsebenen funktionieren: vollständige menschliche Browsererfahrung (JavaScript, CSS, Bilder, Interaktion), reduzierte Browsererfahrung (langsame Verbindung, kein JavaScript), Agentenerfahrung (einfaches HTML, strukturierte Daten, Endpunkte) und grundlegende Agentenerfahrung (nur HTML-Textinhalt).

Jede Ebene bedient einen anderen Kunden. Entwerfen Sie es so, dass durch das Entfernen einer Schicht die darunter liegenden Schichten nicht beschädigt werden. Wenn Ihr JavaScript fehlschlägt, sollte der HTML-Code immer noch wichtige Informationen enthalten. Wenn Ihre Endpunkte nicht funktionieren, sollte der HTML-Code weiterhin lesbar sein.

Der [AEO-Implementierungsleitfaden](/es/docs/implement-aeo/) behandelt die Struktur der Inhaltsschicht.

---

## Häufig gestellte Fragen

**Was ist Agent Responsive Design?**
Ein Interface-Design-Ansatz, der sowohl menschliche Benutzer als auch KI-Agenten über eine einzige Architektur bedient. Semantisches HTML stellt die vom Agenten lesbare Ebene bereit. Visuelles Design stellt die menschliche Ebene dar. Beide nutzen die gleichen zugrunde liegenden Daten.

**Benötige ich separate Schnittstellen für Agenten?**
Normalerweise nicht. Eine gut strukturierte Seite mit semantischem HTML, Schema-Markup und dokumentierten Endpunkten bedient beide Zielgruppen. Separate Schnittstellen sind nur für komplexe Transaktionsabläufe relevant.**Welche Rolle spielt der Mensch im Loop bei AEO?**
Bietet ein Sicherheitsnetz für Aktionen von Hochrisikoagenten. Der Agent schlägt vor, der Mensch stimmt zu, das System führt aus. Dies schafft Vertrauen und verhindert kostspielige Fehler in vollständig autonomen Systemen.

**Wie helfen WebSocket-Endpunkte Agenten?**
Sie behalten den Sitzungsstatus in mehrstufigen Arbeitsabläufen bei und verhindern so den Kontextverlust zwischen aufeinanderfolgenden REST-Aufrufen. Dies ist besonders nützlich für Einkaufsabläufe und komplexe Serviceinteraktionen.

**Sollte ich menschliche UX oder Agenten-UX priorisieren?**
Beides. Wenn Sie gezwungen sind, einen Ausgangspunkt zu wählen, bietet Ihnen Human UX mit semantischem HTML beide Zielgruppen. Agentenspezifische Endpunkte (MCP, WebSocket) können schrittweise hinzugefügt werden.

## Primäre Referenzen

* [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
* [Schema.org-Dokumentation](https://schema.org/docs/documents.html)