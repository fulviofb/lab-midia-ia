# Maestros da IA — vídeo por código que se explica por dentro

## Identificação e limites

- Fonte: <https://youtu.be/WuzMxEKJHkQ>
- Autor: comunidade Maestros da IA (identificação visível no próprio vídeo).
- Formato: 16:9, 7 min 35 s, português, 9 capítulos numerados.
- Assunto: o vídeo explica como ele mesmo foi produzido por código, a partir de um pedido a um modelo de linguagem.
- Interesse comercial: o fechamento divulga uma comunidade paga do autor. Não é patrocínio de terceiro, mas é material promocional.
- Classe de transparência: `methodological_breakdown`.
- Estado: `observed_public_precedent`, limitado ao que o vídeo mostra e afirma.
- Teste pelo laboratório: não realizado.
- Política de cópia: link e síntese própria. Não reproduzir o prompt, o roteiro, as artes, a trilha ou o avatar.
- Data da coleta: 2026-11-12.

**Como a coleta foi feita.** O vídeo foi analisado em duas passadas por um modelo multimodal (Gemini 3.5 Flash, leitura do link público), com perguntas diferentes, e as respostas foram comparadas. Nenhum arquivo foi baixado. A amostragem é de cerca de um quadro por segundo, então textos pequenos, números e versões transcritos abaixo podem conter erro de leitura. Antes de citar qualquer número em aula, confira no vídeo.

## O que a fonte permite afirmar

| Tipo | Registro |
|---|---|
| Observado | Estrutura em capítulos; apresentadora em avatar sobre fundo real; motion 2D, cenas 3D, vídeo de banco, telas de código; selo "FEITO COM…" em todas as cenas; trilha com ducking; capítulo de conferência com erros "antes e depois"; painel de números no fim. |
| Declarado pelo autor | Tudo teria saído de 1 prompt, em 3 h 48 min, sem correção humana: 7.874 linhas de código em 89 arquivos, 91 cenas, 13.671 quadros, 312 deixas de som, 3.196 quadros conferidos. Avatar, voz clonada, contas nos serviços e um motor anterior de 419 linhas já existiam. |
| Inferido pelo laboratório | A força do vídeo vem menos da automação e mais de decisões de direção: mostrar o processo, rotular cada cena, medir e conferir. Essas decisões valem para qualquer pipeline. |
| Não informado | Quantas execuções vieram antes da que foi publicada, custo em créditos e assinaturas, hardware, o que o motor anterior já resolvia, quanto do prompt estruturado foi escrito e refinado por pessoa. |
| Não comprovado | "0 correções humanas", repetibilidade com outro tema, e que o mesmo resultado saia sem o avatar, a voz e o motor que já estavam prontos. |

## Estrutura do vídeo

| Tempo | Capítulo | O que acontece |
|---|---|---|
| 00:00–00:37 | Abertura | Afirma a premissa, mostra o pedido num terminal, declara que rosto e voz são sintéticos, desmonta o quadro em camadas e promete os números no fim. |
| 00:37–01:42 | 01 Vídeo virou texto | Quadros por segundo, quadros-chave, interpolação e curvas de aceleração. |
| 01:42–02:37 | 02 As ferramentas | Bibliotecas de animação por código; a mesma frase em quatro motores; caminho modelo → código → navegador sem tela → quadros → FFmpeg → MP4. |
| 02:37–02:56 | 03 Três dimensões | Câmera, luz e sombra numa cena 3D com o avatar integrado. |
| 02:56–04:13 | 04 Ver, ouvir e ler | Alinhamento da fala palavra a palavra, lista de cortes, pontos do rosto, zona protegida, recorte de pessoa, rastreamento, texto preso ao chão, OCR. |
| 04:13–04:43 | 05 Material de fora | Busca em banco de vídeo por API, escolha, correção de cor, imagens dispostas no espaço 3D. |
| 04:43–05:24 | 06 O som | Voz, efeitos criados por descrição, trilha em blocos do tamanho dos capítulos, ducking, normalização em −14 LUFS. |
| 05:24–05:47 | 07 A conferência | O modelo revisa o render: sobreposição no rosto, transcrição comparada ao roteiro, dois erros reais corrigidos. |
| 05:47–06:36 | 08 Os números | Painel de métricas, o que já existia e o que nasceu do pedido, e o que continua humano: a ideia e o gosto. |
| 06:36–07:35 | 09 E você? | Usos possíveis, glossário dos 12 termos, divulgação da comunidade, pergunta para os comentários, créditos. |

## A abertura, plano a plano

Os primeiros 37 segundos carregam o vídeo inteiro. A ordem é:

1. **Afirmação** (cerca de 4 s): apresentadora em plano médio, título grande sobreposto.
2. **Prova** (3 s): o pedido aparece num terminal e recebe um carimbo.
3. **Inventário** (12 s): cartões numerados listam o que foi produzido (narração, animação, 3D, trilha, cortes).
4. **Confissão** (5 s): a apresentadora diz que ninguém a gravou; malha de pontos sobre o rosto, onda da voz.
5. **Desmontagem** (9 s): o quadro inclina em 3D e se separa em camadas rotuladas (som, selos, pessoa, texto, fundo).
6. **Promessa** (4 s): os números aparecem trancados, "no final", e entra o cartão do capítulo 1.

## Práticas transferíveis e condições de uso

| Prática | Pode ajudar quando | Quando dispensar ou adaptar | Limite |
|---|---|---|---|
| **O vídeo é a própria demonstração** | O tema é um processo de produção | O tema não tem relação com o modo de fazer | Só funciona se o que é mostrado for verdadeiro |
| **Selo de procedência em cada cena** | Há várias técnicas misturadas e o público quer saber qual é qual | Peça curta de uma técnica só | O selo precisa ser gerado da mesma fonte que monta a cena, senão desatualiza |
| **Desmontar o quadro em camadas** | É preciso mostrar que uma imagem é composição | Imagem de camada única | Use uma vez; repetido vira enfeite |
| **Declarar cedo o que é sintético** | Há avatar, voz clonada ou imagem gerada | — | No laboratório é obrigação, não recurso de estilo |
| **Promessa aberta no começo, paga no fim** | Há dados reais para mostrar | Não há medição | Não prometer o que não foi medido |
| **Do alicerce ao topo** | Público leigo | Público técnico | Cada capítulo com uma ideia só |
| **Glossário com contador** (termos 1/12) | Aula ou explicativo com vocabulário novo | Peça institucional | Até cerca de 12 termos |
| **Cartão de capítulo numerado** | Mais de 2 minutos | Vinheta | — |
| **Texto entra na palavra falada** | Há narração | Sem narração | Exige tempo de cada palavra (alinhamento forçado ou transcrição com marcação) |
| **Zona protegida do rosto** | Há pessoa ou personagem em quadro | Só gráficos | Conferir no render, não só no layout |
| **Trilha em blocos por capítulo, com ducking** | Narração longa | Clipe musical | Conferir direitos da trilha |
| **Conferência antes da entrega** | Sempre | — | Mostrar erros reais é mais convincente do que dizer que não houve |
| **O que já existia e o que nasceu** | Sempre que se mostrar números | — | É a parte mais honesta do vídeo e a mais fácil de omitir |

## Crítica do laboratório

- **"1 prompt".** O próprio vídeo lista o que já estava pronto: avatar, clone de voz, contas e um motor de código. O pedido único fecha um trabalho de preparação que não aparece na conta de 3 h 48 min. A experiência do laboratório aponta o contrário do prompt único: o acabamento vem de rodadas de revisão (ver `skills/direcao-de-video/SKILL.md`, princípio 5).
- **"0 correções humanas".** É uma afirmação do autor, sem como auditar. O prompt mostrado é estruturado e claramente trabalhado.
- **Números.** São medições do autor sobre a própria produção. Servem como exemplo de como apresentar métricas, não como referência de prazo.
- **Ritmo.** Planos de 1,5 a 3 s com efeito sonoro em quase toda entrada funcionam para o público do canal. Para público leigo ou sala de aula, o ritmo de cerca de 5 s por ideia da skill de direção é mais seguro.
- **Avatar.** A apresentadora sintética é o fio do vídeo. Só é aceitável com consentimento de quem cedeu rosto e voz e com aviso claro, como o vídeo faz.
- **Ferramentas citadas ou usadas.** Remotion, HyperFrames, GSAP, Lottie, Manim e outras aparecem como panorama. As cenas, segundo os selos, são na maioria Canvas 2D e Three.js, com FFmpeg, Apple Vision, OpenCV, Whisper, ElevenLabs, HeyGen e Pexels. Versões e nomes são leitura de tela; confira antes de citar.

## Relação com o que o laboratório já tem

- A camada de direção já está em `skills/direcao-de-video/`: briefing, timeline única, rodadas, som e direitos.
- Motion por código: `workflows/hyperframes-video-html.md` e `workflows/remotion-video-programatico.md`.
- A conferência do capítulo 7 corresponde a `templates/revisao-de-montagem.md`; os números, a `templates/log-de-geracao.csv`.
- O que é novo para o laboratório: o selo de procedência por cena, a desmontagem em camadas como abertura e o quadro "já existia / nasceu do pedido".

## Fronteira com a Concafras

Este registro é uma análise de fonte com interesse comercial. Não é divulgação da comunidade, do canal ou dos serviços citados, e não é receita pública para a Concafras. Ver `docs/estrategia/principio-da-gratuidade.md`.

## Uso previsto

Referência de linguagem para o vídeo de abertura da aula sobre IA na produção de animações: [conceito do vídeo](../../aulas/ia-para-animacao-video-de-abertura.md).
