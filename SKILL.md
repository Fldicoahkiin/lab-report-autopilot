---
name: lab-report-author
description: Plan, perform, write, and verify evidence-grounded laboratory, experiment, training, coursework, and professional-practice reports. Use when a task involves experiment instructions, reference reports, report templates, DOCX files, simple course code, virtual machines, Windows-only or macOS software, real GUI operation, screenshots, result analysis, conclusions, or final document QA.
---

# Lab Report Author

Produce a report that is traceable to real actions and visible results. Treat screenshots and command output as evidence, not decoration.

## Route the task

1. Classify each input as one of:
   - **Template authority:** controls sections, page geometry, fields, and visual style.
   - **Positive reference:** shows a useful level of detail or evidence pattern.
   - **Counterexample:** reveals omissions, unreadable screenshots, empty steps, copied conclusions, or formatting defects.
   - **Task source:** supplies requirements, data, code, topology, or expected results.
2. Derive patterns from references. Never copy another student's identity, screenshots, environment values, results, or first-person claims.
3. Use the `documents` skill for DOCX reading, editing, rendering, and final visual QA.
4. Use Computer Use for local GUI work when a CLI, API, or dedicated connector cannot produce the required visible evidence.
5. Read the bundled references that match the task:
   - Real software work or an OS mismatch: [environment-playbook.md](references/environment-playbook.md)
   - Any screenshot or result evidence: [evidence-and-screenshots.md](references/evidence-and-screenshots.md)
   - Drafting prose or code: [writing-and-code.md](references/writing-and-code.md)
   - DOCX assembly or delivery: [docx-qa.md](references/docx-qa.md)

## Establish the acceptance contract

Before acting, extract:

- required sections and grading prompts;
- identity fields the user wants filled;
- target software, operating system, data, topology, and output;
- evidence required for each result;
- constraints on length, dates, naming, and file format;
- facts that must come from the user or a cited public source.

State competing interpretations when they change the experiment. Ask only when missing information blocks real execution or would cause fabricated content. Leave teacher signatures, scores, and approval fields untouched unless explicitly supplied.

## Inspect the environment

Run:

```bash
python scripts/probe_environment.py --json
```

Choose the execution path from the actual host and available software. Prefer, in order:

1. the required native application;
2. a behaviorally equivalent native tool when the assignment permits it;
3. an existing virtual machine;
4. an existing remote lab or Windows host authorized by the user.

If a Windows-specific screen or result is required and no usable Windows environment exists, stop that portion and report the blocker. Do not fabricate, generate, restage, or borrow a Windows screenshot.

For networking and security experiments, operate only against course labs, local virtual machines, deliberately vulnerable targets, or systems the user is authorized to test.

## Plan evidence before execution

Create a small evidence plan mapping every report claim to:

- the action that produces it;
- the exact visible success or failure signal;
- the application or terminal to capture;
- the intended report section and figure caption.

Capture meaningful milestones, not every click. Preserve original screenshots. Use generated images only for explanatory diagrams, never as proof that software was run.

After capture, run:

```bash
python scripts/evidence_manifest.py path/to/evidence --output evidence-manifest.json
```

Resolve corrupt images, accidental duplicates, unreadable dimensions, secret exposure, and unexplained gaps before drafting.

## Perform the work

1. Create the smallest setup that satisfies the assignment.
2. Run every submitted command and code path.
3. After each material GUI action, inspect the fresh application state before the next action.
4. Record exact commands, inputs, filenames, versions, IP addresses, observed output, failed attempts, and environment adaptations.
5. Capture the state that proves the claimed result.
6. Keep security experiments isolated and non-destructive.

Do not invent successful output. If the required method fails, document the real cause, try an allowed equivalent, and explain the substitution in the report.

## Draft from evidence

Write each practical step as:

1. **Purpose:** what this step verifies or changes.
2. **Action:** the actual command, code, configuration, or UI operation.
3. **Evidence:** the screenshot or output immediately after the relevant explanation.
4. **Observation:** what is visible, using exact values from the evidence.
5. **Interpretation:** why that result satisfies the task or what remains unresolved.

Keep theory proportional to the assignment. Prefer concrete observations over broad textbook exposition. Write in a natural student voice grounded in the performed work; do not add deliberate errors or attempt to game detector software.

For code, implement only the requested behavior. Avoid unused abstractions, speculative configuration, defensive branches for impossible inputs, and comments that merely restate the code.

## Assemble and verify the document

When a DOCX template is supplied, retain it as the design authority. Fill its real slots instead of rebuilding the document from scratch. Remove sample red text and placeholders only where the user's content replaces them.

Render the latest DOCX to page images and inspect every page at 100% zoom. Repeat until:

- screenshots are legible and aligned with their captions;
- no page contains clipping, overlap, broken tables, missing glyphs, or unintended blank space;
- headings, numbering, fonts, margins, headers, and footers match the template;
- dates, names, commands, paths, IP addresses, figure numbers, results, and conclusions agree;
- no credentials, private work material, or unrelated personal data are exposed.

Deliver only the requested final artifact unless the user asks for source files or QA intermediates.
