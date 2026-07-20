---
title: "Recursos de MCP frente a herramientas frente a indicaciones."
date: 2026-05-23
weight: 135
category: "Guide"
description: "Compare recursos, herramientas e indicaciones de MCP. Descubra qué hace cada función, cuándo usarla y cómo diseñar integraciones de agentes más claras."
summary: "Una comparación práctica de recursos, herramientas e indicaciones de MCP para desarrolladores que crean sistemas legibles por agentes e integraciones de protocolo de contexto modelo."
keywords:
  - Recursos del PCM
  - herramientas MCP
  - Indicaciones de MCP
  - Características del protocolo de contexto del modelo
  - integraciones de agentes
---
# Recursos de MCP frente a herramientas frente a indicaciones: la diferencia práctica

Los recursos de MCP brindan contexto, las herramientas realizan acciones y las indicaciones brindan instrucciones reutilizables. La diferencia es importante porque un diseño deficiente de MCP hace que los agentes no sean confiables: los datos no deben exponerse como una acción, las acciones no deben ocultarse en indicaciones y las indicaciones no deben reemplazar definiciones de capacidades estructuradas.

## La versión corta

El protocolo de contexto modelo tiene varias características de servidor. Tres de los más importantes están documentados como [recursos](https://modelcontextprotocol.io/docs/concepts/resources), [herramientas](https://modelcontextprotocol.io/docs/concepts/tools) y [mensajes](https://modelcontextprotocol.io/docs/concepts/prompts).

Úselos así:

- recursos: "Aquí hay un contexto que puede leer".
- herramientas: "Aquí hay algo que puedes hacer".
- mensajes: "Aquí hay una plantilla de flujo de trabajo que el usuario puede elegir".

Para un contexto más amplio, consulte [MCP vs API para agentes](/es/docs/mcp-vs-api-for-agents/), [Registro de MCP](/es/docs/mcp-registry-guide/) y la [guía para desarrolladores de AEO](/es/docs/developers-guide-aeo/).

## Tabla comparativa

| Característica | Mejor uso | Quién suele iniciarlo | Ejemplo |
|
---|
---|
---|
---|
| Recursos | Exponer datos y contexto | Aplicación cliente o host | Archivo, esquema, catálogo de productos, README |
| Herramientas | Ejecutar acciones o cálculos | Modelo, con control usuario/cliente | Crear ticket, consultar base de datos, calcular cotización |
| Indicaciones | Ofrezca flujos de trabajo reutilizables | Comando o selección controlados por el usuario | "Revisar este código" o "Borrador de notas de la versión" |

Esta división hace que las integraciones sean comprensibles. Los agentes pueden razonar mejor cuando los límites de las capacidades son obvios.

## ¿Para qué sirven los recursos de MCP?

Los recursos son para contexto. La especificación MCP dice que los recursos permiten a los servidores compartir datos como archivos, esquemas de bases de datos o información específica de la aplicación. Cada recurso tiene un URI y puede incluir metadatos como tipo MIME, tamaño, título y anotaciones.

Buenos ejemplos de recursos:

-`file:///project/README.md`
- esquema de base de datos
- instantánea del catálogo de productos
- Documentación de punto final API
- configuración actual del proyecto
- documento de política

Los recursos deben ser lo suficientemente estables para que un modelo pueda inspeccionarlos o hacer referencia a ellos. No deberían alterar el estado empresarial al ser leídos.

## ¿Para qué sirven las herramientas MCP?

Las herramientas son para acciones. La especificación oficial de herramientas dice que los servidores MCP pueden exponer herramientas que los modelos de lenguaje pueden invocar para interactuar con sistemas externos, como API, bases de datos o cálculos.

Buenos ejemplos de herramientas:

- `create_issue`
- `get_order_status`
- `calculate_shipping_quote`
- `search_inventory`
-`submit_refund_request`
- `run_lighthouse_audit`

Las herramientas necesitan esquemas, validación, límites de velocidad, control de acceso y registros de auditoría. La página [barandillas de observabilidad del agente](/es/docs/agent-observability-guardrails/) es relevante aquí.

## Para qué sirven las indicaciones de MCPLas indicaciones son plantillas reutilizables. Ayudan a los usuarios o clientes a desencadenar un flujo de trabajo conocido con argumentos. Un mensaje puede recopilar instrucciones para la revisión del código, la redacción de contenido, la incorporación o la clasificación de soporte.

Las indicaciones son útiles cuando:

- el flujo de trabajo es repetible
- el usuario debe seleccionarlo intencionalmente
- el patrón de instrucción se beneficia de la coherencia
- el resultado tiene mucho lenguaje en lugar de acción

No oculte la ejecución en las indicaciones. Si algo cambia de estado, pertenece a una herramienta con confirmación y registro.

## Errores de diseño a evitar

| Error | Por qué causa problemas | Mejor diseño |
|
---|
---|
---|
| Exponiendo las acciones como recursos | La lectura de datos puede provocar efectos secundarios | Utilice herramientas para acciones |
| Uso de mensajes como envoltorios de API | El modelo puede inferir parámetros de forma vaga | Utilice una herramienta con esquema |
| Poner todo el contexto en las descripciones de las herramientas | Las descripciones se vuelven infladas | Exponer recursos |
| Hacer de cada archivo un recurso | Demasiado ruido contextual | Priorizar los recursos relevantes |
| Sin esquema de salida para herramientas | Más difícil para los clientes validar los resultados | Utilice resultados estructurados siempre que sea posible |

## Implicaciones AEO

Los sitios web legibles por agentes enfrentan el mismo problema de diseño que los servidores MCP: contenido, instrucciones y acciones separados.

Por ejemplo:

- una página de precios es un contexto público similar a un recurso
- una API de pago es una acción similar a una herramienta
- una guía para el comprador es una ayuda rápida para el flujo de trabajo

Una separación clara ayuda a los agentes de IA a comprender qué pueden leer, qué pueden recomendar y qué pueden ejecutar. Esa es la base práctica de [Agent Engine Optimization](/es/docs/what-is-aeo/).

## Lista de verificación de implementación

1. Enumere todo lo que el agente puede leer.
2. Enumere todas las acciones que el agente puede realizar.
3. Enumere los flujos de trabajo repetidos que los usuarios pueden invocar.
4. Asigne cada elemento a un recurso, herramienta o mensaje.
5. Agregue esquemas para herramientas.
6. Agregue metadatos útiles para los recursos.
7. Mantenga las indicaciones controladas por el usuario.
8. Documentar permisos y riesgos.

## Preguntas frecuentes

### ¿Puede un servidor MCP exponer recursos, herramientas y mensajes?

Sí. Muchos servidores útiles expondrán los tres, pero cada característica debe tener una función clara.

### ¿Son los recursos más seguros que las herramientas?

Por lo general, porque los recursos están destinados a leer el contexto. Aún pueden exponer datos confidenciales si el control de acceso es débil.

### ¿El modelo debería invocar automáticamente las indicaciones?

Las indicaciones generalmente están diseñadas para ser controladas por el usuario o seleccionadas explícitamente. La acción automática debe manejarse con cuidado mediante herramientas y permisos.

### ¿Cuál es la regla de diseño de MCP más importante?

Mantenga los efectos secundarios en las herramientas, el contexto en los recursos y las instrucciones reutilizables en las indicaciones.## Conclusión

Un buen diseño de MCP consiste principalmente en límites limpios. Cuando los recursos, las herramientas y las indicaciones hacen cada uno su propio trabajo, es más fácil confiar en los agentes, depurarlos y mejorarlos.