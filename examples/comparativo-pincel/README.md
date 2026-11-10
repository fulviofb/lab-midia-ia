# Comparativo de motores de pincel: lemo-opuscar x p5.brush

A mesma cena de 5 s (morro, árvore, sol, sombra hachurada), com a mesma geometria e a mesma linha do tempo, pintada por dois motores. Relatório: [`docs/testes/p5brush-vs-lemo-pincel-teste.md`](../../docs/testes/p5brush-vs-lemo-pincel-teste.md).

## Arquivos

| Arquivo | Função |
|---|---|
| `scene.js` | Geometria, cores e linha do tempo comuns aos dois motores |
| `p5brush.html` | Cena pintada com o build standalone do p5.brush (WebGL2) |
| `lemo.html` | Cena pintada com o `engine.js` do estilo watercolor do lemo-opuscar (Canvas 2D) |
| `still.mjs` | Salva quadros soltos e confere se o mesmo tempo gera o mesmo quadro |
| `render.mjs` | Renderiza 150 quadros (5 s a 30 fps) e codifica direto em MP4 |
| `flicker.py` | Mede quanto as áreas já prontas mudam de um quadro para o outro |

## Preparar

As bibliotecas não ficam neste repositório. Baixe nos commits testados e coloque em `vendor/`:

```bash
mkdir vendor
curl -L -o vendor/brush.js https://raw.githubusercontent.com/acamposuribe/p5.brush/d56350a647d0b098a9e79d397447a8094f6c45a4/dist/brush.js
curl -L -o vendor/engine.js https://raw.githubusercontent.com/lemomo-ai/lemo-opuscar/9eb7739a0fca4c6990fe966cb8b87b1930f7193a/styles/watercolor/demo/engine.js
npm init -y && npm i -D playwright && npx playwright install chromium
```

Ambos são MIT (p5.brush: Alejandro Campos Uribe; engine.js: LemoLab).

## Rodar

```bash
mkdir out
node still.mjs p5brush.html out/p5 2.5 4.6     # quadros de conferência
node render.mjs p5brush.html out/p5brush.mp4
node render.mjs lemo.html out/lemo.mp4
python flicker.py out/lemo.mp4 out/p5brush.mp4
```

Variáveis opcionais:

- `CHROME_PATH`: caminho do Chrome do sistema, se não quiser o Chromium do Playwright.
- `ANGLE`: `swiftshader` (padrão; nuvem ou Linux sem GPU) ou `d3d11` (Windows com GPU). Não testado no Windows ainda.

Lado a lado com rótulos:

```bash
ffmpeg -i out/lemo.mp4 -i out/p5brush.mp4 -filter_complex "[0:v][1:v]hstack=inputs=2,format=yuv420p" -c:v libx264 -crf 18 out/comparativo.mp4
```
