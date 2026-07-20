---
title: "Como escrever llms.txt corretamente para agentes de IA."
metaTitle: "Como escrever llms.txt para agentes de IA."
date: 2026-04-12
weight: 62
category: "Guide"
description: "llms.txt é o mecanismo de descoberta de agente mais simples e capaz. Estrutura exata, regras de conteúdo, geração dinâmica para sites grandes e."
metaDescription: "Aprenda a escribir llms.txt para agentes de IA, incluida la estructura, las reglas de contenido, la generación dinámica y la integración de esquemas."
summary: "llms.txt informa aos agentes de IA o que seu site oferece e como interagir com ele. Este guia aborda a formatação exata, regras de conteúdo, erros comuns e como gerá-los dinamicamente para sites grandes."
keywords:
  - "guia llms.txt"
  - "Formato llms.txt"
  - "como escrever llms.txt"
  - "descoberta de agente llms.txt"
  - "Implementação de llms.txt"
---
llms.txt é a maneira mais simples e eficaz de fazer com que agentes de IA descubram seu site. Um arquivo Markdown na raiz do seu site informa aos agentes o que você oferece, onde encontrá-lo e como interagir com ele. Os agentes procuram o llms.txt antes de rastrear todo o site, portanto, acertar significa ser descoberto primeiro.

## Por que llms.txt não é negociável em 2026

Os agentes de IA seguem uma hierarquia de descoberta ao encontrar um novo site. Primeiro, pesquise llms.txt. Em segundo lugar, procure agent-card.json. Terceiro, procure dados estruturados em HTML. Quarto, tente analisar o conteúdo bruto da página.

Um site sem llms.txt força os agentes a começarem na etapa três ou quatro, que é mais lenta, menos confiável e tem maior probabilidade de produzir uma extração imprecisa. Um site com um llms.txt claro permite que os agentes entendam todo o escopo de sua oferta em uma única solicitação.

Stripe, Cloudflare e Cursor já publicam arquivos llms.txt. Os primeiros usuários relatam taxas de engajamento de agentes significativamente mais altas e cotações mais precisas nas respostas geradas por IA.

## A estrutura exata

llms.txt é um arquivo Markdown. Use títulos para organizar informações e texto simples para descrições. Aqui está a estrutura recomendada:

**Linha 1: Nome do site como cabeçalho H1.** Uma linha, texto simples.

**Seção 1: O que este site oferece.** Um parágrafo curto (2 a 3 frases) que descreve seu produto, serviço ou conteúdo em termos objetivos. Nenhuma linguagem de marketing. Indique o que faz, para quem se destina e o que o torna útil.

**Seção 2: Páginas principais** Uma lista dos URLs mais importantes com uma descrição de cada uma em uma linha. Inclua sua página inicial, páginas principais de produtos ou serviços, página de preços, documentação e quaisquer páginas onde os agentes devam procurar informações específicas.

**Seção 3: Endpoints disponíveis** Se seu site expõe endpoints de API ou ferramentas MCP, liste-os com breves descrições do que cada um faz, quais entradas são necessárias e o que retorna.

**Seção 4: Autenticação.** Indique como os agentes devem ser autenticados ou declare explicitamente que a autenticação não é necessária para acesso de leitura.

**Seção 5: Restrições.** Limites de taxas, políticas de uso, garantias de atualização de dados e quaisquer restrições sobre como os agentes devem interagir com seu site.

**Seção 6: Contato.** Como reportar erros ou solicitar esclarecimentos.

## Regras de conteúdo

Escreva para extrair, não para persuadir. Cada frase deve conter um fato que um agente possa usar. Elimine adjetivos que não contenham informações. Substitua “nossa plataforma capaz” por “plataforma de programação baseada em API para provedores de saúde”. Limite as descrições a uma ou duas frases por item. Os agentes não precisam de parágrafos. Eles precisam de declarações precisas que possam comparar com as consultas dos usuários.

Atualize llms.txt sempre que adicionar, remover ou alterar um recurso importante. Um llms.txt desatualizado que descreve recursos que você não oferece mais é pior do que nenhum llms.txt porque faz com que os agentes tentem ações que falharão.

## Geração dinâmica para sites grandes

Sites com centenas de produtos ou inventário que muda frequentemente devem gerar llms.txt dinamicamente, em vez de mantê-lo manualmente.Crie um script que consulte o banco de dados do produto, extraia o resumo do catálogo atual, liste os endpoints da API ativos da configuração da rota e grave o resultado como um arquivo Markdown. Execute esse script de acordo com uma programação (diariamente para a maioria dos sites, de hora em hora para sites com muito inventário).

Para sites baseados em Hugo, você pode gerar llms.txt como parte do processo de construção, criando um formato de saída personalizado que representa seus dados de conteúdo como Markdown.

## Integrando llms.txt com marcação de esquema

llms.txt e marcação de esquema servem a propósitos complementares. llms.txt fornece descoberta no nível do site (o que todo o site oferece). A marcação do esquema fornece detalhes no nível da página (o que esta página específica contém).

Consulte seu llms.txt na marcação do esquema, incluindo-o no esquema do seu site como um alvo de ação potencial. Consulte suas páginas marcadas com esquema mais importantes na seção de páginas principais do llms.txt.

Isso cria um sistema de descoberta de duas camadas: os agentes que começam com llms.txt encontram páginas marcadas pelo esquema mais rapidamente, e os agentes que começam com uma página específica podem navegar até llms.txt para ver a imagem completa do site.

## Comparação: com vs sem llms.txt

| Métrica | Sem llms.txt | Com llms.txt |
|
---|
---|
---|
| Taxa de descoberta de agentes | Abaixo de 10 por cento | Até 80 por cento |
| Tempo para a primeira interação do agente | Dias (rastreamento obrigatório) | Segundos (leitura de arquivo único) |
| Precisão de extração | Variável (depende da qualidade da página) | Alto (resumo estruturado) |
| Taxa de retorno do agente | Baixo | Significativamente mais elevado |

## Erros comuns

Escreva llms.txt como texto de marketing. Os agentes não respondem à persuasão. Eles respondem a fatos estruturados. Cada linha deve responder a uma pergunta específica sobre o que seu site pode fazer.

Lista de todas as páginas do site. llms.txt não é um mapa do site. Inclua apenas as páginas mais importantes para a interação do agente. Para um site de 500 páginas, o llms.txt deve fazer referência entre 10 e 30 páginas principais.

Esquecendo de atualizá-lo. Um llms.txt que faz referência a endpoints desatualizados ou produtos descontinuados prejudica ativamente a confiança do agente. O [Guia de implantação do AEO] (/docs/implement-aeo/) aborda como o llms.txt se encaixa no caminho de otimização mais amplo.

---

## Perguntas frequentes

**Onde exatamente o llms.txt deve ser colocado?**
Na raiz do seu domínio: seudominio.com/llms.txt. Os agentes procuram exatamente neste caminho, semelhante ao robots.txt.

**Que formato devo usar para llms.txt?**
Desconto. Use títulos para seções e texto simples para descrições. Sem HTML, sem JSON, sem formatos personalizados.

**Qual deve ser o tamanho do llms.txt?**
Uma ou duas páginas de texto conciso. Tempo suficiente para cobrir suas principais ofertas e endpoints. Curto o suficiente para que um agente possa processá-lo em uma única leitura.

**O llms.txt deve incluir informações sobre preços?**
Sim, se o seu preço for público. Inclua preços base, modelo de preços (por assento, por uso, taxa fixa) e onde encontrar informações detalhadas sobre preços.

**Posso ter llms.txt diferentes para subdomínios diferentes?**
Sim. Cada subdomínio deve ter seu próprio llms.txt que descreve os recursos específicos desse subdomínio.

## Guias relacionados

* [Protocolos de Agente AI](/es/docs/protocols/)
* [camada de execução](/es/docs/execution-layer/)

## Referências primárias* [Guia do Google para recursos de IA generativa](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide)
* [Noções básicas da Pesquisa Google](https://developers.google.com/search/docs/essentials)