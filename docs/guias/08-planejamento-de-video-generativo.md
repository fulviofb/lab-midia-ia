# Planejamento de vídeo generativo narrativo

Este guia complementa `06-ideia-roteiro-cenas-video.md`. O guia 06 continua adequado para motion graphics e vídeos programáticos simples; este documento trata projetos narrativos com personagens, ambientes e múltiplas gerações.

## Princípio

```text
fonte e objetivo
→ dramaturgia
→ bible visual
→ storyboard e cobertura
→ estratégia de condicionamento
→ geração controlada
→ montagem provisória
→ regeneração por lacunas
→ picture lock
→ pós-produção
```

A ferramenta é escolhida depois dos requisitos narrativos e operacionais, não antes.

## Gates humanos

| Gate | Pergunta |
|---|---|
| G0 — direitos/privacidade | o material pode ser analisado e processado? |
| G1 — fonte/adaptação | o que é fato, escopo e decisão de adaptação? |
| G2 — dramaturgia | quais eventos, desejos, obstáculos, viradas e transformações? |
| G3 — direção | quais escolhas visuais/sonoras foram aprovadas? |
| G4 — storyboard | geografia, cobertura, planos e transições fazem sentido? |
| G5 — estratégia técnica | quais locks, referências, modelos e limites de custo? |
| G6 — teste | qual variável, critério de aceite e teto de tentativas? |
| G7 — montagem | o rough cut revelou lacunas? |
| G8 — picture lock | narrativa e duração estão congeladas? |
| G9 — publicação | direitos, privacidade, técnica e contexto foram revisados? |

Nenhum gate criativo deve ser decidido silenciosamente pelo agente.

## 1. Fonte e adaptação

Separe:

- fatos da fonte;
- trechos protegidos;
- escopo escolhido;
- omissões;
- decisões de adaptação;
- condicionamentos herdados de ferramentas antigas;
- alternativas ainda não aprovadas.

Use `templates/contrato-criativo.md` para registrar decisões sem misturá-las com fatos.

## 2. Dramaturgia

Para cada cena, registre:

- evento;
- personagem focal;
- desejo/necessidade;
- obstáculo;
- ponto de virada;
- estado inicial;
- estado final;
- informação que o espectador precisa compreender;
- mudança emocional observável.

Não transforme automaticamente cada beat em um plano.

## 3. Bible visual

A bible pode ser leve ou completa. Selecione apenas os módulos necessários:

- personagem e estados;
- figurino;
- ambiente;
- props;
- paleta e materialidade;
- mapa da locação;
- relações de escala;
- eyelines;
- diagrama de staging;
- depth map;
- regras de continuidade;
- direitos de cada referência.

Use `templates/bible-visual.yml`.

## 4. Storyboard e cobertura

O storyboard é uma superfície de decisão e verificação. Ele pode revelar:

- falta de plano de situação;
- geografia impossível;
- ausência de reação;
- transição inadequada;
- eixo confuso;
- necessidade de detalhe;
- excesso de ações no mesmo plano.

Decisões novas devem ser registradas e aprovadas, não incorporadas silenciosamente.

Use:

- `templates/cartao-de-cena.yml`;
- `templates/cartao-de-plano.yml`;
- `docs/guias/07-gramatica-cinematografica-pratica.md`.

## 5. Estratégia de condicionamento

Escolha conscientemente entre:

- texto para vídeo;
- first frame;
- first/last frame;
- múltiplas referências;
- character sheet;
- prop/environment sheet;
- layout/diagrama;
- depth map;
- blocos fixos de estilo/continuidade/direção;
- transformação do próprio input;
- liberdade controlada seguida de seleção.

Nenhuma estratégia é obrigatória para todos os planos.

## 6. Contrato de experimento

Antes de consumir créditos:

```text
hipótese
→ variável
→ fixture/referências
→ configuração
→ teto de tentativas/créditos
→ critério de aceite
→ condição de interrupção
```

### Modos de iteração

- **diagnóstico:** uma variável por vez;
- **exploração:** variações compostas, nomeadas e comparáveis;
- **produção:** preservar locks aprovados e alterar somente o necessário.

## 7. Geração e registro

Registre cada tentativa em `templates/log-de-geracao.csv`:

- cena/plano/segmento;
- ferramenta/modelo;
- referências;
- prompt/configuração;
- seed quando disponível;
- custo/créditos como exibidos;
- resultado;
- motivo de aprovação/rejeição;
- próximos passos.

Contagens de créditos de plataformas diferentes não são comparáveis sem normalização.

## 8. Montagem provisória

Monte cedo:

```text
seleções
→ assembly
→ rough cut
```

O rough cut permite descobrir:

- ausência de cobertura;
- duração inadequada;
- falta de reação;
- continuidade quebrada;
- necessidade de insert/cutaway;
- lacuna sonora;
- plano que precisa ser encurtado, reeditado ou regenerado.

Não regenere indefinidamente sem verificar a montagem.

## 9. Regeneração por lacunas

Cada nova geração deve responder a uma lacuna registrada:

```text
lacuna observada
→ plano/beat afetado
→ menor alteração suficiente
→ nova tentativa
→ atualização do rough cut
```

Depois do picture lock, novas gerações devem ser exceção aprovada.

## 10. Picture lock e pós

Após congelar narrativa, ordem e duração:

- cleanup;
- estabilização/reparo;
- unificação de cor;
- música;
- sound design;
- voz;
- mixagem;
- legendas;
- validação técnica;
- revisão de direitos/privacidade.

Use `templates/revisao-de-montagem.md`.

## 11. Escalas de processo

### Leve

```text
arco curto
→ poucos assets
→ storyboard
→ iterações por cena
→ montagem
```

### Contrato congelado

```text
STYLE + CONTINUITY + DIRECTION fixos
→ SHOT variável
```

### Controle assimétrico

```text
locks rígidos em pontos críticos
+ liberdade controlada em pontos exploratórios
```

### Completo

```text
dramaturgia
→ bible completa
→ mapas/staging
→ produção
→ rough cut
→ regenerações
→ picture lock
→ pós
```

A escala é uma decisão do projeto.

## 12. Critérios finais

- [ ] fonte e adaptação estão separadas;
- [ ] decisões-chave possuem responsável e gate;
- [ ] direitos e privacidade foram revisados;
- [ ] dramaturgia antecedeu os prompts;
- [ ] identidade e geografia necessárias foram documentadas;
- [ ] beat, keyframe, plano, segmento e cena estão distintos;
- [ ] estratégia de condicionamento foi escolhida por necessidade;
- [ ] testes possuem teto e critério de interrupção;
- [ ] rough cut orientou regenerações;
- [ ] picture lock antecedeu acabamento final;
- [ ] publicação recebeu autorização explícita.
