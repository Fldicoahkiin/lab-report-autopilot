# Discipline registry

Select a pack from the assignment's main learning objective, not from the software name alone. The packs record evidence rules that recur across many courses; they are a starting point, not the list of supported subjects.

| Discipline ID | Use for | Required evidence |
| --- | --- | --- |
| [`packet-analysis`](discipline-packet-analysis.md) | Wireshark, tshark, ARP, ICMP, TCP, DNS, HTTP, PCAP | Capture context, selected frame, decoded fields, interpretation |
| [`routing-switching`](discipline-routing-switching.md) | VLAN, routing, switching, ACL, NAT, network simulators | Topology, addressing, configuration, verification commands |
| [`security-operations`](discipline-security-operations.md) | Alert triage, endpoint review, weak-password remediation, local cyber ranges | Authorized scope, timeline, indicators, decision, local verification |
| [`databases`](discipline-databases.md) | SQL, schema design, CRUD, joins, views, procedures | Executed statement, result grid, row count, schema state |
| [`programming`](discipline-programming.md) | C/C++, Python, Java, data structures, algorithms | Exact source, build/run command, input, output, analysis |
| [`data-visualization`](discipline-data-visualization.md) | Matplotlib, Seaborn, spreadsheet charts, dashboards | Data source, code/settings, rendered chart, interpretation |
| [`web-development`](discipline-web-development.md) | HTML, CSS, JavaScript, responsive pages, browser tools | Source, rendered page, interaction, console/network state |
| [`computer-architecture`](discipline-computer-architecture.md) | CPU, memory, logic circuits, assembly, simulators | Circuit/program state, registers/signals, expected and observed values |

Each pack defines:

- environment routes;
- minimum evidence;
- report-specific analysis;
- common false claims and screenshot mistakes.

## Subjects without a pack

SDN, operating systems, Linux administration, cloud and containers, software testing, embedded systems, machine learning, and many other courses have no pack. Handle them the same way:

1. Read the assignment manual and any reference reports for the expected steps and figures.
2. Look up the named software in its official documentation, release notes, and source repository. Search the web when the manual is missing or outdated.
3. Confirm that the instructions fit the installed version, operating system, and CPU architecture before following them. Course manuals are often written for an older release or for x86.
4. Derive the evidence list from the assignment: for each required item, decide which command output, configuration screen, or result window proves it.
5. When a step fails, read the error and the upstream issue tracker or changelog before retrying. Prefer the upstream fix over an ad-hoc workaround, and state it in the report only when it changes the submitted result.

Pass the course name to `init_report.py --discipline` as free text when no ID fits; the text appears in the draft.

Add a new pack only when its experiments require evidence or analysis rules that the existing packs cannot express. Keep existing IDs stable.
