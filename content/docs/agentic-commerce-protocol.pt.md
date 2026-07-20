---
title: "Protocolo de Negociação de Agentes (ACP): quais são os traders."
date: 2026-05-17
weight: 133
category: "Architecture"
description: "Aprenda o que é o Agent Merchant Protocol, onde o ACP se encaixa no processo de pagamento de IA e como os comerciantes devem compará-lo aos protocolos."
summary: "Um guia prático de ACP para comerciantes, abrangendo vendas no contexto, pagamento por IA, o escopo dos pagamentos e como o ACP difere do UCP e do MCP."
keywords:
  - "Protocolo de Negociação de Agente"
  - "Protocolo ACP"
  - "pagamento com IA"
  - "agente comercial"
  - "Pagamento via ChatGPT"
---
#Protocolo de Negociação de Agente (ACP): O que os comerciantes devem saber

O Agentic Commerce Protocol é a camada de protocolo de documento Stripe para permitir a venda no contexto em agentes de IA. Em termos práticos, ACP trata de efetuar pagamentos dentro da experiência de um agente: um usuário descobre um produto em uma superfície de IA, mantém o fluxo de compra no contexto e o comerciante se conecta a esse fluxo sem reconstruir toda a vitrine em torno de uma sessão de navegador humano.

## O que dizem os documentos oficiais

A documentação do Stripe Agent Commerce instrui as empresas a permitir a venda no contexto em agentes de IA usando o Agent Commerce Protocol. O anúncio de lançamento do Stripe também descreve o ACP como um padrão aberto desenvolvido em parceria com a OpenAI. Isso coloca o ACP diretamente na camada de experiência de transação, em vez de na pesquisa completa, nos dados do produto ou na pilha de orquestração multiagente.

Fontes primárias:

- [Documentos Stripe: Agente de Comércio](https://docs.stripe.com/agentic-commerce)
- [Redação Stripe: Pagamento Instantâneo e ACP](https://stripe.com/newsroom/news/stripe-openai-instant-checkout)

## ACP comparado a protocolos próximos

| Protocolo | Trabalho principal |
|
---|
---|
| ACP | Pagamento contextualizado para experiências de agentes de IA |
| PCU | Ciclo de vida empresarial mais amplo e negociação de capacidades |
| PCM | Acesso a ferramentas e dados para agentes |
| x402 | Fluxo de pagamento automático para recursos HTTP |

O [guia UCP, ACP e MCP](/es/docs/ucp-vs-acp-vs-mcp/) cobre uma comparação mais ampla. O ACP é melhor entendido como um protocolo de experiência de negócios focado, e não como um substituto para qualquer outra parte de uma pilha pronta para agente.

## Quando o ACP é importante

O ACP torna-se relevante quando:

- os compradores descobrem produtos em conversas de IA
- os comerciantes desejam que o pagamento aconteça sem uma rota de redirecionamento desajeitada
- A superfície AI está se tornando um verdadeiro canal de vendas
- o comerciante já possui dados de produtos, preços e informações de política suficientes para fazer compras automatizadas

Este último ponto é fácil de subestimar. O pagamento não resgata dados incorretos do produto. [Lista de verificação de SEO para recomendações de produtos ChatGPT] (/es/docs/chatgpt-product-recommendations-seo/) explica o que precisa acontecer antes da seleção.

##O que os traders devem preparar primeiro?

| Área de preparação | Por que é importante |
|
---|
---|
| Detalhes do produto | Os agentes precisam de dados antes de recomendar ou comprar |
| Preço e disponibilidade | Dados desatualizados quebram a confiança imediatamente |
| Devoluções e envios | As limitações do comprador normalmente incluem ambos |
| Controles de fraude | Pedidos conduzidos por agentes ainda precisam de gerenciamento de risco |
| Confirmação do pedido | O resultado deve ser determinístico e auditável |

O ACP pode reduzir o atrito no processo de checkout, mas a [camada de execução](/es/docs/execution-layer/) ainda precisa de transições de estado de back-end confiáveis.

## ACP versus pagamento de comércio eletrônico tradicional | Caixa tradicional | Fluxo estilo ACP |
|
---|
---|
| O comprador navega pela janela | O comprador pode permanecer na interface AI |
| Sessão e UI dominam | Dominam o protocolo e o Estado estruturado |
| A conversão depende do fluxo da página | A conversão depende do contexto e da qualidade dos dados |
| Humano leu todos os detalhes | O agente pode pré-filtrar as opções |É por isso que as antigas análises pagas por si só não são suficientes. Os comerciantes devem rastrear a descoberta, recomendação, transferência, conclusão do pagamento e correção pós-compra como uma única cadeia.

## Riscos e limites

Não trate nenhum protocolo como entrada automática. O ACP depende de:

- adoção de plataforma
- qualidade da integração comercial
- confiança do usuário
- informações corretas do produto
- políticas de pagamento que ainda fazem sentido quando um agente atua em nome de um comprador

Para produtos regulamentados ou compras de alto preço, a confirmação humana ainda pode ser necessária, mesmo que a superfície de pagamento se torne nativa do agente.

## Perguntas frequentes

### ACP é o mesmo que negociação com agente?

Não. A negociação de agentes é a mudança mais ampla no mercado. ACP é uma abordagem de protocolo para venda contextual de agentes de IA.

### O ACP substitui o UCP?

Não. O ACP concentra-se na experiência de pagamento, enquanto o UCP cobre um ciclo de vida empresarial mais amplo.

### Todos os comerciantes deveriam implementar o ACP agora?

Não automaticamente. Primeiro, confirme se as compras assistidas por IA são um canal significativo para sua categoria e se seu banco de dados está pronto.

### Qual é o melhor primeiro passo?

Corrija os dados do produto, o esquema do produto, a clareza da política e o determinismo do pagamento antes de adicionar novas superfícies de protocolo.

## Conclusão

O ACP é importante porque o pagamento está cada vez mais próximo da conversa. Os comerciantes que desejam vender por meio de plataformas de IA precisam de mais do que uma boa cópia: eles precisam de informações claras sobre os produtos, operações confiáveis ​​e fluxos de pagamento projetados para mediação automatizada.