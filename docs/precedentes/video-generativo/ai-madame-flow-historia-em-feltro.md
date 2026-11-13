# AI Madame — história em feltro no Google Flow, com uma skill que escreve os pedidos

## Identificação e limites

- Fonte: <https://www.youtube.com/watch?v=bFcXHCVQUU0>
- Autor: canal AI Madame.
- Formato: 16:9, 7 min 36 s, inglês, 14 capítulos.
- Assunto: tutorial de um vídeo de história narrada, em estilo de feltro, gerado no Google Flow. Os pedidos são escritos por uma skill para o Claude, distribuída gratuitamente pela autora.
- Interesse comercial: canal próprio, site e ferramenta da autora. A skill é gratuita, mas está hospedada no site dela.
- Classe de transparência: `methodological_breakdown`.
- Estado: `observed_public_precedent`, limitado ao que o vídeo mostra e afirma.
- Teste pelo laboratório: uma cena, em 2026-11-13, com pedidos próprios: [resultado](../../testes/google-flow-cena-com-ficha-teste.md). A skill não foi baixada nem lida.
- Política de cópia: link e síntese própria. Não reproduzir os pedidos, a skill, as artes ou a narração.
- Data da coleta: 2026-11-13.

**Como a coleta foi feita.** Leitura da descrição, dos capítulos e da transcrição automática do YouTube. Depois, conferência visual em folhas de quadros (um a cada 8 s) tiradas de uma cópia que o mantenedor baixou para análise privada; nada foi redistribuído e a skill da autora não foi baixada. Nomes de modelos e de opções da interface vêm da fala e da tela do vídeo e podem estar desatualizados: confira no Flow antes de citar.

## O que a fonte permite afirmar

| Tipo | Registro |
|---|---|
| Observado | Dois filmes curtos completos (a espada na pedra; os primeiros balões, 1782–1783), narrados, com texto na tela, em estilo de feltro. Biblioteca de assets do projeto no Flow com imagem de estilo, personagens, objetos e lugares. Cenas geradas uma a uma, com os assets marcados no pedido. O texto na tela é gerado dentro do próprio vídeo, como letras de feltro. O projeto no Flow separa a biblioteca em imagens, personagens e cenas, e os assets têm nome próprio, escolhido numa lista na hora de montar o pedido. O pedido inicial ao modelo de linguagem é uma frase só (tema, duração, público), e a resposta traz as cenas com a fala e o texto de tela, seguidas da lista de assets a gerar depois da aprovação. |
| Declarado pela autora | Os primeiros pedidos, escritos sem método, falhavam; cada falha foi documentada e virou regra da skill; com a skill, as cenas "funcionam de primeira". A skill serve em outros modelos de linguagem se o arquivo for descompactado e colado na conversa. |
| Inferido pelo laboratório | O que dá consistência não é a ferramenta: é a ordem (plano → imagem de estilo → fichas → conferência → cenas) e o registro de falhas transformado em regra. |
| Não informado | Quantas tentativas cada cena levou, custo em créditos, plano de assinatura, tempo total, quanto foi editado fora do Flow. |
| Não comprovado | "Funciona de primeira"; repetibilidade com outro estilo ou com personagens humanos realistas. |

## O fluxo mostrado

1. **Uma linha de pedido** para o modelo de linguagem: do que trata a história, quanto dura, para quem é.
2. **Poucas perguntas de volta:** visual geral, clima de cor, como o narrador soa.
3. **Roteiro inteiro antes de qualquer pedido de imagem:** todas as cenas, a fala exata do narrador e o texto na tela. A autora lê, corrige e só então segue.
4. **Imagem de estilo:** uma imagem-chave, 16:9, que trava o visual e as cores do filme inteiro.
5. **Fichas:** uma imagem limpa de cada personagem, objeto importante e lugar, sempre com a imagem de estilo anexada como referência e um pedido por item.
6. **Conferência dos assets pelo modelo de linguagem:** as imagens voltam para a conversa. No exemplo, ele percebe passageiros desenhados dentro do cesto de um balão, que apareceriam em cenas erradas; o balão é refeito vazio.
7. **Cenas, uma por vez:** no Flow, modo de "ingredientes", 10 segundos por cena; o pedido marca com `@` a imagem de estilo, o personagem e o lugar daquela cena.
8. **Uma voz só:** a mesma voz de narrador escolhida em todas as cenas, para a narração soar como uma pessoa do começo ao fim.
9. **Conferir cada cena antes da próxima.**

Modelos citados no vídeo: um modelo de imagem para os assets e um modelo de vídeo com áudio para as cenas, ambos dentro do Flow. Os nomes exatos estão no vídeo e mudam com frequência.

## Práticas transferíveis e condições de uso

| Prática | Pode ajudar quando | Quando dispensar ou adaptar | Limite |
|---|---|---|---|
| **Roteiro com fala e texto de tela antes de qualquer imagem** | Sempre que houver narração | Peça sem fala | Já é regra do laboratório (`workflows/roteiro-curto-antes-de-produzir.md`) |
| **Imagem de estilo única como referência de tudo** | Vários personagens e lugares precisam parecer do mesmo mundo | Peça de um plano só | Não substitui a ficha de cada personagem |
| **Uma ficha por personagem, objeto e lugar, com fundo limpo** | Qualquer história com mais de uma cena | — | Conferir se a ficha não traz "passageiros": gente ou objetos que não pertencem a ela |
| **Devolver os assets ao modelo de linguagem para conferência** | Há muitos assets e pouco tempo de revisão | Poucos assets, revisados por pessoa | É uma segunda leitura, não substitui o crivo humano |
| **Marcar os assets no pedido da cena** | A ferramenta aceita referências nomeadas | Ferramenta sem esse recurso | Só entra na cena o que foi marcado |
| **Uma voz de narrador para todas as cenas** | A ferramenta gera a narração junto com o vídeo | Narração gravada à parte | Voz gerada precisa ser sinalizada |
| **Registro de falhas que vira regra** | Toda produção com mais de uma rodada | — | É o equivalente do nosso `templates/log-de-geracao.csv` com uma coluna de "regra que evita" |
| **Estilo de feltro ou massinha** | Público infantil; personagens simples | Rosto realista ou pessoa real | Estilos de material "perdoam" pequenas diferenças entre cenas |

## Crítica do laboratório

- **"Funciona de primeira" é afirmação da autora.** O vídeo mostra as falhas de antes da skill (o rei parecido com o Papai Noel, o personagem que segura a espada em vez de puxá-la), mas não mostra a contagem de tentativas depois dela.
- **O ganho real é de método, e ele já está no laboratório:** imagem primeiro, fichas, conferência, uma cena por vez. O que o vídeo acrescenta é a imagem de estilo única, a conferência das fichas pelo modelo de linguagem e a ideia de transformar cada falha numa regra escrita.
- **A skill é um arquivo de terceiro.** Antes de usar, é preciso baixar, abrir e ler o conteúdo. Não foi feito nesta coleta.
- **A narração é gerada pela própria ferramenta de vídeo.** Isso simplifica muito para quem começa, mas tira o controle fino da voz e exige o aviso de que é voz sintética.
- **Texto na tela gerado por IA** costuma errar letras. O vídeo mostra datas e nomes de lugar na imagem; em português, com acentos, vale testar antes de confiar.

## Relação com o que o laboratório já tem

- A ordem "imagem primeiro, vídeo depois" e a regra de custo: `docs/testes/ltx-local-x-kling-planos-animados-teste.md`.
- Roteiro antes de produzir: `workflows/roteiro-curto-antes-de-produzir.md`.
- Direção e rodadas: `skills/direcao-de-video/`.
- O que é novo: o Google Flow como rota de geração para quem já tem créditos nele, com assets nomeados e narração embutida. **Ainda não testado pelo laboratório.**

## Teste proposto

Uma cena só, com material próprio, para medir o que o vídeo não informa:

1. Imagem de estilo + uma ficha de personagem + uma ficha de lugar, já existentes.
2. Uma cena de 10 s com narração em português.
3. Registrar: tentativas até a primeira cena aproveitável, créditos gastos, fidelidade à ficha, qualidade da voz em português, e se o texto na tela sai correto.
4. Comparar com a rota local (LTX) e com a nuvem já testada.

## Fronteira com a Concafras

Este registro é uma análise de fonte com interesse comercial próprio. Não é divulgação do canal, do site ou das ferramentas citadas. O Google Flow é um serviço que pode cobrar: avise antes, sem recomendação de compra. Ver `docs/estrategia/principio-da-gratuidade.md`.
