# Mapa de ferramentas

Este documento ajuda a escolher a ferramenta certa conforme o objetivo.

## Quero editar vídeos brutos com agente

Use primeiro:

1. `browser-use/video-use`
2. FFmpeg workflows
3. `OpenReel Video` ou `OpenCut` para acabamento visual/manual

Bom para entrevistas, aulas, vídeos falados, cortes para Reels/Shorts, legenda automática, remoção de pausas e filler words.

## Quero editar visualmente no navegador, estilo CapCut

Use/candidate primeiro:

1. `Augani/openreel-video` — editor browser-based, 100% client-side, WebCodecs/WebGPU, MIT. Próximo candidato de smoke test.
2. `OpenCut` — alternativa open-source ao CapCut, mas acompanhar maturidade/reescrita.
3. Editores comerciais quando o objetivo for entrega rápida e não laboratório/reprodutibilidade.

Escolha OpenReel quando quiser privacidade/local-first no navegador, timeline visual e export direto sem depender de nuvem. Testar desempenho com arquivos reais antes de recomendar para pessoas iniciantes.

## Quero criar vídeo animado por código

Use primeiro:

1. HyperFrames
2. Remotion Agent Skills

Escolha **HyperFrames** quando quiser HTML/CSS/GSAP e um fluxo bem agent-first. Escolha **Remotion** quando quiser React, componentes reutilizáveis e controle frame-by-frame.

## Quero gerar short video automático

Use primeiro:

1. MoneyPrinterTurbo
2. Workflows próprios com roteiro → cenas → narração → render
3. Ferramentas de produto/e-commerce/UGC, com revisão de licença e dependência de API

## Quero vídeo generativo estilo Higgsfield/Seedance

Use como referência:

1. `Emily2040/seedance-2.0`
2. `OSideMedia/higgsfield-ai-prompt-skill`
3. `ZeroLu/awesome-seedance`

Regra de ouro: não peça apenas “cinematic”. Defina intenção da cena, ação, câmera, luz, performance e continuidade.

## Quero voz, narração ou clonagem

Use primeiro:

1. Voicebox — estúdio completo local-first; instalação desktop pendente para teste prático.
2. GPT-SoVITS — clonagem/TTS técnico e consolidado.
3. Fish Speech — TTS open-source de alta qualidade.
4. MisoTTS — fala expressiva em inglês, mais experimental.

Com RTX 4060 Laptop GPU 8 GB, vale testar workflows locais mais pesados do que seria recomendado para CPU/Intel UHD apenas.

## Quero transcrição

Use primeiro:

1. Whisper/local quando privacidade ou custo forem prioridade.
2. ElevenLabs Scribe quando houver API key com permissão `speech_to_text`.
3. video-use helpers para integrar transcrição ao fluxo de edição.

Status atual: Scribe foi testado até upload, mas bloqueou porque a API key não tinha permissão `speech_to_text`.

## Quero melhorar design, thumbnails e imagem

Use primeiro:

1. `ui-ux-pro-max-skill`
2. `awesome-gpt-image-2`
3. `awesome-nano-banana-pro-prompts`

## Como avaliar um novo repo

Use esta checklist:

- Tem licença clara?
- Está atualizado?
- Tem README prático?
- Tem exemplos reais?
- Exige GPU local?
- Aproveita GPU dedicada ou WebGPU?
- Depende de API paga?
- Roda no Windows?
- Tem Docker ou modo browser?
- É útil para iniciantes ou só para referência técnica?
- Pode ser usado com agente?
- Produz artefato verificável?
