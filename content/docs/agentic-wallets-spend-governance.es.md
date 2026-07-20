---
title: "Carteras agentes y gobernanza del gasto: cómo los agentes de IA."
metaTitle: "Carteras agentes y gobernanza del gasto."
date: 2026-05-25
weight: 153
category: "Architecture"
description: "Descubra cómo las carteras de agentes, los límites de gasto, la tokenización, los registros de auditoría y los controles de políticas hacen que los pagos."
summary: "Una guía práctica para billeteras agentes y gestión de gastos, que incluye Fireblocks, AP2, Mastercard Agent Pay, autoridad delegada, monedas estables y controles de auditoría."
keywords:
  - carteras agentes
  - gastar gobernanza
  - Pagos de agentes de IA
  - billeteras delegadas
  - controles de pago agentes
---
# Carteras agentes y gobernanza del gasto

Las billeteras agentes permiten a los agentes de IA pagar dentro de las reglas establecidas por un usuario u organización. La gobernanza del gasto es la capa de control: presupuestos, límites comerciales, alcances de tokens, registros de auditoría, comprobaciones de cumplimiento y revocación. Sin esos controles, los pagos agentes son demasiado riesgosos para el comercio rutinario.

## Por qué las billeteras están cambiando

Una billetera humana supone que una persona aprueba cada compra. Una billetera agente supone que una persona o empresa delega autoridad limitada al software.

Eso crea un nuevo problema de diseño:

- El agente necesita suficiente autoridad para completar una tarea.
- El usuario necesita confianza en que el agente no puede gastar de más.
- El comerciante necesita pruebas de que el agente tiene permiso para comprar.
- El emisor, PSP o proveedor de billetera necesita un registro de auditoría.

Agentic Payments Suite de Fireblocks y Mastercard Agent Pay apuntan a este cambio.

## Controles de gobernanza del gasto

| Controlar | Ejemplo |
|
---|
---|
| Límite de importe | Agente puede gastar hasta 50 dólares por compra |
| Ámbito mercantil | El agente sólo puede comprar a proveedores aprobados |
| Alcance de la categoría | El agente puede comprar material de oficina, no productos electrónicos |
| Ventana de tiempo | La autoridad expira después de siete días |
| Alcance del propósito | El agente puede reabastecer una familia de SKU |
| Umbral de aprobación | Se requiere revisión humana por encima de un límite |
| Revocación | El usuario puede desactivar el token de agente o la concesión de billetera |
| Pista de auditoría | Cada acción registra la intención, el pago y el resultado |

Estos controles son fundamentales para la [capa de ejecución](/es/docs/execution-layer/).

## Tokens de tarjetas versus billeteras de monedas estables

| Modelo | Fuerza | Restricción |
|
---|
---|
---|
| Tokenización de red de tarjetas | Aceptación comercial familiar, controles del emisor, reglas de disputa | Necesita señales de autorización e identidad del agente |
| Cartera de moneda estable | Liquidación programable y flujos nativos de las máquinas | Requiere controles de cumplimiento, custodia y conciliación |
| Crédito de cuenta | Útil para SaaS y API | Limitado a una plataforma |
| Transferencia bancaria/rieles en tiempo real | Bueno para mercados con pagos de cuentas rápidos | La disponibilidad y la lógica de reembolso varían |

La [comparación de protocolos de pago del agente](/es/docs/agent-payment-protocols-compared/) asigna la capa de protocolo. Esta página se centra en la capa de control de billetera.

## Implicaciones comerciales

Los comerciantes deberían esperar recibir más transacciones donde:

- un agente actúa en nombre de un usuario
- el instrumento de pago tiene alcance
- la solicitud incluye evidencia de intención
- los límites de la política afectan la autorización
- las disputas dependen de los registros de los agentes

Eso significa que los sistemas de pago deberían almacenar más contexto que una autorización de tarjeta normal.

## Qué preparar ahora

1. Agregue campos para la identidad del agente y la referencia de autorización.2. Registre juntos los eventos de carrito, pago y cumplimiento.
3. Decidir qué productos podrán ser adquiridos por los agentes delegados.
4. Definir categorías de alto riesgo que requieran confirmación humana.
5. Revisar las reglas de fraude para transacciones de origen de agente.
6. Mantenga los estados de reembolso y cancelación legibles por máquina.

El artículo [Fireblocks Agentic Payments Suite](/es/docs/fireblocks-agentic-payments-suite/) cubre un ejemplo de infraestructura.

## Preguntas frecuentes

### ¿Es una billetera agente una billetera digital normal?

No. Es una billetera delegada o una configuración de pago donde un agente de IA puede actuar dentro de límites explícitos.

### ¿Pueden las billeteras agentes usar tarjetas?

Sí. Mastercard describe tokens agentes y Agent Pay para pagos de red de tarjetas específicos. AP2 también incluye muestras de tarjeta y x402.

### ¿Pueden las billeteras agentes usar monedas estables?

Sí. Fireblocks describe billeteras agentes para pagos con monedas estables dentro de límites definidos y pistas de auditoría.

### ¿Cuál es el mayor riesgo?

Autoridad ilimitada. Las billeteras de agentes necesitan límites de gasto estrictos, alcance de propósito, revocación y registros confiables.

## Fuentes

Fuentes principales: [Anuncio de Fireblocks Agentic Payments Suite](https://www.prnewswire.com/news-releases/fireblocks-joins-x402-foundation-launches-agentic-payments-suite-302777251.html), [Documentación AP2](https://ap2-protocol.org/), [Intención verificable de Mastercard](https://www.mastercard.com/europe/en/news-and-trends/stories/2026/verifiable-intent.html) y [Documento técnico sobre compras con tecnología de IA de Mastercard](https://www.mastercard.com/content/dam/mccom/eu/news-and-trends/business-thought-leadership/digital-payments/pdfs/Get_ready_for_AI-powered_shopping_experiences.pdf).