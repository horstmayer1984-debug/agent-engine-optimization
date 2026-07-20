---
title: "chamada de ferramenta de smolagents: guia AEO."
metaTitle: "Smolagents Tool Calling: Guia AEO para agentes."
date: 2026-06-28
weight: 179
category: "Guide"
description: "Os smolagents Hugging Face mostram como funcionam os agentes de código e os agentes de chamada de ferramenta. Descubra o que isso significa."
summary: "Um guia prático para smolagents de uma perspectiva AEO, cobrindo CodeAgent, ToolCallingAgent, esquemas, sandboxing e ferramentas de site."
keywords:
  - "chamada de ferramenta de smolagents"
  - "Abraçando rostos smolagents"
  - "CodeAgent vs ToolCallingAgent"
  - "Ferramentas do agente AEO"
  - "Esquemas de ferramentas do agente AI"
---
# chamadas de ferramenta de smolagents

Os smolagentes são importantes para o AEO porque tornam mais fácil ver a diferença entre agentes baseados em código e agentes estruturados de chamada de ferramentas. Sites que apresentam ferramentas, esquemas e caminhos de execução seguros claros serão mais fáceis de usar para qualquer um dos estilos de agente do que sites que dependem de suposições visuais.

## O que são smolagentes?

A documentação do Hugging Face descreve [smolagents](https://huggingface.co/docs/smolagents/index) como uma biblioteca Python de código aberto para criar agentes com abstrações mínimas. Seus documentos destacam dois tipos principais de agentes: `CodeAgent`, que escreve ações como código, e `ToolCallingAgent`, que usa chamadas de ferramentas estruturadas semelhantes a JSON.

O plug-in GitHub também trouxe à tona o ecossistema de agentes Hugging Face, incluindo [huggingface/agents-course](https://github.com/huggingface/agents-course). O plugin Hugging Face mostrou o [First Agent Template Space] (https://hf.co/spaces/agents-course/First_agent_template), que é rotulado em torno de smolagents e ferramentas.

## CodeAgent vs ToolCallingAgent para AEO

| Tipo de agente | Como funciona | Requisito do site |
|
---|
---|
---|
| Agente de código | Gerar código para chamar ferramentas ou calcular | Exemplos claros, sandboxes seguras, resultados determinísticos |
| Agente de chamada de ferramenta | Emitir chamadas estruturadas para ferramentas | Nomes de ferramentas, esquemas JSON, validação, mensagens de erro |
| Agente do navegador | Operar páginas visuais | UI semântica, rótulos, formulários estáveis, estados claros |

Uma estratégia AEO deve apoiar todos os três, quando relevante: documentos para agentes de código, esquemas para chamadores de ferramentas e uma interface de usuário acessível para agentes navegadores.

## O que publicar para ferramentas de chamada de agentes

1. Nomes de ferramentas que descrevem a ação.
2. Insira esquemas com campos obrigatórios.
3. Esquemas de saída com estados de sucesso e erro.
4. Limites de taxas e regras de autenticação.
5. Regras de aprovação humana.
6. Exemplos que correspondem ao comportamento de produção.
7. Notas de lançamento quando as ferramentas mudam.

Para obter orientação em nível de protocolo, consulte [Recursos MCP x Ferramentas x Prompts](/es/docs/mcp-resources-tools-prompts/) e [API MCP x Agente](/es/docs/mcp-vs-api-for-agents/).

## Implicações do site

smolagents não é uma ferramenta de otimização de sites. É um sinal de como pensam os criadores de agentes. Eles não querem páginas vagas. Eles precisam de ações concretas.

| Tipo de página | Lista de agentes aprimorada |
|
---|
---|
| Documentos API | Adicione exemplos de operação, erros e estados de autenticação. |
| Página de preços | Publique os limites do plano em uma tabela de comparação. |
| Página de comércio eletrônico | Exiba variantes, estoque, preço, frete e devoluções. |
| Página de suporte | Encaminhe incidentes por tipo e dados necessários. |

O objetivo prático é a [camada de execução](/es/docs/execution-layer/): os agentes devem passar da leitura de uma página até a conclusão de uma tarefa limitada com validação e recuperação.

## Perguntas frequentes

### Os smolagents são apenas para desenvolvedores? A biblioteca é para desenvolvedores, mas as implicações afetam profissionais de marketing, equipes de produtos e proprietários de documentação porque os agentes precisam de melhores interfaces de site.

### Um site deve expor o código Python aos agentes?

Geralmente não. Os sites públicos devem expor dados, APIs, documentos e ferramentas estáveis. A execução de código pertence a ambientes controlados.

### O que é mais seguro: agentes de código ou chamadas de ferramenta JSON?Chamadas de ferramentas estruturadas normalmente são mais fáceis de validar. Os agentes de código podem ser mais flexíveis, mas exigem um ambiente de teste robusto.

### Como isso se relaciona com o AEO?

O AEO facilita aos agentes a descoberta, interpretação, execução e verificação de conteúdo e ações.

## Fontes

Fontes primárias: [documentação de smolagents](https://huggingface.co/docs/smolagents/index), [referência de agente smolagents](https://huggingface.co/docs/smolagents/reference/agents), [Repositório de cursos de agentes de abraços faciais](https://github.com/huggingface/agents-course) e [Espaço de modelo do primeiro agente](https://hf.co/spaces/agents-course/First_agent_template).