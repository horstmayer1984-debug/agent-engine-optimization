---
title: "La guía de comercio electrónico para la optimización y la compra."
date: 2026-03-22
weight: 21
category: "Industry"
description: "Cómo las tiendas en línea deben reestructurar los datos de productos, los sistemas de inventario, los flujos de pago y las políticas para vender directamente."
summary: "Los agentes de IA comprarán en nombre de los usuarios. Las tiendas en línea que exponen datos limpios de productos, inventario en tiempo real, pago sin cabeza y políticas legibles por máquina capturarán estas ventas."
keywords:
  - compra agente
  - AEO de comercio electrónico
  - IA de pago sin cabeza
  - agentes de IA de datos de producto
  - API de inventario
  - comercio legible por máquina
---
# La guía de comercio electrónico para la compra y optimización de agentes

Un cliente le dice a su asistente de IA: "Cómprame una camisa de algodón azul de menos de 40 euros con devolución gratuita". El agente escanea cincuenta tiendas en segundos. Comprueba los datos del producto, verifica el stock, lee las políticas de devoluciones, compara precios y completa la compra. Todo el proceso lleva menos tiempo del que un humano necesita para abrir un navegador.

La tienda que gana esta venta no es la que tiene la mejor fotografía o el texto publicitario más inteligente. Es el almacén donde cada punto de datos es explícito, cada política es legible por máquina y el proceso de pago funciona sin un navegador.

Así es como se ve en la práctica el [comercio agente](/es/docs/agentic-commerce/). Esto es lo que las tiendas online deben cambiar.

## Los datos del producto deben estar completos, estructurados y actualizados.

Un agente no puede mirar una fotografía y determinar el material. No puede inferir el peso de las dimensiones. Necesita que todos los atributos se establezcan explícitamente en forma estructurada.

Para cada producto exponer como mínimo:

- nombre, marca, categoría
- precio y moneda (con reglas fiscales)
- tamaño, peso, material y color exactos (utilizando valores estandarizados, no nombres comerciales)
- lógica de variantes (qué tamaños están disponibles y en qué colores)
- dimensiones y peso del envío
- restricciones de compatibilidad
- estado (nuevo, reformado, usado)

Utilice el marcado de oferta y producto JSON-LD. Pero vaya más allá: si sus datos estructurados dicen "InStock" mientras que el inventario real muestra 0 unidades, destruirá la confianza del agente de forma permanente. La precisión de los datos importa más que su integridad.

La denominación inconsistente de los atributos es igualmente dañina. Si un producto dice "duración de la batería" y otro dice "tiempo de ejecución", obliga al agente a adivinar si significan lo mismo. Estandariza tu vocabulario en todo el catálogo.

## El inventario en tiempo real no es opcional

Las señales de acciones obsoletas son la forma más rápida de perder la confianza de los agentes.

Un humano podría aceptar un correo electrónico de disculpa por un artículo agotado. Un agente lo registra como fallo del sistema. La próxima vez que ese agente compare opciones, su tienda perderá la prioridad.

Exponga el inventario a través de un punto final dedicado o, como mínimo, mediante un marcado de esquema preciso que se actualice en minutos, no en horas. Si los recuentos exactos no son prácticos, utilice grupos de estado honestos: en stock, disponibilidad limitada, pedido anticipado, no disponible.

Las [10 principales estrategias AEO para comercio electrónico](/es/docs/aeo-ecommerce/) cubren la confianza del inventario con más detalle.

## Pago sin cabeza para transacciones automáticasLos flujos de pago tradicionales están diseñados para humanos: pasos visuales, barras de progreso, campos de formulario, modales de confirmación. Un agente no necesita nada de eso. Necesita una llamada API única y documentada.

Un punto final de pago sin cabeza acepta:

- identificador de producto y cantidad
- dirección de entrega
- credenciales de pago (a través de un token seguro, no de datos sin procesar de la tarjeta)
- selección del método de envío
- cupón o código de descuento (si corresponde)

Devuelve una confirmación con el ID del pedido, la entrega estimada, el total cobrado y la URL del recibo.

Si su pago solo funciona a través de una sesión de navegador representada con modos JavaScript, CAPTCHA y consentimiento de cookies, los agentes no pueden completar la compra. Le comprarán a un competidor cuya caja sea accesible mediante máquina.

## Las políticas deben ser elementos de decisión, no documentos legales

Las políticas de devolución, las garantías de envío, las garantías y los términos de cancelación no son notas a pie de página para los agentes. Son criterios de selección.

Un agente programado para "comprar sólo en tiendas con devoluciones gratuitas durante 30 días" necesita verificar esa condición en milisegundos. Los largos párrafos de texto legal no ayudan. Los datos de políticas estructuradas hacen:

- ventana de devolución en días
- coste de devolución (gratis, de pago, condicional)
- método de reembolso (pago original, crédito de la tienda)
- duración de la garantía
- garantía de envío (entrega dentro de X días o reembolso)

Incorpórelos como datos estructurados o expóngalos a través de un punto final de política dedicado. Las marcas que hacen que las políticas sean legibles por máquinas obtienen una ventaja mensurable en la selección mediada por agentes. La [capa de ejecución](/es/docs/execution-layer/) explica por qué este cambio de legible por humanos a procesable por máquinas es el núcleo de AEO.

## La comparación de precios debe ser determinista

Los agentes comparan precios entre tiendas. Si su precio requiere representación de JavaScript, inicio de sesión o detección geográfica para mostrar el número real, los agentes pueden extraer el precio incorrecto o ningún precio.

Haga visible el precio real (incluidos los impuestos cuando corresponda) en la fuente de la página y en los datos estructurados. Si ofrece precios escalonados o descuentos por cantidad, exponga las reglas de precios en un formato legible por máquina, no solo como una tabla visual.

---

## Preguntas frecuentes

**¿Qué es la compra agente?**
La compra agente describe el proceso en el que los agentes de IA investigan, comparan y compran productos en nombre de los usuarios. El agente maneja todo el flujo de trabajo, desde el descubrimiento del producto hasta el pago y la confirmación del pedido.

**¿Por qué es importante el pago sin cabeza para los agentes de IA?**
Los agentes de IA no pueden interactuar con flujos de pago visuales, formularios JavaScript o CAPTCHA. Una API de pago sin cabeza permite a los agentes completar compras a través de una única llamada API documentada.**¿Cómo puedo hacer que las políticas de devolución sean legibles por máquina?**
Exprese los términos de la póliza como puntos de datos estructurados: período de devolución en días, costo, método de reembolso y condiciones. Evite confiar en párrafos en lenguaje natural que requieran interpretación.

**¿Qué sucede cuando los datos del inventario son inexactos?**
El agente registra la discrepancia como una falla del sistema. Su tienda pierde confianza y pierde prioridad en futuras comparaciones. Los datos de inventario precisos son un factor de optimización, no solo una preocupación operativa.

**¿Necesito una API separada para las compras de agentes de IA?**
No necesariamente separados, pero su flujo de compras debe ser accesible sin que el navegador lo muestre. Si su pago requiere JavaScript, cookies o interacción visual, es invisible para los agentes.

## Referencias primarias

* [Especificación del Protocolo de Comercio Universal](https://ucp.dev/2026-04-08/specification/overview/)
* [Documentación de Coinbase x402](https://docs.cdp.coinbase.com/x402/welcome)