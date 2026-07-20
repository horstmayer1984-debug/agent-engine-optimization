---
title: "Autenticación agente para el comercio: FIDO, AP2 e intención."
metaTitle: "Autenticación Agentica para Comercio."
date: 2026-05-25
weight: 152
category: "Architecture"
description: "Descubra cómo está surgiendo la autenticación agente para el comercio, cómo FIDO, AP2 y Verifiable Intent respaldan las compras delegadas y qué deben."
summary: "Una guía para la autenticación agente en el comercio, que cubre los grupos de trabajo de FIDO, los mandatos AP2, la intención verificable de Mastercard, la identidad, la privacidad y la confianza del comerciante."
keywords:
  - comercio de autenticación agente
  - Autenticación agente FIDO
  - Intención verificable
  - Pagos de agentes AP2
  - comercio de identidad del agente
---
# Autenticación Agentic para Comercio

La autenticación agente es la capa de confianza que demuestra que un usuario autorizó a un agente de IA a actuar. Es importante porque el comercio mueve dinero real, inventario, lealtad y responsabilidad. AP2, Verifiable Intent y el trabajo de autenticación agente de FIDO convergen en torno a una necesidad central: hacer que la intención delegada sea explícita, verificable, privada y auditable.

## Por qué el inicio de sesión normal no es suficiente

El pago tradicional supone que el ser humano está presente. Inician sesión, hacen clic en comprar, se autentican y pagan. El comercio de agentes cambia eso. El agente puede buscar, crear un carrito y ejecutarlo dentro de las reglas del usuario.

Esto plantea nuevas preguntas:

- ¿Quién autorizó al agente?
- ¿Qué se le permitió hacer exactamente al agente?
- ¿El usuario estuvo presente o no?
- ¿Recibió el comerciante la misma intención que le dio el usuario?
- ¿Qué pruebas existen si se disputa la transacción?

La [documentación AP2](https://ap2-protocol.org/) enmarca esto como una necesidad de intenciones verificables y pistas de auditoría.

## Qué está haciendo FIDO

La Alianza FIDO anunció trabajos sobre interacciones y comercio de agentes de IA confiables. Incluye un grupo de trabajo técnico de autenticación de agentes centrado en cómo los usuarios pueden delegar acciones a agentes de IA con autenticación, privacidad y seguridad sólidas.

Google también anunció que donará AP2 a FIDO y que el marco de intención verificable de Mastercard se contribuirá en el mismo camino de estándares.

Para los comerciantes, la señal es clara: la identidad del agente y la autenticación delegada se están convirtiendo en infraestructura comercial.

## AP2 frente a intención verificable frente a FIDO

| Capa | Rol |
|
---|
---|
| AP2 | Protocolo de autorización de pago con mandatos de pago y pago |
| Intención verificable | Capa de confianza que vincula identidad, intención y acción en un registro que preserva la privacidad |
| FIDO | Organismo de normalización para la autenticación y el trabajo relacionado con la interacción de agentes |
| Sistemas comerciales | Hacer cumplir las decisiones sobre políticas, pago, cumplimiento y soporte |

Esto se conecta a [AP2 vs x402](/es/docs/ap2-vs-x402/) y [Visa TAP vs Mastercard Agent Pay](/es/docs/visa-tap-mastercard-agent-pay/).

## Implicaciones de la implementación del comerciante

Los comerciantes deben prepararse para almacenar y validar:

- identidad del agente o estado de agente verificado
- estado de autorización del usuario
- alcance de intención
- referencia del carrito
- referencia del mandato de pago
- decisión política
- eventos de auditoría con marca de tiempo
- estados de revocación y cancelación

Esta no es sólo una función de pago. Afecta el soporte, el fraude, los reembolsos, la lealtad y el cumplimiento.

## Tabla de preparación para la autenticación

| Pregunta del comerciante | Por qué es importante |
|
---|
---|
| ¿Podemos distinguir una sesión humana de una sesión de agente? | La política y el riesgo difieren || ¿Podemos verificar quién autorizó al agente? | La compra delegada necesita prueba |
| ¿Podemos ver el alcance de la intención? | Los agentes deben mantenerse dentro de las limitaciones |
| ¿Podemos almacenar evidencia de auditoría? | Las disputas necesitan hechos |
| ¿Pueden los usuarios revocar la autoridad del agente? | El control debe permanecer en el usuario |

La página [evidencia de disputas comerciales de agentes](/es/docs/agentic-commerce-dispute-evidence/) profundiza en la capa de auditoría.

## Preguntas frecuentes

### ¿La autenticación agente es lo mismo que la autenticación de pago?

No. La autenticación de pago verifica una acción de pago. La autenticación agente también necesita verificar la delegación, el alcance, la identidad del agente y la intención del usuario.

### ¿Por qué es importante FIDO?

FIDO tiene experiencia en la creación de estándares de autenticación abiertos. Sus nuevos grupos de trabajo pueden ayudar al comercio de agentes a evitar sistemas de confianza propietarios fragmentados.

### ¿Está esto listo para todos los comerciantes?

Aún no. La mayoría de los comerciantes deben preparar primero los datos de los productos, las políticas y la observabilidad del proceso de pago mientras monitorean AP2, Verifiable Intent y la adopción de FIDO.

### ¿Cómo afecta esto al AEO?

Los agentes necesitan rutas de ejecución confiables. La autenticación es una de las puertas entre el contenido legible y la acción segura.

## Fuentes

Fuentes principales: [FIDO sobre interacciones confiables con agentes de IA](https://fidoalliance.org/fido-alliance-to-develop-standards-for-trusted-ai-agent-interactions/), [donación de AP2 de Google a FIDO](https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/), [documentación de AP2](https://ap2-protocol.org/) e [intención verificable de Mastercard](https://www.mastercard.com/europe/en/news-and-trends/stories/2026/verifiable-intent.html).