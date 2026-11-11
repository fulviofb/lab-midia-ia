# Produção sem HyperFrames

Use só quando o HyperFrames não estiver disponível ou a peça reaproveitar componentes React do produto.

## HTML + Playwright + FFmpeg

```powershell
winget install OpenJS.NodeJS.LTS; winget install Gyan.FFmpeg   # abrir terminal novo depois
mkdir motion-lab; cd motion-lab; npm init -y; npm i -D playwright; npx playwright install chromium
```

Contrato de render (colar embaixo do prompt dirigido):

```
Um único arquivo HTML. Só as bibliotecas citadas, fixadas em versão. Sem rede além de fontes e dessas bibliotecas.
Todo frame é função pura do tempo t em segundos: exponha window.renderAt(t).
Com ?t=2.5 na URL, congele nesse frame e não inicie requestAnimationFrame.
Sem Date.now, setTimeout/setInterval, transições CSS soltas ou Math.random sem seed.
Loops: renderize 0 a N-1; o frame N-1 flui para o 0.
```

`render.mjs`: abre o HTML no Chromium headless, espera as fontes, chama `renderAt(i / fps)`, salva um PNG por frame
(usar `pathToFileURL` no Windows). Depois:

```bash
ffmpeg -framerate 30 -i out/frames/%04d.png -c:v libx264 -pix_fmt yuv420p -crf 18 -movflags +faststart out/peca.mp4
```

## Remotion

`npx create-video --yes --blank <peca>` e `npx remotion skills add`. Todo valor animado sai de `useCurrentFrame()`
com `interpolate` ou `spring`. Licença: gratuita para pessoas, entidades sem fins lucrativos e empresas de até 3 funcionários; acima disso, Company License.
Para levar um projeto Remotion ao HyperFrames: `/remotion-to-hyperframes`.

Repositórios comunitários de motion (claude-motion e semelhantes): ler para aproveitar ideias; antes de usar, auditar
commits, dependências e chamadas de rede e fixar o commit num fork próprio.
