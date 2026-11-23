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

# Agent Engine Optimization（AEO）のためのオープンソース

AEO（Agent Engine Optimization）のエコシステムは、機械可読フォーマットの仕様、抽出パーサー、実行プロトコル（MCP）、ローカル検証モデルなど、オープンソース技術に深く支えられています。

本ディレクトリでは、AIエージェント対応に不可欠なGitHubリポジトリ、Hugging Faceモデル、標準規格を整理・評価しています。

> **調査基準日:** 2026年11月22日。GitHubスター数、SPDXライセンス、更新日時は2026年11月22日時点の公式API取得データ。

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

- **GEO基礎論文:** Aggarwal et al., [arXiv:2311.09735](https://arxiv.org/abs/2311.09735)
- **llms.txt仕様:** [AnswerDotAI/llms-txt](https://github.com/AnswerDotAI/llms-txt), [llmstxt.org](https://llmstxt.org/)
- **HTTP Message Signatures:** [RFC 9421](https://www.rfc-editor.org/rfc/rfc9421)
