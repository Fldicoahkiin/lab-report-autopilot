# Evidence and screenshots

## Build an evidence plan

Create one row per result that the report will claim:

| ID | Claim | Action | Visible proof | App/host | Planned caption |
| --- | --- | --- | --- | --- | --- |
| E01 | Database query returned three rows | Run the final SELECT | Query text, result grid, and row count | DataGrip on macOS | 图1 查询条件及返回结果 |

Do not draft a success claim until its proof exists.

## Capture the right state

- Capture the result after the action completes.
- Include enough application context to identify the software and target.
- Keep the command, relevant parameters, and result visible together when possible.
- For GUI configuration, capture the final field values and the resulting behavior, not only the settings dialog.
- For a simple experiment, keep two to four figures that cover the main procedure and result.
- Preserve failed-state screenshots in working files only when they explain an adaptation. Do not place a resolved permission or startup error in the finished report unless it affects the result.
- Use a clear filename sequence such as `01-environment.png`, `02-query-result.png`, and `03-verification.png`.

Avoid:

- screenshots with no explanation;
- repeated images for different claims;
- tiny two-column figures whose text cannot be read at 100% page zoom;
- full-desktop captures containing irrelevant messages or personal files;
- cropped images that hide the command, target, error, or result needed to verify the claim;
- generated, downloaded, or borrowed images presented as execution evidence.

## Preserve and sanitize

1. Keep the original capture unchanged.
2. Work on a copy if cropping or redaction is needed.
3. Redact credentials, tokens, private hostnames, customer data, internal repository names, and unrelated personal notifications.
4. Keep non-sensitive values visible when they are required to understand the experiment.
5. Never blur a value and then quote it as if the reader could verify it.
6. Do not upload sensitive screenshots to third-party tools without specific user approval.

## Verify the evidence set

Run:

```bash
python scripts/evidence_manifest.py evidence --output evidence-manifest.json
```

Review:

- every file opens;
- width and height are adequate for the intended placement;
- duplicate hashes are either removed or justified;
- filenames match the planned order;
- each claim maps to one or more files;
- timestamps, host roles, IP addresses, and versions agree with the notes.

## Place figures in the report

- Put a figure directly after the paragraph that introduces it.
- Use a short factual caption that states what the reader should verify.
- Refer to the visible value in the following observation.
- Preserve aspect ratio.
- Use one large figure instead of two small figures when terminal or UI text would otherwise become unreadable.
- Crop empty margins, but retain application and target context.
- Number figures in first-reference order.
- When a packet filter leaves only one or two rows, drag the horizontal pane divider upward so the decoded protocol fields use the empty space below the packet list.
- For a full-flow packet figure, leave enough list height to show the connection sequence. For request or response figures, favor the decoded-field pane.

An explanation should read like:

> 在查询窗口执行筛选语句后，结果区返回 3 条记录，如图 2 所示。结果中的课程号均为 `C03`，说明连接条件和筛选条件同时生效。

Do not write only “运行结果如下” or “截图如下”.
