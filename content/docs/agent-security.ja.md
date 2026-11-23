---
title: "エージェントセキュリティ：自律型AI時代におけるウェブサイト保護"
metaTitle: "エージェントセキュリティ概要：AIエージェント対応のウェブ保護"
description: "AEOのためのエージェントセキュリティ概要。正当なエージェントの検証、攻撃の防御、APIおよびコマースフローの保護方法を解説します。"
summary: "エージェントセキュリティの包括的入門：正規ボットの検証、脅威の動向、プロンプトインジェクション、安全なインターフェースと不正防止。"
keywords:
  - "エージェントセキュリティ"
  - "AIエージェント"
  - "AEOセキュリティ"
  - "ボット保護"
  - "プロンプトインジェクション"
date: 2026-11-22
weight: 201
category: "セキュリティ"
---

# エージェントセキュリティ：自律型AI時代におけるウェブサイト保護

エージェントセキュリティ（Agent Security）は、Agent Engine Optimization（AEO）における防御の中核です。基本原則は明白です：**正当なAIエージェントによるウェブサイト上での閲覧や取引は円滑に許可し、攻撃的なエージェントは確実に遮断すること。**

本領域は一般的なサイバーセキュリティ情報ではなく、自律型モデル、クラウドブラウザ、実行プロトコル（MCPやWeb Bot Authなど）が交差する実務レイヤーに特化しています。

> **調査基準日:** 2026年11月22日。記載されている数値、日時（Europe/Berlin）、ベンダー発表はすべて検証済みデータに基づきます。

---

## エージェントセキュリティの6大重点領域

1. **[エージェントのアクセスとアイデンティティ](/ja/docs/agent-security-agent-access-and-identity/)**  
   暗号署名された正規エージェント（RFC 9421に基づくChatGPT DotsやCloudflare Personal Agents）の識別と、個別エージェントIDの付与。

2. **[AIエージェントによるサイバー攻撃](/ja/docs/agent-security-attacks-by-ai-agents/)**  
   ARTEXなどの自律型侵入ツールの脅威、初期侵入経路（`/.env`、`/.git/config`）、エージェント偽装クレデンシャルスタッフィングの対策。

3. **[プロンプトインジェクションと改ざんコンテンツ](/ja/docs/agent-security-prompt-injection-and-manipulated-content/)**  
   間接的プロンプトインジェクション、不可視テキスト（Black-Hat GEO）、MCPツール定義の汚染（Tool Poisoning）からの保護。

4. **[安全なインターフェース：API、MCP、WebMCP](/ja/docs/agent-security-secure-interfaces/)**  
   MCPは統合規格でありセキュリティ境界ではないという原則、DNSリバインディング対策、Origin検証、確実な人間承認フロー。

5. **[エージェントコマースと不正防止](/ja/docs/agent-security-agentic-commerce-and-fraud-prevention/)**  
   正規エージェントによる代理購入と不正アクセスの識別、Know Your Human（KYH）による端末照合、チャージバック責任の所在。

6. **[AI時代のセキュア開発](/ja/docs/agent-security-secure-development/)**  
   AIコーディングツールによるシークレット漏洩の防止、テスト用エージェントのサンドボックス分離、デバイスコードフィッシング防御。

---

## 公開予定記事（近日公開）

- *Web Bot Auth解説：ChatGPT Dotsなどの署名済みエージェントを識別する方法*（近日公開）
- *正当な購買エージェントを排除しないボット管理の再設定*（近日公開）
- *借り物のアカウントではなくエージェント専用IDを付与する設計*（近日公開）
- *FBIのARTEX警告と自律型ハッキングエージェントの脅威実態*（近日公開）
