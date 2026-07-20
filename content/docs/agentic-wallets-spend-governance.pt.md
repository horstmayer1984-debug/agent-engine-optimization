---
title: "Portfólios de Agentes e Governança de Gastos: Como Agentes de IA."
metaTitle: "Carteiras de agentes e governança de gastos."
date: 2026-05-25
weight: 153
category: "Architecture"
description: "Saiba como carteiras de agentes, limites de gastos, tokenização, registros de auditoria e controles de políticas fazem com que os pagamentos aconteçam."
summary: "Um guia prático para carteiras de agentes e gerenciamento de despesas, incluindo Fireblocks, AP2, Mastercard Agent Pay, autoridade delegada, stablecoins e controles de auditoria."
keywords:
  - "portfólios de agentes"
  - "governança de gastos"
  - "Pagamentos de agente de IA"
  - "carteiras delegadas"
  - "controles de pagamento do agente"
---
# Carteiras de agentes e governança de gastos

As carteiras dos agentes permitem que os agentes de IA paguem dentro das regras definidas por um usuário ou organização. A governança de gastos é a camada de controle: orçamentos, limites de negociação, escopos de tokens, registros de auditoria, verificações de conformidade e revogação. Sem esses controlos, os pagamentos dos agentes são demasiado arriscados para o comércio de rotina.

## Por que as carteiras estão mudando

Uma carteira humana pressupõe que uma pessoa aprova cada compra. Uma carteira de agente significa que uma pessoa ou empresa delega autoridade limitada ao software.

Isso cria um novo problema de design:

- O agente precisa de autoridade suficiente para concluir uma tarefa.
- O usuário precisa ter certeza de que o agente não poderá gastar mais.
- O comerciante precisa de prova de que o agente tem permissão para comprar.
- O emissor, PSP ou provedor de carteira precisa de uma trilha de auditoria.

Agentic Payments Suite e Mastercard Agent Pay da Fireblocks apontam para essa mudança.

## Controles de governança de gastos

| Controle | Exemplo |
|
---|
---|
| Limite de montante | Agente pode gastar até US$ 50 por compra |
| Área comercial | Agente só pode comprar de fornecedores aprovados |
| Escopo da categoria | Agente pode comprar material de escritório, não eletrônicos |
| Janela de tempo | A autoridade expira após sete dias |
| Âmbito da finalidade | Agente pode reabastecer uma família de SKU |
| Limiar de aprovação | Revisão humana exigida acima de um limite |
| Revogação | O usuário pode desativar o token do agente ou a concessão da carteira |
| Trilha de auditoria | Cada ação registra a intenção, o pagamento e o resultado |

Esses controles são essenciais para a [camada de execução](/es/docs/execution-layer/).

## Tokens de cartão vs. carteiras Stablecoin

| Modelo | Força | Restrição |
|
---|
---|
---|
| Tokenização de rede de cartões | Aceitação de Empresa Familiar, Controles do Emissor, Regras de Disputas | Precisa de sinais de autorização e identidade do agente |
| Carteira Stablecoin | Liquidação programável e fluxos de máquinas nativas | Requer controles de conformidade, custódia e reconciliação |
| Crédito em conta | Útil para SaaS e API | Limitado a uma plataforma |
| Transferência bancária/trilhos em tempo real | Bom para mercados com pagamentos rápidos de contas | A disponibilidade e a lógica de reembolso variam |

A [comparação de protocolos de pagamento de agentes](/es/docs/agent-payment-protocols-compared/) mapeia a camada de protocolo. Esta página concentra-se na camada de controle da carteira.

## Implicações de negócios

Os comerciantes devem esperar receber mais transações onde:

- um agente atua em nome de um usuário
- o instrumento de pagamento tem alcance
- o pedido inclui provas de intenção
- os limites da política afetam a autorização
- as disputas dependem dos registros dos agentes

Isso significa que os sistemas de pagamento devem armazenar mais contexto do que uma autorização normal de cartão.

## O que preparar agora

1. Adicione campos para identidade do agente e referência de autorização.2. Registre eventos de carrinho, checkout e atendimento juntos.
3. Decida quais produtos podem ser adquiridos pelos agentes delegados.
4. Definir categorias de alto risco que requerem confirmação humana.
5. Revise as regras de fraude para transações originadas por agentes.
6. Mantenha as declarações de reembolso e cancelamento legíveis por máquina.

O artigo [Fireblocks Agentic Payments Suite](/es/docs/fireblocks-agentic-payments-suite/) aborda um exemplo de infraestrutura.

## Perguntas frequentes

### Uma carteira de agente é uma carteira digital normal?Não. É uma carteira delegada ou configuração de pagamento onde um agente de IA pode agir dentro de limites explícitos.

### As carteiras dos agentes podem usar cartões?

Sim. Mastercard descreve tokens de agente e Agent Pay para pagamentos de redes de cartões específicos. AP2 também inclui amostras de cartão e x402.

### As carteiras dos agentes podem usar stablecoins?

Sim. Fireblocks descreve carteiras de agentes para pagamentos de stablecoin dentro de limites definidos e trilhas de auditoria.

### Qual é o maior risco?

Autoridade ilimitada. As carteiras dos agentes precisam de limites rígidos de gastos, escopo de finalidade, revogação e registros confiáveis.

## Fontes

Fontes primárias: [Anúncio do Fireblocks Agentic Payments Suite](https://www.prnewswire.com/news-releases/fireblocks-joins-x402-foundation-launches-agentic-payments-suite-302777251.html), [Documentação AP2](https://ap2-protocol.org/), [Intenção verificável da Mastercard](https://www.mastercard.com/europe/en/news-and-trends/stories/2026/verifiable-intent.html) e [Whitepaper de compras com tecnologia de IA da Mastercard](https://www.mastercard.com/content/dam/mccom/eu/news-and-trends/business-thought-leadership/digital-payments/pdfs/Get_ready_for_AI-powered_shopping_experiences.pdf).