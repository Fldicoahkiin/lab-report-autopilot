# Writing and code

## Write from observed work

Use concrete subjects, actions, and values:

- name the tool, module, file, table, interface, host, or command;
- quote short output values that are visible in the evidence;
- distinguish what was configured, what was observed, and what was inferred;
- use first person sparingly for choices, failures, and lessons actually experienced;
- keep terminology at the course's level.

Avoid prose that sounds detached from the experiment:

- long background sections copied from a textbook;
- repeated openings such as “通过本次实验，我深刻认识到”;
- claims that every objective was mastered without evidence;
- inflated phrases about laying a foundation for future development;
- the assignment text repeated as the conclusion;
- generic transition phrases at the start of every paragraph.

Do not introduce spelling mistakes or awkward wording to imitate a person. Naturalness comes from specific evidence, real constraints, and proportional reflection.

## Shape each section

### Purpose and requirements

Condense the task into two to five measurable objectives. Preserve mandatory wording only when the template requires it.

### Environment

Record only details that affect reproducibility:

- host and guest operating systems;
- application or runtime versions;
- network mode and role assignment;
- input data, topology, or dataset;
- environment substitutions.

### Process and result analysis

For each task unit:

1. state the immediate purpose;
2. show the minimal command, code, or configuration;
3. place the real screenshot;
4. identify the exact visible result;
5. explain why it is correct or what failed.

Mention a failed attempt when it caused a meaningful change in method. Do not invent troubleshooting to make the report look detailed.

### Summary or reflection

Use these ranges as defaults, then follow explicit template limits:

- single short experiment: 120-220 Chinese characters;
- multi-part experiment or project: 200-350 Chinese characters;
- professional practice report: 350-600 Chinese characters.

Cover:

- the result that was actually completed;
- one or two skills demonstrated;
- one real issue, adaptation, or limitation;
- one specific improvement or follow-up.

Do not repeat every step. Do not turn the summary into a second theory section.

## Keep course code small

- Implement only the requested input, processing, and output.
- Use direct functions and data structures appropriate to the course.
- Do not add configuration systems, class hierarchies, plugin patterns, retries, logging frameworks, or validation for impossible inputs.
- Avoid unused imports and unused variables.
- Add a comment only for a non-obvious algorithmic choice or domain constraint.
- Keep sample data small and tied to the assignment.
- Run the exact code that appears in the report.
- Capture the source and output at readable scale.

For a basic assignment, prefer:

```python
scores = [82, 91, 76]
average = sum(scores) / len(scores)
print(f"平均成绩：{average:.2f}")
```

Do not wrap this in classes, command parsers, configuration files, or broad exception handling unless the task asks for them.

## Check consistency

Before assembly, compare prose, code, and evidence for:

- filenames and paths;
- input values and output values;
- application and OS names;
- IP addresses, ports, VLAN IDs, and host roles;
- figure order;
- dates and versions;
- claimed success, failure, and substitutions.
