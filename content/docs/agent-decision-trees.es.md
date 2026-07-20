---
title: "Árboles de decisión deterministas: cómo los agentes de IA."
metaTitle: "Árboles de decisión para agentes de IA: Guía de evaluación."
date: 2026-04-14
weight: 92
category: "Architecture"
description: "Los agentes de IA ejecutan estrictos árboles de decisión de aprobación/rechazo antes de realizar transacciones. Qué preguntas deterministas hacen, qué causa."
metaDescription: "Descubra qué comprobaciones de aprobación/rechazo utilizan los agentes de IA antes de actuar, qué causa la exclusión y cómo hacer que su sitio web sea más."
summary: "Los agentes no navegan ni deciden intuitivamente. Ejecutan árboles de decisión deterministas con estrictos criterios de aprobación/rechazo. Falla una verificación y el agente pasa a un competidor."
keywords:
  - árboles de decisión de agentes
  - evaluación determinista del agente
  - criterios de aprobación del agente
  - agentes de mapeo de capacidades
  - criterios de exclusión de agentes
  - evaluación máquina a máquina
---
Los agentes de IA no evalúan su sitio web como lo hacen los humanos. No navegan, no se forman impresiones y poco a poco generan confianza. Ejecutan árboles de decisión deterministas con estrictos criterios de aprobación/falla en cada nodo. Si falla una verificación, el proceso finaliza. El agente pasa al siguiente proveedor sin explicación.

Comprender estos árboles de decisión marca la diferencia entre ser seleccionado y ser excluido silenciosamente.

## Las seis preguntas que todo agente hace

### Pregunta 1: ¿Qué puede hacer este sistema?

El agente busca un manifiesto de capacidad. En las implementaciones UCP, este es el archivo JSON en /.well-known/ucp. En las implementaciones de MCP, son los esquemas de herramientas y recursos devueltos por el servidor. En configuraciones más simples, es el archivo llms.txt o la Tarjeta de Agente.

Si el agente no puede determinar qué admite su sistema, lo omitirá por completo. No hay crédito parcial. O las capacidades están declaradas o no.

Condición de aprobación: una declaración legible por máquina de acciones admitidas, tipos de datos y capacidades de transacción.

Condición de error: sin manifiesto, sin esquema, sin llms.txt. El agente no tiene forma de determinar lo que usted ofrece.

### Pregunta 2: ¿Qué insumos se requieren?

Una vez que el agente sabe lo que puede hacer, verifica si tiene las entradas necesarias para desencadenar la acción. Su sistema debe proporcionar un esquema claro de los valores de entrada esperados: tipos de datos, campos obligatorios versus opcionales, reglas de validación y rangos aceptables.

Condición de aprobación: cada punto final o acción tiene un esquema de entrada documentado con tipos, restricciones y ejemplos.

Condición de error: los requisitos de entrada son vagos, no están documentados o solo se pueden descubrir mediante prueba y error.

### Pregunta 3: ¿Es verificable el estado actual?

El agente no confía en el contenido de la página estática. Necesita verificar el estado crítico en tiempo real.

¿El precio es explícito y actual? Frases humanas como "precio a pedido" o "a partir de" causan exclusión inmediata en transacciones con aversión al riesgo. El agente necesita un número exacto válido para un período de tiempo definido.

¿Se verifica el inventario en tiempo real? El agente envía una llamada API. El HTML almacenado en caché que dice "en stock" no tiene valor si el inventario real se agotó hace dos horas.

¿Están las políticas estructuradas y legibles por máquina? Políticas de devolución, términos de envío, condiciones de cancelación. Si existen sólo como párrafos en prosa en una página legal, el agente no puede analizarlos de manera confiable. Se requieren etiquetas de acción de Schema.org y declaraciones de políticas estructuradas.

Condición de aprobación: estado verificable en tiempo real para cada parámetro de transacción crítico.Condición de falla: datos obsoletos, precios ambiguos, políticas no estructuradas o cualquier parámetro que requiera interpretación en lugar de análisis.

### Pregunta 4: ¿Qué estado se garantiza después de la acción?

El agente necesita garantías deterministas sobre lo que sucederá cuando actúe. Si envía una compra, ¿recibirá una confirmación con un ID de pedido? If it books an appointment, will it receive a confirmed time slot? Si la acción falla, ¿recibirá un error estructurado explicando el motivo?

Condición de aprobación: cada punto final de acción devuelve un resultado determinista (éxito con detalles de confirmación o fracaso con clasificación de error específica).

Condición de error: respuestas ambiguas, confirmaciones en lenguaje humano sin datos estructurados o puntos finales que devuelven éxito sin pruebas verificables.

### Pregunta 5: ¿Coinciden los atributos entre fuentes?

Los agentes cruzan datos de múltiples fuentes. Si su precio en Google Merchant Center difiere de su respuesta API, o su marcado de esquema muestra una disponibilidad diferente a su manifiesto UCP, el agente detecta la inconsistencia.

Las inconsistencias no sólo causan confusión. Provocan exclusión. Un agente que no pueda confiar en sus datos no realizará transacciones a través de su sistema.

Condición de aprobación: valores idénticos de precio, disponibilidad, especificaciones y políticas en todas las fuentes legibles por máquina (marcado de esquema, respuestas API, feeds de productos, manifiesto UCP).

Condición de falla: cualquier discrepancia entre fuentes de datos.

### Pregunta 6: ¿La acción se puede repetir de forma segura?

Los agentes vuelven a intentarlo en caso de error. Si se agota el tiempo de espera de la red después de realizar una compra, el agente enviará la misma solicitud nuevamente. Su sistema debe manejar esto sin crear pedidos duplicados, cargos duplicados o estados corruptos.

Condición de aprobación: puntos finales de transacción idempotentes donde la misma solicitud produce el mismo resultado independientemente de cuántas veces se envíe.

Condición de error: puntos finales no idempotentes donde los reintentos crean duplicados.

## The decision tree in practice

El agente evalúa estas preguntas de forma secuencial. Cada "suspenso" finaliza la evaluación inmediatamente:

¿Capacidad declarada? No → excluido. ¿Insumos documentados? No → excluido. ¿Estado verificable en tiempo real? No → excluido. ¿Resultados deterministas? No → excluido. Data consistent across sources? No → excluido. ¿Reintentos seguros? No → excluido.

Sólo si se aprueban los seis controles, el agente continúa con la transacción.

## Por qué esto difiere de la evaluación humanaUn comprador humano tolera la ambigüedad. "Precio a pedido" significa que llamarán. "Por lo general, se envía en 3 a 5 días" es lo suficientemente cercano. Se hojea y se acepta una política de devolución confusa.

Un agente no tolera nada de esto. Cada ambigüedad es una condición de fracaso. Todo "normalmente" es indeterminado. Toda política no estructurada es imposible de analizar. El agente opera con lógica binaria: verificado o excluido.

Esta es la razón por la que los sitios que parecen pulidos para los humanos pueden obtener una puntuación de cero con los agentes. El diseño visual, la reputación de la marca y el texto persuasivo no tienen peso en un árbol de decisiones determinista.

La [guía de capa de ejecución](/es/docs/execution-layer/) explica los requisitos de infraestructura. La [guía de implementación de AEO](/es/docs/implement-aeo/) cubre la ruta de optimización paso a paso.

---

## Preguntas frecuentes

**¿Qué es un árbol de decisión determinista en AEO?**
Una secuencia estricta de verificaciones de aprobación/rechazo que un agente ejecuta antes de realizar transacciones con su sitio. Cada verificación evalúa un requisito específico (capacidades, insumos, estado, resultados, consistencia, idempotencia). Fallar cualquier verificación causa exclusión inmediata.

**¿Cuál es la razón más común por la que los agentes excluyen un sitio?**
Precios no estructurados o ambiguos. "Precio a pedido", "a partir de" o precios que difieren entre el marcado de esquema y las respuestas de API provocan una exclusión inmediata.

**¿Cómo pruebo si mi sitio pasa la evaluación del agente?**
Simule las seis preguntas manualmente. ¿Puedes encontrar tu declaración de capacidad? ¿Están todas las entradas documentadas? ¿Puedes verificar el estado mediante una llamada API? ¿Todas las fuentes de datos devuelven valores idénticos? Ejecute esta verificación mensualmente.

**¿Qué es un manifiesto de capacidad?**
Un archivo legible por máquina que declara lo que su sistema puede hacer. En UCP: /.conocido/ucp. En MCP: esquemas de herramientas y recursos. En configuraciones más simples: llms.txt o agent-card.json.

**¿Por qué es tan importante la idempotencia?**
Porque los agentes vuelven a intentarlo si fallan. Un tiempo de espera no significa que la acción haya fallado. Si su punto final crea una orden duplicada al reintentar, el agente ha causado un daño real. Los puntos finales idempotentes manejan los reintentos de forma segura al devolver el mismo resultado para la misma solicitud.

## Guías relacionadas

* [arquitectura de comercio agente](/es/docs/agentic-commerce/)

## Referencias primarias

* [Marco de gestión de riesgos de IA del NIST](https://www.nist.gov/itl/ai-risk-management-framework)
* [Documentación de Schema.org](https://schema.org/docs/documents.html)