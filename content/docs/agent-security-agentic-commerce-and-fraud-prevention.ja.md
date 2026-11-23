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

# エージェントコマースと不正防止：正規エージェントによる購買の安全な承認

AIエージェントがクラウド経由で代理購入を行う際、端末の生体情報や物理環境シグナルが存在しないため、従来の不正検知システムによって誤検知・遮断される問題が頻発しています。

> **調査基準日:** 2026年11月22日。時刻表記はEurope/Berlin。

---

## 最新の市場動向（2026年11月22日調査）

### 1. ChatGPT Walletの登場とクラウドブラウザ遮断問題
米国Proユーザー向けに提供開始。OpenAIは、ショップ側のWAFがクラウドブラウザを不正アクセスと誤認して遮断している現状を公式ドキュメントで説明（[@ChatGPT](https://x.com/ChatGPT/status/2121283151729496235), [OpenAI Help Docs](https://developers.openai.com/commerce/agent-access)）。

### 2. Sardineの「Know Your Human（KYH）」プロトコル
Sardineは、エージェントのクラウドセッションとユーザー端末の正当なIP・端末シグナルを暗号的に紐付けるKYHを発表（**事業者発表資料**, [Sardine KYH](https://www.sardine.ai/know-your-human)）。

### 3. ベンダー各社の市場データ
Forterによると、8月以降エージェント経由の注文は4倍以上に急増（**事業者公表値**, [Forter Release](https://www.prnewswire.com/news-releases/forter-turns-the-ai-shopping-agent-surge-into-a-secure-revenue-channel-for-merchants-302906333.html)）。Riskifiedは12月にAgent Identityベータを予定。

### 4. 誤購入時のチャージバック責任と決済基盤
エージェントが上限額を超えて購入した場合の責任分担はカードブランドで検討中（[@sardine](https://x.com/sardine/status/2122728047593824695)）。Visaは欧州で30以上の銀行と提携し2026年7月より実運用を開始（[Visa DE Release](https://www.visa.de/uber-visa/newsroom/press-releases.3457335.html)）。Mastercardは「Agent Pay for Machines」を推進（[@Mastercard](https://x.com/Mastercard/status/2122377314142916918)）。

---

## 公開予定記事（近日公開）

- *ChatGPT Wallet：従来の不正検知が正規エージェントを誤遮断する構造*（近日公開）
- *エージェントが誤った商品を購入した際のチャージバック責任の所在*（近日公開）
