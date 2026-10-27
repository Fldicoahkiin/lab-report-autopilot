from __future__ import annotations

import json
import os
import sys
import tempfile
import types
import unittest
from pathlib import Path
from unittest.mock import patch

from PIL import Image

SKILL_DIR = Path(__file__).resolve().parents[1] / "skills/lab-report-autopilot"
sys.path.insert(0, str(SKILL_DIR))

from scripts import evidence_manifest, init_report, probe_environment


def noise_image() -> Image.Image:
    # Noise keeps the compressed data large enough to damage or cut in half.
    return Image.frombytes("L", (64, 48), os.urandom(64 * 48))


class InitReportTests(unittest.TestCase):
    def test_creates_report_workspace(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "report"
            argv = [
                "init_report.py",
                str(output),
                "--kind",
                "lab",
                "--discipline",
                "packet-analysis",
                "--title",
                "ARP 抓包分析",
            ]
            with patch("sys.argv", argv):
                init_report.main()

            self.assertTrue((output / "draft.md").is_file())
            self.assertTrue((output / "evidence/original").is_dir())
            self.assertTrue((output / "format-contract.md").is_file())
            config = json.loads((output / "report-config.json").read_text())
            self.assertEqual(config["title"], "ARP 抓包分析")


    def test_accepts_course_name_without_registry_id(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "report"
            argv = [
                "init_report.py",
                str(output),
                "--kind",
                "lab",
                "--discipline",
                "SDN 技术",
                "--title",
                "软件定义网络测试床搭建",
            ]
            with patch("sys.argv", argv):
                init_report.main()

            self.assertIn("SDN 技术", (output / "draft.md").read_text(encoding="utf-8"))


    def test_reuses_folder_created_by_bootstrap_but_not_a_draft(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "report"
            (output / ".lab-report-runtime").mkdir(parents=True)
            argv = [
                "init_report.py",
                str(output),
                "--kind",
                "lab",
                "--discipline",
                "databases",
                "--title",
                "SQL 查询",
            ]
            with patch("sys.argv", argv):
                init_report.main()
            self.assertTrue((output / "draft.md").is_file())

            with patch("sys.argv", argv), self.assertRaises(SystemExit):
                init_report.main()


class EvidenceManifestTests(unittest.TestCase):
    def test_reports_unreadable_image_without_stopping(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            Image.new("RGB", (32, 24), "white").save(root / "good.png")
            (root / "bad.png").write_bytes(b"not an image")

            manifest = evidence_manifest.build_manifest(root)

            self.assertEqual(manifest["image_count"], 2)
            self.assertEqual(manifest["error_count"], 1)
            bad = next(image for image in manifest["images"] if image["path"] == "bad.png")
            self.assertIn("error", bad)

    def test_reports_png_with_broken_chunk_checksum(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            noise_image().save(root / "capture.png")
            data = bytearray((root / "capture.png").read_bytes())
            data[data.index(b"IDAT") + 20] ^= 0xFF
            (root / "capture.png").write_bytes(data)

            manifest = evidence_manifest.build_manifest(root)

            self.assertEqual(manifest["error_count"], 1)

    def test_reports_truncated_jpeg(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            noise_image().save(root / "capture.jpg", quality=90)
            data = (root / "capture.jpg").read_bytes()
            (root / "capture.jpg").write_bytes(data[: len(data) // 2])

            manifest = evidence_manifest.build_manifest(root)

            self.assertEqual(manifest["error_count"], 1)

    def test_marks_duplicate_images(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            image = Image.new("RGB", (32, 24), "white")
            image.save(root / "first.png")
            image.save(root / "second.png")

            manifest = evidence_manifest.build_manifest(root)

            self.assertEqual(manifest["image_count"], 2)
            self.assertEqual(manifest["duplicate_count"], 1)

    def test_rejects_missing_directory(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            with self.assertRaises(NotADirectoryError):
                evidence_manifest.build_manifest(Path(directory) / "missing")


class ProbeEnvironmentTests(unittest.TestCase):
    def test_reports_current_system(self) -> None:
        result = probe_environment.inspect_environment()

        self.assertIn("system", result)
        self.assertIn("commands", result)
        self.assertIn("python3", result["commands"])

    def test_finds_windows_app_from_program_files(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            executable = Path(directory) / "Wireshark/Wireshark.exe"
            executable.parent.mkdir()
            executable.touch()

            with patch.dict(os.environ, {"PROGRAMFILES": directory}, clear=True):
                apps = probe_environment.installed_apps("Windows")

            self.assertEqual(apps, [str(executable)])


    def test_finds_vmware_from_registry_install_path(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            vmrun = Path(directory) / "vmrun.exe"
            vmrun.touch()

            class FakeKey:
                def __enter__(self):
                    return self

                def __exit__(self, *exc):
                    return False

            def open_key(root, key):
                if "VMware Workstation" in key:
                    return FakeKey()
                raise FileNotFoundError(key)

            fake = types.SimpleNamespace(
                HKEY_LOCAL_MACHINE=object(),
                OpenKey=open_key,
                QueryValueEx=lambda handle, value: (directory, 1),
            )
            with patch.dict(sys.modules, {"winreg": fake}):
                apps = probe_environment.registry_apps()

            self.assertEqual(apps, [str(vmrun)])


class WindowsBootstrapTests(unittest.TestCase):
    def test_uses_an_isolated_non_admin_runtime(self) -> None:
        script = (SKILL_DIR / "scripts/bootstrap_windows.ps1").read_text()

        self.assertIn(".lab-report-runtime", script)
        self.assertIn("-m venv", script)
        self.assertIn("InstallAllUsers=0", script)
        self.assertIn("PrependPath=0", script)
        self.assertIn("Include_pip=1", script)
        self.assertNotIn("pip install --user", script)

    def test_pins_official_python_installers(self) -> None:
        script = (SKILL_DIR / "scripts/bootstrap_windows.ps1").read_text()

        self.assertIn("https://www.python.org/ftp/python/", script)
        self.assertIn("python-$PythonVersion-amd64.exe", script)
        self.assertIn("python-$PythonVersion-arm64.exe", script)
        self.assertIn("Get-FileHash", script)


if __name__ == "__main__":
    unittest.main()
