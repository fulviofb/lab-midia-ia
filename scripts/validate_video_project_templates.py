#!/usr/bin/env python3
"""Valida relações mínimas da fixture de templates de vídeo.

Não avalia qualidade criativa, direitos ou adequação de provedor.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
from pathlib import Path
import sys
from typing import Any

try:
    import yaml
except ImportError:
    print("Erro: PyYAML não encontrado. Instale com: pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)


REQUIRED_YAML = {
    "registro-de-assets.yml",
    "cartao-de-cena.yml",
    "cartao-de-plano.yml",
    "cartao-de-segmento.yml",
    "contrato-de-experimento.yml",
}
REQUIRED_CSV_COLUMNS = {
    "project_id",
    "project_version",
    "experiment_id",
    "attempt_id",
    "scene_ids",
    "shot_ids",
    "segment_ids",
    "reference_asset_ids",
    "artifact_relative_uri",
    "artifact_sha256",
    "status",
    "decision",
}


def load_yaml(path: Path) -> dict[str, Any]:
    data = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not isinstance(data, dict):
        raise ValueError(f"raiz YAML não é objeto: {path.name}")
    return data


def split_ids(value: str | None) -> set[str]:
    if not value:
        return set()
    return {item.strip() for item in value.split(";") if item.strip()}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def resolve_within(root: Path, relative_uri: str) -> Path:
    candidate = Path(relative_uri)
    if candidate.is_absolute():
        raise ValueError(f"URI absoluta não permitida: {relative_uri}")
    resolved_root = root.resolve()
    resolved = (resolved_root / candidate).resolve()
    if not resolved.is_relative_to(resolved_root):
        raise ValueError(f"URI escapa do projeto: {relative_uri}")
    return resolved


def _validate(project_dir: Path) -> list[str]:
    errors: list[str] = []

    for filename in sorted(REQUIRED_YAML):
        if not (project_dir / filename).is_file():
            errors.append(f"arquivo obrigatório ausente: {filename}")
    log_path = project_dir / "log-de-geracao.csv"
    if not log_path.is_file():
        errors.append("arquivo obrigatório ausente: log-de-geracao.csv")
    if errors:
        return errors

    docs = {name: load_yaml(project_dir / name) for name in REQUIRED_YAML}
    metadata = [data.get("metadata", {}) for data in docs.values()]
    project_ids = {item.get("project_id") for item in metadata}
    project_versions = {item.get("project_version") for item in metadata}
    if None in project_ids or len(project_ids) != 1:
        errors.append(f"project_id inconsistente: {sorted(map(str, project_ids))}")
    if None in project_versions or len(project_versions) != 1:
        errors.append(f"project_version inconsistente: {sorted(map(str, project_versions))}")

    registry = docs["registro-de-assets.yml"]
    asset_items = registry.get("assets", [])
    asset_ids = [item.get("asset_id") for item in asset_items]
    duplicate_asset_ids = sorted({item for item in asset_ids if item and asset_ids.count(item) > 1})
    if duplicate_asset_ids:
        errors.append(f"asset_ids duplicados: {duplicate_asset_ids}")
    assets = {item.get("asset_id"): item for item in asset_items}
    if None in assets:
        errors.append("asset sem asset_id")
    for asset_id, asset in assets.items():
        relative_uri = asset.get("relative_uri")
        if not relative_uri:
            errors.append(f"asset sem relative_uri: {asset_id}")
            continue
        try:
            path = resolve_within(project_dir, relative_uri)
        except ValueError as exc:
            errors.append(f"asset com URI insegura: {asset_id}: {exc}")
            continue
        if not path.is_file():
            errors.append(f"asset ausente: {asset_id} -> {relative_uri}")
            continue
        expected = asset.get("content_hash_sha256")
        if expected and sha256(path) != expected:
            errors.append(f"hash divergente do asset: {asset_id}")

    scene = docs["cartao-de-cena.yml"]
    scene_id = scene["metadata"].get("scene_id")
    beat_items = scene.get("beats", [])
    beat_id_list = [item.get("beat_id") for item in beat_items]
    duplicate_beat_ids = sorted({item for item in beat_id_list if item and beat_id_list.count(item) > 1})
    if duplicate_beat_ids:
        errors.append(f"beat_ids duplicados: {duplicate_beat_ids}")
    beat_ids = set(beat_id_list)

    shot = docs["cartao-de-plano.yml"]
    shot_id = shot["metadata"].get("shot_id")
    if shot["metadata"].get("scene_id") != scene_id:
        errors.append("cartão de plano referencia scene_id inexistente")
    unknown_beats = set(shot.get("narrative", {}).get("related_beat_ids", [])) - beat_ids
    if unknown_beats:
        errors.append(f"plano referencia beats ausentes: {sorted(unknown_beats)}")
    unknown_assets = set(shot.get("references", {}).get("asset_ids", [])) - set(assets)
    if unknown_assets:
        errors.append(f"plano referencia assets ausentes: {sorted(unknown_assets)}")
    subject_assets = set(shot.get("visual", {}).get("subjects", {}).get("asset_ids", []))
    if not subject_assets.issubset(assets):
        errors.append(f"plano usa assets-sujeito ausentes: {sorted(subject_assets - set(assets))}")

    segment = docs["cartao-de-segmento.yml"]
    segment_id = segment["metadata"].get("segment_id")
    coverage = segment.get("coverage", {})
    if scene_id not in coverage.get("scene_ids", []):
        errors.append("segmento não cobre a cena da fixture")
    if shot_id not in coverage.get("shot_ids", []):
        errors.append("segmento não cobre o plano da fixture")
    if not set(coverage.get("beat_ids", [])).issubset(beat_ids):
        errors.append("segmento referencia beat ausente")
    segment_assets = set(segment.get("strategy", {}).get("reference_asset_ids", []))
    if not segment_assets.issubset(assets):
        errors.append("segmento referencia asset ausente")

    experiment = docs["contrato-de-experimento.yml"]
    experiment_id = experiment["metadata"].get("experiment_id")
    scope = experiment.get("scope", {})
    if scene_id not in scope.get("scene_ids", []):
        errors.append("experimento não referencia a cena")
    if shot_id not in scope.get("shot_ids", []):
        errors.append("experimento não referencia o plano")
    if segment_id not in scope.get("segment_ids", []):
        errors.append("experimento não referencia o segmento")
    fixture_assets = set(experiment.get("contract", {}).get("fixture_asset_ids", []))
    if not fixture_assets.issubset(assets):
        errors.append("experimento referencia asset ausente")

    with log_path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        columns = set(reader.fieldnames or [])
        missing_columns = REQUIRED_CSV_COLUMNS - columns
        if missing_columns:
            errors.append(f"colunas ausentes no log: {sorted(missing_columns)}")
        rows = list(reader)
    if not rows:
        errors.append("log não possui nenhuma tentativa")

    project_id = next(iter(project_ids)) if len(project_ids) == 1 else None
    project_version = next(iter(project_versions)) if len(project_versions) == 1 else None
    for index, row in enumerate(rows, start=2):
        prefix = f"log linha {index}"
        if not row.get("attempt_id"):
            errors.append(f"{prefix}: attempt_id obrigatório")
        if row.get("project_id") != project_id:
            errors.append(f"{prefix}: project_id divergente")
        if row.get("project_version") != project_version:
            errors.append(f"{prefix}: project_version divergente")
        if row.get("experiment_id") != experiment_id:
            errors.append(f"{prefix}: experiment_id ausente/divergente")
        row_scene_ids = split_ids(row.get("scene_ids"))
        row_shot_ids = split_ids(row.get("shot_ids"))
        row_segment_ids = split_ids(row.get("segment_ids"))
        row_reference_ids = split_ids(row.get("reference_asset_ids"))
        if not row_scene_ids:
            errors.append(f"{prefix}: scene_ids obrigatório")
        elif not row_scene_ids.issubset({scene_id}):
            errors.append(f"{prefix}: scene_id desconhecido")
        if not row_shot_ids:
            errors.append(f"{prefix}: shot_ids obrigatório")
        elif not row_shot_ids.issubset({shot_id}):
            errors.append(f"{prefix}: shot_id desconhecido")
        if not row_segment_ids:
            errors.append(f"{prefix}: segment_ids obrigatório")
        elif not row_segment_ids.issubset({segment_id}):
            errors.append(f"{prefix}: segment_id desconhecido")
        if fixture_assets and not row_reference_ids:
            errors.append(f"{prefix}: reference_asset_ids obrigatório para esta fixture")
        elif not row_reference_ids.issubset(assets):
            errors.append(f"{prefix}: asset desconhecido")
        artifact_uri = row.get("artifact_relative_uri")
        artifact_hash = row.get("artifact_sha256")
        if artifact_uri:
            try:
                artifact_path = resolve_within(project_dir, artifact_uri)
            except ValueError as exc:
                errors.append(f"{prefix}: URI de artefato insegura: {exc}")
                continue
            if not artifact_path.is_file():
                errors.append(f"{prefix}: artefato ausente: {artifact_uri}")
            elif artifact_hash and sha256(artifact_path) != artifact_hash:
                errors.append(f"{prefix}: hash do artefato divergente")

    return errors


def validate(project_dir: Path) -> list[str]:
    try:
        return _validate(project_dir)
    except (AttributeError, KeyError, TypeError, ValueError, yaml.YAMLError) as exc:
        return [f"estrutura inválida: {exc}"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("project_dir", type=Path)
    args = parser.parse_args()
    project_dir = args.project_dir.resolve()
    if not project_dir.is_dir():
        print(f"Erro: diretório não encontrado: {project_dir}", file=sys.stderr)
        return 2
    try:
        errors = validate(project_dir)
    except (OSError, ValueError, yaml.YAMLError) as exc:
        print(f"Erro de leitura: {exc}", file=sys.stderr)
        return 2
    if errors:
        print("FALHOU")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"OK: relações mínimas válidas em {project_dir.name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
