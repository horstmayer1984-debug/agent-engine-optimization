---
title: "プロンプトインジェクションと改ざんコンテンツ：エージェント読み取りレイヤーの防衛"
metaTitle: "AEOにおけるプロンプトインジェクション：Black-Hat GEOとツール汚染"
description: "不可視テキストや間接的インジェクション、MCPツール汚染がAIエージェントを誤誘導する手口とコード上の対策。"
summary: "プロンプトインジェクションの深層分析：Unit 42のBlack-Hat GEO調査、1PasswordのMCP検証、IBM LLMONの成果。"
keywords:
  - "プロンプトインジェクション"
  - "Black-Hat GEO"
  - "ツール汚染"
  - "OWASP LLM01"
date: 2026-11-22
weight: 204
category: "セキュリティ"
---

# プロンプトインジェクションと改ざんコンテンツ：エージェント読み取りレイヤーの防衛

AIエージェントはWeb上のテキストを単なるデータではなく実行指示として解釈するため、隠しテキストや改ざんされたツール定義による**間接的プロンプトインジェクション**の危険に晒されています。

> **調査基準日:** 2026年11月22日。時刻表記はEurope/Berlin。

---

## 最新の調査・実証データ（2026年11月22日調査）

### 1. 26件の不正サイトで確認されたBlack-Hat GEO
Unit 42は、不可視テキスト（`display: none`等）でエージェントを不正取引サイトへ誘導するキャンペーンを特定（[@Unit42_Intel](https://x.com/Unit42_Intel/status/2120264510350991832), [Unit 42 Research](https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/)）。

### 2. MCPツールの説明文汚染（Tool Poisoning）
悪意あるバイナリを用いずとも、自然言語の説明文を細工するだけでLLMに不正動作を行わせることが可能です（[@1PasswordDev](https://x.com/1PasswordDev/status/2122472408619852202), [OWASP MCP Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html)）。

### 3. 実証実験における攻撃成功率22.9%
主要12フレームワークを対象とした調査で、22.9%の成功率を記録し、防御機能を標準搭載するフレームワークは皆無でした（[arXiv:2611.03555](https://arxiv.org/abs/2611.03555)）。

### 4. IBM GraniteにおけるLLMONの試み
IBMはGranite 4.1において、入力データを実行指示と分離するマークアップ言語LLMONを検証中（[Hugging Face Blog](https://huggingface.co/blog/ibm-granite/llmon-an-llm-native-markup-language-now-in-granite)）。

### 5. OWASP第1位およびGoogleスパムポリシー
- プロンプトインジェクションは[OWASP GenAI Top 10](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/)で首位（LLM01）。
- Googleは[Google Search Spam Policies](https://developers.google.com/search/docs/essentials/spam-policies)で隠しテキストを厳禁。

---

## 公開予定記事（近日公開）

- *間接的プロンプトインジェクション：不可視テキストがエージェントを誤誘導する仕組み*（近日公開）
- *MCPツール汚染：自然言語の説明文がエクスプロイトになる脅威*（近日公開）
