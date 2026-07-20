---
title: "Guía de interoperabilidad del protocolo de comercio agente."
date: 2026-05-25
weight: 159
category: "Architecture"
description: "Compare cómo UCP, AP2, MCP, A2A, x402 y las capas de confianza de red de tarjetas encajan entre sí en descubrimiento, carrito, pago y cumplimiento."
summary: "Un mapa práctico de interoperabilidad para protocolos de comercio de agentes, que muestra en qué se diferencian el descubrimiento, el contexto, la autorización, el pago, la coordinación y el cumplimiento."
keywords:
  - interoperabilidad del protocolo de comercio agente
  - UCP AP2 MCP A2A x402
  - protocolos de comercio agente
  - Arquitectura de comercio de IA
  - protocolos de pago del agente
---
# Interoperabilidad del protocolo de comercio agente

El comercio agente no se ejecutará en un solo protocolo. UCP ayuda a los sistemas comerciales a interoperar, AP2 maneja la autorización de pago verificable, MCP expone herramientas y contexto, A2A coordina a los agentes, x402 maneja las solicitudes de pago nativas de la máquina y las capas de confianza de la red de tarjetas agregan controles de identidad y pago. La tendencia es la interoperabilidad, no el monopolio de protocolos.

## Por qué se espera la superposición de protocolos

El comercio tiene muchas etapas del ciclo de vida. El descubrimiento, el carrito, el pago, el cumplimiento, el reembolso, la autenticación y la coordinación del agente son problemas diferentes.

No se debe esperar que un solo protocolo los resuelva todos.

La página existente [UCP vs ACP vs MCP](/es/docs/ucp-vs-acp-vs-mcp/) compara tres patrones principales. Esta página mapea la pila de comercio agente más amplia.

## Mapa de roles de protocolo

| Protocolo o capa | Papel principal | Etapa de comercio |
|
---|
---|
---|
| UCP | Capacidad de comercio, carrito, pago, interoperabilidad posterior a la compra | Descubrimiento a través del ciclo de vida del pedido |
| AP2 | Autorización y mandatos de pago verificables | Intención, pago, pago |
| PCM | Acceso a herramientas y contexto | Flujos de trabajo de agentes internos y externos |
| A2A | Coordinación entre agentes | Agentes compradores, comerciantes, plataformas y servicios |
| x402 | Solicitud de pago nativa HTTP y patrón de liquidación | API, contenidos y pagos automáticos |
| Intención verificable / TAP / Pago del agente | Confianza, identidad, tokenización y responsabilidad | Autorización y riesgo de pago |

La [comparación de protocolos de pago de agentes](/es/docs/agent-payment-protocols-compared/) explica el lado del pago con más detalle.

## Flujo de ejemplo

Una compra agente podría funcionar así:

1. El agente descubre productos a través de páginas, fuentes, esquemas o capacidad de catálogo UCP.
2. El agente compara opciones utilizando datos estructurados de políticas y productos.
3. El agente crea un carrito a través de UCP o API de comerciante.
4. La intención del usuario se captura a través de mandatos estilo AP2 o una capa de confianza comparable.
5. El pago se realiza mediante tarjetas, billeteras, x402, monedas estables o crédito en la cuenta.
6. Los eventos de cumplimiento actualizan al agente después del pago.
7. La evidencia de disputa vincula la intención del usuario, la acción del agente, el carrito, el pago y la entrega.

Esto explica por qué [Agent Engine Optimization](/es/docs/what-is-aeo/) necesita trabajo tanto en la capa de lectura como en la capa de ejecución.

## Lo que los comerciantes no deben hacer

No espere a que un estándar "gane". En su lugar, diseñe sistemas internos en torno a conceptos estables:

- identidad del producto
- intención del usuario
- estado del carrito
- autorización de pago
- identidad del agente
- política comercial
- estado del pedido
- pista de auditoría

Luego, asigne esos conceptos a los protocolos a medida que maduren.

## Lista de verificación de interoperabilidad| Objeto interno | Necesidad de afrontar el protocolo |
|
---|
---|
| Producto | Esquema, feed, catálogo API, UCP |
| Carrito | API de carrito UCP o carrito comercial |
| Intención | Mandato AP2 o Intención Verificable |
| Pago | AP2, token de tarjeta, billetera, x402, crédito de cuenta |
| Agente | Identidad, autenticación, política |
| Orden | Eventos de cumplimiento y API de estado |
| Auditoría | Rastro de evidencia compartido |

La página [evidencia de disputas comerciales de agentes](/es/docs/agentic-commerce-dispute-evidence/) cubre la capa de auditoría.

## Preguntas frecuentes

### ¿UCP reemplazará a AP2?

No. UCP y AP2 resuelven problemas diferentes. UCP se centra en la interoperabilidad comercial; AP2 se centra en autorizaciones y mandatos de pago seguros.

### ¿X402 compite con AP2?

En ocasiones pueden aparecer en la misma conversación de pago, pero son diferentes. x402 es negociación de pago nativa HTTP; AP2 trata sobre la autorización y la intención verificable en torno a los pagos de los agentes.

### ¿Dónde encaja MCP?

MCP ayuda a los agentes a utilizar herramientas y contexto. Puede admitir flujos de trabajo comerciales, pero no reemplaza los protocolos de pago o pago.

### ¿Qué deberían implementar primero los comerciantes?

Comience con la coherencia interna de los objetos: producto, carrito, intención, pago, política, pedido y auditoría. Las integraciones de protocolos se vuelven más fáciles después de eso.

## Fuentes

Fuentes principales: [documentación UCP](https://ucp.dev/), [documentación AP2](https://ap2-protocol.org/), [actualización de comercio de IA y UCP de Google](https://blog.google/products-and-platforms/products/shopping/shopping-updates-google-marketing-live/), [documentos del protocolo de contexto del modelo](https://modelcontextprotocol.io/docs/concepts/tools), [anuncio de Cloudflare x402](https://blog.cloudflare.com/x402/) y [intención verificable de Mastercard](https://www.mastercard.com/europe/en/news-and-trends/stories/2026/verifiable-intent.html).