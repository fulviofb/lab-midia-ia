# Guia: Como criar narração com IA de forma ética

## Princípios

1. **Sempre peça permissão antes de clonar a voz de alguém.**
2. **Não use voz clonada para enganar, impersonar ou difamar.**
3. **Divulgue quando o áudio for gerado por IA**, especialmente em conteúdo público.
4. **Não gere conteúdo de voz para pessoas sem consentimento**, inclusive figuras públicas.
5. **Respeite os termos de serviço** de cada ferramenta.

## Ferramentas

### Voicebox (local-first)

- Repo: https://github.com/jamiepine/voicebox
- Melhor para: estúdio local completo, TTS, clonagem sem nuvem.
- Status: ainda não testado localmente (Issue #5).

### GPT-SoVITS (clonagem/TTS)

- Repo: https://github.com/RVC-Boss/GPT-SoVITS
- Melhor para: clonagem de voz técnica, TTS em múltiplos idiomas.
- Licença: MIT.
- Status: referência, ainda não testado localmente.

### Fish Speech (TTS open-source)

- Repo: https://github.com/fishaudio/fish-speech
- Melhor para: TTS de alta qualidade.
- Licença: Fish Audio Research License (verificar termos).

### ElevenLabs (API, paga)

- Site: https://elevenlabs.io
- Melhor para: qualidade rápida, timestamps precisos (Scribe), integração com agentes.
- Custo: API paga, com free tier limitado.
- Usado pelo `video-use` para transcrição.

### MisoTTS (experimental)

- Melhor para: fala expressiva em inglês.
- Licença: Modified MIT (revisar termos modificados).

## Fluxo ético recomendado

```txt
1. Definir o que será narrado (roteiro).
2. Escolher a voz:
   - voz sintética padrão (sem clonagem) → mais seguro;
   - clonagem da própria voz → OK com consentimento;
   - clonagem de terceiros → só com permissão expressa.
3. Gerar o áudio.
4. Auditar o resultado: o texto foi dito corretamente? Há erros?
5. Divulgar que o áudio foi gerado por IA, se for conteúdo público.
6. Não usar para conteúdo enganoso, político ou comercial sem disclaimers.
```

## Qualidade vs ética

- Vozes sintéticas padrão (sem clonagem) são suficientes para a maioria dos casos.
- Clonagem deve ser exceção, não regra.
- Sempre prefira a abordagem menos invasiva.

## Credenciais

- Nunca inclua API keys em arquivos commitados.
- Use `.env` não commitado ou variáveis de ambiente.
- O repositório `lab-midia-ia` nunca deve conter chaves.

## Próximos passos

- Issue #5: testar Voicebox localmente;
- Issue #9: testar ElevenLabs Scribe com video-use;
- Criar workflow de voz integrado com Remotion/HyperFrames.

## Referências

- Mapa de ferramentas: `docs/01-mapa-de-ferramentas.md`
- Ética e licenças: `docs/08-etica-licencas-privacidade.md`
