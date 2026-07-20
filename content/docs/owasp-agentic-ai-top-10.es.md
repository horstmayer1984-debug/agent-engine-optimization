---
title: "OWASP Agentic AI Top 10 y seguridad AEO."
date: 2026-05-17
weight: 117
category: "Guide"
description: "OWASP Agentic AI Top 10 explica los riesgos de los agentes autónomos. Descubra cómo los equipos AEO deben manejar la agencia, las herramientas, la memoria."
summary: "Una guía práctica de seguridad AEO basada en OWASP Top 10 para Aplicaciones Agentic, con controles para herramientas, memoria, identidad, permisos y monitoreo."
keywords:
  - Top 10 de IA agente de OWASP
  - seguridad de IA agente
  - Seguridad AEO
  - Riesgos de los agentes de IA
  - gobernanza de agentes autónomos
---
# OWASP Agentic AI Top 10 y seguridad AEO

OWASP Agentic AI Top 10 es importante para AEO porque los sitios web listos para agentes exponen acciones, herramientas, API, memoria y pagos. Esas capacidades crean valor sólo si se controlan. Un sitio que permite a los agentes actuar sin autorización, límites, supervisión y rutas de recuperación no está preparado para los agentes. Está simplemente expuesto.

## Lo que publicó OWASP

El proyecto Gen AI Security de OWASP publicó el Top 10 de aplicaciones agentes 2026 como marco para riesgos de seguridad en sistemas de IA autónomos y agentes. Está dirigido a sistemas que planifican, actúan y toman decisiones en todos los flujos de trabajo.

Fuentes primarias:

- [OWASP Top 10 para aplicaciones agentes 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [Marco de gestión de riesgos de IA del NIST](https://www.nist.gov/itl/ai-risk-management-framework)
- [Seguridad de Microsoft: OWASP Los 10 riesgos principales en IA agente](https://www.microsoft.com/en-us/security/blog/2026/03/30/addressing-the-owasp-top-10-risks-in-agentic-ai-with-microsoft-copilot-studio/)

## Por qué esto pertenece al AEO

La [capa de ejecución](/es/docs/execution-layer/) permite a los agentes hacer cosas: reservar, comprar, actualizar, recuperar, comparar y activar flujos de trabajo. Precisamente por eso es importante la seguridad.

El riesgo tradicional del SEO es principalmente la reputación y la indexación. El riesgo AEO incluye:

- acciones no autorizadas
- agencia excesiva
- mal uso de herramientas
- envenenamiento de la memoria
- fuga de contexto
- delegación insegura
- errores de pago
- cambios de estado irreversibles

El objetivo no es evitar el acceso de los agentes. El objetivo es exponer las acciones correctas con los controles correctos.

## Mapa de control de seguridad AEO

| Superficie AEO | Pregunta de seguridad | Control mínimo |
|
---|
---|
---|
| Contenido público | ¿Pueden los agentes confiar en él? | Fuentes, fechas, claridad de entidad |
| llms.txt | ¿Guía a los agentes de forma segura? | Enlace sólo recursos estables y relevantes |
| Herramientas MCP | ¿Quién puede llamarlos? | Autorización y alcances |
| Herramientas WebMCP | ¿Pueden los agentes del navegador hacer un mal uso de los formularios? | Confirmaciones y validaciones |
| Puntos finales de pago | ¿Se puede escapar el gasto? | Presupuestos, idempotencia, recibos |
| Memoria del agente | ¿Puede persistir el contexto malicioso? | Aislamiento y caducidad |
| Registros | ¿Se pueden auditar las acciones? | ID de agente, ID de usuario, herramienta, resultado |

La [guía de observabilidad del agente](/es/docs/agent-observability-guardrails/) cubre el monitoreo con más profundidad.

## Agencia excesiva

La agencia excesiva ocurre cuando un agente puede hacer más de lo que el usuario o la empresa pretendía. En términos AEO, esta es la diferencia entre "consultar disponibilidad" y "reservar y pagar sin confirmación".

Utilice permisos limitados:

- sólo lectura antes de escribir
- cotización antes de la compra
- solicitud antes de la confirmación
- caja de arena antes de la producción
- aprobación humana ante acciones irreversibles

La [guía de autorización de MCP] (/docs/mcp-authorization-oauth-ai-agents/) explica cómo los alcances ayudan a mantener las herramientas limitadas.

## Riesgos de herramientas y flujo de trabajoLas herramientas de los agentes deben diseñarse como API de producción, no como atajos de demostración.

Un buen diseño de herramientas incluye:

- entradas mecanografiadas
- salidas escritas
- borrar mensajes de error
- validación de entrada
- claves de idempotencia
- límites de tarifas
- reglas de reintento
- registro de auditoría
- acceso con privilegios mínimos

Si una herramienta puede gastar dinero, cambiar datos de clientes o desencadenar un proceso legal, necesita controles más estrictos que un punto final de contenido público.

## Riesgos de memoria y contexto

Los agentes pueden transmitir contexto a través de tareas. Eso crea conveniencia y riesgo.

Los problemas incluyen:

- memoria envenenada por contenido malicioso
- instrucciones obsoletas
- fuga entre clientes
- instrucciones ocultas en el contenido recuperado
- datos de políticas obsoletos

Para los AEO, las páginas públicas deben escribirse de modo que los agentes puedan distinguir hechos, afirmaciones de marketing, instrucciones y limitaciones. No oculte instrucciones operativas dentro del contenido decorativo.

## Señales de confianza de cara al agente

Las señales de confianza deben ser visibles tanto para los humanos como para las máquinas:

- identidad organizacional clara
- página de contacto
- política de privacidad
- página de seguridad o cumplimiento cuando sea relevante
- actualizar fechas para contenido sensible
- enlaces de origen para afirmaciones fácticas
- permisos de herramientas documentados
- página de estado o información de salud de API

La [auditoría de preparación de AEO](/es/docs/audit/) debe incluir controles de seguridad antes de que se active cualquier flujo de trabajo de agentes de alto riesgo.

## Preguntas frecuentes

### ¿OWASP Agentic AI Top 10 es solo para desarrolladores?

No. Es útil para los equipos de producto, seguridad, legal y SEO/AEO porque la exposición de los agentes afecta el contenido, las herramientas, los flujos de trabajo y la gobernanza.

### ¿Cuál es el mayor error de seguridad de AEO?

Brindar a los agentes amplio acceso de escritura antes de diseñar alcances, confirmaciones, límites y registros.

### ¿La seguridad reduce la visibilidad de los agentes?

Una buena seguridad puede mejorar la confianza. Los agentes prefieren sistemas con permisos predecibles y errores recuperables.

### ¿Toda acción de un agente debería requerir la aprobación humana?

No. Las acciones de bajo riesgo pueden ser automáticas. Las acciones de alto riesgo, costosas, reguladas o irreversibles deberían requerir una confirmación más firme.

### ¿Cómo deberían empezar los equipos?

Haga un inventario de cada acción de los agentes, clasifique los riesgos y luego agregue controles antes de expandir el acceso a la capa de ejecución.