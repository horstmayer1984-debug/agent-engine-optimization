---
title: "Botones de agente, API y esquema de acción para AEO."
date: 2026-04-12
weight: 57
category: "Architecture"
description: "Descubra cómo los botones de agente, las API y el esquema de acción exponen los siguientes pasos seguros para que los agentes de IA puedan completar."
summary: "Los botones de agente, el esquema de acción y los puntos finales de API transforman las páginas de contenido estático en superficies donde los agentes de IA pueden ejecutar transacciones comerciales reales. Aquí está la guía de implementación completa."
keywords:
  - implementación de botones de agente
  - esquema de acción AEO
  - Esquema de acción potencial
  - API de transacción del agente
  - Seguridad de terminales AEO
---
Es útil una página de contenido que un agente pueda leer. Es útil una página de contenido a través de la cual un agente pueda actuar. Los botones del agente, el esquema de acción y los puntos finales de API documentados son los que marcan la diferencia. Transforman superficies de publicación estáticas en interfaces transaccionales donde los sistemas autónomos pueden verificar la disponibilidad, solicitar cotizaciones, reservar citas y completar compras.

## ¿Qué son realmente los botones de agente?

Un botón de agente no es un botón visual diseñado para clics humanos. Es una ruta de acción claramente documentada que le dice a un agente: esta tarea específica se puede realizar aquí, estas son las entradas requeridas y este es el punto final al que llamar.

El botón visual de la página sirve al visitante humano. El esquema subyacente y la documentación del punto final sirven al agente. Ambos apuntan al mismo proceso de negocio, pero a través de diferentes interfaces.

## Implementando esquema de acción con PotentialAction

Schema.org proporciona el tipo PotentialAction específicamente para describir acciones disponibles en una página. Úselo para decirles a los agentes lo que pueden hacer.

Para una página de servicio con reserva de citas, la estructura del esquema incluye: el tipo de acción (ReserveAction o ScheduleAction), la URL de destino (su punto final de reserva), las propiedades de entrada requeridas (fecha, hora, tipo de servicio, información de contacto) y el tipo de resultado (Reserva con número de confirmación).

Para una página de producto con capacidad de compra, use BuyAction con la URL de destino que apunte a su carrito o punto final de pago, ingrese propiedades para la selección de cantidad y variante, y el tipo de resultado que describa la confirmación del pedido.

Para una solicitud de cotización, use QuoteAction (o Acción genérica con un nombre descriptivo) con la URL de destino que apunte al punto final de su cotización y propiedades de entrada para las especificaciones que requiere la cotización.

El principio clave: cada esquema de acción debe corresponder a un punto final real y funcional. No agregue esquemas de acción para capacidades que aún no existen. Los agentes que intenten realizar una acción y fracasen perderán la prioridad de su sitio.

## Construyendo los puntos finales de la API

No es necesario que los puntos finales de acción sean API REST de nivel empresarial desde el primer día. Deben aceptar información estructurada, realizar la acción comercial y devolver una respuesta estructurada.

Un punto final mínimo acepta una carga útil JSON con los campos obligatorios, valida la entrada, desencadena el proceso de negocio (envía un correo electrónico, crea un registro, llama a una API externa) y devuelve una respuesta JSON con el estado, el identificador de confirmación y los siguientes pasos.Para equipos sin recursos de desarrollo backend, los puntos finales de webhook n8n o Make.com manejan bien este patrón. Cree un webhook que acepte JSON, agregue pasos de validación, conéctese a sus herramientas comerciales (calendario, CRM, correo electrónico) y devuelva una respuesta estructurada.

Requisitos de seguridad para puntos finales orientados al agente: valide todas las entradas con los tipos y rangos esperados. Solicitudes de límite de tarifas para evitar abusos. Requerir autenticación para cualquier punto final que modifique el estado. Registre todas las solicitudes con fines de auditoría. Devuelva mensajes de error claros que ayuden a los agentes a comprender qué salió mal.

## Conexión de botones a puntos finales

En cada página donde esté disponible una acción, incluya tres cosas:

Un llamado a la acción visible para los visitantes humanos (un botón o enlace con texto claro como "Verificar disponibilidad" o "Solicitar una cotización").

Esquema de acción en el marcado de la página que describe el punto final, las entradas y la salida esperada.

Documentación del punto final (ya sea en línea o vinculado) que especifica el formato de solicitud exacto, los encabezados requeridos y la estructura de respuesta.

Esta triple capa asegura que tanto los humanos como los agentes puedan encontrar y utilizar la acción, a través de sus respectivas interfaces.

## Mejores prácticas de seguridad

Nunca exponga puntos finales de escritura sin autenticación. Incluso los puntos finales de webhook simples deberían requerir una clave API o un token en el encabezado de la solicitud.

Implemente una validación de entrada que rechace solicitudes con formato incorrecto antes de que lleguen a su lógica empresarial. Un agente que envía un formato de fecha no válido debería recibir un error claro, no un fallo del sistema.

Utilice claves de idempotencia para cualquier acción que cree o modifique el estado. Si la misma solicitud llega dos veces (común con los reintentos del agente), la segunda solicitud debería devolver el mismo resultado sin crear una reserva o un pedido duplicado.

Registre cada interacción del agente. Marcas de tiempo, cargas útiles de solicitud, cargas útiles de respuesta e identificador del agente de origen. Esto es esencial para los [bucles de retroalimentación](/es/docs/agent-feedback-loops/) que mejoran la precisión con el tiempo.

El [artículo sobre el plano de control universal](/es/docs/universal-control-plane/) cubre la arquitectura de gobernanza completa para puntos finales orientados al agente.

## Transacciones del agente de prueba

Antes de ponerlo en marcha, pruebe cada punto final con estas comprobaciones:

¿Se puede descubrir el punto final a través del esquema de acción en la página? Analice la página como lo haría un agente y verifique que el esquema apunte a una URL que funcione.

¿El punto final acepta el formato de entrada documentado y devuelve el formato de salida documentado? Envíe una solicitud válida y verifique que la respuesta coincida con la descripción del esquema.¿El punto final maneja correctamente las entradas no válidas? Envíe solicitudes con formato incorrecto y verifique que las respuestas de error sean estructuradas e informativas.

¿El punto final maneja solicitudes duplicadas de forma segura? Envíe la misma solicitud válida dos veces y verifique que no se creen acciones duplicadas.

¿El punto final responde dentro de una latencia aceptable? Los agentes normalmente expiran después de 10 a 30 segundos. Su punto final debería responder bien dentro de esa ventana.

---

## Preguntas frecuentes

**¿Los botones de agente reemplazan a los botones de cara humana?**
No. Coexisten. El botón visual sirve a los visitantes humanos. El esquema de acción y el punto final sirven a los agentes. Ambos desencadenan el mismo proceso de negocio.

**¿Qué es PotentialAction en Schema.org?**
Un tipo de esquema que describe una acción disponible en una página. Incluye el tipo de acción, la URL de destino, las entradas requeridas y el resultado esperado. Los agentes lo utilizan para descubrir qué pueden hacer en su sitio.

**¿Cómo puedo proteger los terminales orientados al agente?**
Exija autenticación (claves API o tokens), valide todas las entradas, implemente limitación de velocidad, use claves de idempotencia para acciones de cambio de estado y registre todas las solicitudes.

**¿Puedo usar herramientas sin código para los puntos finales de los agentes?**
Sí. n8n y Make.com admiten puntos finales de webhook que aceptan JSON estructurado, realizan lógica empresarial y devuelven respuestas estructuradas. Manejan los patrones de transacciones de agentes más básicos.

**¿Qué pasa si mi esquema de acción describe una capacidad que no está disponible temporalmente?**
Devuelva una respuesta de error clara y estructurada que explique la falta de disponibilidad y cuándo se espera que se reanude el servicio. No deje esquemas de acción rotos en páginas donde la capacidad ya no existe.

## Guías relacionadas

* [Protocolos de agente de IA](/es/docs/protocols/)

## Referencias primarias

* [Directrices de datos estructurados de Google](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
* [Documentación de Schema.org](https://schema.org/docs/documents.html)