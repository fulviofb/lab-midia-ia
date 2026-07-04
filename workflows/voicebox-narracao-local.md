# Workflow: narração local com Voicebox

Fonte: https://github.com/jamiepine/voicebox

## Quando usar

Use Voicebox quando quiser:

- gerar narração/TTS localmente sem nuvem;
- clonar voz (com permissão) para uso em vídeos;
- integrar voz com agentes via MCP;
- ditado global (speech-to-text em qualquer app);
- produzir podcasts ou narrativas multi-voz;
- dar voz a agentes de IA.

## Pré-requisitos

- Windows: baixar e instalar o MSI (https://voicebox.sh/download/windows);
- macOS: baixar o DMG;
- Linux: Docker ou build from source;
- GPU recomendada mas não obrigatória (funciona em CPU, mais lento).

## Instalação

### Windows

1. Baixar: https://voicebox.sh/download/windows
2. Executar o MSI como administrador;
3. Abrir o app Voicebox;
4. Aguardar download de modelos na primeira execução;
5. O backend inicia automaticamente em `http://127.0.0.1:17493`.

### Docker

```bash
git clone https://github.com/jamiepine/voicebox.git
cd voicebox
docker compose up
```

## Criar um voice profile

### Opção A: Gravar direto no app

1. Abrir Voicebox;
2. Ir para Profiles;
3. Clicar em "Record";
4. Falar por 5-15 segundos;
5. Salvar o profile com um nome.

### Opção B: Importar arquivo de áudio

1. Abrir Voicebox;
2. Ir para Profiles;
3. Clicar em "Import";
4. Selecionar um arquivo .wav ou .mp3;
5. Salvar o profile.

> **Ética**: só clone vozes com permissão explícita. Ver `docs/guias/05-narracao-com-ia-etica.md`.

## Gerar speech

### Via interface

1. Selecionar um voice profile;
2. Digitar o texto;
3. Escolher o motor TTS (recomendado para iniciantes: Kokoro, leve e rápido);
4. Clicar em "Generate";
5. O áudio é gerado e salvo na aba History.

### Via API REST

```bash
# Listar profiles
curl http://127.0.0.1:17493/profiles

# Gerar speech
curl -X POST http://127.0.0.1:17493/generate \
  -H "Content-Type: application/json" \
  -d '{"text": "Olá, este é um teste.", "profile_id": "<id>", "language": "pt"}'
```

### Via MCP (para agentes)

Configurar no agente:

```bash
claude mcp add voicebox \
  --transport http \
  --url http://127.0.0.1:17493/mcp \
  --header "X-Voicebox-Client-Id: claude-code"
```

Usar no agente:

```ts
await voicebox.speak({
  text: "Teste concluído com sucesso.",
  profile: "Morgan",
});
```

## Escolher motor TTS

| Motor | Idiomas | Melhor para |
|---|---|---|
| Kokoro | 8 | Iniciantes, 82M, rápido em CPU |
| Qwen3-TTS | 10 | Qualidade multilíngue, delivery instructions |
| Qwen CustomVoice | 10 | Presets sem necessidade de amostra |
| LuxTTS | Inglês | Leve (~1GB VRAM), 48kHz |
| Chatterbox Multilingual | 23 | Maior cobertura de idiomas |
| Chatterbox Turbo | Inglês | Paralinguistic tags: [laugh], [sigh] |
| TADA | 10 | Áudio coerente longo (700s+) |

Recomendação para começar: **Kokoro** (mais leve e rápido) ou **Qwen3-TTS** (qualidade).

## Transcrição (STT)

Voicebox usa Whisper para speech-to-text:

```bash
# Transcrever arquivo
curl -X POST http://127.0.0.1:17493/transcribe \
  -F "audio=@gravacao.wav" \
  -F "model=whisper-turbo"
```

Modelos disponíveis: Base, Small, Medium, Large, Turbo.

## Integrar com vídeo

### Com Remotion

1. Gerar narração no Voicebox;
2. Exportar o áudio (.wav ou .mp3);
3. Colocar em `public/narracao.mp3` no projeto Remotion;
4. Adicionar ao componente:

```tsx
import { Audio } from "@remotion/media";
import { staticFile } from "remotion";

<Audio src={staticFile("narracao.mp3")} />
```

### Com HyperFrames

1. Gerar narração no Voicebox;
2. Exportar o áudio;
3. Referenciar na composição HTML:

```html
<audio src="narracao.mp3"></audio>
```

### Com video-use

1. Gerar narração no Voicebox;
2. Usar como track de áudio no `edl.json`;
3. Renderizar com `render.py`.

## Uso responsável

- Sempre peça permissão antes de clonar a voz de alguém;
- Divulgue que o áudio foi gerado por IA em conteúdo público;
- Não use para enganar, impersonar ou fraudar;
- Ver `docs/guias/05-narracao-com-ia-etica.md` e `docs/08-etica-licencas-privacidade.md`.

## Referências

- Repo: https://github.com/jamiepine/voicebox
- Site: https://voicebox.sh
- Docs: https://docs.voicebox.sh
- Teste local: `docs/testes/voicebox-primeiro-teste.md`
- Guia de narração ética: `docs/guias/05-narracao-com-ia-etica.md`
