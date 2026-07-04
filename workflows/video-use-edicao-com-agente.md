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
