"""Roda um workflow API do ComfyArt direto no ComfyUI e mede o tempo.
uso: python rodar_workflow.py <nome-do-workflow> '<json de ajustes {"no.campo": valor}>'
ex.: python rodar_workflow.py cutout-birefnet '{"17.image": "foto.png", "18.filename_prefix": "comfyart_teste/recorte"}'
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

URL = "http://127.0.0.1:8188"
# pasta workflows/ do ComfyArt: defina COMFYART_WORKFLOWS=<ComfyUI>/custom_nodes/ComfyArt/workflows
WF = Path(os.environ.get("COMFYART_WORKFLOWS", "ComfyUI/custom_nodes/ComfyArt/workflows"))

sys.stdout.reconfigure(encoding="utf-8")
nome, ajustes = sys.argv[1], json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
prompt = json.loads((WF / f"{nome}.api.json").read_text(encoding="utf-8"))
for chave, valor in ajustes.items():
    no, campo = chave.rsplit(".", 1)
    prompt[no]["inputs"][campo] = valor
req = urllib.request.Request(URL + "/prompt", data=json.dumps({"prompt": prompt}).encode(),
                             headers={"Content-Type": "application/json"})
try:
    pid = json.load(urllib.request.urlopen(req))["prompt_id"]
except urllib.error.HTTPError as e:
    sys.exit(e.read().decode()[:2500])
t = time.time()
while time.time() - t < 3600:
    h = json.load(urllib.request.urlopen(f"{URL}/history/{pid}"))
    if pid in h:
        st = h[pid]["status"]
        for m in st.get("messages", []):
            if m[0] == "execution_error":
                print(json.dumps(m[1], ensure_ascii=False)[:1800])
        arquivos = [i["filename"] for o in h[pid]["outputs"].values() for i in o.get("images", [])]
        print(nome, st["status_str"], f"{time.time() - t:.0f} s", arquivos)
        break
    time.sleep(1)
