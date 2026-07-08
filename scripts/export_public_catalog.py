#!/usr/bin/env python3
"""
export_public_catalog.py — Gera dados públicos e amigáveis a partir do catalog.yml.

Objetivo:
  Transformar o catálogo técnico do lab-midia-ia em arquivos seguros para consumo
  por sites, aulas e materiais para pessoas leigas/intermediárias.

Saídas:
  - public-data/catalog.public.json
  - public-data/catalog.public.md

Uso:
  python scripts/export_public_catalog.py
  python scripts/export_public_catalog.py --check

O modo --check valida se os arquivos gerados estão atualizados; útil para CI.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("Erro: PyYAML não encontrado. Instale com: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
CATALOG_PATH = ROOT / "catalog.yml"
OUT_DIR = ROOT / "public-data"
JSON_PATH = OUT_DIR / "catalog.public.json"
MD_PATH = OUT_DIR / "catalog.public.md"
SOURCE_REPO_URL = "https://github.com/fulviofb/lab-midia-ia"

CATEGORY_LABELS = {
    "video_programatico": "Vídeo programático",
    "edicao_video": "Edição de vídeo",
    "video_automatico_social": "Vídeo automático/social",
    "video_generativo_cinematico": "Vídeo generativo/cinematográfico",
    "voz_tts_clonagem": "Voz, narração e TTS",
    "imagem_design_prompts": "Imagem, design e prompts",
    "modelos_referencia": "Modelos e referências técnicas",
}

PRIORITY_LABELS = {
    "essential": "Essencial",
    "high": "Alta prioridade",
    "medium": "Prioridade média",
    "low": "Baixa prioridade",
}

STATUS_LABELS = {
    "tested_recommended_windows": "Testado e recomendado no Windows",
    "partially_tested_windows": "Parcialmente testado no Windows",
    "documented_not_installed": "Documentado; instalação prática pendente",
    "test_before_recommending": "Promissor; testar antes de recomendar",
    "watch_and_test": "Acompanhar e testar",
    "practical": "Prático",
    "mature_practical": "Maduro e prático",
    "reference": "Referência",
    "experimental_reference": "Referência experimental",
}

STATUS_RECOMMENDATION = {
    "tested_recommended_windows": "Pode ser recomendado com as observações do teste.",
    "partially_tested_windows": "Use com orientação; parte do fluxo ainda exige validação.",
    "documented_not_installed": "Bom candidato, mas precisa teste prático local antes de indicar para leigos.",
    "test_before_recommending": "Não recomendar ainda como caminho principal; fazer smoke test primeiro.",
    "watch_and_test": "Acompanhar maturidade e testar antes de usar em aula/produção.",
    "practical": "Pode entrar em fluxos práticos, com revisão de custo e dependências.",
    "mature_practical": "Candidato forte para teste prático e uso técnico.",
    "reference": "Use como referência, não como ferramenta principal para iniciantes.",
    "experimental_reference": "Somente para estudo/experimento; não indicar para iniciantes.",
}

CATEGORY_AUDIENCE = {
    "video_programatico": "usuários técnicos, devs e agentes",
    "edicao_video": "criadores, educadores e comunicadores",
    "video_automatico_social": "criadores e equipes de conteúdo",
    "video_generativo_cinematico": "criadores visuais e direção criativa",
    "voz_tts_clonagem": "narração, áudio, voz e acessibilidade",
    "imagem_design_prompts": "design, imagem, thumbnails e posts",
    "modelos_referencia": "estudo técnico e pesquisa",
}

TECHNICAL_LEVEL_LABELS = {
    "beginner": "iniciante",
    "intermediate": "intermediário",
    "technical": "técnico",
    "advanced": "avançado",
}


def slugify(text: str) -> str:
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9áàâãéêíóôõúçñ]+", "-", text, flags=re.I)
    text = text.strip("-")
    return text or "item"


def first_sentence(text: str | None) -> str:
    if not text:
        return ""
    normalized = " ".join(str(text).split())
    parts = re.split(r"(?<=[.!?])\s+", normalized, maxsplit=1)
    return parts[0].strip()


def infer_technical_level(repo: dict[str, Any]) -> str:
    category = repo.get("category")
    subcategory = repo.get("subcategory", "")
    status = repo.get("status", "")
    agent_fit = repo.get("agent_fit", "")
    install_hint = repo.get("install_hint")
    language = repo.get("language", "")

    if category == "modelos_referencia":
        return "advanced"
    if category == "video_programatico":
        return "technical"
    if category == "edicao_video" and subcategory in {"browser_video_editor", "video_editor"}:
        return "beginner"
    if category == "imagem_design_prompts":
        return "beginner"
    if install_hint or agent_fit == "high" or language in {"Python", "TypeScript", "Rust"}:
        if status in {"tested_recommended_windows", "practical", "mature_practical"}:
            return "intermediate"
        return "technical"
    return "intermediate"


def infer_cost_hint(repo: dict[str, Any]) -> str:
    url = (repo.get("url") or "").lower()
    category = repo.get("category")
    license_name = repo.get("license")
    status = repo.get("status")
    notes = (repo.get("notes") or "").lower()

    if "api" in notes or "api key" in notes or "paga" in notes or "comercial" in notes:
        return "Pode exigir API, plano pago ou atenção à licença comercial."
    if license_name in {"MIT", "Apache-2.0"} and "github.com" in url:
        if category in {"voz_tts_clonagem", "video_programatico", "edicao_video"}:
            return "Código aberto; pode exigir instalação local e máquina adequada."
        return "Código aberto ou referência pública; verificar custos de serviços externos."
    if status == "documented_not_installed":
        return "Pode exigir instalação manual e download de modelos."
    return "Verificar custos, limites gratuitos e termos antes de recomendar."


def build_public_summary(repo: dict[str, Any]) -> str:
    use_cases = repo.get("use_cases") or []
    if use_cases:
        return str(use_cases[0]).strip()
    note_sentence = first_sentence(repo.get("notes"))
    if note_sentence:
        return note_sentence
    return f"Ferramenta de {CATEGORY_LABELS.get(repo.get('category'), repo.get('category', 'mídia com IA'))}."


def public_item(repo: dict[str, Any], categories: dict[str, str]) -> dict[str, Any]:
    category = repo.get("category", "")
    priority = repo.get("priority", "")
    status = repo.get("status", "")
    technical_level = infer_technical_level(repo)
    name = repo.get("name") or repo.get("full_name") or "sem-nome"

    # Campos intencionalmente públicos e simples. Evitar notes completas quando forem muito técnicas.
    return {
        "id": slugify(name),
        "name": name,
        "full_name": repo.get("full_name", ""),
        "url": repo.get("url", ""),
        "category": category,
        "category_label": CATEGORY_LABELS.get(category, categories.get(category, category)),
        "subcategory": repo.get("subcategory", ""),
        "priority": priority,
        "priority_label": PRIORITY_LABELS.get(priority, priority or "Não classificado"),
        "status": status,
        "status_label": STATUS_LABELS.get(status, status or "Sem status"),
        "recommendation": STATUS_RECOMMENDATION.get(status, "Avaliar antes de recomendar."),
        "technical_level": technical_level,
        "technical_level_label": TECHNICAL_LEVEL_LABELS[technical_level],
        "audience": CATEGORY_AUDIENCE.get(category, "público geral interessado em mídia com IA"),
        "public_summary": build_public_summary(repo),
        "use_cases": repo.get("use_cases") or [],
        "license": repo.get("license", "unknown"),
        "language": repo.get("language", ""),
        "stars_observed": repo.get("stars_observed"),
        "agent_fit": repo.get("agent_fit", ""),
        "cost_hint": infer_cost_hint(repo),
        "install_hint_public": public_install_hint(repo),
    }


def public_install_hint(repo: dict[str, Any]) -> str:
    status = repo.get("status")
    category = repo.get("category")
    install_hint = repo.get("install_hint")
    if category == "imagem_design_prompts":
        return "Comece pela versão web ou pelo guia/prompt associado."
    if status == "test_before_recommending":
        return "Testar em pequena escala antes de indicar para terceiros."
    if status == "documented_not_installed":
        return "Ler o teste documentado e instalar manualmente antes de usar com público."
    if install_hint:
        return str(install_hint)
    if category in {"video_programatico", "voz_tts_clonagem"}:
        return "Exige ambiente técnico; seguir documentação do teste/workflow antes de recomendar."
    return "Abrir o link oficial e verificar requisitos atuais."


def build_export(data: dict[str, Any]) -> dict[str, Any]:
    categories = data.get("categories", {}) or {}
    repos = data.get("repositories", []) or []
    generated_at = datetime.now(timezone.utc).replace(microsecond=0).isoformat()

    items = [public_item(repo, categories) for repo in repos]
    items.sort(key=lambda item: (category_sort_key(item["category"]), priority_sort_key(item["priority"]), item["name"].lower()))

    grouped: dict[str, list[dict[str, Any]]] = {}
    for item in items:
        grouped.setdefault(item["category"], []).append(item)

    return {
        "schema_version": "1.0.0",
        "generated_at": generated_at,
        "source": {
            "repo": SOURCE_REPO_URL,
            "catalog_path": "catalog.yml",
            "generator": "scripts/export_public_catalog.py",
        },
        "metadata": {
            "name": data.get("metadata", {}).get("name", "lab-midia-ia"),
            "description": data.get("metadata", {}).get("description", ""),
            "language": data.get("metadata", {}).get("language", "pt-BR"),
            "status": data.get("metadata", {}).get("status", ""),
            "public_note": "Dados filtrados para sites, aulas e materiais introdutórios. Consulte catalog.yml para detalhes técnicos.",
        },
        "categories": [
            {
                "id": key,
                "label": CATEGORY_LABELS.get(key, key),
                "description": value,
                "item_count": len(grouped.get(key, [])),
            }
            for key, value in categories.items()
        ],
        "items": items,
        "groups": {
            key: [item["id"] for item in value]
            for key, value in grouped.items()
        },
    }


def category_sort_key(category: str) -> int:
    order = list(CATEGORY_LABELS.keys())
    return order.index(category) if category in order else len(order)


def priority_sort_key(priority: str) -> int:
    order = ["essential", "high", "medium", "low"]
    return order.index(priority) if priority in order else len(order)


def render_markdown(export: dict[str, Any]) -> str:
    lines: list[str] = []
    lines.append("# Catálogo público — Lab Mídia IA")
    lines.append("")
    lines.append("> Arquivo gerado automaticamente por `scripts/export_public_catalog.py` a partir de `catalog.yml`.")
    lines.append("")
    lines.append(f"Gerado em: `{export['generated_at']}`")
    lines.append("")
    lines.append("## Como usar")
    lines.append("")
    lines.append("Este arquivo é uma versão simplificada do catálogo para sites, aulas, materiais introdutórios e pessoas que não precisam ver todos os detalhes técnicos.")
    lines.append("")
    lines.append("Para detalhes completos, consulte o `catalog.yml`.")
    lines.append("")

    category_by_id = {cat["id"]: cat for cat in export["categories"]}
    items_by_id = {item["id"]: item for item in export["items"]}

    for category_id, item_ids in export["groups"].items():
        category = category_by_id.get(category_id, {"label": category_id, "description": ""})
        lines.append(f"## {category['label']}")
        lines.append("")
        if category.get("description"):
            lines.append(str(category["description"]))
            lines.append("")
        for item_id in item_ids:
            item = items_by_id[item_id]
            lines.append(f"### [{item['name']}]({item['url']})")
            lines.append("")
            lines.append(f"- **Status:** {item['status_label']}")
            lines.append(f"- **Prioridade:** {item['priority_label']}")
            lines.append(f"- **Nível:** {item['technical_level_label']}")
            lines.append(f"- **Licença:** {item['license']}")
            if item.get("stars_observed") is not None:
                lines.append(f"- **Estrelas observadas:** {item['stars_observed']}")
            lines.append(f"- **Resumo:** {item['public_summary']}")
            lines.append(f"- **Recomendação:** {item['recommendation']}")
            lines.append(f"- **Custo/requisitos:** {item['cost_hint']}")
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def load_catalog() -> dict[str, Any]:
    if not CATALOG_PATH.exists():
        raise FileNotFoundError(f"Não encontrei {CATALOG_PATH}")
    return yaml.safe_load(CATALOG_PATH.read_text(encoding="utf-8"))


def write_outputs(export: dict[str, Any]) -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    JSON_PATH.write_text(json.dumps(export, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    MD_PATH.write_text(render_markdown(export), encoding="utf-8")


def check_outputs(export: dict[str, Any]) -> int:
    # Preserve o generated_at existente para que --check seja determinístico.
    if JSON_PATH.exists():
        try:
            existing = json.loads(JSON_PATH.read_text(encoding="utf-8"))
            if existing.get("generated_at"):
                export = {**export, "generated_at": existing["generated_at"]}
        except json.JSONDecodeError:
            pass

    expected_json = json.dumps(export, ensure_ascii=False, indent=2) + "\n"
    expected_md = render_markdown(export)
    problems: list[str] = []
    if not JSON_PATH.exists() or JSON_PATH.read_text(encoding="utf-8") != expected_json:
        problems.append(str(JSON_PATH))
    if not MD_PATH.exists() or MD_PATH.read_text(encoding="utf-8") != expected_md:
        problems.append(str(MD_PATH))
    if problems:
        print("Arquivos desatualizados:")
        for problem in problems:
            print(f"  - {problem}")
        print("Rode: python scripts/export_public_catalog.py")
        return 1
    print("OK: exports públicos estão atualizados.")
    return 0


def validate_export(export: dict[str, Any]) -> None:
    assert export["schema_version"]
    assert export["items"], "Nenhum item exportado"
    ids = [item["id"] for item in export["items"]]
    assert len(ids) == len(set(ids)), "IDs duplicados no export público"
    required = {
        "id",
        "name",
        "url",
        "category",
        "category_label",
        "priority_label",
        "status_label",
        "recommendation",
        "technical_level_label",
        "public_summary",
        "license",
        "cost_hint",
    }
    for item in export["items"]:
        missing = required - set(item)
        assert not missing, f"Item {item.get('name')} sem campos: {missing}"
        assert item["url"], f"Item {item['name']} sem URL"


def main() -> int:
    parser = argparse.ArgumentParser(description="Gera export público do catalog.yml")
    parser.add_argument("--check", action="store_true", help="Valida se os exports estão atualizados")
    args = parser.parse_args()

    data = load_catalog()
    export = build_export(data)
    validate_export(export)

    if args.check:
        return check_outputs(export)

    write_outputs(export)
    print(f"Gerado: {JSON_PATH}")
    print(f"Gerado: {MD_PATH}")
    print(f"Itens exportados: {len(export['items'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
