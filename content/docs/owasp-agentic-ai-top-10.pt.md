---
title: "OWASP Agentic AI Top 10 e segurança AEO."
date: 2026-05-17
weight: 117
category: "Guide"
description: "OWASP Agentic AI Top 10 explica os riscos dos agentes autônomos. Descubra como as equipes AEO devem lidar com agência, ferramentas e memória."
summary: "Um guia prático de segurança AEO baseado no OWASP Top 10 for Agentic Applications, com controles para ferramentas, memória, identidade, permissões e monitoramento."
keywords:
  - "Os 10 principais agentes de IA da OWASP"
  - "Agente de segurança de IA"
  - "Segurança AEO"
  - "Riscos dos agentes de IA"
  - "governança de agente autônomo"
---
#OWASP Agentic AI Top 10 e Segurança AEO

OWASP Agentic AI Top 10 é importante para o AEO porque os sites prontos para agentes expõem ações, ferramentas, APIs, memória e pagamentos. Estas capacidades só criam valor se forem controladas. Um site que permite que os agentes atuem sem autorização, limites, supervisão e caminhos de recuperação não está pronto para o agente. Está apenas exposto.

## O que OWASP publicou

O projeto Gen AI Security da OWASP publicou o Top 10 Agent Applications 2026 como uma estrutura para riscos de segurança em sistemas de IA autônomos e de agentes. Destina-se a sistemas que planejam, agem e tomam decisões em todos os fluxos de trabalho.

Fontes primárias:

- [OWASP Top 10 para aplicativos de agente 2026](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [Estrutura de gerenciamento de risco de IA do NIST] (https://www.nist.gov/itl/ai-risk-management-framework)
- [Segurança da Microsoft: Os 10 principais riscos do OWASP na IA do agente](https://www.microsoft.com/en-us/security/blog/2026/03/30/addressing-the-owasp-top-10-risks-in-agentic-ai-with-microsoft-copilot-studio/)

## Por que isso pertence ao AEO

A [camada de execução](/es/docs/execution-layer/) permite que os agentes façam coisas: reservar, comprar, atualizar, recuperar, comparar e ativar fluxos de trabalho. É precisamente por isso que a segurança é importante.

O risco tradicional do SEO é principalmente a reputação e a indexação. O risco AEO inclui:

- ações não autorizadas
- agência excessiva
- uso indevido de ferramentas
- envenenamento de memória
- vazamento de contexto
- delegação insegura
- erros de pagamento
- mudanças de estado irreversíveis

O objetivo não é impedir o acesso do agente. O objetivo é expor as ações corretas com os controles corretos.

## Mapa de controle de segurança AEO

| Superfície AEO | Pergunta de segurança | Controle mínimo |
|
---|
---|
---|
| Conteúdo público | Os agentes podem confiar nele? | Fontes, datas, clareza da entidade |
| llms.txt | Orientar os agentes com segurança? | Vincular apenas recursos estáveis ​​e relevantes |
| Ferramentas MCP | Quem pode ligar para eles? | Autorização e âmbito |
| Ferramentas WebMCP | Os agentes do navegador podem fazer uso indevido de formulários? | Confirmações e validações |
| Pontos finais de pagamento | A despesa pode ser evitada? | Orçamentos, idempotência, receitas |
| Memória do agente | O contexto malicioso pode persistir? | Isolamento e expiração |
| Registros | As ações podem ser auditadas? | ID do agente, ID do usuário, ferramenta, resultado |

O [guia de observabilidade do agente](/es/docs/agent-observability-guardrails/) aborda o monitoramento com mais detalhes.

##Agência excessiva

A agência excessiva ocorre quando um agente é capaz de fazer mais do que o usuário ou a empresa pretendia. Nos termos do AEO, esta é a diferença entre “verificar disponibilidade” e “reservar e pagar sem confirmação”.

Use permissões limitadas:

- leia apenas antes de escrever
- orçamento antes da compra
- solicitação antes da confirmação
- sandbox antes da produção
- aprovação humana diante de ações irreversíveis

O [guia de autorização MCP] (/docs/mcp-authorization-oauth-ai-agents/) explica como os escopos ajudam a manter as ferramentas limitadas.

## Ferramentas e fluxo de trabalho As ferramentas do RiskAgent devem ser projetadas como APIs de produção, não como atalhos de demonstração.

Um bom design de ferramenta inclui:

- entradas digitadas
- saídas escritas
- limpar mensagens de erro
- validação de entrada
- chaves de idempotência
- limites de taxa
- regras de repetição
- registro de auditoria
- acesso com privilégios mínimos

Se uma ferramenta pode gastar dinheiro, alterar dados de clientes ou desencadear processos judiciais, ela precisa de controles mais rígidos do que um endpoint de conteúdo público.

## Riscos de memória e contexto

Os agentes podem transmitir contexto por meio de tarefas. Isso cria conveniência e risco.

Os problemas incluem:- memória envenenada por conteúdo malicioso
- instruções desatualizadas
- vazamento entre clientes
- instruções escondidas no conteúdo recuperado
- dados de política desatualizados

Para os AEOs, as páginas públicas devem ser escritas para que os agentes possam distinguir factos, alegações de marketing, instruções e limitações. Não esconda as instruções de operação no conteúdo decorativo.

## Sinais de confiança para o agente

Os sinais de confiança devem ser visíveis tanto para humanos como para máquinas:

- identidade organizacional clara
- página de contato
- política de privacidade
- página de segurança ou conformidade, quando relevante
- atualizar datas para conteúdo confidencial
- links de fontes para afirmações factuais
- permissões de ferramentas documentadas
- Status da API ou página de informações de saúde

A [auditoria de prontidão AEO](/es/docs/audit/) deve incluir controles de segurança antes que qualquer fluxo de trabalho de agente de alto risco seja ativado.

## Perguntas frequentes

### O OWASP Agentic AI Top 10 é apenas para desenvolvedores?

Não. É útil para equipes de produtos, segurança, jurídicas e SEO/AEO porque a exposição do agente afeta o conteúdo, as ferramentas, os fluxos de trabalho e a governança.

### Qual é o maior erro de segurança do AEO?

Dê aos agentes amplo acesso de gravação antes de projetar escopos, confirmações, limites e logs.

### A segurança reduz a visibilidade do agente?

Uma boa segurança pode melhorar a confiança. Os agentes preferem sistemas com permissões previsíveis e erros recuperáveis.

### Toda ação do agente deve exigir aprovação humana?

Não. As ações de baixo risco podem ser automáticas. As ações de alto risco, dispendiosas, regulamentadas ou irreversíveis deverão exigir uma confirmação mais forte.

### Como as equipes devem começar?

Faça um inventário de cada ação do agente, classifique os riscos e adicione controles antes de expandir o acesso à camada de execução.