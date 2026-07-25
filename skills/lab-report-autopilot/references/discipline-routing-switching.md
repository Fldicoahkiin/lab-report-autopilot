# Routing and switching

## Environment route

- Use the required simulator when available.
- Prefer native Windows for eNSP and other Windows-only vendor simulators. On another host, use any available Windows VM or authorized course lab.
- Run Packet Tracer or command-line network tools on the current host only when the assignment accepts that build and interface.
- Record simulator version, device models, interface names, topology file, and addressing plan.

## Build the experiment

1. Draw the topology before configuration.
2. Create an addressing table with device, interface, IP/prefix, gateway, VLAN, and role.
3. Configure one feature group at a time.
4. Save device configuration after each verified stage.
5. Run verification commands before connectivity tests.

Useful verification categories:

- interface state and addressing;
- VLAN membership and trunk state;
- MAC address table;
- routing table and next hop;
- ACL/NAT match counters;
- end-to-end `ping` and bounded route tracing.

## Minimum evidence

- Complete topology with readable device names and links.
- Addressing/VLAN table.
- Relevant configuration lines.
- Verification command output.
- At least one success path and one isolation or policy result when required.

## Result analysis

Explain why traffic succeeds or fails using the control state:

- name the source and destination;
- state the ingress VLAN or subnet;
- identify the gateway or route;
- identify the policy that permits or blocks the packet;
- match the explanation to the displayed table or counter.

Do not use a topology screenshot alone as proof of connectivity. Do not paste an entire device configuration when only five lines support the result.
