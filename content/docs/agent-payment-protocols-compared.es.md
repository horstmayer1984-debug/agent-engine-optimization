---
title: "Protocolos de pago del agente comparados: x402, ACP, MPP, AP2."
metaTitle: "Protocolos de pago de agentes comparados para el comercio con IA."
date: 2026-05-08
weight: 118
category: "Architecture"
description: "Una comparación práctica de x402, ACP, MPP, AP2, Visa TAP, Mastercard Agent Pay, UCP y Nevermined para pagos de agentes de IA."
summary: "Guía comparativa de protocolos de pago de agentes en 2026, que cubre liquidación, pago, autorización, tarjetas, sesiones e infraestructura de agentes."
keywords:
  - protocolos de pago del agente
  - x402 frente a ACP frente a MPP
  - Pagos de agentes AP2
  - Pagos de agentes de IA
  - protocolos de comercio agente
---
# Protocolos de pago del agente comparados: x402, ACP, MPP, AP2, TAP, pago del agente

Los protocolos de pago de los agentes se dividirán en tres capas en 2026: liquidación, orquestación comercial y confianza. x402 es más potente para pagos HTTP ligeros y liquidación de monedas estables. ACP y UCP cubren el recorrido de compras. MPP apunta a pagos automáticos recurrentes. AP2, Visa TAP y Mastercard Agent Pay se centran en la autorización, la identidad y la confianza en la red de tarjetas.

Esto es importante para Agent Engine Optimization porque los pagos ya no son solo un detalle de pago. Si un agente de IA puede descubrir su oferta pero no puede pagar, autorizar o verificar la transacción, su sitio es visible pero no ejecutable.

## Comparación rápida

| Protocolo o sistema | Principales patrocinadores | Mejor ajuste | Enfoque de pago | Papel típico en la pila |
|
---|
---|
---|
---|
---|
| x402 | Coinbase, Cloudflare, Stripe, ecosistema de la Fundación Linux | API de pago por solicitud y servicios de agente | Liquidación HTTP 402, a menudo monedas estables | Capa de asentamiento |
| ACP | OpenAI y Stripe | Pago en contexto a través de agentes de IA | Pago del comerciante y tokens de pago compartidos | Flujo de comercio |
| MPP | Raya y tempo | Pagos automáticos continuos y uso de API | Sesiones, streaming, facturación basada en uso | Capa de pago de la máquina |
| AP2 | Google y socios de pagos | Demostrar la intención y autorización del usuario | Mandatos criptográficos y confianza | Capa de autorización |
| UCP | Google y socios comerciales | Viajes de compras agentes | Descubrimiento, catálogo, pago, post compra | Capa de protocolo de comercio |
| Visa TAP | Ecosistema de visas | Confianza de los comerciantes en los agentes de IA | Señales de identidad y credenciales del agente | Puente ferroviario de confianza y tarjeta |
| Pago del agente de Mastercard | Mastercard | Transacciones de agentes basadas en tarjetas | Pagos agentes tokenizados | Capa de red de tarjetas |
| Nunca minado | Nunca minado | API de agentes de monetización, herramientas MCP, activos protegidos | Planes, derechos, x402, flujos de tarjetas y monedas estables | Plataforma de infraestructura |

## ¿Qué cambió en mayo de 2026?

El mercado ya no tiene un estándar de pago obvio. Tiene una pila.

x402 pasó del experimento cripto nativo a una infraestructura más amplia después de que la Fundación Linux anunciara la Fundación x402 con Coinbase contribuyendo con el protocolo. Stripe publicó documentación sobre pagos automáticos e introdujo MPP con Tempo. OpenAI y Stripe convirtieron a ACP en la capa comercial detrás de Instant Checkout. Google impulsó AP2 como protocolo de autorización y luego trasladó AP2 hacia la gobernanza de estándares a través de la Alianza FIDO. Visa y Mastercard incorporaron modelos de confianza de redes de tarjetas a la conversación sobre pagos de agentes.La conclusión práctica es sencilla: los comerciantes no deberían preguntarse: "¿Qué protocolo gana?". Deberían preguntar: "¿Qué capa resuelve este protocolo?"

## Capa de liquidación: x402

x402 revive el patrón HTTP 402 Payment Required para pagos de agentes y API. Un cliente solicita un recurso protegido, el servidor devuelve los requisitos de pago, el cliente adjunta un comprobante de pago y el servidor concede acceso después de la verificación.

x402 es sólido cuando el producto es pequeño, digital, basado en API o tiene un precio por solicitud. Un punto final meteorológico, una fuente de datos premium, una herramienta MCP, una llamada de inferencia o un informe legible por máquina pueden cobrar por invocación sin necesidad de crear una cuenta.

Su limitación también es clara. x402 liquida el valor. No resuelve por sí solo todo el proceso de compra. Un comerciante todavía necesita descubrimiento de productos, divulgación de políticas, controles de fraude, reembolsos, identidad, impuestos, soporte y manejo de disputas.

Lea la guía del sitio: [Pagos de agentes x402](/es/docs/x402-agent-payments/).

## Capa de comercio: ACP y UCP

ACP y UCP se encuentran más cerca del proceso de compras que x402.

ACP, desarrollado por OpenAI y Stripe, está diseñado en torno al pago iniciado por el agente. Stripe describe el comercio de agentes como una forma para que compradores, agentes y empresas realicen transacciones de forma segura, con tokens de pago compartidos y manejo de catálogos en el flujo.

La UCP es más amplia. Se posiciona como un lenguaje comercial común para compras agentes a través del descubrimiento, la interacción del catálogo, el pago y el soporte posterior a la compra. Eso lo hace menos parecido a una vía de pago y más a una superficie de protocolo comercial.

Para los equipos de comercio electrónico, ACP y UCP son más relevantes que x402 cuando el problema es una compra minorista normal en lugar de una solicitud API paga.

## Capa de pago de la máquina: MPP

MPP, en coautoría de Stripe y Tempo, está dirigido a agentes que pagan a empresas y otros agentes sin un ser humano al tanto. Su caso de uso más sólido no es un pago aislado. Es una actividad recurrente, continua o medida.

Eso se adapta bien a los sistemas autónomos. Los agentes no siempre saben el número exacto de llamadas futuras. Es posible que necesiten un presupuesto, un período de tiempo, un límite de tarifa y una conciliación una vez finalizado el trabajo.

Si x402 está limpio para una solicitud, MPP es interesante para una serie de solicitudes.

## Capa de autorización: AP2

AP2 es la respuesta de Google al problema de la confianza: ¿cómo sabe un comerciante que un usuario autorizó al agente a comprar ese artículo en estas condiciones?Google describe AP2 como un protocolo abierto para iniciar y realizar transacciones de forma segura con pagos dirigidos por agentes entre plataformas. Su concepto central es el mandato: evidencia criptográficamente verificable que captura la intención del usuario, los detalles del carrito y la autorización de pago.

AP2 tiene menos que ver con la vía de pago y más con la responsabilidad. Puede funcionar con tarjetas, billeteras y rieles de liquidación de criptomonedas. Eso lo convierte en un complemento de x402 en lugar de un puro reemplazo.

## Capa de red de tarjetas: Visa TAP y Mastercard Agent Pay

Visa TAP y Mastercard Agent Pay resuelven un problema diferente: cómo las redes de tarjetas existentes se adaptan al comercio iniciado por agentes.

Visa TAP ofrece a los comerciantes una forma de distinguir los agentes legítimos de IA del tráfico automatizado sospechoso y de pasar el contexto de las credenciales y del agente a través del flujo comercial. Mastercard Agent Pay utiliza conceptos de tokenización que ya se utilizan en el comercio de tarjetas y los aplica a los pagos agentes.

Estos sistemas son importantes porque muchos comerciantes no comenzarán con monedas estables. Comenzarán con tarjetas, procesadores existentes, credenciales tokenizadas y sistemas de fraude en los que ya confían.

## Capa de plataforma: Nevermined

Nevermined no es sólo un protocolo. Es una infraestructura para acceso pago a API de agentes, herramientas MCP y activos protegidos. Su documentación describe la compatibilidad con flujos x402, pago de Stripe, monedas estables, planes y comprobaciones de derechos.

Eso hace que Nevermined sea relevante para los equipos que desean una capa práctica de pago a agentes sin tener que crear todos los componentes ellos mismos.

## ¿Qué protocolo debería elegir una empresa?

| Tipo de negocio | Primer protocolo a evaluar | Por qué |
|
---|
---|
---|
| API de pago o proveedor de datos | x402 o MPP | Por solicitud y el uso medido son opciones naturales |
| Comerciante de comercio electrónico | ACP o UCP | El descubrimiento de productos y el pago son más importantes que la liquidación bruta |
| Flujo de trabajo de adquisiciones empresariales | AP2 más vías de pago existentes | La autorización y la auditabilidad son centrales |
| Tarjeta minorista pesada | Pago del agente Visa TAP o Mastercard | Las redes de tarjetas existentes siguen siendo la base operativa |
| Proveedor de herramientas MCP | x402, MPP o Nevermined | Las herramientas necesitan acceso pago, derechos y flujos seguros de reintento |

## Implicaciones AEO

Para AEO, el patrón ganador es una pila híbrida.

Un sitio debe publicar datos de productos o servicios legibles por máquina, exponer rutas de acción deterministas, documentar los requisitos de autorización y pago, y hacer que el resultado sea verificable. Los protocolos de pago solo ayudan después de que el agente puede comprender qué ofrece el sitio y qué acción es segura tomar.Siguientes pasos internos: lea [Protocolos del agente AI](/es/docs/protocols/), [Capa de ejecución](/es/docs/execution-layer/) y [x402 MCP A2A Full Stack](/es/docs/x402-mcp-a2a-full-stack/).

## Preguntas frecuentes

**¿Cuál es el mejor protocolo de pago a agentes en 2026?**
No existe un único mejor protocolo. x402 es más potente para liquidaciones HTTP ligeras, ACP y UCP son más potentes para flujos comerciales, MPP se adapta a pagos automáticos continuos y AP2 se centra en la autorización y la confianza.

**¿Es x402 mejor que ACP?**
x402 y ACP resuelven diferentes capas. x402 maneja la liquidación de pagos a través de HTTP. ACP maneja el pago iniciado por el agente y la integración del comerciante.

**¿AP2 es una vía de pago?**
AP2 se entiende mejor como un protocolo de autorización y confianza. Puede admitir diferentes métodos de pago y vías de liquidación.

**¿Visa y Mastercard competirán con x402?**
Compiten en algunos casos de uso, pero también resuelven diferentes problemas de adopción. Las redes de tarjetas ayudan a los comerciantes existentes a respaldar los pagos de los agentes sin tener que pasar primero a los rieles cripto nativos.

**¿Qué deberían implementar primero los comerciantes?**
La mayoría de los comerciantes deberían comenzar con datos de productos estructurados, políticas claras y requisitos de pago legibles por los agentes. La elección del protocolo debe seguir el modelo de negocio.

## Fuentes

Las fuentes principales utilizadas para este artículo incluyen [Linux Foundation on the x402 Foundation](https://www.linuxfoundation.org/press/linux-foundation-is-launching-the-x402-foundation-and-welcoming-the-contribution-of-the-x402-protocol), [documentación x402](https://docs.x402.org/faq), [Stripe on ACP](https://stripe.com/newsroom/news/stripe-openai-instant-checkout), [Stripe Machine Payments](https://docs.stripe.com/payments/machine), [Anuncio de Stripe MPP](https://stripe.com/blog/machine-payments-protocol), [Google Cloud AP2 anuncio](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol/), [actualización Google AP2 FIDO](https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/), [documentación UCP](https://ucp.dev/), [página de desarrollador de Visa TAP](https://developer.visa.com/capabilities/trusted-agent-protocol/overview), [anuncio de Mastercard Agent Pay](https://www.mastercard.com/news/press/2025/april/mastercard-unveils-agent-pay-pioneering-agentic-payments-technology-to-power-commerce-in-the-age-of-ai/) y [documentación Nevermined](https://nevermined.ai/docs/getting-started/how-it-works).