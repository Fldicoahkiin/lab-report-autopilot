---
name: lab-report-autopilot
description: Complete Chinese university lab reports (实验报告), training reports (实训报告), coursework (课程设计), and professional-practice reports (专业实践报告) from the user's instructions, identity fields, reference reports, and DOCX template. Use when an agent must set up a Windows, Linux, or macOS environment or a virtual machine (UTM, Parallels, VMware, VirtualBox, WSL); operate terminals or GUI software; run course code; capture real screenshots or packet files; analyze results; preserve the supplied Word format; and return a checked report. Covers networking, SDN, cybersecurity, operating systems, databases, programming, data visualization, web development, computer architecture, and any other computing course, researching unfamiliar subjects from official documentation.
license: MIT
---

# Lab Report Autopilot

Drive the report from assignment to delivery: inspect the files, choose the environment, run the experiment, capture the useful results, fill the user's template, and inspect the finished DOCX. Once the required files and personal fields are available, continue without asking the user to perform routine steps.

Never invent software output, screenshots, user details, citations, or environment values. Interrupt only when an unavailable environment, missing authorization, or missing required field would make the report false.

Never guess, brute-force, or derive passwords, including from student numbers or names. When a VM, guest account, remote host, or application needs credentials, ask the user once for both the account name and the password, then try exactly that pair. Keep credentials out of notes, scripts saved to disk, logs, screenshots, and the report; prefer an SSH key or a temporary `sudoers` rule that is removed when the work ends.

## Set up

Resolve the directory containing this `SKILL.md` as `SKILL_DIR`. Run bundled scripts by absolute path; the current directory may be the user's report folder rather than the skill folder.

Treat the bundled Python scripts as task tools, not as a requirement for the user to repair their global environment. Prefer a Python 3.10 or newer runtime supplied by the host Agent.

On Windows, unless the host Agent provides a known isolated runtime, run the bootstrap before any Python helper:

```powershell
$runtime = & powershell.exe -NoProfile -ExecutionPolicy Bypass `
  -File "$SKILL_DIR\scripts\bootstrap_windows.ps1" `
  -Workspace "work\report-name" | ConvertFrom-Json
$PYTHON = $runtime.python
```

The bootstrap tests `py`, `python`, and `python3`, creates a task-local virtual environment, and installs the bundled requirements there. If no usable interpreter exists, it downloads a checksum-pinned CPython installer from python.org, or from the npmmirror and Huawei Cloud mirrors when python.org fails, and installs it under the report workspace without administrator rights, PATH changes, file associations, shortcuts, or global `pip`.

A host Agent often ships its own Python but does not put it on `PATH`, so the bootstrap misses it and falls back to the download, which frequently fails on mainland-China networks (`基础连接已经关闭` / connection reset to python.org). Before relying on that download, look for a bundled interpreter — for example DeepSeek Harness keeps one under `...\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe` — and pass it with `-SystemPython <path>` so the bootstrap builds the virtual environment from it instead of downloading. A host Agent that bundles Office skills (its own `office-docx` with LibreOffice) usually bundles this runtime too.

On Linux or macOS, resolve a working Python 3.10 or newer from the host Agent or the current system, create a task-local virtual environment, and install `requirements.txt` into that environment. Do not install packages into an unrelated global Python.

If no report workspace exists:

```text
"$PYTHON" "$SKILL_DIR/scripts/init_report.py" work/report-name \
  --kind lab \
  --discipline packet-analysis \
  --title "ARP 协议抓包与字段分析"
```

Use `--kind practice` for professional practice. A supplied DOCX remains the report template; do not replace it with the generic Markdown draft.

The command examples in this Skill use POSIX shell syntax. In PowerShell, call the interpreter with `& $PYTHON "$SKILL_DIR\scripts\init_report.py" ...`, continue lines with a backtick instead of `\`, and set `$env:PYTHONIOENCODING = 'utf-8'` so Chinese output is not garbled.

## Read the material

Classify each input before writing:

- **Template:** controls sections, fields, page layout, and visual style.
- **Good reference:** shows useful step length, wording, or screenshot placement.
- **Counterexample:** shows problems to avoid.
- **Task material:** supplies the required data, code, topology, and expected result.
- **Private material:** follows the user's handling instructions and supplies only authorized facts. Read [user-data-and-privacy.md](references/user-data-and-privacy.md).

Learn the pattern, not another person's identity or results. Do not copy names, screenshots, addresses, private records, or first-person claims.

Read [disciplines.md](references/disciplines.md). If a course pack matches, load it; load a second only when the assignment actually crosses subjects. The packs cover common evidence rules, not every course. When no pack matches, or the assignment names software, versions, or concepts the pack does not cover, research them before running anything: prefer the assignment's own manual, the software's official documentation and release notes, and the source repository; check that the instructions match the installed version and architecture. Keep sources in working notes, not in the submitted report, unless the template asks for references.

## Decide what must be delivered

Record:

- required sections and grading prompts;
- fields the user has supplied;
- software, operating system, data, topology, and expected output;
- the visible result needed for each submitted claim;
- length, date, filename, and file-format rules.

Fill names, student numbers, class, teacher, organization, role, dates, and other fields only from values the user supplies or confirms. Use the same value everywhere it appears. Ask once for missing fields that the template requires. Leave signatures, scores, and approval fields empty unless the user explicitly provides them. Do not reuse a filename pattern from an unrelated report; when several reports for the same assignment share a pattern such as `学号+姓名+标题`, follow that shared pattern and ignore download artifacts such as a trailing ` 1`.

When the user asks to add figures or sections to a report they already have, keep their existing text, figures, and fields unchanged, insert new content with the paragraph and image properties already used in that report, and match the existing figures' environment: user and host in the shell prompt, terminal theme, software versions, and node names. If the original environment is unavailable, use the closest one and tell the user exactly which visible values differ.

When the user points to a reference report to match ("按这个来", "截图和 X 的一样"), treat the reference as the figure checklist, not a loose example. For every sub-item, reproduce the same number of figures covering the same subjects in the same order; when the reference shows two figures for a step (for example the modified input and its result), deliver both. Before finishing, walk each sub-item and confirm its figure count and subjects against the reference; a step that silently ends up with fewer figures than the reference is the most common complaint and must be caught here, not by the user.

Before editing Word, read [docx-qa.md](references/docx-qa.md) and complete the workspace's `format-contract.md`. Read requirements from ordinary paragraphs, table cells, headers, footers, text boxes, content controls, comments, and colored instruction text. Record every stated minimum word count, screenshot count, naming rule, field rule, and formatting rule with its source location.

Measure the supplied template: paper size, margins, sections, tables, fonts, sizes, line spacing, indents, image widths, captions, headers, footers, and page numbering. Record the source file hash. Do not begin assembly until the explicit requirements and measured values are in the contract.

## Choose the environment

Read [environment-playbook.md](references/environment-playbook.md), then inspect the current machine:

```text
"$PYTHON" "$SKILL_DIR/scripts/probe_environment.py" --json
```

Do not assume the author's computer or virtualization product. Follow the operating system and software named by the assignment. For common Chinese university coursework, treat Windows as the main route for Office, PowerShell, SQL Server, eNSP, vendor simulators, and Windows-only teaching software. Use Linux or Kali for Linux networking and security tools. Use macOS natively only when the named software and required screenshots remain equivalent; otherwise use any available Windows or Linux VM, container, WSL, or authorized remote lab.

Desktop control is optional. Use the cheapest route that reaches the software: shell commands first, then application scripting or automation inside a guest, then the host Agent's own computer-use tool if it has one. The playbook's [control routes](references/environment-playbook.md#control-the-desktop) describe each route; never ask the user to install a different Agent only to gain computer use.

Keep permission fixes and failed attempts in working notes unless they change the submitted result. Security work must stay inside local labs, course systems, deliberately vulnerable targets, or other authorized systems.

## Run and capture

Read [evidence-and-screenshots.md](references/evidence-and-screenshots.md) and the selected discipline file.

1. Build the smallest setup that satisfies the task.
2. Run every command and code path that will appear in the report.
3. After a meaningful GUI action, inspect the fresh application state.
4. Record the exact inputs, filenames, versions, addresses, frame numbers, and observed values.
5. Capture the screen that shows the result; do not capture every click.
6. Keep original screenshots, packet files, data, and source code unchanged.

Generated diagrams may explain a concept but may not stand in for a real software result. Screenshots used in one report must agree on filenames, addresses, ports, values, and environment.

Check the image folder before drafting:

```text
"$PYTHON" "$SKILL_DIR/scripts/evidence_manifest.py" evidence/original \
  --output evidence-manifest.json
```

Fix corrupt files, accidental duplicates, unreadable captures, exposed private data, and missing result screens.

## Write from the observed result

Read [writing-and-code.md](references/writing-and-code.md).

For each practical step, state the operation, the value or behavior observed, the nearby screenshot, and a short explanation only when it helps. Keep theory and summaries proportional to the examples and the assignment.

For professional practice, write it as assigned work: what was received, what was checked or operated, how the judgment was made, and what result was recorded. Do not add presentation notes about screenshot counts, report structure, retained artifacts, or what the report chooses not to introduce. Do not add a company homepage merely to fill a source line.

For code, implement only the requested behavior. Do not add unused abstractions, speculative options, impossible-case checks, or comments that restate simple code.

## Build and check the DOCX

Use the host agent's document tools when available; otherwise use compatible DOCX tooling and a real renderer. Fill the supplied template in place. Preserve the template paragraph and cell properties while replacing text; rebuilding a cell from plain text may silently remove font hints, line spacing, indents, or pagination settings. Do not reduce a required font size merely to force a long field onto one line. Remove sample text only where the report content replaces it.

Before visual review, compare the finished DOCX with `format-contract.md` and record the measured result for every rule. Count required section lengths from the finished document, not from the draft. Check package structure, sections, margins, table geometry, merged cells, fonts, sizes, line spacing, indents, fields, image count, and source-template hash.

Render the latest DOCX and inspect every page at 100%:

- screenshots and captions are readable and aligned;
- text, tables, and images do not clip or overlap;
- Chinese and Latin glyphs render correctly;
- headings, numbering, spacing, indents, margins, headers, and footers match the template;
- names, dates, commands, addresses, frame numbers, figures, and conclusions agree;
- no extra blank page or nearly empty carried-over page remains;
- the filename follows this assignment's rule;
- no credentials, private workplace data, or unrelated personal information remain.

When the template targets Microsoft Word and Word is available, open the final DOCX in Word and confirm the page count and first/last pages after the renderer check. Repeat both the structural checks and the render after every layout change. Deliver only the requested files unless the user asks for working material.
