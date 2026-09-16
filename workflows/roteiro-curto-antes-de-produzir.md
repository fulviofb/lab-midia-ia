# Workflow: roteiro curto antes de produzir

Use este fluxo quando o vídeo **precisa de história** (personagens, conflito, virada). Não use para title card, motion graphic de produto ou aula que só encadeia tópicos.

Depois deste roteiro, volte ao guia de produção: `docs/guias/06-ideia-roteiro-cenas-video.md`.

Fonte de método (organização original, MIT): [`jtydhr88/screenwriting-skills`](https://github.com/jtydhr88/screenwriting-skills), commit pinado na avaliação. **Não instale o plugin. Não copie `reference.md`.** Piloto: `docs/testes/screenwriting-skills-piloto.md`.

## Quando parar e ir direto ao guia 06

- duração ≤ 15 s e só texto/logo;
- o “roteiro” é uma lista de fatos a mostrar;
- não há personagem que precise mudar de atitude.

## Recorte que este laboratório usa

Só isto — o restante das 26 skills fica de fora de shorts:

1. uma premissa;
2. um núcleo visível (objeto ou gesto sem o qual a peça cai);
3. cada cena vira um valor, senão corta;
4. diálogo como ação; não narrar a moral;
5. short ≠ longa (sem mapa de 110 páginas, sem 40 cards, sem “100 episódios”).

## 1. Premissa (uma frase)

Preencha:

```txt
[Quem] + [o que insiste em fazer] + [o que isso causa] + [o que muda no fim]
```

Testes:

- dá para dizer a um estranho em uma frase?
- se tirar o objeto/gesto central, a história ainda existe? Se sim, ainda não achou o núcleo;
- uma premissa só; a segunda ideia vira outro vídeo.

Tema (ajuda, medo, vaidade) pode ser comum. O que não pode ser comum é **como** a atitude do personagem muda.

## 2. Núcleo visível

Escolha **um** objeto ou gesto que a câmera possa filmar:

- carimbo que muda de mão;
- cadeira que alguém empurra;
- microfone que passa.

Regra: outra pessoa precisa **fazer algo** com esse objeto. Se só o protagonista o contempla, não é núcleo.

## 3. Quatro batidas (起承转合)

Para 30–90 s, quatro batidas bastam. Personagens ≤ 5.

| Batida | Função | Pergunta |
|---|---|---|
| Começo | Mostra o jeito antigo | O que o protagonista controla demais? |
| Desenvolvimento | O jeito antigo custa | Quem fica de fora? |
| Virada | O núcleo aparece em ação | O que o espectador vê, sem narração? |
| Fecho | Atitude nova, visível | O protagonista faz o que não fazia no começo? |

Não escreva o fecho como cartaz (“Ajudar é…”). Mostre o ofício já dividido.

## 4. Lista de cenas

Uma linha por cena:

```txt
# | lugar | uma frase | valor abre → fecha | batida
```

Corte se:

- o valor não muda (cena de explicação);
- dois personagens concordam o tempo todo;
- a fala poderia ir para qualquer boca.

## 5. Diálogo

Três perguntas por fala:

1. O personagem **quer** o quê agora?
2. Que **ação** a frase tenta fazer (recusar, pedir, ceder, desviar)?
3. Dá para cortar a frase e deixar só o gesto?

Evite:

- narrar a moral em voz off;
- um personagem explicar o tema para o outro;
- “você sabe que…”.

Exceção: cartão institucional **depois** do corte, se a peça exigir marca — não no lugar da virada.

## 6. Passagem para produção

Com a lista de cenas aprovada:

1. virar tabela de tempos do guia 06;
2. escolher HyperFrames ou Remotion;
3. validar e renderizar como no guia.

Não pule o storyboard de produção. Este workflow não substitui lint/snapshot/`ffprobe`.

## Diagnóstico rápido (depois do draft)

- [ ] Uma premissa.
- [ ] Núcleo visível; outra pessoa age sobre ele.
- [ ] Cada cena muda um valor.
- [ ] Fecho é ação, não slogan.
- [ ] Sem mapa de longa nem plugin instalado.

## O que não fazer

- Instalar as 26 skills no agente.
- Copiar citações de livros/roteiros do upstream.
- Aplicar estrutura de série adulta a um short de 60 s.
- Tratar este arquivo como autorização para adaptar obra de terceiros.
