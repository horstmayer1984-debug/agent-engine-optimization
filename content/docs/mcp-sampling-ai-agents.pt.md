---
title: "Amostragem MCP explicada: como os servidores solicitam."
date: 2026-05-23
weight: 133
category: "Architecture"
description: "A amostragem MCP permite que os servidores solicitem gerações de modelos por meio de um cliente. Descubra como funciona, onde ajuda e por que é importante."
summary: "Uma explicação prática para amostragem MCP, cobrindo gerações de LLM solicitadas pelo servidor, controle de cliente, preferências de modelo, segurança e implicações de AEO."
keywords:
  - "Amostragem MCP"
  - "amostragem/criação de mensagem"
  - "Amostragem de protocolo de contexto de modelo"
  - "Arquitetura do agente de IA"
  - "Servidores MCP"
---
# Amostragem MCP explicada: como os servidores solicitam a saída do modelo de IA

A amostragem MCP permite que um servidor MCP solicite ao cliente a geração de resultados de modelo durante um fluxo de trabalho. O servidor não precisa de sua própria chave de API de modelo. O cliente mantém controle sobre o acesso ao modelo, permissões, revisão e entrega final. Isso torna a amostragem útil para fluxos de trabalho de agente, mas arriscada se os prompts e resultados gerados não forem exibidos claramente ao usuário.

## O que é amostragem MCP?

A [especificação de amostragem de protocolo de contexto de modelo] oficial (https://modelcontextprotocol.io/docs/concepts/sampling) descreve a amostragem como uma forma de os servidores solicitarem gerações LLM de modelos de linguagem por meio de clientes. Na revisão do protocolo 2025-06-18, os clientes que o suportam declaram uma capacidade de `amostragem` e os servidores solicitam uma geração via `sampling/createMessage`.

Isso parece abstrato, então aqui está a versão simples: um servidor de ferramentas pode pedir ao cliente de IA do usuário para pensar, resumir, classificar ou gerar texto como parte de um fluxo de ferramenta.

Para um contexto mais amplo, consulte [APIs MCP vs Agente](/es/docs/mcp-vs-api-for-agents/), [Autorização MCP com OAuth](/es/docs/mcp-authorization-oauth-ai-agents/) e [Aplicativos MCP](/es/docs/mcp-apps-guide/).

## Por que existe amostragem

Sem amostragem, um servidor MCP tem duas opções limitadas:

- retornar dados brutos e esperar que o modelo do cliente saiba o que fazer
- ligue diretamente para seu próprio fornecedor de modelo, o que aumenta questões de custo, privacidade e gerenciamento de chaves

A amostragem cria um caminho intermediário. O servidor pode solicitar trabalho de modelo, mas o cliente ainda é o porteiro.

## Amostragem versus ferramentas versus recursos

| Função MCP | Quem o controla? Objetivo principal | Exemplo |
|
---|
---|
---|
---|
| Ferramentas | O modelo invoca a ação do servidor | Execute um recurso | "Criar um ticket" |
| Recursos | O servidor expõe o contexto | Fornecer dados para o modelo | "Leia o esboço do projeto" |
| Direções | Servidor expõe modelos | Guie um fluxo de trabalho controlado pelo usuário | "Executar mensagem de revisão de código" |
| Amostragem | O servidor solicita a saída para o modelo do cliente | Gerar ou raciocinar durante um fluxo de trabalho | “Resuma este documento recuperado” |

A amostragem não substitui ferramentas. É uma forma de aninhar a geração de modelo dentro de um recurso.

## Exemplos de casos de uso

A amostragem pode ajudar quando um servidor precisa de resultados de modelo de linguagem, mas não deve possuir o relacionamento do modelo.

Padrões úteis incluem:

- resumir os documentos recuperados
- compor uma resposta depois que uma ferramenta busca dados
- classificar tickets de suporte
- gerar uma explicação em linguagem natural a partir de dados estruturados
- peça ao modelo cliente para transformar o contexto fornecido pelo usuário
- opções de pontuação baseadas em critérios visíveis ao usuárioPara AEO, isso é importante porque sites e APIs legíveis por agentes podem precisar oferecer suporte a fluxos de trabalho que combinem recuperação, execução e explicação.

## Requisitos de segurança e revisão

A especificação da amostragem enfatiza a revisão humana. As inscrições devem facilitar a revisão de solicitações de amostra, a edição de solicitações antes de enviá-las e a revisão das respostas geradas antes da entrega.

Essa é uma exigência séria. Caso contrário, a amostragem pode se tornar uma chamada de modelo oculta acionada por um servidor que o usuário mal entende.| Risco | Por que é importante | Corrimão |
|
---|
---|
---|
| Injeção rápida oculta | O servidor pode incluir instruções inseguras | Mostrar instruções antes da execução |
| Vazamento de dados | O contexto pode conter informações confidenciais | Permitir que os usuários revisem o contexto compartilhado |
| Surpresas de custos | Chamadas de modelo podem consumir tokens pagos | Modelo de visualização e política de custos |
| Saída incorreta | A resposta gerada pode ser imprecisa | Revisão antes da entrega final |
| Excesso de servidor | Servidor pode solicitar trabalho de modelo desnecessário | Exigir suporte de capacidade explícito |

O guia [Agent Observability Guardrails](/es/docs/agent-observability-guardrails/) estende essa camada de governança.

## Implicações do AEO

A amostragem MCP recompensa o contexto limpo. Se seus documentos, respostas de API, dados de produtos ou descrições de fluxo de trabalho forem vagos, o modelo do cliente terá uma tarefa mais difícil. Se estruturados, concisos e vinculados internamente, os fluxos de trabalho baseados em amostragem podem produzir melhores respostas posteriores.

Para proprietários de sites, isso significa:

- publicar definições claras
- manter as respostas da API estruturadas
- expor documentos legíveis por máquina
- evite enterrar limitações importantes na prosa
- documentar páginas de origem da verdade
- fornecer identificadores estáveis para entidades e ações

O [Guia do desenvolvedor AEO](/es/docs/developers-guide-aeo/) é o próximo passo natural.

## Perguntas frequentes

### O MCP Sampling permite que um servidor chame qualquer modelo que desejar?

Não. O cliente controla o acesso ao modelo. O servidor pode expressar preferências, mas o cliente decide o que está disponível e permitido.

### A amostragem é necessária para servidores MCP?

Não. É uma capacidade do cliente. Muitos fluxos de trabalho do MCP podem usar ferramentas, recursos e prompts sem amostragem.

### A amostragem para produção é segura?

Ele pode ser usado com cuidado, mas precisa de uma revisão rápida, revisão de contexto, logs, limites de permissão e padrões sensatos.

### Por que a amostragem é importante para o AEO?

Isso mostra que os fluxos de trabalho dos agentes podem solicitar aos modelos que raciocinem sobre seu conteúdo durante a execução, e não apenas recuperem páginas. O conteúdo estruturado e baseado na fonte torna-se mais útil.

## Conclusão A amostragem MCP é uma ponte útil entre a execução da ferramenta e o raciocínio do modelo. Trate-o como um recurso controlado, não como um atalho em segundo plano.