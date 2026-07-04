# Guia: Quero criar vídeo com IA — por onde começo?

Você chegou até aqui querendo usar IA para criar ou editar vídeo e não sabe qual ferramenta escolher. Este guia te ajuda a decidir em 5 minutos.

## Primeira pergunta: que tipo de vídeo você quer?

### A) "Tenho um vídeo bruto e quero editar"

Você gravou uma aula, entrevista, podcast ou falar para a câmera e quer:

- cortar pausas e filler words;
- gerar legendas;
- aplicar fades, overlays, color grading;
- exportar um `final.mp4`.

**Ferramenta recomendada:** [browser-use/video-use](https://github.com/browser-use/video-use)

Ver guia: `docs/guias/04-edicao-com-video-use.md`

### B) "Quero criar um vídeo animado do zero com código"

Você quer produzir um motion graphic, title card, vídeo explicativo animado ou peça visual sem footage bruto.

**Duas opções principais:**

| Critério | HyperFrames | Remotion |
|---|---|---|
| Linguagem | HTML/CSS/GSAP | React |
| Melhor quando | agente vai montar HTML direto | projeto React com componentes |
| Curva de aprendizado | menor | média |
| Render local | sim, CLI simples | sim, CLI com bundler |
| Licença | Apache-2.0 | licença especial (verificar uso comercial) |
| Skills para agentes | 21 skills instaláveis | 1 skill (`remotion-best-practices`) |
| Testado no Windows | sim | sim |

**Regra prática:**

- se você ou seu agente pensam em HTML/CSS → **HyperFrames**;
- se você pensa em componentes React, props e reutilização → **Remotion**.

Ver guias:

- `docs/guias/02-primeiro-video-com-hyperframes.md`
- `docs/guias/03-primeiro-video-com-remotion.md`

### C) "Quero gerar um short automático a partir de um tema"

Você quer dar um tema e gerar um vídeo curto automático (estilo "faceless channel").

**Ferramenta de referência:** [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)

Ainda não testado localmente. Linkar e estudar antes de adaptar.

### D) "Quero vídeo generativo estilo Sora/Higgsfield"

Você quer gerar vídeo a partir de texto (text-to-video cinematográfico).

**Ferramentas de referência:**

- `seedance-2.0`
- `higgsfield-ai-prompt-skill`

Atenção: este não é o foco principal do `lab-midia-ia`. O foco aqui é vídeo **programável e editável por agentes**, não vídeo generativo puro.

### E) "Quero voz/narração"

Você quer gerar narração com IA, clonar voz ou fazer TTS local.

**Ferramentas de referência:**

- Voicebox (local-first, ainda não testado localmente);
- GPT-SoVITS (clonagem/TTS);
- Fish Speech (TTS open-source);
- ElevenLabs (API, paga).

Ver workflow futuro: Issue #5 e #9.

### F) "Quero melhorar design, thumbnails e imagem"

**Ferramentas de referência:**

- `ui-ux-pro-max-skill`
- `awesome-gpt-image-2`
- `awesome-nano-banana-pro-prompts`

## Resumo visual

```txt
Tenho vídeo bruto → editar      → video-use
Quero animar do zero com HTML   → HyperFrames
Quero animar do zero com React  → Remotion
Quero short automático          → MoneyPrinterTurbo (referência)
Quero text-to-video cinematográfico → Seedance/Higgsfield (referência)
Quero voz/narração              → Voicebox / GPT-SoVITS / ElevenLabs
Quero thumbnail/design          → ui-ux-pro-max / gpt-image-2
```

## Antes de começar

Leia o guia de pré-requisitos:

```txt
docs/guias/00-pre-requisitos.md
```

E o guia de ética e licenças:

```txt
docs/08-etica-licencas-privacidade.md
```

## Princípios deste laboratório

1. **Linkar fontes originais** em vez de copiar código sem licença.
2. **Testar antes de recomendar.**
3. **Documentar o que funcionou e o que não funcionou.**
4. **Nunca incluir credenciais** em arquivos ou issues.
5. **Usar prompts próprios** em português quando possível.
