# Trilha 04 — Narração e voz com IA de forma ética

## Para quem é

Para quem precisa criar narração, melhorar áudio, testar TTS ou entender clonagem de voz com responsabilidade.

## Resultado esperado

Uma narração utilizável, com boa qualidade e sem violar consentimento, privacidade ou direitos de imagem/voz.

## Regra central

Nunca clone ou simule a voz de alguém sem autorização clara.

Em contexto espírita, o cuidado precisa ser ainda maior: a tecnologia deve servir à mensagem, não manipular emocionalmente o público.

## Caminhos possíveis

### Caminho A — Mais simples

Grave a própria voz em ambiente silencioso e use IA apenas para:

- limpar ruído;
- normalizar volume;
- remover pausas;
- melhorar clareza.

### Caminho B — TTS comum

Use uma voz sintética genérica para narrar.

Bom para:

- vídeos internos;
- rascunhos;
- protótipos;
- conteúdo educativo sem identificação pessoal.

### Caminho C — Clonagem autorizada

Use apenas quando:

- a pessoa autorizou;
- há finalidade clara;
- o público não será enganado;
- existe controle de uso.

## Ferramentas candidatas

- Voicebox — app local-first, documentado; instalação desktop pendente.
- GPT-SoVITS — técnico, few-shot, bom para teste com GPU dedicada.
- Fish Speech — TTS open-source de alta qualidade.
- ElevenLabs — bom serviço comercial, atenção a permissões e custos.

## Prompt para roteiro de narração

```txt
Crie uma narração de até [tempo] sobre [tema].
Público: [público].
Tom: fraterno, simples, respeitoso e claro.
Evite dramatização excessiva, promessas milagrosas e linguagem apelativa.
Inclua pausas naturais e frases curtas.
```

## Checklist ético

- [ ] A voz usada é minha, sintética genérica ou autorizada?
- [ ] O público saberá quando for necessário que é IA?
- [ ] O conteúdo não manipula emoções indevidamente?
- [ ] A mensagem é fiel ao propósito?
- [ ] A gravação original, se houver, está protegida?

## Próximo passo

Para aprofundar:

- `docs/guias/05-narracao-com-ia-etica.md`
- `docs/testes/voicebox-primeiro-teste.md`
- `workflows/voicebox-narracao-local.md`
