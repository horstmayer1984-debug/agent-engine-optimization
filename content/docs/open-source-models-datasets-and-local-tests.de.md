---
title: "Modelle, Datensätze und lokale Testumgebungen für AEO"
metaTitle: "Open-Source-Modelle, Datensätze & lokale AEO-Tests (2026)"
description: "Übersicht von Open-Source-Embeddings, Rerankern, lokalen LLMs (Qwen3, MLX, llama.cpp) und akademischen Benchmarks (GEO-bench, Mind2Web) für AEO."
summary: "Aufbau lokaler Testumgebungen für AEO: mehrsprachige Embeddings, Reranker, quantisierte Modelle auf Apple Silicon und Evaluations-Datensätze."
keywords:
  - "AEO Modelle"
  - "Qwen3"
  - "bge-m3"
  - "llama.cpp"
  - "MLX"
  - "GEO-bench"
  - "Mind2Web"
  - "lokale Tests"
date: 2026-11-22
weight: 214
category: "Open Source"
---

# Modelle, Datensätze und lokale Testumgebungen für AEO

Wer testen will, wie KI-Modelle und autonome Agents Webseiten erfassen, muss nicht zwingend teure Cloud-APIs nutzen. Leistungsfähige Open-Source-Modelle, Embeddings und lokale Inferenz-Engines ermöglichen präzise AEO-Analysen auf der eigenen Hardware.

> **Stand der Recherche:** 22. November 2026. GitHub-Sterne, Lizenzen und Zeitstempel (`pushed_at` in Europe/Berlin) stammen aus der offiziellen GitHub-API-Abfrage vom 22.11.2026. Downloadzahlen wurden in der Recherche nicht erfasst und werden daher nicht geschätzt.

---

## 1. Embeddings für semantische Passung

Embedding-Modelle wandeln Webtexte in Vektoren um und messen, wie präzise ein Seiteninhalt zu den typischen Fragestellungen von KI-Nutzern passt.

- **[Qwen3-Embedding-8B](https://huggingface.co/Qwen/Qwen3-Embedding-8B):** Leistungsfähiges Modell für mehrsprachige semantische Passungstests.
- **[bge-m3](https://huggingface.co/BAAI/bge-m3):** Etabliertes Multilingual-Embedding-Modell für dichte und lexikalische Vektorsuchen.
- **[Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B):** Ressourcenschonende Alternative für schnelle lokale Vorprüfungen.

---

## 2. Reranker zur Prüfung der Passage-Priorisierung

Reranker simulieren die zweite Stufe moderner Antwortsysteme: Sie bewerten, welcher Textabschnitt als Kontext für die finale Antwort ausgewählt wird.

- **[Qwen3-Reranker-8B](https://huggingface.co/Qwen/Qwen3-Reranker-8B):** Hochpräziser Reranker zur Validierung von Textbausteinen.
- **[bge-reranker-v2-m3](https://huggingface.co/BAAI/bge-reranker-v2-m3):** Etablierter mehrsprachiger Reranker mit verlässlicher Scoring-Qualität.
- **[jina-reranker-v3](https://huggingface.co/jinaai/jina-reranker-v3):** Starkes Modell.  
  *Wichtiger Lizenzhinweis:* **Nur für nicht-kommerzielle Nutzung lizenziert.** Darf ohne gesonderte Lizenzvereinbarung nicht in kommerziellen Produkten betrieben werden.

---

## 3. Lokale LLMs und Runtimes (z. B. auf Mac mit 64 GB RAM)

### Modelle
- **[Qwen3.8-27B in MLX 8-bit](https://huggingface.co/mlx-community/Qwen3.8-27B-8bit):** In der Recherche geschätzt rund 28 GB Gewichte (*Schätzung, nicht auf einem konkreten Rechner gemessen*); lässt bei 64 GB RAM ausreichend Raum für große Kontextfenster.
- **[Qwen3.6-35B-A3B als GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF):** Schnelle MoE-Alternative für zügige lokale Inferenz.

### Laufzeitumgebungen
- **[llama.cpp](https://github.com/ggml-org/llama.cpp):** C/C++-Referenz-Engine für lokales LLM-Serving (MIT, 135.988 Sterne, letzte Aktivität 22.11.2026, 09:08 Europe/Berlin).
- **[mlx](https://github.com/ml-explore/mlx):** Hochoptimiertes Framework für Apple Silicon (MIT, 29.241 Sterne, 22.11.2026, 09:03 Europe/Berlin).
- **[mlx-lm](https://github.com/ml-explore/mlx-lm):** Python-Laufzeitumgebung für MLX (MIT, 7.729 Sterne, 21.11.2026, 05:00 Europe/Berlin).

---

## 4. Datensätze und akademische Benchmarks

- **[GEO-bench](https://huggingface.co/datasets/GEO-Optim/geo-bench):** Der offizielle Datensatz zum wegweisenden GEO-Forschungspapier.
- **[Mind2Web](https://huggingface.co/datasets/osunlp/Mind2Web):** Maßstab für Web-Agents auf echten Webseiten ([GitHub Repo](https://github.com/OSU-NLP-Group/Mind2Web), MIT, 1.037 Sterne, 05.11.2025, 01:38 Europe/Berlin).
- **[Online-Mind2Web](https://huggingface.co/datasets/osunlp/Online-Mind2Web):** Interaktiver Benchmark ([GitHub Repo](https://github.com/OSU-NLP-Group/Online-Mind2Web), MIT, 214 Sterne, 04.11.2026, 20:53 Europe/Berlin).
- **[Mind2Web-2](https://huggingface.co/datasets/osunlp/Mind2Web-2):** Aktualisierter Benchmark ([GitHub Repo](https://github.com/OSU-NLP-Group/Mind2Web-2), MIT, 115 Sterne, 25.09.2026, 03:50 Europe/Berlin).
- **[WebArena](https://github.com/web-arena-x/webarena):** Komplexe Testumgebung für Web-Agents (Apache-2.0, 1.645 Sterne, 26.11.2025, 22:16 Europe/Berlin).

---

## Für wen welches Tool?

- **Für semantische Tests:** Starten Sie mit **[bge-m3](https://huggingface.co/BAAI/bge-m3)** und einem Reranker, um zu messen, wie Textabschnitte auf Nutzeranfragen reagieren.
- **Für lokale Textsynthese:** Betreiben Sie **Qwen3.8-27B (MLX)** oder **Qwen3.6-35B (GGUF)** über **[llama.cpp](https://github.com/ggml-org/llama.cpp)**.
- **Zur Methodeneinordnung:** Nutzen Sie **GEO-bench** und **Mind2Web** zur Beurteilung von Agenten-Fähigkeiten, aber verwechseln Sie akademische Benchmarks nicht mit Rankings für die eigene Domain.
