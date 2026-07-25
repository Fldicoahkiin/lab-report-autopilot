from __future__ import annotations

import argparse
import json
import os
import platform
import shutil
from pathlib import Path


COMMANDS = [
    "cmd",
    "powershell",
    "pwsh",
    "winget",
    "wsl",
    "py",
    "python",
    "python3",
    "pip",
    "pip3",
    "node",
    "npm",
    "git",
    "docker",
    "nmap",
    "tshark",
    "sqlcmd",
    "mysql",
    "psql",
    "g++",
    "gcc",
    "clang++",
    "java",
    "javac",
    "dotnet",
    "php",
    "sqlite3",
    "soffice",
]

MAC_APPS = [
    "/Applications/UTM.app",
    "/Applications/Parallels Desktop.app",
    "/Applications/VMware Fusion.app",
    "/Applications/VirtualBox.app",
    "/Applications/Wireshark.app",
    "/Applications/Microsoft Word.app",
]

WINDOWS_APP_PATTERNS = [
    "Wireshark/Wireshark.exe",
    "Oracle/VirtualBox/VirtualBox.exe",
    "VMware/VMware Workstation/vmware.exe",
    "Microsoft Office/root/Office*/WINWORD.EXE",
    "Microsoft VS Code/Code.exe",
    "Microsoft SQL Server Management Studio */Common7/IDE/Ssms.exe",
    "MySQL/MySQL Workbench */MySQLWorkbench.exe",
    "Cisco Packet Tracer */bin/PacketTracer.exe",
    "Huawei/eNSP/eNSP_Client.exe",
    "Huawei/eNSP/eNSP.exe",
]


def installed_apps(system: str) -> list[str]:
    if system == "Darwin":
        return [path for path in MAC_APPS if Path(path).exists()]
    if system != "Windows":
        return []

    roots = [
        Path(value)
        for name in ("PROGRAMFILES", "PROGRAMFILES(X86)", "LOCALAPPDATA")
        if (value := os.environ.get(name))
    ]
    return sorted({
        str(path)
        for root in roots
        for pattern in WINDOWS_APP_PATTERNS
        for path in root.glob(pattern)
        if path.is_file()
    })


def inspect_environment() -> dict[str, object]:
    system = platform.system()
    commands = {name: shutil.which(name) for name in COMMANDS}
    return {
        "system": system,
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "python": platform.python_version(),
        "commands": commands,
        "apps": installed_apps(system),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    result = inspect_environment()

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return

    print(f"{result['system']} {result['release']} ({result['machine']})")
    for name, path in result["commands"].items():
        if path:
            print(f"{name}: {path}")
    for path in result["apps"]:
        print(f"app: {path}")


if __name__ == "__main__":
    main()
