---
title: "エージェントのアクセスとアイデンティティ：正当なAIエージェントの識別と検証"
metaTitle: "エージェントアクセスとアイデンティティ：Web Bot AuthとRFC 9421"
description: "暗号署名された正規エージェント（ChatGPT Dotsなど）の識別、ボット対策の最適化、専用エージェントIDの運用方法。"
summary: "エージェントのアクセスとID管理の分析：Web Bot Auth、Cloudflareポリシー、ChatGPT Wallet、個別クレデンシャル。"
keywords:
  - "エージェントアクセス"
  - "エージェントアイデンティティ"
  - "Web Bot Auth"
  - "RFC 9421"
  - "Cloudflare"
date: 2026-11-22
weight: 202
category: "セキュリティ"
---

# エージェントのアクセスとアイデンティティ：正当なAIエージェントの識別と検証

ウェブサイトは、スクレイピングや不正アクセスを防ぎつつ、正規ユーザーの代理で購入を行うパーソナルAIエージェントを確実に通過させる必要があります。

暗号署名（Web Bot Auth / RFC 9421）、エッジでのきめ細かな制御、および人間用アカウントの使い回しを防ぐエージェント専用IDの確立が必須となります。

> **調査基準日:** 2026年11月22日。時刻表記はEurope/Berlin。

---

## 最新動向（2026年11月22日調査）

### 1. ChatGPT Walletによる署名済みエージェントの受け入れ要請
OpenAIは、ボット対策ツールがDotsエージェントを遮断しないよう明示的に要求しています。Cloudflareでは、**Personal Agents**設定で**「dots, OpenAI」**を**Allow (do not block)**にするか、Bot Detection ID `129220581`（ChatGPT Operator）のWAFルールを設定します。

- **公式ポスト:** [@ChatGPT](https://x.com/ChatGPT/status/2121283151729496235), 2026年11月13日 17:44 Europe/Berlin（約100万インプレッション）。
- **一次情報:** [OpenAI ChatGPT Wallet](https://openai.com/index/introducing-chatgpt-wallet/), [OpenAI Dots](https://openai.com/index/introducing-dots/), [OpenAI Agent Access](https://developers.openai.com/commerce/agent-access)。
- **署名仕様:** [RFC 9421](https://www.rfc-editor.org/rfc/rfc9421) HTTP Message Signatures、`Signature`、`Signature-Input`、`Signature-Agent`（`"https://chatgpt.com"`）、公開鍵ディレクトリ `https://chatgpt.com/.well-known/http-message-signatures-directory`。

### 2. CloudflareのPersonal Agents個別制御機能
2026年11月4日より、Cloudflare管理画面で主要Personal AgentsごとにAllow / Block / Block on pages with adsを設定可能になりました（[Changelog](https://developers.cloudflare.com/changelog/post/2026-11-04-personal-agent-policies/)）。

### 3. 署名が証明するのは「運営事業者」であり「顧客」ではない
Web Bot AuthはリクエストがOpenAIなどの事業者から送信されたことを証明しますが、背後にいるユーザーの身元や承認状態は証明しません。Cloudflareは「Trusted Agent Delegation」構想を発表しました（[Cloudflare Blog](https://blog.cloudflare.com/trusted-agent-delegation/), [draft-ietf-webbotauth-httpsig-protocol](https://datatracker.ietf.org/doc/draft-ietf-webbotauth-httpsig-protocol/)）。

### 4. 借り物のログインではなくエージェント専用のIDを
- [@Cloudflare警告](https://x.com/Cloudflare/status/2118288470275674172)：従業員のログインをエージェントに使い回すと監査ログが破綻します。
- ソリューション：[Okta CIMD](https://www.okta.com/blog/product-innovation/okta-cimd-ai-agent-identity/)、[Auth0](https://www.okta.com/newsroom/articles/auth0-may-2026-product-innovations/)、[Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/agent-identities)。

### 5. WorkOS Agent Vaultのアプローチ
人間が認証情報を預け、エージェントが代理ログインする逆のアプローチ（[WorkOS](https://workos.com/docs/agent-vault)）。

---

## 公開予定記事（近日公開）

- *Web Bot Auth解説：ChatGPT Dotsなどの署名済みエージェントを識別する方法*（近日公開）
- *正当な購買エージェントを排除しないボット管理の再設定*（近日公開）
