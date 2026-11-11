# Avaliação: screenwriting-skills

Data: 2026-09-16
Repositório: [`jtydhr88/screenwriting-skills`](https://github.com/jtydhr88/screenwriting-skills)
Commit avaliado: `50825325b3940a17f032129851f5c83382863000` (14 set 2026)
Clone isolado: `~/ai-media-tests/screenwriting-skills` (fora deste repositório)
Issue do piloto: [#26](https://github.com/fulviofb/lab-midia-ia/issues/26)

## Objetivo

Avaliar se o plugin de skills de dramaturgia cabe no `lab-midia-ia` como **ferramenta de roteiro**, sem instalá-lo globalmente, sem copiar o conjunto e sem tratar um único projeto de conteúdo como critério exclusivo.

Esta avaliação cobre licença, superfície de execução, mapa dos módulos e política de adoção. **Não substitui o piloto comparativo de qualidade dos roteiros.**

## O que é

Plugin de **26 skills textuais** (padrão [agentskills.io](https://agentskills.io)) para dramaturgia de cinema, série e palco. Distila livros de ofício e corpora de roteiros publicados. Os corpos das skills estão em chinês; o README pede que a língua da resposta siga a pergunta.

Não é runtime de vídeo, editor, TTS nem gerador de imagem. Complementa o guia `docs/guias/06-ideia-roteiro-cenas-video.md`, que hoje trata o roteiro sobretudo como tópicos rumo ao render.

Tamanho aproximado do checkout sem `.git`: 3,2 MB / 91 arquivos. GitHub classificava o repositório como Python por causa de `tools/check-skills.py`; o conteúdo útil é Markdown.

## Licença

Verificado nos arquivos do commit pinado, não só no README:

| Arquivo | O que cobre |
|---|---|
| `LICENSE` | MIT, Copyright (c) 2026 Terry Jia. Uso, cópia, adaptação e republicação, inclusive comercial, com aviso de copyright. |
| `NOTICE` | A MIT cobre a organização original: camadas, princípios numerados, checklists, workflows, convenções e o script em `tools/`. **Não cobre** citações de livros, roteiros publicados, partituras, libretos e traduções de terceiros. |

O README ainda pode mencionar “estudo pessoal”; **os arquivos `LICENSE` + `NOTICE` prevalecem**. Citações aparecem também dentro de alguns `SKILL.md`, não só em `reference.md`.

Política deste laboratório:

- referenciar e testar o upstream versionado;
- não espelhar o repositório inteiro;
- não republicar trechos de livros/roteiros de terceiros;
- se no futuro houver skill fina local, usar só a organização original, com atribuição MIT, e sem copiar `reference.md`.

## Superfície de execução

| Item | Resultado |
|---|---|
| Dependências de runtime | Nenhuma além de Python stdlib no validador |
| Hooks / install global | Não há no plugin avaliado |
| Rede / downloads secundários | Skills não instalam pacotes nem baixam modelos |
| `tools/check-skills.py` | 26 skills, 0 erros, 0 avisos |
| Links relativos | Checagem estrutural passou |
| URLs nas skills | Principalmente Wikisource em corpora de ópera; estudo, não bootstrap |

Isso **não** é um tool-skill com CLI pesado. Ainda assim, o volume (~2,8 MB só nas skills, corpora densos) desaconselha vendorizar o conjunto no `lab-midia-ia` ou instalar o plugin em todo agente.

## Mapa dos 26 módulos

### Núcleo geral — prioridade alta para piloto

| Skill | Função |
|---|---|
| `sw-workflow` | Orquestra etapas e `story-bible.md` |
| `sw-premise-theme` | Premissa, tema, logline, 戏核 |
| `sw-story-structure` | Paradigmas de estrutura (Field, Snyder, McKee, 起承转合) |
| `sw-character-conflict` | Personagem, oponente, conflito |
| `sw-dialogue` | Diálogo como ação, subtexto, diagnóstico |
| `sw-scene-craft` | Cena como virada de valor |
| `sw-format-adaptation` | Formato, cadeia outline→treatment→script, adaptação |

### Série / formato recorrente

| Skill | Função |
|---|---|
| `sw-series-engine-bible` | Motor da série, documentos de venda, bible |
| `sw-series-structure` | Act-outs, teaser, A/B/C, forma de temporada |
| `sw-writers-room` | Sala de roteiro |
| `sw-sitcom-comedy` | Meia hora / sitcom |

### Referência avançada (não copiar)

Tradições e anatomias: `sw-japanese-screenwriting`, `sw-korean-french-screenwriting`, `sw-truby-anatomy`, `sw-genre-anatomy`, `sw-american-case-studies`.

Corpora: `chekhov-dramaturgy`, `ozu-screenplay-style`, `succession-series-writing`, `sw-series-case-studies`.

### Fora do recorte imediato do laboratório

Ópera chinesa (4 skills, maior densidade de citação), `sw-chinese-series-practice` (cadeia produtiva da TV na China) e `sw-industry-business` (mercado hollywoodiano). Catalogar como especialização; não entram no piloto.

## O que o laboratório já cobre — e a lacuna

O `lab-midia-ia` está forte em **produção**: HyperFrames, Remotion, video-use, voz. A lacuna é **dramaturgia**: premissa, conflito, cena, diálogo, adaptação e consistência de série.

Isso serve a vários usos públicos do laboratório — curtas, séries, adaptações, UGC narrativo, aulas em vídeo — não a um único canal ou gênero.

Limitações observadas no núcleo:

- vocabulário e exemplos voltados a longas e séries adultas;
- skills em chinês: a saída pode seguir o idioma da pergunta, mas o arquivo em si não é auditável em português;
- não há camada própria de desenvolvimento infantil, educação religiosa ou canção;
- estruturas longas (BS2, 40 cards, 100 episódios) não devem ser aplicadas automaticamente a peças curtas.

## Política de adoção

Padrão igual ao de outros tool-skills grandes:

1. manter o upstream como fonte versionada (commit pinado);
2. clonar só em `~/ai-media-tests/`, nunca dentro deste repo;
3. não instalar o plugin no agente global nem em hooks;
4. medir valor num piloto controlado contra o fluxo atual do guia 06;
5. só então decidir workflow público e/ou skill fina local, **sem** copiar `reference.md`.

## Piloto comparativo (pendente)

Fixture: **uma história original curta**, sintética, sem material de terceiros.

Comparar duas versões do mesmo briefing:

1. fluxo atual (`docs/guias/06-ideia-roteiro-cenas-video.md`);
2. núcleo `sw-workflow` + `sw-premise-theme` + `sw-scene-craft` + `sw-dialogue`.

Critérios: clareza da ação, qualidade do diálogo, custo de processo e se o método ajuda ou só burocratiza. **Não** usar “ficou mais hollywoodiano” como sucesso.

Até o piloto, o status no catálogo permanece `test_before_recommending`.

## Veredito

| Campo | Valor |
|---|---|
| Cabe no catálogo? | Sim, categoria `roteiro_dramaturgia` |
| Status atual | `test_before_recommending` |
| `copy_policy` | `can_reference_and_test` (citações de terceiros fora) |
| Instalar plugin agora? | Não |
| Copiar skills para este repo? | Não |
| Recomendado para iniciantes? | Não, até o piloto e um guia em português |

## Comandos reproduzíveis da avaliação

```bash
git clone https://github.com/jtydhr88/screenwriting-skills.git ~/ai-media-tests/screenwriting-skills
cd ~/ai-media-tests/screenwriting-skills
git checkout 50825325b3940a17f032129851f5c83382863000
python tools/check-skills.py
```

Saída observada: `26 skills checked: 0 errors, 0 warnings`.
