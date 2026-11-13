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
