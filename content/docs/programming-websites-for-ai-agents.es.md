---
title: "Cómo programar sitios web para agentes de IA: 5 elementos."
metaTitle: "Cómo programar sitios web para agentes de IA."
date: 2026-04-12
weight: 60
category: "Architecture"
description: "Prepare su sitio web para agentes con llms.txt, especificaciones OpenAPI, puntos finales MCP, HTML semántico y tarjetas de agente. Incluye sandboxing."
metaDescription: "Prepare los sitios web para agentes con llms.txt, OpenAPI, puntos finales MCP, HTML semántico, tarjetas de agente y patrones seguros para producción."
summary: "Los sitios web están preparados para los agentes agregando llms.txt para descubrimiento, especificaciones OpenAPI con descripciones fáciles de usar para los agentes, servidores MCP para acceso dinámico a herramientas, HTML semántico para extracción y tarjetas de agente para colaboración A2A."
keywords:
  - Programación de sitios web para agentes de IA.
  - Implementación de llms.txt
  - Configuración del servidor MCP
  - tarjeta de agente json
  - desarrollo de sitios web listo para agentes
  - Puntos finales del agente WebSocket
---
Los sitios web están preparados para los agentes al agregar API REST claras, llms.txt, puntos finales MCP, HTML semántico y capas de seguridad para que los agentes autónomos de IA puedan descubrir, comprender y actuar sin código adhesivo personalizado. A continuación se presentan los cinco elementos técnicos esenciales más dos patrones emergentes que los sistemas de producción necesitarán en 2026.

## 1. Cree llms.txt como mapa del sitio del agente

Coloque un archivo Markdown en /llms.txt en la raíz de su sitio. Tiene el mismo propósito para los agentes de IA que el archivo robots.txt para los rastreadores de búsqueda: le dice al agente qué ofrece su sitio, dónde encontrarlo y cómo interactuar con él.

Un llms.txt útil incluye el nombre de su producto o servicio y una descripción de una oración, una lista de páginas clave con su propósito, puntos finales API disponibles con descripciones breves, requisitos de autenticación y cualquier restricción o límite de velocidad.

Los agentes buscan llms.txt antes de rastrear el sitio completo. Un sitio sin uno obliga al agente a adivinar qué hay disponible. Un sitio con un llms.txt claro y actualizado se descubre más rápido y se comprende con mayor precisión.

Mantenlo actualizado. Un llms.txt que describe puntos finales que ya no existen daña la confianza más que no tener ningún llms.txt. La [guía de programación llms.txt](/es/docs/programming-llms-txt/) cubre el formato en detalle.

## 2. Escriba especificaciones de OpenAPI con descripciones fáciles de usar para los agentes

Si su sitio expone puntos finales de API, documentelos con especificaciones de OpenAPI que incluyan ejemplos completos de solicitudes y respuestas, esquemas de error detallados con códigos y mensajes de error específicos, reglas de validación de entrada con tipos, rangos y campos obligatorios, y descripciones en lenguaje sencillo de lo que hace cada punto final y cuándo usarlo.

La mayoría de las especificaciones de OpenAPI están escritas para desarrolladores humanos que pueden inferir el contexto faltante. Los agentes no pueden inferir. Necesitan documentar cada parámetro, describir cada caso de error y hacer explícita cada restricción.

Un error común es escribir descripciones concisas de una sola línea como "Crea una reserva". Una descripción fácil de usar para el agente dice "Crea una reserva para la fecha y hora especificadas. Requiere una fecha válida en formato ISO 8601, un intervalo de tiempo desde el extremo de los espacios disponibles y un correo electrónico de contacto. Devuelve un objeto de confirmación con el ID de la reserva y la fecha límite de cancelación. Falla con 409 si el espacio ya está ocupado".

## 3. Implementar un servidor MCP para el descubrimiento dinámico de herramientas

El Protocolo de contexto modelo (MCP) es el estándar emergente sobre cómo los agentes de IA descubren y llaman a las herramientas. En lugar de codificar integraciones para cada plataforma de IA, expone sus capacidades a través de un único servidor MCP que cualquier agente compatible puede descubrir y utilizar.MCP utiliza JSON-RPC 2.0 para la comunicación. Su servidor anuncia herramientas disponibles (funciones que el agente puede llamar), recursos (datos que el agente puede leer) y avisos (plantillas que el agente puede usar). Los agentes descubren estas capacidades dinámicamente en tiempo de ejecución.

Un servidor MCP mínimo expone sus acciones comerciales principales como herramientas: verificar disponibilidad, obtener precios, crear reservas, enviar consultas. Cada herramienta tiene un esquema escrito que define entradas y salidas.

La inversión es modesta. Un servidor MCP básico en Python o Node.js tarda de 2 a 4 horas en construirse para un sitio con de 3 a 5 acciones principales. El beneficio es que cada agente compatible con MCP puede interactuar inmediatamente con su sitio.

## 4. Utilice HTML semántico que sobreviva sin JavaScript

Los agentes normalmente no ejecutan JavaScript. Obtienen el HTML sin formato y extraen información de la estructura del documento. Si su contenido crítico se representa en el lado del cliente a través de React, Vue o Angular sin representación en el lado del servidor, los agentes ven una página vacía.

Utilice elementos HTML nativos con una semántica clara. Elementos de botón para acciones, elementos de formulario para entradas, elementos de tabla para datos estructurados, elementos de encabezado para jerarquía. Agregue atributos aria-label cuando el propósito del elemento no sea obvio a partir de su contenido.

El servidor procesa toda la información crítica. Los nombres de los productos, los precios, la disponibilidad, las especificaciones y los datos de contacto deben estar en la respuesta HTML inicial, no cargados de forma asincrónica.

Pruebe recuperando su página con curl y verificando si la información esencial es visible en la respuesta. Si no es así, los agentes tampoco podrán verlo.

## 5. Publicar una tarjeta de agente para la colaboración A2A

Una tarjeta de agente es un archivo JSON (agent-card.json) ubicado en la raíz de su sitio que describe las capacidades de su sitio, los requisitos de autenticación y los protocolos admitidos para la comunicación de agente a agente.

El protocolo A2A (Agente a Agente) utiliza Tarjetas de Agente para el descubrimiento. Cuando un agente necesita encontrar un servicio, verifica la Tarjeta de Agente para determinar si el sitio puede ayudar, qué capacidades están disponibles y cómo autenticarse.

Una tarjeta de agente básica incluye el nombre y la descripción de su servicio, protocolos admitidos (MCP, REST, A2A), capacidades disponibles como lista estructurada, método de autenticación y punto final, e información de contacto para informes de errores.

La publicación de una tarjeta de agente duplica su capacidad de descubrimiento en flujos de trabajo de múltiples agentes porque los agentes que descubren su sitio pueden recomendarlo a otros agentes en el mismo flujo de trabajo.

La [Tarjetas de agente y guía A2A] (/docs/agent-cards-a2a-protocol/) cubre la especificación completa.

## Patrón emergente: zona de pruebas de agentesLos sistemas de agentes de producción necesitan aislamiento. Cuando un agente externo ejecuta código o procesa datos en su infraestructura, necesita contención.

El sandboxing basado en WASM (similar a Cloudflare Workers) permite a los agentes ejecutar operaciones que no son de confianza en entornos aislados con límites de recursos definidos. Esto evita que un agente con mal comportamiento afecte a otros usuarios o consuma recursos ilimitados.

Para la mayoría de los sitios, el sandboxing no es un requisito del primer día. Se vuelve importante cuando expone puntos finales de ejecución que aceptan entradas complejas o cuando varios agentes externos interactúan con su sistema simultáneamente.

## Patrón emergente: puntos finales WebSocket en tiempo real

Las API REST estándar funcionan para interacciones únicas de solicitud-respuesta. Los flujos de trabajo de agentes de varios pasos se benefician de las conexiones WebSocket que mantienen el estado durante toda la sesión.

Un punto final WebSocket en /ws/agent-session permite a un agente mantener una conexión persistente para flujos de trabajo que involucran múltiples pasos secuenciales: verificar la disponibilidad, seleccionar opciones, confirmar detalles y completar la transacción. Cada paso ocurre a través de la misma conexión con el estado de sesión compartido.

Esto evita el comportamiento inusual que se produce cuando los agentes realizan varias llamadas REST independientes y pierden el contexto entre ellas.

## Comparación: arquitectura tradicional versus arquitectura optimizada para agentes

| Aspecto | Sitio web tradicional | Sitio web optimizado para agentes |
|
---|
---|
---|
| Descubrimiento | robots.txt y mapa del sitio | llms.txt más Tarjeta de agente más registro MCP |
| Interacción | UI humana basada en navegador | MCP más REST más WebSocket |
| Seguridad | Claves API estáticas | Autenticación específica del agente más cuotas por agente |
| Entrega de datos | HTML para renderizado | JSON estructurado más HTML semántico |
| Métrica de éxito | Vistas de página y clics | Finalización y retención de tareas de agentes |

La [guía de capa de ejecución] (/docs/execution-layer/) explica los principios arquitectónicos. La [guía de implementación de AEO] (/docs/implement-aeo/) cubre la ruta de optimización completa.

---

## Preguntas frecuentes

**¿Necesito los cinco elementos para estar listo para ser agente?**
Comience con llms.txt y HTML semántico (la capa de lectura). Agregue especificaciones de OpenAPI y MCP cuando tenga puntos finales de API. Agregue la Tarjeta de Agente cuando desee visibilidad A2A.

**¿Cuánto tiempo lleva implementar un servidor MCP básico?**
De dos a cuatro horas para un sitio con de 3 a 5 acciones principales, suponiendo que tenga puntos finales de API existentes para ajustar.

**¿Seguirán funcionando los agentes sin un servidor MCP?**
Sí, mediante API REST y extracción de HTML estructurado. MCP hace que el descubrimiento y la interacción sean más estandarizados y confiables, pero no es el único camino.

**¿Es necesaria la compatibilidad con WebSocket para sitios web sencillos?**No. Los WebSockets son importantes para los flujos de trabajo transaccionales de varios pasos. Los sitios de contenido simple y los puntos finales de acción única funcionan bien con REST estándar.

**¿Cómo pruebo si mi sitio está listo para agentes?**
Recupera tus páginas con curl (sin JavaScript). Verifique su llms.txt para verificar la precisión. Valide su especificación OpenAPI. Pruebe su servidor MCP con un cliente compatible. Haga preguntas a los asistentes de IA que su sitio debería responder.

## Referencias primarias

* [Marco de gestión de riesgos de IA del NIST](https://www.nist.gov/itl/ai-risk-management-framework)
* [Documentación de Schema.org](https://schema.org/docs/documents.html)