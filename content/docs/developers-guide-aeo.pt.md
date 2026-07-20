---
title: "Como os desenvolvedores podem criar sites."
metaTitle: "Guia do desenvolvedor para sites prontos para agentes e AEO."
date: 2026-03-22
weight: 20
category: "Guide"
description: "Um guia técnico para desenvolvedores que criam sites prontos para agentes. Abrange dados estruturados, design de API e testes de sandbox."
metaDescription: "Cree sitios web listos para agentes con datos estructurados, diseño de API, pruebas de espacio aislado, autenticación, optimización del servidor y rutas."
summary: "Os desenvolvedores devem ir além do web design centrado no ser humano. Este guia aborda os requisitos técnicos para que sites possam ser operados por agentes autônomos de IA na camada de tempo de execução."
keywords:
  - "AEO para desenvolvedores"
  - "desenvolvimento de site pronto para agente"
  - "desenvolvimento da camada de tempo de execução"
  - "dados estruturados para agentes de IA"
  - "Design de API para agentes."
  - "Desenvolvimento de servidor MCP"
---
# Como os desenvolvedores podem criar sites para Agent Engine Optimization

A maioria dos sites é projetada para humanos. Uma pessoa lê uma manchete, escaneia um parágrafo, clica em um botão, preenche um formulário. Esse modelo funcionou por duas décadas. Não funciona para agentes autônomos de IA.

Um agente não verifica. É extraído. Não clica nos botões. Pontos de extremidade de chamada. Não tolera ambiguidade. Necessita de contributos determinísticos, resultados previsíveis e restrições explícitas. Se o seu site não puder fornecer isso, o agente segue em frente.

Este guia aborda o trabalho técnico necessário para tornar um site operável na [camada de tempo de execução](/es/docs/execution-layer/), a parte do Agent Engine Optimization que vai além da legibilidade do conteúdo.

## Dados estruturados são o mínimo, não o objetivo

Quando um ser humano vê “$ 50” na página de um produto, o contexto preenche a lacuna. Um agente precisa de tags explícitas: o preço é 50, a moeda é USD, a disponibilidade é InStock, a oferta é válida até uma data específica.

A marcação Schema.org (JSON-LD) cuida do básico. Produto, oferta, página de perguntas frequentes, serviço, organização. Mas os dados estruturados por si só servem apenas à camada de leitura. Ajuda os agentes a entender o que uma página diz. Isso não os ajuda a agir.

A camada de execução requer algo mais: caminhos de ação documentados que uma máquina pode seguir sem interpretar HTML.

## Design de API para interação com agentes

A principal mudança técnica é expor as ações como endpoints documentados, e não como fluxos de UI dependentes do navegador.

Para cada ação de alto valor em seu site (reserva, compra, cotação, verificação de disponibilidade), defina:

- a URL do terminal
- parâmetros de entrada necessários com tipos e restrições
- parâmetros opcionais
- formato de resposta esperado
- códigos de erro e seu significado
- limites de taxa
- requisitos de autenticação

Se o seu checkout funcionar apenas por meio de um formulário de várias etapas renderizado em JavaScript, um agente não poderá usá-lo. Se o seu preço exigir a navegação por três menus suspensos e um modal, um agente não poderá acessá-lo.

O [guia de implementação do AEO](/es/docs/implement-aeo/) abrange o quadro estratégico mais amplo. Esta seção se concentra no lado da engenharia.

## Especificações OpenAPI e suporte MCP

Documente suas APIs usando OpenAPI (anteriormente Swagger). Isso dá aos agentes e sistemas de orquestração um contrato legível por máquina sobre como interagir com seus serviços.

Para uma integração mais profunda com sistemas de IA, considere construir um servidor MCP (Model Context Protocol). O MCP permite que os agentes de IA descubram e usem suas ferramentas diretamente. Um manifesto da ferramenta MCP descreve o que seu serviço pode fazer, quais entradas ele precisa e o que ele retorna. Este é o caminho mais direto para a interoperabilidade dos agentes atualmente. A [visão geral do protocolo](/es/docs/protocols/) compara MCP com UCP, A2A e ACP.

## Ambientes sandbox para testes de agentes

Os agentes cometerão erros durante o desenvolvimento. Eles enviarão solicitações malformadas, acionarão casos extremos e tentarão ações em sequências inesperadas.

Crie um ambiente sandbox que espelhe seu sistema de produção, mas seja executado em dados de teste. Este ambiente deve:

- aceitar as mesmas chamadas de API da produção
- retornar dados realistas, mas falsos
- registre todas as interações para depuração
- simular condições de erro sob demanda
- nunca toque em dados reais de clientes ou sistemas de pagamentoSem um sandbox, os fluxos de trabalho dos agentes não podem ser testados com segurança. E sem testes, você não pode saber se seu site realmente funciona na camada de tempo de execução.

## Autenticação e autorização para agentes

Quando um agente atua em nome de um usuário, seu sistema deve verificar duas coisas: se o agente está autorizado a agir e se o usuário concedeu permissão para a ação específica.

OAuth 2.0 com tokens de acesso com escopo lida bem com isso. O agente recebe um token com permissões específicas (ler dados do produto, iniciar compra, verificar o status do pedido) e apresenta esse token a cada solicitação. Seu sistema valida o token, verifica o escopo e executa ou rejeita a ação.

Nunca permita que os agentes operem com credenciais completas de usuário. Os tokens com escopo limitado limitam o raio de explosão de erros ou agentes comprometidos.

## Desempenho do servidor para fluxos de trabalho de agentes

Os agentes processam mais rápido que os humanos e têm menos paciência. Um ser humano poderia esperar 3 segundos para que uma página carregasse. Um agente operando em um fluxo de trabalho de várias etapas atingirá o tempo limite ou reduzirá a confiança após algumas centenas de milissegundos de atraso.

Otimize para:

- tempo de resposta do servidor inferior a 200 ms para operações de leitura
- latência estável e previsível (os agentes penalizam a variação)
- respostas de erro legíveis por máquina (JSON com códigos de erro, não páginas de erro HTML)
- endpoints idempotentes sempre que possível (repetir uma solicitação não deve criar duplicatas)
- downgrade elegante com códigos de status claros

Se sua API retornar uma bela página 404 com links de navegação, um agente receberá lixo. Retorna um objeto JSON com um código de erro, uma mensagem e sugestões de próximas etapas.

## Tratamento automatizado de erros

Cada resposta de erro deve ser processável por máquina. Defina um esquema de erro consistente em todos os endpoints:

- Código de status HTTP (400, 401, 403, 404, 422, 429, 500)
- código de erro legível por máquina (por exemplo, "INVENTORY_UNAVAILABLE")
- mensagem legível por humanos (para registro e depuração)
- comportamento sugerido de nova tentativa (tente novamente após

Se você deseja uma avaliação estruturada da prontidão do agente do seu site, a [Auditoria de prontidão AEO](/es/docs/audit/) avalia a camada de leitura e a camada de execução.

---

## Perguntas frequentes

**Qual é a camada de execução no AEO?**
A camada de execução é a parte da sua infraestrutura digital que permite que os agentes de IA executem ações, não apenas leiam o conteúdo. Inclui APIs, endpoints documentados, mecanismos de autenticação e tratamento de erros legível por máquina.

**Preciso criar uma API específica para agentes de IA?**
Não necessariamente uma API separada. Mas suas APIs existentes devem ser documentadas, estáveis e acessíveis sem exigir interação do navegador. As especificações OpenAPI e os manifestos da ferramenta MCP tornam as APIs existentes compatíveis com os agentes.

**O que é o MCP e por que ele é importante para os desenvolvedores?**
MCP (Model Context Protocol) é um padrão Antrópico que permite que agentes de IA descubram e usem ferramentas externas. A criação de um servidor MCP para o seu serviço possibilita que os agentes de IA o utilizem diretamente, sem trabalho de integração personalizado.**Com que rapidez meu servidor deve responder aos fluxos de trabalho dos agentes?**
Menos de 200 ms para operações de leitura. Os agentes que operam em fluxos de trabalho de várias etapas penalizam respostas lentas ou imprevisíveis, reduzindo a confiança ou ficando sem tempo.

**Que autenticação devo usar para agentes de IA?**
OAuth 2.0 com tokens de acesso com escopo definido. Nunca exponha credenciais completas de usuário aos agentes. Tokens de escopo para ações específicas que o agente está autorizado a executar.

## Referências primárias

* [Estrutura de gerenciamento de risco de IA do NIST](https://www.nist.gov/itl/ai-risk-management-framework)
* [Documentação do Schema.org](https://schema.org/docs/documents.html)