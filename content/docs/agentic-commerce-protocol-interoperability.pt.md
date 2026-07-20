---
title: "Guia de interoperabilidade do protocolo de negociação de agentes."
date: 2026-05-25
weight: 159
category: "Architecture"
description: "Compare como as camadas de confiança da rede UCP, AP2, MCP, A2A, x402 e de cartão se encaixam na descoberta, no carrinho, no checkout e no atendimento."
summary: "Um mapa prático de interoperabilidade para protocolos de comércio de agentes, mostrando como a descoberta, o contexto, a autorização, o pagamento, a coordenação e a conformidade diferem."
keywords:
  - "interoperabilidade do protocolo de negociação de agentes"
  - "Processador central AP2 MCP A2A x402"
  - "protocolos de negociação de agentes"
  - "Arquitetura de negociação de IA"
  - "protocolos de pagamento de agentes"
---
# Interoperabilidade do protocolo de negociação do agente

A negociação de agentes não será executada em um único protocolo. O UCP ajuda os sistemas de negócios a interoperar, o AP2 lida com autorizações de pagamento verificáveis, o MCP expõe ferramentas e contexto, o A2A coordena agentes, o x402 lida com solicitações de pagamento nativas da máquina e as camadas de confiança da rede de cartões adicionam controles de identidade e pagamento. A tendência é a interoperabilidade e não o monopólio de protocolos.

## Por que a sobreposição de protocolo é esperada

O comércio tem muitos estágios do ciclo de vida. Descoberta, carrinho, checkout, atendimento, reembolso, autenticação e coordenação do agente são problemas diferentes.

Não se deve esperar que um único protocolo resolva todos eles.

A página existente [UCP vs ACP vs MCP](/es/docs/ucp-vs-acp-vs-mcp/) compara três padrões principais. Esta página mapeia a pilha mais ampla de negociação de agentes.

## Mapa de funções do protocolo

| Protocolo ou camada | Papel principal | Estágio de negociação |
|
---|
---|
---|
| PCU | Capacidade de comércio, carrinho, checkout, interoperabilidade pós-compra | Descoberta através do ciclo de vida do pedido |
| AP2 | Autorização e mandatos de pagamento verificáveis ​​| Intenção, pagamento, pagamento |
| PCM | Acesso a ferramentas e contexto | Fluxos de trabalho de agentes internos e externos |
| A2A | Coordenação entre agentes | Agentes compradores, comerciantes, plataformas e serviços |
| x402 | Solicitação de pagamento HTTP nativo e padrão de liquidação | API, conteúdo e pagamentos automáticos |
| Intenção verificável / TAP / Pagamento do agente | Confiança, identidade, tokenização e responsabilidade | Autorização e risco de pagamento |

A [comparação de protocolos de pagamento do agente](/es/docs/agent-payment-protocols-compared/) explica o lado do pagamento com mais detalhes.

## Fluxo de exemplo

Uma compra de agente poderia funcionar assim:

1. O agente descobre produtos por meio de páginas, feeds, esquemas ou recurso de catálogo UCP.
2. O agente compara opções usando políticas estruturadas e dados de produtos.
3. O agente cria um carrinho via UCP ou Merchant API.
4. A intenção do usuário é capturada por meio de comandos no estilo AP2 ou de uma camada de confiança comparável.
5. O pagamento é feito através de cartões, carteiras, x402, stablecoins ou crédito em conta.
6. Os eventos de atendimento atualizam o agente após o pagamento.
7. As evidências de disputa vinculam a intenção do usuário, a ação do agente, o carrinho, o pagamento e a entrega.

Isso explica por que [Agent Engine Optimization](/es/docs/what-is-aeo/) precisa de trabalho tanto na camada de leitura quanto na camada de execução.

## O que os comerciantes não devem fazer

Não espere que um padrão “ganhe”. Em vez disso, projete sistemas internos em torno de conceitos estáveis:

- identidade do produto
- intenção do usuário
- status do carrinho
- autorização de pagamento
- identidade do agente
- política comercial
- status do pedido
- trilha de auditoria

Em seguida, mapeie esses conceitos para protocolos à medida que amadurecem.

## Lista de verificação de interoperabilidade | Objeto interno | Precisa enfrentar o protocolo |
|
---|
---|
| Produto | Esquema, feed, catálogo de API, UCP |
| Carrinho | API do carrinho UCP ou carrinho comercial |
| Intenção | Mandato AP2 ou intenção verificável |
| Pagamento | AP2, token de cartão, carteira, x402, crédito em conta |
| Agente | Identidade, autenticação, política |
| Encomendar | API de eventos e status de conformidade |
| Auditoria | Trilha de evidências compartilhadas |

A página [evidência de disputas comerciais entre agentes](/es/docs/agentic-commerce-dispute-evidence/) cobre a camada de auditoria.

## Perguntas frequentes

### O UCP substituirá o AP2?Não. UCP e AP2 resolvem problemas diferentes. A UCP concentra-se na interoperabilidade comercial; AP2 concentra-se em autorizações e mandatos de pagamento seguros.

### O X402 compete com o AP2?

Às vezes eles podem aparecer na mesma conversa de pagamento, mas são diferentes. x402 é negociação de pagamento HTTP nativo; AP2 trata de autorização e intenção verificável em relação aos pagamentos do agente.

### Onde o MCP se encaixa?

O MCP ajuda os agentes a usar ferramentas e contexto. Ele pode oferecer suporte a fluxos de trabalho de negócios, mas não substitui protocolos de checkout ou checkout.

### O que os comerciantes devem implementar primeiro?

Comece com a consistência interna dos objetos: produto, carrinho, intenção, checkout, política, pedido e auditoria. As integrações de protocolo tornam-se mais fáceis depois disso.

## Fontes

Fontes primárias: [documentação UCP](https://ucp.dev/), [documentação AP2](https://ap2-protocol.org/), [Atualização do Google AI e UCP Commerce](https://blog.google/products-and-platforms/products/shopping/shopping-updates-google-marketing-live/), [documentos do Model Context Protocol](https://modelcontextprotocol.io/docs/concepts/tools), [anúncio do Cloudflare x402](https://blog.cloudflare.com/x402/) e [intenção verificável Mastercard](https://www.mastercard.com/europe/en/news-and-trends/stories/2026/verifiable-intent.html).