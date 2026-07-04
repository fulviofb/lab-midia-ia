# Guia: Primeiro vídeo com HyperFrames

HyperFrames transforma HTML/CSS/GSAP em vídeo MP4 de forma determinística. Este guia mostra como criar seu primeiro vídeo do zero.

## Quando usar HyperFrames

- motion graphics curtos;
- title cards;
- vídeos explicativos visuais;
- vídeos a partir de website;
- animações de UI/produto;
- vídeos sociais com tipografia cinética.

## Pré-requisitos

Ver `docs/guias/00-pre-requisitos.md`.

Resumo mínimo:

- Node.js 22+
- npm/npx
- FFmpeg/FFprobe
- Google Chrome instalado

## Passo 1: Instalar skills

```bash
npx --yes skills add heygen-com/hyperframes --all
```

Isso instala 21 skills de agentes, incluindo:

- `hyperframes`
- `hyperframes-core`
- `hyperframes-cli`
- `hyperframes-animation`
- `motion-graphics`
- `website-to-video`
- `product-launch-video`

> Atenção: as skills rodam com permissões do agente. Revise antes de usar em ambientes sensíveis.

## Passo 2: Criar projeto

```bash
mkdir -p ~/ai-media-tests/hyperframes-smoke
cd ~/ai-media-tests/hyperframes-smoke
npx --yes hyperframes init hf-blank --non-interactive --example blank
cd hf-blank
```

## Passo 3: Configurar browser no Windows

Se o `hyperframes browser ensure` falhar, use o Chrome do sistema:

```bash
export HYPERFRAMES_BROWSER_PATH='C:\Program Files\Google\Chrome\Application\chrome.exe'
export PRODUCER_HEADLESS_SHELL_PATH='C:\Program Files\Google\Chrome\Application\chrome.exe'
```

Verificar:

```bash
npx --yes hyperframes browser path
```

Deve mostrar o caminho do Chrome.

## Passo 4: Entender a estrutura

O projeto scaffoldado tem:

```txt
index.html          ← composição principal
hyperframes.json    ← configuração
AGENTS.md           ← instruções para agentes
CLAUDE.md           ← instruções para Claude Code
meta.json           ← metadados
package.json
```

O `index.html` é onde a composição acontece.

## Passo 5: Estrutura de uma composição

Uma composição HyperFrames tem:

```html
<div id="root"
  data-composition-id="main"
  data-start="0"
  data-duration="6"
  data-width="1920"
  data-height="1080">
  <div class="clip" data-start="0" data-duration="6" data-track-index="0">
    conteúdo
  </div>
</div>
```

Atributos importantes:

- `data-composition-id`: identificador da composição;
- `data-start`: quando o elemento começa (segundos);
- `data-duration`: duração do elemento (segundos);
- `data-track-index`: camada/pista do elemento;
- `class="clip"`: marca o elemento como temporizado.

## Passo 6: Animar com GSAP

O HyperFrames usa GSAP para animações. A timeline deve ser pausada e registrada:

```html
<script src="https://cdn.jsdelivr.net/npm/gsap@3.14.2/dist/gsap.min.js"></script>
<script>
  window.__timelines = window.__timelines || {};
  const tl = gsap.timeline({ paused: true });
  tl.from("#titulo", { opacity: 0, y: 50, duration: 1, ease: "power3.out" }, 0.5);
  window.__timelines["main"] = tl;
</script>
```

Regras importantes:

- a timeline deve estar `paused: true`;
- registrar em `window.__timelines["<composition-id>"]`;
- não usar `Date.now()`, `Math.random()` sem seed, nem fetch em tempo de render;
- não usar CSS transitions/animations;
- não usar Tailwind animation classes.

## Passo 7: Validar

Sempre rode estes comandos antes de renderizar:

```bash
npx --yes hyperframes lint .
npx --yes hyperframes validate .
npx --yes hyperframes inspect .
```

Se houver warnings ou erros, corrija antes de prosseguir.

## Passo 8: Snapshot

Gere frames de verificação visual:

```bash
npx --yes hyperframes snapshot . --at 0,1.5,3,5.5
```

Isso gera PNGs e um `contact-sheet.jpg` em `snapshots/`.

## Passo 9: Renderizar

```bash
npx --yes hyperframes render . \
  --quality draft \
  --strict \
  --output renders/meu-video.mp4
```

`--strict` bloqueia render se houver problemas de lint.

## Passo 10: Validar output

```bash
ffprobe -v error \
  -show_entries format=duration,size \
  -show_entries stream=index,codec_type,codec_name,width,height,r_frame_rate \
  -of json renders/meu-video.mp4
```

## Problemas comuns no Windows

### `browser ensure` falha

Sintoma: cache de chrome-headless-shell quebrado, missing executable.

Solução: usar Chrome do sistema com as variáveis de ambiente do Passo 3.

### `timeline_view.py` falha no frame final

Sintoma: erro ao extrair frame exatamente no limite final do vídeo.

Solução: usar um `end` ligeiramente menor que a duração total.

## Próximos passos

- Testar formato vertical 9:16 (mudar `data-width` e `data-height`);
- Testar `hyperframes add` com blocos de catálogo;
- Explorar workflow `website-to-video`;
- Criar um motion graphic para um tema real.

## Referências

- Repo: https://github.com/heygen-com/hyperframes
- Workflow detalhado: `workflows/hyperframes-video-html.md`
- Teste local: `docs/testes/hyperframes-primeiro-teste.md`
- Prompt pronto: `prompts/hyperframes-motion-graphic.md`
