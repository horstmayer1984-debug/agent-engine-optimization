---
title: "Autorização MCP: OAuth para agentes de IA."
metaTitle: "Autorização MCP para agentes de IA: Guia OAuth."
date: 2026-05-17
weight: 114
category: "Architecture"
description: "A autorização MCP define como os agentes de IA acessam ferramentas restritas por HTTP. Aprenda OAuth, metadados de recursos protegidos."
summary: "Um guia prático para autorização MCP para agentes de IA, abrangendo fluxos OAuth, metadados de recursos protegidos, registro de clientes, escopos e preparação de OAO."
keywords:
  - "Autorização MCP"
  - "OAuth do MCP"
  - "Autorização do agente de IA"
  - "metadados de recursos protegidos"
  - "controle de acesso do agente"
---
Autorização #MCP: OAuth para agentes de IA

A autorização do MCP é importante porque as ferramentas do agente geralmente precisam de acesso restrito. As ferramentas públicas podem ser descobertas livremente, mas os fluxos de trabalho reais precisam de identidade, consentimento, escopos e trilhas de auditoria. A especificação de autorização MCP explica como os transportes MCP baseados em HTTP podem usar autorização no estilo OAuth para servidores MCP restritos.

## O que diz a especificação MCP

A especificação de autorização do Model Context Protocol define recursos de autorização no nível de transporte para transportes baseados em HTTP. A especificação atual faz referência a OAuth, metadados de recursos protegidos, registro dinâmico de cliente e requisitos de segurança.

Fontes primárias:

- [Especificação de autorização MCP](https://modelcontextprotocol.io/specification/2025-11-25/basic/authorization)
- [Roteiro MCP 2026](https://modelcontextprotocol.io/development/roadmap)
- [Guia MCP vs API neste site](/es/docs/mcp-vs-api-for-agents/)

## Por que a autorização é um problema de AEO

A [camada de execução](/es/docs/execution-layer/) não é útil se cada ação for pública ou se cada ação exigir que um ser humano copie manualmente as credenciais. Os agentes precisam de acesso controlado.

Exemplos:

- um agente de compras verifica o preço do contrato
- um agente de suporte lê o status do ticket
- um agente de viagens modifica uma reserva
- um agente financeiro recupera faturas
- um agente desenvolvedor abre uma ferramenta de implantação

Todo fluxo de trabalho precisa de uma resposta clara: para quem o agente atua, o que ele pode fazer, quanto tempo dura o acesso e como o acesso pode ser revogado?

## MCP público vs MCP restrito

| Tipo de servidor MCP | Exemplo | Autorização necessária |
|
---|
---|
---|
| Público somente leitura | Catálogo de produtos, pesquisa de documentos, preços públicos | Geralmente nenhum |
| Ação pública | Assinatura de boletim informativo, solicitação de listagem pública | Controles anti-abuso de baixa fricção |
| Leitura do escopo do usuário | Detalhes da conta, status do pedido | OAuth e consentimento do usuário |
| Gravação do escopo do usuário | Reserva, pagamento, cancelamento | Escopos Robustos, Confirmação, Registros de Auditoria |
| Ferramenta de administração | Implementação, configuração de faturamento | Aprovação humana e política rigorosa |

A maioria das empresas deveria começar com ações públicas somente leitura ou de baixo risco antes de expor ferramentas somente para usuários.

## Principais conceitos de autorização

| Conceito | Significado de agentes |
|
---|
---|
| Proprietário do recurso | O usuário ou organização para a qual o agente atua |
| Cliente MCP | O cliente agente solicitando acesso |
| Servidor de autorização | O sistema que concede tokens |
| Metadados de recursos protegidos | Informações legíveis por máquina sobre servidores de autorização |
| Escopo | Permissão específica como leitura de pedidos ou criação de reservas |
| Token de acesso | Credencial usada para solicitação MCP |Esses conceitos não são novos, mas os agentes os tornam mais importantes porque o ator não é mais sempre um ser humano em um navegador.

## Lista de verificação de implantação

1. Classifique as ferramentas MCP por risco.
2. Mantenha as ferramentas de descoberta pública separadas das ferramentas restritas.
3. Defina o escopo por ação e não por ampla área de produto.
4. Publique metadados de autorização onde os clientes possam descobri-los.
5. Use tokens de curta duração para ações de maior risco.
6. Registre a identidade do agente, a identidade do usuário, o nome da ferramenta, o resumo de entrada e o status do resultado.
7. Adicione confirmação humana para ações irreversíveis ou dispendiosas.O [guia de proteção e observabilidade do agente](/es/docs/agent-observability-guardrails/) estende isso ao monitoramento operacional.

## Exemplo de design de escopo

| Alcance ruim | Melhores escopos |
|
---|
---|
| `acesso_conta` | `orders.read`, `orders.cancel`, `invoices.read` |
| `reserva` | `availability.read`, `booking.create`, `booking.cancel` |
| `administrador` | `users.invite`, `billing.read`, `settings.update` |

Os agentes funcionam melhor quando os escopos são explícitos. As equipes de segurança funcionam melhor quando os escopos correspondem às ações comerciais.

## Requisitos de documentação do AEO

Se o seu site oferecer ferramentas MCP restritas, sua documentação pública deverá explicar:

- quais ferramentas existem
- quais ferramentas são públicas
- requerendo autorização
- quais escopos são solicitados
- se for necessária uma etapa de confirmação humana
- como funcionam os registros e a revogação

Adicione links para esses documentos de [llms.txt](/es/docs/programming-llms-txt/) para que os agentes possam descobrir o modelo de acesso antes de tentar chamar as ferramentas.

## Erros comuns

| Erro | Por que falha |
|
---|
---|
| Um token amplo para todas as ferramentas | Demasiada agência e fraca auditabilidade |
| Nenhuma documentação de capacidade pública | Agentes não conseguem agendar acesso |
| Tokens de longa duração para ações de escrita | Maior dano se comprometido |
| Sem revogação | Os usuários não podem interromper o acesso delegado |
| Trate a identidade do agente como identidade do usuário | Desfoca a responsabilidade |

## Perguntas frequentes

### Todos os servidores MCP precisam de OAuth?

Não. Servidores públicos somente leitura podem não exigir autorização. Ferramentas restritas ou com escopo de usuário geralmente são.

### A autorização do MCP está pronta para produção?

A especificação existe e está evoluindo. As equipes devem seguir a versão atual e verificar a compatibilidade cliente/servidor antes do uso em produção.

### O que são metadados de recursos protegidos?

Os metadados são o que ajuda os clientes MCP a identificar os servidores de autorização associados a um recurso protegido.

### Como isso afeta o AEO?

É mais provável que os agentes utilizem serviços que descrevam claramente as ferramentas, permissões e fluxos de acesso disponíveis.

### Os agentes devem ter acesso de administrador? Somente em ambientes internos rigidamente controlados, com registros, aprovações e revogações rigorosos.