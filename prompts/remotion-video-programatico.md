# Prompt: vídeo programático com Remotion

```text
Usando Remotion, crie um vídeo programático em React.

Tema:
[TEMA]

Mensagem central:
[MENSAGEM]

Duração:
[6s / 10s / 15s / 30s]

Formato:
[1920x1080 / 1080x1920 / 1080x1080]

Estilo visual:
[ex.: tecnológico escuro, institucional limpo, educativo, editorial, produto SaaS]

Regras técnicas:
- usar Remotion;
- criar/editar `src/Root.tsx` e `src/Composition.tsx`;
- definir `durationInFrames`, `fps`, `width`, `height` no `<Composition>`;
- animar com `useCurrentFrame()` e `interpolate()`;
- preferir `interpolate()` a `spring()` salvo se a física for necessária;
- usar `<Sequence>` para organizar cenas no tempo;
- evitar CSS transitions, CSS animations e Tailwind animation classes;
- colocar assets locais em `public/` e referenciar com `staticFile()`;
- rodar `npm run lint`;
- gerar um still de sanity-check com `npx remotion still`;
- renderizar com `npx remotion render`;
- validar o MP4 com `ffprobe`.

Entregáveis:
- composição Remotion funcional;
- still de validação;
- `out/final.mp4`;
- resumo com duração, resolução, fps e comandos usados.
```
