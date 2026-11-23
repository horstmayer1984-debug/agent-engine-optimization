---
title: "MCP、WebMCP、エージェントブラウザ：重要リポジトリ徹底ランキング"
metaTitle: "MCP・WebMCP・エージェントブラウザ主要リポジトリ（2026年）"
description: "エージェント実行・連携のための主要オープンソースランキング：browser-use、Playwright MCP、Firecrawl MCP、WebMCPなど。"
summary: "AEO実行レイヤーの主要ツール比較：ブラウザ検証、MCPサーバー、W3C WebMCP仕様、開発SDK。"
keywords:
  - "browser-use"
  - "Playwright MCP"
  - "Firecrawl MCP"
  - "WebMCP"
  - "AEO実行レイヤー"
date: 2026-11-22
weight: 212
category: "オープンソース"
---

従来のSEOがテキスト閲覧にとどまっていたのに対し、AEOでは**実行レイヤー（Execution Layer）**が重要になります。エージェントがサイト内を巡回し、フォームを入力し、APIを実行できるかが問われます。

> **調査基準日:** 2026年11月22日。GitHub公式API取得データ。

---

## 比較ランキング：エージェントインターフェースおよびブラウザ自動化

| 順位 | ツール名 | カテゴリ | AEOへの実用価値 | ライセンス | スター数 (22.11.2026) | 最終更新 (Europe/Berlin) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **1** | [browser-use](https://github.com/browser-use/browser-use) | エージェントブラウザ | AIエージェントが実際にサイト内をクリック・操作する挙動を検証。 | MIT | 121,711 | 22.11.2026, 04:44 |
| **2** | [Playwright MCP](https://github.com/microsoft/playwright-mcp) | 公式MCPサーバー (MS) | Playwrightによるブラウザ制御を標準MCPツールとして提供。 | Apache-2.0 | 39,988 | 18.11.2026, 19:50 |
| **3** | [Firecrawl MCP](https://github.com/firecrawl/firecrawl-mcp-server) | 公式MCPサーバー | Firecrawlの抽出・Markdown化機能をMCPクライアントへ提供。 | MIT | 7,880 | 22.11.2026, 06:53 |
| **4** | [WebMCP](https://github.com/webmachinelearning/webmcp) | W3C草案 | サイト自身がブラウザ内エージェントへ直接ツールを公開する新規格。 | 要リポジトリ確認 | 5,010 | 22.11.2026, 02:23 |
| **4b** | [webmcp-tools](https://github.com/GoogleChromeLabs/webmcp-tools) | Chrome Labs開発ツール | WebMCP Origin Trialを支援するChrome Labs公式ツール群。 | Apache-2.0 | 796 | 20.11.2026, 19:15 |
| **5** | [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk) | 公式Python SDK | 独自AEOツールやMCPサーバー構築のための標準開発キット。 | MIT | 24,929 | 17.11.2026, 10:38 |
| **6** | [NLWeb](https://github.com/nlweb-ai/NLWeb) | 会話型Webレイヤー | サイトを対話可能にする試み。*2026年8月以降コミット停止。* | MIT | 6,262 | 11.08.2026, 21:35 |
| **7** | [fetcher-mcp](https://github.com/jae-jae/fetcher-mcp) | 候補MCPサーバー | 簡易的なWebフェッチ・テスト用サーバー。 | MIT | 1,088 | 05.11.2026, 06:53 |

*追加のエコシステム索引:* [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers)（MIT、98,373スター、最終更新 2026年11月17日 06:21 Europe/Berlin）は幅広いディレクトリとして機能します。

---

## ツール別の要点

### 1. browser-use
- **焦点:** エンドツーエンドのエージェントによるユーザー導線テスト。
- **AEOで重要な理由:** 自律的なビジュアルブラウザエージェントを模擬することで、`browser-use`はボタン、フォーム、モーダルがモデルを混乱させたり無限ループを起こしたりする箇所を明らかにします。
- **リポジトリ:** [github.com/browser-use/browser-use](https://github.com/browser-use/browser-use)

### 2. Playwright MCP（Microsoft）
- **焦点:** 標準ツール経由のエンタープライズ向けブラウザ自動化。
- **AEOで重要な理由:** Claude、Codex、またはローカルエージェントが、CI/CDの検証パイプライン内でWebセッションを対話的に検査・操作できるようにします。
- **リポジトリ:** [github.com/microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)

### 3. WebMCPとChrome Labsツール
- **焦点:** 新興のクライアントサイドWeb標準。
- **AEOで重要な理由:** W3CのWeb Machine Learning議論とGoogle Chrome Labsを通じて進められており、WebMCPは帯域外のサーバー設定なしに、Webページがブラウザエージェントへセマンティックなツールをネイティブ登録できるようにします。
- **リポジトリ:** [github.com/webmachinelearning/webmcp](https://github.com/webmachinelearning/webmcp) および [github.com/GoogleChromeLabs/webmcp-tools](https://github.com/GoogleChromeLabs/webmcp-tools)

### 4. NLWeb（ステータス注記）
- **ステータス:** 2026年前半には広く議論されましたが、`NLWeb`は**2026年8月11日以降、新規コミットがありません**（最終コミットはEurope/Berlin 21:35）。アーカイブ参照としてのみ評価してください。
- **リポジトリ:** [github.com/nlweb-ai/NLWeb](https://github.com/nlweb-ai/NLWeb)

---

## ツール選定の指針

- **エージェント視点での導線テスト:** **[browser-use](https://github.com/browser-use/browser-use)**または**[Playwright MCP](https://github.com/microsoft/playwright-mcp)**を採用。
- **独自MCPツールの開発:** 公式**[MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)**を使用。
- **注意点:** **NLWeb**は2026年8月11日以降コミットが停止している点に留意してください。
