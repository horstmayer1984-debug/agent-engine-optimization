---
title: "API de agentes de Google Genkit: lo que deben aprender."
metaTitle: "API de agentes Genkit de Google y AEO."
date: 2026-07-02
weight: 193
category: "Architecture"
description: "La API Genkit Agents de Google muestra cómo las aplicaciones agentes administran herramientas, estado, transmisión y aprobaciones. Conozca las implicaciones."
summary: "Una guía práctica de AEO para la API Genkit Agents de Google, bucles de herramientas, aprobación humana, estado, transmisión y sitios web listos para agentes."
keywords:
  - API de agentes de Google Genkit
  - Agentes Genkit
  - aplicaciones agentes de pila completa
  - sitios web listos para agentes
  - guía para desarrolladores AEO
---
# API de agentes de Google Genkit

La API Genkit Agents de Google es importante para AEO porque muestra cómo se estructuran las aplicaciones agentes de producción: llamadas de herramientas, estado, transmisión, persistencia, protocolos de interfaz y aprobación humana. Los equipos del sitio web deben tratarlo como una señal de que los agentes necesitan superficies de tareas explícitas, no sólo páginas legibles.

## Lo que anunció Google

El 1 de julio de 2026, Google publicó [Creación de aplicaciones agentes de pila completa con Genkit](https://developers.googleblog.com/build-agentic-full-stack-apps-with-genkit/). Google describe Genkit como un marco de código abierto para crear aplicaciones agentes y basadas en IA en lenguajes como TypeScript, Go, Dart y Python.

La nueva API de agentes está marcada como vista previa en TypeScript y Go. Ese estatus importa. Es útil para aprender patrones de arquitectura, pero los equipos de producción deberían esperar cambios en la API.

## La lección AEO

Genkit empaqueta los requisitos comunes de los agentes en un marco de desarrollo:

| Patrón Genkit | Implicación de la preparación del sitio web |
|
---|
---|
| Bucle de herramientas | Los sitios web necesitan acciones claras y aportaciones estables |
| Historial de mensajes | Los agentes necesitan estado en una tarea, no lecturas de páginas aisladas |
| Transmisión | Los usuarios necesitan ver el progreso durante las tareas largas de los agentes |
| Persistencia | Los flujos de trabajo de los agentes necesitan rutas de reanudación y auditoría |
| Aprobación humana | Las acciones arriesgadas necesitan puertas de confirmación |
| Subagentes | Tareas complejas pueden involucrar a agentes especializados |

Esto refuerza la distinción entre [Optimización del motor de respuesta](/es/docs/answer-engine-optimization/) y [Optimización del motor del agente](/es/docs/what-is-aeo/). Los motores de respuesta citan el contenido. Los agentes también deben completar el trabajo.

## Qué exponer en un sitio web

Un sitio listo para agentes debe exponer tareas importantes como flujos de trabajo estructurados:

1. Encuentre el producto, servicio, artículo o documento adecuado.
2. Compare opciones con hechos actuales.
3. Verifique la elegibilidad, el precio, el inventario o la disponibilidad.
4. Solicite una cotización, reserve una cita o inicie el pago.
5. Pedir confirmación humana antes de acciones irreversibles.
6. Devolver un estado claro de éxito, fracaso o siguiente paso.

Esa es la [Capa de ejecución](/es/docs/execution-layer/) en la práctica.

## Genkit vs optimización de página ordinaria

| Requisito | Página de SEO | Superficie de tareas lista para agentes |
|
---|
---|
---|
| Objetivo principal | Clasificar y atraer clics | Completar una tarea de usuario |
| Entrada | Consulta y haz clic | Intención del usuario más parámetros de la herramienta |
| Salida | Vista de página | Resultado verificado o siguiente paso |
| Modo de falla | Baja clasificación o rebote | Acción incorrecta, tarea estancada, sin seguimiento de auditoría |
| Medición | Impresiones, clics, interacción | Llamadas de herramientas, aprobaciones, finalizaciones, errores |

Ambas capas importan. Un sitio que sólo optimiza páginas puede ser citado pero fracasar cuando un agente intenta actuar.## Lista de verificación de implementación

1. Mapee sus cinco tareas de usuario principales.
2. Convierta cada tarea en un flujo de trabajo documentado.
3. Defina las entradas requeridas, las entradas opcionales y los errores.
4. Agregue la aprobación humana antes de las acciones arriesgadas.
5. Registre las acciones de los agentes por separado de los clics humanos.
6. Haga que las páginas de estado y confirmación sean legibles por máquina.
7. Pruebe tareas con automatización del navegador y herramientas estilo MCP.

Para obtener una lista de verificación más amplia, utilice [Cómo preparar aplicaciones web para agentes](/es/docs/agent-ready-web-apps/) y [MCP vs API para agentes](/es/docs/mcp-vs-api-for-agents/).

## Preguntas frecuentes

### ¿Se requiere Genkit para AEO?

No. AEO es independiente del marco. Genkit es útil porque refleja cómo una importante plataforma de desarrollo espera que se construyan los agentes.

### ¿La producción de la API de agentes es estable?

Google describe la API de agentes como una vista previa de TypeScript y Go en el anuncio de julio de 2026, por lo que los equipos deben tratar las interfaces como sujetas a cambios.

### ¿Qué deberían sacar los especialistas en marketing de Genkit?

Las aplicaciones agentes necesitan tareas claras, no sólo contenido. Las páginas de marketing deben conectarse a formularios, catálogos, API o flujos de trabajo que los agentes puedan utilizar de forma segura.

### ¿Esto reemplaza a MCP?

No. Genkit es un marco de aplicación. MCP es un protocolo para conectar modelos a herramientas y contexto. Pueden ser complementarios.

## Fuentes

Fuente principal: [Blog de desarrolladores de Google: cree aplicaciones agentes de pila completa con Genkit](https://developers.googleblog.com/build-agentic-full-stack-apps-with-genkit/). Contexto relacionado: [Documentación del protocolo de contexto del modelo](https://modelcontextprotocol.io/docs/getting-started/intro).