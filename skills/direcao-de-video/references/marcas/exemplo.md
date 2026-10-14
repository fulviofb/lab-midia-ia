# Kit de marca (modelo)

Um arquivo por marca, neste formato. A marca fornecida pelo usuário sempre vence estes padrões.
Os valores abaixo são de uma marca fictícia ("Trilha", app de cursos) só para mostrar o formato.

## Cores e tipografia (vídeo)

```css
--bg:       #14213D; /* fundo principal */
--accent:   #2EC4B6; /* acento com significado: conquista, CTA, elemento que costura as cenas */
--accent-ink:#1B7F76; /* acento para texto pequeno sobre branco (confira 4.5:1) */
--warm:     #FF9F1C; /* acento secundário pontual, no máximo 1x por cena */
--ink:      #F4F6FB; /* texto sobre o fundo */
--mute:     #9AA6C4; /* texto de apoio */
```

- Tipografia: display com caráter (700–800) + sans de leitura + mono para números. Se o produto já define uma
  família, use a do produto.
- O fundo domina, o acento marca o que importa.
- Tom: <como a marca fala com o público>.
- Ícones: o conjunto do produto (ex.: Lucide), nunca emojis.

## Cenas próprias da marca

- **Celular com o app:** moldura entra com leve rotação, telas reais trocando por corte.
- **Progresso do curso:** anel 0 → 100% com módulos em sequência; selo de conclusão em spring 0.5.
- **Assinatura:** logo, frase de 2 linhas, URL em pílula, CTA curto.

## Exemplo de prompt dirigido (promo 18s)

```
GOAL: quem nunca fez curso online entende em 18s que conclui o primeiro módulo pelo celular e quer baixar o app.
OUTPUT: HyperFrames, workflow product-launch-video, 1080x1920.
TIME: 18s x 30 fps = 540 frames (0–539, globais), 120 BPM (1 beat = 15 frames), sem loop.
LOOK: fundo #14213D, acento #2EC4B6, laranja #FF9F1C 1x por cena, texto #F4F6FB;
  display 800, tracking -0.02em; números em mono.
LAYOUT: margem 64; título x96 y230 largura 888, 88 px, entrelinha 1.05, máx. 2 linhas;
  celular x190 y520 largura 700; legenda x96 y330; camadas: fundo, celular, conteúdo, dedo, legenda.
MOTION: enter cubic-bezier(0.16,1,0.3,1) 18–24 frames; exit cubic-bezier(0.7,0,0.84,0) na metade;
  stagger de palavras 3 frames; cards spring 0.8; selo spring 0.5; texto nunca quica.
  Um ponto no acento costura as cenas: vira botão, barra de progresso, selo e pílula da URL.
SHOTS:
  0–89     gancho "Seu primeiro curso / cabe no bolso." (máscara, 1 palavra no acento); corte no beat.
  90–194   celular entra; login por telefone, código digitado; confirmação no acento.
  195–299  trilha de módulos aparece; dedo escolhe o primeiro.
  300–404  progresso 0→100%, selo de conclusão com pop.
  405–489  dedo até "Próximo módulo" (420–435), toque em 442, toast "Módulo 2 liberado" em 450, parado até 489.
  490–539  assinatura, frase de 2 linhas, URL, CTA "Baixe o app".
BANNED: seção 7 da skill + dados pessoais reais, ícones de stock.
FACTS: nunca invente números; valor sem fonte entra como ILUSTRATIVO.
INPUTS: prints reais das telas, trilha (se houver).
QA: mapa de batidas + 4 stills (gancho, login, conclusão, assinatura) antes de construir;
  abertura primeiro e espera aprovação; depois snapshots em 3.0, 6.5, 10.0, 14.73, 15.0, 16.33 s;
  contact sheet a cada 15 frames; corrigir; render final.
```

Com narração: troque TIME por "duração = narração + 1,5s de assinatura; eventos nos tempos das palavras transcritas"
e acrescente a legenda karaokê no LAYOUT.
