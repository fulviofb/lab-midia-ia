# Trilha 02 — Transformar aula, palestra ou reunião em cortes curtos

## Para quem é

Para educadores, palestrantes, dirigentes, comunicadores e equipes que já têm vídeos longos e querem gerar cortes para redes sociais.

## Resultado esperado

De 3 a 5 cortes curtos com:

- trecho relevante;
- início forte;
- legenda;
- título ou gancho;
- formato vertical quando necessário;
- exportação validada.

## Nível técnico

Iniciante/intermediário.

Use ferramentas visuais se não for técnico. Use `video-use`/FFmpeg se quiser automação.

## Fluxo simples

```txt
vídeo longo → transcrição → seleção dos trechos → corte → legenda → revisão → publicação
```

## Passo a passo

### 1. Escolha o vídeo

Prefira vídeos com:

- áudio claro;
- fala contínua;
- mensagens curtas e destacáveis;
- autorização de uso.

### 2. Transcreva

Opções:

- CapCut/Canva/YouTube para iniciantes;
- Whisper/local para privacidade;
- ElevenLabs Scribe se houver API key com permissão;
- `video-use` para fluxo técnico.

### 3. Peça à LLM para encontrar cortes

Use:

```txt
Vou colar a transcrição de uma aula/palestra.
Identifique 5 trechos bons para cortes curtos.
Para cada trecho, diga:
- título curto;
- início e fim aproximados;
- por que o trecho funciona;
- gancho de abertura;
- texto de legenda/título na tela.
Priorize trechos claros, úteis e respeitosos.
```

### 4. Corte o vídeo

Ferramentas:

- visual/manual: CapCut, OpenReel, OpenCut;
- técnico/automático: FFmpeg, video-use;
- acabamento: Canva ou editor que a pessoa já domina.

### 5. Legende

Boas práticas:

- frases curtas;
- contraste alto;
- não cobrir o rosto;
- revisar palavras doutrinárias e nomes próprios;
- evitar excesso de emojis/efeitos.

### 6. Publique com contexto

Para conteúdo espírita, evite cortes que removam contexto essencial ou gerem interpretação distorcida.

## Checklist final

- [ ] O trecho não distorce a mensagem original?
- [ ] Há autorização para uso da imagem/voz?
- [ ] A legenda está correta?
- [ ] O início prende atenção sem sensacionalismo?
- [ ] A duração é adequada para a plataforma?
- [ ] O arquivo foi testado antes de publicar?

## Para usuários técnicos

Consulte:

- `docs/testes/video-use-primeiro-teste.md`
- `docs/workarounds/video-use-subtitles-windows.md`
- `workflows/video-use-edicao-com-agente.md`

## Próximo passo

Depois de validar manualmente 2 ou 3 cortes, pense em automatizar partes do fluxo com `video-use`, scripts e templates.
