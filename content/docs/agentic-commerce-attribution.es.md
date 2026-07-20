---
title: "Atribución de comercio agente: medición de las referencias."
metaTitle: "Guía de atribución de comercio agente."
date: 2026-05-25
weight: 151
category: "Guide"
description: "Descubra cómo el comercio agente cambia la atribución, por qué las referencias de IA son más difíciles de medir y qué deben registrar los comerciantes."
summary: "Una guía práctica para la atribución del comercio de agentes, que cubre referencias de IA, contexto de UCP, sesiones de origen del agente, datos de intención, lagunas analíticas y métricas de AEO."
keywords:
  - atribución de comercio agente
  - Seguimiento de referencias de IA
  - contexto de la UCP
  - análisis de comercio agente
  - Atribución de compras por IA
---
# Atribución de comercio agente: medición de las referencias y la intención de la IA

La atribución de comercio agente es la práctica de conectar una recomendación, un carrito o una sesión de pago asistida por IA con el agente, la superficie, la intención del usuario y el resultado del comerciante. Es más difícil que el seguimiento de referencias clásico porque la decisión del usuario puede formarse dentro de un sistema de inteligencia artificial antes de que exista una visita normal al sitio web.

## Por qué está cambiando la atribución

El análisis clásico de comercio electrónico supone que el comprador hace clic en un enlace, llega a una página, navega, agrega al carrito y compra. El comercio agente rompe ese camino. El agente puede investigar productos, comparar ofertas, crear un carrito y enviar solo la acción final o la referencia al comerciante.

La investigación sobre comerciantes de PayPal señala que las empresas se están preparando para sistemas de inteligencia artificial que influyen en el descubrimiento antes de que el comprador llegue al sitio. Google también enmarca a UCP y Universal Cart como infraestructura para el comercio agente en las superficies de Google.

Es por eso que [la medición de AEO](/es/docs/aeo-kpis-measurement/) necesita más que clasificaciones y clics.

## Qué deberían atribuir los comerciantes

| Señal | Por qué es importante |
|
---|
---|
| Fuente de IA o superficie del agente | Muestra dónde ocurrió el descubrimiento |
| Categoría de intención del usuario | Distingue investigación, carrito, reorden, soporte o reembolso |
| ID de productos mostrados al agente | Conecta la exposición del catálogo con las ventas |
| Fuente de creación del carrito | Revela si el carro se formó dentro o fuera del sitio |
| Transferencia de pago | Muestra dónde se completó la compra |
| Referencia de mandato o autorización | Enlaces con intención de pago cuando sean compatibles |
| Resultado del cumplimiento | Conecta transacciones de origen de agente con entregas y devoluciones |

El modelo [cinco niveles de comercio agente](/es/docs/five-levels-agentic-commerce/) es útil porque la madurez de la atribución cambia en cada nivel.

## El problema de la UTM

Las etiquetas UTM siguen siendo útiles cuando un asistente de IA envía a un usuario a una página. Pero son débiles cuando el agente no se limita a recomendar a un visitante.

Los viajes agentes pueden necesitar:

- objetos de contexto firmados
- referencias del carrito
- listas de candidatos de productos
- ID de mandato
- estado de consentimiento
- identificadores de plataforma
- confirmación del comerciante registrado

Esto está más cerca del seguimiento de transacciones que del seguimiento de campañas.

## Métricas AEO para el comercio agente

| Métrica | Lo que te dice |
|
---|
---|
| Sesiones referidas por agentes | ¿Con qué frecuencia los sistemas de inteligencia artificial envían tráfico?
| Tarifa de carrito de origen del agente | Si los agentes pueden construir carros con éxito |
| Cobertura del catálogo estructurado | ¿Cuánto inventario es legible por máquina?
| Finalización del pago del agente | Si funciona el traspaso o el pago nativo |
| Tasa de rechazo de políticas | Si las políticas bloquean las transacciones de los agentes || Tasa de excepción posterior a la compra | Si los pedidos de origen de agente generan más reembolsos o problemas de soporte |

Vincule estas métricas a la [capa de ejecución](/es/docs/execution-layer/), no solo a los informes de contenido.

## Lista de verificación de implementación

1. Preservar el seguimiento normal de referencias y UTM.
2. Agregue nombres de eventos de origen del agente en análisis.
3. Registre el agente de usuario, el estado del bot verificado y la plataforma de origen, cuando esté disponible.
4. Almacene el origen del carrito y la ruta de transferencia del carrito.
5. Asigne los ID de productos a los datos expuestos en feeds, esquemas y API.
6. Realice un seguimiento de los errores de pago por separado para las sesiones de origen del agente.
7. Conecte los datos de pedidos, reembolsos y soporte al contexto de origen.

La [guía del Protocolo de comercio universal](/es/docs/universal-commerce-protocol/) explica dónde puede encajar el intercambio en el contexto del comercio.

## Preguntas frecuentes

### ¿Las referencias de IA son visibles en Google Analytics?

Algunos son visibles como referencias normales o tráfico de campaña. Otros pueden aparecer como tráfico directo, de bot, de socios o mediado por plataforma, a menos que la integración preserve el contexto.

### ¿La atribución es sólo un problema de marketing?

No. En el comercio de agentes, la atribución también afecta el fraude, las pruebas de disputas, la política comercial y el soporte posterior a la compra.

### ¿Cuál es la primera métrica a agregar?

Realice un seguimiento de las sesiones de origen del agente y de los inicios del carrito por separado del tráfico orgánico, pago y directo normal.

### ¿Cómo se relaciona esto con el AEO?

AEO necesita demostrar que la infraestructura legible por los agentes genera descubrimiento, actividad de carrito, acciones completadas y resultados confiables.

## Fuentes

Fuentes principales: [hallazgos de PayPal Agentic Commerce Pulse](https://www.paypal.com/us/brc/article/agentic-commerce-pulse-report-findings), [PayPal en escaparates de IA](https://www.paypal.com/us/brc/article/ai-storefront-what-merchants-need-to-know) y [actualización de Google UCP y Universal Cart](https://blog.google/products-and-platforms/products/shopping/shopping-updates-google-marketing-live/).