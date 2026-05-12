---
layout: default
title: "OpenClaw Care Food Skills — HKCSS-Grounded AI Agent Skills"
description: "Hong Kong's Care Food Standard published as native multilingual AI agent skills. Built OpenClaw-native. Free for any compliant AI agent. Grounded in HKCSS Care Food Standard 2023."
lang: en
canonical: "https://dysphagia.cn/en/openclaw/"
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "SeniorDeli Care Food Skills — OpenClaw",
  "applicationCategory": "HealthApplication",
  "operatingSystem": "Any (OpenClaw-compatible AI agent runtime)",
  "description": "Hong Kong's Care Food Standard published as native multilingual AI agent skills. Built OpenClaw-native. Free for any compliant AI agent. Grounded in HKCSS Care Food Standard 2023.",
  "url": "https://dysphagia.cn/en/openclaw/",
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
    "description": "Free for any compliant AI agent"
  }
}
</script>

<nav aria-label="Breadcrumb">
<p><a href="/en/">Home</a> / OpenClaw Skills</p>
</nav>

---

## 🦀 OpenClaw · Ships 19 May 2026 · Free for Compliant Agents

# Hong Kong's Care Food Standard, published as native multilingual AI agent skills

Built OpenClaw-native. Free for any compliant AI agent. Available in 4 languages. Grounded in HKCSS Care Food Standard 2023 — operated by Carewells Limited under HKCSS SED + SE Tree Mark #131.

**[Get the Skills](#get-skills)** · **[Quick Start](#quick-start)**

> Primary landing: [seniordeli.com/openclaw](https://www.seniordeli.com/en/openclaw)

---

## Why Care Food AI Skills, Why Now

Hong Kong's ageing population faces a silent crisis at the dinner table. As AI agents proliferate across eldercare workflows, no standard skill set addresses nutrition safety in the home or care facility — until now.

| | |
|---|---|
| **1.6M** | Elderly residents in Hong Kong by 2036 |
| **40–60%** | RCHE residents affected by dysphagia |
| **640K** | Untrained informal caregivers handling meal preparation |
| **380K** | Foreign domestic helpers facing language gaps in care food instructions |

---

## What the Skill Set Exposes {#skills}

Six purpose-built skills, each callable from any OpenClaw-compatible AI agent runtime.

| Skill identifier | Description |
|---|---|
| `care-food-assessor` | Analyses a meal photo or ingredient list and returns IDDSI level, HKCSS compliance verdict, and recommended modifications. |
| `care-food-cantonese` | Delivers care food guidance and texture modification instructions in fluent Cantonese — audio and text output. |
| `care-food-tagalog` | Provides the same compliance guidance in Tagalog for Filipino domestic helper caregivers. |
| `care-food-bahasa` | Indonesian Bahasa variant — care food instructions and dysphagia risk warnings for Indonesian caregivers. |
| `dysphagia-screener` | Lightweight pre-screening questionnaire (non-diagnostic) that flags swallowing risk and recommends professional assessment referral. |
| `care-food-recipe-modifier` | Takes any Cantonese or Western recipe and restructures it to target IDDSI level while preserving flavour profile and nutritional density. |

---

## Example: care-food-assessor

Meal photo → IDDSI Level + HKCSS compliance verdict + modification recommendations.

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

## Quick Start {#quick-start}

Add care food intelligence to any OpenClaw-compatible AI agent in minutes.

**1. Install**

```bash
$ npm install @seniordeli/care-food-assessor
```

**2. Integrate**

```typescript
import { CareFoodAssessor } from "@seniordeli/care-food-assessor";

const assessor = new CareFoodAssessor({
  // No API key required — runs on OpenClaw agent runtime
});

const result = await assessor.assess({
  photoUrl: mealPhotoUrl,
  residentProfile: { age: 82, diagnosis: ["dysphagia"] },
});

console.log(result.iddsiLevel);   // 4
console.log(result.compliant);    // true
console.log(result.verdict);      // "Meal meets HKCSS Care Food Standard…"
```

No API key required — authentication is handled by the OpenClaw agent runtime. Skills run on-device where supported; cloud fallback available for agents without local inference capability.

---

## Supported Languages

Skills respond in the agent's active language context — no locale configuration required.

- 粵語 Cantonese
- English
- Filipino · Tagalog
- Bahasa Indonesia

*Mandarin (zh-CN) support planned for Q3 2026. Japanese variant under evaluation.*

---

## Standard Attribution

These skills are grounded in the HKCSS Guideline of Care Food Standard 2023 — Hong Kong's authoritative reference for texture-modified foods in residential care settings. Carewells Limited operates these skills as a registered HKCSS Social Enterprise Development (SED) partner under SE Tree Mark #131.

- Primary standard: HKCSS Guideline of Care Food Standard 2023 (香港社會服務聯會照護食指引)
- Operator: Carewells Limited — HKCSS SED partner, SE Tree Mark #131
- HKCSS-derived content is published under CC-BY-SA 4.0. Skill code is Apache-2.0 licensed.

---

## Security & Privacy

| | |
|---|---|
| 🔒 **No Centralised PII** | Meal photos and resident context data are processed transiently. No personally identifiable information is stored in SeniorDeli infrastructure. |
| ⚡ **Edge Inference** | Skills are optimised for on-device execution within the OpenClaw agent runtime, keeping sensitive care data local to the facility's network. |
| 📊 **Adoption Index** | Anonymous, aggregate inference logs feed the Hong Kong 照護食 Adoption Index — a public dataset tracking care food standard uptake across the territory. |

---

## Get the Skills {#get-skills}

Available on npm, GitHub, and ClawHub. Free for any compliant AI agent. No API key required.

- [npm: @seniordeli/care-food-assessor](https://www.npmjs.com/package/@seniordeli/care-food-assessor)
- [npm: @seniordeli/dysphagia-screener](https://www.npmjs.com/package/@seniordeli/dysphagia-screener)
- [npm: @seniordeli/care-food-recipe-modifier](https://www.npmjs.com/package/@seniordeli/care-food-recipe-modifier)
- [View on GitHub](https://github.com/seniordeli/care-food-skills)
- [🦀 Browse on ClawHub](https://openclaw.ai/skills/seniordeli-care-food)

*Free for any compliant OpenClaw AI agent · Apache-2.0 + CC-BY-SA 4.0*

---

## References

1. [HKCSS Guideline of Care Food Standard 2023 (香港社會服務聯會照護食指引)](https://www.hkcss.org.hk)
2. [IDDSI International Dysphagia Diet Standardisation Initiative — Full Framework](https://iddsi.org)
3. [OpenClaw — Open International AI Agent Skill Ecosystem](https://openclaw.ai)
4. [PQSafe — Sister project: pqsafe-pay skill, HKU TEC iDendron cohort HKU25-05](https://pqsafe.xyz/openclaw-skill)
5. TechUp Y06 — Innovation and Technology Commission validation grant (validation track record)
6. [HKU TEC iDendron — incubation programme, cohort HKU25-05](https://www.hkutec.hk/idendron)

HKCSS Care Food Standard content reproduced under CC-BY-SA 4.0. IDDSI framework © IDDSI — reproduced for educational reference. OpenClaw ecosystem partners (OpenAI, Tencent, ByteDance, NVIDIA) are independent parties; no formal partnership with Carewells Limited / SeniorDeli is implied.

---

[← Back to Dysphagia Knowledge Hub](/en/) · [seniordeli.com/openclaw](https://www.seniordeli.com/en/openclaw)
