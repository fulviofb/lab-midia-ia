"""Gera os workflows FLUX.2 klein 4B (destilado) no formato que o ComfyArt aceita.
Saída: klein4b_edit.api.json (Quick edit) e klein4b_angulos.api.json (Multi-angle)."""
import json
from pathlib import Path

AQUI = Path(__file__).parent


def base(texto_no):
    """Grafo comum: 1 imagem de referência, 4 passos, CFG 1, negativo zerado."""
    return {
        "unet": {"class_type": "UNETLoader", "inputs": {"unet_name": "flux-2-klein-4b-fp8.safetensors", "weight_dtype": "default"}, "_meta": {"title": "@unet"}},
        "clip": {"class_type": "CLIPLoader", "inputs": {"clip_name": "qwen_3_4b.safetensors", "type": "flux2", "device": "default"}},
        "vae": {"class_type": "VAELoader", "inputs": {"vae_name": "flux2-vae.safetensors"}},
        "img": {"class_type": "LoadImage", "inputs": {"image": "example.png"}, "_meta": {"title": "@image"}},
        "esc": {"class_type": "ImageScaleToTotalPixels", "inputs": {"image": ["img", 0], "upscale_method": "lanczos", "megapixels": 1.0, "resolution_steps": 16}},
        "tam": {"class_type": "GetImageSize", "inputs": {"image": ["esc", 0]}},
        "enc": {"class_type": "VAEEncode", "inputs": {"pixels": ["esc", 0], "vae": ["vae", 0]}},
        "pos": {"class_type": "CLIPTextEncode", "inputs": {"text": texto_no, "clip": ["clip", 0]}},
        "ref": {"class_type": "ReferenceLatent", "inputs": {"conditioning": ["pos", 0], "latent": ["enc", 0]}},
        "neg": {"class_type": "ConditioningZeroOut", "inputs": {"conditioning": ["ref", 0]}},
        "gui": {"class_type": "CFGGuider", "inputs": {"model": ["unet", 0], "positive": ["ref", 0], "negative": ["neg", 0], "cfg": 1}},
        "smp": {"class_type": "KSamplerSelect", "inputs": {"sampler_name": "euler"}},
        "sch": {"class_type": "Flux2Scheduler", "inputs": {"steps": 4, "width": ["tam", 0], "height": ["tam", 1]}},
        "lat": {"class_type": "EmptyFlux2LatentImage", "inputs": {"width": ["tam", 0], "height": ["tam", 1], "batch_size": 1}},
        "noi": {"class_type": "RandomNoise", "inputs": {"noise_seed": 1}},
        "run": {"class_type": "SamplerCustomAdvanced", "inputs": {"noise": ["noi", 0], "guider": ["gui", 0], "sampler": ["smp", 0], "sigmas": ["sch", 0], "latent_image": ["lat", 0]}},
        "dec": {"class_type": "VAEDecode", "inputs": {"samples": ["run", 0], "vae": ["vae", 0]}},
        "out": {"class_type": "SaveImage", "inputs": {"images": ["dec", 0], "filename_prefix": "comfyart/klein4b"}, "_meta": {"title": "@save"}},
    }


edit = base("")
edit["pos"]["_meta"] = {"title": "@prompt"}

angulos = base(["txt", 0])
angulos.update({
    "cam": {"class_type": "PrimitiveStringMultiline", "inputs": {"value": ""}, "_meta": {"title": "@prompt"}},
    "lim": {"class_type": "StringReplace", "inputs": {"string": ["cam", 0], "find": "<qma>", "replace": ""}},
    "txt": {"class_type": "StringConcatenate", "inputs": {
        "string_a": "Show the exact same person from image 1, with the same face, hair, skin, clothing and accessories, "
                    "same lighting and plain background, photographed from a new camera position:",
        "string_b": ["lim", 0], "delimiter": " "}},
})

gerar = base("")
gerar["pos"]["_meta"] = {"title": "@prompt"}
for k in ("img", "esc", "tam", "enc", "ref"):
    del gerar[k]
gerar["neg"]["inputs"]["conditioning"] = ["pos", 0]
gerar["gui"]["inputs"]["positive"] = ["pos", 0]
gerar["lar"] = {"class_type": "PrimitiveInt", "inputs": {"value": 1024}, "_meta": {"title": "@width"}}
gerar["alt"] = {"class_type": "PrimitiveInt", "inputs": {"value": 1024}, "_meta": {"title": "@height"}}
for k in ("sch", "lat"):
    gerar[k]["inputs"]["width"] = ["lar", 0]
    gerar[k]["inputs"]["height"] = ["alt", 0]

(AQUI / "klein4b_gerar.api.json").write_text(json.dumps(gerar, indent=1), encoding="utf-8")
(AQUI / "klein4b_edit.api.json").write_text(json.dumps(edit, indent=1), encoding="utf-8")
(AQUI / "klein4b_angulos.api.json").write_text(json.dumps(angulos, indent=1), encoding="utf-8")
print("ok")
