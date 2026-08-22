# Workflow: direção cinematográfica com vídeo generativo

Fontes de referência:

- https://github.com/Emily2040/seedance-2.0
- https://github.com/OSideMedia/higgsfield-ai-prompt-skill
- https://github.com/ZeroLu/awesome-seedance
- https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills/h3-prompt-writing
- https://x.com/DumbApe18/status/2088474565878088099
- https://x.com/Framer_X/status/2090430408022491490

> Este documento reúne princípios próprios e duráveis. Não copia bibliotecas comerciais de prompts nem vincula o workflow a um único provedor.

## Ideia central

Não peça apenas “cinematic”. **Dirija, bloqueie e registre a cena.**

O modelo não mantém memória confiável entre gerações. Portanto, o projeto precisa funcionar como memória externa: referências nomeadas, versões aprovadas, decisões registradas e critérios claros de aceitação.

## 1. Contrato criativo

Antes de gerar, fixe:

1. objetivo narrativo;
2. público e plataforma;
3. duração e proporção;
4. tom e limites éticos;
5. orçamento máximo de tentativas/créditos;
6. quem aprova cada etapa.

No ambiente espírita, o processo e a orientação permanecem gratuitos. Se uma ferramenta de terceiro cobrar por geração/API, avise antes e ofereça alternativa gratuita quando existir.

## 2. Bíblia visual e passaportes

Não gere cenas finais antes de bloquear os elementos recorrentes.

Para cada personagem, ambiente ou objeto importante, registre um **passaporte**:

- nome/ID estável;
- descrição visual objetiva;
- roupa, materiais, proporções e cores;
- referências aprovadas;
- elementos que não podem mudar;
- variantes permitidas;
- versão e data da aprovação.

Atribua **uma função clara a cada referência**: identidade, figurino, ambiente, produto, movimento, estilo, voz ou som. Reutilize os mesmos IDs e descrições em todas as cenas.

### Direitos e referências

Stills de filmes podem ajudar em estudo privado de composição, luz e blocking. Não redistribua imagens protegidas no repositório e não presuma que uma referência visual autoriza copiar personagem, marca, estilo protegido ou fotografia. Prefira referências próprias, licenciadas, domínio público ou CC compatível.

## 3. Primeiro frame e teste de consistência

O primeiro frame define grande parte da estabilidade. Antes do vídeo:

- finalize composição, posição, olhar e luz;
- teste ângulos e condições difíceis;
- confira se personagem/objeto continua reconhecível;
- aprove ou revise por checklist, não apenas por impressão.

Não imponha número fixo de tentativas. Defina um orçamento antes de começar e simplifique a cena quando a taxa de falha permanecer alta.

## 4. Cartão de plano

Cada plano deve registrar:

- ID e duração;
- intenção dramática;
- sujeito e ação principal;
- estado inicial e estado final;
- tamanho do plano e ângulo;
- **um movimento principal de câmera**;
- blocking e direção de movimento;
- luz e paleta;
- referências usadas por ID;
- diálogo, ambiente, efeitos e música;
- restrições curtas;
- ligação com o plano anterior e seguinte.

Regra prática: **um plano, uma ação central, um objetivo de câmera**. Se houver ações demais, divida.

## 5. Beats temporizados

Para cenas longas, divida o prompt em beats com tempo. Cada beat deve terminar em um estado observável que inicia o próximo.

```text
[0–4s] estado inicial + ação principal + câmera
Estado final: posição, direção do olhar, objeto nas mãos

[4–9s] continuação a partir do estado anterior
Estado final: ...

[9–15s] resolução + margem para corte
Estado final: ...
```

Descreva ações como processos sequenciais, não apenas resultados.

## 6. Prompt base

```text
Transforme esta ideia em um plano executável para vídeo generativo.
Não use adjetivos genéricos como “cinematic” sem explicar a direção.

Ideia: [descrever]
Duração/formato: [tempo e proporção]
Referências: [ID → função]
Estado inicial: [posição, olhar, luz, objetos]
Ação principal: [uma ação]
Câmera: [tamanho, ângulo e um movimento]
Blocking: [trajetos e direção de tela]
Luz/paleta/look: [concreto]
Áudio: [diálogo, ambiente, SFX, música ou sem música]
Beats temporizados: [se necessário]
Estado final: [posição e continuidade]
Restrições: [curtas e verificáveis]
```

## 7. Iteração controlada

- Altere **uma variável por tentativa**.
- Preserve literalmente o que já funcionou.
- Registre prompt, referências, seed/configuração, custo e resultado.
- Corrija primeiro o beat que falhou; evite regenerar tudo quando houver edição localizada.
- Teste estrutura em menor resolução/duração antes do render final, quando o provedor permitir.
- Se a cena continuar instável, reduza ações, referências ou duração.

## 8. Checklist de edição

A geração não encerra o trabalho. Na montagem:

- [ ] cortar durante a ação quando isso esconder melhor a transição;
- [ ] cada corte revela informação, emoção ou avanço narrativo;
- [ ] preservar direção de movimento e posição dos personagens;
- [ ] respeitar o eixo de 180° ou sinalizar conscientemente a quebra;
- [ ] adequar ritmo de corte à energia/emoção;
- [ ] usar wide para contexto, medium para ação, close para emoção e detail para informação;
- [ ] manter reações importantes tempo suficiente;
- [ ] usar cutaways apenas quando acrescentam contexto;
- [ ] ouvir a trilha e os efeitos para orientar cortes;
- [ ] unificar cor e som entre gerações;
- [ ] conferir texto, logotipos, mãos, rostos e continuidade quadro a quadro.

## 9. Gate final

Aprovar somente quando:

- identidade e cenário permanecem consistentes;
- ação e câmera são legíveis;
- áudio e fala estão inteligíveis;
- não há distorção de contexto ou mensagem;
- direitos, consentimento e transparência foram revisados;
- arquivos, prompts, referências e decisões estão versionados.

## Princípios que sobrevivem à troca de modelo

1. referência forte vale mais que adjetivo genérico;
2. o projeto precisa lembrar o que o modelo esquece;
3. uma ação e uma câmera por plano aumentam controle;
4. beats terminam em estados verificáveis;
5. uma variável muda por tentativa;
6. aprovação por checklist é melhor que seleção por entusiasmo;
7. geração, edição, cor e som são etapas diferentes;
8. publicação automática nunca substitui revisão humana.
