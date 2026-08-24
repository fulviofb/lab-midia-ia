# Roadmap

Este roadmap organiza os próximos passos do `lab-midia-ia` como laboratório público, prático e reproduzível de mídia com IA.

## Fase 1 — Fundação da curadoria

- [x] Criar repositório no GitHub pessoal.
- [x] Criar `README.md` inicial.
- [x] Criar `catalog.yml` com repositórios classificados.
- [x] Criar mapa inicial de ferramentas.
- [x] Criar documento de ética, licenças e privacidade.
- [x] Validar licenças dos projetos principais.
- [x] Tornar o repositório público para compartilhamento.
- [ ] Separar o catálogo em arquivos por categoria quando crescer.

## Fase 2 — Workflows práticos prioritários

- [x] `browser-use/video-use` — edição de vídeo com agente.
- [x] `heygen-com/hyperframes` — vídeo a partir de HTML/CSS/animações.
- [x] Remotion Agent Skills — vídeo programático em React/Remotion.
- [x] `jamiepine/voicebox` — documentado como app desktop; teste prático depende de instalação manual.
- [x] ElevenLabs Scribe via `video-use` — fluxo validado até upload; bloqueado por API key sem `speech_to_text`.
- [ ] `Augani/openreel-video` — editor browser-based, próximo smoke test recomendado.
- [ ] `RVC-Boss/GPT-SoVITS` ou alternativa local de TTS/clonagem para teste com GPU dedicada.

Cada teste deve gerar:

- pré-requisitos;
- comandos de instalação;
- mídia sintética/consentida usada;
- problemas encontrados;
- custo/API necessária;
- resultado validado com ferramenta (`ffprobe`, screenshots, logs etc.);
- veredito: recomendado, promissor, apenas referência ou evitar por enquanto.

## Fase 3 — Guias para pessoas iniciantes

- [x] Pré-requisitos e instalação.
- [x] “Quero criar vídeo com IA, por onde começo?”
- [x] Primeiro vídeo com HyperFrames.
- [x] Primeiro vídeo com Remotion.
- [x] Edição com `video-use`.
- [x] Narração com IA de forma ética.
- [x] Ideia → roteiro → cenas → vídeo.
- [x] Mapa adaptativo de rotas: edição, vídeo programático, montagem híbrida, complementação e narrativa generativa.
- [x] Gramática cinematográfica como repertório transversal, sem estética prescrita.
- [ ] Validar em pilotos os módulos/templates de produção antes de recomendá-los como padrão para contextos específicos.
- [x] Guia comparativo inicial por objetivo em `docs/01-mapa-de-ferramentas.md`.
- [x] Trilhas práticas para pessoas leigas/intermediárias/técnicas.
- [x] Prompt mestre para usar o repositório com ChatGPT/Claude/Gemini sem CLI.
- [ ] Guia comparativo OpenReel vs OpenCut vs video-use após smoke test do OpenReel.

## Fase 4 — Templates e exemplos

- [x] Prompt de vídeo explicativo narrado.
- [x] Prompt UGC/anúncio de produto.
- [x] Prompt de vídeo programático com Remotion.
- [x] Prompts HyperFrames para site/motion graphic.
- [x] Templates modulares de cena, plano, segmento, experimento, assets, tentativas e revisão — estado `lab_synthesis`.
- [x] Fixture sintética mínima e validador de relações estruturais.
- [ ] Aplicar os templates em piloto controlado e revisar campos, perfis e gates.
- [ ] Exemplo leve de projeto OpenReel exportado/importável, se o formato for adequado para versionamento.
- [ ] Exemplo reproduzível de narração local após teste de Voicebox/GPT-SoVITS.

## Fase 5 — Automação do catálogo

- [x] Script para atualizar metadados do GitHub:
  - estrelas;
  - forks;
  - issues abertas;
  - licença;
  - data de atualização;
  - linguagem principal;
  - topics.
- [x] Modo `--dry-run` e `--write`.
- [x] Documentação em `docs/scripts/update_github_metadata.md`.
- [ ] Rodar periodicamente antes de compartilhar curadorias novas.

## Fase 6 — Site Concafras IA e formação

- [x] Diagnosticar o papel do site `concafras-ia.vercel.app` como porta de entrada pública.
- [x] Documentar estratégia em `docs/estrategia/site-concafras-e-formacao.md`.
- [x] Criar materiais públicos para uso com LLM sem CLI.
- [ ] Atualizar o site com seção “Comece por aqui”.
- [ ] Linkar trilhas práticas do `lab-midia-ia` no site.
- [ ] Criar formulário de diagnóstico para direcionar pessoas por objetivo/nível.
- [x] Criar export público JSON/Markdown do catálogo para alimentar o site.
- [ ] Integrar o export público ao build do site Concafras IA.
- [ ] Testar o fluxo com 3 pessoas reais e revisar linguagem.

## Próximos testes prioritários

### 1. OpenReel Video

Objetivo: validar se o editor browser-based é prático no Windows com Chrome/Edge, WebGPU/WebCodecs e RTX 4060 Laptop GPU.

Critérios mínimos:

- abrir app web ou rodar local;
- importar MP4 pequeno;
- cortar/trimar;
- adicionar texto ou legenda;
- exportar MP4;
- validar com `ffprobe`;
- registrar desempenho e limitações.

### 2. Voicebox instalado via MSI

Objetivo: validar geração de fala local, API/MCP e integração com workflows de vídeo.

### 3. TTS/clonagem local aproveitando GPU dedicada

Com a RTX 4060 Laptop GPU 8 GB, vale reavaliar ferramentas que antes seriam pesadas demais, especialmente GPT-SoVITS, Fish Speech e Voicebox com backends acelerados.

## Critérios de qualidade

Um workflow só deve ser marcado como “recomendado” se tiver:

- licença clara ou política de uso segura;
- instalação reproduzível;
- documentação mínima em português;
- custos e dependências explícitos;
- riscos éticos/privacidade documentados;
- exemplo ou teste real.
