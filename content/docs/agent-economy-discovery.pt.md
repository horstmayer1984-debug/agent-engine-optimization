---
title: "A economia dos agentes em números: 480 mil agentes ativos."
metaTitle: "Descobrindo a economia do agente: como o AEO ajuda."
date: 2026-04-19
weight: 115
category: "Analysis"
description: "A economia agente já processa 165 milhões de transações no valor de US$ 50 milhões. Mas descoberta e relatórios."
metaDescription: "Vea cómo AEO ayuda a conectar a los agentes con los servicios cuando la actividad de los agentes está creciendo pero el descubrimiento, la atribución."
summary: "480.000 agentes de IA ativos. 165 milhões de transações. Foram gastos 50 milhões de dólares. A economia do agente é real, mas a descoberta não funciona. O AEO resolve o problema de correspondência entre agentes que têm dinheiro para gastar e serviços que não conseguem encontrar."
keywords:
  - "economia do agente"
  - "agente de mercado"
  - "Transações de agente de IA"
  - "problema de descoberta de agente"
  - "Economia do Agente AEO"
  - "Ecossistema x402"
  - "negociação de máquina para máquina"
---
A economia do agente não é mais teórica. Somente dentro do ecossistema x402, mais de 480.000 agentes ativos de IA completaram mais de 165 milhões de transações, gastando aproximadamente US$ 50 milhões em quase 100.000 serviços digitais. Plataformas como Agentic.Market estão documentando a escala em tempo real.

Mas permanece um problema estrutural. A descoberta está quebrada. Os agentes têm orçamentos para gastar e tarefas para concluir, mas encontrar o serviço certo para a tarefa certa e pelo preço certo ainda não é confiável. Essa lacuna é exatamente o que o Agent Engine Optimization aborda.

## A escala da negociação máquina a máquina

Esses números não são projeções. Eles refletem a atividade atual em um único ecossistema de protocolo. 480 mil agentes operando de forma autônoma, selecionando serviços, negociando prazos, executando pagamentos e concluindo tarefas sem envolvimento humano em nenhuma etapa.

Os padrões de transação não se parecem em nada com o comércio humano. Os valores médios das transações começaram em torno de US$ 1,60 e subiram para US$ 34,50 em 30 dias, à medida que os agentes aprendiam quais serviços ofereciam resultados confiáveis. Os agentes que encontram bons serviços voltam para eles. Os agentes que consideram os serviços não confiáveis ​​saem permanentemente.

Isso cria uma dinâmica em que o vencedor leva mais. Serviços fáceis de descobrir, claramente documentados e executáveis ​​de forma confiável acumulam tráfego de agente. Os serviços que são difíceis de encontrar ou que têm uma oferta ambígua são ignorados, mesmo que a sua capacidade subjacente seja superior.

## Por que a descoberta é o gargalo

O comércio humano possui mecanismos de busca, algoritmos de recomendação, prova social e reconhecimento de marca para resolver a descoberta. A negociação automatizada quase ainda não possui essa infraestrutura.

Um agente encarregado de “encontrar um serviço de resumo de texto que custa menos de US$ 0,05 por solicitação e retorna resultados em 2 segundos” tem opções limitadas para encontrar serviços correspondentes. Você pode verificar logs conhecidos, consultar servidores MCP, ler arquivos llms.txt ou verificar manifestos de recursos. Se o seu serviço não estiver presente em nenhum desses canais de descoberta, o agente não saberá que ele existe.

O problema é agravado porque os agentes operam em alta velocidade. Um humano poderia passar 20 minutos pesquisando opções. Um agente faz sua seleção em milissegundos. Se o seu serviço não for imediatamente detectável com declarações de capacidade claras, o agente já escolheu um concorrente antes mesmo de sua documentação ser carregada.

## Como a pesquisa tradicional falha para os agentes

SEO resolveu descoberta para humanos. Não resolve a descoberta das máquinas. As diferenças são estruturais.

| Aparência | Descoberta humana (SEO) | Descoberta de Agente (AEO) |
|
---|
---|
---|| Público | Humano lendo uma página de resultados | Análise automática de dados estruturados |
| Critérios de decisão | Confiança na marca, design, avaliações | Correspondência exata de capacidade, preço e latência |
| Velocidade de decisão | Minutos a dias | Milissegundos |
| Formato do conteúdo | Texto, imagens e CTAs envolventes | Código estruturado, esquemas TypeScript, API |
| Método de avaliação | Impressão subjetiva | Critérios determinísticos de aprovação/rejeição |
| Pagamento | Entrada manual de cartão de crédito | Automatizado usando x402 ou tokens de protocolo |Um agente não avalia o quão atraente é o seu texto de marketing. Verifica se o seu serviço corresponde exatamente aos parâmetros exigidos. Preço por solicitação, tempo de resposta, formato de entrada, formato de saída, tratamento de erros e disponibilidade. Se algum parâmetro estiver faltando ou for ambíguo, o agente passa para o próximo candidato.

## As três camadas de descoberta de agentes

### Camada 1: descrição estruturada do serviço

Seu serviço deve ser descrito em formato legível por máquina com parâmetros exatos. Não é “rápido e acessível”, mas “tempo médio de resposta: 1,4 segundos, preço: US$ 0,03 por solicitação, entrada: texto UTF-8 de até 10.000 caracteres, saída: JSON com campo de resumo”.

Use [llms.txt](/es/docs/programming-llms-txt/) para descoberta em nível de site, [Cartões de agente](/es/docs/agent-cards-a2a-protocol/) para manifestos de capacidade e marcação de esquema para páginas de serviço individuais.

### Camada 2: registro em nível de protocolo

Registre seus serviços em registros de protocolo onde os agentes pesquisam ativamente. Registros de ferramentas MCP, [Declarações de capacidade UCP](/es/docs/ucp-vs-acp-vs-mcp/) em /.well-known/ucp e listagens de mercado em plataformas como Agentic.Market.

Um agente que descobre seu serviço por meio do registro tem uma intenção de conversão maior do que aquele que encontra seu site. A presença no registro equivale, para o agente, a aparecer nos resultados da pesquisa.

### Camada 3: Preparação da Transação

A descoberta sem capacidade de transação é um beco sem saída. O agente encontra o seu serviço, avalia e então você deve pagar e receber o resultado. [micropagamentos x402](/es/docs/x402-agent-payments/) lidam com a camada de pagamento. Sua API cuida da execução. Ambos devem funcionar em menos de 3 segundos para que o agente conclua a transação.

O [guia da camada de execução](/es/docs/execution-layer/) cobre a arquitetura técnica.

## Defina regras que os agentes podem aplicar

Os agentes não podem interpretar a ambiguidade. Eles não podem ligar para o atendimento ao cliente. Eles não podem negociar informalmente. Cada parâmetro deve ser expresso como absoluto. Preço: valor exato por unidade de trabalho, em que moeda, válido por qual período de tempo. Tempo de resposta: máximo garantido, medido como, com que penalidade por ultrapassá-lo. Restrições de entrada: formato exato, tamanho máximo, campos obrigatórios. Formato de saída: estrutura exata, campos garantidos, esquema de erro. Disponibilidade: Garantia de tempo de atividade, janelas de manutenção, comportamento de serviço degradado.

Os serviços que publicam esses parâmetros como dados estruturados em seus [manifestos de capacidade](/es/docs/agent-decision-trees/) são selecionados. Os serviços que ocultam parâmetros atrás de "entre em contato conosco" ou "a partir de" são excluídos de cada [árvore de decisão determinística](/es/docs/agent-decision-trees/) executada por um agente.

## A vantagem da capitalização

Os pioneiros na descoberta de agentes criam vantagens combinadas. Um agente que realiza transações com sucesso com seu serviço adiciona você à sua lista de provedores preferenciais. As tarefas subsequentes que correspondam ao seu perfil de capacidade serão roteadas para você automaticamente. As pontuações de confiança se acumulam. O histórico de transações é construído.

Um serviço que entra no mercado seis meses depois começa com zero confiança, zero histórico de transações e zero status de provedor preferencial. Você deve competir com serviços estabelecidos nos quais os agentes já confiam. O problema da descoberta se torna mais difícil de resolver quanto mais você espera.É por isso que o [Guia de implantação do AEO](/es/docs/implement-aeo/) enfatiza o início da descoberta básica (llms.txt, marcação de esquema, cartões de agente) mesmo antes da conclusão da camada de execução. Ser detectável precocemente, mesmo com capacidade limitada, cria uma base de confiança que se desenvolve ao longo do tempo.

## O que acontece a seguir?

A economia dos agentes está a crescer mais rapidamente do que a maioria das empresas imagina porque as transações são invisíveis para a análise tradicional. Sem visualizações de página, sem cliques, sem sessões. Apenas chamadas de API, transações de protocolo e micropagamentos que nunca tocam uma interface humana.

As empresas que instrumentam os seus serviços para a descoberta de agentes captam agora um fluxo de receitas crescente que os concorrentes não conseguem ver e, portanto, não conseguem responder. Quando a economia do agente se tornar visível nas métricas tradicionais, as posições de descoberta estarão estabelecidas e serão difíceis de deslocar.

O [artigo sobre modelos de negócios de agentes nativos](/es/docs/agent-native-business-models/) cobre a mudança econômica mais ampla. O [guia de economia de delegação](/es/docs/delegation-economy-agent-autonomy/) explica os cinco níveis de autonomia dos agentes que impulsionam esta transição.

---

## Perguntas frequentes

**Qual será o tamanho da economia dos agentes em abril de 2026?**Só no ecossistema x402: 480.000 agentes ativos, 165 milhões de transações concluídas, aproximadamente US$ 50 milhões em volume de transações, em quase 100.000 serviços. O total em todos os protocolos é provavelmente maior, mas mais difícil de medir.

**Por que os agentes não conseguem encontrar serviços facilmente?**
Porque a maioria dos serviços ainda é projetada para descoberta humana (sites, páginas de marketing, classificações de pesquisa). Os agentes precisam de declarações de capacidade estruturadas, registros de protocolo e parâmetros legíveis por máquina. A maioria dos serviços não possui todos os três.

**Qual é a maneira mais rápida de tornar meu serviço visível para os agentes?**
Publique um arquivo llms.txt que descreva seu serviço com parâmetros exatos. Crie um cartão de agente (agent-card.json) com declarações de capacidade. Registre-se no MCP e nos registros de mercado. Isso leva um ou dois dias e aumenta imediatamente a visibilidade do agente.

**Os agentes realmente têm dinheiro para gastar?**
Sim. Os agentes operam com carteiras financiadas (x402/USDC), autoridade de cartão delegada (Visa Agentic Ready) ou orçamentos de compras empresariais. A capacidade de gasto existe. O mecanismo de descoberta para combinar gastos com serviços é o gargalo.

**O que faz um agente escolher um serviço em vez de outro?**
Correspondência exata de parâmetros (preço, velocidade, capacidade), confiabilidade da transação (taxa histórica de sucesso) e clareza de descoberta (com que rapidez o agente pode verificar se o serviço atende aos requisitos). A reputação da marca não tem peso na seleção do agente.

## Referências primárias

* [Estrutura de gerenciamento de risco de IA do NIST](https://www.nist.gov/itl/ai-risk-management-framework)
* [Documentação do Schema.org](https://schema.org/docs/documents.html)