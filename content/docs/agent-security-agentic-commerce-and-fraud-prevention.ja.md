---
title: "エージェントコマースと不正防止：正規エージェントによる購買の安全な承認"
metaTitle: "エージェントコマースセキュリティ：ChatGPT Walletと不正防止"
description: "正規エージェントによる購買が不正検知に引っかかる理由、Know Your Human（KYH）の役割、誤購入時の責任の所在。"
summary: "エージェントコマースの不正防止分析：ChatGPT Wallet、Sardine KYH、Forter発表データ、Visa/Mastercardの決済基盤。"
keywords:
  - "エージェントコマース"
  - "不正防止"
  - "ChatGPT Wallet"
  - "Know Your Human"
  - "Visa決済"
date: 2026-11-22
weight: 206
category: "セキュリティ"
---

AIエージェントがクラウド経由で代理購入を行う際、端末の生体情報や物理環境シグナルが存在しないため、従来の不正検知システムによって誤検知・遮断される問題が頻発しています。

> **調査基準日:** 2026年11月22日。時刻表記はEurope/Berlin。

---

## 最新の市場動向（2026年11月22日調査）

### 1. ChatGPT Walletの登場とクラウドブラウザ遮断問題
米国Proユーザー向けに提供開始。OpenAIは、ショップ側のWAFがクラウドブラウザを不正アクセスと誤認して遮断している現状を公式ドキュメントで説明しています。決済が中断される原因として、クラウドブラウザの訪問をファイアウォールと不正検知エンジンが日常的に遮断する点を、OpenAI自身が明示しています。

- **発表:** [@ChatGPT](https://x.com/ChatGPT/status/2121283151729496235)、2026年11月13日 17:44 Europe/Berlin（約100万インプレッション）。
- **公式ドキュメント:** [Introducing ChatGPT Wallet](https://openai.com/index/introducing-chatgpt-wallet/) および [Help ensure cloud browser access](https://developers.openai.com/commerce/agent-access)。

### 2. 構造上のジレンマ：正規の購入が不正に似る
クラウドブラウザのエージェントには、ハードウェアエントロピー、バッテリー状態、一般的な住宅用IPの所在がありません。
- **業界での議論:** 決済インフラ企業Sardineは、クラウドブラウザが侵害されたセッションと見分けがつかない点を分析しています（[@sardine](https://x.com/sardine/status/2119825121154048401)、2026年11月9日 17:11 Europe/Berlin、および [@sardine](https://x.com/sardine/status/2118416600529264672)、2026年11月5日 19:54 Europe/Berlin）。
- **ネットワークテレメトリ:** OpenAIはこのギャップを埋めるため、HTTP `Forwarded` ヘッダーへクライアントメタデータ（`asn`、`for`、`ip-country` を含む）を注入します（[OpenAI Accept Payments Guide](https://developers.openai.com/commerce/guides/accept-payments)）。

### 3. Sardineの「Know Your Human（KYH）」プロトコル
Sardineは、エージェントのクラウドセッションとユーザー端末の正当なIP・端末シグナルを暗号的に紐付ける**Know Your Human（KYH）**を発表しました（*事業者の製品説明*）。不正検知エンジンが消費者の意図を検証できるようにします。

- **技術解説:** [Know Your Human: Fraud Prevention for Agentic Commerce](https://www.sardine.ai/blog/know-your-human-agentic-commerce) および [KYH Product Page](https://www.sardine.ai/know-your-human)。
- **提携の文脈:** [@sardine](https://x.com/sardine/status/2122366653388189822)、2026年11月16日 17:30 Europe/Berlin。

### 4. 市場の急増：ForterとRiskifiedのベンダーテレメトリ
不正対策ベンダーForterによると、2026年8月以降、エージェント経由の注文は400%超増加し、同じ期間に自動不正の試行は倍増しました（*事業者公表値*）。一方Riskifiedは、Agent Identity Risk Intelligenceのエンタープライズベータを2026年12月に予定しています。

- **ベンダー発表:** [Forter turns the AI shopping agent surge into a secure revenue channel, PR Newswire](https://www.prnewswire.com/news-releases/forter-turns-the-ai-shopping-agent-surge-into-a-secure-revenue-channel-for-merchants-302906333.html)。
- **ベンダーロードマップ:** [Riskified: Agent Identity Risk Intelligence](https://www.riskified.com/press/agent-identity-risk-intelligence/)。

### 5. 未解決の責任：自律的な誤りの費用は誰が負担するか
主要なカード決済ネットワークは、意図しないエージェント購入についての拘束力のある紛争ルールをまだ確定していません。Sardineが論じた例では、顧客が予算上限を1,000ドルと指定したにもかかわらず、エージェントが1,400ドルのノートPCを購入しました。

- **責任をめぐる議論:** [@sardine](https://x.com/sardine/status/2122428753917665751)、2026年11月16日 21:37 Europe/Berlin、および [@sardine](https://x.com/sardine/status/2122728047593824695)、2026年11月17日 17:26 Europe/Berlin。

### 6. VisaとMastercardのインフラ展開
ChatGPT Walletは米国中心のままですが、欧州の決済ネットワークは迅速に動いています。
- **Visa Europe:** Visaは2026年7月以降、Commerzbank、DKB、S-Payment、Klarnaを含む30以上の欧州の銀行パートナーと、実際のAIエージェント取引を処理していると発表しました（[Visa Press Release DE](https://www.visa.de/uber-visa/newsroom/press-releases.3457335.html) および [Visa UK Release](https://www.visa.co.uk/about-visa/newsroom/press-releases.3457328.html)）。
- **Mastercard:** ハッカソンのショーケースで「Agent Pay for Machines」フレームワークを強調しています（[@Mastercard](https://x.com/Mastercard/status/2122377314142916918)、2026年11月16日 18:12 Europe/Berlin、約318,000インプレッション）。

---

## 公開予定記事（近日公開）

- *ChatGPT Wallet：従来の不正検知が正規エージェントを誤遮断する構造*（近日公開）
- *正規の購買エージェントと不正エージェント：ForterとRiskifiedはどう分類するか*（近日公開）
- *Visa Agentic ReadyとMastercard Agent Pay：加盟店に求められる技術要件*（近日公開）
- *エージェントが誤った商品を購入した際のチャージバック責任の所在*（近日公開）
- *ChatGPT Walletと欧州の銀行レール：エージェント決済の地理的実態*（近日公開）
