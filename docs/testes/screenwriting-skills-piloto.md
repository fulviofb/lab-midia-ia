# Piloto: screenwriting-skills vs guia 06

Data: 2026-09-16
Issue: [#26](https://github.com/fulviofb/lab-midia-ia/issues/26)
Avaliação prévia: `docs/testes/screenwriting-skills-avaliacao.md`
Commit das skills: `50825325` (clone em `~/ai-media-tests/screenwriting-skills`)

## O que este piloto mede

Qualidade de **roteiro**, não render. As duas versões partem do **mesmo briefing congelado**. Nenhuma usa material de terceiros.

Critérios combinados na issue:

- clareza da ação;
- qualidade do diálogo;
- custo de processo (ajuda vs. burocracia).

Não é critério: “ficou mais hollywoodiano”.

## Briefing congelado

| Campo | Valor |
|---|---|
| Peça | short narrativo de 60 s |
| Formato | 16:9 |
| Público | educadores e voluntários de evento comunitário |
| Tom | educativo, concreto, sem slogan |
| Ferramenta de produção (depois) | HyperFrames ou Remotion — fora deste piloto |
| História | original, sintética |

**Situação.** Mesa de credenciamento num evento. Ana faz tudo “porque é mais rápido”. Leo chegou para aprender. A fila cresce. Uma criança não alcança o formulário.

**Proibido no briefing.** Moral dita em voz off; personagens que só escutam sermão; imitação de livros ou canais existentes.

---

## Versão A — guia `docs/guias/06-ideia-roteiro-cenas-video.md`

Seguiu só os passos 1–3 do guia (ideia, roteiro em tópicos, storyboard). Parou antes de composição/render, como combinado.

### Passo 1 — ideia

- **O que:** mostrar que ajudar de verdade é deixar o outro fazer.
- **Para quem:** voluntários e educadores.
- **Mensagem:** “Ajudar não é fazer no lugar; é abrir espaço.”
- **Duração:** 60 s.
- **Formato:** 16:9.
- **Tom:** educativo.

### Passo 2 — roteiro em tópicos

```txt
Cena 1 (0-8s): Título. Mesa de credenciamento. Ana carimba crachás em ritmo acelerado.
Cena 2 (8-18s): Leo chega e pergunta se pode ajudar. Ana sorri e diz que é mais rápido ela mesma.
Cena 3 (18-32s): Fila aumenta. Criança na ponta dos pés não alcança o formulário.
Cena 4 (32-48s): Leo puxa um caixote para a criança. Ana hesita, depois entrega o carimbo a Leo.
Cena 5 (48-60s): Leo carimba; Ana atende perguntas na fila. Texto final: “Ajudar é abrir espaço.”
```

Narração opcional (padrão do guia):

```txt
“Às vezes a gente ajuda fazendo tudo sozinho.
Mas quem está ao lado também precisa aprender.
Abrir espaço é a ajuda que continua quando a gente sai da mesa.”
```

### Passo 3 — storyboard

| Cena | Duração | Elemento | Animação | Cor |
|---|---|---|---|---|
| 1 | 0–8s | Título + Ana carimbando | fade in | fundo claro, destaque âmbar |
| 2 | 8–18s | Leo à margem da mesa | slide in da direita | mesmo fundo |
| 3 | 18–32s | Fila + criança na ponta dos pés | corte seco | fila em muted |
| 4 | 32–48s | Caixote + passagem do carimbo | scale no carimbo | âmbar no objeto |
| 5 | 48–60s | Dois ofícios lado a lado + frase | fade in do texto | branco / âmbar |

### Diagnóstico interno da versão A (depois de escrita, sem usar as skills)

- Produção: fácil de virar composição (tempos, elementos, animações).
- Ação: existe, mas a lição ainda cabe na narração e no texto final.
- Diálogo: quase inexistente; o guia não pede.
- Risco: o vídeo explica o tema em vez de obrigar o espectador a inferir.

---

## Versão B — núcleo `sw-*` (peça curta)

Skills lidas no clone isolado, sem install: `sw-workflow` (caminho de short/小戏: premissa → 起承转合 → personagens ≤5 → draft), `sw-premise-theme`, `sw-scene-craft`, `sw-dialogue`.

Não usei mapas de longa (BS2, 40 cards, 100 episódios). Não copiei `reference.md`.

### Premissa e tema

- **Por que importa:** voluntariado vira gargalo quando a pessoa mais experiente centraliza o ofício.
- **Premissa (personagem + causa + desfecho):** A pressa de Ana em fazer tudo sozinha trava a fila; soltar o carimbo destrava o ofício.
- **Controlling idea:** a ajuda vale quando transfere capacidade, porque o outro consegue agir sem você.
- **Terceira trilha:** Ana quer um evento “redondo”; crença errada: “se eu não fizer, sai errado”.
- **戏核 / núcleo:** o carimbo muda de mão — sem essa passagem a peça não existe.
- **Logline:** Num credenciamento lotado, uma voluntária que faz tudo “mais rápido” precisa soltar o carimbo para o novato, senão a fila não anda.

Uma premissa só. Tema (ajuda) não muda; muda a **atitude** de Ana.

### Personagens

| Pessoa | Quer nesta cena | Crença / obstáculo | Voz |
|---|---|---|---|
| Ana | Fila zero, sem erro | “Eu faço mais rápido” | frases curtas, ordem, sem desculpa longa |
| Leo | Entrar no ofício | Espera permissão | pergunta concreta, não discurso |
| Criança | Alcance o papel | Altura da mesa | quase sem fala; ação |

Oponente da premissa não é Leo: é a pressa da própria Ana.

### 起承转合 (em vez de BS2)

| Parte | Função | Valor na mesa |
|---|---|---|
| 起 | Ana no fluxo; Leo à margem | controle + / fila já tensiona |
| 承 | “É mais rápido eu mesma”; fila cresce | controle + / dignidade de Leo − |
| 转 | Criança não alcança; Leo move o caixote | status de “eficiente” vira atraso visível |
| 合 | Carimbo muda de mão; Ana vai à fila | controle compartilhado; fila anda |

### Lista de cenas (uma virada por cena)

Formato do workflow: `cena \| lugar \| o que acontece \| valor abre→fecha \| posição`.

| # | Lugar | Uma frase | Valor | Posição |
|---|---|---|---|---|
| 1 | Mesa, manhã | Ana carimba dois crachás no tempo de um | ordem aparente → primeiro atraso (fila já existe) | 起 |
| 2 | Mesma mesa | Leo oferece a mão; Ana cobre o carimbo | inclusão possível → recusa educada | 承 |
| 3 | Fila / borda da mesa | Criança não alcança; Ana nem vê | eficiência → ponto cego | 承/转 |
| 4 | Chão ao lado da mesa | Leo puxa o caixote; a criança escreve | criança excluída → incluída sem pedir licença à Ana | 转 |
| 5 | Mesa | Ana entrega o carimbo; vai atender a fila | “só eu sei” → ofício dividido | 合 |

Cena que só explicasse o tema: cortada. A narração da versão A não entra aqui.

### Diálogo (ação, não cartaz)

INT. TENDA DE CREDENCIAMENTO — DIA

Ana carimba sem olhar para cima. A fila já dobrou o corredor. Leo para ao lado da mesa, as mãos livres.

LEO
Posso pegar os crachás?

ANA
Depois. Assim sai mais rápido.

Ela cobre o carimbo com a palma quando a mão dele se aproxima. Na ponta da mesa, uma criança na ponta dos pés. O formulário não desce.

Leo não discute. Puxa um caixote debaixo da mesa, encosta na perna da criança. A criança sobe, pega a caneta, escreve o nome.

Ana vê o papel preenchido — não o discurso. Tira a palma. Empurra o carimbo dois centímetros na direção de Leo.

ANA
Você carimba. Eu vou na fila.

Leo carimba o primeiro crachá, lento, certo. Ana já está no corredor, apontando a mesa seguinte para quem espera.

Fim. Sem frase de encerramento na tela, a menos que a produção peça cartão institucional depois do corte.

### Beats da cena 5 (checagem `sw-scene-craft`)

1. Ana ainda segura o ofício (valor: controle +).
2. Vê a criança já escrevendo — revelação, não fala.
3. Empurra o carimbo (ação que vira o valor).
4. Sai para a fila (consequência visível).

Se o carimbo não mudar de mão, a cena 5 é exposição e cai.

### Custo de processo da versão B

- Lido: quatro `SKILL.md` longos, em chinês.
- Útil de fato: uma premissa, um objeto que vira, “apagar cena sem virada”, diálogo como ação, caminho curto em vez de mapa de longa.
- Descartado neste short: BS2, 40 cards, engine de 100 episódios, oponente “mais forte que o herói” no sentido de série adulta.

---

## Comparação

| Critério | Versão A (guia 06) | Versão B (núcleo sw-*) |
|---|---|---|
| Clareza da ação | Eventos listados; a moral ainda pode ir para a narração | A virada está num objeto (carimbo) e num gesto (caixote) |
| Diálogo | Quase nenhum; o guia não exige | Poucas falas; a recusa e a cessão são ações |
| Custo | ~15 min; encaixa direto em HyperFrames | ~1–2 h na primeira vez, por causa do volume das skills |
| Risco | Peça vira cartaz educativo | Peça pode ficar “de cinema” demais se alguém aplicar BS2 |
| Produção | Storyboard já tem tempo e animação | Precisa de um passo extra para virar tabela de composição |

O guia 06 ganha no caminho até o MP4. O núcleo `sw-*` ganha quando a peça **precisa de história**, não só de slides animados.

Não substitui o guia. Também não justifica instalar as 26 skills no agente.

## Veredito

1. **Manter o upstream como referência versionada** — já catalogado; não copiar, não instalar plugin.
2. **Status do catálogo:** `test_before_recommending` → `partially_tested`. O piloto de roteiro rodou; o pipeline de render não.
3. **Workflow público fino:** sim, em PR **separado**, em português, só com o que este piloto usou:
   - uma premissa;
   - um núcleo visível (objeto ou gesto sem o qual a peça cai);
   - cada cena vira um valor, senão corta;
   - diálogo como ação; sem narrar a moral;
   - short ≠ longa (sem BS2 / 40 cards).
4. **Não fazer:** skill local que espelhe os 26 módulos ou os `reference.md`.

## Comandos (reprodução)

```bash
# skills já clonadas e pinadas na avaliação
python ~/ai-media-tests/screenwriting-skills/tools/check-skills.py
```

Saída já registrada: `26 skills checked: 0 errors, 0 warnings`.
