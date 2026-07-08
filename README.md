# Lab Mídia IA

Curadoria prática em português de ferramentas, skills, prompts e workflows para criar **vídeo, voz, imagem, design e edição com IA**.

Este repositório é um laboratório público e reproduzível: não é só uma lista de links. Cada ferramenta importante deve ter contexto, status de teste, riscos, licença, comandos e próximos passos.

## Para quem é

- Pessoas que perguntam como criar vídeos, imagens e vozes com IA.
- Criadores de conteúdo, educadores, consultores e equipes de marketing.
- Desenvolvedores que querem automatizar produção de mídia com agentes.
- Quem quer entender diferenças entre Remotion, HyperFrames, video-use, OpenReel, OpenCut, Seedance, Higgsfield, Voicebox e ferramentas de short video.

## O que este repo contém

- `catalog.yml`: catálogo estruturado dos repositórios e ferramentas.
- `docs/guias/`: guias em português para iniciantes.
- `docs/trilhas/`: caminhos práticos por objetivo e nível técnico.
- `docs/publico/`: materiais para compartilhar com pessoas leigas, inclusive uso com LLM sem CLI.
- `docs/estrategia/`: estratégia de formação, site Concafras IA e possíveis ofertas.
- `docs/testes/`: relatórios de testes práticos e bloqueios encontrados.
- `docs/workarounds/`: soluções para problemas específicos, especialmente no Windows.
- `docs/scripts/`: documentação dos scripts de automação.
- `workflows/`: fluxos práticos por tipo de tarefa.
- `prompts/`: prompts reutilizáveis para vídeo, imagem, UGC, narração, thumbnails e orientação com LLM.
- `examples/`: espaço para exemplos reproduzíveis leves.
- `scripts/`: automações do laboratório, como atualização de metadados do catálogo.

## Categorias principais

1. **Vídeo programático** — Remotion, HyperFrames, HTML-to-video, animações por código.
2. **Edição com agentes** — video-use, FFmpeg e workflows automatizados.
3. **Editores visuais/browser-based** — OpenReel, OpenCut e alternativas open-source ao CapCut.
4. **Vídeo automático/social** — Shorts, Reels, UGC, anúncios e vídeos de produto.
5. **Vídeo generativo/cinematográfico** — Seedance, Higgsfield, direção cinematográfica e prompts avançados.
6. **Voz/TTS/clonagem** — Voicebox, GPT-SoVITS, Fish Speech, MisoTTS e ferramentas de narração.
7. **Imagem/design/prompts** — GPT Image, Nano Banana, UI/UX skills, thumbnails e capas.

## Repositórios núcleo do laboratório

### Agent-first / vídeo por código

- [`browser-use/video-use`](https://github.com/browser-use/video-use) — edição de vídeo com agentes.
- [`heygen-com/hyperframes`](https://github.com/heygen-com/hyperframes) — HTML/CSS/animações para MP4, feito para agentes.
- [Remotion Agent Skills](https://www.remotion.dev/docs/ai/skills) — base oficial para vídeo programático em Remotion.

### Editores visuais

- [`Augani/openreel-video`](https://github.com/Augani/openreel-video) — editor de vídeo profissional no navegador, alternativa open-source ao CapCut; candidato a smoke test com WebGPU/WebCodecs.
- [`OpenCut-app/OpenCut`](https://github.com/OpenCut-app/OpenCut) — alternativa open-source ao CapCut; acompanhar maturidade e reescrita.

### Automação, voz, vídeo generativo e design

- [`harry0703/MoneyPrinterTurbo`](https://github.com/harry0703/MoneyPrinterTurbo) — geração automática de short videos.
- [`jamiepine/voicebox`](https://github.com/jamiepine/voicebox) — estúdio open-source/local-first de voz.
- [`RVC-Boss/GPT-SoVITS`](https://github.com/RVC-Boss/GPT-SoVITS) — TTS e clonagem de voz few-shot.
- [`Emily2040/seedance-2.0`](https://github.com/Emily2040/seedance-2.0) — direção cinematográfica para Seedance 2.0.
- [`OSideMedia/higgsfield-ai-prompt-skill`](https://github.com/OSideMedia/higgsfield-ai-prompt-skill) — prompts cinematográficos para Higgsfield e modelos de vídeo.
- [`ZeroLu/awesome-seedance`](https://github.com/ZeroLu/awesome-seedance) — biblioteca de prompts e recursos Seedance.
- [`nextlevelbuilder/ui-ux-pro-max-skill`](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) — design intelligence para agentes.
- [`YouMind-OpenLab/awesome-gpt-image-2`](https://github.com/YouMind-OpenLab/awesome-gpt-image-2) — biblioteca de prompts de imagem.

## Status dos testes iniciais

- `video-use`: parcialmente testado no Windows; edição/render funcionaram; Scribe bloqueado por permissão da API key.
- `HyperFrames`: testado e recomendado no Windows, com workaround documentado para browser path.
- `Remotion Agent Skills`: testado e recomendado no Windows; atenção à licença comercial do Remotion.
- `Voicebox`: documentado a partir de código/release; precisa instalação manual do app desktop para teste prático.
- `OpenReel Video`: catalogado; próximo candidato de teste prático com navegador e GPU dedicada.

## Como usar este repo

1. Comece por `docs/guias/00-pre-requisitos.md`.
2. Leia `docs/guias/01-por-onde-comecar.md` para escolher uma ferramenta.
3. Se você quer ajudar uma pessoa leiga, use `docs/publico/como-usar-com-llm-sem-cli.md`.
4. Se você quer um caminho por objetivo, veja `docs/trilhas/`.
5. Consulte `catalog.yml` para status, licença e prioridade.
6. Use os workflows e prompts como ponto de partida.
7. Antes de recomendar uma ferramenta para outra pessoa, veja se há relatório em `docs/testes/`.

## Trilhas práticas

- `docs/trilhas/01-primeiro-video-com-ia.md`
- `docs/trilhas/02-transformar-aula-em-cortes.md`
- `docs/trilhas/03-video-explicativo-narrado.md`
- `docs/trilhas/04-narracao-e-voz-com-ia.md`
- `docs/trilhas/05-video-programatico-para-devs.md`

## Site Concafras IA

Este repositório também serve como base viva para atualizar e sustentar o site:

<https://concafras-ia.vercel.app/>

Estratégia documentada em:

- `docs/estrategia/site-concafras-e-formacao.md`
- `docs/publico/como-usar-com-llm-sem-cli.md`
- `prompts/prompt-mestre-consultor-midia-ia.md`

## Cuidados importantes

- Nem todo repo com estrelas altas é pronto para produção.
- Alguns projetos dependem de APIs pagas, mesmo sendo open-source.
- Repositórios sem licença clara devem ser **linkados**, não copiados.
- Clonagem de voz e geração de imagem/vídeo exigem consentimento, responsabilidade e cuidado com direitos autorais.
- Não coloque API keys, mídias privadas ou dados pessoais neste repositório.

## Automação do catálogo

Para atualizar estrelas, forks, issues e datas via GitHub API:

```bash
python scripts/update_github_metadata.py --dry-run
python scripts/update_github_metadata.py --write
```

Veja `docs/scripts/update_github_metadata.md`.

## Próximos testes recomendados

1. Smoke test do `Augani/openreel-video` no Windows com Chrome/Edge, WebGPU/WebCodecs e RTX 4060 Laptop GPU.
2. Teste prático do Voicebox após instalação do MSI.
3. Re-execução do ElevenLabs Scribe quando houver API key com permissão `speech_to_text`.
4. Separar `catalog.yml` por categoria quando o catálogo crescer mais.
