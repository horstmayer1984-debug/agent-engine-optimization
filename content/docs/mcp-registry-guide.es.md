---
title: "Registro MCP: cómo funciona el descubrimiento de servidores."
date: 2026-05-17
weight: 136
category: "Architecture"
description: "Conozca qué es el Registro MCP oficial, cómo funcionan los metadatos del servidor y por qué la preparación del registro es importante para las herramientas."
summary: "Una guía práctica de Registro MCP que cubre el estado de la vista previa, los metadatos del servidor, los campos de descubrimiento y cómo encaja en la infraestructura lista para agentes."
keywords:
  - Registro MCP
  - Registro de protocolo de contexto modelo
  - Descubrimiento del servidor MCP
  - servidor.json
  - descubrimiento de herramientas de agente
---
# Registro MCP: cómo funciona el descubrimiento de servidores

El Registro MCP es el depósito de metadatos centralizado oficial para servidores MCP de acceso público. Su propósito es simple: hacer que el descubrimiento de servidores sea más consistente brindando a los creadores un lugar para publicar metadatos estandarizados y brindando a los clientes una forma estructurada de encontrar servidores disponibles. Para AEO, es un recordatorio de que el descubrimiento se produce cada vez más a través de registros legibles por máquinas, no sólo a través de páginas web.

## Lo que dicen los documentos oficiales

La documentación de MCP describe el Registro como un servicio de vista previa respaldado por contribuyentes confiables al ecosistema. Almacena metadatos estandarizados, como nombres de servidores, instrucciones de ejecución, descripciones y capacidades.

Fuentes primarias:

- [Documentación oficial del Registro MCP](https://modelcontextprotocol.io/registry/about)
- [Registro oficial de MCP](https://registry.modelcontextprotocol.io/)

## Por qué son importantes los registros

| Sin registro | Con registro |
|
---|
---|
| El descubrimiento depende de documentos dispersos | Discovery puede utilizar metadatos estructurados |
| Los pasos de instalación varían enormemente | Las instrucciones de instalación se vuelven explícitas |
| La evaluación de capacidades es lenta | Los clientes pueden inspeccionar los metadatos primero |
| Las señales de confianza están fragmentadas | Las reglas de publicación y espacio de nombres mejoran la coherencia |

El Registro no reemplaza su sitio de documentación. Lo complementa. Una página explica por qué es importante una herramienta; Los metadatos del registro ayudan al cliente a encontrarlos y configurarlos.

## Campos de metadatos clave

Los documentos oficiales describen metadatos de servidor estandarizados, que incluyen:

- nombre de servidor único
- descripción
- capacidades
- instrucciones de ejecución
- información de instalación y configuración
- gestión del espacio de nombres

Para AEO, la lección es más amplia: si una máquina debe decidir si su servicio es utilizable, la información no puede vivir sólo en textos de marketing.

## Registro frente a llms.txt frente a tarjetas de agente

| Artefacto | Lo mejor para |
|
---|
---|
| Entrada de registro MCP | Descubriendo servidores MCP públicos |
| `llms.txt` | Descubrimiento de contenido curado a nivel de sitio |
| Tarjeta de agente | Declarar las capacidades de un agente para la interacción entre pares |
| Esquema OpenAPI o MCP | Describiendo operaciones invocables |

La [guía llms.txt](/es/docs/programming-llms-txt/), la [guía de tarjetas de agente](/es/docs/agent-cards-a2a-protocol/) y la [guía MCP vs API](/es/docs/mcp-vs-api-for-agents/) cubren las capas vecinas.

## ¿Qué deberían preparar los editores de servidores?

Antes de publicar en un registro:

1. escribe una descripción clara
2. definir las capacidades con precisión
Tercero, autenticación de documentos y variables de entorno.
4. proporcione instrucciones de instalación segura
5. mantener las versiones actualizadas
6. enlace a documentos canónicos
7. exponer suficientes metadatos para su evaluación sin exagerarLos metadatos vagos no son una ventaja de descubrimiento. Es una señal de exclusión.

## Vista previa del estado y riesgo

Los documentos de MCP indican que el Registro está en versión preliminar y puede cambiar antes de la disponibilidad general. Eso significa que los equipos deben usarlo, aprender de él y evitar suposiciones codificadas que sería costoso deshacer más adelante.

La [guía de autorización de MCP](/es/docs/mcp-authorization-oauth-ai-agents/) también es importante aquí: el descubrimiento nunca debe superar el control de acceso.

## Preguntas frecuentes

### ¿Está listo el Registro MCP para producción?

Los documentos oficiales actualmente lo describen como vista previa, con posibles cambios importantes o restablecimientos antes de la disponibilidad general.

### ¿Listar un servidor garantiza la calidad?

No. Los metadatos mejoran el descubrimiento, pero los consumidores aún necesitan evaluar la idoneidad y la seguridad.

### ¿El registro es lo mismo que un mercado?

No exactamente. Los documentos oficiales lo enmarcan como un repositorio de metadatos centralizado que los mercados posteriores pueden consumir.

### ¿Por qué esto es importante para los AEO?

Porque el descubrimiento de máquinas está pasando del análisis de páginas a registros explícitos, manifiestos y metadatos de capacidades.

## Conclusión

El Registro MCP es importante menos porque cada servidor debe estar allí hoy y más porque muestra hacia dónde se dirige el descubrimiento de agentes: desde una interpretación web confusa hacia inventarios explícitos legibles por máquina.