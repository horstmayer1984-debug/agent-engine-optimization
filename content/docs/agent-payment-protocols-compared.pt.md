---
title: "Protocolos de pagamento de agente comparados: x402, ACP, MPP, AP2."
metaTitle: "Protocolos de pagamento de agentes comparados para negociação de IA."
date: 2026-05-08
weight: 118
category: "Architecture"
description: "Uma comparação prática de x402, ACP, MPP, AP2, Visa TAP, Mastercard Agent Pay, UCP e Nevermined para pagamentos de agentes AI."
summary: "Guia de comparação de protocolos de pagamento de agentes em 2026, abrangendo liquidação, pagamento, autorização, cartões, sessões e infraestrutura de agentes."
keywords:
  - "protocolos de pagamento de agentes"
  - "x402 x ACP x MPP"
  - "Pagamentos de Agente AP2"
  - "Pagamentos de agente de IA"
  - "protocolos de negociação de agentes"
---
# Protocolos de pagamento de agente comparados: x402, ACP, MPP, AP2, TAP, pagamento de agente

Os protocolos de pagamento dos agentes serão divididos em três camadas em 2026: liquidação, orquestração comercial e confiança. x402 é mais poderoso para pagamentos HTTP leves e liquidação de stablecoin. ACP e UCP cobrem a jornada de compras. O MPP visa pagamentos recorrentes automáticos. AP2, Visa TAP e Mastercard Agent Pay focam na autorização, identidade e confiança na rede de cartões.

Isso é importante para o Agent Engine Optimization porque os pagamentos não são mais apenas um detalhe de pagamento. Se um agente de IA puder descobrir sua oferta, mas não puder pagar, autorizar ou verificar a transação, seu site estará visível, mas não executável.

## Comparação rápida

| Protocolo ou sistema | Principais patrocinadores | Melhor ajuste | Abordagem de pagamento | Papel típico em pilha |
|
---|
---|
---|
---|
---|
| x402 | Ecossistema Coinbase, Cloudflare, Stripe, Linux Foundation | API Pay Per Request e serviços de agente | Liquidação HTTP 402, geralmente stablecoins | Camada de liquidação |
| ACP | OpenAI e Stripe | Pagamento em contexto através de agentes de IA | Pagamento Comerciante e Tokens de Pagamento Compartilhados | Fluxo comercial |
| MPP | Linha e andamento | Pagamentos automáticos contínuos e uso de API | Sessões, streaming, cobrança baseada no uso | Camada de pagamento por máquina |
| AP2 | Google e parceiros de pagamento | Demonstrar a intenção e autorização do usuário | Mandatos criptográficos e confiança | Camada de autorização |
| PCU | Google e parceiros comerciais | Agentes de compras de viagens | Descoberta, catálogo, pagamento, pós-compra | Camada de protocolo de negociação |
| Visto TAP | Ecossistema de vistos | Confiança dos comerciantes nos agentes de IA | Sinais e credenciais de identidade do agente | Ponte ferroviária confiável e cartão |
| Pagamento de Agente Mastercard | Cartão Master | Transações de agente baseadas em cartão | Pagamentos de agentes tokenizados | Camada de rede da placa |
| Nunca minerado | Nunca minerado | API do agente de monetização, ferramentas MCP, ativos protegidos | Planos, direitos, x402, fluxos de cartões e stablecoins | Plataforma de infraestrutura |

## O que mudou em maio de 2026?

O mercado não possui mais um padrão de pagamento óbvio. Tem uma bateria.

O x402 passou do experimento de criptografia nativa para uma infraestrutura mais ampla depois que a Linux Foundation anunciou a Fundação x402 com a Coinbase contribuindo para o protocolo. Stripe publicou documentação sobre pagamentos automáticos e introduziu MPP com Tempo. OpenAI e Stripe fizeram do ACP a camada de negócios por trás do Instant Checkout. O Google promoveu o AP2 como um protocolo de autorização e depois transferiu o AP2 para a governança de padrões por meio da Aliança FIDO. Visa e Mastercard trouxeram modelos de confiança de rede de cartões para a conversa de pagamentos de agentes. O resultado prático é simples: os comerciantes não deveriam perguntar: “Qual protocolo vence?” Eles deveriam perguntar: "Que camada este protocolo resolve?"

## Camada de liquidação: x402

x402 revive o padrão HTTP 402 Payment Required para pagamentos de agentes e API. Um cliente solicita um recurso protegido, o servidor retorna os requisitos de pagamento, o cliente anexa o comprovante de pagamento e o servidor concede acesso após verificação.

O x402 é forte quando o produto é pequeno, digital, baseado em API ou com preço por solicitação. Um endpoint climático, uma fonte de dados premium, uma ferramenta MCP, uma chamada de inferência ou um relatório legível por máquina podem cobrar por invocação sem a necessidade de criar uma conta.Sua limitação também é clara. x402 estabelece o valor. Não resolve todo o processo de compra sozinho. Um comerciante ainda precisa de descoberta de produtos, divulgação de políticas, controles de fraude, reembolsos, identidade, impostos, suporte e gerenciamento de disputas.

Leia o guia do site: [Agent Payments x402](/es/docs/x402-agent-payments/).

## Camada de Comércio: ACP e UCP

ACP e UCP estão mais próximos do processo de compra do que x402.

O ACP, desenvolvido pela OpenAI e Stripe, foi projetado com base no pagamento iniciado pelo agente. Stripe descreve o comércio de agentes como uma forma de compradores, agentes e empresas realizarem transações com segurança, com tokens de pagamento compartilhados e gerenciamento de catálogo no fluxo.

A UCP é mais ampla. Ele está posicionado como uma linguagem comercial comum para compras de agentes por meio de descoberta, interação com catálogo, pagamento e suporte pós-compra. Isso o torna menos um método de pagamento e mais uma superfície de protocolo comercial.

Para equipes de comércio eletrônico, ACP e UCP são mais relevantes do que x402 quando o problema é uma compra normal no varejo, em vez de uma solicitação de API paga.

## Camada de pagamento por máquina: MPP

O MPP, de coautoria de Stripe e Tempo, destina-se a agentes que pagam empresas e outros agentes sem que um ser humano saiba. Seu caso de uso mais forte não é um pagamento único. É uma atividade recorrente, contínua ou medida.

Isso se adapta bem aos sistemas autônomos. Os agentes nem sempre sabem o número exato das próximas chamadas. Eles podem precisar de uma cotação, prazo, limite de taxa e reconciliação após a conclusão do trabalho.

Se o x402 estiver limpo para uma solicitação, o MPP será interessante para uma série de solicitações.

## Camada de autorização: AP2

AP2 é a resposta do Google para o problema da confiança: como um comerciante sabe que um usuário autorizou o agente a comprar aquele item nessas condições? O Google descreve o AP2 como um protocolo aberto para iniciar e realizar transações seguras de pagamentos conduzidos por agentes em todas as plataformas. Seu conceito central é o mandato: evidência criptograficamente verificável que captura a intenção do usuário, detalhes do carrinho e autorização de pagamento.

AP2 tem menos a ver com forma de pagamento e mais a ver com responsabilidade. Ele pode funcionar com cartões, carteiras e trilhos de liquidação de criptomoedas. Isso o torna um complemento do x402 em vez de um puro substituto.

## Camada de rede do cartão: Visa TAP e Mastercard Agent Pay

Visa TAP e Mastercard Agent Pay resolvem um problema diferente: como as redes de cartões existentes se adaptam ao comércio iniciado pelos agentes.

A Visa TAP oferece aos comerciantes uma maneira de distinguir agentes legítimos de IA de tráfego automatizado suspeito e transmitir credenciais e contexto de agente em todo o fluxo comercial. Mastercard Agent Pay pega conceitos de tokenização já usados ​​no comércio de cartões e os aplica aos pagamentos de agentes.

Esses sistemas são importantes porque muitos traders não começarão com stablecoins. Eles começarão com cartões, processadores, credenciais tokenizadas e sistemas de fraude existentes nos quais já confiam.

## Camada de plataforma: Nevermined

Nevermined não é apenas um protocolo. É uma infraestrutura para acesso pago a APIs de agentes, ferramentas MCP e ativos protegidos. Sua documentação descreve suporte para fluxos x402, pagamento Stripe, stablecoins, planos e verificações de direitos.

Isso torna o Nevermined relevante para equipes que desejam uma camada de pagamento de agente conveniente, sem ter que construir todos os componentes por conta própria.## Qual protocolo uma empresa deve escolher?

| Tipo de negócio | Primeiro protocolo a avaliar | Por que |
|
---|
---|
---|
| API de pagamento ou provedor de dados | x402 ou MPP | Mediante solicitação e uso medido são opções naturais |
| Comerciante de comércio eletrônico | ACP ou UCP | A descoberta e o pagamento do produto são mais importantes do que a liquidação bruta |
| Fluxo de trabalho de compras empresariais | AP2 mais métodos de pagamento existentes | A autorização e a auditabilidade são fundamentais |
| Cartão de varejo pesado | Pagamento de agente Visa TAP ou Mastercard | As redes de cartões existentes continuam a ser a base operacional |
| Fornecedor de ferramentas MCP | x402, MPP ou Nevermined | As ferramentas precisam de acesso pago, direitos e fluxos seguros de novas tentativas |

## Implicações do AEO

Para AEO, o padrão vencedor é uma pilha híbrida.

Um site deve publicar dados de produtos ou serviços legíveis por máquina, expor caminhos de ação determinísticos, documentar autorização e requisitos de pagamento e tornar o resultado verificável. Os protocolos de pagamento só ajudam depois que o agente consegue entender o que o site oferece e quais ações são seguras a serem tomadas. Próximas etapas internas: Leia [Protocolos de Agente AI](/es/docs/protocols/), [Camada de Execução](/es/docs/execution-layer/) e [x402 MCP A2A Full Stack](/es/docs/x402-mcp-a2a-full-stack/).

## Perguntas frequentes

**Qual é o melhor protocolo de pagamento de agente em 2026?**
Não existe um único protocolo melhor. x402 é mais poderoso para liquidações HTTP leves, ACP e UCP são mais poderosos para fluxos de negócios, MPP atende a pagamentos automáticos contínuos e AP2 se concentra em autorização e confiança.

**O x402 é melhor que o ACP?**
x402 e ACP resolvem camadas diferentes. x402 lida com liquidação de pagamentos via HTTP. ACP lida com pagamentos iniciados por agentes e integração de comerciantes.

**AP2 é uma forma de pagamento?**
AP2 é melhor entendido como um protocolo de autorização e confiança. Ele pode oferecer suporte a diferentes métodos de pagamento e liquidação.

**Visa e Mastercard competirão com x402?**
Eles competem em alguns casos de uso, mas também resolvem diversos problemas de adoção. As redes de cartões ajudam os comerciantes existentes a oferecer suporte aos pagamentos dos agentes sem ter que primeiro migrar para os trilhos cripto-nativos.

**O que os comerciantes devem implementar primeiro?**
A maioria dos comerciantes deve começar com dados estruturados de produtos, políticas claras e requisitos de pagamento legíveis pelo agente. A escolha do protocolo deve seguir o modelo de negócio.

## Fontes

As fontes primárias usadas para este artigo incluem [Linux Foundation na x402 Foundation](https://www.linuxfoundation.org/press/linux-foundation-is-launching-the-x402-foundation-and-welcoming-the-contribution-of-the-x402-protocol), [documentação x402](https://docs.x402.org/faq), [Stripe on ACP](https://stripe.com/newsroom/news/stripe-openai-instant-checkout), [Stripe Machine Payments](https://docs.stripe.com/payments/machine), [Stripe MPP Anúncio](https://stripe.com/blog/machine-payments-protocol), [Google Cloud AP2 anúncio](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol/), [atualização do Google AP2 FIDO](https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/), [documentação UCP](https://ucp.dev/), [página do desenvolvedor Visa TAP](https://developer.visa.com/capabilities/trusted-agent-protocol/overview), [anúncio de pagamento do agente Mastercard](https://www.mastercard.com/news/press/2025/april/mastercard-unveils-agent-pay-pioneering-agentic-payments-technology-to-power-commerce-in-the-age-of-ai/) e [documentação Nevermined](https://nevermined.ai/docs/getting-started/how-it-works).