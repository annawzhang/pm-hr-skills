---
name: tool-whitelist
description: >
  Agent 工具白名单：主调度只能调用允许列表中的工具；未授权工具一律拒绝并说明原因。
  用于防「模型随便调 API / 乱推进流程」。当用户提到 tool whitelist、工具白名单、
  Agent 只能调引擎、禁止任意函数调用、Hiring Agent 护栏时使用。
disable-model-invocation: true
---

# 工具白名单（Tool Whitelist）· L1/L2

零密钥。对应能力层：**主调度只路由到白名单 Skill，不开放任意代码执行**。

## 硬规则

1. **先列白名单，再对话**：启动前写清 `tool_id / 入参模式 / 副作用 / 是否需二次确认`。
2. **未在名单 → 拒绝**：返回「该操作不在允许工具内」，不要改去调别的工具「凑合」。
3. **有副作用必须确认**：推进候选人、群发消息、删改知识库 → 需显式确认或授权令牌（公开 Demo 可用布尔 `authorized`）。
4. **每次调用留痕**：`tool_id + args摘要 + 结果态`（成功/拒绝/错误），便于审计。

## 交付模板

```text
白名单：
- screen(cand_id) trim 无副作用
- advance(cand_id) 需确认
- reject(cand_id, reason) 需确认
当前请求：…
判定：允许 / 拒绝（原因）
若允许：调用结果 + 留痕 id
```

## 与公开 Demo

| Demo | 体现 |
|---|---|
| [Hiring Agent](https://annawzhang.github.io/hiring-agent/) | 只调 `Hire.*`；反馈未齐则推进失败 |
| [VOC Agent](https://annawzhang.github.io/voc-voice-agent/) | 只调 search/stats/ceiling/fourStep/checkScript |
| [Sales Ops](https://annawzhang.github.io/sales-ops-assistant/) | 未授权不群发 |

## 禁止

- 不要在公开仓写真实 API Host / Token
- 不要用「模型判断可以」绕过白名单
