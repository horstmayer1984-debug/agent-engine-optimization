---
title: "So schreiben Sie llms.txt für KI-Agenten richtig."
metaTitle: "So schreiben Sie llms.txt für KI-Agenten."
date: 2026-04-12
weight: 62
category: "Guide"
description: "llms.txt ist der einfachste und leistungsfähigste Mechanismus zur Agentenerkennung. Exakte Struktur, Inhaltsregeln, dynamische Generierung für große Websites, z."
metaDescription: "Aprenda a escribir llms.txt para agentes de IA, incluida la estructura, las reglas de contenido, la generación dinámica y la integración de esquemas."
summary: "llms.txt teilt KI-Agenten mit, was Ihre Website bietet und wie sie mit ihr interagieren können. Dieser Leitfaden behandelt die genaue Formatierung, Inhaltsregeln, häufige Fehler und die dynamische Generierung für große Websites."
keywords:
  - "Anleitung llms.txt"
  - "llms.txt-Format"
  - "wie man llms.txt schreibt"
  - "Agentenerkennung llms.txt"
  - "Implementierung von llms.txt"
---
llms.txt ist die einfachste und effektivste Möglichkeit, KI-Agenten dazu zu bringen, Ihre Website zu entdecken. Eine Markdown-Datei im Stammverzeichnis Ihrer Website teilt den Agenten mit, was Sie anbieten, wo sie es finden und wie sie damit interagieren können. Agenten suchen nach llms.txt, bevor sie die gesamte Website crawlen. Wenn Sie es also richtig machen, werden Sie zuerst entdeckt.

## Warum llms.txt im Jahr 2026 nicht verhandelbar ist

KI-Agenten folgen bei der Suche nach einer neuen Site einer Erkennungshierarchie. Suchen Sie zunächst nach llms.txt. Zweitens suchen Sie nach agent-card.json. Drittens suchen Sie nach strukturierten Daten in HTML. Viertens: Versuchen Sie, den rohen Seiteninhalt zu analysieren.

Eine Site ohne llms.txt zwingt Agenten, mit Schritt drei oder vier zu beginnen, was langsamer und weniger zuverlässig ist und mit größerer Wahrscheinlichkeit zu einer ungenauen Extraktion führt. Eine Website mit einer klaren llms.txt ermöglicht es Agenten, den gesamten Umfang Ihres Angebots in einer einzigen Anfrage zu verstehen.

Stripe, Cloudflare und Cursor veröffentlichen bereits llms.txt-Dateien. Frühanwender berichten von deutlich höheren Agentenengagementraten und genaueren Angeboten in KI-generierten Antworten.

## Der genaue Aufbau

llms.txt ist eine Markdown-Datei. Verwenden Sie Überschriften, um Informationen zu organisieren, und Klartext für Beschreibungen. Hier ist die empfohlene Struktur:

**Zeile 1: Site-Name als H1-Header.** Eine Zeile, Klartext.

**Abschnitt 1: Was diese Website bietet.** Ein kurzer Absatz (2 bis 3 Sätze), der Ihr Produkt, Ihre Dienstleistung oder Ihren Inhalt objektiv beschreibt. Keine Marketingsprache. Geben Sie an, was es bewirkt, für wen es gedacht ist und was es nützlich macht.

**Abschnitt 2: Schlüsselseiten** Eine Liste der wichtigsten URLs mit jeweils einer einzeiligen Beschreibung. Fügen Sie Ihre Homepage, Hauptprodukt- oder Serviceseiten, Preisseite, Dokumentation und alle Seiten hinzu, auf denen Agenten nach bestimmten Informationen suchen sollten.

**Abschnitt 3: Verfügbare Endpunkte** Wenn Ihre Site API-Endpunkte oder MCP-Tools bereitstellt, listen Sie diese mit kurzen Beschreibungen auf, was jeder tut, welche Eingaben er erfordert und was er zurückgibt.

**Abschnitt 4: Authentifizierung.** Geben Sie an, wie Agenten authentifiziert werden sollen, oder geben Sie ausdrücklich an, dass für den Lesezugriff keine Authentifizierung erforderlich ist.

**Abschnitt 5: Einschränkungen.** Ratenbeschränkungen, Nutzungsrichtlinien, Datenaktualisierungsgarantien und alle Einschränkungen hinsichtlich der Art und Weise, wie Agenten mit Ihrer Website interagieren müssen.

**Abschnitt 6: Kontakt.** So melden Sie Fehler oder fordern Klarstellungen an.

## Inhaltsregeln

Schreiben Sie, um etwas zu extrahieren, nicht um zu überzeugen. Jeder Satz muss eine Tatsache enthalten, die ein Agent verwenden kann. Eliminieren Sie Adjektive, die keine Informationen enthalten. Ersetzen Sie „unsere leistungsfähige Plattform“ durch „API-basierte Programmierplattform für Gesundheitsdienstleister“. Beschränken Sie die Beschreibungen auf ein oder zwei Sätze pro Artikel. Agenten brauchen keine Absätze. Sie benötigen präzise Aussagen, die sie mit Nutzeranfragen vergleichen können.

Aktualisieren Sie llms.txt jedes Mal, wenn Sie eine wichtige Funktion hinzufügen, entfernen oder ändern. Eine veraltete llms.txt, die Funktionen beschreibt, die Sie nicht mehr anbieten, ist schlimmer als keine llms.txt, da sie dazu führt, dass Agenten Aktionen versuchen, die fehlschlagen.

## Dynamische Generierung für große Websites

Websites mit Hunderten von Produkten oder sich häufig änderndem Inventar sollten llms.txt dynamisch generieren, anstatt es manuell zu verwalten.Erstellen Sie ein Skript, das Ihre Produktdatenbank abfragt, die aktuelle Katalogzusammenfassung extrahiert, die aktiven API-Endpunkte aus Ihrer Routenkonfiguration auflistet und das Ergebnis als Markdown-Datei schreibt. Führen Sie dieses Skript nach einem Zeitplan aus (täglich für die meisten Websites, stündlich für Websites mit viel Inventar).

Für Hugo-basierte Websites können Sie llms.txt als Teil des Build-Prozesses generieren, indem Sie ein benutzerdefiniertes Ausgabeformat erstellen, das Ihre Inhaltsdaten als Markdown darstellt.

## Integration von llms.txt mit Schema-Markup

llms.txt und Schema-Markup dienen komplementären Zwecken. llms.txt ermöglicht die Erkennung auf Site-Ebene (was diese gesamte Site bietet). Schema-Markup stellt Details auf Seitenebene bereit (was diese bestimmte Seite enthält).

Verweisen Sie in Ihrem Schema-Markup auf Ihre llms.txt, indem Sie sie als potenzielles Aktionsziel in Ihr Website-Schema aufnehmen. Verweisen Sie auf Ihre wichtigsten schemamarkierten Seiten im Abschnitt „Schlüsselseiten“ von llms.txt.

Dadurch entsteht ein zweistufiges Erkennungssystem: Agenten, die mit llms.txt beginnen, finden schemamarkierte Seiten schneller, und Agenten, die mit einer bestimmten Seite beginnen, können zu llms.txt navigieren, um das vollständige Bild der Site anzuzeigen.

## Vergleich: mit vs ohne llms.txt

| Metrisch | Ohne llms.txt | Mit llms.txt |
|
---|
---|
---|
| Agentenerkennungsrate | Unter 10 Prozent | Bis zu 80 Prozent |
| Zeit bis zur ersten Agenteninteraktion | Tage (Crawling erforderlich) | Sekunden (Einzeldatei lesen) |
| Extraktionspräzision | Variabel (abhängig von der Qualität der Seite) | Hoch (strukturierte Zusammenfassung) |
| Rücklaufquote der Agenten | Niedrig | Deutlich höher |

## Häufige Fehler

Schreiben Sie llms.txt als Marketingtext. Agenten reagieren nicht auf Überzeugungsarbeit. Sie reagieren auf strukturierte Fakten. Jede Zeile sollte eine spezifische Frage dazu beantworten, was Ihre Website leisten kann.

Liste aller Seiten der Website. llms.txt ist keine Sitemap. Schließen Sie nur die Seiten ein, die für die Agenteninteraktion am wichtigsten sind. Für eine 500-seitige Site sollte die llms.txt zwischen 10 und 30 Schlüsselseiten referenzieren.

Ich habe vergessen, es zu aktualisieren. Eine llms.txt, die auf veraltete Endpunkte oder abgekündigte Produkte verweist, schadet aktiv dem Vertrauen der Agenten. Der [AEO-Bereitstellungsleitfaden] (/docs/implement-aeo/) beschreibt, wie llms.txt in den umfassenderen Optimierungspfad passt.

---

## Häufig gestellte Fragen

**Wo genau soll llms.txt platziert werden?**
Im Stammverzeichnis Ihrer Domain: yourdomain.com/llms.txt. Agenten suchen genau in diesem Pfad danach, ähnlich wie in robots.txt.

**Welches Format sollte ich für llms.txt verwenden?**
Rabatt. Verwenden Sie Überschriften für Abschnitte und Klartext für Beschreibungen. Kein HTML, kein JSON, keine benutzerdefinierten Formate.

**Wie lang sollte llms.txt sein?**
Ein oder zwei Seiten prägnanter Text. Genug Zeit, um Ihre wichtigsten Angebote und Endpunkte abzudecken. Kurz genug, dass ein Agent es in einem einzigen Lesevorgang verarbeiten kann.

**Sollte llms.txt Preisinformationen enthalten?**
Ja, wenn der Preis öffentlich ist. Geben Sie Grundpreise, Preismodell (pro Sitzplatz, pro Nutzung, Pauschalpreis) an und geben Sie an, wo detaillierte Preisinformationen zu finden sind.

**Kann ich unterschiedliche llms.txt für verschiedene Subdomains haben?**
Ja. Jede Subdomäne sollte über eine eigene llms.txt verfügen, die die spezifischen Funktionen dieser Subdomäne beschreibt.

## Verwandte Anleitungen

* [AI-Agent-Protokolle](/es/docs/protocols/)
* [Ausführungsschicht](/es/docs/execution-layer/)

## Primäre Referenzen* [Google-Leitfaden zu generativen KI-Funktionen](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
* [Grundlagen der Google-Suche](https://developers.google.com/search/docs/essentials)