# Como usar este repositório com uma LLM, sem CLI

Este guia é para quem quer ajuda prática sem instalar programas, usar terminal ou dominar GitHub.

A LLM deve funcionar como orientadora: apresentar poucas possibilidades, explicar implicações e ajudar você a escolher. Ela não deve impor um workflow nem decidir criatividade, upload, gasto ou publicação sozinha.

## Caminho simples

1. Abra sua LLM preferida.
2. Copie o [prompt mestre](../../prompts/prompt-mestre-consultor-midia-ia.md).
3. Descreva sua necessidade e o material que já possui.
4. Compare as rotas sugeridas.
5. Escolha o próximo passo; reavalie depois.

## O que informar

- o que quer criar e para quem;
- material já disponível;
- se o conteúdo precisa permanecer factual/real;
- nível técnico e ferramentas conhecidas;
- prazo, canal e orçamento;
- voz/imagem/obra de terceiros;
- o que pode ou não ser enviado para serviços externos;
- decisões que deseja tomar pessoalmente;
- se precisa de uma peça única ou versões reproduzíveis.

Você não precisa responder tudo de uma vez. Uma boa LLM faz no máximo três perguntas por resposta e só pede o que altera a decisão.

## Exemplo

```txt
Quero um vídeo curto para convidar jovens para uma atividade.
Tenho fotos autorizadas, texto e identidade visual.
Sou leigo, uso Canva e não quero instalar nada.
Orçamento gratuito; não publique nem envie as fotos sem minha aprovação.
Mostre poucas rotas, explique o que reaproveito e sugira um próximo passo.
```

A resposta pode comparar, por exemplo:

- edição direta;
- montagem híbrida;
- vídeo programático;
- complementação generativa, somente se houver lacuna real.

## Rotas não são prisões

Se uma rota não funcionar, diga:

```txt
Quero reavaliar a rota.
Explique o que continua válido, o que precisa mudar, novos riscos e o próximo gate.
```

Mudar de rota não significa necessariamente começar de novo. Fotos, roteiro, identidade, decisões e partes da montagem podem continuar úteis.

## Se a LLM não acessar links

Copie somente os arquivos públicos necessários:

- [trilhas](../trilhas/) para caminhos por objetivo;
- [receitas](../receitas/) para tarefas simples;
- [guia de rotas](../guias/06-ideia-roteiro-cenas-video.md);
- [gramática cinematográfica](../guias/07-gramatica-cinematografica-pratica.md);
- [planejamento adaptativo](../guias/08-planejamento-adaptativo-de-video.md);
- [seleção de templates](../../templates/README.md).

Os quatro últimos dependem da entrada da PR #24 no `master`.

## Como pedir simplificação

```txt
Essa resposta ficou técnica demais.
Reescreva em no máximo 5 passos, sem terminal, código ou API.
Mostre só a rota escolhida e o próximo checkpoint.
```

## Como pedir aprofundamento

```txt
Agora detalhe os módulos e ferramentas reproduzíveis adequados à rota escolhida.
Mantenha explícitos os gates de direitos, upload, gasto e publicação.
```

## Cuidados

A LLM pode inventar comandos, preços, recursos, links ou alegar ações que não executou. Confira:

- existência e estado atual da ferramenta;
- custo, créditos e API key;
- processamento local ou remoto;
- direitos e consentimentos;
- retenção/exclusão no provedor;
- adequação ao público;
- artefato real e verificação técnica.

## Checklist da resposta

- [ ] Entendeu a necessidade antes da ferramenta?
- [ ] Apresentou no máximo três rotas quando havia escolha real?
- [ ] Explicou vantagens, limites e reaproveitamento?
- [ ] A sugestão foi contextual, não universal?
- [ ] Pediu decisão nos pontos criativos?
- [ ] Separou upload, geração, gasto, download e publicação?
- [ ] Selecionou apenas módulos úteis?
- [ ] Propôs um próximo passo pequeno?
- [ ] Permitiu mudança de rota?
- [ ] Não alegou execução sem evidência?

## Melhor uso

```txt
necessidade
→ poucas rotas
→ implicações
→ escolha
→ próximo passo
→ checkpoint
→ manter ou mudar
```

Use a LLM como orientadora, não como autoridade final.
