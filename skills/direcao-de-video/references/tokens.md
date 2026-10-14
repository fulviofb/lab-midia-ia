# Números de movimento

Crie um arquivo de tokens por peça e peça "use só estes tokens, nenhum número solto". Guarde juntos deslocamento,
destino, duração e pouso de cada entrada, para uma revisão mexer em um só lugar. A 30 fps, 1 frame ≈ 33 ms
(0,4s = 12 frames; 0,6s = 18; 0,75s ≈ 22).

## Easing

| Nome | cubic-bezier | Uso |
|---|---|---|
| `enter` (ease-out-expo) | 0.16, 1, 0.3, 1 | Revelação de texto e logo |
| `premium` (ease-out-quint) | 0.22, 1, 0.36, 1 | Entradas de card e tela |
| `move` (ease-in-out-quart) | 0.76, 0, 0.24, 1 | Deslocamentos e câmera |
| `exit` (ease-in-expo) | 0.7, 0, 0.84, 0 | Saídas rápidas |
| `pop` (ease-out-back) | 0.34, 1.56, 0.64, 1 | Selo, conquista (com overshoot) |

Entra com ease-out, sai com ease-in, saídas 40–50% mais curtas, atravessa a tela com ease-in-out. Linear só em
rotação, barra de progresso e fase de loop.

## Springs (damping ratio)

| Ratio | Sensação | Uso |
|---|---|---|
| 1.0 | sem quique | Texto, opacidade, cor |
| 0.7–0.85 | premium | Cards, telas, painéis |
| 0.4–0.6 | brincalhão | Selo de nível, badge, número final |
| < 0.3 | cartoon | Evitar em institucional |

Posição e escala podem quicar; **opacidade e cor nunca**. Para afinar, mantenha o destino fixo e mude um parâmetro por vez.

## Durações, stagger, hierarquia

- Feedback de UI 100–200 ms · movimento de UI 200–500 ms · revelação-herói 600–900 ms · contador 1,2–2s.
- Stagger: letras 1 frame · palavras 60–120 ms · itens de lista 40–80 ms · cards até 200 ms. O próximo começa quando
  o anterior está 30–50% feito.
- **Um herói por shot.** Secundários percorrem 50–70% da distância do herói e começam 100–200 ms depois. Ambiente
  < 5% da distância, em seno lento (4–8s).
- Quem é dono da tela: a atenção fica no botão até a resposta aparecer; depois o resultado é dono da janela de leitura.

## Beat grid

Frames por beat = fps × 60 / BPM (120 BPM a 30 fps = 15). Calcule cada beat a partir do tempo e arredonde um por um
(somar o valor arredondado desliza da música). Corte no beat, mude o layout no compasso (a cada 4). Em HyperFrames,
`npx hyperframes beats` extrai os beats da trilha.

## Leitura, câmera, acessibilidade

- Texto na tela ≥ **0,3s por palavra + 0,5s**, contado de quando fica legível; frases nunca menos de 1,2s.
- Hold sem leitura > 1s é tempo morto. Em hold de leitura, push sutil (1.00 → 1.03 em 3s) com o texto parado.
- Câmera recebe as curvas mais suaves; objetos, as mais rápidas. Parallax: frente 1.0, meio 0.5, fundo 0.2.
- Contraste ≥ 4.5:1 em todo frame; nunca mais de 3 flashes por segundo.
- No celular tudo encolhe: exagere poses-chave 10–30% e confira rótulos em tamanho de telefone.
- Motion blur só na entrada rápida; o hold de leitura fica nítido.

## Personagem e mascote

| Princípio | Escreva assim |
|---|---|
| Antecipação | agachar 11 frames (1.2 × 0.75) antes do salto |
| Squash & stretch | 0.85 × 1.28 na decolagem, 1.25 × 0.7 no pouso |
| Ação sobreposta | braços atrasam 4 frames, pernas 6 |
| Follow-through | braços assentam a 2,2 Hz, damping 0.22 |
| Arcos | trajetórias em arco, nunca linha reta |

Mais uma linha de **proporções que não mudam**, para o personagem continuar reconhecível.

## Feedback vago em números

- "Mais punch" → escala 1.0 → 1.08 → 1.0 em 6 frames, pico no beat.
- "Mais premium" → entradas ease-out-quint, springs 0.8, sem overshoot em texto.
- "Está poluído" → remova 30% do movimento; fica só o que guia o olho.
- "Final seco" → hold de 36 frames com push de 2%, assentando em spring 0.8.
