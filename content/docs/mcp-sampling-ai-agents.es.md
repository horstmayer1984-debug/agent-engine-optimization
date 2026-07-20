---
title: "Explicación del muestreo de MCP: cómo los servidores solicitan."
date: 2026-05-23
weight: 133
category: "Architecture"
description: "MCP Sampling permite a los servidores solicitar generaciones de modelos a través de un cliente. Descubra cómo funciona, dónde ayuda y por qué es importante."
summary: "Una explicación práctica para MCP Sampling, que cubre generaciones de LLM solicitadas por el servidor, control del cliente, preferencias de modelo, seguridad e implicaciones de AEO."
keywords:
  - Muestreo MCP
  - muestreo/crearmensaje
  - Muestreo del protocolo de contexto del modelo
  - Arquitectura del agente de IA
  - Servidores MCP
---
# Explicación del muestreo de MCP: cómo los servidores solicitan la salida del modelo de IA

MCP Sampling permite que un servidor MCP solicite al cliente que genere resultados del modelo durante un flujo de trabajo. El servidor no necesita su propia clave API modelo. El cliente mantiene el control sobre el acceso al modelo, los permisos, la revisión y la entrega final. Esto hace que el muestreo sea útil para flujos de trabajo agentes, pero riesgoso si las indicaciones y los resultados generados no se muestran claramente al usuario.

## ¿Qué es el muestreo MCP?

La [especificación de muestreo de protocolo de contexto de modelo] oficial (https://modelcontextprotocol.io/docs/concepts/sampling) describe el muestreo como una forma para que los servidores soliciten generaciones de LLM a partir de modelos de lenguaje a través de clientes. En la revisión del protocolo 2025-06-18, los clientes que lo admiten declaran una capacidad `sampling` y los servidores solicitan una generación a través de `sampling/createMessage`.

Eso suena abstracto, así que aquí está la versión simple: un servidor de herramientas puede pedirle al cliente de IA del usuario que piense, resuma, clasifique o genere texto como parte de un flujo de herramientas.

Para un contexto más amplio, consulte [MCP vs API para agentes](/es/docs/mcp-vs-api-for-agents/), [Autorización de MCP con OAuth](/es/docs/mcp-authorization-oauth-ai-agents/) y [Aplicaciones MCP](/es/docs/mcp-apps-guide/).

## Por qué existe el muestreo

Sin muestreo, un servidor MCP tiene dos opciones limitadas:

- devolver datos sin procesar y esperar que el modelo del cliente sepa qué hacer
- llamar directamente a su propio proveedor de modelo, lo que plantea problemas de costos, privacidad y administración de claves

El muestreo crea un camino intermedio. El servidor puede solicitar trabajo modelo, pero el cliente sigue siendo el guardián.

## Muestreo versus herramientas versus recursos

| Función MCP | ¿Quién lo controla? Propósito principal | Ejemplo |
|
---|
---|
---|
---|
| Herramientas | El modelo invoca la acción del servidor | Ejecutar una capacidad | "Crear un ticket" |
| Recursos | El servidor expone el contexto | Proporcionar datos para el modelo | "Leer esquema del proyecto" |
| Indicaciones | Servidor expone plantillas | Guíe un flujo de trabajo controlado por el usuario | "Ejecutar mensaje de revisión de código" |
| Muestreo | El servidor solicita la salida al modelo del cliente | Generar o razonar durante un flujo de trabajo | "Resumir este documento recuperado" |

El muestreo no reemplaza las herramientas. Es una forma de anidar la generación de modelos dentro de una capacidad.

## Casos de uso de ejemplo

El muestreo puede ayudar cuando un servidor necesita resultados de modelo de lenguaje pero no debería ser propietario de la relación del modelo.

Los patrones útiles incluyen:

- resumir los documentos recuperados
- redactar una respuesta después de que una herramienta obtenga datos
- clasificar tickets de soporte
- generar una explicación en lenguaje natural a partir de datos estructurados
- pedir al modelo de cliente que transforme el contexto proporcionado por el usuario
- opciones de puntuación basadas en criterios visibles para el usuarioPara AEO, esto es importante porque los sitios web y las API legibles por agentes pueden necesitar admitir flujos de trabajo que combinen recuperación, ejecución y explicación.

## Requisitos de seguridad y revisión

La especificación de muestreo enfatiza la revisión humana. Las aplicaciones deben facilitar la revisión de las solicitudes de muestra, editar las solicitudes antes de enviarlas y revisar las respuestas generadas antes de la entrega.

Ésa es una exigencia seria. De lo contrario, el muestreo puede convertirse en una llamada de modelo oculta activada por un servidor que el usuario apenas comprende.

| Riesgo | Por qué es importante | Barandilla |
|
---|
---|
---|
| Inyección rápida oculta | El servidor puede incluir instrucciones no seguras | Mostrar indicaciones antes de la ejecución |
| Fuga de datos | El contexto puede contener información confidencial | Permitir a los usuarios revisar el contexto compartido |
| Sorpresas de costos | Las llamadas de modelos pueden consumir tokens pagados | Modelo de visualización y política de costes |
| Salida incorrecta | La respuesta generada puede ser inexacta | Revisión antes de la entrega final |
| Exceso de alcance del servidor | El servidor puede solicitar trabajo de modelo innecesario | Requerir soporte de capacidad explícito |

La guía [barandillas de observabilidad del agente](/es/docs/agent-observability-guardrails/) amplía esta capa de gobernanza.

## Implicaciones AEO

MCP Sampling recompensa el contexto limpio. Si sus documentos, respuestas de API, datos de productos o descripciones de flujo de trabajo son vagos, el modelo de cliente tiene un trabajo más difícil. Si están estructurados, concisos y vinculados internamente, los flujos de trabajo basados ​​en muestreo pueden producir mejores respuestas posteriores.

Para los propietarios de sitios web, esto significa:

- publicar definiciones claras
- mantener estructuradas las respuestas de la API
- exponer documentos legibles por máquina
- evitar enterrar limitaciones importantes en prosa
- documentar páginas de fuente de verdad
- proporcionar identificadores estables para entidades y acciones

La [guía para desarrolladores de AEO](/es/docs/developers-guide-aeo/) es el siguiente paso natural.

## Preguntas frecuentes

### ¿MCP Sampling permite que un servidor llame a cualquier modelo que desee?

No. El cliente controla el acceso al modelo. El servidor puede expresar preferencias, pero el cliente decide qué está disponible y permitido.

### ¿Se requiere muestreo para los servidores MCP?

No. Es una capacidad del cliente. Muchos flujos de trabajo de MCP pueden utilizar herramientas, recursos e indicaciones sin muestreo.

### ¿Es seguro el muestreo para la producción?

Se puede utilizar con cuidado, pero necesita una revisión rápida, una revisión del contexto, registros, límites de permisos y valores predeterminados sensatos.

### ¿Por qué es importante el muestreo para los AEO?

Muestra que los flujos de trabajo de los agentes pueden pedir a los modelos que razonen sobre su contenido durante la ejecución, no solo que recuperen páginas. El contenido estructurado y respaldado por fuentes se vuelve más útil.

## ConclusiónMCP Sampling es un puente útil entre la ejecución de herramientas y el razonamiento del modelo. Trátelo como una capacidad controlada, no como un atajo en segundo plano.