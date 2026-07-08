# OpenMontage — primeiro teste no Windows

Data: 2026-07-08  
Issue: [#14](https://github.com/fulviofb/lab-midia-ia/issues/14)  
Repositório testado: <https://github.com/calesthio/OpenMontage>  
Commit testado: `de348f1`  
Máquina: Windows 10/11, Acer Predator PHN16-71, Intel i7-13650HX, 32 GB RAM, NVIDIA RTX 4060 Laptop 8 GB

## Resumo executivo

O OpenMontage passou em um **primeiro smoke test local no Windows** para o caminho zero-key baseado em Remotion:

- o repositório foi clonado em diretório isolado fora do `lab-midia-ia`;
- dependências Python principais instalaram em `.venv` isolada;
- dependências do `remotion-composer` instalaram com `npm install`;
- o demo zero-key `code-to-screen` renderizou um MP4 real;
- o MP4 foi validado com `ffprobe`;
- uma imagem de amostra foi extraída com `ffmpeg`;
- o registry do OpenMontage carregou 93 ferramentas;
- `piper-tts` instalou e expôs CLI/import local.

Status recomendado após a rodada completa de testes:

```yaml
status: tested_recommended_windows
```

Com ressalva: recomendar para **usuários técnicos/devs/agentes**, não como primeira ferramenta para público leigo. A rodada final validou um screen-demo sintético de ponta a ponta com schemas/checkpoints, Piper local, Remotion TerminalScene, MP4 final, `ffprobe` e inspeção visual de frames.

## Escopo testado

### Validado

- Instalação Python base com `requirements.txt`.
- Instalação Node/Remotion via `render_demo.py`.
- Download automático do Chrome Headless Shell usado pelo Remotion.
- Render local de composição Remotion com props versionados.
- Validação de MP4 com `ffprobe`.
- Extração de frame com `ffmpeg`.
- Descoberta de ferramentas via `tools.tool_registry`.
- Instalação/import/CLI do `piper-tts`.

### Não validado ainda

- Produção totalmente autônoma por agente real lendo todos os director skills em runtime.
- Uso de APIs pagas/opcionais (`OpenAI`, `ElevenLabs`, `FAL`, `Runway`, `Google`, etc.).
- Fluxo HyperFrames real (`hyperframes-doctor` ou render via HyperFrames).
- Fluxos com stock/open media, YouTube/reference video ou download de mídia.
- Instalação GPU/local video generation (`make install-gpu` / `requirements-gpu.txt`).

## Pré-requisitos encontrados

Comandos executados:

```bash
git --version
python --version
node --version
npm --version
ffmpeg -version | head -1
ffprobe -version | head -1
make --version | head -1 || true
uv --version || true
uname -a
```

Resultado relevante:

```txt
git: git version 2.55.0.windows.2
python: Python 3.11.15
node: v24.16.0
npm: 11.13.0
ffmpeg: ffmpeg version 8.1.2-full_build-www.gyan.dev
ffprobe: ffprobe version 8.1.2-full_build-www.gyan.dev
make: command not found
uv: uv 0.11.23
os: MINGW64_NT-10.0-26200 Fulvionote ... x86_64 Msys
```

Observação: `make` não estava disponível. Usei o caminho alternativo manual/Windows em vez de `make setup`.

## Clonagem

Diretório de teste, fora do repositório curado:

```txt
C:\Users\fulvi\ai-media-tests\OpenMontage
```

Comando:

```bash
mkdir -p /c/Users/fulvi/ai-media-tests
cd /c/Users/fulvi/ai-media-tests
git clone --depth 1 https://github.com/calesthio/OpenMontage.git
cd OpenMontage
git rev-parse --short HEAD
```

Resultado:

```txt
commit=de348f1
```

## Armadilha encontrada: `PYTHONPATH` herdado do Hermes

O terminal do Hermes tinha `PYTHONPATH` apontando para a instalação do Hermes:

```txt
PYTHONPATH=C:\Users\fulvi\AppData\Local\hermes\hermes-agent;C:\Users\fulvi\AppData\Local\hermes\hermes-agent\venv\Lib\site-packages
```

Isso fez a primeira tentativa de instalar dependências enxergar pacotes da venv do Hermes mesmo dentro da `.venv` do OpenMontage.

Diagnóstico:

```bash
.venv/Scripts/python.exe - <<'PY'
import sys, os
print('exe', sys.executable)
print('prefix', sys.prefix)
print('PYTHONPATH', os.environ.get('PYTHONPATH'))
print('\n'.join(sys.path))
PY
```

Correção usada no teste: limpar `PYTHONPATH` explicitamente em todos os comandos Python do OpenMontage:

```bash
PYTHONPATH= .venv/Scripts/python.exe ...
```

Isso isolou corretamente a venv.

## Instalação Python isolada

Comandos finais usados:

```bash
cd /c/Users/fulvi/ai-media-tests/OpenMontage
uv venv --clear --python 3.11 .venv
PYTHONPATH= .venv/Scripts/python.exe -m ensurepip --upgrade
PYTHONPATH= .venv/Scripts/python.exe -m pip install --upgrade pip
PYTHONPATH= .venv/Scripts/python.exe -m pip install -r requirements.txt
```

Validação:

```bash
PYTHONPATH= .venv/Scripts/python.exe - <<'PY'
import sys, openai, numpy, pydantic
print('venv ok', sys.executable)
print('openai', openai.__version__)
print('numpy', numpy.__version__)
print('pydantic', pydantic.__version__)
PY
```

Resultado:

```txt
venv ok C:\Users\fulvi\ai-media-tests\OpenMontage\.venv\Scripts\python.exe
openai 2.44.0
numpy 2.4.6
pydantic 2.13.4
```

## Demo zero-key via Remotion

O projeto tem três demos versionados:

```bash
PYTHONPATH= .venv/Scripts/python.exe render_demo.py --list
```

Resultado:

```txt
Available zero-key demos:
  code-to-screen       Developer workflow explainer with comparison and KPI cards
  focusflow-pitch      Startup-style pitch built only from Remotion components
  world-in-numbers     Global scale story with titles, stats, and charts
```

Render executado:

```bash
PYTHONPATH= .venv/Scripts/python.exe render_demo.py code-to-screen
```

Durante a primeira execução, o script fez:

- `npm install` em `remotion-composer`;
- download do Chrome Headless Shell usado pelo Remotion;
- bundle da composição;
- render de `750` frames em H.264.

Trecho relevante do resultado:

```txt
added 199 packages, and audited 200 packages in 16s
found 0 vulnerabilities
Downloading Chrome Headless Shell https://www.remotion.dev/chrome-headless-shell
Got Headless Shell
Composition          Explainer
Codec                h264
Output               C:\Users\fulvi\ai-media-tests\OpenMontage\projects\demos\renders\code-to-screen.mp4
Rendered 750/750
Encoded 750/750
Done: C:\Users\fulvi\ai-media-tests\OpenMontage\projects\demos\renders\code-to-screen.mp4 (3.5 MB)
```

## Validação do MP4

Arquivo gerado:

```txt
C:\Users\fulvi\ai-media-tests\OpenMontage\projects\demos\renders\code-to-screen.mp4
```

Comando:

```bash
ffprobe -v error \
  -show_entries format=duration,size,bit_rate \
  -show_entries stream=index,codec_type,codec_name,width,height,avg_frame_rate,duration \
  -of json \
  projects/demos/renders/code-to-screen.mp4
```

Resultado resumido:

```json
{
  "streams": [
    {
      "index": 0,
      "codec_name": "h264",
      "codec_type": "video",
      "width": 1920,
      "height": 1080,
      "avg_frame_rate": "30/1",
      "duration": "25.000000"
    },
    {
      "index": 1,
      "codec_name": "aac",
      "codec_type": "audio",
      "duration": "25.045333"
    }
  ],
  "format": {
    "duration": "25.045333",
    "size": "3638991",
    "bit_rate": "1162369"
  }
}
```

Também foi extraído um frame de amostra:

```bash
ffmpeg -y -ss 00:00:05 \
  -i projects/demos/renders/code-to-screen.mp4 \
  -frames:v 1 \
  projects/demos/renders/code-to-screen-frame-5s.jpg
```

Resultado:

```txt
projects/demos/renders/code-to-screen-frame-5s.jpg — 29 KB
```

## Registry / envelope de ferramentas

Comando:

```bash
PYTHONPATH= .venv/Scripts/python.exe - <<'PY'
from tools.tool_registry import registry
import json
registry.discover()
tool_count = len(getattr(registry, '_tools', {}))
print('tool_count', tool_count)
menu = registry.provider_menu()
print('provider_menu_ok', True)
envelope = registry.support_envelope()
print('support_envelope_ok', True)
PY
```

Resultado:

```txt
tool_count 93
provider_menu_ok True
support_envelope_ok True
```

Observação: o README/guia cita exemplo com `registry.tools`, mas a API atual do commit testado usa `_tools`. Para scripts de teste, preferir `getattr(registry, '_tools', {})` ou métodos públicos como `provider_menu()` e `support_envelope()`.

## Py compile mínimo

Comando:

```bash
PYTHONPATH= .venv/Scripts/python.exe -m py_compile \
  tools/base_tool.py \
  tools/tool_registry.py \
  tools/cost_tracker.py \
  tools/analysis/composition_validator.py
```

Resultado:

```txt
py_compile selected files ok
```

## Piper TTS

Instalação opcional:

```bash
PYTHONPATH= .venv/Scripts/python.exe -m pip install piper-tts
```

Resultado:

```txt
Successfully installed ... piper-tts-1.4.2 ... onnxruntime-1.27.0
```

Validação de import:

```bash
PYTHONPATH= .venv/Scripts/python.exe - <<'PY'
import piper
print('piper import ok', getattr(piper, '__file__', 'no-file'))
PY
```

Resultado:

```txt
piper import ok C:\Users\fulvi\ai-media-tests\OpenMontage\.venv\Lib\site-packages\piper\__init__.py
```

Validação de CLI:

```bash
PYTHONPATH= .venv/Scripts/python.exe -m piper --help | head -80
```

Resultado: CLI respondeu corretamente, exigindo modelo ONNX:

```txt
usage: __main__.py [-h] -m MODEL [-c CONFIG] [-i INPUT_FILE] [-f OUTPUT_FILE] ...
```

Não gerei narração Piper neste primeiro teste porque isso exige baixar/selecionar um modelo de voz ONNX e respectivo config.

## Avaliação

### Pontos fortes observados

- O caminho zero-key com Remotion funcionou no Windows.
- A estrutura do projeto é rica: pipelines, skills, registry, schemas, Backlot e runtime Remotion/HyperFrames.
- O projeto já possui demos versionados para validação inicial sem API keys.
- O registry conseguiu descobrir 93 ferramentas, com distinção entre disponíveis e indisponíveis.
- FFmpeg/ffprobe integraram bem ao fluxo.
- Piper instalou no Windows, ao menos no nível package/import/CLI.

### Pontos de atenção

- O projeto é grande e avançado; não é uma porta de entrada para público leigo.
- `make` não estava disponível no ambiente Windows; o caminho alternativo precisa estar documentado para usuários Windows.
- Em sessões Hermes, limpar `PYTHONPATH` é necessário para não misturar dependências do Hermes com a venv do projeto.
- A licença é AGPL-3.0: excelente para estudo/teste, mas exige cautela para adaptação, integração em serviços ou reuso de código.
- A rodada final ainda não prova autonomia completa de um agente externo, mas validou os artefatos/checkpoints e a composição final local.
- Não testei API keys nem geração de vídeo por provedores externos.

## Recomendação de catálogo

Atualizar `catalog.yml` para:

```yaml
status: tested_recommended_windows
```

Resumo recomendado:

> OpenMontage passou em testes Windows com Remotion zero-key, Backlot, Piper TTS real e screen-demo sintético end-to-end com schemas/checkpoints, MP4 final, ffprobe e inspeção visual. Recomendado para usuários técnicos/devs; ainda não é ferramenta inicial para leigos e exige cautela por AGPL-3.0.

## Próximos testes recomendados

1. Rodar `hyperframes-doctor` ou um render HyperFrames mínimo.
2. Baixar um modelo Piper pequeno e gerar narração WAV local.
3. Executar um pipeline real de ponta a ponta com pedido curto, por exemplo:
   - `animated-explainer` com `render_runtime=remotion` e sem APIs pagas, se possível;
   - ou `screen-demo` sintético com Remotion.
4. Testar Backlot:

```bash
PYTHONPATH= .venv/Scripts/python.exe scripts/backlot_simulate_run.py
PYTHONPATH= .venv/Scripts/python.exe -m backlot open backlot-demo-run
```

5. Avaliar se algum fluxo usa a RTX 4060 no Windows com `requirements-gpu.txt`.

## Segunda tentativa: Backlot e Piper real

Data: 2026-07-08

Após o primeiro smoke test, executei uma segunda rodada para validar componentes mais próximos do uso real do sistema.

### Backlot simulado

Objetivo: testar o board/live storyboard local, sem depender de uma produção real completa.

Primeira tentativa:

```bash
PYTHONPATH= .venv/Scripts/python.exe scripts/backlot_simulate_run.py
```

Falha encontrada:

```txt
ModuleNotFoundError: No module named 'pytest'
```

Causa: o simulador importa `tests.contracts.test_phase0_contracts.sample_artifact`, que depende de `pytest`, mas `pytest` não estava em `requirements.txt`.

Correção local:

```bash
PYTHONPATH= .venv/Scripts/python.exe -m pip install pytest
rm -rf projects/backlot-demo-run
PYTHONPATH= .venv/Scripts/python.exe scripts/backlot_simulate_run.py
```

Resultado:

```txt
[sim] init_project backlot-demo-run
[sim] checkpoint research -> in_progress
[sim] checkpoint research -> completed
[sim] checkpoint script -> in_progress
[sim] checkpoint script -> awaiting_human
[sim] checkpoint script -> completed
[sim] checkpoint scene_plan -> in_progress
[sim] checkpoint scene_plan -> awaiting_human
[sim] checkpoint scene_plan -> completed
[sim] checkpoint assets -> in_progress
[sim] generating sc1…
[sim] generating sc2…
[sim] generating sc3…
[sim] generating sc4…
[sim] checkpoint assets -> awaiting_human
[sim] checkpoint assets -> completed
[sim] done — board at http://127.0.0.1:4750/p/backlot-demo-run
```

Arquivos gerados:

```txt
projects/backlot-demo-run/project.json
projects/backlot-demo-run/artifacts/script.json
projects/backlot-demo-run/artifacts/scene_plan.json
projects/backlot-demo-run/artifacts/asset_manifest.json
projects/backlot-demo-run/assets/images/sc1.png
projects/backlot-demo-run/assets/images/sc2.png
projects/backlot-demo-run/assets/images/sc3.png
projects/backlot-demo-run/assets/images/sc4.png
projects/backlot-demo-run/checkpoint_*.json
projects/backlot-demo-run/events.jsonl
projects/backlot-demo-run/history/*.json
```

Servidor:

```bash
PYTHONPATH= .venv/Scripts/python.exe -m backlot serve --port 4750
```

Verificação no navegador:

```txt
http://127.0.0.1:4750/p/backlot-demo-run
Title: Backlot — The Last Lighthouse
Board carregou com STORYBOARD, 4 SCENES, ACTIVITY e navegação.
```

Conclusão: Backlot funciona no Windows após instalar `pytest`, mas o simulador tem uma dependência implícita não documentada no setup principal.

### Piper com modelo real

O pacote `piper-tts` atual não baixa voz com o comando antigo do README:

```bash
PYTHONPATH= .venv/Scripts/python.exe -m piper --download-dir .piper-models --model en_US-lessac-medium
```

Falha:

```txt
ValueError: Unable to find voice: en_US-lessac-medium (use piper.download_voices)
```

Caminho correto para a versão instalada:

```bash
mkdir -p .piper-models
PYTHONPATH= .venv/Scripts/python.exe -m piper.download_voices --download-dir .piper-models en_US-lessac-medium
```

Resultado:

```txt
INFO:__main__:Downloaded: en_US-lessac-medium
.piper-models/en_US-lessac-medium.onnx
.piper-models/en_US-lessac-medium.onnx.json
```

Geração via CLI:

```bash
printf 'OpenMontage can produce offline narration for draft videos.' > /tmp/openmontage_piper_text.txt
PYTHONPATH= .venv/Scripts/python.exe -m piper \
  --data-dir .piper-models \
  --model en_US-lessac-medium \
  --input-file /tmp/openmontage_piper_text.txt \
  --output-file projects/demos/renders/piper-smoke.wav
```

Validação com `ffprobe`:

```txt
codec: pcm_s16le
sample_rate: 22050
channels: 1
duration: 3.877732s
size: 171052 bytes
```

### Piper via tool do OpenMontage

Primeira tentativa com o nome curto do modelo:

```python
from tools.audio.piper_tts import PiperTTS
PiperTTS().execute({
    'text': 'This is OpenMontage using the Piper TTS tool directly.',
    'model': 'en_US-lessac-medium',
    'output_path': 'projects/demos/renders/piper-tool-smoke.wav',
})
```

Falhou:

```txt
ValueError: Unable to find voice: en_US-lessac-medium (use piper.download_voices)
```

Causa: o tool `piper_tts.py` chama `piper --model <model>`, mas não expõe `--data-dir`. Na versão atual do Piper, o modelo baixado em `.piper-models` não é encontrado pelo nome curto.

Workaround bem-sucedido: passar o caminho explícito do `.onnx` como `model`.

```bash
PATH="$PWD/.venv/Scripts:$PATH" PYTHONPATH= .venv/Scripts/python.exe - <<'PY'
from tools.audio.piper_tts import PiperTTS
res = PiperTTS().execute({
    'text': 'This is OpenMontage using the Piper TTS tool directly with an explicit model path.',
    'model': '.piper-models/en_US-lessac-medium.onnx',
    'output_path': 'projects/demos/renders/piper-tool-smoke.wav',
    'sentence_silence': 0.2,
})
print('success', res.success)
print('data', res.data)
PY
```

Resultado:

```txt
status ToolStatus.AVAILABLE
success True
data {'provider': 'piper', 'model': '.piper-models/en_US-lessac-medium.onnx', 'speaker_id': 0, 'text_length': 82, 'output': 'projects\\demos\\renders\\piper-tool-smoke.wav', 'format': 'wav'}
```

Validação:

```txt
codec: pcm_s16le
sample_rate: 22050
channels: 1
duration: 4.760091s
size: 209964 bytes
```

Conclusão: Piper funciona no Windows tanto via CLI quanto pelo tool `piper_tts`, mas o tool deve receber caminho explícito do `.onnx` ou o upstream deve ser ajustado para aceitar/pass-through de `data_dir`.

## Terceira tentativa: screen-demo sintético end-to-end

Data: 2026-07-08

Objetivo: executar o teste sugerido de produção curta controlada, combinando:

- `screen-demo` sintético;
- `TerminalScene` no Remotion;
- narração local com Piper TTS e modelo ONNX;
- artefatos canônicos (`brief`, `script`, `scene_plan`, `asset_manifest`, `edit_decisions`, `render_report`, `final_review`, `publish_log`);
- checkpoints OpenMontage de `idea` até `publish`;
- validação com `ffprobe`;
- inspeção visual de frames.

### Script usado

Criei um script local no clone de teste, sem commitar no repositório curado:

```txt
C:\Users\fulvi\ai-media-tests\OpenMontage\scripts\lab_screen_demo_piper_smoke.py
```

Ele gera um projeto isolado:

```txt
C:\Users\fulvi\ai-media-tests\OpenMontage\projects\lab-screen-demo-piper
```

Tema do vídeo:

```txt
Planejando um vídeo espírita curto com LLM
```

### Problemas encontrados e corrigidos

1. **Schemas rígidos de checkpoint**

   Os primeiros artefatos sintéticos falharam na validação porque não seguiam os schemas canônicos do OpenMontage. Corrigi `brief`, `script`, `scene_plan`, `asset_manifest`, `edit_decisions`, `render_report`, `final_review` e `publish_log` para validar sem desligar a validação.

2. **`npx` no Windows via Python subprocess**

   `subprocess.run(["npx", ...])` falhou com `WinError 2`. Correção:

   ```python
   npx_cmd = shutil.which("npx.cmd") or shutil.which("npx.exe") or shutil.which("npx")
   ```

3. **Áudio local no Remotion**

   Passar caminho absoluto do WAV fez o Remotion tentar baixar `file:///...wav` como URL HTTP. Correção: copiar o WAV para `remotion-composer/public/audio/` e referenciar nos props como caminho relativo público:

   ```txt
   audio/lab-screen-demo-piper-narration.wav
   ```

4. **Frame em ponto de transição**

   O frame extraído exatamente em `00:00:08` ficou vazio/escuro porque caiu na transição entre cenas. Ajustei a verificação para usar `00:00:10`, além de `2s`, `15s` e `21s`.

### Artefatos gerados

```txt
projects/lab-screen-demo-piper/artifacts/brief.json
projects/lab-screen-demo-piper/artifacts/script.json
projects/lab-screen-demo-piper/artifacts/scene_plan.json
projects/lab-screen-demo-piper/artifacts/asset_manifest.json
projects/lab-screen-demo-piper/artifacts/edit_decisions.json
projects/lab-screen-demo-piper/artifacts/render_report.json
projects/lab-screen-demo-piper/artifacts/final_review.json
projects/lab-screen-demo-piper/artifacts/publish_log.json
projects/lab-screen-demo-piper/checkpoint_idea.json
projects/lab-screen-demo-piper/checkpoint_script.json
projects/lab-screen-demo-piper/checkpoint_scene_plan.json
projects/lab-screen-demo-piper/checkpoint_assets.json
projects/lab-screen-demo-piper/checkpoint_edit.json
projects/lab-screen-demo-piper/checkpoint_compose.json
projects/lab-screen-demo-piper/checkpoint_publish.json
projects/lab-screen-demo-piper/renders/final.mp4
projects/lab-screen-demo-piper/renders/frame-2s.jpg
projects/lab-screen-demo-piper/renders/frame-10s.jpg
projects/lab-screen-demo-piper/renders/frame-15s.jpg
projects/lab-screen-demo-piper/renders/frame-21s.jpg
```

### Validação do MP4 final

Arquivo final:

```txt
C:\Users\fulvi\ai-media-tests\OpenMontage\projects\lab-screen-demo-piper\renders\final.mp4
```

`ffprobe`:

```txt
video: h264, 1920x1080, 30 fps, duração 25.000000s
audio: aac, 48000 Hz, 2 canais, duração 25.045333s
format: mp4, tamanho 1,810,643 bytes, bitrate 578357
```

`final_review.json`:

```txt
status: pass
technical_probe.valid_container: true
visual_spotcheck.frames_sampled: 4
audio_spotcheck.narration_present: true
promise_preservation.render_runtime_used: remotion
recommended_action: present_to_user
```

### Inspeção visual

Frames verificados:

- `frame-2s.jpg`: cena inicial legível, com título e terminal sintético;
- `frame-10s.jpg`: segunda cena legível (`prompt-mestre.md`);
- `frame-15s.jpg`: segunda cena legível com roteiro/cenas/revisão;
- `frame-21s.jpg`: cena final legível com validações e callout `3 passos`.

Conclusão visual: o vídeo renderiza terminal sintético válido e legível em 1920x1080.

### Resultado da rodada final

O OpenMontage passou no teste `screen-demo` sintético end-to-end no Windows.

Critérios cumpridos:

- artefatos canônicos schema-valid;
- checkpoints de `idea` a `publish`;
- Piper TTS local com modelo real;
- Remotion `TerminalScene`;
- MP4 final com áudio;
- `ffprobe` aprovado;
- frames verificados visualmente.

Limitação restante: o pipeline foi orquestrado por script local dentro do clone, não por um agente autônomo externo executando todos os director skills em runtime. Ainda assim, para catálogo prático de ferramentas, isso é suficiente para marcar como `tested_recommended_windows` com ressalva de ferramenta avançada/técnica.

## Decisão

OpenMontage merece permanecer como candidato forte no laboratório, agora com evidências melhores:

- **para leigos:** não recomendar como primeira ferramenta;
- **para devs/agentes:** muito promissor;
- **para o site Concafras IA:** pode aparecer na seção técnica como ferramenta avançada, com status de teste parcial;
- **para produção real:** ainda aguardar teste agentic completo antes de chamar de recomendado.

O status continua correto como:

```yaml
status: partially_tested_windows
```

Mas a confiança aumentou: além do render zero-key Remotion, agora também passaram Backlot simulado e Piper real com modelo ONNX.
