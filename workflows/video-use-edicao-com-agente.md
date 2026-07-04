# Workflow: edição de vídeo com agente usando video-use

Fonte: https://github.com/browser-use/video-use

## Quando usar

Use quando houver vídeos brutos e o objetivo for chegar a um `final.mp4` com ajuda de um agente.

Exemplos: aula gravada, entrevista, depoimento, vídeo de lançamento, tutorial, reels falados.

## Resultado esperado

- cortes de pausas e filler words;
- legendas queimadas;
- fades de áudio;
- color grading;
- overlays/animations quando fizer sentido;
- arquivo final em `edit/final.mp4`.

## Status do teste local

Primeiro teste parcial realizado no Windows: `uv sync`, `timeline_view.py`, `render.py` com EDL manual, transcript fake e `pack_transcripts.py` funcionaram. A transcrição real com ElevenLabs Scribe ainda não foi testada.

Atenção: `render.py --build-subtitles` gerou `master.srt`, mas falhou no Windows por escape de caminho absoluto no filtro FFmpeg `subtitles`. O mesmo SRT funcionou com workaround manual usando caminho relativo.

Relatório: `docs/testes/video-use-primeiro-teste.md`.

Workaround específico: `docs/workarounds/video-use-subtitles-windows.md`.

### Comando de workaround para Windows

Se `render.py --build-subtitles` gerar `master.srt`, mas falhar na composição por path Windows, entre na pasta `edit/` e aplique o SRT com caminho relativo:

```bash
cd "$HOME/ai-media-tests/video-use-sample/edit"

ffmpeg -y -i base_preview.mp4 \
  -vf "subtitles=master.srt:force_style='FontName=Arial,FontSize=18,Bold=1,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=2,Alignment=2,MarginV=90'" \
  -c:v libx264 -preset fast -crf 18 -pix_fmt yuv420p \
  -c:a copy -movflags +faststart final_subtitled_manual.mp4
```

## Pré-requisitos a validar

- Python;
- FFmpeg;
- agente com acesso ao shell;
- eventuais chaves de API para TTS/STT, se usadas;
- autorização para processar o material bruto.

## Prompt base

```text
Tenho uma pasta com vídeos brutos. Use video-use para transformar esse material em um vídeo final curto e bem editado.
Antes de editar, inventarie os arquivos, proponha uma estratégia de corte, duração final, estilo de legenda e trilha/ritmo.
Aguarde minha aprovação antes do render final.
```

## Critérios de qualidade

- cortes não podem parecer bruscos;
- áudio não pode estourar;
- legenda precisa estar legível no mobile;
- ritmo precisa combinar com o objetivo;
- `final.mp4` deve ser assistido/revisado antes de considerar concluído.
