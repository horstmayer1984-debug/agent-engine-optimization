---
title: "Agent UX y diseño Human-in-the-Loop: creación de interfaces."
metaTitle: "Agent UX y diseño Human-in-The-Loop."
date: 2026-04-12
weight: 86
category: "Guide"
description: "Diseñe la UX del agente con aprobaciones, vistas previas, reversibilidad y comentarios de estado claros para que las personas puedan supervisar acciones."
metaDescription: "Diseñe interfaces para humanos y agentes de IA con HTML semántico, aprobaciones, comentarios estructurados, mensajes de estado y flujos de trabajo."
summary: "Las interfaces modernas deben atender a dos audiencias simultáneamente: usuarios humanos y agentes de IA. El diseño receptivo al agente utiliza HTML semántico, puntos finales estructurados y bucles de retroalimentación para satisfacer ambos."
keywords:
  - diseño UX del agente
  - agentes humanos en el circuito
  - diseño responsivo del agente
  - diseño de interfaz dual
  - flujos de trabajo de aprobación de agentes
---
El diseño que responde a los agentes hace que las interfaces funcionen para dos audiencias simultáneamente: usuarios humanos que navegan visualmente y agentes de inteligencia artificial que analizan estructuralmente. Las mejores implementaciones no requieren interfaces separadas. Construyen un sistema que sirve a ambos a través de una arquitectura limpia.

## El desafío de la doble audiencia

La página de un producto debe persuadir a un comprador humano con diseño visual, narración de marca y desencadenantes emocionales. La misma página debe informar a un agente de IA con especificaciones estructuradas, precios precisos y disponibilidad explícita.

Estos no son objetivos contradictorios, sino objetivos diferentes. El error es optimizar para una audiencia y asumir que la otra está satisfecha.

Una página con bellas imágenes y una narrativa convincente, pero sin datos estructurados, sirve a los humanos y excluye a los agentes. Una página con puntos finales JSON sin formato y sin diseño visual sirve a los agentes y excluye a los humanos. El objetivo es una página unificada que contenga ambas capas.

## HTML semántico como base

Los agentes ignoran el contenido renderizado en JavaScript en la mayoría de los casos. Analizan el HTML sin formato. Los elementos semánticos (jerarquía de encabezados, elementos de tabla, elementos de lista, elementos de formulario, elementos de botón) proporcionan la información estructural que los agentes necesitan.

Utilice elementos HTML nativos en lugar de divs con estilo. Un elemento de botón le dice a un agente que existe una acción en la que se puede hacer clic. Un div diseñado para parecerse a un botón no le dice nada al agente.

Agregue atributos aria-label cuando el propósito del elemento no sea obvio a partir de su contenido. Un agente que analiza su página se beneficia de las mismas prácticas de accesibilidad que utilizan los lectores de pantalla.

Procesa en servidor todo el contenido crítico. Si el nombre, el precio y la disponibilidad de su producto requieren que aparezca JavaScript, los agentes no pueden verlos. La [guía de programación de sitios web para agentes](/es/docs/programming-websites-for-ai-agents/) cubre los requisitos técnicos.

## Flujos de aprobación humanos en el circuito

No todas las acciones de los agentes deberían completarse de forma autónoma. Diseñe flujos de aprobación que se detengan para la confirmación humana en decisiones de alto riesgo.

El flujo de aprobación tiene tres componentes: el agente propone una acción (que se muestra al ser humano en términos claros y estructurados), el ser humano revisa y aprueba o rechaza, y el sistema ejecuta o cancela según la decisión humana.

Para los puntos finales de su sitio, esto significa admitir flujos de trabajo asincrónicos. Un agente envía una solicitud de reserva. Su sistema devuelve un estado pendiente con un ID de tarea. Las revisiones humanas. Su sistema actualiza el estado a confirmado o rechazado. El agente sondea el ID de la tarea y recibe el estado final.Este patrón funciona para aprobaciones de compras por encima de un umbral de gasto, envíos de documentos legales, modificaciones de cuentas y cualquier acción que se beneficie del juicio humano.

## Interfaces de retroalimentación estructuradas

Tanto los humanos como los agentes deben informar los problemas. Pero informan de manera diferente.

Comentarios humanos: un cuadro de comentarios, una calificación de estrellas, un ticket de soporte. No estructurado, rico en contexto, requiere interpretación.

Comentarios del agente: un punto final estructurado que acepta la URL de una página, datos esperados, datos reales encontrados y clasificación de errores. No se necesita interpretación.

Construye ambos. El formulario de comentarios humanos en la página visible. El punto final de comentarios del agente documentado en su llms.txt y en su Tarjeta de agente. Ambos alimentan el mismo proceso de mejora a través de sus [bucles de retroalimentación](/es/docs/agent-feedback-loops/).

## Puntos finales WebSocket para sesiones en vivo

Las API REST estándar funcionan para interacciones sin estado. Los flujos de trabajo de agentes de varios pasos se benefician de las conexiones WebSocket que mantienen el estado de la sesión.

Un punto final WebSocket en /ws/agent-session permite a un agente mantener el contexto a través de una secuencia de acciones: explorar productos, limitar la selección, verificar la disponibilidad de la mejor opción y completar una compra. Cada paso ocurre en la misma conexión con estado compartido.

Para el paralelo humano: la misma lógica de sesión subyacente puede impulsar un flujo de compra guiado en la interfaz de usuario del navegador, utilizando la misma lógica de negocios a través de una interfaz diferente.

## Diseño para una degradación elegante

Su interfaz debe funcionar en todos los niveles de capacidad: experiencia de navegador humana completa (JavaScript, CSS, imágenes, interacción), experiencia de navegador reducida (conexión lenta, sin JavaScript), experiencia del agente (HTML sin formato, datos estructurados, puntos finales) y experiencia básica del agente (solo el contenido de texto HTML).

Cada capa atiende a un cliente diferente. Diseñe de manera que al quitar una capa no se rompan las capas debajo de ella. Si su JavaScript falla, el HTML aún debería contener información esencial. Si sus puntos finales no funcionan, el HTML aún debería ser legible.

La [guía de implementación de AEO](/es/docs/implement-aeo/) cubre la estructura de la capa de contenido.

---

## Preguntas frecuentes

**¿Qué es el diseño receptivo al agente?**
Un enfoque de diseño de interfaz que sirve tanto a usuarios humanos como a agentes de IA a través de una única arquitectura. El HTML semántico proporciona la capa legible por el agente. El diseño visual proporciona la capa humana. Ambos comparten los mismos datos subyacentes.

**¿Necesito interfaces separadas para los agentes?**
Normalmente no. Una página bien estructurada con HTML semántico, marcado de esquema y puntos finales documentados sirve a ambas audiencias. Las interfaces separadas son relevantes sólo para flujos de trabajo transaccionales complejos.**¿Cuál es el papel del ser humano en el circuito en AEO?**
Proporciona una red de seguridad para acciones de agentes de alto riesgo. El agente propone, el humano aprueba, el sistema ejecuta. Esto genera confianza y evita errores costosos en sistemas totalmente autónomos.

**¿Cómo ayudan los puntos finales de WebSocket a los agentes?**
Mantienen el estado de la sesión en flujos de trabajo de varios pasos, evitando la pérdida de contexto entre llamadas REST secuenciales. Esto es particularmente útil para flujos de compra e interacciones de servicios complejas.

**¿Debería priorizar la UX humana o la UX del agente?**
Ambos. Si se ve obligado a elegir un punto de partida, la UX humana con HTML semántico le ofrece ambas audiencias. Los puntos finales específicos del agente (MCP, WebSocket) se pueden agregar de forma incremental.

## Referencias primarias

* [Marco de gestión de riesgos de IA del NIST](https://www.nist.gov/itl/ai-risk-management-framework)
* [Documentación de Schema.org](https://schema.org/docs/documents.html)