# Gramática cinematográfica prática para vídeo com IA

Este guia ajuda a transformar uma intenção simples em direção executável. Ele serve para conversa com o Assistente de Mídia IA, vídeo generativo, storyboard, filmagem comum, Remotion e workflows ComfyUI.

> Não comece perguntando “qual efeito usar?”. Comece perguntando: **o que o público deve perceber, sentir ou compreender neste plano?**

## Modo simples — cinco decisões

Para iniciantes, um plano precisa de apenas cinco respostas:

1. **O que aparece?** — sujeito, ambiente e objeto importante.
2. **O que acontece?** — uma ação principal, em ordem temporal.
3. **Como enquadrar?** — aberto, médio, próximo ou detalhe.
4. **Como a câmera se comporta?** — parada ou um movimento principal.
5. **Qual sensação?** — luz, cor, ritmo e som coerentes com a intenção.

Exemplo:

```text
Uma educadora abre um livro antigo sobre a mesa.
Plano médio, câmera na altura dos olhos.
Push-in lento enquanto ela encontra uma anotação.
Luz suave de janela, cores quentes, ambiente silencioso com páginas virando.
Terminar com a mão apontando para a frase.
```

## Modo avançado — cartão de plano

```yaml
shot_id: CENA01-PLANO03
purpose: "O que este plano revela ou faz o público sentir"
duration_s: 6
subject: "Quem ou o que é o foco"
initial_state: "Posição, olhar, objeto e luz no início"
action: "Uma ação principal em ordem temporal"
final_state: "Posição, olhar e objeto no final"
framing: "Tamanho do plano + ângulo"
composition: "Posição no quadro + camadas + direção do olhar"
camera: "Um movimento principal, com início e fim"
lens_focus: "Distância focal aparente + profundidade + mudança de foco"
lighting_color: "Fonte, direção, contraste, paleta e atmosfera"
audio: "Diálogo, ambiente, efeitos e música ou ausência dela"
references: "ID e função de cada referência aprovada"
continuity: "O que precisa coincidir com os planos vizinhos"
constraints: "Poucas restrições verificáveis"
acceptance: "Como saber se o plano passou"
```

## 1. Função narrativa

Escolha primeiro a função do plano:

- **situar:** mostrar onde estamos;
- **explicar:** tornar uma ação ou informação legível;
- **aproximar:** criar intimidade;
- **revelar:** apresentar algo que estava oculto;
- **acompanhar:** fazer o público percorrer a ação;
- **contrastar:** mostrar mudança, oposição ou descoberta;
- **desorientar:** causar instabilidade de modo consciente;
- **contemplar:** dar tempo para sentir e observar.

Se o plano tenta cumprir quatro funções ao mesmo tempo, divida-o.

## 2. Enquadramento e ângulo

### Tamanho do plano

| Escolha | Uso principal |
|---|---|
| Plano geral/extremo | Lugar, escala, contexto e isolamento |
| Plano inteiro | Corpo, deslocamento e relação com o espaço |
| Plano médio | Conversa, gesto e ação cotidiana |
| Close-up | Emoção, reação e decisão |
| Detalhe/extremo close | Informação específica, textura e objeto narrativo |
| OTS/sobre o ombro | Relação, diálogo e ponto de vista parcial |
| POV | O que o personagem vê |

### Ângulo

| Escolha | Efeito provável |
|---|---|
| Altura dos olhos | Neutralidade e proximidade |
| Ângulo baixo | Presença, poder ou escala |
| Ângulo alto | Fragilidade, mapa ou redução de escala |
| Vista superior | Geometria, organização e localização |
| Inclinação holandesa | Instabilidade; usar apenas com intenção clara |

O efeito depende do contexto. Um ângulo baixo não torna alguém “poderoso” automaticamente.

## 3. Composição

Defina:

- posição do sujeito: esquerda, centro ou direita;
- primeiro plano, plano intermediário e fundo;
- espaço na direção do olhar ou movimento;
- linhas que conduzem a atenção;
- simetria ou desequilíbrio intencional;
- objeto ou área que deve permanecer livre para texto;
- direção de tela que continuará no próximo corte.

A composição deve servir à informação e à emoção, não apenas “ficar bonita”.

## 4. Movimento de câmera

### Movimentos físicos

| Movimento | O que a câmera faz | Uso comum |
|---|---|---|
| Estática | Não se move | Clareza, observação, solenidade |
| Pan | Gira horizontalmente | Seguir ou revelar lateralmente |
| Tilt | Gira verticalmente | Mostrar altura ou revelar de baixo para cima |
| Dolly in/out | Aproxima ou afasta fisicamente | Intensificar ou revelar contexto |
| Truck lateral | Desloca para o lado | Acompanhar ação ou mudar paralaxe |
| Pedestal | Sobe ou desce sem inclinar | Reenquadrar verticalmente |
| Tracking | Mantém relação com sujeito em movimento | Jornada e continuidade |
| Orbit | Circula o sujeito | Ênfase e mudança de perspectiva |
| Crane/jib | Move em arco ou altura | Revelação espacial e escala |
| Handheld | Movimento orgânico de mão | Urgência, presença ou documental |
| Whip pan | Pan muito rápido | Transição energética; usar com parcimônia |

### Operações de lente e foco

Não confunda com deslocamento físico:

- **zoom:** altera o campo de visão sem mover a câmera;
- **rack focus:** muda o foco entre planos de profundidade;
- **dolly zoom:** combina deslocamento e zoom opostos para distorcer a perspectiva;
- **profundidade rasa:** isola o sujeito;
- **foco profundo:** mantém ambiente e sujeito legíveis.

Regra prática: **um movimento dominante por plano**. Se a câmera faz dolly, órbita, zoom e whip pan em seis segundos, o modelo e o público perdem a intenção.

## 5. Escolha pela intenção

| Intenção | Possível combinação |
|---|---|
| Apresentar o lugar | Plano geral + câmera estática ou movimento lento |
| Aproximar emocionalmente | Close-up + push-in lento |
| Mostrar descoberta | Plano médio/detalhe + reveal ou rack focus |
| Acompanhar jornada | Tracking lateral, frontal ou traseiro |
| Evidenciar escala | Ângulo baixo ou plano geral + crane |
| Criar isolamento | Plano aberto + pull-out lento |
| Transmitir urgência | Handheld controlado + cortes mais curtos |
| Criar contemplação | Estática, composição limpa e plano mais longo |
| Sinalizar desorientação | Ângulo inclinado ou dolly zoom, com justificativa narrativa |

Essas combinações são pontos de partida, não fórmulas obrigatórias.

## 6. Luz, cor e atmosfera

Descreva elementos observáveis:

- fonte: janela, sol, lua, vela, luminária, tela;
- direção: frontal, lateral, traseira, superior;
- qualidade: dura ou suave;
- contraste: alto ou baixo;
- temperatura: quente, neutra ou fria;
- paleta: cores dominantes e cores que devem ser evitadas;
- atmosfera: limpa, névoa, chuva, poeira, fumaça;
- continuidade: o que não pode mudar entre planos.

Evite “luz cinematográfica” sem dizer de onde ela vem e o que revela.

## 7. Ação e tempo

Descreva a ação como processo:

```text
Estado inicial → ação → reação → estado final
```

Para um plano mais longo, use beats:

```text
[0–2s] observa o objeto
[2–5s] aproxima a mão e o abre
[5–7s] encontra a marca e olha para fora do quadro
```

Cada beat deve terminar em um estado que o próximo consiga continuar.

## 8. Som

Especifique:

- diálogo exato e idioma;
- ambiente;
- efeitos sincronizados;
- presença ou ausência de música;
- silêncio intencional;
- ponte sonora para o corte seguinte.

Não confie que o modelo escolherá automaticamente um som coerente com a mensagem.

## 9. Continuidade

Antes de aprovar, confira:

- posição e direção do olhar;
- mão que segura o objeto;
- roupa, cabelo e acessórios;
- luz e horário;
- direção de movimento;
- eixo entre personagens;
- estado final do plano anterior;
- texto e marcas;
- ambiente, trilha e ruído de fundo.

O storyboard **não deve inventar decisões novas**. Ele traduz decisões já aprovadas no roteiro, na bíblia visual e nos cartões de plano.

## 10. Como o MCP entra sem virar a porta de entrada

O MCP reduz a dificuldade operacional do ComfyUI, mas não elimina a necessidade de brief, direitos, aprovação e revisão.

```text
Pessoa leiga
→ receita ou Assistente de Mídia IA
→ cartão de plano estruturado
→ aprovação humana
→ agente técnico + MCP
→ workflow ComfyUI conhecido
→ artefato
→ revisão humana
```

A pessoa leiga não precisa aprender nodes. O operador técnico mantém:

- ambiente isolado;
- workflows aprovados;
- modelos compatíveis com o hardware;
- limites de diretório e rede;
- registro de versões e custos externos;
- inspeção do resultado.

## Checklist final

- [ ] O plano tem uma função narrativa clara?
- [ ] Existe somente uma ação central?
- [ ] O enquadramento mostra a informação necessária?
- [ ] O movimento de câmera serve à intenção?
- [ ] Estado inicial e final estão definidos?
- [ ] Luz, cor e som estão concretos?
- [ ] Referências têm função e direitos conhecidos?
- [ ] A continuidade com os planos vizinhos foi conferida?
- [ ] O resultado será revisado antes da publicação?
