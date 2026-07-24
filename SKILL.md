---
name: lab-report-autopilot
description: Automatically plan, perform, document, and verify evidence-grounded laboratory, experiment, training, coursework, and professional-practice reports across computing disciplines. Use when a task involves assignment instructions, reference reports, DOCX templates, simple course code, macOS or Windows tools, Parallels or Kali virtual machines, GUI operation, screenshots, packet capture, networking, cybersecurity, databases, programming, data visualization, web development, computer architecture, result analysis, conclusions, or final document QA.
---

# Lab Report Autopilot

Run the report as an evidence pipeline: understand the assignment, choose a discipline pack, inspect the environment, perform the work, capture proof, write from the proof, and verify the final document.

Automation never authorizes invented output, borrowed screenshots, or false claims about workplace activity. Stop at a real environment or evidence blocker.

## Route the inputs

Classify every input:

- **Template authority:** controls sections, fields, page geometry, and visual style.
- **Positive reference:** shows a useful level of detail or evidence pattern.
- **Counterexample:** reveals empty steps, unreadable screenshots, copied conclusions, or formatting defects.
- **Task source:** supplies requirements, data, topology, code, or expected results.
- **Confidential workplace material:** supplies only a general competency or workflow direction. Read [confidential-work.md](references/confidential-work.md) before using it.

Derive patterns from references. Never copy another person's identity, screenshots, environment values, results, private records, or first-person claims.

## Initialize the task

When no task workspace exists, run:

```bash
python scripts/init_report.py work/report-name \
  --kind lab \
  --discipline packet-analysis \
  --title "ARP 协议抓包与字段分析"
```

Use `--kind practice` for professional practice. The script creates a draft, evidence plan, configuration file, and folders for original evidence, working copies, notes, source code, and output.

If the user supplies a DOCX template, keep it unchanged and use it instead of the generic Markdown draft.

## Load one discipline pack

Read [disciplines.md](references/disciplines.md), then load only the matching pack:

- Packet capture and protocol analysis: [discipline-packet-analysis.md](references/discipline-packet-analysis.md)
- Routing and switching: [discipline-routing-switching.md](references/discipline-routing-switching.md)
- Security operations and local cyber ranges: [discipline-security-operations.md](references/discipline-security-operations.md)
- SQL and databases: [discipline-databases.md](references/discipline-databases.md)
- Programming and data structures: [discipline-programming.md](references/discipline-programming.md)
- Data visualization: [discipline-data-visualization.md](references/discipline-data-visualization.md)
- Web development: [discipline-web-development.md](references/discipline-web-development.md)
- Computer architecture and simulators: [discipline-computer-architecture.md](references/discipline-computer-architecture.md)

Load at most two packs unless the assignment genuinely crosses disciplines.

## Establish the acceptance contract

Extract:

- required sections and grading prompts;
- identity fields the user wants filled;
- target software, operating system, data, topology, and expected output;
- evidence required for each result;
- limits on length, dates, naming, and file format;
- facts that must come from the user or a cited public source.

State competing interpretations when they change the experiment. Ask only when missing information blocks execution or would cause fabricated content. Leave teacher signatures, scores, and approval fields untouched unless explicitly supplied.

## Inspect and choose the environment

Read [environment-playbook.md](references/environment-playbook.md), then run:

```bash
python scripts/probe_environment.py --json
```

On macOS, use native terminals and applications first. When a required tool is unavailable or Windows/Linux-specific, use an existing Parallels virtual machine. Prefer Kali for Linux networking and security tools. Use an existing Windows guest when the assignment requires Windows commands, dialogs, or vendor software.

If the required environment does not exist, stop that portion and report the blocker. Do not generate or restage a screenshot that implies a different operating system was used.

For networking and security work, operate only against local virtual machines, course labs, deliberately vulnerable targets, or systems the user is authorized to test.

## Plan and collect evidence

Read [evidence-and-screenshots.md](references/evidence-and-screenshots.md). Map each report claim to:

- the action that produces it;
- the exact visible success or failure signal;
- the application, terminal, host, or virtual machine to capture;
- the intended section and figure caption.

Capture meaningful milestones, not every click. Preserve original screenshots and packet captures. Use generated images only for explanatory diagrams, never as proof that software was run.

After capture, run:

```bash
python scripts/evidence_manifest.py path/to/evidence --output evidence-manifest.json
```

Resolve corrupt images, accidental duplicates, unreadable dimensions, secret exposure, and unexplained gaps before drafting.

## Perform the work

1. Create the smallest setup that satisfies the assignment.
2. Run every submitted command and code path.
3. After each material GUI action, inspect the fresh application state before continuing.
4. Record exact commands, inputs, filenames, versions, IP addresses, observed output, failed attempts, and environment adaptations.
5. Capture the state that proves the claimed result.
6. Keep security experiments isolated and non-destructive.

If the requested method fails, document the real cause, try an allowed equivalent, and explain the substitution. Do not rewrite failure as success.

## Draft from evidence

Read [writing-and-code.md](references/writing-and-code.md). Write each practical step as:

1. **Purpose:** what the step verifies or changes.
2. **Action:** the actual command, code, configuration, or UI operation.
3. **Evidence:** the screenshot or output after the relevant explanation.
4. **Observation:** exact values visible in the evidence.
5. **Interpretation:** why the result satisfies the task or what remains unresolved.

Keep theory proportional to the assignment. Write in a natural student voice grounded in performed work. Do not add deliberate errors or attempt to game detector software.

For code, implement only the requested behavior. Avoid unused abstractions, speculative configuration, defensive branches for impossible inputs, and comments that restate the code.

## Assemble and verify

Read [docx-qa.md](references/docx-qa.md). Use the `documents` skill for DOCX reading, template distillation, editing, rendering, and visual QA.

When a DOCX template is supplied, retain it as the design authority. Fill its intended slots instead of rebuilding it. Remove sample red text and placeholders only where the user's content replaces them.

Render the latest DOCX and inspect every page at 100% zoom. Repeat until:

- screenshots are legible and aligned with their captions;
- no page contains clipping, overlap, broken tables, missing glyphs, or unintended blank space;
- headings, numbering, fonts, margins, headers, and footers match the template;
- dates, names, commands, paths, IP addresses, frame numbers, figure numbers, results, and conclusions agree;
- no credentials, workplace data, or unrelated personal information are exposed.

Deliver only the requested final artifact unless the user asks for source files or QA intermediates.
