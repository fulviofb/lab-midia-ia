# Gramática cinematográfica prática para vídeo com IA

**Estado:** repertório conceitual sintetizado pelo laboratório; não prescreve uma estética.

Este guia ajuda a transformar intenção em direção observável. Pode apoiar filmagem, edição, vídeo programático, complementação generativa e produção narrativa.

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
Aproximação lenta quando ela encontra uma anotação.
Luz suave de janela, cores quentes e ambiente silencioso.
O plano termina com a mão indicando a frase.
```

## Modo detalhado

Use apenas os campos necessários do [`cartao-de-plano.yml`](../../templates/cartao-de-plano.yml).

---

## 1. Função narrativa

Possibilidades:

- **situar:** apresentar lugar, tempo ou escala;
- **explicar:** tornar informação ou ação legível;
- **aproximar:** criar intimidade;
- **revelar:** apresentar algo antes oculto;
- **acompanhar:** percorrer a ação;
- **contrastar:** evidenciar oposição ou mudança;
- **desorientar:** causar instabilidade intencional;
- **contemplar:** dar tempo para observar e sentir.

Um plano pode contribuir para várias funções, mas uma intenção dominante facilita avaliação e montagem.

## 2. Enquadramento e ângulo

### Tamanho do plano

| Escolha | Uso possível |
|---|---|
| Plano geral/extremo | lugar, escala, contexto, isolamento |
| Plano inteiro | corpo, deslocamento, relação espacial |
| Plano médio | conversa, gesto, ação cotidiana |
| Close-up | emoção, reação, decisão |
| Detalhe/extremo close | informação, textura, objeto narrativo |
| Sobre o ombro (OTS) | relação e ponto de vista parcial |
| Ponto de vista (POV) | percepção do personagem |

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
- âncoras espaciais.

A composição serve à informação e à emoção, não apenas à aparência. Áreas grandes sem função podem enfraquecer a peça mesmo quando o render está tecnicamente correto.

## 4. Movimento de câmera

| Movimento | Operação | Uso possível |
|---|---|---|
| Estática | não se desloca | clareza, observação, solenidade |
| Panorâmica horizontal (pan) | gira horizontalmente | seguir ou revelar lateralmente |
| Panorâmica vertical (tilt) | gira verticalmente | revelar altura |
| Aproximação/afastamento físico (dolly) | desloca em profundidade | intensificar ou contextualizar |
| Deslocamento lateral (truck) | move lateralmente | acompanhar e criar paralaxe |
| Elevação (pedestal) | sobe/desce sem inclinar | reenquadrar verticalmente |
| Acompanhamento (tracking) | segue o sujeito | jornada e continuidade |
| Órbita (orbit) | circula o sujeito | ênfase e mudança de perspectiva |
| Grua (crane/jib) | move em arco/altura | escala e revelação espacial |
| Câmera na mão (handheld) | movimento orgânico | urgência ou presença documental |
| Panorâmica rápida (whip pan) | giro muito rápido | transição energética |

### Lente e foco

- **zoom:** altera o campo de visão sem mover a câmera;
- **mudança de foco (rack focus):** transfere foco entre planos;
- **dolly zoom:** combina dolly e zoom em sentidos opostos;
- **profundidade rasa:** isola sujeito;
- **foco profundo:** mantém camadas legíveis.

Como regra de diagnóstico, um movimento dominante por plano atômico facilita identificar o que funcionou. Não é proibição universal nem regra para segmentos que contenham vários planos.

## 5. Escolha pela intenção

| Intenção | Ponto de partida possível |
|---|---|
| apresentar lugar | geral + estática ou movimento lento |
| aproximar emocionalmente | close + aproximação lenta |
| mostrar descoberta | médio/detalhe + revelação ou mudança de foco |
| acompanhar jornada | tracking |
| evidenciar escala | geral/ângulo baixo + grua |
| criar isolamento | aberto + afastamento |
| transmitir urgência | câmera na mão controlada + cobertura curta |
| contemplar | estática + plano longo |
| desorientar | inclinação ou dolly zoom justificado |

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

O storyboard não deve alterar silenciosamente decisões aprovadas. Quando revelar decisão nova de posicionamento, cobertura, câmera ou transição, registre alternativas e leve-as ao gate correspondente.

## 10. Relação entre unidades

```text
beat narrativo
≠ quadro-chave de storyboard
≠ imagem de condicionamento
≠ plano
≠ segmento gerado
≠ cena montada
```

- **beat:** mudança de informação, ação, emoção ou estado;
- **quadro-chave de storyboard:** imagem que representa uma decisão visual do plano/cena;
- **imagem de condicionamento:** input usado para orientar uma geração;
- **plano (shot):** unidade contínua de câmera na montagem;
- **segmento gerado:** arquivo produzido pelo modelo, contendo um ou mais planos;
- **cena montada:** unidade narrativa composta por planos/segmentos.

Não use a equivalência rígida `1 beat = 1 quadro-chave = 1 clipe`.

## 11. Uso conforme a rota

- **edição direta:** ajuda a selecionar enquadramentos e cortes existentes;
- **vídeo programático:** orienta composição, hierarquia, ritmo e movimento;
- **montagem híbrida:** cria linguagem comum entre materiais diferentes;
- **complementação generativa:** define o plano ausente sem regenerar o projeto inteiro;
- **narrativa generativa:** apoia storyboard, cobertura, continuidade e avaliação.

## 12. Glossário híbrido

| Termo | Sentido neste laboratório |
|---|---|
| Bible visual | memória externa de identidades, ambientes, regras e variações |
| Prop | objeto de cena com função/continuidade |
| Staging | posicionamento e deslocamento em cena |
| Eyeline | direção coerente do olhar |
| Lock | aspecto aprovado que deve permanecer estável |
| Assembly | primeira montagem das seleções |
| Rough cut | corte provisório usado para avaliar e descobrir lacunas |
| Fine cut | corte refinado antes do travamento |
| Picture lock | ordem, duração e pontos de corte congelados |
| Cleanup | reparo/limpeza visual posterior |
| Sound design | construção de ambientes e efeitos sonoros |
| First/last frame | imagens usadas para condicionar estados inicial/final |

## Checklist

- [ ] A função narrativa está clara?
- [ ] O enquadramento mostra o necessário?
- [ ] A câmera serve à intenção?
- [ ] Estados inicial/final são observáveis?
- [ ] Luz, cor e som são concretos?
- [ ] Referências têm função e direitos conhecidos?
- [ ] A continuidade foi conferida?
- [ ] Quadro-chave, condicionamento, plano e segmento não foram confundidos?
- [ ] Decisões novas foram submetidas ao gate?
- [ ] A escolha continua sendo possibilidade, não fórmula automática?
