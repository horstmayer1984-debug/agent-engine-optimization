---
title: "Guía de auditoría de navegación de Lighthouse Agentic."
metaTitle: "Auditoría de navegación de Lighthouse Agentic: Guía AEO."
date: 2026-05-17
weight: 110
category: "Guide"
description: "Chrome Lighthouse ahora incluye comprobaciones experimentales de navegación con agentes. Descubra lo que significan llms.txt, WebMCP y las auditorías."
summary: "Una guía práctica para las auditorías de navegación agente de Chrome Lighthouse, que incluye comprobaciones de llms.txt, visibilidad de la herramienta WebMCP, puntuación y próximos pasos de AEO."
keywords:
  - Navegación agente del faro
  - auditoría llms.txt
  - Auditoría WebMCP
  - SEO de navegación agente
  - auditoría AEO
---
# Guía de auditoría de navegación de Lighthouse Agentic

La categoría de navegación agente de Chrome Lighthouse es importante porque incorpora comprobaciones de preparación de los agentes a un flujo de trabajo de auditoría de desarrolladores convencional. Las comprobaciones actuales son experimentales, pero indican hacia dónde se dirige la web: los agentes de IA necesitan resúmenes legibles por máquinas, herramientas detectables y superficies de interacción deterministas.

## ¿Qué cambió?

Chrome para desarrolladores ahora documenta las auditorías de Lighthouse para la navegación agente. Las comprobaciones documentadas incluyen una auditoría `llms.txt` y una auditoría informativa para las herramientas WebMCP registradas. Chrome dice que la categoría es experimental y se basa en estándares propuestos, por lo que debe tratarse como una capa de diagnóstico temprano en lugar de una puntuación final.

Fuentes primarias:

- [Chrome: auditoría de Lighthouse llms.txt](https://developer.chrome.com/docs/lighthouse/agentic-browsing/llms-txt)
- [Chrome: puntuación de navegación agente de Lighthouse](https://developer.chrome.com/docs/lighthouse/agentic-browsing/scoring)
- [Chrome: auditoría de herramientas WebMCP registradas](https://developer.chrome.com/docs/lighthouse/agentic-browsing/registered-webmcp-tools)

## Lo que comprueban las auditorías

| Auditoría | Lo que significa | Respuesta práctica AEO |
|
---|
---|
---|
| llms.txt | Comprueba si la raíz del sitio proporciona un resumen legible por máquina | Publique un `llms.txt` conciso con enlaces clave |
| Herramientas WebMCP registradas | Enumera las herramientas que la página expone a los agentes del navegador | Agregue nombres claros de herramientas y descripciones de acciones |
| Categoría de navegación agente | Muestra señales de aprobación/rechazo y preparación informativa | Úselo como una lista de verificación técnica, no como una puntuación de clasificación |

La documentación `llms.txt` de Chrome hace una distinción importante: un archivo faltante se puede marcar como No aplicable porque el archivo es opcional, pero los errores del servidor se marcan. Eso significa que un `llms.txt` roto es peor que ningún archivo.

## Por qué esto es importante para los AEO

La [auditoría de preparación de AEO](/es/docs/audit/) ya verifica el descubrimiento, la capa de lectura, la capa de ejecución y la confianza. Lighthouse agrega una forma sencilla para los desarrolladores de captar algunas de esas señales dentro de un entorno de herramientas familiar.

No reemplaza una auditoría AEO completa. Ayuda a los desarrolladores a validar piezas técnicas específicas:

- ¿La raíz del sitio sirve `llms.txt` de forma limpia?
- ¿Las acciones de la página son visibles como herramientas WebMCP?
- ¿Las señales experimentales de preparación del agente son visibles durante las pruebas del navegador?

## Cómo preparar llms.txt

Para la navegación agente, `llms.txt` debería ser breve y útil. No es un clon del mapa del sitio.

Un expediente práctico debe incluir:

- propósito del sitio
- conceptos básicos
- mejores páginas de inicio
- herramientas o servicios clave
- recursos legibles por máquina
- fecha de actualización

La [guía llms.txt](/es/docs/programming-llms-txt/) explica cómo estructurarlo. La regla principal es simple: ayudar al agente a comprender qué leer primero.

## Cómo preparar herramientas WebMCPLa auditoría de herramientas WebMCP registradas es informativa. Si no hay herramientas registradas, la lista está vacía. Esto no es automáticamente una falla, pero revela si la página expone acciones de una manera amigable para el agente del navegador.

Las primeras buenas herramientas incluyen:

- solicitar auditoría
- reservar cita
- solicitar cotización
- añadir al carrito
- consultar disponibilidad
- enviar ticket de soporte
- comparar productos

La [guía WebMCP](/es/docs/webmcp-agent-ready-websites/) cubre cuándo usar herramientas a nivel de página versus MCP del lado del servidor.

## Flujo de trabajo sugerido

| Paso | Acción | Salida |
|
---|
---|
---|
| 1 | Ejecute Lighthouse en la página de inicio y en plantillas importantes | Señales de navegación agentes de referencia |
| 2 | Solucionar errores de respuesta `llms.txt` | Resumen raíz estable legible por máquina |
| 3 | Agregue WebMCP a una página de acción de bajo riesgo | Herramienta registrada visible |
| 4 | Repetir Faro | Confirmar detección |
| 5 | Agregar registros del lado del servidor para las acciones de los agentes | Capa de medición |

Este flujo de trabajo conecta la validación técnica a la [capa de ejecución](/es/docs/execution-layer/). Pasar una auditoría es menos importante que demostrar que un agente puede completar una tarea útil.

## Qué no hacer

No agregue un archivo `llms.txt` falso solo para pasar una verificación. No registre herramientas WebMCP genéricas como `submit_form` sin una descripción significativa. No exponer acciones de alto riesgo porque la auditoría existe.

La mejor implementación de navegación agente es aburrida: contenido claro, acciones estables, permisos explícitos y buenos registros.

## Preguntas frecuentes

### ¿La puntuación de navegación agente de Lighthouse es un factor de clasificación?

Ninguna fuente oficial dice eso. Trátelo como una señal de preparación experimental, no como un factor de clasificación de Google.

### ¿Se requiere llms.txt?

La documentación de Chrome dice que es opcional por el momento. Un archivo faltante puede ser No aplicable, mientras que los errores del servidor se pueden marcar.

### ¿Debo agregar WebMCP a cada formulario?

No. Comience con acciones de alto valor y bajo riesgo en las que la ejecución del agente ayudaría a los usuarios.

### ¿En qué se diferencia esto de una auditoría SEO normal?

Las auditorías de SEO tradicionales se centran en la capacidad de rastreo, la velocidad, los metadatos y el contenido. Las auditorías de navegación de agentes se centran en si los agentes pueden comprender y actuar en el sitio.

### ¿Qué se debe medir después de la implementación?

Realice un seguimiento de las acciones activadas por los agentes, la finalización de formularios, los errores, las solicitudes no válidas y las páginas que los agentes leen antes de actuar.