---
title: "Eventos de atendimento de comércio agente: pedidos."
metaTitle: "Eventos de conformidade comercial de agentes."
date: 2026-05-25
weight: 156
category: "Architecture"
description: "Descubra por que os eventos de atendimento são importantes na negociação de agentes, como os agentes precisam do status do pedido e da entrega."
summary: "Um guia para o comércio pós-compra do agente, abrangendo eventos de atendimento, status do pedido, devoluções, reembolsos, fidelidade, ciclo de vida do pedido UCP e prontidão para AEO."
keywords:
  - "conformidade comercial do agente"
  - "agentes de IA de eventos de conformidade"
  - "Ciclo de vida do pedido UCP"
  - "O agente de IA retorna"
  - "agente comercial de fidelidade"
---
# Eventos de atendimento comercial de agente

A negociação do agente não termina quando o pagamento é autorizado. Os agentes também precisam do status do pedido, eventos de envio, confirmação de entrega, cancelamento, devoluções, reembolsos, garantia e dados de fidelidade. Se os status pós-compra não forem legíveis por máquina, o agente não poderá realizar a tarefa após o pagamento.

## Por que a conformidade faz parte do AEO

O comércio eletrônico tradicional muitas vezes trata o atendimento como um processo administrativo. A negociação do agente faz parte do fluxo de trabalho do usuário porque o agente pode ser responsável por monitorar o pedido.

Por exemplo, um agente pode precisar:

- confirme a entrega antes de fechar uma tarefa
- reordenar se a conformidade falhar
- solicitar um reembolso
- atualizar um usuário sobre um atraso
- aplicar benefícios de fidelidade
- verifique se uma assinatura foi iniciada

Este é o comportamento da camada de execução. Pertence junto com [execução de negociação de agente](/es/docs/agentic-commerce-execution/) e [Os 5 níveis de negociação de agente](/es/docs/five-levels-agentic-commerce/).

## Eventos pós-compra que os agentes precisam

| Evento | Usando o agente |
|
---|
---|
| Encomenda aceite | Confirme se a compra existe |
| Pagamento capturado | Confirmar movimentação de dinheiro |
| Inventário reservado | Reduz o risco de cancelamento |
| Envio criado | Dá visibilidade de rastreamento |
| Entrega confirmada | Marcar tarefa concluída |
| Retorno iniciado | Iniciar tratamento de exceções |
| Reembolso emitido | Confirmar resolução |
| Lealdade aplicada | Confirmar benefícios e link de identidade |

## UCP e pensamento de ciclo de vida de pedidos

A documentação do UCP descreve capacidades comerciais além da descoberta e do pagamento, incluindo experiências pós-compra. O Google também enquadra o UCP como uma infraestrutura ao longo da jornada comercial do agente.

Isso é importante porque os agentes precisam de mais do que um recibo. Eles precisam de transições de estado com significados claros.

## Lista de verificação de implantação

1. Use IDs de pedido e carrinho estáveis.
2. Devolva a confirmação estruturada após o pagamento.
3. Exiba o status de rastreamento em um formato legível por máquina.
4. Publicar regras de elegibilidade para cancelamento e devolução.
5. Mantenha o status do reembolso separado do status da devolução.
6. Conecte a identidade de fidelidade ao pedido quando autorizado.
7. Registrar eventos de ordem de origem do agente para equipes de suporte.
8. Forneça estados de erro que os agentes possam explicar aos usuários.

O [Guia do carrinho universal](/es/docs/universal-cart-agentic-commerce/) cobre o lado do pré-pagamento; Esta página cobre após o pagamento.

## Tabela de risco de conformidade

| Risco | Impacto | Correção |
|
---|
---|
---|
| Estados de ordem vagos | O agente não consegue explicar o que aconteceu | Use códigos de status explícitos |
| Falta acompanhamento | O agente deve encaminhar o usuário ao site da operadora | Expor eventos e URLs de rastreamento || Ambiguidade da Política de Devolução | O agente não consegue determinar a elegibilidade | Estrutura da janela e condições de retorno |
| Incompatibilidade de lealdade | Usuário perde benefícios | Suporta vinculação de identidade quando disponível |
| Reembolsar opacidade | Aumenta o volume de suporte | Expor o status e o valor do reembolso |

## Defina eventos de cumprimento como um contrato estávelCada evento de atendimento deve identificar o pedido, o tipo de evento, o carimbo de data/hora, o estado atual, o estado anterior e as próximas ações permitidas. O evento também precisa de um identificador estável para que uma repetição do webhook não resulte em reembolso, cancelamento ou ajuste de fidelidade duplicados.

Trate o texto de status legível como uma apresentação, não como um contrato. Um agente deve agir em um estado documentado, como `enviado`, `entregue`, `return_requested` ou `reembolsado`. Texto livre, como “a caminho”, pode permanecer nas mensagens do cliente, mas não deve controlar a lógica do fluxo de trabalho.

Teste três casos de falha antes do lançamento: eventos que chegam fora de ordem, o mesmo evento que chega duas vezes e um reembolso parcial que não fecha todo o pedido. Uma implementação confiável preserva o histórico e expõe o estado atual da autoridade após cada instância.

## Perguntas frequentes

### Por que os agentes precisam de eventos de conformidade?

Porque muitas tarefas delegadas incluem acompanhar o resultado, não apenas fazer o pedido.

### A conformidade faz parte do UCP?

O UCP foi projetado para fluxos comerciais além do checkout, incluindo experiências pós-compra. Os detalhes de implementação dependem do comerciante e da plataforma.

### O que os traders devem expor primeiro?

Confirmação do pedido, status de envio, status de entrega, elegibilidade para cancelamento, elegibilidade para devolução e status de reembolso.

### Isso afeta o SEO?

Afeta o AEO. Os agentes precisam de dados pós-compra confiáveis ​​para concluir tarefas com segurança e manter os usuários informados.

## Fontes

Fontes primárias: [documentação UCP](https://ucp.dev/), [Atualização do Google UCP e AI Commerce](https://blog.google/products-and-platforms/products/shopping/shopping-updates-google-marketing-live/) e [PayPal na infraestrutura da AI Store](https://www.paypal.com/us/brc/article/ai-storefront-what-merchants-need-to-know).