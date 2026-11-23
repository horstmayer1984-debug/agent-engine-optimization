---
title: "Modelos, Conjuntos de Datos y Entornos de Prueba Locales para AEO"
metaTitle: "Modelos y Datasets para Pruebas Locales de AEO (2026)"
description: "Guía de modelos de embeddings, rerankers, LLMs locales y benchmarks académicos (GEO-bench, Mind2Web) para auditorías AEO."
summary: "Configuración de entornos locales para pruebas de AEO: embeddings multilingües, rerankers y datasets de evaluación."
keywords:
  - "modelos AEO"
  - "Qwen3"
  - "bge-m3"
  - "llama.cpp"
  - "MLX"
  - "GEO-bench"
  - "Mind2Web"
date: 2026-11-22
weight: 214
category: "Código Abierto"
---

# Modelos, Conjuntos de Datos y Entornos de Prueba Locales para AEO

Realizar auditorías locales de AEO permite comprobar qué información extraen los modelos sin depender de servicios de terceros en la nube.

> **Estado de la investigación:** 22 de noviembre de 2026. Datos oficiales de GitHub (Europe/Berlin). Descargas de Hugging Face no registradas.

---

## 1. Modelos de Embeddings
- **[Qwen3-Embedding-8B](https://huggingface.co/Qwen/Qwen3-Embedding-8B):** Medición de similitud semántica multilingüe.
- **[bge-m3](https://huggingface.co/BAAI/bge-m3):** Estándar de la industria para búsqueda densa y léxica.
- **[Qwen3-Embedding-0.6B](https://huggingface.co/Qwen/Qwen3-Embedding-0.6B):** Alternativa ligera.

---

## 2. Rerankers Neuronales
- **[Qwen3-Reranker-8B](https://huggingface.co/Qwen/Qwen3-Reranker-8B):** Reordenamiento de alta capacidad.
- **[bge-reranker-v2-m3](https://huggingface.co/BAAI/bge-reranker-v2-m3):** Evaluación de relevancia multilingüe.
- **[jina-reranker-v3](https://huggingface.co/jinaai/jina-reranker-v3):** *Aviso de licencia:* **Exclusivamente para uso no comercial.**

---

## 3. LLMs Locales y Runtimes
- **[Qwen3.8-27B MLX 8-bit](https://huggingface.co/mlx-community/Qwen3.8-27B-8bit):** Estimación de ~28 GB de pesos en memoria unificada (*estimación de investigación*).
- **[llama.cpp](https://github.com/ggml-org/llama.cpp):** Motor C/C++ (MIT, 135.988 estrellas).
- **[mlx](https://github.com/ml-explore/mlx) y [mlx-lm](https://github.com/ml-explore/mlx-lm):** Optimizado para chips Apple Silicon.

---

## 4. Datasets y Benchmarks
- **[GEO-bench](https://huggingface.co/datasets/GEO-Optim/geo-bench):** Dataset oficial del artículo de GEO.
- **[Mind2Web](https://github.com/OSU-NLP-Group/Mind2Web):** Evaluación de agentes en tareas web reales.
- **[WebArena](https://github.com/web-arena-x/webarena):** Entorno de pruebas para agentes web.
