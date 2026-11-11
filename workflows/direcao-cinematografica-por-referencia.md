# Direção cinematográfica por referência

Fluxo para transformar referências de cinema em decisões concretas para vídeo generativo: enquadramento, composição, técnica, luz, movimento, prompt e montagem.

> **Princípio:** não peça apenas “cinematic”. Especifique o que a câmera faz, o que a luz faz, como o sujeito se move e qual função dramática o plano cumpre.

## Quando usar

Use este fluxo quando um vídeo precisa de mais controle visual, continuidade entre planos ou uma direção estética coerente. Ele serve para vídeos explicativos, institucionais, teasers, vídeos de produto, faceless explainers e sequências geradas por IA.

Não é necessário visitar os seis sites em todos os casos. A rota é adaptativa:

- **Moodboard rápido:** Shot.Cafe ou FilmGrab.
- **Encontrar o nome de uma técnica:** Eyecannndy.
- **Escrever o prompt do plano:** Melies.
- **Resolver movimento de câmera:** AI Camera Movements.
- **Refinar luz, montagem e acabamento:** GrokFilm.

## Rota de pesquisa

### 1. Procurar referências de cortes

- [Shot.Cafe](https://shot.cafe)

Use para procurar frames por filme, tags, cores e características visuais. O objetivo é encontrar uma referência para a função do plano, não copiar um frame isolado.

**Anotar:** sujeito, escala do plano, posição no quadro, cor dominante, direção do olhar e sensação produzida.

### 2. Observar sistemas visuais de filmes

- [FilmGrab](https://film-grab.com)

Observe vários frames do mesmo filme, diretor ou cinematógrafo. Um único frame mostra um resultado; uma sequência revela o sistema: contraste, distância da câmera, recorrência de cores, uso de espaço negativo e ritmo visual.

**Anotar:** o que se repete entre os planos e o que muda de acordo com a narrativa.

### 3. Nomear a técnica

- [Eyecannndy](https://eyecannndy.com)

Use a biblioteca para descobrir o vocabulário técnico de uma referência: dolly, dolly zoom, tracking, central framing, split diopter, match cut, whip pan, halation, silhouette, rack focus e outros.

O nome é um ponto de partida. A técnica só deve entrar no prompt quando tiver função visual ou narrativa.

### 4. Entender a função e converter em prompt

- [Melies — Cinematic Techniques](https://melies.co/cinematic-techniques)

Use a definição da técnica para entender como ela funciona e qual efeito produz. O site também oferece linguagem de prompt para câmera, enquadramento, iluminação, composição, cor, movimento, efeitos e edição.

**Regra:** combinar uma intenção dramática com uma decisão técnica. “Dolly lento para aproximar o público do personagem” é mais útil do que “dolly cinematográfico”.

### 5. Especificar o movimento da câmera

- [AI Camera Movements](https://aicameramovements.com)

Use para selecionar uma trajetória simples e traduzi-la em prompt: tilt, pan, dolly, orbit, tracking, crane, slider ou câmera estática.

Para clipes curtos, preferir **um movimento primário por plano**. Movimentos complexos demais podem confundir o modelo e prejudicar a continuidade.

### 6. Refinar luz e montagem

- [GrokFilm](https://grokfilm.app)

Use como índice de técnicas de câmera, iluminação, composição, edição, som, narrativa, efeitos e gêneros. A linguagem pode ser adaptada para outros modelos; os botões e exemplos específicos de Grok não devem ser tratados como independentes de plataforma.

**Refinar:** luz motivada, contraste, temperatura de cor, ritmo, tipo de corte, transição, textura e atmosfera.

## Ficha de plano

Preencha antes de gerar. Se um campo não tiver função, deixe-o vazio em vez de acrescentar adjetivos genéricos.

```yaml
shot:
  id: "S01"
  purpose: "aproximar o público do personagem"
  narrative_beat: "o personagem percebe algo fora do quadro"
  reference_source: "FilmGrab"
  reference_url: "https://film-grab.com"
  reference_description: "personagem isolado em corredor escuro, espaço negativo à direita"
  technique: "slow dolly forward"
  framing: "medium close-up"
  angle: "eye level"
  lens_or_optics: "50mm spherical, shallow depth of field"
  composition: "negative space à direita, leading lines do corredor"
  subject: "uma educadora diante de uma porta entreaberta"
  action: "ela interrompe o movimento e olha para a luz"
  blocking: "personagem permanece no terço esquerdo do quadro"
  lighting: "motivated side light from the doorway, low-key interior"
  color: "cool shadows, warm light from the room"
  atmosphere: "subtle haze, restrained film grain"
  edit: "cut on reaction"
  continuity: "a luz da porta deve permanecer à direita no plano seguinte"
  model: "[modelo usado]"
  status: "to_test"
```

## Prompt-base para geração

```text
Crie um plano de vídeo generativo com a seguinte direção:

Função dramática: [o que o espectador deve sentir ou entender]
Sujeito: [quem ou o que aparece]
Ação: [uma ação clara e observável]
Enquadramento: [tamanho do plano]
Ângulo e perspectiva: [altura, lado, ponto de vista]
Lente/óptica: [se for relevante]
Composição: [posição, linhas, espaço negativo, profundidade]
Movimento da câmera: [um movimento primário, com direção e velocidade]
Blocking: [trajetória do sujeito no quadro]
Iluminação: [fonte motivada, direção, dureza e contraste]
Cor e textura: [paleta, contraste, grão ou acabamento]
Atmosfera: [névoa, chuva, poeira, fumaça ou ambiente — somente se necessário]
Montagem: [tipo de entrada, saída ou corte]
Continuidade: [relação com o plano anterior e o seguinte]

Evite uma estética genérica. Não adicione movimentos de câmera não solicitados,
objetos novos, mudança de horário ou mudança de direção da luz.
```

## Exemplo preenchido

```text
Plano médio fechado de uma educadora parada diante de uma porta entreaberta,
no terço esquerdo do quadro, com espaço negativo escuro à direita. A câmera faz
um slow dolly forward, muito suave, em direção ao rosto dela, na altura dos olhos,
com lente esférica de 50mm e profundidade de campo rasa. As linhas do corredor
conduzem o olhar até a porta. A iluminação interna é low-key e motivada pela luz
quente que vem da sala; o corredor tem sombras azuladas e contraste controlado.
Ela interrompe o movimento, percebe algo fora do quadro e olha para a luz. Leve
haze atmosférico e grão de filme discreto. Corte no momento da reação. Preserve
a porta e a fonte de luz no lado direito para manter continuidade no plano seguinte.
Não introduza outro personagem nem altere o horário da cena.
```

## Validação antes de aceitar o plano

- [ ] O plano tem uma função narrativa clara?
- [ ] Há uma ação observável e simples?
- [ ] O movimento da câmera é único, descrito com direção e velocidade?
- [ ] A composição foi escolhida por uma razão?
- [ ] A luz tem uma fonte ou motivação identificável?
- [ ] O plano mantém direção, personagem, cenário e paleta da sequência?
- [ ] O resultado funciona em movimento, não apenas como frame parado?
- [ ] O prompt evita depender apenas de “cinematic”, “beautiful” ou “high quality”?

## Direitos, licença e dependências

Os sites são referências para pesquisa e não autorizam automaticamente a redistribuição dos frames, GIFs ou trechos encontrados. Para moodboards privados ou estudo, preserve a fonte e o crédito. Para publicação, apresentação comercial ou material didático distribuído, verifique os termos do site e os direitos da obra original.

Não copie grandes blocos de texto de bibliotecas de prompts sem verificar a licença. Registre qual plataforma/modelo foi usado, especialmente quando o site oferece geração integrada, links afiliados ou recursos exclusivos de um fornecedor.

## Relação com outros workflows

- [Direção cinematográfica com Seedance/Higgsfield](seedance-direcao-cinematografica.md)
- [Vídeo generativo com narrativa musical](../docs/precedentes/video-generativo/machina-narrativa-musical.md)
- [Vídeo programático com Remotion](remotion-video-programatico.md)
- [Vídeo com HyperFrames](hyperframes-video-html.md)
