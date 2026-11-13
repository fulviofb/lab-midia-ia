# Teste: ComfyUI-Omnichar (personagem consistente com `.char`)

Data: 2026-11-13
Status: **aprovado para imagem com FLUX.2 klein 4B em 8 GB de VRAM; LoRA, voz e MiniMax H3 não testados**

## Objetivo

Verificar se o formato `.char` do [ComfyUI-Omnichar](https://github.com/omnichar/ComfyUI-Omnichar) mantém um personagem reconhecível em cenas novas, numa máquina modesta, em dois casos:

1. **Personagem ilustrado** (aquarela de livro infantil).
2. **Personagem realista** (mulher fictícia, gerada do zero pelo próprio modelo).

Em cada cena, gerar também uma **linha de base**: mesmo prompt, mesma seed, só a descrição do personagem, sem as imagens de referência. A diferença entre as duas é o que o `.char` acrescenta de fato.

## O que é o `.char`

Um arquivo que empacota um personagem:

- até 3 referências de rosto, 3 de corpo e 3 de figurino, em ordem fixa;
- uma descrição travada, que todo modelo lê;
- opcional: um LoRA treinado no Omnichar Studio e um clipe de voz de ~30 s (só o MiniMax H3 usa).

Os nós montam o prompt no endereçamento de cada modelo: FLUX.2 lê prosa ordinal ("Images 1 and 2 show…"), MiniMax H3 lê `<Picture N>`, Seedance lê `@ImageN`. Não é um modelo novo: é uma forma de organizar e reaproveitar as referências.

Nós: Load, Decode, Encode e Save Character; Character Reference, References Split e Reference Latent; Apply Character LoRA. Biblioteca Python independente: `omnichar-sdk` (CLI `inspect`, `extract`, `prompt`).

## Ambiente

- Windows 11 · RTX 4060 Laptop **8 GB VRAM** · 32 GB RAM
- ComfyUI 0.34.0 (Comfy Desktop), Python 3.13
- ComfyUI-Omnichar commit `251c02e` · `omnichar-sdk` 0.1.1
- FLUX.2 klein 4B destilado: `flux-2-klein-4b-fp8` (4,1 GB) + `qwen_3_4b` (8 GB, text encoder) + `flux2-vae` (0,3 GB)
- Amostragem: euler, 4 passos, CFG 1, negativo zerado (`ConditioningZeroOut`), como no template oficial do klein destilado

## Instalação

```bash
cd <ComfyUI>/custom_nodes
git clone https://github.com/omnichar/ComfyUI-Omnichar
# instalar no Python do PRÓPRIO ComfyUI, não no global
uv pip install -r ComfyUI-Omnichar/requirements.txt --python <ComfyUI>/.venv/Scripts/python.exe
```

Reiniciar o ComfyUI. Os `.char` ficam em `models/characters/` (a pasta é criada pelo nó Save Character).

## Resultados

### Ilustrado: funciona bem

Referências: 1 rosto e 1 corpo inteiro, recortados do model sheet sobre fundo creme.

- **Com `.char`:** cabelo, tom de pele, acessório no cabelo e figurino corretos nas 3 cenas.
- **Linha de base (sem referências, mesma seed):** sai outra criança, com cabelo mais curto, pele mais clara e o acessório transformado em outro objeto.
- **Defeito:** em cena noturna o traço puxou para desenho com contorno preto e a pele clareou. Cenas diurnas mantiveram a aquarela.

### Realista, tentativa 1: referências incoerentes

Rosto e corpo gerados **separadamente** por texto. Saíram incoerentes entre si (cabelo longo numa, curto na outra; pinta em lugares diferentes). Resultado: mesmo "tipo" de pessoa, mas o rosto mudava e envelhecia em close e perfil.

### Realista, tentativa 2: receita que funciona

1. Gerar **uma** foto de rosto e tratá-la como âncora.
2. Gerar as outras vistas **por edição a partir dela** (klein com a foto como `ReferenceLatent`): ¾, perfil e corpo inteiro com o figurino. Prompt no formato *"The same woman from image 1, same face, same hair… now in three-quarter view"*.
3. Montar o `.char` com rosto ×3 + corpo ×1, e escrever a descrição de acordo com o que as referências mostram.

Resultado nas mesmas 3 cenas e seeds (podcast, rua, janela de trem): cabelo, pinta, brincos e figurino consistentes; o perfil passou a segurar o rosto. A linha de base ainda sai "parecida", porque a descrição é detalhada, mas com outro rosto e outro cabelo. **O ganho do `.char` no realista é fidelidade de rosto, não de tipo.**

Ressalva: pedir "perfil estrito" na edição rendeu algo mais perto de ¾, o que serviu.

### Tempos (RTX 4060 8 GB, modelo já carregado)

| Referências no `.char` | Tempo por imagem |
| --- | --- |
| 2 | ~24 s |
| 4 | 60–80 s |

Criar o `.char` (Encode + Save) leva poucos segundos.

## Veredito

- **Usar** para personagem recorrente quando o destino final aceita referências (FLUX.2, MiniMax H3, Seedance).
- **Regra:** todas as referências devem sair do mesmo rosto. Referências que se contradizem não dão ao modelo um rosto único para seguir.
- **Não cobre LTX:** para vídeo local com LTX, usar o `.char` só para gerar os quadros-chave e animar depois em imagem-para-vídeo.
- **A testar:** klein 9B (mais fidelidade, mais memória), LoRA treinado no Omnichar Studio, voz com MiniMax H3 na nuvem.

## Arquivos de exemplo

[`examples/comfyui-omnichar/`](../../examples/comfyui-omnichar/): o script de geração pela API do ComfyUI e os pedidos (jobs) da tentativa 2 do realista.
