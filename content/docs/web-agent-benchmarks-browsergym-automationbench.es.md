---
title: "BrowserGym y AutomationBench: puntos de referencia de agentes."
metaTitle: "BrowserGym y AutomationBench para AEO."
date: 2026-06-28
weight: 185
category: "Analysis"
description: "BrowserGym y AutomationBench muestran cómo se evalúan los agentes web y API. Aprenda cómo convertir esas lecciones en pruebas prácticas de AEO."
summary: "Una guía práctica para BrowserGym y AutomationBench desde una perspectiva AEO, que cubre tareas de agentes web, flujos de trabajo de API, comprobaciones de políticas y éxito de tareas."
keywords:
  - NavegadorAutomatización de gimnasioBanco
  - puntos de referencia del agente web
  - Pruebas comparativas AEO
  - Comparativa del agente API
  - evaluación del agente del navegador
---
# BrowserGym y AutomationBench

BrowserGym y AutomationBench son importantes para AEO porque muestran cómo se evalúa a los agentes: no por las páginas vistas, sino por si completan las tareas. Los sitios web que quieran trabajar con agentes deben probar flujos de trabajo reales, incluida la navegación, el descubrimiento de API, el cumplimiento de políticas y la verificación del estado final.

## Qué cara de abrazo surgió

La búsqueda de artículos de Hugging Face surgió [The BrowserGym Ecosystem for Web Agent Research](https://hf.co/papers/2412.05467) y [AutomationBench](https://hf.co/papers/2604.18934) como artículos relevantes para agentes web y agentes que utilizan herramientas.

BrowserGym se centra en entornos estandarizados para evaluar agentes web. AutomationBench se centra en la orquestación del flujo de trabajo entre aplicaciones a través de API REST, incluido el descubrimiento, el cumplimiento de políticas y la precisión de los datos.

Esa división se corresponde bien con AEO:

| Punto de referencia | Lección AEO |
|
---|
---|
| NavegadorGimnasio | Pruebe si los agentes pueden utilizar sus flujos web visibles. |
| Banco de automatización | Pruebe si los agentes pueden descubrir y ejecutar flujos de trabajo API. |

## Por qué los puntos de referencia son mejores que el tráfico solo

Las referencias de IA y las búsquedas de agentes son útiles, pero no demuestran el éxito de la tarea.

| Métrica débil | Métrica AEO más sólida |
|
---|
---|
| Vista de página | Tarea completada |
| Profundidad de desplazamiento | Transición de estado correcta |
| Referente de IA | Conversión o resultado verificado |
| Agente de usuario de bot | Llamada de herramienta exitosa |
| Tiempo en la página | Finalización conforme a las políticas |

Para un seguimiento más amplio, consulte [KPI de AEO](/es/docs/aeo-kpis-measurement/) y [Tráfico web del agente de IA en 2026](/es/docs/ai-agent-web-traffic-2026/).

## Cree un pequeño punto de referencia para su sitio

No necesita un laboratorio de investigación para comenzar.

1. Elija cinco tareas de alto valor.
2. Definir el estado final correcto para cada tarea.
3. Ejecute las tareas con un agente de navegador y un agente que utilice herramientas siempre que sea posible.
4. Registrar fracasos.
5. Corrija etiquetas, documentos, esquemas, API, políticas o confirmaciones.
6. Repetir mensualmente.

Tareas de ejemplo:

| Tipo de sitio | Tarea de referencia |
|
---|
---|
| Comercio electrónico | Encuentre un producto, consulte la política de devoluciones, prepare un carrito. |
| SaaS | Compara planes y solicita una demostración. |
| Portal de desarrolladores | Encuentre documentos de endpoints y realice una llamada API de prueba. |
| Sitio de soporte | Dirija un problema de facturación al canal de soporte correcto. |
| Sitio de viajes | Encuentre disponibilidad reembolsable bajo restricciones de política. |

## Qué medir

1. Tasa de finalización.
2. Tasa de acciones incorrectas.
3. Tasa de infracción de políticas.
4. Número de intentos de recuperación.
5. Errores de contexto faltantes.
6. Traspasos de aprobación humana.
7. Verificación del estado final.

Esto se vincula directamente con [Parámetros de evaluación del agente](/es/docs/agent-evaluation-benchmarks/) y [Observabilidad y barreras de protección del agente](/es/docs/agent-observability-guardrails/).

## Preguntas frecuentes### ¿Son BrowserGym y AutomationBench herramientas SEO?

No. Son puntos de referencia de evaluación de agentes. Son importantes para AEO porque AEO se trata del éxito de las tareas de los agentes, no solo de la visibilidad de búsqueda.

### ¿Qué estilo de referencia deberían copiar primero los sitios web?

Los sitios web con formularios y flujos de interfaz de usuario deben comenzar con pruebas de agente de navegador. Las empresas que utilizan muchas API también deberían probar las herramientas y los flujos de trabajo de API.

### ¿Qué es un estado aprobado o reprobado?

Un estado de aprobación es un resultado verificable, como un ticket creado, una cotización correcta, una respuesta API válida, un carrito preparado o un borrador de reserva confirmado.

### ¿Con qué frecuencia se deben ejecutar las evaluaciones comparativas de los agentes?

Mensualmente es suficiente para la mayoría de los sitios. Ejecútelo con más frecuencia cuando los documentos de pago, precios, soporte o API cambien con frecuencia.

## Fuentes

Fuentes principales: [documento de BrowserGym](https://hf.co/papers/2412.05467), [documento de AutomationBench](https://hf.co/papers/2604.18934), [documento de AgentRewardBench](https://hf.co/papers/2504.08942) y [documento de ST-WebAgentBench](https://hf.co/papers/2410.06703).