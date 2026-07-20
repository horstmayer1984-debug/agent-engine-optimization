---
title: "Aplicaciones MCP: interfaces interactivas para flujos de trabajo."
date: 2026-05-17
weight: 135
category: "Architecture"
description: "Descubra qué son las aplicaciones MCP, cómo funcionan los componentes interactivos de la interfaz de usuario dentro de los hosts MCP y cuándo los sitios web."
summary: "Una guía práctica de aplicaciones MCP que cubre la interfaz de usuario en línea, la representación segura, los casos de uso y cómo la extensión cambia el diseño del producto orientado al agente."
keywords:
  - Aplicaciones MCP
  - Interfaz de usuario de MCP
  - interfaces interactivas de agentes
  - Aplicaciones de protocolo de contexto modelo
  - UI de flujos de trabajo del agente
---
# Aplicaciones MCP: interfaces interactivas para flujos de trabajo de agentes

Las aplicaciones MCP son una extensión oficial del Protocolo de contexto modelo que permite que las herramientas devuelvan interfaces de usuario interactivas, no solo texto o datos estructurados. Esto es importante porque algunos flujos de trabajo de agentes necesitan gráficos, formularios de aprobación, paneles o controles de varios pasos dentro de la propia conversación. Las aplicaciones MCP mantienen el flujo de trabajo en contexto y, al mismo tiempo, brindan a los usuarios una interfaz más rica cuando el texto sin formato no es suficiente.

## Lo que dicen los documentos oficiales de MCP

El proyecto MCP anunció MCP Apps como su primera extensión oficial en enero de 2026. Los documentos oficiales describen interfaces HTML interactivas representadas dentro de los hosts MCP, con zona de pruebas y un puente de comunicación seguro entre la aplicación y el host.

Fuentes primarias:

- [Blog de MCP: anuncio en vivo de aplicaciones de MCP](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/)
- [Descripción general de aplicaciones MCP](https://modelcontextprotocol.io/extensions/apps/overview)
- [Descripción general de las extensiones MCP](https://modelcontextprotocol.io/extensions)

## Por qué existen las aplicaciones MCP

El texto es suficiente para muchas respuestas de herramientas:

- un resultado de búsqueda
- un estado
- una simple recomendación

Pero el texto se vuelve torpe para:

- gráficos
- comparaciones visuales
- flujos de trabajo de aprobación
- lienzos de diseño
- formularios con varios campos dependientes
- paneles con estado en vivo

Las aplicaciones MCP agregan una capa de interfaz de usuario sin obligar a los usuarios a abandonar la experiencia del host.

## Aplicaciones MCP frente a aplicaciones web normales

| Pregunta | Aplicación web independiente | Aplicación MCP |
|
---|
---|
---|
| ¿Dónde se renderiza? | Sitio o pestaña separada | Dentro del host MCP |
| ¿Se conserva el contexto de la conversación? | Generalmente no | Sí |
| Lo mejor para | Productos completos | Fragmentos de flujo de trabajo y UI vinculada a herramientas |
| Comunicación | API de aplicaciones de navegador | Puente de aplicación MCP plus |
| Viaje del usuario | Cambio de contexto | Continuación en línea |

Las aplicaciones MCP no reemplazan todas las aplicaciones web. Son útiles cuando la interfaz es parte de una tarea mediada por un agente en lugar de todo el producto.

## Implicaciones AEO

La [capa de ejecución](/es/docs/execution-layer/) a menudo necesita un punto de control humano. Las aplicaciones MCP pueden hacer que ese punto de control sea práctico:

- aprobar un reembolso
- inspeccionar una cotización
- elegir entre opciones
- revisar un gráfico
- confirmar una acción arriesgada

Esto se conecta naturalmente con [la experiencia del usuario del agente y el diseño humano en el circuito](/es/docs/agent-ux-human-in-the-loop/), donde la pregunta no es "humano o agente" sino "¿qué partes necesitan qué interfaz?"

## Cuándo usar aplicaciones MCP

Úsalos cuando:

- el resultado de una herramienta necesita interpretación visual
- el siguiente paso requiere aportación humana estructurada
- quieres preservar el contexto conversacional
- la interfaz de usuario está subordinada a un flujo de trabajo de herramientas

No los utilice cuando:

- una simple respuesta de texto es suficiente
- la experiencia necesita un producto completo e independiente
- el ecosistema de alojamiento al que se dirige aún no admite la extensión## Seguridad e implementación

Los documentos oficiales describen la representación en espacio aislado y un puente de mensajes seguro. Eso significa que los equipos aún deben pensar detenidamente en:

- qué datos ingresan a la interfaz de usuario
- qué herramienta puede activar la llamada a la interfaz de usuario
- si se requiere aprobación
- cómo se registra el estado
- cómo varía el soporte del anfitrión

La [guía de autorización de MCP](/es/docs/mcp-authorization-oauth-ai-agents/) sigue siendo relevante porque la interfaz de usuario enriquecida no elimina la necesidad de permisos estrictos.

## Preguntas frecuentes

### ¿Las aplicaciones MCP son parte del MCP principal?

Son una extensión oficial, no el protocolo central en sí.

### ¿Las aplicaciones MCP reemplazan un sitio web?

No. Son mejores para la interfaz de usuario del flujo de trabajo en línea, no para reemplazar todas las experiencias web públicas.

### ¿Qué clientes los apoyan?

El soporte del anfitrión varía. Los documentos de MCP mantienen una matriz de soporte al cliente para extensiones oficiales.

### ¿Cuál es el mejor primer caso de uso?

Los flujos de aprobación y los paneles pequeños son puntos de partida sólidos porque necesitan más que texto pero menos que una interfaz de usuario completa del producto.

## Conclusión

Las aplicaciones MCP son importantes porque los flujos de trabajo de los agentes aún necesitan momentos de juicio humano. Traen fragmentos de interfaz útiles al mismo lugar donde ya está trabajando el agente.