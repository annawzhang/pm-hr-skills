# Playbook · 人力量化实验 SOP

演示：[People Stats Kit](https://annawzhang.github.io/people-stats-kit/)

## 开实验前
- [ ] 写清单一变量（文案 / 分层策略 / 渠道）
- [ ] 用双比例样本量估算：基线率、目标率、α、功效
- [ ] 约定排他：混合进组样本不参与对比（NOT EXISTS 思路）

## 跑完后
- [ ] 双比例 z 检验：报告 rate、lift、z、p
- [ ] 漏斗各步给 Wilson 95% CI，不要只看点估计
- [ ] 招聘周期用 Kaplan–Meier，区分事件与删失
- [ ] 评分模型做分箱校准 + Brier，高分档转化应更高

## 禁止
- 未算样本量就宣称「AB 失败」
- 把删失当成失败入职
- 用黑盒分数做决策却不看校准
