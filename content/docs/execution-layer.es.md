---
title: "La capa de ejecución: donde actúan los agentes de IA."
description: "Descubra qué es la capa de ejecución, por qué la necesitan los agentes de IA y cómo los sitios web exponen acciones, datos en tiempo real, verificación."
summary: "Una guía para la capa de ejecución: la infraestructura que permite a los agentes autónomos de IA actuar a través de API, herramientas, datos y puntos finales de transacciones."
keywords:
  - capa de ejecución
  - Optimización del motor del agente
  - acciones del agente
  - infraestructura lista para agentes
date: 2026-03-09
weight: 3
category: "Architecture"
---
Cuando un sistema de inteligencia artificial cita su contenido en una respuesta generada, esa es la capa de lectura funcionando. Útil, pero pasivo.

Cuando un agente de IA utiliza su API para verificar el inventario en tiempo real, lo compara con las restricciones presupuestarias de un usuario y completa una compra, esa es la capa de ejecución. Activo, transaccional y fundamentalmente diferente en lo que requiere de su infraestructura.

La capa de ejecución es donde AEO se separa de todo lo anterior. No es un problema de optimización de contenidos. Es un **problema de arquitectura de infraestructura**.

---

## Qué agentes necesitan actuar

Un agente autónomo que realiza una tarea (reservar una habitación de hotel de menos de 150 euros en Barcelona para el próximo martes) necesita:

### 1. Descubrimiento

Encuentre servicios que coincidan con el tipo de tarea. Esto es en parte un problema de la capa de lectura. Los datos estructurados, el marcado de esquema y la indexación adecuada ayudan a los agentes a descubrir su servicio. Pero el descubrimiento por sí solo no permite actuar.

### 2. Comprensión de la capacidad

Sepa qué puede hacer su servicio y bajo qué limitaciones. El agente necesita una descripción legible por máquina de sus capacidades: qué acciones están disponibles, qué parámetros aceptan, qué resultados devuelven, qué restricciones se aplican. Esto es lo que proporcionan los manifiestos de capacidad y las descripciones de las herramientas MCP.

### 3. Acceso a datos en tiempo real

Obtenga precios, disponibilidad y condiciones actuales. Las páginas HTML estáticas con los precios de ayer no funcionan. El agente necesita un punto final que devuelva datos estructurados y actuales que pueda evaluar mediante programación.

### 4. Coincidencia de restricciones

Evalúe si su oferta se ajusta a los requisitos del usuario. ¿Presupuesto inferior a 150 euros? Disponible el martes? ¿En Barcelona? ¿Incluye desayuno? El agente debe comparar estas restricciones con sus datos. Esto requiere datos estructurados y deterministas, no textos de marketing.

### 5. Ejecución de acciones

Activar la reserva, compra o solicitud. El agente necesita un punto final de transacción. Aquí es donde entran protocolos como UCP (para comercio) y MCP (para acceso general a herramientas).

### 6. Verificación del estado

Confirme que la acción fue exitosa. ¿Se realizó la reserva? El agente necesita transiciones de estado observables: disponible, reservado, confirmado. Sin verificación, el agente no puede informar de manera confiable.

---

## Los bloques de construcción

### Esquemas de acción

Schema.org define tipos de acciones como BuyAction, ReserveAction, OrderAction. Estos les dicen a los agentes qué acciones son posibles en una página o a través de un servicio. La mayoría de los sitios web utilizan Schema.org únicamente para marcado informativo. Extenderlo al marcado a nivel de acción es un primer paso que no requiere API backend.

### Manifiestos de capacidadUn documento legible por máquina que describe lo que puede hacer un servicio, qué protocolos admite y cómo interactuar con él. Piense en ello como un archivo robots.txt para las capacidades del agente, excepto que en lugar de decir lo que puede rastrear, dice lo que puede hacer.

### Entradas y salidas deterministas

Las páginas de marketing están diseñadas para la persuasión humana. Los datos de cara al agente deben diseñarse para la toma de decisiones por parte de las máquinas: parámetros fijos, formatos de respuesta estructurados, valores inequívocos, códigos de error legibles por máquinas.

Lo que dice el sitio web:

> "Nuestro plan premium comienza en solo $49 al mes con todas las funciones que su equipo necesita".

Qué necesita el agente:

```json
{
  "plan": "premium",
  "price": { "amount": 49, "currency": "USD", "interval": "month" },
  "features": ["feature_a", "feature_b", "feature_c"],
  "limits": { "users": 50, "storage_gb": 100 },
  "trial": { "available": true, "days": 14 }
}
```

### Compatibilidad de protocolos

**MCP (Protocolo de contexto de modelo)**: permite que los modelos de IA accedan a herramientas y datos externos a través de una interfaz estandarizada. Un comerciante con un servidor MCP permite que cualquier agente compatible con MCP consulte su catálogo sin una integración personalizada.

**UCP (Protocolo de comercio universal)**: estandariza todo el proceso de compra para que cualquier agente pueda realizar transacciones con cualquier comerciante utilizando el mismo protocolo.

**A2A (Agente a agente)**: permite a los agentes delegar tareas a agentes especializados.

Las organizaciones que implementan estos protocolos tempranamente se convierten en las opciones predeterminadas para la finalización de tareas de los agentes.

### Transiciones estatales

Los agentes necesitan verificar que las acciones produzcan los resultados esperados. Esto requiere transiciones de estado observables:

`available > reserved > payment_pending > confirmed > fulfilled`

Cada transición debe ser consultable. Sin esto, los agentes no pueden gestionar de forma fiable flujos de trabajo de varios pasos.

### Confianza y verificación

Un agente que reserve un viaje de 2.000 euros debe confiar en la fuente. Las señales de confianza para los agentes son diferentes de las señales de confianza para los humanos. Los agentes necesitan identidades comerciales verificables, recibos de transacciones firmados criptográficamente (AP2), datos consistentes y precisos en todos los puntos de contacto, documentación de restricciones transparente y pistas de auditoría.

---

## Qué significa esto para su organización

La capa de ejecución no es algo que se construye de la noche a la mañana. Es una capacidad que se desarrolla de forma incremental:

**Fase 1 (ahora):** Audite la preparación actual de su agente. Evalúe los datos estructurados, la cobertura del esquema, la estructura del contenido y la superficie API existente.

**Fase 2 (de 3 a 6 meses):** Implemente optimizaciones de la capa de lectura y comience a planificar la infraestructura de la capa de ejecución. Agregue esquemas de acción, cree documentación de capacidades, evalúe la compatibilidad del protocolo.

**Fase 3 (6 a 18 meses):** Desarrollar capacidades de capa de ejecución. Exponga API, implemente compatibilidad de protocolos, cree puntos finales de datos orientados al agente, desarrolle mecanismos de verificación de estado.[Auditoría de preparación de AEO](/es/docs/audit/): comience con una evaluación sistemática.

[¿Qué es AEO?](/es/docs/what-is-aeo/): definición y alcance completos.

## Preguntas frecuentes

### ¿La capa de ejecución reemplaza la interfaz del sitio web?

No. Las interfaces humanas siguen siendo importantes. La capa de ejecución agrega rutas estructuradas que el software puede usar sin tener que adivinar cómo funciona una interfaz visual.

### ¿Qué hace que una acción sea segura para los agentes?

La acción necesita entradas explícitas, validación, autorización, estados estables, reintentos limitados, errores claros y un resultado que pueda verificarse.

### ¿Deberían los equipos exponer cada acción interna?

No. Exponga únicamente acciones con un beneficio de usuario definido, modelo de permiso, propietario, registro de auditoría y proceso de recuperación de fallas.

## Guías relacionadas

* [arquitectura de comercio agente](/es/docs/agentic-commerce/)

## Referencias primarias

* [Marco de gestión de riesgos de IA del NIST](https://www.nist.gov/itl/ai-risk-management-framework)
* [Documentación de Schema.org](https://schema.org/docs/documents.html)