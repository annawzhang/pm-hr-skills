#!/usr/bin/env python3
"""本地可跑的入职材料合规规则引擎（虚构数据，无外部依赖）。"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path

TOP20_SURNAMES = list("赵钱孙李周吴郑王冯陈褚卫蒋沈韩杨朱秦尤许")
GLASSES_KEYWORDS = ("眼镜", "佩戴眼镜", "glasses", "spectacles")


def parse_date(date_str: str) -> datetime | None:
    if not date_str:
        return None
    for fmt in ("%Y/%m/%d", "%Y-%m-%d", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%dT%H:%M:%S"):
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    return None


def calculate_age(dob_str: str, today: datetime | None = None) -> int | None:
    dob = parse_date(dob_str)
    if not dob:
        return None
    today = today or datetime.now()
    age = today.year - dob.year
    if (today.month, today.day) < (dob.month, dob.day):
        age -= 1
    return age


def audit_employee(emp: dict, ocr_fields: dict | None = None, today: datetime | None = None) -> dict:
    """执行 5 项示例规则，返回 issue_codes / issues / is_abnormal。"""
    today = today or datetime.now()
    ocr_fields = ocr_fields or emp.get("ocr_fields") or {}
    issues: list[str] = []
    codes: list[str] = []

    system_name = (emp.get("name") or "").strip()
    id_name = (ocr_fields.get("id_card", {}).get("name") or system_name).strip()
    contract_name = (ocr_fields.get("labor_contract", {}).get("name") or system_name).strip()
    degree_name = (ocr_fields.get("degree", {}).get("name") or system_name).strip()
    names = [n for n in (system_name, id_name, contract_name, degree_name) if n]
    if len(set(names)) > 1:
        issues.append(f"姓名不一致: {sorted(set(names))}")
        codes.append("NAME_MISMATCH")

    valid_to = parse_date(emp.get("id_valid_to", ""))
    if valid_to and valid_to.replace(tzinfo=None) < today.replace(tzinfo=None):
        issues.append("证件已过期")
        codes.append("ID_EXPIRED")

    age = None
    if emp.get("age"):
        try:
            age = int(emp["age"])
        except ValueError:
            age = calculate_age(emp.get("dob", ""), today)
    else:
        age = calculate_age(emp.get("dob", ""), today)
    if age is not None and (age < 22 or age > 60):
        issues.append("年龄不在 22-60 范围")
        codes.append("AGE_OUT_OF_RANGE")

    check_name = system_name or id_name
    if check_name and check_name[0] not in TOP20_SURNAMES:
        issues.append("姓氏不在百家姓 TOP20（示例规则）")
        codes.append("SURNAME_NOT_TOP20")

    id_text = ocr_fields.get("id_card", {}).get("raw_text", "") or ""
    if any(kw in id_text for kw in GLASSES_KEYWORDS):
        issues.append("身份证照片检测到戴眼镜关键词")
        codes.append("PHOTO_GLASSES")

    return {
        "emp_id": emp.get("emp_id", ""),
        "issue_codes": codes,
        "issues": issues,
        "is_abnormal": "是" if codes else "否",
        "age_calculated": age,
    }


def run_batch(employees: list[dict], today: datetime | None = None) -> dict:
    results = [audit_employee(e, today=today) for e in employees]
    abnormal = [r["emp_id"] for r in results if r["is_abnormal"] == "是"]
    return {
        "total": len(results),
        "abnormal_count": len(abnormal),
        "abnormal_emps": abnormal,
        "results": results,
    }


def self_test() -> None:
    today = datetime(2026, 10, 13)
    ok = {
        "emp_id": "E001",
        "name": "李明",
        "dob": "1995-05-01",
        "id_valid_to": "2030-01-01",
        "ocr_fields": {
            "id_card": {"name": "李明", "raw_text": "姓名李明"},
            "degree": {"name": "李明"},
            "labor_contract": {"name": "李明"},
        },
    }
    bad = {
        "emp_id": "E002",
        "name": "欧阳修",
        "dob": "2008-01-01",
        "id_valid_to": "2020-01-01",
        "ocr_fields": {
            "id_card": {"name": "欧阳修", "raw_text": "佩戴眼镜"},
            "degree": {"name": "欧阳修"},
            "labor_contract": {"name": "王五"},
        },
    }
    r_ok = audit_employee(ok, today=today)
    r_bad = audit_employee(bad, today=today)
    assert r_ok["is_abnormal"] == "否", r_ok
    assert "NAME_MISMATCH" in r_bad["issue_codes"]
    assert "ID_EXPIRED" in r_bad["issue_codes"]
    assert "AGE_OUT_OF_RANGE" in r_bad["issue_codes"]
    assert "SURNAME_NOT_TOP20" in r_bad["issue_codes"]
    assert "PHOTO_GLASSES" in r_bad["issue_codes"]
    print("self-test passed")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="HR materials audit rule engine")
    parser.add_argument("--input", help="employees JSON path")
    parser.add_argument("--output", help="summary JSON path")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args(argv)

    if args.self_test:
        self_test()
        return 0
    if not args.input:
        parser.error("--input or --self-test required")

    employees = json.loads(Path(args.input).read_text(encoding="utf-8"))
    if isinstance(employees, dict):
        employees = employees.get("employees", [])
    summary = run_batch(employees)
    out = Path(args.output) if args.output else Path("hr_audit_summary.json")
    out.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"total={summary['total']} abnormal={summary['abnormal_count']} -> {out}")
    for emp_id in summary["abnormal_emps"]:
        print(f"  abnormal: {emp_id}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
