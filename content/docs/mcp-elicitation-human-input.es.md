---
title: "Obtención de MCP: aportación humana para flujos de trabajo."
date: 2026-05-23
weight: 134
category: "Architecture"
description: "MCP Elicitation permite a los servidores solicitar entradas estructuradas del usuario a través del cliente. Aprenda cuándo ayuda, qué no debe pedir y cómo."
summary: "Una guía práctica para la obtención de MCP, la entrada estructurada del usuario, aceptar/rechazar/cancelar flujos, diseño humano en el circuito e implicaciones del flujo de trabajo AEO."
keywords:
  - Elicitación de MCP
  - provocar/crear
  - agentes humanos en el circuito
  - Entrada del usuario MCP
  - seguridad del flujo de trabajo del agente
---
# Obtención de MCP: aportación humana para flujos de trabajo de agentes más seguros

MCP Elicitation permite que un servidor MCP solicite información estructurada del usuario a través del cliente mientras se ejecuta un flujo de trabajo. Es útil cuando un agente necesita detalles que faltan, pero no debe usarse para información confidencial. Un buen diseño de obtención hace que los flujos de trabajo de los agentes sean más seguros porque los usuarios pueden aceptar, rechazar o cancelar solicitudes en lugar de tener que pasar por una automatización oculta.

## ¿Qué es la obtención de MCP?

La [especificación de obtención de MCP] oficial (https://modelcontextprotocol.io/docs/concepts/elicitation) describe una forma estándar para que los servidores soliciten información adicional del usuario a través del cliente. Los servidores envían una solicitud `elicitation/create` con un mensaje y un esquema JSON restringido para la respuesta esperada.

El usuario puede responder de tres formas:

- aceptar con datos
- declive
- cancelar

Ese modelo de respuesta simple importa. Le brinda al cliente una forma clara de mantener el control del usuario.

Para conocer la arquitectura relacionada, lea [MCP vs API para agentes](/es/docs/mcp-vs-api-for-agents/), [UX del agente y diseño humano en el bucle](/es/docs/agent-ux-human-in-the-loop/) y [Autorización de MCP con OAuth](/es/docs/mcp-authorization-oauth-ai-agents/).

## Por qué existe la elicitación

Los agentes suelen comenzar con instrucciones incompletas. Es posible que a un servidor le falte un campo antes de poder completar una tarea.

Ejemplos:

- "¿A qué proyecto debería asignarse este número?"
- "¿Qué fecha debe cubrir el informe?"
- "¿Qué dirección de envío se debe utilizar?"
- "¿A qué entorno debería apuntar la implementación?"
- "¿Qué proveedor aprobado debe utilizar el pedido?"

Sin un flujo de entrada estándar, los servidores pueden inventar patrones de avisos inconsistentes o pedirle al modelo que adivine. La elicitación le da a esta interacción un camino estructurado.

## Elicitación versus preguntas de chat normales

| Característica | Pregunta de chat normal | Obtención de MCP |
|
---|
---|
---|
| Solicitar origen | Asistente o usuario | Servidor MCP a través del cliente |
| Formato de respuesta | Texto libre | Esquema estructurado |
| Opciones de usuario | Normalmente responde o ignora | Aceptar, rechazar, cancelar |
| Validación | Dependiente del modelo | El cliente puede validar campos |
| Postura de seguridad | Varía | Spec advierte contra solicitudes de datos confidenciales |

La elicitación no es simplemente "hacerle una pregunta al usuario". Es una solicitud estandarizada de entrada estructurada dentro del flujo de trabajo de un agente.

## Qué servidores no deben solicitar

La especificación MCP dice que los servidores no deben utilizar la obtención para solicitar información confidencial. En la práctica, evite solicitar:

- contraseñas
- claves privadas
- números de tarjetas de pago
- códigos de acceso de un solo uso
- tokens de acceso sin procesar
- datos personales confidenciales
- secretos que pertenecen a una bóveda seguraSi un flujo de trabajo necesita una autorización confidencial, utilice un flujo de autenticación adecuado, no una obtención. La [capa de ejecución](/es/docs/execution-layer/) depende de límites confiables.

## Buenos casos de uso

| Caso de uso | Buen campo de obtención | Mal campo de obtención |
|
---|
---|
---|
| Triaje de apoyo | Nivel de prioridad | Contraseña de cliente |
| Implementación | Entorno objetivo | Clave raíz de la nube |
| Adquisiciones | Proveedor aprobado | Número de tarjeta completo |
| Publicación de contenidos | Categoría de artículo | Contraseña de administrador de CMS |
| Planificación de viajes | Aeropuerto preferido | Escaneo de pasaporte |

El patrón es simple: provocar preferencias y elecciones no sensibles, no secretos.

## Implicaciones AEO

La obtención es importante para las empresas legibles por agentes porque no todas las acciones pueden ser completamente autónomas. A veces, la mejor experiencia de usuario es una pausa clara:

"Puedo continuar, pero necesito una opción aprobada".

Los sitios web y API que se preparen para esto pueden publicar:

- requisitos de acción claros
- valores de parámetros permitidos
- reglas de confirmación
- caminos de escalada
- ejemplos de entradas válidas
- mensajes de error que los agentes pueden entender

Esto convierte formas humanas vagas en flujos de trabajo compatibles con agentes. La guía [sitios web de programación para agentes de IA](/es/docs/programming-websites-for-ai-agents/) cubre más de ese trabajo de preparación.

## Lista de verificación de diseño

1. Pregunta sólo por la información mínima que falta.
2. Muestra qué servidor está solicitando la información.
3. Utilice etiquetas que los usuarios puedan entender.
4. Validar los insumos antes de enviarlos.
5. Ofrezca opciones de rechazo y cancelación.
6. Nunca solicites secretos mediante la obtención de secretos.
7. Registre el tipo de solicitud, el servidor y el resultado.
8. Mantenga las acciones de alto riesgo detrás de la confirmación.

## Preguntas frecuentes

### ¿La obtención de MCP es un formulario?

Puede generar una interfaz de usuario similar a un formulario, pero el protocolo en sí define el patrón estructurado de solicitud y respuesta, no una interfaz específica.

### ¿Puede la Elicitación solicitar objetos anidados?

La especificación limita los esquemas a estructuras planas más simples con valores primitivos. Esto hace que la implementación del cliente sea más fácil y segura.

### ¿Debería Elicitación recopilar los detalles de pago?

No. Las credenciales de pago y otros secretos deben utilizar autorización o flujos de pago seguros, no obtención.

### ¿Por qué esto es importante para los propietarios de sitios web?

Los flujos de trabajo listos para los agentes necesitan momentos claros en los que los agentes puedan preguntar a los humanos las opciones que faltan en lugar de adivinar. La elicitación le da a ese patrón una forma estándar.

## Conclusión

MCP Elicitation es una pequeña característica con una gran lección de diseño: los agentes seguros deben preguntar claramente cuándo necesitan la participación humana y los usuarios deben tener una opción real para decir que no.