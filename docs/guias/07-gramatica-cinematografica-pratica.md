# Gramática cinematográfica prática para vídeo com IA

Este guia ajuda a transformar intenção em direção observável. Serve para storyboard, filmagem, vídeo generativo, Remotion e workflows técnicos.

> Não comece por “qual efeito usar?”. Comece por: **o que o público deve perceber, sentir ou compreender neste plano?**

## Modo simples — cinco decisões

1. **O que aparece?** — sujeito, ambiente e objeto importante.
2. **O que acontece?** — ação dominante e reação.
3. **Como enquadrar?** — aberto, médio, próximo ou detalhe.
4. **Como a câmera se comporta?** — parada ou movimento dominante.
5. **Qual sensação deve resultar?** — luz, cor, ritmo e som.

Exemplo neutro:

```text
Uma educadora abre um livro sobre a mesa.
Plano médio, câmera na altura dos olhos.
Push-in lento quando ela encontra uma anotação.
Luz suave de janela, cores quentes, páginas e ambiente silencioso.
O plano termina com a mão indicando a frase.
```

## Modo avançado

Use o template [`templates/cartao-de-plano.yml`](../../templates/cartao-de-plano.yml).

---

## 1. Função narrativa

Escolha a função dominante do plano:

- **situar:** apresentar lugar, tempo ou escala;
- **explicar:** tornar informação ou ação legível;
- **aproximar:** criar intimidade;
- **revelar:** apresentar algo antes oculto;
- **acompanhar:** percorrer a ação;
- **contrastar:** evidenciar oposição ou mudança;
- **desorientar:** causar instabilidade intencional;
- **contemplar:** dar tempo para observar e sentir.

Um plano pode contribuir para várias funções, mas deve ter uma intenção dominante verificável.

## 2. Enquadramento e ângulo

### Tamanho do plano

| Escolha | Uso possível |
|---|---|
| Plano geral/extremo | lugar, escala, contexto, isolamento |
| Plano inteiro | corpo, deslocamento, relação espacial |
| Plano médio | conversa, gesto, ação cotidiana |
| Close-up | emoção, reação, decisão |
| Detalhe/extremo close | informação, textura, objeto narrativo |
| OTS | relação, diálogo, ponto de vista parcial |
| POV | percepção do personagem |

### Ângulo

| Escolha | Efeito possível |
|---|---|
| Altura dos olhos | proximidade e neutralidade aparente |
| Ângulo baixo | presença, poder ou escala |
| Ângulo alto | fragilidade, mapa ou redução de escala |
| Vista superior | geometria, organização, localização |
| Inclinação holandesa | instabilidade deliberada |

O efeito depende do contexto. Nenhum ângulo possui significado automático.

## 3. Composição

Defina quando necessário:

- posição do sujeito;
- primeiro plano, plano intermediário e fundo;
- espaço na direção do olhar/movimento;
- linhas que conduzem atenção;
- simetria ou desequilíbrio;
- área livre para texto;
- direção de tela para o corte seguinte;
- relações de escala;
- elementos que funcionam como âncoras espaciais.

A composição serve à informação e à emoção, não apenas à aparência.

## 4. Movimento de câmera

### Movimentos físicos

| Movimento | Operação | Uso possível |
|---|---|---|
| Estática | não se desloca | clareza, observação, solenidade |
| Pan | gira horizontalmente | seguir ou revelar lateralmente |
| Tilt | gira verticalmente | revelar altura |
| Dolly in/out | aproxima ou afasta fisicamente | intensificar ou contextualizar |
| Truck lateral | desloca lateralmente | acompanhar e criar paralaxe |
| Pedestal | sobe/desce sem inclinar | reenquadrar verticalmente |
| Tracking | acompanha sujeito | jornada e continuidade |
| Orbit | circula o sujeito | ênfase e mudança de perspectiva |
| Crane/jib | move em arco/altura | escala e revelação espacial |
| Handheld | movimento orgânico | urgência ou presença documental |
| Whip pan | giro muito rápido | transição energética |

### Lente e foco

- **zoom:** altera campo de visão sem mover a câmera;
- **rack focus:** transfere foco entre planos;
- **dolly zoom:** combina dolly e zoom opostos;
- **profundidade rasa:** isola sujeito;
- **foco profundo:** mantém camadas legíveis.

Regra diagnóstica: **um movimento dominante por plano atômico** aumenta a capacidade de identificar o que funcionou. Não é proibição universal de movimentos compostos nem regra para segmentos gerados que contenham vários planos.

## 5. Escolha pela intenção

| Intenção | Ponto de partida possível |
|---|---|
| apresentar lugar | geral + estática ou movimento lento |
| aproximar emocionalmente | close + push-in lento |
| mostrar descoberta | médio/detalhe + reveal ou rack focus |
| acompanhar jornada | tracking |
| evidenciar escala | geral/ângulo baixo + crane |
| criar isolamento | aberto + pull-out |
| transmitir urgência | handheld controlado + cobertura curta |
| contemplar | estática + plano longo |
| desorientar | ângulo inclinado ou dolly zoom justificado |

São possibilidades, não fórmulas.

## 6. Luz, cor e atmosfera

Descreva elementos observáveis:

- fonte;
- direção;
- qualidade dura/suave;
- contraste;
- temperatura;
- paleta dominante;
- cores evitadas;
- atmosfera;
- continuidade com planos vizinhos.

Evite “luz cinematográfica” sem origem, função e efeito observável.

## 7. Ação e tempo

Para um plano atômico:

```text
estado inicial → ação → reação → estado final
```

Para uma sequência dentro de um segmento:

```text
[0–2s] estado/ação
[2–5s] reação/deslocamento
[5–7s] estado final ou corte
```

Beats descrevem mudanças narrativas; não são automaticamente keyframes, planos ou arquivos gerados.

## 8. Som

Especifique quando aplicável:

- diálogo e idioma;
- ambiente;
- efeitos sincronizados;
- presença ou ausência de música;
- silêncio intencional;
- ponte sonora;
- direitos e origem dos elementos.

Não presuma que o modelo escolherá som coerente ou que áudio gerado seja desejável.

## 9. Continuidade

Verifique:

- posição e olhar;
- mãos e objetos;
- roupa, cabelo e acessórios;
- luz e horário;
- direção de movimento;
- eixo;
- estado anterior e seguinte;
- texto e marcas;
- ambiente e som.

O storyboard não deve alterar silenciosamente decisões aprovadas. Quando revelar uma decisão nova de staging, cobertura, câmera ou transição, registre-a e leve-a ao gate correspondente.

## 10. Relação entre unidades

```text
beat narrativo
≠ keyframe
≠ plano
≠ segmento gerado
≠ cena montada
```

- **beat:** mudança de informação, ação, emoção ou estado;
- **keyframe:** imagem de referência/decisão visual;
- **plano:** unidade contínua de câmera na montagem;
- **segmento gerado:** arquivo produzido pelo modelo, contendo um ou mais planos;
- **cena montada:** combinação editorial de planos/segmentos.

Não use a equivalência rígida `1 beat = 1 keyframe = 1 clipe`.

## 11. Como o MCP pode entrar

```text
pedido humano
→ brief/cartão estruturado
→ aprovação
→ operador/agente técnico
→ MCP em ambiente isolado
→ workflow conhecido
→ artefato
→ revisão humana
```

MCP reduz atrito operacional; não elimina direitos, gates, segurança ou conhecimento técnico.

## Checklist

- [ ] A função narrativa está clara?
- [ ] O enquadramento mostra o necessário?
- [ ] A câmera serve à intenção?
- [ ] Estados inicial/final são observáveis?
- [ ] Luz, cor e som são concretos?
- [ ] Referências têm função e direitos conhecidos?
- [ ] A continuidade foi conferida?
- [ ] Beat, keyframe, plano e segmento não foram confundidos?
- [ ] Decisões novas foram levadas ao gate?
- [ ] O resultado será revisado antes da publicação?
