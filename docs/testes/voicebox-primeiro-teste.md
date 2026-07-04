# Teste: Voicebox

Data: 2026-07-04
Issue: #5

## Objetivo

Validar `jamiepine/voicebox` como pilar local-first para voz, TTS, clonagem e ditado no Windows.

## O que é Voicebox

Voicebox é um **app desktop** (Tauri/Rust + Python FastAPI backend), não um CLI. É uma alternativa open-source a ElevenLabs (output) e WisprFlow (input) em um só app, rodando localmente.

### Características principais

- **7 motores TTS**: Qwen3-TTS, Qwen CustomVoice, LuxTTS, Chatterbox Multilingual, Chatterbox Turbo, HumeAI TADA, Kokoro
- **23 idiomas**
- **Clonagem de voz** zero-shot a partir de amostra curta
- **50+ vozes preset** (Kokoro e Qwen CustomVoice)
- **Dictação global** com hotkey (push-to-talk e toggle)
- **Whisper STT** para transcrição
- **MCP server** integrado — agentes podem falar via `voicebox.speak`
- **REST API** em `http://127.0.0.1:17493`
- **Local LLM** (Qwen3 0.6B/1.7B/4B) para refinamento e personalidade
- **Efeitos de áudio**: pitch shift, reverb, delay, chorus, compressor, filtros
- **Stories editor**: timeline multi-track para conversas/podcasts
- **Captures tab**: histórico de ditados e áudios

### Suporte de GPU

| Plataforma | Backend | Notas |
|---|---|---|
| macOS (Apple Silicon) | MLX (Metal) | 4-5x mais rápido via Neural Engine |
| Windows / Linux (NVIDIA) | PyTorch (CUDA) | Auto-download do binário CUDA |
| Linux (AMD) | PyTorch (ROCm) | Auto-configura HSA_OVERRIDE |
| Windows (qualquer GPU) | DirectML | Suporte universal Windows GPU |
| Intel Arc | IPEX/XPU | Intel discrete GPU |
| Any | CPU | Funciona em qualquer lugar, mais lento |

## Ambiente testado

- OS: Windows
- Clone do repo em `C:\Users\fulvi\ai-media-tests\voicebox`
- Versão analisada: v0.5.0 (release mais recente)
- Licença: MIT
- Estrelas: 37.661

## Instalação

### Opção A: App desktop (recomendada)

Baixar o instalador MSI:

```txt
https://voicebox.sh/download/windows
```

Ou diretamente do GitHub Releases:

```txt
https://github.com/jamiepine/voicebox/releases/latest
```

Arquivo: `Voicebox_0.5.0_x64_en-US.msi` (~517 MB)

Passos:

1. Baixar o MSI;
2. Executar como administrador;
3. Abrir o app Voicebox;
4. Na primeira execução, o app baixa modelos automaticamente do HuggingFace;
5. O backend FastAPI inicia automaticamente em `http://127.0.0.1:17493`.

### Opção B: Docker

```bash
git clone https://github.com/jamiepine/voicebox.git
cd voicebox
docker compose up
```

### Opção C: Build from source

Pré-requisitos: Bun, Rust, Python 3.11+, Tauri prerequisites.

```bash
git clone https://github.com/jamiepine/voicebox.git
cd voicebox
just setup
just dev
```

No Windows, instalar [just](https://github.com/casey/just) primeiro.

## API REST

Voicebox expõe uma API REST completa em `http://127.0.0.1:17493` quando o app está rodando.

### Endpoints principais

```bash
# Health check
curl http://127.0.0.1:17493/health

# Listar perfis de voz
curl http://127.0.0.1:17493/profiles

# Gerar speech
curl -X POST http://127.0.0.1:17493/generate \
  -H "Content-Type: application/json" \
  -d '{"text": "Olá, mundo!", "profile_id": "...", "language": "pt"}'

# Falar (para agentes/scripts)
curl -X POST http://127.0.0.1:17493/speak \
  -H "Content-Type: application/json" \
  -H "X-Voicebox-Client-Id: my-script" \
  -d '{"text": "Deploy completo.", "profile": "Morgan"}'

# Transcrever áudio
curl -X POST http://127.0.0.1:17493/transcribe \
  -F "audio=@recording.wav" \
  -F "model=whisper-turbo"
```

### Documentação interativa

Quando o app está rodando:

```txt
http://127.0.0.1:17493/docs
```

90 endpoints organizados por domínio: profiles, generation, history, transcription, stories, effects, audio, models, tasks, cuda.

## MCP Server

Voicebox inclui um servidor MCP (Model Context Protocol) para integração com agentes.

### Configurar no Claude Code

```bash
claude mcp add voicebox \
  --transport http \
  --url http://127.0.0.1:17493/mcp \
  --header "X-Voicebox-Client-Id: claude-code"
```

### Configurar no Cursor / Windsurf / VS Code

```json
{
  "mcpServers": {
    "voicebox": {
      "url": "http://127.0.0.1:17493/mcp",
      "headers": { "X-Voicebox-Client-Id": "cursor" }
    }
  }
}
```

### Tools disponíveis

- `voicebox.speak` — falar em voz clonada;
- `voicebox.transcribe` — transcrever áudio;
- `voicebox.list_captures` — listar capturas recentes;
- `voicebox.list_profiles` — listar perfis de voz.

### Per-client voice binding

Cada cliente MCP pode ter uma voz associada diferente:

- Claude Code → voz "Morgan";
- Cursor → voz "Scarlett";
- etc.

Gerenciado em **Settings → MCP**.

## Uso responsável

Voicebox tem um `RESPONSIBLE_USE.md` no repo. Pontos principais:

### Usos permitidos

- Clonar a própria voz;
- Clonar voz com permissão explícita do falante;
- Usar material licenciado, público ou autorizado;
- Ferramentas de acessibilidade, projetos criativos, jogos, podcasts, protótipos.

### Usos proibidos

- Impersonar alguém sem permissão;
- Fraude, scam, phishing, social engineering;
- Assédio, ameaças;
- Comunicações enganosas (política, legal, financeira, médica);
- Uso comercial da voz de alguém sem direito legal.

### Disclosure

Se publicar ou distribuir áudio sintético, divulgue que é gerado por IA quando exigido por lei, política de plataforma ou expectativa do público.

## Comparação com GPT-SoVITS

| Critério | Voicebox | GPT-SoVITS |
|---|---|---|
| Interface | App desktop completa (Tauri) | WebUI + CLI |
| Motores TTS | 7 motores | 1 motor (GPT-SoVITS) |
| Idiomas | 23 | Principalmente chinês/japonês, suporte multilíngue |
| STT/Dictation | Sim (Whisper) | Não |
| MCP | Sim (4 tools) | Não |
| Local LLM | Sim (Qwen3) | Não |
| Efeitos de áudio | Sim (pedalboard, 8 efeitos) | Limitado |
| Stories editor | Sim (multi-track) | Não |
| GPU support | MLX, CUDA, ROCm, DirectML, CPU | CUDA, CPU |
| Licença | MIT | MIT |
| Estrelas | ~37.6k | ~47k |
| Foco | Estúdio completo de voz I/O | Clonagem TTS técnica |
| Melhor para | Uso geral, agentes, acessibilidade | Clonagem técnica avançada |

### Quando usar Voicebox

- você quer um estúdio completo local;
- quer integração com agentes via MCP;
- precisa de dictation + TTS no mesmo app;
- quer efeitos de áudio e stories editor;
- valoriza interface desktop nativa.

### Quando usar GPT-SoVITS

- você quer clonagem técnica avançada;
- foco em chinês/japonês;
- prefere WebUI/CLI;
- não precisa de dictation ou MCP.

## Status do teste

Voicebox é um **app desktop**, não um CLI. Não é possível instalar e testar o app GUI a partir do terminal. A análise foi feita a partir de:

- clone do repo;
- leitura completa do README, backend README, requirements.txt, RESPONSIBLE_USE.md;
- análise da release v0.5.0 e seus assets;
- leitura dos release notes.

Status recomendado no catálogo:

```yaml
status: documented_not_installed
```

### Para concluir o teste local

1. Baixar e instalar o MSI: `https://voicebox.sh/download/windows`;
2. Abrir o app;
3. Aguardar download de modelos;
4. Criar um voice profile (gravar ou importar amostra);
5. Gerar speech de teste;
6. Testar API REST com curl;
7. Configurar MCP no agente preferido;
8. Testar `voicebox.speak`;
9. Documentar resultados.

## Veredito

Voicebox é a ferramenta mais completa do catálogo para voz local:

- local-first (privacidade total);
- 7 motores TTS;
- clonagem zero-shot;
- dictation global;
- MCP server para agentes;
- API REST;
- efeitos de áudio;
- stories editor;
- MIT license.

Recomendado como pilar de voz do `lab-midia-ia`, pending instalação e teste prático local.

## Pendências

- Instalar o app desktop no Windows;
- Testar geração de speech com Kokoro (mais leve, 82M);
- Testar clonagem com Qwen3-TTS;
- Testar API REST `/generate` e `/speak`;
- Configurar MCP e testar `voicebox.speak`;
- Testar transcrição com Whisper Turbo;
- Avaliar performance no hardware local (Intel UHD Graphics → DirectML ou CPU).

## Referências

- Repo: https://github.com/jamiepine/voicebox
- Site: https://voicebox.sh
- Docs: https://docs.voicebox.sh
- Release: https://github.com/jamiepine/voicebox/releases/latest
- Responsible Use: https://github.com/jamiepine/voicebox/blob/main/RESPONSIBLE_USE.md
- API docs: `http://127.0.0.1:17493/docs` (quando rodando)
