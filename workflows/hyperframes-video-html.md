# Workflow: vídeo programático com HyperFrames

Fonte: https://github.com/heygen-com/hyperframes

## Quando usar

Use HyperFrames quando você quiser transformar HTML/CSS/GSAP em vídeo MP4 de forma determinística e agent-friendly.

Bons casos:

- motion graphics curtos;
- title cards;
- vídeos explicativos visuais;
- vídeos a partir de website;
- animações de UI/produto;
- vídeos sociais com tipografia cinética;
- overlays e lower-thirds.

## Pré-requisitos

- Node.js 22+
- npm/npx ou bun
- FFmpeg/FFprobe
- Chrome/Chromium/headless shell disponível

No Windows testado, foi necessário apontar explicitamente para o Chrome do sistema:

```bash
export HYPERFRAMES_BROWSER_PATH='C:\Program Files\Google\Chrome\Application\chrome.exe'
export PRODUCER_HEADLESS_SHELL_PATH='C:\Program Files\Google\Chrome\Application\chrome.exe'
```

## Instalação de skills

```bash
npx skills add heygen-com/hyperframes --all
```

Ou, ao criar um projeto:

```bash
npx hyperframes init my-video --non-interactive --example blank
```

O `init` também verifica/instala as skills.

> Atenção: as skills rodam com permissões do agente. Revise antes de usar em ambientes sensíveis. No teste, o instalador mostrou avaliações de risco por skill.

## Scaffold mínimo

```bash
mkdir -p "$HOME/ai-media-tests/hyperframes-smoke"
cd "$HOME/ai-media-tests/hyperframes-smoke"
npx --yes hyperframes init hf-blank --non-interactive --example blank
cd hf-blank
```

## Gates obrigatórios

Depois de editar `index.html`:

```bash
npx --yes hyperframes@0.7.31 lint . --json > lint.json
npx --yes hyperframes@0.7.31 validate . --json > validate.json
npx --yes hyperframes@0.7.31 inspect . --json > inspect.json
```

Critério mínimo:

```txt
ok=true
errors=0
warnings=0
```

## Snapshot visual

```bash
npx --yes hyperframes@0.7.31 snapshot . --at 0,1.5,3,5.5
```

Isso gera PNGs e `contact-sheet.jpg` em `snapshots/`.

## Render

```bash
npx --yes hyperframes@0.7.31 render . \
  --quality draft \
  --strict \
  --output renders/hyperframes-smoke.mp4
```

Valide com:

```bash
ffprobe -v error \
  -show_entries format=duration,size \
  -show_entries stream=index,codec_type,codec_name,width,height,r_frame_rate \
  -of json renders/hyperframes-smoke.mp4
```

## Resultado do teste local

Relatório: `docs/testes/hyperframes-primeiro-teste.md`.

Status:

```yaml
status: tested_recommended_windows
```

O teste local no Windows gerou um MP4 de 6s, 1920×1080, 30fps, com render `--strict` aprovado.

## HyperFrames vs Remotion

Use **HyperFrames** quando:

- HTML/CSS é o caminho mais natural;
- o agente vai montar a composição diretamente;
- você quer evitar React/bundler;
- precisa de motion graphics, cards, overlays, site tour, UI animation.

Use **Remotion** quando:

- o projeto já é React;
- há componentes React reutilizáveis;
- a lógica do vídeo depende fortemente de estado/composição React;
- o time já conhece Remotion.
