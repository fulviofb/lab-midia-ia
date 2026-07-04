# Prompt: motion graphic com HyperFrames

```text
Usando HyperFrames, crie um motion graphic curto em HTML/CSS/GSAP.

Tema:
[TEMA]

Mensagem central:
[MENSAGEM]

Duração:
[6s / 10s / 15s]

Formato:
[16:9 horizontal / 9:16 vertical / 1:1 quadrado]

Estilo visual:
[ex.: escuro tecnológico, editorial limpo, educativo, futurista, institucional]

Elementos obrigatórios:
- título principal;
- subtítulo curto;
- 1 elemento visual animado;
- encerramento com chamada curta.

Regras técnicas:
- usar HyperFrames;
- composição em `index.html`;
- root com `data-composition-id`, `data-width`, `data-height`, `data-duration`;
- todo elemento temporizado deve ter `class="clip"`, `data-start`, `data-duration`, `data-track-index`;
- timeline GSAP deve ser pausada e registrada em `window.__timelines["<id>"]`;
- não usar `Date.now()`, `Math.random()` sem seed, nem fetch em tempo de render;
- rodar `lint`, `validate`, `inspect`, `snapshot` e `render --strict` antes de considerar concluído.

Entregáveis:
- `index.html`;
- snapshots de verificação;
- `renders/final.mp4`;
- resumo com duração, resolução, fps e comandos usados.
```
