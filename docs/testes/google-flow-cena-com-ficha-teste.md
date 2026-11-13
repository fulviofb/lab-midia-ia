# Teste: uma cena no Google Flow com ficha de personagem própria

Data: 2026-11-13

## Objetivo

Medir o que o [precedente da AI Madame](../precedentes/video-generativo/ai-madame-flow-historia-em-feltro.md) não informa: tentativas, créditos, fidelidade a uma ficha de personagem já existente, voz de narrador em português e texto com acentos gerado dentro do vídeo.

## Ambiente

- Google Flow, plano Pro, 1.050 créditos no início do teste
- Imagens: Nano Banana 2.1, 16:9, nível de raciocínio alto
- Vídeo: Omni 1.2 Flash, modo "Elementos", 720p, 10 s, uma geração por vez
- Personagem: ficha própria em estilo de animação clássica (frente, três quartos, perfil, costas e expressões), de um professor do início do século XX, gerada antes em outra ferramenta
- A skill do tutorial não foi usada: os pedidos foram escritos para este teste

## Passos

1. Subir a ficha e criar um personagem a partir dela, sem voz e com uma descrição que diz que ele nunca fala.
2. Gerar uma imagem de estilo com a ficha como referência.
3. Gerar a ficha do lugar (sala de aula vazia).
4. Gerar a fachada de um prédio a partir de uma foto histórica, com a ficha como referência de estilo.
5. Gerar uma cena de 10 s com dois elementos (personagem e sala), narração em português pedida no texto e uma frase escrita a giz no quadro.

## Resultados

### Imagens: 0 créditos

| Rodada | Geradas | Resultado |
|---|---|---|
| Imagem de estilo (rua) | 4 | Traço correto. Conteúdo reprovado pelo mantenedor: o pedido descrevia uma cidade genérica, sem base em fonte. |
| Sala, rodada 1 (só a imagem de estilo como referência) | 4 | Reprovada: saiu com textura e luz realistas, diferente da ficha; uma das quatro trouxe um crucifixo na parede, que ninguém pediu. |
| Sala, rodada 2 (imagem de estilo + ficha, pedido mais firme) | 4 | Aprovada: contorno e cor chapada, quadro vazio, sala sem ninguém, paredes sem símbolos. |
| Fachada a partir de foto histórica | 4 | Aprovada: fiel à arquitetura da foto, sem pessoas e sem letreiro. Nenhuma tem porta, porque a foto não mostra. |

### Cena de 10 s: 30 créditos

| Item | Resultado |
|---|---|
| Tentativas até a primeira aproveitável | 1 |
| Personagem igual à ficha | Sim: cabelo, bigode, terno de três peças e gravata |
| Câmera parada | Sim |
| Gente ou objeto não pedido | Não |
| Texto no quadro | Correto, com "ç" e "ã", escrito aos poucos |
| Boca fechada, como pedido | Sim, nos quadros conferidos (um por segundo) |
| Narração | Em português do Brasil; aprovada de ouvido. A transcrição automática ouviu um artigo a mais em relação ao texto pedido. |
| Entrega | 1920×1080, 24 fps |
| Defeitos | Entre 5 s e 6 s o personagem muda de posição rápido demais; um livro aparece e some de cima da mesa. |

Conferência: folha de quadros a 1 quadro por segundo e transcrição local do áudio (Whisper).

### Segunda cena, com corte entre dois lugares: 30 créditos

Três elementos (personagem, sala e fachada) e a instrução de dois planos: 3 s de exterior, corte, 7 s de interior. Por um erro na montagem do pedido, ele foi enviado **sem** o trecho da narração e sem a frase do quadro.

| Item | Resultado |
|---|---|
| Corte entre dois lugares numa geração | Funcionou: 3 s de fachada parada, corte seco, 7 s de sala |
| Personagem igual à ficha | Sim |
| Gesto completo em 7 s | Sim |
| Texto no quadro | Rabisco ilegível, como esperado sem a frase no pedido |
| Narração | Nenhuma, como esperado sem voz no pedido: só som ambiente (−44 dB de média, contra −16 dB na primeira cena) |

O que isso mostra: o gerador não acrescentou narração nem frase por conta própria. Voz e texto só aparecem quando são pedidos.

## Diferenças em relação ao tutorial

- O modo de "ingredientes" aparece como **Elementos**. Há também **Frames** (primeiro e último quadro).
- Não foi possível renomear imagens soltas; os elementos foram escolhidos pela miniatura. Só o personagem recebeu nome.
- A escolha de voz não aparece no painel do vídeo; a voz foi descrita no texto do pedido.
- Vídeo de 8 s custou 24 créditos; de 10 s, 30.

## O que aprendemos

- **Imagem de graça, vídeo pago.** Neste plano, o custo ficou todo no vídeo. Isso reforça a ordem "imagem primeiro, vídeo depois".
- **Duas referências seguram o estilo melhor que uma.** A sala só entrou no traço certo quando o pedido levou a imagem de estilo e a ficha do personagem, e disse o que não queria (textura fotográfica, luz realista).
- **O gerador põe símbolos por conta própria.** Uma sala de escola antiga veio com crucifixo. Em material de casa espírita, a lista do que não pode aparecer precisa estar no pedido, e a conferência continua sendo de pessoa.
- **Lugar com base em fonte.** A rua inventada foi reprovada; a fachada feita sobre uma foto histórica foi aprovada. Para lugar real, partir de documento.
- **Pessoas da foto de referência não entram.** O pedido mandou não copiar ninguém da fotografia e deixar o letreiro de fora; o nome do prédio entra depois, por código, com a grafia original.
- **Um anexo a mais muda a cena.** A fachada foi retirada dos elementos antes de gerar a cena interna, para o gerador não misturar os dois lugares.

## Limites deste teste

- Uma cena só, com um personagem só. Não mede consistência entre várias cenas, nem cena com duas pessoas.
- A mesma voz em todas as cenas não foi testada: sem lista de vozes, depende do texto do pedido.
- Créditos de serviços diferentes não são comparáveis entre si. Ver o [teste LTX local x Kling](ltx-local-x-kling-planos-animados-teste.md) para as outras rotas.
- O Google Flow é serviço que pode cobrar. Ver `docs/estrategia/principio-da-gratuidade.md`.

## Próximos testes

- Quatro cenas seguidas com o mesmo personagem e a mesma voz.
- Repetir a cena com corte com o pedido completo, para saber se voz e texto se mantêm quando há dois planos.
- Uma cena com duas pessoas.
