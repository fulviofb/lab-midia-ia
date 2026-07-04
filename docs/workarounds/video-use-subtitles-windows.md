# Workaround Windows: subtitles no `browser-use/video-use`

Issue relacionada: #8

## Resumo

No teste local do `browser-use/video-use` no Windows, o comando:

```bash
uv run --project "$HOME/ai-media-tests/video-use" \
  python "$HOME/ai-media-tests/video-use/helpers/render.py" \
  edit/edl.json -o edit/final_subtitled.mp4 --preview --build-subtitles
```

conseguiu gerar o arquivo:

```txt
edit/master.srt
```

mas falhou na etapa de composição final com FFmpeg quando o filtro `subtitles` recebeu o caminho absoluto Windows do SRT.

## Sintoma

Erro observado, resumido:

```txt
subprocess.CalledProcessError ...
-filter_complex "[0:v]subtitles='C\\:\\Users\\...\\master.srt':force_style='...'[outv]"
```

O problema não é o `master.srt` em si. O mesmo arquivo funcionou quando aplicado com caminho relativo a partir da pasta `edit/`.

## Causa provável

O filtro `subtitles` do FFmpeg/libass é sensível ao escape de caminhos Windows, especialmente por causa de:

- letra de drive, como `C:`;
- barras invertidas `\`;
- combinação de aspas, dois-pontos e `filter_complex`.

O `render.py` resolve o caminho absoluto e tenta escapar `:`:

```python
subs_abs = str(subtitles_path.resolve()).replace(":", r"\:").replace("'", r"\'")
```

No ambiente testado, isso ainda falhou.

## Workaround validado

A partir da pasta `edit/`, aplique o SRT usando caminho relativo:

```bash
cd "$HOME/ai-media-tests/video-use-sample/edit"

ffmpeg -y -i base_preview.mp4 \
  -vf "subtitles=master.srt:force_style='FontName=Arial,FontSize=18,Bold=1,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=1,Outline=2,Alignment=2,MarginV=90'" \
  -c:v libx264 -preset fast -crf 18 -pix_fmt yuv420p \
  -c:a copy -movflags +faststart final_subtitled_manual.mp4
```

## Resultado validado

`ffprobe` confirmou:

```txt
arquivo: final_subtitled_manual.mp4
duração: 6.04s
vídeo: H.264, 1920x1080, 24fps
áudio: AAC
tamanho: ~3.85 MB
```

Também foi gerado PNG de verificação:

```txt
edit/verify_final_subtitled_manual_0-5_8.png
```

## Procedimento recomendado para Windows

Quando `render.py --build-subtitles` falhar na composição:

1. Rode o `render.py` mesmo assim para gerar:

   ```txt
   edit/base_preview.mp4
   edit/master.srt
   ```

2. Entre na pasta `edit/`.
3. Aplique o `master.srt` com caminho relativo usando o comando acima.
4. Valide com:

   ```bash
   ffprobe -v error \
     -show_entries format=duration,size \
     -show_entries stream=index,codec_type,codec_name,width,height,r_frame_rate \
     -of json final_subtitled_manual.mp4
   ```

## Observação sobre `timeline_view.py`

No mesmo teste, `timeline_view.py` falhou ao tentar extrair frame exatamente no limite final do vídeo:

```bash
timeline_view.py final_subtitled_manual.mp4 0 6
```

Funcionou usando uma pequena margem:

```bash
timeline_view.py final_subtitled_manual.mp4 0 5.8
```

Regra prática no Windows/FFmpeg: ao gerar filmstrip de verificação, use `end = duration - 0.2s` para evitar erro no frame final.

## Possível correção upstream

Uma correção no `render.py` poderia evitar path absoluto Windows no filtro `subtitles` quando possível:

- executar o FFmpeg com `cwd=edit_dir`;
- passar `subtitles=master.srt` quando o SRT está dentro de `edit_dir`;
- ou converter o path para formato aceito pelo FFmpeg/libass no Windows, validando com testes.

Pseudo-abordagem:

```python
if subtitles_path.parent.resolve() == edit_dir.resolve():
    subs_filter_path = subtitles_path.name
else:
    subs_filter_path = escape_ffmpeg_subtitles_path(subtitles_path)
```

E chamar `subprocess.run(..., cwd=edit_dir)` quando usar caminho relativo.

## Status

Workaround documentado e validado no Windows.
