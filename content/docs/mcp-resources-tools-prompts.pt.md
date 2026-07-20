---
title: "Recursos MCP versus ferramentas versus prompts."
date: 2026-05-23
weight: 135
category: "Guide"
description: "Compare recursos, ferramentas e prompts do MCP. Descubra o que cada recurso faz, quando usá-lo e como projetar integrações de agentes mais claras."
summary: "Uma comparação prática de recursos, ferramentas e prompts do MCP para desenvolvedores que criam sistemas legíveis por agentes e modelam integrações de protocolo de contexto."
keywords:
  - "Recursos PCM"
  - "Ferramentas MCP"
  - "Indicações de PCM"
  - "Recursos do protocolo de contexto do modelo"
  - "integrações de agentes"
---
# Recursos CCM vs. Ferramentas vs. Prompts: A Diferença Prática

Os recursos do MCP fornecem contexto, as ferramentas executam ações e os prompts fornecem instruções reutilizáveis. A diferença é importante porque o mau design do MCP torna os agentes não confiáveis: os dados não devem ser expostos como uma ação, as ações não devem ser ocultadas em prompts e os prompts não devem substituir definições de capacidade estruturadas.

## A versão curta

O protocolo de contexto do modelo possui diversas características de servidor. Três dos mais importantes estão documentados como [recursos](https://modelcontextprotocol.io/docs/concepts/resources), [ferramentas](https://modelcontextprotocol.io/docs/concepts/tools) e [mensagens](https://modelcontextprotocol.io/docs/concepts/prompts).

Use-os assim:

- recursos: "Aqui está um contexto que você pode ler."
- ferramentas: "Aqui está algo que você pode fazer."
- mensagens: "Aqui está um modelo de fluxo de trabalho que o usuário pode escolher."

Para obter mais contexto, consulte [API MCP vs Agent](/es/docs/mcp-vs-api-for-agents/), [Registro MCP](/es/docs/mcp-registry-guide/) e o [Guia do desenvolvedor AEO](/es/docs/developers-guide-aeo/).

## Tabela comparativa

| Recurso | Melhor uso | Quem costuma começar | Exemplo |
|
---|
---|
---|
---|
| Recursos | Expor dados e contexto | Aplicativo cliente ou host | Arquivo, esquema, catálogo de produtos, README |
| Ferramentas | Execute ações ou cálculos | Modelo, com controle usuário/cliente | Criar ticket, consultar banco de dados, calcular cotação |
| Direções | Forneça fluxos de trabalho reutilizáveis ​​| Comando ou seleção controlada pelo usuário | "Revise este código" ou "Rascunho de notas de versão" |

Essa divisão torna as integrações compreensíveis. Os agentes podem raciocinar melhor quando os limites das capacidades são óbvios.

## Para que servem os recursos do MCP?

Os recursos são para contexto. A especificação MCP diz que os recursos permitem que os servidores compartilhem dados como arquivos, esquemas de banco de dados ou informações específicas de aplicativos. Cada recurso possui um URI e pode incluir metadados como tipo MIME, tamanho, título e anotações.

Bons exemplos de recursos:

-`arquivo:///projeto/README.md`
- esquema do banco de dados
- instantâneo do catálogo de produtos
- Documentação de endpoint de API
- configuração atual do projeto
- documento de política

Os recursos devem ser estáveis o suficiente para que um modelo possa inspecioná-los ou referenciá-los. Eles não devem alterar o estado do negócio quando lidos.

## Para que são utilizadas as ferramentas MCP?

Ferramentas são para ações. A especificação oficial das ferramentas diz que os servidores MCP podem expor ferramentas que os modelos de linguagem podem invocar para interagir com sistemas externos, como APIs, bancos de dados ou cálculos.

Bons exemplos de ferramentas:

- `criar_problema`
- `get_order_status`
- `calcular_cotação_de_envio`
- `pesquisa_inventário`
-`submit_refund_request`
- `run_lighthouse_audit`

As ferramentas precisam de esquemas, validação, limites de taxa, controle de acesso e registros de auditoria. A página [proteção de observabilidade do agente](/es/docs/agent-observability-guardrails/) é relevante aqui.

## Para que servem os prompts do MCPOs prompts são modelos reutilizáveis. Eles ajudam usuários ou clientes a acionar um fluxo de trabalho conhecido com argumentos. Uma mensagem pode coletar instruções para revisão de código, redação de conteúdo, integração ou triagem de suporte.

As instruções são úteis quando:

- o fluxo de trabalho é repetível
- o usuário deve selecioná-lo intencionalmente
- o padrão instrucional se beneficia da consistência
- o resultado tem muita linguagem em vez de açãoNão esconda a execução nos prompts. Se algo mudar de estado, pertence a uma ferramenta com confirmação e registro.

## Erros de design a serem evitados

| Erro | Por que causa problemas | Melhor desenho |
|
---|
---|
---|
| Expondo ações como recursos | Ler dados pode causar efeitos colaterais | Utilize ferramentas para ações |
| Usando mensagens como wrappers de API | O modelo pode inferir parâmetros vagamente | Use uma ferramenta com contorno |
| Coloque todo o contexto nas descrições das ferramentas | As descrições ficam infladas | Expor recursos |
| Faça de cada arquivo um recurso | Muito ruído contextual | Priorizar recursos relevantes |
| Sem esquema de saída para ferramentas | Mais difícil para os clientes validarem os resultados | Use resultados estruturados sempre que possível |

## Implicações do AEO

Os sites legíveis por agentes enfrentam o mesmo problema de design que os servidores MCP: conteúdo, instruções e ações separados.

Por exemplo:

- uma página de preços é um contexto público semelhante a um recurso
- uma API de pagamento é uma ação semelhante a uma ferramenta
- um guia do comprador é uma ajuda rápida para o fluxo de trabalho

Uma separação clara ajuda os agentes de IA a entender o que podem ler, o que podem recomendar e o que podem executar. Essa é a base prática do [Agent Engine Optimization](/es/docs/what-is-aeo/).

## Lista de verificação de implantação

1. Liste tudo o que o agente pode ler.
2. Liste todas as ações que o agente pode realizar.
3. Liste os fluxos de trabalho repetidos que os usuários podem invocar.
4. Atribua cada item a um recurso, ferramenta ou mensagem.
5. Adicione esquemas para ferramentas.
6. Adicione metadados úteis para recursos.
7. Mantenha os prompts controlados pelo usuário.
8. Documente permissões e riscos.

## Perguntas frequentes

### Um servidor MCP pode expor recursos, ferramentas e mensagens?

Sim. Muitos hosts úteis exporão todos os três, mas cada recurso deve ter uma função clara.

### Os recursos são mais seguros que as ferramentas?

Geralmente porque os recursos são destinados a ler o contexto. Eles ainda podem expor dados confidenciais se o controle de acesso for fraco.

### O modelo deve invocar prompts automaticamente?

Os prompts geralmente são projetados para serem controlados pelo usuário ou selecionados explicitamente. A ação automática deve ser tratada com cuidado usando ferramentas e permissões.

### Qual é a regra de design de MCP mais importante?

Mantenha os efeitos colaterais nas ferramentas, o contexto nos recursos e as instruções reutilizáveis nos prompts.## Conclusão

Um bom design de MCP envolve principalmente limites claros. Quando recursos, ferramentas e prompts fazem seu próprio trabalho, é mais fácil confiar, depurar e melhorar os agentes.