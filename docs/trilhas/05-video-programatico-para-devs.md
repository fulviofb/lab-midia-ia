# Trilha 05 — Vídeo programático para desenvolvedores e usuários técnicos

## Para quem é

Para quem já entende um pouco de terminal, Git, Node, React ou quer usar agentes/LLMs para gerar vídeos por código.

## Resultado esperado

Um vídeo reproduzível, versionável e editável por agente.

## Quando escolher vídeo programático

Escolha este caminho quando você precisa de:

- templates reutilizáveis;
- vídeos em lote;
- dados dinâmicos;
- identidade visual consistente;
- automação;
- revisão por código;
- integração com agentes.

## Ferramentas principais

### HyperFrames

Bom para:

- HTML/CSS/GSAP;
- motion graphics;
- vídeos explicativos;
- renderização de animações web para MP4;
- fluxo agent-first.

Consulte:

- `docs/testes/hyperframes-primeiro-teste.md`
- `workflows/hyperframes-video-html.md`

### Remotion

Bom para:

- React;
- componentes reutilizáveis;
- controle frame-by-frame;
- vídeos parametrizados;
- pipelines mais estruturados.

Consulte:

- `docs/testes/remotion-agent-skills-primeiro-teste.md`
- `workflows/remotion-video-programatico.md`

### video-use

Bom para:

- edição de vídeo bruto com agente;
- cortes;
- legendas;
- EDL;
- integração com FFmpeg.

Consulte:

- `docs/testes/video-use-primeiro-teste.md`
- `workflows/video-use-edicao-com-agente.md`

## Fluxo recomendado com LLM/CLI

```txt
1. Defina objetivo e duração.
2. Escolha HyperFrames ou Remotion.
3. Peça à LLM um plano de cenas.
4. Gere a composição inicial.
5. Rode lint/validate/render.
6. Revise o MP4.
7. Itere até ficar publicável.
```

## Prompt inicial

```txt
Você é meu assistente de vídeo programático.
Objetivo do vídeo: [objetivo]
Público: [público]
Duração: [tempo]
Stack preferida: [HyperFrames/Remotion]
Estilo visual: [referência]

Crie:
1. plano de cenas;
2. estrutura de componentes;
3. roteiro/narração;
4. assets necessários;
5. checklist de renderização.
```

## Checklist final

- [ ] O projeto roda localmente?
- [ ] O vídeo renderiza MP4?
- [ ] Há comando reproduzível?
- [ ] O visual está consistente?
- [ ] O arquivo final foi validado?
- [ ] As dependências/licenças são aceitáveis?

## Próximo passo

Se a pessoa não é técnica, volte para:

- `01-primeiro-video-com-ia.md`
- `03-video-explicativo-narrado.md`
