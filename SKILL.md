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
- teacher, technical-title, unit, and class fields explicitly supplied by the user;
- target software, operating system, data, topology, and expected output;
- evidence required for each result;
- limits on length, dates, naming, and file format;
- facts that must come from the user or a cited public source.

State competing interpretations when they change the experiment. Ask only when missing information blocks execution or would cause fabricated content. Leave teacher signatures, scores, and approval fields untouched unless explicitly supplied. When the user supplies a teacher or technical title, fill the matching fields consistently in the task sheet and report information table. Keep a supplied or inferred job title short, ordinary, and aligned with the performed work.

Resolve the submission filename before assembly. Follow only the naming rule or example supplied for the current task. Naming varies by course, class, teacher, and submission system, so do not reuse a previous report's formula as a default. If no rule is supplied, use the user's requested name or a concise name based on the current task without treating it as a reusable convention.

## Lock the Word format contract

Before drafting into a supplied DOCX, distill the template and record exact values for:

- paper size, orientation, margins, section breaks, and header/footer distance;
- table rows, columns, merged cells, widths, and signature areas;
- Chinese and Latin fonts, body and heading sizes, weight, alignment, and first-line indent;
- body, heading, code, figure, and caption line spacing and paragraph spacing;
- image width rules, caption position, page numbering, and final filename.

Treat these values as build inputs. If the template requires 1.5 line spacing, set an explicit numeric `1.5` on the relevant paragraphs and verify it in the produced DOCX. Do not reduce the required line spacing to make the report shorter. To remove an orphaned last page, first remove unintended paragraph or figure spacing, then adjust evidence image width while preserving legibility, and only then shorten redundant prose.

## Inspect and choose the environment

Read [environment-playbook.md](references/environment-playbook.md), then run:

```bash
python scripts/probe_environment.py --json
```

On macOS, use native terminals and applications first. When a required tool is unavailable or Windows/Linux-specific, use an existing Parallels virtual machine. Prefer Kali for Linux networking and security tools. Use an existing Windows guest when the assignment requires Windows commands, dialogs, or vendor software.

If the required environment does not exist, stop that portion and report the blocker. Do not generate or restage a screenshot that implies a different operating system was used.

For networking and security work, operate only against local virtual machines, course labs, deliberately vulnerable targets, or systems the user is authorized to test.

Keep environment discovery and troubleshooting in working notes. The finished report normally names only the operating system and tools used in the successful procedure. Include a permission fix, failed attempt, or environment substitution only when it changes the submitted result or the assignment explicitly asks for it.

## Plan and collect evidence

Read [evidence-and-screenshots.md](references/evidence-and-screenshots.md). Map each report claim to:

- the action that produces it;
- the exact visible success or failure signal;
- the application, terminal, host, or virtual machine to capture;
- the intended section and figure caption.

Capture meaningful milestones, not every click. A simple experiment normally needs two to four figures. A professional-practice report can use four to six figures when they cover distinct work stages such as task input, visible result, artifact properties, complete flow, field verification, and disposition. Preserve original screenshots and packet captures. Use generated images only for explanatory diagrams, never as proof that software was run.

After capture, run:

```bash
python scripts/evidence_manifest.py path/to/evidence --output evidence-manifest.json
```

Resolve corrupt images, accidental duplicates, unreadable dimensions, secret exposure, and unexplained gaps before drafting.

## Perform the work

1. Create the smallest setup that satisfies the assignment.
2. Run every submitted command and code path.
3. After each material GUI action, inspect the fresh application state before continuing.
4. Record exact commands, inputs, filenames, versions, IP addresses, observed output, failed attempts, and environment adaptations in working notes.
5. Capture the state that proves the claimed result.
6. Keep security experiments isolated and non-destructive.

If the requested method fails, document the real cause in working notes and try an allowed equivalent. In the report, explain the substitution only when the reader must know it to understand the submitted result. Do not rewrite an unresolved failure as success.

## Draft from evidence

Read [writing-and-code.md](references/writing-and-code.md). For a short course experiment, write each practical step with only the parts that help the reader follow the operation:

1. **Action:** the actual command, code, configuration, or UI operation.
2. **Result:** the exact visible value or behavior.
3. **Evidence:** the screenshot placed near the matching text.
4. **Short explanation:** why the result is correct when it is not already obvious.

Do not add generic sections such as “测试场景与数据边界”“保密边界”“证据链” or a long debugging record unless the template or assignment requires them. Keep the finished report close to the reference reports' step density and wording level.

For `--kind practice`, frame the report as assigned work rather than a longer experiment: task intake, object and known fields, execution, judgment basis, result record, and work-related reflection. Do not narrate how the report is assembled: omit screenshot counts, section-order announcements, artifact inventories written as presentation notes, and statements about what the report will or will not introduce. Mention a retained file only when its operational purpose or handoff status matters. Do not add a decorative company-homepage source.

For packet-based security practice, prefer a non-repeating evidence set:

1. visible service or task result;
2. capture-file properties showing interface, capture filter, packet count, drops, or hash;
3. complete connection sequence;
4. request fields;
5. response fields and timing.

Use fewer figures when one screen already proves two adjacent claims. Never mix screenshots from captures with different addresses, ports, filenames, or environments.

Keep theory proportional to the assignment. Write in a natural student voice grounded in performed work. Do not add deliberate errors or attempt to game detector software.

For code, implement only the requested behavior. Avoid unused abstractions, speculative configuration, defensive branches for impossible inputs, and comments that restate the code.

## Assemble and verify

Read [docx-qa.md](references/docx-qa.md). Use the `documents` skill for DOCX reading, template distillation, editing, rendering, and visual QA.

When a DOCX template is supplied, retain it as the design authority. Fill its intended slots instead of rebuilding it. Remove sample red text and placeholders only where the user's content replaces them.

Render the latest DOCX and inspect every page at 100% zoom. Repeat until:

- screenshots are legible and aligned with their captions;
- no page contains clipping, overlap, broken tables, missing glyphs, or unintended blank space;
- no final page contains only a carried-over sentence, caption, or signature row;
- headings, numbering, fonts, margins, headers, and footers match the template;
- measured line spacing, paragraph spacing, first-line indent, image width, and table geometry match the recorded format contract;
- dates, names, commands, paths, IP addresses, frame numbers, figure numbers, results, and conclusions agree;
- the delivered filename follows the requested submission pattern;
- no credentials, workplace data, or unrelated personal information are exposed.

Deliver only the requested final artifact unless the user asks for source files or QA intermediates.
