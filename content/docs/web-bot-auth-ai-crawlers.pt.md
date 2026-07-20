---
title: "Autenticação Webbot para rastreadores de IA: um guia."
date: 2026-05-23
weight: 131
category: "Architecture"
description: "O Web Bot Auth usa assinaturas HTTP criptográficas para verificar bots e agentes automatizados. Descubra como isso se adapta à confiança dos rastreadores."
summary: "Um guia prático para Web Bot Auth para rastreadores de IA, agentes assinados, verificação de rastreadores e design de políticas para sites legíveis por agentes."
keywords:
  - "Autenticação de webbot"
  - "Verificação do rastreador AI"
  - "agentes assinados"
  - "Assinaturas de mensagens HTTP"
  - "identidade do rastreador"
---
Autenticação #Webbot para rastreadores de IA: um guia prático da AEO

Web Bot Auth é uma forma de rastreadores e agentes automatizados provarem sua identidade com assinaturas HTTP criptográficas. Para o AEO, isso é importante porque a identidade do rastreador está se tornando uma camada de confiança: os proprietários de sites devem distinguir tráfego útil de pesquisa, resposta e agente de falsificação, raspagem e abuso.

## O que é autenticação de Web Bot?

A documentação de autenticação do Web Bot da Cloudflare (https://developers.cloudflare.com/bots/reference/bot-verification/web-bot-auth/) descreve-o como um método de autenticação que usa assinaturas criptográficas em mensagens HTTP para verificar se uma solicitação vem de um bot automatizado. A Cloudflare o utiliza para bots verificados e agentes assinados, com base em rascunhos ativos da IETF para diretório de chave pública e comportamento de assinatura de solicitação.

Em termos leigos: um rastreador publica uma chave pública, assina solicitações com sua chave privada e a infraestrutura receptora pode verificar se a solicitação realmente vem desse rastreador.

Este é um problema diferente do [robots.txt para rastreadores de IA](/es/docs/ai-crawlers-robots-txt/). Robots.txt informa o que um rastreador deve fazer. O Web Bot Auth ajuda a provar quem é o rastreador.

## Por que a identidade do rastreador agora é importante

A pesquisa de IA e os agentes autônomos criam uma mistura de tráfego confusa:

- rastreadores de pesquisa clássicos
- Rastreadores de resposta de IA
- treinamento de rastreador
- agentes de navegador que atuam em nome dos usuários
- sistemas de raspagem comercial
- bots falsos usando strings de agente de usuário confiáveis
- scanners e monitores de segurança

Se todos forem parecidos, o proprietário do site terá apenas escolhas rígidas: permitir demais ou bloquear demais. AEO precisa de uma camada intermediária onde agentes confiáveis ​​possam acessar conteúdo público e o tráfego não confiável possa ser desafiado ou limitado.

## Web Bot Auth versus métodos de verificação comuns

| Método | O que isso prova | Força | Fraqueza |
|
---|
---|
---|
---|
| String do agente do usuário | O que afirma o requerente | Fácil de ler | Fácil de falsificar |
| DNS reverso | Se o IP pertencer a um fornecedor conhecido | Maduro para grandes rastreadores | Faixas de IP e mudança de infraestrutura |
| Lista de permissões de IP | A solicitação vem de endereços permitidos | Simples para casais estáveis ​​| Frágil e difícil de escalar |
| Autenticação Webbot | A solicitação é assinada por uma chave registrada | Prova de identidade mais forte | Requer adoção de rastreador e implementação correta |
| Token de login/API | Acesso autorizado à conta | Forte para sistemas privados | Não é adequado para rastejar sozinho em público |

O futuro provável não é que um método substitua todos os outros. É uma verificação em camadas.

## Como funciona o fluxo

Em alto nível:

1. O rastreador gera uma chave de assinatura.
2. O rastreador hospeda um diretório de chaves em um local conhecido.3. O rastreador registra o bot e o diretório de chaves com o provedor de verificação.
4. Após a verificação, o rastreador assina as solicitações.
5. O sistema receptor valida a assinatura e aplica a política.

A documentação da Cloudflare inclui requisitos específicos, como chaves Ed25519, um diretório de chaves, HTTPS e cabeçalhos HTTP assinados.

## Implicações da política AEO

O Web Bot Auth ajuda a responder a uma questão prática: "Essa solicitação de máquina deve ser confiável o suficiente para acessar nossas superfícies públicas legíveis pelo agente?"

Para um site pronto para AEO, isso pode influenciar:- se os rastreadores de IA podem acessar a documentação
- se o tráfego do agente pode ler guias públicos
- se a velocidade de raspagem de alto volume for limitada
- se os documentos da API estiverem visíveis, mas os endpoints de execução exigirem autenticação
- se os agentes assinados são tratados de forma diferente dos bots anônimos

Isso se conecta diretamente à [camada de execução](/es/docs/execution-layer/) e às [proteções de observabilidade do agente](/es/docs/agent-observability-guardrails/).

## Layout de acesso recomendado

| Área do local | Política de acesso sugerida |
|
---|
---|
| Guias públicos | Permitir rastreadores credenciados; volume de controle |
| llms.txt e mapa do site | Mantenha acessível |
| Documentos de referência da API | Permitir descoberta; proteger credenciais e execução |
| Preços e páginas de produtos | Permitir busca e recuperação de respostas |
| Pagamento, conta, administrador | Autenticação e limite de taxa |
| Dados exclusivos para associados | Exigir autenticação assinada ou tokens de conta |

O objetivo é tornar a web pública útil para os agentes sem transformar sistemas privados em ferramentas abertas.

## Lista de verificação de implantação

1. Bots de inventário que estão chegando ao site.
2. Pesquisa separada, inteligência artificial, treinamento, monitoramento e eliminação de tráfego.
3. Mantenha [llms.txt](/es/docs/llms-txt-vs-robots-txt/) e documentos públicos acessíveis.
4. Adicione regras de bot que não bloqueiem acidentalmente o Googlebot, o Bingbot e outros sistemas de descoberta populares.
5. Use Web Bot Auth ou verificação semelhante quando houver suporte.
6. Registre o status de verificação junto com o URL, o código de status e a ação de limite de taxa.
7. Revise as regras após cada mudança de CDN, firewall ou migração de site.

## Perguntas frequentes

### A autenticação do Web Bot é apenas para Cloudflare?

A Cloudflare documenta sua implementação, mas a ideia é baseada em rascunhos mais amplos de assinaturas de mensagens HTTP e diretórios principais. A adoção depende da infraestrutura e do suporte do rastreador.

### O Web Bot Auth informa aos rastreadores para que eles podem usar o conteúdo?

Não. Verifique a identidade. As preferências de uso ainda precisam de camadas de políticas como robots.txt, tokens de conteúdo, contratos ou regras de acesso.

### O Web Bot Auth pode substituir a verificação reversa de DNS?

Não imediatamente. Muitos sites usarão ambos, especialmente quando a adoção de rastreadores assinados for desigual.### Por que isso é importante para agentes de IA?

Cada vez mais, os agentes farão solicitações web em nome de usuários ou sistemas. A identidade assinada facilita a aplicação de diferentes regras a agentes confiáveis, rastreadores anônimos e automação abusiva.

## Conclusão

Web Bot Auth é um rastreador primitivo confiável. Isso não resolverá o licenciamento de conteúdo ou a visibilidade da IA ​​por si só, mas dará às equipes de AEO uma base melhor para decidir qual tráfego de máquina merece acesso.