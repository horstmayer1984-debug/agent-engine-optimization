---
title: "Como programar sites para agentes de IA: 5 elementos."
metaTitle: "Como programar sites para agentes de IA."
date: 2026-04-12
weight: 60
category: "Architecture"
description: "Prepare seu site para agentes com llms.txt, especificações OpenAPI, endpoints MCP, HTML semântico e cartões de agente. Inclui sandbox."
metaDescription: "Prepare los sitios web para agentes con llms.txt, OpenAPI, puntos finales MCP, HTML semántico, tarjetas de agente y patrones seguros para producción."
summary: "Os sites estão prontos para agentes adicionando llms.txt para descoberta, especificações OpenAPI com descrições amigáveis ​​para agentes, servidores MCP para acesso dinâmico a ferramentas, HTML semântico para extração e cartões de agente para colaboração A2A."
keywords:
  - "Programação de sites para agentes de IA."
  - "Implementação de llms.txt"
  - "Configuração do servidor MCP"
  - "cartão de agente json"
  - "desenvolvimento de site pronto para agente"
  - "Terminais do agente WebSocket"
---
Os sites estão prontos para agentes, adicionando APIs REST claras, llms.txt, endpoints MCP, HTML semântico e camadas de segurança para que agentes de IA autônomos possam descobrir, compreender e agir sem código fixo personalizado. Abaixo estão os cinco elementos técnicos essenciais, além de dois padrões emergentes que os sistemas de produção necessitarão em 2026.

## 1. Crie llms.txt como mapa do site do agente

Coloque um arquivo Markdown em /llms.txt na raiz do seu site. Ele tem a mesma finalidade para agentes de IA que o arquivo robots.txt para rastreadores de pesquisa: informa ao agente o que seu site oferece, onde encontrá-lo e como interagir com ele.

Um llms.txt útil inclui o nome do seu produto ou serviço e uma descrição de uma frase, uma lista das páginas principais com sua finalidade, endpoints de API disponíveis com descrições curtas, requisitos de autenticação e quaisquer restrições ou limites de velocidade.

Os agentes procuram llms.txt antes de rastrear todo o site. Um site sem site força o agente a adivinhar o que está disponível. Um site com um llms.txt claro e atualizado é descoberto com mais rapidez e compreendido com mais precisão.

Mantenha-o atualizado. Um llms.txt que descreve endpoints que não existem mais prejudica mais a confiança do que não ter nenhum llms.txt. O [guia de programação llms.txt](/es/docs/programming-llms-txt/) cobre o formato em detalhes.

## 2. Escreva especificações OpenAPI com descrições amigáveis ao agente

Se o seu site expõe endpoints de API, documente-os com especificações OpenAPI que incluem exemplos completos de solicitações e respostas, esquemas de erro detalhados com códigos e mensagens de erro específicos, regras de validação de entrada com tipos, intervalos e campos obrigatórios e descrições em linguagem simples do que cada endpoint faz e quando usá-lo.

A maioria das especificações OpenAPI são escritas para desenvolvedores humanos que podem inferir o contexto ausente. Os agentes não podem inferir. Eles precisam documentar cada parâmetro, descrever cada caso de erro e tornar cada restrição explícita.

Um erro comum é escrever descrições concisas de uma linha, como “Criar uma reserva”. Uma descrição amigável ao agente diz "Cria uma reserva para a data e hora especificadas. Requer uma data válida no formato ISO 8601, um intervalo de tempo a partir do final dos slots disponíveis e um e-mail de contato. Retorna um objeto de confirmação com o ID da reserva e o prazo de cancelamento. Falha com 409 se o slot já estiver ocupado."

## 3. Implante um servidor MCP para descoberta dinâmica de ferramentas

O Model Context Protocol (MCP) é o padrão emergente de como os agentes de IA descobrem e chamam ferramentas. Em vez de codificar integrações para cada plataforma de IA, ele expõe seus recursos por meio de um único servidor MCP que qualquer agente compatível pode descobrir e usar. O MCP usa JSON-RPC 2.0 para comunicação. Seu servidor anuncia ferramentas disponíveis (funções que o agente pode chamar), recursos (dados que o agente pode ler) e prompts (modelos que o agente pode usar). Os agentes descobrem esses recursos dinamicamente em tempo de execução.

Um servidor MCP mínimo expõe suas principais ações de negócios como ferramentas: verificar disponibilidade, obter preços, criar reservas, enviar consultas. Cada ferramenta possui um esquema escrito que define entradas e saídas.O investimento é modesto. Um servidor MCP básico em Python ou Node.js leva de 2 a 4 horas para ser construído para um site com 3 a 5 ações principais. A vantagem é que cada agente habilitado para MCP pode interagir imediatamente com seu site.

## 4. Use HTML semântico que sobrevive sem JavaScript

Os agentes normalmente não executam JavaScript. Eles obtêm o HTML bruto e extraem informações da estrutura do documento. Se o seu conteúdo crítico for renderizado no lado do cliente via React, Vue ou Angular sem renderização no lado do servidor, os agentes verão uma página vazia.

Use elementos HTML nativos com semântica clara. Elementos de botão para ações, elementos de formulário para entradas, elementos de tabela para dados estruturados, elementos de cabeçalho para hierarquia. Adicione atributos aria-label quando a finalidade do elemento não for óbvia em seu conteúdo.

O servidor processa todas as informações críticas. Nomes de produtos, preços, disponibilidade, especificações e detalhes de contato devem estar na resposta HTML inicial, não carregados de forma assíncrona.

Tente recuperar sua página com curl e verifique se as informações essenciais estão visíveis na resposta. Caso contrário, os agentes também não poderão vê-lo.

## 5. Publique um cartão de agente para colaboração A2A

Um cartão de agente é um arquivo JSON (agent-card.json) localizado na raiz do seu site que descreve os recursos do site, os requisitos de autenticação e os protocolos suportados para comunicação entre agentes.

O protocolo A2A (Agente para Agente) usa Cartões de Agente para descoberta. Quando um agente precisa encontrar um serviço, ele verifica o Cartão do Agente para determinar se o site pode ajudar, quais recursos estão disponíveis e como autenticar.

Um cartão de agente básico inclui o nome e a descrição do seu serviço, protocolos suportados (MCP, REST, A2A), recursos disponíveis como lista estruturada, método de autenticação e endpoint e informações de contato para relatório de erros.

A publicação de um cartão de agente duplica sua capacidade de descoberta em fluxos de trabalho multiagentes porque os agentes que descobrem seu site podem recomendá-lo a outros agentes no mesmo fluxo de trabalho.

Os [Cartões de Agente e Guia A2A] (/docs/agent-cards-a2a-protocol/) cobrem a especificação completa.

## Padrão emergente: Agent SandboxOs sistemas de agentes de produção precisam de isolamento. Quando um agente externo executa código ou processa dados na sua infraestrutura, ele precisa de contenção.

O sandboxing baseado em WASM (semelhante ao Cloudflare Workers) permite que os agentes executem operações não confiáveis ​​em ambientes isolados com limites de recursos definidos. Isso evita que um agente malcomportado afete outros usuários ou consuma recursos ilimitados.

Para a maioria dos sites, o sandbox não é um requisito do primeiro dia. Torna-se importante quando você expõe terminais de execução que aceitam entradas complexas ou quando vários agentes externos interagem com seu sistema simultaneamente.

## Padrão emergente: endpoints WebSocket em tempo real

APIs REST padrão funcionam para interações únicas de solicitação-resposta. Os fluxos de trabalho do agente em várias etapas se beneficiam das conexões WebSocket que mantêm o estado durante toda a sessão.Um endpoint WebSocket em /ws/agent-session permite que um agente mantenha uma conexão persistente para fluxos de trabalho que envolvem várias etapas sequenciais: verificação de disponibilidade, seleção de opções, confirmação de detalhes e conclusão da transação. Cada etapa ocorre na mesma conexão com estado de sessão compartilhada.

Isso evita comportamentos incomuns que ocorrem quando os agentes fazem diversas chamadas REST independentes e perdem o contexto entre elas.

## Comparação: arquitetura tradicional versus arquitetura otimizada por agente

| Aparência | Site tradicional | Site otimizado para agente |
|
---|
---|
---|
| Descoberta | robots.txt e mapa do site | llms.txt mais Cartão de Agente mais Registro MCP |
| Interação | UI humana baseada em navegador | MCP mais REST mais WebSocket |
| Segurança | Chaves de API estáticas | Autenticação específica do agente mais taxas do agente |
| Entrega de dados | HTML para renderização | JSON estruturado mais HTML semântico |
| Métrica de sucesso | Visualizações de páginas e cliques | Conclusão e retenção de tarefas do agente |

O [guia da camada de execução] (/docs/execution-layer/) explica os princípios arquitetônicos. O [guia de implementação AEO] (/docs/implement-aeo/) cobre todo o caminho de otimização.

---

## Perguntas frequentes

**Preciso de todos os cinco elementos para estar pronto para ser um agente?**
Comece com llms.txt e HTML semântico (a camada de leitura). Adicione especificações OpenAPI e MCP quando você tiver endpoints de API. Adicione o Cartão de Agente quando desejar visibilidade A2A.

**Quanto tempo leva para implantar um servidor MCP básico?**
Duas a quatro horas para um site com 3 a 5 ações principais, supondo que você tenha endpoints de API existentes para ajustar.

**Os agentes ainda funcionarão sem um servidor MCP?**
Sim, usando API REST e extração estruturada de HTML. O MCP torna a descoberta e a interação mais padronizadas e confiáveis, mas não é a única maneira.

**O suporte WebSocket é necessário para sites simples?**Não. WebSockets são importantes para fluxos de trabalho transacionais de várias etapas. Sites de conteúdo simples e endpoints de ação única funcionam bem com REST padrão.

**Como faço para testar se meu site está pronto para agente?**
Recupere suas páginas com curl (sem JavaScript). Verifique a precisão do seu llms.txt. Valide sua especificação OpenAPI. Teste seu servidor MCP com um cliente compatível. Faça perguntas aos assistentes de IA que seu site deve responder.

## Referências primárias

* [Estrutura de gerenciamento de risco de IA do NIST](https://www.nist.gov/itl/ai-risk-management-framework)
* [Documentação do Schema.org](https://schema.org/docs/documents.html)