---
title: "Cómo escribir llms.txt correctamente para que los agentes de IA."
metaTitle: "Cómo escribir llms.txt para agentes de IA."
date: 2026-04-12
weight: 62
category: "Guide"
description: "llms.txt es el mecanismo de descubrimiento de agentes más simple y capaz. Estructura exacta, reglas de contenido, generación dinámica para sitios grandes e."
metaDescription: "Aprenda a escribir llms.txt para agentes de IA, incluida la estructura, las reglas de contenido, la generación dinámica y la integración de esquemas."
summary: "llms.txt les dice a los agentes de IA qué ofrece su sitio y cómo interactuar con él. Esta guía cubre el formato exacto, las reglas de contenido, los errores comunes y cómo generarlo dinámicamente para sitios grandes."
keywords:
  - guía llms.txt
  - formato llms.txt
  - cómo escribir llms.txt
  - descubrimiento de agentes llms.txt
  - Implementación de llms.txt
---
llms.txt es la forma más sencilla y eficaz de hacer que los agentes de IA descubran su sitio web. Un archivo Markdown en la raíz de su sitio les dice a los agentes qué ofrece, dónde encontrarlo y cómo interactuar con él. Los agentes buscan llms.txt antes de rastrear el sitio completo, por lo que hacerlo bien significa ser descubierto primero.

## Por qué llms.txt no es negociable en 2026

Los agentes de IA siguen una jerarquía de descubrimiento cuando encuentran un sitio nuevo. Primero, busque llms.txt. En segundo lugar, busque agent-card.json. En tercer lugar, busque datos estructurados en HTML. Cuarto, intente analizar el contenido de la página sin formato.

Un sitio sin llms.txt obliga a los agentes a comenzar en el paso tres o cuatro, que es más lento, menos confiable y es más probable que produzca una extracción inexacta. Un sitio con un llms.txt claro permite a los agentes comprender el alcance completo de su oferta en una sola solicitud.

Stripe, Cloudflare y Cursor ya publican archivos llms.txt. Los sitios que adoptaron temprano reportan tasas de interacción de agentes significativamente más altas y citas más precisas en las respuestas generadas por IA.

## La estructura exacta

llms.txt es un archivo Markdown. Utiliza títulos para organizar la información y texto sin formato para las descripciones. Aquí está la estructura recomendada:

**Línea 1: nombre del sitio como encabezado H1.** Una línea, texto sin formato.

**Sección 1: Qué ofrece este sitio.** Un breve párrafo (de 2 a 3 oraciones) que describe su producto, servicio o contenido en términos objetivos. Sin lenguaje de marketing. Indique qué hace, para quién es y qué lo hace útil.

**Sección 2: Páginas clave.** Una lista de las URL más importantes con una descripción de una línea de cada una. Incluya su página de inicio, páginas principales de productos o servicios, página de precios, documentación y cualquier página donde los agentes deban buscar información específica.

**Sección 3: Puntos finales disponibles.** Si su sitio expone puntos finales API o herramientas MCP, enumerelos con descripciones breves de lo que hace cada uno, qué entradas requiere y qué devuelve.

**Sección 4: Autenticación.** Indique cómo deben autenticarse los agentes o indique explícitamente que no se requiere autenticación para el acceso de lectura.

**Sección 5: Restricciones.** Límites de tarifas, políticas de uso, garantías de actualización de datos y cualquier restricción sobre cómo los agentes deben interactuar con su sitio.

**Sección 6: Contacto.** Cómo reportar errores o solicitar aclaraciones.

## Reglas de contenido

Escriba para extraer, no para persuadir. Cada oración debe contener un hecho que un agente pueda utilizar. Elimina los adjetivos que no lleven información. Reemplace "nuestra plataforma capaz" por "plataforma de programación basada en API para proveedores de atención médica".Mantenga las descripciones en una o dos oraciones por elemento. Los agentes no necesitan párrafos. Necesitan afirmaciones precisas que puedan comparar con las consultas de los usuarios.

Actualice llms.txt cada vez que agregue, elimine o cambie una capacidad importante. Un llms.txt desactualizado que describa características que usted ya no ofrece es peor que ningún llms.txt porque hace que los agentes intenten acciones que fallarán.

## Generación dinámica para sitios grandes

Los sitios con cientos de productos o inventario que cambia con frecuencia deberían generar llms.txt dinámicamente en lugar de mantenerlo manualmente.

Cree un script que consulte la base de datos de su producto, extraiga el resumen del catálogo actual, enumere los puntos finales API activos de su configuración de ruta y escriba el resultado como un archivo Markdown. Ejecute este script según una programación (diariamente para la mayoría de los sitios, cada hora para sitios con mucho inventario).

Para los sitios basados ​​en Hugo, puede generar llms.txt como parte del proceso de compilación creando un formato de salida personalizado que represente los datos de su contenido como Markdown.

## Integrando llms.txt con marcado de esquema

llms.txt y el marcado de esquema tienen propósitos complementarios. llms.txt proporciona descubrimiento a nivel de sitio (qué ofrece todo este sitio). El marcado de esquema proporciona detalles a nivel de página (qué contiene esta página específica).

Haga referencia a su llms.txt desde el marcado de su esquema incluyéndolo en el esquema de su sitio web como un objetivo de acción potencial. Haga referencia a sus páginas marcadas con esquemas más importantes en la sección de páginas clave de llms.txt.

Esto crea un sistema de descubrimiento de dos capas: los agentes que comienzan con llms.txt encuentran las páginas marcadas con esquema más rápidamente, y los agentes que comienzan con una página específica pueden navegar a llms.txt para ver la imagen completa del sitio.

## Comparación: con vs sin llms.txt

| Métrica | Sin llms.txt | Con llms.txt |
|
---|
---|
---|
| Tasa de descubrimiento de agentes | Por debajo del 10 por ciento | Hasta el 80 por ciento |
| Tiempo hasta la interacción del primer agente | Días (requiere gatear) | Segundos (lectura de un solo archivo) |
| Precisión de extracción | Variable (depende de la calidad de la página) | Alto (resumen estructurado) |
| Tasa de retorno del agente | Bajo | Significativamente mayor |

## Errores comunes

Escribir llms.txt como texto de marketing. Los agentes no responden a la persuasión. Responden a hechos estructurados. Cada línea debe responder una pregunta específica sobre lo que puede hacer su sitio.

Listado de todas las páginas del sitio. llms.txt no es un mapa del sitio. Incluya solo las páginas que más importan para la interacción del agente. Para un sitio de 500 páginas, el llms.txt debe hacer referencia a entre 10 y 30 páginas clave.

Olvidándose de actualizarlo. Un llms.txt que haga referencia a puntos finales obsoletos o productos descontinuados perjudica activamente la confianza de los agentes.La [guía de implementación de AEO] (/docs/implement-aeo/) cubre cómo llms.txt encaja en la ruta de optimización más amplia.

---

## Preguntas frecuentes

**¿Dónde se debe colocar exactamente llms.txt?**
En la raíz de su dominio: sudominio.com/llms.txt. Los agentes lo buscan en esta ruta exacta, similar a robots.txt.

**¿Qué formato debería utilizar llms.txt?**
Rebaja. Utilice títulos para las secciones y texto sin formato para las descripciones. Sin HTML, sin JSON, sin formatos personalizados.

**¿Cuánto tiempo debe tener llms.txt?**
Una o dos páginas de texto conciso. El tiempo suficiente para cubrir sus ofertas y puntos finales clave. Lo suficientemente breve como para que un agente pueda procesarlo en una sola lectura.

**¿Debería llms.txt incluir información sobre precios?**
Sí, si su precio es público. Incluya precios base, modelo de precios (por asiento, por uso, tarifa plana) y dónde encontrar información detallada sobre precios.

**¿Puedo tener diferentes llms.txt para diferentes subdominios?**
Sí. Cada subdominio debe tener su propio llms.txt que describa las capacidades específicas de ese subdominio.

## Guías relacionadas

* [Protocolos de agente de IA](/es/docs/protocols/)
* [la capa de ejecución](/es/docs/execution-layer/)

## Referencias primarias

* [Guía de Google para funciones de IA generativa](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
* [Conceptos básicos de búsqueda de Google](https://developers.google.com/search/docs/essentials)