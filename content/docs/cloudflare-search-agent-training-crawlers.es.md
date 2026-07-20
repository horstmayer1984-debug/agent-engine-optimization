---
title: "Rastreadores de búsqueda, agentes y capacitación de Cloudflare."
metaTitle: "Búsqueda de Cloudflare, agente y rastreadores de capacitación."
date: 2026-07-02
weight: 188
category: "Analysis"
description: "Cloudflare ahora separa el tráfico de IA en rastreadores de búsqueda, agentes y capacitación. Descubra lo que esto significa para AEO, robots.txt y acceso."
summary: "Una guía práctica de AEO para la taxonomía de tráfico de IA de Cloudflare de julio de 2026 para rastreadores de búsqueda, agentes y capacitación."
keywords:
  - Rastreadores de capacitación del agente de búsqueda de Cloudflare
  - Taxonomía de rastreadores de IA
  - acceso al rastreador del agente
  - Controles de tráfico de IA
  - Política de rastreadores AEO
---
# Rastreadores de búsqueda, agentes y capacitación de Cloudflare

Los controles de tráfico de IA de Cloudflare de julio de 2026 dividen el tráfico de IA automatizado en tres categorías prácticas: búsqueda, agente y capacitación. Para los equipos AEO, el cambio importante es que la política de rastreadores ya no puede ser una opción contundente de "permitir IA" o "bloquear IA". La visibilidad de búsqueda, la ejecución de tareas de agentes y la capacitación de modelos ahora necesitan reglas separadas.

## Qué cambió en julio de 2026

El 1 de julio de 2026, Cloudflare anunció [nuevas opciones de tráfico de IA para todos los clientes](https://blog.cloudflare.com/content-independence-day-ai-options/). Los nuevos controles clasifican la automatización relacionada con la IA por finalidad:

| Categoría | Lo que significa | Implicación AEO |
|
---|
---|
---|
| Buscar | Rastrear o indexar contenido para poder encontrarlo más tarde | Generalmente vale la pena permitir páginas de descubrimiento público |
| Agente | Automatización dirigida por el usuario que visita un sitio para completar una tarea | Necesita UX, permisos y manejo de errores seguros para la acción |
| Formación | Rastreo de contenido para entrenar o ajustar modelos | A menudo necesita una decisión legal, de licencia o de monetización por separado |

Cloudflare dice que las opciones están disponibles para todos los clientes, incluidos los usuarios de nivel gratuito. Esto es importante porque la gobernanza de los rastreadores está pasando de un control exclusivo de la empresa a una decisión de publicación normal.

## Por qué esto es importante para Agent Engine Optimization

El SEO tradicional trataba a los rastreadores principalmente como indexadores. AEO debe tratar a los visitantes automatizados como actores diferentes:

- un rastreador de búsqueda que ayuda a los usuarios a descubrir una página
- un motor de respuestas que puede citar o resumir la página
- un agente de navegador que puede hacer clic, comparar o enviar
- un rastreador de capacitación que puede absorber el contenido sin devolver el tráfico

Es por eso que [Agent Engine Optimization](/es/docs/what-is-aeo/) separa la [Capa de lectura](/es/docs/answer-engine-optimization/) de la [Capa de ejecución](/es/docs/execution-layer/). Los rastreadores de búsqueda pertenecen principalmente a la capa de lectura. Los rastreadores de agentes están más cerca de la ejecución.

## El cambio predeterminado del 15 de septiembre de 2026

Cloudflare también anunció un cambio predeterminado programado para los nuevos dominios que se incorporan a Cloudflare el 15 de septiembre de 2026. Para las páginas con publicidad, las categorías Capacitación y Agentes se bloquearán de manera predeterminada, mientras que la Búsqueda seguirá permitida de manera predeterminada.

El detalle que los equipos AEO no deben perderse: los rastreadores multipropósito pueden verse afectados por la regla seleccionada más restrictiva. Cloudflare señala explícitamente que los rastreadores que combinan Búsqueda con Capacitación pueden bloquearse cuando el propietario de un sitio decide bloquear la Capacitación.

Eso crea un riesgo real para el SEO. Un editor puede intentar bloquear la capacitación pero restringir accidentalmente un rastreador que también admite el descubrimiento de búsqueda.

## Política de rastreador recomendada por tipo de página| Tipo de página | Buscar | Agente | Formación | Notas |
|
---|
---:|
---:|
---:|
---|
| Página de inicio pública | Permitir | Generalmente permitir | Decidir por modelo de negocio | Mantenga la marca visible |
| Páginas de productos | Permitir | Permitir con límites de tarifa | Generalmente restringir o licenciar | Los datos del producto deben estar actualizados |
| Documentación | Permitir | Permitir | Decidir | Los agentes necesitan documentos para completar tareas |
| Pagar | Restringir | Permitir sólo con controles estrictos | Bloquear | Las reglas de pago e identidad importan |
| Investigación pagada | Quizás permita fragmentos | Restringir | Bloquear o monetizar | Considere resúmenes y detalles privados |
| Herramientas internas | Bloquear | Sólo autenticación | Bloquear | Sin valor de rastreador público |

Esto debe combinarse con [AI Crawlers and robots.txt](/es/docs/ai-crawlers-robots-txt/) y [Cloudflare AI Crawl Control](/es/docs/cloudflare-ai-crawl-control/).

## Lista de verificación de implementación

1. Enumere los tipos de páginas públicas de alto valor.
2. Decida qué páginas necesitan visibilidad de búsqueda.
3. Decidir dónde se debe permitir que actúen los agentes dirigidos por el usuario.
4. Separar el uso de capacitación del uso de búsqueda en el lenguaje de políticas.
5. Revise los controles de tráfico de IA de Cloudflare si el sitio se ejecuta detrás de Cloudflare.
6. Audite si las reglas de firewall existentes bloquean a los referentes o agentes de IA conocidos.
7. Supervise el volumen de rastreo y las referencias después de cambiar las reglas.

No copie la lista de bloqueo de un competidor. Un sitio de medios, un centro de documentación SaaS, una tienda de comercio electrónico y un negocio de API tienen diferentes necesidades de exposición y monetización.

## Error de AEO que se debe evitar

El mayor error es tratar al "rastreador de IA" como una sola intención. Un agente de navegador que intenta comprar un producto para un usuario no es lo mismo que un rastreador de entrenamiento que toma contenido para mejorar el modelo. Si ambos están bloqueados por una regla, el sitio puede proteger el contenido pero perder conversiones asistidas por agentes.

## Preguntas frecuentes

### ¿Todos los sitios deberían permitir rastreadores de búsqueda?

La mayoría de los sitios públicos deberían permitir rastreadores de búsqueda de buena reputación en páginas indexables. Las excepciones incluyen URL privadas, pagas, restringidas legalmente o de bajo valor.

### ¿Deberían permitirse los rastreadores de agentes?

Solo donde el agente pueda completar tareas seguras que beneficien al usuario. Las páginas de solo lectura son más simples que los carritos, los formularios, los cambios de cuenta o las compras.

### ¿El rastreo de entrenamiento es malo para el AEO?

No automáticamente. Algunas marcas pueden aceptarlo por motivos de visibilidad o de licencia. Otros pueden restringirlo porque no crea referencias directas.

### ¿Bloquear la formación puede perjudicar el SEO?

Puede ser posible si un rastreador tiene múltiples propósitos y la infraestructura aplica la categoría más restrictiva. La actualización de julio de 2026 de Cloudflare hace que ese riesgo sea más explícito.

## FuentesFuente principal: [Cloudflare: Tu sitio, tus reglas](https://blog.cloudflare.com/content-independence-day-ai-options/). Contexto de implementación relacionado: [Documentos de Cloudflare AI Crawl Control](https://developers.cloudflare.com/ai-crawl-control/).