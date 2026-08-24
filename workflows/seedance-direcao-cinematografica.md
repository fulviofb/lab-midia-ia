# Adaptador em validação: plataformas generativas de vídeo

**Estado de evidência:** `lab_synthesis` — baseado em referências públicas; não validado como workflow universal.

Este arquivo adapta a rota [`storyboard-first`](video-generativo-storyboard-first.md) e outras rotas generativas às capacidades observadas na interface/provedor. Não recomenda automaticamente Seedance, Higgsfield ou MiniMax e não substitui teste de viabilidade.

Consulte:

- [`guia de rotas`](../docs/guias/06-ideia-roteiro-cenas-video.md);
- [`gramática cinematográfica`](../docs/guias/07-gramatica-cinematografica-pratica.md);
- [`planejamento adaptativo`](../docs/guias/08-planejamento-adaptativo-de-video.md).

## Referências e política de uso

| Fonte | Licença detectada em 2026-08-23 | Política neste laboratório |
|---|---|---|
| [`Emily2040/seedance-2.0`](https://github.com/Emily2040/seedance-2.0) | MIT | referenciar, estudar e testar com atribuição |
| [`OSideMedia/higgsfield-ai-prompt-skill`](https://github.com/OSideMedia/higgsfield-ai-prompt-skill) | MIT | referenciar, estudar e testar com atribuição |
| [`ZeroLu/awesome-seedance`](https://github.com/ZeroLu/awesome-seedance) | MIT | referenciar, estudar e testar com atribuição |
| [`MiniMax-AI/MiniMax-H3`](https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills/h3-prompt-writing) | licença não detectada | link-only/estudo até verificação manual; não copiar conteúdo substancial |

Licenças podem mudar. Verifique o commit/termos antes de adaptar. Não copie prompts integrais de terceiros apenas porque estão públicos.

## Quando este adaptador pode ajudar

- rota de produção narrativa generativa;
- complementação generativa localizada;
- teste de condicionamento;
- planejamento de segmento com um ou vários planos;
- comparação de capacidades entre provedores.

## Quando não usar

- edição direta suficiente;
- motion graphic determinístico;
- material privado sem autorização de upload;
- necessidade que exige autenticidade documental;
- custo/retensão não conhecidos;
- ferramenta ainda não inspecionada na conta real.

## Matriz de capacidade por tentativa

Antes de escolher uma estratégia, confirme na interface/conta:

| Capacidade | Observado na conta | Fonte/evidência | Impacto |
|---|---|---|---|
| modelo/versão | | | |
| duração | | | |
| resolução/formato | | | |
| referências aceitas | | | |
| first frame | | | |
| first/last frame | | | |
| áudio automático/desativação | | | |
| extensão/edição | | | |
| créditos/custo | | | |
| confirmação antes de gerar | | | |
| retenção/exclusão | | | |
| política de upload | | | |

Não confie apenas em marketing ou preferências de confirmação da conta.

## Estratégias possíveis

- texto para vídeo;
- first frame;
- first/last frame;
- múltiplas referências;
- sheets de personagem/prop/ambiente;
- locks fixos + bloco variável;
- layout/diagrama como input;
- input transformado;
- plano atômico;
- segmento com vários cortes dirigidos;
- liberdade controlada e seleção na montagem.

Nenhuma estratégia é superior em todos os contextos.

## Blocos possíveis de prompt

Use somente os necessários:

```text
SCENE CONTEXT
ACTIVE REFERENCES — IDs e funções
LOCATION / STAGING / EYELINES
INITIAL STATE
ACTION OR TIMED SEGMENTS
CAMERA / FRAMING
PHYSICS
LIGHTING / LOOK
DIALOGUE / AUDIO
FINAL STATE
CONTINUITY LOCKS
ACCEPTANCE / CONSTRAINTS
```

Quando o modelo não mantém contexto, o prompt/configuração precisa ser autocontido ou apontar claramente para referências versionadas.

## Gate de upload

- [ ] material autorizado para envio externo;
- [ ] provedor e finalidade autorizados;
- [ ] dados pessoais/sensíveis revisados;
- [ ] retenção/exclusão conhecida ou risco aceito;
- [ ] somente cópias selecionadas serão enviadas.

## Gate de geração

- [ ] estratégia e referências aprovadas;
- [ ] duração e áudio verificados;
- [ ] prompt/configuração versionados;
- [ ] condição de interrupção definida;
- [ ] geração autorizada;
- [ ] gasto/créditos autorizados separadamente, se aplicável.

Preferências da interface como “confirmar sempre” não substituem verificação operacional do botão/ação.

## Depois da geração

1. registre job, configuração, custo e artefato;
2. valide duração, codec, resolução e áudio;
3. inspecione frames internos;
4. leve o resultado ao rough cut;
5. avalie função na montagem;
6. decida editar, regenerar, trocar ferramenta ou mudar de rota.

Não aprove um segmento isolado apenas porque está tecnicamente íntegro.

## Estado deste adaptador

- práticas de condicionamento: observadas em referências públicas;
- síntese de blocos/gates: elaborada pelo laboratório;
- aplicabilidade entre plataformas: requer verificação por conta/modelo;
- recomendação institucional: ainda não estabelecida;
- atualização: revisar após pilotos e mudanças de interface.
