# Discipline registry

Select a pack from the assignment's main learning objective, not from the software name alone.

| Discipline ID | Use for | Required evidence |
| --- | --- | --- |
| `packet-analysis` | Wireshark, tshark, ARP, ICMP, TCP, DNS, HTTP, PCAP | Capture context, selected frame, decoded fields, interpretation |
| `routing-switching` | VLAN, routing, switching, ACL, NAT, network simulators | Topology, addressing, configuration, verification commands |
| `security-operations` | Alert triage, endpoint review, weak-password remediation, local cyber ranges | Authorized scope, timeline, indicators, decision, local verification |
| `databases` | SQL, schema design, CRUD, joins, views, procedures | Executed statement, result grid, row count, schema state |
| `programming` | C/C++, Python, Java, data structures, algorithms | Exact source, build/run command, input, output, analysis |
| `data-visualization` | Matplotlib, Seaborn, spreadsheet charts, dashboards | Data source, code/settings, rendered chart, interpretation |
| `web-development` | HTML, CSS, JavaScript, responsive pages, browser tools | Source, rendered page, interaction, console/network state |
| `computer-architecture` | CPU, memory, logic circuits, assembly, simulators | Circuit/program state, registers/signals, expected and observed values |

Each pack defines:

- environment routes;
- minimum evidence;
- report-specific analysis;
- common false claims and screenshot mistakes.

Add a new pack only when its experiments require evidence or analysis rules that the existing packs cannot express. Keep the registry ID stable once used by `scripts/init_report.py`.
