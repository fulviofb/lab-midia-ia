# Guia: Como transformar ideia em roteiro, cenas e vídeo

Este guia mostra um fluxo completo para motion graphics e vídeos programáticos simples: da ideia inicial ao vídeo final renderizado.

Para projetos narrativos com personagens recorrentes, múltiplas gerações, bible visual e montagem provisória, use também:

- `docs/guias/08-planejamento-de-video-generativo.md`;
- `workflows/video-generativo-storyboard-first.md`.

## Fluxo geral

```txt
Ideia → Roteiro → Storyboard → Composição → Validação → Render → MP4
```

## Passo 1: Definir a ideia

Responda:

- **O que** você quer comunicar?
- **Para quem** é o vídeo? (público)
- **Qual** a mensagem central em uma frase?
- **Qual** a duração? (6s, 15s, 30s, 60s)
- **Qual** o formato? (16:9 horizontal, 9:16 vertical, 1:1 quadrado)
- **Qual** o tom? (institucional, educativo, promocional, tech, editorial)

## Passo 2: Roteiro

Escreva o roteiro em tópicos curtos. Exemplo:

```txt
Cena 1 (0-2s): Título aparece com fade in
Cena 2 (2-4s): Subtítulo explicativo
Cena 3 (4-6s): Chamada final / badge
```

Ou em formato narrado:

```txt
"Você sabia que HTML pode virar vídeo?
Com HyperFrames, agentes criam motion graphics diretamente em HTML/CSS.
Renderize em MP4 com um comando."
```

## Passo 3: Storyboard

Para cada cena, defina:

- **duração** (em segundos ou frames);
- **elementos visuais** (texto, formas, imagens);
- **animação** (fade, slide, scale, rotate);
- **cor de fundo** e **cores de destaque**;
- **posição** dos elementos.

Exemplo:

| Cena | Duração | Elemento | Animação | Cor |
|---|---|---|---|---|
| 1 | 0-2s | Título | fade in + slide up | cyan |
| 2 | 2-4s | Subtítulo | fade in | branco/muted |
| 3 | 4-6s | Badge | fade in + scale | branco com borda |

## Passo 4: Escolher a ferramenta

Use a árvore de decisão:

```txt
É motion graphic / peça visual?
  → HTML/CSS é natural? → HyperFrames
  → React é vantagem?   → Remotion

É edição de vídeo bruto?
  → video-use

É short automático?
  → MoneyPrinterTurbo (referência)
```

Ver: `docs/guias/01-por-onde-comecar.md`

## Passo 5: Criar a composição

### Se HyperFrames

1. Scaffold: `npx hyperframes init meu-video --non-interactive --example blank`
2. Editar `index.html` com a composição;
3. Definir `data-composition-id`, `data-duration`, `data-width`, `data-height`;
4. Criar elementos com `class="clip"`, `data-start`, `data-duration`, `data-track-index`;
5. Animar com GSAP timeline pausada em `window.__timelines["<id>"]`.

Ver guia: `docs/guias/02-primeiro-video-com-hyperframes.md`

### Se Remotion

1. Scaffold: `npx create-video@latest --yes --blank --no-tailwind meu-video`
2. Editar `src/Root.tsx` com `durationInFrames`, `fps`, `width`, `height`;
3. Editar `src/Composition.tsx` com a composição em React;
4. Animar com `useCurrentFrame()` e `interpolate()`;
5. Organizar cenas com `<Sequence>`.

Ver guia: `docs/guias/03-primeiro-video-com-remotion.md`

## Passo 6: Validar

### HyperFrames

```bash
npx hyperframes lint .
npx hyperframes validate .
npx hyperframes inspect .
npx hyperframes snapshot . --at 0,1.5,3,5.5
```

### Remotion

```bash
npm run lint
npx remotion still MyComp --frame=45 --output=out/frame.png --scale=0.5
```

## Passo 7: Renderizar

### HyperFrames

```bash
npx hyperframes render . --quality draft --strict --output renders/final.mp4
```

### Remotion

```bash
npx remotion render MyComp out/final.mp4 --codec=h264 --overwrite
```

## Passo 8: Validar output

```bash
ffprobe -v error \
  -show_entries format=duration,size \
  -show_entries stream=index,codec_type,codec_name,width,height,r_frame_rate \
  -of json renders/final.mp4
```

## Passo 9: Adicionar narração (opcional)

Se o vídeo tiver narração:

1. Gere o áudio com TTS (ver `docs/guias/05-narracao-com-ia-etica.md`);
2. Em Remotion, use `<Audio src={staticFile("narracao.mp3")} />`;
3. Em HyperFrames, adicione `<audio>` na composição;
4. Sincronize a animação com a narração.

## Passo 10: Iterar

- Revise o vídeo;
- Ajuste timings, cores, texto;
- Re-renderize;
- Repita até estar satisfeito.

## Checklist final

```txt
[ ] Roteiro definido
[ ] Storyboard pronto
[ ] Ferramenta escolhida
[ ] Composição criada
[ ] Lint passou
[ ] Snapshot/still validado
[ ] Render executado
[ ] ffprobe confirmou formato
[ ] Áudio sincronizado (se aplicável)
[ ] Vídeo final pronto
```

## Prompts prontos

- `prompts/video-explicativo-narrado.md`
- `prompts/video-ugc-anuncio-produto.md`
- `prompts/hyperframes-motion-graphic.md`
- `prompts/hyperframes-video-site.md`
- `prompts/remotion-video-programatico.md`

## Referências

- Guia de início: `docs/guias/01-por-onde-comecar.md`
- Pré-requisitos: `docs/guias/00-pre-requisitos.md`
- Ética e licenças: `docs/08-etica-licencas-privacidade.md`
