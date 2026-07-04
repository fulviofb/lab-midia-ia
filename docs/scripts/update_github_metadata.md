# Script: update_github_metadata.py

Atualiza os metadados do `catalog.yml` consultando a GitHub API para cada repositório.

## Uso

### Dry-run (recomendado antes de aplicar)

```bash
python scripts/update_github_metadata.py --dry-run
```

Mostra todas as mudanças que seriam aplicadas, sem escrever no arquivo.

### Aplicar mudanças

```bash
python scripts/update_github_metadata.py --write
```

Atualiza o `catalog.yml` com os dados mais recentes da GitHub API.

## Pré-requisitos

- Python 3.11+
- PyYAML (`pip install pyyaml`)
- `gh` CLI autenticado **ou** variável `GITHUB_TOKEN` no ambiente

### Autenticação

O script tenta autenticar nesta ordem:

1. Variável `GITHUB_TOKEN` no ambiente;
2. Variável `GITHUB_API_TOKEN` no ambiente;
3. `gh auth token` (gh CLI);

Se nenhuma funcionar, roda sem autenticação (rate limit: 60 requests/hora).

## Campos atualizados

Para cada repositório no catálogo:

| Campo | Descrição | Comportamento |
|---|---|---|
| `stars_observed` | Número de estrelas | Sempre atualiza |
| `forks_observed` | Número de forks | Novo campo, sempre adiciona |
| `open_issues_observed` | Issues abertas | Novo campo, sempre adiciona |
| `language` | Linguagem principal | Só atualiza se vazio ou "unknown" |
| `license` | Licença SPDX | Só atualiza se "unknown"/"NOASSERTION" |
| `github_updated_at` | Data último push | Novo campo, sempre adiciona |
| `archived` | Se arquivado | Novo campo, só adiciona se True |
| `disabled` | Se desabilitado | Novo campo, só adiciona se True |
| `topics` | Tópicos do repo | Novo campo, só adiciona se não vazio |

## Exemplo de output

```txt
Autenticado na GitHub API via gh CLI.
Total de repositórios no catálogo: 18
Modo: DRY-RUN (sem escrita)

  [1/18] video-use (browser-use/video-use)
    stars_observed: 14603 → 14656
    forks_observed: (novo) → 1750
    open_issues_observed: (novo) → 53
    github_updated_at: (novo) → 2026-07-01T00:33:52Z
  ...

Resumo:
  Repos atualizados: 17
  Repos sem mudanças: 1
  Repos com erro:     0
  Total de mudanças:  81
```

## Notas

- O script respeita rate limits da GitHub API;
- Pula repositórios cuja URL não é do GitHub (ex: `remotion-dev/remotion/packages/skills` aponta para remotion.dev);
- Trata caminhos com subpath (ex: `remotion-dev/remotion/packages/skills` → busca `remotion-dev/remotion`);
- Preserva campos manuais como `notes`, `status`, `priority`, `copy_policy` e `use_cases`;
- Não sobrescreve licenças já identificadas manualmente;
- Não sobrescreve linguagem já identificada, exceto se "unknown".

## Cron job (opcional)

Para rodar periodicamente via Hermes cron:

```
cronjob action=create schedule="0 9 * * 1" prompt="Rode python scripts/update_github_metadata.py --write no repo lab-midia-ia, commit e push as mudanças"
```
