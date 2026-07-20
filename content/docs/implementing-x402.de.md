---
title: "So implementieren Sie x402 auf Ihrer Website oder Zahlungs-API."
metaTitle: "Implementierung von Agentenzahlungen x402."
date: 2026-04-12
weight: 71
category: "Architecture"
description: "Schritt-für-Schritt-Anleitung zum Hinzufügen von x402-Zahlungsmiddleware zu Ihrer Website oder API. Deckt das 402-Antwortformat, die Zahlungsvalidierung und die Integration mit llms.txt ab."
metaDescription: "Agregue middleware de pago x402 con respuestas 402, validación, integración de llms.txt y tarjetas de agente para pagos de agentes de IA."
summary: "x402 macht Ihre API für den Agenten sofort monetarisierbar. Wenn ein Agent Inhalte oder Computer anfordert, gibt Ihr Server 402 zurück, der Agent zahlt mit USDC und erhält Zugriff. Hier ist der Implementierungsleitfaden."
keywords:
  - "x402 implementieren"
  - "x402-Middleware"
  - "HTTP 402-Implementierung"
  - "Agenten-Zahlungs-API"
  - "x402-Entwicklerhandbuch"
  - "USDC-Mikrozahlungs-API"
---
Durch die Implementierung von x402 können Agenten Ihre Website oder API sofort monetarisieren. Wenn ein KI-Agent Inhalte oder Berechnungen anfordert, gibt sein Server HTTP 402 mit strukturierten Zahlungsbedingungen zurück. Der Agent zahlt mit USDC. Der Zugang wird gewährt. Alles in einem zustandslosen HTTP-Roundtrip.

## Umsetzung in fünf Schritten

### Schritt 1: Middleware hinzufügen, die die Zahlung überprüft

Fügen Sie Middleware vor Ihren geschützten Endpunkten ein. Prüft den X-PAYMENT-Header in eingehenden Anfragen. Wenn der Header vorhanden und gültig ist, wird die Anfrage fortgesetzt. Wenn es fehlt oder nicht ausreicht, gibt die Middleware eine 402-Antwort zurück.

Diese Middleware sitzt zwischen Ihrem Webserver und Ihrer Geschäftslogik. Es ändert nichts an der internen Funktionsweise Ihrer Endpunkte.

### Schritt 2: Strukturieren Sie die 402-Antwort

Wenn die Zahlung ausbleibt, wird ein 402-Statuscode mit einem JSON-Text zurückgegeben, der Folgendes enthält: Preis (der erforderliche Betrag), Währung (USDC), Kette (die zu zahlende Blockchain, Basis ist die Standardeinstellung), Zahlungsempfänger (Ihre Wallet-Adresse), Beschreibung (worauf die Zahlung Zugriff gewährt) und Ablauf (wie lange die Zahlungsbedingungen gültig bleiben).

Eine strukturierte Reaktion ermöglicht es Agenten, automatische Zahlungen vorzunehmen. Ein einfacher 402 ohne diesen JSON-Body gibt dem Agenten nichts, womit er arbeiten kann.

### Schritt 3: Eingegangene Zahlungen validieren

Wenn ein Agent es erneut mit einem X-PAYMENT-Header versucht, validieren Sie die On-Chain-Zahlung. Verwenden Sie das Coinbase Developer Platform SDK oder einen direkten RPC-Aufruf, um zu überprüfen, ob die Zahlung an die richtige Adresse für den richtigen Betrag in der richtigen Kette erfolgt ist.

Die Validierung muss innerhalb des Anforderungslebenszyklus abgeschlossen sein. Lassen Sie den Agenten nicht auf einen separaten Bestätigungsfluss warten.

### Schritt 4: Zugriff gewähren und Transaktion aufzeichnen

Sobald die Zahlung bestätigt ist, verarbeiten Sie die ursprüngliche Anfrage normal und senden Sie die Antwort zurück. Zeichnen Sie die Transaktion auf: Agenten-ID, gezahlter Betrag, zugegriffener Endpunkt, zurückgegebene Antwort, Zeitstempel.

Diese Protokolle speisen Ihre [Feedbackschleifen](/es/docs/agent-feedback-loops/) und Ihre Umsatzanalyse.

### Schritt 5 – Veröffentlichen Sie Ihre x402-Endpunkte in Erkennungsdateien

Fügen Sie Ihre kostenpflichtigen Terminals mit Preisinformationen zu Ihrer llms.txt hinzu. Fügen Sie sie unter Angabe der Zahlungsanforderung in Ihre agent-card.json-Funktionsliste ein. Wenn Sie über einen MCP-Server verfügen, fügen Sie den entsprechenden Toolbeschreibungen das Feld payment_required hinzu.

Dadurch wird sichergestellt, dass Agenten nicht nur erfahren, was Ihre Website leisten kann, sondern auch, wie viel die Nutzung der einzelnen Funktionen kostet.

## Kombination von x402 mit Kartenzahlungen

Mit Nevermined Agent Card Payments (gestartet am 9. April 2026) können Agenten mit delegierter Vollmacht von Visa oder Mastercard bezahlen, während Händler die Abrechnung über Standard-Zahlungsabwickler wie Stripe oder Adyen erhalten. Dieser hybride Ansatz ermöglicht es Ihnen, Krypto-Mikrozahlungen (für Agenten mit Wallets) und herkömmliche Kartenzahlungen (für Agenten mit delegierter Kartenautorität) über denselben Endpunkt zu akzeptieren.

##Vergleich: Traditionelle API-Monetarisierung vs. x402

| Methode | Rüstzeit | Agentenreibung | Erlösmodell | Mindestzahlung |
|
---|
---|
---|
---|
---|
| API-Schlüssel mit Abonnements | Tage | Stopp (Kontoerstellung) | Monatliche Raten | Dollar pro Monat |
| x402 | Stunden | Null | Zahlung pro Anfrage | Bruchteile eines Cent |

## Häufige FehlerRückgabe eines einfachen 402 ohne den strukturierten JSON-Body. Agenten können keine automatischen Zahlungen durchführen, wenn sie keine strukturierten Zahlungsbedingungen erhalten. Geben Sie immer die vollständige JSON-Spezifikation an.

Veröffentlichen Sie keine x402-Endpunkte in Erkennungsdateien. Wenn Agenten nicht wissen, dass ein Terminal eine Zahlung erfordert, bevor sie es anrufen, fühlt sich die 402-Antwort eher wie ein Fehler als wie eine Transaktionsmöglichkeit an.

Für Mikrozahlungs-Anwendungsfälle sind die Preise zu hoch angesetzt. Die Leistung von x402 ermöglicht Zahlungen, die zuvor zu klein waren, um verarbeitet zu werden. Eine Datenabfrage, die 5 $ kostet, erhält weniger Agentenanrufe als eine, die 0,01 $ kostet und deren Volumen zunimmt.

Die [x402-Übersicht](/es/docs/x402-agent-payments/) erläutert den strategischen Kontext. Die [Agent-Ready Web Applications Checklist](/es/docs/agent-ready-web-apps/) deckt die umfassendere Einrichtung für Entwickler ab.

---

## Häufig gestellte Fragen

**Wie lange dauert die x402-Implementierung?**
Einfache Middleware für einen einzelnen Endpunkt dauert 1–2 Stunden. Durch das Hinzufügen der Zahlungsvalidierung und Registrierung werden weitere 2–4 Stunden benötigt. Die vollständige Integration mit llms.txt und Agent Cards dauert einen Tag.

**Für welche Programmiersprachen ist x402-Middleware verfügbar?**
Node.js, Python, Go und Cloudflare Workers verfügen alle über vorgefertigte Middleware. Das Protokoll ist einfach genug, um es in jeder Sprache zu implementieren, die HTTP-Antworten zurückgeben und RPC-Aufrufe durchführen kann.

**Benötige ich eine Krypto-Wallet?**
Ja, um Zahlungen zu erhalten. Eine einfache USDC-Wallet auf Base reicht aus. Sie können erhaltene USDC über jede Börse oder jeden Zahlungsabwickler, der die Abwicklung mit Stablecoins unterstützt, in Fiat umwandeln.

**Kann ich unterschiedliche Preise für verschiedene Endpunkte festlegen?**
Ja. Jeder Endpunkt kann seine eigene 402-Antwort mit unterschiedlichen Preisen zurückgeben. Eine einfache Datenabfrage kann 0,001 US-Dollar kosten, während eine komplexe Berechnung 1 US-Dollar kostet.

**Was passiert, wenn ein Agent x402 nicht unterstützt?**
Der Agent erhält eine 402-Antwort, die er nicht verarbeiten kann, und fährt fort. Sie können alternative Zugriffsmethoden (API-Schlüssel, Abonnements) für Nicht-x402-Kunden anbieten und dabei x402 als primären Zahlungspfad des Agenten beibehalten.

---*Dieser Artikel behandelt Zahlungsprotokolle und Kryptowährungsinfrastruktur nur zu Bildungs- und Informationszwecken. Es handelt sich nicht um eine Finanzberatung. Die vollständigen Bedingungen finden Sie in unserem [Rechtlichen Hinweis](/es/docs/disclaimer/).*

## Primäre Referenzen

* [Coinbase x402-Dokumentation](https://docs.cdp.coinbase.com/x402/welcome)
* [x402-Spezifikations-Repository](https://github.com/x402-foundation/x402)