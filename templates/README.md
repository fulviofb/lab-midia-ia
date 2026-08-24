# Módulos e templates de produção

**Estado:** templates autorais sintetizados pelo laboratório, em validação. Não constituem workflow obrigatório.

Use estes artefatos para reduzir incerteza ou preservar decisões. Não os preencha automaticamente.

## Estados de evidência

- `observed_public_precedent` — prática observada em processo público;
- `recurring_public_pattern` — padrão recorrente em múltiplos precedentes;
- `lab_synthesis` — estrutura criada pelo laboratório a partir dos achados;
- `lab_validation` — em aplicação controlada;
- `validated_specific_pilot` — validado em piloto/contexto identificado;
- `recommended_context` — recomendado somente para contexto declarado;
- `not_applicable` — dispensável no projeto atual.

Os arquivos desta pasta usam inicialmente `lab_synthesis`.

## Seleção por necessidade

| Módulo | Pode ajudar quando | Pode ser dispensado quando |
|---|---|---|
| `contrato-criativo.md` | há decisões, direitos, gastos ou aprovadores | pedido simples sem dado sensível; use versão reduzida |
| `registro-de-assets.yml` | há material de terceiros, múltiplas referências ou uploads | tudo é criado localmente e sem terceiros |
| `bible-visual.yml` | identidades, ambientes ou regras reaparecem | peça abstrata/única sem continuidade |
| `cartao-de-cena.yml` | função narrativa, cobertura ou geografia importam | peça programática simples |
| `cartao-de-plano.yml` | plano precisa de direção/continuidade compartilhada | decisão cabe em poucas linhas |
| `cartao-de-segmento.yml` | arquivo gerado cobre um ou vários planos | plano e arquivo são equivalentes e simples |
| `contrato-de-experimento.yml` | teste é caro, lento, sensível ou comparativo | tentativa barata e reversível |
| `log-de-geracao.csv` | tentativas precisam ser comparadas/auditadas | teste isolado sem reutilização |
| `revisao-de-montagem.md` | há corte, master ou publicação | artefato simples revisado por checklist curto |

## Perfis

### Leve

Use somente:

- seção reduzida do contrato;
- asset registry quando houver terceiros;
- um cartão de cena **ou** plano;
- revisão curta do artefato.

### Intermediário

Acrescente conforme risco:

- papéis e gates;
- bible seletiva;
- cartões de cena e plano;
- segmento separado;
- log de tentativas relevantes;
- rough cut.

### Complexo

Pode incluir:

- todos os módulos necessários;
- IDs/versões qualificados;
- experimentos e tetos hierárquicos;
- retenção/exclusão por provedor;
- picture lock formal;
- QC e publicação separados.

Perfil não define estética nem regime de controle.

## Relação entre artefatos

```text
project_id/project_version
→ scene_id
→ beat_id
→ shot_id
↔ segment_id
→ experiment_id
→ attempt_id
→ artifact_id/hash
→ gap_id/cut_version
→ decisão/aprovação
```

- um segmento pode cobrir vários planos;
- um plano pode aparecer em mais de um segmento;
- um experimento pode gerar várias tentativas;
- uma lacuna deve apontar para evidência e artefatos relacionados.

## Convenções

- IDs qualificados: `PROJ01-SC01-B01`, `PROJ01-SC01-P01`;
- datas: ISO 8601;
- `null` significa não definido; zero nunca significa “sem limite”;
- listas de IDs no CSV usam ponto e vírgula (`;`);
- caminhos relativos ao workspace, não caminhos pessoais absolutos;
- estados devem usar os valores documentados;
- publicação exige versão sanitizada e autorização própria;
- uma pessoa pode acumular papéis, mas isso deve ser explícito.

## Papéis sugeridos

- `creative_decision_owner`;
- `technical_operator`;
- `rights_privacy_owner`;
- `budget_owner`;
- `upload_authorizer`;
- `publication_authorizer`.

## Estados de decisão

- `open`;
- `approved`;
- `rejected`;
- `deferred`;
- `blocked`;
- `not_applicable`;
- `superseded`;
- `revoked`.

## Uso seguro

1. copie somente módulos necessários para workspace privado;
2. troque/remova fixtures como `PROJ-DEMO`;
3. não publique caminhos locais, credenciais ou assets privados;
4. preserve versões e IDs;
5. registre o arquivo/versão exatos aprovados;
6. se mudar de rota, registre o que permanece e o que é invalidado;
7. declare estado da evidência e contexto de recomendação.

## Exemplo

`examples/video-adaptativo-minimo/` contém fixture sintética, não religiosa e sem mídia de terceiros. Ela demonstra relações estruturais; não prova qualidade criativa nem valida um provedor.

## Validação

Execute:

```bash
python scripts/validate_video_project_templates.py examples/video-adaptativo-minimo
```

O validador verifica sintaxe e relações mínimas. Ele não avalia direitos, qualidade narrativa ou adequação criativa.
