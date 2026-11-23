---
title: "Schema.org- und JSON-LD-Tools im Vergleich für AEO"
metaTitle: "Schema.org & JSON-LD Tools für KI-Agents (2026)"
description: "Vergleich der besten Tools zur Modellierung, Validierung und Prüfung von Schema.org und JSON-LD: schemaorg, schema-dts, extruct und jsonld.js."
summary: "Praxisleitfaden für strukturierte Daten bei AEO: typisierte Schemas, Parser-Audits und Modellierung von Entitäten."
keywords:
  - "Schema.org"
  - "JSON-LD"
  - "schema-dts"
  - "extruct"
  - "jsonld.js"
  - "strukturierte Daten AEO"
date: 2026-11-22
weight: 211
category: "Open Source"
---

Strukturierte Daten im JSON-LD-Format sind das semantische Rückgrat der Agent Engine Optimization. Während LLMs Fließtext flexibel interpretieren, verlangen verlässliche Aktionen (Preise, Verfügbarkeit, Geschäftsidentitäten) eindeutige Schema.org-Daten.

Dieser Leitfaden vergleicht die wichtigsten Open-Source-Tools zur Erstellung, Typisierung und Prüfung strukturierter Daten.

> **Stand der Recherche:** 22. November 2026. GitHub-Sterne, Lizenzen und Zeitstempel (`pushed_at` in Europe/Berlin) stammen aus der offiziellen GitHub-API-Abfrage vom 22.11.2026.

---

## Ranking-Tabelle: Schema.org und JSON-LD

| Rang | Tool | Kategorie | Nutzen für AEO | Lizenz | Sterne (22.11.2026) | Letzte Aktivität (Europe/Berlin) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | [schemaorg](https://github.com/schemaorg/schemaorg) | Offizielles Vokabular | Das verbindliche Vokabular für maschinenlesbare Entitäten im Web. | Apache-2.0 | 6.316 | 20.11.2026, 15:36 |
| **2** | [schema-dts](https://github.com/google/schema-dts) | TypeScript-Typen | Ermöglicht typisiertes JSON-LD statt frei erfundener oder fehlerhafter Felder. | Apache-2.0 | 1.262 | 01.11.2026, 20:13 |
| **3** | [extruct](https://github.com/scrapinghub/extruct) | Parser-Audit | Zeigt transparent, welches Markup ein Parser tatsächlich ausliest. | BSD-3 (Recherche-Angabe) | nicht erfasst | nicht erfasst |
| **4** | [jsonld.js](https://github.com/digitalbazaar/jsonld.js) | JSON-LD-Verarbeitung | Referenz-Engine zur Prüfung, Erweiterung und Kompaktierung von JSON-LD. | siehe LICENSE im Repo prüfen | 1.819 | 04.03.2026, 17:43 |

---

## Kurzbeschreibung je Tool

### 1. schemaorg
- **Fokus:** Definition der weltweiten Vokabulare.
- **Nutzen für AEO:** Sämtliche Entitäten und Relationen, die KI-Agents verstehen, werden hier standardisiert.
- **Repository:** [github.com/schemaorg/schemaorg](https://github.com/schemaorg/schemaorg)

### 2. schema-dts (Google)
- **Fokus:** Typsicherheit bei der Softwareentwicklung.
- **Nutzen für AEO:** Verhindert Tippfehler in Schema-Feldern bereits zur Entwicklungszeit, indem JSON-LD-Objekte gegen vollständige TypeScript-Definitionen geprüft werden.
- **Repository:** [github.com/google/schema-dts](https://github.com/google/schema-dts)

### 3. extruct
- **Fokus:** Qualitätsprüfung im Live-Betrieb.
- **Nutzen für AEO:** Liest Webseiten ein und extrahiert eingebettete JSON-LD-, Microdata- und OpenGraph-Daten exakt so, wie es autonome Parser tun.
- **Repository:** [github.com/scrapinghub/extruct](https://github.com/scrapinghub/extruct)

### 4. jsonld.js
- **Fokus:** Graph-Transformation.
- **Nutzen für AEO:** Prüft und normalisiert komplexe Linked-Data-Graphen. *Hinweis zur Lizenz:* Im GitHub-Lizenzfeld am 22.11.2026 stand `NOASSERTION` (im Recherchetext als BSD-3 vermerkt; vor Weiterverwendung empfiehlt sich ein Blick in die LICENSE-Datei des Repos).
- **Repository:** [github.com/digitalbazaar/jsonld.js](https://github.com/digitalbazaar/jsonld.js)

---

## Für wen welches Tool?

- **Zum Schreiben und Modellieren:** Nutzen Sie **[schemaorg](https://github.com/schemaorg/schemaorg)** als Referenz und **[schema-dts](https://github.com/google/schema-dts)** in Ihrem TypeScript-/Build-Stack.
- **Zum Prüfen und Validieren:** Setzen Sie **[extruct](https://github.com/scrapinghub/extruct)** und **[jsonld.js](https://github.com/digitalbazaar/jsonld.js)** ein, um zu verifizieren, was Parser wirklich sehen.
- **Schlüssel-Entitäten für AEO:** Konzentrieren Sie sich vorrangig auf `Organization`, `Article`, `FAQPage` und `Product` mit stabilen `@id`-URIs.
