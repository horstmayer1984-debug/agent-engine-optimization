---
title: "Como implementar x402 em seu site ou API de pagamento."
metaTitle: "Implementação de pagamentos de agentes x402."
date: 2026-04-12
weight: 71
category: "Architecture"
description: "Guia passo a passo para adicionar middleware de pagamento x402 ao seu site ou API. Abrange formato de resposta 402, validação de pagamento, integração com llms.txt."
metaDescription: "Agregue middleware de pago x402 con respuestas 402, validación, integración de llms.txt y tarjetas de agente para pagos de agentes de IA."
summary: "O x402 torna sua API monetizável instantaneamente pelo agente. Quando um agente solicita conteúdo ou computação, seu servidor retorna 402, o agente paga com USDC e recebe acesso. Aqui está o guia de implementação."
keywords:
  - "implementar x402"
  - "intermediário x402"
  - "Implementação HTTP 402"
  - "API de pagamento do agente"
  - "guia do desenvolvedor x402"
  - "API de micropagamentos USDC"
---
A implementação do x402 torna seu site ou API monetizável instantaneamente pelos agentes. Quando um agente de IA solicita conteúdo ou computação, seu servidor retorna HTTP 402 com condições de pagamento estruturadas. O agente paga com USDC. O acesso é concedido. Tudo em uma viagem de ida e volta HTTP sem estado.

## Implementação em cinco etapas

### Etapa 1: Adicionar middleware que verifica o pagamento

Insira o middleware antes dos seus endpoints protegidos. Verifica o cabeçalho X-PAYMENT nas solicitações recebidas. Se o cabeçalho estiver presente e for válido, a solicitação continua. Se estiver faltando ou for insuficiente, o middleware retornará uma resposta 402.

Este middleware fica entre o seu servidor web e a sua lógica de negócios. Isso não altera o funcionamento interno dos seus endpoints.

### Etapa 2: Estruture a resposta 402

Quando o pagamento está faltando, ele retorna um código de status 402 com um corpo JSON contendo: preço (o valor necessário), moeda (USDC), cadeia (a blockchain a ser paga, Base é o padrão), beneficiário (endereço de sua carteira), descrição (a que o pagamento concede acesso) e expiração (por quanto tempo as condições de pagamento permanecem válidas).

A resposta estruturada é o que permite aos agentes fazer pagamentos automáticos. Um simples 402 sem esse corpo JSON não dá ao agente nada com que trabalhar.

### Passo 3: Validar pagamentos recebidos

Quando um agente tentar novamente com um cabeçalho X-PAYMENT, valide o pagamento na rede. Use o SDK da Coinbase Developer Platform ou uma chamada RPC direta para verificar se o pagamento foi feito no endereço correto pelo valor correto na cadeia correta.

A validação deve ser concluída dentro do ciclo de vida da solicitação. Não faça o agente esperar por um fluxo de confirmação separado.

### Etapa 4: Conceda acesso e registre a transação

Assim que o pagamento for validado, processe a solicitação original normalmente e retorne a resposta. Registre a transação: ID do agente, valor pago, endpoint acessado, resposta retornada, carimbo de data/hora.

Esses registros alimentam seus [loops de feedback](/es/docs/agent-feedback-loops/) e análise de receita.

### Etapa 5 – Publique seus endpoints x402 em arquivos de descoberta

Adicione seus terminais pagos ao seu llms.txt com informações de preços. Inclua-os em sua lista de recursos agent-card.json com o requisito de pagamento anotado. Se você tiver um servidor MCP, adicione um campo payment_required às descrições da ferramenta relevante.

Isso garante que os agentes descubram não apenas o que seu site pode fazer, mas também quanto custa usar cada recurso.

## Combinando x402 com pagamentos com cartão

Nevermined Agent Card Payments (lançado em 9 de abril de 2026) permite que os agentes paguem com autoridade delegada da Visa ou Mastercard enquanto os comerciantes recebem a liquidação por meio de processadores de pagamento padrão como Stripe ou Adyen. Essa abordagem híbrida permite aceitar micropagamentos criptográficos (para agentes com carteiras) e pagamentos com cartão tradicionais (para agentes com autoridade de cartão delegada) por meio do mesmo endpoint.

##Comparação: monetização de API tradicional versus x402

| Método | Tempo de configuração | Fricção do Agente | Modelo de receita | Pagamento mínimo viável |
|
---|
---|
---|
---|
---|
| Chaves de API com assinaturas | Dias | Parar (criação de conta) | Parcelas mensais | Dólares por mês |
| x402 | Horas | Zero | Pagamento por solicitação | Frações de centavo |

## Erros comunsRetornando um 402 simples sem o corpo JSON estruturado. Os agentes não podem efetuar pagamentos automáticos se não receberem condições de pagamento estruturadas. Sempre inclua a especificação JSON completa.

Não publique endpoints x402 em arquivos de descoberta. Se os agentes não souberem que um terminal exige pagamento antes de ligar para ele, a resposta 402 parecerá um erro e não uma oportunidade de transação.

Definir preços muito altos para casos de uso de micropagamento. O poder do x402 permite pagamentos que antes eram muito pequenos para serem processados. Uma consulta de dados que custa US$ 5 receberá menos chamadas de agente do que uma que custa US$ 0,01 e aumenta em volume.

A [visão geral do x402](/es/docs/x402-agent-payments/) explica o contexto estratégico. A [Lista de verificação de aplicativos Web prontos para agente](/es/docs/agent-ready-web-apps/) abrange a configuração mais ampla para desenvolvedores.

---

## Perguntas frequentes

**Quanto tempo leva a implementação do x402?**
O middleware básico para um único endpoint leva de 1 a 2 horas. Adicionar validação de pagamento e registro adiciona mais 2 a 4 horas. A integração total com llms.txt e cartões de agente leva um dia.

**Quais linguagens de programação têm middleware x402 disponível?**
Node.js, Python, Go e Cloudflare Workers possuem middleware pré-construído. O protocolo é simples o suficiente para ser implementado em qualquer linguagem que possa retornar respostas HTTP e fazer chamadas RPC.

**Preciso de uma carteira criptografada?**
Sim, para receber pagamentos. Uma simples carteira USDC no Base é suficiente. Você pode converter USDC recebido em moeda fiduciária por meio de qualquer bolsa ou processador de pagamento que suporte liquidação de moeda estável.

**Posso definir preços diferentes para endpoints diferentes?**
Sim. Cada endpoint pode retornar sua própria resposta 402 com preços diferentes. Uma consulta de dados simples pode custar US$ 0,001, enquanto um cálculo complexo custa US$ 1.

**O que acontece se um agente não suportar x402?**
O agente recebe uma resposta 402 que não pode processar e continua. Você pode oferecer métodos de acesso alternativos (chaves de API, assinaturas) para clientes não x402, mantendo o x402 como principal forma de pagamento do agente.

---*Este artigo discute protocolos de pagamento e infraestrutura de criptomoeda apenas para fins educacionais e informativos. Não constitui aconselhamento financeiro. Consulte nosso [Aviso Legal](/es/docs/disclaimer/) para obter os termos completos.*

## Referências primárias

* [Documentação Coinbase x402](https://docs.cdp.coinbase.com/x402/welcome)
* [repositório de especificações x402](https://github.com/x402-foundation/x402)