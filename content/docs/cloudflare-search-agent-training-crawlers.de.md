---
title: "Cloudflare Search Tracker, Agents und Schulungen."
metaTitle: "Cloudflare-Such-, Agenten- und Schulungs-Tracker."
date: 2026-07-02
weight: 188
category: "Analysis"
description: "Cloudflare unterteilt den KI-Verkehr jetzt in Suchcrawler, Agenten und Schulungen. Finden Sie heraus, was das für AEO, robots.txt und Access bedeutet."
summary: "Ein praktischer AEO-Leitfaden zur KI-Traffic-Taxonomie von Cloudflare vom Juli 2026 für Such-Crawler, Agenten und Schulungen."
keywords:
  - "Cloudflare Search Agent Training Crawler"
  - "Taxonomie von KI-Crawlern"
  - "Zugriff auf den Agenten-Tracker"
  - "KI-Verkehrskontrollen"
  - "AEO-Tracker-Richtlinie"
---
# Cloudflare Search Tracker, Agents und Schulungen

Die KI-Verkehrskontrollen von Cloudflare vom Juli 2026 unterteilen den automatisierten KI-Verkehr in drei praktische Kategorien: Suche, Agent und Schulung. Für AEO-Teams besteht die wichtige Änderung darin, dass die Tracker-Richtlinie nicht länger eine klare Wahl zwischen „KI zulassen“ oder „KI blockieren“ sein kann. Suchsichtbarkeit, Agentenaufgabenausführung und Modellschulung erfordern jetzt separate Regeln.

## Was sich im Juli 2026 geändert hat

Am 1. Juli 2026 kündigte Cloudflare [neue KI-Traffic-Optionen für alle Kunden](https://blog.cloudflare.com/content-independence-day-ai-options/) an. Die neuen Kontrollen klassifizieren KI-bezogene Automatisierung nach Zweck:

| Kategorie | Was es bedeutet | AEO-Implikation |
|
---|
---|
---|
| Suche | Inhalte crawlen oder indizieren, damit Sie sie später finden können | Generell lohnt es sich, öffentliche Discovery-Seiten zuzulassen |
| Agent | Automatisierung, die durch den Benutzer gesteuert wird, der eine Website besucht, um eine Aufgabe auszuführen | Benötigen Sie aktionssichere UX, Berechtigungen und Fehlerbehandlung |
| Ausbildung | Crawlen von Inhalten zum Trainieren oder Optimieren von Modellen | Erfordert häufig eine gesonderte Rechts-, Lizenz- oder Monetarisierungsentscheidung |

Laut Cloudflare stehen die Optionen allen Kunden zur Verfügung, auch Benutzern des kostenlosen Kontingents. Dies ist wichtig, da sich die Governance von Trackern von einer reinen Unternehmenskontrolle zu einer normalen Veröffentlichungsentscheidung entwickelt.

## Warum dies für die Agent Engine-Optimierung wichtig ist

Traditionelles SEO behandelt Crawler in erster Linie als Indexer. AEO sollte automatisierte Besucher als unterschiedliche Akteure behandeln:

– ein Such-Crawler, der Benutzern hilft, eine Seite zu entdecken
- eine Antwortmaschine, die die Seite zitieren oder zusammenfassen kann
- ein Browser-Agent, der klicken, vergleichen oder senden kann
- ein Trainings-Tracker, der Inhalte aufnehmen kann, ohne Traffic zurückzugeben

Deshalb trennt [Agent Engine Optimization](/es/docs/what-is-aeo/) die [Leseschicht](/es/docs/answer-engine-optimization/) von der [Ausführungsschicht](/es/docs/execution-layer/). Suchcrawler gehören hauptsächlich zur Leseschicht. Agenten-Tracker sind näher an der Ausführung.

## Die Standardänderung vom 15. September 2026

Cloudflare kündigte außerdem eine geplante Standardänderung für neue Domänen an, die am 15. September 2026 Cloudflare beitreten. Für werbefinanzierte Seiten werden die Kategorien „Schulung“ und „Agent“ standardmäßig blockiert, während die Suche weiterhin standardmäßig zulässig ist.

Das Detail, das AEO-Teams nicht verpassen sollten: Mehrzweck-Tracker können von der restriktivsten ausgewählten Regel betroffen sein. Cloudflare weist ausdrücklich darauf hin, dass Crawler, die Suche mit Training kombinieren, blockiert werden können, wenn ein Websitebesitzer beschließt, Training zu blockieren.

Das stellt ein echtes Risiko für SEO dar. Ein Herausgeber versucht möglicherweise, das Training zu blockieren, schränkt jedoch versehentlich einen Crawler ein, der auch die Sucherkennung unterstützt.## Empfohlene Crawler-Richtlinie nach Seitentyp| Seitentyp | Suche | Agent | Ausbildung | Notizen |
|
---|
---:|
---:|
---:|
---|
| Öffentliche Homepage | Erlauben | Erlauben Sie im Allgemeinen | Entscheiden Sie sich für ein Geschäftsmodell | Halten Sie die Marke sichtbar |
| Produktseiten | Erlauben | Mit Ratenbegrenzung zulassen | Generell einschränken oder lizenzieren | Produktdaten müssen aktuell sein |
| Dokumentation | Erlauben | Erlauben | Entscheiden | Agenten benötigen Dokumente, um Aufgaben zu erledigen |
| Bezahlen | Einschränken | Nur mit strengen Kontrollen zulassen | Blockieren | Zahlungs- und Identitätsregeln sind wichtig |
| Bezahlte Forschung | Vielleicht Fragmente zulassen | Einschränken | Blockieren oder monetarisieren | Berücksichtigen Sie Zusammenfassungen und private Details |
| Interne Werkzeuge | Blockieren | Nur Authentifizierung | Blockieren | Kein öffentlicher Trackerwert |

Dies sollte mit [AI Crawlers and robots.txt](/es/docs/ai-crawlers-robots-txt/) und [Cloudflare AI Crawl Control](/es/docs/cloudflare-ai-crawl-control/) kombiniert werden.

## Checkliste für die Bereitstellung

1. Listen Sie die Arten hochwertiger öffentlicher Seiten auf.
2. Entscheiden Sie, welche Seiten Suchsichtbarkeit benötigen.
3. Entscheiden Sie, wo benutzergesteuerte Agenten agieren dürfen.
4. Trennen Sie den Einsatz von Schulungen vom Einsatz der Suche in der Politiksprache.
5. Überprüfen Sie die KI-Verkehrskontrollen von Cloudflare, wenn die Site hinter Cloudflare ausgeführt wird.
6. Überprüfen Sie, ob bestehende Firewall-Regeln bekannte KI-Referrer oder Agenten blockieren.
7. Überwachen Sie das Crawling-Volumen und die Verweise nach einer Änderung der Regeln.

Kopieren Sie nicht die Sperrliste eines Konkurrenten. Eine Medienseite, ein SaaS-Dokumentationszentrum, ein E-Commerce-Shop und ein API-Unternehmen haben unterschiedliche Anforderungen an die Präsenz und Monetarisierung.

## AEO-Fehler, den Sie vermeiden sollten

Der größte Fehler besteht darin, den „KI-Tracker“ als eine einzelne Absicht zu behandeln. Ein Browser-Agent, der versucht, ein Produkt für einen Benutzer zu kaufen, ist nicht dasselbe wie ein Trainings-Crawler, der Inhalte verwendet, um das Modell zu verbessern. Wenn beide durch eine Regel blockiert werden, schützt die Website möglicherweise Inhalte, verliert jedoch durch Agenten unterstützte Konvertierungen.

## Häufig gestellte Fragen

### Sollten alle Websites Suchcrawler zulassen?

Die meisten öffentlichen Websites sollten seriöse Suchcrawler auf indexierbaren Seiten zulassen. Ausnahmen sind private, kostenpflichtige, gesetzlich eingeschränkte oder geringwertige URLs.

### Sollten Agenten-Tracker erlaubt sein?

Nur dort, wo der Agent sichere Aufgaben erledigen kann, die dem Benutzer zugute kommen. Schreibgeschützte Seiten sind einfacher als Warenkörbe, Formulare, Kontoänderungen oder Einkäufe.

### Ist Trainings-Tracking schlecht für AEO?

Nicht automatisch. Einige Marken akzeptieren dies möglicherweise aus Sichtbarkeits- oder Lizenzgründen. Andere schränken es möglicherweise ein, da es keine direkten Referenzen erstellt.

### Kann Blockierungstraining SEO schaden?

Dies kann möglich sein, wenn ein Tracker mehreren Zwecken dient und die Infrastruktur die restriktivste Kategorie anwendet. Das Cloudflare-Update vom Juli 2026 macht dieses Risiko deutlicher.

## QuellenHauptquelle: [Cloudflare: Ihre Website, Ihre Regeln](https://blog.cloudflare.com/content-independence-day-ai-options/). Zugehöriger Implementierungskontext: [Cloudflare AI Crawl Control-Dokumente](https://developers.cloudflare.com/ai-crawl-control/).