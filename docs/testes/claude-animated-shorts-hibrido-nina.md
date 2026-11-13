# Teste: claude-animated-shorts com personagem pintado (híbrido)

Data: 2026-11-13
Status: **técnica validada no Windows; integração de estilo ainda não testada**

## Objetivo

O `mromidev/claude-animated-shorts` desenha os personagens em código (cabeça de feijão, membros de palito, nanquim). Esse é o mesmo ponto em que o ReelMimic e o painted-animation perderam a folha do Pietro. Mas, como os personagens do repo são **cartões 2D dentro de um mundo 3D**, dá para trocar só essa camada.

Pergunta: mantendo do repo o mundo, a câmera, a luz e o pós-processamento, um personagem **pintado** (clipe i2v em chroma já recortado) funciona como cartão nesse mundo, sem perder a identidade?

## Ambiente

- Windows 11, RTX 4060 Laptop, Node 24.16.0, Chrome do sistema
- Repo: commit `e3b817b` (clone raso em `C:\Users\fulvi\ai-media-tests\claude-animated-shorts`)
- Projeto de teste: `C:\Users\fulvi\ai-media-tests\animated-shorts-nina` (fora do OneDrive)
- remotion / @remotion/three 4.0.543, react 19.3, @react-three/fiber 9.8, @react-three/postprocessing 3.2, postprocessing 6.39, three 0.187
- Personagem: Nina, 97 quadros do teste LTX-2.5 i2v em chroma (`keyed-nina-ltx/`, 576×896 RGBA, 24 fps), **sem** o passe de luz feito para o ENV-01

## O que foi feito

1. Copiamos `templates/bridge/` (o curta da ponte) sem mudar o mundo, a câmera, as luzes nem o pós-processamento.
2. Criamos um módulo novo, `nina.ts`, com a classe `NinaCard`:
   - é um plano com os quadros da Nina como textura, trocados a cada quadro (24→30 fps);
   - usa o **mesmo shader de cartão do repo** (`cardShade`) e a camada `NOINK`, então a luz da cena tinge o cartão, ele projeta sombra e o nanquim do mundo não o contorna;
   - os pés ficam ancorados no chão, com a altura achada por um raio vertical;
   - o cartão gira só no eixo vertical para encarar a câmera;
   - a altura é de 1,12 m, ao lado dos adultos de 2,16 m.
3. Posicionamos a Nina em dois planos existentes: o parque ao entardecer (plano 12) e a ponte de dia (plano 15).

## Resultado

Arquivos em `teste-repos-video/`: `nina-animated-shorts-hibrido-stills.jpg` (4 quadros) e `nina-animated-shorts-hibrido-ponte.mp4` (2,3 s, 540×960).

**O que funcionou**
- **A identidade fica 100% preservada.** É o próprio clipe pintado: cachos, jardineira, pincel e gesto do LTX.
- **A luz do mundo age no cartão.** A Nina projeta sombra no deque na direção do sol da cena, e o desfoque de lente (DOF) do plano a desfoca quando ela está fora do foco (parque).
- A escala ficou coerente com os outros personagens. A câmera deslizando dá paralaxe sem custo extra.
- Render rápido: cerca de 5 a 8 s por quadro em 540×960, depois de ~40 s de bundle.

**Limites encontrados**
- **Choque de estilo.** Uma menina pintada e realista num mundo de cartoon chapado com contorno preto. A técnica funciona, mas para o Sementes o mundo precisa ser repintado no estilo da série: as texturas de `paint.ts` em aquarela, o passe de nanquim suave ou desligado, e o grade em `grade.ts`.
- **O cartão é plano.** O gesto e o ângulo vêm do clipe i2v (de frente). Câmeras que contornam o personagem revelam isso. Funciona com dolly, push-in e travelling suave, que é a gramática do próprio repo.
- **O brilho de contorno do pôr do sol e o gradiente lateral** do `cardShade` usam as zonas de UV dos bonecos do repo (cabeça entre v 0,58 e 0,69). Para a Nina é preciso recalibrar, porque no entardecer ela ficou pouco dourada.
- **A posição é definida por câmera.** No quadro vertical, quando a câmera muda, ela sai do enquadramento (fim do clipe). Em produção, cada movimento de câmera precisa de uma marca de posição.

## Problemas e soluções (Windows)

1. **Os modelos Kenney (.glb) não vêm no repo** (`public/bridge/kenney/*` dá 404). O mundo renderiza sem esses objetos (lanternas, barracas, canoa...). São CC0 e podem ser baixados do site do Kenney.
2. **Quadro em branco no render com @react-three/fiber 9 + @react-three/postprocessing 3.** O `EffectComposer` registra os passes num efeito que roda depois de o `ThreeCanvas` já ter desenhado o quadro, e no render (frameloop `never`) ninguém redesenha. No Studio funcionava, no render saía só o fundo. A troca de backend de GPU (angle, swangle, swiftshader, vulkan, angle-egl) não resolveu. **Solução:** um componente `LateAdvance` dentro do canvas chama `advance()` de novo dois `requestAnimationFrame` depois, segurando o `delayRender` até lá.
3. **O render paralelo falhou** (`seekToFrame`, timeout). Usar `--concurrency=1`.
4. **TEMP no disco grande:** cada bundle copia `public/` para o temp. Usamos `TEMP=TMP=D:/remotion-tmp`.

## Próximos passos sugeridos

1. Repintar o mundo no estilo do Sementes: texturas de `paint.ts` em aquarela (reaproveitar o motor do lemo-opuscar ou o p5.brush), nanquim fino ou desligado, grade quente.
2. Recalibrar o `cardShade` para a folha da Nina e do Pietro (zonas de cabeça e tronco) e testar o contorno dourado.
3. Usar o FLF do LTX (mesma pose no início e no fim) para gestos em loop enquanto a câmera do repo faz o movimento.
4. Animatic: montar um episódio inteiro com cartões fixos (poses da folha) só para validar o ritmo e a câmera antes de gerar os clipes.

## Rodada 2 (2026-11-13): passe de aquarela no mundo

Objetivo: aproximar o mundo do repo da referência da série (ENV-01: aquarela quente, clara e enevoada, sem contorno preto) sem refazer as texturas uma a uma.

O que foi feito, como modo opcional (`inputProps: { look: "aquarela" }`; o padrão continua `toon`):
- **Nanquim:** marrom `#7a5638`, mais fino (1,8 a 1,1 px) e com intensidade 0,5, via `InkPass.set()`.
- **`WatercolorPass`** (`watercolor.ts`), depois do tone map e do grade. Ele faz:
  - bordas tremidas por ruído;
  - Kuwahara de 4 setores, que achata a imagem em manchas de tinta;
  - borda de pigmento acumulado;
  - granulação e textura de papel;
  - paleta mais clara e quente, com menos saturação nos azuis;
  - névoa de luz somada vinda do topo do quadro.
- **Máscara de proteção:** o cartão da Nina é desenhado num alvo à parte e fica fora da suavização, do tremido e da borda de pigmento. Ele recebe só a paleta. Sem a máscara, o Kuwahara apagava os olhos dela.

Resultado (`teste-repos-video/nina-animated-shorts-aquarela-antes-depois.jpg`):
- O mundo deixou de ser cartoon chapado e virou ilustração pintada, em guache. A família visual com a Nina melhorou, e o rosto e o cabelo dela ficaram intactos com a máscara.
- **Ainda não chega no estilo da série.** O filtro muda o acabamento, mas não o conteúdo nem a luz: continuam a ponte, os soldados de feijão, as sombras fortes e as cores saturadas.
- Iterações: a v1 ficou escura e barrenta (contraste em torno de 0,5 escurece as luzes). A v2 ficou acinzentada (a mistura com o papel vira véu cinza). A v3 usa luz somada (screen) e papel mais claro.

Conclusão e próximo passo: para chegar ao visual do Sementes, o **conteúdo** do mundo precisa ser nosso. O caminho mais fiel é o **multiplano**: montar o cenário com pranchas pintadas da série (ENV-01 separado em fundo, plano médio e primeiro plano) como cartões em profundidade. Assim reaproveitamos do repo a câmera, o desfoque de lente, a luz nos personagens e a sombra. O passe de aquarela continua útil como acabamento leve para unificar.

## Rodada 3 (2026-11-13): multiplano com a prancha ENV-01

Em vez de filtrar o mundo do repo, o cenário passou a ser a **prancha pintada da série**, separada em camadas e reprojetada a partir da própria câmera da pintura. Composição `Multiplano` (1920×1080, 24 fps, 97 quadros) em `src/videos/multiplano/Multiplano.tsx`.

**Camadas** (`scripts/camadas_env01.py`, rodando no venv do ComfyUI):
- **Profundidade:** Depth Anything V2 Small (Hugging Face, Apache-2.0, ~100 MB), cerca de 10 s na GPU.
- **Camada do meio:** profundidade maior que 0,25, acima da borda do deque (67,5 % da altura). Pega a varanda, os postes, os vasos e as trepadeiras.
- **Fundo:** a varanda é removida e o buraco é preenchido com `cv2.inpaint` (Telea), em 1/4 da resolução. Fica borrado, mas só aparece atrás das grades e desfocado pela lente.

**Câmera da pintura** (resolvida a partir da prancha, supondo o parapeito com 1 m): lente a 0,46 m do deque, borda do deque a 4,05 m, horizonte no centro, FOV horizontal de 60°.

**Montagem 3D:** um shader projeta a prancha a partir dessa câmera sobre três superfícies:
- o chão do deque;
- um cartão vertical na borda do deque, recortado pela máscara;
- um cartão de jardim a 12 m.

Por isso, no quadro 0 a imagem é idêntica à prancha, e qualquer movimento de câmera gera paralaxe real.

**O que veio do repo:** o deslizamento de câmera (smootherstep), o desfoque de lente com foco na Nina e a correção `LateAdvance`.

**Nina:** usa os quadros já iluminados para o ENV-01 (`keyed-nina-ltx-lit`), num cartão sem iluminação. Ela projeta sombra num plano só de sombra (`ShadowMaterial`) sobre o deque, com o sol atrás à esquerda, e tem uma mancha de contato sob os pés.

**Resultado**
- **Este é o caminho para o Sementes.** O cenário é a nossa pintura, a Nina é ela mesma, e a câmera avança com paralaxe: a varanda desliza sobre o jardim e o fundo desfoca.
- A sombra dela no deque cai na mesma direção das sombras pintadas do parapeito.
- Render: cerca de 3 s por quadro em 960×540.

**Limites**
- **Movimentos amplos expõem a reprojeção.** Os postes da esquerda estão mais perto que o cartão do meio, e o preenchimento do fundo é grosseiro. Com avanço curto e deslizamento lateral de até ~30 cm não aparece.
- A câmera precisa ser resolvida para cada prancha. É um cálculo simples, mas depende da altura suposta de algum objeto de referência.
