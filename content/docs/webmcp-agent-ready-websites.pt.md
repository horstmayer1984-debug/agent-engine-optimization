---
title: "WebMCP para sites prontos para agentes."
metaTitle: "WebMCP para sites prontos para agentes: guia."
date: 2026-05-17
weight: 109
category: "Architecture"
description: "O WebMCP permite que sites exponham ferramentas nativas do navegador a agentes de IA. Aprenda quando usar o WebMCP e como ele difere do MCP."
summary: "Um guia prático para WebMCP para sites prontos para agentes, abrangendo ferramentas nativas de navegador, diferenças de MCP, formulários, padrões de implantação e implicações de AEO."
keywords:
  - "WebMCP"
  - "WebMCP x MCP"
  - "sites prontos para agentes"
  - "agentes de navegador"
  - "Ferramentas Web do Agente AI"
---
# WebMCP para sites prontos para agentes

O WebMCP é importante porque oferece aos sites uma maneira de expor ferramentas de nível de página diretamente aos agentes do navegador, em vez de forçar os agentes a inferir ações a partir de capturas de tela, estrutura DOM ou rótulos de botões frágeis. Para AEO, o WebMCP é uma ponte entre páginas da web orientadas para humanos e ações executáveis ​​por máquina.

## O que é WebMCP?

Os materiais WebMCP do Chrome descrevem o WebMCP como uma forma do lado do navegador para os sites esclarecerem a finalidade das funções do aplicativo e fornecerem recursos estruturados aos agentes do navegador. O guia do Chrome deixa explícito que o WebMCP não substitui o MCP. Ambos resolvem problemas diferentes.

Fontes primárias:

- [Chrome: quando usar WebMCP e MCP](https://developer.chrome.com/blog/webmcp-mcp-usage)
- [Chrome Lighthouse: ferramentas WebMCP registradas] (https://developer.chrome.com/docs/lighthouse/agentic-browsing/registered-webmcp-tools)
- [Guia do Titereiro WebMCP] (https://pptr.dev/guides/webmcp)

## WebMCP versus MCP

| Pergunta | PCM | WebMCP |
|
---|
---|
---|
| Onde funciona? | Ambiente ou ferramenta de servidor | Contexto da página do navegador |
| Trabalho principal | Conecte agentes a ferramentas, APIs, dados e fluxos de trabalho | Informar aos agentes do navegador quais ações uma página suporta |
| Bom para | Ações de back-end, acesso a dados, ferramentas de negócios | Formulários, ações de página, etapas de pagamento, reservas |
| Método de descoberta | Servidor MCP Anuncia Ferramentas | Página registra ferramentas de forma declarativa ou com JavaScript |
| Função AEO | Camada de execução para APIs e serviços | Camada de execução para interfaces web |

O [guia MCP vs API] (/docs/mcp-vs-api-for-agents/) explica o MCP no lado do servidor. WebMCP adiciona uma camada de nível de página para sites onde o navegador ainda faz parte da jornada do usuário.

## Por que o WebMCP muda o AEO

Muitos sites já possuem ações: marcar consulta, adicionar produto ao carrinho, solicitar orçamento, filtrar estoque, enviar ticket de suporte. O problema é que essas ações geralmente são visíveis apenas como elementos da UI.

Um agente navegador pode tentar operar a página como uma pessoa, mas isso é frágil. Os rótulos mudam. Aparecem boas maneiras. Os campos estão ocultos. O teste A/B altera o DOM. O WebMCP dá ao site uma forma de indicar a ação diretamente: este formulário marca um agendamento, esses campos são obrigatórios, esta ação deve ser utilizada quando o usuário desejar uma reserva.

Esse é um sinal de [camada de execução] (/es/docs/execution-layer/) mais forte do que apenas um rótulo de botão.

## Padrões de implementação

A documentação do Lighthouse do Chrome diz que as ferramentas podem ser registradas com atributos declarativos em formulários ou com uma API JavaScript imperativa como `navigator.modelContext.registerTool`.

| Padrão | O melhor para | Exemplo |
|
---|
---|
---|
| Ferramentas de formulário declarativo | Formulários existentes com ações claras | `reserva_compromisso`, `request_quote` || Registo imperativo | Aplicações dinâmicas e ações complexas | pesquisa de inventário, mutação de carrinho |
| Servidor MCP | Fluxos de trabalho de back-end independentes de navegador | pesquisa de clientes, criação de faturas |
| Híbrido | Sites com ações de API e UI da Web | e-commerce, reservas, painéis SaaS |

Para a maioria dos sites, a primeira ação útil do WebMCP deve ser um formulário de baixo risco: solicitação de lead, consulta de agendamento, caminho de suporte ou filtro de produto.

## O que torna uma boa ferramenta WebMCP?O nome da ferramenta deve ser orientado para a ação e estável. A descrição deve informar ao agente quando usá-lo e qual resultado esperar.

Fraco:

```text
toolname="submit"
tooldescription="Submits the form"
```

Melhor:

```text
toolname="request_audit"
tooldescription="Request an AEO readiness audit for a website. Use when the user wants a human review of AI search, crawler, and execution-layer readiness."
```

Os agentes precisam de intenção, informações necessárias e resultados esperados. O [Guia de resumo de ações e botões do agente] (/docs/agent-buttons-action-schema/) cobre o mesmo princípio para instruções de ação além do WebMCP.

## Implicações de SEO e AEO

WebMCP não é um fator de classificação tradicional. Trate isso como um sinal de ação, não como um atalho para classificações.

A sequência útil de SEO/AEO é:

1. Torne a página rastreável e indexável.
2. Adicione conteúdo, títulos, contornos e links internos claros.
3. Publique arquivos de descoberta como [llms.txt](/es/docs/programming-llms-txt/).
4. Adicione ferramentas WebMCP para ações de alto valor.
5. Experimente auditorias de navegação do agente Lighthouse.
6. Monitore preenchimentos de formulários e eventos acionados por agentes.

Se o conteúdo da página for fraco, o WebMCP não resolverá o problema. Ajuda os agentes a agir assim que entendem a página.

## Riscos

Não exponha ações confidenciais sem confirmação e autorização. Uma ação nativa do navegador não deve permitir que um agente altere o faturamento, exclua dados ou conclua compras sem o devido consentimento.

Boas grades incluem:

- descrições claras das ferramentas
- confirmação explícita para ações de alto risco
- validação do lado do servidor
- registro de auditoria
- limites de taxa
- revisão humana para tarefas regulamentadas

## Perguntas frequentes

### WebMCP é o mesmo que MCP?

Não. O MCP conecta agentes a ferramentas e sistemas. O WebMCP ajuda os sites a expor ações no nível da página aos agentes do navegador.

### Todos os sites deveriam implementar WebMCP?

Ainda não. Comece com sites onde os agentes precisam preencher formulários, reservas, filtros ou outras ações do navegador.

### O WebMCP melhora as classificações?

Não há nenhuma afirmação oficial de que o WebMCP seja um fator de classificação. Seu valor está na capacidade de ação do agente, não na classificação convencional de SEO.

### O que devo implementar primeiro?

Comece com uma ação de baixo risco, como solicitar um orçamento, agendar uma consulta ou abrir um caminho de suporte.

### Como faço para testar o WebMCP?

Use as auditorias do agente de navegação Chrome do Lighthouse e as ferramentas do navegador que podem listar ferramentas WebMCP registradas.