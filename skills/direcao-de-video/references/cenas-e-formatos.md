# Cenas e formatos

## Estrutura por duração

| Duração | Estrutura |
|---|---|
| 6–8s loop | 1 ideia, 1 herói, emenda invisível (o movimento final atravessa o frame 0) |
| 15s | Gancho 2,5s → 2 cenas de produto (4s) → assinatura 2,5s |
| 18–20s | Gancho 3s → 3–4 cenas de 3–3,5s → assinatura 2s |
| 30s | Gancho 3s → problema 4s → 4 cenas de 4s → prova/número 4s → assinatura 3s |
| 60s | Versão de 30s + depoimento ou dado de impacto + bloco para empresas |

Lançamento centrado numa ação: frase de abertura de no máximo 8 palavras; a demonstração carrega a explicação.

## Cenas reutilizáveis

- **Gancho tipográfico:** 3–5 palavras, display bold, revelação com máscara (`yPercent: 110 → 0`), uma palavra no acento.
- **Celular:** moldura entra com leve rotação (`y: 120, rotate: -6 → 0`), legenda no topo, telas reais trocando por corte.
- **Toque em botão:** evento completo (aproximação, toque 1 → 0.92 → 1, resposta, resultado, hold).
- **Digitação:** caractere a caractere (~0,035s/caractere); confirmação no acento.
- **Número-herói:** número enorme em rolagem até o marco, rótulo curto, fonte do dado pequena.
- **Gráfico:** barras/linha crescendo do eixo; rótulo só no valor final.
- **Legenda karaokê:** palavra atual destacada no tempo exato da fala.
- **Assinatura:** logo, frase de 2 linhas, URL em pílula, CTA curto.

Cenas próprias de cada marca ficam no kit (`marcas/`). Guarde entradas e textos aprovados como componentes (ou
blocos do registry) para a próxima peça.

## Layout

- Construa no formato principal e **derive** os outros pela timeline. Nunca recorte o master.
- 9:16: texto entre 12% e 80% da altura (topo e rodapé ficam sob a interface do Reels/Stories). Margem ~60–64 px em 1080.
- Mínimos em 1080 de largura: título ≥ 78 px, apoio ≥ 39 px.
- Frame 0 é a thumbnail do autoplay mudo: nunca preto ou vazio.
- **Teste com o texto mais longo** possível. Se o título quebra em 3 linhas, encurte, alargue a caixa ou mude de shot.

## B-roll sobre vídeo gravado

Depoimentos, falas da diretoria, aulas: o vídeo gravado é a base; as animações entram sincronizadas com a fala.
Workflow HyperFrames: `talking-head-recut` (ou `embedded-captions` só para legendas).

1. Transcrição com tempos por palavra (`npx hyperframes transcribe`).
2. Análise: enquadramento, onde está a pessoa, onde há espaço vazio.
3. **Plano de clipes para aprovação:** para cada frase importante, cutaway em tela cheia (2–4s), painel no espaço
   vazio, ou nada. Não anime toda frase.
4. Cada clipe começa na palavra que o motiva e sai antes da próxima ideia.
5. Nunca cobrir rosto ou boca. Cortes de silêncio/erro só com lista revisada por uma pessoa.
