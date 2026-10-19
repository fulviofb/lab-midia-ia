---
name: direcao-de-video
description: >
  Boas práticas de direção e produção de vídeo, do briefing ao MP4: motion graphics por código (HyperFrames),
  planos gerados por IA (ComfyUI local ou nuvem, imagem-para-vídeo, personagem consistente) e vídeo gravado
  (B-roll, legendas, narração). Use SEMPRE que pedirem um vídeo, animação, motion, vinheta, promo, reels,
  explicativo, episódio animado, clipe gerado por IA ou edição com animação, para qualquer marca ou projeto
  (institucional, produto, educativo, infantil, pessoal). Decide o quê e por quê; as skills de cada ferramenta decidem como.
---

# Direção de vídeo

Esta skill é a **camada de direção**: briefing, roteiro em frames, números de movimento, revisão, som, direitos e
marca. A execução fica com a ferramenta de cada tipo de produção (seção 0). Em conflito de direção ou processo,
esta skill vence; em conflito de API ou contrato da ferramenta, a skill da ferramenta vence.

## Princípios

1. **Adjetivo vira número.** "Premium", "dinâmico", "fofo" geram resultado genérico. Troque cada um por hex,
   cubic-bezier, damping, frames, pixels, ou (em plano gerado) por ação, tamanho no quadro e câmera explícitos.
2. **Diga o que mostrar e em que ordem.** Ações e telas nomeadas. Nunca "os momentos-chave de X".
3. **Uma timeline só** comanda imagem, som e revisão. Com narração, a voz é a timeline.
4. **Trave antes de gerar.** Estilo, personagens e cenários aprovados antes do primeiro shot; um quadro aprovado
   antes de animá-lo. Qualidade vem de planejamento, não de um prompt.
5. **Primeiro render é rascunho.** Acabamento vem de 2–4 rodadas com notas por número de frame, não por sensação.
   Um loop de 6–8s bem acabado leva ~3h com som; planeje o prazo com isso.

## 0. Tipo de produção e ferramenta

Uma peça pode misturar os três; a montagem final acontece num só lugar (HyperFrames, por padrão).

| Tipo | Quando | Ferramenta | Detalhes |
|---|---|---|---|
| **Motion por código** | Tipografia, UI, números, gráficos, vinheta, explicativo, ilustrado desenhado em código | **HyperFrames** (`/hyperframes` escolhe o workflow) | seções 1–5, `references/tokens.md`, `references/cenas-e-formatos.md` |
| **Plano gerado por IA** | Personagem animado, cena pintada, ação física que código não desenha | **ComfyUI** local (LTX, Wan) ou modelo na nuvem; montagem no HyperFrames | `references/planos-gerados.md` |
| **Vídeo gravado** | Depoimento, aula, fala, tutorial filmado | `talking-head-recut`, `embedded-captions`; Tesseract para editar e mixar | `references/cenas-e-formatos.md` (B-roll) |

Caminho **rápido** (vinheta, post, promo ≤ 20s): briefing curto → prompt dirigido → 1–2 rodadas → entrega.
Caminho **completo** (lançamento, institucional, episódio): todas as seções, 3 conceitos, build em etapas, 3–4 rodadas.

HyperFrames: `npx hyperframes` (Node 22+, FFmpeg). Antes de animar à mão, procure no catálogo:
`npx hyperframes catalog --query "<efeito, em inglês>"`. Atualize as skills com `npx hyperframes skills update`.
Sem HyperFrames: `references/fallback.md`. **Nomeie ferramenta e workflow no prompt**, senão cada rodada sai diferente.

## 1. Briefing (gate: BRIEF.md preenchido)

Pergunte só o que faltar, no máximo 5 perguntas por vez. Mostre o BRIEF antes de construir.

```
PEÇA: <slug>                 MARCA/ESTILO: <kit em references/marcas/ | estilo travado do projeto>
TIPO: motion | plano gerado | gravado | misto      FORMATO: 9:16 1080x1920 | 4:5 | 1:1 | 16:9
OBJETIVO: <o que o espectador sente ou faz, 1 frase>
PÚBLICO: <quem assiste e o que já sabe; ex.: "criança de 3 a 6 anos", "jovem que nunca usou o app">
DURAÇÃO: <s ou "pela narração">          PROMESSA/MENSAGEM: <1 frase>
MOMENTOS (3–5, em ordem): <ações ou telas nomeadas>
CTA / FECHO: <...>
DADOS REAIS: <número + fonte; sem fonte = ILUSTRATIVO>
ASSETS: <prints reais, logo, fichas de personagem/cenário, fotos autorizadas, trilha, vídeo gravado>
ÁUDIO: sem som | SFX | trilha licenciada (link) | narração (voz própria | TTS | voz clonada com consentimento)
PROIBIDO / PRAZO / REVISOR: <...>
```

- Sem OBJETIVO em uma frase, não dá para animar. Resolva isso primeiro.
- PÚBLICO define vocabulário, ritmo e tempo de leitura.
- Número sem fonte entra marcado **ILUSTRATIVO** no BRIEF e na entrega. Nunca publique número inventado como fato.
- Vídeo que mostra um app pede **prints reais**; tela desenhada é só teste.
- Sem narração, cada ideia precisa ser legível na tela: corte ideias, não tempo de leitura.

## 2. Tratamento (gate: conceito aprovado)

Caminho completo: 3 conceitos com recomendação. Lentes úteis: **jornada** (a pessoa passa pelas etapas),
**número-herói** (um número grande conduz), **antes/depois** (problema → resposta), **arco emocional**
(expectativa → virada → resolução, para narrativa).

**Cena = um evento** que o espectador consegue seguir:
estado inicial assentado → aproximação → ação registra → resultado aparece → hold até ler ou sentir.

```
f120 lista assentada · f180 dedo chega em "Candidatar" · f195 toque (escala 1→0.92→1, f192–201)
f210 toast "Candidatura enviada" · f234 toast legível, parado até o corte                (30 fps)
```

**Explicativo:** um processo do início ao fim, ou cenas listadas: problema → o que fazemos → 3 passos → prova →
assinatura. Ritmo inicial ~5s por ideia.
**Ilustrado ou animado:** três aprovações antes de animar — história, quadros de estilo, storyboard.
Com plano gerado, some a elas as fichas de personagem e cenário (`references/planos-gerados.md`).

**Beat sheet:** tempo, uma ação-herói por cena, e como passa para a próxima. O estado de saída de uma cena é o estado
de entrada da seguinte. Prefira um **elemento que costura** as cenas a transições genéricas.

## 3. Prompt dirigido (gate: todas as linhas preenchidas)

Todo pedido de animação por código sai neste formato. Cada linha tira uma decisão do modelo; as decisões padrão do
modelo são o visual genérico. Plano gerado usa o **Shot Spec** de `references/planos-gerados.md`.

```
GOAL:    o que o espectador sente ou faz, para quem
OUTPUT:  HyperFrames, workflow <nome>, L x A
TIME:    s x fps = frames (globais, inclusivos); BPM se houver música; loop sim/não
         com narração: tempos vindos das palavras transcritas
LOOK:    paleta em hex, 1 acento, fonte + peso + tamanho + tracking (kit da marca)
LAYOUT:  px a partir do canto sup. esq.; margem; caixa do título (x, y, largura, tamanho, máx. linhas);
         caixas de card/tela/personagem; âncoras de ação e resultado; ordem das camadas
MOTION:  easings em cubic-bezier, springs por damping ratio, durações em frames (references/tokens.md)
SHOTS:   faixas de frame, 1 movimento-herói por shot, eventos (seção 2), passagem (corte no beat | match cut |
         elemento que costura | máscara). Padrão é o corte; transição é decisão.
BANNED:  seção 7 + o que o 1º render usou, cada item com o que fazer no lugar
FACTS:   nunca invente números ou citações; sem fonte = ILUSTRATIVO
INPUTS:  o que pedir antes (prints, valores reais, trilha, WAV da narração, clipes gerados aprovados)
QA:      mapa de batidas + 4 stills antes de construir; abertura primeiro e espera aprovação
```

Determinismo é exigência do HyperFrames: uma timeline pausada, nada de `Date.now`, `setTimeout` ou `Math.random`
sem seed (regras em `/hyperframes-core`). Loop: o último frame flui para o 0.

## 4. Revisão (gate: passada limpa)

**Build em etapas.** Construa só a abertura; confira frames de entrada, pouso e fim do hold; relate e **espere
aprovação**. Depois as outras cenas, conferindo cada evento e cada fronteira de cena.

Ferramentas (HyperFrames):
- `npx hyperframes lint` durante a escrita; `npx hyperframes check --snapshots` como gate (inclui contraste WCAG).
- `npx hyperframes snapshot --at 0,2.5,6.5` para stills em tempos exatos; abra e descreva antes de mudar algo.
- `npx hyperframes preview --background` para a prévia; render só depois de aprovado
  (`--quality draft` iterando, `--quality delivery` no final).
- Contact sheet de qualquer MP4: `ffmpeg -i out.mp4 -vf "select='not(mod(n\,12))',scale=400:-1,tile=4x3" -frames:v 1 contact.png`

**Passada de direção com 3 stills** (abertura, momento principal, fechamento): o essencial é legível? o resultado
aparece? algo cortado ou sobreposto? o fechamento respira?

**Correção em quatro campos** — onde (frame global), problema, mudança, o que fica igual:

```
Problema: o cursor cobre o toast no frame 210.
Mude só o caminho do cursor após o toque: sai em 204, repousa em 210 dentro do card, 24 px de folga do toast.
Preserve: toque em 195, revelação em 210, geometria do card, textos, cues de áudio.
Stills em 195, 210, 222, 240; confira os frames intermediários.
```

Ordem: **informação faltando e texto ilegível → timing → detalhe visual.** Diga sempre se o frame é local ou global
(local 30 numa cena que começa em 120 = global 150). Feedback vago ("mais punch", "mais premium") vira número em
`references/tokens.md`.

### Checklist

- [ ] Um foco por frame; secundários depois do herói; saídas 40–50% mais curtas que entradas.
- [ ] Nada colidindo ou cortado; zona segura; texto mais longo testado.
- [ ] Holds de leitura cumpridos (≥ 0,3s/palavra + 0,5s, contados de quando fica legível); texto parado enquanto é lido.
- [ ] Contraste ≥ 4.5:1 em todo frame; ≤ 3 flashes por segundo.
- [ ] Texto em PT-BR revisado, no vocabulário do público.
- [ ] Fatos com fonte ou ILUSTRATIVO; telas reais ou aprovadas.
- [ ] Plano gerado: identidade e estilo iguais à ficha; sem zoom, gente ou objeto que não foi pedido.
- [ ] Narração: cada animação entra na palavra que a motiva; legenda bate com a fala.
- [ ] Loop sem soluço. Direitos e LGPD (seção 6).

## 5. Som e narração

O Claude não ouve: som se compõe por número de frame e se confere por medição. Cue list ao lado dos eventos visuais,
hit 1 frame depois do evento, um só riser e um só impacto por peça. Mixagem e ducking: `/hyperframes-audio`.
Detalhes: `references/som-e-narracao.md`.

**Com narração, a voz vem primeiro:** roteiro aprovado → voz gravada/gerada (WAV 48 kHz) →
`npx hyperframes transcribe` para tempos por palavra (conferir nomes e números) → cada evento visual no tempo da
palavra que o motiva → duração = última frase + hold do fecho. Legenda sempre.

## 6. Direitos e LGPD

- **Menores:** imagem só com termo assinado pelo responsável legal, para aquele uso. Sem termo: ilustração,
  silhueta, mãos ou tela. Personagem criado a partir de foto de criança fica estilizado, nunca retrato.
- Quem aparece ou empresta a voz: autorização para aquele uso. Voz clonada só com consentimento escrito; nunca de
  menores; nunca clonar voz comercial ou de terceiros.
- Telas sem nome, telefone, CPF ou foto real: dados fictícios evidentes.
- Logo e telas de terceiros só com autorização. Música só licenciada (link) ou sintetizada.
- Modelos de IA: conferir a licença de uso de cada modelo e LoRA (alguns exigem aceite ou proíbem uso comercial).
- Referências externas inspiram técnica e números, nunca visual, personagem ou marca de terceiros.

## 7. BANNED padrão (sempre no prompt, com o substituto)

- Glow, neon, lens flare, gradiente roxo/azul ou multicolorido → cor chapada da paleta.
- Partículas, shockwave, confete, RGB split, camera shake, fundo piscando → um gesto do elemento-herói.
- Crossfade → corte no beat ou o mesmo elemento mudando de estado.
- Overshoot em tudo → no máximo um, pequeno, só em pouso; texto nunca quica.
- Tudo entrando junto; fade-and-slide-up em todo elemento → um herói, secundários escalonados.
- Movimento sem origem; hold sem leitura > 1s → todo movimento nasce de algo na tela; corte ou push sutil.
- Tudo centralizado; texto que se move enquanto é lido.
- "Apresentamos…", taglines empilhadas, rótulo acima de título, emojis, ícones de stock.
- Tela falsa apresentada como real. Fecho: "qualquer coisa que pareça template".

Mantenha 5–9 itens por peça: rode, anote o que apareceu sem ser pedido, acrescente. "Evite visual de IA" não funciona;
nomes específicos funcionam.

## 8. Entrega

1. MP4 no formato principal, com som, assistido inteiro em velocidade normal.
2. `ffprobe` confere resolução, fps e duração esperados.
3. Versão muda + SRT/VTT quando houver fala. Poster PNG (frame aprovado). Variantes derivadas da timeline, nunca
   recortadas do master. Overlays com alpha (`--format webm` ou `mov`) quando forem para outro editor.
4. Projeto versionado junto do render: BRIEF, prompts e Shot Specs, follow-ups, cue list, palavras transcritas,
   seeds e workflows dos planos gerados.

Na resposta: duração, formato, o que é ILUSTRATIVO, o que precisa de aprovação.

## Referências desta skill

- `references/tokens.md` — easing, springs, durações, stagger, beat grid, leitura, câmera, personagem, feedback vago.
- `references/cenas-e-formatos.md` — estruturas por duração, cenas reutilizáveis, layout 9:16, B-roll sobre gravado.
- `references/planos-gerados.md` — fichas, Shot Spec, ComfyUI/LTX, chroma e composição, QA de clipe gerado.
- `references/som-e-narracao.md` — cue list, loudness, narração passo a passo.
- `references/marcas/` — um kit por marca (`exemplo.md`: modelo com prompt dirigido de 18s). Marca nova: copiar o formato.
- `references/fallback.md` — produção sem HyperFrames (HTML + Playwright, Remotion).
