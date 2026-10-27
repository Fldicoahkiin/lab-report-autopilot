from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


DISCIPLINES = {
    "packet-analysis": "网络协议与抓包分析",
    "routing-switching": "路由与交换",
    "security-operations": "网络安全运维",
    "databases": "数据库",
    "programming": "程序设计与数据结构",
    "data-visualization": "数据可视化",
    "web-development": "网页设计与开发",
    "computer-architecture": "计算机组成与体系结构",
}

TEMPLATES = {
    "lab": "lab-report.md",
    "practice": "professional-practice.md",
}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    parser.add_argument("--kind", choices=("lab", "practice"), required=True)
    parser.add_argument(
        "--discipline",
        required=True,
        help="a registry ID such as packet-analysis, or the course name when no ID fits",
    )
    parser.add_argument("--title", required=True)
    args = parser.parse_args()

    skill_dir = Path(__file__).resolve().parent.parent
    template = skill_dir / "assets" / "templates" / TEMPLATES[args.kind]
    draft = template.read_text(encoding="utf-8")
    draft = draft.replace("{{TITLE}}", args.title)
    draft = draft.replace("{{DISCIPLINE}}", DISCIPLINES.get(args.discipline, args.discipline))

    # The helper runtime step may already have created the folder.
    if (args.output / "draft.md").exists():
        sys.exit(f"report workspace already initialized: {args.output}")
    args.output.mkdir(parents=True, exist_ok=True)
    for name in ("evidence/original", "evidence/working", "notes", "src", "output"):
        (args.output / name).mkdir(parents=True, exist_ok=True)

    (args.output / "draft.md").write_text(draft, encoding="utf-8")
    format_contract = skill_dir / "assets" / "templates" / "format-contract.md"
    (args.output / "format-contract.md").write_text(
        format_contract.read_text(encoding="utf-8"),
        encoding="utf-8",
    )
    (args.output / "evidence-plan.md").write_text(
        "# 证据计划\n\n"
        "| ID | 子项 | 参考图 | 报告结论 | 产生结论的操作 | 画面中必须可见的内容 | 软件/主机 | 图题 | 文件名 | 状态 |\n"
        "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n"
        "| E01 |  |  |  |  |  |  |  | 01-.png | 待执行 |\n",
        encoding="utf-8",
    )
    config = {
        "title": args.title,
        "kind": args.kind,
        "discipline": args.discipline,
        "created_at": datetime.now().astimezone().isoformat(timespec="seconds"),
    }
    (args.output / "report-config.json").write_text(
        json.dumps(config, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


if __name__ == "__main__":
    main()
