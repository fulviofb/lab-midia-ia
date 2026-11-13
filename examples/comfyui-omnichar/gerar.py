"""Gera imagens com FLUX.2 klein 4B (destilado) a partir de um .char do Omnichar.
Uso: python gerar.py jobs.json   (lista de {char, prompt, seed, w, h, prefix, refs:true|false, style})
refs=false -> mesma descrição, sem imagens de referência (linha de base p/ comparar).
char=null  -> texto puro (sem personagem), p/ criar referências novas."""
import json, sys, time, urllib.request
URL = 'http://127.0.0.1:8188'

def build(j):
    w, h = j.get('w', 832), j.get('h', 1216)
    p = {
        "unet": {"class_type": "UNETLoader", "inputs": {"unet_name": "flux-2-klein-4b-fp8.safetensors", "weight_dtype": "default"}},
        "clip": {"class_type": "CLIPLoader", "inputs": {"clip_name": "qwen_3_4b.safetensors", "type": "flux2", "device": "default"}},
        "vae": {"class_type": "VAELoader", "inputs": {"vae_name": "flux2-vae.safetensors"}},
        "lat": {"class_type": "EmptyFlux2LatentImage", "inputs": {"width": w, "height": h, "batch_size": 1}},
        "sch": {"class_type": "Flux2Scheduler", "inputs": {"steps": j.get('steps', 4), "width": w, "height": h}},
        "smp": {"class_type": "KSamplerSelect", "inputs": {"sampler_name": "euler"}},
        "noi": {"class_type": "RandomNoise", "inputs": {"noise_seed": j.get('seed', 1)}},
        "dec": {"class_type": "VAEDecode", "inputs": {"samples": ["run", 0], "vae": ["vae", 0]}},
        "out": {"class_type": "SaveImage", "inputs": {"images": ["dec", 0], "filename_prefix": j['prefix']}},
    }
    if j.get('char'):
        p["load"] = {"class_type": "OmnicharLoadCharacter", "inputs": {"char": j['char']}}
        p["deco"] = {"class_type": "OmnicharDecodeCharacter", "inputs": {
            "char": ["load", 0], "clip": ["clip", 0], "prompt": j['prompt'],
            "style": j.get('style', 'ordinal' if j.get('refs', True) else 'description-only'),
            "arch": "flux2-klein"}}
        pos = ["deco", 0]
        if j.get('refs', True):
            p["rl"] = {"class_type": "OmnicharCharacterReferenceLatent", "inputs": {"conditioning": ["deco", 0], "refs": ["deco", 2], "vae": ["vae", 0]}}
            pos = ["rl", 0]
        p["sheet"] = {"class_type": "PreviewAny", "inputs": {"source": ["deco", 4]}}
    else:
        p["txt"] = {"class_type": "CLIPTextEncode", "inputs": {"text": j['prompt'], "clip": ["clip", 0]}}
        pos = ["txt", 0]
    # edit_images: imagens de entrada usadas como referência direta (edição klein, sem .char)
    for k, name in enumerate(j.get('edit_images', [])):
        p[f"li{k}"] = {"class_type": "LoadImage", "inputs": {"image": name}}
        p[f"sc{k}"] = {"class_type": "ImageScaleToTotalPixels", "inputs": {"image": [f"li{k}", 0], "upscale_method": "lanczos", "megapixels": 1.0, "resolution_steps": 16}}
        p[f"ve{k}"] = {"class_type": "VAEEncode", "inputs": {"pixels": [f"sc{k}", 0], "vae": ["vae", 0]}}
        p[f"rl{k}"] = {"class_type": "ReferenceLatent", "inputs": {"conditioning": pos, "latent": [f"ve{k}", 0]}}
        pos = [f"rl{k}", 0]
    p["neg"] = {"class_type": "ConditioningZeroOut", "inputs": {"conditioning": pos}}
    p["gd"] = {"class_type": "CFGGuider", "inputs": {"model": ["unet", 0], "positive": pos, "negative": ["neg", 0], "cfg": 1}}
    p["run"] = {"class_type": "SamplerCustomAdvanced", "inputs": {"noise": ["noi", 0], "guider": ["gd", 0], "sampler": ["smp", 0], "sigmas": ["sch", 0], "latent_image": ["lat", 0]}}
    return p

def submit(prompt, wait=7200):
    req = urllib.request.Request(URL + '/prompt', data=json.dumps({'prompt': prompt}).encode(), headers={'Content-Type': 'application/json'})
    try:
        pid = json.load(urllib.request.urlopen(req))['prompt_id']
    except urllib.error.HTTPError as e:
        print(e.read().decode()[:3000]); return None
    t = time.time()
    while time.time() - t < wait:
        h = json.load(urllib.request.urlopen(URL + '/history/' + pid))
        if pid in h:
            st = h[pid]['status']
            for m in st.get('messages', []):
                if m[0] == 'execution_error': print(json.dumps(m[1])[:2000])
            files = [i['filename'] for o in h[pid]['outputs'].values() for i in o.get('images', [])]
            txt = [x for o in h[pid]['outputs'].values() for x in o.get('text', [])]
            return st['status_str'], round(time.time() - t), files, txt
        time.sleep(2)

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    for j in json.load(open(sys.argv[1], encoding='utf-8')):
        r = submit(build(j))
        print(j['prefix'], r[:3] if r else r)
        if r and r[3] and j.get('show_prompt'): print('   PROMPT:', r[3][0][:600])
