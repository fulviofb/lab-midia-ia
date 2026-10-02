# Teste: personagem em chroma + composição, com motor de aquarela

Data: 2026-10-02

## Objetivo

Verificar se três técnicas vistas em repos de vídeo feito por código compensam num pipeline de animação infantil em aquarela (stills gerados por IA + composição no Remotion):

1. **Motor de pincelada** do estilo watercolor do `lemomo-ai/lemo-opuscar`: um elemento que se pinta pincelada a pincelada.
2. **Cortina de pincel** (brush-edge wipe) no lugar de corte seco.
3. **Personagem em chroma** do `makevoid/motion-graphics-music-video-skill`: o image-to-video anima só o personagem, e cenário e objetos ficam na composição.

## Ambiente

- Windows 11, Git Bash
- Remotion 4.0.484 (dependências instaladas com bun; render com `bunx remotion render`)
- FFmpeg com os filtros `chromakey` e `despill`
- Python 3 com Pillow e NumPy
- Image-to-video: MiniMax H3 Max via Magnific

## 1. Motor de pincelada (lemo-opuscar)

`styles/watercolor/demo/engine.js` tem 142 linhas, não tem dependências e é Canvas 2D puro em função de `t`. Foi portado para TypeScript com atribuição (MIT, LemoLab), mantendo só o núcleo: RNG com seed, ruído, `mk`, `drawS` e `drawList`. Roda dentro de um `<canvas>` numa composição do Remotion, com `delayRender`/`continueRender` por quadro.

O teste pintou uma constelação, estrela por estrela, ao longo de um risco que atravessa uma lua pintada numa tábua.

- O desenho é feito nas **coordenadas da imagem do objeto**, e cada plano tem uma única função mundo→tela. Num plano aberto posterior, a constelação continuou na tábua sem ajuste nenhum.
- Na primeira versão as estrelas ficaram pequenas demais para ler. Foi preciso dobrar o tamanho, então vale conferir o tamanho final em folha de contato.
- Os traços criados no render precisam estar dentro de `withSeed`, senão os workers paralelos discordam.

**Resultado:** funciona e não custa nenhuma geração.

## 2. Cortina de pincel

A cena nova entra por um recorte de borda ondulada, feita com ruído de baixa frequência, mais duas pinceladas verticais de cor de papel molhado ao longo da borda. A borda é redesenhada a 12 fps, como um traço que ferve à mão.

**Resultado:** funciona e substitui o corte seco. A borda ainda pede refinamento estético.

## 3. Personagem em chroma

### 3a. Recorte, sem gerar vídeo

As poses existentes foram coladas sobre chroma, codificadas em h264 yuv420p (como sai um vídeo gerado) e recortadas de volta.

| Caso | Resultado |
|---|---|
| Personagem sem verde na roupa, fundo `#00B140` | Recorte limpo, inclusive em cabelo cacheado. Diferença média de cor contra o original: 3 a 5 numa escala de 0 a 255. |
| Personagem **com roupa verde**, fundo verde | O `despill` deixa a roupa verde **cinza**. Não serve. |
| Mesmo personagem, fundo **magenta** `#FF00FF` | A cor da roupa fica certa. Sobra franja rosa, resolvida com despill próprio (subtrair `max(0, min(R,B) − G)` de R e B) e erosão de 1 px no alfa. Pequeno defeito em áreas claras com tom rosado, como os dentes. |

**Regra:** escolher a cor do chroma **por personagem**, ausente do figurino.

### 3b. Image-to-video real

- **Modelo:** MiniMax H3 Max, 768p, 6 s, 16:9, a partir de um quadro inicial com o personagem sobre `#00B140`. Custou 480 créditos.
- **Prompt:** identidade e estilo, depois ação com marcas de tempo (`[0s] … [1s] … [3s] … [5s]`), depois os invariantes do chroma: câmera travada, fundo verde liso o clipe todo, sem chão, sem sombra, sem texto, silhueta inteira dentro do quadro.

**Resultados:**

- **Fundo:** uniforme, com desvio-padrão menor que 1 nível por canal. Recorte direto com `chromakey=color=0x00AA3C:similarity=0.11:blend=0.05,despill=type=green` (a cor foi medida no próprio clipe).
- **Identidade e ação:** rosto, cabelo e figurino se mantiveram. A ação pedida, pegar o pincel atrás da orelha e segurá-lo, foi executada.
- **Defeito:** apesar de "câmera travada", o modelo fez um **push-in de ~7%**. A composição corrige: mede a linha dos pés em cada quadro, crava os pés no chão e compensa a escala.
- **Sombra:** sem chão no chroma, quem desenha a sombra de contato é a composição.
- **Resolução:** 768p ampliado para 1080p fica um pouco mais suave que o cenário. Para entrega final, testar um modelo em 1080p.

**Resultado:** compensa. Cenário e objetos continuam com os pixels idênticos, e o personagem ganha movimento orgânico que um recorte parado não tem.

## Conclusões

- A rota image-to-video de um pipeline com cenário travado passa a ser: **personagem em chroma → recorte → composição sobre cenário e props canônicos**. Gerar a cena inteira em vídeo fica como exceção justificada, quando o personagem precisa manipular um objeto gerado.
- Do `lemo-opuscar` vale adaptar o motor de pincelada, com atribuição, e usar o DIRECTOR.md como checklist. O pipeline completo pede WSL no Windows e não foi instalado.
- O plugin `makevoid` não precisa ser instalado: o padrão é reproduzível com qualquer provedor de image-to-video e ffmpeg.

## Não feito

- Instalar os plugins `lemo-opuscar`, `makevoid` e `opus-video-skills`.
- Comparar modelos de image-to-video em 1080p no mesmo quadro inicial.
- Ação com objeto canônico entre as mãos (prop composto entre as palmas).
