---
title: "x402 vs ACP vs MPP: capa de pago, capa de pago, capa de pago."
metaTitle: "x402 vs ACP vs MPP: Comparación de protocolos."
date: 2026-05-08
weight: 119
category: "Architecture"
description: "Compare x402, ACP y MPP para pagos de agentes con IA, incluidos micropagos HTTP, pago de agentes, sesiones, streaming, monedas fiduciarias y monedas estables."
summary: "Una guía práctica sobre las diferencias entre x402, ACP y MPP para comercio agente y pagos automáticos."
keywords:
  - x402 frente a ACP frente a MPP
  - Protocolo de pagos automáticos
  - Protocolo de comercio agente
  - Micropagos de agentes de IA
---
# x402 vs ACP vs MPP: capa de pago, capa de pago, capa de pago automático

x402, ACP y MPP a menudo se consideran competidores, pero resuelven diferentes problemas de pago. x402 es un patrón de liquidación ligero para recursos HTTP. ACP es un protocolo de pago comercial para compras iniciadas por agentes. MPP es un estándar de pago automático para sesiones, uso medido y actividad continua de los agentes.

La forma más sencilla de compararlos es preguntando qué está comprando el agente.

Si el agente compra una respuesta API, x402 encaja. Si el agente compra un producto a un comerciante, encaja ACP. Si el agente paga repetidamente durante una tarea en curso, el MPP se vuelve más interesante.

## Diferencia central

| Pregunta | x402 | ACP | MPP |
|---|---|---|---|
| ¿Qué se está solucionando? | Pago por recursos HTTP protegidos | Pago iniciado por el agente | Pagos automáticos a lo largo del tiempo |
| Patrón de comprador primario | Cliente o agente API | Agente de compras que actúa para un usuario | Flujo de trabajo de agente, servicio o máquina |
| Mejor unidad de valor | Una solicitud o un recurso | Un pedido o carrito | Sesión, transmisión, suscripción, uso medido |
| Modelo de pago | Liquidación de monedas comúnmente estables | Credenciales de pago y pago del comerciante | Fiat o cripto mediante sesiones de pago automático |
| Mejor ejemplo | Pague 0,01 USDC por una llamada API | Comprar un producto dentro de un asistente de IA | Pague continuamente por el uso de API |

## ¿Qué hace bien x402?

x402 es atractivo porque mantiene el protocolo cerca de la web. Un servidor puede responder con HTTP 402 Pago requerido, especificar el precio y los requisitos de pago y luego verificar el pago antes de servir el recurso.

Para flujos de trabajo de agentes, esto es posible. Elimina la configuración de cuentas, la negociación de suscripciones y el aprovisionamiento de claves API de pequeñas transacciones digitales.

Los buenos casos de uso de x402 incluyen:

1. Herramientas MCP pagas
2. Puntos finales de datos premium
3. Inferencia por solicitud
4. Informes legibles por máquina
5. Muros de pago de contenido accesible para agentes
6. Llamadas API donde se conoce el precio antes de la ejecución.

La debilidad no es la elegancia técnica. La debilidad es el alcance. x402 no describe todo el recorrido minorista, el estado del carrito, las devoluciones, los impuestos, el cumplimiento o la atención al cliente.

## Qué hace bien ACP

ACP está diseñado para el comercio de agentes. OpenAI y Stripe lo desarrollaron para casos en los que un asistente de IA ayuda a un usuario a descubrir, evaluar y comprar a un comerciante.La documentación de comercio agente de Stripe apunta a tokens de pago compartidos, manejo de catálogos de productos y ventas en contexto. Ese es un problema diferente al de x402. Una compra minorista no es sólo un pago. Incluye inventario, variantes, envío, impuestos, preguntas del comerciante registrado, confirmación de pedido, cancelación y devoluciones.

El ACP es más fuerte cuando el agente opera dentro de un flujo de compra de consumidores.

## Qué hace bien MPP

MPP, presentado por Stripe y Tempo, está diseñado para pagos automáticos en los que el agente no realiza una sola llamada. Puede operar bajo una sesión, seguir usando un recurso o pagar repetidamente a medida que continúa el trabajo.

Eso se adapta bien a los sistemas autónomos. Los agentes no siempre saben el número exacto de llamadas futuras. Es posible que necesiten un presupuesto, un período de tiempo, un límite de tarifa y una conciliación una vez finalizado el trabajo.

MPP encaja mejor conceptualmente con:

1. Uso continuo de API
2. Suscripciones de agentes
3. Facturación basada en el uso
4. Pagos con máquinas de streaming
5. Un presupuesto delegado para un flujo de trabajo autónomo

## Cómo pueden trabajar los tres juntos

Una pila realista puede utilizar más de un protocolo.

Un agente de IA puede descubrir a un comerciante a través de una superficie comercial, usar ACP para realizar el pago, confiar en AP2 o controles de red de tarjetas para la autorización y pagar a un proveedor de datos independiente a través de x402 o MPP durante el paso de investigación.

En un flujo de trabajo de desarrollador, un agente puede llamar a herramientas MCP pagas a través de x402 para solicitudes aisladas y luego cambiar a MPP para una tarea de datos de larga duración con uso repetido.

La regla de diseño importante es la separación de preocupaciones.

## ¿Cuál deberían implementar primero los desarrolladores?

| Tu operas | Empezar con | Razón |
|---|---|---|
| Una API paga | x402 | El punto final puede fijar el precio y verificar cada solicitud |
| Una API SaaS con uso recurrente | MPP | Materia de facturación basada en sesiones y uso |
| Una tienda de comercio electrónico | ACP | El proceso de pago es el verdadero problema |
| Un mercado de datos | x402 y MPP | Algunos activos se compran una sola vez, otros se miden |
| Una plataforma de agentes de IA | ACP, MPP y x402 | Diferentes vendedores requerirán diferentes modos de pago |

## Notas de implementación AEO

Para AEO, el soporte del protocolo debe estar visible antes de intentar el pago.

Agregue una página legible por máquina o un punto final que indique:

1. Protocolos de pago admitidos
2. Monedas o rieles aceptados
3. Tamaño de carga mínimo y máximo
4. Política de reembolso o reversión
5. Requisitos de autenticación
6. Códigos de error
7. Reglas de idempotencia
8. Ruta de contacto o disputa

Esto convierte el pago de un evento de pago oculto en una capacidad legible por el agente.

## Preguntas frecuentes

**¿MPP está reemplazando a x402?**No directamente. MPP es mejor para sesiones y uso continuo. x402 permanece más limpio para una liquidación simple del nivel de solicitud.

**¿ACP es solo para ChatGPT?**
ACP se creó con OpenAI y Stripe para el comercio agente, pero el protocolo se posiciona como un estándar de comercio abierto en lugar de una función exclusiva de ChatGPT.

**¿Puede un comerciante utilizar x402 y ACP juntos?**
Sí. Un comerciante podría usar ACP para realizar pagos y x402 para acceso API pago, datos premium o servicios de agente.

**¿Qué protocolo es mejor para los micropagos con monedas estables?**
x402 es la opción más clara para micropagos ligeros de monedas estables a través de HTTP. Stripe Machine Payments también admite pagos automáticos con liquidación criptográfica en la infraestructura de Stripe.

## Fuentes

Referencias principales: [documentación x402](https://docs.x402.org/faq), [anuncio de Linux Foundation x402 Foundation](https://www.linuxfoundation.org/press/linux-foundation-is-launching-the-x402-foundation-and-welcoming-the-contribution-of-the-x402-protocol), [anuncio de Stripe ACP](https://stripe.com/newsroom/news/stripe-openai-instant-checkout), [documentación de comercio agente de Stripe](https://docs.stripe.com/agentic-commerce), [documentación de Stripe Machine Payments](https://docs.stripe.com/payments/machine) y [Stripe MPP anuncio](https://stripe.com/blog/machine-payments-protocol).

## Guías relacionadas

* [arquitectura de comercio agente](/es/docs/agentic-commerce/)
* [protocolos de pago del agente](/es/docs/agent-payment-protocols-compared/)
* [la capa de ejecución](/es/docs/execution-layer/)