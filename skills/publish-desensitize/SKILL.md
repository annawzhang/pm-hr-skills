---
name: publish-desensitize
description: >
  公开发布前脱敏检查：扫描手机号、邮箱、内网 URL、工号/门店明细、密钥形态字符串，
  输出风险清单与改写建议。用于开源 README、Pages、Skill、Demo 上线前自检。
  当用户提到脱敏、脱敏检查、能不能公开、防泄漏、publish checklist 时使用。
disable-model-invocation: true
---

# 发布脱敏检查（Publish Desensitize）· L4 治理

零密钥、本地规则。在 **Push / Pages 发布前**跑一遍，降低误传企业数据风险。

## 扫描类别（公开示例）

| 类别 | 示例模式（说明级） | 处置建议 |
|---|---|---|
| 手机号 | 大陆 11 位号段 | 删除或改 `138****0000` |
| 邮箱 | 企业域名邮箱 | 改 `name@example.com` |
| 内网 | `http://10.*` / `*.local` / 内网域名 | 删除；改「内部系统」 |
| 密钥形态 | `sk-` / `Bearer ` / `SECRET=` / 私钥头 | **必须删除**；改 `.env.example` |
| 身份 | 真实姓名+工号+证件号并列 | 改虚构 fixture |
| 经营明细 | 真实门店名/店码表 | 改虚构门店 |

## 输出模板

```text
文件：…
风险：
- [P0] path:line 疑似密钥 → 删除
- [P1] path:line 疑似手机号 → 脱敏
结论：可公开发布 / 修复后再发
```

## 发布门禁清单

- [ ] README 有虚构/脱敏声明  
- [ ] LICENSE + 版权短句  
- [ ] 无 `.env`（仅有 `.env.example`）  
- [ ] Demo 数据为 synth/fixture  
- [ ] 私有仓未误设 Public  

## 禁止

- 不要把扫描到的真实密钥写进 Issue/聊天记录长期保存；本地改完即止
- 本 Skill 不替代专业秘钥扫描服务，只作开源前人工辅助
