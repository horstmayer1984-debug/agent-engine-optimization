---
title: "Relación de rastreo-referencia de IA: cómo medir el valor."
metaTitle: "Relación de rastreo a referencia de IA para AEO."
date: 2026-07-02
weight: 190
category: "Guide"
description: "La relación entre rastreo y referencia de IA muestra si los rastreadores devuelven valor. Aprenda a medir el tráfico del rastreador de IA antes de bloquearlo."
summary: "Una guía de medición de la proporción de rastreo y referencia de IA, valor del rastreador, referencias de IA y decisiones de control de acceso."
keywords:
  - Relación de rastreo y referencia de IA
  - Valor del rastreador de IA
  - Análisis de rastreadores de IA
  - referencias de rastreadores
  - Medición AEO
---
# Relación de rastreo a referencia de IA

La relación de rastreo a referencia de IA compara la frecuencia con la que un rastreador de IA solicita su contenido con la frecuencia con la que ese sistema de IA devuelve a los usuarios. Es una de las métricas AEO más útiles porque convierte el debate sobre los rastreadores de opinión en evidencia.

## Qué significa la métrica

La fórmula es sencilla:

```text
AI crawl-to-referral ratio = AI crawler requests / AI referral visits
```

Si un bot rastrea 10.000 páginas y la superficie de IA relacionada envía 100 visitas, la proporción es 100:1. Si rastrea 10.000 páginas y envía una visita, la proporción es 10.000:1.

El [anuncio de Attribution Business Insights] de Cloudflare (https://blog.cloudflare.com/attribution-business-insights/) dice que ha observado ratios de rastreadores de IA que van desde 118:1 hasta casi 50.000:1 en torno a su análisis del Día de la Independencia del Contenido de 2025. El número exacto de su sitio variará según la industria, el tipo de página, la política de rastreo y la demanda de la marca.

## Por qué es importante para los AEO

Los equipos AEO deben responder tres preguntas:

1. ¿Qué sistemas de IA pueden acceder al sitio?
2. ¿Qué sistemas de IA citan, refieren o actúan en el sitio?
3. ¿Qué sistemas de IA consumen recursos sin devolver valor?

El volumen del rastreador por sí solo no es suficiente. Un rastreador de gran volumen podría generar visibilidad en el futuro. También podría costar ancho de banda y no producir descubrimientos, citas ni conversiones.

Esto se conecta directamente a [Atribución de referencia de IA para AEO SEO](/es/docs/ai-referral-attribution-seo/), [Tráfico web del agente de IA en 2026](/es/docs/ai-agent-web-traffic-2026/) y [Control de rastreo de IA de Cloudflare](/es/docs/cloudflare-ai-crawl-control/).

## Qué medir

| Métrica | Por qué es importante |
|
---|
---|
| Solicitudes de rastreadores de IA | Muestra el uso de recursos y el apetito de rastreo |
| Referencias de IA | Muestra el tráfico directo devuelto desde superficies de IA |
| URL citadas | Muestra qué páginas se utilizan en las respuestas |
| Proporción de rastreo a referencia por bot | Identifica rastreadores de alto y bajo valor |
| Tasa de conversión después de la referencia de IA | Separa el tráfico de curiosidad del valor comercial |
| Solicitudes de IA bloqueadas | Muestra si sus controles ocultan páginas útiles |
| Solicitudes de `/llms.txt` | Muestra intentos de descubrimiento orientados al agente |

## Cómo calcularlo sin Cloudflare

El panel de Cloudflare es útil si el sitio utiliza Cloudflare Bot Management. De lo contrario, aún puedes crear una versión básica:

1. Exporte los registros del servidor de los últimos 30 días.
2. Solicitudes de grupo por agente de usuario de rastreador de IA conocido e IP verificada cuando sea posible.
3. Separe los robots de búsqueda, agentes, capacitación y desconocidos cuando la evidencia lo permita.
4. Extraiga sesiones de referencia de IA de los registros de análisis y del servidor.
5. Haga coincidir cuidadosamente la familia de rastreadores con la familia de referencia. No asuma que cada solicitud "OpenAI" crea cada referencia de ChatGPT.
6. Calcule proporciones por bot, sección y tipo de página.El resultado será imperfecto, pero más útil que adivinar.

## Tabla de decisiones

| Patrón de proporción | Posible interpretación | Acción |
|
---|
---|
---|
| Rastreo bajo, referencia alta | Descubrimiento eficiente | Mantener el acceso abierto y mejorar las páginas citadas |
| Alto rastreo, alta referencia | útil pero costoso | Permitir, monitorear el ancho de banda, optimizar el caché |
| Alto rastreo, baja referencia | Riesgo de extracción | Limitar, restringir o negociar el acceso |
| Sin rastreo, alta referencia | Demanda de marca o citación indirecta | Mejorar la claridad de las fuentes y las páginas de destino |
| Sin rastreo, sin referencias | No visible | Revisar el bloqueo, la calidad del contenido y las señales de entidad |

## Errores comunes

El principal error es tratar las referencias de IA como el único valor. Algunos sistemas de agentes pueden buscar una página, responder una pregunta y no enviar ningún clic. Eso aún puede afectar la preferencia de marca, las visitas directas posteriores o las compras en otros lugares.

El segundo error es considerar malas todas las solicitudes del rastreador. Los sistemas de búsqueda y respuesta necesitan contenido actual. El objetivo no es que la IA no se rastree. El objetivo es una política de rastreadores que coincida con el modelo de negocio.

## Preguntas frecuentes

### ¿Qué es una buena proporción de rastreo y referencia?

No existe un punto de referencia universal. Compare por bot, tipo de página y valor comercial. Un sitio de documentación y un editor de noticias no deberían utilizar el mismo umbral.

### ¿Debería bloquear los rastreadores con proporciones altas?

No inmediatamente. Primero verifique si citan su contenido, envían conversiones asistidas o respaldan una superficie de búsqueda importante.

### ¿Puede Google Analytics medir esto?

Sólo en parte. Muchas solicitudes de rastreadores nunca ejecutan análisis de JavaScript. Utilice registros del servidor o registros CDN.

### ¿Es esto una métrica de seguridad o SEO?

Ambos. Los equipos de SEO lo utilizan para comprender el valor del descubrimiento. Los equipos de seguridad e infraestructura lo utilizan para gestionar el costo y el abuso de los recursos.

## Fuentes

Fuente principal: [Cloudflare Attribution Business Insights](https://blog.cloudflare.com/attribution-business-insights/). Fuente relacionada: [Opciones de tráfico de IA de Cloudflare](https://blog.cloudflare.com/content-independence-day-ai-options/).