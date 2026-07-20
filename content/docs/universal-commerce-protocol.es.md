---
title: "Protocolo de Comercio Universal (UCP): una guía práctica."
date: 2026-05-17
weight: 132
category: "Architecture"
description: "Conozca qué es el Protocolo de Comercio Universal, cómo UCP maneja los flujos de trabajo de comercio agente y qué deben preparar los comerciantes antes de su."
summary: "Una guía práctica de UCP para comerciantes y desarrolladores, que cubre la negociación de capacidades, el pago, el cumplimiento, la flexibilidad del transporte y las implicaciones de AEO."
keywords:
  - Protocolo de comercio universal
  - comercio UCP
  - Agentes de IA de la UCP
  - protocolo de comercio agente
  - comercio para agentes
---
# Protocolo de Comercio Universal (UCP): una guía práctica

El Protocolo de Comercio Universal es un estándar de comercio abierto desarrollado conjuntamente por Shopify y Google para compras impulsadas por agentes. Está diseñado para permitir a los comerciantes y agentes negociar capacidades, manejar operaciones comerciales estandarizadas y avanzar a través de flujos de trabajo como descubrimiento, pago, pedidos y poscompra sin reconstruir integraciones personalizadas para cada nueva superficie de IA.

## ¿Qué hace la UCP?

Shopify describe UCP como un protocolo para integrar el comercio con los agentes. Sus materiales oficiales enfatizan primitivos universales, operaciones estandarizadas, extensiones personalizadas, negociación dinámica, pagos abiertos y flexibilidad de transporte.

Fuentes primarias:

- [Shopify: Protocolo de comercio universal](https://www.shopify.com/ucp)
- [Ingeniería de Shopify: Creación del protocolo de comercio universal](https://shopify.engineering/UCP)
- [especificación UCP](https://ucp.dev/)

## UCP en una tabla

| Capacidad UCP | Por qué es importante |
|
---|
---|
| Negociación dinámica | Agentes y comerciantes pueden declarar lo que apoya cada parte |
| Operaciones estandarizadas | Los flujos comunes como el pago y los pedidos se vuelven reutilizables |
| Extensiones personalizadas | Los comerciantes pueden expresar descuentos, cumplimiento o reglas especiales |
| Pagos abiertos | Los gestores de pagos se negocian en lugar de codificarse |
| Transportes múltiples | La lógica empresarial puede funcionar en REST, GraphQL, JSON-RPC, A2A o MCP |

## Por qué debería importarles a los comerciantes

Las integraciones de comercio electrónico tradicionales asumen que el escaparate es la interfaz principal. El comercio de agentes cambia eso. Es posible que un comerciante deba atender a los agentes de compras provenientes de la búsqueda, el chat, las billeteras o los asistentes, manteniendo al mismo tiempo las mismas reglas para descuentos, envío, pago y cumplimiento.

UCP es importante porque intenta estandarizar la capa comercial en lugar de obligar a cada comerciante a crear conectores únicos para cada plataforma de agente.

La [guía de comercio agente] (/docs/agentic-commerce/) explica el cambio estratégico. La [guía de ejecución de comercio agente] (/docs/agentic-commerce-execution/) cubre el trabajo de backend requerido después del descubrimiento.

## UCP frente a API ordinarias

| Integración API ordinaria | Enfoque UCP |
|
---|
---|
| Puntos finales específicos del comerciante | Semántica del comercio compartido |
| Descubrimiento a medida | Negociación de capacidades |
| Los supuestos de pago a menudo se incorporan | Manejadores de pago abiertos |
| Reconstrucción por socio | Reutilización entre agentes compatibles |
| Transporte vinculado a la implementación | Modelo flexible para el transporte |

UCP no elimina la necesidad de buenas API. Proporciona a las operaciones comerciales un lenguaje compartido para que los agentes puedan razonar sobre lo que respalda el comerciante.

## Qué deben preparar los comerciantesAntes de implementar cualquier protocolo, corrija los fundamentos:

1. catálogo de productos preciso
2. precio actual y disponibilidad
3. Lógica determinista de carrito y pago
4. normas de envío e impuestos
5. política de devolución y cancelación
6. visibilidad del estado del orden
7. auditabilidad para acciones automatizadas

Esa preparación se superpone fuertemente con la [guía AEO de comercio electrónico](/es/docs/aeo-ecommerce/) porque un agente no puede completar el comercio de forma segura si los datos subyacentes son vagos.

## Dónde encaja UCP en la pila

| Capa | Rol de ejemplo |
|
---|
---|
| Leer capa | Páginas de productos, datos estructurados, `llms.txt` |
| Capa de capacidad | Perfil del comerciante UCP y operaciones soportadas |
| Capa de ejecución | Pago, envío de pedidos, actualizaciones de cumplimiento |
| Capa de pago | Gestores de pagos negociados o protocolos complementarios |

UCP no es el único protocolo en el comercio de agentes. La [Comparación UCP, ACP y MCP] (/docs/ucp-vs-acp-vs-mcp/) muestra dónde encaja junto a los protocolos de pago y acceso a herramientas nativos de ChatGPT.

## Preguntas frecuentes

### ¿UCP es solo para comerciantes de Shopify?

No. Shopify lo presenta como un protocolo abierto, desarrollado conjuntamente con Google y abierto a ecosistemas comerciales más amplios.

### ¿UCP reemplaza a los procesadores de pagos?

No. Shopify describe pagos abiertos y manejadores de pagos negociados, no un único procesador obligatorio.

### ¿La UCP se aplica únicamente al pago?

No. El material oficial incluye descubrimiento, pago, pedidos y flujos posteriores a la compra.

### ¿Qué deberían hacer los comerciantes primero?

Haga que las reglas de productos, precios, disponibilidad y pedidos sean legibles por máquina antes de buscar integraciones de protocolos.

## Conclusión

UCP es importante porque convierte el comercio de un problema de integración único en un problema de protocolo reutilizable. Los comerciantes que ya cuentan con datos limpios de productos y operaciones deterministas estarán mejor posicionados para adoptarlos cuando la demanda del canal sea real.