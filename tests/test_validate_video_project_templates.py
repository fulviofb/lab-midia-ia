from __future__ import annotations

import csv
import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest

import yaml


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts" / "validate_video_project_templates.py"
SPEC = importlib.util.spec_from_file_location("validate_video_project_templates", MODULE_PATH)
assert SPEC and SPEC.loader
VALIDATOR = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(VALIDATOR)
FIXTURE = ROOT / "examples" / "video-adaptativo-minimo"


class ValidateVideoProjectTemplatesTest(unittest.TestCase):
    def copy_fixture(self) -> tuple[tempfile.TemporaryDirectory[str], Path]:
        temp = tempfile.TemporaryDirectory()
        target = Path(temp.name) / "fixture"
        shutil.copytree(FIXTURE, target)
        return temp, target

    def test_valid_fixture(self) -> None:
        self.assertEqual([], VALIDATOR.validate(FIXTURE))

    def test_unknown_shot_reference_fails(self) -> None:
        temp, target = self.copy_fixture()
        self.addCleanup(temp.cleanup)
        path = target / "cartao-de-segmento.yml"
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        data["coverage"]["shot_ids"] = ["UNKNOWN-SHOT"]
        path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")
        errors = VALIDATOR.validate(target)
        self.assertTrue(any("não cobre o plano" in error for error in errors), errors)

    def test_artifact_hash_mismatch_fails(self) -> None:
        temp, target = self.copy_fixture()
        self.addCleanup(temp.cleanup)
        log_path = target / "log-de-geracao.csv"
        with log_path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
            fieldnames = list(rows[0])
        rows[0]["artifact_sha256"] = "0" * 64
        with log_path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        errors = VALIDATOR.validate(target)
        self.assertTrue(any("hash do artefato divergente" in error for error in errors), errors)

    def test_asset_path_traversal_fails(self) -> None:
        temp, target = self.copy_fixture()
        self.addCleanup(temp.cleanup)
        path = target / "registro-de-assets.yml"
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        data["assets"][0]["relative_uri"] = "../outside.svg"
        path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")
        errors = VALIDATOR.validate(target)
        self.assertTrue(any("URI insegura" in error for error in errors), errors)

    def test_absolute_asset_path_fails(self) -> None:
        temp, target = self.copy_fixture()
        self.addCleanup(temp.cleanup)
        path = target / "registro-de-assets.yml"
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        data["assets"][0]["relative_uri"] = str((target.parent / "outside.svg").resolve())
        path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")
        errors = VALIDATOR.validate(target)
        self.assertTrue(any("URI insegura" in error for error in errors), errors)

    def test_duplicate_asset_id_fails(self) -> None:
        temp, target = self.copy_fixture()
        self.addCleanup(temp.cleanup)
        path = target / "registro-de-assets.yml"
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        data["assets"].append(dict(data["assets"][0]))
        path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")
        errors = VALIDATOR.validate(target)
        self.assertTrue(any("asset_ids duplicados" in error for error in errors), errors)

    def test_empty_log_fails(self) -> None:
        temp, target = self.copy_fixture()
        self.addCleanup(temp.cleanup)
        log_path = target / "log-de-geracao.csv"
        header = log_path.read_text(encoding="utf-8").splitlines()[0]
        log_path.write_text(header + "\n", encoding="utf-8")
        errors = VALIDATOR.validate(target)
        self.assertTrue(any("nenhuma tentativa" in error for error in errors), errors)

    def test_empty_required_relations_fail(self) -> None:
        temp, target = self.copy_fixture()
        self.addCleanup(temp.cleanup)
        log_path = target / "log-de-geracao.csv"
        with log_path.open(encoding="utf-8", newline="") as handle:
            rows = list(csv.DictReader(handle))
            fieldnames = list(rows[0])
        rows[0]["scene_ids"] = ""
        rows[0]["shot_ids"] = ""
        rows[0]["segment_ids"] = ""
        rows[0]["reference_asset_ids"] = ""
        with log_path.open("w", encoding="utf-8", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
        errors = VALIDATOR.validate(target)
        self.assertTrue(any("scene_ids obrigatório" in error for error in errors), errors)
        self.assertTrue(any("shot_ids obrigatório" in error for error in errors), errors)
        self.assertTrue(any("segment_ids obrigatório" in error for error in errors), errors)
        self.assertTrue(any("reference_asset_ids obrigatório" in error for error in errors), errors)

    def test_structurally_invalid_yaml_is_controlled(self) -> None:
        temp, target = self.copy_fixture()
        self.addCleanup(temp.cleanup)
        path = target / "cartao-de-cena.yml"
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
        data["metadata"] = []
        path.write_text(yaml.safe_dump(data, sort_keys=False, allow_unicode=True), encoding="utf-8")
        errors = VALIDATOR.validate(target)
        self.assertTrue(any("estrutura inválida" in error for error in errors), errors)


if __name__ == "__main__":
    unittest.main()
