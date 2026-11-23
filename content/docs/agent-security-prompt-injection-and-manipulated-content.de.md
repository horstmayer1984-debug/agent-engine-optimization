---
title: "Prompt Injection und manipulierte Inhalte: Schutz der Lese-Ebene für KI-Agents"
metaTitle: "Prompt Injection bei AEO: Black-Hat-GEO und Tool Poisoning"
description: "Wie versteckter Inhalt, indirekte Prompt Injection und MCP Tool Poisoning KI-Agents manipulieren und was niemals im Seitencode stehen darf."
summary: "Detaillierte Analyse zu Prompt Injection: Unit 42 zu Black-Hat-GEO, 1Password zu Tool Poisoning, empirische Erfolgsraten und IBM LLMON."
keywords:
  - "Prompt Injection"
  - "Black-Hat-GEO"
  - "MCP Tool Poisoning"
  - "OWASP LLM01"
  - "IBM LLMON"
  - "GEOHunter"
date: 2026-11-22
weight: 204
category: "Sicherheit"
---

# Prompt Injection und manipulierte Inhalte: Schutz der Lese-Ebene für KI-Agents

Wenn autonome KI-Agents Websites erfassen, lesen sie nicht nur Text, sondern interpretieren ihn als Handlungsanweisung. Dadurch entsteht ein gravierendes Risiko: **indirekte Prompt Injection**, bei der versteckte Inhalte im Seitencode oder manipulierte Tool-Beschreibungen die Entscheidungen von Agents manipulieren.

> **Stand der Recherche:** 22. November 2026. Alle genannten Zahlen, Zeiten (Europe/Berlin) und Quellen basieren auf verifizierten Forschungsdaten.

---

## Aktuelle Forschungs- und Vorfallslage (Recherche 22. November 2026)

### 1. Black-Hat-GEO auf 26 gefälschten Trading-Seiten
Unit 42 von Palo Alto Networks deckte eine aktive Kampagne auf: Unsichtbare Textpassagen (u. a. via `display: none` oder winzige Schriftgrößen) wiesen Agents an, Nutzer ausschließlich auf gefälschte Plattformen umzuleiten. Unit 42 stuft dies als webbasierte indirekte Prompt Injection bzw. Black-Hat-GEO ein.

- **Post:** [@Unit42_Intel](https://x.com/Unit42_Intel/status/2120264510350991832), 10.11.2026, 22:17 Europe/Berlin.
- **IOC-Notiz:** [Unit 42 Timely Threat Intel, 2026-11-06-IDPI-campaign](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-11-06-IDPI-campaign.txt).
- **Forschungsbericht:** [Fooling AI Agents: Web-Based Indirect Prompt Injection Observed in the Wild](https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/).

### 2. Tool Poisoning als neues Lieferkettenrisiko
Um einen KI-Agenten zu kompromittieren, ist oft kein schädlicher Programmcode erforderlich: Es genügt, die textuelle Beschreibung eines MCP-Tools so zu manipulieren, dass das Modell vertrauliche Daten ausleitet oder unerwünschte Aktionen ausführt.

- **Experten-Thread:** [@1PasswordDev](https://x.com/1PasswordDev/status/2122472408619852202), 17.11.2026, 00:30 Europe/Berlin (rund 132.000 Impressionen); vertiefend zu Tool Poisoning: [https://x.com/1PasswordDev/status/2122473198147313902](https://x.com/1PasswordDev/status/2122473198147313902).
- **Leitfäden:** [1Password: Where MCP fits and where it doesn’t](https://1password.com/blog/where-mcp-fits-and-where-it-doesnt) sowie das [OWASP MCP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html).

### 3. Empirische Studie zur Erfolgsrate von Tool Poisoning
In einer Testreihe mit zwölf Agent-Frameworks war der Angriff in **22,9 % aller Fälle erfolgreich**. Keines der zwölf getesteten Frameworks verfügte über eine eingebaute Abwehr gegen manipulierte Tool-Beschreibungen.

- **Wissenschaftliche Publikation:** [MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study, arXiv:2611.03555](https://arxiv.org/abs/2611.03555).

### 4. IBM trennt Befehle von Daten (LLMON)
Mit den Modellen Granite 4.1 3B und 8B erprobt IBM die Auszeichnungssprache LLMON. Gelesene Inhalte sollen strikt als passive Nutzdaten und nicht als ausführbare Befehle interpretiert werden. IBM betont, dass dies ein erlerntes Verhalten darstellt und kein mathematisch garantiertes Sicherheitsmerkmal ist.

- **Publikation:** [LLMON: An LLM-Native Markup Language, now in Granite 4.1](https://huggingface.co/blog/ibm-granite/llmon-an-llm-native-markup-language-now-in-granite).

### 5. Prompt Injection bleibt ungelöst (OWASP Platz 1)
Prompt Injection belegt weiterhin unangefochten Platz 1 der [OWASP GenAI LLM Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/) (LLM01). Beliebte Verstecke sind weißer Text auf weißem Grund ([@Pksingh900](https://x.com/Pksingh900/status/2116788637019124196), 1.11.2026, 08:05 Europe/Berlin), Alt-Texte, PDFs und Kalendereinladungen.

### 6. Erkennung in freier Wildbahn und Richtlinien der Suchmaschinen
- **Praxisbericht:** Eine Nutzerin beobachtete, dass ihr Agent manipulierte Hinweise auf einer Slack-Seite erkannte und ignorierte ([@NoemiTitarenco](https://x.com/NoemiTitarenco/status/2119947195860361318), 10.11.2026, 01:16 Europe/Berlin, Einzelbeobachtung).
- **Google Richtlinien:** Google verbietet versteckten Text und Cloaking ausdrücklich in den [Google Search Spam Policies](https://developers.google.com/search/docs/essentials/spam-policies).

---

## Geplante Artikel (Demnächst)

- *Indirekte Prompt Injection: Wie versteckter Text Agents umlenkt* (Demnächst)
- *Tool Poisoning bei MCP: Wenn eine Tool-Beschreibung zum Angriff wird* (Demnächst)
- *Saubere Inhalte für Agents: Was nicht im Seitencode stehen darf* (Demnächst)
- *Black-Hat-GEO ist Prompt Injection* (Demnächst)
- *Tool-Beschreibungen wie Abhängigkeiten im Code prüfen* (Demnächst)
- *GEOHunter: Wie bezahlte GEO-Netzwerke funktionieren (arXiv:2611.26564)* (Demnächst)
