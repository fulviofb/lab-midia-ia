# Export público do catálogo

O script `scripts/export_public_catalog.py` transforma o `catalog.yml` técnico em arquivos públicos e amigáveis para sites, aulas e materiais introdutórios.

## Arquivos gerados

```txt
public-data/catalog.public.json
public-data/catalog.public.md
```

## Para que serve

O `catalog.yml` contém informações úteis para manutenção do laboratório, mas nem tudo é ideal para aparecer no site ou para pessoas leigas.

O export público filtra e reescreve o catálogo para expor apenas campos seguros e úteis:

- nome;
- link;
- categoria;
- prioridade em linguagem humana;
- status em linguagem humana;
- nível técnico sugerido;
- público-alvo;
- resumo público;
- casos de uso;
- licença;
- linguagem principal;
- estrelas observadas;
- recomendação;
- indicação de custo/requisitos;
- orientação simples de instalação/uso.

Ele evita campos mais internos/técnicos, como:

- `notes` completas;
- `copy_policy`;
- `forks_observed`;
- `open_issues_observed`;
- `topics`;
- detalhes de manutenção do catálogo.

## Uso

Gerar/atualizar os exports:

```bash
python scripts/export_public_catalog.py
```

Validar se os exports estão atualizados:

```bash
python scripts/export_public_catalog.py --check
```

## Estrutura do JSON

Exemplo resumido:

```json
{
  "schema_version": "1.0.0",
  "generated_at": "2026-07-08T...Z",
  "source": {
    "repo": "https://github.com/fulviofb/lab-midia-ia",
    "catalog_path": "catalog.yml",
    "generator": "scripts/export_public_catalog.py"
  },
  "metadata": {
    "name": "lab-midia-ia",
    "description": "...",
    "language": "pt-BR",
    "status": "public_lab"
  },
  "categories": [
    {
      "id": "edicao_video",
      "label": "Edição de vídeo",
      "description": "...",
      "item_count": 3
    }
  ],
  "items": [
    {
      "id": "openreel-video",
      "name": "OpenReel Video",
      "url": "https://github.com/Augani/openreel-video",
      "category_label": "Edição de vídeo",
      "status_label": "Promissor; testar antes de recomendar",
      "technical_level_label": "iniciante",
      "public_summary": "Editar vídeos visualmente no navegador sem upload para nuvem.",
      "recommendation": "Não recomendar ainda como caminho principal; fazer smoke test primeiro."
    }
  ],
  "groups": {
    "edicao_video": ["openreel-video", "opencut"]
  }
}
```

## Como o site Concafras IA pode consumir

### Opção A — copiar arquivo para o site

No curto prazo, copiar `public-data/catalog.public.json` para o site:

```txt
concafras-ia/public/data/catalog.public.json
```

E consumir no React:

```ts
const response = await fetch('/data/catalog.public.json');
const catalog = await response.json();
```

Vantagem: simples e confiável.

Desvantagem: ainda exige copiar o arquivo quando atualizar.

### Opção B — consumir direto do GitHub Raw

Usar:

```txt
https://raw.githubusercontent.com/fulviofb/lab-midia-ia/master/public-data/catalog.public.json
```

Exemplo:

```ts
const response = await fetch(
  'https://raw.githubusercontent.com/fulviofb/lab-midia-ia/master/public-data/catalog.public.json'
);
const catalog = await response.json();
```

Vantagem: o site sempre lê o export publicado no repo.

Desvantagens:

- depende de rede/GitHub no runtime;
- pode haver cache;
- falhas de rede precisam de fallback.

### Opção C — buscar no build/deploy

No médio prazo, criar um script no repositório do site para baixar o JSON durante o build Vercel:

```bash
curl -L https://raw.githubusercontent.com/fulviofb/lab-midia-ia/master/public-data/catalog.public.json \
  -o public/data/catalog.public.json
```

Vantagem: site fica estático e rápido.

Desvantagem: precisa ajustar o build.

## Recomendação atual

Para a próxima etapa, usar a **Opção C**:

```txt
lab-midia-ia publica public-data/catalog.public.json
concafras-ia baixa esse JSON durante o build e renderiza seções amigáveis
```

Assim o `lab-midia-ia` continua sendo a base viva, e o site fica mais automático sem depender de fetch em runtime.

## Quando rodar

Rode o export sempre que alterar:

- `catalog.yml`;
- nomes/categorias/status/prioridades;
- textos públicos desejados;
- mapeamentos dentro de `scripts/export_public_catalog.py`.

Fluxo recomendado:

```bash
python scripts/update_github_metadata.py --write
python scripts/export_public_catalog.py
python scripts/export_public_catalog.py --check
git add catalog.yml public-data scripts docs
git commit -m "chore: update public catalog export"
```
