---
title: "Puntos finales del sitio web NLWeb: interfaces legibles."
metaTitle: "Puntos finales del sitio web NLWeb para agentes."
date: 2026-06-28
weight: 173
category: "Architecture"
description: "NLWeb ofrece a los sitios web puntos finales en lenguaje natural para humanos y agentes de IA. Descubra cómo utiliza Schema.org, RSS, MCP y datos del sitio."
summary: "Una introducción práctica a los puntos finales de sitios web de NLWeb, por qué son importantes para los sitios web legibles por agentes y cómo preparar contenido y datos."
keywords:
  - Puntos finales del sitio web NLWeb
  - NLWeb para agentes de IA
  - puntos finales de sitios web legibles por máquina
  - API web en lenguaje natural
  - NL Web MCP
---
# Puntos finales del sitio web NLWeb

NLWeb es un proyecto de Microsoft de código abierto para agregar interfaces de lenguaje natural a sitios web. Es importante para los sitios listos para agentes porque convierte los datos existentes del sitio, como Schema.org y RSS, en puntos finales que pueden servir a humanos y agentes de IA. Es un puente práctico entre el contenido, la búsqueda y las herramientas de estilo MCP.

## ¿Qué es NLWeb?

El [repositorio de Microsoft NLWeb](https://github.com/microsoft/NLWeb) describe NLWeb como una forma de crear interfaces conversacionales para sitios web. Su README dice que soporta MCP de forma nativa, utiliza Schema.org y formatos semiestructurados similares a RSS, y proporciona protocolos abiertos más código de implementación.

Eso hace que NLWeb sea relevante para sitios que quieren que los agentes hagan preguntas estructuradas en lugar de buscar páginas a ciegas.

NLWeb no debe tratarse como una capa mágica de SEO. Se acerca más al patrón de interfaz de un sitio web: una forma de exponer el conocimiento y los registros propios del sitio a través del acceso en lenguaje natural.

## Por qué NLWeb es una nueva oportunidad para palabras clave

La mayoría de los sitios web todavía piensan en tres capas:

1. Páginas HTML para humanos.
2. Mapas de sitio para motores de búsqueda.
3. API para desarrolladores.

NLWeb apunta a una cuarta capa: puntos finales en lenguaje natural para agentes y usuarios asistidos por IA.

| Capa | Usuario principal | Formato típico |
|
---|
---|
---|
| Sitio web | Visitante humano | HTML |
| Mapa del sitio | Rastreador de búsqueda | XML |
| Datos estructurados | Sistemas de búsqueda e inteligencia artificial | Schema.org JSON-LD |
| Punto final NLWeb | Agente humano o de IA que hace una pregunta sobre una tarea | Interfaz en lenguaje natural respaldada por datos del sitio |
| Herramienta MCP | Agente que necesita una acción estructurada | Esquema de herramienta y punto final |

Para conocer la arquitectura relacionada, consulte [Recursos de MCP, herramientas y mensajes](/es/docs/mcp-resources-tools-prompts/) y [MCP frente a API para agentes](/es/docs/mcp-vs-api-for-agents/).

## ¿Qué sitios deberían ver NLWeb primero?

NLWeb es más interesante para sitios con datos ricos y consultables:

1. Catálogos de comercio electrónico.
2. Inventario de viajes.
3. Listados de bienes inmuebles.
4. Bolsas de trabajo.
5. Portales de documentación.
6. Directorios locales.
7. Apoyar las bases de conocimiento.
8. Bases de datos de eventos.

Estos sitios ya contienen hechos estructurados. NLWeb les ofrece un camino hacia la recuperación conversacional y legible por el agente.

## Cómo prepararse para NLWeb

Incluso si aún no implementas NLWeb, prepara la capa de datos:

1. Utilice nombres de entidades coherentes en todas las páginas y datos estructurados.
2. Mantenga el marcado de Schema.org alineado con el contenido visible.
3. Mantenga feeds limpios de productos, artículos, eventos, listados o documentos.
4. Cree URL canónicas estables para cada entidad importante.
5. Frecuencia de actualización de documentos y reglas de disponibilidad.
6. Decidir qué agentes de datos pueden consultar y qué datos requieren autenticación.7. Asigne posibles preguntas a los campos de datos de origen.

Esto se superpone con [Programación de sitios web para agentes de IA](/es/docs/programming-websites-for-ai-agents/) y [Aplicaciones web listas para agentes](/es/docs/agent-ready-web-apps/).

## NLWeb frente a raspado

| Pregunta | Raspado | Punto final estilo NLWeb |
|
---|
---|
---|
| ¿El sitio controla la forma de la respuesta? | Generalmente no | Sí |
| ¿Puede el agente hacer una pregunta específica? | Indirectamente | Sí |
| ¿La salida está vinculada a los datos de origen? | A menudo frágil | Más controlable |
| ¿Es más fácil hacer cumplir la política de acceso? | Más duro | Más fácil si se diseña bien |
| ¿Reemplaza las páginas normales? | No | No |

El beneficio estratégico es el control. Si los agentes van a consultar su sitio de todos modos, un punto final estructurado puede ser más seguro y preciso que obligarlos a pasar por páginas visuales.

## Preguntas frecuentes

### ¿NLWeb es un estándar web oficial?

NLWeb es un proyecto de Microsoft de código abierto con protocolos abiertos y código de implementación. Trátelo como un enfoque emergente, no como un estándar universal establecido.

### ¿NLWeb reemplaza a Schema.org?

No. NLWeb se basa en datos de sitios como Schema.org y formatos similares a RSS. Los buenos datos estructurados siguen siendo importantes.

### ¿NLWeb es lo mismo que MCP?

No. NLWeb puede admitir MCP, pero MCP es un protocolo para herramientas e intercambio de contexto. NLWeb se centra en interfaces de sitios web en lenguaje natural.

### ¿Todos los sitios web deberían implementar NLWeb ahora?

No. Comience con sitios donde los usuarios o agentes necesitan hacer preguntas detalladas sobre datos estructurados del sitio.

## Fuentes

Fuentes primarias y de referencia: [repositorio de Microsoft NLWeb GitHub](https://github.com/microsoft/NLWeb), [fuente sin formato README de NLWeb](https://raw.githubusercontent.com/microsoft/NLWeb/main/README.md), [documentación del protocolo de contexto del modelo](https://modelcontextprotocol.io/docs/getting-started/intro), [Schema.org](https://schema.org/) y [documentación de datos estructurados de Google](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data).