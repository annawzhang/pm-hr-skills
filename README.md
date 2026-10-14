# PM / HR Skills & Playbooks

**可公开、零密钥的 Cursor Agent Skill + SOP。**  
把「减幻觉、安全治理、招聘、触达、VOC」等方法写成 Agent 能执行的说明；示例全部虚构。

> **安全承诺**：不含 Token / 内网地址 / 真实员工或客户数据。需要密钥的部署类仓库已设为 Private，不在本仓。

## Skills（可复制到 Cursor）

| Skill | 解决什么 | 路径 |
|---|---|---|
| **[减幻觉 · 引用落地](skills/citation-grounding/)** | 无引用不下结论；检索空则拒答 | `skills/citation-grounding/` |
| **[安全治理 · 内容护栏](skills/content-safety-rails/)** | P0–P3 分级处置；输入/输出双侧检查 | `skills/content-safety-rails/` |
| [结构化招聘](skills/structured-hiring/) | 评分卡 → 证据化初筛 → 独立反馈 → 校准 | `skills/structured-hiring/` |
| [人力材料审核](skills/hr-materials-audit/) | 虚构 fixture + 5 条合规规则可跑 | `skills/hr-materials-audit/` |

## Playbooks

| Playbook | 一句话 |
|---|---|
| [citation-grounding](playbooks/citation-grounding.md) | 无证据，不发言 |
| [content-safety-rails](playbooks/content-safety-rails.md) | 分级处置 + 双侧扫描，密钥不进公开仓 |
| [structured-hiring](playbooks/structured-hiring.md) | 结构化招聘 SOP |
| [outreach-approval](playbooks/outreach-approval.md) | 预览 → 授权 → 群发 → 留痕 |
| [voc-script-qa](playbooks/voc-script-qa.md) | 原声 → 话术 → 禁止话术检查 |
| [people-stats](playbooks/people-stats.md) | 样本量 / p 值 / 漏斗 CI / 校准 |

## 对齐的公开 Demo（均可点开）

| Demo | 对应能力 |
|---|---|
| [VOC Voice Agent](https://annawzhang.github.io/voc-voice-agent/) | 减幻觉（强制 cite）+ 禁止话术 |
| [Hiring Copilot](https://annawzhang.github.io/hiring-copilot/) / [Hiring Agent](https://annawzhang.github.io/hiring-agent/) | 证据化初筛 + 推进护栏 |
| [Sales Ops Assistant](https://annawzhang.github.io/sales-ops-assistant/) | 触达授权护栏 |
| [Enterprise AI Console](https://annawzhang.github.io/enterprise-ai-console/) | 工作台权限与治理叙事 |
| [People Stats Kit](https://annawzhang.github.io/people-stats-kit/) | 可复现统计 |

手册入口：[People Product Handbook · Skills](https://annawzhang.github.io/people-product-handbook/sections/07-skills.html)

## 怎么用

```bash
# 复制到本机 Cursor Skills 目录后，对话里点名，例如：
# 「按 citation-grounding 回答，没有引用就拒答」
# 「按 content-safety-rails 给这份话术定级并给出处置」
```

材料审核可跑示例：

```bash
cd skills/hr-materials-audit
python3 scripts/audit_rules.py --self-test
```

## 背景

公开学习与面试作品。方法抽象自产品实习，**不是**任何公司的内部系统、词库或真实数据导出。
