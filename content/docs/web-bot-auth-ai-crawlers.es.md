---
title: "Autenticación de bots web para rastreadores de IA: una guía."
date: 2026-05-23
weight: 131
category: "Architecture"
description: "Web Bot Auth utiliza firmas HTTP criptográficas para verificar bots y agentes automatizados. Descubra cómo se adapta a la confianza de los rastreadores."
summary: "Una guía práctica sobre Web Bot Auth para rastreadores de IA, agentes firmados, verificación de rastreadores y diseño de políticas para sitios web legibles por agentes."
keywords:
  - Autenticación de bots web
  - Verificación del rastreador de IA
  - agentes firmados
  - Firmas de mensajes HTTP
  - identidad del rastreador
---
# Autenticación de bots web para rastreadores de IA: una guía práctica de AEO

Web Bot Auth es una forma para que los rastreadores y agentes automatizados demuestren su identidad con firmas HTTP criptográficas. Para AEO, es importante porque la identidad del rastreador se está convirtiendo en una capa de confianza: los propietarios de sitios deben distinguir el tráfico de búsqueda, respuesta y agente útil de la suplantación, el raspado y el abuso.

## ¿Qué es la autenticación de Web Bot?

La [documentación de autenticación de Web Bot] (https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/) de Cloudflare lo describe como un método de autenticación que utiliza firmas criptográficas en mensajes HTTP para verificar que una solicitud proviene de un bot automatizado. Cloudflare lo utiliza para bots verificados y agentes firmados, basándose en borradores activos del IETF para el directorio de claves públicas y el comportamiento de firma de solicitudes.

En términos sencillos: un rastreador publica una clave pública, firma solicitudes con su clave privada y la infraestructura receptora puede verificar si la solicitud realmente proviene de ese rastreador.

Este es un problema diferente del [robots.txt para rastreadores de IA](/es/docs/ai-crawlers-robots-txt/). Robots.txt dice lo que debe hacer un rastreador. Web Bot Auth ayuda a demostrar quién es el rastreador.

## Por qué la identidad del rastreador es ahora importante

La búsqueda por IA y los agentes autónomos crean una mezcla de tráfico confusa:

- rastreadores de búsqueda clásicos
- Rastreadores de respuestas de IA
- entrenamiento de rastreadores
- agentes del navegador que actúan para los usuarios
- sistemas de raspado comerciales
- bots falsos que utilizan cadenas de usuario-agente confiables
- escáneres y monitores de seguridad

Si todos ellos se parecen, el propietario de un sitio sólo tiene opciones contundentes: permitir demasiado o bloquear demasiado. AEO necesita una capa intermedia donde los agentes confiables puedan acceder al contenido público y el tráfico no confiable pueda ser desafiado o limitado.

## Web Bot Auth frente a métodos de verificación comunes

| Método | Lo que prueba | Fuerza | Debilidad |
|
---|
---|
---|
---|
| Cadena de agente de usuario | Lo que afirma el solicitante | Fácil de leer | Fácil de falsificar |
| DNS inverso | Si la IP pertenece a un proveedor conocido | Maduro para los principales rastreadores | Rangos de IP y cambio de infraestructura |
| Lista de IP permitidas | La solicitud proviene de direcciones permitidas | Sencillo para parejas estables | Frágil y difícil de escalar |
| Autenticación de bots web | La solicitud está firmada por una clave registrada | Prueba de identidad más sólida | Requiere adopción de rastreadores e implementación correcta |
| Token de inicio de sesión/API | Acceso autorizado a la cuenta | Fuerte para los sistemas privados | No apto para gatear en público solo |

El futuro probable no es que un método reemplace a todos los demás. Es una verificación en capas.

## Cómo funciona el flujo

A alto nivel:

1. El rastreador genera una clave de firma.
2. El rastreador aloja un directorio clave en una ubicación conocida.3. El rastreador registra el bot y el directorio de claves con el proveedor de verificación.
4. Después de la verificación, el rastreador firma las solicitudes.
5. El sistema receptor valida la firma y aplica la política.

La documentación de Cloudflare incluye requisitos específicos como claves Ed25519, un directorio de claves, HTTPS y encabezados HTTP firmados.

## Implicaciones de la política AEO

Web Bot Auth ayuda a responder una pregunta práctica: "¿Debería esta solicitud de máquina ser lo suficientemente confiable como para acceder a nuestras superficies públicas legibles por agentes?"

Para un sitio preparado para AEO, eso puede influir en:

- si los rastreadores de IA pueden acceder a la documentación
- si el tráfico de agentes puede leer guías públicas
- si se limita la velocidad del scraping de gran volumen
- si los documentos API son visibles pero los puntos finales de ejecución requieren autenticación
- si los agentes firmados reciben un trato diferente al de los bots anónimos

Esto se conecta directamente a la [capa de ejecución](/es/docs/execution-layer/) y a las [barandillas de observabilidad del agente](/es/docs/agent-observability-guardrails/).

## Diseño de acceso recomendado

| Superficie del sitio | Política de acceso sugerida |
|
---|
---|
| Guías públicos | Permitir rastreadores acreditados; controlar el volumen |
| llms.txt y mapa del sitio | Mantener accesible |
| Documentos de referencia de API | Permitir el descubrimiento; proteger credenciales y ejecución |
| Precios y páginas de productos | Permitir búsqueda y recuperación de respuestas |
| Pagar, cuenta, administrador | Autenticar y limitar la tasa |
| Datos exclusivos para socios | Requerir autenticación firmada o tokens de cuenta |

El objetivo es hacer que la web pública sea útil para los agentes sin convertir los sistemas privados en herramientas abiertas.

## Lista de verificación de implementación

1. Bots de inventario que actualmente están llegando al sitio.
2. Separe el tráfico de búsqueda, inteligencia artificial, capacitación, monitoreo y raspado.
3. Mantenga accesibles [llms.txt](/es/docs/llms-txt-vs-robots-txt/) y los documentos públicos.
4. Agregue reglas de bot que no bloqueen por accidente el robot de Google, Bingbot y otros sistemas de descubrimiento conocidos.
5. Utilice Web Bot Auth o una verificación similar cuando sea compatible.
6. Registre el estado de verificación junto con la URL, el código de estado y la acción de límite de velocidad.
7. Revise las reglas después de cada cambio de CDN, firewall o migración de sitio.

## Preguntas frecuentes

### ¿La autenticación de Web Bot es solo para Cloudflare?

Cloudflare documenta su implementación, pero la idea se basa en borradores más amplios de firmas de mensajes HTTP y directorios de claves. La adopción depende del soporte de infraestructura y rastreadores.

### ¿Web Bot Auth les dice a los rastreadores para qué pueden usar el contenido?

No. Verifica la identidad. Las preferencias de uso aún necesitan capas de políticas como robots.txt, señales de contenido, contratos o reglas de acceso.

### ¿Puede Web Bot Auth reemplazar la verificación DNS inversa?

No inmediatamente. Muchos sitios utilizarán ambos, especialmente cuando la adopción de rastreadores firmados es desigual.### ¿Por qué esto es importante para los agentes de IA?

Los agentes realizarán cada vez más solicitudes web en nombre de usuarios o sistemas. La identidad firmada facilita la aplicación de diferentes reglas a agentes confiables, rastreadores anónimos y automatización abusiva.

## Conclusión

Web Bot Auth es una primitiva de confianza del rastreador. No resolverá las licencias de contenido ni la visibilidad de la IA por sí solo, pero brinda a los equipos AEO una mejor base para decidir qué tráfico de máquinas merece acceso.