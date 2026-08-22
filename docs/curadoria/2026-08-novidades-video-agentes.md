# Curadoria — novidades de vídeo e agentes (agosto de 2026)

Data da revisão: 2026-08-22

## Objetivo

Organizar os artigos, posts e projetos recebidos; separar princípios duráveis de marketing; e decidir o que incorporar, testar, monitorar ou manter apenas como referência no Lab Mídia IA.

## Resumo executivo

### Incorporar agora

1. Fortalecer o workflow de direção cinematográfica com:
   - bíblia visual e passaportes de assets;
   - referências com papéis nomeados;
   - primeiro frame aprovado antes do vídeo;
   - uma ação e um movimento principal de câmera por plano;
   - beats temporizados com estados finais;
   - mudança de uma variável por tentativa;
   - checklist de montagem e continuidade.
2. Registrar `snapcn`, `Comfy MCP`, `srt-whiteboard-animation`, MiniMax H3 e ferramentas relacionadas no catálogo.
3. Criar pilotos separados, sem instalação global e sem publicar automaticamente.

### Testar primeiro

1. `snapcn` integrado ao Remotion já validado no Windows.
2. `srt-whiteboard-animation` para explicadores educacionais a partir de SRT.
3. Comfy MCP local em ambiente isolado e com escopo restrito.
4. Skill oficial portátil `h3-prompt-writing`, sem instalar o conjunto inteiro de skills.
5. ComfyUI MiniMax H3 Promptor somente depois do ambiente ComfyUI estar controlado.

### Apenas monitorar/referenciar

- MiniMax H3 local completo: os pesos base somam aproximadamente 134 GiB antes de overhead; não é adequado à RTX 4060 Laptop de 8 GB.[5][7]
- MiniMax H3 Single-Frame VAE 500K: checkpoint experimental de 9 GB, decoder-only, sem suporte a vídeo completo.[4]
- Higgsfield/Seedance 2.5: úteis como referência de processo, mas dependem de plataforma/créditos e contêm marketing.
- Bibliotecas comerciais de prompts: linkar e resumir princípios; não copiar prompts substanciais.

## 1. Direção cinematográfica, referências e edição

### Fontes

- pipeline com bíblia visual, passaportes e iteração controlada.[11]
- referências visuais para composição, luz e blocking.[12]
- direção por plano, primeiro frame e ações em sequência.[16]
- princípios de montagem e continuidade.[14]
- páginas comerciais sobre Seedance/Higgsfield enviadas para análise; não reproduzidas
  como links no ecossistema público

### O que é durável

- O pipeline precisa funcionar como memória externa do modelo.
- Personagens, locais e objetos recorrentes precisam de referências e descrições aprovadas.
- O primeiro frame, a posição e a iluminação devem ser resolvidos antes do movimento.
- Cada plano deve concentrar uma ação central e um objetivo de câmera.
- Ações longas devem ser descritas como sequência de estados.
- A iteração deve alterar uma variável por vez e registrar o resultado.
- A montagem precisa revisar continuidade, eixo de 180°, corte na ação, tamanho de plano, reação, ritmo e som.

### O que é marketing ou não está comprovado

- Alegações de exclusividade de modelos/plataformas e de produção equivalente a grandes orçamentos.
- Números de receita ou desempenho apresentados em posts sem dados auditáveis.
- A regra de 10–15 tentativas por plano não deve virar padrão: o orçamento precisa ser definido pelo projeto.
- O projeto “Kok Boru” comprova que a plataforma hospeda um filme de 14:59 e informa mais de 12 mil gerações, mas não comprova eficiência, custo ou qualidade média.

### Direitos

O FilmGrab e outros arquivos de stills são úteis para estudo privado. Não copiar stills para o repositório nem presumir autorização para redistribuição, treinamento ou publicação. Criar referências próprias/licenciadas sempre que possível.

## 2. MiniMax H3

### Fontes

- https://github.com/MiniMax-AI/MiniMax-H3
- https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills
- https://github.com/MiniMax-AI/skills
- https://x.com/MireilleDartois/status/2090246582025486440

### Descobertas

O repositório oficial inclui nove skills. Apenas `h3-prompt-writing` declara portabilidade para agentes genéricos; as outras oito dependem do canvas e das ferramentas do MiniMax Hub.[5][6]

A skill portátil cobre T2VA, I2VA, FL2VA, L2VA e Ref2VA, com estruturas específicas para áudio, referências e keyframes. Ela pode ser estudada ou pilotada isoladamente.

O repositório amplo `MiniMax-AI/skills` é MIT e inclui skills de documentos e um toolkit multimodal baseado nas APIs MiniMax. Não instalar globalmente: avaliar apenas a skill necessária em clone/versionamento controlado.[10]

### Licença e hardware

Os pesos H3 usam licença comunitária própria, com restrições territoriais e de uso. O Brasil está no território permitido, mas EUA, UE, Reino Unido e Coreia estão excluídos. A licença também proíbe usar outputs para melhorar outro modelo de IA.[7]

O conjunto base de pesos identificado no Hugging Face soma aproximadamente:

- text encoder: 62,13 GiB;
- transformer: 61,73 GiB;
- VAE: 9,70 GiB;
- audio VAE: 0,56 GiB;
- total base: 134,13 GiB, antes de overhead.

Conclusão: não testar o H3 completo localmente na RTX 4060 Laptop 8 GB. Se houver piloto, usar rota web/API com teto de créditos e mídia sintética.

## 3. ComfyUI MiniMax H3 Promptor

### Fontes

- anúncio/discussão comunitária da versão 1.3.0.[1]
- repositório do projeto.[2]

### Valor

- separa análise visual e estruturação textual;
- suporta vários modos H3 e múltiplas referências;
- aceita provedores cloud ou locais (Ollama, LM Studio, llama.cpp);
- usa pipeline de duas etapas para blueprint e storyboard;
- licença GPL-3.0.

### Cautelas

A discussão do Reddit relata bugs recentes, lentidão local, regressão no drag-and-drop e necessidade de reiniciar servidores em alguns cenários.[1] O projeto é novo e ativo; não recomendá-lo ainda. O piloto deve validar apenas a geração de prompts primeiro, sem baixar H3.

## 4. Comfy MCP local

### Fontes

- anúncio oficial.[17]
- repositório oficial.[18]

### Valor

O servidor oficial permite que agentes MCP descubram hardware, modelos, nodes e templates; iniciem o ComfyUI; validem e executem workflows; monitorem jobs; instalem nodes e baixem modelos. O projeto declara 40 ferramentas e status beta.[17][18]

### Risco e governança

O próprio threat model afirma que o servidor não é sandbox. Um agente comprometido pode, por design, ler/escrever arquivos, executar workflows arbitrários, controlar o processo ComfyUI e instalar código de custom nodes. A licença é AGPL-3.0-or-later ou comercial.

Piloto recomendado somente com:

- workspace e venv isolados;
- servidor em loopback, nunca `--listen 0.0.0.0` sem aprovação;
- mídia sintética;
- sem API paga no primeiro teste;
- confirmação humana para download, node install, update, rede e gasto;
- workflow conhecido e inspecionado;
- verificação de saída real.

## 5. snapcn

### Fonte

- site e registro de componentes.[19]
- repositório MIT.[20]

### Valor

Registro MIT de componentes Remotion instalados por shadcn. Inclui títulos, captions, terminais, frames de dispositivos, AI chat, cenas e logos. O código é copiado para o projeto, sem runtime snapcn.

É o candidato de ganho mais rápido porque o laboratório já validou Remotion e OpenMontage no Windows. O teste deve instalar apenas 2–3 componentes em projeto isolado e produzir um MP4 real.

## 6. SRT Whiteboard Animation

### Fonte

- repositório MIT.[21]

### Valor

Skill MIT que transforma SRT em animação de quadro branco com:

- divisão de cenas de 25–35 segundos;
- storyboard e aprovação por etapas;
- desenho progressivo por regiões;
- editor de anotações no navegador;
- render MP4 e união de cenas.

Tem alto potencial para aulas, evangelização, formação e vídeos explicativos. Se o smoke test passar, pode originar uma quarta receita gratuita: “transformar narração/SRT em vídeo explicativo de quadro branco”.

## 7. Automação diária com Hermes

### Fonte

- relato de automação diária com Hermes.[15]

O post descreve geração e publicação diária automatizada de carrosséis. Os números comerciais apresentados não foram auditados e não devem orientar o projeto.

Princípio aproveitável: Hermes pode orquestrar pesquisa, texto, imagens e preparação de publicação. Para o ambiente Concafras, a automação deve parar em **rascunho para aprovação humana**. Não adotar multiplicação automática de contas, postagem sem revisão ou otimização de volume.

## Backlog recomendado

| Prioridade | Item | Decisão | Issue |
|---|---|---|---|
| 1 | snapcn + Remotion | Smoke test Windows imediato | [#17](https://github.com/fulviofb/lab-midia-ia/issues/17) |
| 2 | SRT Whiteboard Animation | Smoke test e avaliar nova receita educacional | [#18](https://github.com/fulviofb/lab-midia-ia/issues/18) |
| 3 | Comfy MCP local | Piloto isolado com revisão de segurança | [#19](https://github.com/fulviofb/lab-midia-ia/issues/19) |
| 4 | H3 prompt-writing | Piloto fino, sem instalar todas as skills | [#20](https://github.com/fulviofb/lab-midia-ia/issues/20) |
| 5 | H3 Promptor | Fase B da issue #20, após ComfyUI/MCP | [#20](https://github.com/fulviofb/lab-midia-ia/issues/20) |
| 6 | MiniMax H3 completo / VAE | Monitorar; não baixar nesta máquina | — |
| contínuo | Direção/edição | Princípios já incorporados ao workflow próprio | — |

## Regra de publicação

Estas novidades não mudam o princípio de gratuidade:

- nenhuma oferta paga ou captação dentro do ambiente espírita;
- custos de APIs/ferramentas de terceiros devem ser avisados;
- exemplos comerciais são analisados criticamente, não promovidos;
- automação prepara rascunhos, mas publicação exige revisão humana;
- prompts e referências de terceiros só são copiados quando a licença permitir e com atribuição.

## Sources

[1] https://www.reddit.com/r/comfyui/comments/1vsus0l/comfyuiminimaxh3promptor_v130_fullreference_scene — Reddit: ComfyUI-MiniMax-H3-Promptor v1.3.0
[2] https://github.com/1038lab/ComfyUI-MiniMax-H3-Promptor — 1038lab/ComfyUI-MiniMax-H3-Promptor
[4] https://huggingface.co/iamkaikai/MiniMax-H3-Single-Frame-VAE-500K — MiniMax H3 Single-Frame VAE 500K
[5] https://github.com/MiniMax-AI/MiniMax-H3 — MiniMax-AI/MiniMax-H3
[6] https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills — MiniMax H3 Skills
[7] https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/LICENSE — MiniMax H3 Community License
[10] https://github.com/MiniMax-AI/skills — MiniMax-AI/skills
[11] https://x.com/EXM7777/status/2088992368695628159
[12] https://x.com/VibeEverything/status/2088495158006280682
[14] https://x.com/Framer_X/status/2090430408022491490
[15] https://x.com/SDDFounder/status/2089637760629911743
[16] https://x.com/DumbApe18/status/2088474565878088099
[17] https://blog.comfy.org/p/open-sourcing-comfy-mcp-on-local
[18] https://github.com/Comfy-Org/Comfy-mcp
[19] https://www.snapcn.dev
[20] https://github.com/snapcndev/snapcn
[21] https://github.com/geeklee/srt-whiteboard-animation
