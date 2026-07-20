---
title: "Deterministische Entscheidungsbäume: Wie KI-Agenten."
metaTitle: "Entscheidungsbäume für KI-Agenten: Evaluierungsleitfaden."
date: 2026-04-14
weight: 92
category: "Architecture"
description: "KI-Agenten führen strenge Pass/Fail-Entscheidungsbäume durch, bevor sie Transaktionen durchführen. Welche deterministischen Fragen stellen sie, welche Ursache."
metaDescription: "Descubra qué comprobaciones de aprobación/rechazo utilizan los agentes de IA antes de actuar, qué causa la exclusión y cómo hacer que su sitio web sea más."
summary: "Agenten navigieren oder entscheiden nicht intuitiv. Sie führen deterministische Entscheidungsbäume mit strengen Pass/Fail-Kriterien aus. Eine Prüfung schlägt fehl und der Agent wechselt zu einem Konkurrenten."
keywords:
  - "Agentenentscheidungsbäume"
  - "deterministische Bewertung des Agenten"
  - "Genehmigungskriterien für Agenten"
  - "Fähigkeitszuordnungsagenten"
  - "Ausschlusskriterien für Agenten"
  - "Maschine-zu-Maschine-Auswertung"
---
KI-Agenten bewerten Ihre Website nicht wie Menschen. Sie navigieren nicht, sie machen sich keine Eindrücke und nach und nach bauen sie Vertrauen auf. Sie führen an jedem Knoten deterministische Entscheidungsbäume mit strengen Pass/Fail-Kriterien aus. Wenn eine Überprüfung fehlschlägt, wird der Prozess beendet. Der Agent wechselt ohne Erklärung zum nächsten Anbieter.

Das Verständnis dieser Entscheidungsbäume macht den Unterschied zwischen ausgewählt und stillschweigendem Ausschluss aus.

## Die sechs Fragen, die jeder Agent stellt

### Frage 1: Was kann dieses System?

Der Agent strebt eine Leistungsbescheinigung an. In UCP-Implementierungen ist dies die JSON-Datei in /.well-known/ucp. In MCP-Implementierungen handelt es sich um die vom Server zurückgegebenen Tool- und Ressourcenschemata. In einfacheren Konfigurationen ist es die Datei llms.txt oder die Agent Card.

Wenn der Agent nicht feststellen kann, was Ihr System unterstützt, wird er es vollständig ignorieren. Es gibt keine Teilgutschrift. Entweder sind die Fähigkeiten deklariert oder nicht.

Genehmigungsbedingung: Eine maschinenlesbare Erklärung der unterstützten Aktionen, Datentypen und Transaktionsfähigkeiten.

Fehlerbedingung: kein Manifest, kein Schema, keine llms.txt. Der Makler hat keine Möglichkeit festzustellen, was Sie anbieten.

### Frage 2: Welche Materialien werden benötigt?

Sobald der Agent weiß, was er tun kann, prüft er, ob er über die notwendigen Eingaben verfügt, um die Aktion auszulösen. Ihr System sollte einen klaren Überblick über die erwarteten Eingabewerte bieten: Datentypen, erforderliche und optionale Felder, Validierungsregeln und akzeptable Bereiche.

Erfolgsbedingung: Jeder Endpunkt oder jede Aktion verfügt über ein dokumentiertes Eingabeschema mit Typen, Einschränkungen und Beispielen.

Fehlerbedingung: Die Einreisebestimmungen sind vage, nicht dokumentiert oder können nur durch Versuch und Irrtum ermittelt werden.

### Frage 3: Ist der aktuelle Stand überprüfbar?

Der Agent vertraut dem Inhalt der statischen Seite nicht. Sie müssen den kritischen Status in Echtzeit überprüfen.

Ist der Preis explizit und aktuell? Menschliche Phrasen wie „Preis auf Anfrage“ oder „ab“ führen bei risikoaversen Transaktionen zum sofortigen Ausschluss. Der Agent benötigt eine genaue Nummer, die für einen definierten Zeitraum gültig ist.

Wird der Bestand in Echtzeit überprüft? Der Agent sendet einen API-Aufruf. Der zwischengespeicherte HTML-Code mit der Meldung „auf Lager“ ist wertlos, wenn der tatsächliche Lagerbestand vor zwei Stunden ausverkauft war.

Sind die Richtlinien strukturiert und maschinenlesbar? Rückgabebedingungen, Versandbedingungen, Stornierungsbedingungen. Wenn sie nur als Prosaabsätze auf einer juristischen Seite existieren, kann der Agent sie nicht zuverlässig analysieren. Schema.org-Aktions-Tags und strukturierte Richtlinienanweisungen sind erforderlich.

Erfolgsbedingung: Überprüfbarer Echtzeitstatus für jeden kritischen Transaktionsparameter. Fehlerbedingung: Veraltete Daten, unklare Preise, unstrukturierte Richtlinien oder alle Parameter, die eher einer Interpretation als einer Analyse bedürfen.

### Frage 4: Welcher Zustand ist nach der Aktion garantiert?

Der Agent benötigt deterministische Garantien darüber, was passieren wird, wenn er handelt. Wenn Sie einen Kauf tätigen, erhalten Sie eine Bestätigung mit einer Bestellnummer? Erhält das Unternehmen bei der Buchung eines Termins ein bestätigtes Zeitfenster? Wenn die Aktion fehlschlägt, erhalten Sie eine strukturierte Fehlermeldung mit einer Begründung?

Erfolgsbedingung: Jeder Aktionsendpunkt gibt ein deterministisches Ergebnis zurück (Erfolg mit Commit-Details oder Fehler mit spezifischer Fehlerklassifizierung).

Fehlerbedingung: Mehrdeutige Antworten, Bestätigungen in menschlicher Sprache ohne strukturierte Daten oder Endpunkte, die ohne überprüfbare Beweise Erfolg melden.

### Frage 5: Stimmen die Attribute zwischen den Quellen überein?Agenten verweisen auf Daten aus mehreren Quellen. Wenn Ihr Preis im Google Merchant Center von Ihrer API-Antwort abweicht oder Ihr Schema-Markup eine andere Verfügbarkeit anzeigt als Ihr UCP-Manifest, erkennt der Agent die Inkonsistenz.

Inkonsistenzen sorgen nicht nur für Verwirrung. Sie bewirken Ausgrenzung. Ein Agent, der Ihren Daten nicht vertrauen kann, wird keine Transaktionen über Ihr System durchführen.

Genehmigungsbedingung: Identische Werte für Preis, Verfügbarkeit, Spezifikationen und Richtlinien in allen maschinenlesbaren Quellen (Schema-Markup, API-Antworten, Produkt-Feeds, UCP-Manifest).

Fehlerbedingung: Jegliche Diskrepanz zwischen Datenquellen.

### Frage 6: Kann die Aktion sicher wiederholt werden?

Im Fehlerfall versuchen es die Agenten erneut. Wenn das Netzwerk nach dem Kauf eine Zeitüberschreitung erfährt, sendet der Agent dieselbe Anfrage erneut. Ihr System sollte dies bewältigen, ohne dass doppelte Bestellungen, doppelte Gebühren oder fehlerhafte Status erstellt werden.

Erfolgsbedingung: Idempotente Transaktionsendpunkte, bei denen dieselbe Anfrage dasselbe Ergebnis liefert, unabhängig davon, wie oft sie übermittelt wird.

Fehlerbedingung: Nicht idempotente Endpunkte, bei denen Wiederholungsversuche Duplikate erzeugen.

## Der Entscheidungsbaum in der Praxis

Der Agent wertet diese Fragen nacheinander aus. Bei jedem „Nichtbestehen“ wird die Bewertung sofort beendet:

Deklarierte Kapazität? Nein → ausgeschlossen. Dokumentierte Eingaben? Nein → ausgeschlossen. Überprüfbarer Status in Echtzeit? Nein → ausgeschlossen. Deterministische Ergebnisse? Nein → ausgeschlossen. Daten konsistent über alle Quellen hinweg? Nein → ausgeschlossen. Sichere Wiederholungsversuche? Nein → ausgeschlossen.

Erst wenn alle sechs Prüfungen bestanden sind, fährt der Agent mit der Transaktion fort.

## Warum sich dies von der menschlichen Bewertung unterscheidetEin menschlicher Käufer toleriert Unklarheiten. „Preis auf Anfrage“ bedeutet, dass sie anrufen. „Normalerweise in 3–5 Tagen versandfertig“ ist nahe genug. Sie blättern durch und akzeptieren eine verwirrende Rückgaberichtlinie.

Ein Agent duldet nichts davon. Jede Unklarheit ist eine Bedingung des Scheiterns. Alles „normalerweise“ ist unbestimmt. Jede unstrukturierte Politik ist unmöglich zu analysieren. Der Agent arbeitet mit binärer Logik: verifiziert oder ausgeschlossen.

Aus diesem Grund können Websites, die für Menschen elegant aussehen, bei Agenten null Punkte erzielen. Visuelles Design, Markenruf und überzeugende Texte haben in einem deterministischen Entscheidungsbaum keine Bedeutung.

Der [Leitfaden zur Ausführungsebene](/es/docs/execution-layer/) erläutert die Infrastrukturanforderungen. Der [AEO-Implementierungsleitfaden](/es/docs/implement-aeo/) behandelt den schrittweisen Optimierungspfad.

---

## Häufig gestellte Fragen

**Was ist ein deterministischer Entscheidungsbaum in AEO?**
Eine strenge Abfolge von Genehmigungs-/Fehlerprüfungen, die ein Agent durchführt, bevor er eine Transaktion mit Ihrer Website durchführt. Bei jeder Verifizierung wird eine bestimmte Anforderung bewertet (Fähigkeiten, Eingaben, Zustand, Ergebnisse, Konsistenz, Idempotenz). Das Scheitern einer Überprüfung führt zum sofortigen Ausschluss.

**Was ist der häufigste Grund, warum Agenten eine Website ausschließen?**
Unstrukturierte oder mehrdeutige Preise. „Preis auf Anfrage“, „ab“ oder Preise, die zwischen Schema-Markup und API-Antworten abweichen, führen zu einem sofortigen Ausschluss.

**Wie teste ich, ob meine Website die Agentenbewertung besteht?**
Simulieren Sie alle sechs Fragen manuell. Können Sie Ihre Fähigkeitserklärung finden? Sind alle Einträge dokumentiert? Können Sie den Status mithilfe eines API-Aufrufs überprüfen? Geben alle Datenquellen identische Werte zurück? Führen Sie diese Prüfung monatlich durch.**Was ist ein Fähigkeitsmanifest?**
Eine maschinenlesbare Datei, die erklärt, was Ihr System tun kann. In UCP: /.known/ucp. In MCP: Tools und Ressourcenschemata. In einfacheren Konfigurationen: llms.txt oder agent-card.json.

**Warum ist Idempotenz so wichtig?**
Denn Agenten versuchen es erneut, wenn sie scheitern. Eine Zeitüberschreitung bedeutet nicht, dass die Aktion fehlgeschlagen ist. Wenn Ihr Endpunkt bei einem erneuten Versuch eine doppelte Bestellung erstellt, hat der Agent echten Schaden angerichtet. Idempotente Endpunkte verarbeiten Wiederholungsversuche sicher, indem sie dasselbe Ergebnis für dieselbe Anfrage zurückgeben.

## Verwandte Anleitungen

* [Agent-Handelsarchitektur](/es/docs/agentic-commerce/)

## Primäre Referenzen

* [NIST AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
* [Schema.org-Dokumentation](https://schema.org/docs/documents.html)