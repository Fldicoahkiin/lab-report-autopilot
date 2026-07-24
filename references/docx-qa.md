# DOCX assembly and QA

## Preserve the template

When a supplied DOCX controls the output:

1. keep the source file unchanged;
2. use the `documents` skill's template distillation workflow;
3. identify body, table, header, footer, text-box, and content-control slots;
4. preserve unknown package parts and teacher-owned fields;
5. replace only the intended student content and sample placeholders;
6. retain page size, margins, styles, numbering, headers, footers, and signature areas.

Do not rebuild a school form from a generic report design.

## Insert content

- Keep heading levels and numbering consistent with the template.
- Use editable text for code and commands when the template allows it.
- Use a monospace font and restrained shading for code only if that treatment already fits the template.
- Center screenshots and preserve aspect ratio.
- Size terminal and UI screenshots so their text is readable at 100% page zoom.
- Keep a caption with its figure.
- Avoid fixed-height rows for screenshots or long prose.
- Prevent a heading from being stranded at the bottom of a page.
- Remove example red text, placeholder dates, and instructional notes only when the matching student content is ready.
- Leave signatures, teacher comments, and scores blank unless explicitly provided.

## Render and inspect

Use the `documents` skill renderer after every layout-sensitive edit. Inspect every page at 100% zoom.

Check:

- expected page count and section order;
- no missing glyphs, clipping, overlap, or broken tables;
- no unintended blank pages or large empty gaps;
- screenshot text remains readable;
- figure captions and references match;
- headers, footers, page numbers, margins, and signature blocks remain intact;
- no source-template text survives in student sections;
- the latest rendered pages match the latest DOCX.

If fonts render as boxes or substitute poorly, install or select an available compatible font before delivery. Do not treat unreadable Chinese text as a passing render.

## Content audit

- Every requested item has a filled response.
- Every success claim maps to real evidence.
- Results in prose match screenshots and command output.
- Environment adaptations are stated once and remain consistent.
- The summary length fits the report's scale.
- No other student's name, ID, screenshot, or first-person claim remains.
- No credentials, private company data, internal chat, or unrelated personal information appears.
- The file properties and document metadata do not expose unintended authors.

## Delivery

Return only the requested final DOCX unless the user asks for evidence files, source code, manifests, or rendered pages. Keep QA renders and intermediate copies outside the deliverable folder.
