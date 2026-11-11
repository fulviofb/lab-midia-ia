# Planejamento adaptativo de vídeo: rotas, módulos e mudanças de caminho

**Estado:** estrutura conceitual sintetizada pelo laboratório, em evolução.

Este guia não define um workflow universal. Ele organiza possibilidades para ajudar pessoas e equipes a escolher, combinar e mudar rotas conforme objetivo, material, risco, nível técnico e momento do projeto.

> Práticas observadas em produções públicas podem funcionar para objetivos específicos sem se tornarem regras universais. Os templates do laboratório transformam esse conhecimento em módulos reutilizáveis, ainda sujeitos a validação e melhoria.

## 1. O sistema que estamos construindo

### Biblioteca operacional

- precedentes;
- práticas;
- ferramentas;
- workflows;
- templates;
- checklists;
- experimentos.

### Camada de orientação

```text
necessidade
→ diagnóstico
→ rotas possíveis
→ implicações
→ escolha humana
→ módulos úteis
→ execução
→ avaliação
→ permanência ou mudança de rota
```

A orientação não substitui os módulos; ajuda a escolher quando e por que usá-los.

## 2. Estados de evidência

| Estado | Significado |
|---|---|
| `observed_public_precedent` | prática aparece em processo público documentado |
| `recurring_public_pattern` | abordagem semelhante aparece em vários precedentes |
| `lab_synthesis` | laboratório transformou achados em guia/template próprio |
| `lab_validation` | módulo está sendo aplicado em piloto controlado |
| `validated_specific_pilot` | funcionou para objetivo e contexto registrados |
| `recommended_context` | há base para recomendar no contexto declarado |
| `not_applicable` | módulo não agrega valor naquela rota/projeto |

“Validado em um precedente” significa utilizado com resultado naquele contexto; não prova causalidade, eficiência universal ou transferibilidade automática.

## 3. Diagnóstico sem escolher pela pessoa

Pergunte somente o necessário:

- objetivo e público;
- material existente;
- necessidade de fidelidade factual;
- prazo e canal;
- nível técnico;
- orçamento/créditos;
- privacidade e direitos;
- decisões que a pessoa quer assumir;
- necessidade de versões/reprodutibilidade.

Apresente poucas rotas plausíveis com implicações. A pessoa escolhe a direção inicial.

## 4. Rotas

As famílias estão descritas no [`guia 06`](06-ideia-roteiro-cenas-video.md):

- edição direta;
- vídeo programático;
- montagem híbrida;
- complementação generativa;
- produção narrativa generativa.

Uma rota pode conter sub-rotas. Storyboard-first é uma opção para narrativas com alto risco de continuidade e montagem.

## 5. Dimensões, não “um nível correto”

### Porte/risco

| Perfil | Características possíveis |
|---|---|
| Leve | poucos assets/planos, uma pessoa, baixo risco, decisões rápidas |
| Intermediário | múltiplos assets/formatos, alguma continuidade, revisão compartilhada |
| Complexo | personagens/ambientes recorrentes, muitos planos, direitos sensíveis, equipe e orçamento |

### Regime de controle

| Regime | Uso possível |
|---|---|
| Exploratório | liberdade controlada e seleção editorial |
| Locks fixos | estilo, continuidade ou direção permanecem congelados |
| Assimétrico | rigidez nos pontos críticos e liberdade nos exploratórios |

### Modo de iteração

| Modo | Comportamento |
|---|---|
| Diagnóstico | altera uma variável para entender falha/capacidade |
| Exploração | compara variações compostas e registradas |
| Produção | preserva decisões aprovadas e corrige lacuna específica |

Um projeto leve pode usar controle assimétrico. Um projeto complexo pode explorar antes de congelar locks.

## 6. Módulos

### Módulos básicos possíveis

- contrato criativo e autorizações;
- registro de assets/referências;
- cartão de cena/plano;
- revisão do artefato;
- validação técnica.

### Módulos condicionais

- dramaturgia formal;
- bible visual;
- mapa de locação;
- staging e eyelines;
- storyboard completo;
- cartão de segmento;
- contrato de experimento;
- log detalhado de gerações;
- rough cut formal;
- picture lock.

Use [`templates/README.md`](../../templates/README.md) para selecionar módulos. “Condicional” não significa menos valioso: significa dependente do problema.

## 7. Gates escaláveis

### Sempre explícitos

- direitos, privacidade e processamento local/remoto;
- decisões criativas-chave;
- upload externo;
- geração;
- gasto/créditos;
- publicação.

### Condicionais ao projeto

- fonte/adaptação;
- dramaturgia;
- direção;
- storyboard;
- estratégia técnica;
- experimento;
- rough cut;
- picture lock;
- aprovação institucional do master.

Uma pessoa pode acumular papéis em projeto leve. Em contexto institucional, diferencie:

- dono da decisão criativa;
- operador técnico;
- responsável por direitos/privacidade;
- responsável por orçamento;
- autorizador de upload;
- autorizador de publicação.

## 8. Fonte e adaptação

Quando houver obra, documento ou material anterior, separe:

- fatos da fonte;
- trechos protegidos;
- escopo escolhido;
- omissões;
- decisões de adaptação;
- condicionamentos herdados de ferramenta antiga;
- alternativas abertas.

Isso evita confundir uma limitação técnica anterior com decisão criativa permanente.

## 9. Dramaturgia como módulo

Núcleo aplicável a diferentes cenas:

- evento/função;
- estado inicial;
- estado final;
- informação necessária;
- mudança observável.

Quando fizer sentido, acrescente:

- personagem focal;
- desejo/necessidade;
- obstáculo;
- ponto de virada.

Cenas educativas, contemplativas, documentais ou poéticas não precisam ser forçadas ao mesmo modelo dramático.

## 10. Referências e continuidade

Selecione conforme o risco:

- personagem e estados;
- figurino;
- ambiente;
- props;
- paleta/materialidade;
- mapa da locação;
- escala;
- eyelines;
- staging;
- depth map;
- áudio/ambiente;
- variações permitidas;
- proveniência e direitos.

Uma referência precisa de função. Mais referências não significam necessariamente mais controle.

## 11. Storyboard como superfície de decisão

O storyboard pode revelar:

- geografia impossível;
- ausência de reação;
- falta de plano de contexto;
- eixo confuso;
- transição inadequada;
- excesso de ações;
- necessidade de detalhe.

Quando revelar decisão nova:

```text
achado
→ alternativas e implicações
→ decisão humana
→ atualização do plano
```

## 12. Sondagem e escolha técnica

Antes do storyboard final, um teste sintético barato pode responder dúvida crítica sobre:

- referências suportadas;
- first/last frame;
- áudio automático;
- duração;
- continuidade;
- formato;
- custo;
- upload e retenção.

Depois, escolha a estratégia final por plano ou segmento:

- texto para vídeo;
- first frame;
- first/last frame;
- múltiplas referências;
- sheets de personagem/prop/ambiente;
- layout/diagrama;
- depth map;
- locks textuais;
- input transformado;
- liberdade controlada.

## 13. Contrato de experimento

Antes de uma tentativa paga, demorada ou sensível:

```text
hipótese
→ modo de iteração
→ variável/direção
→ fixtures/referências
→ configuração
→ teto por experimento
→ critério de aceite
→ condição de interrupção
→ autorizações
```

A geração exige autorização mesmo quando gratuita. Gasto/créditos exigem autorização adicional.

## 14. Montagem provisória

Monte cedo quando a rota tiver múltiplos planos:

```text
seleções
→ assembly
→ rough cut
→ lacunas
→ edição ou regeneração localizada
```

O gate do rough cut decide:

- lacunas aceitas/priorizadas;
- correção em edição ou regeneração;
- novo teto autorizado;
- aptidão para avançar.

## 15. Picture lock e publicação

Picture lock congela:

- ordem dos planos;
- pontos de corte;
- estrutura temporal;
- duração;
- exceções registradas.

Depois dele, novas gerações são exceções aprovadas.

Separe:

1. aceitação editorial/técnica do master;
2. autorização de publicação.

## 16. Mudança de rota

Registre:

```yaml
reason: ""
from_route: ""
to_route: ""
preserved_assets: []
invalidated_decisions: []
new_risks: []
new_permissions: []
next_gate: ""
```

Exemplos:

- edição direta → híbrida para explicar comparação;
- programático → híbrido para inserir depoimento real;
- narrativa generativa → complementação localizada depois do rough cut;
- geração → filmagem/asset real quando autenticidade se torna prioritária.

## 17. Critérios para recomendar

Antes de recomendar uma rota ou módulo, declare:

- contexto adequado;
- quando dispensar;
- evidência disponível;
- custo e dependências;
- privacidade e direitos;
- nível técnico;
- possibilidade de mudança;
- pontos ainda não validados.

## Checklist

- [ ] O sistema apresentou possibilidades em vez de impor workflow?
- [ ] Prática observada e síntese do laboratório foram diferenciadas?
- [ ] A rota atual atende ao contexto de agora?
- [ ] Só os módulos úteis foram selecionados?
- [ ] Os gates foram escalados por risco?
- [ ] A pessoa preservou decisões criativas-chave?
- [ ] Há uma saída clara para mudar de rota?
- [ ] Artefatos reaproveitáveis foram identificados?
- [ ] Estado da evidência e limites foram declarados?
