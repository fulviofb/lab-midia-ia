# Receita 02 — Transformar palestra em cortes para redes sociais

**O que você vai ter no final:** 3 vídeos curtos (30 a 90 segundos) com legenda, tirados de uma palestra ou aula gravada, prontos para Instagram, YouTube Shorts ou WhatsApp.

**Tempo estimado:** 1 a 2 horas na primeira vez; bem menos depois.

**O que você precisa:** o vídeo da palestra, o aplicativo gratuito CapCut (celular ou computador) e uma LLM gratuita (ChatGPT, Gemini ou Claude).

## Antes de começar

Peça autorização ao palestrante para publicar os cortes. É rápido, evita constrangimento e é o certo a fazer.

## Passo a passo

### 1. Gere a transcrição

No CapCut: importe o vídeo e use **Legendas automáticas**. Ele transcreve a fala inteira.

Alternativa: se o vídeo está no YouTube, abra a transcrição automática lá (botão "..." → Mostrar transcrição) e copie o texto.

### 2. Peça à LLM para encontrar os melhores trechos

Cole a transcrição com este pedido:

```txt
Esta é a transcrição de uma palestra espírita.
Encontre os 3 melhores trechos para vídeos curtos de 30 a 90 segundos.
Para cada trecho, me dê:
- um título curto que desperte interesse sem sensacionalismo;
- as primeiras e as últimas palavras do trecho (para eu localizar no vídeo);
- por que esse trecho funciona sozinho, sem perder o contexto.
Evite trechos que, isolados, possam distorcer a mensagem original.
```

### 3. Corte no CapCut

Para cada trecho: localize pelas palavras indicadas, corte o início e o fim, e exporte em formato vertical (9:16) se for para Instagram/Shorts.

### 4. Capriche na legenda

As legendas automáticas do passo 1 já acompanham o corte. Revise uma a uma:

- nomes próprios e termos espíritas costumam sair errados (ex.: "Kardec", "psicografia");
- frases curtas, letra grande, sem cobrir o rosto de quem fala.

### 5. Revise e publique

- [ ] O trecho isolado mantém o sentido original da palestra?
- [ ] O palestrante autorizou?
- [ ] A legenda está correta?
- [ ] O início prende a atenção nos primeiros 3 segundos?
- [ ] Assistiu ao vídeo exportado até o fim antes de publicar?

Ao publicar, escreva na descrição o nome do palestrante e o link da palestra completa — isso dá contexto e convida ao aprofundamento.

## Se der errado

- **A transcrição saiu muito errada:** o áudio pode estar ruim; tente um vídeo com som mais limpo ou aproxime o trecho manualmente.
- **Os trechos sugeridos não são bons:** peça — "sugira outros 3, priorizando ensinamentos práticos para o dia a dia".
- **Quer automatizar (você é técnico):** veja a trilha `docs/trilhas/02-transformar-aula-em-cortes.md` e `workflows/`.
