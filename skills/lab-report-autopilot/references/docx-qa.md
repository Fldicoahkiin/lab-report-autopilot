# DOCX assembly and QA

## Preserve the template

When a supplied DOCX controls the output:

1. keep the source file unchanged;
2. record its path, SHA-256, intended opening application, and visible page count;
3. use the host Agent's DOCX tools when it has them; otherwise edit a copy with a library that preserves unknown package parts, such as `python-docx` or direct XML edits;
4. identify body, table, header, footer, text-box, content-control, comment, and drawing-text slots;
5. copy every explicit instruction into `format-contract.md`, including requirements written in red or placed inside a table;
6. preserve unknown package parts and teacher-owned fields;
7. replace only the intended student content and sample placeholders;
8. retain page size, margins, styles, numbering, headers, footers, and signature areas.

Do not rebuild a school form from a generic report design.

## Finish the requirement ledger first

For each requirement, record its template location, expected value, how the final value will be measured, and pass/fail result. Treat these as measurable rules, not writing suggestions.

Include:

- minimum or maximum word counts for each named section;
- required headings, numbering levels, and section order;
- font family, font size, weight, line spacing, paragraph spacing, indent, and alignment by role;
- figure and table placement, caption position, screenshot count, and filename;
- fields that must be filled, fields that must remain blank, and values that repeat;
- page size, margins, section starts, page-number behavior, and signature areas;
- example text or instruction text that must be removed.

If two parts of the template conflict, show the conflict to the user before writing. Do not silently choose the easier rule.

## Insert content

- Write a task-local format contract before assembly. Record paper geometry, section breaks, table layout, Chinese and Latin fonts, exact font sizes, line spacing, paragraph spacing, first-line indent, image widths, caption spacing, page-number fields, signature areas, and final filename.
- Keep heading levels and numbering consistent with the template.
- Use editable text for code and commands when the template allows it.
- Use a monospace font and restrained shading for code only if that treatment already fits the template.
- Center screenshots and preserve aspect ratio.
- Size terminal and UI screenshots so their text is readable at 100% page zoom.
- Keep a caption with its figure.
- Avoid fixed-height rows for screenshots or long prose.
- Prevent a heading from being stranded at the bottom of a page.
- Remove example red text, placeholder dates, and instructional notes only when the matching student content is ready.
- If the user supplies the teacher and technical title, fill both the task sheet and report information table with the same values. Signature, score, and approval fields stay blank.
- When replacing text in an existing paragraph or table cell, preserve its paragraph properties and only replace the intended runs. Assigning plain `cell.text` may remove line spacing, character-grid settings, font hints, and other template behavior.
- Keep the template's stated font size for filled fields. If a value wraps, first confirm that the original column widths, cell margins, paragraph properties, and font mappings were preserved. Do not hide the problem by shrinking the text.
- Keep the source template hash unchanged. Build from a working copy and place the finished file at a different path.

## Enforce paragraph and figure geometry

- Apply template line spacing as an explicit numeric value. For a template requiring 1.5 line spacing, set `1.5` on body paragraphs and headings covered by that rule.
- Do not use inherited or renderer-dependent defaults for line spacing, first-line indent, paragraph spacing, or figure width.
- Keep required line spacing when reducing page count.
- Remove unintended space before and after figures and captions before shrinking a screenshot.
- If an orphaned signature page remains, reduce only the width of unusually tall screenshots while keeping their text readable.
- Keep a caption directly after its image and prevent a heading from being stranded at the bottom of a page.

## Render and inspect

Render with the host Agent's document renderer or LibreOffice (`soffice --headless --convert-to pdf`) after every layout-sensitive edit, and inspect every page at 100% zoom.

Page count and pagination come from the application the template targets. LibreOffice and Microsoft Word can differ by several pages on the same file because they snap line spacing to the document grid differently. When Word is available, read the page count from Word and export a PDF from Word for the final inspection.

A filled field that wraps to an extra line can push a template's spacer paragraphs onto the next page and leave it blank. Remove only those empty spacer paragraphs, keep any page break they carried, record the change in the contract, and re-check in the target application.

Check:

- expected page count and section order;
- no missing glyphs, clipping, overlap, or broken tables;
- no unintended blank pages or large empty gaps;
- no page containing only a signature row, one carried-over line, or one detached caption;
- screenshot text remains readable;
- figure captions and references match;
- headers, footers, page numbers, margins, and signature blocks remain intact;
- no source-template text survives in student sections;
- the latest rendered pages match the latest DOCX.

Inspect the DOCX structure as well as the render:

- section count and A4/Letter geometry match the template;
- table row/column counts, grid widths, cell margins, and merged-cell patterns match the template;
- body line spacing and first-line indent equal the format contract;
- image count, dimensions, and captions match the evidence plan;
- page-number fields, headers, footers, and signature blocks remain present;
- the delivered filename matches the naming rule for the current task, without reusing an unsupported convention from another report.

If a long body row must be split to prevent Word from moving it to a later page, record the change in the contract, keep the visible border continuous, and verify that no unrelated table geometry changed. Any structural difference needs a stated pagination reason and a visual check.

Generic style linters may report direct formatting or Normal-style headings because the source school form itself uses them. Compare warnings with the source template; do not normalize the document into a different design.

If fonts render as boxes or substitute poorly, install or select an available compatible font before delivery. Do not treat unreadable Chinese text as a passing render.

## Content audit

- Every requested item has a filled response.
- Every row in `format-contract.md` has a measured value and pass/fail result.
- Required section lengths are counted from the finished DOCX after captions, placeholders, and headings are excluded according to the template's rule.
- Every success claim maps to real evidence.
- Results in prose match screenshots and command output.
- Environment adaptations are stated once and remain consistent.
- The summary length fits the report's scale.
- No other student's name, ID, screenshot, or first-person claim remains.
- No credentials, private company data, internal chat, or unrelated personal information appears.
- The file properties and document metadata do not expose unintended authors.

## Delivery

Return only the requested final DOCX unless the user asks for evidence files, source code, manifests, or rendered pages. Keep QA renders and intermediate copies outside the deliverable folder.
