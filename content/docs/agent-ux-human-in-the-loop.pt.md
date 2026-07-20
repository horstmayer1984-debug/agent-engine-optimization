---
title: "Agent UX e design Human-in-the-Loop: criação de interface."
metaTitle: "UX do agente e design Human-in-The-Loop."
date: 2026-04-12
weight: 86
category: "Guide"
description: "Projete a experiência do usuário do agente com aprovações claras, visualizações, reversibilidade e feedback de status para que as pessoas possam monitorar as ações."
metaDescription: "Diseñe interfaces para humanos y agentes de IA con HTML semántico, aprobaciones, comentarios estructurados, mensajes de estado y flujos de trabajo."
summary: "As interfaces modernas devem atender dois públicos simultaneamente: usuários humanos e agentes de IA. O design responsivo do agente usa HTML semântico, terminais estruturados e ciclos de feedback para satisfazer ambos."
keywords:
  - "design UX do agente"
  - "agentes humanos no circuito"
  - "design responsivo do agente"
  - "design de interface dupla"
  - "fluxos de trabalho de aprovação de agentes"
---
O design responsivo ao agente faz com que as interfaces funcionem para dois públicos simultaneamente: usuários humanos que navegam visualmente e agentes de IA que analisam estruturalmente. As melhores implementações não requerem interfaces separadas. Eles constroem um sistema que atende a ambos por meio de uma arquitetura limpa.

## O desafio do duplo público

A página de um produto deve persuadir um comprador humano com design visual, narrativa de marca e gatilhos emocionais. A mesma página deve informar um agente de IA com especificações estruturadas, preços precisos e disponibilidade explícita.

Não se trata de objectivos contraditórios, mas de objectivos diferentes. O erro é otimizar para um público e presumir que o outro está satisfeito.

Uma página com belas imagens e uma narrativa convincente, mas sem dados estruturados, atende ao ser humano e exclui os agentes. Uma página com endpoints JSON simples e sem design visual atende agentes e exclui humanos. O objetivo é uma página unificada que contenha ambas as camadas.

## HTML semântico como base

Os agentes ignoram o conteúdo renderizado em JavaScript na maioria dos casos. Eles analisam HTML bruto. Os elementos semânticos (hierarquia de cabeçalho, elementos de tabela, elementos de lista, elementos de formulário, elementos de botão) fornecem as informações estruturais de que os agentes precisam.

Use elementos HTML nativos em vez de divs estilizados. Um elemento de botão informa ao agente que existe uma ação clicável. Uma div projetada para se parecer com um botão não diz nada ao agente.

Adicione atributos aria-label quando a finalidade do elemento não for óbvia em seu conteúdo. Um agente que analisa sua página se beneficia das mesmas práticas de acessibilidade usadas pelos leitores de tela.

Processe todo o conteúdo crítico no servidor. Se o nome, o preço e a disponibilidade do seu produto exigirem a exibição de JavaScript, os agentes não poderão vê-los. O [Guia de programação do site do agente](/es/docs/programming-websites-for-ai-agents/) cobre os requisitos técnicos.

##Fluxos de aprovação humanos no circuito

Nem todas as ações do agente devem ser concluídas de forma autônoma. Fluxos de aprovação de projetos que param para confirmação humana em decisões de alto risco.

O fluxo de aprovação tem três componentes: o agente propõe uma ação (que é mostrada ao humano em termos claros e estruturados), o humano analisa e aprova ou rejeita, e o sistema executa ou cancela com base na decisão humana.

Para os endpoints do seu site, isso significa oferecer suporte a fluxos de trabalho assíncronos. Um agente envia uma solicitação de reserva. Seu sistema retorna um status pendente com um ID de tarefa. Avaliações humanas. Seu sistema atualiza o status para confirmado ou rejeitado. O agente pesquisa o ID da tarefa e recebe o status final. Esse padrão funciona para aprovações de compras acima de um limite de gastos, envios de documentos legais, modificações de contas e qualquer ação que se beneficie do julgamento humano.

## Interfaces de feedback estruturadas

Tanto humanos quanto agentes devem relatar problemas. Mas eles relatam de forma diferente.

Feedback humano: uma caixa de comentários, uma avaliação com estrelas, um ticket de suporte. Não estruturado, rico em contexto, requer interpretação.

Feedback do agente: um endpoint estruturado que aceita o URL de uma página, dados esperados, dados reais encontrados e classificação de erros. Nenhuma interpretação necessária.Construa ambos. O formulário de feedback humano na página visível. O endpoint de feedback do agente documentado em seu llms.txt e no cartão do agente. Ambos alimentam o mesmo processo de melhoria através de seus [ciclos de feedback](/es/docs/agent-feedback-loops/).

## Endpoints WebSocket para sessões ao vivo

APIs REST padrão funcionam para interações sem estado. Os fluxos de trabalho do agente em várias etapas se beneficiam das conexões WebSocket que mantêm o estado da sessão.

Um endpoint WebSocket em /ws/agent-session permite que um agente mantenha o contexto por meio de uma sequência de ações: navegar pelos produtos, restringir a seleção, verificar a disponibilidade da melhor opção e concluir uma compra. Cada etapa ocorre na mesma conexão com estado compartilhado.

Para o paralelo humano: a mesma lógica de sessão subjacente pode conduzir um fluxo de checkout guiado na UI do navegador, usando a mesma lógica de negócios por meio de uma interface diferente.

## Design para degradação elegante

Sua interface deve funcionar em todos os níveis de capacidade: experiência completa do navegador humano (JavaScript, CSS, imagens, interação), experiência reduzida do navegador (conexão lenta, sem JavaScript), experiência do agente (HTML simples, dados estruturados, endpoints) e experiência básica do agente (apenas conteúdo de texto HTML).

Cada camada atende um cliente diferente. Projete de forma que a remoção de uma camada não quebre as camadas abaixo dela. Se o seu JavaScript falhar, o HTML ainda deverá conter informações essenciais. Se seus endpoints não funcionarem, o HTML ainda deverá estar legível.

O [Guia de Implementação AEO](/es/docs/implement-aeo/) cobre a estrutura da camada de conteúdo.

---

## Perguntas frequentes

**O que é Design Responsivo do Agente?**
Uma abordagem de design de interface que atende usuários humanos e agentes de IA por meio de uma única arquitetura. O HTML semântico fornece a camada legível pelo agente. O design visual fornece a camada humana. Ambos compartilham os mesmos dados subjacentes.

**Preciso de interfaces separadas para agentes?**
Normalmente não. Uma página bem estruturada com HTML semântico, marcação de esquema e endpoints documentados atende a ambos os públicos. Interfaces separadas são relevantes apenas para fluxos de trabalho transacionais complexos.**Qual é o papel do ser humano no circuito do AEO?**
Fornece uma rede de segurança para ações de agentes de alto risco. O agente propõe, o humano aprova, o sistema executa. Isso gera confiança e evita erros dispendiosos em sistemas totalmente autônomos.

**Como os endpoints WebSocket ajudam os agentes?**
Eles mantêm o estado da sessão em fluxos de trabalho de várias etapas, evitando a perda de contexto entre chamadas REST sequenciais. Isto é particularmente útil para fluxos de compras e interações de serviços complexas.

**Devo priorizar a UX humana ou a UX do agente?**
Ambos. Se você for forçado a escolher um ponto de partida, Human UX com Semantic HTML oferece ambos os públicos. Endpoints específicos do agente (MCP, WebSocket) podem ser adicionados de forma incremental.

## Referências primárias

* [Estrutura de gerenciamento de risco de IA do NIST](https://www.nist.gov/itl/ai-risk-management-framework)
* [Documentação do Schema.org](https://schema.org/docs/documents.html)