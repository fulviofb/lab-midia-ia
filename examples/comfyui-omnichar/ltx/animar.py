"""Anima quadros-chave no LTX-2.5 local (template video_ltx2_5_i2v) via comfy-cli.
uso: python animar.py jobs.json   -> [{"id","image","prompt","dur","seed"}]
16:9, 0.5 MP, prompt enhance desligado. Coloque em base/ os templates do ComfyUI salvos como JSON: ltx25_i2v.json (video_ltx2_5_i2v) e
ltx25_flf2v.json (video_ltx2_5_flf2v). Jobs com "last" usam primeiro/último quadro."""
import json, os, shutil, subprocess, sys
from pathlib import Path
AQUI = Path(__file__).parent
COMFY = shutil.which("comfy") or "comfy"  # comfy-cli no PATH
ENV = {**os.environ, "PYTHONIOENCODING": "utf-8", "PYTHONUTF8": "1"}
REAL = (" Photorealistic live-action footage with natural motion; she keeps exactly the same face, hair, "
        "gold hoop earrings, mustard-yellow blazer and white t-shirt as in the first frame. She is the only "
        "person in focus; nobody else enters the frame. No text, no letters, no black frames.")

def run(args):
    r = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace", env=ENV, timeout=180)
    if r.returncode: raise RuntimeError(r.stdout[-800:] + r.stderr[-800:])
    return r.stdout

sys.stdout.reconfigure(encoding="utf-8")
(AQUI / "jobs").mkdir(exist_ok=True)
for j in json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")):
    wf = AQUI / "jobs" / f"{j['id']}.json"
    if j.get("last"):  # primeiro/último quadro (template video_ltx2_5_flf2v, 1 estágio)
        shutil.copy(AQUI / "base" / "ltx25_flf2v.json", wf)
        run([COMFY, "--no-json", "workflow", "set-slot", str(wf),
             f"31.image={j['image']}", f"39.image={j['last']}",
             f"251.value={j['prompt'].strip()}{REAL}", "251.value_1=false",
             f"251.value_2={int(j.get('dur', 4))}", "251.value_3=960", "251.value_4=544",
             f"251.noise_seed={int(j.get('seed', 42))}", f"68.filename_prefix=video/omni/{j['id']}"])
        print(j['id'], run([COMFY, "--no-json", "--where", "local", "run", "--workflow", str(wf)]).strip()[-150:], flush=True)
        continue
    shutil.copy(AQUI / "base" / "ltx25_i2v.json", wf)
    run([COMFY, "--no-json", "workflow", "set-slot", str(wf),
         f"395.image={j['image']}", f"398.value={j['prompt'].strip()}{REAL}", "398.value_1=false",
         f"398.value_2={int(j.get('dur', 4))}", f"398.noise_seed={int(j.get('seed', 42))}",
         "403.aspect_ratio=16:9 (Widescreen)", "403.megapixels=0.5",
         f"75.filename_prefix=video/omni/{j['id']}"])
    print(j['id'], run([COMFY, "--no-json", "--where", "local", "run", "--workflow", str(wf)]).strip()[-150:], flush=True)
