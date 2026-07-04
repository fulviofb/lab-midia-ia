# Teste: Remotion Agent Skills

Data: 2026-07-04
Issue: #4

## Objetivo

Validar as Remotion Agent Skills oficiais e um fluxo mínimo de vídeo programático em React no Windows.

## Ambiente

- OS: Windows com terminal bash/MSYS
- Node.js: 24.16.0
- npm/npx: 11.13.0
- FFmpeg/FFprobe: disponível, versão 8.1.2 full build
- Remotion: 4.0.484
- Template: `create-video@4.0.484 --blank --no-tailwind`

## API key ElevenLabs

Não foi usada neste teste. Para testes futuros de voz/transcrição, usar variável de ambiente local ou `.env` não commitado. Não colar chaves em issues nem no repositório.

## Instalação das skills

Comando executado:

```bash
npx --yes skills add remotion-dev/skills --all --full-depth
```

Resultado:

```txt
Found 1 skill
Installed: remotion-best-practices
Security: Med Risk
```

A skill instalada fica acessível no ambiente de agentes local e recomenda scaffold com:

```bash
npx create-video@latest --yes --blank --no-tailwind my-video
```

A skill também registra boas práticas importantes:

- animar com `useCurrentFrame()` e `interpolate()`;
- preferir `interpolate()` a `spring()` salvo necessidade física explícita;
- evitar CSS transitions/animations para animações de vídeo;
- usar `<Sequence>` para atrasos e recortes de tempo;
- configurar `durationInFrames`, `fps`, `width` e `height` em `src/Root.tsx`;
- usar `npx remotion still` para sanity-check de frame;
- usar `npx remotion render` para render final.

## Projeto de teste

Criado fora do repositório de curadoria:

```txt
C:\Users\fulvi\ai-media-tests\remotion-smoke-20260704\remotion-blank
```

Scaffold:

```bash
mkdir -p "$HOME/ai-media-tests/remotion-smoke-20260704"
cd "$HOME/ai-media-tests/remotion-smoke-20260704"
npx --yes create-video@4.0.484 --yes --blank --no-tailwind remotion-blank
cd remotion-blank
npm i
```

Observação: apesar de `--no-tailwind`, o template ainda trouxe `@remotion/tailwind-v4` e `tailwindcss` no `package.json`/config. Isso não bloqueou o teste.

## Dependências

`npm i` instalou 308 pacotes.

Resultado de auditoria exibido pelo npm:

```txt
2 low severity vulnerabilities
```

Não foi executado `npm audit fix --force`, pois isso poderia alterar versões e fugir do teste controlado.

## Composição criada

Arquivos editados:

```txt
src/Root.tsx
src/Composition.tsx
```

Configuração final:

```txt
Composition ID: MyComp
Duração: 180 frames
FPS: 30
Resolução: 1920×1080
Duração nominal: 6s
```

A composição é um motion graphic simples em português:

- fundo gradiente;
- grid;
- orbs animados;
- título: “React também vira vídeo”;
- subtítulo sobre Remotion;
- animações com `useCurrentFrame()` e `interpolate()`;
- sem CSS animations/transitions.

## Gates de validação

### Lint/typecheck

Comando:

```bash
npm run lint
```

Resultado:

```txt
eslint src && tsc
ok
```

### Still frame

Comando:

```bash
npx remotion still MyComp --frame=45 --output=out/frame-45.png --scale=0.5
```

Resultado:

```txt
out/frame-45.png
```

Na primeira execução, Remotion baixou automaticamente o Chrome Headless Shell:

```txt
Downloading Chrome Headless Shell https://www.remotion.dev/chrome-headless-shell
Got Headless Shell
```

Diferente do HyperFrames, o download/cache do browser funcionou sem workaround.

### Render MP4

Comando:

```bash
npx remotion render MyComp out/remotion-smoke.mp4 --codec=h264 --overwrite
```

Resultado:

```txt
out/remotion-smoke.mp4 864.7 kB
```

### FFprobe

Comando:

```bash
ffprobe -v error \
  -show_entries format=duration,size \
  -show_entries stream=index,codec_type,codec_name,width,height,r_frame_rate \
  -of json out/remotion-smoke.mp4
```

Resultado resumido:

```txt
Vídeo: H.264
Resolução: 1920×1080
FPS: 30/1
Áudio: AAC
Duração: 6.058667s
Tamanho: 864710 bytes
```

O stream AAC apareceu mesmo sem áudio explícito na composição. Isso parece comportamento padrão/aceitável do render neste template/configuração.

## Veredito

Status recomendado no catálogo:

```yaml
status: tested_recommended_windows
```

Remotion fica recomendado como pilar de vídeo programático quando o projeto se beneficia de React e componentes reutilizáveis.

## Remotion vs HyperFrames

Use **Remotion** quando:

- o time já usa React;
- você quer componentes reutilizáveis;
- o vídeo depende de lógica, props, dados ou composição em React;
- quer usar o ecossistema maduro do Remotion;
- quer gerar variações parametrizadas de vídeos.

Use **HyperFrames** quando:

- HTML/CSS/GSAP é suficiente e mais rápido;
- o agente vai montar a peça visual diretamente;
- o objetivo é motion graphic, card, site tour, UI demo ou vídeo web-like;
- você quer evitar estrutura React.

## Pendências futuras

- Criar exemplo vertical 9:16.
- Testar props/Zod para vídeo parametrizável.
- Testar áudio/voiceover em Remotion com ElevenLabs em issue separada.
- Testar render server/API se virar necessidade de produto.
- Revisar implicações da licença Remotion para uso comercial em organizações maiores.
