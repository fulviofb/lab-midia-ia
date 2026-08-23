# Workflow: direção cinematográfica com Seedance/Higgsfield

Este arquivo é um adaptador para ferramentas de vídeo generativo. O método completo e independente de provedor está em:

- [`video-generativo-storyboard-first.md`](video-generativo-storyboard-first.md)
- [`docs/guias/07-gramatica-cinematografica-pratica.md`](../docs/guias/07-gramatica-cinematografica-pratica.md)
- [`docs/guias/08-planejamento-de-video-generativo.md`](../docs/guias/08-planejamento-de-video-generativo.md)

## Fontes de referência

- <https://github.com/Emily2040/seedance-2.0>;
- <https://github.com/OSideMedia/higgsfield-ai-prompt-skill>;
- <https://github.com/ZeroLu/awesome-seedance>;
- <https://github.com/MiniMax-AI/MiniMax-H3/tree/main/skills/h3-prompt-writing>.

As fontes são referências de estudo. Não copie prompts de terceiros sem verificar licença e atribuição.

## Adaptação por capacidade da ferramenta

Antes de gerar, confirme na interface/conta:

- modelo e versão realmente disponíveis;
- duração solicitável;
- quantidade/tipo de referências;
- first frame ou first/last frame;
- áudio automático e possibilidade de desativá-lo;
- custo/créditos antes do job;
- confirmação real antes de gerar;
- política de upload e direitos.

Não confie apenas em marketing ou preferências de confirmação da conta.

## Blocos possíveis de prompt

Use somente os blocos necessários:

```text
SCENE CONTEXT
ACTIVE REFERENCES — ID e função
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

O prompt deve ser autocontido quando o modelo não mantém contexto entre gerações.

## Estratégias

- plano atômico com ação e câmera dominantes;
- segmento com vários cortes dirigidos;
- first frame;
- first/last frame;
- múltiplas referências;
- locks fixos + bloco `SHOT` variável;
- layout/diagrama como input;
- liberdade controlada para seleção na montagem.

Não presuma que uma única estratégia é superior para todos os planos.

## Gate de geração

Antes de acionar a plataforma:

- [ ] direitos de upload confirmados;
- [ ] custo/teto aprovado;
- [ ] referências selecionadas;
- [ ] prompt/configuração versionados;
- [ ] duração e áudio verificados;
- [ ] condição de interrupção definida.

Após gerar, registre a tentativa e leve-a ao rough cut. Não aprove plano isolado sem verificar sua função na montagem.
