# Guia: Pré-requisitos e instalação

Antes de testar qualquer ferramenta do `lab-midia-ia`, instale estes pré-requisitos no seu computador.

## Windows

Este guia foi validado no Windows com terminal bash (git-bash/MSYS).

### 1. Node.js

- Versão recomendada: 22+ (testado com 24.16.0)
- Download: https://nodejs.org/
- Verificar:

```bash
node --version
npm --version
npx --version
```

### 2. Python

- Versão recomendada: 3.11+ (testado com 3.11.15 e 3.13.14)
- Download: https://www.python.org/downloads/
- Verificar:

```bash
python --version
python3 --version
```

### 3. UV (gerenciador Python)

Necessário para `video-use`.

```bash
# instalar via pip
pip install uv
# ou via powershell
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Verificar:

```bash
uv --version
```

### 4. FFmpeg e FFprobe

Necessário para renderização de vídeo, validação e edição.

- Download: https://ffmpeg.org/download.html
- No Windows, recomenda-se o build completo (full build) via winget:

```powershell
winget install Gyan.FFmpeg
```

Verificar:

```bash
ffmpeg -version
ffprobe -version
```

### 5. Git

Necessário para clonar repositórios e versionar.

- Download: https://git-scm.com/download/win
- Verificar:

```bash
git --version
```

### 6. GitHub CLI (gh)

Necessário para criar issues, comentar e gerenciar o repositório.

- Download: https://cli.github.com/
- Verificar e autenticar:

```bash
gh --version
gh auth status
```

Se não estiver autenticado:

```bash
gh auth login
```

### 7. Google Chrome (opcional, mas recomendado)

Necessário como fallback para HyperFrames no Windows.

- O Chrome do sistema funciona como browser de renderização.
- Verificar se existe em:

```txt
C:\Program Files\Google\Chrome\Application\chrome.exe
```

HyperFrames pode precisar de:

```bash
export HYPERFRAMES_BROWSER_PATH='C:\Program Files\Google\Chrome\Application\chrome.exe'
export PRODUCER_HEADLESS_SHELL_PATH='C:\Program Files\Google\Chrome\Application\chrome.exe'
```

Remotion baixa o Chrome Headless Shell automaticamente na primeira renderização.

### 8. Docker (opcional)

Algumas ferramentas podem usar Docker, mas não é obrigatório para os testes principais.

## Estrutura de pastas sugerida

Mantenha testes fora do repositório de curadoria:

```txt
C:\Users\<usuario>\lab-midia-ia\          ← repositório de curadoria
C:\Users\<usuario>\ai-media-tests\        ← pasta de testes práticos
    ├── video-use\                         ← clone do video-use
    ├── video-use-sample\                  ← pasta de teste do video-use
    ├── hyperframes\                       ← clone do hyperframes
    ├── hyperframes-smoke\                 ← pasta de teste do hyperframes
    └── remotion-smoke-AAAAMMDD\           ← pasta de teste do remotion
```

## Próximos passos

Depois de instalar os pré-requisitos, escolha um guia:

- `docs/guias/01-por-onde-comecar.md`
- `docs/guias/02-primeiro-video-com-hyperframes.md`
- `docs/guias/03-primeiro-video-com-remotion.md`
- `docs/guias/04-edicao-com-video-use.md`
