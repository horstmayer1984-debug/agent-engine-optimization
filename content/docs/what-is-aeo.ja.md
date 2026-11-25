---
title: "Agent Engine Optimization (AEO) とは？"
metaTitle: "AEOとは？読み取り層・実行層とアーキテクチャ解説（2026）"
description: "2026年後半におけるAEOの意味、SEOやGEOとの違い、AIエージェントにとって発見しやすく安全で実行可能なWebサイトの条件を解説します。"
metaDescription: "2026年11月更新ガイド：AEOの定義、SEO・GEOを実行層へ拡張する仕組み、エージェント対応サイトの構築とセキュリティ対策。"
summary: "読み取り層、実行層、主要プロトコル、Agent Securityを含む2026年最新のAgent Engine Optimization定義。"
keywords:
  - AEOとは
  - Agent Engine Optimization
  - エージェント対応サイト
  - 実行層
  - AIエージェント 2026
date: 2026-11-25
weight: 1
category: "Framework"
---

Agent Engine Optimization（AEO）とは、自律型AIエージェントがWebサイト、API、データ、デジタルサービスを発見し、信頼境界を検証し、機能を理解した上で予約・購入・データ取得・比較・ワークフローなどのアクションを実行できるように構造化する実践手法です。

AEOは、デジタルインフラの次の主要な利用者が「ブラウザを閲覧する人間」だけでなく「人間の代理として行動する自律型AIエージェント」であるという前提に立っています。

---

## AEOが解決する課題

「来月リスボン行きの航空券を400ユーロ未満で予約して」と指示された自律型AIエージェントには、次の5段階が必要です。

1. **発見（Discover）**: 該当路線を提供する航空会社や予約基盤を見つける
2. **読み取り（Read）**: 価格、空席状況、制約条件などの構造化データを取得する
3. **比較（Compare）**: ユーザーの予算や条件と照合する
4. **実行（Execute）**: 機械可読なトランザクションIF経由で予約を実行する
5. **検証（Verify）**: 状態遷移を確認し、確実な予約確認を受け取る

現在のWebの多くはステップ1と部分的なステップ2には対応していますが、ステップ3〜5に必要な決定論的データ、明確な制約条件、安全な実行エンドポイントを備えていません。

この「AIが要約できること」と「エージェントが安全に実行できること」のギャップを埋めるのがAEOです。

---

## AEOではないもの

**AEOはSEOの単なる言い換えではありません。** SEOは人間の検索行動と検索順位アルゴリズムに最適化します。AEOは機械による発見とタスク実行を最適化します。

**AEOはGEOと同じではありません。** [Generative Engine Optimization（GEO）](/ja/docs/generative-engine-optimization/)はAI回答内での引用・言及に焦点を当て、[Answer Engine Optimization](/ja/docs/answer-engine-optimization/)は直接回答の抽出に焦点を当てます。AEOはその先の実行層、すなわち自律エージェントがツールや取引エンドポイントとして利用できる状態を対象とします。

**AEOは将来の構想ではなく運用フェーズにあります。** 2026年を通じて主要仕様が実運用に入りました。GoogleとShopifyのUniversal Commerce Protocol（UCP）、OAuth認可・Sampling・Elicitation・公式レジストリを備えたAnthropicのModel Context Protocol（MCP）、ブラウザ向けWebMCP Origin Trial、RFC 9421（Web Bot Auth）による署名検証とエージェントウォレット決済が実際の商取引で稼働しています。

---

## AEOの2つの層

### 読み取り層（Read Layer）

AIシステムがコンテンツを正確に発見・検証・解釈できる状態にします。Schema.orgの構造化データ、セマンティックHTML、`llms.txt`、明快な出典表示、機械可読なドキュメント設計が含まれます。

### 実行層（Execution Layer）

自律型エージェントがデジタルサービス上でアクションを実行できる状態にします。OpenAPIで定義されたAPI、MCPサーバー、WebMCPブラウザツール、UCP/ACPコマースフロー、決定論的データ構造、機械可読な制約条件、検証可能な状態遷移で構成されます。詳細は[AIエージェント実行層ガイド](/ja/docs/execution-layer/)を参照してください。

---

## 今すぐAEOが必要な領域

**即時重要性が高い分野（2026年後半）：**
- ECプラットフォームおよびオンライン小売（UCP・ACP・エージェントウォレットが稼働）
- 旅行・予約サービス（航空券・ホテルのリアルタイム空席・条件連携）
- APIを提供するB2B SaaS（エージェントによる発見と細かいOAuthスコープが必要）
- 開発者ツールおよびAPI基盤（MCP連携が直接的な採用要因）

**急速に拡大している分野（2027年以降）：**
- フィンテック・保険・決済基盤（AP2委任やx402マシン決済）
- B2B調達・サプライチェーン管理
- 監査可能な人間承認フローを必要とする規制産業

---

## 2026年のプロトコル市場

| プロトコル | 主導組織 | AEOにおける役割 |
|---|---|---|
| **UCP** | Google / Shopify | エージェントと加盟店間の標準化された商取引プロトコル |
| **MCP** | Anthropic / Linux Foundation | AIモデル向けの汎用ツール・リソース・OAuth接続層 |
| **WebMCP** | W3C / Chrome | Webページが直接公開するブラウザ側ツール契約 |
| **A2A** | Google | 自律エージェント間の発見と協調連携 |
| **ACP** | OpenAI / Stripe | 安全なチェックアウトと認証情報の委任 |
| **AP2** | Google | 暗号的に検証された決済委任（Mandate） |
| **Web Bot Auth** | IETF (RFC 9421) | 正規AIエージェントの暗号的署名検証 |

これらのプロトコルは競合ではなく補完関係にあります。1つのワークフロー内で、Web Bot Authで身元を検証し、MCPまたはWebMCPでツールを実行し、UCP/ACPで注文を確定し、AP2/x402で決済を完了できます。

---

## エージェント対応基盤のセキュリティとOSS活用

防御策なしに実行エンドポイントを公開すると重大なリスクを生みます。実運用のAEOには利便性とセキュリティの両立が不可欠です。

- **[Agent Security（エージェント・セキュリティ）](/ja/docs/agent-security/):** 暗号署名された正規エージェントと悪意あるボットを識別し、MCP・API境界を堅牢化し、読み取り層を間接プロンプトインジェクションから防御します。
- **[AEO向けオープンソースツール](/ja/docs/open-source/):** `llms.txt`生成ツール、クローラー検証、JSON-LDバリデータ、MCP SDK、Web Bot Authライブラリを比較評価できます。
- **[AEO vs. SEO vs. GEO](/ja/docs/aeo-vs-seo-vs-geo/):** 検索順位、AI引用、自律実行の違いを整理しています。
- **[AEO準備状況監査](/ja/docs/audit/):** 読み取り層・実行層・セキュリティ体制を体系的に評価するか、[無料AEOレディネスチェッカー](/tools/aeo-readiness-checker.html)をご利用ください。

---

## よくある質問

### Agent Engine OptimizationはAnswer Engine Optimizationと同じですか？

いいえ。Answer Engine Optimizationは生成AI回答での可視性や直接引用に焦点を当てます。Agent Engine Optimizationはそれに加え、自律エージェントが実際のタスクを完了・検証するためのAPI、プロトコル、セキュリティ制御までを含みます。

### すべてのWebサイトにMCP・WebMCP・UCPが必要ですか？

いいえ。コンテンツ中心のサイトは、クリーンなHTML、Schema.org構造化データ、出典明記、`llms.txt`から始められます。実行プロトコルは、サイトがツール実行・予約・決済・エージェント間連携を公開する場合に重要になります。

### 2026年後半に企業が最初に取り組むべきことは何ですか？

エージェントに委任する価値のあるタスクを特定し、クローラーアクセスと構造化データを監査した上で、[Agent Security](/ja/docs/agent-security/)でAPIやフォーム境界を保護し、[AEO準備状況監査](/ja/docs/audit/)で決定論的エンドポイントを検証してください。

## 主な参考文献

* [NIST AI リスク管理フレームワーク](https://www.nist.gov/itl/ai-risk-management-framework)
* [Schema.org ドキュメント](https://schema.org/docs/documents.html)
* [Model Context Protocol 仕様](https://modelcontextprotocol.io/specification/2026-07-28/server/tools)
* [RFC 9421: HTTP Message Signatures](https://www.rfc-editor.org/rfc/rfc9421)
