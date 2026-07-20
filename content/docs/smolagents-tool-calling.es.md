---
title: "Llamada de herramientas de smolagents: guía de AEO."
metaTitle: "Smolagents Tool Calling: guía de AEO para agentes."
date: 2026-06-28
weight: 179
category: "Guide"
description: "Los smolagents de Hugging Face muestran cómo funcionan los agentes de código y los agentes de llamada de herramientas. Descubra lo que eso significa."
summary: "Una guía práctica sobre smolagents desde una perspectiva AEO, que cubre CodeAgent, ToolCallingAgent, esquemas, sandboxing y herramientas de sitios web."
keywords:
  - llamada de herramientas smolagents
  - Hugging Face smolagents
  - CodeAgent y ToolCallingAgent
  - herramientas de agente AEO
  - Esquemas de herramientas de agentes de IA
---
# Llamadas de herramientas de smolagents

Los smolagents son importantes para AEO porque hacen que sea fácil ver la diferencia entre agentes basados en código y agentes estructurados de llamada de herramientas. Los sitios web que exponen herramientas claras, esquemas y rutas de ejecución seguras serán más fáciles de usar para cualquiera de los estilos de agente que los sitios que dependen de conjeturas visuales.

## ¿Qué son los smolagentes?

La documentación de Hugging Face describe [smolagents](https://huggingface.co/docs/smolagents/index) como una biblioteca Python de código abierto para crear agentes con abstracciones mínimas. Sus documentos destacan dos tipos de agentes principales: `CodeAgent`, que escribe acciones como código, y `ToolCallingAgent`, que utiliza llamadas de herramientas estructuradas tipo JSON.

El complemento de GitHub también hizo emerger el ecosistema de agentes de Hugging Face, incluido [huggingface/agents-course](https://github.com/huggingface/agents-course). El complemento Hugging Face mostró el [Espacio de plantilla de primer agente] (https://hf.co/spaces/agents-course/First_agent_template), que está etiquetado alrededor de smolagents y herramientas.

## CodeAgent frente a ToolCallingAgent para AEO

| Tipo de agente | Cómo actúa | Requisito del sitio web |
|
---|
---|
---|
| Agente de código | Genera código para llamar a herramientas o calcular | Ejemplos claros, entornos sandbox seguros, resultados deterministas |
| Agente de llamada de herramientas | Emite llamadas estructuradas a herramientas | Nombres de herramientas, esquemas JSON, validación, mensajes de error |
| Agente del navegador | Opera páginas visuales | UI semántica, etiquetas, formas estables, estados claros |

Una estrategia AEO debe admitir los tres cuando sea relevante: documentos para agentes de código, esquemas para llamadores de herramientas y una interfaz de usuario accesible para agentes de navegador.

## Qué publicar para los agentes que llaman a herramientas

1. Nombres de herramientas que describen la acción.
2. Ingrese esquemas con campos obligatorios.
3. Esquemas de salida con estados de éxito y error.
4. Límites de tarifas y reglas de autenticación.
5. Reglas de aprobación humana.
6. Ejemplos que coinciden con el comportamiento de producción.
7. Notas de versión cuando cambian las herramientas.

Para obtener orientación a nivel de protocolo, consulte [Recursos de MCP frente a herramientas frente a indicaciones](/es/docs/mcp-resources-tools-prompts/) y [MCP frente a API para agentes](/es/docs/mcp-vs-api-for-agents/).

## Implicaciones del sitio web

smolagents no es una herramienta de optimización de sitios web. Es una señal sobre cómo piensan los creadores de agentes. No quieren páginas vagas. Necesitan acciones concretas.

| Tipo de página | Mejora lista para el agente |
|
---|
---|
| Documentos API | Agregue ejemplos de operación, errores y estados de autenticación. |
| Página de precios | Publicar los límites del plan en una tabla comparativa. |
| Página de comercio electrónico | Exponer variantes, inventario, precio, envío y devoluciones. |
| Página de soporte | Enrutar incidencias por tipo y datos requeridos. |

El objetivo práctico es la [capa de ejecución](/es/docs/execution-layer/): los agentes deben pasar de leer una página a completar una tarea limitada con validación y recuperación.

## Preguntas frecuentes

### ¿Los smolagents son solo para desarrolladores?La biblioteca es para desarrolladores, pero las implicaciones afectan a los especialistas en marketing, equipos de productos y propietarios de documentación porque los agentes necesitan mejores interfaces de sitios web.

### ¿Debería un sitio web exponer el código Python para los agentes?

Generalmente no. Los sitios web públicos deben exponer datos, API, documentos y herramientas estables. La ejecución de código pertenece a entornos controlados.

### ¿Qué es más seguro: agentes de código o llamadas a herramientas JSON?

Las llamadas a herramientas estructuradas suelen ser más fáciles de validar. Los agentes de código pueden ser más flexibles, pero requieren un entorno de pruebas sólido.

### ¿Cómo se relaciona esto con el AEO?

AEO facilita que los agentes descubran, interpreten, ejecuten y verifiquen el contenido y las acciones.

## Fuentes

Fuentes principales: [documentación de smolagents](https://huggingface.co/docs/smolagents/index), [referencia de agentes smolagents](https://huggingface.co/docs/smolagents/reference/agents), [repositorio de cursos de agentes de Hugging Face](https://github.com/huggingface/agents-course) y [First Agent Template Space](https://hf.co/spaces/agents-course/First_agent_template).
