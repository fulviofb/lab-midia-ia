# Rota opcional: vídeo narrativo storyboard-first

**Estado de evidência:** `lab_synthesis` — sintetizado a partir de práticas observadas em precedentes públicos; em validação no laboratório.

Este workflow é **uma rota possível**, não o método universal para produzir vídeo. Ele organiza projetos narrativos em que geografia, continuidade, cobertura e montagem justificam pré-produção estruturada.

Consulte primeiro:

- [`guia de rotas`](../docs/guias/06-ideia-roteiro-cenas-video.md);
- [`planejamento adaptativo`](../docs/guias/08-planejamento-adaptativo-de-video.md).

## Quando considerar

- personagens ou ambientes reaparecem;
- há múltiplos planos/segmentos;
- continuidade é risco central;
- transformação precisa ser legível;
- rough cut orientará novas gerações;
- equipe precisa compartilhar decisões.

## Quando simplificar ou dispensar

- peça abstrata/programática;
- um único plano simples;
- material existente já resolve o objetivo;
- storyboard não reduz risco relevante;
- prazo não comporta pré-produção formal.

## Rotas alternativas

- edição direta;
- vídeo programático;
- montagem híbrida;
- complementação generativa localizada;
- filmagem/asset real.

## Módulos sugeridos

### Perfil leve

- contrato criativo reduzido;
- registro de assets quando houver terceiros;
- cartão de cena ou plano;
- revisão de montagem/artefato.

### Perfil intermediário

- contrato e papéis;
- registro de assets;
- cartão de cena e planos;
- bible seletiva;
- cartão de segmento quando geração e montagem não coincidirem;
- log de tentativas relevantes;
- rough cut.

### Perfil complexo

- todos os anteriores conforme necessidade;
- contrato de experimento;
- mapas/staging/eyelines;
- cadeia de versões/IDs;
- teto global e por experimento;
- picture lock formal;
- QC técnico e autorização de publicação separados.

Não preencha módulos automaticamente. Veja [`templates/README.md`](../templates/README.md).

## 1. Contrato e autorizações

Use [`contrato-criativo.md`](../templates/contrato-criativo.md).

Separe:

- análise local;
- cópia para workspace;
- processamento local;
- upload externo;
- geração;
- gasto/créditos;
- download;
- publicação;
- retenção/exclusão no provedor.

Defina papéis. Uma pessoa pode acumulá-los, mas isso deve ser explícito.

## 2. Dramaturgia proporcional

Use o núcleo:

```text
função/evento
+ estado inicial
+ estado final
+ informação necessária
+ mudança observável
```

Quando aplicável:

```text
personagem focal
+ desejo/necessidade
+ obstáculo
+ ponto de virada
```

Registre em [`cartao-de-cena.yml`](../templates/cartao-de-cena.yml).

## 3. Assets, referências e continuidade

Registre fontes e permissões em [`registro-de-assets.yml`](../templates/registro-de-assets.yml). Use a [`bible-visual.yml`](../templates/bible-visual.yml) somente quando identidades/regras recorrentes justificarem.

Módulos possíveis:

- personagem/estado;
- ambiente/geografia;
- prop;
- áudio;
- mapa;
- staging;
- eyelines;
- relações de escala;
- locks e variações permitidas.

## 4. Storyboard e cobertura

Para cada plano relevante, use [`cartao-de-plano.yml`](../templates/cartao-de-plano.yml).

O storyboard pode revelar decisões. Quando ocorrer:

```text
achado
→ alternativas/implicações
→ gate humano
→ atualização
```

Verifique, conforme a cena:

- situação;
- ação;
- reação;
- detalhe;
- geografia;
- transição;
- ponte sonora.

## 5. Sondagem técnica

Antes de finalizar todos os planos, teste com material sintético quando houver dúvida crítica:

- referências;
- duração;
- áudio;
- first/last frame;
- continuidade;
- formato;
- custo;
- retenção.

A sondagem informa viabilidade; não escolhe direção criativa.

## 6. Segmentos de geração

Plano de montagem e arquivo gerado não são equivalentes. Um segmento pode conter vários planos, e um plano pode ser coberto por mais de um segmento.

Use [`cartao-de-segmento.yml`](../templates/cartao-de-segmento.yml) para registrar:

- planos/beats cobertos;
- estratégia;
- estados inicial/final;
- duração;
- referências;
- áudio;
- critérios de aceite.

## 7. Experimentos

Use [`contrato-de-experimento.yml`](../templates/contrato-de-experimento.yml) quando uma tentativa for cara, lenta, sensível ou comparativa.

Modos:

- diagnóstico;
- exploração;
- produção.

Nenhuma geração sem autorização. Gasto requer autorização adicional.

## 8. Tentativas e artefatos

Registre tentativas relevantes em [`log-de-geracao.csv`](../templates/log-de-geracao.csv):

- IDs e versões;
- provedor/modelo/job;
- configuração/prompt;
- referências;
- custo/créditos com unidade;
- artefato/hash;
- falhas;
- decisão e próxima ação.

Preserve falhas úteis sem misturá-las aos assets aprovados.

## 9. Assembly e rough cut

Monte cedo, inclusive com placeholders:

```text
seleções
→ assembly
→ rough cut
```

Avalie:

- narrativa;
- ritmo;
- áreas sem função;
- geografia;
- continuidade;
- transformação;
- áudio.

## 10. Lacunas e mudança de rota

Para cada lacuna:

- evidência/timecode;
- severidade;
- plano/segmento/tentativa relacionados;
- opção de edição;
- opção de regeneração;
- possibilidade de filmagem/asset real;
- decisão humana;
- novo teto, se houver.

É válido mudar para edição, vídeo programático, filmagem ou outra ferramenta.

## 11. Fine cut e picture lock

Congele:

- ordem;
- pontos de corte;
- duração;
- estrutura temporal;
- exceções.

Após picture lock, novas gerações são exceções aprovadas.

## 12. Pós, master e publicação

Use [`revisao-de-montagem.md`](../templates/revisao-de-montagem.md) para registrar:

- revisão editorial;
- QC técnico com valores observados;
- direitos/privacidade;
- arquivo/hash do master;
- autorização de publicação separada.

## Saídas desta rota

A rota pode terminar ou migrar quando:

- material existente já resolve;
- ferramenta não atende;
- autenticidade exige filmagem/asset real;
- orçamento atingiu o teto;
- montagem revela que abordagem mais simples é suficiente;
- decisão criativa muda.

## Critério de conclusão

- [ ] módulos foram escolhidos por necessidade;
- [ ] prática observada e síntese do laboratório foram diferenciadas;
- [ ] autorizações estão separadas;
- [ ] IDs e versões fecham a cadeia;
- [ ] rough cut orientou lacunas;
- [ ] mudança de rota permaneceu possível;
- [ ] master e publicação foram aprovados separadamente;
- [ ] estado de validação foi declarado.
