# Guia: Edição de vídeo com video-use

`browser-use/video-use` permite que agentes de IA editem vídeos brutos via código: cortar pausas, gerar legendas, aplicar fades, color grading e overlays.

## Quando usar

- editar vídeos falados (aulas, entrevistas, podcasts);
- cortar silêncios e filler words;
- gerar legendas automáticas;
- criar cortes para Reels/Shorts;
- aplicar fades e color grading;
- exportar `final.mp4` pronto para publicar.

## Pré-requisitos

Ver `docs/guias/00-pre-requisitos.md`.

Resumo mínimo:

- Python 3.11+
- `uv` (gerenciador Python)
- FFmpeg/FFprobe
- Node.js (para alguns helpers)

## Passo 1: Clonar e instalar

```bash
mkdir -p ~/ai-media-tests
cd ~/ai-media-tests
git clone https://github.com/browser-use/video-use.git
cd video-use
uv sync
```

Isso cria um `.venv` com todas as dependências.

## Passo 2: Configurar ElevenLabs (opcional)

Para transcrição real com timestamps precisos, o video-use usa ElevenLabs Scribe.

Crie um arquivo `.env` **não commitado** na pasta do video-use:

```txt
ELEVENLABS_API_KEY=sua_chave_aqui
```

> Nunca commite este arquivo. Nunca cole a chave em issues, chats ou repositórios.

Se não tiver a chave, é possível testar com transcript fake (ver `docs/testes/video-use-primeiro-teste.md`).

## Passo 3: Preparar pasta de trabalho

```bash
mkdir -p ~/ai-media-tests/video-use-sample/edit
cd ~/ai-media-tests/video-use-sample
```

Coloque seu vídeo bruto na pasta:

```txt
video-use-sample/
  sample.mp4       ← vídeo bruto
  edit/            ← saídas vão aqui
```

## Passo 4: Visualizar o vídeo

Gere uma imagem de visão geral para o agente entender o conteúdo:

```bash
VU="$HOME/ai-media-tests/video-use"

uv run --project "$VU" \
  python "$VU/helpers/timeline_view.py" \
  sample.mp4 0 6 -o edit/visao-geral.png --n-frames 6
```

Isso gera um PNG com frames do vídeo para análise visual.

## Passo 5: Transcrever (com ElevenLabs)

```bash
uv run --project "$VU" \
  python "$VU/helpers/transcribe.py" \
  sample.mp4 --edit-dir edit
```

Isso gera `edit/transcripts/sample.json` com timestamps de cada palavra.

## Passo 6: Empacotar transcrição

```bash
uv run --project "$VU" \
  python "$VU/helpers/pack_transcripts.py" \
  --edit-dir edit
```

Isso gera `edit/takes_packed.md` com frases e timestamps para o agente decidir cortes.

## Passo 7: Criar EDL

Crie `edit/edl.json` com os cortes desejados:

```json
{
  "segments": [
    {
      "source": "sample.mp4",
      "start": 1.0,
      "end": 4.5,
      "label": "introdução"
    },
    {
      "source": "sample.mp4",
      "start": 7.0,
      "end": 10.5,
      "label": "ponto principal"
    }
  ]
}
```

## Passo 8: Renderizar

### Sem legendas

```bash
uv run --project "$VU" \
  python "$VU/helpers/render.py" \
  edit/edl.json -o edit/final.mp4 --preview --no-subtitles
```

### Com legendas

```bash
uv run --project "$VU" \
  python "$VU/helpers/render.py" \
  edit/edl.json -o edit/final.mp4 --preview --build-subtitles
```

## Passo 9: Validar output

```bash
ffprobe -v error \
  -show_entries format=duration,size \
  -show_entries stream=index,codec_type,codec_name,width,height,r_frame_rate \
  -of json edit/final.mp4
```

## Problemas comuns no Windows

### `render.py --build-subtitles` falha

Sintoma: erro de path absoluto no filtro `subtitles` do FFmpeg.

Solução: usar caminho relativo a partir da pasta `edit/`:

```bash
cd edit
ffmpeg -y -i base_preview.mp4 \
  -vf "subtitles=master.srt:force_style='FontName=Arial,FontSize=18,Bold=1,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=2,Alignment=2,MarginV=90'" \
  -c:v libx264 -preset fast -crf 18 -pix_fmt yuv420p \
  -c:a copy -movflags +faststart final_subtitled.mp4
```

Ver detalhes: `docs/workarounds/video-use-subtitles-windows.md`

### `timeline_view.py` falha no frame final

Sintoma: erro ao extrair frame no limite exato da duração.

Solução: usar um `end` ligeiramente menor que a duração total.

## Fluxo completo

```txt
vídeo bruto
    ↓
timeline_view.py (visão geral)
    ↓
transcribe.py (transcrição com ElevenLabs)
    ↓
pack_transcripts.py (frases empacotadas)
    ↓
agente decide cortes → edl.json
    ↓
render.py (composição final)
    ↓
ffprobe (validação)
    ↓
final.mp4 pronto
```

## Sem ElevenLabs: transcript fake

Se não tem a chave ainda, crie um transcript fake compatível:

```txt
edit/transcripts/sample.json
```

Com entradas no formato Scribe:

```json
[
  {"type": "word", "text": "Olá", "start": 0.5, "end": 0.9, "speaker_id": "S0"},
  {"type": "spacing", "start": 0.9, "end": 1.0},
  {"type": "word", "text": "mundo", "start": 1.0, "end": 1.5, "speaker_id": "S0"}
]
```

Depois siga do Passo 6 em diante.

## Próximos passos

- Testar com vídeo real falado;
- Testar geração automática de EDL por agente baseado em `takes_packed.md`;
- Explorar color grading com `grade.py`;
- Criar overlays e animações.

## Referências

- Repo: https://github.com/browser-use/video-use
- Workflow detalhado: `workflows/video-use-edicao-com-agente.md`
- Teste local: `docs/testes/video-use-primeiro-teste.md`
- Workaround Windows: `docs/workarounds/video-use-subtitles-windows.md`
- Prompt pronto: `prompts/video-explicativo-narrado.md`
