# Caso Machina — comparação com o acervo e piloto proposto

**Estado:** análise documental concluída; módulos incrementais e piloto propostos, não executados. Esta proposta não autoriza instalação, geração, upload, gasto ou publicação no site.

Fonte analisada: [ficha crítica do precedente](../precedentes/video-generativo/machina-narrativa-musical.md).

## Base da comparação

A revisão encontrou trabalho já preparado em PRs abertas. Não confundir conteúdo proposto nessas branches com documentação já incorporada ao `master`.

| Base consultada | Revisão de referência | Escopo |
|---|---|---|
| `master` | `c560336` | README, estrutura e assistente público anterior |
| [PR #23](https://github.com/fulviofb/lab-midia-ia/pull/23) | `6b47b68700cd09b44b1e6fb71c52ac71e548b764` | Curadoria e precedentes públicos |
| [PR #24](https://github.com/fulviofb/lab-midia-ia/pull/24) | `097daf92d48d554cd154bf4e678486279ffbacf0` | Rotas, módulos e templates |
| [PR #25](https://github.com/fulviofb/lab-midia-ia/pull/25) | `f388cf601d377c39dd7fc36040dddf458da9fc43` | Assistente adaptativo e cenários |

A comparação se baseou nos arquivos e escopos dessas revisões; não é auditoria exaustiva de todo o histórico. Se as branches mudarem, reavaliar a sobreposição antes de integrar novos templates.

## O que já está coberto

| Necessidade do artigo | Material já proposto | Decisão |
|---|---|---|
| Distinguir relato, observação e inferência | Política de precedentes da #23 | Usar as mesmas categorias; não criar taxonomia paralela |
| Fixar personagens, objetos e geografia | `templates/bible-visual.yml` da #24 | Reutilizar; não criar outra ficha de personagem |
| Associar referências e ações a segmentos | `templates/cartao-de-segmento.yml`, campos `reference_asset_ids` e `timed_sections`, da #24 | Ampliar apenas se o piloto mostrar necessidade |
| Controlar testes e tentativas | Contrato de experimento e log da #24 | Reutilizar IDs e limites existentes |
| Revisar som, continuidade e publicação | `templates/revisao-de-montagem.md` da #24 | Reutilizar, acrescentando evidência temporal quando pertinente |
| Escolher rotas sem imposição universal | Assistente da #25 | A correção já está proposta; não duplicar nesta mudança |

A crítica ao assistente encontrado no `master` continua válida para aquela versão, mas a solução já está contemplada na #25. Este caso não justifica reescrever o assistente em outra branch.

## Lacunas incrementais identificadas

### 1. Mapa de trilha-mestre e janelas

**Proposta:** módulo opcional, inicialmente `lab_synthesis`, para ligar tempo global de montagem ao tempo local da referência/segmento.

Campos mínimos a experimentar:

- ID, versão e hash da trilha-mestre; direitos e proveniência pelo registro de assets existente;
- início/fim da janela no master e unidade temporal explícita;
- frase ou evento de referência, descrito sem copiar letras protegidas;
- IDs de cena/beat/plano/segmento relacionados;
- início local do recorte, deslocamentos, margem de corte e eventuais mudanças de velocidade;
- evento visual pretendido, tolerância de sincronismo aprovada e timecode observado;
- revisão do mapa e decisão de aprovação.

**Quando ajuda:** narrativa conduzida por música ou voz temporizada.
**Quando dispensar:** peça sem sincronismo relevante ou edição simples resolvida na timeline.
**Integração:** referenciar assets e segmentos existentes, sem copiar o cadastro nem confundir uma janela musical com uma cena.
**Saída:** se a trilha mudar, preservar versões anteriores e identificar apenas as janelas e decisões afetadas.

Não criar ainda um novo schema/validador: primeiro testar se uma tabela junto aos cartões existentes é suficiente.

### 2. Ficha leve de aprendizagem com referência

**Proposta:** seção opcional no registro de precedente, não banco paralelo.

Campos: pergunta de pesquisa, fonte, estrutura observada, intenção original, hipótese transferível, limite ético/autoral, adaptação pretendida e evidência necessária.

**Quando ajuda:** a equipe está estudando uma estrutura para resolver uma necessidade concreta.
**Quando dispensar:** referência apenas estética ou tarefa já definida.
**Estado:** síntese proposta, sem validação.

### Não são lacunas novas

Bible, cartão por segmento, log de tentativas, escolha de rota e autorizações já têm proposta própria. Guardar resultados em Markdown também não exige instalar Obsidian.

## Piloto mínimo proposto — aguardando aprovação

### Pergunta

Um mapa explícito de tempo global/local facilita localizar e revisar pontos de sincronismo numa peça curta, sem impor um pipeline musical a outros tipos de vídeo?

### Escopo sugerido, não decisão criativa tomada

- Peça neutra e não religiosa, sem produto, marca, pessoa identificável ou material privado.
- Duração sugerida: 20–30 segundos, com três janelas de referência.
- Áudio próprio ou com licença compatível, já disponível e autorizado; não presumir direitos de uma faixa existente.
- Primeira etapa com imagens/elementos simples e montagem local: sem serviços externos ou novas dependências.
- Se não houver áudio apropriado, interromper para escolher material ou aprovar uma alternativa; não buscar/baixar por conta própria.

### Etapa A — validar documentação e montagem

1. Aprovar objetivo, material, direção visual, duração, formato e critérios.
2. Registrar master e referências nos módulos existentes ou, enquanto a #24 estiver aberta, em instância isolada explicitamente vinculada à revisão usada.
3. Mapear as janelas e montar a peça localmente com ferramentas já disponíveis.
4. Revisar sincronismo e executar uma alteração localizada aprovada, mantendo rastreabilidade.
5. Registrar resultado, dificuldade, tempo observado e campos úteis/desnecessários.

Não se pretende provar superioridade causal com uma única peça nem comparar qualidade de fornecedores.

### Critérios de aceite propostos

- Todas as janelas apontam para a versão exata do master e para os segmentos correspondentes.
- Eventos previstos e observados são registrados; tolerância é aprovada antes da montagem, não escolhida depois para fazer o teste passar.
- Uma revisão localizada pode ser rastreada sem sobrescrever o original.
- O arquivo final é reaberto e inspecionado do início ao fim; duração e streams são verificados por ferramenta disponível.
- Há relato explícito do que funcionou, falhou e pode ser dispensado.
- Direitos e ausência de dados sensíveis são revisados.

### Etapa B — opcional e separada

Somente se necessário para testar condicionamento por áudio em geração: verificar documentação oficial, escolher provedor/modelo, aprovar referências e retenção, autorizar upload, teto de tentativas e gasto. A aprovação da etapa A não autoriza esta etapa.

Registrar tentativas rejeitadas e custo real. Interromper ao atingir o teto ou encontrar capacidade incompatível; considerar montagem convencional como alternativa.

### Resultado e estado da evidência

Um sucesso na etapa A permite apenas `validated_specific_pilot` para a documentação/montagem naquele contexto. Não valida Suno, Higgsfield, Seedance ou desempenho publicitário. Uma aprovação de plataforma exigiria teste próprio.

Relatório futuro deve incluir: escopo aprovado, revisões usadas, materiais, ferramentas/versões, evidências temporais, alterações, limitações, falhas e decisão sobre quais módulos manter.

## Limites desta entrega documental

- Sem alteração de `catalog.yml`, exports, prompts, templates operacionais ou site Concafras.
- Sem merge das PRs #23–#25.
- Sem teste de fornecedor, geração de mídia ou consumo de créditos.
- Sem promoção automática do caso à camada pública de orientação.

Após revisar esta proposta, aprovar separadamente o piloto e suas escolhas criativas. Só depois decidir o que incorporar aos templates e o que merece adaptação educativa pública.
