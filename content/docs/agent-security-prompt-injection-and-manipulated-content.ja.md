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

AIエージェントはWeb上のテキストを単なるデータではなく実行指示として解釈するため、隠しテキストや改ざんされたツール定義による**間接的プロンプトインジェクション**の危険に晒されています。

> **調査基準日:** 2026年11月22日。時刻表記はEurope/Berlin。

---

## 最新の調査・実証データ（2026年11月22日調査）

### 1. 26件の不正サイトで確認されたBlack-Hat GEO
Palo Alto Networks Unit 42は、閲覧中のAIエージェントへ不正な取引プラットフォームだけを案内するよう仕向ける不可視テキスト（`display: none` や微細フォントなど）を使った、実在のキャンペーンを発見しました。Unit 42は本手法を、Web経由の間接的プロンプトインジェクションおよびBlack-Hat GEOと正式に分類しています。

- **脅威インテリジェンス:** [@Unit42_Intel](https://x.com/Unit42_Intel/status/2120264510350991832)、2026年11月10日 22:17 Europe/Berlin。
- **侵害指標:** [Unit 42 Timely Threat Intel, 2026-11-06-IDPI-campaign](https://github.com/PaloAltoNetworks/Unit42-timely-threat-intel/blob/main/2026-11-06-IDPI-campaign.txt)。
- **調査公開:** [Fooling AI Agents: Web-Based Indirect Prompt Injection Observed in the Wild](https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/)。

### 2. MCPツールの説明文汚染（Tool Poisoning）
エージェントを攻撃するのに、悪意あるバイナリの実行は必要ありません。MCPツールの自然言語の説明を操作するだけで、編成役のLLMに機密データを漏えいさせたり、意図しない操作を呼び出させたりできます。

- **開発者分析:** [@1PasswordDev](https://x.com/1PasswordDev/status/2122472408619852202) のスレッド、2026年11月17日 00:30 Europe/Berlin（約132,000インプレッション）。ツール汚染の詳細: [https://x.com/1PasswordDev/status/2122473198147313902](https://x.com/1PasswordDev/status/2122473198147313902)。
- **基本ガイダンス:** [1Password: Where MCP fits and where it doesn’t](https://1password.com/blog/where-mcp-fits-and-where-it-doesnt) および [OWASP MCP Security Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html)。

### 3. 実証実験における攻撃成功率：フレームワーク横断研究
主要なエージェントフレームワーク12件を調べた学術的な測定研究では、ツール汚染は評価したテストケースの**22.9%**で成功しました。懸念されるのは、評価した12フレームワークのいずれにも、汚染された説明に対する意図的な組み込み防御がなかったことです。

- **論文:** [MCP Tool Poisoning in Agentic AI Frameworks: A Cross-Framework Measurement Study, arXiv:2611.03555](https://arxiv.org/abs/2611.03555)。

### 4. アーキテクチャ上の分離：IBM GraniteとLLMON
IBMは、Granite 4.1の3Bおよび8BモデルでLLMON（LLM-Native Markup Language）によるアーキテクチャ上の防御を探っています。LLMONは、外部から取得したコンテンツを実行可能な指示ではなく受動的なデータとして厳密に解釈するよう、transformerへ明示的に指示します。ただしIBMは、これは学習された挙動であり、数学的に保証されたセキュリティ制御ではないと明記しています。

- **技術報告:** [LLMON: An LLM-Native Markup Language, now in Granite 4.1 3B and 8B](https://huggingface.co/blog/ibm-granite/llmon-an-llm-native-markup-language-now-in-granite)。

### 5. プロンプトインジェクションは未解決のまま（OWASP LLM01）
プロンプトインジェクションは、OWASP Top 10 for LLM Applicationsの第1位（LLM01）のままです。文書化された隠蔽経路には、白背景の白文字（[@Pksingh900](https://x.com/Pksingh900/status/2116788637019124196)、2026年11月1日 08:05 Europe/Berlin）、画像の隠しaltテキスト、PDFに埋め込まれたコメントレイヤー、会議招待があります。

- **参照フレームワーク:** [OWASP GenAI LLM Top 10 2026](https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/)。

### 6. 新興のモデル耐性と検索エンジンの立場
- **現場の観察:** 敵対的な指示をモデルが認識した散発的な事例が報告されています（例：[@NoemiTitarenco](https://x.com/NoemiTitarenco/status/2119947195860361318)、2026年11月10日 01:16 Europe/Berlin。SlackのWebページ上の隠し指示をエージェントが検知して無視した）。
- **検索エンジンの方針:** Googleは[Google Search Spam Policies](https://developers.google.com/search/docs/essentials/spam-policies)で、隠しテキスト、クローキング、欺瞞的な操作を厳禁しています。不可視テキストでAI回答エンジンを操作しようとする試みは、重大な手動対策の対象になると警告しています。

---

## 公開予定記事（近日公開）

- *間接的プロンプトインジェクション：不可視テキストがエージェントを誤誘導する仕組み*（近日公開）
- *MCPツール汚染：自然言語の説明文がエクスプロイトになる脅威*（近日公開）
- *エージェント向けクリーンコンテンツ：ソースコードに決して含めてはならないもの*（近日公開）
- *Black-Hat GEOはプロンプトインジェクションである：実在キャンペーンの解剖*（近日公開）
- *ツール説明文をサードパーティ依存関係と同じように監査する*（近日公開）
- *GEOHunter：スポンサードGEOのシンジケートが回答エンジンを操作する仕組み（arXiv:2611.26564）*（近日公開）
