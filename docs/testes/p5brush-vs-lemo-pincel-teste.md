# Teste: motor de pincel p5.brush x lemo-opuscar

Data: 2026-11-10

## Objetivo

Comparar o `acamposuribe/p5.brush` com o motor de pincelada do `lemomo-ai/lemo-opuscar`, já portado no [teste de aquarela](chroma-composite-aquarela-teste.md), para explicativos ilustrados pintados em código. A pergunta: o p5.brush entrega textura melhor sem perder o que importa num render quadro a quadro (o mesmo tempo gera o mesmo quadro, as áreas prontas não tremem, o tempo de render é aceitável)?

## Ambiente

- Linux na nuvem, sem GPU (rodada principal)
- Windows no notebook, com GPU Intel integrada (ver "Rodada no Windows")
- Google Chrome headless via Playwright 1.63, WebGL2 por software (`--use-angle=swiftshader --enable-unsafe-swiftshader`)
- FFmpeg com libx264
- p5.brush 3.0.0, build standalone `dist/brush.js`, commit `d56350a`
- lemo-opuscar `styles/watercolor/demo/engine.js`, commit `9eb7739`

Arquivos para reproduzir: [`examples/comparativo-pincel/`](../../examples/comparativo-pincel/).

## Cena

960×540, 5 s a 30 fps. A mesma geometria e a mesma linha do tempo nos dois motores:

| Tempo | Elemento | p5.brush | lemo-opuscar |
|---|---|---|---|
| 0,0–1,0 s | Linha do morro | `spline` com grafite `2B` | `mk` + `drawS` (perfil `even`) |
| 0,6–1,6 s | Tronco | `spline` com `2B` grosso | perfil `trunk` |
| 1,2–2,2 s | Galhos | `spline` com `2B` | perfil `tip` |
| 2,0–3,2 s | Sol | `fill` (aquarela) com opacidade subindo | cordas horizontais com `drawList` |
| 2,6–3,8 s | Copa | `fill` (aquarela) | `clump` de folhas |
| 3,2–4,2 s | Morro e sombra | `fill` + `hatch` revelado por `clip` | faixas largas + hachura com `drawList`, recortadas no polígono |

Os traços parciais do p5.brush são a polilinha cortada no comprimento do progresso. Cada elemento chama `brush.seed()` com um valor fixo antes de desenhar.

## Resultados

| Critério | lemo-opuscar | p5.brush |
|---|---|---|
| Mesmo tempo gera o mesmo quadro | Sim (hash igual em 2,5 s e 4,6 s) | Sim (hash igual em 2,5 s e 4,6 s) |
| Áreas prontas tremendo (mudança média por quadro, 0–255) | 0,001 na linha; 0 no sol | 0,004 na linha; 0,005 no sol (invisível) |
| Tempo de desenho por quadro | 2,8 ms | 6,4 ms |
| Tempo total do render de 150 quadros | ~10 s | ~2 min 37 s |
| Erros no console | Nenhum | Nenhum |

**Visual.** O p5.brush entrega aquarela de verdade: borda irregular, anel de pigmento, granulação e manchas. O grafite tem grão de papel e a hachura sai a lápis. O lemo-opuscar parece guache em pinceladas, mais gráfico e legível; o sol vira listras e a copa vira tufos de folhas.

**Tempo na nuvem.** O desenho em si é rápido nos dois. A diferença está em ler o quadro de volta do WebGL por software: ~1 s por quadro, contra ~0,07 s do Canvas 2D.

## Rodada no Windows

Mesmos arquivos, no notebook (Windows, Node 24.16, FFmpeg 8.1.2, Chrome do sistema via `CHROME_PATH`), com o script `rodar-gpu.cmd`. O `gpu.mjs` confirmou o renderizador do WebGL2 em cada modo.

| Render (150 quadros) | Renderizador | Tempo total |
|---|---|---|
| p5.brush, `ANGLE=d3d11` | Intel UHD Graphics (D3D11) | 14,2 s |
| p5.brush, `ANGLE=swiftshader` | SwiftShader (CPU) | 30,9 s |
| lemo-opuscar, `ANGLE=d3d11` | Canvas 2D | 7,2 s |
| p5.brush na nuvem (referência) | SwiftShader (CPU) | ~157 s |

- Mesmo tempo, mesmo quadro também no Windows (hash igual em 2,5 s e 4,6 s).
- Os três renders do p5.brush (GPU no PC, CPU no PC, nuvem) são praticamente iguais: diferença média de 0,33 a 0,48 numa escala de 0 a 255, invisível a olho.
- Mesmo com GPU integrada, o p5.brush fica a ~2× do tempo do lemo-opuscar, o que é aceitável para peças curtas. A lentidão na nuvem vinha mais da máquina do que do SwiftShader.
- O Chrome escolheu a GPU Intel integrada. Não testei forçar a NVIDIA.

## Pontos de atenção do p5.brush

- **Seed por elemento.** Sem `brush.seed()` fixo antes de cada fill e de cada traço, a aquarela muda a cada quadro.
- **Revelar fill.** Subir a opacidade funciona. Crescer o raio muda o formato da mancha a cada quadro; não foi usado.
- **Peso dos traços.** Com `scaleBrushes(2.5)` em 960×540, grafite peso 1,3 ficou fino demais; peso 2,4–4,5 ficou legível. Conferir em folha de contato.
- **Fills que se tocam** no mesmo quadro se misturam (a copa feathera sobre o tronco). É efeito de aquarela, mas a ordem de desenho importa.
- **`clip` afeta só traço e hachura**, não fill.
- O build standalone exige `brush.render()` no fim de cada quadro.

## Conclusões

- Para explicativos ilustrados com cara de aquarela, grafite ou nanquim, **o p5.brush é a melhor escolha**. A textura do lemo-opuscar continua boa para um estilo mais gráfico e para renders rápidos.
- O p5.brush cumpre as regras de render quadro a quadro (mesmo quadro para o mesmo tempo, sem tremor), desde que haja seed por elemento.
- No Windows com GPU, o tempo é aceitável (~0,1 s por quadro em 960×540). Na nuvem sem GPU, para prévias rápidas, renderize em resolução menor ou a cada 2 quadros.

## Não feito

- Forçar a GPU NVIDIA no Chrome e comparar com a Intel integrada.
- Embutir o p5.brush numa composição do Remotion ou do HyperFrames.
- Testar resolução 1920×1080 e `pixelDensity` maior.
- Testar campos vetoriais (`refreshField(t)`) para traço "vivo".
