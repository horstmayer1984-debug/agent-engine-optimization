---
title: "Autorización MCP: OAuth para agentes de IA."
metaTitle: "Autorización de MCP para agentes de IA: Guía de OAuth."
date: 2026-05-17
weight: 114
category: "Architecture"
description: "La autorización MCP define cómo los agentes de IA acceden a herramientas restringidas a través de HTTP. Aprenda OAuth, metadatos de recursos protegidos."
summary: "Una guía práctica para la autorización de MCP para agentes de IA, que cubre flujos de OAuth, metadatos de recursos protegidos, registro de clientes, alcances y preparación de OAO."
keywords:
  - Autorización MCP
  - MCP OAuth
  - Autorización del agente de IA
  - metadatos de recursos protegidos
  - control de acceso del agente
---
# Autorización MCP: OAuth para agentes de IA

La autorización de MCP es importante porque las herramientas del agente a menudo necesitan acceso restringido. Las herramientas públicas se pueden descubrir libremente, pero los flujos de trabajo reales necesitan identidad, consentimiento, alcances y pistas de auditoría. La especificación de autorización MCP explica cómo los transportes MCP basados ​​en HTTP pueden utilizar autorización estilo OAuth para servidores MCP restringidos.

## Lo que dice la especificación MCP

La especificación de autorización del Protocolo de contexto modelo define capacidades de autorización en el nivel de transporte para transportes basados en HTTP. La especificación actual hace referencia a OAuth, metadatos de recursos protegidos, registro dinámico de clientes y requisitos de seguridad.

Fuentes primarias:

- [Especificación de autorización MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [Hoja de ruta de MCP 2026](https://modelcontextprotocol.io/development/roadmap)
- [Guía MCP vs API en este sitio](/es/docs/mcp-vs-api-for-agents/)

## Por qué la autorización es una cuestión de AEO

La [capa de ejecución](/es/docs/execution-layer/) no es útil si cada acción es pública o cada acción requiere que un humano copie las credenciales manualmente. Los agentes necesitan acceso controlado.

Ejemplos:

- un agente de adquisiciones verifica el precio del contrato
- un agente de soporte lee el estado del ticket
- un agente de viajes modifica una reserva
- un agente financiero recupera facturas
- un agente desarrollador abre una herramienta de implementación

Cada flujo de trabajo necesita una respuesta clara: ¿para quién actúa el agente, qué puede hacer, cuánto dura el acceso y cómo se puede revocar el acceso?

## MCP público frente a MCP restringido

| Tipo de servidor MCP | Ejemplo | Necesidad de autorización |
|
---|
---|
---|
| Público de sólo lectura | Catálogo de productos, búsqueda de documentos, precios públicos | Generalmente ninguno |
| Acción pública | Suscripción al boletín, solicitud de cotización pública | Controles antiabuso de baja fricción |
| Lectura de ámbito de usuario | Datos de cuenta, estado del pedido | OAuth y consentimiento del usuario |
| Escritura de ámbito de usuario | Reserva, pago, cancelación | Alcances sólidos, confirmación, registros de auditoría |
| Herramienta de administración | Implementación, configuración de facturación | Aprobación humana y política estricta |

La mayoría de las empresas deberían comenzar con acciones públicas de solo lectura o de bajo riesgo antes de exponer herramientas exclusivas del usuario.

## Conceptos clave de autorización

| Concepto | Significado de agentes |
|
---|
---|
| Propietario del recurso | El usuario u organización para la que actúa el agente |
| Cliente MCP | El cliente agente que solicita acceso |
| Servidor de autorización | El sistema que otorga tokens |
| Metadatos de recursos protegidos | Información legible por máquina sobre servidores de autorización |
| Alcance | Permiso específico como leer pedidos o crear reservas |
| Token de acceso | Credencial utilizada para la solicitud de MCP |Estos conceptos no son nuevos, pero los agentes los hacen más importantes porque el actor ya no es siempre un ser humano en un navegador.

## Lista de verificación de implementación

1. Clasificar las herramientas MCP por riesgo.
2. Mantenga las herramientas de descubrimiento públicas separadas de las herramientas restringidas.
3. Definir alcances por acción, no por área amplia de producto.
4. Publicar metadatos de autorización donde los clientes puedan descubrirlos.
5. Utilice tokens de corta duración para acciones de mayor riesgo.
6. Registre la identidad del agente, la identidad del usuario, el nombre de la herramienta, el resumen de entrada y el estado del resultado.
7. Agregue confirmación humana para acciones irreversibles o costosas.

La [guía de observabilidad y barreras de seguridad del agente](/es/docs/agent-observability-guardrails/) amplía esto al monitoreo operativo.

## Ejemplo de diseño de alcance

| Mal alcance | Mejores alcances |
|
---|
---|
| `account_access` | `orders.read`, `orders.cancel`, `invoices.read` |
| `booking` | `availability.read`, `booking.create`, `booking.cancel` |
| `admin` | `users.invite`, `billing.read`, `settings.update` |

Los agentes funcionan mejor cuando los alcances son explícitos. Los equipos de seguridad funcionan mejor cuando los ámbitos se corresponden con acciones comerciales.

## Requisitos de documentación AEO

Si su sitio ofrece herramientas MCP restringidas, su documentación pública debe explicar:

- qué herramientas existen
- qué herramientas son públicas
- que requieren autorización
- qué alcances se solicitan
- si se requiere un paso de confirmación humana
- cómo funcionan los registros y la revocación

Agregue enlaces a esos documentos desde [llms.txt](/es/docs/programming-llms-txt/) para que los agentes puedan descubrir el modelo de acceso antes de intentar llamar a las herramientas.

## Errores comunes

| Error | Por qué falla |
|
---|
---|
| Un token amplio para todas las herramientas | Demasiada agencia y débil auditabilidad |
| No hay documentación de capacidad pública | Los agentes no pueden planificar el acceso |
| Tokens de larga duración para acciones de escritura | Mayor daño si se ve comprometido |
| Sin vía de revocación | Los usuarios no pueden detener el acceso delegado |
| Tratar la identidad del agente como identidad del usuario | Desdibuja la responsabilidad |

## Preguntas frecuentes

### ¿Todos los servidores MCP necesitan OAuth?

No. Es posible que los servidores públicos de solo lectura no necesiten autorización. Las herramientas restringidas o de ámbito de usuario suelen serlo.

### ¿Está lista la autorización de MCP para producción?

La especificación existe y está evolucionando. Los equipos deben seguir la versión actual y verificar la compatibilidad cliente/servidor antes del uso en producción.

### ¿Qué son los metadatos de recursos protegidos?

Son metadatos los que ayudan a los clientes MCP a identificar los servidores de autorización asociados con un recurso protegido.

### ¿Cómo afecta esto al AEO?

Es más probable que los agentes utilicen servicios que describan claramente las herramientas, los permisos y los flujos de acceso disponibles.

### ¿Deberían los agentes tener acceso de administrador?Solo en entornos internos estrictamente controlados con registros, aprobaciones y revocaciones estrictos.