# Guia: da necessidade às rotas de produção de vídeo

**Estado:** orientação conceitual em evolução.

Este guia é a porta de entrada para planejar um vídeo sem pressupor uma ferramenta ou um workflow universal.

> A melhor rota depende do objetivo, do material disponível, do nível técnico, dos direitos, do prazo, do orçamento e das decisões que a pessoa deseja tomar.

Para decisões de direção, consulte [`07-gramatica-cinematografica-pratica.md`](07-gramatica-cinematografica-pratica.md). Para combinar rotas, módulos e mudanças de caminho, consulte [`08-planejamento-adaptativo-de-video.md`](08-planejamento-adaptativo-de-video.md).

## 1. Comece pela necessidade

Responda apenas o suficiente para escolher uma rota inicial:

- O que o público deve compreender, sentir ou fazer?
- Que material já existe?
- O conteúdo precisa representar fatos/pessoas reais?
- Qual é o canal, prazo e duração aproximada?
- Qual é o nível técnico de quem vai produzir?
- Há orçamento ou créditos? Qual é o teto?
- Quais decisões a pessoa quer tomar pessoalmente?
- O vídeo é peça única ou precisa gerar versões reproduzíveis?

Duração, formato, estética e ferramenta podem permanecer abertos até serem realmente necessários.

## 2. Famílias de rotas

### Rota A — edição direta de material existente

```text
fotos/vídeos/áudio reais
→ seleção
→ roteiro de montagem
→ edição
→ revisão
→ exportação
```

**Pode fazer sentido quando:**

- o material já comunica o essencial;
- realidade documental é importante;
- o prazo é curto;
- a pessoa prefere editor visual.

**Ferramentas possíveis:** editores visuais, FFmpeg ou `video-use`, conforme o nível técnico.

### Rota B — vídeo programático

```text
conteúdo e assets
→ composição determinística
→ animação
→ validação
→ render
```

**Pode fazer sentido quando:**

- textos, números e comparações são centrais;
- haverá várias versões ou formatos;
- identidade e repetibilidade importam;
- HTML/CSS ou React são vantagens.

**Ferramentas possíveis:** HyperFrames e Remotion.

### Rota C — montagem híbrida

```text
material real
+ composição/animação
+ edição humana
→ acabamento
```

**Pode fazer sentido quando:**

- o material real deve permanecer central;
- alguns trechos precisam de explicação visual;
- diferentes ferramentas resolvem partes distintas;
- sensibilidade editorial importa mais que automação total.

### Rota D — complementação generativa

```text
montagem existente
→ lacuna observada
→ geração localizada
→ integração
→ nova revisão
```

**Pode fazer sentido quando:**

- falta um plano, insert, transição ou elemento específico;
- filmar novamente é inviável;
- o uso de conteúdo sintético é aceitável e transparente;
- upload, direitos, representação e custo estão autorizados.

### Rota E — produção narrativa generativa

```text
fonte/objetivo
→ dramaturgia
→ referências e continuidade
→ storyboard/cobertura
→ geração
→ rough cut
→ regenerações por lacunas
→ pós
```

**Pode fazer sentido quando:**

- personagens, ambientes ou transformações precisam persistir;
- há múltiplos planos e gerações;
- continuidade e montagem são riscos centrais;
- o projeto comporta uma pré-produção mais estruturada.

A rota [`storyboard-first`](../../workflows/video-generativo-storyboard-first.md) é uma possibilidade desta família, não uma obrigação.

## 3. Rotas podem ser combinadas

Exemplos:

```text
edição direta
→ acrescentar motion graphic
→ montagem híbrida
```

```text
vídeo programático
→ inserir depoimento real
→ montagem híbrida
```

```text
rough cut
→ falta um plano de contexto
→ complementação generativa
```

Mudar de rota não significa necessariamente recomeçar.

## 4. Antes de mudar de rota

Registre:

- motivo da mudança;
- o que continua válido;
- o que precisa ser refeito;
- novos riscos e custos;
- novas permissões necessárias;
- próximo ponto de revisão.

## 5. Módulos opcionais

Uma rota pode usar alguns destes módulos:

- contrato criativo e autorizações;
- roteiro;
- dramaturgia;
- registro de assets/referências;
- bible visual;
- storyboard;
- cartão de cena;
- cartão de plano;
- cartão de segmento;
- contrato de experimento;
- log de tentativas;
- revisão de montagem;
- validação técnica.

Não preencha todos automaticamente. Consulte [`templates/README.md`](../../templates/README.md) para saber quando usar ou dispensar cada um.

## 6. Sondagem técnica sem deixar a ferramenta dirigir o projeto

Antes de detalhar tudo, pode ser útil confirmar:

- se a ferramenta aceita o formato e a duração;
- como trata áudio;
- quais referências suporta;
- se o processamento é local ou remoto;
- custo, créditos e política de retenção;
- se um teste sintético barato resolve a dúvida crítica.

Isso é uma sondagem provisória. A escolha técnica final pode ocorrer por plano ou segmento.

## 7. Gates que não desaparecem

Independentemente da rota:

- direitos, privacidade e fluxo de dados;
- decisões criativas-chave;
- autorização de upload;
- autorização de geração;
- autorização adicional para gasto/créditos;
- revisão do artefato;
- autorização de publicação.

Projetos complexos podem acrescentar gates de dramaturgia, bible, storyboard, rough cut e picture lock.

## 8. Exemplo de vídeo programático simples

Para uma peça visual curta:

```text
objetivo
→ roteiro em blocos
→ storyboard simples
→ HyperFrames ou Remotion
→ lint/snapshot
→ render
→ ffprobe
```

Guias específicos:

- [`02-primeiro-video-com-hyperframes.md`](02-primeiro-video-com-hyperframes.md);
- [`03-primeiro-video-com-remotion.md`](03-primeiro-video-com-remotion.md).

## 9. Validação da entrega

Conforme a rota, verifique:

- narrativa e legibilidade;
- áreas visuais/temporais sem função;
- continuidade;
- direitos e privacidade;
- codec, resolução, FPS, duração e áudio;
- arquivo final reaberto;
- publicação autorizada separadamente.

Exemplo técnico:

```bash
ffprobe -v error \
  -show_entries format=duration,size \
  -show_entries stream=index,codec_type,codec_name,width,height,r_frame_rate \
  -of json final.mp4
```

## 10. Estado da evidência

Ao recomendar uma prática, informe seu estado:

- observado em precedente público;
- recorrente em múltiplos precedentes;
- sintetizado pelo laboratório;
- em validação no laboratório;
- validado em piloto específico;
- recomendado para determinado contexto.

Uma prática bem-sucedida em um caso não se torna regra universal.

## Checklist de orientação

- [ ] A necessidade foi compreendida antes da ferramenta?
- [ ] Mais de uma rota plausível foi considerada?
- [ ] As implicações foram apresentadas?
- [ ] A pessoa escolheu as decisões-chave?
- [ ] Foram selecionados apenas os módulos úteis?
- [ ] Há possibilidade explícita de mudança de rota?
- [ ] O estado da evidência foi declarado?
- [ ] Autorizações foram separadas?
- [ ] O artefato será verificado antes de publicar?
