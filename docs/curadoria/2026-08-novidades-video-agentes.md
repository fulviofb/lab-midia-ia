# Curadoria — novidades de vídeo e agentes (agosto de 2026)

**Data da revisão inicial:** 2026-08-22
**Revisão estrutural:** 2026-08-23

## Objetivo

Organizar os artigos, posts e projetos recebidos; separar princípios duráveis de marketing; e decidir o que documentar, testar, monitorar ou manter somente como referência no Lab Mídia IA.

Este documento registra **candidaturas e decisões de curadoria**. Uma ferramenta só entra no catálogo canônico com status adequado depois da revisão de licença e, quando necessária, evidência prática.

## Política aplicada

```text
fonte recebida
→ triagem de segurança/licença
→ candidatura documentada
→ issue de teste ou monitoramento
→ evidência real
→ decisão sobre catalog.yml
```

Portanto, aparecer neste relatório **não significa recomendação**.

## Resumo executivo

### Incorporar como conhecimento durável

- bible visual e assets versionados;
- referências com papéis nomeados;
- distinção entre beat, keyframe, plano, segmento gerado e cena montada;
- estratégias condicionais de controle: first frame, first/last frame, múltiplas referências, layouts, locks e transformação do input;
- dramaturgia e storyboard antes da geração;
- montagem provisória e regeneração orientada por lacunas;
- revisão humana antes da publicação;
- gramática cinematográfica própria, sem copiar bibliotecas comerciais de prompts.

### Manter como candidaturas com issues

1. `snapcn` integrado ao Remotion — [issue #17](https://github.com/fulviofb/lab-midia-ia/issues/17).
2. `srt-whiteboard-animation` — [issue #18](https://github.com/fulviofb/lab-midia-ia/issues/18).
3. Comfy MCP local isolado — [issue #19](https://github.com/fulviofb/lab-midia-ia/issues/19).
4. `h3-prompt-writing` e H3 Promptor sem baixar H3 completo — [issue #20](https://github.com/fulviofb/lab-midia-ia/issues/20).
5. Storyboard e gates seletivos do portfólio `shuohao-skills` — [issue #22](https://github.com/fulviofb/lab-midia-ia/issues/22).

### Apenas monitorar ou referenciar

- MiniMax H3 local completo: pesos base estimados em aproximadamente 134 GiB antes de overhead; inadequado à RTX 4060 Laptop de 8 GB no formato consultado.
- MiniMax H3 Single-Frame VAE 500K: checkpoint experimental, decoder-only e com documentação de licença incompleta na revisão.
- Showcases Higgsfield/Seedance: úteis como precedentes de processo; não provam eficiência, custo ou disponibilidade na conta do usuário.
- Bibliotecas comerciais de prompts e câmera: extrair princípios; não copiar conteúdo substancial nem promover serviços no ecossistema comunitário.

---

## 1. Primeira rodada — 16 fontes

A primeira rodada reuniu fontes sobre:

- MiniMax H3 e suas skills;
- ComfyUI MiniMax H3 Promptor;
- Single-Frame VAE;
- Comfy MCP;
- snapcn;
- SRT Whiteboard Animation;
- Seedance e Higgsfield;
- direção cinematográfica;
- automação de mídia com Hermes;
- posts e demonstrações públicas.

### Resultado de curadoria

- ferramentas novas permaneceram fora do `catalog.yml` até teste/status definido;
- foram abertas as issues #17–#20;
- claims comerciais foram separados de fatos observáveis;
- direitos de código, pesos, modelos e assets foram tratados separadamente;
- nenhum instalador ou skill foi habilitado globalmente.

---

## 2. Segunda rodada — storyboard e gramática cinematográfica

Fontes recebidas:

- <https://github.com/eternityspring/shuohao-skills>;
- `42 Camera Movements AI Prompts`;
- CinePrompt;
- Director’s Eye/Moodnode.

### Resultado de curadoria

- o portfólio `shuohao-skills` foi clonado isoladamente no teste original;
- 1.262 assertions determinísticas de scripts/schemas passaram no Windows;
- isso validou código e estruturas, **não** chamadas de modelo, qualidade narrativa, imagens ou render final;
- a issue #22 propõe avaliar somente o módulo necessário, sem instalação global;
- as referências comerciais inspiraram taxonomia autoral de câmera, luz, composição e continuidade;
- links comerciais não foram promovidos nas portas públicas do ecossistema.

---

## 3. MiniMax H3

### Fontes principais

- <https://github.com/MiniMax-AI/MiniMax-H3>;
- <https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills>;
- <https://github.com/MiniMax-AI/skills>;
- <https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE>.

### Achados

O repositório oficial inclui nove skills. Na revisão realizada, apenas `h3-prompt-writing` se apresentava como portável para agentes genéricos; as demais dependiam do canvas e das ferramentas do MiniMax Hub.

A skill portátil cobre modos T2VA, I2VA, FL2VA, L2VA e Ref2VA. Pode ser estudada ou testada seletivamente sem instalar o portfólio inteiro.

### Hardware e licença

O conjunto base de pesos consultado somava aproximadamente:

- text encoder: 62,13 GiB;
- transformer: 61,73 GiB;
- VAE: 9,70 GiB;
- audio VAE: 0,56 GiB;
- total: 134,13 GiB antes de overhead.

Conclusão operacional: não baixar o H3 completo para a RTX 4060 Laptop 8 GB. Eventual teste deve usar rota compatível, teto explícito de créditos e mídia sintética.

A licença comunitária dos pesos possui restrições próprias; código, skills, pesos e outputs devem ser avaliados separadamente.

---

## 4. ComfyUI MiniMax H3 Promptor

### Fontes

- <https://www.reddit.com/r/comfyui/comments/1vsus0l/comfyuiminimaxh3promptor_v130_fullreference_scene/>;
- <https://github.com/1038lab/ComfyUI-MiniMax-H3-Promptor>.

### Valor declarado

- separação entre análise visual e estruturação textual;
- suporte a modos H3 e múltiplas referências;
- provedores cloud ou locais;
- pipeline de blueprint e storyboard;
- licença GPL-3.0.

### Cautelas

A discussão comunitária consultada relatava bugs, lentidão local e regressões. O projeto não deve ser recomendado sem teste. A fase inicial da issue #20 avalia apenas a engenharia de prompt, sem baixar H3.

---

## 5. Comfy MCP local

### Fontes

- <https://blog.comfy.org/p/open-sourcing-comfy-mcp-on-local>;
- <https://github.com/Comfy-Org/Comfy-mcp>.

### Valor declarado

O servidor permite que agentes descubram hardware, modelos, nodes e templates; iniciem o ComfyUI; validem/executem workflows; monitorem jobs; instalem nodes e baixem modelos.

### Risco e governança

O projeto informa que não é sandbox. Um agente pode, por design, ler/escrever arquivos, executar workflows, controlar o ComfyUI e instalar custom nodes.

A issue #19 exige:

- conta sem privilégio administrativo;
- workspace e venv isolados;
- MCP apenas no projeto;
- loopback;
- allowlist de diretórios;
- mídia sintética;
- sem API paga no primeiro teste;
- confirmação humana para download, instalação, update, rede e gasto;
- workflow conhecido e inspecionado;
- artefato final verificado.

MCP reduz atrito operacional, mas não transforma automaticamente ComfyUI em ferramenta para leigos.

---

## 6. snapcn

### Fontes

- <https://www.snapcn.dev/>;
- <https://github.com/snapcndev/snapcn>.

Registro MIT de componentes Remotion instalados no estilo shadcn. O código TSX é copiado para o projeto, sem runtime snapcn.

É um candidato incremental porque Remotion já foi validado no Windows. A issue #17 prevê:

- instalar somente poucos componentes;
- fixar versão quando possível;
- revisar o diff do TSX copiado;
- evitar skill global;
- renderizar MP4 sintético;
- validar com `ffprobe` e inspeção visual.

---

## 7. SRT Whiteboard Animation

### Fonte

- <https://github.com/geeklee/srt-whiteboard-animation>.

O projeto MIT propõe transformar SRT em animação de quadro branco com divisão de cenas, storyboard, aprovação por etapas, desenho progressivo, editor de anotações e render.

A issue #18 separa duas evidências:

1. render whiteboard a partir de SRT + line art preparado;
2. eventual geração da ilustração.

A licença MIT do código não licencia imagens, fontes, modelos ou outros insumos.

---

## 8. Automação de mídia com Hermes

Um dos relatos recebidos descrevia produção/publicação automática de carrosséis. Claims comerciais não foram auditados.

Princípio transferível:

```text
pesquisa
→ rascunho
→ assets
→ preparação de publicação
→ aprovação humana
```

No ambiente comunitário, automação deve parar antes da publicação. Não adotar multiplicação automática de contas, postagem sem revisão ou otimização por volume.

---

## 9. Precedentes públicos de produção

A análise inicial de Kok Boru foi posteriormente ampliada para 11 projetos públicos de autores, durações e graus de transparência diferentes.

O relatório comparativo sanitizado está em:

- [`docs/precedentes/video-generativo/higgsfield-processos-publicos-2026-08.md`](../precedentes/video-generativo/higgsfield-processos-publicos-2026-08.md)

A comparação não escolhe modelo, estética ou pipeline. Seu objetivo é mapear módulos de processo e registrar limites de evidência.

---

## 10. Backlog

| Item | Situação | Issue |
|---|---|---|
| snapcn + Remotion | candidato a smoke test | [#17](https://github.com/fulviofb/lab-midia-ia/issues/17) |
| SRT Whiteboard | candidato educacional | [#18](https://github.com/fulviofb/lab-midia-ia/issues/18) |
| Comfy MCP | somente piloto isolado | [#19](https://github.com/fulviofb/lab-midia-ia/issues/19) |
| H3 prompt-writing | piloto fino | [#20](https://github.com/fulviofb/lab-midia-ia/issues/20) |
| H3 Promptor | depois do ambiente ComfyUI controlado | [#20](https://github.com/fulviofb/lab-midia-ia/issues/20) |
| Storyboard/gates externos | avaliar seletivamente | [#22](https://github.com/fulviofb/lab-midia-ia/issues/22) |
| MiniMax H3 completo | monitorar; não baixar nesta máquina | — |
| Single-Frame VAE 500K | fora do roadmap enquanto faltar clareza documental | — |

---

## 11. Regra de publicação

- nenhuma oferta paga ou captação no ambiente espírita;
- custos de terceiros permanecem visíveis;
- exemplos comerciais são analisados, não promovidos;
- automação prepara rascunhos; publicação exige revisão;
- conteúdo de terceiros só é adaptado quando licença e atribuição permitirem;
- material privado não entra no repositório sem sanitização e autorização;
- ferramentas candidatas não são apresentadas como testadas.
