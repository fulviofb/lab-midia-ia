# Vídeo de abertura — aula sobre IA na produção de animações

**Estado:** rascunho de conceito, ainda não aprovado nem produzido. Os campos marcados **A DEFINIR** dependem do mantenedor.

Referência de linguagem: [Maestros da IA — vídeo por código que se explica por dentro](../precedentes/video-generativo/maestros-da-ia-video-explicado-por-dentro.md). Daquele vídeo aproveitamos a forma (o vídeo demonstra o próprio processo). Não aproveitamos roteiro, artes, trilha, nem a tese do "prompt único".

## Ideia

A aula começa com um plano animado bonito, em tela cheia, sem explicação. Em seguida o vídeo se desmonta na frente da turma e mostra de que é feito: a arte que uma pessoa desenhou, o plano que a IA animou, a pincelada que o código pintou, a voz, a trilha, as tentativas que não serviram e quanto custou. Fecha dizendo o que nenhuma ferramenta fez, e entrega a aula.

Em uma frase: **a abertura é o primeiro exemplo da aula, e todos os dados que ela mostra são verdadeiros.**

## O que muda em relação à referência

| Na referência | Na nossa abertura | Por quê |
|---|---|---|
| 7 min 35 s, vídeo completo | 75 a 90 s, só abertura | A aula é que explica; o vídeo abre o apetite |
| "1 prompt, 0 correções" | "N tentativas, M aproveitadas, X rodadas" | É o que acontece de verdade, e é o que a turma precisa saber antes de começar |
| Avatar apresentando | Sem apresentador; a animação é a protagonista | O assunto é animação, e quem apresenta está na sala |
| Voz clonada | **A DEFINIR:** voz própria gravada, ou TTS sinalizado | Critério de transparência e de respeito |
| Selo "FEITO COM…" como estética técnica | Selo como compromisso de transparência | Liga com os 5 critérios da aula da EFAS |
| Planos de 1,5 a 3 s | Cerca de 5 s por ideia | Público de sala, primeira vez vendo o assunto |
| Fundo escuro, estética de painel | Papel e aquarela, a estética dos testes do laboratório | Coerência com o que a aula ensina a fazer |
| Fecha em chamada para comunidade paga | Fecha no título da aula | Princípio da gratuidade |

## BRIEF

```
PEÇA: abertura-aula-ia-animacao          MARCA/ESTILO: A DEFINIR (proposta: papel + aquarela)
TIPO: misto (motion por código + planos gerados)      FORMATO: 16:9 1920x1080, 30 fps
OBJETIVO: a turma entende em 90 s que uma animação com IA é montagem de camadas e escolhas,
          e quer aprender cada camada.
PÚBLICO: A DEFINIR (proposta: pessoas que nunca animaram, com ou sem experiência em IA)
DURAÇÃO: pela narração, alvo 75–90 s     PROMESSA: "tudo o que você viu aqui, você vai saber de onde veio"
MOMENTOS: 1 plano animado em tela cheia · 2 o quadro se desmonta em camadas · 3 cada camada
          mostra sua origem · 4 as tentativas e os números · 5 o que ficou com a gente
CTA / FECHO: título da aula
DADOS REAIS: tentativas, aproveitamento, tempo e custo medidos na produção deste vídeo
             (log de geração). Sem medição, o número não entra.
ASSETS: A DEFINIR — arte de origem com autorização de uso (ver "Decisões em aberto")
ÁUDIO: narração + trilha licenciada ou gerada + SFX discretos
PROIBIDO: número sem fonte; rosto ou voz de terceiros; qualquer menção a serviço pago como recomendação
PRAZO / REVISOR: A DEFINIR
```

## Roteiro em batidas

Tempos de referência a 30 fps, para ajustar à narração gravada (a voz é a timeline).

| Tempo | Batida | Imagem | Narração (rascunho) | Selo |
|---|---|---|---|---|
| 0–8 s | **Encanto** | Plano-herói animado em tela cheia. Sem texto, só trilha. | — | entra aos 6 s: `PLANO ANIMADO POR IA · tentativa 2 de 4` |
| 8–14 s | **Virada** | O plano congela num quadro. | "Ninguém desenhou este movimento quadro a quadro. E também não foi um pedido só." | o mesmo |
| 14–26 s | **Desmontagem** | O quadro inclina e se separa em camadas rotuladas: ARTE ORIGINAL · PERSONAGEM · CENÁRIO · PINCELADA · LETRA · SOM. | "Uma animação é uma pilha de camadas. Cada uma veio de um lugar." | `COMPOSIÇÃO POR CÓDIGO` |
| 26–34 s | **A mão** | A camada ARTE ORIGINAL vem à frente: a ilustração parada, como foi desenhada. | "Começa numa arte feita por alguém." | `ILUSTRAÇÃO DE <autor>, usada com autorização` |
| 34–44 s | **O plano gerado** | Folha de contato das tentativas do plano-herói; as recusadas ficam riscadas, com o motivo em duas palavras (rosto mudou, câmera andou). | "A IA anima. Nem sempre do jeito pedido. Escolher faz parte." | `IMAGEM → VÍDEO · <modelo>` |
| 44–52 s | **O código** | Uma pincelada se pinta sozinha; ao lado, as poucas linhas que a desenham. | "O que precisa ser exato, a gente escreve." | `PINCEL POR CÓDIGO · <motor>` |
| 52–60 s | **O som** | Onda da voz; a trilha desce quando a fala entra. | "E metade do que você sente vem do som." | `NARRAÇÃO: <voz própria ou TTS> · TRILHA: <origem>` |
| 60–72 s | **Os números** | Painel com dados medidos: planos tentados, aproveitados, rodadas de revisão, horas, custo. Ao lado, duas colunas: "já existia" e "nasceu para este vídeo". | "Este vídeo levou … tentativas, … rodadas e custou …" | `NÚMEROS MEDIDOS · <data>` |
| 72–82 s | **O que ficou com a gente** | As camadas se recompõem no plano-herói, que volta a andar. Duas palavras: A IDEIA · O CRIVO. | "A ferramenta executa. A ideia e o crivo continuam nossos." | — |
| 82–90 s | **Entrega** | Cartão com o título da aula. | "Hoje a gente monta esse caminho, camada por camada." | — |

Notas de direção:

- **Elemento que costura:** o plano-herói. Ele abre, é desmontado, e fecha recomposto. Não usar transição genérica entre batidas; cada camada sai da pilha e volta para ela.
- **Selo de procedência:** canto inferior esquerdo, sempre no mesmo lugar e tamanho, gerado a partir dos mesmos dados que montam a cena. Fora da zona do personagem.
- **A desmontagem acontece uma vez.** É o momento mais forte da referência e perde efeito se repetido.
- **"O crivo"** substitui "o gosto" da referência: além de julgar se ficou bom, julgar se está fiel, respeitoso e sereno. Trocar a palavra se a aula não for para o público espírita.
- **Glossário:** se a aula tiver termos novos (quadro-chave, imagem-para-vídeo, composição, semente), um contador discreto `TERMOS 1/6` no canto superior direito prepara o vocabulário. Opcional; cortar se pesar.

## Como produzir com o que o laboratório já tem

| Camada | Rota já testada | Onde está |
|---|---|---|
| Direção, briefing, rodadas | Skill de direção de vídeo | `skills/direcao-de-video/` |
| Plano-herói animado | LTX local primeiro; nuvem só no plano que o local não resolver | `docs/testes/ltx-local-x-kling-planos-animados-teste.md` |
| Personagem separado do cenário | Personagem em chroma + composição | `docs/testes/chroma-composite-aquarela-teste.md` |
| Pincelada por código | p5.brush ou motor lemo | `docs/testes/p5brush-vs-lemo-pincel-teste.md`, `examples/comparativo-pincel/` |
| Montagem, camadas, selos, painel | HyperFrames | `workflows/hyperframes-video-html.md` |
| Narração | Voz própria, ou TTS local sinalizado | `docs/guias/05-narracao-com-ia-etica.md` |
| Registro das tentativas | Log de geração | `templates/log-de-geracao.csv` |
| Conferência final | Revisão de montagem | `templates/revisao-de-montagem.md` |

Ordem de trabalho:

1. Responder às decisões em aberto e fechar o BRIEF.
2. Escolher o plano-herói. Se já existir um plano aprovado de um teste anterior com tentativas registradas, a batida "o plano gerado" já tem material verdadeiro.
3. **Abrir o log de geração antes da primeira tentativa.** Os números da batida 60–72 s saem dele; não dá para reconstruir depois.
4. Gravar ou gerar a narração e travar a timeline por ela.
5. Montar em etapas: quadros parados de cada batida → aprovação → movimento → som.
6. Duas a quatro rodadas de revisão com notas por tempo.
7. Conferência: selo presente e correto em toda cena, nada sobre o personagem, narração igual ao roteiro, todo número com origem no log.

## Decisões em aberto

1. **Qual aula, para quem e quando.** Define vocabulário, duração e se "o crivo" fica.
2. **Arte de origem.** As páginas do livro ilustrado dos testes podem aparecer em público? Precisa de autorização de quem ilustrou e de crédito no selo. Sem isso, usar arte própria feita para o vídeo.
3. **Narração.** Voz própria gravada (recomendado: é a mais coerente com o critério de transparência) ou TTS sinalizado.
4. **Só ferramentas gratuitas?** Se a aula seguir o princípio da gratuidade, o plano-herói sai do gerador local e o custo mostrado no painel é zero, o que por si já é um argumento da aula.
5. **Duração.** 75–90 s como abertura, ou uma versão de 3–4 min que também sirva sozinha no YouTube.
6. **Estética.** Papel e aquarela (proposta) ou a identidade de um kit em `skills/direcao-de-video/references/marcas/`.
