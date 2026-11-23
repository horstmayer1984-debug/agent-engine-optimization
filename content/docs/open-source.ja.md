---
title: "Agent Engine Optimization（AEO）のためのオープンソース"
metaTitle: "オープンソースAEOツール：リポジトリ、仕様、モデル"
description: "AEOのためのオープンソースツール、仕様、モデル、データセットの厳選ランキングと一覧。2026年11月22日時点の検証データ。"
summary: "6つのカテゴリーにわたるオープンソースAEOツール一覧：llms.txt、クローラー、構造化データ、MCP、ボット検証、検証用モデル。"
keywords:
  - "オープンソースAEO"
  - "llms.txtツール"
  - "Firecrawl"
  - "Model Context Protocol"
  - "Web Bot Auth"
date: 2026-11-22
weight: 208
category: "オープンソース"
---

AEO（Agent Engine Optimization）のエコシステムは、機械可読フォーマットの仕様、抽出パーサー、実行プロトコル（MCP）、ローカル検証モデルなど、オープンソース技術に深く支えられています。

本ディレクトリでは、AIエージェント対応に不可欠なGitHubリポジトリ、Hugging Faceモデル、標準規格を整理・評価しています。

> **調査基準日:** 2026年11月22日。GitHubスター数、SPDXライセンス、更新日時は2026年11月22日時点の公式API取得データ。
> 
> *方法論について:* ランキングは、AEOにおける実用性、メンテナンスの活発さ、採用度を優先した編集上の評価です。公式なベンチマーク表彰やスポンサード掲載ではありません。

---

## AEOオープンソースの6大カテゴリー

1. **[機械可読ファイル（llms.txtと関連ツール）](/ja/docs/open-source-machine-readable-files/)**  
   `llms.txt`の生成、監査、リファレンス仕様（claude-seo、OpenGSO、公式仕様）。

2. **[クローラーと抽出ツール：エージェントの視界を検証](/ja/docs/open-source-crawlers-and-extractors/)**  
   WebコンテンツをクリーンなMarkdownや構造化データへ変換（Firecrawl、Crawl4AI、Jina Reader）。

3. **[Schema.orgとJSON-LD構造化データ](/ja/docs/open-source-structured-data/)**  
   機械可読エンティティの公式語彙と型定義（schemaorg、schema-dts、extruct）。

4. **[エージェントインターフェース：MCP、WebMCP、ブラウザ](/ja/docs/open-source-agent-interfaces/)**  
   実行レイヤー：ブラウザ自動化、公式MCP SDK、WebMCP実験（browser-use、Playwright MCP、WebMCP）。

5. **[エージェントトラフィックの識別と検証](/ja/docs/open-source-identity-and-agent-traffic/)**  
   暗号署名検証（Web Bot Auth / RFC 9421）およびトラフィック分析（AgentCake、mintlify/agent-traffic）。

6. **[モデル、データセット、ローカル検証環境](/ja/docs/open-source-models-datasets-and-local-tests/)**  
   埋め込み、リランカー、ローカル実行環境（llama.cpp、MLX）、評価ベンチマーク（GEO-bench、Mind2Web）。

---

## 主要論文および標準規格

AEOアーキテクチャを規定する基盤規格と学術的評価です。

- **GEO基礎論文:** Aggarwal et al., [arXiv:2311.09735](https://arxiv.org/abs/2311.09735)。付属コード: [GEO-optim/GEO](https://github.com/GEO-optim/GEO)（Apache-2.0、352スター、最終活動 2025年10月30日 03:55 Europe/Berlin）。
- **2026年の批判的検証:** [arXiv:2607.14035](https://arxiv.org/abs/2607.14035) — 広く引用される「可視性+40%」という主張は、制約された実験室条件下でのみ成り立つことを示しています。
- **ChatGPTの引用を理解する:** [arXiv:2610.15382](https://arxiv.org/abs/2610.15382)。
- **GEOHunter（シンジケーション型の操作）:** [arXiv:2611.26564](https://arxiv.org/abs/2611.26564)（2026年11月19日）。
- **llms.txt仕様:** [AnswerDotAI/llms-txt](https://github.com/AnswerDotAI/llms-txt) および [llmstxt.org](https://llmstxt.org/)。
- **HTTP Message Signatures:** [RFC 9421](https://www.rfc-editor.org/rfc/rfc9421) および IETF草案 [draft-ietf-webbotauth-httpsig-protocol](https://datatracker.ietf.org/doc/draft-ietf-webbotauth-httpsig-protocol/)。
- **Model Context Protocol:** [MCP Specification](https://modelcontextprotocol.io/specification/2026-07-28/server/tools) および [MCP Security Best Practices](https://modelcontextprotocol.io/docs/2026-07-28/tutorials/security/security_best_practices)。
- **WebMCP（W3C草案）:** [webmachinelearning/webmcp](https://github.com/webmachinelearning/webmcp)。

---

## 追加で監視しているリポジトリ

2026年11月22日の調査監査で追跡したリポジトリは次のとおりです。

| リポジトリ | URL | スター数 (22.11.2026) | ライセンス | 最終更新 (Europe/Berlin) | 焦点 |
| :--- | :--- | :--- | :--- | :--- | :--- |
| modelcontextprotocol/servers | https://github.com/modelcontextprotocol/servers | 92,155 | NOASSERTION | 19.11.2026, 17:41 | 参照用MCPサーバーレジストリ |
| modelcontextprotocol/modelcontextprotocol | https://github.com/modelcontextprotocol/modelcontextprotocol | 9,744 | NOASSERTION | 22.11.2026, 01:31 | プロトコル中核仕様 |
| firecrawl/llmstxt-generator | https://github.com/firecrawl/llmstxt-generator | 540 | None in API | 17.06.2025, 14:37 | 生成ユーティリティ |
| firecrawl/create-llmstxt-py | https://github.com/firecrawl/create-llmstxt-py | 327 | None in API | 02.06.2025, 16:25 | Python CLIツール |
| SecretiveShell/Awesome-llms-txt | https://github.com/SecretiveShell/Awesome-llms-txt | 112 | MIT | 18.10.2026, 10:46 | 厳選カタログ |
| langchain-ai/mcpdoc | https://github.com/langchain-ai/mcpdoc | 1,029 | MIT | 20.08.2026, 07:34 | MCPドキュメントツール |
| coleam00/mcp-crawl4ai-rag | https://github.com/coleam00/mcp-crawl4ai-rag | 2,267 | MIT | 25.07.2025, 16:17 | Crawl4AIのMCP連携 |
| executeautomation/mcp-playwright | https://github.com/executeautomation/mcp-playwright | 5,682 | MIT | 13.12.2025, 05:28 | Playwrightサーバー |
| ServiceNow/WorkArena | https://github.com/ServiceNow/WorkArena | 281 | NOASSERTION | 28.09.2026, 20:31 | 企業向けエージェントベンチマーク |
| invertase/docs.page | https://github.com/invertase/docs.page | 684 | Apache-2.0 | 19.11.2026, 11:04 | ドキュメント公開基盤 |
