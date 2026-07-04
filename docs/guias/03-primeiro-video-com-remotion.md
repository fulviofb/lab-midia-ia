# Guia: Primeiro vídeo com Remotion

Remotion cria vídeos programáticos em React com timeline determinística. Este guia mostra como criar seu primeiro vídeo do zero.

## Quando usar Remotion

- vídeos parametrizados;
- variações em massa;
- motion graphics com dados;
- vídeos em produtos/SaaS;
- componentes React reaproveitados;
- cenas com lógica mais complexa;
- render server/API.

## Pré-requisitos

Ver `docs/guias/00-pre-requisitos.md`.

Resumo mínimo:

- Node.js 22+
- npm/npx
- FFmpeg/FFprobe

Diferente do HyperFrames, Remotion baixa o Chrome Headless Shell automaticamente na primeira renderização.

## Passo 1: Instalar skills

```bash
npx --yes skills add remotion-dev/skills --all --full-depth
```

Isso instala a skill `remotion-best-practices`.

## Passo 2: Criar projeto

```bash
mkdir -p ~/ai-media-tests/remotion-smoke
cd ~/ai-media-tests/remotion-smoke
npx --yes create-video@latest --yes --blank --no-tailwind meu-video
cd meu-video
npm i
```

## Passo 3: Entender a estrutura

```txt
src/
  Root.tsx          ← define composições (id, fps, dimensões, duração)
  Composition.tsx   ← componente do vídeo
  index.ts          ← entry point
  index.css         ← estilos globais
remotion.config.ts  ← configuração do Remotion
package.json
```

## Passo 4: Configurar a composição

Em `src/Root.tsx`:

```tsx
import { Composition } from "remotion";
import { MyComposition } from "./Composition";

export const RemotionRoot: React.FC = () => {
  return (
    <Composition
      id="MyComp"
      component={MyComposition}
      durationInFrames={180}
      fps={30}
      width={1920}
      height={1080}
    />
  );
};
```

- `durationInFrames`: duração total em frames (180 frames ÷ 30 fps = 6 segundos);
- `fps`: frames por segundo;
- `width` e `height`: resolução.

## Passo 5: Criar o componente

Em `src/Composition.tsx`, use `useCurrentFrame()` e `interpolate()`:

```tsx
import { AbsoluteFill, useCurrentFrame, interpolate, Easing } from "remotion";

export const MyComposition = () => {
  const frame = useCurrentFrame();

  const opacity = interpolate(frame, [0, 30], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
    easing: Easing.bezier(0.16, 1, 0.3, 1),
  });

  return (
    <AbsoluteFill style={{ backgroundColor: "#050816" }}>
      <div style={{ opacity, color: "#f8fafc", fontSize: 80, textAlign: "center" }}>
        Olá, Remotion!
      </div>
    </AbsoluteFill>
  );
};
```

### Boas práticas da skill oficial

- animar com `useCurrentFrame()` e `interpolate()`;
- preferir `interpolate()` a `spring()` salvo necessidade física;
- usar `Easing.bezier()` para personalizar curvas;
- manter `interpolate()` inline no `style` para permitir edição no Studio;
- usar propriedades individuais (`scale`, `translate`, `rotate`) em vez de `transform`;
- CSS transitions e animations são **proibidos**;
- Tailwind animation classes são **proibidas**;
- assets em `public/` referenciados com `staticFile()`.

## Passo 6: Organizar cenas com Sequence

```tsx
import { AbsoluteFill, Sequence } from "remotion";

export const MyComposition = () => {
  return (
    <AbsoluteFill style={{ backgroundColor: "#050816" }}>
      <Sequence>
        <Background />
      </Sequence>
      <Sequence from={30} durationInFrames={60}>
        <Title />
      </Sequence>
      <Sequence from={90} durationInFrames={60}>
        <Subtitle />
      </Sequence>
    </AbsoluteFill>
  );
};
```

- `from`: frame de início;
- `durationInFrames`: duração em frames;
- `layout="none"` para conteúdo inline.

## Passo 7: Lint

```bash
npm run lint
```

Isso roda ESLint + TypeScript. Se passar, pode renderizar.

## Passo 8: Still de validação

```bash
npx remotion still MyComp --frame=45 --output=out/frame-45.png --scale=0.5
```

Na primeira execução, Remotion baixa o Chrome Headless Shell automaticamente.

## Passo 9: Renderizar

```bash
npx remotion render MyComp out/meu-video.mp4 --codec=h264 --overwrite
```

## Passo 10: Validar output

```bash
ffprobe -v error \
  -show_entries format=duration,size \
  -show_entries stream=index,codec_type,codec_name,width,height,r_frame_rate \
  -of json out/meu-video.mp4
```

## Adicionando áudio

```tsx
import { Audio } from "@remotion/media";
import { staticFile } from "remotion";

export const MyComposition = () => {
  return (
    <AbsoluteFill>
      <Audio src={staticFile("narracao.mp3")} />
    </AbsoluteFill>
  );
};
```

Coloque o arquivo em `public/narracao.mp3`.

## Adicionando vídeo

```tsx
import { Video } from "@remotion/media";
import { staticFile } from "remotion";

export const MyComposition = () => {
  return (
    <AbsoluteFill>
      <Video src={staticFile("footage.mp4")} style={{ opacity: 0.5 }} />
    </AbsoluteFill>
  );
};
```

## Licença

Remotion usa licença especial:

- indivíduos e pequenas empresas podem usar gratuitamente;
- empresas maiores/for-profit podem precisar de licença comercial;
- verificar: https://remotion.dev/license

## Remotion vs HyperFrames

| Critério | HyperFrames | Remotion |
|---|---|---|
| Linguagem | HTML/CSS/GSAP | React |
| Melhor quando | HTML direto, agente monta peça | React, componentes, props |
| Curva de aprendizado | menor | média |
| Chrome no Windows | precisa de workaround | funciona automático |
| Licença | Apache-2.0 | especial |

## Próximos passos

- Testar formato vertical 9:16 (mudar `width`/`height`);
- Adicionar props com Zod para vídeo parametrizável;
- Adicionar áudio/voiceover;
- Explorar templates: `Hello World`, `Audiogram`, `Music Visualization`;
- Estudar render server se precisar gerar vídeos sob demanda.

## Referências

- Docs: https://www.remotion.dev/docs
- Workflow detalhado: `workflows/remotion-video-programatico.md`
- Teste local: `docs/testes/remotion-agent-skills-primeiro-teste.md`
- Prompt pronto: `prompts/remotion-video-programatico.md`
