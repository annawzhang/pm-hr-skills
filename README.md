# PM / HR Skills & Playbooks

**把实习里验证过的产品与运营方法，抽成可复用的 Cursor Agent Skill 和 Markdown Playbook。**  
数据、接口、表格均为虚构示例；不含任何公司内部地址或真实员工信息。

| 类型 | 名称 | 一句话 |
|---|---|---|
| Skill | [人力运营材料审核](skills/hr-materials-audit/) | OCR/结构化字段 + 5 条合规规则 + 异常汇总（本地 fixture 可跑） |
| Skill | [结构化招聘](skills/structured-hiring/) | 开岗评分卡 → 证据化初筛 → 独立反馈 → 校准复盘 |
| Playbook | [structured-hiring](playbooks/structured-hiring.md) | 招聘流程 SOP（对齐 Greenhouse / Ashby 思路） |
| Playbook | [outreach-approval](playbooks/outreach-approval.md) | 业务群触达：预览 → 授权 → 群发 → 留痕 |
| Playbook | [voc-script-qa](playbooks/voc-script-qa.md) | 舆情洞察 → 话术 → 禁止话术检查 |

可运行的产品演示见：[hiring-copilot](https://github.com/annawzhang/hiring-copilot) · [sales-ops-assistant](https://github.com/annawzhang/sales-ops-assistant) · [voc-insight-kit](https://github.com/annawzhang/voc-insight-kit) · [hris-prototype](https://github.com/annawzhang/hris-prototype)


| Playbook | [people-stats](playbooks/people-stats.md) | 开实验前算样本量，跑完看 p 值 / 漏斗 CI / 周期 / 校准 |
| Demo | [People Stats Kit](https://github.com/annawzhang/people-stats-kit) | 可运行报告 |
| Demo | [VOC Voice Agent](https://github.com/annawzhang/voc-voice-agent) | 原声对话 Agent |

## 怎么用 Skill

把 `skills/<name>` 复制到你的 Cursor Agent Skills 目录（或本机 `~/.cursor/skills/`），在对话里点名触发，例如：「按 hr-materials-audit 审核这批入职材料」。

## 本地跑材料审核示例

```bash
cd skills/hr-materials-audit
python3 scripts/audit_rules.py --input fixtures/employees.json
python3 scripts/audit_rules.py --self-test
```

## 背景

公开学习与求职作品。规则与流程来自作者在 HR / 销售策略产品实习中的方法抽象，**不是任何公司的内部系统或真实数据导出**。
