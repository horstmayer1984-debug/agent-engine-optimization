---
title: "Endpoints do site NLWeb: interfaces legíveis."
metaTitle: "Endpoints do site NLWeb para agentes."
date: 2026-06-28
weight: 173
category: "Architecture"
description: "NLWeb fornece sites com terminais de linguagem natural para humanos e agentes de IA. Descubra como ele usa Schema.org, RSS, MCP e dados do site."
summary: "Uma introdução prática aos endpoints de sites NLWeb, por que eles são importantes para sites legíveis por agentes e como preparar conteúdo e dados."
keywords:
  - "Terminais do site NLWeb"
  - "NLWeb para agentes de IA"
  - "endpoints de sites legíveis por máquina"
  - "API Web de linguagem natural"
  - "NL Web MCP"
---
# endpoints do site NLWeb

NLWeb é um projeto de código aberto da Microsoft para adicionar interfaces de linguagem natural a sites. É importante para sites prontos para agentes porque transforma dados de sites existentes, como Schema.org e RSS, em endpoints que podem servir humanos e agentes de IA. É uma ponte útil entre conteúdo, pesquisa e ferramentas estilo MCP.

## O que é NLWeb?

O [repositório NLWeb da Microsoft] (https://github.com/microsoft/NLWeb) descreve o NLWeb como uma forma de criar interfaces de conversação para sites. Seu README diz que suporta MCP nativamente, usa Schema.org e formatos semiestruturados semelhantes a RSS e fornece protocolos abertos mais código de implementação.

Isso torna o NLWeb relevante para sites que desejam que os agentes façam perguntas estruturadas em vez de pesquisar páginas às cegas.

NLWeb não deve ser tratado como uma camada mágica de SEO. Está mais próximo do padrão de interface de um site: uma forma de expor o conhecimento e os logs do próprio site por meio de acesso em linguagem natural.

## Por que NLWeb é uma nova oportunidade para palavras-chave

A maioria dos sites ainda pensa em três camadas:

1. Páginas HTML para humanos.
2. Sitemaps para motores de busca.
3. API para desenvolvedores.

NLWeb tem como alvo uma quarta camada: endpoints de linguagem natural para agentes e usuários assistidos por IA.

| Camada | Usuário principal | Formato típico |
|
---|
---|
---|
| Site | Visitante humano | HTML |
| Mapa do site | Rastreador de pesquisa | XML |
| Dados estruturados | Sistemas de busca e inteligência artificial | Schema.org JSON-LD |
| Ponto final NLWeb | Agente humano ou de IA fazendo uma pergunta sobre uma tarefa | Interface de linguagem natural suportada por dados do site |
| Ferramenta MCP | Agente que necessita de ação estruturada | Esquema de ferramentas e ponto final |

Para arquitetura relacionada, consulte [Recursos, ferramentas e mensagens do MCP](/es/docs/mcp-resources-tools-prompts/) e [MCP vs. API para agentes](/es/docs/mcp-vs-api-for-agents/).

## Quais sites devem ver o NLWeb primeiro?

NLWeb é mais interessante para sites com dados ricos e pesquisáveis:

1. Catálogos de comércio eletrônico.
2. Inventário de viagens.
3. Listagens de imóveis.
4. Quadros de empregos.
5. Portais de documentação.
6. Diretórios locais.
7. Apoiar bases de conhecimento.
8. Bancos de dados de eventos.

Esses sites já contêm fatos estruturados. O NLWeb oferece a eles um caminho de recuperação legível pelo agente e conversacional.

## Como se preparar para NLWeb

Mesmo que você ainda não implemente o NLWeb, prepare a camada de dados:

1. Use nomes de entidades consistentes em todas as páginas e dados estruturados.
2. Mantenha a marcação do Schema.org alinhada com o conteúdo visível.
3. Mantenha feeds limpos de produtos, artigos, eventos, listagens ou documentos.
4. Crie URLs canônicos estáveis ​​para cada entidade importante.
5. Documente a frequência de atualização e as regras de disponibilidade.
6. Decida quais data brokers podem consultar e quais dados requerem autenticação.7. Mapeie possíveis perguntas para campos de dados de origem.

Isso se sobrepõe a [Programação de site do agente de IA](/es/docs/programming-websites-for-ai-agents/) e [Aplicativos Web prontos para agente](/es/docs/agent-ready-web-apps/).

## NLWeb vs raspagem| Pergunta | Raspado | Ponto de extremidade estilo NLWeb |
|
---|
---|
---|
| O site controla a forma da resposta? | Geralmente não | Sim |
| O agente pode fazer uma pergunta específica? | Indiretamente | Sim |
| A saída está vinculada aos dados de origem? | Muitas vezes frágil | Mais controlável |
| É mais fácil aplicar a política de acesso? | Mais difícil | Mais fácil se bem projetado |
| Substitui páginas normais? | Não | Não |

O benefício estratégico é o controle. Se os agentes forem verificar seu site de qualquer maneira, um endpoint estruturado pode ser mais seguro e preciso do que forçá-los a navegar pelas páginas visuais.

## Perguntas frequentes

### O NLWeb é um padrão oficial da web?

NLWeb é um projeto de código aberto da Microsoft com protocolos e código de implementação abertos. Trate-o como uma abordagem emergente e não como um padrão universal estabelecido.

### O NLWeb substitui o Schema.org?

O NLWeb depende de dados de sites como Schema.org e formatos semelhantes ao RSS. Dados bem estruturados ainda são importantes.

### NLWeb é o mesmo que MCP?

Não. NLWeb pode suportar MCP, mas MCP é um protocolo para ferramentas e troca de contexto. NLWeb se concentra em interfaces de sites em linguagem natural.

### Todos os sites deveriam implementar o NLWeb agora?

Não. Comece com sites onde os usuários ou agentes precisam fazer perguntas detalhadas sobre dados estruturados no site.

## Fontes

Fontes primárias e de referência: [repositório Microsoft NLWeb GitHub] (https://github.com/microsoft/NLWeb), [fonte bruta README NLWeb] (https://raw.githubusercontent.com/microsoft/NLWeb/main/README.md), [documentação do Model Context Protocol] (https://modelcontextprotocol.io/docs/getting-started/intro), [Schema.org] (https://schema.org/) e [documentação de dados estruturados do Microsoft NLWeb] (https://modelcontextprotocol.io/docs/getting-started/intro). Google](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data).