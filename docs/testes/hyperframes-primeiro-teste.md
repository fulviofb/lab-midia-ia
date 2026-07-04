# Teste: HyperFrames

Data: 2026-07-04
Issue: #3

## Objetivo

Validar `heygen-com/hyperframes` como ferramenta agent-friendly para criar vídeo programático a partir de HTML/CSS/GSAP no Windows.

## Ambiente

- OS: Windows com terminal bash/MSYS
- Node.js: 24.16.0
- npm/npx: 11.13.0
- FFmpeg/FFprobe: disponível, versão 8.1.2 full build
- Browser do sistema: Google Chrome instalado em `C:\Program Files\Google\Chrome\Application\chrome.exe`
- HyperFrames CLI testado: `0.7.31`

## Instalação / skills

O comando de scaffold executado foi:

```bash
npx --yes hyperframes init hf-blank --non-interactive --example blank
```

Durante o `init`, o HyperFrames verificou e instalou automaticamente as 21 skills em diretórios de agentes:

```txt
~\.claude\skills\...
~\.agents\skills\...
```

A verificação posterior confirmou:

```txt
missing: 0
outdated: 0
skills: 21
```

A instalação incluiu, entre outras:

- `hyperframes`
- `hyperframes-core`
- `hyperframes-animation`
- `hyperframes-cli`
- `motion-graphics`
- `product-launch-video`
- `website-to-video`
- `faceless-explainer`
- `embedded-captions`
- `talking-head-recut`
- `pr-to-video`
- `remotion-to-hyperframes`

O instalador também mostrou avisos de risco de segurança por skill. Destaque observado: `pr-to-video` apareceu como `Critical Risk` no Snyk. Isso não bloqueou o teste, mas deve ser mencionado em guias de uso: revisar skills antes de usar, pois rodam com permissões do agente.

## Projeto de teste

Criado fora do repositório de curadoria:

```txt
C:\Users\fulvi\ai-media-tests\hyperframes-smoke\hf-blank
```

Arquivos scaffoldados:

```txt
AGENTS.md
CLAUDE.md
hyperframes.json
index.html
meta.json
package.json
```

O `index.html` foi substituído por uma composição simples de 6 segundos, 1920×1080, com:

- fundo gradiente;
- grid;
- orbs animados;
- título em português;
- subtítulo;
- badge informativo;
- timeline GSAP pausada registrada em `window.__timelines["main"]`.

## Problema encontrado: Chrome headless cache quebrado

`npx hyperframes doctor --json` indicou:

```txt
Chrome: false
Docker: false
Docker running: false
```

Ao tentar `hyperframes browser ensure`, o CLI encontrou uma pasta de cache existente, mas sem o executável:

```txt
C:\Users\fulvi\.cache\hyperframes\chrome\chrome-headless-shell\win64-131.0.6778.85\...
```

Erro resumido:

```txt
Cached Chrome binary was missing ... and re-download failed
Run `hyperframes browser ensure --force` to re-download.
```

Mesmo com `--force`, o erro persistiu.

## Workaround validado para Windows

Definir explicitamente o Chrome do sistema antes de validar/renderizar:

```bash
export HYPERFRAMES_BROWSER_PATH='C:\Program Files\Google\Chrome\Application\chrome.exe'
export PRODUCER_HEADLESS_SHELL_PATH='C:\Program Files\Google\Chrome\Application\chrome.exe'
```

Com essas variáveis, o CLI usou o browser com origem `env` e os comandos funcionaram.

## Gates de validação

Comandos executados:

```bash
npx --yes hyperframes@0.7.31 lint . --json > lint.json
npx --yes hyperframes@0.7.31 validate . --json > validate.json
npx --yes hyperframes@0.7.31 inspect . --json > inspect.json
```

Resultado final após ajuste da timeline GSAP:

```txt
lint.json     ok=true, errors=0, warnings=0
validate.json ok=true, errors=0, warnings=0
inspect.json  ok=true, errors=0, warnings=0
```

## Snapshot

Comando:

```bash
npx --yes hyperframes@0.7.31 snapshot . --at 0,1.5,3,5.5
```

Resultado:

```txt
snapshots/frame-00-at-0.0s.png
snapshots/frame-01-at-1.5s.png
snapshots/frame-02-at-3.0s.png
snapshots/frame-03-at-5.5s.png
snapshots/frame-04-at-5.8s.png
snapshots/contact-sheet.jpg
```

Observação: o CLI adicionou automaticamente um frame no fim da timeline, em `5.8s`.

## Render

Comando final:

```bash
npx --yes hyperframes@0.7.31 render . \
  --quality draft \
  --strict \
  --output renders/hyperframes-smoke.mp4
```

Resultado:

```txt
renders/hyperframes-smoke.mp4
907.6 KB · 6.0s video · rendered in 12.0s
```

`ffprobe` confirmou:

```txt
Duração: 6.000000s
Vídeo: H.264
Resolução: 1920×1080
FPS: 30/1
Tamanho: 929398 bytes
```

## Observações do render

- O render local funcionou em modo screenshot no Windows.
- O CLI detectou GPU via browser do sistema:

```txt
browserGpuMode auto → hardware
ANGLE / Intel UHD Graphics / Direct3D11
```

- Houve log não bloqueante:

```txt
[non-blocking] Failed to load resource: 404
```

Não impediu `validate`, `inspect` ou `render --strict`.

## Feedback enviado ao projeto upstream

Após render bem-sucedido, foi enviado feedback via CLI:

```bash
npx --yes hyperframes@0.7.31 feedback --rating 4 --comment "..."
```

Comentário resumido: smoke test Windows funcionou usando `HYPERFRAMES_BROWSER_PATH` e `PRODUCER_HEADLESS_SHELL_PATH`; `browser ensure` falhou por cache quebrado; lint/validate/inspect/render passaram com browser via env.

## Veredito

Status recomendado no catálogo:

```yaml
status: tested_recommended_windows
```

HyperFrames é recomendado como pilar de vídeo programático do laboratório, especialmente quando o objetivo é criar vídeo a partir de HTML/CSS/animações com agentes.

## Quando usar HyperFrames vs Remotion

Use HyperFrames quando:

- o agente vai criar HTML/CSS diretamente;
- o vídeo é motion graphic, title card, site tour, pitch visual, social clip ou composição web-like;
- você quer evitar projeto React/bundler;
- precisa de render determinístico local com CLI simples;
- quer instalar skills agent-friendly com workflows prontos.

Use Remotion quando:

- o time já usa React;
- há componentes React reutilizáveis;
- o vídeo depende fortemente de lógica/composição em React;
- você quer usar o ecossistema maduro do Remotion.

## Pendências futuras

- Testar `hyperframes add` com blocos de catálogo, ex. `data-chart`.
- Testar workflow `/website-to-video` com uma página real.
- Testar render vertical 9:16.
- Criar exemplo versionado dentro do `lab-midia-ia` ou manter apenas documentação/link para pasta de teste.
- Documentar workaround permanente para cache quebrado do Chrome headless no Windows, se recorrente.
