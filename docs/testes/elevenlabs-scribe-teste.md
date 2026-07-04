# Teste: ElevenLabs Scribe com video-use

Data: 2026-07-04
Issue: #9

## Objetivo

Testar transcrição real com ElevenLabs Scribe no fluxo do `browser-use/video-use`.

## Ambiente

- Python 3.11+ com `uv`
- `video-use` clonado em `C:\Users\fulvi\ai-media-tests\video-use`
- `.env` configurado em `C:\Users\fulvi\ai-media-tests\video-use\.env` com `ELEVENLABS_API_KEY`
- FFmpeg com suporte a `flite` (TTS sintético)
- Vídeo de teste criado em `C:\Users\fulvi\ai-media-tests\video-use-elevenlabs-test\sample.mp4`

## Vídeo de teste criado

Para testar a transcrição, criei um vídeo com fala sintética usando `flite` (TTS do FFmpeg):

```bash
ffmpeg -y -f lavfi -i "flite=text='Hello, this is a test of the ElevenLabs Scribe transcription service...'" -t 20 speech_full.wav

ffmpeg -y \
  -f lavfi -i "color=c=#0a0a2a:s=1280x720:d=20:r=30" \
  -i speech_full.wav \
  -c:v libx264 -preset fast -pix_fmt yuv420p \
  -c:a aac -b:a 128k \
  -shortest -movflags +faststart \
  sample.mp4
```

Resultado:

```txt
sample.mp4
106 KB
duração: 15.461s
vídeo: H.264, 1280×720
áudio: AAC
```

## Tentativa de transcrição

Comando executado:

```bash
uv run --project "$HOME/ai-media-tests/video-use" \
  python "$HOME/ai-media-tests/video-use/helpers/transcribe.py" \
  sample.mp4 --edit-dir edit --language en
```

### O que funcionou

- O script `transcribe.py` carregou a API key do `.env` corretamente;
- O áudio foi extraído do vídeo com FFmpeg (`ffmpeg -vn -ac 1 -ar 16000 -c:a pcm_s16le`);
- O upload do WAV (0.5 MB) para a API foi feito;
- O script conectou na `https://api.elevenlabs.io/v1/speech-to-text`.

### O que falhou

O ElevenLabs retornou HTTP 401:

```json
{
  "detail": {
    "type": "authentication_error",
    "code": "unauthorized",
    "message": "The API key you used is missing the permission speech_to_text to execute this operation.",
    "status": "missing_permissions"
  }
}
```

## Análise da API key

Criei um script de diagnóstico (`check_elevenlabs.py`) que testou a key em dois endpoints:

1. **`GET /v1/user`** → HTTP 401: `missing permission user_read`
2. **`POST /v1/speech-to-text`** → HTTP 401: `missing permission speech_to_text`

A key tem 64 caracteres e formato válido, mas não tem permissões para:

- `user_read` — ler informações da conta;
- `speech_to_text` — usar o Scribe.

### Possíveis causas

1. **Plano Free/Starter**: o Scribe pode exigir um plano pago (Creator ou superior);
2. **Key com permissões restritas**: a key pode ter sido criada com escopo limitado;
3. **Scribe não incluído**: o plano pode não incluir speech-to-text.

### Como resolver

Para que o teste funcione, é necessário:

1. Verificar o plano da conta em https://elevenlabs.io/app/settings
2. Confirmar se o plano inclui **Speech-to-Text (Scribe)**
3. Se necessário, fazer upgrade para um plano que inclua Scribe
4. Ou criar uma nova API key com todas as permissões marcadas

Após obter uma key com permissão de `speech_to_text`, basta atualizar o `.env`:

```txt
ELEVENLABS_API_KEY=nova_chave_aqui
```

E rodar novamente:

```bash
cd ~/ai-media-tests/video-use-elevenlabs-test
uv run --project "$HOME/ai-media-tests/video-use" \
  python "$HOME/ai-media-tests/video-use/helpers/transcribe.py" \
  sample.mp4 --edit-dir edit --language en
```

## Status

O teste **não foi concluído** devido à limitação de permissões da API key.

O que foi validado:

- ✅ `.env` configurado corretamente;
- ✅ `transcribe.py` carrega a key do `.env`;
- ✅ FFmpeg extrai áudio do vídeo;
- ✅ Upload do áudio funciona;
- ✅ Script conecta na API do ElevenLabs;
- ❌ API key sem permissão `speech_to_text`.

## Descoberta importante: FFmpeg com flite

Durante o teste, descobrimos que o FFmpeg instalado na máquina tem suporte a `flite` (TTS sintético):

```bash
ffmpeg -f lavfi -i "flite=text='Hello world'" -t 10 speech.wav
```

Isso pode ser útil para gerar áudios de teste sem precisar de TTS externo.

## Veredito

O fluxo do `video-use` com ElevenLabs Scribe está tecnicamente pronto para uso, mas bloqueado pela permissão da API key. Quando uma key com permissão adequada estiver disponível, o teste pode ser re-executado com o mesmo vídeo e comandos.

## Referências

- Issue: https://github.com/fulviofb/lab-midia-ia/issues/9
- Teste anterior do video-use: `docs/testes/video-use-primeiro-teste.md`
- Workflow: `workflows/video-use-edicao-com-agente.md`
- Script de diagnóstico: `C:\Users\fulvi\ai-media-tests\check_elevenlabs.py`
