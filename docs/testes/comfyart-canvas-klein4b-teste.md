# Teste: ComfyArt (canvas de design no ComfyUI) numa placa de 8 GB

Data: 2026-11-18 e 2026-11-19
Status: **aprovado para imagem com o FLUX.2 klein 4B plugado como workflow próprio; fluxos padrão de edição e multi-ângulo exigem ComfyUI mais novo**

## Objetivo

O [ComfyArt](https://github.com/jtydhr88/ComfyArt) foi premiado no desafio *Open Source Higgsfield* da Comfy (novembro de 2026) e apareceu em vídeos como alternativa local a estúdios pagos. A pergunta do teste: ele roda numa placa de 8 GB e serve para gerar folhas de personagem (frente, ¾, perfil, costas) sem créditos de nuvem?

## O que é

Um custom node que abre um canvas de design (tldraw + React) em `http://127.0.0.1:8188/comfyart/`, servido pelo próprio ComfyUI:

- canvas com páginas, pranchetas, camadas, texto e vetores; exporta PNG, JPG, PDF e PPTX editável;
- geração de imagem, vídeo, áudio e 3D, sempre por workflows do ComfyUI;
- ferramentas de imagem: edição rápida, ângulo de câmera, recorte de fundo, upscale, inpaint, expansão, separação em camadas, "Edit Elements" (OCR que transforma um pôster pronto em camadas editáveis);
- um **servidor MCP** que deixa um agente (Claude Code, Codex, Gemini CLI, Cursor) operar o canvas;
- um "Agent" próprio que chama esses CLIs.

## Ambiente

- Windows 11 · RTX 4060 Laptop **8 GB VRAM** · 32 GB RAM
- ComfyUI 0.34.0 (Comfy Desktop), Python 3.13
- ComfyArt commit `2a990a7` (v1.3.0, MIT)

## Instalação

```bash
cd <ComfyUI>/custom_nodes
git clone --depth 1 https://github.com/jtydhr88/ComfyArt
# no Python do PRÓPRIO ComfyUI
uv pip install -r ComfyArt/requirements.txt --python <ComfyUI>/.venv/Scripts/python.exe
```

Reiniciar o ComfyUI. `dist/` já vem compilado, então não precisa de Node.

Antes de instalar, simulamos as dependências (`uv pip install --dry-run`): entram 6 pacotes novos (`pypdfium2`, `rapidocr`, `shapely`, `pyclipper`, `omegaconf`, `colorlog`) e **nenhum pacote existente muda de versão**. No código, as únicas chamadas externas vão para `huggingface.co` e `cloud.comfy.org`; processos só são abertos pelo "Agent", que deixamos desligado.

## Limite encontrado

O levantamento dos 32 workflows que vêm com o ComfyArt mostrou que, sem baixar nada, só 3 rodam (recorte de fundo e os dois de MiniMax H3, que não cabem em 8 GB). Os fluxos padrão de **edição, multi-ângulo e expansão** usam o Qwen Image 2.1, cujos nós (`QwenImage21Cache`, `TextEncodeQwenImage21`) **não existem no ComfyUI 0.34**. Usá-los exige atualizar o ComfyUI. O FLUX.2 klein 4B também não está entre os modelos padrão (só o 9B em NVFP4, formato sem aceleração em placas Ada).

## Solução: plugar o klein 4B como workflow próprio

O ComfyArt deixa trocar quase toda função por um workflow seu, em formato API, marcando os nós pelo título (`@image`, `@prompt`, `@width`/`@height`, `@save`…). Montamos três workflows do klein 4B destilado (4 passos, CFG 1, negativo zerado):

| Função do ComfyArt | Workflow | Detalhe |
| --- | --- | --- |
| Gerar imagem | `klein4b_gerar` | `@prompt` + `@width`/`@height` (nós Int ligados ao latente e ao scheduler) |
| Edição rápida | `klein4b_edit` | imagem como `ReferenceLatent` + instrução |
| Multi-ângulo | `klein4b_angulos` | o ComfyArt manda uma descrição de câmera com `<qma>`; o workflow remove a marca e antepõe "Show the exact same person from image 1… photographed from a new camera position:" |

Instalação pelo MCP do próprio ComfyArt: ferramenta `custom_workflow`, primeiro `check` (valida as marcas) e depois `install` (salva e passa a usar). Os três passaram na validação e o klein 4B virou um modelo do gerador.

Para usar o MCP: ligar **Enable MCP** em Agent Settings. O endpoint é `http://127.0.0.1:8188/comfyart/mcp?project=<id>`, e as ferramentas do canvas só rodam com a aba daquele projeto aberta.

## Resultados (RTX 4060, 8 GB)

| Ação | Tempo | Resultado |
| --- | --- | --- |
| Gerar personagem (klein 4B) | 26 s | Marceneiro idoso em estilo de animação 3D, boa qualidade |
| `change_angle` 45°, 90°, 180° + `edit_image` (expressão) | 84 s os quatro | Giro consistente: boné, óculos, barba, avental (alças cruzadas nas costas) e botas iguais nas quatro vistas; expressão "rindo" correta |
| `remove_background` (BiRefNet) | 10 s | Borda limpa, inclusive em cabelo cacheado |
| `upscale_image` 2x (4x-UltraSharp) | 21 s | OK |
| Gerar personagem (Z-Image Turbo, modelo padrão do ComfyArt) | 37 s (60 s na 1ª) | Mesmo prompt sai mais cartunesco (cabeça e olhos grandes); segue bem os detalhes do figurino |

Observações:

- O ComfyArt lista só modelos que já existem no ComfyUI e **lê essa lista quando a página carrega**: depois de baixar um modelo, recarregue a página.
- O Z-Image Turbo (12,3 GB) teve o download derrubado várias vezes pelo servidor; `curl -C -` em laço retomou até completar.
- Klein 4B para proporção realista, edição e ângulos; Z-Image para visual fofo ou de mascote.

## Veredito

- **Usar** como canvas local para thumbnails, posts e **folhas de personagem**, sem créditos de nuvem, plugando o klein 4B.
- As vistas geradas aqui podem alimentar um `.char` do [ComfyUI-Omnichar](comfyui-omnichar-personagem-consistente.md).
- **A testar:** atualizar o ComfyUI e comparar o multi-ângulo do Qwen Image 2.1; "Edit Elements" em pôsteres reais; exportação PPTX; o Agent com Claude Code.

## Arquivos de exemplo

[`examples/comfyart/`](../../examples/comfyart/): o gerador dos três workflows do klein 4B, os workflows prontos e um cliente mínimo do MCP do ComfyArt.
