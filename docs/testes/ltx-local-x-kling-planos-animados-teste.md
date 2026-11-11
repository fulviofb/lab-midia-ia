# Teste: planos animados de um livro ilustrado, LTX 2.5 local x Kling 2.5

Data: 2026-10-25

## Objetivo

Animar planos curtos a partir das páginas prontas de um livro infantil ilustrado (lápis de cor + aquarela) para um clipe musical de cerca de 80 s, e descobrir:

1. quanto dá para fazer de graça, com um gerador local;
2. em que tipo de plano vale pagar um gerador na nuvem;
3. quanto custa errar.

O clipe é um caso "misto": a base é motion sobre as artes originais (câmera, letra na tela) e só alguns planos-herói são animados por IA.

## Ambiente

- Windows 11, notebook com RTX 4060 Laptop (8 GB de VRAM) e 32 GB de RAM
- ComfyUI Desktop 0.34, template `video_ltx2_5_i2v` (e `video_ltx2_5_flf2v` para primeiro + último quadro), arquivos int8, operado pelo `comfy-cli`
- Kling 2.5 pelo Magnific (pago em créditos)
- Montagem no HyperFrames

## Critério de aprovação

Câmera parada como pedido, rosto e roupa iguais ao livro, ninguém inventado, gesto legível e crivo da casa (nada que fuja dos princípios do material).

## Rodada 1: LTX 2.5 local, imagem para vídeo

9 planos × 2 sementes, em 1 h (~3,5 min por clipe de 7 s). Custo: zero.

| Tipo de plano | Resultado |
|---|---|
| Abraço de duas pessoas | Aprovado nas duas sementes |
| Abraço de três pessoas | Aprovado |
| Irmãos andando de mãos dadas | Aprovado |
| Luz do sol no tapete | Usável: a câmera aproxima sozinha ~25% |
| Criança segurando um livro | Usável: aproximação forte no fim |
| Avô sentado, crianças em volta | Só os 4 s iniciais: depois as crianças cobrem o rosto dele |
| Ciranda de 5 crianças | **Reprovado**: as crianças se fundem e trocam de lugar |
| Avô explicando, close com espaço vazio | **Reprovado**: a câmera recua e inventa uma criança com roupa errada |
| Crianças com as mãos para cima | **Reprovado**: a câmera anda e inventa estante e crianças |

## Rodada 2: LTX 2.5 local, primeiro e último quadro iguais (FLF)

Mesmo quadro como início e fim, para travar a câmera. Custo: zero.

| Plano | Resultado |
|---|---|
| Luz do sol no tapete | **Aprovado**: câmera travada, a luz cintila e as crianças se mexem |
| Criança segurando um livro | **Aprovado**: o livro não se move (0 px medido) |
| Crianças com as mãos para cima | Usável: câmera travada, mas um menino muda de corpo no meio |
| Avô explicando | **Reprovado** de novo |

## Rodada 3: Kling 2.5 na nuvem

650 créditos por clipe de 10 s.

| Plano | Resultado |
|---|---|
| Raio de sol entrando (tinha uma versão LTX "usável") | **Aprovado**: gesto mais vivo, 1080p, câmera e personagens mantidos |
| Avô explicando | **Aprovado**: câmera parada; ele fala, pisca e gesticula |
| Ciranda de 5 crianças | **Reprovado**: depois do 1º segundo aparecem 7 crianças e a protagonista fica de costas. Os 650 créditos foram perdidos e a cena ficou com a arte parada. |

Um vídeo lado a lado do mesmo plano (LTX × Kling) ficou guardado no projeto como material de aula.

## O que aprendemos

- **O gerador local acerta gesto pequeno, câmera parada e poucas pessoas** (abraço, andar de mãos dadas).
- **Ele falha em grupo em movimento e em close com muito espaço vazio:** a câmera "procura" e inventa gente.
- **"The camera does not move" não basta.** Primeiro + último quadro iguais (FLF) travou a câmera em 2 de 4 planos que tinham falhado.
- **A nuvem é melhor, mas não é garantia.** O Kling resolveu dois planos que o LTX não resolveu e errou feio na ciranda. Errar em vídeo custa o clipe inteiro.
- **Imagens sagradas nunca são geradas:** em todo plano com uma figura religiosa, a página original entra por cima do vídeo como máscara, para o gerador nunca redesenhar a figura.

## Regra de custo que saiu daqui

1. Primeiro, todos os planos no gerador local, com 2 sementes cada.
2. O que falhar vai para FLF, ainda local.
3. Só o que continuar falhando vai para a nuvem, um plano por vez, com aprovação de custo.
4. Plano de grupo em movimento (ciranda, roda, multidão) não vale a aposta: fica com a arte parada e câmera.

Resultado do clipe: 7 planos animados (5 locais, 2 na nuvem) e o resto em motion sobre as artes originais. Gasto na nuvem: 3 × 650 = 1.950 créditos, dos quais 650 se perderam.

## Relacionados

- [Teste de personagem em chroma + composição](chroma-composite-aquarela-teste.md)
- [Direção cinematográfica por referência](../../workflows/direcao-cinematografica-por-referencia.md)
