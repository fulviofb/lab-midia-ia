# Exemplo: personagem consistente com ComfyUI-Omnichar

Scripts do teste [`docs/testes/comfyui-omnichar-personagem-consistente.md`](../../docs/testes/comfyui-omnichar-personagem-consistente.md).

Pré-requisitos: ComfyUI rodando em `http://127.0.0.1:8188`, nó ComfyUI-Omnichar instalado e os três arquivos do FLUX.2 klein 4B (`flux-2-klein-4b-fp8`, `qwen_3_4b`, `flux2-vae`). Rode com o Python do próprio ComfyUI.

## Arquivos

- `gerar.py`: monta o workflow em formato de API e envia ao ComfyUI. Cada job aceita:
  - `char`: nome do `.char` em `models/characters/`, ou `null` para texto puro;
  - `refs`: `false` gera a linha de base (só a descrição, sem as imagens);
  - `edit_images`: imagens da pasta `input/` usadas como referência direta (edição);
  - `prompt`, `seed`, `w`, `h`, `steps`, `prefix`, `show_prompt`.
- `jobs_vistas_do_rosto.json`: a partir de uma foto-âncora (`exemplo_clara_face.png` em `input/`), gera ¾, perfil e corpo inteiro.
- `encode_character.json`: workflow de API que junta as 4 imagens no `clara2.char` (copie antes as saídas para `input/` com os nomes indicados).
- `jobs_cenas.json`: 3 cenas com o `.char` e uma linha de base sem referências.

## Ordem

```bash
python gerar.py jobs_vistas_do_rosto.json
# copiar as saídas para input/ como exemplo_clara2_tq.png, exemplo_clara2_perfil.png, exemplo_clara2_corpo.png
python -c "import json,gerar; print(gerar.submit(json.load(open('encode_character.json'))))"
python gerar.py jobs_cenas.json
```
