---
title: "Google ADK 2.0 e fluxos de trabalho de agentes determinísticos."
metaTitle: "Fluxos de trabalho do agente determinístico do Google ADK 2.0."
date: 2026-07-02
weight: 194
category: "Architecture"
description: "O Google ADK 2.0 enfatiza fluxos de trabalho determinísticos para agentes confiáveis. Saiba o que isso significa para o AEO, caminhos de execução e aprovações."
summary: "Um guia AEO para o Google ADK 2.0, fluxos de trabalho determinísticos, orquestração baseada em gráficos, controles humanos no circuito e ações de agentes confiáveis."
keywords:
  - "Google ADK 2.0"
  - "fluxos de trabalho de agentes determinísticos"
  - "kit de desenvolvimento de agente"
  - "orquestração de agentes"
  - "Camada de Execução AEO"
---
# Google ADK 2.0 e fluxos de trabalho de agentes determinísticos

O Google ADK 2.0 é importante para o AEO porque direciona o design do agente para fluxos de trabalho determinísticos onde o caminho é conhecido, observável e recuperável. É exatamente disso que os sites precisam quando os agentes passam da leitura de páginas à conclusão de reservas, compras, solicitações de suporte e processos de negócios.

## O que o Google anunciou

O Google publicou [Por que construímos o ADK 2.0](https://developers.googleblog.com/why-we-built-adk-20/) em 1º de julho de 2026. O argumento central é simples: grandes modelos de linguagem são úteis para o raciocínio, mas os agentes de produção também precisam de execução determinística quando o fluxo de trabalho é claro.

O Google também anunciou o [ADK Go 2.0](https://developers.googleblog.com/announcing-adk-go-20/) com um mecanismo de fluxo de trabalho baseado em gráfico, suporte humano integrado, orquestração dinâmica, novas tentativas, estado e comportamento de retomada.

## Por que os fluxos de trabalho determinísticos são importantes

Muitas tarefas web não devem ser improvisadas. Um reembolso, pagamento, solicitação de cotação, reclamação de seguro ou escalonamento de suporte precisam de um caminho previsível.

| Comportamento do Agente | Bom para | Risco |
|
---|
---|
---|
| Raciocínio de forma livre | Pesquisa, comparação, resumo | Caminho de execução pouco claro |
| Chamada de ferramenta | Obtendo dados ou executando uma etapa | Uso indevido de ferramentas sem limitações |
| Fluxo de trabalho determinístico | Processos de várias etapas conhecidos | Requer modelagem inicial |
| Fluxo de trabalho humano em constante evolução | Ações arriscadas ou irreversíveis | Mais lento, mas mais seguro |

A [Camada de Execução](/es/docs/execution-layer/) deve favorecer caminhos determinísticos para ações comerciais importantes.

## Impacto do AEO para sites

O ADK 2.0 reforça uma regra prática: não faça os agentes adivinharem seu fluxo de trabalho a partir de botões e textos de marketing. Publique o fluxo de trabalho.

Isso significa definir:

- estados de tarefa permitidos
- ingressos necessários
- regras de validação
- portões de aprovação
- tentar novamente a lógica
- rotas de cancelamento
- mensagens finais de confirmação
- registros de auditoria

Isso se conecta a [Agent UX e Human-in-the-Loop Design](/es/docs/agent-ux-human-in-the-loop/), [Multi-Agent AEO](/es/docs/multi-agent-aeo/) e [Aplicativos Web prontos para agente](/es/docs/agent-ready-web-apps/).

## Exemplo: agendamento de consulta

| Etapa | Requisito determinístico |
|
---|
---|
| Selecione o serviço | Use um ID de serviço estável, não apenas o texto da página |
| Verifique a disponibilidade | Retornar intervalos de tempo atuais |
| Coletar dados do usuário | Validar campos obrigatórios |
| Mostrar política | Regras de preços e cancelamento para devoluções |
| Confirmar reserva | Exigir aprovação explícita do usuário |
| Resultado de retorno | Forneça o ID da reserva e próximas etapas |

Um agente pode raciocinar sobre qual serviço é adequado ao usuário. A rota de confirmação de reserva não deve ser inventada.

## Como auditar seu site

1. Escolha um fluxo de trabalho de alto valor.
2. Escreva a máquina de estado exata para esse fluxo de trabalho.3. Identifique onde seu site atualmente depende de sugestões visuais.
4. Adicione tags, esquemas, APIs ou ferramentas MCP legíveis por máquina quando necessário.
5. Adicione portas de aprovação antes de ações irreversíveis.
6. Registre cada transição de estado relevante para o agente.
7. Experimente os caminhos do fracasso, não apenas os caminhos do sucesso.

## Perguntas frequentes

### O design de fluxo de trabalho determinístico é apenas para desenvolvedores?

As equipes de produto, SEO, jurídico, suporte e operações devem ajudar a definir quais ações exigem aprovação e quais status são válidos.### O ADK 2.0 substitui LangGraph ou outras estruturas?

Não. É outro caminho de desenvolvimento de agentes. A lição útil do AEO é o princípio do design: execução determinística para fluxos de trabalho conhecidos.

### Por que isso afeta o SEO?

O SEO clássico leva os usuários às páginas. O agente de SEO também precisa que essas páginas e fluxos de trabalho possam ser utilizados por assistentes automatizados.

### Qual é o primeiro fluxo de trabalho a ser modelado?

Comece com a ação de maior valor que um agente poderia realizar: reserva, solicitação de orçamento, comparação de produtos, pagamento, ticket de suporte ou solicitação de demonstração.

## Fontes

Principais fontes: [Blog do desenvolvedor do Google: Por que criamos o ADK 2.0](https://developers.googleblog.com/why-we-built-adk-20/) e [Blog do desenvolvedor do Google: ADK Go 2.0](https://developers.googleblog.com/announcing-adk-go-20/).