# Teste: browser-use/video-use

Data: 2026-07-04
Issue: #2

## Objetivo

Validar um fluxo mínimo do `browser-use/video-use` no Windows antes de recomendar como workflow prático do Lab Mídia IA.

## Ambiente

- OS: Windows com terminal bash/MSYS
- Git: disponível
- GitHub CLI: disponível e autenticado
- Python: `python` 3.11.15; `python3` 3.13.14
- `uv`: disponível
- FFmpeg/FFprobe: disponível, versão 8.1.2 full build
- Node/npm/npx: disponível, Node 24.16.0
- Bun: não instalado

## Instalação testada

O repositório foi clonado fora do repo de curadoria, em pasta de testes:

```txt
C:\Users\fulvi\ai-media-tests\video-use
```

Commit testado:

```txt
92c2b34 Merge pull request #91 from ShawnPana/patch-1
```

Dependências instaladas com:

```bash
uv sync
```

Resultado: ambiente `.venv` criado e dependências instaladas com sucesso.

## Observações do install.md

O `install.md` define três requisitos principais:

1. repositório `video-use` clonado em caminho estável;
2. `ffmpeg`/`ffprobe` no PATH;
3. `ELEVENLABS_API_KEY` para transcrição via ElevenLabs Scribe.

A transcrição real **não foi testada** porque exige chave ElevenLabs e pode consumir créditos. O teste abaixo validou os helpers locais e o render a partir de um EDL manual.

## Vídeo sintético de teste

Foi criado um vídeo neutro, sem dados pessoais:

```txt
C:\Users\fulvi\ai-media-tests\video-use-sample\sample.mp4
```

Comando usado:

```bash
ffmpeg -y \
  -f lavfi -i "testsrc2=size=1280x720:rate=30:duration=12" \
  -f lavfi -i "sine=frequency=440:duration=12" \
  -c:v libx264 -preset veryfast -crf 23 -pix_fmt yuv420p \
  -c:a aac -b:a 128k -shortest sample.mp4
```

`ffprobe` confirmou:

- duração: 12s;
- vídeo H.264 1280×720 30fps;
- áudio AAC mono.

## Teste do timeline_view

Comando:

```bash
uv run --project "$HOME/ai-media-tests/video-use" \
  python "$HOME/ai-media-tests/video-use/helpers/timeline_view.py" \
  sample.mp4 0 4 -o edit/verify_sample_0-4.png --n-frames 6
```

Resultado:

```txt
edit/verify_sample_0-4.png
```

O helper gerou corretamente uma imagem de verificação com filmstrip/waveform.

## Teste do render.py com EDL manual

Foi criado um `edit/edl.json` manual, com dois cortes:

- 1s a 4s;
- 7s a 10s.

Comando:

```bash
uv run --project "$HOME/ai-media-tests/video-use" \
  python "$HOME/ai-media-tests/video-use/helpers/render.py" \
  edit/edl.json -o edit/final.mp4 --preview --no-subtitles
```

Resultado gerado:

```txt
edit/final.mp4
```

`ffprobe` confirmou:

- duração: 6.07s;
- vídeo H.264 1920×1080 24fps;
- áudio AAC;
- tamanho aproximado: 2.8 MB.

Arquivos gerados:

```txt
edit/base_preview.mp4
edit/clips_preview/seg_00_sample.mp4
edit/clips_preview/seg_01_sample.mp4
edit/edl.json
edit/final.mp4
edit/verify_sample_0-4.png
```

## Resultado

O teste local foi bem-sucedido para:

- instalar dependências com `uv sync`;
- gerar vídeo sintético;
- rodar `timeline_view.py`;
- rodar `render.py` com EDL manual;
- validar `final.mp4` com `ffprobe`.

## Limitações ainda não testadas

- Transcrição real com ElevenLabs Scribe.
- Geração de `takes_packed.md` a partir de transcrição.
- Seleção automática de cortes por agente baseada em transcript.
- Subtitles via `--build-subtitles`.
- Overlays via HyperFrames/Remotion/Manim.
- Registro como skill nativa no Hermes.

## Veredito parcial

Status recomendado no catálogo:

```yaml
status: partially_tested
```

O projeto é promissor e os helpers locais funcionaram no Windows. Para marcar como `tested_recommended`, ainda falta validar a transcrição ElevenLabs e um fluxo real com material falado.
