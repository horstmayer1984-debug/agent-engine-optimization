---
title: "Guia de auditoria de navegação do Lighthouse Agentic."
metaTitle: "Auditoria de navegação agente do Lighthouse: Guia AEO."
date: 2026-05-17
weight: 110
category: "Guide"
description: "O Chrome Lighthouse agora inclui verificações experimentais de navegação do agente. Descubra o que significam llms.txt, WebMCP e auditorias."
summary: "Um guia prático para auditorias de navegação do agente Chrome Lighthouse, incluindo verificações de llms.txt, visibilidade da ferramenta WebMCP, pontuação e próximas etapas do AEO."
keywords:
  - "Navegação do agente Lighthouse"
  - "auditar llms.txt"
  - "Auditoria WebMCP"
  - "Navegação do agente SEO"
  - "Auditoria AEO"
---
#Guia de auditoria de navegação Agentic do Lighthouse

A categoria de navegação do agente do Chrome Lighthouse é importante porque incorpora verificações de prontidão do agente em um fluxo de trabalho convencional de auditoria do desenvolvedor. Os testes atuais são experimentais, mas indicam o rumo que a web está tomando: os agentes de IA precisam de resumos legíveis por máquina, ferramentas detectáveis ​​e superfícies de interação determinísticas.

## O que mudou?

O Chrome for Developers agora documenta auditorias do Lighthouse para navegação de agentes. As verificações documentadas incluem uma auditoria `llms.txt` e uma auditoria informativa para ferramentas WebMCP registradas. O Chrome afirma que a categoria é experimental e baseada em padrões propostos, portanto deve ser tratada como uma camada de diagnóstico precoce, e não como uma pontuação final.

Fontes primárias:

- [Chrome: auditoria do Lighthouse llms.txt](https://developer.chrome.com/docs/lighthouse/agentic-browsing/llms-txt)
- [Chrome: pontuação de navegação do agente Lighthouse](https://developer.chrome.com/docs/lighthouse/agentic-browsing/scoring)
- [Chrome: Auditoria de ferramentas WebMCP registradas](https://developer.chrome.com/docs/lighthouse/agentic-browsing/registered-webmcp-tools)

## O que as auditorias comprovam

| Auditoria | O que significa | Resposta Prática AEO |
|
---|
---|
---|
| llms.txt | Verifica se a raiz do site fornece um resumo legível por máquina | Publique um `llms.txt` conciso com links importantes |
| Ferramentas WebMCP registradas | Lista as ferramentas que a página expõe aos agentes do navegador | Adicione nomes de ferramentas e descrições de ações claros |
| Categoria de navegação do agente | Mostra sinais de aprovação/rejeição e preparação informativa | Use como uma lista de verificação técnica, não como uma pontuação de classificação |

A documentação `llms.txt` do Chrome faz uma distinção importante: um arquivo ausente pode ser marcado como Não aplicável porque o arquivo é opcional, mas os erros do servidor são sinalizados. Isso significa que um `llms.txt` quebrado é pior do que nenhum arquivo.

## Por que isso é importante para os AEOs

A [Auditoria de Preparação AEO](/es/docs/audit/) já verifica a descoberta, a camada de leitura, a camada de execução e a confiança. O Lighthouse adiciona uma maneira fácil para os desenvolvedores capturarem alguns desses sinais em um ambiente de ferramentas familiar.

Não substitui uma auditoria completa do AEO. Ajuda os desenvolvedores a validar peças técnicas específicas:

- A raiz do site serve `llms.txt` de forma limpa?
- As ações da página são visíveis como ferramentas WebMCP?
- Os sinais de prontidão do agente experimental são visíveis durante os testes do navegador?

## Como preparar llms.txt

Para navegação do agente, `llms.txt` deve ser curto e útil. Não é um clone do mapa do site.

Um arquivo prático deve incluir:

- finalidade do site
- conceitos básicos
- melhores páginas iniciais
- principais ferramentas ou serviços
- recursos legíveis por máquina
- data de atualização

O [guia llms.txt](/es/docs/programming-llms-txt/) explica como estruturá-lo. A regra principal é simples: ajude o agente a entender o que ler primeiro.

## Como preparar ferramentas WebMCPA auditoria das ferramentas WebMCP registradas é informativa. Se não houver ferramentas cadastradas, a lista estará vazia. Isso não é automaticamente uma falha, mas revela se a página expõe ações de uma forma amigável para o agente do navegador.

Boas primeiras ferramentas incluem:

- solicitar auditoria
- marcar uma consulta
- solicitar orçamento
- adicionar ao carrinho
- verificar disponibilidade
- enviar ticket de suporte
- comparar produtos

O [guia WebMCP](/es/docs/webmcp-agent-ready-websites/) aborda quando usar ferramentas de nível de página versus MCP do lado do servidor.

## Fluxo de trabalho sugerido| Etapa | Ação | Saída |
|
---|
---|
---|
| 1 | Execute o Lighthouse na página inicial e nos modelos importantes | Agentes de referência de sinais de navegação |
| 2 | Corrigir erros de resposta `llms.txt` | Resumo raiz legível por máquina estável |
| 3 | Adicionar WebMCP a uma página de ação de baixo risco | Ferramenta registrada visível |
| 4 | Farol de repetição | Confirmar detecção |
| 5 | Adicionar logs do lado do servidor para ações do agente | Camada de medição |

Este fluxo de trabalho conecta a validação técnica à [camada de execução](/es/docs/execution-layer/). Passar em uma auditoria é menos importante do que provar que um agente pode concluir uma tarefa útil.

## O que não fazer

Não adicione um arquivo `llms.txt` falso apenas para passar na verificação. Não registre ferramentas WebMCP genéricas como `submit_form` sem uma descrição significativa. Não exponha ações de alto risco porque a auditoria existe.

A melhor implementação de navegação do agente é enfadonha: conteúdo claro, ações estáveis, permissões explícitas e bom registro.

## Perguntas frequentes

### A pontuação de navegação do Lighthouse Agent é um fator de classificação?

Nenhuma fonte oficial diz isso. Trate isso como um sinal de prontidão experimental, não como um fator de classificação do Google.

### O llms.txt é necessário?

A documentação do Chrome diz que é opcional no momento. Um arquivo ausente pode ser Não aplicável, enquanto erros do servidor podem ser sinalizados.

### Devo adicionar WebMCP a cada formulário?

Não. Comece com ações de alto valor e baixo risco, nas quais a execução do agente ajudaria os usuários.

### Qual a diferença entre isso e uma auditoria normal de SEO?

As auditorias tradicionais de SEO concentram-se na rastreabilidade, velocidade, metadados e conteúdo. As auditorias de navegação do agente concentram-se em saber se os agentes conseguem compreender e agir no site.

### O que deve ser medido após a implementação?

Rastreie ações acionadas por agentes, preenchimentos de formulários, erros, solicitações inválidas e páginas que os agentes leem antes de agir.