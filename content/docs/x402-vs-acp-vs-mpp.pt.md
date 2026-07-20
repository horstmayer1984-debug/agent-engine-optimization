---
title: "x402 vs ACP vs MPP: camada de pagamento, camada de pagamento, camada de pagamento."
metaTitle: "x402 vs ACP vs MPP: Comparação de protocolos."
date: 2026-05-08
weight: 119
category: "Architecture"
description: "Compare x402, ACP e MPP para pagamentos de agentes de IA, incluindo micropagamentos HTTP, pagamentos de agentes, sessões, streaming, moedas fiduciárias e stablecoins."
summary: "Um guia prático sobre as diferenças entre x402, ACP e MPP para comércio de agentes e pagamentos automáticos."
keywords:
  - "x402 x ACP x MPP"
  - "Protocolo de pagamentos automáticos"
  - "Protocolo de Negociação de Agente"
  - "Micropagamentos de agente de IA"
---
#x402 vs ACP vs MPP: camada de pagamento, camada paga, camada de pagamento automático

x402, ACP e MPP são frequentemente considerados concorrentes, mas resolvem diversos problemas de pagamento. x402 é um padrão de liquidação leve para recursos HTTP. ACP é um protocolo de pagamento comercial para compras iniciadas por agentes. MPP é um padrão de pagamento automático para sessões, uso medido e atividade contínua do agente.

A maneira mais fácil de compará-los é perguntar o que o agente está comprando.

Se o agente adquirir uma resposta de API, o x402 será adequado. Se o agente compra um produto de um comerciante, cabe o ACP. Se o agente pagar repetidamente durante uma tarefa em andamento, o MPP torna-se mais interessante.

## Diferença central

| Pergunta | x402 | ACP | MPP |
|---|---|---|---|
| O que está sendo resolvido? | Pagamento por recursos HTTP protegidos | Agente iniciou pagamento | Pagamentos automáticos ao longo do tempo |
| Padrão de comprador primário | Cliente ou Agente API | Agente de compras agindo por conta de um usuário | Fluxo de trabalho de agente, serviço ou máquina |
| Unidade de melhor valor | Uma solicitação ou recurso | Um pedido ou carrinho | Sessão, streaming, assinatura, uso medido |
| Modelo de pagamento | Liquidação de moedas normalmente estáveis ​​| Credenciais de checkout e checkout do comerciante | Fiat ou criptografia por meio de sessões de pagamento automático |
| Melhor exemplo | Pague 0,01 USDC por uma chamada de API | Compre um produto dentro de um assistente de IA | Pague continuamente pelo uso da API |

## O que o x402 faz bem?

O x402 é atraente porque mantém o protocolo próximo da web. Um servidor pode responder com HTTP 402 Payment Required, especificar o preço e os requisitos de pagamento e, em seguida, verificar o pagamento antes de servir o recurso.

Para fluxos de trabalho de agentes, isso é possível. Elimina a configuração de contas, a negociação de assinaturas e o provisionamento de chaves de API em pequenas transações digitais.

Bons casos de uso para x402 incluem:

1. Ferramentas MCP pagas
2. Endpoints de dados premium
3. Inferência por solicitação
4. Relatórios legíveis por máquina
5. Paywalls de conteúdo acessíveis ao agente
6. Chamadas de API onde o preço é conhecido antes da execução.

O ponto fraco não é a elegância técnica. O ponto fraco é o escopo. x402 não descreve toda a jornada de varejo, status do carrinho, devoluções, impostos, atendimento ou atendimento ao cliente.

## O que o ACP faz bem

O ACP foi projetado para negociação de agentes. OpenAI e Stripe o desenvolveram para casos em que um assistente de IA ajuda um usuário a descobrir, avaliar e comprar de um comerciante. A documentação de comércio de agentes do Stripe visa tokens de pagamento compartilhados, gerenciamento de catálogo de produtos e vendas contextualizadas. Esse é um problema diferente do x402. Uma compra no varejo não é apenas um pagamento. Inclui estoque, variantes, frete, impostos, dúvidas de comerciantes registrados, confirmação de pedido, cancelamento e devoluções.

O ACP é mais forte quando o agente opera dentro de um fluxo de compra do consumidor.

## O que o MPP faz bem

O MPP, oferecido a você pela Stripe e Tempo, foi projetado para pagamentos automatizados onde o agente não faz uma única ligação. Você pode operar em uma sessão, continuar usando um recurso ou pagar repetidamente enquanto o trabalho continua.

Isso se adapta bem aos sistemas autônomos. Os agentes nem sempre sabem o número exato das próximas chamadas. Eles podem precisar de uma cotação, prazo, limite de taxa e reconciliação após a conclusão do trabalho.

O MPP se ajusta melhor conceitualmente com:1. Uso contínuo de API
2. Assinaturas de agentes
3. Faturamento baseado no uso
4. Pagamentos com máquinas de streaming
5. Um orçamento delegado para um fluxo de trabalho autônomo

## Como vocês três podem trabalhar juntos

Uma pilha realista pode usar mais de um protocolo.

Um agente de IA pode descobrir um comerciante por meio de uma superfície comercial, usar ACP para fazer o pagamento, contar com AP2 ou controles de rede de cartão para autorização e pagar um provedor de dados terceirizado por meio de x402 ou MPP durante a etapa de investigação.

Em um fluxo de trabalho de desenvolvedor, um agente pode chamar ferramentas MCP pagas por meio de x402 para solicitações isoladas e depois mudar para MPP para uma tarefa de dados de longa duração com uso repetido.

A regra de design importante é a separação de interesses.

## O que os desenvolvedores devem implementar primeiro?

| Você opera | Comece com | Razão |
|---|---|---|
| Uma API paga | x402 | O endpoint pode definir o preço e verificar cada solicitação |
| Uma API SaaS com uso recorrente | MPP | Faturamento baseado em sessão e uso é importante |
| Uma loja de comércio eletrônico | ACP | O processo de pagamento é o verdadeiro problema |
| Um mercado de dados | x402 e MPP | Alguns ativos são adquiridos uma vez, outros são mensurados |
| Uma plataforma de agente de IA | ACP, MPP e x402 | Vendedores diferentes exigirão métodos de pagamento diferentes |

## Notas de implementação do AEO

Para AEO, o suporte do protocolo deve estar visível antes da tentativa de pagamento.

Adicione uma página ou endpoint legível por máquina informando:

1. Protocolos de pagamento suportados
2. Moedas ou trilhos aceitos
3. Tamanho mínimo e máximo de upload
4. Política de reembolso ou reversão
5. Requisitos de autenticação
6. Códigos de erro
7. Regras de idempotência
8. Via de contato ou disputa

Isso converte o pagamento de um evento de pagamento oculto em um recurso legível pelo agente.

## Perguntas frequentes

**O MPP está substituindo o x402?**Não diretamente. MPP é melhor para sessões e uso contínuo. O x402 permanece mais limpo para uma liquidação simples no nível da solicitação.

**O ACP é apenas para ChatGPT?**
O ACP foi construído com OpenAI e Stripe para comércio de agentes, mas o protocolo está posicionado como um padrão de comércio aberto em vez de um recurso exclusivo do ChatGPT.

**Um comerciante pode usar x402 e ACP juntos?**
Sim. Um comerciante poderia usar ACP para fazer pagamentos e x402 para acesso pago à API, dados premium ou serviços de agente.

**Qual protocolo é melhor para micropagamentos com stablecoins?**
x402 é a escolha mais clara para micropagamentos leves de stablecoin via HTTP. Stripe Machine Payments também oferece suporte a pagamentos automatizados com liquidação criptográfica na infraestrutura Stripe.

## Fontes

Principais referências: [documentação x402](https://docs.x402.org/faq), [anúncio da Linux Foundation x402 Foundation](https://www.linuxfoundation.org/press/linux-foundation-is-launching-the-x402-foundation-and-welcoming-the-contribution-of-the-x402-protocol), [anúncio do Stripe ACP](https://stripe.com/newsroom/news/stripe-openai-instant-checkout), [documentação do Stripe Agent Commerce](https://docs.stripe.com/agentic-commerce), [documentação do Stripe Machine Payments](https://docs.stripe.com/payments/machine) e [Stripe MPP anúncio](https://stripe.com/blog/machine-payments-protocol).

## Guias relacionados

* [arquitetura de comércio do agente](/es/docs/agentic-commerce/)
* [protocolos de pagamento do agente](/es/docs/agent-payment-protocols-compared/)
* [camada de execução](/es/docs/execution-layer/)