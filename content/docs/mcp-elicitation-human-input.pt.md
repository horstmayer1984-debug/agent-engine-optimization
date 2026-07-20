---
title: "Obtenção de MCP: contribuição humana para fluxos de trabalho."
date: 2026-05-23
weight: 134
category: "Architecture"
description: "A Elicitação MCP permite que os servidores solicitem entradas estruturadas do usuário por meio do cliente. Saiba quando ajuda, o que não pedir e como."
summary: "Um guia prático para obter MCP, entrada estruturada do usuário, fluxos de aceitação/rejeição/cancelamento, design humano no circuito e implicações do fluxo de trabalho AEO."
keywords:
  - "Elicitação MCP"
  - "provocar/criar"
  - "agentes humanos no circuito"
  - "Entrada do usuário MCP"
  - "segurança do fluxo de trabalho do agente"
---
# Obtenção de MCP: contribuição humana para fluxos de trabalho de agentes mais seguros

A Elicitação MCP permite que um servidor MCP solicite informações estruturadas do usuário por meio do cliente enquanto um fluxo de trabalho está em execução. É útil quando um agente precisa de detalhes faltantes, mas não deve ser usado para informações confidenciais. Um bom design de obtenção torna os fluxos de trabalho dos agentes mais seguros porque os usuários podem aceitar, rejeitar ou cancelar solicitações em vez de passar pela automação oculta.

## O que o MCP está ganhando?

A [especificação de busca MCP] oficial (https://modelcontextprotocol.io/docs/concepts/elicitation) descreve uma maneira padrão para os servidores solicitarem informações adicionais do usuário por meio do cliente. Os servidores enviam uma solicitação de `elicitação/criação` com uma mensagem e um esquema JSON restrito para a resposta esperada.

O usuário pode responder de três maneiras:

- aceitar com dados
- declínio
- cancelar

Esse modelo de resposta simples é importante. Oferece ao cliente uma maneira clara de manter o controle do usuário.

Para arquitetura relacionada, leia [MCP vs Agent API](/es/docs/mcp-vs-api-for-agents/), [Agent UX e Human-in-the-Loop Design](/es/docs/agent-ux-human-in-the-loop/) e [MCP Authorization with OAuth](/es/docs/mcp-authorization-oauth-ai-agents/).

## Por que existe a elicitação

Os agentes geralmente começam com instruções incompletas. Um servidor pode estar faltando um campo antes de poder concluir uma tarefa.

Exemplos:

- "A qual projeto esse número deve ser atribuído?"
- "Que data o relatório deve cobrir?"
- "Qual endereço de entrega deve ser usado?"
- "Qual ambiente a implantação deve ter como alvo?"
- "Qual fornecedor aprovado deve ser utilizado o pedido?"

Sem um fluxo de entrada padrão, os servidores podem inventar padrões de prompt inconsistentes ou pedir ao modelo para adivinhar. A elicitação dá a essa interação um caminho estruturado.

## Elicitação vs. perguntas normais de bate-papo

| Recurso | Pergunta normal do bate-papo | Obtenção de MCP |
|
---|
---|
---|
| Origem do pedido | Assistente ou usuário | Servidor MCP via cliente |
| Formato de resposta | Texto livre | Esquema estruturado |
| Opções do usuário | Normalmente responde ou ignora | Aceitar, rejeitar, cancelar |
| Validação | Dependente do modelo | O cliente pode validar campos |
| Postura de segurança | Varia | Spec alerta contra solicitações de dados confidenciais |

Elicitação não é simplesmente “fazer uma pergunta ao usuário”. É uma solicitação de entrada padronizada estruturada no fluxo de trabalho de um agente.

## Quais servidores não devem solicitar

A especificação MCP diz que os servidores não devem usar get para solicitar informações confidenciais. Na prática, evite solicitar:

- senhas
- chaves privadas
- números de cartão de pagamento
- códigos de acesso de uso único
- tokens de acesso brutos
- dados pessoais confidenciais
- segredos que pertencem a um cofre seguro. Se um fluxo de trabalho exigir autorização confidencial, use um fluxo de autenticação apropriado, não um get. A [camada de execução](/es/docs/execution-layer/) depende de limites confiáveis.

## Bons casos de uso

| Caso de uso | Bom campo de obtenção | Campo de obtenção ruim |
|
---|
---|
---|
| Triagem de apoio | Nível de prioridade | Senha do cliente |
| Implementação | Ambiente alvo | Chave raiz da nuvem |
| Aquisições | Fornecedor aprovado | Número completo do cartão |
| Publicação de conteúdo | Categoria do artigo | Senha do administrador do CMS |
| Planejamento de viagem | Aeroporto preferido | Digitalização de passaporte |

O padrão é simples: provocar preferências e escolhas não sensíveis e não secretas.

## Implicações do AEOA obtenção é importante para empresas legíveis pelos agentes porque nem todas as ações podem ser completamente autônomas. Às vezes, a melhor experiência do usuário é uma pausa clara:

“Posso continuar, mas preciso de uma opção aprovada.”

Sites e APIs que se preparam para isso podem publicar:

- requisitos de ação claros
- valores de parâmetros permitidos
- regras de confirmação
- trilhas de escalada
- exemplos de entradas válidas
- mensagens de erro que os agentes podem entender

Isso transforma formas humanas vagas em fluxos de trabalho amigáveis aos agentes. O guia [Sites de programação de agentes de IA](/es/docs/programming-websites-for-ai-agents/) cobre mais desse trabalho de preparação.

## Lista de verificação de design

1. Peça apenas as informações mínimas que faltam.
2. Mostra qual servidor está solicitando as informações.
3. Use rótulos que os usuários possam entender.
4. Valide as entradas antes de enviá-las.
5. Ofereça opções de recusa e cancelamento.
6. Nunca peça segredos obtendo segredos.
7. Registre o tipo de solicitação, servidor e resultado.
8. Mantenha as ações de alto risco atrás da confirmação.

## Perguntas frequentes

### Obter o MCP é um formulário?

Você pode gerar uma interface de usuário semelhante a um formulário, mas o próprio protocolo define a solicitação estruturada e o padrão de resposta, não uma interface específica.

### O Elicitation pode solicitar objetos aninhados?

A especificação limita os esquemas a estruturas planas mais simples com valores primitivos. Isso torna a implantação do cliente mais fácil e segura.

### A Elicitación deve coletar detalhes de pagamento?

Não. As credenciais de pagamento e outros segredos devem usar autorização ou fluxos de pagamento seguros, e não aquisição.

### Por que isso é importante para proprietários de sites?

Os fluxos de trabalho prontos para os agentes precisam de momentos claros em que os agentes possam solicitar aos humanos as opções que faltam, em vez de adivinhar. A elicitação dá a esse padrão uma forma padrão.

## Conclusão

A elicitação de MCP é um pequeno recurso com uma grande lição de design: os agentes seguros devem perguntar claramente quando precisam de intervenção humana, e os usuários devem ter uma opção real de dizer não.