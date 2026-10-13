# 字段字典（虚构示例）

> 不含真实多维表格链接。字段名可按贵司表结构映射。

## materials（员工主数据）

| 字段 | 类型 | 说明 |
|---|---|---|
| emp_id | text | 工号（主键） |
| name | text | 系统姓名 |
| gender | text | 性别 |
| dob | text | 出生日期 |
| age | text | 年龄（可空，空则由 dob 推算） |
| id_valid_from / id_valid_to | text | 证件有效期 |
| degree_level / degree_school / degree_major / degree_date / degree_no | text | 学历信息 |
| company / title / contract_from / contract_to / probation | text | 合同信息 |

## audit_results（审核结果）

| 字段 | 说明 |
|---|---|
| emp_id | 工号 |
| system_name / id_legal_name / degree_name / contract_name | 各来源姓名 |
| issue_codes | 规则编码列表 |
| issues | 问题描述列表 |
| is_abnormal | 是 / 否 |
