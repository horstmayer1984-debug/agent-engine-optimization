---
title: "Webbot-Authentifizierung für KI-Crawler: Ein Leitfaden."
date: 2026-05-23
weight: 131
category: "Architecture"
description: "Web Bot Auth verwendet kryptografische HTTP-Signaturen, um Bots und automatisierte Agenten zu überprüfen. Finden Sie heraus, wie es mit dem Vertrauen der Tracker zusammenpasst."
summary: "Ein praktischer Leitfaden zur Web-Bot-Authentifizierung für KI-Crawler, signierte Agenten, Crawler-Verifizierung und Richtliniendesign für von Agenten lesbare Websites."
keywords:
  - "Webbot-Authentifizierung"
  - "AI-Tracker-Überprüfung"
  - "unterzeichnete Agenten"
  - "HTTP-Nachrichtensignaturen"
  - "Tracker-Identität"
---
#Webbot-Authentifizierung für KI-Crawler: Ein praktischer Leitfaden von AEO

Web Bot Auth ist eine Möglichkeit für Crawler und automatisierte Agenten, ihre Identität mit kryptografischen HTTP-Signaturen nachzuweisen. Für AEO ist dies wichtig, da die Crawler-Identität zu einer Vertrauensebene wird: Websitebesitzer müssen nützlichen Such-, Antwort- und Agentenverkehr von Spoofing, Scraping und Missbrauch unterscheiden.

## Was ist Web-Bot-Authentifizierung?

Cloudflares Web Bot Authentication Documentation (https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/) beschreibt es als eine Authentifizierungsmethode, die kryptografische Signaturen in HTTP-Nachrichten verwendet, um zu überprüfen, ob eine Anfrage von einem automatisierten Bot stammt. Cloudflare verwendet es für verifizierte Bots und signierte Agenten, basierend auf aktiven IETF-Entwürfen für das öffentliche Schlüsselverzeichnis und das Anforderungssignaturverhalten.

Laienhaft ausgedrückt: Ein Tracker veröffentlicht einen öffentlichen Schlüssel, signiert Anfragen mit seinem privaten Schlüssel und die empfangende Infrastruktur kann überprüfen, ob die Anfrage wirklich von diesem Tracker kommt.

Dies ist ein anderes Problem als [robots.txt für KI-Crawler](/es/docs/ai-crawlers-robots-txt/). Robots.txt sagt, was ein Crawler tun soll. Web Bot Auth hilft beim Nachweis, wer der Tracker ist.

## Warum die Tracker-Identität jetzt wichtig ist

KI-Suche und autonome Agenten sorgen für einen verwirrenden Traffic-Mix:

- klassische Such-Tracker
- KI-Reaktions-Tracker
- Tracker-Training
- Browser-Agenten, die für Benutzer agieren
- kommerzielle Schabesysteme
– Fake-Bots, die vertrauenswürdige User-Agent-Strings verwenden
- Sicherheitsscanner und -monitore

Wenn sie alle gleich aussehen, hat ein Websitebesitzer nur eine schwierige Wahl: zu viel zulassen oder zu viel blockieren. AEO benötigt eine mittlere Ebene, auf der vertrauenswürdige Agenten auf öffentliche Inhalte zugreifen können und nicht vertrauenswürdiger Datenverkehr herausgefordert oder eingeschränkt werden kann.

## Web-Bot-Authentifizierung im Vergleich zu gängigen Verifizierungsmethoden

| Methode | Was es beweist | Stärke | Schwäche |
|
---|
---|
---|
---|
| Benutzeragentenzeichenfolge | Was der Antragsteller behauptet | Leicht zu lesen | Leicht zu fälschen |
| Reverse-DNS | Wenn die IP zu einem bekannten Anbieter gehört | Reif für große Tracker | IP-Bereiche und Infrastrukturänderungen |
| IP-Zulassungsliste | Die Anfrage kommt von erlaubten Adressen | Einfach für stabile Paare | Zerbrechlich und schwer zu klettern |
| Webbot-Authentifizierung | Die Anfrage wird mit einem registrierten Schlüssel | signiert Stärkerer Identitätsnachweis | Erfordert die Einführung und korrekte Implementierung des Trackers |
| Anmeldetoken/API | Autorisierter Kontozugriff | Stark für private Systeme | Nicht zum alleinigen Kriechen in der Öffentlichkeit geeignet |

Die wahrscheinliche Zukunft ist nicht, dass eine Methode alle anderen ersetzen wird. Es handelt sich um eine mehrschichtige Überprüfung.

## So funktioniert der Ablauf

Auf hohem Niveau:

1. Der Tracker generiert einen Signaturschlüssel.
2. Der Crawler hostet ein Schlüsselverzeichnis an einem bekannten Ort.3. Der Crawler registriert den Bot und das Schlüsselverzeichnis beim Verifizierungsanbieter.
4. Nach der Überprüfung signiert der Tracker die Anfragen.
5. Das empfangende System validiert die Signatur und wendet die Richtlinie an.

Die Cloudflare-Dokumentation enthält spezifische Anforderungen wie Ed25519-Schlüssel, ein Schlüsselverzeichnis, HTTPS und signierte HTTP-Header.

## Auswirkungen der AEO-Richtlinie

Web Bot Auth hilft bei der Beantwortung einer praktischen Frage: „Sollte diese Maschinenanfrage vertrauenswürdig genug sein, um auf unsere von Agenten lesbaren öffentlichen Oberflächen zuzugreifen?“

Für eine AEO-fähige Website kann dies Folgendes beeinflussen:- ob KI-Crawler auf die Dokumentation zugreifen können
– ob der Agentenverkehr öffentliche Leitfäden lesen kann
- wenn die Geschwindigkeit beim Schaben mit hohem Volumen begrenzt ist
– wenn API-Dokumente sichtbar sind, Ausführungsendpunkte jedoch eine Authentifizierung erfordern
- ob signierte Agenten anders behandelt werden als anonyme Bots

Dies stellt eine direkte Verbindung zur [Ausführungsebene](/es/docs/execution-layer/) und zu den [Beobachtbarkeitsleitplanken für Agenten](/es/docs/agent-observability-guardrails/) her.

## Empfohlenes Zugangslayout

| Site-Bereich | Vorgeschlagene Zugriffsrichtlinie |
|
---|
---|
| Öffentliche Reiseführer | Akkreditierte Tracker zulassen; Lautstärke regeln |
| llms.txt und Sitemap | Zugänglich bleiben |
| API-Referenzdokumente | Entdeckung zulassen; Anmeldeinformationen und Ausführung schützen |
| Preis- und Produktseiten | Suche und Abruf von Antworten zulassen |
| Bezahlung, Konto, Administrator | Authentifizierung und Ratenbegrenzung |
| Exklusive Daten für Mitglieder | Signierte Authentifizierung oder Kontotoken erforderlich |

Ziel ist es, das öffentliche Web für Agenten nutzbar zu machen, ohne private Systeme in offene Tools zu verwandeln.

## Checkliste für die Bereitstellung

1. Inventarisieren Sie Bots, die derzeit auf der Website eintreffen.
2. Separate Suche, künstliche Intelligenz, Schulung, Überwachung und Scraping-Verkehr.
3. Halten Sie [llms.txt](/es/docs/llms-txt-vs-robots-txt/) und öffentliche Dokumente zugänglich.
4. Fügen Sie Bot-Regeln hinzu, die Googlebot, Bingbot und andere beliebte Erkennungssysteme nicht versehentlich blockieren.
5. Verwenden Sie Web Bot Auth oder eine ähnliche Überprüfung, sofern unterstützt.
6. Notieren Sie den Verifizierungsstatus zusammen mit der URL, dem Statuscode und der Ratenbegrenzungsaktion.
7. Überprüfen Sie die Regeln nach jeder CDN-, Firewall- oder Site-Migrationsänderung.

## Häufig gestellte Fragen

### Gilt die Web-Bot-Authentifizierung nur für Cloudflare?

Cloudflare dokumentiert seine Implementierung, aber die Idee basiert auf umfassenderen Entwürfen von HTTP-Nachrichtensignaturen und Schlüsselverzeichnissen. Die Akzeptanz hängt von der Infrastruktur und der Tracker-Unterstützung ab.

### Teilt Web Bot Auth Crawlern mit, wofür sie den Inhalt verwenden können?

Nein. Identität überprüfen. Nutzungspräferenzen erfordern weiterhin Richtlinienebenen wie robots.txt, Inhaltstoken, Verträge oder Zugriffsregeln.

### Kann Web Bot Auth die Reverse-DNS-Verifizierung ersetzen?

Nicht sofort. Viele Websites nutzen beide, insbesondere wenn die Akzeptanz signierter Tracker uneinheitlich ist.### Warum ist das für KI-Agenten wichtig?

Agenten stellen zunehmend Webanfragen im Namen von Benutzern oder Systemen. Eine signierte Identität erleichtert die Anwendung unterschiedlicher Regeln auf vertrauenswürdige Agenten, anonyme Tracker und missbräuchliche Automatisierung.

## Fazit

Web Bot Auth ist ein vertrauenswürdiges Crawler-Grundelement. Es wird die Inhaltslizenzierung oder die KI-Sichtbarkeit nicht allein lösen, aber es gibt AEO-Teams eine bessere Grundlage für die Entscheidung, welcher Maschinenverkehr Zugriff verdient.