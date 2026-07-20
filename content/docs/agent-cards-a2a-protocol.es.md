---
title: "Tarjetas de agente y protocolo A2A para sitios listos."
date: 2026-04-12
weight: 63
category: "Architecture"
description: "Cómo las tarjetas de agente y A2A ayudan a los agentes autónomos a descubrir capacidades, colaborar de forma segura e interactuar con sitios web listos."
summary: "Las Tarjetas de agente les dicen a otros agentes lo que su sitio puede hacer. El protocolo A2A permite el intercambio directo de tareas de agente a agente. Juntos hacen que su sitio sea reconocible y colaborativo en flujos de trabajo de múltiples agentes."
keywords:
  - tarjeta de agente json
  - protocolo A2A
  - protocolo agente a agente
  - colaboración de agentes
  - implementación de tarjeta de agente
  - descubrimiento de múltiples agentes
---
Las tarjetas de agente y el protocolo A2A (agente a agente) le permiten programar su sitio web para que agentes autónomos lo descubran y colaboren con él sin que usted cree cada integración manualmente. Una Tarjeta de Agente describe lo que su sitio puede hacer. El protocolo A2A define cómo los agentes intercambian tareas y resultados.

Juntos, hacen que su sitio participe en flujos de trabajo de múltiples agentes en lugar de un punto final pasivo que los agentes individuales consultan de forma aislada.

## Qué contiene una Tarjeta de Agente

Una tarjeta de agente es un archivo JSON (agent-card.json) ubicado en la raíz de su sitio. Sirve como un manifiesto de capacidad legible por máquina que les dice a otros agentes: quién es usted, qué puede hacer, cómo autenticarse y qué protocolos admite.

Los campos principales: nombre (el nombre de su servicio), descripción (qué hace su servicio en una oración), URL (su URL base), capacidades (una lista estructurada de acciones que su sitio puede realizar), protocolos (qué estándares de comunicación admite, como MCP, REST, A2A), autenticación (cómo deben autenticarse los agentes) y contacto (dónde informar problemas).

Cada capacidad de la lista incluye un nombre, una descripción, un esquema de entrada y un esquema de salida. Esto es lo que utilizan los agentes para decidir si su sitio puede ayudarles con su tarea actual.

## Por qué las tarjetas de agente son importantes para el descubrimiento

En un flujo de trabajo de múltiples agentes, un agente coordinador necesita encontrar servicios que puedan manejar subtareas específicas. Sin Tarjetas de Agente, el coordinador tiene que adivinar según el contenido de la página. Con las Tarjetas de Agente, el coordinador lee un manifiesto estructurado y toma una decisión de enrutamiento informada en milisegundos.

Las tarjetas de agente también permiten la recomendación. Un agente que utilice su sitio con éxito puede pasar su Tarjeta de Agente a otros agentes que necesiten capacidades similares. Esto crea un mecanismo de descubrimiento de boca en boca dentro del ecosistema de agentes.

## Conceptos básicos del protocolo A2A

El protocolo A2A estandariza cómo los agentes intercambian tareas. Un agente envía una solicitud de tarea (qué se debe hacer, qué entradas están disponibles, qué restricciones se aplican). El agente receptor procesa la tarea y devuelve un resultado estructurado.

El protocolo maneja la gestión del ciclo de vida de las tareas: creación de tareas, actualizaciones de estado, finalización y fallas. También admite tareas de larga duración en las que el resultado no está disponible de inmediato.

Para su sitio, implementar A2A significa exponer puntos finales de tareas que aceptan solicitudes estructuradas y devuelven respuestas estructuradas. El formato sigue la especificación A2A de Google con objetos de tarea escritos y enumeraciones de estado.

## Implementación paso a paso

### Paso 1: crear agent-card.jsonEscriba el archivo JSON con la descripción y las capacidades de su servicio. Sea preciso acerca de qué hace cada capacidad, qué insumos requiere y qué resultados produce. Colóquelo en la raíz de su dominio.

### Paso 2: Agregar puntos finales de tareas A2A

Exponga puntos finales que aceptan solicitudes de tareas y devuelven resultados de tareas. Se necesita una implementación mínima: POST /a2a/tasks (crear una nueva tarea), GET /a2a/tasks/{id} (verificar el estado de la tarea) y GET /a2a/tasks/{id}/result (recuperar el resultado completo).

### Paso 3: Conéctese con MCP

Si ya tiene un servidor MCP, sus puntos finales de tareas A2A pueden delegar internamente a las herramientas MCP. La capa A2A maneja la comunicación entre agentes mientras que MCP maneja la ejecución real de la herramienta.

### Paso 4: Regístrese públicamente

Incluya su tarjeta de agente en los registros de MCP y directorios de agentes para que los agentes fuera de su red directa puedan descubrir su servicio.

## Colaboración en tiempo real con WebSockets

Los patrones estándar de solicitud-respuesta funcionan para tareas simples. Los flujos de trabajo colaborativos de varios pasos se benefician de las conexiones WebSocket.

Un punto final WebSocket en /ws/agent-collaboration permite que dos agentes mantengan una conexión persistente para flujos de trabajo que requieren negociación de ida y vuelta: verificar múltiples espacios de disponibilidad, comparar opciones, ajustar parámetros en función de resultados intermedios.

Esto es particularmente útil para flujos de trabajo comerciales donde un agente necesita reservar inventario, verificar opciones de envío, aplicar reglas de descuento y confirmar la autoridad de pago en una secuencia coordinada.

## Zona de pruebas de agentes para seguridad

Cuando los agentes externos ejecutan tareas en su infraestructura, el sandboxing les impide acceder a recursos fuera de su alcance autorizado.

El sandboxing basado en WASM ejecuta operaciones enviadas por agentes en entornos aislados con límites de memoria definidos, límites de CPU y restricciones de acceso a la red.

Para la mayoría de los sitios, el sandboxing se vuelve relevante cuando expone puntos finales de ejecución que aceptan entradas complejas o cuando permite que los agentes ejecuten lógica personalizada dentro de su sistema.

## Comparación: MCP frente a A2A

| Aspecto | PCM | A2A |
|
---|
---|
---|
| Propósito | Comunicación agente-herramienta | Comunicación de agente a agente |
| Descubrimiento | Esquemas de herramientas | Tarjetas de agente |
| Patrón de interacción | Solicitud-respuesta única | Ciclo de vida de la tarea con seguimiento de estado |
| Lo mejor para | Ejecución directa de herramientas | Flujos de trabajo colaborativos de varios pasos |
| Su implementación | Servidor JSON-RPC | Puntos finales de tareas más tarjeta de agente |

Ambos protocolos se complementan. MCP maneja las herramientas. A2A maneja la colaboración entre agentes que utilizan esas herramientas.El [artículo AEO sobre múltiples agentes](/es/docs/multi-agent-aeo/) explica cómo los flujos de trabajo orquestados dependen de estos protocolos. La [guía MCP vs API](/es/docs/mcp-vs-api-for-agents/) cubre la capa de acceso a la herramienta en detalle.

---

## Preguntas frecuentes

**¿Cuánto tiempo lleva crear una Tarjeta de Agente?**
Treinta minutos para una Tarjeta de Agente básica con 3 a 5 capacidades. La estructura JSON es sencilla.

**¿Necesito tanto MCP como A2A?**
No necesariamente. Comience con MCP si su necesidad principal es que los agentes llamen a sus herramientas. Agregue A2A cuando desee que los agentes colaboren con su servicio como pares en flujos de trabajo de múltiples agentes.

**¿Cuál es la diferencia entre una Tarjeta de Agente y llms.txt?**
llms.txt es una descripción general legible por humanos y máquinas de su sitio en Markdown. Una tarjeta de agente es un manifiesto de capacidad estrictamente legible por máquina en JSON. Ambos sirven para el descubrimiento, pero las Tarjetas de Agente están más estructuradas y son más específicas del protocolo.

**¿Pueden los agentes descubrir mi sitio sin una Tarjeta de Agente?**
Sí, a través de llms.txt, marcado de esquema o rastreo directo de páginas. Una tarjeta de agente acelera el descubrimiento y permite la colaboración A2A, pero no es la única vía de descubrimiento.

**¿A2A es solo para grandes empresas?**
No. Cualquier sitio que exponga acciones de agentes puede realizar beneficios de A2A. Incluso un servicio pequeño con un punto final de reserva puede participar en flujos de trabajo de múltiples agentes a través de una tarjeta de agente simple y un punto final de tarea.

## Guías relacionadas

* [arquitectura de comercio agente](/es/docs/agentic-commerce/)

## Referencias primarias

* [Especificación del protocolo A2A](https://github.com/a2aproject/A2A/blob/main/docs/specification.md)
* [Especificación del protocolo de contexto del modelo](https://modelcontextprotocol.io/specification/2025-06-18/basic/index)