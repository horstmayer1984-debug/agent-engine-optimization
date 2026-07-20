---
title: "UCP, ACP e MCP: os três protocolos que irão promover."
metaTitle: "UCP vs ACP vs MCP: comparação de protocolos."
date: 2026-04-14
weight: 90
category: "Framework"
description: "O MCP fornece contexto, o UCP lida com os ciclos de vida do comércio, o ACP permite o checkout nativo do ChatGPT. Como os três protocolos diferem."
metaDescription: "Compare MCP, UCP y ACP en el intercambio de contexto, los ciclos de vida del comercio, el pago, el uso de herramientas y cuándo encaja cada protocolo."
summary: "Três protocolos dominarão a infraestrutura dos agentes em 2026. O MCP conecta os agentes aos dados. O UCP cuida de todo o ciclo de vida do comércio. ACP permite pagamento dentro do ChatGPT. Veja quando usar cada um."
keywords:
  - "UCP x ACP x MCP"
  - "protocolos de negociação de agentes"
  - "Protocolo de Negociação Universal"
  - "Protocolo de Negociação de Agente"
  - "Comparação de protocolo de contexto de modelo"
  - "pilha de protocolos do agente 2026"
---
Três protocolos dominam a camada de infraestrutura do Agent Engine Optimization em 2026. Cada um resolve um problema diferente. Escolher o errado desperdiça tempo de desenvolvimento. A escolha da combinação certa oferece aos agentes um caminho completo, desde o acesso aos dados até a conclusão da transação.

MCP (Model Context Protocol) conecta agentes aos seus dados. UCP (Protocolo de Comércio Universal) lida com todo o ciclo de vida do comércio. ACP (Agent Commerce Protocol) permite o pagamento direto dentro do ChatGPT sem que o comprador visite seu site.

## MCP: Dando aos agentes acesso aos seus dados e ferramentas

A Anthropic desenvolveu o MCP e o portou para a Linux Foundation. É um protocolo de integração vertical. Um servidor MCP expõe suas fontes de dados, documentos e ferramentas internas aos agentes de IA por meio de uma interface JSON-RPC padronizada.

O MCP responde a uma pergunta: o que este sistema pode me dizer e quais ferramentas posso usar? Ele permite que os agentes consultem seu CMS, recuperem documentos, verifiquem registros de banco de dados e chamem funções internas. Ela não administra pagamentos, fluxos de pagamentos ou transações comerciais por conta própria.

Use o MCP quando os agentes precisarem acessar os dados da sua empresa (catálogos de produtos, documentação, bases de conhecimento), quando você quiser que qualquer agente habilitado para MCP descubra e use suas ferramentas sem uma integração personalizada e quando a interação for de leitura ou consulta em vez de transacional.

A implementação técnica é um servidor JSON-RPC 2.0 que anuncia ferramentas (funções que os agentes podem chamar), recursos (dados que os agentes podem ler) e mensagens (modelos que os agentes podem usar). O [guia MCP vs API] (/docs/mcp-vs-api-for-agents/) cobre a implementação em detalhes.

## UCP: Gerencie todo o ciclo de vida do comércio

O Google desenvolveu o UCP em parceria com Shopify, Target, Walmart, Etsy e Wayfair. Foi lançado na NRF em janeiro de 2026. UCP é o protocolo para todo o ciclo de vida do comércio: verificação de estoque, negociação de preços, autorização de pagamento, envio de pedidos e rastreamento de atendimento.

A inovação técnica mais importante é a Declaração de Capacidade. Sua loja publica um arquivo de manifesto JSON em /.well-known/ucp que informa aos agentes exatamente quais transações, descontos, métodos de pagamento e políticas ela suporta. O agente lê este manifesto antes de tentar qualquer interação, para que você nunca precise adivinhar.

A UCP trabalha com o Agent Payments Protocol (AP2) para mandatos de pagamento criptográficos e trilhas de auditoria. Juntos, eles permitem que os agentes verifiquem o estoque, validem preços, autorizem pagamentos, enviem pedidos e acompanhem o atendimento por meio de um único fluxo padronizado. Use o UCP ao vender produtos ou serviços por meio de uma loja, quando desejar que agentes operando no Google AI Mode ou Gemini realizem transações com você e quando precisar de todo o ciclo de vida da compra, desde a descoberta até a confirmação do cumprimento.

O [artigo sobre Agent Trade Execution] (/docs/agentic-commerce-execution/) explica como o UCP funciona em arquiteturas de comércio eletrônico.

## ACP: pagamento dentro do ChatGPT

OpenAI desenvolveu ACP em parceria com Stripe. É um protocolo de código aberto projetado especificamente para minimizar o atrito ao lidar com o pagamento diretamente na interface ChatGPT.O mecanismo principal é SharedPaymentToken. As credenciais de pagamento do comprador são compartilhadas de forma segura com o comerciante, sem que o comprador saia do ChatGPT. O agente cuida da seleção do produto, o protocolo ACP cuida da troca segura de tokens de pagamento e a transação é concluída nativamente na conversa.

Use o ACP quando seu principal canal de vendas orientado por agente for o ChatGPT, quando você quiser fazer um pagamento sem redirecionamento (o comprador nunca visita seu site) e quando você usar o Stripe como processador de pagamentos (o ACP se integra nativamente à infraestrutura do Stripe).

## Como os três protocolos funcionam juntos

Os protocolos não são concorrentes. Diferentes camadas da mesma pilha servem.

O MCP fornece a camada de dados. Um agente usa o MCP para acessar seu catálogo de produtos, verificar especificações e recuperar documentação.

UCP fornece a camada de negócios. Assim que o agente tiver os dados necessários, o UCP trata da transação: reserva de estoque, validação de preço, autorização de pagamento e envio do pedido.

ACP fornece a camada de interface especificamente para ChatGPT. Envolve a experiência de pagamento na conversa ChatGPT usando tokens de pagamento seguros.

Uma infraestrutura completa pronta para agentes poderia usar todos os três: MCP para acesso a dados, UCP para ciclo de vida de negócios em fluxos de trabalho de agentes com tecnologia Google e ACP para transações ChatGPT nativas.

## Comparação de protocolo

| Aparência | PCM | PCU | ACP |
|
---|
---|
---|
---|
| Desenvolvedor | Anthropo (Fundação Linux) | Google com Shopify e parceiros | OpenAI com faixa |
| Objetivo principal | Acesso a dados e ferramentas | Ciclo de vida comercial completo | Pagamento no chat |
| Base técnica | JSON-RPC 2.0 | Declaração de capacidade mais AP2 | Token de pagamento compartilhado |
| Gestão de pagamentos | Nenhum pagamento nativo | Sim, através do AP2 | Sim, através do Stripe |
| Onde os agentes realizam transações | Qualquer ambiente compatível com MCP | Modo IA do Google, Gêmeos | Bate-papoGPT |
| Mecanismo de descoberta | Esquemas de ferramentas e recursos | /.manifesto conhecido/ucp | Registro de endpoint ACP || O melhor para | Consultas de dados, acesso a ferramentas | E-commerce, reservas, serviços | Vendas nativas ChatGPT |
| Esforço de implementação | 2 a 4 horas para servidor básico | 1 a 2 semanas para ciclo de vida completo | Dias, requer integração com Stripe |

## Estrutura de decisão estratégica

Se você deseja que os agentes acessem seus dados e ferramentas: implemente primeiro o MCP. É o mais rápido de implementar e atende a mais ampla gama de agentes.

Se você vende produtos ou serviços e deseja que os agentes do ecossistema do Google os comprem: adicione o UCP com uma declaração de capacidade em /.well-known/ucp.

Se ChatGPT é um canal de vendas importante para o seu negócio: adicione ACP com integração Stripe.

Se você deseja cobertura máxima: implemente todos os três. MCP para camada de dados, UCP para negociação do ecossistema Google, ACP para negociação ChatGPT. A lógica de negócios subjacente é compartilhada. Apenas as interfaces de protocolo diferem.

Os [artigos do protocolo x402] (/docs/x402-agent-payments/) cobrem a camada complementar de micropagamentos que funciona junto com todos os três protocolos.

---

## Perguntas frequentes

**Preciso dos três protocolos?**
Não. Comece com o MCP para acessar os dados. Adicione UCP ou ACP dependendo de quais plataformas de IA impulsionam suas vendas. A maioria das empresas começa com um protocolo de negociação e adiciona o segundo quando o canal assim o justifica.**O UCP e o ACP podem coexistir no mesmo local?**
Sim. Eles atendem a diferentes ecossistemas de agentes. A UCP lida com agentes fornecidos pelo Google. ACP lida com ChatGPT. Os mesmos dados de produto e lógica de negócios servem ambos através de diferentes interfaces de protocolo.

**O MCP é apenas para produtos técnicos?**
Não. Qualquer empresa com dados que os agentes precisam para acessar se beneficia do MCP. Um restaurante com cardápio, um hotel com disponibilidade de quartos, um consultor com descrições de serviços. O MCP torna qualquer informação estruturada acessível aos agentes.

**Qual protocolo foi mais adotado em abril de 2026?**
O MCP tem a adoção mais ampla (centenas de milhares de sites). UCP é o protocolo de negociação dominante com suporte de varejo significativo. ACP é mais recente, mas está crescendo rapidamente no ecossistema ChatGPT.

**O que é uma Declaração de Capacidade?**
Um manifesto JSON publicado em /.well-known/ucp que informa aos agentes exatamente o que sua loja oferece suporte: quais tipos de transação, métodos de pagamento, regras de desconto e políticas estão disponíveis. Os agentes o leem antes de tentar qualquer interação.

## Referências primárias

* [Especificação do protocolo de contexto do modelo](https://modelcontextprotocol.io/specification/2025-06-18/basic/index)
* [primitivas do servidor MCP](https://modelcontextprotocol.io/specification/2025-06-18/server/index)