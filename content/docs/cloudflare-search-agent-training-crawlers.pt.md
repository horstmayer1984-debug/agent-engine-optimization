---
title: "Rastreadores de pesquisa, agentes e treinamento da Cloudflare."
metaTitle: "Pesquisa Cloudflare, agentes e rastreadores de treinamento."
date: 2026-07-02
weight: 188
category: "Analysis"
description: "A Cloudflare agora separa o tráfego de IA em rastreadores de pesquisa, agentes e treinamento. Descubra o que isso significa para AEO, robots.txt e acesso."
summary: "Um guia prático de AEO para a taxonomia de tráfego de IA da Cloudflare de julho de 2026 para rastreadores de pesquisa, agentes e treinamento."
keywords:
  - "Rastreadores de treinamento de agentes de pesquisa da Cloudflare"
  - "Taxonomia de rastreadores de IA"
  - "acesso ao rastreador de agente"
  - "Controles de tráfego de IA"
  - "Política de rastreadores AEO"
---
# Rastreadores de pesquisa, agentes e treinamento da Cloudflare

Os controles de tráfego de IA da Cloudflare de julho de 2026 dividem o tráfego automatizado de IA em três categorias práticas: pesquisa, agente e treinamento. Para as equipes AEO, a mudança importante é que a política de rastreamento não pode mais ser uma escolha contundente de “permitir IA” ou “bloquear IA”. A visibilidade da pesquisa, a execução de tarefas do agente e o treinamento do modelo agora precisam de regras separadas.

## O que mudou em julho de 2026

Em 1º de julho de 2026, a Cloudflare anunciou [novas opções de tráfego de IA para todos os clientes](https://blog.cloudflare.com/content-independence-day-ai-options/). Os novos controles classificam a automação relacionada à IA por finalidade:

| Categoria | O que significa | Implicação do AEO |
|
---|
---|
---|
| Pesquisar | Rastrear ou indexar conteúdo para encontrá-lo mais tarde | Geralmente vale a pena permitir páginas de descoberta pública |
| Agente | Automação direcionada pelo usuário que visita um site para concluir uma tarefa | Precisa de UX seguro para ações, permissões e tratamento de erros |
| Treinamento | Rastreando conteúdo para treinar ou ajustar modelos | Muitas vezes necessita de uma decisão legal, de licenciamento ou de monetização separada |

A Cloudflare afirma que as opções estão disponíveis para todos os clientes, incluindo usuários de nível gratuito. Isto é importante porque a governança dos rastreadores está passando de um controle exclusivo da empresa para uma decisão de publicação normal.

## Por que isso é importante para o Agent Engine Optimization

O SEO tradicional tratava os rastreadores principalmente como indexadores. O AEO deve tratar os visitantes automatizados como atores diferentes:

- um rastreador de pesquisa que ajuda os usuários a descobrir uma página
- um mecanismo de resposta que pode citar ou resumir a página
- um agente de navegador que pode clicar, comparar ou enviar
- um rastreador de treinamento que pode absorver conteúdo sem retornar tráfego

É por isso que [Agent Engine Optimization](/es/docs/what-is-aeo/) separa a [Camada de leitura](/es/docs/answer-engine-optimization/) da [Camada de execução](/es/docs/execution-layer/). Os rastreadores de pesquisa pertencem principalmente à camada de leitura. Os rastreadores de agentes estão mais próximos da execução.

## A mudança padrão de 15 de setembro de 2026

A Cloudflare também anunciou uma mudança padrão programada para novos domínios ingressando na Cloudflare em 15 de setembro de 2026. Para páginas com suporte de publicidade, as categorias Treinamento e Agente serão bloqueadas por padrão, enquanto a Pesquisa ainda será permitida por padrão.

O detalhe que as equipes AEO não devem perder: os rastreadores polivalentes podem ser afetados pela regra selecionada mais restritiva. A Cloudflare observa explicitamente que os rastreadores que combinam pesquisa com treinamento podem ser bloqueados quando o proprietário de um site decide bloquear o treinamento.

Isso cria um risco real para o SEO. Um editor pode tentar bloquear o treinamento, mas acidentalmente restringir um rastreador que também oferece suporte à descoberta de pesquisa.## Política de rastreador recomendada por tipo de página | Tipo de página | Pesquisar | Agente | Treinamento | Notas |
|
---|
---:|
---:|
---:|
---|
| Página inicial pública | Permitir | Geralmente permitir | Decidir sobre o modelo de negócios | Manter a marca visível |
| Páginas de produtos | Permitir | Permitir com limites de taxa | Geralmente restringir ou licenciar | Os dados do produto devem estar atualizados |
| Documentação | Permitir | Permitir | Decidir | Agentes precisam de documentos para concluir tarefas |
| Pagar | Restringir | Permitir apenas com controles rígidos | Bloco | Regras de pagamento e identidade são importantes |
| Pesquisa paga | Talvez permita fragmentos | Restringir | Bloquear ou monetizar | Considere resumos e detalhes privados |
| Ferramentas internas | Bloco | Apenas autenticação | Bloco | Nenhum valor de rastreador público |

Isso deve ser combinado com [AI Crawlers e robots.txt](/es/docs/ai-crawlers-robots-txt/) e [Cloudflare AI Crawl Control](/es/docs/cloudflare-ai-crawl-control/).

## Lista de verificação de implantação

1. Liste os tipos de páginas públicas de alto valor.
2. Decida quais páginas precisam de visibilidade de pesquisa.
3. Decida onde os agentes direcionados ao usuário deverão poder atuar.
4. Separar o uso da formação do uso da pesquisa na linguagem política.
5. Revise os controles de tráfego de IA da Cloudflare se o site estiver sendo executado por trás da Cloudflare.
6. Audite se as regras de firewall existentes bloqueiam referenciadores ou agentes de IA conhecidos.
7. Monitore o volume de rastreamento e referências após alterar as regras.

Não copie a lista de bloqueio de um concorrente. Um site de mídia, um centro de documentação SaaS, uma loja de comércio eletrônico e um negócio de API têm diferentes necessidades de exposição e monetização.

## Erro AEO a evitar

O maior erro é tratar o “rastreador de IA” como uma intenção única. Um agente navegador tentando comprar um produto para um usuário não é o mesmo que um rastreador de treinamento que utiliza conteúdo para melhorar o modelo. Se ambos forem bloqueados por uma regra, o site poderá proteger o conteúdo, mas perderá as conversões assistidas pelo agente.

## Perguntas frequentes

### Todos os sites deveriam permitir rastreadores de pesquisa?

A maioria dos sites públicos deve permitir rastreadores de pesquisa confiáveis ​​em páginas indexáveis. As exceções incluem URLs privados, pagos, legalmente restritos ou de baixo valor.

### Os rastreadores de agentes devem ser permitidos?

Somente onde o agente pode concluir tarefas seguras que beneficiam o usuário. As páginas somente leitura são mais simples do que carrinhos, formulários, alterações de conta ou compras.

### O monitoramento de treinamento é ruim para o AEO?

Não automaticamente. Algumas marcas podem aceitá-lo por motivos de visibilidade ou licenciamento. Outros podem restringi-lo porque não cria referências diretas.

### O bloqueio do treinamento pode prejudicar o SEO?

Pode ser possível se um rastreador tiver múltiplas finalidades e a infraestrutura aplicar a categoria mais restritiva. A atualização de julho de 2026 da Cloudflare torna esse risco mais explícito.

## FontesFonte principal: [Cloudflare: Seu site, suas regras](https://blog.cloudflare.com/content-independence-day-ai-options/). Contexto de implementação relacionado: [documentos de controle de rastreamento de IA da Cloudflare](https://developers.cloudflare.com/ai-crawl-control/).