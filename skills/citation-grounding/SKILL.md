---
name: citation-grounding
description: >
  减幻觉 / 证据护栏：回答必须绑定可核对引用（原声、文档段落、简历原文、指标定义）。
  无引用则拒答或明确标「证据不足」；禁止编造数字、政策条款、用户原话。
  当用户提到幻觉、无证据不下结论、必须引用、citation、RAG 可溯源、VOC 原声护栏时使用。
disable-model-invocation: true
---

# 减幻觉 · 引用落地（Citation Grounding）

零密钥、纯方法 Skill。适用于产品答疑、VOC、知识库 Bot、招聘初筛等「必须可核对」场景。

## 硬规则

1. **无引用，不下结论**：每一条事实性陈述旁必须有 `cite_id` / 原文片段 / 指标口径链接。
2. **检索为空 → 拒答**：输出固定句式：「当前语料/文档中没有可引用证据，不能臆造。」
3. **禁止粉饰**：缺证据时写「未知 / 样本不足」，不要用「一般来说」「业界通常」顶替。
4. **数字必须带来源**：转化率、未命中率、价位点等，写明样本 n 与计算口径。
5. **多源冲突要并列**：列出冲突引用，让人裁决，不擅自揉成一个「真相」。

## 回答模板

```text
结论：（一句话）
证据：
- [cite_id] 「原文摘录…」（来源 / 时间 / 权重如点赞）
- [cite_id] …
限制：样本 n=…；未覆盖…；因此不能推断…
下一步：（要补哪类证据 / 是否转人工）
```

## Agent 自检清单（输出前）

- [ ] 是否至少 1 条可点击/可定位的引用？
- [ ] 是否存在无 cite 的绝对化措辞（一定、保证、全网最低）？
- [ ] 是否把「检索失败」说成了肯定答案？
- [ ] 示例数据是否仍为虚构（未粘贴真实员工/客户原文）？

## 与公开 Demo 对齐

| Demo | 怎么体现本 Skill |
|---|---|
| [VOC Voice Agent](https://annawzhang.github.io/voc-voice-agent/) | `citations` 为空直接 `error` |
| [Hiring Copilot](https://annawzhang.github.io/hiring-copilot/) | 初筛分必须挂简历证据 |
| [KB Gap Finder](https://annawzhang.github.io/kb-gap-finder/) | 未命中不编 FAQ，进入补库队列 |

## 禁止

- 不要调用需要 Token / 内网地址的接口；本 Skill 只约束回答形态
- 不要在示例里写入真实工单号、员工姓名、客户手机号
