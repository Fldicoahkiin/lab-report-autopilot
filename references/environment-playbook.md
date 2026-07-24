# Environment playbook

## Decide from the host, not from the assignment wording

Run `scripts/probe_environment.py --json`, then inventory the named software and any existing virtual machines. Do not install a large toolchain before checking what is already available.

| Requirement | macOS path | Windows path | Blocker rule |
| --- | --- | --- | --- |
| Cross-platform CLI or code | Run natively and record exact versions | Run natively and record exact versions | Stop if the required runtime is absent and installation is not authorized |
| Windows command with a clear macOS equivalent | Use the equivalent only if the learning objective and expected evidence remain valid | Use the named command | Explain the substitution and output differences |
| Windows-only GUI or device simulator | Use an existing Windows VM or authorized remote lab | Use the native app | Never create a substitute screenshot that implies Windows was used |
| Linux security or networking lab | Use an existing local VM/container and an isolated network | Use an existing local VM/container and an isolated network | Do not target public or unapproved systems |
| Vendor-specific network simulator | Use its supported host, VM, or authorized lab | Use the supported Windows build | If the topology cannot run, report the missing environment |

## macOS execution

1. Check native binaries and apps first.
2. Use Computer Use for applications whose visible state is part of the evidence.
3. Prefer native Terminal, Wireshark, Python, compilers, database clients, and browsers when they satisfy the assignment.
4. When native tools do not satisfy it, prefer an existing Parallels guest before installing another virtualization stack.
5. Use Kali in Parallels for Linux networking and security tools. Use a Windows guest for Windows commands, dialogs, and vendor software.
6. Confirm VM network mode before networking experiments. Record NAT, bridged, host-only, and relevant IP addresses.
7. Keep host and guest roles explicit in notes and captions.
8. Use macOS-native alternatives only when they preserve the assignment's learning objective.

For Wireshark capture permission on macOS:

1. Use the official Wireshark ChmodBPF component when it is installed.
2. If the task is authorized for administrator access, repair the capture permission with the official helper or run the bounded capture command with `sudo`.
3. Never save, print, or place an administrator password in notes, commands, screenshots, or the report.
4. After capture works, write only the successful capture step in the report unless permission setup is itself part of the assignment.

When controlling Parallels:

1. Capture the guest name and current power state.
2. Start the existing guest; do not create a new VM unless the task requires it.
3. Inspect the guest desktop before running commands.
4. Keep the Parallels window frame visible in environment evidence when the guest identity matters.
5. Capture application content inside the guest at a readable scale.
6. Shut down or suspend the guest only when the user requested it or the task normally requires it.

When using Computer Use:

1. Fetch the current app state.
2. Derive fresh element indexes from that state.
3. Perform the next bounded action.
4. Fetch the new state before deciding what follows.
5. Save a screenshot only when the state proves a planned claim.

## Windows execution

1. Record the Windows edition, version, architecture, and relevant application versions.
2. Use PowerShell or Command Prompt according to the assignment.
3. Keep command syntax and path separators native to Windows.
4. Capture the title bar, command, and result when the application identity matters.
5. Avoid mixing screenshots from different Windows versions without explaining the reason.

## Environment substitutions

Write an environment note only when a different tool or OS remains visible in the submitted procedure or changes the result. Keep it factual:

> 原实验要求使用 Hydra 对 RDP 进行测试。本机 macOS 版本未提供对应模块，Kali 虚拟机中的旧版 FreeRDP 也无法与目标协商连接，因此改用 Windows 11 靶机和 NetExec 完成同一弱口令验证。后续步骤和结果均以该环境为准。

Include:

- original requirement;
- observed incompatibility or missing component;
- chosen substitute;
- why the substitute still tests the intended concept;
- any output difference the reader will see.

Do not claim the original software succeeded after switching tools. If the native method is repaired and used for the final evidence, omit earlier abandoned routes from the report.
