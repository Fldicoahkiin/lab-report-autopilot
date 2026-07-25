# User-supplied and private material

The user's template, identity fields, dates, school details, organization details, and handling instructions control what may be written. Fill supplied values exactly and do not guess missing personal information.

## Separate three fact classes

| Class | Allowed use |
| --- | --- |
| Public fact | Cite the current official or public source |
| User-confirmed personal fact | Use only where the user authorizes it |
| Private workplace fact | Use only as authorized; otherwise replace it with a general description or a local reproduction |

Never move customer names, internal hostnames, IP addresses, alert details, asset identifiers, staff names, screenshots, credentials, ticket text, file paths, or private datasets into the report repository.

## Convert work into a local reproduction

1. Name the general skill involved, such as endpoint inventory, suspicious outbound-connection review, false-positive analysis, weak-password remediation, or alert triage.
2. Build a new exercise with public data, synthetic logs, or the user's own local virtual machines.
3. Reproduce the method, not the production event.
4. Capture new evidence from Windows, Linux, or macOS in the local lab.
5. State the boundary in the report:

> 为避免接触真实业务数据，以下步骤在本地隔离环境中复现同类处理流程，截图与结果均来自本次自建实验。

6. Describe genuine workplace duties only at a general level confirmed by the user.
7. Label local screenshots as local reproduction evidence. Do not present them as production screenshots.

## Professional-practice wording

Use:

- “参与终端安全告警的分类与复核” when the user confirms that duty;
- “在本地环境复现异常外联分析流程” for the report's demonstrable exercise;
- “根据域名、目标地址、进程和时间线判断告警是否需要继续处置” when those are the local analysis fields.

Avoid claims about a named customer, production incident, exact event count, remediation outcome, or internal platform unless the user explicitly approves the fact for disclosure.

Public company facts can be researched when drafting the report. Verify them at that time and cite the public source.
