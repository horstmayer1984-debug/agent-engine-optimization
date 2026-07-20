---
title: "A camada de execução: onde atuam os agentes de IA."
description: "Descubra o que é a camada de execução, por que os agentes de IA precisam dela e como os sites expõem ações, dados em tempo real e verificação."
summary: "Um guia para a camada de execução: a infraestrutura que permite que agentes autônomos de IA atuem por meio de APIs, ferramentas, dados e terminais de transação."
keywords:
  - "camada de execução"
  - "Otimização do mecanismo do agente"
  - "ações do agente"
  - "infraestrutura pronta para agente"
date: 2026-03-09
weight: 3
category: "Architecture"
---
Quando um sistema de IA cita seu conteúdo em uma resposta gerada, essa é a camada de leitura em ação. Útil, mas passivo.

Quando um agente de IA usa sua API para verificar o inventário em tempo real, compará-lo com as restrições orçamentárias de um usuário e concluir uma compra, essa é a camada de execução. Ativo, transacional e fundamentalmente diferente no que exige da sua infraestrutura.

A camada de execução é onde o AEO se separa de tudo o que veio antes. Não é um problema de otimização de conteúdo. É um **problema de arquitetura de infraestrutura**.

---

## Quais agentes precisam agir

Um agente freelancer que desempenhe uma tarefa (reservar um quarto de hotel inferior a 150 euros em Barcelona para a próxima terça-feira) necessita de:

### 1. Descoberta

Encontre serviços que correspondam ao tipo de tarefa. Isto é parcialmente um problema da camada de leitura. Dados estruturados, marcação de esquema e indexação adequada ajudam os agentes a descobrir seu serviço. Mas a descoberta por si só não permite a acção.

### 2. Compreender a capacidade

Saiba o que seu serviço pode fazer e sob quais limitações. O agente precisa de uma descrição legível por máquina de suas capacidades: quais ações estão disponíveis, quais parâmetros eles aceitam, quais resultados retornam, quais restrições se aplicam. Isto é o que os manifestos de capacidade e as descrições das ferramentas MCP fornecem.

### 3. Acesso a dados em tempo real

Obtenha preços, disponibilidade e condições atuais. Páginas HTML estáticas com preços de ontem não funcionam. O agente precisa de um endpoint que retorne dados atuais e estruturados que possam ser avaliados programaticamente.

### 4. Correspondência de restrições

Avalie se sua oferta atende aos requisitos do usuário. Orçamento inferior a 150 euros? Disponível terça-feira? Em Barcelona? Inclui café da manhã? O agente deve comparar essas restrições com seus dados. Isso requer dados estruturados e determinísticos, não textos de marketing.

### 5. Execução de ações

Ative a reserva, compra ou solicitação. O agente precisa de um terminal de transação. É aqui que entram protocolos como UCP (para negociação) e MCP (para acesso geral a ferramentas).

### 6. Verificação de status

Confirme se a ação foi bem-sucedida. A reserva foi feita? O agente precisa de transições de estado observáveis: disponível, reservado, confirmado. Sem verificação, o agente não pode reportar de forma confiável.

---

## Blocos de construção

### Esquemas de ação

Schema.org define tipos de ação como BuyAction, ReserveAction, OrderAction. Eles informam aos agentes quais ações são possíveis em uma página ou por meio de um serviço. A maioria dos sites usa Schema.org apenas para marcação informativa. Estendê-lo para marcação em nível de ação é uma primeira etapa que não requer APIs de back-end.

### Manifestos de capacidadeUm documento legível por máquina que descreve o que um serviço pode fazer, quais protocolos ele suporta e como interagir com ele. Pense nisso como um arquivo robots.txt para as capacidades do agente, só que em vez de dizer o que pode rastrear, diz o que pode fazer.

### Entradas e saídas determinísticas

As páginas de marketing são projetadas para a persuasão humana. Os dados voltados para o agente devem ser projetados para a tomada de decisões por máquina: parâmetros fixos, formatos de resposta estruturados, valores inequívocos, códigos de erro legíveis por máquina.

O que diz o site:

> "Nosso plano premium começa em apenas US$ 49 por mês com todos os recursos que sua equipe precisa."

O que o agente precisa:

```json
{
  "plan": "premium",
  "price": { "amount": 49, "currency": "USD", "interval": "month" },
  "features": ["feature_a", "feature_b", "feature_c"],
  "limits": { "users": 50, "storage_gb": 100 },
  "trial": { "available": true, "days": 14 }
}
```

### Compatibilidade de protocolo**MCP (Model Context Protocol)**: permite que modelos de IA acessem ferramentas e dados externos por meio de uma interface padronizada. Um comerciante com um servidor MCP permite que qualquer agente habilitado para MCP consulte seu catálogo sem uma integração personalizada.

**UCP (Protocolo de Comércio Universal)** – Padroniza todo o processo de compra para que qualquer agente possa realizar transações com qualquer comerciante usando o mesmo protocolo.

**A2A (Agente para Agente)**: permite que os agentes deleguem tarefas a agentes especializados.

As organizações que implementam esses protocolos antecipadamente tornam-se as opções padrão para a conclusão de tarefas do agente.

### Transições de estado

Os agentes precisam verificar se as ações produzem os resultados esperados. Isso requer transições de estado observáveis:

`disponível > reservado > pagamento_pendente > confirmado > cumprido`

Cada transição deve ser consultável. Sem isso, os agentes não poderão gerenciar fluxos de trabalho de várias etapas de maneira confiável.

### Confiança e verificação

Um agente que reserva uma viagem de 2.000 euros deve confiar na fonte. Os sinais de confiança para os agentes são diferentes dos sinais de confiança para os humanos. Os agentes precisam de identidades comerciais verificáveis, recibos de transações assinados criptograficamente (AP2), dados consistentes e precisos em todos os pontos de contato, documentação de restrições transparente e trilhas de auditoria.

---

## O que isso significa para sua organização

A camada de execução não é algo construído da noite para o dia. É uma capacidade que se desenvolve de forma incremental:

**Fase 1 (agora):** Audite a preparação atual do seu agente. Avalie dados estruturados, cobertura de esquema, estrutura de conteúdo e presença de API existente.

**Fase 2 (3 a 6 meses):** Implemente otimizações da camada de leitura e comece a planejar a infraestrutura da camada de execução. Adicione esquemas de ação, crie documentação de recursos, avalie a compatibilidade de protocolos.

**Fase 3 (6 a 18 meses):** Desenvolver recursos da camada de execução. Exponha APIs, implemente suporte a protocolos, crie endpoints de dados voltados para agentes, desenvolva mecanismos de verificação de integridade.[Auditoria de prontidão AEO](/es/docs/audit/) – Comece com uma avaliação sistemática.

[O que é AEO?](/es/docs/what-is-aeo/): Definição completa e escopo.

## Perguntas frequentes

### A camada de tempo de execução substitui o frontend do site?

Não. As interfaces humanas ainda são importantes. A camada de execução adiciona caminhos estruturados que o software pode usar sem ter que adivinhar como funciona uma interface visual.

### O que torna uma ação segura para os agentes?

A ação precisa de entradas explícitas, validação, autorização, estados estáveis, tentativas limitadas, erros claros e um resultado verificável.

### As equipes devem expor todas as ações internas?

Não. Exponha apenas ações com benefício de usuário, modelo de permissão, proprietário, log de auditoria e processo de failover definidos.

## Guias relacionados

* [arquitetura de negociação do agente](/es/docs/agentic-commerce/)

## Referências primárias

* [Estrutura de gerenciamento de risco de IA do NIST](https://www.nist.gov/itl/ai-risk-management-framework)
* [Documentação do Schema.org](https://schema.org/docs/documents.html)