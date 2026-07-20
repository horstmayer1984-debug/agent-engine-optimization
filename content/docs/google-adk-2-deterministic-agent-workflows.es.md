---
title: "Google ADK 2.0 y flujos de trabajo de agentes deterministas."
metaTitle: "Flujos de trabajo del agente determinista de Google ADK 2.0."
date: 2026-07-02
weight: 194
category: "Architecture"
description: "Google ADK 2.0 enfatiza los flujos de trabajo deterministas para agentes confiables. Conozca lo que significa para AEO, rutas de ejecución y aprobaciones."
summary: "Una guía AEO para Google ADK 2.0, flujos de trabajo deterministas, orquestación basada en gráficos, controles humanos en el circuito y acciones confiables de los agentes."
keywords:
  - GoogleADK 2.0
  - flujos de trabajo deterministas del agente
  - kit de desarrollo de agente
  - orquestación de agentes
  - Capa de ejecución AEO
---
# Google ADK 2.0 y flujos de trabajo de agentes deterministas

Google ADK 2.0 es importante para AEO porque impulsa el diseño de agentes hacia flujos de trabajo deterministas donde la ruta es conocida, observable y recuperable. Eso es exactamente lo que los sitios web necesitan cuando los agentes pasan de leer páginas a completar reservas, compras, solicitudes de soporte y procesos comerciales.

## Lo que anunció Google

Google publicó [Por qué construimos ADK 2.0](https://developers.googleblog.com/why-we-built-adk-20/) el 1 de julio de 2026. El argumento central es simple: los modelos de lenguaje grandes son útiles para el razonamiento, pero los agentes de producción también necesitan una ejecución determinista cuando el flujo de trabajo es claro.

Google también anunció [ADK Go 2.0](https://developers.googleblog.com/announcing-adk-go-20/) con un motor de flujo de trabajo basado en gráficos, soporte integrado para humanos, orquestación dinámica, reintentos, estado y comportamiento de reanudación.

## Por qué son importantes los flujos de trabajo deterministas

Muchas tareas web no deben improvisarse. Un reembolso, un pago, una solicitud de cotización, un reclamo de seguro o una escalada de soporte necesitan un camino predecible.

| Comportamiento del agente | Bueno para | Riesgo |
|
---|
---|
---|
| Razonamiento de forma libre | Investigación, comparación, resumen | Ruta de ejecución poco clara |
| Llamada de herramientas | Obteniendo datos o realizando un paso | Mal uso de herramientas sin limitaciones |
| Flujo de trabajo determinista | Procesos de varios pasos conocidos | Requiere modelado inicial |
| Flujo de trabajo humano en el circuito | Acciones arriesgadas o irreversibles | Más lento pero más seguro |

La [Capa de ejecución](/es/docs/execution-layer/) debería favorecer rutas deterministas para acciones comerciales importantes.

## Impacto AEO para los sitios web

ADK 2.0 refuerza una regla práctica: no haga que los agentes adivinen su flujo de trabajo a partir de botones y textos de marketing. Publicar el flujo de trabajo.

Eso significa definir:

- estados de tarea permitidos
- entradas requeridas
- reglas de validación
- puertas de aprobación
- lógica de reintento
- rutas de cancelación
- mensajes de confirmación finales
- registros de auditoría

Esto se conecta a [Agent UX y Human-in-the-Loop Design](/es/docs/agent-ux-human-in-the-loop/), [Multi-Agent AEO](/es/docs/multi-agent-aeo/) y [Agent-Ready Web Apps](/es/docs/agent-ready-web-apps/).

## Ejemplo: reserva de cita

| Paso | Requisito determinista |
|
---|
---|
| Seleccionar servicio | Utilice una identificación de servicio estable, no solo el texto de la página |
| Consultar disponibilidad | Volver franjas horarias actuales |
| Recopilar datos de usuario | Validar campos obligatorios |
| Mostrar política | Normas de fijación de precios y cancelación de devoluciones |
| Confirmar reserva | Requerir la aprobación explícita del usuario |
| Devolver resultado | Proporcionar ID de reserva y próximos pasos |

Un agente puede razonar sobre qué servicio se adapta al usuario. No se debe inventar la ruta de confirmación de la reserva.

## Cómo auditar su sitio

1. Elija un flujo de trabajo de alto valor.
2. Escriba la máquina de estado exacta para ese flujo de trabajo.3. Identifique dónde se basa actualmente su sitio web en sugerencias visuales.
4. Agregue etiquetas, esquemas, API o herramientas MCP legibles por máquina cuando sea necesario.
5. Agregue puertas de aprobación antes de acciones irreversibles.
6. Registre cada transición de estado relevante para el agente.
7. Pruebe los caminos del fracaso, no sólo los caminos exitosos.

## Preguntas frecuentes

### ¿El diseño determinista del flujo de trabajo es solo para desarrolladores?

No. Los equipos de producto, SEO, legal, soporte y operaciones deben ayudar a definir qué acciones requieren aprobación y qué estados son válidos.

### ¿ADK 2.0 reemplaza a LangGraph u otros marcos?

No. Es otro camino de desarrollo de agentes. La lección útil de AEO es el principio de diseño: ejecución determinista para flujos de trabajo conocidos.

### ¿Por qué afecta esto al SEO?

El SEO clásico lleva a los usuarios a las páginas. El SEO agente también necesita que esas páginas y flujos de trabajo sean utilizables por asistentes automatizados.

### ¿Cuál es el primer flujo de trabajo a modelar?

Comience con la acción de mayor valor que un agente podría realizar razonablemente: reserva, solicitud de cotización, comparación de productos, pago, ticket de soporte o solicitud de demostración.

## Fuentes

Fuentes principales: [Blog de desarrolladores de Google: Por qué creamos ADK 2.0](https://developers.googleblog.com/why-we-built-adk-20/) y [Blog de desarrolladores de Google: ADK Go 2.0](https://developers.googleblog.com/announcing-adk-go-20/).