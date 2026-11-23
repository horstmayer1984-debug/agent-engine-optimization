---
title: "Las mejores herramientas de código abierto para llms.txt: Comparativa"
metaTitle: "Mejores herramientas llms.txt Open Source (2026)"
description: "Ranking de herramientas open source para generar, auditar e indexar archivos llms.txt según utilidad AEO, actividad y estrellas de GitHub."
summary: "Comparativa de herramientas para llms.txt: claude-seo, OpenGSO, especificación de referencia, plugins de VitePress y Starlight."
keywords:
  - "llms.txt"
  - "claude-seo"
  - "OpenGSO"
  - "herramientas AEO"
  - "código abierto"
date: 2026-11-22
weight: 209
category: "Código Abierto"
---

El archivo `/llms.txt` permite que los agentes de IA indexen y comprendan la documentación técnica de un sitio web sin procesar código innecesario.

> **Estado de la investigación:** 22 de noviembre de 2026. Datos consultados vía API de GitHub (Europe/Berlin).

---

## Tabla Comparativa: Herramientas llms.txt

| Rango | Herramienta | Categoría | Utilidad para AEO | Licencia | Estrellas (22.11.2026) | Última Actividad (Europe/Berlin) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | [claude-seo](https://github.com/AgriciDaniel/claude-seo) | Skill para Claude Code | Audita páginas para GEO, AEO y compatibilidad con agentes. | MIT | 31.471 | 16.11.2026, 07:16 |
| **2** | [OpenGSO](https://github.com/sherwinvishesh/OpenGSO) | Auditoría y Generador | Evalúa un sitio (0–100) y genera `llms.txt`, `robots.txt` y sitemap. | Apache-2.0 | 398 | 09.11.2026, 16:17 |
| **3** | [Especificación llms.txt](https://github.com/AnswerDotAI/llms-txt) | Especificación oficial | Referencia autoritativa de estructura para `llms.txt`. | Apache-2.0 | 2.699 | 24.09.2026, 19:21 |
| **4** | [vitepress-plugin-llms](https://github.com/okineadev/vitepress-plugin-llms) | Plugin generador | Genera `llms.txt` para sitios VitePress. | MIT | 418 | 10.11.2026, 15:20 |
| **5** | [starlight-llms-txt](https://github.com/delucis/starlight-llms-txt) | Plugin generador | Genera `llms.txt` para Astro Starlight. | MIT | 118 | 18.11.2026, 01:12 |
| **6** | [llms-txt-hub](https://github.com/thedaviddias/llms-txt-hub) | Directorio público | Colección de sitios que adoptan `llms.txt`. | NOASSERTION | 930 | 22.11.2026, 06:05 |

---

## Perfiles detallados

### 1. claude-seo
- **Enfoque:** Integración en el flujo de trabajo del desarrollador.
- **Por qué importa para AEO:** Integrado como habilidad de auditoría interactiva en Claude Code, `claude-seo` valida los cambios locales de código para la optimización de motores generativos (GEO) y la Agent Engine Optimization (AEO) antes de enviar el código a producción.
- **Repositorio:** [github.com/AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)

### 2. OpenGSO
- **Enfoque:** Auditorías automatizadas e integrales de preparación.
- **Por qué importa para AEO:** Genera una puntuación determinista de preparación (0–100) en las páginas y, al mismo tiempo, compone configuraciones válidas de `llms.txt`, `robots.txt` y sitemaps XML.
- **Repositorio:** [github.com/sherwinvishesh/OpenGSO](https://github.com/sherwinvishesh/OpenGSO)

### 3. Especificación llms.txt (AnswerDotAI)
- **Enfoque:** Estándar fundacional.
- **Por qué importa para AEO:** Define las secciones Markdown estándar (`# Project Name`, bloque `> Summary`, documentos opcionales frente a documentos principales). Debe consultarse antes de implementar canalizaciones de generación propias.
- **Repositorio:** [github.com/AnswerDotAI/llms-txt](https://github.com/AnswerDotAI/llms-txt)

### 4. vitepress-plugin-llms y starlight-llms-txt
- **Enfoque:** Integración nativa con generadores de sitios estáticos.
- **Por qué importa para AEO:** Plugins de configuración cero para VitePress y Astro Starlight que agrupan las jerarquías de documentación en puntos de acceso canónicos legibles por máquinas durante los pasos habituales de compilación.
- **Repositorios:** [github.com/okineadev/vitepress-plugin-llms](https://github.com/okineadev/vitepress-plugin-llms) y [github.com/delucis/starlight-llms-txt](https://github.com/delucis/starlight-llms-txt)

### 5. llms-txt-hub
- **Enfoque:** Descubrimiento del ecosistema.
- **Por qué importa para AEO:** Sirve como índice de referencia para observar cómo los principales proyectos de código abierto estructuran sus archivos públicos `llms.txt`. El campo de licencia de GitHub figura como `NOASSERTION`.
- **Repositorio:** [github.com/thedaviddias/llms-txt-hub](https://github.com/thedaviddias/llms-txt-hub)

---

## ¿Para quién es cada herramienta?

- **Punto de partida:** Consulte la **[especificación oficial](https://github.com/AnswerDotAI/llms-txt)** antes de implementar generadores propios.
- **Para VitePress o Starlight:** Utilice los plugins respectivos en su pipeline de compilación.
- **Para auditorías con puntuación:** **[OpenGSO](https://github.com/sherwinvishesh/OpenGSO)** ofrece scoring y generación completa.
- **Para desarrollo con Claude Code:** Utilice **[claude-seo](https://github.com/AgriciDaniel/claude-seo)** en su IDE.
- **Para investigación y comparación:** Explore **[llms-txt-hub](https://github.com/thedaviddias/llms-txt-hub)** como referencia de cómo se estructuran archivos `llms.txt` en dominios en producción.
