---
title: "Relação de referência de rastreamento de IA: como medir valor."
metaTitle: "Taxa de rastreamento de IA para referência para AEO."
date: 2026-07-02
weight: 190
category: "Guide"
description: "O relacionamento de rastreamento para referência da IA ​​mostra se os rastreadores retornam valor. Aprenda como medir o tráfego do rastreador de IA antes de bloqueá-lo."
summary: "Um guia para medir a proporção de rastreamento por referência de IA, valor do rastreador, referências de IA e decisões de controle de acesso."
keywords:
  - "Rastreamento de IA e relacionamento de referência"
  - "Valor do rastreador de IA"
  - "Análise de rastreadores de IA"
  - "referências de rastreador"
  - "Medição OEA"
---
# Rastreamento de IA para relação de referência

A proporção de rastreamento/referência de IA compara a frequência com que um rastreador de IA solicita seu conteúdo com a frequência com que o sistema de IA retorna usuários. É uma das métricas AEO mais úteis porque transforma o debate sobre os rastreadores de sentimento em evidência.

## O que significa a métrica?

A fórmula é simples:

```text
AI crawl-to-referral ratio = AI crawler requests / AI referral visits
```

Se um bot rastrear 10.000 páginas e a superfície de IA relacionada enviar 100 acessos, a proporção será de 100:1. Se você rastrear 10.000 páginas e enviar uma visita, a proporção será de 10.000:1.

O [anúncio do Attribution Business Insights] (https://blog.cloudflare.com/attribution-business-insights/) da Cloudflare afirma que viu proporções de rastreadores de IA variando de 118:1 a quase 50.000:1 em torno de sua análise do Dia da Independência de Conteúdo de 2025. O número exato em seu site varia dependendo do setor, tipo de página, política de rastreamento e demanda da marca.

## Por que é importante para os AEOs

As equipes AEO devem responder a três perguntas:

1. Quais sistemas de IA podem acessar o site?
2. Quais sistemas de IA você cita, refere ou utiliza no site?
3. Quais sistemas de IA consomem recursos sem retornar valor?

O volume do rastreador por si só não é suficiente. Um rastreador de alto volume poderia gerar visibilidade no futuro. Também poderia custar largura de banda e não produzir descobertas, compromissos ou conversões.

Isso se conecta diretamente a [Atribuição de referência de IA para AEO SEO](/es/docs/ai-referral-attribution-seo/), [Tráfego da Web do agente de IA em 2026](/es/docs/ai-agent-web-traffic-2026/) e [Controle de rastreamento de IA da Cloudflare](/es/docs/cloudflare-ai-crawl-control/).

## O que medir

| Métrica | Por que é importante |
|
---|
---|
| Solicitações de rastreador de IA | Mostra o uso de recursos e o apetite por rastreamento |
| Referências de IA | Mostra o tráfego direto retornado de superfícies de IA |
| URLs citados | Mostra quais páginas são usadas nas respostas |
| Proporção de rastreamento por referência por bot | Identifique rastreadores de alto e baixo valor |
| Taxa de conversão após referência de IA | Separe o tráfego de curiosidade do valor comercial |
| Solicitações de IA bloqueadas | Mostra se seus controles ocultam páginas úteis |
| Solicitações de `/llms.txt` | Mostra tentativas de descoberta orientadas ao agente |

## Como calcular sem Cloudflare

O painel Cloudflare é útil se o seu site usa Cloudflare Bot Management. Caso contrário, você ainda poderá criar uma versão básica:

1. Exporte os logs do servidor dos últimos 30 dias.
2. Agrupe solicitações por agente de usuário rastreador de IA conhecido e IP verificado quando possível.
3. Separe robôs de busca, agentes, treinamento e estranhos quando as evidências permitirem.
4. Extraia sessões de referência de IA de análises e logs do servidor.
5. Combine cuidadosamente a família do rastreador com a família de referência. Não presuma que toda solicitação "OpenAI" cria todas as referências ChatGPT.
6. Calcule proporções por bot, seção e tipo de página. O resultado será imperfeito, mas mais útil do que adivinhar.

## Tabela de decisão| Padrão de proporção | Interpretação possível | Ação |
|
---|
---|
---|
| Baixo traço, alta referência | Descoberta eficiente | Manter o acesso aberto e melhorar as páginas citadas |
| Alto rastreamento, alta referência | útil, mas caro | Permitir, monitorar largura de banda, otimizar cache |
| Traço alto, referência baixa | Risco de extração | Limitar, restringir ou negociar o acesso |
| Sem rastreamento, alta referência | Processo de marca ou citação indireta | Melhorar a clareza das fontes e páginas de destino |
| Sem rastreamento, sem referências | Não visível | Revise o bloqueio, a qualidade do conteúdo e os sinais da entidade |

## Erros comuns

O principal erro é tratar as referências de IA como o único valor. Alguns sistemas de agentes podem pesquisar uma página, responder a uma pergunta e não enviar um clique. Isso ainda pode afetar a preferência da marca, visitas diretas subsequentes ou compras em outro lugar.

O segundo erro é considerar todas as solicitações do rastreador ruins. Os sistemas de busca e resposta precisam de conteúdo atual. O objetivo não é que a IA não seja rastreada. O objetivo é uma política de rastreador que corresponda ao modelo de negócios.

## Perguntas frequentes

### Qual é uma boa proporção entre rastreamento e referência?

Não existe um ponto de referência universal. Compare por bot, tipo de página e valor comercial. Um site de documentação e um editor de notícias não devem usar o mesmo limite.

### Devo bloquear rastreadores com proporções altas?

Não imediatamente. Primeiro, verifique se eles citam seu conteúdo, enviam conversões assistidas ou oferecem suporte a uma importante superfície de pesquisa.

### O Google Analytics pode medir isso?

Apenas em parte. Muitas solicitações do rastreador nunca executam a análise de JavaScript. Use logs de servidor ou logs CDN.

### Esta é uma métrica de segurança ou SEO?

Ambos. As equipes de SEO o utilizam para compreender o valor da descoberta. As equipes de segurança e infraestrutura usam-no para gerenciar o abuso de custos e recursos.

## Fontes

Fonte primária: [Cloudflare Attribution Business Insights](https://blog.cloudflare.com/attribution-business-insights/). Fonte relacionada: [Opções de tráfego de IA da Cloudflare](https://blog.cloudflare.com/content-independence-day-ai-options/).