# Trilha 03 — Vídeo explicativo narrado

## Para quem é

Para quem quer explicar uma ideia, campanha, estudo, projeto social, atividade da casa espírita ou tema doutrinário em formato audiovisual curto.

## Resultado esperado

Um vídeo de 1 a 3 minutos com:

- roteiro claro;
- narração;
- cenas ou imagens de apoio;
- textos pontuais;
- chamada final.

## Estrutura recomendada

```txt
1. Abertura: problema ou pergunta
2. Contexto: por que isso importa
3. Explicação: 2 ou 3 ideias principais
4. Exemplo prático
5. Convite/chamada final
```

## Passo a passo

### 1. Defina o público

Exemplos:

- jovens;
- trabalhadores da casa espírita;
- famílias;
- evangelizadores;
- público geral;
- equipe de comunicação.

### 2. Crie roteiro com a LLM

```txt
Crie um roteiro de vídeo explicativo de até 2 minutos sobre [tema].
Público: [público].
Tom: claro, fraterno, educativo e sem sensacionalismo.
Estrutura:
1. abertura com pergunta;
2. explicação simples;
3. exemplo prático;
4. convite final.
Inclua sugestões de cenas visuais e texto na tela.
```

### 3. Gere narração

Opções:

- gravar com voz humana;
- usar TTS com consentimento e transparência;
- Voicebox/GPT-SoVITS/Fish Speech quando testados;
- ElevenLabs, PlayHT ou similares com atenção a custo/licença.

### 4. Crie apoio visual

Use imagens, ícones, vídeos simples ou motion graphics.

Ferramentas possíveis:

- Canva/CapCut para iniciantes;
- HyperFrames para vídeo HTML/CSS/GSAP;
- Remotion para vídeo React;
- ferramentas generativas de imagem/vídeo para cenas pontuais.

### 5. Monte e revise

A revisão deve olhar não só beleza, mas fidelidade da mensagem.

Perguntas úteis:

- Isso ensina ou só impressiona?
- A estética combina com o conteúdo?
- Há exagero visual?
- A narração está natural?
- Alguém leigo entende?

## Checklist final

- [ ] O vídeo tem uma ideia central?
- [ ] A narração é clara?
- [ ] O visual não compete com a mensagem?
- [ ] Há cuidado ético/doutrinário?
- [ ] O final convida para uma ação concreta?

## Próximo passo técnico

Se quiser automatizar ou padronizar vídeos explicativos, consulte:

- `workflows/hyperframes-video-html.md`
- `workflows/remotion-video-programatico.md`
- `prompts/video-explicativo-narrado.md`
