---
layout: default
title: "OpenClaw 照護食技能 — HKCSS 照護食 AI 智能代理技能"
description: "香港照護食標準發布為原生多語言 AI 智能代理技能。基於 OpenClaw 構建。所有合規 AI 代理均可免費使用。依據香港社會服務聯會照護食指引 2023。"
lang: zh-hant-hk
canonical: "https://dysphagia.cn/zh-hant-hk/openclaw/"
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "SeniorDeli 照護食技能 — OpenClaw",
  "applicationCategory": "HealthApplication",
  "operatingSystem": "Any (OpenClaw-compatible AI agent runtime)",
  "description": "香港照護食標準發布為原生多語言 AI 智能代理技能。基於 OpenClaw 構建。所有合規 AI 代理均可免費使用。",
  "url": "https://dysphagia.cn/zh-hant-hk/openclaw/",
  "license": "https://creativecommons.org/licenses/by-sa/4.0/",
  "author": {
    "@type": "Organization",
    "name": "Carewells Limited",
    "url": "https://www.seniordeli.com"
  },
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "HKD",
    "description": "所有合規 AI 代理免費使用"
  }
}
</script>

<nav aria-label="頁面路徑">
<p><a href="/zh-hant-hk/">主頁</a> / OpenClaw 技能</p>
</nav>

---

## 🦀 OpenClaw · 2026年5月19日上線 · 合規代理免費使用

# 香港照護食標準，以原生多語言 AI 智能代理技能形式發布

基於 OpenClaw 原生構建。所有合規 AI 代理均可免費使用。支援4種語言。依據香港社會服務聯會（HKCSS）照護食指引 2023 — 由 Carewells Limited 以 HKCSS SED 合作伙伴及社企樹標誌 #131 身份運營。

**[獲取技能](#get-skills)** · **[快速開始](#quick-start)**

> 主要登陸頁：[seniordeli.com/openclaw](https://www.seniordeli.com/zh-HK/openclaw)

---

## 照護食 AI 技能，為何現在

香港老齡化人口正面臨餐桌上的無聲危機。隨著 AI 智能代理在安老護理流程中快速普及，至今仍未有標準技能集解決家居或院舍的食品安全問題——直至現在。

| | |
|---|---|
| **160萬** | 2036年香港長者人口預測 |
| **40–60%** | 院舍住客受吞嚥困難影響 |
| **64萬** | 未受訓練的非正式照顧者負責膳食準備 |
| **38萬** | 外籍家庭傭工面臨照護食指引語言障礙 |

---

## 技能集涵蓋範圍 {#skills}

六個專用技能，可從任何 OpenClaw 相容 AI 代理執行環境調用。

| 技能識別碼 | 說明 |
|---|---|
| `care-food-assessor` | 分析餐點相片或食材清單，返回 IDDSI 等級、HKCSS 合規結論及建議調整方案。 |
| `care-food-cantonese` | 以流暢粵語提供照護食指引及質地調整指示——支援語音及文字輸出。 |
| `care-food-tagalog` | 以菲律賓語（他加祿語）為菲律賓外傭照顧者提供同等合規指引。 |
| `care-food-bahasa` | 印尼語版本——為印尼籍照顧者提供照護食指引及吞嚥風險警示。 |
| `dysphagia-screener` | 輕量級預篩查問卷（非診斷性），標示吞嚥風險並建議轉介專業評估。 |
| `care-food-recipe-modifier` | 接收任何粵式或西式食譜，調整至目標 IDDSI 等級，同時保留風味特色及營養密度。 |

---

## 範例：care-food-assessor

餐點相片 → IDDSI 等級 + HKCSS 合規結論 + 調整建議。

```json
// Request
{
  "skill": "care-food-assessor",
  "version": "1.0",
  "input": {
    "photo_url": "https://cdn.example.com/meal/rice-and-fish.jpg",
    "context": {
      "resident_age": 82,
      "known_diagnosis": ["dysphagia", "stroke"]
    }
  }
}

// Response
{
  "iddsi_level": 4,
  "iddsi_label": "Pureed",
  "compliant": true,
  "verdict": "Meal meets HKCSS Care Food Standard at IDDSI Level 4.",
  "modifications": [],
  "confidence": 0.91,
  "standard_ref": "HKCSS Care Food Standard 2023, §3.2"
}
```

---

## 快速開始 {#quick-start}

幾分鐘內為任何 OpenClaw 相容 AI 代理加入照護食智能。

**1. 安裝**

```bash
$ npm install @seniordeli/care-food-assessor
```

**2. 整合**

```typescript
import { CareFoodAssessor } from "@seniordeli/care-food-assessor";

const assessor = new CareFoodAssessor({
  // 無需 API 金鑰——由 OpenClaw 代理執行環境處理身份驗證
});

const result = await assessor.assess({
  photoUrl: mealPhotoUrl,
  residentProfile: { age: 82, diagnosis: ["dysphagia"] },
});

console.log(result.iddsiLevel);   // 4
console.log(result.compliant);    // true
console.log(result.verdict);      // "Meal meets HKCSS Care Food Standard…"
```

無需 API 金鑰——身份驗證由 OpenClaw 代理執行環境處理。技能在支援設備上本地運行；代理缺乏本地推理能力時可使用雲端備援。

---

## 支援語言

技能自動以代理的當前語言環境回應——無需手動設定語言。

- 粵語 Cantonese
- English
- Filipino · Tagalog
- Bahasa Indonesia

*普通話（zh-CN）支援計劃於2026年第三季推出。日語版本評估中。*

---

## 標準歸屬聲明

本技能集依據香港社會服務聯會（HKCSS）照護食指引 2023——香港住宿安老服務質地調整食品的權威參考。Carewells Limited 以 HKCSS 社會企業發展（SED）合作伙伴、社企樹標誌 #131 身份運營本技能集。

- 主要依據：香港社會服務聯會照護食指引 2023（HKCSS Guideline of Care Food Standard 2023）
- 運營方：Carewells Limited — HKCSS SED 合作伙伴，社企樹標誌 #131
- HKCSS 衍生內容依 CC-BY-SA 4.0 授權發布。技能代碼採用 Apache-2.0 授權。

---

## 安全與私隱

| | |
|---|---|
| 🔒 **不集中儲存個人資料** | 餐點相片及住客背景資料僅作即時處理。SeniorDeli 基礎設施不儲存任何可識別個人身份的資訊。 |
| ⚡ **邊緣推理** | 技能針對 OpenClaw 代理執行環境內的本地設備執行優化，確保敏感護理數據保留在院舍網絡範圍內。 |
| 📊 **採用指數** | 匿名化的聚合推理日誌輸入香港照護食採用指數——一個追蹤全港照護食標準普及程度的公開數據集。 |

---

## 獲取技能 {#get-skills}

可從 npm、GitHub 及 ClawHub 取得。所有合規 AI 代理均可免費使用，無需 API 金鑰。

- [npm: @seniordeli/care-food-assessor](https://www.npmjs.com/package/@seniordeli/care-food-assessor)
- [npm: @seniordeli/dysphagia-screener](https://www.npmjs.com/package/@seniordeli/dysphagia-screener)
- [npm: @seniordeli/care-food-recipe-modifier](https://www.npmjs.com/package/@seniordeli/care-food-recipe-modifier)
- [在 GitHub 查看](https://github.com/seniordeli/care-food-skills)
- [🦀 在 ClawHub 瀏覽](https://openclaw.ai/skills/seniordeli-care-food)

*所有合規 OpenClaw AI 代理免費使用 · Apache-2.0 + CC-BY-SA 4.0*

---

## 參考資料

1. [香港社會服務聯會照護食指引 2023（HKCSS Guideline of Care Food Standard 2023）](https://www.hkcss.org.hk)
2. [IDDSI 國際吞嚥困難飲食標準化倡議——完整框架](https://iddsi.org)
3. [OpenClaw——開放國際 AI 智能代理技能生態系統](https://openclaw.ai)
4. [PQSafe——姊妹項目：pqsafe-pay 技能，HKU TEC iDendron 隊列 HKU25-05](https://pqsafe.xyz/openclaw-skill)
5. TechUp Y06——創新科技署驗證資助（實績佐證）
6. [HKU TEC iDendron——培育計劃，隊列 HKU25-05](https://www.hkutec.hk/idendron)

HKCSS 照護食標準內容依 CC-BY-SA 4.0 授權轉載。IDDSI 框架 © IDDSI——僅供教育參考用途轉載。OpenClaw 生態系統合作伙伴（OpenAI、騰訊、ByteDance、NVIDIA）均為獨立第三方；並不意味 Carewells Limited / SeniorDeli 與其有任何正式合作關係。

---

[← 返回吞嚥困難知識庫](/zh-hant-hk/) · [seniordeli.com/openclaw](https://www.seniordeli.com/zh-HK/openclaw)
