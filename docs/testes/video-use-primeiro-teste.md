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

## Teste adicional sem API: transcript fake e legendas

Para evitar consumo de créditos ElevenLabs, foi criado um transcript fake compatível com o formato esperado pelo Scribe:

```txt
edit/transcripts/sample.json
```

O transcript contém entradas `word` com `start`, `end`, `speaker_id` e entradas `spacing` para simular pausas.

### `pack_transcripts.py`

Comando:

```bash
uv run --project "$HOME/ai-media-tests/video-use" \
  python "$HOME/ai-media-tests/video-use/helpers/pack_transcripts.py" \
  --edit-dir edit
```

Resultado:

```txt
edit/takes_packed.md
```

Saída confirmada:

```txt
packed 1 transcripts → .../edit/takes_packed.md
4 phrases, 8.9s total runtime
```

Conteúdo gerado:

```txt
## sample  (duration: 8.9s, 4 phrases)
  [001.10-002.80] S0 Teste do Lab Mídia IA.
  [003.45-004.00] S0 Render validado.
  [007.10-008.72] S0 Segundo trecho com legendas.
  [009.30-010.00] S0 Fim do teste.
```

### `render.py --build-subtitles`

Comando tentado:

```bash
uv run --project "$HOME/ai-media-tests/video-use" \
  python "$HOME/ai-media-tests/video-use/helpers/render.py" \
  edit/edl.json -o edit/final_subtitled.mp4 --preview --build-subtitles
```

Resultado parcial:

- `master.srt` foi gerado corretamente com 8 cues;
- a composição com subtitles falhou no Windows ao usar caminho absoluto no filtro `subtitles` do FFmpeg.

Erro observado:

```txt
subprocess.CalledProcessError ... filter_complex "[0:v]subtitles='C\\:\\Users\\...\\master.srt'..."
```

Hipótese: bug de escape de path Windows em `render.py` ao passar `subtitles_path.resolve()` para o filtro `subtitles`. O FFmpeg funcionou quando o mesmo SRT foi aplicado com caminho relativo a partir do diretório `edit/`.

### Workaround validado

A partir de `edit/`, este comando funcionou:

```bash
ffmpeg -y -i base_preview.mp4 \
  -vf "subtitles=master.srt:force_style='FontName=Arial,FontSize=18,Bold=1,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=2,Alignment=2,MarginV=90'" \
  -c:v libx264 -preset fast -crf 18 -pix_fmt yuv420p \
  -c:a copy -movflags +faststart final_subtitled_manual.mp4
```

`ffprobe` confirmou:

- duração: 6.04s;
- vídeo H.264 1920×1080 24fps;
- áudio AAC;
- tamanho: ~3.85 MB.

Também foi gerado um PNG de verificação:

```txt
edit/verify_final_subtitled_manual_0-5_8.png
```

Observação: `timeline_view.py` falhou quando solicitado exatamente até `end=6.0`, mas funcionou com `end=5.8`. Possível fragilidade ao extrair frame no limite final do vídeo no Windows/FFmpeg.

## Limitações ainda não testadas

- Transcrição real com ElevenLabs Scribe.
- Seleção automática de cortes por agente baseada em transcript real.
- Overlays via HyperFrames/Remotion/Manim.
- Registro como skill nativa no Hermes.

## Bugs/fragilidades encontrados no Windows

1. `render.py --build-subtitles` gera `master.srt`, mas falha na composição por escape de caminho absoluto Windows no filtro FFmpeg `subtitles`.
2. `timeline_view.py` pode falhar ao extrair frame exatamente no limite final do vídeo; usar margem, ex. `end=duration-0.2`, funcionou.

## Veredito parcial

Status recomendado no catálogo:

```yaml
status: partially_tested_windows
```

O projeto é promissor e os helpers locais funcionaram no Windows para render sem legenda, transcript fake, `takes_packed.md` e legenda via workaround manual. Para marcar como `tested_recommended`, ainda falta validar a transcrição ElevenLabs, um fluxo real com material falado e corrigir/contornar o bug de path Windows em `render.py --build-subtitles`.
