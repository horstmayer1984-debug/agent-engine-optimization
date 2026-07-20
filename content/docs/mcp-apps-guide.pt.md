---
title: "Aplicativos MCP: Interfaces interativas para fluxos de trabalho."
date: 2026-05-17
weight: 135
category: "Architecture"
description: "Descubra o que são aplicativos MCP, como os componentes interativos da interface do usuário funcionam nos hosts MCP e quando são os sites."
summary: "Um guia prático para aplicativos MCP que abrange interface de usuário on-line, renderização segura, casos de uso e como a extensão altera o design do produto orientado ao agente."
keywords:
  - "Aplicativos MCP"
  - "Interface de usuário MCP"
  - "interfaces de agente interativas"
  - "Aplicativos de protocolo de contexto de modelo"
  - "IU de fluxos de trabalho do agente"
---
# Aplicativos MCP: interfaces interativas para fluxos de trabalho de agentes

Os aplicativos MCP são uma extensão oficial do Model Context Protocol que permite que as ferramentas retornem interfaces de usuário interativas, não apenas texto ou dados estruturados. Isso é importante porque alguns fluxos de trabalho de agentes exigem gráficos, formulários de aprovação, painéis ou controles de várias etapas na própria conversa. Os aplicativos MCP mantêm o fluxo de trabalho contextualizado e, ao mesmo tempo, fornecem aos usuários uma interface mais rica quando o texto simples não é suficiente.

## O que dizem os documentos oficiais do MCP

O projeto MCP anunciou MCP Apps como sua primeira extensão oficial em janeiro de 2026. Os documentos oficiais descrevem interfaces HTML interativas renderizadas em hosts MCP, com sandbox e uma ponte de comunicação segura entre o aplicativo e o host.

Fontes primárias:

- [Blog MCP: Anúncio ao vivo dos aplicativos MCP](https://blog.modelcontextprotocol.io/posts/2026-01-26-mcp-apps/)
- [Visão geral dos aplicativos MCP](https://modelcontextprotocol.io/extensions/apps/overview)
- [Visão geral das extensões MCP](https://modelcontextprotocol.io/extensions)

## Por que existem aplicativos MCP

O texto é suficiente para muitas respostas de ferramentas:

- um resultado de pesquisa
- um estado
- uma recomendação simples

Mas o texto fica desajeitado para:

- gráficos
- comparações visuais
- fluxos de trabalho de aprovação
- telas de design
- formulários com vários campos dependentes
- painéis com status ao vivo

Os aplicativos MCP adicionam uma camada de interface de usuário sem forçar os usuários a deixar a experiência do host.

## Aplicativos MCP versus aplicativos da Web regulares

| Pergunta | Aplicativo web independente | Aplicação MCP |
|
---|
---|
---|
| Onde é renderizado? | Site ou aba separada | Dentro do host MCP |
| O contexto da conversa é preservado? | Geralmente não | Sim |
| O melhor para | Produtos completos | Trechos de fluxo de trabalho e interface de usuário vinculada a ferramentas |
| Comunicação | API do aplicativo do navegador | MCP mais ponte de aplicação |
| Jornada do usuário | Mudança de contexto | Continuação on-line |

Os aplicativos MCP não substituem todos os aplicativos da web. Eles são úteis quando a interface faz parte de uma tarefa mediada por um agente, e não do produto inteiro.

## Implicações do AEO

A [camada de execução](/es/docs/execution-layer/) geralmente precisa de um ponto de verificação humano. Os aplicativos MCP podem tornar esse ponto de verificação prático:

- aprovar um reembolso
- inspecionar uma cotação
- escolha entre as opções
- revisar um gráfico
- confirmar uma ação arriscada

Isso se conecta naturalmente à [experiência do usuário do agente e design humano no circuito] (/es/docs/agent-ux-human-in-the-loop/), onde a questão não é "humano ou agente", mas "quais partes precisam de qual interface?"

## Quando usar aplicativos MCP

Use-os quando:

- o resultado de uma ferramenta precisa de interpretação visual
- o próximo passo requer contribuição humana estruturada
- você deseja preservar o contexto conversacional
- a interface do usuário está subordinada a um fluxo de trabalho de ferramenta

Não os use quando:

- uma simples resposta de texto é suficiente
- a experiência precisa de um produto completo e independente
- o ecossistema de hospedagem direcionado ainda não suporta a extensão## Segurança e implantação

Documentos oficiais descrevem a renderização em sandbox e uma ponte de mensagens segura. Isso significa que as equipes ainda precisam pensar cuidadosamente sobre:

- quais dados entram na interface do usuário
- qual ferramenta pode acionar a chamada da IU
- se a aprovação for necessária
- como o status é registrado
- como o suporte do anfitrião variaO [guia de autorização MCP](/es/docs/mcp-authorization-oauth-ai-agents/) ainda é relevante porque a interface de usuário avançada não elimina a necessidade de permissões estritas.

## Perguntas frequentes

### Os aplicativos MCP fazem parte do MCP principal?

Eles são uma extensão oficial, não o protocolo principal em si.

### Os aplicativos MCP substituem um site?

Não. Eles são melhores para UI de fluxo de trabalho on-line e não para substituir todas as experiências públicas da Web.

### Quais clientes apoiam você?

O suporte do anfitrião varia. Os documentos do MCP mantêm uma matriz de suporte ao cliente para extensões oficiais.

### Qual é o melhor primeiro caso de uso?

Fluxos de aprovação e pequenos painéis são pontos de partida sólidos porque exigem mais do que texto, mas menos do que uma interface de usuário completa do produto.

## Conclusão

Os aplicativos MCP são importantes porque os fluxos de trabalho dos agentes ainda precisam de momentos de julgamento humano. Eles trazem fragmentos úteis da interface para o mesmo local onde o agente já está trabalhando.