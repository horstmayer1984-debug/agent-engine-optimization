---
title: "Árvores de decisão determinísticas: como os agentes de IA."
metaTitle: "Árvores de decisão para agentes de IA: guia de avaliação."
date: 2026-04-14
weight: 92
category: "Architecture"
description: "Os agentes de IA executam árvores de decisão rigorosas de aprovação/reprovação antes de fazer transações. Que perguntas determinísticas eles fazem, qual a causa."
metaDescription: "Descubra qué comprobaciones de aprobación/rechazo utilizan los agentes de IA antes de actuar, qué causa la exclusión y cómo hacer que su sitio web sea más."
summary: "Os agentes não navegam nem decidem intuitivamente. Eles executam árvores de decisão determinísticas com critérios rígidos de aprovação/reprovação. Uma verificação falha e o agente passa para um concorrente."
keywords:
  - "árvores de decisão do agente"
  - "avaliação determinística do agente"
  - "critérios de aprovação do agente"
  - "agentes de mapeamento de capacidade"
  - "critérios de exclusão de agente"
  - "avaliação máquina a máquina"
---
Os agentes de IA não avaliam o seu site como os humanos. Não navegam, não formam impressões e aos poucos vão construindo confiança. Eles executam árvores de decisão determinísticas com critérios rigorosos de aprovação/reprovação em cada nó. Se uma verificação falhar, o processo termina. Agente passa para o próximo provedor sem explicação.

Compreender essas árvores de decisão faz a diferença entre ser selecionado e ser excluído silenciosamente.

## As seis perguntas que todo agente faz

### Pergunta 1: O que este sistema pode fazer?

O agente busca um manifesto de capacidade. Nas implementações UCP, este é o arquivo JSON em /.well-known/ucp. Nas implementações MCP, eles são os esquemas de ferramentas e recursos retornados pelo servidor. Em configurações mais simples, é o arquivo llms.txt ou o Cartão do Agente.

Se o agente não conseguir determinar o que o seu sistema suporta, ele irá ignorá-lo completamente. Não há crédito parcial. As capacidades são declaradas ou não.

Condição de aprovação: uma declaração legível por máquina de ações, tipos de dados e recursos de transação suportados.

Condição de erro: sem manifesto, sem esquema, sem llms.txt. O agente não tem como determinar o que você oferece.

### Pergunta 2: Quais suprimentos são necessários?

Uma vez que o agente sabe o que pode fazer, ele verifica se possui os insumos necessários para acionar a ação. Seu sistema deve fornecer um esboço claro dos valores de entrada esperados: tipos de dados, campos obrigatórios versus campos opcionais, regras de validação e intervalos aceitáveis.

Condição de aprovação: cada endpoint ou ação possui um esquema de entrada documentado com tipos, restrições e exemplos.

Condição de erro: Os requisitos de entrada são vagos, não documentados ou só podem ser descobertos por tentativa e erro.

### Pergunta 3: O estado atual é verificável?

O agente não confia no conteúdo da página estática. Você precisa verificar o status crítico em tempo real.

O preço é explícito e atual? Frases humanas como “preço sob consulta” ou “a partir de” causam exclusão imediata em transações avessas ao risco. O agente precisa de um número exato válido por um período de tempo definido.

O inventário é verificado em tempo real? O agente envia uma chamada de API. O HTML em cache que diz “em estoque” não terá valor se o estoque real estiver esgotado há duas horas.

As políticas são estruturadas e legíveis por máquina? Políticas de devolução, termos de envio, condições de cancelamento. Se existirem apenas como parágrafos em prosa numa página jurídica, o agente não poderá analisá-los de forma confiável. São necessárias tags de ação e declarações de política estruturadas do Schema.org.

Condição de aprovação: status verificável em tempo real para cada parâmetro crítico da transação. Condição de falha: dados desatualizados, preços ambíguos, políticas não estruturadas ou qualquer parâmetro que exija interpretação em vez de análise.

### Pergunta 4: Qual estado é garantido após a ação?

O agente precisa de garantias determinísticas sobre o que acontecerá quando ele agir. Se você enviar uma compra, receberá uma confirmação com um ID do pedido? Se marcar uma consulta, receberá um horário confirmado? Se a ação falhar, você receberá um erro estruturado explicando o motivo?

Condição de aprovação: cada endpoint de ação retorna um resultado determinístico (sucesso com detalhes de commit ou falha com classificação de erro específica).

Condição de erro: respostas ambíguas, confirmações em linguagem humana sem dados estruturados ou endpoints retornando sucesso sem evidências verificáveis.

### Pergunta 5: Os atributos correspondem entre as fontes?Os agentes fazem referência cruzada de dados de diversas fontes. Se o seu preço no Google Merchant Center for diferente da resposta da API ou se a marcação do esquema mostrar uma disponibilidade diferente do manifesto UCP, o agente detectará a inconsistência.

Inconsistências não causam apenas confusão. Eles causam exclusão. Um agente que não pode confiar nos seus dados não fará transações através do seu sistema.

Condição de aprovação: Valores idênticos para preço, disponibilidade, especificações e políticas em todas as fontes legíveis por máquina (marcação de esquema, respostas de API, feeds de produtos, manifesto UCP).

Condição de falha: Qualquer discrepância entre fontes de dados.

### Pergunta 6: A ação pode ser repetida com segurança?

Os agentes tentam novamente em caso de erro. Se a rede expirar após a compra, o agente enviará a mesma solicitação novamente. Seu sistema deve lidar com isso sem criar pedidos duplicados, cobranças duplicadas ou status corrompidos.

Condição de aprovação: terminais de transação idempotentes onde a mesma solicitação produz o mesmo resultado, independentemente de quantas vezes for enviada.

Condição de erro: endpoints não idempotentes onde novas tentativas criam duplicatas.

## A árvore de decisão na prática

O agente avalia essas questões sequencialmente. Cada “falha” encerra a avaliação imediatamente:

Capacidade declarada? Não → excluído. Entradas documentadas? Não → excluído. Status verificável em tempo real? Não → excluído. Resultados determinísticos? Não → excluído. Dados consistentes entre fontes? Não → excluído. Novas tentativas seguras? Não → excluído.

Somente se todas as seis verificações forem aprovadas o agente continua com a transação.

## Por que isso difere da avaliação humana Um comprador humano tolera ambiguidade. "Preço sob consulta" significa que eles ligarão. "Normalmente é enviado em 3-5 dias" é próximo o suficiente. Você navega e aceita uma política de devolução confusa.

Um agente não tolera nada disso. Toda ambigüidade é uma condição de fracasso. Tudo “normalmente” é indeterminado. Qualquer política não estruturada é impossível de analisar. O agente opera com lógica binária: verificada ou excluída.

É por isso que sites que parecem sofisticados para os humanos podem pontuar zero com os agentes. O design visual, a reputação da marca e o texto persuasivo não têm peso em uma árvore de decisão determinística.

O [guia da camada de execução](/es/docs/execution-layer/) explica os requisitos de infraestrutura. O [guia de implementação AEO](/es/docs/implement-aeo/) cobre o caminho de otimização passo a passo.

---

## Perguntas frequentes

**O que é uma árvore de decisão determinística no AEO?**
Uma sequência estrita de verificações de aprovação/reprovação que um agente executa antes de realizar uma transação com seu site. Cada verificação avalia um requisito específico (capacidades, entradas, estado, resultados, consistência, idempotência). A falha em qualquer verificação causa exclusão imediata.

**Qual é o motivo mais comum pelo qual os agentes excluem um site?**
Preços não estruturados ou ambíguos. "Preço sob consulta", "a partir de" ou preços que diferem entre a marcação do esquema e as respostas da API causam uma exclusão imediata.

**Como faço para testar se meu site passa na avaliação do agente?**
Simule todas as seis perguntas manualmente. Você consegue encontrar sua declaração de capacidade? Todas as entradas estão documentadas? Você pode verificar o status usando uma chamada de API? Todas as fontes de dados retornam valores idênticos? Execute esta verificação mensalmente.**O que é um manifesto de capacidade?**
Um arquivo legível por máquina que declara o que seu sistema pode fazer. Em UCP: /.conhecido/ucp. No MCP: esquemas de ferramentas e recursos. Em configurações mais simples: llms.txt ou agent-card.json.

**Por que a idempotência é tão importante?**
Porque os agentes tentam novamente se falharem. Um tempo limite não significa que a ação falhou. Se o seu endpoint criar um pedido duplicado na nova tentativa, o agente causou danos reais. Endpoints idempotentes lidam com novas tentativas com segurança, retornando o mesmo resultado para a mesma solicitação.

## Guias relacionados

* [arquitetura de negociação do agente](/es/docs/agentic-commerce/)

## Referências primárias

* [Estrutura de gerenciamento de risco de IA do NIST](https://www.nist.gov/itl/ai-risk-management-framework)
* [Documentação do Schema.org](https://schema.org/docs/documents.html)