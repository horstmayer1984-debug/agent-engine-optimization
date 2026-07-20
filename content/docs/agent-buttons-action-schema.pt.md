---
title: "Botões de agente, API e esquema de ação para AEO."
date: 2026-04-12
weight: 57
category: "Architecture"
description: "Saiba como os botões do agente, as APIs e o esquema de ação expõem as próximas etapas seguras a serem concluídas pelos agentes de IA."
summary: "Botões de agente, esquema de ação e endpoints de API transformam páginas de conteúdo estático em superfícies onde agentes de IA podem executar transações comerciais reais. Aqui está o guia de implementação completo."
keywords:
  - "implementação do botão do agente"
  - "Esquema de ação AEO"
  - "Esquema de ação potencial"
  - "API de transação do agente"
  - "Segurança do Terminal AEO"
---
Uma página de conteúdo que um agente possa ler é útil. Uma página de conteúdo através da qual um agente pode agir é útil. Botões de agente documentados, esquema de ação e endpoints de API são o que fazem a diferença. Eles transformam superfícies de publicação estáticas em interfaces transacionais onde sistemas autônomos podem verificar a disponibilidade, solicitar orçamentos, agendar compromissos e concluir compras.

## O que realmente são botões de agente?

Um botão de agente não é um botão visual projetado para cliques humanos. É um caminho de ação claramente documentado que informa a um agente: esta tarefa específica pode ser executada aqui, estas são as entradas necessárias e este é o terminal a ser chamado.

O botão visual na página atende ao visitante humano. O esquema subjacente e a documentação do endpoint atendem ao agente. Ambos visam o mesmo processo de negócios, mas por meio de interfaces diferentes.

## Implementando esquema de ação com PotentialAction

Schema.org fornece o tipo PotentialAction especificamente para descrever ações disponíveis em uma página. Use-o para informar aos agentes o que eles podem fazer.

Para uma página de serviço com reserva de compromisso, a estrutura do esquema inclui: o tipo de ação (ReserveAction ou ScheduleAction), o URL de destino (seu endpoint de reserva), as propriedades de entrada necessárias (data, hora, tipo de serviço, informações de contato) e o tipo de resultado (Reserva com número de confirmação).

Para uma página de produto comprável, use BuyAction com o URL de destino apontando para seu carrinho ou endpoint de checkout, insira propriedades para seleção de quantidade e variante e o tipo de resultado que descreve a confirmação do pedido.

Para uma solicitação de cotação, use QuoteAction (ou Ação genérica com um nome amigável) com o URL de destino apontando para o ponto final da sua cotação e propriedades de entrada para as especificações exigidas pela cotação.

O princípio fundamental: cada esquema de ação deve corresponder a um objetivo real e funcional. Não adicione esquemas de ação para capacidades que ainda não existem. Os agentes que tentarem uma ação e falharem perderão a prioridade no seu site.

## Construindo os endpoints da API

Os endpoints de ação não precisam ser APIs REST de nível empresarial desde o primeiro dia. Eles devem aceitar informações estruturadas, executar a ação comercial e retornar uma resposta estruturada.

Um endpoint mínimo aceita uma carga JSON com os campos obrigatórios, valida a entrada, aciona o processo de negócios (envia um email, cria um registro, chama uma API externa) e retorna uma resposta JSON com o status, o identificador de confirmação e as próximas etapas. Para equipes sem recursos de desenvolvimento de back-end, os endpoints de webhook n8n ou Make.com lidam bem com esse padrão. Crie um webhook que aceite JSON, adicione etapas de validação, conecte-se às suas ferramentas de negócios (calendário, CRM, e-mail) e retorne uma resposta estruturada.

Requisitos de segurança para pontos finais voltados para o agente: Valide todas as entradas com tipos e intervalos esperados. Solicitações de limite de taxa para evitar abusos. Exija autenticação para qualquer endpoint que modifique o estado. Registre todas as solicitações para fins de auditoria. Retorne mensagens de erro claras que ajudam os agentes a entender o que deu errado.

## Conectando botões a endpoints

Em cada página onde uma ação estiver disponível, inclua três coisas:Uma frase de chamariz visível para visitantes humanos (um botão ou link com texto simples, como “Verificar disponibilidade” ou “Solicitar um orçamento”).

Esquema de ação na marcação da página que descreve o terminal, as entradas e a saída esperada.

Documentação do endpoint (em linha ou vinculada) especificando o formato exato da solicitação, os cabeçalhos necessários e a estrutura da resposta.

Essa tripla camada garante que tanto humanos quanto agentes possam encontrar e utilizar a ação, por meio de suas respectivas interfaces.

## Melhores práticas de segurança

Nunca exponha endpoints graváveis sem autenticação. Mesmo endpoints de webhook simples devem exigir uma chave de API ou token no cabeçalho da solicitação.

Implemente validação de entrada que rejeite solicitações malformadas antes que elas cheguem à sua lógica de negócios. Um agente que envia um formato de data inválido deve receber um erro claro, não uma falha no sistema.

Use chaves idempotentes para qualquer ação que crie ou modifique o estado. Se a mesma solicitação chegar duas vezes (comum em novas tentativas do agente), a segunda solicitação deverá retornar o mesmo resultado sem criar uma reserva ou pedido duplicado.

Registre cada interação do agente. Carimbos de data e hora, cargas de solicitação, cargas de resposta e identificador do agente de origem. Isso é essencial para [loops de feedback](/es/docs/agent-feedback-loops/) que melhoram a precisão ao longo do tempo.

O [artigo do plano de controle universal](/es/docs/universal-control-plane/) abrange a arquitetura de governança completa para endpoints voltados para agentes.

##Testar transações do agente

Antes de entrar no ar, teste cada endpoint com estas verificações:

O endpoint pode ser descoberto por meio do esboço da ação na página? Analise a página como um agente faria e verifique se o esquema aponta para um URL funcional.

O terminal aceita o formato de entrada documentado e retorna o formato de saída documentado? Envie uma solicitação válida e verifique se a resposta corresponde à descrição do esquema. O endpoint lida corretamente com entradas inválidas? Envie solicitações malformadas e verifique se as respostas aos erros são estruturadas e informativas.

O endpoint lida com solicitações duplicadas com segurança? Envie a mesma solicitação válida duas vezes e verifique se nenhuma ação duplicada foi criada.

O endpoint está respondendo com uma latência aceitável? Os agentes normalmente expiram após 10 a 30 segundos. Seu endpoint deve responder bem nessa janela.

---

## Perguntas frequentes

**Os botões de agente substituem os botões de rosto humano?**
Não. Eles coexistem. O botão visual atende visitantes humanos. O esquema de ação e o ponto final servem aos agentes. Ambos acionam o mesmo processo de negócios.

**O que é PotentialAction em Schema.org?**
Um tipo de esboço que descreve uma ação disponível em uma página. Inclui o tipo de ação, URL de destino, entradas necessárias e resultado esperado. Os agentes o utilizam para descobrir o que podem fazer no seu site.

**Como posso proteger endpoints voltados para o agente?**
Exija autenticação (chaves de API ou tokens), valide todas as entradas, implemente limitação de taxa, use chaves idempotentes para ações de mudança de estado e registre todas as solicitações.**Posso usar ferramentas sem código para endpoints de agente?**
Sim. n8n e Make.com oferecem suporte a endpoints de webhook que aceitam JSON estruturado, executam lógica de negócios e retornam respostas estruturadas. Eles lidam com os padrões de transação mais básicos do agente.

**E se meu esboço de ação descrever um recurso que está temporariamente indisponível?**
Retorne uma resposta de erro clara e estruturada que explique a indisponibilidade e quando o serviço deverá ser retomado. Não deixe esquemas de ação quebrados em páginas onde o recurso não existe mais.

## Guias relacionados

* [Protocolos de Agente AI](/es/docs/protocols/)

## Referências primárias

* [Diretrizes de dados estruturados do Google](https://developers.google.com/search/docs/appearance/structured-data/sd-policies)
* [Documentação do Schema.org](https://schema.org/docs/documents.html)