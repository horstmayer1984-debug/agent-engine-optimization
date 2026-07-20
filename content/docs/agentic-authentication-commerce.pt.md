---
title: "Autenticação de agentes para comércio: FIDO, AP2 e intenção."
metaTitle: "Autenticação Agentic para Comércio."
date: 2026-05-25
weight: 152
category: "Architecture"
description: "Descubra como a autenticação de agente está surgindo para o comércio, como FIDO, AP2 e Verifiable Intent oferecem suporte à compra delegada e o que deveriam."
summary: "Um guia para autenticação de agentes no comércio, abrangendo grupos de trabalho FIDO, mandatos AP2, intenção verificável da Mastercard, identidade, privacidade e confiança do comerciante."
keywords:
  - "comércio de autenticação de agente"
  - "Autenticação do agente FIDO"
  - "Intenção verificável"
  - "Pagamentos de Agente AP2"
  - "negociação de identidade de agente"
---
# Autenticação Agentic para Comércio

A autenticação do agente é a camada de confiança que demonstra que um usuário autorizou um agente de IA a agir. É importante porque o comércio movimenta dinheiro real, estoque, fidelidade e responsabilidade. O trabalho de autenticação de agente AP2, Verifiable Intent e FIDO converge em torno de uma necessidade central: tornar a intenção delegada explícita, verificável, privada e auditável.

## Por que o login normal não é suficiente

O pagamento tradicional pressupõe a presença do ser humano. Eles fazem login, clicam em comprar, autenticam e pagam. A negociação de agentes muda isso. O agente pode pesquisar, criar um carrinho e executá-lo dentro das regras do usuário.

Isso levanta novas questões:

-Quem autorizou o agente?
- O que exatamente o agente foi autorizado a fazer?
- O usuário estava presente ou não?
- O comerciante recebeu a mesma intenção que o usuário deu?
- Que provas existem se a transação for contestada?

A [documentação AP2](https://ap2-protocol.org/) enquadra isso como uma necessidade de intenção verificável e trilhas de auditoria.

## O que a FIDO está fazendo

A FIDO Alliance anunciou trabalho em interações e comércio confiáveis de agentes de IA. Inclui um grupo de trabalho técnico de autenticação de agente focado em como os usuários podem delegar ações a agentes de IA com autenticação forte, privacidade e segurança.

O Google também anunciou que doará o AP2 para a FIDO e que a estrutura de intenção verificável da Mastercard contribuirá para o mesmo caminho de padrões.

Para os comerciantes, o sinal é claro: a identidade do agente e a autenticação delegada estão se tornando uma infraestrutura comercial.

## AP2 vs Intenção Verificável vs FIDO

| Camada | Função |
|
---|
---|
| AP2 | Protocolo de autorização de pagamento com pagamento e mandatos de pagamento |
| Intenção verificável | Camada de confiança que vincula identidade, intenção e ação em um registro que preserva a privacidade |
| FIDO | Organismo de padronização para trabalho de autenticação e interação com agentes |
| Sistemas de negociação | Aplicar políticas, pagamentos, conformidade e decisões de suporte |

Isso se conecta a [AP2 vs x402](/es/docs/ap2-vs-x402/) e [Visa TAP vs Mastercard Agent Pay](/es/docs/visa-tap-mastercard-agent-pay/).

## Implicações da implementação do comerciante

Os comerciantes devem se preparar para armazenar e validar:

- identidade do agente ou status do agente verificado
- status de autorização do usuário
- escopo da intenção
- referência do carrinho
- referência do mandato de pagamento
- decisão política
- eventos de auditoria com carimbo de data/hora
- status de revogação e cancelamento

Este não é apenas um recurso pago. Afeta suporte, fraude, reembolsos, fidelidade e conformidade.

## Tabela de preparação de autenticação

| Pergunta do comerciante | Por que é importante |
|
---|
---|
| Podemos distinguir uma sessão humana de uma sessão de agente? | A política e o risco diferem || Podemos verificar quem autorizou o agente? | A compra delegada necessita de prova |
| Podemos ver o alcance da intenção? | Os agentes devem permanecer dentro das limitações |
| Podemos armazenar evidências de auditoria? | As disputas precisam de fatos |
| Os usuários podem revogar a autoridade do agente? | O controle deve permanecer com o usuário |

A página [evidência de disputas comerciais entre agentes](/es/docs/agentic-commerce-dispute-evidence/) se aprofunda na camada de auditoria.

## Perguntas frequentes

### A autenticação do agente é igual à autenticação de pagamento?Não. A autenticação de pagamento verifica uma ação de pagamento. A autenticação do agente também precisa verificar a delegação, o escopo, a identidade do agente e a intenção do usuário.

### Por que o FIDO é importante?

A FIDO tem experiência na criação de padrões de autenticação abertos. Seus novos grupos de trabalho podem ajudar o comércio de agentes a evitar sistemas de confiança proprietários fragmentados.

### Isso está pronto para todos os traders?

Ainda não. A maioria dos comerciantes deve primeiro preparar os dados do produto, as políticas e a observabilidade do checkout enquanto monitoram o AP2, a intenção verificável e a adoção do FIDO.

### Como isso afeta o AEO?

Os agentes precisam de caminhos de execução confiáveis. A autenticação é uma das portas entre o conteúdo legível e a ação segura.

## Fontes

Principais fontes: [FIDO em interações confiáveis com agentes de IA](https://fidoalliance.org/fido-alliance-to-develop-standards-for-trusted-ai-agent-interactions/), [Doação do Google AP2 para FIDO](https://blog.google/products-and-platforms/platforms/google-pay/agent-payments-protocol-fido-alliance/), [Documentação AP2](https://ap2-protocol.org/) e [Intenção verificável da Mastercard](https://www.mastercard.com/europe/en/news-and-trends/stories/2026/verifiable-intent.html).