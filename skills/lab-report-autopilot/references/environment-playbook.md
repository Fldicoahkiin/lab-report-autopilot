# Environment playbook

## Select from the assignment first

Resolve the helper runtime before probing the course environment, as the Skill's [Set up](../SKILL.md#set-up) section describes; on Windows, see also [Windows helper runtime](#windows-helper-runtime).

Run:

```text
"$PYTHON" "$SKILL_DIR/scripts/probe_environment.py" --json
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

1. Establish the isolated helper runtime before running any bundled Python script.
2. Record the Windows edition, version, architecture, and relevant application versions.
3. Use PowerShell or Command Prompt according to the assignment.
4. Keep drive letters, path separators, commands, and window chrome native to Windows.
5. Prefer the named classroom application over a substitute with a different interface.
6. Capture the application title, command or configuration, target, and result when they are needed to understand the step.
7. Avoid mixing screenshots from different Windows versions or virtual machines without explaining the change.

Common routes include native Windows, Hyper-V, VMware Workstation, VirtualBox, a Windows guest on another host, and an authorized remote classroom machine. Use what already exists before installing another platform.

The helper Python exists to run this Skill's setup and image checks. Do not describe it in the submitted report unless Python itself is part of the experiment. Course software, compilers, database clients, Office, packet tools, and simulators still need their own availability checks.

<a id="windows-helper-runtime"></a>
### Windows helper runtime

Do not assume that `python`, `python3`, `py`, or `pip` is usable merely because the command exists. `bootstrap_windows.ps1` runs each candidate to check it, creates a virtual environment under `<workspace>\.lab-report-runtime`, and installs only this Skill's requirements. It needs no elevation and does not change PATH, file associations, shortcuts, or global packages. The runtime JSON goes to stdout and to `runtime.json` in that folder, which is UTF-8. Failed downloads and failed venv attempts that it recovered from are logged to `bootstrap.log` there. A failure prints its reason to stderr and exits with a nonzero code; read that log as well.

The bootstrap takes the first of:

1. a virtual environment already in the workspace that has `pip`; a broken one is rebuilt from the interpreter found below;
2. the interpreter passed with `-SystemPython`; if it is not a working Python 3.10 or newer, or cannot create a virtual environment, the script stops instead of downloading, and running it again without the flag continues with the steps below;
3. `py -3`, `python`, or `python3` on PATH; if the first one that works cannot create a virtual environment, the reason goes to `bootstrap.log` and the search moves on to step 4;
4. a Python 3.12 that the python.org installer already installed for this Windows user; if it does not start, the script stops and suggests running again, a repair, or `-SystemPython`, because the installer would modify that install instead of adding another;
5. a CPython 3.12 downloaded from npmmirror, then Huawei Cloud, then python.org, each file matching the pinned SHA-256, and installed once for this Windows user under `%LOCALAPPDATA%\lab-report-autopilot`; later report workspaces reuse it, and it can be removed in Settings > Apps.

A first run that downloads and installs Python can take several minutes; give the command a timeout of 10 minutes when the host allows it. A run that was cut off can be repeated; if the Python installer it started is still running, wait for it to finish first.

Host Agents often ship Python without putting it on PATH. Before running the bootstrap, use the host's own report of its runtime when it has one, such as DeepSeek Harness's `load_workspace_dependencies` tool; otherwise search the host's install and runtime folders for `python.exe`, for example DeepSeek Harness's `...\dsh-runtimes\dsh-primary-runtime\dependencies\python\python.exe`. When that Python can `import PIL`, as DeepSeek Harness's can, use it as `$PYTHON` and skip the bootstrap; otherwise pass it with `-SystemPython`.

python.org often resets or crawls on mainland-China networks (`基础连接已经关闭`), so the bootstrap tries the mirrors first; a host runtime avoids the download altogether. `pip` reads `PIP_INDEX_URL` from the environment; when PyPI is unreachable, set it to a mirror the user accepts, such as `https://pypi.tuna.tsinghua.edu.cn/simple`, and run the bootstrap again. PyPI packages are not hash-pinned, so the bootstrap does not choose an index itself.

### Linux guests in VMware Workstation

Students often keep VMware on a second drive. A `VMware VIX` folder under Program Files does not mean Workstation is there. Find it from the registry value `InstallPath` under `HKLM\SOFTWARE\WOW6432Node\VMware, Inc.\VMware Workstation`, then use `vmrun.exe` from that folder. Find guests by searching for `*.vmx` files.

`vmrun` can drive a guest without desktop control once VMware Tools is running and the user has given the guest account:

1. `vmrun -T ws start <vmx> gui` starts the guest with its window; poll `checkToolsState` until it reports `running`.
2. Guest operations take `-gu <user> -gp <password>`. On "Invalid user name or password", ask the user for the exact account name as well as the password; a prompt such as `txs@ubuntu` names the account of older screenshots, not necessarily of this VM.
3. `runScriptInGuest` does not return the script's output. Make the script write to a log file in the guest and fetch it with `CopyFileFromGuestToHost`; fetch screenshots the same way.
4. Write guest scripts to `.sh` files with LF line endings and copy them in with `CopyFileFromHostToGuest`. Inline Bash inside a PowerShell double-quoted string loses `$()` and `$VAR` to PowerShell expansion.
5. Run GUI commands as the logged-in desktop user with `DISPLAY=:0` and the user's D-Bus address; see [capture techniques](evidence-and-screenshots.md#capture-techniques).

PowerShell output from native tools can arrive in the wrong encoding: set `$env:PYTHONIOENCODING = 'utf-8'` before Python helpers and `[Console]::OutputEncoding = [Text.Encoding]::UTF8` for UTF-8 tools; `wsl.exe` writes UTF-16LE.

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

### Apple Silicon

Apple Silicon Macs run ARM64 guests at native speed and x86 guests only through slow emulation. Plan the guest around that:

| Need | Route |
| --- | --- |
| Linux course work (Mininet, OVS, Kali tools, compilers, servers) | ARM64 Linux guest in UTM or Parallels |
| Windows course work (Office, PowerShell, SQL Server) | Windows 11 ARM guest; it runs most x86 apps through built-in translation |
| x86-only kernel drivers or simulators (eNSP, some vendor tools) | Course lab machine, remote Windows, or an x86 PC; emulation is a last resort |

UTM is free, uses QEMU, and can be scripted: AppleScript creates and reconfigures VMs, and `/Applications/UTM.app/Contents/MacOS/utmctl` starts, stops, and lists them. Parallels Desktop is heavier and paid, but integrates guest tools and offers `prlctl`. Use whichever already exists before installing another.

ARM64 Linux details that course manuals usually miss:

- Ubuntu ARM64 packages live under `ubuntu-ports`. A mirror line such as `http://mirrors.tuna.tsinghua.edu.cn/ubuntu-ports/` works; the x86 path `.../ubuntu/` does not.
- Ubuntu 20.04 ships only a server ISO for ARM64. Install `ubuntu-desktop-minimal` afterwards when the report needs a GUI.
- Prebuilt x86 binaries and offline install scripts from the course may not run. Prefer the distribution package or the upstream source build.

When the guest is created without manual clicks:

- Ubuntu autoinstall reads a `cidata` seed disk, but asks for confirmation unless the kernel command line contains `autoinstall`; add it to the ISO's `grub.cfg` with `xorriso` and set a short timeout.
- During installation only the ISO's package pool is reachable. Listing a package that is not on the ISO, such as `qemu-guest-agent`, fails the whole install; install it after first boot.
- Set `shutdown: poweroff`, then detach the ISO before the next boot, or the installer runs again.
- Put the SSH public key in the seed so later steps run over SSH. Remove the key when the work is done.
- A QEMU serial console exposed as a host pty echoes input back into the guest unless the host side stays in raw mode. Hold it open from one process instead of reopening it per command.

<a id="control-the-desktop"></a>
## Control the desktop

Computer use is one route among several, and usually the slowest. Choose the first route that reaches the software:

| Order | Route | Works with | Use for |
| --- | --- | --- | --- |
| 1 | Shell commands on the host or over SSH | Every Agent with a terminal | Installs, configuration, command-line experiments, file transfer |
| 2 | Application scripting | Every Agent with a terminal | macOS: AppleScript and `osascript` for Word, Terminal, UTM; Linux guests: `xdotool` and ImageMagick `import` on an X11 session; Office COM on Windows |
| 3 | The host Agent's built-in computer use | Agents that ship it | Native GUI programs that expose no script interface |
| 4 | A desktop-control MCP server the user already installed | Agents with MCP support | Same as route 3 when the Agent has no built-in tool |
| 5 | Ask the user for one named click | Any | A permission dialog, login, or CAPTCHA that automation must not touch |

Built-in computer use differs by Agent, plan, operating system, and region, and changes often; check the current documentation instead of assuming. Common limits: terminals and IDEs are click-only or excluded, administrator and privacy prompts cannot be approved, and Windows sessions may take over the foreground. Do not ask the user to install another Agent only to gain computer use; routes 1 and 2 complete most labs.

When the user declines desktop control for an app, respect it and continue through routes 1 and 2. A Linux guest desktop can be driven entirely from SSH: set `DISPLAY` and `XAUTHORITY` for the logged-in session, type into a terminal with `xdotool`, and capture windows inside the guest. See [capture techniques](evidence-and-screenshots.md#capture-techniques).

Whatever the route:

1. Inspect the current application state.
2. Perform one bounded action.
3. Inspect the new state before deciding what follows.
4. Save a screenshot only when it shows a planned result.

## Virtual machines

1. Record the guest name, operating system, architecture, and power state.
2. Start an existing guest before considering a new VM.
3. Inspect the guest desktop before running commands.
4. Keep the VM frame visible only when guest identity matters.
5. Capture application content at a readable scale.
6. Do not shut down or suspend a guest unless the user asks or the task normally requires it.
7. When the work is done and the user wants to keep the guest, remove task leftovers and temporary keys, restore guest settings changed for automation (input method, screen lock, resolution), keep installed course tools, and tell the user how to log in.

## Environment substitutions

Mention a substitution in the report only when it remains visible or changes the result. State the required environment, the observed incompatibility, the replacement, and why the replacement still tests the requested concept.

Do not claim the original software succeeded after switching tools. If the named method is repaired and used for the final result, omit abandoned attempts from the report.
