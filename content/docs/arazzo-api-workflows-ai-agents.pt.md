---
title: "Fluxos de trabalho da API Arazzo para agentes de IA."
metaTitle: "Fluxos de trabalho da API Arazzo para agentes de IA: guia."
date: 2026-05-17
weight: 115
category: "Architecture"
description: "Arazzo define fluxos de trabalho de API legíveis por máquina com base no OpenAPI. Descubra por que isso é importante para os agentes de IA, MCP e SEO na camada."
summary: "Um guia prático da Arazzo para agentes de IA, explicando descrições de fluxo de trabalho, sequenciamento OpenAPI, critérios de sucesso e padrões de implantação AEO."
keywords:
  - "Especificação Arazzo"
  - "Fluxos de trabalho de API para agentes de IA"
  - "OpenAPI Arazzo"
  - "APIs prontas para agente"
  - "Camada de execução SEO"
---
# Fluxos de trabalho da API Arazzo para agentes de IA

Arazzo é importante para o AEO porque o OpenAPI descreve operações individuais da API, mas os agentes geralmente precisam de fluxos de trabalho. Uma tarefa de reserva, cotação, pagamento ou integração pode exigir várias chamadas de API na ordem correta. Arazzo oferece às equipes uma maneira legível por máquina para descrever essas sequências.

## O que é Arazzo

A Iniciativa OpenAPI descreve Arazzo como uma especificação para expressar sequências de chamadas de API e suas dependências para alcançar um resultado. Ele complementa o OpenAPI em vez de substituí-lo.

Fontes primárias:

- [Iniciativa OpenAPI: Especificação Arazzo](https://www.openapis.org/arazzo-specification)
- [Especificação Arazzo] (https://spec.openapis.org/arazzo/latest.html)
- [Especificação OpenAPI](https://spec.openapis.org/oas/v3.1.0.html)

##Por que o OpenAPI por si só não é suficiente

OpenAPI é ótimo para descrever endpoints. Ele informa ao desenvolvedor ou à máquina quais operações existem, quais parâmetros elas aceitam e quais respostas retornam.

Mas muitas tarefas reais precisam de ordem:

1. Pesquise os serviços disponíveis.
2. Selecione um serviço.
3. Verifique as vagas disponíveis.
4. Crie uma reserva.
5. Confirme a reserva.

Se um agente vir apenas terminais individuais, ele deverá inferir a sequência. Isso pode funcionar para APIs simples, mas torna-se frágil quando dependências, tokens, estados ou regras de validação estão envolvidos.

## OpenAPI x Arazzo x MCP

| Camada | Trabalho principal | Benefício de agente |
|
---|
---|
---|
| API aberta | Descreve operações de API | Compreendendo os endpoints disponíveis |
| Arazzo | Descreve fluxos de trabalho entre operações | Entenda como concluir uma tarefa |
| PCM | Expõe ferramentas e recursos que podem ser chamados | Invocar ações por meio de uma interface de agente |

O [guia MCP vs API](/es/docs/mcp-vs-api-for-agents/) explica a camada de ferramentas. Arazzo ajuda a documentar a lógica do fluxo de trabalho por trás dessas ferramentas.

## Onde Arazzo se encaixa no AEO

O AEO é mais forte quando os agentes podem passar por esta sequência:

1. Conheça o serviço.
2. Compreenda as capacidades.
3. Leia as restrições.
4. Execute o fluxo de trabalho.
5. Verifique o resultado.

Arazzo oferece suporte às etapas 2 a 5, tornando explícitos os fluxos de trabalho de várias etapas. É especialmente útil para a [camada de execução](/es/docs/execution-layer/), onde um agente precisa fazer mais do que buscar conteúdo.

## Casos de uso fortes

| Caso de uso | Por que Arazzo ajuda |
|
---|
---|
| Pagamento de comércio eletrônico | Carrinho, frete, imposto, pagamento e confirmação acontecem em sequência |
| Solicitação de orçamento B2B | Elegibilidade, configuração, preço e envio dependem uns dos outros |
| Reserva de viagens | Disponibilidade, regras tarifárias, dados do passageiro e confirmação são solicitados |
| Integração SaaS | As configurações de espaço de trabalho, usuário, cobrança e permissões têm dependências || Escalada de Apoio | Precisa de status para criação, classificação, anexação e roteamento de tickets |
| Fluxo de Trabalho Financeiro | A divulgação, a elegibilidade e o consentimento devem ocorrer antes de serem tomadas medidas |

A [Lista de verificação de aplicativos da Web prontos para agente](/es/docs/agent-ready-web-apps/) aborda como projetar a superfície subjacente do produto.

## O que incluir em um fluxo de trabalho Arazzo

No mínimo, documente:

- objetivo do fluxo de trabalho
- ingressos necessários
- etapas ordenadas
- Operações de origem OpenAPI
- dependências entre etapas
- critérios de sucesso
- partidas
- estados de erro
- expectativas de nova tentativa e idempotência

Os critérios de sucesso são especialmente importantes. Os agentes precisam saber o que significa “pronto”.## Exemplo de formulário de fluxo de trabalho

Para uma API de reserva de compromissos:

| Etapa | Operação | Saída usada posteriormente |
|
---|
---|
---|
| 1 | `lista_serviços` | `ID_serviço` |
| 2 | `lista_disponíveis_slots` | `slot_id` |
| 3 | `criar_reserva` | `id_reserva` |
| 4 | `get_booking` | estado confirmado |

Sem a documentação do fluxo de trabalho, um agente pode ligar primeiro para o endpoint errado ou perder a etapa de confirmação.

## Caminho de implantação

1. Limpe seu documento OpenAPI.
2. Escolha três fluxos de trabalho de alto valor.
3. Escreva descrições Arazzo para esses fluxos de trabalho.
4. Teste-os com um agente ou executor de fluxo de trabalho.
5. Vincule os documentos de fluxo de trabalho dos documentos da API e `llms.txt`.
6. Empacote os mesmos fluxos de trabalho das ferramentas MCP quando útil.

Isso mantém o sistema fundamentado: OpenAPI descreve operações, Arazzo descreve sequenciamento, MCP expõe ferramentas que podem ser chamadas.

## Perguntas frequentes

### O Arazzo substitui o OpenAPI?

Não. Ele complementa o OpenAPI descrevendo fluxos de trabalho que usam operações OpenAPI.

### Arazzo é apenas para agentes de IA?

Não. É útil para documentação, geração de SDK, testes e conformidade. Os agentes de IA são um forte caso de uso.

### Preciso do Arazzo antes do MCP?

Nem sempre. Para ferramentas simples, o MCP pode ser suficiente. Para fluxos de trabalho de várias etapas, Arazzo ajuda a tornar o processo explícito.

### Qual é o ângulo de SEO?

Arazzo não é um fator de classificação. Melhora a prontidão da camada de execução, tornando os fluxos de trabalho legíveis por máquina.

### Quais fluxos de trabalho devem ser documentados primeiro?

Comece com fluxos de trabalho vinculados a receitas, resolução de suporte, reservas, integração ou ações sensíveis à conformidade.