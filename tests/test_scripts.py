from __future__ import annotations

import json
import os
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from PIL import Image

SKILL_DIR = Path(__file__).resolve().parents[1] / "skills/lab-report-autopilot"
sys.path.insert(0, str(SKILL_DIR))

from scripts import evidence_manifest, init_report, probe_environment


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
            config = json.loads((output / "report-config.json").read_text())
            self.assertEqual(config["title"], "ARP 抓包分析")


class EvidenceManifestTests(unittest.TestCase):
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


if __name__ == "__main__":
    unittest.main()
