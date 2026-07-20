---
title: "Cartões de agente e protocolo A2A para sites prontos."
date: 2026-04-12
weight: 63
category: "Architecture"
description: "Como os cartões de agente e o A2A ajudam os agentes autônomos a descobrir recursos, colaborar com segurança e interagir com sites prontos."
summary: "Os Cartões de Agente informam a outros agentes o que seu site pode fazer. O protocolo A2A permite a troca direta de tarefas de agente para agente. Juntos, eles tornam seu site detectável e colaborativo em fluxos de trabalho multiagentes."
keywords:
  - "cartão de agente json"
  - "Protocolo A2A"
  - "protocolo de agente para agente"
  - "colaboração do agente"
  - "implementação de cartão de agente"
  - "descoberta multiagente"
---
Os cartões de agente e o protocolo A2A (agente para agente) permitem que você programe seu site para que agentes autônomos o descubram e colaborem com ele sem que você crie cada integração manualmente. Um Cartão de Agente descreve o que seu site pode fazer. O protocolo A2A define como os agentes trocam tarefas e resultados.

Juntos, eles fazem com que seu site participe de fluxos de trabalho multiagentes, em vez de um endpoint passivo que agentes individuais consultam isoladamente.

## O que contém um Cartão de Agente?

Um cartão de agente é um arquivo JSON (agent-card.json) localizado na raiz do seu site. Ele serve como um manifesto de capacidade legível por máquina que informa aos outros agentes: quem você é, o que pode fazer, como autenticar e quais protocolos você suporta.

Os campos principais: nome (o nome do seu serviço), descrição (o que o seu serviço faz em uma frase), URL (sua URL base), capacidades (uma lista estruturada de ações que seu site pode realizar), protocolos (quais padrões de comunicação ele suporta, como MCP, REST, A2A), autenticação (como os agentes devem autenticar) e contato (onde relatar problemas).

Cada recurso na lista inclui um nome, uma descrição, um esquema de entrada e um esquema de saída. É isso que os agentes usam para decidir se o seu site pode ajudá-los em suas tarefas atuais.

## Por que os cartões de agente são importantes para a descoberta

Em um fluxo de trabalho multiagente, um agente coordenador precisa encontrar serviços que possam lidar com subtarefas específicas. Sem os Cartões de Agente, o coordenador precisa adivinhar com base no conteúdo da página. Com os Agent Cards, o coordenador lê um manifesto estruturado e toma uma decisão de roteamento informada em milissegundos.

Os cartões de agente também permitem encaminhamento. Um agente que usa seu site com sucesso pode passar seu Cartão de Agente para outros agentes que precisam de recursos semelhantes. Isso cria um mecanismo de descoberta boca a boca dentro do ecossistema do agente.

## Noções básicas do protocolo A2A

O protocolo A2A padroniza como os agentes trocam tarefas. Um agente envia uma solicitação de tarefa (o que precisa ser feito, quais entradas estão disponíveis, quais restrições se aplicam). O agente receptor processa a tarefa e retorna um resultado estruturado.

O protocolo lida com o gerenciamento do ciclo de vida das tarefas: criação de tarefas, atualizações de status, conclusão e falhas. Ele também suporta tarefas de longa duração onde o resultado não está disponível imediatamente.

Para o seu site, implementar A2A significa expor terminais de tarefas que aceitam solicitações estruturadas e retornam respostas estruturadas. O formato segue a especificação A2A do Google com objetos de tarefa digitados e enumerações de status.

## Implementação passo a passo

### Etapa 1: Crie agent-card.jsonEscreva o arquivo JSON com a descrição e os recursos do seu serviço. Seja preciso sobre o que cada capacidade faz, quais informações são necessárias e quais resultados produz. Coloque-o na raiz do seu domínio.

### Etapa 2: Adicionar terminais de tarefa A2A

Exponha endpoints que aceitam solicitações de tarefas e retornam resultados de tarefas. É necessária uma implementação mínima: POST /a2a/tasks (criar uma nova tarefa), GET /a2a/tasks/{id} (verificar o status da tarefa) e GET /a2a/tasks/{id}/result (recuperar o resultado completo).

### Etapa 3: Conecte-se ao MCP

Se você já possui um servidor MCP, seus terminais de tarefa A2A podem delegar internamente para ferramentas MCP. A camada A2A cuida da comunicação entre os agentes enquanto o MCP cuida da execução real da ferramenta.

### Etapa 4: Registre-se publicamenteInclua seu cartão de agente nos registros MCP e diretórios de agentes para que agentes fora de sua rede direta possam descobrir seu serviço.

## Colaboração em tempo real com WebSockets

Os padrões padrão de solicitação-resposta funcionam para tarefas simples. Fluxos de trabalho colaborativos em várias etapas se beneficiam das conexões WebSocket.

Um endpoint WebSocket em /ws/agent-collaboration permite que dois agentes mantenham uma conexão persistente para fluxos de trabalho que exigem negociação de ida e volta: verificação de vários slots de disponibilidade, comparação de opções, ajuste de parâmetros com base em resultados intermediários.

Isto é particularmente útil para fluxos de trabalho empresariais onde um agente precisa reservar inventário, verificar opções de envio, aplicar regras de desconto e confirmar autoridade de pagamento em uma sequência coordenada.

## Sandbox do agente para segurança

Quando agentes externos executam tarefas na sua infraestrutura, o sandboxing impede que eles acessem recursos fora do escopo autorizado.

O sandboxing baseado em WASM executa operações enviadas por agente em ambientes isolados com limites de memória, limites de CPU e restrições de acesso à rede definidos.

Para a maioria dos sites, o sandbox se torna relevante quando você expõe endpoints de execução que aceitam entradas complexas ou quando permite que agentes executem lógica personalizada em seu sistema.

## Comparação: MCP vs A2A

| Aparência | PCM | A2A |
|
---|
---|
---|
| Finalidade | Comunicação agente-ferramenta | Comunicação entre agentes |
| Descoberta | Esquemas de ferramentas | Cartões de Agente |
| Padrão de interação | Pedido-resposta único | Ciclo de vida da tarefa com rastreamento de status |
| O melhor para | Execução direta de ferramentas | Fluxos de trabalho colaborativos em várias etapas |
| Sua implementação | Servidor JSON-RPC | Terminais de tarefa mais cartão de agente |

Ambos os protocolos se complementam. O MCP lida com as ferramentas. A2A lida com a colaboração entre agentes usando essas ferramentas. O [artigo multiagente AEO](/es/docs/multi-agent-aeo/) explica como os fluxos de trabalho orquestrados dependem desses protocolos. O [guia MCP vs API](/es/docs/mcp-vs-api-for-agents/) cobre detalhadamente a camada de acesso à ferramenta.

---

## Perguntas frequentes

**Quanto tempo leva para criar um Cartão de Agente?**
Trinta minutos para um Cartão de Agente básico com 3 a 5 capacidades. A estrutura JSON é simples.

**Preciso de MCP e A2A?**
Não necessariamente. Comece com o MCP se sua principal necessidade for que os agentes liguem para suas ferramentas. Adicione A2A quando quiser que os agentes colaborem com seu serviço como pares em fluxos de trabalho multiagentes.

**Qual é a diferença entre um Cartão de Agente e um llms.txt?**
llms.txt é uma visão geral legível por humanos e máquinas do seu site no Markdown. Um cartão de agente é um manifesto de recurso estritamente legível por máquina em JSON. Ambos são para descoberta, mas os Cartões de Agente são mais estruturados e específicos do protocolo.

**Os agentes podem descobrir meu site sem um Cartão de Agente?**
Sim, via llms.txt, marcação de esquema ou rastreamento direto de página. Um cartão de agente acelera a descoberta e permite a colaboração A2A, mas não é o único caminho para a descoberta.

**A2A é apenas para grandes empresas?**
Qualquer site que exiba ações do corretor pode gerar lucros A2A. Mesmo um pequeno serviço com um endpoint de reserva pode participar de fluxos de trabalho multiagentes por meio de um simples cartão de agente e um endpoint de tarefa.## Guias relacionados

* [arquitetura de negociação do agente](/es/docs/agentic-commerce/)

## Referências primárias

* [Especificação do protocolo A2A](https://github.com/a2aproject/A2A/blob/main/docs/specification.md)
* [Especificação do protocolo de contexto do modelo](https://modelcontextprotocol.io/specification/2025-06-18/basic/index)