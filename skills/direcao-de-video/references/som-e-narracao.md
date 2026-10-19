# Som e narração

## Som

- Cue list lida da mesma timeline dos eventos visuais:
  ```
  TOQUE NO BOTÃO   frame 195  transiente de clique
  RESULTADO        frame 210  acento de revelação
  HOLD FINAL       frame 438  música assenta
  ```
- Hit **1 frame depois** do evento visual. Em arquivo com entrada suave, ache o pico real no waveform e desloque o clipe.
- Hits 3–6 dB acima da base. Um riser e um impacto por peça. Tudo tonal na mesma tonalidade. Efeitos e música em
  trilhas separadas.
- Celular quase não reproduz abaixo de ~150 Hz: confira a banda 200 Hz–6 kHz. Ouça no fone e no alto-falante do celular.
- Master ~−14 LUFS (−16 em peças calmas). Limite o WAV a −2,2 dBTP (o AAC sobe o pico); o MP4 final ≤ −1 dBTP.
  Medir: `ffmpeg -i out.mp4 -af loudnorm=print_format=summary -f null -`
- Loop: o AAC adiciona ~16 ms de padding; fade raised-cosine de 2 ms nas pontas.
- Origem do áudio (TTS, SFX, trilha): `/media-use`. Mixagem, fades, ducking: `/hyperframes-audio`.

## Narração: a voz vem primeiro

Animar antes e encaixar a voz depois sempre sai fora de tempo.

1. Roteiro aprovado em frases curtas, uma ideia por frase.
2. Voz em WAV 48 kHz: voz própria (melhor para institucional), TTS local, ou TTS pago já em uso.
   Voz clonada só com consentimento escrito; nunca de menores.
3. `npx hyperframes transcribe` → tempos por palavra. Conferir nomes próprios e números.
4. Cada evento visual no tempo da palavra que o motiva (a barra sobe em "progresso").
   Duração = fim da última frase + hold da assinatura.
5. Mixagem: a voz manda; trilha 8–12 dB abaixo sob a fala; SFX só em eventos fortes, sem cobrir sílabas.
6. Legenda sempre (a maioria assiste sem som); karaokê opcional pelos mesmos tempos.
7. Os textos-chave continuam legíveis sem o áudio.
