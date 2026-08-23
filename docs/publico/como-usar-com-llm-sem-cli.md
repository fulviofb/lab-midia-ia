# Como usar este repositório com uma LLM, sem CLI

Este guia é para quem quer ajuda prática, mas não quer instalar programas, usar terminal ou entender GitHub profundamente.

Você pode usar uma LLM como ChatGPT, Claude ou Gemini como “guia de estudo” deste repositório.

## Caminho simples

1. Abra sua LLM preferida.
2. Copie o prompt mestre:
   - `prompts/prompt-mestre-consultor-midia-ia.md`
3. Preencha sua situação.
4. Peça um passo a passo.
5. Se ficar complexo demais, diga: “simplifique para uma pessoa leiga”.

## O que dizer para a LLM

Informe:

- o que você quer criar;
- para quem;
- seu nível técnico;
- ferramentas que já usa;
- se tem orçamento;
- se há uso de voz/imagem de pessoas;
- onde o conteúdo será publicado.

Se for um vídeo narrativo ou generativo, diga também quais decisões você quer tomar pessoalmente — por exemplo estética, duração, intensidade, representação de pessoas/personagens, voz e música.

## Exemplo

```txt
Quero criar um vídeo curto para convidar jovens para uma atividade da casa espírita.
Meu nível técnico é leigo.
Uso Canva e ChatGPT.
Não quero instalar nada.
Orçamento: gratuito.
Use como referência o repositório https://github.com/fulviofb/lab-midia-ia.
Me dê um passo a passo simples e ético.
```

## Se a LLM não conseguir acessar links

Copie e cole um destes arquivos junto com seu pedido:

- `docs/trilhas/01-primeiro-video-com-ia.md`
- `docs/trilhas/02-transformar-aula-em-cortes.md`
- `docs/trilhas/03-video-explicativo-narrado.md`
- `docs/trilhas/04-narracao-e-voz-com-ia.md`
- `docs/trilhas/05-video-programatico-para-devs.md`

## Como pedir simplificação

Use:

```txt
Essa resposta ficou técnica demais.
Reescreva para uma pessoa leiga, com apenas 5 passos, usando ferramentas web e sem terminal.
```

## Como pedir aprofundamento

Use:

```txt
Agora me dê uma versão mais técnica usando ferramentas reproduzíveis e, se fizer sentido, scripts ou workflows do repositório.
```

## Cuidados

A LLM pode inventar comandos, preços, recursos ou links. Sempre confira:

- se a ferramenta ainda existe;
- se há custo;
- se precisa de API key;
- se pode usar imagem/voz de terceiros;
- se a ferramenta é adequada para o público.

Para vídeo generativo, confira também se a LLM:

- separou beat, keyframe, plano, segmento e cena;
- pediu aprovação antes de escolher direção criativa;
- definiu teto de tentativas/créditos antes de gerar;
- tratou upload, geração e publicação como autorizações diferentes.

## Melhor uso

Use a LLM como orientadora, não como autoridade final.

O processo ideal é:

```txt
sua necessidade → prompt mestre → trilha recomendada → execução simples → revisão → próximo passo
```
