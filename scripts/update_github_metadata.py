#!/usr/bin/env python3
"""
update_github_metadata.py — Atualiza metadados do catalog.yml via GitHub API.

Para cada repositório listado em `repositories`, busca na GitHub API:
  - stars (stargazers_count)
  - forks (forks_count)
  - license (spdx_id ou "NOASSERTION")
  - language (linguagem principal)
  - updated_at (data de último push)
  - archived (bool)
  - disabled (bool)
  - topics (lista)
  - open_issues_count

Atualiza os campos correspondentes no catalog.yml:
  - stars_observed
  - language (se vazio ou "unknown")
  - license (se "unknown"/"NOASSERTION")
  - archived (novo campo, se True)
  - disabled (novo campo, se True)
  - github_updated_at (novo campo)
  - forks_observed (novo campo)
  - open_issues_observed (novo campo)
  - topics (novo campo, se não vazio)

Modos:
  --dry-run   Mostra mudanças sem escrever no arquivo.
  --write     Escreve as mudanças no catalog.yml.

Uso:
  python scripts/update_github_metadata.py --dry-run
  python scripts/update_github_metadata.py --write

Pré-requisitos:
  - Python 3.11+
  - PyYAML (pip install pyyaml)
  - gh CLI autenticado OU variável GITHUB_TOKEN

Autenticação:
  O script usa `gh api` por padrão. Se gh não estiver disponível, usa GITHUB_TOKEN
  ou GITHUB_API_TOKEN do ambiente.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    print("Erro: PyYAML não encontrado. Instale com: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

CATALOG_PATH = Path(__file__).parent.parent / "catalog.yml"
API_BASE = "https://api.github.com/repos"
RATE_LIMIT_DELAY = 0.5  # segundos entre requests


def get_github_token() -> str | None:
    """Tenta obter token do ambiente ou via gh CLI."""
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GITHUB_API_TOKEN")
    if token:
        return token
    # Tentar gh CLI
    try:
        result = subprocess.run(
            ["gh", "auth", "token"],
            capture_output=True,
            text=True,
            timeout=10,
        )
        if result.returncode == 0 and result.stdout.strip():
            return result.stdout.strip()
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass
    return None


def fetch_repo_data(full_name: str, token: str | None) -> dict[str, Any] | None:
    """Busca dados de um repositório na GitHub API."""
    # Tratar casos onde full_name não é um repo GitHub direto
    # ex: "remotion-dev/remotion/packages/skills" → usar "remotion-dev/remotion"
    parts = full_name.split("/")
    if len(parts) < 2:
        return None
    owner_repo = f"{parts[0]}/{parts[1]}"
    url = f"{API_BASE}/{owner_repo}"

    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "lab-midia-ia-catalog-updater",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            return data
    except urllib.error.HTTPError as e:
        if e.code == 404:
            print(f"  [WARN] {owner_repo}: 404 Not Found", file=sys.stderr)
            return None
        if e.code == 403:
            # Rate limit
            remaining = e.headers.get("X-RateLimit-Remaining", "?")
            print(f"  [WARN] {owner_repo}: 403 Forbidden (rate limit remaining: {remaining})", file=sys.stderr)
            if remaining == "0":
                reset = e.headers.get("X-RateLimit-Reset")
                if reset:
                    reset_time = time.strftime("%H:%M:%S", time.localtime(int(reset)))
                    print(f"  [WARN] Rate limit reset at: {reset_time}", file=sys.stderr)
            return None
        print(f"  [ERROR] {owner_name}: HTTP {e.code}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"  [ERROR] {owner_repo}: {e}", file=sys.stderr)
        return None


def normalize_license(license_data: dict | None) -> str | None:
    """Extrai SPDX ID da licença."""
    if not license_data:
        return None
    spdx = license_data.get("spdx_id")
    if spdx and spdx != "NOASSERTION":
        return spdx
    return None


def compute_changes(repo_entry: dict, api_data: dict) -> dict[str, Any]:
    """Compara dados atuais com dados da API e retorna mudanças."""
    changes: dict[str, Any] = {}

    # Stars
    current_stars = repo_entry.get("stars_observed")
    new_stars = api_data.get("stargazers_count")
    if new_stars is not None and current_stars != new_stars:
        changes["stars_observed"] = new_stars

    # Forks (novo campo)
    new_forks = api_data.get("forks_count")
    if new_forks is not None:
        changes["forks_observed"] = new_forks

    # Open issues (novo campo)
    new_issues = api_data.get("open_issues_count")
    if new_issues is not None:
        changes["open_issues_observed"] = new_issues

    # Language
    current_lang = repo_entry.get("language")
    new_lang = api_data.get("language")
    if new_lang and (not current_lang or current_lang == "unknown"):
        changes["language"] = new_lang

    # License — só atualizar se atual for unknown/NOASSERTION/None
    current_license = repo_entry.get("license")
    new_license = normalize_license(api_data.get("license"))
    if new_license and current_license in (None, "unknown", "NOASSERTION", ""):
        changes["license"] = new_license

    # Archived
    if api_data.get("archived"):
        changes["archived"] = True

    # Disabled
    if api_data.get("disabled"):
        changes["disabled"] = True

    # Updated at
    new_updated = api_data.get("pushed_at") or api_data.get("updated_at")
    if new_updated:
        changes["github_updated_at"] = new_updated

    # Topics
    topics = api_data.get("topics", [])
    if topics:
        changes["topics"] = topics

    return changes


def run(dry_run: bool = True) -> int:
    """Executa a atualização do catálogo."""
    if not CATALOG_PATH.exists():
        print(f"Erro: {CATALOG_PATH} não encontrado.", file=sys.stderr)
        return 1

    # Ler catalog.yml
    with open(CATALOG_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    data = yaml.safe_load(content)

    if not data or "repositories" not in data:
        print("Erro: catalog.yml não contém 'repositories'.", file=sys.stderr)
        return 1

    repos = data["repositories"]
    token = get_github_token()

    if token:
        print(f"Autenticado na GitHub API via {'GITHUB_TOKEN' if os.environ.get('GITHUB_TOKEN') else 'gh CLI'}.")
    else:
        print("Aviso: sem autenticação. Rate limit não autenticado: 60 requests/hora.", file=sys.stderr)

    print(f"Total de repositórios no catálogo: {len(repos)}")
    print(f"Modo: {'DRY-RUN (sem escrita)' if dry_run else 'WRITE (atualizando arquivo)'}")
    print()

    total_changes = 0
    total_updated = 0
    total_unchanged = 0
    total_errors = 0

    for i, repo in enumerate(repos):
        full_name = repo.get("full_name", "")
        name = repo.get("name", full_name)

        if not full_name:
            print(f"  [{i+1}/{len(repos)}] {name}: sem full_name, pulando.")
            continue

        # Pular se URL não é GitHub
        url = repo.get("url", "")
        if "github.com" not in url:
            print(f"  [{i+1}/{len(repos)}] {name}: URL não é GitHub, pulando.")
            total_unchanged += 1
            continue

        print(f"  [{i+1}/{len(repos)}] {name} ({full_name})")

        api_data = fetch_repo_data(full_name, token)
        time.sleep(RATE_LIMIT_DELAY)

        if not api_data:
            print(f"    → sem dados da API")
            total_errors += 1
            continue

        changes = compute_changes(repo, api_data)

        if not changes:
            print(f"    → sem mudanças")
            total_unchanged += 1
            continue

        # Mostrar mudanças
        for key, value in changes.items():
            old_val = repo.get(key)
            if old_val is not None:
                print(f"    {key}: {old_val} → {value}")
            else:
                print(f"    {key}: (novo) → {value}")

        total_changes += len(changes)

        if not dry_run:
            # Aplicar mudanças
            for key, value in changes.items():
                repo[key] = value

        total_updated += 1

    print()
    print(f"Resumo:")
    print(f"  Repos atualizados: {total_updated}")
    print(f"  Repos sem mudanças: {total_unchanged}")
    print(f"  Repos com erro:     {total_errors}")
    print(f"  Total de mudanças:  {total_changes}")

    if dry_run:
        print()
        print("DRY-RUN: nenhuma mudança foi escrita.")
        print("Para aplicar as mudanças, rode: python scripts/update_github_metadata.py --write")
        return 0

    if total_changes > 0:
        # Escrever catalog.yml
        # Usar yaml.dump com preserve order e allow_unicode
        # Configurar Dumper para não quebrar unicode
        class IndentedDumper(yaml.SafeDumper):
            def increase_indent(self, flow=False, indentless=False):
                return super().increase_indent(flow, False)

        output = yaml.dump(
            data,
            Dumper=IndentedDumper,
            default_flow_style=False,
            allow_unicode=True,
            sort_keys=False,
            width=120,
        )

        # Adicionar comment header
        output = f"# catalog.yml — atualizado por update_github_metadata.py em {time.strftime('%Y-%m-%d %H:%M:%S')}\n{output}"

        with open(CATALOG_PATH, "w", encoding="utf-8") as f:
            f.write(output)

        print(f"\nArquivo atualizado: {CATALOG_PATH}")
    else:
        print("\nNenhuma mudança para escrever.")

    return 0


def main():
    args = sys.argv[1:]
    dry_run = "--write" not in args

    if "--help" in args or "-h" in args:
        print(__doc__)
        return

    exit_code = run(dry_run=dry_run)
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
