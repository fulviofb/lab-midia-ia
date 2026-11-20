# Exemplo: FLUX.2 klein 4B dentro do ComfyArt

Scripts do teste [`docs/testes/comfyart-canvas-klein4b-teste.md`](../../docs/testes/comfyart-canvas-klein4b-teste.md).

Pré-requisitos: ComfyUI em `http://127.0.0.1:8188` com o ComfyArt instalado, os arquivos do klein 4B (`flux-2-klein-4b-fp8`, `qwen_3_4b`, `flux2-vae`) e **Enable MCP** ligado em Agent Settings do ComfyArt. Rode com o Python do próprio ComfyUI.

## Arquivos

- `montar_klein4b.py`: gera os três workflows em formato API, já com os títulos que o ComfyArt procura.
  - `klein4b_gerar.api.json`: função *Text to image* (`@prompt`, `@width`, `@height`).
  - `klein4b_edit.api.json`: função *Quick edit* (`@image`, `@prompt`).
  - `klein4b_angulos.api.json`: função *Multi-angle* (`@image`, `@prompt`). Remove a marca `<qma>` que o ComfyArt manda e antepõe uma instrução de "mesma pessoa, nova posição de câmera".
- `mcp_cli.py`: cliente mínimo do MCP do ComfyArt (JSON-RPC por HTTP).
- `rodar_workflow.py`: roda um workflow que vem com o ComfyArt direto no ComfyUI e mede o tempo (defina `COMFYART_WORKFLOWS`).

## Instalar os workflows no ComfyArt

Abra um projeto no ComfyArt (o id é o `project=` da URL) e mantenha a aba aberta.

```bash
python montar_klein4b.py
python mcp_cli.py <projeto> tools
```

Para cada workflow, monte um JSON `{"action": "check", "feature": "<função>", "workflow": <conteúdo do .api.json>}` e passe com `@arquivo`; se vier `"ok": true`, repita com `"action": "install"` e um `"name"`. Funções: `generate`, `edit`, `angles`.

```bash
python mcp_cli.py <projeto> call custom_workflow @check_edit.json
python mcp_cli.py <projeto> call custom_workflow @install_edit.json
python mcp_cli.py <projeto> call list_models '{}'
```

## Usar pelo MCP

```bash
python mcp_cli.py <projeto> call generate_image '{"prompt": "...", "model": "custom:generate", "ratio": "3:4"}'
python mcp_cli.py <projeto> call change_angle '{"id": "<shape>", "horizontal": 90}'
python mcp_cli.py <projeto> call wait_generation '{"ids": ["<id>"], "timeout_s": 170}'
```
