---
title: "Atribuição de negociação do agente: Medindo referências."
metaTitle: "Guia de atribuição de negociação de agentes."
date: 2026-05-25
weight: 151
category: "Guide"
description: "Descubra como a negociação de agentes muda a atribuição, por que os benchmarks de IA são mais difíceis de medir e o que os traders devem registrar."
summary: "Um guia prático para atribuição de comércio de agentes, abrangendo benchmarks de IA, contexto UCP, sessões de origem de agentes, dados de intenção, lacunas analíticas e métricas AEO."
keywords:
  - "atribuição de negociação de agente"
  - "Rastreamento de referência de IA"
  - "Contexto UCP"
  - "análise de negociação de agentes"
  - "Atribuição de compra de IA"
---
# Atribuição de comércio do agente: medindo referências e intenção de IA

A atribuição de comércio do agente é a prática de conectar uma recomendação, um carrinho ou uma sessão de checkout assistida por IA ao agente, à superfície, à intenção do usuário e ao resultado do comerciante. É mais difícil do que o rastreamento de referências clássico porque a decisão do usuário pode ser formada dentro de um sistema de inteligência artificial antes de haver uma visita normal ao site.

## Por que a atribuição está mudando

A análise clássica de comércio eletrônico pressupõe que o comprador clica em um link, chega a uma página, navega, adiciona ao carrinho e compra. A negociação de agentes quebra esse caminho. O agente pode pesquisar produtos, comparar ofertas, criar um carrinho e enviar apenas a ação final ou indicação ao lojista.

A pesquisa comercial do PayPal observa que as empresas estão se preparando para sistemas de inteligência artificial que influenciam a descoberta antes que o comprador chegue ao site. O Google também enquadra o UCP e o Universal Cart como infraestrutura para o comércio de agentes nas superfícies do Google.

É por isso que a [medição AEO](/es/docs/aeo-kpis-measurement/) precisa de mais do que classificações e cliques.

## O que os comerciantes devem atribuir

| Sinal | Por que é importante |
|
---|
---|
| Fonte de IA ou Superfície do Agente | Mostra onde ocorreu a descoberta |
| Categoria de intenção do usuário | Distinguir pesquisa, carrinho, novo pedido, suporte ou reembolso |
| ID dos produtos mostrados ao agente | Conecte a exposição do catálogo às vendas |
| Fonte de criação do carrinho | Revela se o carro foi formado dentro ou fora do local |
| Transferência de pagamento | Mostra onde a compra foi finalizada |
| Referência de comando ou autorização | Links com intenção de pagamento quando suportado |
| Resultado de conformidade | Conecte transações de origem do agente com entregas e devoluções |

O modelo [cinco níveis de comércio de agentes](/es/docs/five-levels-agentic-commerce/) é útil porque a maturidade da atribuição muda em cada nível.

## O problema UTM

As tags UTM ainda são úteis quando um assistente de IA envia um usuário para uma página. Mas são fracos quando o agente não simplesmente recomenda um visitante.

Os agentes de viagens podem precisar de:

- objetos de contexto assinados
- referências de carrinho
- listas de candidatos de produtos
- ID do comando
- status de consentimento
- identificadores de plataforma
- confirmação do comerciante registrado

Isso está mais próximo do rastreamento de transações do que do rastreamento de campanhas.

## Métricas AEO para negociação de agentes

| Métrica | O que isso diz a você |
|
---|
---|
| Sessões indicadas pelo agente | Com que frequência os sistemas de IA enviam tráfego?
| Taxa do carrinho de origem do agente | Se os agentes puderem construir carros com sucesso |
| Cobertura de catálogo estruturado | Quanto inventário pode ser lido por máquina?
| Conclusão do pagamento do agente | Se a transferência ou pagamento nativo funcionar |
| Taxa de rejeição de políticas | Se as políticas bloquearem as transações do agente || Taxa de exceção pós-compra | Se pedidos provenientes de agentes causarem mais reembolsos ou problemas de suporte |

Vincule essas métricas à [camada de execução](/es/docs/execution-layer/), não apenas aos relatórios de conteúdo.

## Lista de verificação de implantação1. Preservar o rastreamento de referência normal e UTM.
2. Adicione nomes de eventos de origem ao agente em análise.
3. Registre o agente do usuário, o status verificado do bot e a plataforma de origem, quando disponível.
4. Armazene a origem do carrinho e o caminho de transferência do carrinho.
5. Mapeie IDs de produtos para dados expostos em feeds, esquemas e APIs.
6. Rastreie erros de pagamento separadamente para sessões de origem do agente.
7. Conecte dados de pedidos, reembolsos e suporte ao contexto de origem.

O [Guia do Protocolo de Negociação Universal](/es/docs/universal-commerce-protocol/) explica onde a negociação pode se encaixar no contexto da negociação.

## Perguntas frequentes

### As referências de IA são visíveis no Google Analytics?

Alguns são visíveis como referências normais ou tráfego de campanha. Outros podem aparecer como tráfego direto, de bot, de parceiro ou mediado por plataforma, a menos que a integração preserve o contexto.

### A atribuição é apenas um problema de marketing?

Não. No comércio de agentes, a atribuição também afeta fraude, testes de disputa, política comercial e suporte pós-compra.

### Qual é a primeira métrica a ser adicionada?

Rastreie as sessões de origem do agente e o início do carrinho separadamente do tráfego regular orgânico, pago e direto.

### Como isso se relaciona com o AEO?

O AEO precisa demonstrar que a infraestrutura legível pelo agente impulsiona a descoberta, a atividade do carrinho, as ações concluídas e os resultados confiáveis.

## Fontes

Principais fontes: [descobertas do PayPal Agentic Commerce Pulse](https://www.paypal.com/us/brc/article/agentic-commerce-pulse-report-findings), [PayPal em AI Storefronts](https://www.paypal.com/us/brc/article/ai-storefront-what-merchants-need-to-know) e [atualização do Google UCP e do carrinho universal](https://blog.google/products-and-platforms/products/shopping/shopping-updates-google-marketing-live/).