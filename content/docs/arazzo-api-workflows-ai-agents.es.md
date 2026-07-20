---
title: "Flujos de trabajo de la API de Arazzo para agentes de IA."
metaTitle: "Flujos de trabajo de la API de Arazzo para agentes de IA: Guía."
date: 2026-05-17
weight: 115
category: "Architecture"
description: "Arazzo define flujos de trabajo API legibles por máquina además de OpenAPI. Descubra por qué es importante para los agentes de IA, MCP y SEO en la capa."
summary: "Una guía práctica de Arazzo para agentes de IA, que explica las descripciones del flujo de trabajo, la secuenciación de OpenAPI, los criterios de éxito y los patrones de implementación de AEO."
keywords:
  - Especificación de Arazzo
  - Flujos de trabajo API para agentes de IA
  - OpenAPI Arazzo
  - API listas para agentes
  - capa de ejecución SEO
---
# Flujos de trabajo de la API de Arazzo para agentes de IA

Arazzo es importante para AEO porque OpenAPI describe operaciones API individuales, pero los agentes a menudo necesitan flujos de trabajo. Una tarea de reserva, cotización, pago o incorporación puede requerir varias llamadas a la API en el orden correcto. Arazzo ofrece a los equipos una forma legible por máquina para describir esas secuencias.

## Qué es Arazzo

La Iniciativa OpenAPI describe a Arazzo como una especificación para expresar secuencias de llamadas API y sus dependencias para lograr un resultado. Complementa OpenAPI en lugar de reemplazarlo.

Fuentes primarias:

- [Iniciativa OpenAPI: Especificación Arazzo](https://www.openapis.org/arazzo-specification)
- [Especificación Arazzo](https://spec.openapis.org/arazzo/latest.html)
- [Especificación de OpenAPI](https://spec.openapis.org/oas/v3.1.0.html)

## Por qué OpenAPI por sí solo no es suficiente

OpenAPI es excelente para describir puntos finales. Le dice a un desarrollador o máquina qué operaciones existen, qué parámetros aceptan y qué respuestas devuelven.

Pero muchas tareas reales necesitan orden:

1. Buscar servicios disponibles.
2. Seleccione un servicio.
3. Verifique los espacios disponibles.
4. Crea una reserva.
5. Confirmar la reserva.

Si un agente solo ve puntos finales individuales, debe inferir la secuencia. Esto puede funcionar para API simples, pero se vuelve frágil cuando están involucradas dependencias, tokens, estados o reglas de validación.

## OpenAPI frente a Arazzo frente a MCP

| Capa | Trabajo principal | Beneficio del agente |
|
---|
---|
---|
| API abierta | Describe las operaciones API | Comprender los puntos finales disponibles |
| Arazzo | Describe los flujos de trabajo en todas las operaciones | Comprender cómo completar una tarea |
| PCM | Expone herramientas y recursos invocables | Invocar acciones a través de una interfaz de agente |

La [guía MCP vs API](/es/docs/mcp-vs-api-for-agents/) explica la capa de herramientas. Arazzo ayuda a documentar la lógica del flujo de trabajo detrás de esas herramientas.

## Dónde encaja Arazzo en AEO

AEO es más fuerte cuando los agentes pueden moverse a través de esta secuencia:

1. Descubre el servicio.
2. Comprender las capacidades.
3. Leer restricciones.
4. Ejecute el flujo de trabajo.
5. Verifique el resultado.

Arazzo admite los pasos 2 a 5 al hacer explícitos los flujos de trabajo de varios pasos. Es especialmente útil para la [capa de ejecución](/es/docs/execution-layer/), donde un agente necesita hacer más que buscar contenido.

## Casos de uso sólidos

| Caso de uso | Por qué ayuda Arazzo |
|
---|
---|
| Pago de comercio electrónico | El carrito, el envío, los impuestos, el pago y la confirmación suceden en secuencia |
| Solicitud de cotización B2B | La elegibilidad, la configuración, los precios y el envío dependen unos de otros |
| Reserva de viajes | Se ordena disponibilidad, reglas tarifarias, datos de pasajeros y confirmación |
| Incorporación de SaaS | La configuración del espacio de trabajo, el usuario, la facturación y los permisos tiene dependencias || Escalada de soporte | Estado de necesidad de creación, clasificación, adjunto y enrutamiento de boletos |
| Flujo de trabajo financiero | Las divulgaciones, la elegibilidad y el consentimiento deben ocurrir antes de tomar acción |

La [lista de verificación de aplicaciones web listas para agentes](/es/docs/agent-ready-web-apps/) cubre cómo diseñar la superficie subyacente del producto.

## Qué incluir en un flujo de trabajo de Arazzo

Como mínimo, documente:

- objetivo del flujo de trabajo
- entradas requeridas
- pasos ordenados
- operaciones de origen OpenAPI
- dependencias entre pasos
- criterios de éxito
- salidas
- estados de error
- expectativas de reintento y de idempotencia

Los criterios de éxito son especialmente importantes. Los agentes necesitan saber qué significa "hecho".

## Ejemplo de forma de flujo de trabajo

Para una API de reserva de citas:

| Paso | Operación | Salida utilizada más tarde |
|
---|
---|
---|
| 1 | `list_services` | `service_id` |
| 2 | `list_available_slots` | `slot_id` |
| 3 | `create_booking` | `booking_id` |
| 4 | `get_booking` | estado confirmado |

Sin documentación del flujo de trabajo, un agente puede llamar primero al punto final equivocado o perder el paso de confirmación.

## Ruta de implementación

1. Limpia tu documento OpenAPI.
2. Elija tres flujos de trabajo de alto valor.
3. Escriba descripciones de Arazzo para esos flujos de trabajo.
4. Pruébelos con un agente o ejecutor de flujo de trabajo.
5. Vincule los documentos de flujo de trabajo de los documentos API y `llms.txt`.
6. Empaquetar los mismos flujos de trabajo que las herramientas MCP cuando sea útil.

Esto mantiene el sistema conectado a tierra: OpenAPI describe las operaciones, Arazzo describe la secuenciación, MCP expone herramientas invocables.

## Preguntas frecuentes

### ¿Arazzo reemplaza a OpenAPI?

No. Complementa OpenAPI al describir flujos de trabajo que utilizan operaciones de OpenAPI.

### ¿Arazzo es solo para agentes de IA?

No. Es útil para documentación, generación de SDK, pruebas y cumplimiento. Los agentes de IA son un caso de uso sólido.

### ¿Necesito a Arazzo antes que MCP?

No siempre. Para herramientas simples, MCP puede ser suficiente. Para flujos de trabajo de varios pasos, Arazzo ayuda a que el proceso sea explícito.

### ¿Cuál es el ángulo del SEO?

Arazzo no es un factor de ranking. Mejora la preparación de la capa de ejecución al hacer que los flujos de trabajo sean legibles por máquina.

### ¿Qué flujos de trabajo deberían documentarse primero?

Comience con flujos de trabajo vinculados a ingresos, resolución de soporte, reservas, incorporación o acciones sensibles al cumplimiento.