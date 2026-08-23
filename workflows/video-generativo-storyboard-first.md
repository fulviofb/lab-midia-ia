# Workflow: vídeo generativo storyboard-first

Este workflow é independente de provedor. Ele organiza decisões e artefatos para vídeo generativo narrativo sem pressupor que beat, keyframe, plano e clipe sejam equivalentes.

## Resultado esperado

Ao final, o projeto deve possuir:

- contrato criativo aprovado;
- bible visual proporcional ao risco;
- cartões de cena e plano;
- estratégia de condicionamento por plano/segmento;
- log de gerações;
- rough cut;
- registro de lacunas e regenerações;
- picture lock;
- revisão de pós e publicação.

## 0. Princípios

1. roteiro e dramaturgia antecedem prompts;
2. o projeto funciona como memória externa;
3. decisões criativas pertencem ao responsável humano;
4. controle pode estar em texto, imagem, mapa, layout ou locks;
5. rigidez é seletiva;
6. montagem começa antes do fim das gerações;
7. regenerações respondem a lacunas observadas;
8. publicação exige revisão humana.

## 1. Abrir o contrato criativo

Preencha [`templates/contrato-criativo.md`](../templates/contrato-criativo.md).

Gate obrigatório:

- escopo;
- fonte e direitos;
- público;
- objetivo;
- decisões que somente o usuário pode tomar;
- orçamento/teto;
- responsáveis por aprovação;
- limites éticos e de privacidade.

Não escolher duração, estética ou ferramenta quando ainda forem decisões abertas.

## 2. Estruturar dramaturgia

Para cada cena:

```text
evento
+ desejo/necessidade
+ obstáculo
+ virada
+ estado inicial
+ estado final
```

Registre em [`templates/cartao-de-cena.yml`](../templates/cartao-de-cena.yml).

Gate: o responsável aprova a função da cena e os beats antes de produzir assets finais.

## 3. Construir a bible visual

Use [`templates/bible-visual.yml`](../templates/bible-visual.yml).

### Módulos básicos

- personagens e estados;
- roupas/objetos;
- ambientes;
- materialidade/estilo;
- referências com função e direitos;
- locks e variantes permitidas.

### Módulos opcionais por risco

- mapa de locação;
- staging;
- eyelines;
- relações de escala;
- depth map;
- paleta por estado;
- descritor textual estável associado à imagem;
- versões de assets.

Gate: cada referência possui ID, função, proveniência e aprovação.

## 4. Planejar storyboard e cobertura

Para cada plano, use [`templates/cartao-de-plano.yml`](../templates/cartao-de-plano.yml).

O storyboard pode revelar decisões novas. Quando isso ocorrer:

```text
decisão revelada
→ registrar alternativa/implicação
→ gate humano
→ somente então atualizar o plano
```

Verifique cobertura:

- situação/estabelecimento;
- ação;
- reação;
- detalhe necessário;
- continuidade espacial;
- transição;
- som/ponte.

## 5. Escolher estratégia por plano ou segmento

Opções possíveis:

| Estratégia | Quando considerar |
|---|---|
| texto para vídeo | identidade/geografia pouco restritivas |
| first frame | composição inicial é âncora principal |
| first/last frame | transformação entre estados é crítica |
| múltiplas referências | identidade, ambiente e props precisam coexistir |
| character/prop sheet | recorrência e variações controladas |
| layout/diagrama | posições e trajetos são críticos |
| depth map | profundidade e relação espacial são críticas |
| locks textuais | estilo/continuidade/direção devem persistir |
| input transformado | física/orientação não responde ao texto |
| liberdade controlada | seleção editorial é aceitável |

A escolha deve registrar benefício, risco e critério de aceite.

## 6. Preparar contrato de experimento

Para cada teste pago ou demorado, registre:

```yaml
hypothesis: ""
mode: diagnostic | exploration | production
variable: ""
fixtures: []
model_and_version: ""
settings: {}
max_attempts: 0
max_displayed_credits: 0
acceptance: []
stop_conditions: []
approver: ""
```

### Modos

- `diagnostic`: alterar uma variável;
- `exploration`: comparar direções compostas registradas;
- `production`: preservar locks e corrigir lacuna específica.

Gate: nenhuma geração paga sem teto e autorização.

## 7. Gerar e registrar

Use [`templates/log-de-geracao.csv`](../templates/log-de-geracao.csv).

Para cada tentativa:

- ID;
- cena/plano/segmento;
- ferramenta/modelo;
- estratégia;
- referências e versões;
- prompt/configuração;
- seed;
- duração solicitada/entregue;
- áudio solicitado/entregue;
- créditos como exibidos;
- resultado;
- decisão e motivo.

Preserve falhas úteis. Não as misture aos assets aprovados.

## 8. Montar cedo

Crie:

```text
assembly
→ rough cut
```

O rough cut deve ser assistível, mesmo com placeholders. Avalie narrativa, ritmo, geografia, transformação e som antes de buscar acabamento.

## 9. Registrar lacunas

Exemplos:

- falta reação;
- plano longo demais;
- gesto ilegível;
- direção de tela mudou;
- identidade rompeu;
- áudio indesejado;
- transformação não é compreensível;
- falta plano de situação;
- corte exige margem adicional.

Cada lacuna recebe:

- evidência;
- severidade;
- plano afetado;
- opção de edição;
- opção de regeneração;
- decisão humana.

## 10. Regenerar com finalidade

```text
lacuna
→ menor mudança suficiente
→ nova tentativa registrada
→ substituição no rough cut
→ reavaliação
```

Não regenerar todo o projeto por falha localizada. Não usar preferência visual do agente como justificativa suficiente.

## 11. Fine cut e picture lock

Antes do lock:

- ordem;
- duração;
- cortes;
- reações;
- continuidade;
- compreensão da narrativa;
- aprovação criativa.

Após picture lock, novas gerações são exceção documentada.

## 12. Pós-produção

Use [`templates/revisao-de-montagem.md`](../templates/revisao-de-montagem.md).

- cleanup;
- cor;
- música;
- sound design;
- voz;
- mix;
- legendas;
- export;
- `ffprobe`;
- inspeção visual;
- direitos e privacidade.

## 13. Publicação e aprendizado

Separar:

- artefato privado;
- documentação interna;
- aprendizado generalizável;
- versão pública sanitizada.

Nenhum case, asset ou prompt privado entra no laboratório sem autorização específica.

## Definições obrigatórias

```text
beat       = mudança narrativa/emocional
keyframe   = decisão/referência visual
plano      = tomada contínua na montagem
segmento   = arquivo gerado; pode conter vários planos
cena       = unidade narrativa montada
```

## Critério de conclusão

- [ ] gates registrados;
- [ ] assets com proveniência;
- [ ] planos e segmentos distintos;
- [ ] gerações auditáveis;
- [ ] rough cut revisado;
- [ ] lacunas resolvidas ou aceitas;
- [ ] picture lock aprovado;
- [ ] pós validada;
- [ ] publicação autorizada separadamente.
