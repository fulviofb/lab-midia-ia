# Estratégia: lab-midia-ia + site Concafras IA + formação prática

Este documento organiza como transformar o `lab-midia-ia` em uma base prática para auxiliar pessoas que pedem ajuda com IA, vídeo, áudio, imagem e comunicação espírita — especialmente no contexto da aula da Concafras sobre uso de IA na Casa Espírita.

Site atual: <https://concafras-ia.vercel.app/>

Repo público: <https://github.com/fulviofb/lab-midia-ia>

Tudo neste projeto é gratuito. Ver `principio-da-gratuidade.md`.

## Diagnóstico do site atual

O site `concafras-ia.vercel.app` já funciona bem como uma vitrine bonita e inspiradora. Ele tem:

- proposta clara: IA na Comunicação Espírita;
- curadoria de ferramentas de imagem;
- curadoria de ferramentas de vídeo;
- fluxo criativo;
- assistentes IA/GPTs/Gems;
- estudos/insights;
- estilos visuais;
- glossário visual;
- prompts de imagem e vídeo;
- seção de novidades.

Pela estrutura local encontrada, o site é um app:

- React;
- Vite;
- Tailwind;
- componentes em `src/sections/`;
- conteúdo hoje majoritariamente hardcoded dentro dos componentes.

## Problema principal

O site é ótimo para apresentação, mas tende a desatualizar porque o conteúdo fica manualmente espalhado em componentes React.

O `lab-midia-ia`, por outro lado, está virando a base viva:

- catálogo estruturado;
- relatórios de teste;
- workflows;
- prompts;
- trilhas;
- issues de próximos testes;
- metadados atualizáveis via script.

Portanto, o melhor caminho é separar funções:

```txt
site Concafras IA = porta de entrada bonita, simples e pastoral/educativa
lab-midia-ia      = base técnica viva, versionada e atualizável
```

O site não deve tentar conter tudo. Ele deve orientar e encaminhar.

## Público-alvo em níveis

### Nível 0 — Leigo absoluto

Pessoa que quer resultado e não quer aprender terminal/GitHub.

Precisa de:

- trilhas simples;
- linguagem sem jargão;
- ferramentas web primeiro;
- exemplos prontos;
- checklist;
- prompt copiável.

### Nível 1 — Usuário curioso

Já usa ChatGPT, Canva, CapCut, Gemini, Claude ou ferramentas similares.

Precisa de:

- prompts melhores;
- roteiro → cena → imagem/vídeo → narração → legenda;
- comparação de ferramentas;
- guias com decisões simples;
- uso de LLM como assistente, sem CLI.

### Nível 2 — Técnico leve

Consegue instalar programas com passo a passo.

Pode usar:

- OpenReel/OpenCut;
- FFmpeg guiado;
- Remotion/HyperFrames com ajuda;
- video-use;
- workflows locais.

### Nível 3 — Avançado/equipe

Quer pipeline, automação ou treinamento de equipe.

Pode usar:

- agentes com CLI;
- GitHub;
- scripts;
- automação de catálogo;
- workflows próprios para instituição/projeto.

## Escada de autonomia recomendada

```txt
1. Site público simples
2. Trilhas guiadas
3. Prompt mestre para usar com LLM
4. Repositório técnico público
5. Oficinas práticas gratuitas
6. Formação de multiplicadores nas casas e regiões
```

Não começar por LLM + CLI para todos. Isso deve ser camada avançada, não porta de entrada.

## Papel do site Concafras IA

O site deve responder rapidamente:

1. O que posso fazer com IA na comunicação espírita?
2. Qual caminho devo seguir conforme meu objetivo?
3. Que cuidados éticos devo ter?
4. Que ferramenta usar primeiro?
5. Onde encontro um passo a passo?
6. Como pedir ajuda a uma LLM?
7. Como tirar dúvidas ou sugerir melhorias?

## Novo conteúdo recomendado para o site

### 1. Seção “Comece por aqui”

Cards por objetivo:

- Quero criar meu primeiro vídeo com IA.
- Quero transformar aula/palestra em cortes.
- Quero criar narração com IA.
- Quero fazer imagem/post/carrossel.
- Quero editar vídeo sem ser técnico.
- Sou dev e quero automatizar vídeo.

Cada card aponta para uma trilha no repo.

### 2. Seção “Trilhas práticas”

Puxar/espelhar os arquivos de `docs/trilhas/`.

### 3. Seção “Use com uma LLM”

Explicar que a pessoa pode copiar o prompt mestre e usar no ChatGPT/Claude/Gemini.

### 4. Seção “Ferramentas testadas”

Resumo filtrado do `catalog.yml`:

- recomendadas;
- em teste;
- para estudo;
- exigem API paga;
- exigem instalação/GPU.

### 5. Seção “Cuidados éticos”

Consentimento, imagem de terceiros, voz, direitos autorais, divulgação responsável, transparência.

### 6. Seção “Quer ajuda?”

Tudo gratuito, com caminhos claros:

- material de estudo (trilhas, guias, prompts);
- canal de dúvidas (formulário de diagnóstico);
- oficinas práticas e formação de multiplicadores.

## Estratégia técnica de integração

### Curto prazo — manual controlado

Manter site estático, mas adicionar links para:

- README do repo;
- trilhas;
- prompt mestre;
- catálogo;
- formulário de diagnóstico.

Vantagem: rápido, baixo risco, funciona já.

### Médio prazo — conteúdo estruturado local

Mover dados hardcoded do site para arquivos como:

```txt
src/content/tools.ts
src/content/trilhas.ts
src/content/prompts.ts
src/content/links.ts
```

Assim o conteúdo fica mais fácil de manter.

### Médio/longo prazo — sincronização com GitHub

Criar script no site ou no repo para gerar JSON público a partir do `catalog.yml`:

```txt
public/data/catalog.public.json
public/data/trilhas.public.json
```

O site consome esses JSONs em build-time ou runtime.

### Longo prazo — CMS leve

Se o volume crescer, avaliar:

- Markdown/MDX local;
- Decap CMS;
- Notion como fonte;
- GitHub Issues/Discussions como entrada;
- formulário de diagnóstico com respostas em planilha.

## Princípio da gratuidade

Todo o conteúdo deste projeto — site Concafras IA, este repositório, trilhas, prompts, oficinas e orientações ligadas ao movimento espírita — é gratuito e assim permanecerá.

Nenhuma oferta paga deve ser divulgada, sugerida ou vinculada a este espaço. Regra completa e checklist em `principio-da-gratuidade.md`.

## Próximos passos práticos

1. Criar trilhas iniciais no `lab-midia-ia`.
2. Criar prompt mestre para uso com LLM sem CLI.
3. Criar documento “Como usar este repo pelo site”.
4. Atualizar site com seção “Comece por aqui”.
5. Criar formulário de diagnóstico.
6. Automatizar export público do catálogo para JSON.
7. Testar com 3 pessoas reais antes de sofisticar a plataforma.

## Veredito

O site deve ser a porta simples e bonita. O GitHub deve ser a base viva. A LLM deve ser uma ponte opcional — primeiro via prompt copiável, depois via CLI apenas para usuários avançados.
