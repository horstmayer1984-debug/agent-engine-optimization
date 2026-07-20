---
title: "AP2 vs x402: capa de autorización versus capa de liquidación."
date: 2026-05-08
weight: 120
category: "Architecture"
description: "Comparación de AP2 y x402 para pagos de agentes de IA: mandatos, confianza, autorización, liquidación HTTP 402, monedas estables y pilas híbridas."
summary: "Una comparación de AP2 y x402 de Google, que explica por qué AP2 es una capa de confianza mientras que x402 es una capa de liquidación de pagos."
keywords:
  - AP2 frente a x402
  - Protocolo de pagos de agentes
  - protocolo de pago x402
  - Autorización del agente de IA
---
# AP2 vs x402: Capa de autorización vs Capa de liquidación de pagos

AP2 y x402 son más complementarios que sustitutos directos. AP2 responde si un agente estaba autorizado a realizar un pago. x402 responde cómo un recurso HTTP protegido puede solicitar y verificar el pago. Una pila de comercio de agentes seria puede necesitar ambos.

La confusión proviene de la palabra "pago". AP2 trata sobre permiso, prueba y responsabilidad. x402 se trata de liquidación y acceso.

## La versión corta

| Criterio | AP2 | x402 |
|
---|
---|
---|
| Función principal | Demuestra autorización e intención del usuario | Solicita y verifica pago a través de HTTP |
| Artefacto principal | Mandatos y prueba criptográfica | Solicitud de pago HTTP 402 y comprobante de pago |
| Mejor ajuste | Pago de agentes, comercio delegado, auditabilidad | API pagas, herramientas MCP, acceso a datos, microtransacciones |
| Ferrocarril de pago | Método de pago independiente | A menudo basado en monedas estables, que se expande a través del soporte del ecosistema |
| Riesgo central abordado | ¿Se le permitió a este agente comprar esto? | ¿Se ha pagado por este recurso? |

## Para qué está diseñado AP2

Google introdujo AP2 para hacer que los pagos realizados por agentes sean más seguros en todas las plataformas. La cuestión central no es sólo la ejecución de los pagos. Es autorización.

Un comerciante, emisor o procesador de pagos necesita evidencia de que un humano le dio a un agente autoridad para actuar. La evidencia también debe coincidir con el carro final. Si el usuario pidió zapatillas para correr de menos de $120, el agente no debería comprar silenciosamente una chaqueta de $230.

AP2 aborda esto a través de conceptos de mandato. El protocolo registra la intención del usuario y el contexto de pago de una manera que pueda verificarse más adelante. La última actualización AP2 de Google también introdujo soluciones para transacciones autónomas en las que el ser humano puede no estar presente en el momento exacto del pago, según una autorización previa.

Esa es una capa de confianza.

## Para qué está diseñado x402

x402 resuelve un problema más concreto y muy práctico: ¿cómo puede un servidor solicitar un pago antes de conceder acceso a un recurso?

Un cliente solicita un recurso. El servidor responde con HTTP 402 Pago requerido y detalles de pago. El cliente paga o adjunta comprobante de pago. El servidor verifica y devuelve el recurso.

Este patrón es especialmente útil para los agentes porque las transacciones pequeñas y automatizadas son incómodas en los sistemas de pago tradicionales. Un agente no debe crear una cuenta y negociar una suscripción solo para comprar una respuesta API.

## Por qué se pueden combinar AP2 y x402

En una pila híbrida, AP2 puede demostrar la autorización mientras x402 maneja la liquidación.

Flujo de ejemplo:

1. Un usuario autoriza a un agente a comprar datos de mercado premium hasta un presupuesto definido.2. AP2 captura la intención del usuario y los límites de autorización.
3. El agente llama a un punto final de datos protegido.
4. El punto final devuelve un requisito de pago x402.
5. El agente liquida a través de x402 dentro de los límites autorizados.
6. El comerciante o servicio conserva la prueba tanto de la autorización como del pago.

Esa pila es más fuerte que cualquiera de las capas por sí sola.

## Donde AP2 es más fuerte

AP2 es más fuerte cuando la transacción tiene riesgo legal, de cumplimiento, de fraude o de responsabilidad.

Los buenos casos de uso de AP2 incluyen:

1. Compras minoristas realizadas por un asistente
2. Adquisición basada en agentes
3. Reserva de viajes
4. Servicio de pólizas de seguro
5. Compras de alto valor con restricciones previamente autorizadas
6. Pagos de agente a agente cuando la responsabilidad importa

## Donde x402 es más fuerte

x402 es más fuerte cuando la transacción es pequeña, digital y directamente vinculada al acceso a los recursos.

Los buenos casos de uso de x402 incluyen:

1. Llamadas API pagas
2. Invocación de la herramienta MCP
3. Contenido web premium para agentes
4. Paquetes de datos
5. Inferencia por solicitud
6. Archivos de investigación legibles por máquina

## Implicaciones AEO

Los equipos AEO deben exponer los requisitos de pago y autorización en forma legible por máquina.

Para cada acción pagadera, documente:

1. Si la acción requiere autorización del usuario
2. Si se permite la ejecución autónoma
3. ¿Qué protocolos de pago son compatibles?
4. Si se acepta el pago x402
5. ¿Qué mandato o prueba de credencial se requiere?
6. Cómo se manejan los errores y los reembolsos
7. Cómo verifica un agente la finalización

Esta documentación debe estar vinculada desde [llms.txt](/llms.txt), el [centro de protocolos](/es/docs/protocols/) y las páginas de acciones relevantes.

## Preguntas frecuentes

**¿AP2 es mejor que x402?**
AP2 es mejor para autorización y responsabilidad. x402 es mejor para la liquidación de pagos HTTP directos. Resuelven diferentes capas.

**¿AP2 utiliza x402?**
AP2 es independiente del método de pago y puede funcionar con diferentes rieles. x402 se puede utilizar como mecanismo de liquidación en flujos compatibles con AP2.

**¿Deberían los proveedores de API implementar AP2?**
La mayoría de los proveedores de API deberían considerar primero x402 o MPP. AP2 se vuelve más importante cuando la acción API tiene autoridad delegada, alto riesgo o un mandato de compra.

**¿Deberían los comerciantes de comercio electrónico implementar x402?**
No como primer protocolo en la mayoría de los casos. Los comerciantes de comercio electrónico generalmente necesitan capas de comercio y autorización antes de la liquidación sin procesar por solicitud.

## Fuentes

Referencias principales: [anuncio de Google Cloud AP2](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol/), [actualización de Google AP2 FIDO Alliance](https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/), [documentación x402](https://docs.x402.org/faq) y [anuncio de la Fundación Linux x402](https://www.linuxfoundation.org/press/linux-foundation-is-launching-the-x402-foundation-and-welcoming-the-contribution-of-the-x402-protocol).

## Guías relacionadas* [arquitectura de comercio agente](/es/docs/agentic-commerce/)
* [protocolos de pago del agente](/es/docs/agent-payment-protocols-compared/)