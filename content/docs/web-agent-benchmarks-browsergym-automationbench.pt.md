---
title: "BrowserGym e AutomationBench: benchmarks de agentes."
metaTitle: "BrowserGym e AutomationBench para AEO."
date: 2026-06-28
weight: 185
category: "Analysis"
description: "BrowserGym e AutomationBench mostram como os agentes web e APIs são avaliados. Aprenda como transformar essas lições em testes práticos de AEO."
summary: "Um guia prático para BrowserGym e AutomationBench de uma perspectiva AEO, cobrindo tarefas de agente web, fluxos de trabalho de API, verificações de políticas e sucesso de tarefas."
keywords:
  - "BrowserGym AutomationBench"
  - "benchmarks de agente web"
  - "Testes Comparativos AEO"
  - "Comparação de agentes de API"
  - "avaliação do agente do navegador"
---
# BrowserGym e AutomationBench

BrowserGym e AutomationBench são importantes para AEO porque mostram como os agentes são avaliados: não pelas visualizações de página, mas pela conclusão de tarefas. Os sites que desejam trabalhar com agentes devem testar fluxos de trabalho reais, incluindo navegação, descoberta de API, aplicação de políticas e verificação do estado final.

## Que cara de abraço surgiu

A pesquisa por artigos Hugging Face surgiu [The BrowserGym Ecosystem for Web Agent Research](https://hf.co/papers/2412.05467) e [AutomationBench](https://hf.co/papers/2604.18934) como artigos relevantes para agentes web e agentes que usam ferramentas.

O BrowserGym concentra-se em ambientes padronizados para avaliação de agentes web. O AutomationBench se concentra na orquestração de fluxo de trabalho entre aplicativos por meio de APIs REST, incluindo descoberta, aplicação de políticas e precisão de dados.

Essa divisão corresponde bem ao AEO:

| Ponto de referência | Lição AEO |
|
---|
---|
| NavigatorGym | Teste se os agentes podem usar seus fluxos web visíveis. |
| Bancada de automação | Teste se os agentes podem descobrir e executar fluxos de trabalho de API. |

## Por que os benchmarks são melhores do que apenas o tráfego

As referências de IA e as pesquisas de agentes são úteis, mas não demonstram o sucesso da tarefa.

| Métrica Fraca | Métricas AEO mais fortes |
|
---|
---|
| Visualização de página | Tarefa concluída |
| Profundidade de rolagem | Transição de estado bem sucedida |
| Referência de IA | Conversão ou resultado verificado |
| Agente de usuário de bot | Chamada de ferramenta bem-sucedida |
| Tempo na página | Conclusão conforme |

Para um rastreamento mais amplo, consulte [AEO KPI](/es/docs/aeo-kpis-measurement/) e [AI Agent Web Traffic em 2026](/es/docs/ai-agent-web-traffic-2026/).

## Crie um pequeno ponto de referência para seu site

Você não precisa de um laboratório de pesquisa para começar.

1. Escolha cinco tarefas de alto valor.
2. Defina o estado final correto para cada tarefa.
3. Execute tarefas com um agente navegador e um agente que utilize ferramentas sempre que possível.
4. Registre as falhas.
5. Corrija rótulos, documentos, esquemas, APIs, políticas ou commits.
6. Repita mensalmente.

Tarefas de exemplo:

| Tipo de site | Tarefa de referência |
|
---|
---|
| Comércio eletrônico | Encontre um produto, verifique a política de devolução, prepare um carrinho. |
| SaaS | Compare planos e solicite uma demonstração. |
| Portal do desenvolvedor | Encontre documentos de endpoint e faça uma chamada de API de teste. |
| Site de suporte | Encaminhe um problema de faturamento para o canal de suporte correto. |
| Site de viagens | Encontre disponibilidade reembolsável sob restrições da política. |

## O que medir

1. Taxa de conclusão.
2. Taxa de ações incorretas.
3. Taxa de violação da política.
4. Número de tentativas de recuperação.
5. Erros de contexto ausentes.
6. Transferências de aprovação humana.
7. Verificação do estado final.

Isso está diretamente vinculado a [Parâmetros de avaliação do agente](/es/docs/agent-evaluation-benchmarks/) e [Observabilidade do agente e barreiras de proteção](/es/docs/agent-observability-guardrails/).

## Perguntas frequentes### O BrowserGym e o AutomationBench são ferramentas de SEO?

Não. São referências de avaliação de agentes. Eles são importantes para o AEO porque o AEO tem a ver com o sucesso da tarefa do agente, e não apenas com a visibilidade da pesquisa.

### Qual estilo de referência os sites devem copiar primeiro?

Sites com formulários e fluxos de UI devem começar com testes de agente de navegador. As empresas que usam muitas APIs também devem testar ferramentas e fluxos de trabalho de API.### O que é um status de aprovação ou reprovação?

Um status de aprovação é um resultado verificável, como um ticket criado, uma cotação bem-sucedida, uma resposta válida da API, um carrinho preparado ou um rascunho de reserva confirmado.

### Com que frequência os benchmarks do agente devem ser executados?

Mensalmente é suficiente para a maioria dos sites. Execute-o com mais frequência quando os documentos de pagamento, preços, suporte ou API mudam com frequência.

## Fontes

Fontes primárias: [documento BrowserGym](https://hf.co/papers/2412.05467), [documento AutomationBench](https://hf.co/papers/2604.18934), [documento AgentRewardBench](https://hf.co/papers/2504.08942) e [documento ST-WebAgentBench](https://hf.co/papers/2410.06703).