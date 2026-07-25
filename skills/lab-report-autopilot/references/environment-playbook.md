# Environment playbook

## Select from the assignment first

Run:

```bash
python3 "$SKILL_DIR/scripts/probe_environment.py" --json
```

Then inspect the software named by the assignment and any existing virtual machines, containers, WSL distributions, or authorized remote labs. Do not assume the author's operating system or virtualization product.

Choose in this order:

1. Use the operating system and application explicitly required by the assignment.
2. For common Chinese university software with a Windows-native workflow, prefer Windows.
3. For Linux networking and security tools, prefer Linux, Kali, WSL, or an isolated Linux VM.
4. For cross-platform code, databases, browsers, and packet tools, use the current host when the interface and submitted result remain equivalent.
5. Use macOS natively only when it satisfies the same task. It is a supported route, not the default.

| Requirement | Windows route | Linux route | macOS route |
| --- | --- | --- | --- |
| Office and DOCX templates | Microsoft Word and the supplied template | LibreOffice only when layout remains exact | Microsoft Word or Pages only after render comparison |
| PowerShell, CMD, registry, Event Viewer, Defender | Run natively | Use a Windows VM or authorized remote lab | Use a Windows VM or authorized remote lab |
| SQL Server, SSMS, Access | Run natively | Use a Windows VM or an accepted database substitute | Use a Windows VM or an accepted database substitute |
| eNSP or Windows-only teaching software | Run the supported Windows build | Use a Windows VM or course lab | Use a Windows VM or course lab |
| Wireshark and common code toolchains | Run natively | Run natively | Run natively when the assignment accepts it |
| Kali or Linux security tools | Use WSL, a Linux VM, or isolated lab | Run natively | Use a Linux VM, container, or isolated lab |

If the required environment does not exist and installation is not authorized, stop only that part and state what is missing. Do not create a screenshot that implies another operating system or application was used.

## Windows execution

1. Record the Windows edition, version, architecture, and relevant application versions.
2. Use PowerShell or Command Prompt according to the assignment.
3. Keep drive letters, path separators, commands, and window chrome native to Windows.
4. Prefer the named classroom application over a substitute with a different interface.
5. Capture the application title, command or configuration, target, and result when they are needed to understand the step.
6. Avoid mixing screenshots from different Windows versions or virtual machines without explaining the change.

Common routes include native Windows, Hyper-V, VMware Workstation, VirtualBox, a Windows guest on another host, and an authorized remote classroom machine. Use what already exists before installing another platform.

## Linux and Kali execution

1. Use native Linux, WSL, a VM, or a container according to the tool and screenshot requirement.
2. Keep vulnerable services and security exercises on an isolated or course-authorized network.
3. Record distribution, release, interface, network mode, addresses, and tool versions.
4. Use a desktop VM when the report must show a Linux GUI; use a terminal environment when only commands and output matter.

## macOS execution

1. Use native Terminal, Wireshark, Python, compilers, database clients, browsers, and Microsoft Word only when they satisfy the assignment.
2. If the required software or visible interface is Windows- or Linux-specific, use any available compatible VM, container, or remote lab.
3. Confirm VM network mode before networking experiments. Record NAT, bridged, host-only, and relevant addresses.
4. Use macOS alternatives only when they preserve the required operation and submitted evidence.

For Wireshark capture permission, use the official ChmodBPF component or an authorized bounded capture command. Never save, print, or place an administrator password in notes, commands, screenshots, or the report.

## GUI automation and virtual machines

When the host agent can control desktop applications:

1. Inspect the current application state.
2. Perform one bounded action.
3. Inspect the new state before deciding what follows.
4. Save a screenshot only when it shows a planned result.

For any VM platform:

1. Record the guest name, operating system, and power state.
2. Start an existing guest before considering a new VM.
3. Inspect the guest desktop before running commands.
4. Keep the VM frame visible only when guest identity matters.
5. Capture application content at a readable scale.
6. Do not shut down or suspend a guest unless the user asks or the task normally requires it.

## Environment substitutions

Mention a substitution in the report only when it remains visible or changes the result. State the required environment, the observed incompatibility, the replacement, and why the replacement still tests the requested concept.

Do not claim the original software succeeded after switching tools. If the named method is repaired and used for the final result, omit abandoned attempts from the report.
