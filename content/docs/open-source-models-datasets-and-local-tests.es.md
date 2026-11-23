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

*Contexto de prueba:* evaluación en una estación de trabajo estándar (por ejemplo, Apple Mac Studio con 64 GB de memoria unificada).

### Modelos de lenguaje cuantizados
- **[Qwen3.8-27B MLX 8-bit](https://huggingface.co/mlx-community/Qwen3.8-27B-8bit):** Estimación de ~28 GB de pesos en memoria unificada (*estimación de investigación, no medida en hardware físico*), con margen en una configuración de 64 GB de memoria unificada para ventanas de contexto extendidas.
- **[Qwen3.6-35B-A3B en GGUF](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF):** Variante cuantizada Mixture-of-Agents, con un caudal superior de tokens por segundo en estaciones de trabajo locales.

### Motores de ejecución
- **[llama.cpp](https://github.com/ggml-org/llama.cpp):** Motor C/C++ multiplataforma (MIT, 135.988 estrellas, última actividad el 22.11.2026, 09:08 Europe/Berlin).
- **[mlx](https://github.com/ml-explore/mlx):** Marco de arrays de alto rendimiento para Apple Silicon (MIT, 29.241 estrellas, última actividad el 22.11.2026, 09:03 Europe/Berlin).
- **[mlx-lm](https://github.com/ml-explore/mlx-lm):** Runtime en Python para servir y ajustar LLMs con MLX (MIT, 7.729 estrellas, última actividad el 21.11.2026, 05:00 Europe/Berlin).

---

## 4. Datasets y Benchmarks
- **[GEO-bench](https://huggingface.co/datasets/GEO-Optim/geo-bench):** Dataset oficial del artículo de GEO.
- **[Mind2Web](https://github.com/OSU-NLP-Group/Mind2Web):** Evaluación de agentes en tareas web reales. Benchmark multitarea de agentes web generalistas en sitios en producción ([conjunto en Hugging Face](https://huggingface.co/datasets/osunlp/Mind2Web); MIT, 1.037 estrellas, 05.11.2025, 01:38 Europe/Berlin).
- **[Online-Mind2Web](https://huggingface.co/datasets/osunlp/Online-Mind2Web):** Benchmark web dinámico ([repositorio](https://github.com/OSU-NLP-Group/Online-Mind2Web), MIT, 214 estrellas, 04.11.2026, 20:53 Europe/Berlin).
- **[Mind2Web-2](https://huggingface.co/datasets/osunlp/Mind2Web-2):** Benchmark de agentes web de segunda generación ([repositorio](https://github.com/OSU-NLP-Group/Mind2Web-2), MIT, 115 estrellas, 25.09.2026, 03:50 Europe/Berlin).
- **[WebArena](https://github.com/web-arena-x/webarena):** Entorno de pruebas para agentes web, de extremo a extremo y realista (Apache-2.0, 1.645 estrellas, 26.11.2025, 22:16 Europe/Berlin).

---

## Guía de decisión: cómo montar un entorno de prueba de AEO

- **Para auditar la alineación semántica:** Ejecute **[bge-m3](https://huggingface.co/BAAI/bge-m3)** y **[bge-reranker-v2-m3](https://huggingface.co/BAAI/bge-reranker-v2-m3)** a fin de puntuar en qué medida los fragmentos de la página coinciden con las consultas de los clientes.
- **Para probar la extracción local de agentes:** Aloje **Qwen3.8-27B (MLX de 8 bits)** mediante **[mlx-lm](https://github.com/ml-explore/mlx-lm)** o **llama.cpp**, y compruebe si los modelos locales interpretan con precisión tablas y esquemas, sin latencia de la nube.
- **Interpretación de los benchmarks:** Utilice **GEO-bench** y **Mind2Web** para comprender las capacidades generales de los modelos, pero evite tratar las puntuaciones generalizadas como garantías de ranking específicas del dominio.
