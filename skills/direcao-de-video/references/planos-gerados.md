# Planos gerados por IA

Para personagens e cenas que código não desenha. Regra de ouro: **a IA anima; o resto se compõe.** O modelo de vídeo
cuida só do que precisa de movimento orgânico (personagem); cenário, props, texto, câmera e luz ficam no compositor
(HyperFrames), onde são exatos e repetíveis.

## Ordem de produção (cada passo com aprovação)

1. **Estilo travado:** paleta, traço, textura, 2–3 quadros de referência. Teste: troque o assunto da imagem; o que
   continuar verdadeiro é estilo.
2. **Fichas antes de qualquer shot:**
   - personagem: frente, 3/4, lado e costas, linha de expressões, poses de ação, chips de cor, closes de detalhe,
     comparação de altura (em cabeças), fundo branco liso;
   - cenário: plano de estabelecimento, sub-áreas rotuladas, ângulos, props-chave, luz, chips de cor.
   Personagem novo entra em **line-up ao lado dos existentes**, com 2–3 graus de estilização para escolher. Semelhança
   com pessoa real vem pelos traços (cabelo, roupa), nunca pela renderização: estilos misturados parecem mundos diferentes.
3. **Roteiro e beat sheet** (SKILL.md, seção 2).
4. **Um still por shot**, aprovado antes de animar.
5. **Movimento** (este arquivo).
6. **Som** e **montagem** no HyperFrames, com passe de cor.

## Shot Spec (um por plano)

```
SHOT: <id>   DURAÇÃO: <s>   FPS: <24>
HISTÓRIA: o que muda neste plano (expectativa → virada, se houver)
TEMPO: o que acontece em cada segundo (0–1s ..., 1–2,5s ..., 2,5–4s ...)
PERSONAGEM: ficha + pose inicial (e final, se FLF); tamanho no quadro (% da altura)
CENÁRIO: ficha + área; estado dos props (ex.: tábua lisa → uma marca → várias)
ESCALA: alturas em números (personagem vs. objetos)
CÂMERA: posição e movimento explícitos (travada | push-in 3% em 4s); plano (geral = onde, médio = ação, close = emoção)
ATUAÇÃO: o processo emocional quadro a quadro, não um rótulo ("pausa, respira fundo, ombros relaxam, levanta a
         cabeça, sorriso calmo" em vez de "fica feliz")
ROTA: i2v | primeiro+último quadro | trajetória | referência; modelo; seed(s)
```

## Rotas de geração (ComfyUI)

| Rota | Quando | Observação |
|---|---|---|
| **Imagem-para-vídeo (i2v)** | Ação simples a partir do still aprovado | Preserva o estilo do quadro inicial |
| **Primeiro + último quadro (FLF)** | Arco emocional pose A → pose B; segurar câmera | Mesma pose nas duas pontas = gesto que volta ao lugar, sem zoom |
| **Trajetória (Motion Track)** | Gesto com caminho e tempo exatos (mão pega objeto) | Trajetórias geradas por código; trava o 1º quadro pintado |
| **Referência / ingredientes** | Animatic e previz com elementos consistentes | Tende a puxar para o estilo dos dados do LoRA (ex.: 3D); não usar no final pintado |
| **Pose por vídeo de referência** | Atuação com peso e timing reais | Filmar uma pessoa atuando e transferir para o personagem |

Modelos de referência testados: LTX 2.5 (i2v, FLF, IC-LoRAs) roda numa GPU de 8 GB em int8 (~3–6 min por clipe
de 4s); Wan 2.2 5B é a opção leve. Modelos maiores ou 1080p: nuvem. Para prompts controlados, **desligue o prompt
enhancer** dos templates.

## Regras de prompt que funcionaram

- **Personagem grande no quadro.** Fundo de chroma é pixel desperdiçado: quadro vertical com o personagem a ~85% da
  altura. Prop pequeno em baixa resolução vira outra coisa (pincel virou cartão) → enquadrar maior, subir resolução e
  descrever o objeto explicitamente, repetindo o nome.
- **Câmera:** "The camera does not move or zoom" ajuda, mas não basta. Gestos em direção à câmera provocam zoom-in →
  pedir o gesto **para o lado** ("reaches to her side… stays the same size in the frame"). Zoom teimoso: FLF com a
  mesma pose nas duas pontas e "then settles back to the starting pose".
- **Ninguém além do personagem.** Citar outra pessoa ("a friend to his left") faz o modelo desenhá-la. Escreva
  "someone off-screen to the left of the frame" + "He is the only person in the frame; nobody else appears and
  nothing enters the frame".
- **Tudo no positivo.** Com modelos destilados (cfg 1), o negative prompt é ignorado.
- **Descreva o processo da ação**, com tempos (seção Shot Spec), não o resultado.
- **Duas seeds por ação.** Cerca de 1 em 4 clipes vem com zoom ou intruso.
- FLF costuma terminar o movimento antes do fim e congelar no quadro-âncora → aparar na montagem ou pedir mais ação.

## Chroma e composição

- Personagem sobre chroma liso, câmera travada; o cenário entra no compositor. Personagem que veste verde → chroma
  **magenta ou azul**.
- O modelo devolve o chroma deslocado (ex.: #00B140 vira ~RGB 0,170,60): **meça a cor real** no clipe antes de
  recortar. Recorte com `ffmpeg chromakey` + despill + erosão de 1 px no alfa.
- **Integre pela direção da luz, não pela média:** primeiro plano tem mais contraste que o fundo (perspectiva
  atmosférica). Ajuste leve de preto e saturação, aquecimento do lado do sol, gradiente sol → sombra, contorno de luz na
  borda voltada para a fonte, sombra projetada coerente e sombra de contato sob os pés.
- Crave os pés: se o modelo fizer push-in, compense escala e posição no compositor a partir de um ponto fixo.

## QA de clipe gerado

- Identidade e estilo iguais à ficha do início ao fim (cuidado com deriva de cor na pele e no cabelo).
- Fundo de chroma uniforme (desvio-padrão baixo); câmera parada de verdade.
- Nenhuma pessoa, objeto ou zoom que não foi pedido; props mantêm a forma.
- Movimento contínuo, sem saltos (diferença quadro a quadro).
- Registrar modelo, workflow, seed, prompt e resultado de cada clipe: os erros viram regra no Shot Spec seguinte.

## Máquina local (GPU de 8 GB)

- Feche o navegador antes de gerar: ele disputa RAM e dobra o tempo por passo. VAE decode estoura → tiles menores.
- Lote noturno: enfileire tudo antes de sair, mantenha o sistema acordado pedindo também a tela ativa (Modern
  Standby ignora só "sistema ativo") e ponha timeout em cada chamada da CLI (pode travar sem fim).
- Modelos com acesso restrito no Hugging Face: a pessoa aceita a licença e faz login; o agente não aceita termos.
