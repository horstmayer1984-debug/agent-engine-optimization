---
title: "Marcos de referencia y evaluación de agentes: AEO basado."
metaTitle: "Puntos de referencia de evaluación de agentes para AEO basado."
date: 2026-04-12
weight: 84
category: "Guide"
description: "Los marcos de evaluación de agentes miden la autonomía, la precisión, el costo, la latencia y el éxito de las tareas durante todo el ciclo de vida. Haga."
metaDescription: "Utilice puntos de referencia de evaluación de agentes para medir la autonomía, la precisión, el costo, la latencia y el éxito de las tareas durante todo."
summary: "La evaluación del desempeño de los agentes va más allá de la precisión. Los marcos modernos miden la autonomía, la rentabilidad, la latencia y la finalización de tareas en el mundo real. A continuación se explica cómo construir una práctica de evaluación."
keywords:
  - marcos de evaluación de agentes
  - Puntos de referencia de agentes de IA
  - prueba de agente AEO
  - medición de la precisión del agente
  - Evaluaciones de LangChain
  - métricas de rendimiento del agente
---
Los marcos de evaluación de agentes miden no solo la precisión sino también la autonomía, el costo, la latencia y el éxito de las tareas en el mundo real durante todo el ciclo de vida del agente. Convierten AEO de conjeturas en optimización basada en datos al mostrar exactamente dónde tienen éxito y dónde fallan las interacciones de los agentes con su sitio.

## Por qué la evaluación es importante para los AEO

Cuando un agente interactúa con su sitio, el resultado depende tanto de las capacidades del agente como de la estructura de su sitio. Los marcos de evaluación le ayudan a separar los dos. Si los agentes constantemente no logran extraer sus precios, el problema son sus datos estructurados. Si los agentes extraen correctamente pero se recomienda el producto incorrecto, el problema es el mapeo de su entidad.

Sin evaluación no se puede hacer esa distinción. Cada fracaso parece igual desde fuera.

## Las cinco dimensiones de la evaluación del agente

### Precisión

¿El agente extrae información correcta de su sitio? Compare los datos extraídos por el agente con su fuente de verdad. Los nombres de los productos, los precios, la disponibilidad, las especificaciones y los términos de la política deben coincidir exactamente.

Mida la precisión por página y por campo de datos. Un sitio puede tener un 98 por ciento de precisión en los nombres de los productos, pero sólo un 75 por ciento de precisión en las políticas de envío. Esa especificidad le dice dónde enfocar la mejora.

### Autonomía

¿Cuántos pasos puede completar el agente sin intervención humana? Una interacción totalmente autónoma (descubrimiento, extracción, acción, pago, verificación) obtiene una puntuación más alta que una que requiere aprobación humana en el paso tres.

Para AEO, esto mide qué tan bien su capa de ejecución admite los flujos de trabajo de los agentes de un extremo a otro. La [guía de capa de ejecución](/es/docs/execution-layer/) explica los requisitos de infraestructura.

### Rentabilidad

¿Cuánto cuesta la interacción de cada agente en tokens, llamadas API y tiempo de procesamiento? Los altos costos por interacción desalientan el tráfico de agentes. Los sitios con datos limpios y comprimidos reducen los costos de los agentes y atraen un mayor uso.

La ingeniería de contexto (consulte la [guía de ingeniería de contexto](/es/docs/context-engineering-aeo/)) mejora directamente la rentabilidad al reducir la cantidad de datos que los agentes deben procesar.

### Latencia

¿Cuánto tiempo dura cada interacción? Los agentes normalmente expiran después de 10 a 30 segundos. Si sus puntos finales responden en 200 milisegundos, los flujos de trabajo de los agentes se completan sin problemas. Si responden en 8 segundos, los agentes pueden abandonar o volver a intentarlo.

Mida la latencia por punto final y por paso de interacción. Identifique cuellos de botella que ralentizan los flujos de trabajo de varios pasos.

### Tasa de finalización de tareasLa métrica definitiva. ¿Qué porcentaje de los flujos de trabajo de los agentes que involucran a su sitio se completan exitosamente? Un flujo de trabajo que comienza con el descubrimiento de productos en su sitio pero falla en el proceso de pago se considera incompleto.

Realice un seguimiento de la finalización por tipo de flujo de trabajo. Los flujos de trabajo de comparación, los flujos de trabajo de compra y los flujos de trabajo de consulta pueden tener tasas de éxito muy diferentes, y cada uno de ellos apunta a diferentes oportunidades de optimización.

## Construyendo una práctica de evaluación

Comience con la evaluación manual. Cada dos semanas, ejecute 20 consultas representativas a través de asistentes de inteligencia artificial y documente los resultados. ¿Qué consultas mencionan su sitio? ¿La información extraída es correcta? ¿Puede el agente completar la tarea prevista?

Escale a la evaluación automatizada. Cree scripts de prueba que simulen interacciones de agentes, extraigan datos de sus páginas, intenten realizar llamadas a puntos finales y comparen los resultados con los esperados. Ejecútelos diariamente.

Agregue pruebas de regresión. Cuando cambie el contenido, el esquema o los puntos finales, vuelva a ejecutar el conjunto de evaluación para verificar que no haya ningún problema. Los cambios que enfrentan los agentes tienen efectos dominó que no siempre son obvios en las pruebas en humanos.

## Herramientas de evaluación en 2026

LangChain Evals proporciona cadenas de evaluación que prueban la precisión de la recuperación, la calidad de la respuesta y el uso correcto de las herramientas. Integre con sus implementaciones de agentes LangChain o LangGraph existentes.

Ragas se centra en la evaluación de generación aumentada por recuperación. Mide la relevancia del contexto, la fidelidad de las respuestas y la relevancia de las respuestas. Útil para evaluar qué tan bien los agentes usan su contenido.

TruLens proporciona una evaluación basada en seguimiento que sigue la ruta de razonamiento completa de un agente. Útil para comprender por qué un agente tomó una decisión específica sobre su contenido.

La [guía de KPI de AEO](/es/docs/aeo-kpis-measurement/) cubre el marco de medición más amplio.

## Comparación: pruebas ad hoc versus evaluación estructurada

| Enfoque | Pruebas ad hoc | Evaluación estructurada |
|
---|
---|
---|
| Frecuencia | Cuando algo se rompe | Continuo (automatizado diario más manual quincenal) |
| Cobertura | Lo que sea que pienses probar | Sistemático en todas las páginas clave y puntos finales |
| Detección de regresión | Lento, a menudo pasado por alto | Inmediato, automatizado |
| Guía de optimización | Vago (algo anda mal) | Específico (este campo en esta página tiene un 73% de precisión) |

## Error común

Evaluando solo la precisión e ignorando el costo y la latencia. Un agente que extrae perfectamente pero tarda 15 segundos por página será sustituido por uno que extrae adecuadamente en 2 segundos. Optimice para obtener la imagen completa.

---

## Preguntas frecuentes

**¿Con qué frecuencia debo evaluar las interacciones de los agentes con mi sitio?**Evaluación automatizada diaria. Evaluación manual cada dos semanas. Pruebas de regresión después de cada cambio significativo de contenido o punto final.

**¿Con qué herramienta de evaluación debería empezar?**
Para la mayoría de las implementaciones de AEO, comience con pruebas manuales (ejecutar consultas a través de asistentes de IA) además de pruebas básicas de extracción automatizadas. Agregue LangChain Evals o Ragas cuando necesite un análisis más granular.

**¿Cuál es un buen objetivo de precisión?**
95 por ciento o más para campos de datos críticos (precios, disponibilidad, especificaciones). 90 por ciento para campos secundarios (descripciones, recomendaciones). Por debajo del 85 por ciento indica problemas estructurales.

**¿Cómo evalúo las interacciones de los agentes que no puedo observar?**
Supervise los registros del servidor para detectar patrones de tráfico de agentes. Realice un seguimiento del uso de terminales por parte de agentes de usuario que no son de navegador. Utilice la arquitectura del circuito de retroalimentación para capturar los problemas informados por los agentes.

**¿La evaluación es solo para sitios con alto tráfico de agentes?**
No. Incluso los sitios con un tráfico mínimo de agentes se benefician de la evaluación porque revela problemas estructurales y de contenido que también afectan a los usuarios humanos y las citas de IA.

## Referencias primarias

* [Marco de gestión de riesgos de IA del NIST](https://www.nist.gov/itl/ai-risk-management-framework)
* [Documentación de Schema.org](https://schema.org/docs/documents.html)