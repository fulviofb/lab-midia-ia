# Teste: ReelMimic

Data de preparo: 2026-11-10
Status: **piloto encerrado na fase de plano (2026-11-11); produção não executada**

## Objetivo

Validar `edenfunf/reelmimic` no Windows como orquestrador de vídeo 2D por referência, respondendo a três perguntas:

1. **Fidelidade ao personagem:** um personagem com folha própria (Pietro, série Sementes do Coração) continua reconhecível em todos os planos quando é desenhado pelos motores em código?
2. **Custo real:** quanto tempo e quanto da cota do plano Claude Code um vídeo de 30 s consome?
3. **Qualidade do processo:** a decomposição da referência, o plano para aprovação e a revisão cruzada entre agentes geram um resultado melhor que o nosso fluxo manual com HyperFrames?

## Ambiente

- OS: Windows 11, terminal bash/MSYS
- Node.js 24.16.0 · Python 3.11.15 (venv isolado em `D:\reelmimic\.venv`, via `uv`)
- FFmpeg/FFprobe 8.1.2 full build · Chrome do sistema
- Claude Code 2.1.84 · Codex CLI 0.140.0
- ReelMimic: commit `4e64585` (clone raso em `D:\reelmimic`, fora do OneDrive)

## Instalação

Não usamos o `install.bat`, porque ele roda `pip install` no Python global. Os passos equivalentes foram:

```bash
git clone --depth 1 https://github.com/edenfunf/reelmimic.git D:/reelmimic
cd D:/reelmimic
uv venv .venv --python 3.11
uv pip install --python .venv/Scripts/python.exe -r requirements.txt
cd app && npm install && npm run build
node scripts/doctor.mjs
```

Configuração mínima em `~/.reelmimic/secrets.json` (fora do repo):

```json
{
  "PYTHON": "D:/reelmimic/.venv/Scripts/python.exe",
  "BUILDERS": "3",
  "MAX_AGENTS": "4"
}
```

`BUILDERS=3` (o padrão é 6) reduz a chance de bater no limite de uso do plano durante o piloto.

Resultado do `doctor`: todos os itens obrigatórios OK. Opcionais ausentes: `YATING_KEY`, `PIXABAY_KEY`, `FREESOUND_KEY`, Blender (só para a trilha 3D, que está pausada) e CLI do HyperFrames (é baixado pelo `npx` no primeiro uso).

Observação: o `npm install` avisou que scripts de instalação (ex.: `esbuild`) estão bloqueados pela política do npm, mas o `npm run build` concluiu normalmente.

## Piloto planejado

- Pasta: `D:\reelmimic-piloto\` (`brief.md` + `pietro-model-sheet.png`)
- Motor alvo: **crayon storybook** (giz de cera), mais próximo da aquarela de livro ilustrado da série
- Duração: 30 s, sem narração e sem texto na tela, música calma sem letra
- História: Pietro brinca com o ursinho, o ursinho cai, ele para, recolhe, limpa, abraça e vai embora de mãos dadas com ele (cuidado e atenção, sem castigo nem susto)
- Referência: `referencia-maria-0-41s.mp4`, os primeiros 41 s (versos 1 a 7) do nosso clipe "No abraço de Maria". É material próprio: feltro costurado, uma imagem por verso, dissolves suaves (sem nenhum corte seco detectado) e movimento feito com Kling. O brief pede que ele aprenda só o ritmo e a edição, sem o visual de feltro e sem a faixa de letra.
- Motor fixado em giz de cera, mesmo com a referência em feltro. Assim a fidelidade do Pietro fica comparável com a folha dele. O efeito colateral também é observado: o feltro não existe entre os 7 motores, então vale registrar se ele propõe um estilo novo.

### Como rodar

```bash
cd D:/reelmimic && ./start.sh   # no Windows: start.bat
```

Abrir <http://localhost:4318>, soltar a referência, colar o brief, anexar a folha do Pietro e escolher Claude Code. Revisar o plano antes de clicar em **Approve and start**.

## Métricas a registrar

| Métrica | Como medir | Resultado |
|---|---|---|
| Tempo até o plano | relógio, da submissão ao plano pronto | — |
| Tempo de produção | do "Approve and start" ao vídeo final | — |
| Uso da cota | `/usage` do Claude Code antes e depois; pausas por limite | — |
| Motor escolhido | aba do plano | — |
| Fidelidade do Pietro | line-up de 1 quadro por plano ao lado da folha: cabelo, capa, bolsa, proporção | — |
| Rodadas de correção | aba Production line | — |
| Problemas no Windows | log | — |

## Riscos conhecidos

- Os agentes rodam com `--permission-mode acceptEdits` (Claude) ou `danger-full-access` (Codex). Por isso a instalação fica numa pasta isolada.
- O ReelMimic traz cópias próprias das skills HyperFrames. Não misturar com as instaladas globalmente no mesmo projeto.
- Exige assinatura paga de Claude Code ou Codex. Pelo [princípio da gratuidade](../estrategia/principio-da-gratuidade.md), ele não entra em trilhas públicas como ferramenta gratuita.

## Execução — fase de plano (2026-11-10)

### Tropeços de ambiente no Windows
1. **Claude Code de terminal sem login.** O ReelMimic chama o `claude` de linha de comando, que não compartilha o login do app desktop. Sintoma no chat do projeto: `Not logged in · Please run /login`.
2. **Kaspersky bloqueia o `/login`** (`SELF_SIGNED_CERT_IN_CHAIN`). O antivírus intercepta o HTTPS e o Node não confia no certificado raiz dele. Correção: exportar o "Kaspersky Anti-Virus Personal Root Certificate" para `~/.certs/kaspersky-root.pem` e definir `NODE_EXTRA_CA_CERTS` com esse caminho, tanto no terminal do login quanto no processo do servidor do ReelMimic.
3. **Atenção à conta.** Na primeira tentativa, o cabeçalho do CLI mostrou "API Usage Billing". Escolher "Claude account with subscription" no login; senão o uso é cobrado como API.
4. **A referência com dissolves dá 0 planos** na análise: o detector de cenas só reconhece cortes secos. Ainda assim, BPM, picos de tensão e zoom lento foram medidos corretamente, e o diretor deduziu "~7 s por cena virtual".

### Tempo e uso
| Métrica | Resultado |
|---|---|
| Análise da referência | ~1 min |
| Estilo + plano + elenco + quadros de estilo | 31 min (22:14 → 22:45) |
| Uso do plano Pro | janela de 5 h: 9% → 19%; semana: 11% → 12% |
| Motor escolhido | `crayon-storybook`, confiança 0,95 (respeitou o brief, citou paper-cutout como o mais próximo do feltro) |

### Fidelidade do Pietro: **reprovado**
Folha de elenco e quadros de estilo em `D:\reelmimic-piloto\plano-v1-quadros-e-elenco.jpg`. O motor desenha um boneco chibi genérico em código:
- cabelo em bloco, não cacheado;
- **sem capa de folhas, sem bolsa a tiracolo, sem bermuda** (pernas de palito);
- olhos de **coração** nas poses "love" e "hug", estilo emoji, fora da série;
- nos planos abertos, Pietro ocupa ~15% da altura do quadro.

Isso confirma a hipótese que já tínhamos com o painted-animation: motor que desenha personagem em código não reproduz folha de personagem pintada ou gerada por IA. A direção, o plano e o raciocínio sobre a referência são bons; o gargalo é o desenho do personagem.

O próprio diretor aprovou o quadro de estilo ("This passes for a style frame"). A revisão automática dele não compara com a folha enviada.

## Conclusão

Decisão (2026-11-11): **parar e registrar**. O projeto foi cancelado antes do "Approve and start" e a produção não rodou. Ela consumiria de 1 a 3,5 h da cota do Pro para um resultado que já foi reprovado no critério principal.

Respostas às três perguntas do objetivo:

1. **Fidelidade ao personagem: reprovada.** Os motores desenham o personagem em código e não reproduzem uma folha pintada ou gerada por IA. Uma rodada de correção pelo chat poderia acrescentar capa e bolsa, mas não mudaria o traço.
2. **Custo:** só a fase de plano levou 31 min e cerca de 10 pontos da janela de 5 h do Pro. Com a produção, um vídeo de 30 s caberia em uma janela, mas não em duas por dia.
3. **Processo:** é bom. A leitura da referência funcionou mesmo sem cortes secos, o plano saiu segundo a segundo e as perguntas abertas foram pertinentes. A revisão automática, porém, não compara o resultado com a folha enviada.

**Veredito para o portfólio:** serve como referência de **direção e decomposição de ritmo**: dá para estudar o `plan.json` e as análises para montar o nosso próprio plano no HyperFrames. **Não serve** para episódios com personagem de folha própria (Sementes do Coração). Pode valer em peças sem personagem fixo, como vinhetas, explicativos e clipes de objetos. Exige plano pago, então não entra em trilhas públicas como gratuito.

Status no catálogo: `partially_tested_windows`.

Artefatos preservados: `D:\reelmimic\projects\20261111-xzv46\` (plano, análise, quadros de estilo) e `D:\reelmimic-piloto\plano-v1-quadros-e-elenco.jpg`.
