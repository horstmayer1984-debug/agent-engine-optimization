---
title: "AP2 vs x402: camada de autorização versus camada de liquidação."
date: 2026-05-08
weight: 120
category: "Architecture"
description: "Comparação de AP2 e x402 para pagamentos de agentes de IA: mandatos, confiança, autorização, liquidação HTTP 402, stablecoins e pilhas híbridas."
summary: "Uma comparação entre o AP2 e o x402 do Google, explicando por que o AP2 é uma camada de confiança, enquanto o x402 é uma camada de liquidação de pagamentos."
keywords:
  - "AP2 versus x402"
  - "Protocolo de pagamento do agente"
  - "protocolo de pagamento x402"
  - "Autorização do agente de IA"
---
#AP2 vs x402: Camada de Autorização vs Camada de Liquidação de Pagamento

AP2 e x402 são mais complementares que substitutos diretos. AP2 responde se um agente foi autorizado a efetuar um pagamento. O x402 responde como um recurso HTTP protegido pode solicitar e verificar o pagamento. Uma pilha de negociação de agentes séria pode precisar de ambos.

A confusão vem da palavra “pagamento”. AP2 trata de permissão, teste e responsabilidade. x402 trata de liquidação e acesso.

## A versão curta

| Critério | AP2 | x402 |
|
---|
---|
---|
| Função principal | Demonstra autorização e intenção do usuário | Solicitar e verificar pagamento via HTTP |
| Artefato principal | Comandos e prova criptográfica | Solicitação de pagamento HTTP 402 e comprovante de pagamento |
| Melhor ajuste | Pagamento de agente, comércio delegado, auditabilidade | APIs pagas, ferramentas MCP, acesso a dados, microtransações |
| Pagar ferrovia | Método de pagamento independente | Freqüentemente baseado em stablecoins, expandindo-se por meio do suporte ao ecossistema |
| Risco principal abordado | Este agente foi autorizado a comprar isso? | Este recurso foi pago? |

## Para que o AP2 foi projetado

O Google introduziu o AP2 para tornar os pagamentos dos agentes mais seguros em todas as plataformas. A questão central não é apenas a execução dos pagamentos. É autorização.

Um comerciante, emissor ou processador de pagamentos precisa de evidências de que um ser humano deu autoridade a um agente para agir. A evidência também deve corresponder ao carro final. Se o usuário encomendou tênis de corrida abaixo de US$ 120, o agente não deveria comprar discretamente uma jaqueta de US$ 230.

AP2 aborda isso através de conceitos de mandato. O protocolo registra a intenção do usuário e o contexto do pagamento de uma forma que pode ser verificada posteriormente. A última atualização AP2 do Google também introduziu soluções para transações autônomas onde o humano pode não estar presente no exato momento do pagamento, dependendo de autorização prévia.

Essa é uma camada de confiança.

## Para que o x402 foi projetado

O x402 resolve um problema mais concreto e muito prático: como um servidor pode solicitar pagamento antes de conceder acesso a um recurso?

Um cliente solicita um recurso. O servidor responde com HTTP 402 Pagamento obrigatório e detalhes de pagamento. O cliente paga ou anexa o comprovante de pagamento. O servidor verifica e retorna o recurso.

Esse padrão é especialmente útil para agentes porque pequenas transações automatizadas são complicadas em sistemas de pagamento tradicionais. Um agente não deve criar uma conta e negociar uma assinatura apenas para adquirir uma resposta de API.

## Por que AP2 e x402 podem ser combinados

Em uma pilha híbrida, o AP2 pode demonstrar autorização enquanto o x402 cuida da liquidação.

Fluxo de exemplo:

1. Um usuário autoriza um agente a adquirir dados de mercado premium até um orçamento definido.2. AP2 captura a intenção do usuário e os limites de autorização.
3. O agente chama um terminal de dados protegido.
4. O endpoint retorna uma exigência de pagamento x402.
5. O agente liquida através do x402 dentro dos limites autorizados.
6. O comerciante ou serviço retém o comprovante da autorização e do pagamento.

Essa pilha é mais forte do que qualquer uma das camadas sozinha.

## Onde AP2 é mais forte

AP2 é mais forte quando a transação apresenta riscos legais, de conformidade, de fraude ou de responsabilidade.

Bons casos de uso para AP2 incluem:1. Compras no varejo feitas por um assistente
2. Aquisição baseada em agente
3. Reserva de viagens
4. Serviço de apólice de seguro
5. Compras de alto valor com restrições previamente autorizadas
6. Pagamentos de agente para agente quando a responsabilidade é importante

## Onde x402 é mais forte

O x402 é mais forte quando a transação é pequena, digital e diretamente ligada ao acesso aos recursos.

Bons casos de uso para x402 incluem:

1. Chamadas de API pagas
2. Invocação da ferramenta MCP
3. Conteúdo web premium para agentes
4. Pacotes de dados
5. Inferência por solicitação
6. Arquivos de pesquisa legíveis por máquina

## Implicações do AEO

As equipas AEO devem apresentar os requisitos de pagamento e autorização num formato legível por máquina.

Para cada ação a pagar, documente:

1. Se a ação requer autorização do usuário
2. Se é permitida a execução autónoma
3. Quais protocolos de pagamento são suportados?
4. Se o pagamento for aceito x402
5. Que mandato ou prova de credencial é necessária?
6. Como são tratados erros e reembolsos
7. Como um agente verifica a conclusão

Esta documentação deve estar vinculada ao [llms.txt](/llms.txt), ao [centro de protocolo](/es/docs/protocols/) e às páginas de ação relevantes.

## Perguntas frequentes

**O AP2 é melhor que o x402?**
AP2 é melhor para autorização e responsabilidade. x402 é melhor para liquidação direta de pagamentos HTTP. Eles resolvem diferentes camadas.

**O AP2 usa x402?**
AP2 é independente de método de pagamento e pode funcionar com diferentes trilhos. O x402 pode ser usado como mecanismo de liquidação em fluxos compatíveis com AP2.

**Os provedores de API devem implementar o AP2?**
A maioria dos provedores de API deve considerar primeiro o x402 ou o MPP. AP2 torna-se mais importante quando a ação da API tem autoridade delegada, alto risco ou mandato de compra.

**Os comerciantes de comércio eletrônico devem implementar o x402?**
Não como primeiro protocolo na maioria dos casos. Os comerciantes de comércio eletrônico normalmente precisam de camadas de negociação e autorização antes da liquidação bruta por solicitação.

## Fontes

Referências principais: [anúncio do Google Cloud AP2](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol/), [atualização da Google AP2 FIDO Alliance](https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/), [documentação x402](https://docs.x402.org/faq) e [anúncio da x402 Linux Foundation](https://www.linuxfoundation.org/press/linux-foundation-is-launching-the-x402-foundation-and-welcoming-the-contribution-of-the-x402-protocol).

## Guias relacionados* [arquitetura de comércio de agente](/es/docs/agentic-commerce/)
* [protocolos de pagamento do agente](/es/docs/agent-payment-protocols-compared/)