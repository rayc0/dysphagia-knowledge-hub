---
layout: default
title: "OpenClaw 照护食技能集 — 符合 HKCSS 标准的多语言 AI Agent 技能"
description: "香港照护食标准发布为原生多语言 AI Agent 技能。基于 OpenClaw 构建。所有合规 AI Agent 均可免费调用。依据 HKCSS 照护食指引 2023。"
lang: zh-hans
canonical: "https://softmeal.org/zh-hans/openclaw/"
robots: noindex
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "SeniorDeli 照护食技能集 — OpenClaw",
  "applicationCategory": "HealthApplication",
  "operatingSystem": "Any (OpenClaw-compatible AI agent runtime)",
  "description": "香港照护食标准发布为原生多语言 AI Agent 技能。基于 OpenClaw 构建。所有合规 AI Agent 均可免费调用。",
  "url": "https://softmeal.org/zh-hans/openclaw/",
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
    "description": "所有合规 AI Agent 免费调用"
  }
}
</script>

<nav aria-label="页面路径">
<p><a href="/zh-hans/">首页</a> / OpenClaw 技能</p>
</nav>

---

## 🦀 OpenClaw · 2026年5月19日发布 · 合规 Agent 免费调用

# 香港照护食标准，以原生多语言 AI Agent 技能形式开放

基于 OpenClaw 生态原生构建。所有符合标准的 AI Agent 均可免费调用，支持 4 种语言。内容依据香港社会服务联会（HKCSS）照护食指引 2023，由 Carewells Limited 以 HKCSS SED 合作伙伴（社企树标志 #131）身份运营。

**[获取技能包](#get-skills)** · **[快速接入](#quick-start)**

> 主要登陆页：[seniordeli.com/openclaw](https://www.seniordeli.com/zh-CN/openclaw)

---

## 为什么是照护食 AI 技能，为什么是现在

香港老龄化人口在饮食安全层面面临结构性缺口。随着 AI Agent 在安老护理流程中加速渗透，业界至今缺乏一套覆盖家庭及院舍场景的食品安全标准技能集——直至现在。

| | |
|---|---|
| **160万** | 2036年香港长者人口预测 |
| **40–60%** | 安老院舍住客受吞咽困难影响 |
| **64万** | 无专业培训的非正式照护者负责膳食准备 |
| **38万** | 外籍家政人员面临照护食指引的语言障碍 |

---

## 技能集能力边界 {#skills}

六个专用技能，可从任何 OpenClaw 兼容的 AI Agent 运行时直接调用。

| 技能标识符 | 功能说明 |
|---|---|
| `care-food-assessor` | 输入餐点图片或食材清单，返回 IDDSI 等级、HKCSS 合规判定及修改建议。 |
| `care-food-cantonese` | 以流利粤语输出照护食指导及质地调整指引，支持语音与文本双模态输出。 |
| `care-food-tagalog` | 以菲律宾语（他加禄语）为菲籍家政照护人员提供同等合规指引。 |
| `care-food-bahasa` | 印尼语版本——为印尼籍照护人员提供照护食说明及吞咽风险预警。 |
| `dysphagia-screener` | 轻量级预筛查问卷（非诊断性），标记吞咽风险并建议专业评估转介。 |
| `care-food-recipe-modifier` | 接收任意粤式或西式食谱，重构至目标 IDDSI 等级，同时保留风味特征与营养密度。 |

---

## 示例：care-food-assessor

餐点图片 → IDDSI 等级 + HKCSS 合规判定 + 修改建议。

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

## 快速接入 {#quick-start}

数分钟内为任何 OpenClaw 兼容 AI Agent 集成照护食智能能力。

**1. 安装**

```bash
$ npm install @seniordeli/care-food-assessor
```

**2. 集成**

```typescript
import { CareFoodAssessor } from "@seniordeli/care-food-assessor";

const assessor = new CareFoodAssessor({
  // 无需 API 密钥——由 OpenClaw Agent 运行时处理身份验证
});

const result = await assessor.assess({
  photoUrl: mealPhotoUrl,
  residentProfile: { age: 82, diagnosis: ["dysphagia"] },
});

console.log(result.iddsiLevel);   // 4
console.log(result.compliant);    // true
console.log(result.verdict);      // "Meal meets HKCSS Care Food Standard…"
```

无需 API 密钥——身份验证由 OpenClaw Agent 运行时处理。技能在支持设备上本地运行；Agent 缺乏本地推理能力时可使用云端备援。

---

## 支持语言

技能自动以 Agent 的当前语言环境响应——无需手动配置语言。

- 粵語 Cantonese
- English
- Filipino · Tagalog
- Bahasa Indonesia

*普通话（zh-CN）支持计划于2026年第三季度推出。日语版本评估中。*

---

## 标准归属声明

本技能集依据香港社会服务联会（HKCSS）照护食指引 2023——香港住宿安老服务质地调整食品的权威参考。Carewells Limited 以 HKCSS 社会企业发展（SED）合作伙伴、社企树标志 #131 身份运营本技能集。

- 主要依据：香港社会服务联会照护食指引 2023（HKCSS Guideline of Care Food Standard 2023）
- 运营方：Carewells Limited — HKCSS SED 合作伙伴，社企树标志 #131
- HKCSS 衍生内容依 CC-BY-SA 4.0 授权发布。技能代码采用 Apache-2.0 授权。

---

## 安全与隐私

| | |
|---|---|
| 🔒 **不集中存储个人信息** | 餐点图片及住客背景数据仅作即时处理。SeniorDeli 基础设施不存储任何可识别个人身份的信息。 |
| ⚡ **边缘推理** | 技能针对 OpenClaw Agent 运行时内的本地设备执行优化，确保敏感护理数据保留在院舍网络范围内。 |
| 📊 **采用指数** | 匿名化的聚合推理日志输入香港照护食采用指数——一个追踪全港照护食标准普及程度的公开数据集。 |

---

## 获取技能包 {#get-skills}

可从 npm、GitHub 及 ClawHub 获取。所有合规 AI Agent 均可免费调用，无需 API 密钥。

- [npm: @seniordeli/care-food-assessor](https://www.npmjs.com/package/@seniordeli/care-food-assessor)
- [npm: @seniordeli/dysphagia-screener](https://www.npmjs.com/package/@seniordeli/dysphagia-screener)
- [npm: @seniordeli/care-food-recipe-modifier](https://www.npmjs.com/package/@seniordeli/care-food-recipe-modifier)
- [在 GitHub 查看](https://github.com/seniordeli/care-food-skills)
- [🦀 在 ClawHub 浏览](https://openclaw.ai/skills/seniordeli-care-food)

*所有合规 OpenClaw AI Agent 免费调用 · Apache-2.0 + CC-BY-SA 4.0*

---

## 参考资料

1. [香港社会服务联会照护食指引 2023（HKCSS Guideline of Care Food Standard 2023）](https://www.hkcss.org.hk)
2. [IDDSI 国际吞咽困难饮食标准化倡议——完整框架](https://iddsi.org)
3. [OpenClaw——开放国际 AI 智能代理技能生态系统](https://openclaw.ai)
4. [PQSafe——姊妹项目：pqsafe-pay 技能，HKU TEC iDendron 队列 HKU25-05](https://pqsafe.xyz/openclaw-skill)
5. TechUp Y06——创新科技署验证资助（实绩佐证）
6. [HKU TEC iDendron——培育计划，队列 HKU25-05](https://www.hkutec.hk/idendron)

HKCSS 照护食标准内容依 CC-BY-SA 4.0 授权转载。IDDSI 框架 © IDDSI——仅供教育参考用途转载。OpenClaw 生态系统合作伙伴（OpenAI、腾讯、ByteDance、NVIDIA）均为独立第三方；并不意味 Carewells Limited / SeniorDeli 与其有任何正式合作关系。

---

[← 返回吞咽困难知识库](/zh-hans/) · [seniordeli.com/openclaw](https://www.seniordeli.com/zh-CN/openclaw)
