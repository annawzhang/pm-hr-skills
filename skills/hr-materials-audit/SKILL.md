---
name: hr-materials-audit
description: >
  人力运营材料审核工作流：对入职/在职材料做字段核对与合规规则检查
  （姓名比对、证件过期、年龄范围、姓氏示例规则、证件照眼镜关键词），
  输出异常编码与汇总。用于 HR 材料审核、入职资料合规检查、员工档案批量校验。
  当用户提到人力运营材料审核、员工材料审核、入职材料 OCR 审核、身份证/学历/合同审核时使用。
disable-model-invocation: true
---

# 人力运营材料审核

## 目标

把「读表 → 取材料字段 → 规则审核 → 写回结果 → 汇总异常」做成可重复执行的流程。  
本公开版用**本地 JSON fixture**演示规则引擎；真实环境可替换为表格 API / OCR / 消息通道。

## 步骤

1. 读取员工主数据（工号、系统姓名、证件有效期、出生日期等）
2. 读取各材料字段（身份证 / 学历 / 合同）；公开版直接读 fixture 里的 `ocr_fields`
3. 对每人执行规则包，得到 `issue_codes` / `issues` / `is_abnormal`
4. 汇总异常工号，生成 `hr_audit_summary.json`
5. （可选）由宿主系统发送通知；本仓库不内置真实 IM 凭证

## 规则包（示例）

| 编码 | 含义 |
|---|---|
| NAME_MISMATCH | 系统姓名与证件/合同/学历姓名不一致 |
| ID_EXPIRED | 证件有效期止 < 今天 |
| AGE_OUT_OF_RANGE | 年龄不在 22–60 |
| SURNAME_NOT_TOP20 | 姓氏不在示例百家姓 TOP20（教学用，可替换） |
| PHOTO_GLASSES | 证件照 OCR 文本含眼镜相关词（真实场景应用 CV） |

## 命令

```bash
python3 scripts/audit_rules.py --input fixtures/employees.json
python3 scripts/audit_rules.py --self-test
```

## 接入真实系统时

- 材料下载、OCR、表格读写用环境变量配置，**不要把 URL / Token 写进 Skill**
- 通知通道（飞书等）只读 `FEISHU_APP_ID` / `FEISHU_APP_SECRET` 等环境变量
- 规则阈值（年龄区间、姓氏名单）放到可编辑配置，便于业务方审查

## 参考

- `references/table_schema.md`：字段字典
- `fixtures/employees.json`：虚构员工样例
