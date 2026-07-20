---
title: "UCP, ACP y MCP: los tres protocolos que impulsarán."
metaTitle: "UCP vs ACP vs MCP: comparación de protocolos."
date: 2026-04-14
weight: 90
category: "Framework"
description: "MCP proporciona contexto, UCP maneja los ciclos de vida del comercio, ACP permite el pago nativo de ChatGPT. En qué se diferencian los tres protocolos."
metaDescription: "Compare MCP, UCP y ACP en el intercambio de contexto, los ciclos de vida del comercio, el pago, el uso de herramientas y cuándo encaja cada protocolo."
summary: "Tres protocolos dominarán la infraestructura de agentes en 2026. MCP conecta a los agentes con los datos. UCP maneja todo el ciclo de vida del comercio. ACP permite el pago dentro de ChatGPT. Aquí es cuando usar cada uno."
keywords:
  - UCP frente a ACP frente a MCP
  - protocolos de comercio de agentes
  - Protocolo de comercio universal
  - Protocolo de comercio agente
  - Comparación del protocolo de contexto del modelo
  - pila de protocolos de agente 2026
---
Tres protocolos dominan la capa de infraestructura de Agent Engine Optimization en 2026. Cada uno resuelve un problema diferente. Elegir el incorrecto hace perder tiempo de desarrollo. Elegir la combinación correcta brinda a los agentes un camino completo desde el acceso a los datos hasta la finalización de la transacción.

MCP (Protocolo de contexto modelo) conecta a los agentes con sus datos. UCP (Protocolo de comercio universal) maneja el ciclo de vida completo del comercio. ACP (Protocolo de comercio agente) permite el pago directo dentro de ChatGPT sin que el comprador visite su sitio.

## MCP: brindando a los agentes acceso a sus datos y herramientas

Anthropic desarrolló MCP y lo trasladó a la Fundación Linux. Es un protocolo de integración vertical. Un servidor MCP expone sus fuentes de datos internas, documentos y herramientas a agentes de IA a través de una interfaz JSON-RPC estandarizada.

MCP responde una pregunta: ¿qué me puede decir este sistema y qué herramientas puedo utilizar? Permite a los agentes consultar su CMS, recuperar documentos, verificar registros de bases de datos y llamar a funciones internas. No maneja pagos, flujos de pago ni transacciones comerciales por sí solo.

Utilice MCP cuando los agentes necesiten acceder a los datos de su empresa (catálogos de productos, documentación, bases de conocimiento), cuando desee que cualquier agente compatible con MCP descubra y utilice sus herramientas sin una integración personalizada y cuando la interacción sea de lectura o de consultas en lugar de transaccional.

La implementación técnica es un servidor JSON-RPC 2.0 que anuncia herramientas (funciones que los agentes pueden llamar), recursos (datos que los agentes pueden leer) y mensajes (plantillas que los agentes pueden usar). La [guía MCP vs API] (/docs/mcp-vs-api-for-agents/) cubre la implementación en detalle.

## UCP: gestionar el ciclo de vida completo del comercio

Google desarrolló UCP en asociación con Shopify, Target, Walmart, Etsy y Wayfair. Se lanzó en NRF en enero de 2026. UCP es el protocolo para todo el ciclo de vida del comercio: verificación de inventario, negociación de precios, autorización de pago, envío de pedidos y seguimiento de cumplimiento.

La innovación técnica más importante es la Declaración de Capacidad. Su tienda publica un archivo de manifiesto JSON en /.well-known/ucp que les indica a los agentes exactamente qué transacciones, descuentos, métodos de pago y políticas admite. El agente lee este manifiesto antes de intentar cualquier interacción, por lo que nunca tiene que adivinar.

UCP trabaja con el Protocolo de pagos de agentes (AP2) para mandatos de pago criptográfico y pistas de auditoría. Juntos, permiten a los agentes verificar el inventario, validar precios, autorizar pagos, enviar pedidos y realizar un seguimiento del cumplimiento a través de un único flujo estandarizado.Utilice UCP cuando venda productos o servicios a través de una tienda, cuando desee que los agentes que operan en Google AI Mode o Gemini realicen transacciones con usted y cuando necesite el ciclo de vida completo de la compra, desde el descubrimiento hasta la confirmación del cumplimiento.

El [artículo sobre ejecución de comercio agente] (/docs/agentic-commerce-execution/) explica cómo funciona UCP en arquitecturas de comercio electrónico.

## ACP: pago dentro de ChatGPT

OpenAI desarrolló ACP en asociación con Stripe. Es un protocolo de código abierto diseñado específicamente para minimizar la fricción al manejar el pago directamente dentro de la interfaz ChatGPT.

El mecanismo clave es SharedPaymentToken. Las credenciales de pago del comprador se comparten de forma segura con el comerciante sin que el comprador abandone ChatGPT. El agente maneja la selección de productos, el protocolo ACP maneja el intercambio seguro de tokens de pago y la transacción se completa de forma nativa dentro de la conversación.

Utilice ACP cuando su principal canal de ventas impulsado por agentes sea ChatGPT, cuando desee realizar un pago sin redireccionamiento (el comprador nunca visita su sitio web) y cuando utilice Stripe como procesador de pagos (ACP se integra de forma nativa con la infraestructura de Stripe).

## Cómo funcionan juntos los tres protocolos

Los protocolos no son competidores. Sirven diferentes capas de la misma pila.

MCP proporciona la capa de datos. Un agente utiliza MCP para acceder a su catálogo de productos, verificar especificaciones y recuperar documentación.

UCP proporciona la capa comercial. Una vez que el agente tiene los datos que necesita, UCP maneja la transacción: reserva de inventario, validación de precios, autorización de pago y envío de pedidos.

ACP proporciona la capa de interfaz específicamente para ChatGPT. Envuelve la experiencia de pago dentro de la conversación ChatGPT utilizando tokens de pago seguros.

Una infraestructura completa lista para agentes podría utilizar los tres: MCP para acceso a datos, UCP para el ciclo de vida comercial en flujos de trabajo de agentes impulsados ​​por Google y ACP para transacciones nativas de ChatGPT.

## Comparación de protocolos

| Aspecto | PCM | UCP | ACP |
|
---|
---|
---|
---|
| Desarrollador | Antrópico (Fundación Linux) | Google con Shopify y socios | OpenAI con raya |
| Propósito principal | Acceso a datos y herramientas | Ciclo de vida completo del comercio | Pago en el chat |
| Base técnica | JSON-RPC 2.0 | Declaración de Capacidad más AP2 | Token de pago compartido |
| Manejo de pagos | Sin pago nativo | Sí, vía AP2 | Sí, a través de Stripe |
| Dónde realizan transacciones los agentes | Cualquier entorno compatible con MCP | Modo IA de Google, Géminis | ChatGPT |
| Mecanismo de descubrimiento | Esquemas de herramientas y recursos | /.well-known/ucp manifiesto | Registro de punto final ACP || Lo mejor para | Consultas de datos, acceso a herramientas | Comercio electrónico, reservas, servicios | Ventas nativas de ChatGPT |
| Esfuerzo de implementación | 2 a 4 horas para servidor básico | 1 a 2 semanas para el ciclo de vida completo | Días, requiere integración de Stripe |

## Marco de decisión estratégica

Si desea que los agentes accedan a sus datos y herramientas: primero implemente MCP. Es el más rápido de implementar y atiende a la gama más amplia de agentes.

Si vende productos o servicios y desea que los agentes del ecosistema de Google los compren: agregue UCP con una Declaración de capacidad en /.well-known/ucp.

Si ChatGPT es un canal de ventas importante para su negocio: agregue ACP con integración de Stripe.

Si desea la máxima cobertura: implemente los tres. MCP para la capa de datos, UCP para el comercio del ecosistema de Google, ACP para el comercio ChatGPT. La lógica empresarial subyacente es compartida. Sólo difieren las interfaces de protocolo.

Los [artículos sobre el protocolo x402] (/docs/x402-agent-payments/) cubren la capa de micropagos complementaria que funciona junto con los tres protocolos.

---

## Preguntas frecuentes

**¿Necesito los tres protocolos?**
No. Comience con MCP para acceder a los datos. Agregue UCP o ACP según las plataformas de IA que impulsen sus ventas. La mayoría de las empresas comienzan con un protocolo comercial y agregan el segundo cuando el canal lo justifica.

**¿Pueden coexistir UCP y ACP en el mismo sitio?**
Sí. Sirven a diferentes ecosistemas de agentes. UCP maneja agentes impulsados ​​por Google. ACP maneja ChatGPT. Los mismos datos de producto y lógica empresarial sirven a ambos a través de diferentes interfaces de protocolo.

**¿MCP es solo para productos técnicos?**
No. Cualquier empresa con datos a los que los agentes deban acceder se beneficia de MCP. Un restaurante con menú, un hotel con disponibilidad de habitaciones, un asesor con descripciones de servicios. MCP hace que cualquier información estructurada sea accesible para los agentes.

**¿Qué protocolo tiene más adopción en abril de 2026?**
MCP tiene la adopción más amplia (cientos de miles de sitios). UCP es el protocolo comercial dominante con un importante respaldo minorista. ACP es más nuevo pero está creciendo rápidamente dentro del ecosistema ChatGPT.

**¿Qué es una Declaración de Capacidad?**
Un manifiesto JSON publicado en /.well-known/ucp que les dice a los agentes exactamente qué admite su tienda: qué tipos de transacciones, métodos de pago, reglas de descuento y políticas están disponibles. Los agentes lo leen antes de intentar cualquier interacción.

## Referencias primarias

* [Especificación del protocolo de contexto del modelo](https://modelcontextprotocol.io/specification/2025-06-18/basic/index)
* [primitivas del servidor MCP](https://modelcontextprotocol.io/specification/2025-06-18/server/index)