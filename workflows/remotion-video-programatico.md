# Workflow: vídeo programático com Remotion

Fonte: https://www.remotion.dev/

Skill oficial: `remotion-dev/skills`, skill `remotion-best-practices`.

## Quando usar

Use Remotion quando você quiser criar vídeos com React, componentes reutilizáveis e timeline determinística.

Bons casos:

- vídeos parametrizados;
- variações em massa;
- motion graphics com dados;
- vídeos em produtos/SaaS;
- componentes React reaproveitados;
- render server/API;
- cenas com lógica mais complexa.

## Pré-requisitos

- Node.js
- npm/npx
- FFmpeg/FFprobe
- Chrome Headless Shell, baixado automaticamente pelo Remotion na primeira renderização

## Instalar Remotion Agent Skills

```bash
npx --yes skills add remotion-dev/skills --all --full-depth
```

No teste local, isso instalou a skill:

```txt
remotion-best-practices
```

Avaliação de segurança observada:

```txt
Med Risk
```

Revise skills antes de usar em ambientes sensíveis.

## Scaffold mínimo

```bash
mkdir -p "$HOME/ai-media-tests/remotion-smoke-20260704"
cd "$HOME/ai-media-tests/remotion-smoke-20260704"
npx --yes create-video@4.0.484 --yes --blank --no-tailwind remotion-blank
cd remotion-blank
npm i
```

## Criar composição

Arquivos principais:

```txt
src/Root.tsx
src/Composition.tsx
```

Em `Root.tsx`, defina:

```tsx
<Composition
  id="MyComp"
  component={MyComposition}
  durationInFrames={180}
  fps={30}
  width={1920}
  height={1080}
/>
```

Boas práticas da skill:

- animar com `useCurrentFrame()` e `interpolate()`;
- evitar CSS animations/transitions;
- usar `<Sequence>` para organizar tempo;
- usar assets em `public/` via `staticFile()`;
- renderizar um still antes do vídeo completo.

## Gates obrigatórios

```bash
npm run lint
```

Frame de validação:

```bash
npx remotion still MyComp --frame=45 --output=out/frame-45.png --scale=0.5
```

Render:

```bash
npx remotion render MyComp out/remotion-smoke.mp4 --codec=h264 --overwrite
```

Validação:

```bash
ffprobe -v error \
  -show_entries format=duration,size \
  -show_entries stream=index,codec_type,codec_name,width,height,r_frame_rate \
  -of json out/remotion-smoke.mp4
```

## Resultado do teste local

Relatório: `docs/testes/remotion-agent-skills-primeiro-teste.md`.

Status:

```yaml
status: tested_recommended_windows
```

O teste local gerou um MP4 H.264, 1920×1080, 30fps, duração ~6.06s.

## Remotion vs HyperFrames

Use **Remotion** quando:

- React é vantagem;
- haverá componentes reutilizáveis;
- o vídeo depende de props/dados/lógica;
- você quer variações parametrizadas;
- o projeto pode evoluir para render server/API.

Use **HyperFrames** quando:

- HTML/CSS/GSAP resolve mais rápido;
- o agente vai montar diretamente uma peça visual;
- o vídeo é motion graphic, site tour, card, UI demo ou peça web-like.
