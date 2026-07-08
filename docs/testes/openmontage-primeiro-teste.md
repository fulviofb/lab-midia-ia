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

Status recomendado após este teste:

```yaml
status: partially_tested_windows
```

Não marcar ainda como `tested_recommended_windows`, porque este teste **não executou uma produção agentic completa de ponta a ponta** usando o sistema de pipelines com aprovação, roteiro, assets, edição e composição final. Ele validou o caminho local/zero-key de render e parte importante da infraestrutura.

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

- Produção agentic completa via pipeline real (`animated-explainer`, `screen-demo`, `documentary-montage` etc.).
- Uso de APIs pagas/opcionais (`OpenAI`, `ElevenLabs`, `FAL`, `Runway`, `Google`, etc.).
- Geração real de narração com Piper usando modelo baixado.
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
- O smoke test não prova ainda o fluxo agentic completo de produção.
- Não testei API keys nem geração de vídeo por provedores externos.

## Recomendação de catálogo

Atualizar `catalog.yml` para:

```yaml
status: partially_tested_windows
```

Resumo recomendado:

> Primeiro smoke test local no Windows aprovado para caminho zero-key Remotion: instalação Python/Node, render de demo MP4, ffprobe, registry e Piper package/CLI. Ainda requer teste de pipeline agentic completo antes de recomendação ampla.

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

## Decisão

OpenMontage merece permanecer como candidato forte no laboratório, mas com posição clara:

- **para leigos:** não recomendar como primeira ferramenta;
- **para devs/agentes:** muito promissor;
- **para o site Concafras IA:** pode aparecer na seção técnica como ferramenta avançada, com status de teste parcial;
- **para produção real:** aguardar teste agentic completo antes de chamar de recomendado.
