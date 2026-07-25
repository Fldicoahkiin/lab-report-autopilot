---
name: lab-report-autopilot
description: Run and document computing lab, training, coursework, and professional-practice assignments from supplied instructions, reference reports, and DOCX templates. Use when Codex must inspect macOS, Windows, Kali, or Parallels; operate terminals or GUI tools; capture actual screenshots or packet files; write simple course code; analyze results; and return a checked report for networking, cybersecurity, databases, programming, data visualization, web development, or computer architecture.
---

# Lab Report Autopilot

Complete reports from actual work: read the assignment, run the experiment, keep the useful results, write into the supplied template, and inspect the finished DOCX.

Never invent software output, screenshots, workplace activity, citations, or environment details. Stop when a missing environment or missing fact would force fabrication.

## Set up

Resolve the directory containing this `SKILL.md` as `SKILL_DIR`. Run bundled scripts by absolute path; the current directory may be the user's report folder rather than the skill folder.

If no report workspace exists:

```bash
python3 "$SKILL_DIR/scripts/init_report.py" work/report-name \
  --kind lab \
  --discipline packet-analysis \
  --title "ARP 协议抓包与字段分析"
```

Use `--kind practice` for professional practice. A supplied DOCX remains the report template; do not replace it with the generic Markdown draft.

The image checker needs Pillow:

```bash
python3 -m pip install -r "$SKILL_DIR/requirements.txt"
```

## Read the material

Classify each input before writing:

- **Template:** controls sections, fields, page layout, and visual style.
- **Good reference:** shows useful step length, wording, or screenshot placement.
- **Counterexample:** shows problems to avoid.
- **Task material:** supplies the required data, code, topology, and expected result.
- **Confidential material:** supplies only a general work direction. Read [confidential-work.md](references/confidential-work.md).

Learn the pattern, not another person's identity or results. Do not copy names, screenshots, addresses, private records, or first-person claims.

Read [disciplines.md](references/disciplines.md), then load the one matching discipline file. Load a second only when the assignment actually crosses subjects.

## Decide what must be delivered

Record:

- required sections and grading prompts;
- fields the user has supplied;
- software, operating system, data, topology, and expected output;
- the visible result needed for each submitted claim;
- length, date, filename, and file-format rules.

Ask only when a missing answer blocks the work or would make the report false. Leave signatures, scores, and approval fields empty unless the user explicitly provides them. Do not reuse a filename pattern from an unrelated report.

Before editing Word, read [docx-qa.md](references/docx-qa.md) and measure the supplied template: paper size, margins, tables, fonts, sizes, line spacing, indents, image widths, captions, headers, footers, and page numbering. These measured values control the output.

## Choose the environment

Read [environment-playbook.md](references/environment-playbook.md), then inspect the current machine:

```bash
python3 "$SKILL_DIR/scripts/probe_environment.py" --json
```

On macOS, use installed native tools first. Use an existing Parallels guest when the assignment needs Windows or Linux. Prefer Kali for Linux networking and security work; use Windows when the required interface or vendor software is Windows-only.

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

```bash
python3 "$SKILL_DIR/scripts/evidence_manifest.py" path/to/evidence \
  --output evidence-manifest.json
```

Fix corrupt files, accidental duplicates, unreadable captures, exposed private data, and missing result screens.

## Write from the observed result

Read [writing-and-code.md](references/writing-and-code.md).

For each practical step, state the operation, the value or behavior observed, the nearby screenshot, and a short explanation only when it helps. Keep theory and summaries proportional to the examples and the assignment.

For professional practice, write it as assigned work: what was received, what was checked or operated, how the judgment was made, and what result was recorded. Do not add presentation notes about screenshot counts, report structure, retained artifacts, or what the report chooses not to introduce. Do not add a company homepage merely to fill a source line.

For code, implement only the requested behavior. Do not add unused abstractions, speculative options, impossible-case checks, or comments that restate simple code.

## Build and check the DOCX

Use the `documents` skill for DOCX reading, editing, rendering, and page inspection. Fill the supplied template in place. Remove sample text only where the report content replaces it.

Render the latest DOCX and inspect every page at 100%:

- screenshots and captions are readable and aligned;
- text, tables, and images do not clip or overlap;
- Chinese and Latin glyphs render correctly;
- headings, numbering, spacing, indents, margins, headers, and footers match the template;
- names, dates, commands, addresses, frame numbers, figures, and conclusions agree;
- no extra blank page or nearly empty carried-over page remains;
- the filename follows this assignment's rule;
- no credentials, private workplace data, or unrelated personal information remain.

Repeat the render after every layout change. Deliver only the requested files unless the user asks for working material.
